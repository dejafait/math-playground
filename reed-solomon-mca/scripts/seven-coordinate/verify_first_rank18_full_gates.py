"""Independent same-step replay of one rank-18 locus (no producer imports).

Uses the prior independent derivative/ratio block and integer-elimination
utilities, with separate determining-coefficient gate and moment checks.
Run: python3 scripts/seven-coordinate/verify_first_rank18_full_gates.py
"""
from collections import Counter
from hashlib import sha256
from itertools import combinations
from pathlib import Path
import json

import verify_nondisjoint_third_diagnostic as independent

P = 97
HERE = Path(__file__).resolve().parent
S = [1, 8, 12, 18, 22, 27, 33]
H = sorted({pow(8, j, P) for j in range(16)})
J = sorted(set(H)-set(S))
ROWS = [{'I': i, 'K': k} for i, k in [
    ([1, 8], [47, 50]), ([12, 18], [64, 70]),
    ([1, 12], [75, 79]), ([8, 12], [85, 89])]]
PAIRS = list(combinations(range(7), 2))
QUADS = list(combinations(range(7), 4))
MONOMIALS = [(a, b) for a in range(3) for b in range(a, 3)]
UNIT = [[int(a == b) for b in range(3)] for a in range(3)]
PROBES = UNIT+[[a+b for a, b in zip(UNIT[i], UNIT[j])] for i, j in combinations(range(3), 2)]


def dot(a, b):
    assert len(a) == len(b)
    return sum(x*y for x, y in zip(a, b)) % P


def linear(f, t):
    return dot(f, t)


def quadratic(f, t):
    return dot(f, [t[a]*t[b] % P for a, b in MONOMIALS])


