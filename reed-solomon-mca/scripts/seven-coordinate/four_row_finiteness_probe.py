"""Three predeclared exact loci only; no census or point sampling.

Run: python3 scripts/seven-coordinate/four_row_finiteness_probe.py
Full linear certificates and restricted homogeneous equations are saved.
"""
from itertools import combinations, combinations_with_replacement, product
from pathlib import Path
import json

import zero_anchor_support_filter as direct
from new_pair_filter import eliminate

P = 97
CASES = [
    [((1, 8), (47, 50)), ((12, 18), (64, 79)),
     ((1, 12), (70, 75)), ((8, 18), (85, 89))],
    [((1, 8), (64, 96)), ((12, 18), (79, 89)),
     ((1, 12), (47, 85)), ((8, 18), (50, 70))],
    [((1, 8), (47, 50)), ((12, 18), (64, 79)),
     ((1, 22), (70, 75)), ((8, 27), (85, 89))],
]


def run():
    universe = list(product(combinations(direct.S, 2), combinations(direct.J, 2)))
    records, failures = [], []
    for number, keys in enumerate(CASES, 1):
        supports = [set(i + k) for i, k in keys]
        sizes = [len(supports[a] & supports[b]) for a, b in combinations(range(4), 2)]
        labels = [universe.index(key) for key in keys]
        eligible = (sizes[0] == sizes[5] == 0 and max(sizes) <= 1
                    and len(set(labels)) == 4 and labels[0] < labels[1]
                    and labels[2] < labels[3])
        if not eligible:
            failures.append(f'case {number}: not eligible')
        blocks = [direct.block(*key) for key in keys]
        matrix = [row for block in blocks for row in block['matrix']]
        linear = eliminate(matrix)
        minor = [[matrix[r][c] for c in linear['pivot_columns']]
                 for r in linear['minor_rows']]
        det = direct.integer_determinant(minor)
        if not det % P or det % P != linear['minor_residue']:
            failures.append(f'case {number}: minor mismatch')
        basis = linear['kernel_basis']
        free = sorted(set(range(21)) - set(linear['pivot_columns']))
        identity = [[v[c] for c in free] for v in basis]
        if identity != [[int(i == j) for j in range(len(basis))]
                        for i in range(len(basis))]:
            failures.append(f'case {number}: kernel independence failed')
        monomials = list(combinations_with_replacement(range(len(basis)), 2))
        quadrics = []
        for a, b, c, d in combinations(range(7), 4):
            terms = [(1, (a, b), (c, d)), (-1, (a, c), (b, d)),
                     (1, (a, d), (b, c))]
            coeff = [0] * len(monomials)
            for sign, left, right in terms:
                u, v = direct.PAIRS.index(left), direct.PAIRS.index(right)
                for n, (i, j) in enumerate(monomials):
                    value = basis[i][u] * basis[j][v]
                    if i != j:
                        value += basis[j][u] * basis[i][v]
                    coeff[n] = (coeff[n] + sign * value) % P
            quadrics.append(dict(coordinates=[direct.S[i] for i in (a,b,c,d)],
                                 coefficients=coeff))
        locus = dict(status='unresolved', planes=[])
        if not basis:
            locus = dict(status='empty', cardinality=0, planes=[])
        else:
            expected = [[int(c == pivot) for c in range(21)] for pivot in (2, 6)]
            expected_quadrics = [[0, 1, 0]] + [[0, 0, 0]] * 34
            if basis != expected or [q['coefficients'] for q in quadrics] != expected_quadrics:
                failures.append(f'case {number}: two-coordinate-point proof does not apply')
            else:
                planes = []
                for labels_pair in ((1, 18), (8, 12)):
                    vectors = [[int(x == label) for x in direct.S] for label in labels_pair]
                    restrictions = [[[sum(a*b for a,b in zip(q,v)) % P for v in vectors]
                                     for q in block['covectors']] for block in blocks]
                    ranks = [direct.rank_and_rows(m)[0] for m in restrictions]
                    if ranks != [1]*4:
                        failures.append(f'case {number}: coordinate plane rank test failed')
                    planes.append(dict(coordinate_labels=labels_pair, vectors=vectors,
                                       restrictions=restrictions, actual_ranks=ranks,
                                       required_ranks=[1]*4))
                locus = dict(status='two_points', cardinality=2, planes=planes,
                             argument='Complete kernel p=s e1^e18+t e8^e12; '
                                      'Plucker equation st=0 over every extension field')
        records.append(dict(case=number, keys=keys, labels_zero_based=labels,
                            intersection_sizes=sizes, eligible=eligible,
                            blocks=blocks, matrix=matrix, linear=linear,
                            minor=minor, integer_minor_determinant=det,
                            free_columns=free, kernel_identity=identity,
                            monomials=monomials, plucker_quadrics=quadrics,
                            exact_locus=locus))
    out = dict(modulus=P, S=direct.S, H=direct.H, J=direct.J,
               column_pairs=[[direct.S[a],direct.S[b]] for a,b in direct.PAIRS],
               scope='Three predeclared quadruples; not universal finiteness',
               cases=records, failures=failures)
    path = Path(__file__).with_name('four-row-finiteness-probe.json')
    path.write_text(json.dumps(out, indent=2) + '\n')
    for r in records:
        print(f"Case {r['case']}: eligible={r['eligible']}, "
              f"actual rank={r['linear']['rank']}/21, "
              f"complete kernel dimension={len(r['linear']['kernel_basis'])}; "
              f"exact locus size={r['exact_locus'].get('cardinality', 'unresolved')}; "
              'required infinite family: not attained')
    print(f'Failures: {failures}; full certificate: {path.relative_to(Path.cwd())}')
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    run()
