"""Same-step independent replay of the named-third diagnostic.

No producer imports. Full kernels, all chart coefficient identities, every
point gate and complete support coverage are checked, not sampled.
Run: python3 scripts/seven-coordinate/verify_nondisjoint_third_diagnostic.py
"""
from collections import Counter
from hashlib import sha256
from itertools import combinations, product
from pathlib import Path
import json

P = 97
H = sorted({pow(8, j, P) for j in range(16)})
S = [1, 8, 12, 18, 22, 27, 33]
J = sorted(set(H)-set(S))
PAIRS = list(combinations(range(7), 2))
INDEX = {q: n for n, q in enumerate(PAIRS)}
QUADS = list(combinations(range(7), 4))
SEED = [([1, 8], [47, 50]), ([12, 18], [64, 70]), ([1, 22], [75, 79])]
HERE = Path(__file__).resolve().parent


def dot(a, b):
    return sum(x*y for x, y in zip(a, b)) % P


def forward(matrix):
    a = [row[:] for row in matrix]
    pivots = []
    for col in range(len(a[0])):
        n = len(pivots)
        pivot = next((k for k in range(n, len(a)) if a[k][col]), None)
        if pivot is None:
            continue
        a[n], a[pivot] = a[pivot], a[n]
        inv = pow(a[n][col], -1, P)
        a[n] = [v*inv % P for v in a[n]]
        for k in range(n+1, len(a)):
            factor = a[k][col]
            a[k] = [(x-factor*y) % P for x, y in zip(a[k], a[n])]
        pivots.append(col)
    return a, pivots


def nullspace(matrix):
    a, pivots = forward(matrix)
    free = sorted(set(range(len(a[0])))-set(pivots))
    basis = []
    for c in free:
        v = [0]*len(a[0])
        v[c] = 1
        for n in reversed(range(len(pivots))):
            col = pivots[n]
            v[col] = -sum(a[n][j]*v[j] for j in range(col+1, len(v))) % P
        basis.append(v)
    return pivots, basis


def integer_det(matrix):
    a = [row[:] for row in matrix]
    previous, sign = 1, 1
    for n in range(len(a)-1):
        pivot = next((k for k in range(n, len(a)) if a[k][n]), None)
        if pivot is None:
            return 0
        if pivot != n:
            a[n], a[pivot] = a[pivot], a[n]
            sign = -sign
        value = a[n][n]
        for i in range(n+1, len(a)):
            for j in range(n+1, len(a)):
                numerator = a[i][j]*value-a[i][n]*a[n][j]
                q, r = divmod(numerator, previous)
                assert r == 0
                a[i][j] = q
            a[i][n] = 0
        previous = value
    return sign*a[-1][-1]


def block(i, k):
    # Independent derivative construction; also check the direct polynomial on H.
    coeff = [1]
    for root in sorted(set(J)-set(k)):
        new = [0]*(len(coeff)+1)
        for j, c in enumerate(coeff):
            new[j] = (new[j]-root*c) % P
            new[j+1] = (new[j+1]+c) % P
        coeff = new
    values = {}
    for x in H:
        value = 0
        for c in reversed(coeff):
            value = (value*x+c) % P
        values[x] = value
        assert (value != 0) == (x in S+list(k))
        if value:
            denominator = 1
            for y in S+list(k):
                if y != x:
                    denominator = denominator*(x-y) % P
            assert value == 16*pow(x, 15, P)*pow(denominator, -1, P) % P
    observed = sorted(set(S)-set(i))
    z = observed[-1]
    # Ratio quotients and greatest pivot differ from the producer's Q.
    ratios = [[(int(x == t)*pow(values[t], -1, P)
                -int(x == z)*pow(values[z], -1, P)) % P for x in S]
              for t in observed[:-1]]
    exterior = [[(u[a]*v[b]-u[b]*v[a]) % P for a, b in PAIRS]
                for u, v in combinations(ratios, 2)]
    # Original-order covectors only for comparing the saved polynomial systems.
    low = observed[0]
    q = [[(values[low]*int(label == x)-values[x]*int(label == low)) % P
          for label in S] for x in observed[1:]]
    return values, q, exterior


def alternating(p):
    a = [[0]*7 for _ in range(7)]
    for (i, j), value in zip(PAIRS, p):
        a[i][j], a[j][i] = value, -value % P
    return a


def plucker_values(p):
    return [(p[INDEX[a, b]]*p[INDEX[c, d]]-p[INDEX[a, c]]*p[INDEX[b, d]]
             +p[INDEX[a, d]]*p[INDEX[b, c]]) % P for a, b, c, d in QUADS]


def quadratic_value(coefficients, monomials, variables):
    return sum(c*variables[a]*variables[b] for c, (a, b) in zip(coefficients, monomials)) % P


