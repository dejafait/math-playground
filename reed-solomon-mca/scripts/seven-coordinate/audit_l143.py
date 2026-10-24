"""Separate L143 audit: complete saved evidence and isolated reproduction.

Run: python3 -E -B scripts/seven-coordinate/audit_l143.py
No new locus, census, changed-row gate, basis conversion or assembly.
"""
from collections import Counter
from hashlib import sha256
from itertools import combinations
from pathlib import Path
from tempfile import TemporaryDirectory
import json
import shutil
import subprocess
import sys

# Inspected, side-effect-free helpers from the existing capacity audit.
from audit_l142 import determinant, dot, normalize

HERE = Path(__file__).resolve().parent
P = 97


def digest(name):
    return sha256((HERE/name).read_bytes()).hexdigest()


def read(name):
    return json.loads((HERE/name).read_bytes())


def run():
    out = dict(step_id='2026-10-23-mca-431-l143-critical-audit', checks=[],
               failures=[], input_sha256={}, runs=[], records=[], capacity={})

    def check(name, condition):
        out['checks'].append(dict(name=name, passes=bool(condition)))
        if not condition:
            raise ValueError(name)

    try:
        check('assertions enabled', __debug__)
        cert_name = 'l141-l142-literal-reuse.json'
        replay_name = 'l141-l142-literal-reuse-replay.json'
        programs = ['l141_l142_literal_reuse.py', 'verify_l141_l142_literal_reuse.py']
        cert, replay = read(cert_name), read(replay_name)
        manifests = [cert['input_sha256']]
        for name, count in [('l140-critical-audit.json', 419),
                            ('l141-critical-audit.json', 431),
                            ('l142-critical-audit.json', 4363)]:
            a = read(name)
            check('complete prior verdict '+name, a['failures'] == [] and
                  len(a['checks']) == count and all(c['passes'] for c in a['checks']) and
                  a['original_artifacts_byte_unchanged'] and len(a['runs']) == 2 and
                  all(r['returncode'] == 0 for r in a['runs']))
            manifests.append(a['input_sha256'])
        partition = read('l125-critical-audit.json')
        check('L125 complete audited replay', not partition['failures'] and
              partition['original_artifacts_byte_unchanged'] and partition['full_saved_replay_identical'])
        manifests.append(partition['audited_input_hashes'])
        for manifest in manifests:
            for name, expected in manifest.items():
                check('local manifest path '+name, (HERE/name).resolve().is_relative_to(HERE.parent.parent))
                actual = digest(name)
                check('complete manifest binding '+name, actual == expected)
                out['input_sha256'][name] = actual
        for name in programs+[cert_name,replay_name,'audit_l142.py','audit_l141.py','audit_l140.py']:
            out['input_sha256'][name] = digest(name)
        check('saved source/replay byte bindings', cert['failures'] == replay['failures'] == [] and
              cert['original_inputs_unchanged'] and cert['code_sha256'] == digest(programs[0]) and
              replay['verifier_sha256'] == digest(programs[1]) and
              replay['certificate_sha256'] == digest(cert_name))
        for n in (140,141,142):
            check('prior audit program binding '+str(n),
                  read(f'l{n}-critical-audit.json')['audit_code_sha256'] == digest(f'audit_l{n}.py'))

        # Preserve all notebook-relative paths. Only the two L143 programs run.
        with TemporaryDirectory(prefix='l143-audit-', dir=HERE) as temp:
            root = Path(temp)/'notebook'/'scripts'/'seven-coordinate'
            root.mkdir(parents=True)
            for name in out['input_sha256']:
                dest = (root/name).resolve()
                check('isolated path containment '+name, dest.is_relative_to(Path(temp)))
                dest.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(HERE/name, dest)
            for program in programs:
                result = subprocess.run([sys.executable,'-E','-B',str(root/program)],
                                        capture_output=True,text=True,check=False)
                out['runs'].append(dict(program=program,returncode=result.returncode,
                    stdout=result.stdout.replace(temp,'<isolated-copy>'),
                    stderr=result.stderr.replace(temp,'<isolated-copy>')))
                check('full isolated execution '+program, result.returncode == 0)
            for name, expected in out['input_sha256'].items():
                check('full isolated byte equality '+name,
                      sha256((root/name).read_bytes()).hexdigest() == expected)

        master, prior = read('new-pair-filter.json'), read('l139-literal-reuse.json')
        s = [1,8,12,18,22,27,33]
        h = [x for x in range(1,P) if pow(x,16,P) == 1]
        universe = sorted([[sorted(set(a)&set(s)),sorted(set(a)-set(s))]
                           for a in combinations(h,4) if len(set(a)&set(s)) == 2])
        check('independent support universe', len(universe) == 756 and universe == master['universe'])
        domain = prior['unmatched_indices']
        check('exact 46-minus-one domain', len(domain) == len(set(map(tuple,domain))) == 46 and
              domain.count([199,565]) == 1 and cert['removed_only'] == [[199,565]] and
              cert['required_scope_indices'] == [x for x in domain if x != [199,565]] and
              [r['indices'] for r in cert['overlay']] == cert['required_scope_indices'] and
              len(cert['overlay']) == 45)
        histories = [('historical_residual_occurrences','new-pair-filter.json','residual_occurrences',154),
                     ('historical_l132_mismatches','residual-locus-reuse.json','unmatched_indices',118),
                     ('historical_l134_mismatches','l133-literal-reuse.json','unmatched_indices',100),
                     ('historical_l136_mismatches','l135-literal-reuse.json','unmatched_indices',82),
                     ('historical_l138_mismatches','l137-literal-reuse.json','unmatched_indices',64),
                     ('historical_l140_mismatches','l139-literal-reuse.json','unmatched_indices',46)]
        for field,name,key,count in histories:
            check('full historical list '+field, cert[field] == read(name)[key] and len(cert[field]) == count)
        source = read('first-l140-mismatch-locus-gates.json')
        source_replay = read('first-l140-mismatch-locus-gates-replay.json')
        source_audit = read('l141-critical-audit.json')
        imported = cert['source_imports'][0]
        check('one complete source', len(cert['source_imports']) == 1 and
              imported['lemma'] == 'L141/L142' and imported['kernel_basis'] == source['kernel_basis'])
        check('whole homogeneous import', imported['imported_locus'] ==
              {k:source[k] for k in ('plucker_quadruples','plucker_coefficients_s2_st_t2',
               'affine_gcd','bezout_coefficients','affine_quotients',
               'complete_projective_parameter_locus','infinity_is_decomposable')} and
              len(source['plucker_coefficients_s2_st_t2']) == 35 and
              source['complete_projective_parameter_locus'] == [[1,0],[1,81]] and
              source['infinity_is_decomposable'] is False)
        # Bind the complete homogeneous evidence, rather than the two-point summary.
        quads = list(combinations(s,4))
        multiples = {(1,8,12,18):53,(1,8,18,22):36,(1,8,18,27):28,(1,8,18,33):87,
                     (1,12,18,22):36,(1,12,18,27):80,(1,12,18,33):64,
                     (1,18,22,27):28,(1,18,22,33):10,(1,18,27,33):91}
        expected_q = [[0,16*multiples.get(q,0)%P,multiples.get(q,0)] for q in quads]
        check('all homogeneous, division, Bezout and infinity evidence',
              source['plucker_coefficients_s2_st_t2'] == source_replay['plucker_coefficients_s2_st_t2'] == expected_q and
              source['affine_gcd'] == [0,16,1] and
              source['affine_quotients'] == [[q[2]] if q[2] else [] for q in expected_q] and
              source['bezout_coefficients'] == [[16] if q == (1,18,27,33) else [] for q in quads] and
              expected_q[quads.index((1,18,27,33))] == [0,1,91])
        first, second = imported['point_bindings']
        gate = source['points_and_all_row_gates'][0]['row_gates'][0]
        check('first point complete row/gate binding', first['row_input']['I'] == [1,8] and
              first['row_input']['K'] == [47,50] and first['row_input']['z'] == 12 and
              first['row_input']['original_block'] == source['blocks'][0] and
              first['unchanged_rejecting_gate'] == gate == source_audit['complete_row_checks'][0]['full_gate'] and
              gate['direction_coefficients'] == [53,0] and gate['lambda_value'] == 0 and
              gate['error_weights'] == [53,0,0,0] and gate['moment_residuals'] == [0]*8 and
              gate['h_minus_error_minus_lambda_g_on_H'] == [0]*16 and not gate['passes'])
        expected_pivots = [r for r in source_replay['all_pivot_replay'] if r['point'] == 0 and r['row'] == 1]
        check('entire imported first-point pivot evidence', first['all_nonzero_pivot_replay'] == expected_pivots and
              expected_pivots == [r for r in source_audit['complete_pivot_checks'] if r['point'] == 0 and r['row'] == 1] and
              len(expected_pivots) > 0 and all(r['scalar'] and r['lambda_value'] == 0 for r in expected_pivots))
        check('second point exact plane and separate capacity import', second['kind'] == 'exact_plane_capacity' and
              second['u'] == source['points_and_all_row_gates'][1]['u'] == [1,0,42,90,52,62,61] and
              second['v'] == source['points_and_all_row_gates'][1]['v'] == [0,69,60,1,72,45,80] and
              second['input_manifest'] == read('l142-critical-audit.json')['input_sha256'] and
              len(second['input_manifest']) == 30 and len(second['inherited_manifest']) == 25)
        # Verify the existing complete capacity evidence; do not execute its census.
        verify_capacity_evidence(out['capacity'], check, read)

        matched, unmatched = [], []
        kinds = Counter()
        original_entries = null_entries = 0
        for entry in cert['overlay']:
            n,u = entry['indices']
            shard = read(entry['shard'])
            rec = shard['cases'][int(entry['case_pointer'].split('/')[-1])]
            old = next(r for r in prior['overlay'] if r['indices'] == [n,u])
            check(f'{n},{u} complete original provenance', rec == entry['complete_original_record'] == old['complete_original_record'] and
                  rec['fourth_index'] == u and rec['status'] == 'residual' and old['disposition'] == 'unmatched')
            rows = master['first_indices']+[n,u]
            matrix = [r for j in rows for r in master['blocks'][j]['matrix']]
            basis, pivots, rank = rec['kernel_basis'], rec['pivot_columns'], rec['rank']
            free = [j for j in range(21) if j not in pivots]
            minor = [[matrix[a][b] for b in pivots] for a in rec['minor_rows']]
            det = determinant(minor)
            residuals = [[dot(r,v) for r in matrix] for v in basis]
            check(f'{n},{u} full extension rank certificate', len(matrix) == 24 and all(len(r) == 21 for r in matrix) and
                  len(pivots) == len(set(pivots)) == len(rec['minor_rows']) == rank and
                  det%P == rec['minor_residue'] != 0 and len(basis) == 21-rank and
                  all(len(v) == 21 for v in basis) and residuals == rec['kernel_residuals'] == [[0]*24 for v in basis] and
                  [[v[j] for j in free] for v in basis] == [[int(a==b) for b in range(len(free))] for a in range(len(free))])
            original_entries += 504
            null_entries += 24*len(basis)
            comparison = entry['comparisons'][0]
            equal = basis == source['kernel_basis']
            check(f'{n},{u} complete literal comparison', len(entry['comparisons']) == 1 and
                  comparison['literal_ordered_basis_equal'] == equal and comparison['covered'] == equal and
                  entry['disposition'] == ('covered' if equal else 'unmatched'))
            if equal:
                matched.append([n,u])
                check('only the exact old exchange', [n,u] == [565,199] and comparison['mismatch'] is None and
                      comparison['point_row_bindings'] == [dict(source_point_index=0,target_row_number=1,complete_row_input_equal=True),
                          dict(source_point_index=1,exact_plane_and_capacity_bound=True)] and
                      entry['rows'] == source['rows'][:2]+[source['rows'][3],source['rows'][2]])
            else:
                unmatched.append([n,u])
                if len(basis) != len(source['kernel_basis']):
                    mismatch = dict(kind='basis_length',actual=len(basis),source=len(source['kernel_basis']))
                else:
                    a,b = next((a,b) for a in range(len(basis)) for b in range(21) if basis[a][b] != source['kernel_basis'][a][b])
                    mismatch = dict(kind='basis_entry',basis_index=a,column=b,actual=basis[a][b],source=source['kernel_basis'][a][b])
                kinds[mismatch['kind']] += 1
                check(f'{n},{u} entire mismatch witness', comparison['mismatch'] == mismatch and comparison['point_row_bindings'] == [])
            out['records'].append(dict(indices=[n,u],rank=rank,matrix=matrix,minor_integer_determinant=det,
                complete_basis=basis,residuals=residuals,comparison=comparison))
        check('complete result and all mismatch kinds', matched == cert['covered_indices'] == replay['covered_indices'] == [[565,199]] and
              unmatched == cert['unmatched_indices'] == replay['unmatched_indices'] and len(unmatched) == 44 and
              kinds == {'basis_length':8,'basis_entry':36} and cert['additional_binding_indices'] == [] and
              original_entries == replay['original_entries_rebuilt'] == 22680 and
              null_entries == replay['null_residual_entries_replayed'] == 1968 and
              cert['summary'] == replay['summary'])
        out['summary'] = dict(actual_records=45,required_records=45,complete_minors=45,
            original_entries=original_entries,null_residual_entries=null_entries,matched=1,
            required_point_bindings=2,actual_point_bindings=2,mismatches=44,mismatch_kinds=dict(kinds),
            reference_exchanges=1,additional_bindings=0,new_unordered_families=0,
            capacity_directions=4,required_directions=12,capacity_shortfall=8,
            capacity_rows_verified=756,bound_inputs=len(out['input_sha256']))
    except Exception as error:
        out['failures'].append(f'{type(error).__name__}: {error}')
    finally:
        preserved = all(digest(name) == value for name,value in out['input_sha256'].items())
        out['original_artifacts_byte_unchanged'] = preserved
        if not preserved:
            out['failures'].append('An original changed')
        out['audit_code_sha256'] = digest(Path(__file__).name)
        out['qualification'] = 'Existing finite method limitation only; reused inspected capacity-evidence verification; shared Python/residue arithmetic and inherited finite inputs; no new census or assembly.'
        path = HERE/'l143-critical-audit.json'
        path.write_text(json.dumps(out,indent=2)+'\n')
        print(json.dumps(out.get('summary',{}),sort_keys=True))
        print(f"Checks {sum(c['passes'] for c in out['checks'])}/{len(out['checks'])}; failures {out['failures']}; originals unchanged {preserved}; certificate {path}")
    if out['failures']:
        raise SystemExit(1)


