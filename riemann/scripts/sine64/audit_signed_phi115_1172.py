"""Audit every saved1170 record and the complete analytic-error assembly.

Finer enclosures reuse the separately audited1168 implementation, not
the1170 generator or its1166 arithmetic. Full evidence is written to disk.
The analytic justification and exact scope are canonical in C750o Section6.
"""
from fractions import Fraction as F
from math import isqrt
from pathlib import Path
import hashlib
import json
from audit_negative_loss_enclosures_1168 import (
    G, PI, box, add, sub, mul, div, times, sqrt_integer, log_box,
    trig, record, contained,
)


def main():
    root = Path(__file__).parent
    source = root/'signed-phi115-1170.json'
    source_bytes = source.read_bytes()
    old = json.loads(source_bytes)
    S = int(old['scale'])
    assert S == 10**40
    checks, failures = {}, []
    domains = {'log_calls': 0, 'trig_calls': 0, 'sinc_small_calls': 0,
               'sinc_division_calls': 0}

    def check(name, ok):
        checks[name] = bool(ok)
        if not ok:
            failures.append(name)

    def pair(r):
        assert int(r['scale']) == S
        a, b = int(r['lo']), int(r['hi'])
        assert a <= b
        return a, b

    # Independent old-grid rational endpoint operations; no1166 imports.
    def round_box(a, b=None):
        a, b = F(a), F(a if b is None else b)
        return a.numerator*S//a.denominator, -((-b.numerator*S)//b.denominator)

    def osum(x, y):
        return x[0]+y[0], x[1]+y[1]

    def odiff(x, y):
        return x[0]-y[1], x[1]-y[0]

    def oproduct(x, y):
        v = [F(a*b, S*S) for a in x for b in y]
        return round_box(min(v), max(v))

    def oratio(x, y):
        assert y[0]*y[1] > 0
        v = [F(a, b) for a in x for b in y]
        return round_box(min(v), max(v))

    def opow2(x):
        return oproduct(x, x)

    def omult(x, q):
        return oproduct(x, round_box(q))

    def log_domain(x):
        domains['log_calls'] += 1
        assert x[0] > 0
        while x[0] >= 2*S:
            x = oratio(x, round_box(2))
        while x[1] < S:
            x = omult(x, 2)
        assert S <= x[0] <= x[1] <= 2*S

    opi = pair(old['parameters']['pi'])

    def trig_domain(x):
        domains['trig_calls'] += 1
        k = (x[0]+x[1]+2*opi[0])//(4*opi[0])
        r = odiff(x, omult(opi, 2*k))
        assert max(abs(z) for z in r) <= 4*S

    def sinc_domain(x):
        if max(abs(z) for z in x) <= 4*S:
            domains['sinc_small_calls'] += 1
        else:
            domains['sinc_division_calls'] += 1
            assert x[0]*x[1] > 0
            trig_domain(x)

    def sinc(x):
        if max(abs(z) for z in x) <= 7*G:
            return trig(x, 'sinc')
        assert x[0]*x[1] > 0
        return div(trig(x, 'sin'), x)

    L = log_box(box(101))
    b = times(L, F(1, 2))
    alpha = div(times(PI, 115), L)
    A, prime = box(0), box(0)
    op = {k: pair(v) for k, v in old['parameters'].items()}
    check('old_b_assembly', op['b'] == oratio(op['L'], round_box(2)))
    check('old_alpha_assembly', op['alpha'] == oratio(omult(opi, 115), op['L']))
    log_domain(round_box(2))  # LOG2 initialization
    log_domain(round_box(101))
    powers = {}
    for n in range(2, 101):
        p = next(d for d in range(2, n+1) if n % d == 0)
        r = n
        while r % p == 0:
            r //= p
        if r == 1:
            powers[n] = p
    check('exact_all35_pairs', len(powers) == 35 and
          [(r['n'], r['p']) for r in old['prime_powers']] == list(powers.items()))
    term_records = []
    old_prime, old_A = round_box(0), round_box(0)
    for saved, (n, p) in zip(old['prime_powers'], powers.items()):
        ell = log_box(box(n))
        c = div(times(log_box(box(p)), 2), sqrt_integer(n))
        angle = mul(alpha, ell)
        corr = add(mul(sub(box(1), div(ell, L)), trig(angle, 'cos')),
                   div(trig(angle, 'sin'), mul(L, alpha)))
        contribution = mul(c, corr)
        values = dict(c=c, ell=ell, correlation=corr, contribution=contribution)
        tests = {k: contained(v, saved[k]) for k, v in values.items()}
        tests['old_product'] = pair(saved['contribution']) == oproduct(pair(saved['c']), pair(saved['correlation']))
        term_records.append(dict(n=n, p=p, values={k: record(v) for k, v in values.items()}, checks=tests))
        A, prime = add(A, c), add(prime, contribution)
        old_A = osum(old_A, pair(saved['c']))
        old_prime = osum(old_prime, pair(saved['contribution']))
        log_domain(round_box(n))
        log_domain(round_box(p))
        trig_domain(oproduct(op['alpha'], pair(saved['ell'])))
        trig_domain(oproduct(op['alpha'], pair(saved['ell'])))
    check('all35_independent_enclosures_and_products', all(all(t['checks'].values()) for t in term_records))
    check('old_complete_prime_sum', old_prime == pair(old['prime_expectation']))
    check('old_complete_A_sum', old_A == op['A'])
    params = dict(pi=PI, L=L, b=b, alpha=alpha, A=A)
    check('all_independent_parameters', all(contained(v, old['parameters'][k]) for k, v in params.items()))

    cells, integral, old_integral = [], box(0), round_box(0)
    check('mesh_and_domain', old['positive_frequency_interval'] == [1, 512]
          and F(old['mesh']) == F(1, 100) and len(old['cells']) == 51100)
    for k, saved in enumerate(old['cells']):
        midpoint = 1+F(2*k+1, 200)
        t = box(midpoint)
        u, v = sub(mul(b, t), times(PI, F(115, 2))), add(mul(b, t), times(PI, F(115, 2)))
        amplitude = add(sinc(u), sinc(v))
        logval = log_box(div(t, times(PI, 2)))
        contribution = div(mul(mul(mul(times(logval, F(1, 100)), b), amplitude), amplitude), PI)
        ot = round_box(midpoint)
        ou, ov = odiff(oproduct(op['b'], ot), omult(opi, F(115, 2))), osum(oproduct(op['b'], ot), omult(opi, F(115, 2)))
        sinc_domain(ou)
        sinc_domain(ov)
        log_domain(oratio(ot, omult(opi, 2)))
        og, ol = pair(saved['G']), pair(saved['log_symbol'])
        product = oratio(oproduct(oproduct(oproduct(omult(ol, F(1, 100)), op['b']), og), og), opi)
        tests = dict(index=saved['k'] == k, midpoint=F(saved['midpoint']) == midpoint,
                     G=contained(amplitude, saved['G']), log_symbol=contained(logval, saved['log_symbol']),
                     contribution=contained(contribution, saved['contribution']),
                     old_product=product == pair(saved['contribution']))
        cells.append(dict(k=k, midpoint=str(midpoint), G=record(amplitude),
                          log_symbol=record(logval), contribution=record(contribution), checks=tests))
        integral = add(integral, contribution)
        old_integral = osum(old_integral, pair(saved['contribution']))
        if (k+1) % 10000 == 0:
            print('Audited cells:', k+1, '/51100; failed records:',
                  sum(not all(c['checks'].values()) for c in cells), flush=True)
    check('all51100_independent_cells', all(all(c['checks'].values()) for c in cells))
    check('old_complete_midpoint_sum', old_integral == pair(old['complete_midpoint_sum']))
    check('independent_midpoint_sum_contained', contained(integral, old['complete_midpoint_sum']))

    aa = mul(alpha, alpha)
    root101 = sqrt_integer(101)
    cosh_b = times(add(root101, div(box(1), root101)), F(1, 2))
    pole = div(times(mul(aa, add(cosh_b, box(1))), 4),
               mul(mul(b, add(aa, box(F(1, 4)))), add(aa, box(F(1, 4)))))
    e0 = div(times(aa, 44), mul(mul(mul(PI, b), sub(aa, box(1))), sub(aa, box(1))))
    e1 = add(div(box(128), times(mul(mul(PI, b), aa), 9)), div(box(8), aa))
    eB = mul(div(times(aa, 64), times(mul(PI, b), 9)),
             div(add(log_box(div(box(512), times(PI, 2))), box(F(1, 3))), box(3*512**3)))
    eq = box(F(186, 80000))
    independent_errors = dict(midpoint=eq, gamma_0_1=e0, gamma_asymptotic=e1, log_tail=eB)
    check('all_independent_errors_contained', all(contained(v, old['errors'][k]) for k, v in independent_errors.items()))
    check('independent_pole_contained', contained(pole, old['full_pole']))

    # Replay the entire old-grid error formulas and form assembly separately.
    oaa = opow2(op['alpha'])
    sq = isqrt(101*S*S)
    oroot = (sq, sq+(sq*sq != 101*S*S))
    ocosh = oratio(osum(oroot, oratio(round_box(1), oroot)), round_box(2))
    oaap = osum(oaa, round_box(F(1, 4)))
    opole = oratio(oproduct(omult(oaa, 4), osum(ocosh, round_box(1))),
                   oproduct(oproduct(op['b'], oaap), oaap))
    oe0 = oratio(omult(oaa, 44), oproduct(oproduct(oproduct(opi, op['b']), odiff(oaa, round_box(1))), odiff(oaa, round_box(1))))
    oe1 = osum(oratio(round_box(128), oproduct(oproduct(omult(opi, 9), op['b']), oaa)), oratio(round_box(8), oaa))
    check('old_pole_exact_assembly', opole == pair(old['full_pole']))
    check('old_near_zero_error_exact_assembly', oe0 == pair(old['errors']['gamma_0_1']))
    check('old_asymptotic_error_exact_assembly', oe1 == pair(old['errors']['gamma_asymptotic']))
    check('old_midpoint_error_exact', pair(old['errors']['midpoint']) == round_box(F(186, 80000)))
    log_domain(oratio(round_box(512), omult(opi, 2)))
    # eB is independently enclosed above; no unrecorded old log primitive
    # is guessed. Its saved upper endpoint is the certified tail allowance.
    errors = {k: pair(old['errors'][k]) for k in independent_errors}
    ogamma = old_integral
    for key in ('midpoint', 'gamma_0_1', 'gamma_asymptotic'):
        upper = errors[key][1]
        ogamma = osum(ogamma, (-upper, upper))
    ogamma = osum(ogamma, (0, errors['log_tail'][1]))
    oenergy = osum(odiff(ogamma, old_prime), opole)
    oreduced = odiff(oenergy, round_box(0, F(1, 10**8)))
    check('old_Gamma_exact_assembly', ogamma == pair(old['gamma_expectation']))
    check('old_E_exact_assembly', oenergy == pair(old['full_E']))
    check('old_R_exact_assembly', oreduced == pair(old['full_R']))
    check('saved_E_R_allowance', F(old['errors']['E_minus_R_upper']) == F(1, 10**8))

    # Independently reassemble using exactly the SAME saved analytic
    # allowances. This audits the stated enclosure without optimizing it.
    allowance = sum(F(errors[k][1], S) for k in ('midpoint', 'gamma_0_1', 'gamma_asymptotic'))
    gamma = add(add(integral, box(-allowance, allowance)), box(0, F(errors['log_tail'][1], S)))
    energy = add(sub(gamma, prime), pole)
    reduced = sub(energy, box(0, F(1, 10**8)))
    check('independent_Gamma_contained', contained(gamma, old['gamma_expectation']))
    check('independent_E_contained', contained(energy, old['full_E']))
    check('independent_R_contained', contained(reduced, old['full_R']))
    check('b_alpha_A_ranges', 2*S < op['b'][0] and op['b'][1] < F(5, 2)*S and
          2*S < op['alpha'][0] and op['alpha'][1] < 80*S and op['A'][1] < 34*S)
    tail_bound = F(409600, 54)*F(151, 9)/10**15
    check('log_U_justification', F(8, 3)**12 > 100000)
    check('tail_bound_lt_allowance', 0 < tail_bound < F(1, 10**8))
    check('integrated_midpoint_bound', 1+4*F(5, 2)+28*F(5, 2)**2 == 186)
    rlo, rhi = (F(z, S) for z in oreduced)
    check('positive_outer_interval', F(61177, 100000) < rlo < rhi < F(62173, 100000))
    check('required_width', rhi-rlo <= F(1, 50))
    check('original_checks_consistent', all(old['checks'].values()) and old['failures'] == [])
    check('source_unchanged', source.read_bytes() == source_bytes)
    result = dict(scope='Complete fixed phi115 audit only; no complementary lower spectral floor.',
                  source=source.name, source_sha256=hashlib.sha256(source_bytes).hexdigest(),
                  method='Independent audited1168 primitives on10^-70; all finite records and old-grid complete assembly.',
                  parameters={k: record(v) for k, v in params.items()},
                  independent_errors={k: record(v) for k, v in independent_errors.items()},
                  domain_counts=domains, terms=term_records, cells=cells,
                  assembly=dict(midpoint=record(integral), prime=record(prime), pole=record(pole),
                                Gamma=record(gamma), E=record(energy), R=record(reduced)),
                  saved_full_R=old['full_R'], actual_width=str(rhi-rlo), required_width='1/50',
                  E_minus_R_rational_majorant=str(tail_bound), E_minus_R_allowance='1/100000000',
                  checks=checks, failures=failures, passed=not failures)
    out = root/'signed-phi115-audit-1172.json'
    out.write_text(json.dumps(result, indent=2)+'\n')
    print('Full audit:', len(cells), 'cells;', len(term_records), 'terms; checks', sum(checks.values()), '/', len(checks))
    print('R enclosure:', rlo, rhi)
    print('Actual width:', rhi-rlo, '; required <=1/50.')
    print('E-R majorant:', tail_bound, '; required <1/100000000.')
    print('Failures:', failures)
    print('Certificate:', out.relative_to(Path.cwd()))
    raise SystemExit(bool(failures))


if __name__ == '__main__':
    main()
