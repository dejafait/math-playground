"""One approved named-third diagnostic; preserve all extension-field loci.

Run: python3 scripts/seven-coordinate/nondisjoint_third_diagnostic.py
Reuses audited matrix/rank utilities, with independent blocks and minors.
No deficient kernel is interpreted as an actual recovery.
"""
from collections import Counter
from itertools import combinations, product
from pathlib import Path
import json

import zero_anchor_support_filter as direct
import fixed_three_row_extensions as kernels
import verify_fixed_three_row_extensions as independent
import residual_kernel_gates as point_gates

P = 97
S, H, J = direct.S, direct.H, direct.J
PAIRS = list(combinations(range(7), 2))
INDEX = {ij: n for n, ij in enumerate(PAIRS)}
QUADS = list(combinations(range(7), 4))
SEED = [([1, 8], [47, 50]), ([12, 18], [64, 70]),
        ([1, 22], [75, 79])]
HERE = Path(__file__).resolve().parent


def homogeneous_plucker(basis):
    """All 35 quadrics, coefficients on b_a*b_b for a<=b (no /2)."""
    monomials = list(combinations(range(len(basis)), 2))
    monomials = sorted(monomials+[(a, a) for a in range(len(basis))])
    equations = []
    for a, b, c, d in QUADS:
        terms = [(1, (a, b), (c, d)), (-1, (a, c), (b, d)),
                 (1, (a, d), (b, c))]
        values = []
        for x, y in monomials:
            value = 0
            for sign, ij, kl in terms:
                i, k = INDEX[ij], INDEX[kl]
                value += sign*basis[x][i]*basis[y][k]
                if x != y:
                    value += sign*basis[y][i]*basis[x][k]
            values.append(value % P)
        equations.append(values)
    return {'kernel_coordinate_monomials': [list(m) for m in monomials],
            'label_quadruples': [[S[x] for x in q] for q in QUADS],
            'coefficients': equations}


def linear_product(a, b, monomials):
    return [(a[x]*b[y]+(a[y]*b[x] if x != y else 0)) % P
            for x, y in monomials]


def linear_combination(vectors, coefficients, width):
    return [sum(c*v[j] for c, v in zip(coefficients, vectors)) % P
            for j in range(width)]


def span_solver(generators):
    """Return exact original-generator coordinates or None; no ideal inference."""
    echelon = {}
    count = len(generators)
    for index, value in enumerate(generators):
        value = value[:]
        certificate = [int(j == index) for j in range(count)]
        for col, (v, c) in sorted(echelon.items()):
            factor = value[col]
            value = [(a-factor*b) % P for a, b in zip(value, v)]
            certificate = [(a-factor*b) % P for a, b in zip(certificate, c)]
        pivot = next((j for j, x in enumerate(value) if x), None)
        if pivot is not None:
            inverse = pow(value[pivot], -1, P)
            echelon[pivot] = ([inverse*x % P for x in value],
                              [inverse*x % P for x in certificate])

    def solve(value):
        remainder = value[:]
        answer = [0]*count
        for col, (v, c) in sorted(echelon.items()):
            factor = remainder[col]
            remainder = [(a-factor*b) % P for a, b in zip(remainder, v)]
            answer = [(a+factor*b) % P for a, b in zip(answer, c)]
        if any(remainder):
            return None
        assert linear_combination(generators, answer, len(value)) == value
        return answer
    return solve


