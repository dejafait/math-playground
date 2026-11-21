#!/usr/bin/env python3
"""The approved 48 exact Schur tests; no floating point or theta evaluation."""
from collections import Counter
from fractions import Fraction as F
from hashlib import sha256
from itertools import combinations, permutations
from math import comb, factorial, lcm, prod
from pathlib import Path
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).with_suffix('.json')
report = {'task': 'L938 full S_12 arithmetic average: approved 48 tuples',
          'arithmetic': 'Python integers and fractions.Fraction only',
          'checks': [], 'failures': []}


def check(name, ok, actual=None, required=None):
    item = {'name': name, 'ok': bool(ok)}
    if actual is not None:
        item['actual'] = actual
    if required is not None:
        item['required'] = required
    report['checks'].append(item)
    if not ok:
        report['failures'].append(item)


def clean(p):
    return {a: c for a, c in p.items() if c}


def padd(p, q):
    r = dict(p)
    for a, c in q.items():
        r[a] = r.get(a, 0) + c
    return clean(r)


def scale(p, c):
    return clean({a: c*b for a, b in p.items()})


def pmul(p, q):
    r = {}
    for a, c in p.items():
        for b, d in q.items():
            z = tuple(x+y for x, y in zip(a, b))
            r[z] = r.get(z, 0) + c*d
    return clean(r)


def determinant_rows():
    zero = (0,)*6
    q = [{zero: 1}]
    for j in range(6):
        e = tuple(int(i == j) for i in range(6))
        q.append({e: (-1)**(j+1)})
    ss = [{}]
    for n in range(1, 7):
        sn = scale(q[n], -n)
        for j in range(1, n):
            sn = padd(sn, scale(pmul(ss[j], q[n-j]), -1))
        ss.append(sn)
    det = {}
    for perm in permutations(range(3)):
        inversions = sum(perm[i] > perm[j] for i in range(3)
                         for j in range(i+1, 3))
        term = {zero: (-1)**inversions}
        for i in range(3):
            term = pmul(term, ss[2+i+perm[i]])
        det = padd(det, term)
    return {(12-sum(a),)+a: c for a, c in det.items()}


def subset_counts(alpha, m):
    """Coefficient [z^m x^s] product_k (1+z*x^k)^alpha[k]."""
    state = {(0, 0): 1}
    for k, count in enumerate(alpha):
        nxt = {}
        for (used, degree), c in state.items():
            for b in range(min(count, m-used)+1):
                key = (used+b, degree+k*b)
                nxt[key] = nxt.get(key, 0) + c*comb(count, b)
        state = nxt
    return [state.get((m, s), 0) for s in range(13)]


def pair_derivative_counts(alpha, m):
    """Fix ordered exponents at the two differentiated coordinates."""
    result = [0]*13
    assignment_count = 0
    for k, nk in enumerate(alpha):
        if not nk:
            continue
        for ell, nl in enumerate(alpha):
            ways = nk*(nl-int(k == ell))
            if not ways:
                continue
            remaining = list(alpha)
            remaining[k] -= 1
            remaining[ell] -= 1
            counts = subset_counts(remaining, m-1)
            assignment_count += ways*sum(counts)
            for s, c in enumerate(counts):
                if not c:
                    continue
                if k:
                    result[k-1+s] += ways*c*k
                if ell:
                    result[k+s] -= ways*c*ell
    denom = 12*11*comb(10, m-1)
    return [F(c, denom) for c in result], assignment_count


def block_difference(h, m):
    """H'/m - (12H-qH')/(12-m), ambient partial difference."""
    return [F((s+1)*h[s+1], m) - F((12-s)*h[s], 12-m)
            if s < 12 else F(0) for s in range(13)]


def evaluate(p, q):
    value = F(0)
    for c in reversed(p):
        value = value*q+c
    return value


def derivative(p):
    return [i*p[i] for i in range(1, len(p))]


def strings(xs):
    return [str(x) for x in xs]


