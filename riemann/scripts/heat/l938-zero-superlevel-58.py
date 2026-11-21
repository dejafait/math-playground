#!/usr/bin/env python3
"""One approved six-polynomial sign test; exact integers/Fractions only."""
from fractions import Fraction as Q
from hashlib import sha256
from itertools import combinations
from math import comb, factorial, gcd, lcm, prod
from pathlib import Path
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).with_suffix('.json')
report = {'task': 'Complete positive-root/sign tables for unchanged L940 H_1,...,H_6',
          'arithmetic': 'Python integers and fractions.Fraction only; ascending coefficients',
          'checks': [], 'failures': []}


def check(name, ok, actual=None, required=None):
    item = dict(name=name, ok=bool(ok))
    if actual is not None:
        item['actual'] = actual
    if required is not None:
        item['required'] = required
    report['checks'].append(item)
    if not ok:
        report['failures'].append(item)
        raise ValueError(name)


def trim(p):
    p = list(map(Q, p))
    while p and not p[-1]:
        p.pop()
    return p


def strings(p):
    return [str(c) for c in p]


def add(p, q):
    r = [Q(0)]*max(len(p), len(q))
    for i, c in enumerate(p):
        r[i] += c
    for i, c in enumerate(q):
        r[i] += c
    return trim(r)


def mul(p, q):
    if not p or not q:
        return []
    r = [Q(0)]*(len(p)+len(q)-1)
    for i, c in enumerate(p):
        for j, d in enumerate(q):
            r[i+j] += c*d
    return trim(r)


def scale(p, c):
    return trim([c*x for x in p])


def derivative(p):
    return trim([i*p[i] for i in range(1, len(p))])


def value(p, x):
    v = Q(0)
    for c in reversed(p):
        v = v*x+c
    return v


def sign(x):
    return int(x > 0)-int(x < 0)


def primitive(p):
    """p -> positive factor * p, never reversing its sign."""
    p = trim(p)
    if not p:
        return [], Q(1)
    denominator = lcm(*(x.denominator for x in p))
    integers = [int(x*denominator) for x in p]
    content = gcd(*integers)
    factor = Q(denominator, content)
    return scale(p, factor), factor


def divide(a, b):
    if not b:
        raise ZeroDivisionError('polynomial division by zero')
    r = trim(a)
    q = [Q(0)]*max(0, len(a)-len(b)+1)
    while r and len(r) >= len(b):
        j = len(r)-len(b)
        c = r[-1]/b[-1]
        q[j] += c
        for i, d in enumerate(b):
            r[i+j] -= c*d
        r = trim(r)
    q = trim(q)
    if add(mul(q, b), r) != trim(a):
        raise ArithmeticError('division identity failed')
    return q, r


def sturm(p, label):
    """Signed remainders, each rescaled by a positive rational only."""
    p = trim(p)
    if not p:
        raise ValueError('zero polynomial has no finite root table')
    a, sa = primitive(p)
    b, sb = primitive(derivative(p))
    chain = [a]
    identities = []
    if b:
        chain.append(b)
        while True:
            quotient, remainder = divide(a, b)
            nxt, factor = primitive(scale(remainder, -1))
            ok = add(mul(quotient, b), scale(nxt, -1/factor)) == a
            check(f'{label}: signed division {len(identities)}', ok,
                  'a = quotient*b - next/factor', 'exact coefficient equality')
            identities.append({'quotient': strings(quotient),
                               'next_positive_factor': str(factor),
                               'next': strings(nxt), 'identity_verified': ok})
            if not nxt:
                break
            check(f'{label}: strict remainder degree {len(identities)}',
                  len(nxt) < len(b))
            chain.append(nxt)
            a, b = b, nxt
    return chain, {'initial_positive_factors': [str(sa), str(sb)],
                   'polynomials': [strings(c) for c in chain],
                   'division_identities': identities}


def endpoint(chain, x):
    vals = [value(c, x) for c in chain]
    signs = [sign(v) for v in vals]
    nz = [s for s in signs if s]
    variations = sum(a != b for a, b in zip(nz, nz[1:]))
    return {'q': str(x), 'values': strings(vals), 'signs': signs,
            'variations': variations}


