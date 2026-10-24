"""Separate L150 audit; no historical main routines or new census target."""
from collections import Counter
from fractions import Fraction
from hashlib import sha256
from itertools import combinations
from math import prod
from pathlib import Path
from tempfile import TemporaryDirectory
import ast
import json
import shutil
import subprocess
import sys

HERE = Path(__file__).resolve().parent
P = 97
S = [1, 8, 12, 18, 22, 27, 33]
H = [x for x in range(1, P) if pow(x, 16, P) == 1]
J = sorted(set(H)-set(S))


def det(a):
    a = [[Fraction(x) for x in row] for row in a]
    answer = Fraction(1)
    for c in range(len(a)):
        r = next((r for r in range(c, len(a)) if a[r][c]), None)
        if r is None:
            return 0
        if r != c:
            a[c], a[r] = a[r], a[c]
            answer = -answer
        pivot = a[c][c]
        answer *= pivot
        for r in range(c+1, len(a)):
            factor = a[r][c]/pivot
            a[r] = [x-factor*y for x, y in zip(a[r], a[c])]
    assert answer.denominator == 1
    return int(answer)


def dot(a, b):
    assert len(a) == len(b)
    return sum(x*y for x, y in zip(a, b)) % P


def normalize(a):
    factor = pow(next(x for x in a if x), -1, P)
    return [x*factor % P for x in a]