def check_algebraic(record, rows, rebuilt, counts):
    basis = record['kernel_basis']
    dimension = len(basis)
    assert dimension == 3
    saved = record['algebraic_gate_system']
    system = record['plucker_system']
    monomials = [tuple(m) for m in system['kernel_coordinate_monomials']]
    assert monomials == sorted((a, b) for a in range(dimension) for b in range(a, dimension))
    unit = [[int(j == i) for j in range(dimension)] for i in range(dimension)]
    probes = unit+[[x+y for x, y in zip(unit[a], unit[b])] for a, b in combinations(range(dimension), 2)]
    # These exact evaluations determine EVERY homogeneous quadratic coefficient.
    # Diagonals are f(e_i); mixed coefficients are f(e_i+e_j)-f(e_i)-f(e_j).
    coordinates = [[b[j] for b in basis] for j in range(21)]
    assert saved['bivector_coordinate_linear_forms'] == coordinates
    assert saved['quadratic_monomials'] == [list(m) for m in monomials]
    assert saved['coordinate_variables'] == ['b0', 'b1', 'b2']
    assert system['label_quadruples'] == [[S[a] for a in q] for q in QUADS]
    generators = system['coefficients']
    assert len(generators) == 35 and not any(map(any, generators))

    def quadratic(coeff, variables):
        assert len(coeff) == len(monomials)
        return quadratic_value(coeff, monomials, variables)

    def identity(target, certificate):
        assert certificate is not None and len(certificate) == 35
        assert [sum(c*q[n] for c, q in zip(certificate, generators)) % P
                for n in range(len(monomials))] == target
        counts['polynomial_identities_checked'] += 1

    charts = saved['charts']
    assert len(charts) == 21
    for (a, b), chart in zip(PAIRS, charts):
        assert chart['pivot_labels'] == [S[a], S[b]]
        assert chart['pivot_linear_form'] == coordinates[INDEX[a, b]]
        if not any(coordinates[INDEX[a, b]]):
            assert chart['status'] == 'empty_pivot_chart' and chart['rows'] == []
            counts['empty_pivot_charts'] += 1
            continue
        counts['nonempty_pivot_charts'] += 1
        assert len(chart['rows']) == 4
        for j, (row, data) in enumerate(zip(rows, chart['rows'])):
            values, q, _ = rebuilt[tuple(row['I']), tuple(row['K'])]
            i, k = row['I'], row['K']
            assert data['I'] == i and data['K'] == k
            z = S.index(min(set(S)-set(i)))
            assert data['g_pivot'] == values[S[z]]
            assert len(data['branches']) == 4
            for f, cert in zip(data['projection_minor_quadrics'], data['projection_minor_plucker_identities']):
                identity(f, cert)
            for n, branch in enumerate(data['branches']):
                assert branch['quotient_row_index'] == n
                assert branch['weight_names'] == ['lambda']+[f'overlap_at_{x}' for x in i]
                for f, cert in zip(branch['quotient_residual_quadrics'], branch['quotient_residual_plucker_identities']):
                    identity(f, cert)
                for f, cert in zip(branch['weight_numerator_quadrics'], branch['zero_weight_plucker_identities']):
                    if cert is not None:
                        identity(f, cert)
                    else:
                        # Here every generator is zero: no nonzero target is in their span.
                        assert any(f)
                no_pivot = not any(data['Q_U_linear_forms'][n]+data['Q_V_linear_forms'][n])
                first_zero = next((m for m, f in enumerate(branch['weight_numerator_quadrics']) if not any(f)), None)
                expected = ('empty_projection_pivot' if no_pivot else
                            'excluded_zero_weight_identity' if first_zero is not None else 'unresolved')
                assert branch['status'] == expected
                assert branch['first_identically_zero_weight'] == first_zero
                counts['symbolic_row_pivot_branches_checked'] += 1
            assert data['row_all_branches_excluded'] == all(b['status'] != 'unresolved' for b in data['branches'])
            for variables in probes:
                p = [dot(c, variables) for c in coordinates]
                alt = alternating(p)
                u, v = [alt[x][b] for x in range(7)], alt[a][:]
                assert [dot(c, variables) for c in chart['U_linear_forms']] == u
                assert [dot(c, variables) for c in chart['V_linear_forms']] == v
                assert [quadratic(f, variables) for f in generators] == plucker_values(p)
                qu, qv = [dot(c, u) for c in q], [dot(c, v) for c in q]
                assert [dot(c, variables) for c in data['Q_U_linear_forms']] == qu
                assert [dot(c, variables) for c in data['Q_V_linear_forms']] == qv
                expected_minors = [(qu[r]*qv[s]-qu[s]*qv[r]) % P for r, s in combinations(range(4), 2)]
                assert [quadratic(f, variables) for f in data['projection_minor_quadrics']] == expected_minors
                for n, branch in enumerate(data['branches']):
                    alpha, beta = -qv[n] % P, qu[n]
                    h = [(alpha*x+beta*y) % P for x, y in zip(u, v)]
                    assert [dot(c, variables) for c in branch['projection_pivot_nonzero_alternatives']] == [qu[n], qv[n]]
                    assert dot(branch['alpha_linear_form'], variables) == alpha
                    assert dot(branch['beta_linear_form'], variables) == beta
                    assert dot(branch['finite_gate_D_coefficient'], variables) == alpha
                    assert dot(branch['finite_gate_C_coefficient'], variables) == -beta % P
                    assert [quadratic(f, variables) for f in branch['intersection_vector_quadrics']] == h
                    assert [quadratic(f, variables) for f in branch['quotient_residual_quadrics']] == [dot(c, h) for c in q]
                    weight_numerators = [h[z]]+[(values[S[z]]*h[S.index(label)]-values[label]*h[z]) % P for label in i]
                    assert [quadratic(f, variables) for f in branch['weight_numerator_quadrics']] == weight_numerators
                    counts['determining_polynomial_evaluations_checked'] += 1
        assert chart['status'] == 'excluded_by_row' and chart['excluded_row'] == 0
        assert chart['rows'][0]['row_all_branches_excluded']
        assert all(b['status'] == 'empty_projection_pivot' or b['first_identically_zero_weight'] == 0
                   for b in chart['rows'][0]['branches'])
    assert saved['status'] == record['gate_status'] == 'excluded_all_charts'
    assert saved['unresolved_chart_indices'] == []


