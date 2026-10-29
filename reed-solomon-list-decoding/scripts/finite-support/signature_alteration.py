"""Exact occupancy histograms and protected first-moment alteration budget.

Read-only input: audited L131 embedding. Enumerate every coefficient triple.
Write all occupancy/loss/expectation rows, not a sampled-map certificate.
"""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import comb
from pathlib import Path
import hashlib
import json

HERE = Path(__file__).resolve().parent
SOURCE = HERE / 'mixed-core-l031-embedding.json'
OUTPUT = HERE / 'signature-alteration.json'
Q = 137
T = (16, 64, 70, 102, 112, 118, 121)
N = Q**3
THRESHOLD = 1532496
SIZES = (949, 6, 6, 1)  # signatures 00,01,10,11, with d_0,a removed


def signature(x, first, second):
    return 2 * int(x in first) + int(x in second)


def choose(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def intersection_law(m, n):
    law = [Fraction(1)]
    for size, a, b in zip(SIZES, m, n):
        local = [Fraction(choose(a, j) * choose(size-a, b-j),
                          choose(size, b)) for j in range(b+1)]
        new = [Fraction(0)] * (len(law)+b)
        for j, x in enumerate(law):
            for k, y in enumerate(local):
                new[j+k] += x*y
        law = new
    assert sum(law) == 1 and len(law) == 8
    return law


def frac(x):
    return dict(numerator=x.numerator, denominator=x.denominator)


def tail_by_moments(m, n):
    # Independent inclusion-exclusion identity:
    # 1_{J>=4}=sum_{k=4}^7 (-1)^(k-4) C(k-1,3) C(J,k).
    moments = [Fraction(1)]
    for size, a, b in zip(SIZES, m, n):
        local = [Fraction(choose(a,k)*choose(b,k), choose(size,k))
                 for k in range(min(a,b)+1)]
        new = [Fraction(0)] * (len(moments)+len(local)-1)
        for j,x in enumerate(moments):
            for k,y in enumerate(local):
                new[j+k] += x*y
        moments = new
    return sum(((-1)**(k-4)*comb(k-1,3)*moments[k]
                for k in range(4,len(moments))), Fraction(0))


def main():
    raw = SOURCE.read_bytes()
    source = json.loads(raw)
    checks = []

    def check(name, actual, required):
        checks.append(dict(name=name, actual=actual, required=required,
                           passed=actual == required))

    check('input failures', source['failures'], [])
    check('auxiliary parameters', [source['parameters']['q'],
                                 source['parameters']['T']], [Q, list(T)])
    supports = [set(s) for s in source['supports']]
    cores = [set(c) for c in source['cores']]
    a, b = source['a'], source['b']
    R3, R4 = (supports[i] - cores[1] for i in (2, 3))
    Y = set(source['domain']) - (cores[0] | cores[1])
    check('target part sizes',
          [sum(signature(x, R3, R4) == s for x in Y) for s in range(4)],
          list(SIZES))
    mapping = {tuple(row['label']): row['image']
               for row in source['sides'][0]['map']}
    check('left bijection', sorted(mapping.values()),
          sorted(set(source['domain']) - cores[0]))
    check('left distinguished image', mapping[('g', 16, 1)], b)
    lookup = [[signature(mapping[('g', t, y)], R3, R4)
               for y in range(Q)] for t in T]
    # Domain classes relative to B_0,B_(Z-16), independent of right map.
    domain_lookup = [[2*int(y == 0)+int(y == (t-16) % Q)
                      for y in range(Q)] for t in T]
    check('remaining domain class sizes',
          [sum(row.count(s) for row in domain_lookup) + (3 if s == 0 else 0)
           for s in range(4)], list(SIZES))
    left = Counter()
    right = Counter()
    removed = Counter()
    eligible = 0
    planted = {}
    # Full histograms by quadratic coefficient permit bounded exact replay.
    layers = []
    for w in range(Q):
        layer_left, layer_right, layer_loss = Counter(), Counter(), Counter()
        for v in range(Q):
            base = [(w*t*t+v*t) % Q for t in T]
            for u in range(Q):
                ys = [(u+x) % Q for x in base]
                n = [0]*4
                for i, y in enumerate(ys):
                    n[domain_lookup[i][y]] += 1
                layer_right[tuple(n)] += 1
                if ys[0] == 1:
                    continue
                eligible += 1
                m = [0]*4
                for i, y in enumerate(ys):
                    m[lookup[i][y]] += 1
                hit3, hit4 = m[2]+m[3], m[1]+m[3]
                loss = (int(hit3 >= 4), int(hit4 >= 4))
                if any(loss):
                    layer_loss[loss] += 1
                else:
                    layer_left[tuple(m)] += 1
                if (w, v, u) in ((0, 0, 0), (0, 1, Q-16)):
                    U = {mapping[('g', t, y)] for t, y in zip(T, ys)}
                    planted['p' if v == 0 else 'r'] = dict(
                        coefficients=[u, v, w], occupancy=m,
                        right_domain_occupancy=n, left_deleted=any(loss),
                        cross_intersections=[60+hit3, 60+hit4],
                        matches_left_support=cores[0] | U == supports[v])
        left.update(layer_left)
        right.update(layer_right)
        removed.update(layer_loss)
        layers.append(dict(w=w, left=rows(layer_left), right=rows(layer_right),
                           removed=rows(layer_loss)))
    L = sum(left.values())
    D = sum(removed.values())
    check('eligible left count', eligible, N-Q**2)
    check('left partition', L+D, eligible)
    check('right polynomial count', sum(right.values()), N)
    check('protected p and r', sorted(planted), ['p', 'r'])
    check('planted left survival', [x['left_deleted'] for x in planted.values()],
          [False, False])
    check('planted left support identities',
          [x['matches_left_support'] for x in planted.values()], [True, True])
    check('planted full cross intersections',
          [x['cross_intersections'] for x in planted.values()], [[62,62],[62,62]])
    expectation = Fraction(0)
    expectation_rows = []
    right_types = []
    probability_mismatches = []
    for n, count_n in sorted(right.items()):
        conditional = Fraction(0)
        for m, count_m in sorted(left.items()):
            law = intersection_law(m, n)
            tail = sum(law[4:])
            alternate_tail = tail_by_moments(m,n)
            if tail != alternate_tail:
                probability_mismatches.append([list(m),list(n)])
            contribution = count_m * count_n * tail
            expectation += contribution
            conditional += count_m * tail
            expectation_rows.append(dict(left=list(m), right=list(n),
                left_count=count_m, right_count=count_n,
                law=[frac(x) for x in law], tail=frac(tail),
                alternate_tail=frac(alternate_tail),
                contribution=frac(contribution)))
        right_types.append(dict(occupancy=list(n), count=count_n,
                               expected_degree=frac(conditional)))
    floor = expectation.numerator // expectation.denominator
    check('all independent moment tail comparisons', probability_mismatches, [])
    check('number of probability rows',len(expectation_rows),len(left)*len(right))
    check('exact floor remainder bounds',
          0 <= expectation.numerator-floor*expectation.denominator
          < expectation.denominator, True)
    for label in ('p', 'r'):
        n = tuple(planted[label]['right_domain_occupancy'])
        check('protected right '+label+' expected degree',
              frac(sum(c*sum(intersection_law(m,n)[4:]) for m,c in left.items())),
              frac(Fraction(0)))
    failures = [x['name'] for x in checks if not x['passed']]
    cert = dict(parameters=dict(q=Q,T=list(T),part_sizes=list(SIZES),
                               threshold=THRESHOLD),
        source=dict(path=str(SOURCE.relative_to(HERE.parent.parent)),
                    sha256=hashlib.sha256(raw).hexdigest()),
        enumeration=dict(order='w,v,u; f=u+vZ+wZ^2',layers=layers,
                         eligible_left=eligible, removed=rows(removed),
                         left=rows(left),right=rows(right),planted=planted),
        probabilities=expectation_rows, right_types=right_types,
        result=dict(left_size=L, deterministic_left_loss=D,
                    left_initial_budget=eligible-THRESHOLD,
                    left_remaining_budget=L-THRESHOLD,
                    expected_edges=frac(expectation), edge_floor=floor,
                    right_budget=N-THRESHOLD, right_size_bound=N-floor,
                    right_margin=N-floor-THRESHOLD,
                    sufficient_test_passed=(L>=THRESHOLD and N-floor>=THRESHOLD)),
        checks=checks,failures=failures,
        limitations=['not a sampled or explicit favorable map',
                     'separate critical audit pending',
                     'no RS realization or universal forcing conclusion'])
    OUTPUT.write_text(json.dumps(cert,indent=2)+'\n')
    print(json.dumps(dict(checks=len(checks),failures=failures,
        left_types=len(left),right_types=len(right),result=cert['result'],
        certificate=str(OUTPUT.relative_to(HERE.parent.parent)))))
    if failures:
        raise SystemExit(1)


def rows(counter):
    return [dict(type=list(k),count=v) for k,v in sorted(counter.items())]


if __name__ == '__main__':
    main()
