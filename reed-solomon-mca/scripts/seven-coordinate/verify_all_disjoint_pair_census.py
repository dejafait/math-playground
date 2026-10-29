"""Complete independent replay; imports no producer or elimination helper.

Polynomial/Horner ratio blocks, full Gauss-Jordan kernels, transposed
minor determinants, and ordered-complement pair indexing are independent
of the producer paths. Shared Python and F_97 arithmetic remain.
"""
from collections import Counter
from hashlib import sha256
from itertools import combinations
from math import comb
from pathlib import Path
import json

P = 97
HERE = Path(__file__).resolve().parent
SOURCE = HERE / 'all-disjoint-pair-census.json'
OUT = HERE / 'all-disjoint-pair-census-replay'


def encoded(value):
    return json.dumps(value, separators=(',', ':')).encode()


def polynomial(roots):
    out = [1]
    for root in roots:
        new = [0] * (len(out) + 1)
        for d, v in enumerate(out):
            new[d] = (new[d] - root * v) % P
            new[d + 1] = (new[d + 1] + v) % P
        out = new
    return out


def evaluate(coeff, x):
    out = 0
    for v in reversed(coeff):
        out = (out * x + v) % P
    return out


def rref_kernel(matrix):
    a = [row[:] for row in matrix]
    pivots = []
    for c in range(21):
        start = len(pivots)
        pivot = next((r for r in range(start, len(a)) if a[r][c]), None)
        if pivot is None:
            continue
        a[start], a[pivot] = a[pivot], a[start]
        inverse = pow(a[start][c], -1, P)
        a[start] = [v * inverse % P for v in a[start]]
        for r in range(len(a)):
            if r != start and a[r][c]:
                scale = a[r][c]
                a[r] = [(v - scale * w) % P for v, w in zip(a[r], a[start])]
        pivots.append(c)
    free = [c for c in range(21) if c not in pivots]
    basis = []
    for c in free:
        v = [0] * 21
        v[c] = 1
        for r, pivot in enumerate(pivots):
            v[pivot] = -a[r][c] % P
        basis.append(v)
    return pivots, basis


def minor_determinant(matrix):
    # Transpose, then column-oriented elimination on the original minor.
    a = [list(row) for row in zip(*matrix)]
    out = 1
    for c in range(len(a)):
        pivot = next((r for r in range(c, len(a)) if a[r][c]), None)
        if pivot is None:
            return 0
        if pivot != c:
            a[c], a[pivot] = a[pivot], a[c]
            out = -out
        value = a[c][c]
        out = out * value % P
        inverse = pow(value, -1, P)
        for r in range(c + 1, len(a)):
            scale = a[r][c] * inverse % P
            if scale:
                for j in range(c + 1, len(a)):
                    a[r][j] = (a[r][j] - scale * a[c][j]) % P
                a[r][c] = 0
    return out % P