def check_point(record, rows, rebuilt, counts):
    p = record['kernel_basis'][0]
    assert not any(plucker_values(p)) and record['point_is_decomposable']
    saved = record['point_gates']
    u, v = saved['u'], saved['v']
    assert saved['bivector'] == p
    assert [(u[a]*v[b]-u[b]*v[a]) % P for a, b in PAIRS] == p
    assert len(saved['row_gates']) == 4
    for row, gate in zip(rows, saved['row_gates']):
        i, k = row['I'], row['K']
        values, q, _ = rebuilt[tuple(i), tuple(k)]
        qu, qv = [dot(c, u) for c in q], [dot(c, v) for c in q]
        assert gate['Q_u'] == qu and gate['Q_v'] == qv
        assert gate['projection_minors'] == [(qu[a]*qv[b]-qu[b]*qv[a]) % P for a, b in combinations(range(4), 2)] == [0]*6
        projection_rank = int(any(qu+qv))
        assert gate['projection_rank'] == projection_rank
        if not projection_rank:
            assert gate['failed_gates'] == ['projection_rank_zero'] and not gate['passes']
            continue
        observed = sorted(set(S)-set(i))
        # Solve the original five evaluation equations, not the quotient pivot formula.
        augmented = [[u[S.index(x)], v[S.index(x)], -values[x] % P] for x in observed]
        _, solutions = nullspace(augmented)
        assert len(solutions) == 1
        alpha, beta = gate['direction_coefficients']
        h = [(alpha*x+beta*y) % P for x, y in zip(u, v)]
        assert any(h) and h == gate['intersection_vector']
        lam = gate['lambda_value']
        actual = [alpha, beta, lam]
        solution = solutions[0]
        assert all(dot(r, actual) == 0 for r in augmented)
        assert all((actual[a]*solution[b]-actual[b]*solution[a]) % P == 0 for a, b in combinations(range(3), 2))
        error = {x: (h[S.index(x)]-lam*values[x]) % P for x in i}
        error.update({x: -lam*values[x] % P for x in k})
        assert gate['overlap_weights'] == [error[x] for x in i]
        assert gate['error_weights'] == [error[x] for x in i+k]
        residuals = [sum(((h[S.index(x)] if x in S else 0)-error.get(x, 0))*pow(x, d, P) for x in H) % P for d in range(1, 9)]
        assert gate['moment_residuals'] == residuals == [0]*8
        failed = (['lambda_zero'] if not lam else [])+[f'overlap_weight_zero_at_{x}' for x in i if not error[x]]
        assert gate['failed_gates'] == failed and gate['passes'] == (not failed)
        assert gate['prescribed_finite_gate'] == {'D_coefficient': alpha, 'C_coefficient': -beta % P}
        counts['point_projection_rows_checked'] += 1
        counts['full_moment_residuals_checked'] += 8
    assert saved['row_gates'][0]['projection_rank'] == 1 and saved['row_gates'][0]['lambda_value'] == 0
    assert not saved['passes_intrinsic_gates'] and record['gate_status'] == 'excluded_point_gates'


