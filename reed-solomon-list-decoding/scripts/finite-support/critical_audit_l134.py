"""Independent exhaustive replay of L134; production inputs remain read-only.

Reconstruct the prescribed maps; enumerate u,v,w with Horner evaluation;
use integer generating polynomials for full image laws, then check all
binomial moments. No production module is imported and no rank is redone.
"""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import comb, prod
from pathlib import Path
import hashlib
import json

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
OUTPUT = HERE / 'l134-critical-audit.json'
checks = []


def equal(name, actual, required):
    actual = json.loads(json.dumps(actual))
    required = json.loads(json.dumps(required))
    checks.append(dict(name=name, actual=actual, required=required,
                       passed=actual == required))


def choose(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def rational(value):
    return dict(numerator=value.numerator, denominator=value.denominator)


def rows(counts):
    return [dict(type=list(key), count=value)
            for key, value in sorted(counts.items())]


def sig(x, pair):
    return 2 * (x in pair[0]) + (x in pair[1])


def polynomial_law(m, n, sizes):
    # Integer generating polynomials count all choices of the image subsets.
    coefficients = [1]
    denominator = 1
    for size, hits, selected in zip(sizes, m, n):
        denominator *= comb(size, selected)
        factor = [choose(hits, j) * choose(size-hits, selected-j)
                  for j in range(selected+1)]
        coefficients = [sum(coefficients[a] * factor[j-a]
                            for a in range(len(coefficients))
                            if 0 <= j-a < len(factor))
                        for j in range(len(coefficients)+selected)]
    return [Fraction(c, denominator) for c in coefficients]


def subset_moment(m, n, sizes, order):
    # Independently count distinguished subsets of an intersection.
    total = Fraction(0)
    for ks in product(*(range(min(x, y)+1) for x, y in zip(m, n))):
        if sum(ks) == order:
            total += prod((Fraction(comb(x, k)*comb(y, k), comb(s, k))
                           for s, x, y, k in zip(sizes, m, n, ks)),
                          start=Fraction(1))
    return total


def main():
    filenames = ['signature-alteration.json', 'signature_alteration.py',
                 'mixed-core-l031-embedding.json', 'l131-critical-audit.json']
    raw = {name: (HERE / name).read_bytes() for name in filenames}
    hashes = {name: hashlib.sha256(value).hexdigest()
              for name, value in raw.items()}
    saved = json.loads(raw[filenames[0]])
    embedding = json.loads(raw[filenames[2]])
    old_audit = json.loads(raw[filenames[3]])
    q, ts, prime, generator = 137, [16, 64, 70, 102, 112, 118, 121], 65537, 19139
    threshold, sizes = 1532496, [949, 6, 6, 1]
    h, point = [], 1
    for _ in range(1024):
        h.append(point)
        point = point * generator % prime
    equal('subgroup recurrence closes', point, 1)
    equal('subgroup has 1024 distinct labels', len(set(h)), 1024)
    a, b, core = h[0], h[10], set(h[12:72])
    cores = [core | {a}, core | {b}]
    edges = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
    pairs = [set(h[2*j:2*j+2]) for j in range(6)]
    supports = [core | set(h[72+2*i:74+2*i]) |
                set().union(*(pair for edge, pair in zip(edges, pairs) if i in edge))
                for i in range(4)]
    exponent = {x: j for j, x in enumerate(h)}
    equal('all actual supports', embedding['supports'],
          [sorted(s, key=exponent.get) for s in supports])
    equal('actual cores', embedding['cores'],
          [sorted(c, key=exponent.get) for c in cores])
    equal('actual distinguished labels', [embedding['a'], embedding['b']], [a, b])
    equal('entire subgroup in embedding', embedding['domain'], h)
    equal('embedding parameters', embedding['parameters'],
          dict(P=prime, generator=generator, q=q, T=ts))
    equal('embedding failures', embedding['failures'], [])
    equal('accepted L131 audit failures', old_audit['failures'], [])
    equal('accepted L131 audit links the current embedding',
          old_audit['input_hashes']['mixed-core-l031-embedding.json'], hashes[filenames[2]])
    equal('L134 source path and byte hash', saved['source'],
          dict(path='scripts/finite-support/mixed-core-l031-embedding.json',
               sha256=hashes[filenames[2]]))
    equal('L134 parameters', saved['parameters'],
          dict(q=q, T=ts, part_sizes=sizes, threshold=threshold))

    labels = [('g', t, y) for t in ts for y in range(q)]
    labels += [('d', i) for i in range(4)]
    planted_blocks = [{('g', t, 0) for t in ts},
                      {('g', t, (t-16) % q) for t in ts}]
    maps = []
    for side, vertices, fixed, value in [(0, (0, 1), ('g', 16, 1), b),
                                         (1, (2, 3), ('d', 0), a)]:
        residuals = [supports[i] - cores[side] for i in vertices]
        target_order = [x for x in h if x not in cores[side]]
        mapping = {fixed: value}
        domain_parts, target_parts = [], []
        for bit in range(4):
            source = [x for x in labels if x != fixed and sig(x, planted_blocks) == bit]
            target = [x for x in target_order if x != value and sig(x, residuals) == bit]
            domain_parts.append(len(source))
            target_parts.append(len(target))
            mapping.update(zip(source, target))
        equal(f'side {side} remaining part capacities', [domain_parts, target_parts],
              [sizes, sizes])
        equal(f'side {side} complete bijection',
              [len(mapping), len(set(mapping.values())), set(mapping.values()) == set(target_order)],
              [963, 963, True])
        expected_map = [dict(label=list(x), image=mapping[x], exponent=exponent[mapping[x]])
                        for x in labels]
        equal(f'side {side} every ordered map entry', embedding['sides'][side]['map'], expected_map)
        for j, index in enumerate(vertices):
            equal(f'side {side} planted support {j}',
                  sorted(cores[side] | {mapping[x] for x in planted_blocks[j]}),
                  sorted(supports[index]))
        maps.append(mapping)
    equal('right inverse image of a is only d0',
          [list(x) for x in labels if maps[1][x] == a], [['d', 0]])
    equal('all four supports have size 68', [len(s) for s in supports], [68]*4)
    equal('all six protected pair intersections',
          [len(supports[i] & supports[j]) for i, j in edges], [62]*6)
    Y = set(h) - core - {a, b}
    right_residuals = [supports[i] - cores[1] for i in (2, 3)]
    equal('Y size and target signature sizes',
          [len(Y), [sum(sig(x, right_residuals) == j for x in Y) for j in range(4)]],
          [962, sizes])
    equal('right remaining domain signature sizes',
          [sum(sig(x, planted_blocks) == j for x in labels if x != ('d', 0))
           for j in range(4)], sizes)

    # Deliberately change the production loop order and evaluation formula.
    # Keep every layer, including absent losses and zero/lower degrees.
    layers_left = [Counter() for _ in range(q)]
    layers_right = [Counter() for _ in range(q)]
    layers_loss = [Counter() for _ in range(q)]
    eligible, planted = 0, {}
    signature_tables = [[sig(maps[0][('g', t, y)], right_residuals)
                         for y in range(q)] for t in ts]
    max_protected_hits = [0, 0]
    for u in range(q):
        for v in range(q):
            # Horner's rule evaluated for every quadratic coefficient.
            for w in range(q):
                values = [((w*t+v)*t+u) % q for t in ts]
                hits = Counter(2*(y == 0) + (y == (t-16) % q)
                               for t, y in zip(ts, values))
                n = tuple(hits[j] for j in range(4))
                layers_right[w][n] += 1
                if (256*w+16*v+u) % q == 1:
                    continue
                eligible += 1
                hits = Counter(signature_tables[j][y] for j, y in enumerate(values))
                m = tuple(hits[j] for j in range(4))
                hit3, hit4 = m[2]+m[3], m[1]+m[3]
                max_protected_hits[0] = max(max_protected_hits[0], hit3)
                max_protected_hits[1] = max(max_protected_hits[1], hit4)
                loss = (int(hit3 > 3), int(hit4 > 3))
                if any(loss):
                    layers_loss[w][loss] += 1
                else:
                    layers_left[w][m] += 1
                if (u, v, w) in [(0, 0, 0), (121, 1, 0)]:
                    index = 0 if v == 0 else 1
                    image = {maps[0][('g', t, y)] for t, y in zip(ts, values)}
                    planted['p' if index == 0 else 'r'] = dict(
                        coefficients=[u, v, w], occupancy=list(m),
                        right_domain_occupancy=list(n), left_deleted=any(loss),
                        cross_intersections=[len((cores[0] | image) & supports[j])
                                             for j in (2, 3)],
                        matches_left_support=cores[0] | image == supports[index])
        if u in (0, 68, 136):
            print(json.dumps(dict(stage='complete coefficient slices',
                                  constant_coefficients_done=u+1, required=137)), flush=True)
    left, right, loss = Counter(), Counter(), Counter()
    layers = []
    for w in range(q):
        layer = dict(w=w, left=rows(layers_left[w]), right=rows(layers_right[w]),
                     removed=rows(layers_loss[w]))
        equal(f'complete coefficient layer w={w}', saved['enumeration']['layers'][w], layer)
        layers.append(layer)
        left.update(layers_left[w])
        right.update(layers_right[w])
        loss.update(layers_loss[w])
    enumeration = dict(order='w,v,u; f=u+vZ+wZ^2', layers=layers,
                       eligible_left=eligible, removed=rows(loss),
                       left=rows(left), right=rows(right), planted=planted)
    equal('all enumeration fields and number of layers', saved['enumeration'], enumeration)
    equal('all coefficients and eligibility', [sum(right.values()), eligible], [q**3, q**3-q**2])
    equal('no eligible left conflicts with either protected right support',
          [sum(loss.values()), max_protected_hits], [0, [3, 3]])
    equal('exact numbers of occupancy types', [len(left), len(right)], [17, 14])

    probability_rows, right_types = [], []
    expectation = Fraction(0)
    moment_checks = []
    for n, nr in sorted(right.items()):
        degree = Fraction(0)
        for m, nl in sorted(left.items()):
            law = polynomial_law(m, n, sizes)
            moments = [subset_moment(m, n, sizes, k) for k in range(8)]
            from_law = [sum((comb(j, k)*law[j] for j in range(k, 8)), Fraction(0))
                        for k in range(8)]
            tail = sum(law[4:])
            alternate = sum(((-1)**(k-4)*comb(k-1, 3)*moments[k]
                             for k in range(4, 8)), Fraction(0))
            row = dict(left=list(m), right=list(n), left_count=nl, right_count=nr,
                       law=[rational(x) for x in law], tail=rational(tail),
                       alternate_tail=rational(alternate),
                       contribution=rational(nl*nr*tail))
            i = len(probability_rows)
            equal(f'full probability row {i}', saved['probabilities'][i], row)
            equal(f'normalization positivity moments and tail row {i}',
                  [len(law), sum(law) == 1, all(x >= 0 for x in law),
                   from_law == moments, alternate == tail], [8, True, True, True, True])
            moment_checks.append(dict(left=list(m), right=list(n),
                                      subset_moments=[rational(x) for x in moments],
                                      law_moments=[rational(x) for x in from_law]))
            probability_rows.append(row)
            expectation += nl*nr*tail
            degree += nl*tail
        right_types.append(dict(occupancy=list(n), count=nr, expected_degree=rational(degree)))
    equal('every probability row and no extra rows', saved['probabilities'], probability_rows)
    equal('all right conditional degrees', saved['right_types'], right_types)
    protected_degrees = [row['expected_degree'] for row in right_types
                         if row['occupancy'] in [planted[x]['right_domain_occupancy']
                                                 for x in ('p', 'r')]]
    equal('two protected right degree-zero types', protected_degrees,
          [rational(Fraction(0))]*2)
    # Check the finite identity on the entire support, not just in expectation.
    equal('indicator identity for every J=0,...,7',
          [sum((-1)**(k-4)*comb(k-1, 3)*choose(j, k) for k in range(4, 8))
           for j in range(8)], [0]*4+[1]*4)
    floor = expectation.numerator // expectation.denominator
    result = dict(left_size=sum(left.values()), deterministic_left_loss=sum(loss.values()),
                  left_initial_budget=eligible-threshold,
                  left_remaining_budget=sum(left.values())-threshold,
                  expected_edges=rational(expectation), edge_floor=floor,
                  right_budget=q**3-threshold, right_size_bound=q**3-floor,
                  right_margin=q**3-floor-threshold,
                  sufficient_test_passed=sum(left.values()) >= threshold and q**3-floor >= threshold)
    equal('every exact result and budget', saved['result'], result)
    equal('stated exact expectation', rational(expectation),
          dict(numerator=953535880348964195654027, denominator=4237514312360044716))
    equal('stated floor and retained sizes', [floor, result['left_size'], result['right_size_bound']],
          [225022, 2552584, 2346331])
    equal('strict integer rounding', floor < expectation < floor+1, True)
    equal('budget test', [floor <= result['right_budget'],
                         result['left_size'] >= threshold,
                         result['right_size_bound'] >= threshold], [True]*3)
    equal('production check names and count',
          [len(saved['checks']), len({c['name'] for c in saved['checks']})], [18, 18])
    # Reconstruct all production check values instead of trusting their flags.
    values = [[], [q, ts], sizes, sorted(maps[0].values()), b, sizes, eligible,
              sum(left.values())+sum(loss.values()), sum(right.values()), ['p', 'r'],
              [planted[x]['left_deleted'] for x in ('p', 'r')],
              [planted[x]['matches_left_support'] for x in ('p', 'r')],
              [planted[x]['cross_intersections'] for x in ('p', 'r')],
              [], len(probability_rows), True, rational(Fraction(0)), rational(Fraction(0))]
    for record, actual in zip(saved['checks'], values):
        equal('production check replay '+record['name'],
              [record['actual'], record['required'], record['passed']], [actual, actual, True])
    equal('production failures', saved['failures'], [])
    equal('original certificate limitations preserved', saved['limitations'],
          ['not a sampled or explicit favorable map', 'separate critical audit pending',
           'no RS realization or universal forcing conclusion'])
    for name in filenames:
        equal('input remains byte-identical '+name, (HERE / name).read_bytes() == raw[name], True)
    failures = [c['name'] for c in checks if not c['passed']]
    certificate = dict(input_hashes=hashes, enumeration=enumeration,
                       probabilities=probability_rows, right_types=right_types,
                       binomial_moment_checks=moment_checks, result=result,
                       protected_intersection_maxima=max_protected_hits,
                       map_entries_checked=1926, rank_recomputed=False,
                       checks=checks, failures=failures)
    OUTPUT.write_text(json.dumps(certificate, indent=2)+'\n')
    print(json.dumps(dict(outcome='PASS' if not failures else 'FAIL', checks=len(checks),
                          coefficient_triples=sum(right.values()), required_triples=q**3,
                          layers=len(layers), required_layers=q,
                          probability_rows=len(probability_rows), required_probability_rows=238,
                          result=result, failures=failures,
                          certificate=str(OUTPUT.relative_to(ROOT)))))
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