def main():
    src = ROOT/'lemmas/L938-actual-h2-fixed-energy-density-and-cell-test.md'
    src939 = ROOT/'lemmas/L939-actual-h2-balanced-energy-tail-asymptotic.md'
    assessment = ROOT/'drafts/literature/2026-11-09-l938-simplex-majorization-scope-54.md'
    report['input_sha256'] = {
        str(p.relative_to(ROOT)): sha256(p.read_bytes()).hexdigest()
        for p in (src, src939, assessment, Path(__file__))}
    parsed = re.findall(r'^\|\s*(-?\d+)\s*\|\s*\(([^)]+)\)\s*\|\s*$',
                        src.read_text(), re.M)
    rows = [(int(c), tuple(map(int, a.split(',')))) for c, a in parsed]
    check('table has 34 rows', len(rows) == 34, len(rows), 34)
    check('rows are distinct', len({a for _, a in rows}) == 34)
    rebuilt = determinant_rows()
    check('Newton recurrence and six Leibniz terms reproduce full table',
          rebuilt == {a: c for c, a in rows})
    check('ordinary degree at most six before A0 homogenization',
          all(a[0] >= 6 for a in rebuilt))
    if report['failures']:
        raise ValueError('Invalid input table')

    records = []
    row_blocks = {}
    for idx, (c, alpha) in enumerate(rows):
        ks = tuple(k for k, n in enumerate(alpha) for _ in range(n))
        denom = prod(factorial(2*k)**n for k, n in enumerate(alpha))
        check(f'row {idx+1} twelve slots and degree twelve',
              len(ks) == 12 and sum(ks) == 12)
        check(f'row {idx+1} all factorials',
              denom == prod(factorial(2*k) for k in ks))
        orbit_size = factorial(12)//prod(factorial(n) for n in alpha)
        multiplicity = prod(factorial(n) for n in alpha)
        check(f'row {idx+1} orbit multiplicity',
              orbit_size*multiplicity == factorial(12))
        record = {'row': idx+1, 'coefficient': c, 'alpha': list(alpha),
                  'exponents': list(ks), 'factorial_denominator': str(denom),
                  'labelled_weight': str(F(c, denom)),
                  'orbit_size': orbit_size, 'stabilizer_size': multiplicity,
                  'blocks': {}}
        for m in range(1, 7):
            counts = subset_counts(alpha, m)
            enumerated = Counter(sum(ks[j] for j in subset)
                                 for subset in combinations(range(12), m))
            check(f'row {idx+1}, m={m}, subset coefficients',
                  counts == [enumerated[s] for s in range(13)])
            check(f'row {idx+1}, m={m}, normalized full average',
                  sum(counts) == comb(12, m))
            h = [F(c*x, denom*comb(12, m)) for x in counts]
            delta = block_difference(h, m)
            raw_pair, assignment_count = pair_derivative_counts(alpha, m)
            pair = [F(c, denom)*x for x in raw_pair]
            check(f'row {idx+1}, m={m}, conditioned derivative normalization',
                  assignment_count == 12*11*comb(10, m-1))
            check(f'row {idx+1}, m={m}, independent ambient derivative coefficients',
                  delta == pair)
            check(f'row {idx+1}, m={m}, equal coordinates',
                  evaluate(delta, F(1)) == 0)
            row_blocks[(idx, m)] = (h, delta, pair)
            record['blocks'][str(m)] = {
                'subset_counts': counts, 'subset_denominator': comb(12, m),
                'H_coefficients': strings(h),
                'ambient_difference_coefficients': strings(delta),
                'conditioned_difference_coefficients': strings(pair),
                'conditioned_assignment_count': assignment_count}
        records.append(record)
    report['rows'] = records

    blocks = {}
    for m in range(1, 7):
        h = [sum((row_blocks[(i, m)][0][s] for i in range(34)), F(0))
             for s in range(13)]
        delta = block_difference(h, m)
        check(f'm={m}, balanced coefficient',
              evaluate(h, F(1)) == F(1, 371319795000))
        blocks[m] = (h, delta)
    report['block_polynomials'] = {
        str(m): {'H_coefficients': strings(h),
                 'ambient_difference_coefficients': strings(delta)}
        for m, (h, delta) in blocks.items()}

    qs = [F(1, 16), F(1, 8), F(1, 4), F(1, 2), F(2), F(4), F(8), F(16)]
    tests = []
    for m in range(1, 7):
        h, delta = blocks[m]
        for q in qs:
            s = m*q+12-m
            a, b = q/s, 1/s
            value = evaluate(h, q)
            prime = evaluate(derivative(h), q)
            pa = prime/m/s**11
            pb = (12*value-q*prime)/(12-m)/s**11
            direct_d = (q-1)*evaluate(delta, q)/s**12
            d = (a-b)*(pa-pb)
            formula_d = (q-1)*(s*prime-12*m*value)/(m*(12-m)*s**12)
            row_values = []
            for i in range(34):
                rh, rd, rp = row_blocks[(i, m)]
                row_values.append((q-1)*evaluate(rp, q)/s**12)
            check(f'm={m}, q={q}, interior unit simplex',
                  a > 0 and b > 0 and m*a+(12-m)*b == 1)
            check(f'm={m}, q={q}, Euler identity',
                  m*a*pa+(12-m)*b*pb == 12*value/s**12)
            check(f'm={m}, q={q}, all derivative evaluations agree',
                  d == direct_d == formula_d == sum(row_values, F(0)))
            tests.append({'m': m, 'q': str(q), 's': str(s),
                          't': strings([a]*m+[b]*(12-m)),
                          'i': 1, 'j': m+1, 'Pbar': str(value/s**12),
                          'partial_i': str(pa), 'partial_j': str(pb),
                          'D': str(d), 'sign': (d > 0)-(d < 0),
                          'row_D_contributions': strings(row_values)})
    report['tests'] = tests
    check('exactly the 48 prescribed tuples, no additional test points',
          len(tests) == 48 and len({(t['m'], t['q']) for t in tests}) == 48)
    positives = [t for t in tests if t['sign'] > 0]
    # Prefer the single-coordinate block for a compact hand-verifiable witness.
    if positives:
        witness = min(positives,
                      key=lambda t: (t['m'] != 1, F(t['q']) < 1,
                                     len(t['D']), t['m'], F(t['q'])))
        report['witness'] = dict(witness)
        wm = witness['m']
        report['witness']['H_coefficients'] = strings(blocks[wm][0])
        report['witness']['ambient_difference_coefficients'] = strings(blocks[wm][1])
        common = lcm(*(c.denominator for c in blocks[wm][0]))
        integer_h = [int(c*common) for c in blocks[wm][0]]
        wq, ws = F(witness['q']), F(witness['s'])
        integer_value = evaluate(integer_h, wq)
        integer_prime = evaluate(derivative(integer_h), wq)
        bracket = ws*integer_prime-12*wm*integer_value
        check('compact witness integer-polynomial identity',
              F(witness['D']) == (wq-1)*bracket/
              (wm*(12-wm)*ws**12*common))
        report['witness']['integer_polynomial'] = {
            'common_denominator': str(common), 'coefficients': integer_h,
            'N_at_q': str(integer_value), 'N_prime_at_q': str(integer_prime),
            's_N_prime_minus_12m_N': str(bracket)}
    else:
        report['witness'] = None
    report['summary'] = {
        'tested': len(tests), 'positive': len(positives),
        'zero': sum(t['sign'] == 0 for t in tests),
        'negative': sum(t['sign'] < 0 for t in tests),
        'required_obstruction': 'at least one exact D > 0',
        'outcome': 'OBSTRUCTION' if positives else 'INCONCLUSIVE',
        'checks': len(report['checks']), 'failures': len(report['failures']),
        'certificate': str(OUT.relative_to(ROOT)),
        'all_signs': [{'m': m, 'signs_in_prescribed_q_order':
                       [t['sign'] for t in tests if t['m'] == m]}
                      for m in range(1, 7)]}


try:
    main()
except Exception as exc:
    report['exception'] = {'type': type(exc).__name__, 'message': str(exc)}
    report['failures'].append({'name': 'execution completed', 'ok': False,
                               'exception': report['exception']})
finally:
    OUT.write_text(json.dumps(report, indent=2)+'\n')

if report['failures']:
    print(json.dumps({'result': 'FAILED', 'failures': report['failures'],
                      'certificate': str(OUT.relative_to(ROOT))}, indent=2))
    sys.exit(1)
print(json.dumps(report['summary'], indent=2))
if report['witness']:
    w = report['witness']
    print(f"Witness m={w['m']}, q={w['q']}: D={w['D']} > 0")
