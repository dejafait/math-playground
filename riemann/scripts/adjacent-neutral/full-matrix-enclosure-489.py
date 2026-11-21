#!/usr/bin/env python3
"""Complete C744l finite matrices by the SAME exact power-log functional.

All 255 columns, both signs, all257 projection rows, complete covariance.
Multiprocessing only batches independent integer arithmetic, never agents.
Persistent per-column/per-piece checkpoints permit interruption recovery.
No analytic audit, beta_1, RH or novelty claim is made by this program.
"""
import concurrent.futures as cf
import gzip
import hashlib
import importlib.util
import json
import os
from pathlib import Path
from fractions import Fraction as F
from math import lcm
import subprocess
import sys
import time

sys.set_int_max_str_digits(0)
HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
WORK = HERE/'full-matrix-489'
WORK.mkdir(exist_ok=True)
spec = importlib.util.spec_from_file_location('matrix488', HERE/'matrix-enclosure-488.py')
p = importlib.util.module_from_spec(spec)
spec.loader.exec_module(p)
m, B, S, ZERO, ONE = p.m, p.B, p.S, p.ZERO, p.ONE
INDICES = tuple(range(2,257))
GRID_BITS = 512
GRID_S = 1 << GRID_BITS
GRID_UNIT = S//GRID_S
DEN_ROOT = 1
for _k in range(1,2050): DEN_ROOT = lcm(DEN_ROOT,_k)
DEN = DEN_ROOT**3
WEIGHTS = [[DEN//(k+1)**r for k in range(2049)] for r in (1,2,3)]
EXE = WORK/'exact-gram-489'


def grid(x):
    return B((x.lo//GRID_UNIT)*GRID_UNIT,
             m.scalar.ceildiv(x.hi,GRID_UNIT)*GRID_UNIT)


def enc(x):
    assert x.lo%GRID_UNIT==x.hi%GRID_UNIT==0
    return [str(x.lo//GRID_UNIT),str(x.hi//GRID_UNIT)]


def dec(x):
    return B(int(x[0])*GRID_UNIT,int(x[1])*GRID_UNIT)


def matenc(a): return [[enc(x) for x in row] for row in a]
def matdec(a): return [[dec(x) for x in row] for row in a]


def dumpgz(path,value):
    temp = Path(str(path)+'.part')
    with gzip.open(temp,'wt',compresslevel=1) as f:
        json.dump(value,f,separators=(',',':'))
    os.replace(temp,path)


def loadgz(path):
    with gzip.open(path,'rt') as f: return json.load(f)


def weighted_hankel(a,order,last):
    """sum_i a[i]*DEN/(i+k+1)^order for ALL k0..last, exactly.

    This is coefficient len(a)-1+k of reversed(a)*weights[order-1].
    No integral approximation or rounded intermediate moment is used.
    """
    values = m.iconv(a[::-1],WEIGHTS[order-1][:len(a)+last])
    return values[len(a)-1:len(a)+last]


def moment_numerators(pair):
    pm,_ = m.midpoint(pair[0]); qm,_ = m.midpoint(pair[1])
    up = weighted_hankel(pm,1,1024)
    uq = weighted_hankel(qm,2,1024)
    vp = weighted_hankel(pm,2,256)
    vq = weighted_hankel(qm,3,256)
    return pm,qm,[a-b for a,b in zip(up,uq)],[-a+2*b for a,b in zip(vp,vq)]


def initialize():
    global CONST,RATIOS,Q,H,TRANSFORMS,LENGTHS
    CONST,_,RATIOS,_ = m.scalar.scalar_inputs()
    Q = [m.rational(x) for x in m.action.quotient_coefficients(F(1,2),97)[1:]]
    H = [m.rational(x/2) for x in m.action.quotient_coefficients(F(-3,2),97)[1:]]
    half,b = B.rational(1,2),CONST['split_b']
    LENGTHS = (b,half-b,half)
    TRANSFORMS = [m.projection_polynomials(u,v)
                  for u,v in ((ZERO,b),(half,b-half),(ONE,-half))]


def column(n):
    path = WORK/f'column-{n}.json.gz'
    if path.exists():
        return n,'reused'
    saved = WORK/f'coefficients-{n}.json.gz'
    if saved.exists():
        raw = loadgz(saved)
        pieces = [{'g':[p.ball(x) for x in v['g']],
                   'signs':{int(s):([p.ball(x) for x in a['P']],
                                    [p.ball(x) for x in a['Q']])
                            for s,a in v['signs'].items()}} for v in raw]
    else:
        pieces = m.build_column(n,CONST,RATIOS[n-2],Q,H)
        raw = [{'g':[x.json() for x in v['g']],
                'signs':{str(s):{'P':[x.json() for x in pair[0]],
                                'Q':[x.json() for x in pair[1]]}
                         for s,pair in v['signs'].items()}} for v in pieces]
        dumpgz(saved,raw)
    result = {'n':n,'grid_bits':GRID_BITS,'signs':{},
              'coefficients_sha256':hashlib.sha256(saved.read_bytes()).hexdigest()}
    for s in (-1,1):
        power=[]; errors=[]
        for j,piece in enumerate(pieces):
            pair=piece['signs'][s]
            pm,qm,u,v=moment_numerators(pair)
            # These are exact rational midpoint operands for the native dot
            # products; save all of them. All padding is an exact zero.
            left=pm+[0]*(1025-len(pm))+qm+[0]*(257-len(qm))
            assert len(left)==len(u)+len(v)==1282
            dumpgz(WORK/f'dot-{s}-{j}-{n}.json.gz',
                   {'left':[str(x) for x in left],
                    'right':[str(x) for x in u+v]})
            size,error=m.action_size_error(pair)
            errors.append([str(size),str(error)])
            moments=[]
            for x in u[:257]:
                center=B.rational(x,DEN*S)
                moments.append(B(center.lo-error,center.hi+error))
            power.append(moments)
        projected=[]
        for k in range(257):
            x=ZERO
            for j in range(3):
                x=x+m.interval_dot(TRANSFORMS[j][k],power[j])*LENGTHS[j]
            projected.append(grid(x))
        result['signs'][str(s)]={'projected_moments':[enc(x) for x in projected],
                                 'piece_size_error':errors}
    dumpgz(path,result)
    return n,'computed'


def native_piece(job):
    s,j=job
    path=WORK/f'gram-piece-{s}-{j}.json.gz'
    if path.exists(): return s,j,'reused'
    inp=WORK/f'native-input-{s}-{j}.txt'
    with inp.open('w') as f:
        f.write(f'{len(INDICES)} 1282\n')
        for n in INDICES:
            v=loadgz(WORK/f'dot-{s}-{j}-{n}.json.gz')
            f.write('\n'.join(v['left'])+'\n'+'\n'.join(v['right'])+'\n')
    # Keep the complete native input compressed; no omitted midpoint operand.
    proc=subprocess.Popen([str(EXE)],stdin=inp.open('r'),stdout=subprocess.PIPE,
                          text=True)
    out=[]
    for i in range(len(INDICES)):
        row=[]
        for k in range(i,len(INDICES)):
            text=proc.stdout.readline()
            if not text: raise RuntimeError('native dot product ended early')
            row.append(text.strip())
        out.append(row)
    assert not proc.stdout.read().strip()
    assert proc.wait()==0
    dumpgz(path,{'sign':s,'piece':j,'indices':list(INDICES),
                 'denominator':str(DEN*S*S),'upper_triangle':out,
                 'input_sha256':hashlib.sha256(inp.read_bytes()).hexdigest()})
    with inp.open('rb') as src,gzip.open(str(inp)+'.gz','wb',compresslevel=1) as dest:
        while chunk:=src.read(1<<20): dest.write(chunk)
    inp.unlink()  # Only this newly created duplicate; complete input retained.
    return s,j,'computed'


def shifted_ldl(a):
    n=len(a); lower=[[ZERO]*n for _ in range(n)]; pivots=[]
    for j in range(n):
        value=a[j][j]-B.rational(1,25)
        for k in range(j): value=value-lower[j][k]*lower[j][k]*pivots[k]
        pivot=grid(value); pivots.append(pivot)
        if pivot.lo<=0:
            return {'passed':False,'failed_index':INDICES[j],
                    'pivots':[enc(x) for x in pivots],'lower':matenc(lower)}
        lower[j][j]=ONE
        for i in range(j+1,n):
            value=a[i][j]
            for k in range(j): value=value-lower[i][k]*lower[j][k]*pivots[k]
            lower[i][j]=grid(value/pivot)
        if j%32==0: print(f'LDL column {INDICES[j]}',flush=True)
    return {'passed':True,'failed_index':None,
            'pivots':[enc(x) for x in pivots],'lower':matenc(lower)}


def self_checks():
    checks={}
    cases=[([2,-3,7],1,6),([-4,0,5],2,7),([1,-2**2500,3],3,3)]
    checks['all_batched_moment_test_coefficients']=all(
        weighted_hankel(a,r,last)==[
            sum(x*(DEN//(i+k+1)**r) for i,x in enumerate(a))
            for k in range(last+1)] for a,r,last in cases)
    small=WORK/'native-small-test.txt'
    left=[[2,-3,7],[-4,0,5],[2**2500,1,-2**2400]]
    right=[[6,-2,1],[-3,8,2],[2,-2**2100,3]]
    small.write_text('3 3\n'+'\n'.join(str(x) for a,b in zip(left,right) for x in a+b)+'\n')
    raw=subprocess.check_output([str(EXE)],input=small.read_bytes()).decode().split()
    checks['every_native_signed_dot_test']=list(map(int,raw))==[
        sum(x*y for x,y in zip(left[i],right[j])) for i in range(3) for j in range(i,3)]
    checks['all_257_integer_legendre_recurrences']=m.check_integer_polynomials()
    checks['all_unsimplified_kernel_identity_comparisons']=m.check_kernel_identity()
    return checks


def assemble(s,checks):
    path=WORK/f'full-sign-{s}.json.gz'
    if path.exists():
        d=loadgz(path)
        checks.update(d['checks'])
        return d['summary']
    size=len(INDICES)
    rows=[loadgz(WORK/f'column-{n}.json.gz')['signs'][str(s)] for n in INDICES]
    projected=[[dec(x) for x in row['projected_moments']] for row in rows]
    gram=[[ZERO]*size for _ in range(size)]
    for piece in range(3):
        raw=loadgz(WORK/f'gram-piece-{s}-{piece}.json.gz')
        assert int(raw['denominator'])==DEN*S*S
        for i in range(size):
            for j in range(i,size):
                center=B.rational(int(raw['upper_triangle'][i][j-i]),DEN*S*S)
                b1,e1=map(int,rows[i]['piece_size_error'][piece])
                b2,e2=map(int,rows[j]['piece_size_error'][piece])
                error=m.scalar.ceildiv(b1*e2+b2*e1+e1*e2,S)
                value=B(center.lo-error,center.hi+error)*LENGTHS[piece]
                gram[i][j]=gram[j][i]=grid(gram[i][j]+value)
        del raw
    head=[[grid(projected[j][n]-RATIOS[n-2]*projected[j][n%2])
           for j in range(size)] for n in INDICES]
    cov=[[ZERO]*size for _ in range(size)]; schur=[[ZERO]*size for _ in range(size)]
    for i in range(size):
        for j in range(i,size):
            cov[i][j]=cov[j][i]=grid(gram[i][j]-m.interval_dot(projected[i],projected[j]))
            schur[i][j]=schur[j][i]=grid((head[i][j]+head[j][i]).integer_div(2)
                                       -cov[i][j]*B.rational(250,171))
    old=json.loads((HERE/'matrix-enclosure-488.json').read_text())
    d=old['signs'][str(s)]
    overlap=lambda x,y: x.lo<=y.hi and y.lo<=x.hi
    local={f'{s}_all_old_projection_intervals_overlap':all(
        overlap(projected[n-2][k],p.ball(d['projected_moments'][i][k]))
        for i,n in enumerate(old['indices']) for k in range(257)),
        f'{s}_all_old_matrix_intervals_overlap':all(
        overlap(mat[n-2][other-2],p.ball(d[key][i][j]))
        for key,mat in (('unsymmetrized_head',head),('total_gram',gram),
                        ('complete_covariance',cov),('schur',schur))
        for i,n in enumerate(old['indices']) for j,other in enumerate(old['indices']))}
    ldl=shifted_ldl(schur)
    width=F(max(x.hi-x.lo for a in (head,gram,cov,schur) for row in a for x in row),S)
    pivot=F(min(dec(x).lo for x in ldl['pivots']),S)
    local[f'{s}_complete_shifted_ldl_positive']=ldl['passed'] and len(ldl['pivots'])==255
    local[f'{s}_matrix_width_below_1e_minus_30']=width<F(1,10**30)
    summary={'sign':s,'finite_lower_bound':m.scalar.frac_json(F(1,25)) if ldl['passed'] else None,
             'minimum_pivot_lower':m.scalar.frac_json(pivot),
             'maximum_matrix_interval_width':m.scalar.frac_json(width),
             'ldl_passed':ldl['passed'],'failed_index':ldl['failed_index'],
             'artifact':str(path.relative_to(ROOT))}
    dumpgz(path,{'indices':list(INDICES),'grid_bits':GRID_BITS,
        'projected_moments':matenc(projected),'unsymmetrized_head':matenc(head),
        'total_gram':matenc(gram),'complete_covariance':matenc(cov),
        'schur':matenc(schur),'shifted_ldl':ldl,'checks':local,'summary':summary})
    checks.update(local)
    print(f'sign{s:+}: full LDL={ldl["passed"]}; minimum pivot>{float(pivot):.12g}; '
          f'width<={m.scalar.up(width)}; required matrix threshold1/25, width<1e-30',flush=True)
    return summary


def main():
    start=time.monotonic()
    subprocess.run(['/usr/bin/clang','-O3','-I/opt/homebrew/include',str(HERE/'exact-gram-489.c'),
                    '-L/opt/homebrew/lib','-lgmp','-o',str(EXE)],check=True)
    checks=self_checks()
    if not all(checks.values()): raise RuntimeError(checks)
    # Split only the reused coefficient archive into the new checkpoint set.
    old=loadgz(HERE/'matrix-coefficients-488.json.gz')
    assert old['precision_bits']==2048
    for n,raw in old['columns'].items():
        target=WORK/f'coefficients-{n}.json.gz'
        if not target.exists(): dumpgz(target,raw)
    del old
    with cf.ProcessPoolExecutor(max_workers=8,initializer=initialize) as pool:
        for n,status in pool.map(column,INDICES,chunksize=1):
            print(f'Column{n} {status}; elapsed{time.monotonic()-start:.1f}s',flush=True)
    initialize()
    print('All255 coefficient maps and all257 projection rows complete.',flush=True)
    with cf.ProcessPoolExecutor(max_workers=6) as pool:
        for s,j,status in pool.map(native_piece,[(s,j) for s in (-1,1) for j in range(3)]):
            print(f'Gram piece{s:+}/{j} {status}; elapsed{time.monotonic()-start:.1f}s',flush=True)
    summaries=[]
    for s in (-1,1): summaries.append(assemble(s,checks))
    result={'scope':'Both COMPLETE255-dimensional C744l finite matrices; analytic inputs unaudited.',
            'indices':list(INDICES),'projection_rows':257,'coefficient_bits':2048,'matrix_grid_bits':512,
            'exact_midpoint_gram_denominator':str(DEN*S*S),
            'signs':summaries,'checks':checks,'failures':[k for k,v in checks.items() if not v],
            'full_finite_two_sign_bound_certified':all(v['ldl_passed'] for v in summaries) and all(checks.values()),
            'analytic_inputs_independently_audited':False,'rh_conclusion':False,
            'unresolved':['Independent audit of C744i/j/k/l and the certificate remains required.',
                          'Remote/non-neutral/odd/all-window actual-Xi signs remain open.']}
    path=Path(__file__).with_suffix('.json')
    path.write_text(json.dumps(result,indent=2)+'\n')
    print(f'Checks{sum(checks.values())}/{len(checks)}; failures{result["failures"]}; certificate{path}',flush=True)
    if result['failures']: raise SystemExit(1)


if __name__=='__main__': main()
