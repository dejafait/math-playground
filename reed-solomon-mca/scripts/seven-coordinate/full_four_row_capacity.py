"""Exact linear certificate for one full four-row locus; no parameter sampling.

The complete field-valued case split belongs in L165. This producer saves
the maps, basis identities, rank minors, and capacity witness it needs.
"""
from itertools import combinations, product
from pathlib import Path
import json

P = 97
S = [1, 8, 12, 18, 22, 27, 33]
J = [47, 50, 64, 70, 75, 79, 85, 89, 96]
FIXED = [35, 522, 477, 566]
X0 = [2, 50, 5, 77, 16, 45, 81]
Y0 = [75, 32, 0, 69, 3, 1, 0]
X1 = [58, 92, 4, 81, 71, 36, 26]
Y1 = [0, 0, 30, 0, 0, 0, 1]


def apply(matrix, vector):
    return [sum(a*b for a, b in zip(row, vector)) % P for row in matrix]


def transpose(matrix):
    return [list(row) for row in zip(*matrix)]


def rref(matrix):
    a = [[v % P for v in row] for row in matrix]
    pivots = []
    for col in range(len(a[0])):
        k = len(pivots)
        row = next((i for i in range(k, len(a)) if a[i][col]), None)
        if row is None:
            continue
        a[k], a[row] = a[row], a[k]
        scale = pow(a[k][col], -1, P)
        a[k] = [v*scale % P for v in a[k]]
        for i in range(len(a)):
            if i != k:
                scale = a[i][col]
                a[i] = [(v-scale*w) % P for v, w in zip(a[i], a[k])]
        pivots.append(col)
    return a, pivots


def determinant(matrix):
    a = [row[:] for row in matrix]
    value = 1
    for k in range(len(a)):
        pivot = next((i for i in range(k, len(a)) if a[i][k] % P), None)
        if pivot is None:
            return 0
        if pivot != k:
            a[k], a[pivot] = a[pivot], a[k]
            value = -value
        value = value*a[k][k] % P
        for i in range(k+1, len(a)):
            c = a[i][k]*pow(a[k][k], -1, P) % P
            a[i] = [(v-c*w) % P for v, w in zip(a[i], a[k])]
    return value % P


def rank_witness(matrix):
    _, columns = rref(matrix)
    _, rows = rref(transpose(matrix))
    minor = [[matrix[i][j] for j in columns] for i in rows]
    return dict(rank=len(columns), rows=rows, columns=columns,
                minor=minor, determinant_mod_97=determinant(minor))


def quotient(I, K):
    values = []
    for x in S:
        value = 1
        for y in J:
            if y not in K:
                value = value*(x-y) % P
        values.append(value)
    observed = [i for i, x in enumerate(S) if x not in I]
    z = observed[0]
    Q = [[((values[z] if i == col else 0) -
           (values[i] if z == col else 0)) % P for col in range(7)]
         for i in observed[1:]]
    return dict(I=list(I), K=list(K), support=sorted(I+K),
                g_values=values, anchor=S[z], Q=Q)


def main():
    labels = list(product(combinations(S, 2), combinations(J, 2)))
    maps = [dict(label=j, **quotient(*labels[j])) for j in FIXED]
    a, b, c, d = [v['Q'] for v in maps]
    e12 = [int(s == 12) for s in S]
    triple_matrix = ([row+[0]*7 for row in a] +
                     [[0]*7+row for row in b] + [row+row for row in c])
    triple_basis = [X0+Y0, X1+Y1, [0]*7+e12]
    triple_rank = rank_witness(triple_matrix)
    basis_rank = rank_witness(triple_basis)
    triple_residuals = [apply(triple_matrix, z) for z in triple_basis]
    bc_matrix = b+c
    bc_rank = rank_witness(bc_matrix)
    bc_residual = apply(bc_matrix, e12)
    # A = span(e_1,e_8,g_a), by the original quotient definition.
    a_basis = [[int(s == v) for s in S] for v in (1, 8)] + [maps[0]['g_values']]
    boundary_basis = a_basis+[e12]
    boundary_images = transpose([apply(d, v) for v in boundary_basis])
    boundary_det = determinant(boundary_images)
    uvw = [apply(d, y) for y in (Y0, Y1, e12)]
    uvw_matrix = transpose(uvw)
    uvw_rank = rank_witness(uvw_matrix)
    fourth_images = []
    for z in triple_basis:
        fourth_images.append(dict(constant=apply(d, z[:7]), linear=apply(d, z[7:])))
    family_relations = [[(v+26*w) % P for v, w in zip(row['constant'], row['linear'])]
                        for row in fourth_images[:2]]
    intersections = [dict(pair=[FIXED[i], FIXED[j]],
                          intersection=sorted(set(maps[i]['support']) & set(maps[j]['support'])))
                     for i, j in combinations(range(4), 2)]
    fixed_degrees = {str(z): sum(z in v['support'] for v in maps) for z in S+J}
    residual_capacities = {z: 4-value for z, value in fixed_degrees.items()}
    weights = {str(z): int(z == 27) for z in S+J}
    cost = sum(residual_capacities[z]*w for z, w in weights.items())
    failures = []
    requirements = [
        (triple_rank['rank'] == 11, 'three-row pair-space rank must be 11'),
        (basis_rank['rank'] == 3, 'three displayed generators must be independent'),
        (not any(map(any, triple_residuals)), 'three-row basis residuals'),
        (bc_rank['rank'] == 6 and not any(bc_residual), 'B intersect C must equal E e_12'),
        (boundary_det != 0, 'Q_d must be injective on A+E e_12'),
        (uvw_rank['rank'] == 3, 'U,V,W must be independent'),
        (not any(map(any, family_relations)), 'Q_d x_i = -26 Q_d y_i'),
        (not any(fourth_images[2]['constant']), 'boundary generator has x=0'),
        (cost == 3 and cost < 8, 'residual coordinate cost must be 3 < 8'),
    ]
    for passed, description in requirements:
        if not passed:
            failures.append(description)
    out = dict(modulus=P, S=S, J=J, fixed_labels=FIXED, maps=maps,
               intersections=intersections, triple_matrix=triple_matrix,
               triple_rank=triple_rank, triple_basis=triple_basis,
               basis_rank=basis_rank, triple_residuals=triple_residuals,
               bc_matrix=bc_matrix, bc_rank=bc_rank, bc_kernel_generator=e12,
               bc_residual=bc_residual, boundary_basis=boundary_basis,
               boundary_images=boundary_images, boundary_determinant=boundary_det,
               fourth_images=fourth_images, UVW=uvw, uvw_matrix=uvw_matrix,
               uvw_rank=uvw_rank, family_relations=family_relations,
               fixed_degrees=fixed_degrees, residual_capacities=residual_capacities,
               coordinate_weights=weights, capacity_cost=cost, required_strict_threshold=8,
               capacity_mask_input='L163 complete family mask; L164 common coordinate 27',
               failures=failures)
    path = Path(__file__).with_name('full-four-row-capacity.json')
    path.write_text(json.dumps(out, indent=2)+'\n')
    print('Three-row rank:', triple_rank['rank'], '(required 11); basis rank:', basis_rank['rank'], '(required 3)')
    print('B/C stack rank:', bc_rank['rank'], '(required 6); boundary determinant:', boundary_det, '(required nonzero)')
    print('Fourth-row image rank:', uvw_rank['rank'], '(required 3); residual cost:', cost, '(required < 8)')
    print('Failures:', failures)
    print('Certificate:', path.relative_to(Path.cwd()))
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
