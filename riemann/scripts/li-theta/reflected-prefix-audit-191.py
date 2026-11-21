#!/usr/bin/env python3
"""Independent full rational validation of L971; does not alter step189."""
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import json

HERE = Path(__file__).parent
ROOT = HERE.parent.parent


def mul(a, b):
    out = [Q(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def shift(a, c):
    out = [Q(0)]
    for x in reversed(a):
        out = mul(out, [c, Q(1)])
        out[0] += x
    return out[:len(a)]


def strings(xs):
    return [str(x) for x in xs]


def main():
    original_path = HERE / 'reflected-prefix-certificate-189.json'
    replay_path = HERE / 'reflected-prefix-replay-191.json'
    original_bytes = original_path.read_bytes()
    saved = json.loads(original_bytes)
    replay = json.loads(replay_path.read_text())
    checks = {}
    checks['complete_replay_equality'] = saved == replay
    assessment = (ROOT / 'drafts/literature/2026-11-10-reflected-prefix-counterexample-audit-review-189.md').read_text()
    invocation = (ROOT / 'drafts/2026-11-10-l971-audit-working-191.md').read_text()
    target = next(s[8:] for s in assessment.splitlines() if s.startswith('TARGET: '))
    action = next(s[len('Invocation Next action: '):] for s in invocation.splitlines()
                  if s.startswith('Invocation Next action: '))
    covered = [s[16:] for s in assessment.splitlines() if s.startswith('COVERED_TARGET: ')]
    checks['prior_assessment_exact_target_match'] = target == action and action in covered
    checks['prior_assessment_specialize'] = 'DECISION: SPECIALIZE' in assessment.splitlines()
    n, b, h = 18, Q(1, 4), 64 * 9**18
    checks['all_parameters'] = saved['parameters'] == {
        'n': n, 'theta': '1/2', 'b': '1/4', 'h': str(h),
        'rho': '1/2', 'eta': str(Q(1, h))}

    # Binomial coefficients by recurrence; no construction-script formula loop.
    choose = [1]
    for k in range(n):
        choose.append(choose[-1] * (n-k) // (k+1))
    v = [Q(choose[k], 2**(k-1)) for k in range(1, n+1, 2)]
    w = mul(v, v)
    B = [Q(0)] * n
    for s, x in enumerate(w):
        B[n-1-s] = (-1)**s * x
    shifted = shift(B, -b)
    D = [(-1)**(n-1-r) * x for r, x in enumerate(shifted)]
    # Divide h*B(-b+y) by h-b+y as a power series, then read principal parts.
    quotient = []
    previous = Q(0)
    for x in shifted:
        previous = (h*x-previous)/(h-b)
        quotient.append(previous)
    d = [(-1)**(k-1)*quotient[n-k] for k in range(1, n+1)]
    A = [2**m * x for m, x in enumerate(d)]
    M = sum(A)
    normalized = [x/M for x in A]
    all_values = {'v': v, 'w': w, 'D': D, 'd': d, 'A': A,
                  'normalized_weights': normalized}
    residuals = {}
    for name, values in all_values.items():
        stored = list(map(Q, saved['coefficients'][name]))
        checks['all_'+name+'_values_and_length'] = len(stored) == len(values) and stored == values
        residuals[name] = strings([x-y for x, y in zip(stored, values)])
    checks['M_exact_positive'] = Q(saved['coefficients']['M']) == M and M > 0
    checks['all_coefficient_positivity'] = all(x > 0 for values in all_values.values() for x in values)
    checks['normalization'] = sum(normalized) == 1

    # Full denominator-cleared rational identity, not selected evaluations.
    bpowers = [[Q(1)]]
    for k in range(n):
        bpowers.append(mul(bpowers[-1], [b, Q(1)]))
    rhs = [-d[0]*x for x in bpowers[n]]
    for k in range(1, n+1):
        part = mul([Q(h), Q(1)], bpowers[n-k])
        for r, x in enumerate(part):
            rhs[r] += (-1)**(k-1)*d[k-1]*x
    polynomial_residual = [rhs[r] - (h*B[r] if r < n else 0) for r in range(n+1)]
    checks['full_partial_fraction_polynomial_identity'] = all(x == 0 for x in polynomial_residual)

    # Taylor terms generated recursively, and factorial built by integer product.
    fact66 = 1
    for k in range(1, 67):
        fact66 *= k
    lower = upper = normalized[0]
    sine_residuals = []
    checks['eight_sine_records'] = len(saved['sine_enclosures']) == 8
    for j in range(1, 9):
        term = poly = Q(j)
        for r in range(32):
            term *= Q(-j*j, (2*r+2)*(2*r+3))
            poly += term
        error = Q(j**66, fact66)
        weight = normalized[2*j]/j
        expected = {'j': j, 'polynomial': str(poly), 'remainder': str(error),
                    'sin_enclosure': {'lower': str(poly-error), 'upper': str(poly+error)},
                    'weight': str(weight)}
        checks['sine_record_'+str(j)+'_all_fields'] = saved['sine_enclosures'][j-1] == expected
        lower += weight*(poly-error)
        upper += weight*(poly+error)
        sine_residuals.append({'j': j, 'weight_positive': weight > 0,
                               'degree': 65, 'remainder_order': 66,
                               'all_saved_fields_equal': checks['sine_record_'+str(j)+'_all_fields']})
    eps = Q(1, 2) / Q(31, 32) * Q(1, 16) * Q(33, 32)
    checks['analytic_constants_exact'] = eps == Q(33, 992) and Q(33,32)**2 > Q(17,16)
    coarse = Q(-688,10000) + eps
    expected_bounds = {'S_over_M': {'lower': str(lower), 'upper': str(upper)},
        'full_prefix_error_over_gM': str(eps), 'pi_B_over_gM_upper': str(upper+eps),
        'simple_pi_B_over_gM_upper': '-7/200', 'TEST_required_lower': 'd1*G(h)/pi > 0'}
    checks['complete_bounds_exact'] = saved['bounds'] == expected_bounds
    checks['strict_S_box'] = Q(-689,10000) < lower <= upper < Q(-688,10000)
    checks['strict_negative_margin'] = upper+eps < coarse == Q(-22031,620000) < Q(-7,200)
    checks['retained_h_charge_factors'] = h > 0 and d[0] > 0
    checks['all_original_thirteen_checks'] = len(saved['checks']) == 13 and all(saved['checks'].values()) and saved['failures'] == []
    failures = [k for k, v in checks.items() if not v]
    report = {'source_sha256': hashlib.sha256(original_bytes).hexdigest(),
        'prior_target': target, 'prior_next_action': action,
        'checks': checks, 'failures': failures,
        'coefficient_residuals': residuals, 'M_residual': str(Q(saved['coefficients']['M'])-M),
        'full_polynomial_residual': strings(polynomial_residual),
        'sine_validation': sine_residuals, 'bounds': expected_bounds,
        'coarse_upper': str(coarse), 'required_upper': '-7/200',
        'analytic_limit': 'G(h)>0 is the inherited L966 theta-integral theorem, not a numerical check.',
        'summary': {'all_checks_pass': not failures, 'checks': len(checks),
                    'coefficients_validated': {k:len(v) for k,v in all_values.items()},
                    'sines_validated': 8, 'failures': failures}}
    path = HERE / 'reflected-prefix-audit-191.json'
    path.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps({'result': report['summary'], 'actual_coarse_upper': str(coarse),
                      'required_upper': '-7/200', 'certificate': str(path)}))
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
