"""Exact L034 error-budget test; hypothetical input errors, not a sign certificate."""
import json
from fractions import Fraction as F
from pathlib import Path

from check_continuum_heat_tail import inverse_exp_upper, rounded_upper


def record(x):
    return dict(numerator=str(x.numerator), denominator=str(x.denominator),
                decimal_upper=rounded_upper(x)[1]['decimal_upper'])


def main():
    path = Path(__file__).with_name('retained-error-budget-certificate.json')
    s0, s10 = F('9.95308720484'), F('5.32283164890e12')
    bounds = [c * 7**5 * s10 * s0**6 for c in (11584512, 46338048)]
    beta = 82 * inverse_exp_upper(F(80), 160)
    tails = [F('1.37381915696e-11'), F('5.49527662781e-11')]
    comparators = [F('453.073657044287'), F('3352.593155019382')]
    time_bounds = [beta*b for b in bounds]
    thresholds = [F('0.0015'), F('0.006')]
    assert all(x < t for x, t in zip(time_bounds, thresholds))
    rows = []
    for bits in (52, 64, 94, 95, 96, 112):
        e = F(1, 2**bits)
        errors = [((1+e)**10-1)*b for b in bounds]
        totals = [x+t+s for x, t, s in zip(errors, time_bounds, tails)]
        rows.append(dict(bits=bits, assumed_eta_epsilon_s_epsilon_r=record(e),
                         assumed_arithmetic_error=0,
                         perturbation_allowances=[record(x) for x in errors],
                         total_allowances=[record(x) for x in totals],
                         less_than_diagnostic_only=[x < c for x, c in zip(totals, comparators)]))
    first_bits = []
    for b, t, s, c in zip(bounds, time_bounds, tails, comparators):
        first_bits.append(next(p for p in range(1, 201)
                              if ((1+F(1, 2**p))**10-1)*b+t+s < c))
    result = dict(scope='L034 full absolute expansion budget at retained cutoff 112.',
                  method='Exact fractions and outward display rounding; all input-error budgets are hypothetical.',
                  absolute_expansion_majorants=[record(x) for x in bounds],
                  exact_window_description='tau=1/16, U=80/[3(pi/8)^2]; actual program endpoints still need validation.',
                  ideal_time_tail_bounds=[record(x) for x in time_bounds],
                  required_time_tail_bounds=[str(x) for x in thresholds],
                  time_tail_checks_passed=True,
                  spectral_tail_bounds=[str(x) for x in tails],
                  diagnostic_comparators=[str(x) for x in comparators],
                  comparator_source='continuum-tensor112-degree144-certificate.json, cutoff 112, time degree 16',
                  rows=rows, first_integer_bits_passing_hypothetical_budget=first_bits,
                  failures=[dict(test='Scalar propagation with eta=epsilon_s=epsilon_r=2^-52 and E=0',
                                 actual=[x['decimal_upper'] for x in rows[0]['total_allowances']],
                                 required=[str(x) for x in comparators],
                                 meaning='Sufficient test fails; this is not a lower bound on actual error.')],
                  actual_retained_enclosure=None, rigorous_sign_certified=False,
                  unresolved=['Certified coefficient errors', 'Certified finite-window inverse-weight errors',
                              'Arithmetic residuals, including eigenvalues and phases',
                              'Other Ward-response terms and compensation'])
    path.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(dict(actual_time_tail_bounds=[record(x)['decimal_upper'] for x in time_bounds],
                          required_time_tail_bounds=result['required_time_tail_bounds'],
                          failed_binary64_budget=result['failures'][0],
                          hypothetical_first_passing_bits=first_bits,
                          actual_retained_enclosure=None, path=str(path))))


if __name__ == '__main__':
    main()