def run():
    out = dict(step_id='2026-10-24-mca-459-l150-critical-audit', checks=[], failures=[],
               input_sha256={}, runs=[], planes=[])

    def check(name, value):
        out['checks'].append(dict(name=name, passes=bool(value)))
        if not value:
            raise ValueError(name)

    def digest(name):
        return sha256((HERE/name).read_bytes()).hexdigest()

    def read(name):
        return json.loads((HERE/name).read_bytes())

    try:
        check('assertions enabled', __debug__)
        programs = ['l149_survivor_full_rows.py', 'verify_l149_survivor_full_rows.py']
        outputs = ['l149-survivor-full-rows.json', 'l149-survivor-full-rows-replay.json']
        cert, replay = map(read, outputs)
        audit, source = read('l149-critical-audit.json'), read('l148-rank20-gates.json')
        names = sorted(set(cert['input_hashes_before']) | set(programs+outputs))
        for name in names:
            check('local path '+name, (HERE/name).resolve().is_relative_to(HERE))
            out['input_sha256'][name] = digest(name)
        check('all original bindings', len(cert['input_hashes_before']) == 504 and
              cert['input_hashes_before'] == cert['input_hashes_after'] == replay['input_hashes'])
        for name, value in cert['input_hashes_before'].items():
            check('original hash '+name, digest(name) == value)
        check('complete L149 audit', audit['failures'] == [] and len(audit['checks']) == 4476 and
              all(c['passes'] for c in audit['checks']) and len(audit['runs']) == 2 and
              all(r['returncode'] == 0 for r in audit['runs']) and audit['original_artifacts_byte_unchanged'] and
              audit['audit_code_sha256'] == digest('audit_l149.py') and len(audit['input_sha256']) == 502)
        check('L149 full manifest equality', set(cert['input_hashes_before']) ==
              set(audit['input_sha256']) | {'l149-critical-audit.json','audit_l149.py'} and
              all(digest(n) == v for n,v in audit['input_sha256'].items()))
        check('program and output bindings', cert['producer_sha256'] == digest(programs[0]) and
              replay['verifier_sha256'] == digest(programs[1]) and
              replay['producer_certificate_sha256'] == digest(outputs[0]) and
              cert['failures'] == replay['failures'] == cert['unresolved'] == replay['unresolved'] == [])
        for name in programs:
            tree = ast.parse((HERE/name).read_text())
            imports = [n for n in tree.body if isinstance(n,(ast.Import,ast.ImportFrom))]
            modules = {n.module if isinstance(n,ast.ImportFrom) else a.name
                       for n in imports for a in n.names}
            check('standalone standard-library imports '+name, modules <=
                  {'collections','hashlib','itertools','pathlib','json'})
        universe = sorted([[sorted(set(a)&set(S)), sorted(set(a)-set(S))]
                           for a in combinations(H,4) if len(set(a)&set(S)) == 2])
        check('independent full universe', len(universe) == 756 and
              read('new-pair-filter.json')['universe'] == universe and cert['H'] == H and cert['S'] == S)
        expected = [
            ('P',[1,0,40,56,96,57,34],[0,45,56,59,65,18,55],[[467,750],[750,467]],
             [(0,[74,22],[1,37],60,[43,65,94,31]),(412,[20,12],[1,20],52,[15,74,82,35]),
              (467,[39,54],[1,76],52,[58,7,31,69]),(750,[59,6],[1,56],52,[18,65,57,84])]),
            ('R',[1,0,31,55,34,85,3],[0,47,67,90,86,57,18],[[608,695],[695,608]],
             [(0,[12,6],[1,49],22,[75,56,28,34]),(412,[64,12],[1,79],50,[85,93,49,15]),
              (608,[5,78],[1,35],50,[90,23,29,35]),(695,[77,11],[1,14],50,[75,66,96,80])])]
        check('two complete planes', len(cert['planes']) == len(replay['planes']) == 2)
        for rec, rep, (label,u,v,indices,table) in zip(cert['planes'],replay['planes'],expected):
            check(label+' exact scope', rec['label'] == label and rec['u'] == u and rec['v'] == v and
                  rec['historical_indices'] == rep['historical_indices'] == indices and
                  len(rec['rows']) == len(rep['rows']) == 756)
            plane = dict(label=label, original_bindings=[], rows=[], successful_rows=[])
            out['planes'].append(plane)
            for pair in indices:
                old = next(r for r in source['records'] if r['indices'] == pair)
                original = read(old['shard'])['cases'][int(old['case_pointer'].split('/')[-1])]
                check(label+' original '+str(pair), original == old['complete_original_record'] and
                      original['fourth_index'] == pair[1] and original['rank'] == 20 and
                      original['kernel_basis'] == old['kernel_basis'] and
                      old['plane_and_all_row_gates']['u'] == u and old['plane_and_all_row_gates']['v'] == v and
                      old['disposition'] == 'intrinsic_survivor')
                check(label+' selected row labels '+str(pair), old['rows'] ==
                      [dict(I=universe[n][0],K=universe[n][1]) for n in [0,412]+pair])
                minor = [[old['original_matrix'][r][c] for c in old['rank_minor_columns']]
                         for r in old['rank_minor_rows']]
                determinant = det(minor)
                check(label+' original minor '+str(pair), determinant % P == old['rank_minor_residue'] != 0)
                plane['original_bindings'].append(dict(indices=pair,shard=old['shard'],pointer=old['case_pointer'],
                                                        integer_minor=determinant,residue=determinant%P))
            fixed_count, alternate_count, groups = 0, 0, {}
            for n, ((i,k), row, evidence) in enumerate(zip(universe,rec['rows'],rep['rows'])):
                tag = f'{label}/{n}'
                check(tag+' exact row', row['row_index'] == evidence['row_index'] == n and
                      row['I'] == evidence['I'] == i and row['K'] == evidence['K'] == k)
                m = [[dot(u,[pow(x,d,P) for x in S]),dot(v,[pow(x,d,P) for x in S])]+
                     [-pow(x,d,P)%P for x in i+k] for d in range(1,9)]
                r, e, piv, basis = (evidence[key] for key in
                    ['moment_rref','left_multiplier','pivot_columns','complete_null_basis'])
                rank = len(piv)
                check(tag+' original matrix', evidence['moment_matrix'] == m and rank == evidence['moment_rank'])
                check(tag+' elimination identity', len(e) == 8 and all(len(a)==8 for a in e) and
                      [[dot(a,col) for col in zip(*m)] for a in e] == r)
                determinant = det(e)
                check(tag+' invertible elimination', determinant == evidence['left_multiplier_integer_determinant'] and
                      determinant % P == evidence['left_multiplier_determinant_residue'] != 0)
                free = [c for c in range(6) if c not in piv]
                check(tag+' full normal form', len(set(piv)) == rank and
                      [[r[a][c] for c in piv] for a in range(rank)] ==
                      [[int(a==b) for b in range(rank)] for a in range(rank)] and
                      len(r) == 8 and all(len(a)==6 for a in r) and not any(x for a in r[rank:] for x in a) and
                      len(basis) == 6-rank and all(len(b)==6 and all(dot(a,b)==0 for a in m) for b in basis) and
                      [[b[c] for c in free] for b in basis] ==
                      [[int(a==b) for b in range(len(free))] for a in range(len(free))])
                error_minor = [a[2:] for a in m[:4]]
                error_det = det(error_minor)
                check(tag+' no pure-error kernel', error_minor == evidence['error_minor_first_four_moment_rows'] and
                      error_det == evidence['error_minor_integer_determinant'] and error_det % P != 0)
                # Derivative of X^16-1 gives g at retained labels, independently of both programs.
                g = {x:(16*pow(x,15,P)*pow(prod(x-y for y in S+k if y!=x)%P,-1,P))%P
                     for x in S+k}
                g.update({x:0 for x in J if x not in k})
                z = min(set(S)-set(i))
                q = [[((g[z] if y==x else 0)-(g[x] if y==z else 0))%P for y in S]
                     for x in S if x not in i+[z]]
                qu,qv = [dot(a,u) for a in q],[dot(a,v) for a in q]
                minors = [(qu[a]*qv[b]-qu[b]*qv[a])%P for a,b in combinations(range(4),2)]
                qr = 2 if any(minors) else int(any(qu+qv))
                check(tag+' independent quotient', row['g_values_on_H'] == [g[x] for x in H] and
                      row['Q'] == q and row['Q_u'] == qu and row['Q_v'] == qv and
                      row['projection_minors'] == minors and row['z'] == z and qr == row['projection_rank'] == rank-4)
                plane['rows'].append(dict(row_index=n,rank=rank,integer_elimination_determinant=determinant,
                                          integer_error_minor=error_det))
                if rank == 6:
                    check(tag+' complete rejection', not basis and row['status']=='rank_two_no_intersection')
                    continue
                check(tag+' only single-line branch', rank == 5 and len(basis) == 1)
                gate = row['recovery']
                alpha,beta = gate['direction_coefficients']
                h = [(alpha*a+beta*b)%P for a,b in zip(u,v)]
                lam = h[S.index(z)]*pow(g[z],-1,P)%P
                weights = [(h[S.index(x)]-lam*g[x])%P for x in i]+[-lam*g[x]%P for x in k]
                check(tag+' entire full moment solution', normalize([alpha,beta]+weights)==normalize(basis[0]) and
                      h == gate['h'] and weights == gate['error_weights'] and lam == gate['lambda_value'] and
                      lam and all(weights) and gate['failed_gates']==[] and gate['passes_intrinsic'] and
                      row['status']=='intrinsic_success' and gate['normalized_direction']==normalize([alpha,beta]))
                err = dict(zip(i+k,weights))
                identity = [((h[S.index(x)] if x in S else 0)-err.get(x,0)-lam*g[x])%P for x in H]
                moments = [sum(((h[S.index(x)] if x in S else 0)-err.get(x,0))*pow(x,d,P) for x in H)%P
                           for d in range(1,9)]
                check(tag+' all identities and chart', identity == gate['identity_residuals'] == [0]*16 and
                      moments == gate['shifted_moment_residuals'] == [0]*8 and
                      gate['prescribed_finite_gate']==dict(D_coefficient=alpha,C_coefficient=-beta%P))
                fixed = evidence['all_nonzero_projection_pivots']
                check(tag+' full fixed pivot domain', [a['component'] for a in fixed] ==
                      [j for j in range(4) if qu[j] or qv[j]])
                for a in fixed:
                    scale=a['scale']; j=a['component']
                    check(tag+' fixed pivot '+str(j), scale and a['direction']==[-qv[j]%P,qu[j]]==
                          [scale*x%P for x in [alpha,beta]] and a['lambda_value']==scale*lam%P and
                          a['error_weights']==[scale*x%P for x in weights])
                exterior = [[(u[a]*v[b]-u[b]*v[a])%P for b in range(7)] for a in range(7)]
                alternatives = evidence['all_exterior_and_projection_pivot_recoveries']
                domains=[]
                for a,b in combinations(range(7),2):
                    pv=exterior[a][b]
                    if not pv:
                        continue
                    uu=[exterior[x][b]*pow(pv,-1,P)%P for x in range(7)]; vv=exterior[a]
                    for j,cov in enumerate(q):
                        if dot(cov,uu) or dot(cov,vv):
                            domains.append(([a,b],j))
                check(tag+' full exterior pivot domain', [(a['pivot'],a['projection_component']) for a in alternatives]==domains)
                for index,a in enumerate(alternatives):
                    b,c=a['pivot']; uu,vv=a['u'],a['v']; j=a['projection_component']; scale=a['scale']
                    direction=[-dot(q[j],vv)%P,dot(q[j],uu)]
                    hh=[(direction[0]*x+direction[1]*y)%P for x,y in zip(uu,vv)]
                    ll=hh[S.index(z)]*pow(g[z],-1,P)%P
                    ww=[(hh[S.index(x)]-ll*g[x])%P for x in i]+[-ll*g[x]%P for x in k]
                    check(tag+' exterior recovery '+str(index), a['nonzero_value']==exterior[b][c]!=0 and
                          uu==[exterior[x][c]*pow(exterior[b][c],-1,P)%P for x in range(7)] and vv==exterior[b] and
                          [[(uu[x]*vv[y]-uu[y]*vv[x])%P for y in range(7)] for x in range(7)]==exterior and
                          a['direction']==direction and a['h']==hh==[scale*x%P for x in h] and scale and
                          a['lambda_value']==ll==scale*lam%P and a['error_weights']==ww==[scale*x%P for x in weights])
                fixed_count+=len(fixed); alternate_count+=len(alternatives)
                groups.setdefault(tuple(normalize([alpha,beta])),[]).append(n)
                plane['successful_rows'].append((n,[alpha,beta],normalize([alpha,beta]),lam,weights))
            check(label+' exact published table', plane['successful_rows']==table)
            dg=[dict(direction=list(d),row_indices=rows) for d,rows in sorted(groups.items())]
            check(label+' distinct directions and complete counts', rec['direction_groups']==rep['direction_groups']==dg and
                  len(groups)==4 and all(len(rows)==1 for rows in groups.values()) and
                  dict(Counter(a['rank'] for a in plane['rows']))=={5:4,6:752} and
                  fixed_count==15 and alternate_count==300 and rec['summary']==rep['summary'] and
                  rec['summary']['distinct_directions_before_chart']==4 and rec['summary']['required_distinct_directions']==12 and
                  rec['disposition']=='excluded_necessary_shortfall')
            plane['summary']=dict(covered=756,required=756,full_directions=4,necessary_directions=12,
                                  shortfall=8,fixed_pivots=fixed_count,alternative_pivots=alternate_count)
        with TemporaryDirectory(prefix='l150-audit-',dir=HERE) as temp:
            isolated=Path(temp)/'reed-solomon-mca'/'scripts'/'seven-coordinate'
            for name in names:
                destination=isolated/name
                destination.parent.mkdir(parents=True,exist_ok=True)
                shutil.copyfile(HERE/name,destination)
            for name in programs:
                result=subprocess.run([sys.executable,'-E','-B',str(isolated/name)],cwd=isolated.parent.parent,
                                      capture_output=True,text=True,check=False)
                out['runs'].append(dict(program=name,returncode=result.returncode,
                                       stdout=result.stdout.replace(temp,'<isolated-copy>'),stderr=result.stderr.replace(temp,'<isolated-copy>')))
                check('isolated complete execution '+name,result.returncode==0)
            for name in names:
                check('isolated byte preservation '+name,sha256((isolated/name).read_bytes()).hexdigest()==out['input_sha256'][name])
        out['summary']=dict(plane_support_cases=1512,required_cases=1512,full_rows=8,rank6_rejections=1504,
                            fixed_pivots=30,alternative_pivots=600,pointwise_entries=128,original_moments=64,
                            inherited_bindings=504,bound_originals=len(names),byte_identical_outputs=2,required_outputs=2,
                            directions_per_plane=4,necessary_per_plane=12,ordered_applications=4)
    except Exception as exc:
        out['failures'].append(f'{type(exc).__name__}: {exc}')
    finally:
        preserved=all(digest(name)==value for name,value in out['input_sha256'].items())
        out['original_artifacts_byte_unchanged']=preserved
        if not preserved:
            out['failures'].append('Original artifact changed')
        out['audit_code_sha256']=sha256(Path(__file__).read_bytes()).hexdigest()
        out['qualification']='Restricted separate audit; shared Python/residue arithmetic and inherited finite certificates; no assembly or global improvement.'
        target=HERE/'l150-critical-audit.json'
        target.write_text(json.dumps(out,indent=2)+'\n')
        print(json.dumps(out.get('summary',{}),sort_keys=True))
        print(f"Checks {sum(c['passes'] for c in out['checks'])}/{len(out['checks'])}; failures {out['failures']}; originals unchanged {preserved}; certificate {target}")
    if out['failures']:
        raise SystemExit(1)


if __name__=='__main__':
    run()
