"""Exact bounded reference-root sign test, not a global root-count proof."""
from fractions import Fraction as F
from pathlib import Path
from itertools import combinations
import json


def trim(p):
    p = list(map(F, p))
    while p and not p[-1]:
        p.pop()
    return p


def add(p, q):
    return trim([(p[i] if i < len(p) else 0)+(q[i] if i < len(q) else 0)
                 for i in range(max(len(p), len(q)))])


def scale(p, c):
    return trim([F(c)*a for a in p])


def mul(p, q):
    z = [F(0)]*(len(p)+len(q)-1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            z[i+j] += a*b
    return trim(z)


def deriv(p):
    return trim([i*p[i] for i in range(1, len(p))])


def apply(p, t):
    return add(add(p, deriv(p)), scale(deriv(deriv(p)), t))


def divmodp(p, q):
    p, q = trim(p), trim(q)
    assert q
    out = [F(0)]*max(0, len(p)-len(q)+1)
    while p and len(p) >= len(q):
        j, c = len(p)-len(q), p[-1]/q[-1]
        out[j] = c
        p = add(p, [F(0)]*j+scale(q, -c))
    return trim(out), p


def val(p, x):
    z = F(0)
    for c in reversed(p):
        z = z*x+c
    return z


def sign(x):
    return (x > 0)-(x < 0)


def sturm(p):
    seq = [trim(p), deriv(p)]
    while seq[-1]:
        rem = divmodp(seq[-2], seq[-1])[1]
        if not rem:
            break
        seq.append(scale(rem, -1))
    return seq


def variations(seq, x):
    s = [sign(val(p, x)) for p in seq]
    s = [a for a in s if a]
    return sum(a != b for a, b in zip(s, s[1:]))


def interval_value(p, a, b):
    lo = hi = F(0)
    for c in reversed(p):
        products = [lo*a, lo*b, hi*a, hi*b]
        lo, hi = min(products)+c, max(products)+c
    return lo, hi


def isolate(p):
    seq = sturm(p)
    radius = 2+max((abs(c/p[-1]) for c in p[:-1]), default=F(0))
    todo = [(-radius, radius)]
    roots = []
    while todo:
        a, b = todo.pop()
        count = variations(seq, a)-variations(seq, b)
        if not count:
            continue
        if count == 1:
            roots.append((a, b))
            continue
        # Avoid roots at all interval endpoints.
        m = (a+b)/2
        while not val(p, m):
            m = (a+m)/2
        todo += [(m, b), (a, m)]
    return sorted(roots), seq


def evaluate_reference(l, k, t):
    a, b = 1+4*t*l, 1+2*l+2*t*(l*l+2*k)
    c, d = 1+4*l+6*t*(l*l+2*k), 2*l+2*(l*l+2*k)+12*t*l*k
    f, g = -2*t, -2-12*t*l
    delta, nb, nc = a*d-b*c, f*d-b*g, a*g-f*c
    m = 4*nc*delta-nb*nb
    if not (F(1, 4) <= t <= F(5, 18) and k and l*l > 4*k
            and delta < 0 and m > 0):
        return None
    B, C = nb/delta, nc/delta
    R = mul([1, l, k], [1, l, k])
    Q = [C, B, F(1)]
    P = mul(R, Q)
    output = apply(P, t)
    assert output[:2] == [0, 0]
    H, J = output[2:], apply(R, t)
    K = add(R, scale(deriv(R), 2*t))
    rhs = add(add(mul(Q, J), mul(deriv(Q), K)), scale(R, 2*t))
    assert rhs == output
    roots, seq = isolate(J)
    gcd = sturm(J)[-1]
    common = [J, H]
    while common[-1]:
        rem = divmodp(common[-2], common[-1])[1]
        if not rem:
            break
        common.append(rem)
    if len(common[-1]) > 1:
        return {'parameters': list(map(str, (l, k, t))), 'shared': list(map(str, common[-1]))}
    signs, evidence = [], []
    for a, b in roots:
        for _ in range(200):
            lo, hi = interval_value(H, a, b)
            if lo > 0 or hi < 0:
                break
            mid = (a+b)/2
            while not val(J, mid):
                mid = (a+mid)/2
            if variations(seq, a)-variations(seq, mid):
                b = mid
            else:
                a = mid
        else:
            raise RuntimeError('Sign isolation unresolved; do not infer a sign.')
        signs.append(1 if lo > 0 else -1)
        evidence.append({'interval': list(map(str, (a, b))),
                         'J_endpoint_values': list(map(str, (val(J, a), val(J, b)))),
                         'sturm_variations': [variations(seq, a), variations(seq, b)],
                         'H_interval': list(map(str, (lo, hi)))})
    pattern = any([signs[i], signs[j], signs[h]] == [-1, 1, -1]
                  for i, j, h in combinations(range(len(signs)), 3))
    return {'parameters': {'l': str(l), 'k': str(k), 't': str(t)},
            'collision': dict(zip(['Delta', 'N_B', 'N_C', 'M', 'B', 'C'],
                                  map(str, (delta, nb, nc, m, B, C)))),
            'polynomials_ascending': {name: list(map(str, poly)) for name, poly in
                                     [('R', R), ('Q', Q), ('P', P), ('output', output),
                                      ('H', H), ('J', J), ('K', K)]},
            'J_sturm_chain': [list(map(str, p)) for p in seq],
            'J_squarefree': len(gcd) == 1,
            'J_H_coprime': len(common[-1]) == 1,
            'root_evidence': evidence, 'signs': signs, 'pattern': pattern,
            'checks': {'product_rule_identity': rhs == output,
                       'double_collision': output[:2] == [0, 0],
                       'four_distinct_reference_roots': len(roots) == 4 and len(gcd) == 1}}


def main():
    trials = []
    # Deterministic small rational test, no floating roots or randomness.
    points = [(F(0), -F(1), F(5, 18))]
    points += [(F(l, 2), F(k, 2), t)
               for t in [F(5, 18), F(19, 72), F(1, 4)]
               for l in range(-6, 7) for k in range(-8, 5) if k]
    stopped = None
    for l, k, t in points:
        item = evaluate_reference(l, k, t)
        if item is None:
            continue
        trials.append(item)
        if 'shared' in item or not item['pattern']:
            stopped = len(trials)-1
            break
    # Verify the complete saved interval evidence. Four disjoint strict
    # endpoint sign changes already exhaust a quartic's roots.
    interval_checks = []
    for item in trials:
        if 'shared' in item:
            interval_checks.append(False)
            continue
        polys = {n: list(map(F, p)) for n, p in item['polynomials_ascending'].items()}
        intervals = [tuple(map(F, e['interval'])) for e in item['root_evidence']]
        ok = len(intervals) == 4 and all(a < b for a, b in intervals)
        ok = ok and all(b <= c for (a, b), (c, d) in zip(intervals, intervals[1:]))
        for (a, b), e, s in zip(intervals, item['root_evidence'], item['signs']):
            endpoints = [val(polys['J'], a), val(polys['J'], b)]
            lo, hi = interval_value(polys['H'], a, b)
            ok = ok and endpoints[0]*endpoints[1] < 0
            ok = ok and list(map(str, endpoints)) == e['J_endpoint_values']
            ok = ok and list(map(str, (lo, hi))) == e['H_interval']
            ok = ok and ((lo > 0 and s == 1) or (hi < 0 and s == -1))
        interval_checks.append(ok)
    aggregate = {
        'all_polynomial_checks': all(all(item.get('checks', {}).values())
                                     and bool(item.get('checks')) for item in trials),
        'all_complete_interval_certificates': all(interval_checks),
        'all_tested_patterns': all(item.get('pattern', False) for item in trials),
    }
    failures = [n for n, ok in aggregate.items() if not ok]
    record = {'status': 'BOUNDED_EXACT_REFERENCE_SIGN_TEST',
              'tested_admissible': len(trials), 'stopped_index': stopped,
              'distinct_parameters': len({tuple(item['parameters'].values()) for item in trials
                                          if isinstance(item['parameters'], dict)}),
              'aggregate_checks': aggregate, 'failures': failures,
              'trials': trials,
              'required': 'Every admissible collision must have a negative-positive-negative subsequence at ordered J zeros for the proposed strict sign test.',
              'limitations': 'A failed pattern refutes that sufficient test only, not the sextic target; shared-root cases need separate analysis.'}
    path = Path(__file__).with_suffix('.json')
    path.write_text(json.dumps(record, indent=2)+'\n')
    print('Admissible exact tests:', len(trials), '; stopped index:', stopped)
    if trials:
        last = trials[-1]
        print('Last parameters:', last['parameters'])
        print('Actual signs/shared:', last.get('signs', last.get('shared')))
    print('Required: a negative-positive-negative ordered subsequence.')
    print('Complete interval checks:', sum(interval_checks), '/', len(interval_checks))
    print('Distinct parameters:', record['distinct_parameters'])
    print('Failures:', failures)
    print('Actual: finite exact instances only; no universal outer-threshold bound.')
    print('Full certificate:', path)


if __name__ == '__main__':
    main()