def verify_capacity_evidence(out, check, read):
    """Reuse the fully inspected L142 certificate checks, without its census runs.

    This is binding/reverification of existing evidence, not an independent
    third capacity implementation. The copied checks retain every matrix,
    multiplier, kernel, weight and nonzero pivot record.
    """
    out.update(rows=[], pivots=[])
    cert = read('l141-survivor-full-rows.json')
    replay = read('l141-survivor-full-rows-replay.json')
    s = [1, 8, 12, 18, 22, 27, 33]
    h = [x for x in range(1, P) if pow(x, 16, P) == 1]
    universe = sorted([(sorted(set(a)&set(s)), sorted(set(a)-set(s)))
                       for a in combinations(h, 4) if len(set(a)&set(s)) == 2])
    check('field and complete independently generated support domain', cert['modulus'] == P and
          cert['H'] == h and cert['S'] == s and len(h) == 16 and len(universe) == 756)
    check('one complete plane in both outputs', len(cert['planes']) == len(replay['planes']) == 1)
    plane, rep = cert['planes'][0], replay['planes'][0]
    u, v = [1, 0, 42, 90, 52, 62, 61], [0, 69, 60, 1, 72, 45, 80]
    check('exact plane and occurrence', plane['u'] == u and plane['v'] == v and
          plane['historical_indices'] == rep['historical_indices'] == [[199, 565]] and
          len(plane['rows']) == len(rep['rows']) == 756)
    old = read('first-l140-mismatch-locus-gates.json')
    overlay = read('l139-literal-reuse.json')
    shard = read('new-pair-filter/third-199.json')
    check('original record and complete audited overlay', shard['third_index'] == 199 and
          shard['cases'][167]['fourth_index'] == 565 and
          overlay['overlay'][8]['indices'] == [199, 565] and
          overlay['overlay'][8]['complete_original_record'] == shard['cases'][167] and
          old['audited_mismatch_binding']['complete_overlay'] == overlay['overlay'][8] and
          old['source']['pointer'] == '/cases/167' and
          old['audited_mismatch_binding']['pointer'] == '/overlay/8' and
          old['complete_projective_parameter_locus'] == [[1, 0], [1, 81]] and
          old['points_and_all_row_gates'][1]['u'] == u and old['points_and_all_row_gates'][1]['v'] == v)
    check('audited other exhaustive point rejected',
          old['points_and_all_row_gates'][0]['u'] == [1,0,0,0,0,0,0] and
          old['points_and_all_row_gates'][0]['v'] == [0,0,0,1,0,0,0] and
          all(g['projection_rank'] == 1 and g['lambda_value'] == 0 and not g['passes']
              for g in old['points_and_all_row_gates'][0]['row_gates']) and
          [p['passes_intrinsic_gates'] for p in old['points_and_all_row_gates']] == [False, True])
    historical = [('historical_residual_occurrences','new-pair-filter.json','residual_occurrences',154),
                  ('historical_l132_mismatches','residual-locus-reuse.json','unmatched_indices',118),
                  ('historical_l134_mismatches','l133-literal-reuse.json','unmatched_indices',100),
                  ('historical_l136_mismatches','l135-literal-reuse.json','unmatched_indices',82),
                  ('historical_l138_mismatches','l137-literal-reuse.json','unmatched_indices',64)]
    for field, name, key, count in historical:
        check('complete historical list '+field, overlay[field] == read(name)[key] and len(overlay[field]) == count)
    check('46 mismatches preserved', len(overlay['unmatched_indices']) == 46 and
          overlay['unmatched_indices'][0] == [199, 565])

    directions = []
    fixed_pivots = 0
    for n, ((i, k), row, witness) in enumerate(zip(universe, plane['rows'], rep['rows'])):
        check(f'row {n} complete indexed support', row['row_index'] == witness['row_index'] == n and
              row['I'] == witness['I'] == i and row['K'] == witness['K'] == k)
        support = i+k
        m = [[sum(u[j]*pow(x,d,P) for j,x in enumerate(s)) % P,
              sum(v[j]*pow(x,d,P) for j,x in enumerate(s)) % P] +
             [-pow(x,d,P) % P for x in support] for d in range(1,9)]
        r, e, piv = witness['moment_rref'], witness['left_multiplier'], witness['pivot_columns']
        rank = witness['moment_rank']
        free = [j for j in range(6) if j not in piv]
        basis = witness['complete_null_basis']
        det_e = determinant(e)
        error_minor = [rr[2:] for rr in m[:4]]
        det_error = determinant(error_minor)
        check(f'row {n} original matrix, determinant and invertible multiplier', witness['moment_matrix'] == m and
              len(e) == 8 and all(len(rr) == 8 for rr in e) and
              len(r) == 8 and all(len(rr) == 6 for rr in r) and
              [[sum(e[a][b]*m[b][c] for b in range(8)) % P for c in range(6)] for a in range(8)] == r and
              det_e == witness['left_multiplier_integer_determinant'] and
              det_e % P == witness['left_multiplier_determinant_residue'] != 0 and
              error_minor == witness['error_minor_first_four_moment_rows'] and
              det_error == witness['error_minor_integer_determinant'] and det_error % P != 0)
        check(f'row {n} entire extension kernel', rank == len(piv) and len(set(piv)) == rank and
              rank in [5,6] and len(basis) == 6-rank and
              len(witness['nonzero_pivot_values']) == rank and all(witness['nonzero_pivot_values']) and
              [[r[a][b] for b in piv] for a in range(rank)] ==
              [[int(a == b) for b in range(rank)] for a in range(rank)] and
              all(rr == [0]*6 for rr in r[rank:]) and
              all(len(b) == 6 and all(dot(rr,b) == 0 for rr in m) for b in basis) and
              [[b[j] for j in free] for b in basis] ==
              [[int(a == b) for b in range(6-rank)] for a in range(6-rank)])
        g = {}
        for x in h:
            value = 1
            for y in h:
                if y not in s+k:
                    value = value*(x-y) % P
            g[x] = value
        z = min(set(s)-set(i))
        q = [[(int(y == x)*g[z]-int(y == z)*g[x]) % P for y in s]
             for x in s if x not in i+[z]]
        qu, qv = [dot(c,u) for c in q], [dot(c,v) for c in q]
        minors = [(qu[a]*qv[b]-qu[b]*qv[a]) % P for a,b in combinations(range(4),2)]
        check(f'row {n} complete quotient comparison', row['z'] == z and
              row['g_values_on_H'] == [g[x] for x in h] and all(g[x] for x in s+k) and
              row['Q'] == q and row['Q_u'] == qu and row['Q_v'] == qv and
              row['projection_minors'] == minors and row['projection_rank'] == rank-4 and
              (any(minors) if rank == 6 else (not any(minors) and any(qu+qv))))
        out['rows'].append(dict(row_index=n,I=i,K=k,rank=rank,moment_matrix=m,
            left_multiplier_integer_determinant=det_e,error_minor_integer_determinant=det_error,
            complete_null_basis=basis,projection_rank=rank-4,passes=True))
        if rank == 6:
            check(f'row {n} rejection', not basis and row['status'] == 'rank_two_no_intersection')
            continue
        gate = row['recovery']
        alpha, beta = gate['direction_coefficients']
        hh = [(alpha*x+beta*y) % P for x,y in zip(u,v)]
        lam = hh[s.index(z)]*pow(g[z],-1,P) % P
        weights = [(hh[s.index(x)]-lam*g[x]) % P for x in i]+[-lam*g[x] % P for x in k]
        errors = dict(zip(support, weights))
        identity = [((hh[s.index(x)] if x in s else 0)-errors.get(x,0)-lam*g[x]) % P for x in h]
        moments = [sum(((hh[s.index(x)] if x in s else 0)-errors.get(x,0))*pow(x,d,P) for x in h) % P for d in range(1,9)]
        pivot = next(j for j in range(4) if qu[j] or qv[j])
        check(f'row {n} all weights, moments and finite gate', row['status'] == 'intrinsic_success' and
              row['projection_pivot'] == pivot and [alpha,beta] == [-qv[pivot]%P,qu[pivot]] and
              lam == gate['lambda_value'] != 0 and gate['h'] == hh and weights == gate['error_weights'] and all(weights) and
              identity == gate['identity_residuals'] == [0]*16 and moments == gate['shifted_moment_residuals'] == [0]*8 and
              gate['failed_gates'] == [] and gate['passes_intrinsic'] and
              gate['prescribed_finite_gate'] == dict(D_coefficient=alpha,C_coefficient=-beta%P) and
              normalize(basis[0]) == witness['normalized_full_solution'] == normalize([alpha,beta]+weights) and
              normalize([alpha,beta]) == gate['normalized_direction'])
        directions.append((gate['normalized_direction'],n))
        expected_fixed = []
        for j in range(4):
            if qu[j] or qv[j]:
                d = [-qv[j]%P,qu[j]]
                c = next(jj for jj in range(2) if [alpha,beta][jj])
                scale = d[c]*pow([alpha,beta][c],-1,P) % P
                check(f'row {n} fixed pivot {j}', scale != 0 and d == [scale*x%P for x in [alpha,beta]])
                expected_fixed.append(dict(component=j,scale=scale,direction=d,lambda_value=scale*lam%P,
                                           error_weights=[scale*w%P for w in weights]))
        fixed_pivots += len(expected_fixed)
        check(f'row {n} complete fixed pivot evidence', witness['all_nonzero_projection_pivots'] == expected_fixed)
        exterior = [[(u[a]*v[b]-u[b]*v[a]) % P for b in range(7)] for a in range(7)]
        expected = []
        for a,b in combinations(range(7),2):
            value = exterior[a][b]
            if not value:
                continue
            uu = [exterior[x][b]*pow(value,-1,P)%P for x in range(7)]
            vv = exterior[a][:]
            check(f'row {n} exterior reconstruction {a},{b}',
                  [[(uu[x]*vv[y]-uu[y]*vv[x])%P for y in range(7)] for x in range(7)] == exterior)
            qa,qb = [dot(c,uu) for c in q],[dot(c,vv) for c in q]
            for j in range(4):
                if not (qa[j] or qb[j]):
                    continue
                d = [-qb[j]%P,qa[j]]
                hv = [(d[0]*x+d[1]*y)%P for x,y in zip(uu,vv)]
                coordinate = next(x for x in range(7) if hh[x])
                scale = hv[coordinate]*pow(hh[coordinate],-1,P)%P
                ll = hv[s.index(z)]*pow(g[z],-1,P)%P
                ee = [(hv[s.index(x)]-ll*g[x])%P for x in i]+[-ll*g[x]%P for x in k]
                check(f'row {n} exterior/projection pivot {a},{b},{j}', scale != 0 and
                      hv == [scale*x%P for x in hh] and ll == scale*lam%P and ee == [scale*w%P for w in weights])
                expected.append(dict(pivot=[a,b],nonzero_value=value,u=uu,v=vv,projection_component=j,
                                     direction=d,h=hv,scale=scale,lambda_value=ll,error_weights=ee))
        check(f'row {n} complete exterior pivot evidence', witness['all_exterior_and_projection_pivot_recoveries'] == expected)
        out['pivots'].append(dict(row_index=n,fixed=expected_fixed,exterior=expected))

    expected_groups = [dict(direction=d,row_indices=[n]) for d,n in sorted(directions)]
    check('four distinct full directions and complete groups', len(directions) == 4 and
          len({tuple(d) for d,n in directions}) == 4 and
          plane['direction_groups'] == rep['direction_groups'] == expected_groups and
          plane['duplicate_direction_groups'] == [])
    expected_summary = dict(covered_rows=756,required_rows=756,projection_rank_counts={'1':4,'2':752},
        status_counts={'intrinsic_success':4,'rank_two_no_intersection':752},failed_gate_counts={},full_rows=4,
        distinct_directions_before_chart=4,required_distinct_directions=12,duplicate_direction_groups=0,
        shortfall=8,rank_zero_obstruction=False)
    check('complete summary and rank comparison', plane['summary'] == rep['summary'] == expected_summary and
          rep['moment_rank_counts'] == {'5':4,'6':752} and
          dict(Counter(str(r['rank']) for r in out['rows'])) == {'5':4,'6':752} and
          plane['disposition'] == 'excluded_necessary_shortfall')
    for oldrow, oldgate in zip(old['rows'],old['points_and_all_row_gates'][1]['row_gates']):
        row = next(r for r in plane['rows'] if r['I'] == oldrow['I'] and r['K'] == oldrow['K'])
        check('complete selected-row regression '+str(row['row_index']), all(row['recovery'][key] == oldgate[key]
              for key in ['direction_coefficients','lambda_value','error_weights','prescribed_finite_gate']))
    check('all pivot cases covered', fixed_pivots == 16 and sum(len(p['exterior']) for p in out['pivots']) == 336)
    out['summary'] = dict(actual_supports=756,required_supports=756,rank_six=752,rank_five=4,
        complete_original_matrices=756,invertible_multiplier_certificates=756,error_minors=756,
        full_directions=4,required_directions=12,shortfall=8,fixed_projection_pivots=16,
        exterior_projection_pivots=336,bound_inputs=len(read('l142-critical-audit.json')['input_sha256']),inherited_bound_inputs=25)


if __name__ == "__main__":
    run()
