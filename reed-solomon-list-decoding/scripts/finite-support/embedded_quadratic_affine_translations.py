"""Exhaust exactly the assessed common auxiliary affine-translation family.

Certificates contain complete arrays, all invertible row operations, and
all subset intersections (shared core plus the saved outside points).
The old search is never invoked. No label-rank symmetry is used.
"""
from collections import Counter
from hashlib import sha256
from itertools import combinations
from pathlib import Path
import json

from embedded_quadratic_search import rref, product, integer_determinant

HERE = Path(__file__).resolve().parent
OUT = HERE / 'embedded-quadratic-affine-translations'
P, A, G = 65537, 137, 19139
T = [16, 64, 70, 102, 112, 118, 121]
Q = [(33, 27, 3), (106, 120, 2), (0, 0, 0), (64, 44, 1), (34, 47, 2)]


def eye(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]


def reconstruct(a, b, powers, core):
    values = [[(c + (d+a)*t + e*t*t+b) % A for t in T] for c, d, e in Q]
    exponents = [[61+A*j+y for j, y in enumerate(row)] for row in values]
    labels = [[powers[e] for e in row] for row in exponents]
    supports = [sorted(core+row) for row in labels]
    subsets = []
    for size in range(1, 6):
        for indices in combinations(range(5), size):
            points = sorted(set.intersection(*(set(labels[i]) for i in indices)))
            auxiliary = sorted(powers[61+A*j+values[indices[0]][j]] for j in range(7)
                               if all(values[i][j] == values[indices[0]][j] for i in indices))
            assert points == auxiliary, ('intersection', a, b, indices)
            subsets.append({'indices': list(indices), 'outside': points})
    stars, matrix = [], []
    for x in sorted(set().union(*map(set, labels))):
        incident = [i for i in range(5) if x in labels[i]]
        anchor = min(incident)
        for other in incident[1:]:
            stars.append({'point': x, 'anchor': anchor, 'other': other, 'incident': incident})
            matrix.append([((int(i == anchor)-int(i == other))*pow(x, d, P)) % P
                           for i in range(4) for d in range(3)])
    return dict(parameter=[a, b], polynomials=[[(c+b) % A, (d+a) % A, e] for c, d, e in Q],
                graph_values=values, label_exponents=exponents, outside_labels=labels,
                supports=supports, subset_intersections=subsets, stars=stars, matrix=matrix)


def verify(case, core, base_values, base_stars):
    a, b = case['parameter']
    values, labels, mat = case['graph_values'], case['outside_labels'], case['matrix']
    assert len(set(map(tuple, values))) == 5
    assert all(len(set(row)) == 7 and set(row).isdisjoint(core) for row in labels)
    assert all(len(set(s)) == len(s) == 68 for s in case['supports'])
    assert all((values[i][j] == values[k][j]) == (base_values[i][j] == base_values[k][j])
               for i in range(5) for k in range(5) for j in range(7))
    # Compare complete incident sets through the auxiliary column/y bijection,
    # retaining triple and four-way overlaps and their full star row counts.
    incidents = Counter(tuple(row['incident']) for row in case['stars'])
    assert incidents == base_stars and len(mat) == 12
    R, U, ops, pivots = rref(mat, 12)
    replay, transform = [r[:] for r in mat], eye(12)
    for kind, i, *rest in ops:
        assert 0 <= i < 12
        if kind == 'swap':
            j, = rest
            assert 0 <= j < 12 and i != j
            for z in (replay, transform):
                z[i], z[j] = z[j], z[i]
        elif kind == 'scale':
            s, = rest
            assert 0 < s < P
            for z in (replay, transform):
                z[i] = [x*s % P for x in z[i]]
        elif kind == 'subtract':
            j, s = rest
            assert 0 <= j < 12 and i != j and 0 <= s < P
            for z in (replay, transform):
                z[i] = [(x-s*y) % P for x, y in zip(z[i], z[j])]
        else:
            raise AssertionError(kind)
    assert replay == R and transform == U and product(U, mat) == R
    rank = len(pivots)
    leading = [next((j for j, x in enumerate(row) if x), None) for row in R]
    assert pivots == sorted(set(pivots)) and leading == pivots+[None]*(12-rank)
    assert all(R[i][p] == int(i == k) for k, p in enumerate(pivots) for i in range(12))
    determinant = 1
    for kind, i, *rest in ops:
        if kind == 'swap':
            determinant = -determinant % P
        elif kind == 'scale':
            determinant = determinant*pow(rest[0], -1, P) % P
    if rank == 12:
        assert R == eye(12) and product(mat, U) == eye(12)
        kernel = None
    else:
        determinant = 0
        free = next(j for j in range(12) if j not in pivots)
        kernel = [int(j == free) for j in range(12)]
        for i, p in enumerate(pivots):
            kernel[p] = -R[i][free] % P
        assert any(kernel) and all(sum(x*y for x, y in zip(row, kernel)) % P == 0 for row in mat)
    case.update(rank=rank, required_full_rank=12, rref=R, row_transform=U,
                operations=ops, pivots=pivots, determinant_mod_P=determinant,
                nonzero_kernel=kernel, verification={
                    'support_and_incidence': True, 'complete_operation_replay': True,
                    'full_transformation_identity': True, 'rref_including_zero_rows': True,
                    'both_inverse_identities': rank == 12,
                    'nonzero_kernel_checked': rank < 12})


