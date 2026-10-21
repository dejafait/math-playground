"""Selected exact checks of L065's algebra; its uniform proof is analytic.

Save every disjoint-P support, not just projected survivors. No recovery
maximum or original-chart assertion is inferred from these two cases.
"""
from itertools import combinations
from pathlib import Path
import json

MOD = 97
H = tuple(x for x in range(1, MOD) if pow(x, 16, MOD) == 1)


def prod(values):
    out = 1
    for value in values:
        out = out * value % MOD
    return out


def polynomial(roots):
    out = [1]
    for root in roots:
        nxt = [0] * (len(out) + 1)
        for i, value in enumerate(out):
            nxt[i] = (nxt[i] - root * value) % MOD
            nxt[i + 1] = (nxt[i + 1] + value) % MOD
        out = nxt
    return out


def multiply(left, right):
    out = [0] * (len(left) + len(right) - 1)
    for i, x in enumerate(left):
        for j, y in enumerate(right):
            out[i + j] = (out[i + j] + x * y) % MOD
    return out


def evaluate(poly, value):
    out = 0
    for coefficient in reversed(poly):
        out = (out * value + coefficient) % MOD
    return out


def rank(rows):
    mat = [[x % MOD for x in row] for row in rows]
    pivot = 0
    for col in range(len(mat[0])):
        found = next((i for i in range(pivot, len(mat)) if mat[i][col]), None)
        if found is None:
            continue
        mat[pivot], mat[found] = mat[found], mat[pivot]
        scale = pow(mat[pivot][col], -1, MOD)
        mat[pivot] = [x * scale % MOD for x in mat[pivot]]
        for i in range(len(mat)):
            if i != pivot:
                scale = mat[i][col]
                mat[i] = [(x - scale * y) % MOD
                          for x, y in zip(mat[i], mat[pivot])]
        pivot += 1
        if pivot == len(mat):
            break
    return pivot


def check_case(name, shared, pairs):
    singleton = set().union(*map(set, pairs))
    union = singleton | set(shared)
    outside = tuple(h for h in H if h not in union)
    quadratics = [polynomial(pair) for pair in pairs]
    independent = rank(quadratics) == 3
    net = [multiply(quadratics[1], quadratics[2]),
           multiply(quadratics[0], quadratics[2]),
           multiply(quadratics[0], quadratics[1])]
    assert rank(net) == 3
    groups = {}
    for h in outside:
        ratio = evaluate(quadratics[0], h) * pow(
            evaluate(quadratics[1], h), -1, MOD) % MOD
        groups.setdefault(ratio, []).append(h)
    double_fibers = [set(group) for group in groups.values() if len(group) == 2]
    expected_exception = {frozenset(set(pair) | fiber)
                          for pair in pairs for fiber in double_fibers}
    expected_exception |= {frozenset(left | right)
                           for left, right in combinations(double_fibers, 2)}
    counts = {'one_pair': [0, 0, 0], 'no_pair': 0, 'two_pairs': 0}
    rows, no_pair_supports, failures = [], [], []
    for support in combinations((h for h in H if h not in shared), 4):
        support_set = set(support)
        f = polynomial(support)
        sums = [sum(prod(x - h for h in outside) * x
                    * evaluate(f, x) * prod(x - h for h in shared)
                    for x in pair) % MOD for pair in pairs]
        projected = sums[0] == sums[1] == 0
        net_member = rank(net + [f]) == 3
        pair_indices = [i for i, pair in enumerate(pairs)
                        if set(pair) <= support_set]
        complete_pairs = all(len(support_set & set(pair)) in (0, 2) for pair in pairs)
        row_failures = []
        if projected != net_member or (projected and (sums[2] or not complete_pairs)):
            row_failures.append('interpolation_equivalence')
        if projected:
            if len(pair_indices) == 2:
                counts['two_pairs'] += 1
            elif len(pair_indices) == 1:
                counts['one_pair'][pair_indices[0]] += 1
            else:
                counts['no_pair'] += 1
                no_pair_supports.append(support)
        if not independent and len(pair_indices) != 2:
            if projected != (frozenset(support) in expected_exception):
                row_failures.append('exceptional_fiber_classification')
        failures.extend({'K': support, 'failure': failure} for failure in row_failures)
        rows.append({'K': support, 'f': f, 'projected_sums': sums,
                     'net_member': net_member, 'complete_pairs': complete_pairs,
                     'pair_indices': pair_indices, 'failures': row_failures})
    if independent:
        assert counts['no_pair'] <= 2
        assert all(len(set(left) & set(right)) <= 1
                   for left, right in combinations(no_pair_supports, 2))
    assert max(counts['one_pair']) <= 3
    assert len(rows) == 715
    assert not failures
    return {'name': name, 'P': shared, 'pairs': pairs, 'outside': outside,
            'quadratic_rank': rank(quadratics), 'double_fibers': [sorted(x) for x in double_fibers],
            'counts': counts, 'support_rows': rows, 'failures': failures}


def main():
    cases = [check_case('independent', (1, 8, 12),
                        ((18, 22), (27, 33), (47, 50))),
             check_case('dependent', (18, 22, 27),
                        ((1, 96), (8, 89), (12, 85)))]
    assert [case['quadratic_rank'] for case in cases] == [3, 2]
    certificate = {'scope': 'Two selected exact algebra regressions; no uniform computational bound',
                   'support_tests': sum(len(case['support_rows']) for case in cases),
                   'failures': [], 'cases': cases}
    path = Path(__file__).with_name('both-zero-interpolation-check.json')
    path.write_text(json.dumps(certificate, indent=2) + '\n')
    for case in cases:
        fiber_count = len(case['double_fibers'])
        no_pair_bound = (2 if case['quadratic_rank'] == 3
                         else fiber_count * (fiber_count - 1) // 2)
        print(f"{case['name']}: rank={case['quadratic_rank']}; actual={case['counts']}; "
              f"required one-pair<=3 each, no-pair<={no_pair_bound}; "
              f"double fibers={len(case['double_fibers'])}; failures={len(case['failures'])}")
    print(f"Complete support tests={certificate['support_tests']}; required=1430; failures=0; path={path}")


if __name__ == '__main__':
    main()
