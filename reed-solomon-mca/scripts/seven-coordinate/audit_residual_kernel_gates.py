"""Separate L112 audit: complete residual bases and augmented recovery systems.

No imports from either producer or prior verifier. Replays those programs
only after all saved evidence has been checked. Run from the notebook:
python3 scripts/seven-coordinate/audit_residual_kernel_gates.py
"""
from collections import Counter
from hashlib import sha256
from itertools import combinations
from pathlib import Path
import json
import subprocess
import sys

P = 97
HERE = Path(__file__).resolve().parent
S = [1, 8, 12, 18, 22, 27, 33]
H = [x for x in range(1, P) if pow(x, 16, P) == 1]
J = sorted(set(H)-set(S))
PAIRS = list(combinations(range(7), 2))
QUADS = list(combinations(range(7), 4))
INDEX = {ij: n for n, ij in enumerate(PAIRS)}
SOURCE_HASH = '34d6bb68537b8e5b153552801426c2f37266c96fa1446bb8ec89ae03885f85c2'


def reduce_matrix(rows, width):
    a, pivots = [r[:] for r in rows], []
    for j in range(width):
        n = len(pivots)
        pivot = next((k for k in range(n, len(a)) if a[k][j]), None)
        if pivot is None:
            continue
        a[n], a[pivot] = a[pivot], a[n]
        inv = pow(a[n][j], -1, P)
        a[n] = [x*inv % P for x in a[n]]
        for k in range(len(a)):
            if k != n:
                factor = a[k][j]
                a[k] = [(x-factor*y) % P for x, y in zip(a[k], a[n])]
        pivots.append(j)
    free = [j for j in range(width) if j not in pivots]
    basis = []
    for j in free:
        v = [0]*width
        v[j] = 1
        for i, c in enumerate(pivots):
            v[c] = -a[i][j] % P
        basis.append(v)
    return pivots, basis


def dot(a, b):
    return sum(x*y for x, y in zip(a, b)) % P


def poly_product(a, b):
    out = [0]*(len(a)+len(b)-1) if a and b else []
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] = (out[i+j]+x*y) % P
    return out


def trim(a):
    while a and a[-1] == 0:
        a.pop()
    return a


def block(row):
    coeff = [1]
    for y in sorted(set(J)-set(row['K'])):
        coeff = poly_product(coeff, [-y % P, 1])
    values = {}
    for x in H:
        v = 0
        for c in reversed(coeff):
            v = (v*x+c) % P
        values[x] = v
        assert (v != 0) == (x in S+row['K'])
    observed = sorted(set(S)-set(row['I']))
    z = observed[0]
    q = [[(values[z]*int(x == label)-values[x]*int(z == label)) % P
          for label in S] for x in observed[1:]]
    n = [[(a[i]*b[j]-a[j]*b[i]) % P for i, j in PAIRS]
         for a, b in combinations(q, 2)]
    return coeff, values, q, n


def alternating(p):
    a = [[0]*7 for _ in S]
    for (i, j), x in zip(PAIRS, p):
        a[i][j], a[j][i] = x, -x % P
    return a


def homogeneous_quadrics(basis):
    b0 = basis[0]
    b1 = basis[1] if len(basis) == 2 else [0]*21
    out = []
    for a, b, c, d in QUADS:
        triples = [0, 0, 0]
        for sign, ij, kl in [(1, (a,b), (c,d)), (-1, (a,c), (b,d)), (1, (a,d), (b,c))]:
            j, k = INDEX[ij], INDEX[kl]
            triples[0] += sign*b0[j]*b0[k]
            triples[1] += sign*(b0[j]*b1[k]+b1[j]*b0[k])
            triples[2] += sign*b1[j]*b1[k]
        out.append([x % P for x in triples])
    return out