def algebraic_charts(basis, rows, plucker):
    """Complete pivot cover; only checked degree-two ideal identities exclude.

    In chart p_ab!=0 use U_x=p_xb, V_x=p_ax. On the Plucker locus,
    U wedge V=p_ab*p; hence these vectors span the required plane.
    For each nonzero quotient row pair (qU_n,qV_n), H=-qV_n*U+qU_n*V.
    Every polynomial is saved by its complete coefficient vector.
    """
    dimension = len(basis)
    monomials = [tuple(m) for m in plucker['kernel_coordinate_monomials']]
    width = len(monomials)
    generators = plucker['coefficients']
    solve = span_solver(generators)
    zero = [0]*dimension
    coordinates = [[basis[n][j] for n in range(dimension)] for j in range(21)]

    def p(x, y):
        if x == y:
            return zero[:]
        if x < y:
            return coordinates[INDEX[x, y]][:]
        return [-z % P for z in coordinates[INDEX[y, x]]]

    charts = []
    for a, b in PAIRS:
        chart = {'pivot_labels': [S[a], S[b]], 'pivot_linear_form': p(a, b)}
        if not any(p(a, b)):
            chart.update(status='empty_pivot_chart', rows=[])
            charts.append(chart)
            continue
        u, v = [p(x, b) for x in range(7)], [p(a, x) for x in range(7)]
        row_records = []
        for row in rows:
            i, k = row['I'], row['K']
            block = direct.block(i, k)
            qu = [linear_combination(u, c, dimension) for c in block['covectors']]
            qv = [linear_combination(v, c, dimension) for c in block['covectors']]
            minors = [[(x-y) % P for x, y in zip(
                linear_product(qu[n], qv[m], monomials),
                linear_product(qu[m], qv[n], monomials))]
                for n, m in combinations(range(4), 2)]
            minor_identities = [solve(f) for f in minors]
            assert all(c is not None for c in minor_identities)
            branches = []
            z = S.index(block['pivot'])
            gz = direct.g(k, S[z])
            assert gz
            for n in range(4):
                h = [[(x-y) % P for x, y in zip(
                    linear_product(qu[n], v[x], monomials),
                    linear_product(qv[n], u[x], monomials))] for x in range(7)]
                quotient_residuals = [linear_combination(h, c, width)
                                      for c in block['covectors']]
                residual_identities = [solve(f) for f in quotient_residuals]
                assert all(c is not None for c in residual_identities)
                # Actual lambda=H_z/g(z); overlap weight=(g(z)H_i-g(i)H_z)/g(z).
                weight_numerators = [h[z]]+[
                    [(gz*x-direct.g(k, label)*y) % P for x, y in zip(h[S.index(label)], h[z])]
                    for label in i]
                zero_identities = [solve(f) for f in weight_numerators]
                failure = next((j for j, c in enumerate(zero_identities) if c is not None), None)
                no_pivot = not any(qu[n]+qv[n])
                branches.append({
                    'quotient_row_index': n,
                    'projection_pivot_nonzero_alternatives': [qu[n], qv[n]],
                    'alpha_linear_form': [-x % P for x in qv[n]],
                    'beta_linear_form': qu[n],
                    'intersection_vector_quadrics': h,
                    'quotient_residual_quadrics': quotient_residuals,
                    'quotient_residual_plucker_identities': residual_identities,
                    'weight_numerator_quadrics': weight_numerators,
                    'weight_names': ['lambda']+[f'overlap_at_{x}' for x in i],
                    'zero_weight_plucker_identities': zero_identities,
                    'finite_gate_D_coefficient': [-x % P for x in qv[n]],
                    'finite_gate_C_coefficient': [-x % P for x in qu[n]],
                    'status': ('empty_projection_pivot' if no_pivot else
                               'excluded_zero_weight_identity' if failure is not None else
                               'unresolved'),
                    'first_identically_zero_weight': failure})
            row_records.append({'I': i, 'K': k, 'g_pivot': gz,
                                'Q_U_linear_forms': qu, 'Q_V_linear_forms': qv,
                                'projection_minor_quadrics': minors,
                                'projection_minor_plucker_identities': minor_identities,
                                'branches': branches,
                                'row_all_branches_excluded': all(b['status'] != 'unresolved' for b in branches)})
        # Each row must pass. One row failing in every pivot branch excludes this chart.
        excluded_row = next((j for j, row in enumerate(row_records)
                             if row['row_all_branches_excluded']), None)
        chart.update(U_linear_forms=u, V_linear_forms=v, rows=row_records,
                     status='excluded_by_row' if excluded_row is not None else 'unresolved',
                     excluded_row=excluded_row)
        charts.append(chart)
    return {'coordinate_variables': [f'b{j}' for j in range(dimension)],
            'quadratic_monomials': [list(m) for m in monomials],
            'bivector_coordinate_linear_forms': coordinates,
            'semantics': 'b!=0, all Plucker quadrics=0; choose p_ab!=0 chart. For each row choose n and one nonzero projection alternative, all three weight numerators nonzero and D*alpha-C*beta!=0 in its prescribed original basis. Choices across rows are independent and must all pass. Rank-zero projection has no pivot. Empty chart and identity exclusions are exact; every other chart remains unresolved.',
            'charts': charts,
            'status': ('excluded_all_charts' if all(c['status'] != 'unresolved' for c in charts)
                       else 'unresolved'),
            'unresolved_chart_indices': [j for j, c in enumerate(charts) if c['status'] == 'unresolved']}


