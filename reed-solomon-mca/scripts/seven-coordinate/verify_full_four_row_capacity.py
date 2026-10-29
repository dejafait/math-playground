"""Independent coefficient/minor check; imports no producer routines.

Integer determinants use rational elimination, independently of the
producer's modular elimination. Existing L163's all-parameter mask is
imported, not reproved. The new full-locus case split is written in L165.
"""
from fractions import Fraction
from hashlib import sha256
from pathlib import Path
import json
import re

BASE = Path(__file__).resolve().parent
ROOT = BASE.parent.parent
P = 97
S = [1, 8, 12, 18, 22, 27, 33]
J = [47, 50, 64, 70, 75, 79, 85, 89, 96]
FIXED = [35, 522, 477, 566]
CHECKS = []
DETERMINANTS = {}


def check(name, actual, required):
    CHECKS.append(dict(name=name, passed=actual == required,
                       actual=actual, required=required))


def image(matrix, vector):
    answer = []
    for row in matrix:
        value = 0
        for i in range(len(vector)):
            value += row[i]*vector[i]
        answer.append(value % P)
    return answer


def columns(vectors):
    return [[v[i] for v in vectors] for i in range(len(vectors[0]))]


def det_integer(matrix):
    a = [[Fraction(v) for v in row] for row in matrix]
    result = Fraction(1)
    for j in range(len(a)):
        if not a[j][j]:
            k = next((i for i in range(j+1, len(a)) if a[i][j]), None)
            if k is None:
                return 0
            a[j], a[k] = a[k], a[j]
            result = -result
        pivot = a[j][j]
        result *= pivot
        for i in range(j+1, len(a)):
            ratio = a[i][j]/pivot
            for k in range(j, len(a)):
                a[i][k] -= ratio*a[j][k]
    assert result.denominator == 1
    return result.numerator


def verify_minor(name, matrix, witness, rank):
    check(name+'/rank', witness['rank'], rank)
    rows, cols = witness['rows'], witness['columns']
    check(name+'/row_count', len(rows), rank)
    check(name+'/column_count', len(cols), rank)
    check(name+'/distinct_rows', len(set(rows)), rank)
    check(name+'/distinct_columns', len(set(cols)), rank)
    assert all(0 <= i < len(matrix) for i in rows)
    assert all(0 <= j < len(matrix[0]) for j in cols)
    minor = [[matrix[i][j] for j in cols] for i in rows]
    check(name+'/minor_entries', witness['minor'], minor)
    value = det_integer(minor)
    DETERMINANTS[name] = dict(rows=rows, columns=cols, minor=minor,
                              integer_determinant=value, residue=value % P)
    check(name+'/residue', witness['determinant_mod_97'], value % P)
    check(name+'/nonzero_mod_97', value % P != 0, True)


def build_labels():
    labels = []
    for i in range(len(S)):
        for j in range(i+1, len(S)):
            for k in range(len(J)):
                for l in range(k+1, len(J)):
                    labels.append(([S[i], S[j]], [J[k], J[l]]))
    return labels


def build_map(I, K):
    # Expand g as an integer polynomial, then evaluate modulo 97 by Horner.
    coeff = [1]
    for root in J:
        if root in K:
            continue
        new = [0]*(len(coeff)+1)
        for i, v in enumerate(coeff):
            new[i] -= root*v
            new[i+1] += v
        coeff = new
    values = []
    for x in S:
        value = 0
        for v in reversed(coeff):
            value = (x*value+v) % P
        values.append(value)
    assert all(values)
    observed = [x for x in S if x not in I]
    anchor = observed[0]
    a = S.index(anchor)
    Q = []
    for x in observed[1:]:
        i = S.index(x)
        # Independent normalized-map reconstruction, with checked denominators.
        normalized = [0]*7
        normalized[i] = pow(values[i], -1, P)
        normalized[a] = -pow(values[a], -1, P)
        Q.append([v*values[i]*values[a] % P for v in normalized])
    return dict(I=I, K=K, support=sorted(I+K), g_values=values,
                anchor=anchor, Q=Q)