def run():
    path = HERE/'nondisjoint-third-diagnostic.json'
    raw = path.read_bytes()
    source = json.loads(raw)
    assert H == [x for x in range(1, P) if pow(x, 16, P) == 1]
    assert source['modulus'] == P and source['H'] == H and source['S'] == S and source['J'] == J
    assert source['seed'] == [{'I': i, 'K': k} for i, k in SEED]
    assert source['column_pairs'] == [[S[a], S[b]] for a, b in PAIRS]
    expected = set(product(combinations(S, 2), combinations(J, 2)))
    cases = source['cases']
    actual = [(tuple(r['I']), tuple(r['K'])) for r in cases]
    assert len(cases) == len(set(actual)) == 756 and set(actual) == expected
    rebuilt = {key: block(*key) for key in expected}
    seed = [r for i, k in SEED for r in rebuilt[tuple(i), tuple(k)][2]]
    assert len(forward(seed)[1]) == source['summary']['seed_rank'] == 17
    seed_sets = [set(i+k) for i, k in SEED]
    ranks, linear_ranks, counts = Counter(), Counter(), Counter()
    results = []
    for number, record in enumerate(cases):
        i, k = record['I'], record['K']
        matrix = seed+rebuilt[tuple(i), tuple(k)][2]
        pivots, basis = nullspace(matrix)
        rank = len(pivots)
        assert rank == record['rank'] and pivots == record['pivot_columns']
        assert basis == record['kernel_basis'] and len(basis) == record['kernel_dimension'] == 21-rank
        intersections = [len(set(i+k) & a) for a in seed_sets]
        linear = max(intersections) <= 1
        assert intersections == record['seed_intersections'] and linear == record['pairwise_linear']
        if rank == 21:
            # Saved minor refers to producer's direct-order rows, so rebuild those.
            original = []
            for a, b in SEED+[(i, k)]:
                q = rebuilt[tuple(a), tuple(b)][1]
                original += [[(u[x]*v[y]-u[y]*v[x]) % P for x, y in PAIRS]
                             for u, v in combinations(q, 2)]
            indices = record['minor_row_indices']
            assert len(indices) == len(set(indices)) == 21 and all(0 <= n < 24 for n in indices)
            determinant = integer_det([original[n] for n in indices])
            assert determinant == record['integer_minor_determinant']
            assert determinant % P == record['minor_residue'] != 0
            counts['exact_full_rank_minors_checked'] += 1
        else:
            assert all(not dot(row, v) for row in matrix for v in basis)
            counts['complete_deficient_kernels_checked'] += 1
            counts['complete_kernel_vectors_checked'] += len(basis)
            if linear:
                # This full basis identity controls arbitrary extension-field points.
                assert all(not v[j] for v in basis for j, (a, b) in enumerate(PAIRS) if a != 0)
                assert record['kernel_supported_on_label_one_pairs']
                counts['linear_kernels_with_coordinate_factor_checked'] += 1
                rows = [{'I': a, 'K': b} for a, b in SEED]+[{'I': i, 'K': k}]
                if len(basis) == 1:
                    check_point(record, rows, rebuilt, counts)
                else:
                    check_algebraic(record, rows, rebuilt, counts)
        ranks[rank] += 1
        if linear:
            linear_ranks[rank] += 1
        results.append({'case_index': number, 'I': i, 'K': k, 'rank': rank,
                        'complete_basis_verified': True, 'linear': linear,
                        'gate_status': record.get('gate_status', 'rank_or_incidence_excluded')})
    assert dict(ranks) == {int(k): v for k, v in source['summary']['all_rank_histogram'].items()}
    assert dict(linear_ranks) == {int(k): v for k, v in source['summary']['linear_rank_histogram'].items()}
    statuses = Counter(r['gate_status'] for r in cases if r['pairwise_linear'] and r['rank'] < 21)
    assert dict(statuses) == source['summary']['gate_status_counts'] == {'excluded_point_gates': 112, 'excluded_all_charts': 24}
    assert source['summary']['unresolved_case_indices'] == source['summary']['intrinsic_point_survivor_indices'] == source['failures'] == []
    assert counts['linear_kernels_with_coordinate_factor_checked'] == 136
    summary = {'actual_cases': len(results), 'required_cases': 756,
               'pairwise_linear_cases': sum(linear_ranks.values()),
               'required_linear_cases': 254, 'linear_rank_histogram': dict(sorted(linear_ranks.items())),
               **dict(counts), 'required_excluded_linear_deficient_cases': 136,
               'unresolved_cases': 0, 'surviving_cases': 0}
    output = {'source_sha256': sha256(raw).hexdigest(),
              'scope': 'same-step independent coefficient and complete-case replay; no separate critical audit',
              'summary': summary, 'cases': results, 'failures': []}
    target = HERE/'nondisjoint-third-diagnostic-replay.json'
    target.write_text(json.dumps(output, indent=2)+'\n')
    print(json.dumps(summary, sort_keys=True))
    print(f'Failures: 0; full replay: {target}')


if __name__ == '__main__':
    run()
