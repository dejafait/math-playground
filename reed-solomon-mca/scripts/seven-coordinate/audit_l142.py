"""Separate audit of the existing L142 certificates; no enlarged census.

Run: python3 -E -B scripts/seven-coordinate/audit_l142.py
"""
from collections import Counter
from fractions import Fraction
from hashlib import sha256
from itertools import combinations
from pathlib import Path
from tempfile import TemporaryDirectory
import json
import shutil
import subprocess
import sys

HERE = Path(__file__).resolve().parent
P = 97


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def determinant(matrix):
    """Exact rational Gaussian elimination, separate from Bareiss."""
    a = [[Fraction(x) for x in row] for row in matrix]
    d = Fraction(1)
    for j in range(len(a)):
        k = next((k for k in range(j, len(a)) if a[k][j]), None)
        if k is None:
            return 0
        if k != j:
            a[j], a[k] = a[k], a[j]
            d = -d
        pivot = a[j][j]
        d *= pivot
        for k in range(j+1, len(a)):
            scale = a[k][j]/pivot
            a[k] = [x-scale*y for x, y in zip(a[k], a[j])]
    assert d.denominator == 1
    return int(d)


def normalize(v):
    c = pow(next(x for x in v if x), -1, P)
    return [c*x % P for x in v]


def dot(a, b):
    assert len(a) == len(b)
    return sum(x*y for x, y in zip(a, b)) % P


def run():
    out = dict(step_id='2026-10-23-mca-427-l142-critical-audit',
               checks=[], failures=[], input_sha256={}, runs=[], rows=[], pivots=[])

    def check(name, condition):
        out['checks'].append(dict(name=name, passes=bool(condition)))
        if not condition:
            raise ValueError(name)

    def read(name):
        return json.loads((HERE/name).read_bytes())

    try:
        check('assertions enabled', __debug__)
        cert = read('l141-survivor-full-rows.json')
        replay = read('l141-survivor-full-rows-replay.json')
        prior = read('l141-critical-audit.json')
        programs = ['l141_survivor_full_rows.py', 'verify_l141_survivor_full_rows.py']
        outputs = ['l141-survivor-full-rows.json', 'l141-survivor-full-rows-replay.json']
        names = list(cert['input_hashes_before'])+programs+outputs+[
            '../../lemmas/L141-first-l140-mismatch-intrinsic-survivor.md']
        check('exact 25-input inherited manifest', len(cert['input_hashes_before']) == 25 and
              cert['input_hashes_before'] == cert['input_hashes_after'] == replay['input_hashes'] and
              set(cert['input_hashes_before']) == set(prior['input_sha256']) | {'l141-critical-audit.json', 'audit_l141.py'})
        for name in names:
            path = (HERE/name).resolve()
            check('notebook-local input '+name, path.is_relative_to(HERE.parent.parent))
            out['input_sha256'][name] = digest(path)
        for name, value in cert['input_hashes_before'].items():
            check('complete inherited binding '+name, out['input_sha256'][name] == value)
        check('complete prior audit verdict', not prior['failures'] and len(prior['checks']) == 431 and
              all(c['passes'] for c in prior['checks']) and prior['original_artifacts_byte_unchanged'] and
              len(prior['runs']) == 2 and all(r['returncode'] == 0 for r in prior['runs']) and
              prior['audit_code_sha256'] == digest(HERE/'audit_l141.py') and
              all(digest(HERE/n) == h for n, h in prior['input_sha256'].items()))
        check('producer and replay byte bindings', cert['producer_sha256'] == digest(HERE/programs[0]) and
              replay['verifier_sha256'] == digest(HERE/programs[1]) and
              replay['producer_certificate_sha256'] == digest(HERE/outputs[0]) and
              cert['failures'] == cert['unresolved'] == replay['failures'] == replay['unresolved'] == [])

        # Preserve ../.. paths in inherited manifests, without copying other notebooks.
        with TemporaryDirectory(prefix='l142-audit-', dir=HERE) as temp:
            root = Path(temp)/'notebook'/'scripts'/'seven-coordinate'
            root.mkdir(parents=True)
            for name in names:
                dest = (root/name).resolve()
                check('isolated path containment '+name, dest.is_relative_to(Path(temp)))
                dest.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(HERE/name, dest)
            for program in programs:
                result = subprocess.run([sys.executable, '-E', '-B', str(root/program)],
                                        capture_output=True, text=True, check=False)
                out['runs'].append(dict(program=program, returncode=result.returncode,
                    stdout=result.stdout.replace(temp, '<isolated-copy>'),
                    stderr=result.stderr.replace(temp, '<isolated-copy>')))
                check('complete isolated execution '+program, result.returncode == 0)
            for name in names:
                check('byte reproduction/preservation '+name, digest(root/name) == out['input_sha256'][name])

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
            exterior_projection_pivots=336,bound_inputs=len(names),inherited_bound_inputs=25)
    except Exception as error:
        out['failures'].append(f'{type(error).__name__}: {error}')
    finally:
        preserved = all(digest(HERE/name) == h for name,h in out['input_sha256'].items())
        out['original_artifacts_byte_unchanged'] = preserved
        if not preserved:
            out['failures'].append('An original changed')
        out['audit_code_sha256'] = digest(Path(__file__))
        out['qualification'] = 'Restricted existing exclusion only; shared Python/residue arithmetic and inherited finite certificates; no new census or assembly.'
        target = HERE/'l142-critical-audit.json'
        target.write_text(json.dumps(out,indent=2)+'\n')
        print(json.dumps(out.get('summary',{}),sort_keys=True))
        print(f"Checks {sum(c['passes'] for c in out['checks'])}/{len(out['checks'])}; failures {out['failures']}; originals unchanged {preserved}; certificate {target}")
    if out['failures']:
        raise SystemExit(1)


if __name__ == '__main__':
    run()