def main():
    path = BASE/'full-four-row-capacity.json'
    data = json.loads(path.read_text())
    check('modulus', data['modulus'], P)
    check('S', data['S'], S)
    check('J', data['J'], J)
    check('fixed_labels', data['fixed_labels'], FIXED)
    labels = build_labels()
    check('label_count', len(labels), 756)
    maps = [dict(label=j, **build_map(*labels[j])) for j in FIXED]
    check('all_four_actual_maps', data['maps'], maps)
    a, b, c, d = [v['Q'] for v in maps]
    l162 = ROOT/'lemmas/L162-explicit-four-row-infinite-family.md'
    source = l162.read_text()
    vectors = []
    for name in ('x_0', 'y_0', 'x_1', 'y_1'):
        match = re.search(r'^\s*'+name+r'=\(([^)]*)\)', source, re.M)
        assert match is not None
        vectors.append([int(v.strip()) for v in match.group(1).split(',')])
    x0, y0, x1, y1 = vectors
    e12 = [0, 0, 1, 0, 0, 0, 0]
    basis = [x0+y0, x1+y1, [0]*7+e12]
    matrix = [row+[0]*7 for row in a]+[[0]*7+row for row in b]+[row+row for row in c]
    check('triple_matrix', data['triple_matrix'], matrix)
    check('triple_basis_from_canonical_L162', data['triple_basis'], basis)
    residuals = [image(matrix, v) for v in basis]
    check('triple_residual_records', data['triple_residuals'], residuals)
    check('triple_all_zero', residuals, [[0]*12 for _ in range(3)])
    verify_minor('triple', matrix, data['triple_rank'], 11)
    verify_minor('basis', basis, data['basis_rank'], 3)
    check('triple_dimension_squeeze', 14-11, 3)
    check('bc_matrix', data['bc_matrix'], b+c)
    check('bc_kernel_generator', data['bc_kernel_generator'], e12)
    check('bc_residual_record', data['bc_residual'], image(b+c, e12))
    check('bc_kernel_identity', image(b+c, e12), [0]*8)
    verify_minor('bc', b+c, data['bc_rank'], 6)
    boundary_basis = [[1, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0],
                      maps[0]['g_values'], e12]
    check('boundary_basis', data['boundary_basis'], boundary_basis)
    check('A_basis_kernel_identities', [image(a, v) for v in boundary_basis[:3]], [[0]*4]*3)
    boundary = columns([image(d, v) for v in boundary_basis])
    check('boundary_images', data['boundary_images'], boundary)
    boundary_det = det_integer(boundary)
    DETERMINANTS['boundary'] = dict(minor=boundary, integer_determinant=boundary_det,
                                    residue=boundary_det % P)
    check('boundary_determinant', data['boundary_determinant'], boundary_det % P)
    check('boundary_injectivity', boundary_det % P != 0, True)
    fourth = [dict(constant=image(d, v[:7]), linear=image(d, v[7:])) for v in basis]
    check('fourth_images', data['fourth_images'], fourth)
    uvw = [image(d, v) for v in (y0, y1, e12)]
    check('UVW', data['UVW'], uvw)
    check('uvw_matrix', data['uvw_matrix'], columns(uvw))
    verify_minor('uvw', columns(uvw), data['uvw_rank'], 3)
    relations = [[(q+26*r) % P for q, r in zip(v['constant'], v['linear'])] for v in fourth[:2]]
    check('family_relations_record', data['family_relations'], relations)
    check('family_relations_zero', relations, [[0]*4]*2)
    check('fourth_boundary_constant_zero', fourth[2]['constant'], [0]*4)
    check('cross_ratio_nonzero_and_not_one', 26 not in (0, 1), True)
    intersections = []
    for i in range(4):
        for j in range(i+1, 4):
            overlap = sorted(set(maps[i]['support']) & set(maps[j]['support']))
            intersections.append(dict(pair=[FIXED[i], FIXED[j]], intersection=overlap))
            check(f'fixed_intersection/{i}/{j}', overlap, [12] if (i, j) == (1, 2) else [])
    check('intersection_records', data['intersections'], intersections)
    degrees = {str(z): sum(z in v['support'] for v in maps) for z in S+J}
    residual = {z: 4-n for z, n in degrees.items()}
    weights = {str(z): int(z == 27) for z in S+J}
    check('fixed_degrees', data['fixed_degrees'], degrees)
    check('residual_capacities', data['residual_capacities'], residual)
    check('nonnegative_capacities', all(v >= 0 for v in residual.values()), True)
    check('nonnegative_coordinate_weights', data['coordinate_weights'], weights)
    l163 = ROOT/'lemmas/L163-l162-complete-additional-row-parameter-loci.md'
    match = re.search(r'B=\{([^}]*)\}', l163.read_text())
    assert match is not None
    B = [int(v.strip()) for v in match.group(1).split(',')]
    check('complete_canonical_mask_count', len(B), 40)
    check('complete_canonical_mask_distinct', len(set(B)), 40)
    support_evidence = []
    for j in B:
        I, K = labels[j]
        support = I+K
        overlaps = [sorted(set(support) & set(v['support'])) for v in maps]
        value = sum(weights[str(z)] for z in support)
        check(f'mask/{j}/eligible', j not in FIXED and all(len(v) <= 1 for v in overlaps), True)
        check(f'mask/{j}/cover_weight', value, 1)
        support_evidence.append(dict(label=j, I=I, K=K, intersections=overlaps, cover_weight=value))
    cost = sum(weights[z]*residual[z] for z in weights)
    check('capacity_cost_record', data['capacity_cost'], cost)
    check('capacity_cost', cost, 3)
    check('required_threshold', data['required_strict_threshold'], 8)
    check('strict_sub_eight', cost < 8, True)
    check('producer_failures', data['failures'], [])
    sources = [ROOT/'lemmas/L109-seven-coordinate-parameter-free-support-filter.md',
               ROOT/'lemmas/C155a-original-pair-segre-locus-and-projection-ranks.md', l162, l163,
               ROOT/'lemmas/L164-fixed-family-twelve-support-capacity-obstruction.md',
               BASE/'full_four_row_capacity.py', Path(__file__)]
    failures = [v for v in CHECKS if not v['passed']]
    result = dict(source_sha256={str(v.relative_to(ROOT)): sha256(v.read_bytes()).hexdigest() for v in sources},
                  certificate_sha256=sha256(path.read_bytes()).hexdigest(),
                  checks=CHECKS, determinants=DETERMINANTS, support_evidence=support_evidence,
                  imported_mask_qualification='L163 supplies all-parameter and all-eligible-label exhaustion; not reaudited here',
                  result=dict(checks=len(CHECKS), failures=failures, cost=cost, required_strict_threshold=8))
    output = BASE/'full-four-row-capacity-verification.json'
    output.write_text(json.dumps(result, indent=2)+'\n')
    print(f'Independent checks: {len(CHECKS)}; failures: {len(failures)}')
    print('Exact determinant residues:', {key: value['residue'] for key, value in DETERMINANTS.items()})
    print(f'Cover weights checked on all {len(B)} canonical possible labels; cost {cost}, required < 8')
    print('Certificate:', output.relative_to(ROOT))
    if failures:
        print('Failed checks:', [v['name'] for v in failures])
        raise SystemExit(1)


if __name__ == '__main__':
    main()
