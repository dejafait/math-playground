"""One approved new-pair census. No residual feasibility or pair exclusion.

Run from the notebook: python3 scripts/seven-coordinate/new_pair_filter.py
Each completed third is checkpointed before proceeding.
"""
from collections import Counter
from hashlib import sha256
from itertools import combinations, product
from pathlib import Path
import json

import zero_anchor_support_filter as direct

P = 97
HERE = Path(__file__).resolve().parent
OUT = HERE / 'new-pair-filter'
S, H, J, PAIRS = direct.S, direct.H, direct.J, direct.PAIRS
FIRST = [((1, 8), (47, 50)), ((12, 18), (64, 75))]


def eliminate(matrix):
    """Incremental row echelon, original minor, and back-substitution kernel."""
    echelon, rows, insertion, determinant = {}, [], [], 1
    for index, original in enumerate(matrix):
        row = original[:]
        for col in sorted(echelon):
            multiple = row[col]
            if multiple:
                pivot = echelon[col]
                for c in range(col, 21):
                    row[c] = (row[c] - multiple*pivot[c]) % P
        col = next((c for c, value in enumerate(row) if value), None)
        if col is None:
            continue
        determinant = determinant*row[col] % P
        inverse = pow(row[col], -1, P)
        echelon[col] = [value*inverse % P for value in row]
        rows.append(index)
        insertion.append(col)
    columns = sorted(echelon)
    inversions = sum(a > b for a, b in combinations(insertion, 2))
    determinant = determinant * (-1 if inversions % 2 else 1) % P
    assert determinant
    free = sorted(set(range(21))-set(columns))
    basis = []
    for c in free:
        v = [0]*21
        v[c] = 1
        for pivot in reversed(columns):
            v[pivot] = -sum(echelon[pivot][j]*v[j]
                            for j in range(pivot+1, 21)) % P
        basis.append(v)
    residuals = [[sum(a*b for a, b in zip(row, v)) % P
                  for row in matrix] for v in basis]
    assert not any(map(any, residuals))
    return dict(rank=len(columns), minor_rows=rows, pivot_columns=columns,
                minor_residue=determinant, kernel_basis=basis,
                kernel_residuals=residuals)


def witness(basis, columns):
    return next(([n, c, v[c]] for n, v in enumerate(basis)
                 for c in columns if v[c]), None)


def tests(basis, keys):
    factors = []
    for j, (i, k) in enumerate(keys):
        for c in i:
            forbidden = [n for n, (a, b) in enumerate(PAIRS)
                         if c not in (S[a], S[b])]
            w = witness(basis, forbidden)
            factors.append(dict(row=j, coordinate=c, passes=w is None,
                                failure_witness=w))
    activity = []
    for c in S:
        incident = [n for n, (a, b) in enumerate(PAIRS)
                    if c in (S[a], S[b])]
        w = witness(basis, incident)
        activity.append(dict(coordinate=c, passes=w is None,
                             failure_witness=w))
    return factors, activity


def gate(i, k, c):
    b = direct.block(i, k)
    h = [int(x == c) for x in S]
    lam = h[S.index(b['pivot'])]*pow(direct.g(k, b['pivot']), -1, P) % P
    error = [(h[S.index(x)]-lam*direct.g(k, x)) % P for x in i]
    error += [-lam*direct.g(k, x) % P for x in k]
    projection = [sum(a*v for a, v in zip(row, h)) % P for row in b['covectors']]
    moments = [(sum(h[S.index(x)]*pow(x, d, P) for x in S)
                -sum(v*pow(x, d, P) for x, v in zip(i+k, error))) % P
               for d in range(1, 9)]
    assert not any(projection) and lam == 0 and not any(moments)
    assert error == [int(x == c) for x in i+k]
    return dict(coordinate=c, pivot=b['pivot'], g_pivot=direct.g(k, b['pivot']),
                projection=projection, lambda_value=lam, error=error,
                moment_residuals=moments)