def main():
    OUT.mkdir(exist_ok=True)
    powers = [pow(G, j, P) for j in range(1024)]
    core = powers[:61]
    assert pow(G, 1024, P) == 1 and pow(G, 512, P) == P-1 and len(set(powers)) == 1024
    assert len(set(powers[61:1020])) == 959 and set(powers[61:]).isdisjoint(core)
    base = reconstruct(0, 0, powers, core)
    base_values = base['graph_values']
    base_stars = Counter(tuple(r['incident']) for r in base['stars'])
    source = HERE / 'embedded-quadratic-search-results.json'
    original = json.loads(source.read_text())['trials'][10]
    assert base['matrix'] == original['matrix'] and base['stars'] == original['row_labels']
    summary = dict(parameters=dict(prime=P, auxiliary_prime=A, generator=G, T=T,
                       polynomials=Q, core=core, count=A*A, order='lexicographic (a,b)'),
                   intersection_schema='Each full intersection is core union subset_intersections.outside',
                   original_certificate_sha256=sha256(source.read_bytes()).hexdigest(),
                   completed_parameters=0, rank_distribution={}, singular_parameters=[],
                   operation_count=0, failures=[], certificates=[])
    counts = Counter()
    try:
        for a in range(A):
            cases = []
            for b in range(A):
                case = reconstruct(a, b, powers, core)
                verify(case, core, base_values, base_stars)
                if (a, b) == (0, 0):
                    det, trace = integer_determinant(case['matrix'])
                    assert det % P == case['determinant_mod_P'] == 26669
                    assert case['row_transform'] == original['row_transform']
                    summary['unshifted_check'] = dict(matrix_matches=True, inverse_matches=True,
                        integer_determinant=det, determinant_mod_P=26669, bareiss_trace=trace)
                cases.append(case)
                counts[case['rank']] += 1
                summary['operation_count'] += len(case['operations'])
                summary['completed_parameters'] += 1
                if case['rank'] < 12:
                    summary['singular_parameters'].append([a, b])
                    (OUT / f'singular-{a:03d}-{b:03d}.json').write_text(json.dumps(case, separators=(',', ':'))+'\n')
            path = OUT / f'a-{a:03d}.json'
            path.write_text(json.dumps(dict(core=core, cases=cases), separators=(',', ':'))+'\n')
            summary['certificates'].append(dict(path=str(path.relative_to(HERE)),
                a=a, cases=len(cases), sha256=sha256(path.read_bytes()).hexdigest()))
            summary['rank_distribution'] = {str(k): v for k, v in sorted(counts.items())}
            (OUT / 'summary.json').write_text(json.dumps(summary, separators=(',', ':'))+'\n')
            if a % 20 == 0 or a == A-1:
                print(f'a={a}: verified {summary["completed_parameters"]}/{A*A}; ranks={dict(counts)}; failures=0', flush=True)
    except Exception as exc:
        summary['failures'].append(dict(parameter=[a, b], error=repr(exc)))
        (OUT / 'failure-case.json').write_text(json.dumps(case, separators=(',', ':'))+'\n')
        raise
    finally:
        summary['rank_distribution'] = {str(k): v for k, v in sorted(counts.items())}
        (OUT / 'summary.json').write_text(json.dumps(summary, separators=(',', ':'))+'\n')
    print(json.dumps(dict(actual_parameters=summary['completed_parameters'], required_parameters=A*A,
        actual_ranks=summary['rank_distribution'], required_full_rank=12,
        singular_count=len(summary['singular_parameters']), failures=summary['failures'],
        certificate=str((OUT/'summary.json').relative_to(HERE.parent.parent))), indent=2))


if __name__ == '__main__':
    main()
