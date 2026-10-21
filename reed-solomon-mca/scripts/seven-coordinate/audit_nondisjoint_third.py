"""Step-309 supplement: direct polynomial coefficients and complete moment bridges.

Run after the reviewed producer and independent replay. No producer imports.
This supplements their full rank replay; it is not a replacement rank census.
"""
from collections import Counter
from hashlib import sha256
from itertools import combinations
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent
P = 97
S = [1, 8, 12, 18, 22, 27, 33]
H = [x for x in range(1, P) if pow(x, 16, P) == 1]
J = sorted(set(H)-set(S))
PAIRS = list(combinations(range(7), 2))
INDEX = {pair: n for n, pair in enumerate(PAIRS)}
SEED = [([1, 8], [47, 50]), ([12, 18], [64, 70]), ([1, 22], [75, 79])]


def add(*vectors):
    assert len({len(v) for v in vectors}) == 1
    return [sum(column) % P for column in zip(*vectors)]


def scale(c, v):
    return [c*x % P for x in v]


def run():
    before = json.loads((ROOT.parent.parent/'drafts/2026-10-18-nondisjoint-third-audit-before.json').read_text())
    hashes = {name: sha256((ROOT.parent.parent/name).read_bytes()).hexdigest() for name in before}
    assert hashes == before, 'Producer/replay evidence changed'
    source = json.loads((ROOT/'nondisjoint-third-diagnostic.json').read_text())
    counts = Counter()
    cases = []
    for number, case in enumerate(source['cases']):
        rows = SEED+[(case['I'], case['K'])]
        blocks = []
        for i, k in rows:
            g = {}
            for x in H:
                value = 1
                for y in J:
                    if y not in k:
                        value = value*(x-y) % P
                g[x] = value
            observed = sorted(set(S)-set(i))
            z = observed[0]
            assert all(g[x] for x in S+list(k))
            q = [[(g[z]*int(t == x)-g[x]*int(t == z)) % P for t in S]
                 for x in observed[1:]]
            block = [[(u[a]*v[b]-u[b]*v[a]) % P for a, b in PAIRS]
                     for u, v in combinations(q, 2)]
            blocks.append((i, k, z, g, q, block))
        basis = case['kernel_basis']
        assert len(basis) == 21-case['rank'] and all(len(v) == 21 for v in basis)
        if basis:
            matrix = [row for data in blocks for row in data[5]]
            residuals = [[sum(x*y for x, y in zip(row, v)) % P for row in matrix] for v in basis]
            assert residuals == case['kernel_residuals'] and not any(map(any, residuals))
            free = sorted(set(range(21))-set(case['pivot_columns']))
            assert [[v[c] for c in free] for v in basis] == [[int(a == b) for b in range(len(basis))] for a in range(len(basis))]
            counts['complete_saved_basis_residuals_checked'] += len(basis)*24
        if not case['pairwise_linear'] or not basis:
            continue
        dimension = len(basis)
        monomials = [(a, b) for a in range(dimension) for b in range(a, dimension)]
        zero = [0]*len(monomials)
        coordinates = [[v[j] for v in basis] for j in range(21)]

        def p(a, b):
            if a == b:
                return [0]*dimension
            return coordinates[INDEX[a, b]] if a < b else scale(-1, coordinates[INDEX[b, a]])

        def mul(u, v):
            assert len(u) == len(v) == dimension
            # Full ordered convolution, then collect commutative monomials.
            result = dict.fromkeys(monomials, 0)
            for a in range(dimension):
                for b in range(dimension):
                    key = tuple(sorted((a, b)))
                    result[key] = (result[key]+u[a]*v[b]) % P
            return [result[key] for key in monomials]

        plucker = [add(mul(p(a,b), p(c,d)), scale(-1, mul(p(a,c), p(b,d))), mul(p(a,d), p(b,c)))
                   for a,b,c,d in combinations(range(7),4)]
        system = case['plucker_system']
        assert system['kernel_coordinate_monomials'] == [list(m) for m in monomials]
        assert system['coefficients'] == plucker and plucker == [zero]*35
        assert system['label_quadruples'] == [[S[x] for x in quad] for quad in combinations(range(7),4)]
        assert all(not v[j] for v in basis for j,(a,b) in enumerate(PAIRS) if a != 0)
        counts['complete_plucker_coefficient_vectors_checked'] += 35
        if dimension == 1:
            continue
        assert dimension == 3
        charts = case['algebraic_gate_system']['charts']
        assert len(charts) == 21
        chart_results = []
        for (a,b), chart in zip(PAIRS, charts):
            assert chart['pivot_labels'] == [S[a],S[b]] and chart['pivot_linear_form'] == p(a,b)
            if not any(p(a,b)):
                assert chart['rows'] == [] and chart['status'] == 'empty_pivot_chart'
                continue
            u, v = [p(x,b) for x in range(7)], [p(a,x) for x in range(7)]
            assert chart['U_linear_forms'] == u and chart['V_linear_forms'] == v
            wedge = [add(mul(u[x],v[y]), scale(-1,mul(u[y],v[x]))) for x,y in PAIRS]
            assert wedge == [mul(p(a,b),p(x,y)) for x,y in PAIRS]
            counts['reconstruction_coefficient_identities_checked'] += 21
            assert len(chart['rows']) == 4
            branch_results = []
            for row_number, ((i,k,z,g,q,_), data) in enumerate(zip(blocks,chart['rows'])):
                qu = [add(*(scale(c,w) for c,w in zip(cov,u))) for cov in q]
                qv = [add(*(scale(c,w) for c,w in zip(cov,v))) for cov in q]
                assert data['Q_U_linear_forms'] == qu and data['Q_V_linear_forms'] == qv
                minors = [add(mul(qu[x],qv[y]),scale(-1,mul(qu[y],qv[x]))) for x,y in combinations(range(4),2)]
                assert data['projection_minor_quadrics'] == minors == [zero]*6
                assert len(data['projection_minor_plucker_identities']) == 6 and len(data['branches']) == 4
                for n, branch in enumerate(data['branches']):
                    alpha, beta = scale(-1,qv[n]), qu[n]
                    h = [add(mul(alpha,ux),mul(beta,vx)) for ux,vx in zip(u,v)]
                    assert branch['intersection_vector_quadrics'] == h
                    assert branch['projection_pivot_nonzero_alternatives'] == [qu[n],qv[n]]
                    assert branch['alpha_linear_form'] == branch['finite_gate_D_coefficient'] == alpha
                    assert branch['beta_linear_form'] == beta and branch['finite_gate_C_coefficient'] == scale(-1,beta)
                    residuals = [add(*(scale(c,w) for c,w in zip(cov,h))) for cov in q]
                    assert branch['quotient_residual_quadrics'] == residuals == [zero]*4
                    assert len(branch['quotient_residual_plucker_identities']) == 4
                    lam = scale(pow(g[z],-1,P),h[S.index(z)])
                    error = {x:add(h[S.index(x)],scale(-g[x],lam)) for x in i}
                    error.update({x:scale(-g[x],lam) for x in k})
                    weights = [h[S.index(z)]]+[scale(g[z],error[x]) for x in i]
                    assert branch['weight_numerator_quadrics'] == weights
                    assert len(branch['zero_weight_plucker_identities']) == 3
                    differences = {x:add(h[S.index(x)] if x in S else zero,scale(-1,error.get(x,zero))) for x in H}
                    assert all(differences[x] == scale(g[x],lam) for x in H)
                    moments = [add(*(scale(pow(x,d,P),differences[x]) for x in H)) for d in range(1,9)]
                    assert moments == [zero]*8
                    if row_number == 0:
                        assert weights[0] == weights[2] == zero
                        assert branch['status'] in ('empty_projection_pivot','excluded_zero_weight_identity')
                    branch_results.append({'row':row_number,'pivot':n,'moment_coefficient_residuals':moments,
                                           'first_row_lambda_and_label8_zero':row_number == 0 and weights[0] == weights[2] == zero})
                    counts['branches_with_direct_coefficient_and_moment_checks'] += 1
                    counts['moment_coefficient_residuals_checked'] += 8*len(monomials)
            chart_results.append({'pivot_labels':chart['pivot_labels'],'branches':branch_results})
        cases.append({'case_index':number,'I':case['I'],'K':case['K'],'nonempty_charts':chart_results})
    assert len(cases) == 24
    assert counts['branches_with_direct_coefficient_and_moment_checks'] == 2304
    assert counts['complete_saved_basis_residuals_checked'] == 1041*24
    assert counts['complete_plucker_coefficient_vectors_checked'] == 136*35
    summary = dict(counts, actual_larger_kernels=len(cases),required_larger_kernels=24,
                   actual_symbolic_branches=2304,required_symbolic_branches=2304,
                   failures=0,source_and_replay_unchanged=True)
    output={'scope':'Separate step-309 supplement to reviewed complete producer/replay',
            'unchanged_hashes':hashes,'summary':summary,'larger_kernel_coefficients':cases,'failures':[]}
    path=ROOT/'nondisjoint-third-critical-audit.json'
    path.write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps(summary,sort_keys=True))
    print(f'Full certificate: {path}')


if __name__ == '__main__':
    run()
