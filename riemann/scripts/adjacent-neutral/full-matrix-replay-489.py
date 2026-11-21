#!/usr/bin/env python3
"""Replay EVERY full saved matrix entry and shifted interval LDL operand.

This verifies the complete finite bookkeeping, not the analytic inputs or
an independent regeneration of the action coefficients/native dot kernel.
"""
import gzip
import hashlib
import importlib.util
import json
from fractions import Fraction as F
from pathlib import Path
import subprocess
import sys

sys.set_int_max_str_digits(0)
HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('full489',HERE/'full-matrix-enclosure-489.py')
q=importlib.util.module_from_spec(spec)
spec.loader.exec_module(q)
m,B,S,ZERO=q.m,q.B,q.S,q.ZERO
q.initialize()
meta=json.loads((HERE/'full-matrix-enclosure-489.json').read_text())
checks={
    'exact_all_255_indices':meta['indices']==list(q.INDICES),
    'all_257_projection_rows_declared':meta['projection_rows']==257,
    'precision_2048_512':meta['coefficient_bits']==2048 and meta['matrix_grid_bits']==512,
    'exact_midpoint_denominator':int(meta['exact_midpoint_gram_denominator'])==q.DEN*S*S,
}
exe=q.WORK/'interval-projection-489'
subprocess.run(['/usr/bin/clang','-O3','-I/opt/homebrew/include',str(HERE/'interval-projection-489.c'),
                '-L/opt/homebrew/lib','-lgmp','-o',str(exe)],check=True)


def projection_dots(projected,label):
    """Exactly the Python2048-bit interval dots, using native integer sums.

    Each input endpoint is a512-bit dyadic. Its products are1024-bit
    dyadics, hence exactly representable on the2048-bit Python grid.
    Taking all four corners and adding their extrema is bit-identical
    to m.interval_dot, with no additional coarsening or assumption.
    """
    n,k=len(projected),len(projected[0])
    inp=q.WORK/f'projection-input-{label}.txt'
    inp.write_text(f'{n} {k}\n'+'\n'.join(' '.join(q.enc(x)) for row in projected for x in row)+'\n')
    values=subprocess.check_output([str(exe)],input=inp.read_bytes()).decode().splitlines()
    assert len(values)==n*(n+1)//2
    matrix=[[ZERO]*n for _ in range(n)]
    raw=[]; idx=0
    for i in range(n):
        row=[]
        for j in range(i,n):
            lo,hi=values[idx].split(); idx+=1
            row.append([lo,hi])
            x=B(int(lo)*(1<<1024),int(hi)*(1<<1024))
            matrix[i][j]=matrix[j][i]=x
        raw.append(row)
    q.dumpgz(q.WORK/f'projection-dots-{label}.json.gz',
             {'endpoint_denominator_bits':1024,'upper_triangle':raw,
              'input_sha256':hashlib.sha256(inp.read_bytes()).hexdigest()})
    return matrix


test=[[q.dec([str(lo),str(hi)]) for lo,hi in row] for row in
      [[(-3,4),(2,7),(-8,-1)],[(0,0),(-7,-2),(1<<510,(1<<510)+5)],
       [(-1<<509,1<<508),(3,3),(-9,-4)]]]
test_dots=projection_dots(test,'test')
checks['all_native_interval_dot_test_endpoints']=all(
    test_dots[i][j].json()==m.interval_dot(test[i],test[j]).json()
    for i in range(len(test)) for j in range(len(test)))
if not checks['all_native_interval_dot_test_endpoints']:
    raise RuntimeError('native interval dot mismatch')
bounds={}
columns=[q.loadgz(q.WORK/f'column-{n}.json.gz') for n in q.INDICES]
checks['all_coefficient_hashes_match']=all(
    hashlib.sha256((q.WORK/f'coefficients-{n}.json.gz').read_bytes()).hexdigest()
    ==v['coefficients_sha256'] for n,v in zip(q.INDICES,columns))