def run():
    assert H == independent.H and S == independent.S and J == independent.J
    expected = list(product(combinations(S, 2), combinations(J, 2)))
    assert len(expected) == len(set(expected)) == 756
    blocks, ratios = {}, {}
    for i, k in expected:
        blocks[i, k] = direct.block(i, k)['matrix']
        assert blocks[i, k] == independent.block(i, k)
        ratios[i, k] = kernels.ratio_block(i, k)
    seed_keys = [(tuple(i), tuple(k)) for i, k in SEED]
    seed_sets = [set(i+k) for i, k in SEED]
    assert all(len(a & b) <= 1 for a, b in combinations(seed_sets, 2))
    stack = [r for key in seed_keys for r in blocks[key]]
    ratio_stack = [r for key in seed_keys for r in ratios[key]]
    assert direct.rank_and_rows(stack)[0] == independent.column_rank(stack)[0]
    records, failures = [], []
    counts, linear_counts = Counter(), Counter()
    for i, k in expected:
        matrix = stack+blocks[i, k]
        rank, rows = direct.rank_and_rows(matrix)
        other_rank, pivots = independent.column_rank(matrix)
        assert rank == other_rank
        intersections = [len(set(i+k) & a) for a in seed_sets]
        linear = all(n <= 1 for n in intersections)
        rec = {'I': list(i), 'K': list(k), 'seed_intersections': intersections,
               'pairwise_linear': linear, 'rank': rank,
               'pivot_columns': pivots, 'kernel_dimension': 21-rank,
               'kernel_basis': []}
        if rank == 21:
            minor = [matrix[r] for r in rows]
            det = direct.determinant(minor)
            integer_det = independent.integer_det(minor)
            assert integer_det % P == det != 0
            rec.update(minor_row_indices=rows, minor_residue=det,
                       integer_minor_determinant=integer_det)
        else:
            kernel_pivots, basis = kernels.rref_kernel(ratio_stack+ratios[i, k])
            assert pivots == kernel_pivots and len(basis) == 21-rank
            free = sorted(set(range(21))-set(pivots))
            assert [[v[c] for c in free] for v in basis] == [
                [int(a == b) for b in range(len(free))] for a in range(len(free))]
            residuals = [[sum(x*y for x, y in zip(r, v)) % P for r in matrix]
                         for v in basis]
            assert not any(map(any, residuals))
            rec.update(kernel_basis=basis, kernel_residuals=residuals)
            if linear:
                rec['plucker_system'] = homogeneous_plucker(basis)
                all_rows = [{'I': a, 'K': b} for a, b in SEED]+[{'I': list(i), 'K': list(k)}]
                if len(basis) == 1:
                    decomposable = not any(q[0] for q in rec['plucker_system']['coefficients'])
                    rec['point_is_decomposable'] = decomposable
                    if decomposable:
                        rec['point_gates'] = point_gates.plane_gates(basis[0], all_rows)
                        rec['gate_status'] = ('intrinsic_point_survivor' if rec['point_gates']['passes_intrinsic_gates']
                                              else 'excluded_point_gates')
                    else:
                        rec['gate_status'] = 'excluded_point_plucker'
                else:
                    rec['algebraic_gate_system'] = algebraic_charts(basis, all_rows, rec['plucker_system'])
                    rec['gate_status'] = rec['algebraic_gate_system']['status']
        records.append(rec)
        counts[rank] += 1
        if linear:
            linear_counts[rank] += 1
    actual = [(tuple(r['I']), tuple(r['K'])) for r in records]
    assert len(actual) == len(set(actual)) == 756 and set(actual) == set(expected)
    summary = {'actual_fourth_supports': len(records), 'required_fourth_supports': 756,
               'seed_rank': direct.rank_and_rows(stack)[0],
               'all_rank_histogram': dict(sorted(counts.items())),
               'pairwise_linear_cases': sum(linear_counts.values()),
               'linear_rank_histogram': dict(sorted(linear_counts.items())),
               'linear_deficient_cases': sum(n for r, n in linear_counts.items() if r < 21),
               'required_exclusion_rank': 21}
    gated = [r for r in records if r['pairwise_linear'] and r['rank'] < 21]
    for rec in gated:
        rec['kernel_supported_on_label_one_pairs'] = all(
            all(not v[n] for n, (a, b) in enumerate(PAIRS) if a != 0)
            for v in rec['kernel_basis'])
        assert rec['kernel_supported_on_label_one_pairs']
    summary.update(gate_status_counts=dict(Counter(r['gate_status'] for r in gated)),
                   complete_kernels_supported_on_label_one_pairs=sum(
                       r['kernel_supported_on_label_one_pairs'] for r in gated),
                   required_deficient_kernel_gate_exclusions=len(gated),
                   unresolved_case_indices=[j for j, r in enumerate(records) if r.get('gate_status') == 'unresolved'],
                   intrinsic_point_survivor_indices=[j for j, r in enumerate(records)
                                                      if r.get('gate_status') == 'intrinsic_point_survivor'])
    out = {'modulus': P, 'H': H, 'S': S, 'J': J,
           'seed': [{'I': i, 'K': k} for i, k in SEED],
           'column_pairs': [[S[a], S[b]] for a, b in PAIRS],
           'scope': 'one named nondisjoint third; necessary four-row gates only',
           'summary': summary, 'cases': records, 'failures': failures}
    path = HERE/'nondisjoint-third-diagnostic.json'
    path.write_text(json.dumps(out, indent=2)+'\n')
    print(json.dumps(summary, sort_keys=True))
    print(f'Failures: {len(failures)}; full certificate: {path}')


if __name__ == '__main__':
    run()