def run():
    source_raw = (HERE/'third-row-variation.json').read_bytes()
    gate_raw = (HERE/'residual-kernel-gates.json').read_bytes()
    replay_raw = (HERE/'residual-kernel-gates-replay.json').read_bytes()
    source, gates, replay = map(json.loads, (source_raw, gate_raw, replay_raw))
    prior_audit = json.loads((HERE/'third-row-critical-audit.json').read_bytes())
    assert sha256(source_raw).hexdigest() == SOURCE_HASH
    assert source['modulus'] == gates['modulus'] == P
    assert source['H'] == gates['H'] == H and len(H) == 16
    assert source['S'] == gates['S'] == S and source['J'] == J
    assert source['column_pairs'] == [[S[a], S[b]] for a,b in PAIRS]
    assert source['failures'] == gates['failures'] == replay['failures'] == prior_audit['failures'] == []
    assert gates['source_sha256'] == replay['source_sha256'] == SOURCE_HASH
    assert replay['gate_certificate_sha256'] == sha256(gate_raw).hexdigest()
    assert prior_audit['producer_replay']['before_sha256'] == prior_audit['producer_replay']['after_sha256'] == SOURCE_HASH
    assert prior_audit['producer_replay']['returncode'] == 0
    first = [{'I':[1,8], 'K':[47,50]}, {'I':[12,18], 'K':[64,70]}]
    assert source['first_two'] == first
    used = set(x for r in first for x in r['I']+r['K'])
    expected_thirds = {(i,k) for i in combinations(sorted(set(S)-used),2)
                       for k in combinations(sorted(set(J)-used),2)}
    assert len(expected_thirds) == len(source['seeds']) == 30
    assert {(tuple(s['third_I']), tuple(s['third_K'])) for s in source['seeds']} == expected_thirds
    expected_indices = [(n,m) for n,s in enumerate(source['seeds']) if not s['reused_audited_L110']
                        for m,c in enumerate(s['cases']) if c['pairwise_linear'] and c['rank'] < 21]
    assert len(expected_indices) == 266
    assert [(r['seed_index'],r['case_index']) for r in gates['records']] == expected_indices
    assert [(r['seed_index'],r['case_index']) for r in replay['records']] == expected_indices
    records, dimensions, failed_gates = [], Counter(), Counter()
    row_count = moment_count = point_count = 0
    per_seed = {}
    for rec in gates['records']:
        n, m = rec['seed_index'], rec['case_index']
        seed, case = source['seeds'][n], source['seeds'][n]['cases'][m]
        rows = first+[{'I':seed['third_I'], 'K':seed['third_K']}, {'I':case['I'], 'K':case['K']}]
        assert rec['rows'] == rows
        assert all(len(set(a['I']+a['K']) & set(b['I']+b['K'])) <= 1 for a,b in combinations(rows,2))
        blocks = [block(row) for row in rows]
        matrix = [v for _,_,_,b in blocks for v in b]
        pivots, basis = reduce_matrix(matrix, 21)
        assert len(pivots) == rec['rank'] == case['rank']
        assert basis == rec['kernel_basis'] == case['kernel_basis']
        assert len(basis) == 21-len(pivots) in (1,2)
        residuals = [[dot(v,w) for w in matrix] for v in basis]
        assert residuals == rec['kernel_residuals'] and not any(any(r) for r in residuals)
        assert len(reduce_matrix(basis,21)[0]) == len(basis)
        dimensions[len(basis)] += 1
        quadrics = homogeneous_quadrics(basis)
        assert len(quadrics) == len(rec['bezout_coefficients']) == 35
        assert quadrics == rec['homogeneous_plucker_coefficients']
        assert all(q[0] == q[2] == 0 for q in quadrics)
        assert bool(any(q[1] for q in quadrics)) == (len(basis) == 2)
        total = []
        for c,q in zip(rec['bezout_coefficients'],quadrics):
            term = poly_product(c,q)
            total += [0]*max(0,len(term)-len(total))
            for j,x in enumerate(term):
                total[j] = (total[j]+x) % P
        assert trim(total) == rec['affine_gcd'] == ([0,1] if len(basis)==2 else [])
        assert rec['infinity_is_decomposable'] == (len(basis)==2)
        assert len(rec['decomposable_points']) == len(basis)
        point_records = []
        for p,saved in zip(basis,rec['decomposable_points']):
            assert p == saved['bivector'] and len(saved['row_gates']) == 4
            a = alternating(p)
            pcols, _ = reduce_matrix(a,7)
            assert len(pcols) == 2
            # Independent row-space basis, rather than the producer's pivot formula.
            chosen, vectors = [], []
            for index,row in enumerate(a):
                if len(reduce_matrix(vectors+[row],7)[0]) > len(vectors):
                    chosen.append(index)
                    vectors.append(row)
            assert len(vectors) == 2
            u,v = vectors
            assert len(reduce_matrix([u,v,saved['u'],saved['v']],7)[0]) == 2
            assert [(saved['u'][i]*saved['v'][j]-saved['u'][j]*saved['v'][i]) % P for i,j in PAIRS] == p
            all_rows = []
            for row, (_,g,q,_), old in zip(rows,blocks,saved['row_gates']):
                observed = sorted(set(S)-set(row['I']))
                # Solve alpha*u_x+beta*v_x-lambda*g(x)=0 directly on all five
                # coordinates, instead of projecting and choosing a quotient pivot.
                system = [[u[S.index(x)],v[S.index(x)],-g[x] % P] for x in observed]
                piv, kernel = reduce_matrix(system,3)
                assert len(piv) == 2 and len(kernel) == 1
                alpha,beta,lam = kernel[0]
                assert alpha or beta
                h = [(alpha*x+beta*y) % P for x,y in zip(u,v)]
                assert any(h)
                ratio = h[next(j for j,x in enumerate(old['intersection_vector']) if x)]*pow(next(x for x in old['intersection_vector'] if x),-1,P) % P
                assert ratio and h == [ratio*x % P for x in old['intersection_vector']]
                assert lam == ratio*old['lambda_value'] % P
                restricted = [[dot(c,u),dot(c,v)] for c in q]
                assert len(reduce_matrix(restricted,2)[0]) == old['projection_rank'] == 1
                assert old['Q_u'] == [dot(c,saved['u']) for c in q]
                assert old['Q_v'] == [dot(c,saved['v']) for c in q]
                assert old['projection_minors'] == [0]*6
                weights = [(h[S.index(x)]-lam*g[x]) % P for x in row['I']]+[-lam*g[x] % P for x in row['K']]
                assert weights == [ratio*x % P for x in old['error_weights']]
                assert old['overlap_weights'] == old['error_weights'][:2]
                error = dict(zip(row['I']+row['K'],weights))
                identities = [((h[S.index(x)] if x in S else 0)-error.get(x,0)-lam*g[x]) % P for x in H]
                assert identities == [0]*16
                moments = [sum(((h[S.index(x)] if x in S else 0)-error.get(x,0))*pow(x,d,P) for x in H) % P for d in range(1,9)]
                assert moments == old['moment_residuals'] == [0]*8
                failed = (['lambda_zero'] if not lam else [])+['overlap_weight_zero_at_'+str(x) for x,w in zip(row['I'],weights[:2]) if not w]
                assert failed == old['failed_gates'] and old['passes'] == (not failed)
                failed_gates.update(failed)
                ca,cb = old['direction_coefficients']
                assert old['intersection_vector'] == [(ca*x+cb*y) % P for x,y in zip(saved['u'],saved['v'])]
                assert old['prescribed_finite_gate'] == {'D_coefficient':ca,'C_coefficient':-cb % P}
                all_rows.append({'augmented_system':system,'pivot_columns':piv,'complete_kernel':kernel,
                                 'intersection_vector':h,'scale_from_producer':ratio,'lambda_value':lam,
                                 'error_weights':weights,'codeword_identity_residuals':identities,
                                 'moment_residuals':moments,'failed_gates':failed})
                row_count += 1
                moment_count += 8
            # A direct coordinate-space test independently establishes lambda=0
            # at the fourth support: its plane has a unique nonzero I4-supported line.
            i4 = rows[3]['I']
            outside = [[u[S.index(x)],v[S.index(x)]] for x in S if x not in i4]
            cpiv, cker = reduce_matrix(outside,2)
            assert len(cpiv) == len(cker) == 1
            coordinate_line = [(cker[0][0]*x+cker[0][1]*y) % P for x,y in zip(u,v)]
            assert any(coordinate_line) and all(coordinate_line[j] == 0 for j,x in enumerate(S) if x not in i4)
            assert all_rows[3]['lambda_value'] == 0 and not saved['passes_intrinsic_gates']
            point_records.append({'bivector':p,'alternate_basis_rows':chosen,'u':u,'v':v,
                                  'row_gates':all_rows,'fourth_coordinate_system':outside,
                                  'fourth_coordinate_kernel':cker,'fourth_coordinate_line':coordinate_line})
            point_count += 1
        key = str((tuple(rows[2]['I']),tuple(rows[2]['K'])))
        counts = per_seed.setdefault(key,{'occurrences':0,'points':0,'fourth_lambda_zero':0})
        counts['occurrences'] += 1
        counts['points'] += len(point_records)
        counts['fourth_lambda_zero'] += len(point_records)
        records.append({'seed_index':n,'case_index':m,'rows':rows,'matrix':matrix,
                        'rank':len(pivots),'pivot_columns':pivots,'complete_kernel_basis':basis,
                        'kernel_residuals':residuals,'homogeneous_plucker_coefficients':quadrics,
                        'verified_bezout_sum':total,'points':point_records})
    assert dict(dimensions) == {1:257,2:9}
    assert (point_count,row_count,moment_count) == (275,1100,8800)
    assert dict(failed_gates) == gates['summary']['failed_gate_counts']
    assert gates['summary']['intrinsically_passing_points'] == 0
    producer_replays = []
    for program, artifact in [('residual_kernel_gates.py','residual-kernel-gates.json'),
                              ('verify_residual_kernel_gates.py','residual-kernel-gates-replay.json')]:
        before = (HERE/artifact).read_bytes()
        result = subprocess.run([sys.executable,str(HERE/program)],capture_output=True,text=True)
        after = (HERE/artifact).read_bytes()
        producer_replays.append({'program':program,'returncode':result.returncode,'stdout':result.stdout,
                                 'stderr':result.stderr,'before_sha256':sha256(before).hexdigest(),
                                 'after_sha256':sha256(after).hexdigest(),'byte_identical':before==after})
        assert result.returncode == 0 and before == after
    assert (HERE/'third-row-variation.json').read_bytes() == source_raw
    summary = {'occurrences_checked':len(records),'required_occurrences':266,'kernel_dimensions':dict(dimensions),
               'projective_points_checked':point_count,'required_projective_points':275,
               'homogeneous_quadrics_checked':35*len(records),'required_quadrics':9310,
               'augmented_recovery_systems':row_count,'required_systems':1100,
               'codeword_identity_entries_checked':16*row_count,'moment_residuals_checked':moment_count,
               'fourth_coordinate_line_checks':point_count,'fourth_lambda_zero_points':point_count,
               'intrinsically_passing_points':0,'required_passing_points':0,
               'per_seed':per_seed,'failed_gate_counts':dict(failed_gates),'byte_identical_replays':len(producer_replays)}
    output = {'scope':'Separate L112 critical audit; complete residual bases, projective equations and augmented recovery systems',
              'source_sha256':SOURCE_HASH,'prior_L111_audit_sha256':sha256((HERE/'third-row-critical-audit.json').read_bytes()).hexdigest(),
              'gate_certificate_sha256':sha256(gate_raw).hexdigest(),'replay_certificate_sha256':sha256(replay_raw).hexdigest(),
              'summary':summary,'records':records,'program_replays':producer_replays,'failures':[]}
    path = HERE/'residual-kernel-critical-audit.json'
    path.write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps(summary,sort_keys=True))
    print('Failures: 0; full certificate:',path)


if __name__ == '__main__':
    run()