for s in (-1,1):
    data=q.loadgz(q.WORK/f'full-sign-{s}.json.gz')
    projected,head,gram,cov,schur=[q.matdec(data[key]) for key in
        ('projected_moments','unsymmetrized_head','total_gram','complete_covariance','schur')]
    size=len(q.INDICES)
    checks[f'{s}_all_matrix_dimensions']=all(len(a)==size and all(len(row)==size for row in a)
                                              for a in (head,gram,cov,schur))
    checks[f'{s}_every_projection_row']=len(projected)==size and all(len(row)==257 for row in projected)
    checks[f'{s}_all_saved_projection_endpoints']=all(
        [q.enc(x) for x in row]==v['signs'][str(s)]['projected_moments']
        for row,v in zip(projected,columns))
    complete_gram=[[ZERO]*size for _ in range(size)]
    for piece in range(3):
        raw=q.loadgz(q.WORK/f'gram-piece-{s}-{piece}.json.gz')
        digest=hashlib.sha256()
        with gzip.open(q.WORK/f'native-input-{s}-{piece}.txt.gz','rb') as f:
            while chunk:=f.read(1<<20): digest.update(chunk)
        checks[f'{s}_{piece}_complete_native_input_hash']=digest.hexdigest()==raw['input_sha256']
        checks[f'{s}_{piece}_all_triangular_dimensions']=raw['indices']==list(q.INDICES) and (
            len(raw['upper_triangle'])==size and all(len(row)==size-i for i,row in enumerate(raw['upper_triangle'])))
        checks[f'{s}_{piece}_exact_midpoint_denominator']=int(raw['denominator'])==q.DEN*S*S
        for i in range(size):
            for j in range(i,size):
                center=B.rational(int(raw['upper_triangle'][i][j-i]),q.DEN*S*S)
                b1,e1=map(int,columns[i]['signs'][str(s)]['piece_size_error'][piece])
                b2,e2=map(int,columns[j]['signs'][str(s)]['piece_size_error'][piece])
                error=m.scalar.ceildiv(b1*e2+b2*e1+e1*e2,S)
                value=B(center.lo-error,center.hi+error)*q.LENGTHS[piece]
                complete_gram[i][j]=complete_gram[j][i]=q.grid(complete_gram[i][j]+value)
        del raw
    checks[f'{s}_every_gram_endpoint']=q.matenc(complete_gram)==data['total_gram']
    h=[[q.grid(projected[j][n]-q.RATIOS[n-2]*projected[j][n%2])
        for j in range(size)] for n in q.INDICES]
    checks[f'{s}_every_head_endpoint']=q.matenc(h)==data['unsymmetrized_head']
    projection_gram=projection_dots(projected,str(s))
    c=[[ZERO]*size for _ in range(size)]; a=[[ZERO]*size for _ in range(size)]
    for i in range(size):
        for j in range(i,size):
            c[i][j]=c[j][i]=q.grid(complete_gram[i][j]-projection_gram[i][j])
            a[i][j]=a[j][i]=q.grid((h[i][j]+h[j][i]).integer_div(2)-c[i][j]*B.rational(250,171))
    checks[f'{s}_every_covariance_endpoint']=q.matenc(c)==data['complete_covariance']
    checks[f'{s}_every_schur_endpoint']=q.matenc(a)==data['schur']
    checks[f'{s}_exact_interval_symmetry']=all(q.enc(a[i][j])==q.enc(a[j][i])
                                             for i in range(size) for j in range(size))
    ldl=q.shifted_ldl(a)
    checks[f'{s}_every_ldl_operand']=ldl==data['shifted_ldl']
    checks[f'{s}_all_255_shifted_pivots_positive']=ldl['passed'] and len(ldl['pivots'])==255 and all(
        q.dec(x).lo>0 for x in ldl['pivots'])
    width=F(max(x.hi-x.lo for matrix in (h,complete_gram,c,a) for row in matrix for x in row),S)
    pivot=F(min(q.dec(x).lo for x in ldl['pivots']),S)
    checks[f'{s}_exact_width_bound']=m.scalar.frac_json(width)==data['summary']['maximum_matrix_interval_width']
    checks[f'{s}_exact_pivot_bound']=m.scalar.frac_json(pivot)==data['summary']['minimum_pivot_lower']
    checks[f'{s}_width_below_1e_minus_30']=width<F(1,10**30)
    checks[f'{s}_reported_finite_bound']=data['summary']['finite_lower_bound']==m.scalar.frac_json(F(1,25))
    checks[f'{s}_summary_matches_top_level']=data['summary']==next(x for x in meta['signs'] if x['sign']==s)
    bounds[str(s)]={'finite_lower_bound':m.scalar.frac_json(F(1,25)),
                    'maximum_matrix_interval_width':m.scalar.frac_json(width),
                    'minimum_pivot_lower':m.scalar.frac_json(pivot)}
    print(f'sign{s:+}: replay all255 pivots positive={ldl["passed"]}; '
          f'width<={m.scalar.up(width)} (required<1e-30); finite bound1/25',flush=True)
    del data,projected,head,gram,cov,schur,complete_gram,h,c,a,ldl,projection_gram
result={'scope':'Complete finite saved-operation replay; coefficient/native/analytic independent audit pending.',
        'checks':checks,'bounds':bounds,'failures':[k for k,v in checks.items() if not v],
        'analytic_inputs_independently_audited':False,'rh_conclusion':False}
path=Path(__file__).with_suffix('.json')
path.write_text(json.dumps(result,indent=2)+'\n')
print(f'Full replay checks{sum(checks.values())}/{len(checks)}; failures{result["failures"]}; evidence{path}',flush=True)
if result['failures']: raise SystemExit(1)