def run():
    path = HERE/'first-rank18-full-gates.json'
    raw = path.read_bytes()
    saved = json.loads(raw)
    assert saved['failures'] == []
    assert saved['modulus'] == P and saved['H'] == H and saved['S'] == S and saved['J'] == J
    assert saved['rows'] == ROWS and saved['column_pairs'] == [[S[a], S[b]] for a, b in PAIRS]
    supports = [set(r['I']+r['K']) for r in ROWS]
    assert len({tuple(sorted(v)) for v in supports}) == 4
    assert all(len(a & b) <= 1 for a, b in combinations(supports, 2))
    source_raw = (HERE/saved['source']['path']).read_bytes()
    assert sha256(source_raw).hexdigest() == saved['source']['sha256']
    source = json.loads(source_raw)
    assert source['summary']['third_I'] == ROWS[2]['I'] and source['summary']['third_K'] == ROWS[2]['K']
    old = source['cases'][249]
    assert saved['source']['pointer'] == '/cases/249'
    assert old['I'] == ROWS[3]['I'] and old['K'] == ROWS[3]['K']
    assert old['eligible'] and old['intersections'] == [1, 1, 1]
    rebuilt = [independent.block(row['I'], row['K']) for row in ROWS]
    original = [[(a[x]*b[y]-a[y]*b[x]) % P for x, y in PAIRS]
                for _, q, _ in rebuilt for a, b in combinations(q, 2)]
    assert original == saved['original_matrix'] and len(original) == 24
    ratio = [r for _, _, block in rebuilt for r in block]
    pivots, basis = independent.nullspace(ratio)
    assert len(pivots) == 18 and pivots == old['pivot_columns'] == saved['pivot_columns']
    assert basis == old['kernel_basis'] == saved['kernel_basis'] and len(basis) == 3
    free = sorted(set(range(21))-set(pivots))
    assert [[v[c] for c in free] for v in basis] == UNIT
    residuals = [[dot(v, row) for row in original] for v in basis]
    assert residuals == old['kernel_residuals'] == saved['kernel_residuals']
    assert not any(map(any, residuals))
    minor_rows, minor_cols = saved['rank_minor_rows'], saved['rank_minor_columns']
    assert len(minor_rows) == len(set(minor_rows)) == len(minor_cols) == 18
    assert all(0 <= r < 24 for r in minor_rows) and minor_cols == pivots
    minor_residue = independent.integer_det([[original[r][c] for c in minor_cols] for r in minor_rows]) % P
    assert minor_residue == saved['rank_minor_residue'] != 0
    factor = S.index(saved['common_coordinate_factor'])
    assert S[factor] == 12
    assert all(v[n] == 0 for v in basis for n, pair in enumerate(PAIRS) if factor not in pair)
    system, gates = saved['plucker_system'], saved['algebraic_gate_system']
    assert system['kernel_coordinate_monomials'] == gates['quadratic_monomials'] == [list(m) for m in MONOMIALS]
    assert system['label_quadruples'] == [[S[x] for x in q] for q in QUADS]
    assert gates['coordinate_variables'] == ['b0', 'b1', 'b2']
    coords = [[v[n] for v in basis] for n in range(21)]
    assert coords == gates['bivector_coordinate_linear_forms']
    generators = system['coefficients']
    assert len(generators) == 35 and all(len(q) == 6 for q in generators)
    assert not any(map(any, generators))
    for t in PROBES:
        p = [linear(c, t) for c in coords]
        assert [quadratic(q, t) for q in generators] == independent.plucker_values(p)
    counts = Counter()

    def identity(f, cert):
        assert cert is not None and len(cert) == 35
        assert [sum(c*g[m] for c, g in zip(cert, generators)) % P for m in range(6)] == f
        counts['exact_original_generator_identities'] += 1

    assert len(gates['charts']) == 21
    for n, ((a, b), chart) in enumerate(zip(PAIRS, gates['charts'])):
        assert chart['pivot_labels'] == [S[a], S[b]] and chart['pivot_linear_form'] == coords[n]
        if not any(coords[n]):
            assert chart['status'] == 'empty_pivot_chart' and chart['rows'] == []
            counts['empty_charts'] += 1
            continue
        counts['nonempty_charts'] += 1
        assert len(chart['rows']) == 4
        for row, record, (values, q, _) in zip(ROWS, chart['rows'], rebuilt):
            i, k = row['I'], row['K']
            assert record['I'] == i and record['K'] == k
            z = min(set(S)-set(i))
            assert record['g_pivot'] == values[z] != 0
            assert record['rank_zero_branch'] == {
                'all_zero_linear_forms': record['Q_U_linear_forms']+record['Q_V_linear_forms'],
                'status': 'rejected_by_actual_nonpersistence_L109'}
            assert len(record['projection_minor_quadrics']) == len(record['projection_minor_plucker_identities']) == 6
            for f, cert in zip(record['projection_minor_quadrics'], record['projection_minor_plucker_identities']):
                identity(f, cert)
            assert len(record['branches']) == 4
            for r, branch in enumerate(record['branches']):
                assert branch['quotient_row_index'] == r
                assert branch['weight_names'] == ['lambda']+[f'overlap_at_{x}' for x in i]
                assert len(branch['quotient_residual_quadrics']) == len(branch['quotient_residual_plucker_identities']) == 4
                for f, cert in zip(branch['quotient_residual_quadrics'], branch['quotient_residual_plucker_identities']):
                    identity(f, cert)
                assert len(branch['weight_numerator_quadrics']) == len(branch['zero_weight_plucker_identities']) == 3
                for f, cert in zip(branch['weight_numerator_quadrics'], branch['zero_weight_plucker_identities']):
                    if cert is None:
                        assert any(f)
                    else:
                        identity(f, cert)
                no_pivot = not any(record['Q_U_linear_forms'][r]+record['Q_V_linear_forms'][r])
                first_zero = next((j for j, f in enumerate(branch['weight_numerator_quadrics']) if not any(f)), None)
                assert branch['first_identically_zero_weight'] == first_zero
                assert branch['status'] == ('empty_projection_pivot' if no_pivot else
                    'excluded_zero_weight_identity' if first_zero is not None else 'unresolved')
                assert branch['error_label_order'] == i+k
                moments = branch['original_shifted_moment_residual_quadrics']
                assert len(moments) == 8 and all(len(f) == 6 for f in moments)
                assert not any(map(any, moments))
                counts['moment_coefficients_checked'] += 48
                counts['row_projection_pivots'] += 1
            assert record['row_all_branches_excluded'] == all(b['status'] != 'unresolved' for b in record['branches'])
            # Linear forms and homogeneous quadrics are completely determined
            # by these six exact evaluations: coefficients are f(e_i) and
            # f(e_i+e_j)-f(e_i)-f(e_j). No point-sampling inference is used.
            for t in PROBES:
                p = [linear(c, t) for c in coords]
                alt = independent.alternating(p)
                u, v = [alt[x][b] for x in range(7)], alt[a]
                assert [linear(f, t) for f in chart['U_linear_forms']] == u
                assert [linear(f, t) for f in chart['V_linear_forms']] == v
                assert [(u[x]*v[y]-u[y]*v[x]) % P for x, y in PAIRS] == [p[n]*w % P for w in p]
                qu, qv = [dot(c, u) for c in q], [dot(c, v) for c in q]
                assert [linear(f, t) for f in record['Q_U_linear_forms']] == qu
                assert [linear(f, t) for f in record['Q_V_linear_forms']] == qv
                assert [quadratic(f, t) for f in record['projection_minor_quadrics']] == [
                    (qu[x]*qv[y]-qu[y]*qv[x]) % P for x, y in combinations(range(4), 2)]
                for r, branch in enumerate(record['branches']):
                    alpha, beta = -qv[r] % P, qu[r]
                    h = [(alpha*x+beta*y) % P for x, y in zip(u, v)]
                    assert [linear(f, t) for f in branch['projection_pivot_nonzero_alternatives']] == [qu[r], qv[r]]
                    assert linear(branch['alpha_linear_form'], t) == alpha
                    assert linear(branch['beta_linear_form'], t) == beta
                    assert linear(branch['finite_gate_D_coefficient'], t) == alpha
                    assert linear(branch['finite_gate_C_coefficient'], t) == -beta % P
                    assert [quadratic(f, t) for f in branch['intersection_vector_quadrics']] == h
                    assert [quadratic(f, t) for f in branch['quotient_residual_quadrics']] == [dot(c, h) for c in q]
                    lam = h[S.index(z)]*pow(values[z], -1, P) % P
                    numerators = [h[S.index(z)]]+[(values[z]*h[S.index(x)]-values[x]*h[S.index(z)]) % P for x in i]
                    assert [quadratic(f, t) for f in branch['weight_numerator_quadrics']] == numerators
                    assert quadratic(branch['lambda_quadratic'], t) == lam
                    error = {x: (h[S.index(x)]-lam*values[x]) % P for x in i}
                    error.update({x: -lam*values[x] % P for x in k})
                    assert [quadratic(f, t) for f in branch['error_weight_quadrics']] == [error[x] for x in i+k]
                    actual = [sum(((h[S.index(x)] if x in S else 0)-error.get(x, 0))*pow(x, d, P) for x in H) % P for d in range(1, 9)]
                    assert actual == [quadratic(f, t) for f in branch['original_shifted_moment_residual_quadrics']] == [0]*8
                    counts['determining_branch_evaluations'] += 1
        second = chart['rows'][1]
        assert second['row_all_branches_excluded']
        for branch in second['branches']:
            assert not any(branch['weight_numerator_quadrics'][0])
            assert not any(branch['weight_numerator_quadrics'][2])
        assert chart['status'] == 'excluded_by_row'
        assert chart['excluded_row'] == next(j for j, r in enumerate(chart['rows']) if r['row_all_branches_excluded'])
    assert counts['empty_charts'] == 15 and counts['nonempty_charts'] == 6
    assert counts['row_projection_pivots'] == 96 and counts['moment_coefficients_checked'] == 4608
    assert gates['status'] == 'excluded_all_charts' and gates['unresolved_chart_indices'] == []
    assert saved['summary'] == {
        'actual_loci': 1, 'required_loci': 1, 'rank': 18, 'kernel_dimension': 3,
        'basis_residuals': 72, 'plucker_equations': 35, 'projective_charts': 21,
        'empty_charts': 15, 'nonempty_charts': 6, 'row_projection_pivots': 96,
        'nonzero_alternatives': 192, 'moment_coefficients': 4608,
        'unresolved_charts': 0, 'excluded_row_number': 2}
    output = {'source_sha256': sha256(raw).hexdigest(), 'summary': dict(counts),
              'rank_minor_residue': minor_residue,
              'rank': 18, 'complete_basis_vectors': 3, 'basis_residuals': 72,
              'common_coordinate_factor': 12, 'excluded_loci': 1,
              'required_loci': 1, 'failures': [],
              'scope': 'Independent same-step exact replay, not a separate critical audit.'}
    out = HERE/'first-rank18-full-gates-replay.json'
    out.write_text(json.dumps(output, indent=2)+'\n')
    print(json.dumps(output['summary'], sort_keys=True))
    print(f'Excluded loci: 1/1; complete basis: 3/3; original residuals: 72/72; failures: 0; replay: {out}')


if __name__ == '__main__':
    run()