def run():
    OUT.mkdir(exist_ok=True)
    universe = list(product(combinations(S, 2), combinations(J, 2)))
    support = [set(i+k) for i, k in universe]
    first_indices = [universe.index(k) for k in FIRST]
    assert len(universe) == len(set(universe)) == 756
    assert not support[first_indices[0]] & support[first_indices[1]]
    blocks = [direct.block(*key) for key in universe]
    gates = [[gate(*key, c) for c in key[0]] for key in universe]
    thirds, third_screen = [], []
    for u, a in enumerate(support):
        intersections = [len(a & support[j]) for j in first_indices]
        eligible = u not in first_indices and max(intersections) <= 1
        third_screen.append(dict(index=u, intersections=intersections,
                                 distinct=u not in first_indices, eligible=eligible))
        if eligible:
            thirds.append(u)
    counts, statuses = Counter(), Counter()
    summaries, residuals = [], []
    factor_occ = omission_occ = factor_tests = omission_tests = vectors = 0
    for n, c_index in enumerate(thirds):
        seed_indices = first_indices+[c_index]
        seed = [support[u] for u in seed_indices]
        stack = [row for u in seed_indices for row in blocks[u]['matrix']]
        screen, records = [], []
        local_ranks, local_status = Counter(), Counter()
        residual_indices = []
        for d_index, a in enumerate(support):
            intersections = [len(a & b) for b in seed]
            distinct = d_index not in seed_indices
            eligible = distinct and max(intersections) <= 1
            screen.append(dict(index=d_index, intersections=intersections,
                               distinct=distinct, eligible=eligible))
            if not eligible:
                continue
            matrix = stack+blocks[d_index]['matrix']
            record = dict(fourth_index=d_index, **eliminate(matrix))
            basis = record['kernel_basis']
            if record['rank'] == 21:
                record.update(factor_tests=[], omission_tests=[], status='rank')
            else:
                factors, omissions = tests(basis, FIRST+[universe[c_index], universe[d_index]])
                fp = any(t['passes'] for t in factors)
                op = any(t['passes'] for t in omissions)
                factor_occ += fp
                omission_occ += op
                factor_tests += sum(t['passes'] for t in factors)
                omission_tests += sum(t['passes'] for t in omissions)
                record.update(factor_tests=factors, omission_tests=omissions,
                              status='factor' if fp else 'omission' if op else 'residual')
            vectors += len(basis)
            if record['status'] == 'residual':
                residuals.append([c_index, d_index])
                residual_indices.append(d_index)
            counts[record['rank']] += 1
            local_ranks[record['rank']] += 1
            statuses[record['status']] += 1
            local_status[record['status']] += 1
            records.append(record)
        shard = dict(third_index=c_index, fourth_screen=screen, cases=records,
                     residual_indices=residual_indices, failures=[])
        data = (json.dumps(shard, separators=(',', ':'))+'\n').encode()
        path = OUT/f'third-{c_index:03d}.json'
        path.write_bytes(data)
        summaries.append(dict(third_index=c_index, certificate=str(path.relative_to(HERE)),
                              sha256=sha256(data).hexdigest(), cases=len(records),
                              ranks=dict(sorted(local_ranks.items())),
                              statuses=dict(sorted(local_status.items()))))
        if (n+1) % 25 == 0 or n+1 == len(thirds):
            print(f'Thirds {n+1}/{len(thirds)}; ordered cases {sum(counts.values())}; '
                  f'residuals {len(residuals)}; failures 0', flush=True)
    required = sum(1 for c in thirds for d in thirds if c != d
                   and len(support[c] & support[d]) <= 1)
    assert sum(counts.values()) == required
    summary = dict(actual_thirds=len(thirds), actual_cases=sum(counts.values()),
                   required_cases=required, rank_histogram=dict(sorted(counts.items())),
                   statuses=dict(sorted(statuses.items())),
                   factor_passing_occurrences=factor_occ, omission_passing_occurrences=omission_occ,
                   factor_passing_tests=factor_tests, omission_passing_tests=omission_tests,
                   complete_kernel_vectors=vectors, original_residual_entries=24*vectors,
                   residual_thirds=len(set(c for c, d in residuals)),
                   required_exclusion_rank=21)
    master = dict(modulus=P, H=H, S=S, J=J, first_two=FIRST, first_indices=first_indices,
                  universe=universe, column_pairs=[[S[a], S[b]] for a, b in PAIRS],
                  blocks=blocks, factor_gate_coefficients=gates,
                  third_screen=third_screen, third_indices=thirds, thirds=summaries,
                  summary=summary, residual_occurrences=residuals, failures=[],
                  scope='ordered sufficient-filter partition only; residuals are not feasible planes',
                  code_sha256=sha256(Path(__file__).read_bytes()).hexdigest(),
                  direct_helper_sha256=sha256(Path(direct.__file__).read_bytes()).hexdigest())
    path = HERE/'new-pair-filter.json'
    path.write_text(json.dumps(master, indent=2)+'\n')
    print(json.dumps(summary, sort_keys=True))
    print(f'Failures: 0; certificate {path}; complete shards {OUT}', flush=True)


if __name__ == '__main__':
    run()