def run():
    OUT.mkdir(exist_ok=True)
    raw = SOURCE.read_bytes()
    saved = json.loads(raw)
    failures = []
    check_count = 0

    def check(label, actual, required):
        nonlocal check_count
        check_count += 1
        if actual != required:
            failures.append(dict(check=label, actual=actual, required=required))

    h = sorted({pow(8, d, P) for d in range(16)})
    s = [1, 8, 12, 18, 22, 27, 33]
    jset = sorted(set(h) - set(s))
    columns = list(combinations(s, 2))
    # Independently form four-sets first, then split and sort by (I,K).
    universe = sorted((tuple(x for x in a if x in s),
                       tuple(x for x in a if x not in s))
                      for a in combinations(h, 4) if len(set(a) & set(s)) == 2)
    positions = {key: n for n, key in enumerate(universe)}
    ordered = []
    for a, (i, k) in enumerate(universe):
        for ii in combinations(sorted(set(s) - set(i)), 2):
            for kk in combinations(sorted(set(jset) - set(k)), 2):
                ordered.append((a, positions[(ii, kk)]))
    required_pairs = sorted({tuple(sorted(pair)) for pair in ordered})
    # Choose four labels in each part, one of 3 unordered S partitions,
    # and one of 6 allocations of the four J labels to these two S pairs.
    independent_count = comb(7, 4) * comb(9, 4) * 3 * 6
    check('subgroup generator half power', pow(8, 8, P), 96)
    check('subgroup cardinality', len(h), 16)
    for key, actual in [('modulus', P), ('H', h), ('S', s), ('J', jset),
                        ('column_pairs', [list(c) for c in columns]),
                        ('universe', [[list(i), list(k)] for i, k in universe])]:
        check(key, saved[key], actual)
    check('ordered pairs unique', len(set(ordered)), len(ordered))
    check('both orders exactly once', len(ordered), 2 * len(required_pairs))
    check('independent count', len(required_pairs), independent_count)
    reconstructed, ratios, block_evidence = [], [], []
    for index, (i, k) in enumerate(universe):
        coeff = polynomial(sorted(set(jset) - set(k)))
        values = {x: evaluate(coeff, x) for x in h}
        check(f'block {index} exact roots', [x for x in h if not values[x]],
              sorted(set(jset) - set(k)))
        observed = sorted(set(s) - set(i))
        z = observed[0]
        d = {x: [((pow(values[x], -1, P) if t == x else 0)
                  - (pow(values[z], -1, P) if t == z else 0)) % P for t in s]
             for x in observed[1:]}
        covectors = [[v * values[z] * values[x] % P for v in d[x]]
                     for x in observed[1:]]
        ratio, matrix, scales = [], [], []
        for x, y in combinations(observed[1:], 2):
            row = [(d[x][s.index(a)] * d[y][s.index(b)]
                    - d[x][s.index(b)] * d[y][s.index(a)]) % P for a, b in columns]
            scale = values[z] ** 2 * values[x] * values[y] % P
            scales.append(scale)
            ratio.append(row)
            matrix.append([v * scale % P for v in row])
        check(f'block {index} nonzero scales', all(scales), True)
        check(f'block {index} all original fields', saved['blocks'][index],
              dict(I=list(i), K=list(k), pivot=z, covectors=covectors, matrix=matrix))
        check(f'block {index} rank', len(rref_kernel(ratio)[0]), 6)
        reconstructed.append(matrix)
        ratios.append(ratio)
        block_evidence.append(dict(index=index, polynomial=coeff, values=values,
                                   pivot=z, scales=scales, ratio_matrix=ratio))

    seen, batches, ranks = [], [], Counter()
    vectors = original_entries = ratio_entries = 0
    binding_records = {}
    for batch_number, batch in enumerate(saved['batches']):
        path = HERE / batch['path']
        batch_raw = path.read_bytes()
        check(f'batch {batch_number} sha256', sha256(batch_raw).hexdigest(), batch['sha256'])
        data = json.loads(batch_raw)
        local, records = Counter(), []
        check(f'batch {batch_number} count', len(data['records']), batch['count'])
        check(f'batch {batch_number} grouping', data['overlap_pairs'], batch['overlap_pairs'])
        for record in data['records']:
            a, b = record['pair']
            name = f'pair {a},{b}'
            seen.append((a, b))
            check(name + ' grouping', [list(universe[a][0]), list(universe[b][0])],
                  data['overlap_pairs'])
            check(name + ' disjoint', set(sum(universe[a], ())).isdisjoint(
                set(sum(universe[b], ()))), True)
            original = reconstructed[a] + reconstructed[b]
            quotient = ratios[a] + ratios[b]
            pivots, basis = rref_kernel(quotient)
            rank = len(pivots)
            free = [c for c in range(21) if c not in pivots]
            check(name + ' rank', record['rank'], rank)
            check(name + ' pivots', record['pivot_columns'], pivots)
            check(name + ' complete basis', record['kernel_basis'], basis)
            check(name + ' rank-nullity', rank + len(basis), 21)
            check(name + ' independent basis', [[v[c] for c in free] for v in basis],
                  [[int(x == y) for y in range(len(free))] for x in range(len(free))])
            sparse = [[(c, v) for c, v in enumerate(row) if v] for row in original]
            sparse_ratio = [[(c, v) for c, v in enumerate(row) if v] for row in quotient]
            residuals = [[sum(v[c] * w for c, w in row) % P for row in sparse]
                         for v in basis]
            ratio_residuals = [[sum(v[c] * w for c, w in row) % P for row in sparse_ratio]
                              for v in basis]
            check(name + ' saved original residuals', record['kernel_residuals'], residuals)
            check(name + ' all original residuals zero', any(map(any, residuals)), False)
            check(name + ' all ratio residuals zero', any(map(any, ratio_residuals)), False)
            rows = record['minor_rows']
            check(name + ' independent original row count', len(set(rows)), rank)
            check(name + ' original rows in range', all(0 <= r < 12 for r in rows), True)
            minor = [[original[r][c] for c in pivots] for r in rows]
            det = minor_determinant(minor)
            check(name + ' original minor residue', record['minor_residue'], det)
            check(name + ' original minor nonzero', bool(det), True)
            local[rank] += 1
            vectors += len(basis)
            original_entries += sum(map(len, residuals))
            ratio_entries += sum(map(len, ratio_residuals))
            records.append(dict(pair=[a, b], rank=rank, pivot_columns=pivots,
                                independent_minor_residue=det,
                                rebuilt_basis_sha256=sha256(encoded(basis)).hexdigest(),
                                original_residual_entries=sum(map(len, residuals)),
                                ratio_residual_entries=sum(map(len, ratio_residuals)),
                                all_residuals_zero=not any(map(any, residuals + ratio_residuals))))
            for binding in saved['prefix_bindings']:
                if [a, b] == binding['pair']:
                    check(name + ' binding record', binding['record'], record)
                    check(name + ' original prefix hash', binding['stack_sha256'],
                          sha256(encoded(original)).hexdigest())
                    binding_records[binding['name']] = dict(pair=[a, b], rank=rank,
                        pivot_columns=pivots, basis_sha256=sha256(encoded(basis)).hexdigest())
        check(f'batch {batch_number} rank histogram', batch['rank_histogram'],
              {str(k): v for k, v in sorted(local.items())})
        ranks.update(local)
        replay_path = OUT / path.name
        replay_raw = encoded(dict(records=records)) + b'\n'
        replay_path.write_bytes(replay_raw)
        batches.append(dict(path=replay_path.relative_to(HERE).as_posix(),
                            sha256=sha256(replay_raw).hexdigest(), count=len(records)))
        if (batch_number + 1) % 15 == 0:
            print(f'Independent replay: {batch_number + 1}/{len(saved["batches"])} batches', flush=True)

    check('all pair indices exactly required', sorted(seen), required_pairs)
    check('no repeated pair records', len(set(seen)), len(seen))
    check('all pairs in increasing order', all(a < b for a, b in seen), True)
    old110 = json.loads((HERE / 'fixed-three-row-extensions.json').read_text())
    old109 = json.loads((HERE / 'zero-anchor-support-filter.json').read_text())
    old125 = json.loads((HERE / 'new-pair-filter.json').read_text())
    for binding in saved['prefix_bindings']:
        name = binding['name']
        literal = ([[v['I'], v['K']] for v in old110['seed'][:2]] if name == 'L110'
                   else old125['first_two'])
        check(name + ' literal prefix inputs', binding['keys'], literal)
        check(name + ' complete index binding', binding['pair'],
              [positions[(tuple(i), tuple(k))] for i, k in literal])
        oldblocks = (old109['blocks'][:2] if name == 'L110' else
                     [old125['blocks'][n] for n in old125['first_indices']])
        for index, block in zip(binding['pair'], oldblocks):
            check(name + f' original six-row block {index}', reconstructed[index], block['matrix'])
    check('both historical prefixes bound', sorted(binding_records), ['L110', 'L125'])
    summary = dict(actual_pairs=len(seen), required_pairs=independent_count,
                   ordered_pairs=len(ordered), universe_size=len(universe),
                   batches=len(batches), rank_histogram=dict(sorted(ranks.items())),
                   complete_kernel_vectors=vectors, original_residual_entries=original_entries,
                   ratio_residual_entries=ratio_entries, exclusion_rank_required=21,
                   checks=check_count, failures=failures)
    for key in saved['summary']:
        check('summary ' + key, saved['summary'][key], json.loads(json.dumps(summary[key])))
    summary['checks'] = check_count
    # Full relevant equality evidence is in the original and replay batches;
    # no preview or sampled case is used to accept the census.
    out = dict(source_sha256=sha256(raw).hexdigest(), summary=summary,
               blocks=block_evidence, batches=batches, prefix_bindings=binding_records,
               source_code_sha256={name: sha256((HERE / name).read_bytes()).hexdigest()
                    for name in ['all_disjoint_pair_census.py', 'verify_all_disjoint_pair_census.py',
                                 'zero_anchor_support_filter.py', 'new_pair_filter.py']})
    path = HERE / 'all-disjoint-pair-census-replay.json'
    path.write_bytes(encoded(out) + b'\n')
    # Report a bounded failure list; full details always remain on disk.
    printed = {key: value for key, value in summary.items() if key != 'failures'}
    printed['failure_count'] = len(failures)
    print(json.dumps(printed, sort_keys=True), flush=True)
    print(f'Failures: {len(failures)}; full replay: {path.relative_to(HERE.parent.parent)}', flush=True)
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    run()