def count(chain, a, b):
    if not value(chain[0], a) or not value(chain[0], b):
        raise ValueError('root endpoint in Sturm count')
    return endpoint(chain, a)['variations']-endpoint(chain, b)['variations']


def isolate(chain, a, b, roots, budget):
    n = count(chain, a, b)
    if not n:
        return
    if n == 1 and b-a <= Q(1, 4096):
        roots.append((a, b))
        return
    budget[0] += 1
    if budget[0] > 10000:
        raise RuntimeError('isolation subdivision budget exceeded')
    mid = (a+b)/2
    # Avoid root endpoints even if the exact root is rational.
    denominator = 3
    while not value(chain[0], mid):
        mid = a+(b-a)/denominator
        denominator += 1
    isolate(chain, a, mid, roots, budget)
    isolate(chain, mid, b, roots, budget)


def main():
    paths = [ROOT/'lemmas/L938-actual-h2-fixed-energy-density-and-cell-test.md',
             ROOT/'lemmas/L939-actual-h2-balanced-energy-tail-asymptotic.md',
             ROOT/'lemmas/L940-symmetrized-h2-polynomial-schur-concavity-obstruction.md',
             ROOT/'scripts/heat/l938-schur-obstruction-56.json',
             ROOT/'drafts/literature/2026-11-09-l938-zero-superlevel-balancing-scope-56.md',
             Path(__file__)]
    report['input_sha256'] = {str(p.relative_to(ROOT)): sha256(p.read_bytes()).hexdigest()
                              for p in paths}
    rows = [(int(c), tuple(map(int, a.split(',')))) for c, a in
            re.findall(r'^\|\s*(-?\d+)\s*\|\s*\(([^)]+)\)\s*\|\s*$',
                       paths[0].read_text(), re.M)]
    check('34 distinct original rows', len(rows) == len({a for _, a in rows}) == 34)
    saved = json.loads(paths[3].read_text())
    row_records = []
    hs = {m: [Q(0)]*13 for m in range(1, 7)}
    for row, (c, alpha) in enumerate(rows, 1):
        ks = [k for k, n in enumerate(alpha) for _ in range(n)]
        check(f'row {row}: unchanged twelve slots and degree', len(ks) == sum(ks) == 12)
        denom = prod(factorial(2*k) for k in ks)
        blocks = {}
        for m in range(1, 7):
            # Explicit labelled subsets, not the old dynamic-programming producer.
            counts = [0]*13
            for subset in combinations(range(12), m):
                counts[sum(ks[j] for j in subset)] += 1
            check(f'row {row}, m={m}: average denominator', sum(counts) == comb(12, m))
            h = [Q(c*n, denom*comb(12, m)) for n in counts]
            check(f'row {row}, m={m}: saved row coefficients',
                  strings(h) == saved['rows'][row-1]['blocks'][str(m)]['H_coefficients'])
            for j in range(13):
                hs[m][j] += h[j]
            blocks[str(m)] = {'counts': counts, 'H_coefficients': strings(h)}
        row_records.append({'row': row, 'c': c, 'alpha': alpha,
                            'factorial_denominator': str(denom), 'blocks': blocks})
    report['rows'] = row_records
    report['blocks'] = {}
    summaries = []
    for m, raw in hs.items():
        h = trim(raw)
        check(f'm={m}: saved full coefficients',
              strings(raw) == saved['block_polynomials'][str(m)]['H_coefficients'])
        check(f'm={m}: balanced value from L939(5)-(6)',
              value(h, Q(1)) == Q(1, 371319795000),
              str(value(h, Q(1))), '1/371319795000')
        # Each row has the same q=1 value for every block size.
        for r in row_records:
            actual = sum(map(Q, r['blocks'][str(m)]['H_coefficients']))
            required = Q(r['c'], int(r['factorial_denominator']))
            check(f'm={m}, row {r["row"]}: balanced row value', actual == required)
        n, normalization = primitive(h)
        entry = {'H_coefficients': strings(h), 'integer_coefficients': strings(n),
                 'integer_positive_factor': str(normalization),
                 'degree': len(n)-1, 'zero_polynomial': not n,
                 'constant_polynomial': len(n) == 1}
        report['blocks'][str(m)] = entry
        check(f'm={m}: nonzero nonconstant input', len(n) > 1)
        # Domain endpoint 0 is excluded. Remove its entire exact multiplicity.
        zero_order = 0
        while n and not n[0]:
            zero_order += 1
            n = n[1:]
        entry['excluded_zero_multiplicity'] = zero_order
        chain, chain_record = sturm(n, f'm={m}, primary')
        entry['sturm'] = chain_record
        # Gcd recovered from final Euclidean remainder, with monic normalization.
        g = scale(chain[-1], 1/chain[-1][-1])
        layer_records, layer_chains = [], []
        current = n
        while len(g) > 1:
            quotient, remainder = divide(current, g)
            check(f'm={m}: gcd layer divisibility {len(layer_records)+1}', not remainder)
            gc, record = sturm(g, f'm={m}, gcd layer {len(layer_records)+1}')
            record['gcd'] = strings(g)
            record['previous_divided_by_gcd'] = strings(quotient)
            layer_records.append(record)
            layer_chains.append(gc)
            current = g
            g = scale(gc[-1], 1/gc[-1][-1])
        entry['successive_gcds'] = layer_records
        entry['terminal_monic_gcd'] = strings(g)
        entry['primary_last_remainder'] = strings(chain[-1])
        # Strict Cauchy bound for monic n: every root has |q| < B.
        bound = Q(1)+max(abs(c/n[-1]) for c in n[:-1])
        B = Q(bound.numerator//bound.denominator+1)
        check(f'm={m}: strict root bound', B > bound, str(B), f'> {bound}')
        entry['root_bound'] = {'monic_Cauchy': str(bound), 'outer_integer': str(B)}
        check(f'm={m}: endpoints 0,1,B are nonroots',
              all(value(n, x) != 0 for x in [Q(0), Q(1), B]))
        total = count(chain, Q(0), B)
        roots = []
        budget = [0]
        isolate(chain, Q(0), Q(1), roots, budget)
        isolate(chain, Q(1), B, roots, budget)
        check(f'm={m}: complete positive-root count', len(roots) == total,
              len(roots), total)
        entry['total_positive_roots'] = total
        entry['global_endpoints'] = [endpoint(chain, x) for x in [Q(0), Q(1), B]]
        entry['isolation_subdivisions'] = budget[0]
        root_records = []
        for i, (a, b) in enumerate(roots):
            multiplicities = [count(gc, a, b) for gc in layer_chains]
            check(f'm={m}, root {i+1}: isolator count', count(chain, a, b) == 1)
            check(f'm={m}, root {i+1}: gcd counts binary',
                  all(c in [0, 1] for c in multiplicities))
            root_records.append({'index': i+1, 'lower': str(a), 'upper': str(b),
                                 'left': endpoint(chain, a), 'right': endpoint(chain, b),
                                 'multiplicity': 1+sum(multiplicities),
                                 'successive_gcd_counts': multiplicities,
                                 'gcd_endpoints': [[endpoint(gc, a), endpoint(gc, b)]
                                                   for gc in layer_chains],
                                 'value_at_root': '0', 'included_in_zero_superlevel': True})
        entry['roots'] = root_records
        intervals = []
        for i in range(len(roots)+1):
            if not roots:
                sample = Q(1)
            elif i == 0:
                sample = roots[0][0]/2
            elif i == len(roots):
                sample = B
            else:
                sample = (roots[i-1][1]+roots[i][0])/2
            val = value(h, sample)
            check(f'm={m}, interval {i}: nonzero exact sign', val != 0)
            intervals.append({'index': i, 'left': '0' if i == 0 else f'root_{i}',
                              'right': 'infinity' if i == len(roots) else f'root_{i+1}',
                              'sample': str(sample), 'H_at_sample': str(val),
                              'sign': sign(val)})
        entry['open_intervals'] = intervals
        # At EVERY root, closed-set inclusion requires nonnegative on its inward side.
        exits = []
        for i, root in enumerate(root_records):
            a, b = Q(root['lower']), Q(root['upper'])
            inward_interval = i+1 if b < 1 else i
            check(f'm={m}, root {i+1}: lies strictly on one side of 1', b < 1 or a > 1)
            root['inward_interval'] = inward_interval
            root['inward_sign'] = intervals[inward_interval]['sign']
            if root['inward_sign'] < 0:
                exits.append({'root': i+1, 'q0_algebraic': f'unique root in ({a},{b})',
                              'q1': intervals[inward_interval]['sample'],
                              'q1_H': intervals[inward_interval]['H_at_sample']})
        # If signs are positive at 1 and inward of every root, the union of
        # closed nonnegative intervals has no inward exit, including isolated zeros.
        entry['inward_exits'] = exits
        entry['zero_superlevel_inward_preserved'] = not exits
        summaries.append({'m': m, 'degree': len(h)-1, 'positive_roots': total,
                          'outer_root_bound': {'actual_B': str(B),
                                               'required_strictly_greater_than': str(bound)},
                          'multiplicities': [r['multiplicity'] for r in root_records],
                          'interval_signs': [r['sign'] for r in intervals],
                          'isolators': [[r['lower'], r['upper']] for r in root_records],
                          'inward_exits': len(exits), 'preserved': not exits})
    # Compact rational witness uses existing nonroot isolator endpoints only.
    block = report['blocks']['4']
    root = block['roots'][1]
    q0, q1 = Q(root['lower']), Q(root['upper'])
    h = list(map(Q, block['H_coefficients']))
    n = list(map(Q, block['integer_coefficients']))
    v0, v1 = value(h, q0), value(h, q1)
    check('rational witness: inward order', 0 < q0 < q1 < 1)
    check('rational witness: strict inward exit', v0 > 0 and v1 < 0,
          [sign(v0), sign(v1)], [1, -1])
    denominator = lcm(q0.denominator, q1.denominator)
    nn0 = value(n, q0)*denominator**12
    nn1 = value(n, q1)*denominator**12
    check('rational witness: integer numerators', nn0.denominator == nn1.denominator == 1)
    def t(q):
        s = 4*q+8
        return [q/s]*4+[1/s]*8
    t0, t1 = t(q0), t(q1)
    rho = ((q1-1)/(4*q1+8))/((q0-1)/(4*q0+8))
    check('rational witness: doubly stochastic mixture',
          0 < rho < 1 and all(b == rho*a+(1-rho)/12 for a, b in zip(t0, t1)))
    report['witness'] = {'m': 4, 'q0': str(q0), 'q1': str(q1),
                         't0': strings(t0), 't1': strings(t1), 'rho': str(rho),
                         'H_q0': str(v0), 'H_q1': str(v1),
                         'integer_polynomial': block['integer_coefficients'],
                         'integer_positive_factor': block['integer_positive_factor'],
                         'evaluation_denominator': str(denominator**12),
                         'N_q0_numerator': str(nn0), 'N_q1_numerator': str(nn1),
                         'Pbar_t0': str(v0/(4*q0+8)**12),
                         'Pbar_t1': str(v1/(4*q1+8)**12)}
    report['summary'] = {'result': 'SIX_PATH_PASS' if all(x['preserved'] for x in summaries)
                         else 'INWARD_EXIT_OBSTRUCTION',
                         'required': 'no inward negative interval adjacent to any positive root',
                         'blocks': summaries, 'checks': len(report['checks']),
                         'failures': len(report['failures']),
                         'witness': {'m': 4, 'q0': str(q0), 'q1': str(q1),
                                     'actual_scaled_N_q0': str(nn0),
                                     'actual_scaled_N_q1': str(nn1),
                                     'required_signs': ['>0', '<0']},
                         'certificate': str(OUT.relative_to(ROOT))}


try:
    main()
except Exception as exc:
    report['exception'] = {'type': type(exc).__name__, 'message': str(exc)}
    report['failures'].append({'name': 'execution completed', 'exception': report['exception']})
finally:
    OUT.write_text(json.dumps(report, indent=2)+'\n')

if report['failures']:
    print(json.dumps({'result': 'FAILED', 'failures': report['failures'],
                      'certificate': str(OUT.relative_to(ROOT))}, indent=2))
    sys.exit(1)
print(json.dumps(report['summary'], indent=2))
