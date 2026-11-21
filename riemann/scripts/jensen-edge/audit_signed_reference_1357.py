"""Independent exact certificate audit for C019f; no original functions imported.

Airy terms are checked from closed-form coefficients and endpoint powers,
not the generating script's interval recurrence. Every recorded term is read.
Analytic validity of the imported identities and tails is recorded in C019f.
"""
from fractions import Fraction as Q
from math import factorial, prod
from pathlib import Path
import hashlib
import json

HERE = Path(__file__).resolve().parent
SOURCE = HERE / 'signed-reference-1355.json'
OUTPUT = HERE / 'signed-reference-audit-1357.json'
GRID = 10**60
checks = []


def check(label, condition):
    checks.append({'claim': label, 'passed': bool(condition)})
    if not condition:
        raise AssertionError(label)


def interval(value):
    lo, hi = map(Q, value)
    check('ordered interval', lo <= hi)
    return lo, hi


def rounded(lo, hi):
    return (Q(lo.numerator * GRID // lo.denominator, GRID),
            Q(-((-hi.numerator * GRID) // hi.denominator), GRID))


def contains(outer, inner):
    return outer[0] <= inner[0] <= inner[1] <= outer[1]


def plus(a, b):
    return a[0] + b[0], a[1] + b[1]


def times(a, b):
    endpoints = [u*v for u in a for v in b]
    return min(endpoints), max(endpoints)


def reciprocal(a):
    check('reciprocal avoids zero', a[0]*a[1] > 0)
    return 1/a[1], 1/a[0]


def scale(a, c):
    return times(a, (Q(c), Q(c)))


def packed(a):
    return list(map(str, a))


def atan(q):
    s = sum((Q((-1)**k, (2*k+1)*q**(2*k+1)) for k in range(101)), Q())
    e = Q(1, 203*q**203)
    return s-e, s+e


def coefficient(j, k):
    return Q(prod(3*h+j+1 for h in range(k)), factorial(3*k+j))


def main():
    cert = json.loads(SOURCE.read_text())
    constants = cert['constants']
    pi = interval(constants['pi'])
    check('Machin rational tangent identity',
          (Q(120, 119)-Q(1, 239))/(1+Q(120, 119*239)) == 1)
    check('Machin positive angle below 4/5', 4*(Q(1, 5)-Q(1, 375))-Q(1, 239) > 0)
    check('pi enclosure contains exact arctangent bounds',
          contains(pi, plus(scale(atan(5), 16), scale(atan(239), -4))))
    roots = {}
    for n in (3, 4):
        roots[n] = interval(constants[f'cube_root_{n}'])
        lo, hi = roots[n]
        check(f'cube root {n} endpoints', 0 < lo and lo**3 <= n <= hi**3)
    gamma = {}
    for m in (0, 1):
        stored = constants[f'gamma_{m+1}_3']
        check(f'gamma {m} parameters', (stored['m'], stored['N'], stored['cutoff_u']) == (m, 320, 4))
        s = sum((Q(3*(-1)**k*4**(3*k+m+1), factorial(k)*(3*k+m+1))
                 for k in range(321)), Q())
        err = Q(3*4**(964+m), factorial(321)*(964+m))
        tail = Q(1, 2**64)
        check(f'gamma {m} full Taylor sum and error',
              s == Q(stored['integrated_sum']) and err == Q(stored['integrated_taylor_error']))
        check(f'gamma {m} positive tail', tail == Q(stored['positive_tail_upper']))
        gamma[m] = interval(stored['enclosure'])
        check(f'gamma {m} enclosure and error threshold',
              contains(gamma[m], (s-err, s+err+tail)) and gamma[m][0] > 0 and err < Q(1, 10**60))
    ai0 = interval(constants['Ai_0'])
    aip0 = interval(constants['Ai_prime_0'])
    check('Ai(0) exact formula', contains(ai0, reciprocal(times(times(roots[3], roots[3]), gamma[1]))))
    check('Ai prime(0) exact formula', contains(aip0, scale(reciprocal(times(roots[3], gamma[0])), -1)))
    beta = interval(constants['beta'])
    check('beta exact formula', contains(beta, times(scale(roots[4], 16), reciprocal(times(pi, pi)))))
    results = {}
    all_terms = 0
    for x in (1, 2, 4):
        v = cert['values'][str(x)]
        z = interval(v['argument'])
        check(f'x={x} argument and range', contains(z, scale(beta, -x)) and -11 < z[0] <= z[1] < 0)
        bases = []
        for j in (0, 1):
            b = v[f'basis{j}']
            check(f'x={x},j={j} parameters',
                  (b['residue'], b['last_k'], b['absolute_argument_bound'], len(b['term_enclosures'])) == (j, 100, 11, 101))
            direct_sum = (Q(), Q())
            for k, stored_term in enumerate(b['term_enclosures']):
                power = 3*k+j
                endpoints = [coefficient(j, k)*u**power for u in z]
                exact_term = (min(endpoints), max(endpoints))
                check(f'x={x},j={j},k={k} closed-form term', contains(interval(stored_term), exact_term))
                direct_sum = plus(direct_sum, rounded(*exact_term))
                all_terms += 1
            check(f'x={x},j={j} partial sum', contains(interval(b['partial_sum']), direct_sum))
            first = coefficient(j, 101)*11**(303+j)
            ratio = Q(1331, (303+j)*(302+j))
            remainder = first/(1-ratio)
            check(f'x={x},j={j} complete geometric tail',
                  Q(b['first_omitted_upper']) == first and Q(b['tail_ratio_upper']) == ratio
                  and 0 < ratio < 1 and Q(b['tail_upper']) == remainder < Q(1, 10**60))
            basis = rounded(*plus(direct_sum, (-remainder, remainder)))
            check(f'x={x},j={j} full basis', contains(interval(b['enclosure']), basis))
            bases.append(basis)
        airy = plus(times(ai0, bases[0]), times(aip0, bases[1]))
        ref = times(roots[4], airy)
        saved_ref = interval(v['reference'])
        check(f'x={x} Ai and reference inclusions', contains(interval(v['Ai']), airy) and contains(saved_ref, ref))
        coarse = interval(v['coarse'])
        check(f'x={x} coarse inclusion', contains(coarse, saved_ref))
        width = saved_ref[1]-saved_ref[0]
        check(f'x={x} width thresholds', width < Q(1, 10**12) < Q(1, 10**6))
        check(f'x={x} sign', saved_ref[0] > 0 if x == 2 else saved_ref[1] < 0)
        results[str(x)] = {'independent_reference': packed(rounded(*ref)),
                           'original_width': str(width), 'coarse': packed(coarse)}
    check('all 606 retained terms checked', all_terms == 606)
    replay = HERE / 'replay-1357' / SOURCE.name
    check('replay byte identity', replay.read_bytes() == SOURCE.read_bytes())
    return {'summary': {'audit_checks': len(checks), 'retained_terms_checked': all_terms,
                        'all_checks_passed': all(c['passed'] for c in checks),
                        'actual_widths_strictly_below': '1/1000000000000',
                        'required_width': '1/1000000', 'gamma_and_Airy_tail_threshold': '1/10^60',
                        'enclosure_failures': [], 'rejected_target': 'Opposite signs at x=1 and x=4; both are negative.',
                        'source_sha256': hashlib.sha256(SOURCE.read_bytes()).hexdigest()},
            'reference_checks': results, 'checks': checks}


if __name__ == '__main__':
    try:
        report = main()
    except Exception as exc:
        OUTPUT.write_text(json.dumps({'checks': checks, 'failure': repr(exc)}, indent=2)+'\n')
        print('AUDIT FAILED:', exc, 'Full evidence:', OUTPUT)
        raise
    OUTPUT.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(report['summary'], indent=2))
    print('Full audit certificate:', OUTPUT.relative_to(Path.cwd()))
