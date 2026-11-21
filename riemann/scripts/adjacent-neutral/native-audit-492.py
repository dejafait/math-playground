#!/usr/bin/env python3
"""Read-only source archives; exhaustive native provenance/product/sign audit.

Reuses audited action/scalar interval formulas and shared GMP. Fresh native
summation and an independent 512-bit row-wise LDL implementation are used.
All inputs, output products, matrix endpoints and factors have certificates.
"""
import concurrent.futures as cf
from fractions import Fraction as F
import gzip
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import time

sys.set_int_max_str_digits(0)
HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('source489',HERE/'full-matrix-enclosure-489.py')
q=importlib.util.module_from_spec(spec);spec.loader.exec_module(q)
OUT=HERE/'native-audit-492';OUT.mkdir(exist_ok=True)
EXE=OUT/'reverse-gram-492'
B,S,ZERO=q.B,q.S,q.ZERO
G=1<<512

def sha(path):
    h=hashlib.sha256()
    with path.open('rb') as f:
        while block:=f.read(1<<20):h.update(block)
    return h.hexdigest()

def save(path,data):
    path.write_text(json.dumps(data,indent=2)+'\n')

def require(value,label):
    if not value:raise RuntimeError(label)

def audit_piece(job):
    sign,piece=job;start=time.monotonic()
    raw=q.loadgz(q.WORK/f'gram-piece-{sign}-{piece}.json.gz')
    checks={'indices':raw['indices']==list(q.INDICES),
            'sign_piece':raw['sign']==sign and raw['piece']==piece,
            'denominator':int(raw['denominator'])==q.DEN*S*S,
            'triangular_dimensions':len(raw['upper_triangle'])==255 and all(
                len(row)==255-i for i,row in enumerate(raw['upper_triangle']))}
    require(all(checks.values()),checks)
    proc=subprocess.Popen([str(EXE)],stdin=subprocess.PIPE,stdout=subprocess.PIPE)
    digest=hashlib.sha256();dots=[];count=0
    with gzip.open(q.WORK/f'native-input-{sign}-{piece}.txt.gz','rb') as src:
        header=src.readline();require(header==b'255 1282\n','header')
        digest.update(header);proc.stdin.write(header)
        for n in q.INDICES:
            path=q.WORK/f'dot-{sign}-{piece}-{n}.json.gz'
            operands=q.loadgz(path);dots.append({'n':n,'sha256':sha(path)})
            require(len(operands['left'])==len(operands['right'])==1282,'dot dimensions')
            for side in ('left','right'):
                for expected in operands[side]:
                    line=src.readline()
                    require(line==(expected+'\n').encode(),f'input mismatch {sign}/{piece}/{n}/{side}/{count}')
                    count+=1;digest.update(line);proc.stdin.write(line)
        require(src.read()==b'','extra native input')
    proc.stdin.close()
    checks['all_653820_input_integers_match']=count==255*2564
    checks['uncompressed_input_hash']=digest.hexdigest()==raw['input_sha256']
    require(all(checks.values()),checks)
    output=OUT/f'products-{sign}-{piece}.txt.gz';products=0
    with gzip.open(output,'wb',compresslevel=1) as dst:
        for i,row in enumerate(raw['upper_triangle']):
            for off,expected in enumerate(row):
                line=proc.stdout.readline()
                require(line==(expected+'\n').encode(),f'product mismatch {sign}/{piece}/{i}/{i+off}')
                dst.write(line);products+=1
        require(proc.stdout.read()==b'','extra native output')
    checks['fresh_native_exit_zero']=proc.wait()==0
    checks['all_32640_products_match']=products==32640
    result={'sign':sign,'piece':piece,'checks':checks,'input_integer_count':count,
            'product_count':products,'uncompressed_input_sha256':digest.hexdigest(),
            'archived_products_sha256':sha(q.WORK/f'gram-piece-{sign}-{piece}.json.gz'),
            'fresh_products_sha256':sha(output),'dot_artifacts':dots,
            'failures':[k for k,v in checks.items() if not v]}
    save(OUT/f'piece-{sign}-{piece}.json',result)
    print(f'Native {sign:+}/{piece}: {count} input integers, {products}/32640 exact products; '
          f'failures={result["failures"]}; {time.monotonic()-start:.1f}s',flush=True)
    return result

# Separate integer endpoint arithmetic, rounding every primitive to 512 bits.
# Matrices enclose the same exact quantities; endpoint equality with the old
# LDL is neither required nor asserted.
def ceil(n,d):
    require(d>0,'positive divisor');return -((-n)//d)
def add(x,y):return (x[0]+y[0],x[1]+y[1])
def sub(x,y):return (x[0]-y[1],x[1]-y[0])
def mul(x,y):
    corners=[a*b for a in x for b in y]
    return (min(corners)//G,ceil(max(corners),G))
def div(x,y):
    require(y[0]>0,'positive interval divisor')
    return (min(a*G//b for a in x for b in y),max(ceil(a*G,b) for a in x for b in y))
def independent_ldl(matrix):
    size=len(matrix);lower=[[(0,0)]*size for _ in range(size)];diag=[]
    shift=(G//25,ceil(G,25))
    for i in range(size):
        lower[i][i]=(G,G)
        for j in range(i):
            value=matrix[i][j]
            for k in range(j):value=sub(value,mul(mul(lower[i][k],lower[j][k]),diag[k]))
            lower[i][j]=div(value,diag[j])
        value=sub(matrix[i][i],shift)
        for k in range(i):value=sub(value,mul(mul(lower[i][k],lower[i][k]),diag[k]))
        require(value[0]>0,f'nonpositive independent pivot {i+2}')
        diag.append(value)
        if i%64==0:print(f'Independent LDL row {i+2}/{size+1}',flush=True)
    return {'passed':True,'pivots':[[str(a),str(b)] for a,b in diag],
            'lower':[[[str(a),str(b)] for a,b in row] for row in lower],
            'denominator_bits':512,'shift':{'numerator':1,'denominator':25}}

def projection_dots(projected,sign):
    exe=OUT/'interval-projection-489'
    inp=OUT/f'projection-input-{sign}.txt'
    inp.write_text('255 257\n'+'\n'.join(' '.join(q.enc(x)) for row in projected for x in row)+'\n')
    values=subprocess.check_output([str(exe)],input=inp.read_bytes()).decode().splitlines()
    require(len(values)==32640,'projection output dimension')
    matrix=[[ZERO]*255 for _ in range(255)];index=0;raw=[]
    for i in range(255):
        row=[]
        for j in range(i,255):
            lo,hi=values[index].split();index+=1;row.append([lo,hi])
            matrix[i][j]=matrix[j][i]=B(int(lo)*(1<<1024),int(hi)*(1<<1024))
        raw.append(row)
    q.dumpgz(OUT/f'projection-dots-{sign}.json.gz',{'upper_triangle':raw,
             'endpoint_denominator_bits':1024,'input_sha256':sha(inp)})
    return matrix

def audit_sign(sign):
    q.initialize();checks={};size=255
    columns=[q.loadgz(q.WORK/f'column-{n}.json.gz') for n in q.INDICES]
    data=q.loadgz(q.WORK/f'full-sign-{sign}.json.gz')
    checks['indices']=data['indices']==list(q.INDICES)
    projected=[[q.dec(x) for x in c['signs'][str(sign)]['projected_moments']] for c in columns]
    checks['all_projection_endpoints']=q.matenc(projected)==data['projected_moments']
    checks['all_257_projection_rows']=all(len(row)==257 for row in projected)
    gram=[[ZERO]*size for _ in range(size)]
    for piece in range(3):
        raw=q.loadgz(q.WORK/f'gram-piece-{sign}-{piece}.json.gz')
        for i in range(size):
            for j in range(i,size):
                center=B.rational(int(raw['upper_triangle'][i][j-i]),q.DEN*S*S)
                b1,e1=map(int,columns[i]['signs'][str(sign)]['piece_size_error'][piece])
                b2,e2=map(int,columns[j]['signs'][str(sign)]['piece_size_error'][piece])
                error=ceil(b1*e2+b2*e1+e1*e2,S)
                value=B(center.lo-error,center.hi+error)*q.LENGTHS[piece]
                gram[i][j]=gram[j][i]=q.grid(gram[i][j]+value)
        del raw
    checks['every_gram_endpoint']=q.matenc(gram)==data['total_gram']
    head=[[q.grid(projected[j][n]-q.RATIOS[n-2]*projected[j][n%2])
           for j in range(size)] for n in q.INDICES]
    checks['every_head_endpoint']=q.matenc(head)==data['unsymmetrized_head']
    pg=projection_dots(projected,sign)
    cov=[[ZERO]*size for _ in range(size)];schur=[[ZERO]*size for _ in range(size)]
    for i in range(size):
        for j in range(i,size):
            cov[i][j]=cov[j][i]=q.grid(gram[i][j]-pg[i][j])
            schur[i][j]=schur[j][i]=q.grid((head[i][j]+head[j][i]).integer_div(2)-cov[i][j]*B.rational(250,171))
    checks['every_covariance_endpoint']=q.matenc(cov)==data['complete_covariance']
    checks['every_schur_endpoint']=q.matenc(schur)==data['schur']
    checks['symmetric_complete_matrix']=all(q.enc(schur[i][j])==q.enc(schur[j][i]) for i in range(size) for j in range(size))
    width=F(max(x.hi-x.lo for mat in (head,gram,cov,schur) for row in mat for x in row),S)
    checks['matrix_width_below_1e_minus_30']=width<F(1,10**30)
    checks['exact_old_width']=q.m.scalar.frac_json(width)==data['summary']['maximum_matrix_interval_width']
    require(all(checks.values()),checks)
    ints=[[tuple(map(int,q.enc(x))) for x in row] for row in schur]
    ldl=independent_ldl(ints)
    checks['all_255_fresh_shifted_pivots_positive']=len(ldl['pivots'])==255 and all(int(x[0])>0 for x in ldl['pivots'])
    pivot=F(min(int(x[0]) for x in ldl['pivots']),G)
    certificate={'indices':list(q.INDICES),'grid_bits':512,'projected_moments':q.matenc(projected),
                 'unsymmetrized_head':q.matenc(head),'total_gram':q.matenc(gram),
                 'complete_covariance':q.matenc(cov),'schur':q.matenc(schur),'fresh_ldl':ldl}
    q.dumpgz(OUT/f'finite-sign-{sign}.json.gz',certificate)
    result={'sign':sign,'checks':checks,'finite_lower_bound':{'numerator':1,'denominator':25},
            'maximum_matrix_interval_width':q.m.scalar.frac_json(width),
            'minimum_fresh_pivot_lower':q.m.scalar.frac_json(pivot),
            'finite_certificate_sha256':sha(OUT/f'finite-sign-{sign}.json.gz'),
            'failures':[k for k,v in checks.items() if not v]}
    save(OUT/f'sign-{sign}.json',result)
    print(f'Sign {sign:+}: all255 independent shifted pivots positive, minimum>{float(pivot):.12g}; '
          f'matrix width<={q.m.scalar.up(width)}, required<1e-30; finite bound1/25; failures={result["failures"]}',flush=True)
    return result

def main():
    start=time.monotonic()
    sources=['reverse-gram-492.c','interval-projection-489.c','native-audit-492.py',
             'full-matrix-enclosure-489.py','matrix-enclosure-487.py','power-log-enclosure-486.py']
    hashes={name:sha(HERE/name) for name in sources}
    for source,exe in [('reverse-gram-492.c',EXE),('interval-projection-489.c',OUT/'interval-projection-489')]:
        subprocess.run(['/usr/bin/clang','-O3','-I/opt/homebrew/include',str(HERE/source),
                        '-L/opt/homebrew/lib','-lgmp','-o',str(exe)],check=True)
    # Replay provenance of every column against the preceding fresh audit.
    prior=json.loads((HERE/'finite-reconstruction-491.json').read_text())
    require(prior['complete_255_columns'] and prior['indices']==list(q.INDICES) and not prior['failures'],'prior completeness')
    provenance=[]
    for n in q.INDICES:
        old=json.loads((HERE/'finite-reconstruction-491'/f'column-{n}.json').read_text())
        require(old['n']==n and not old['failures'] and all(old['checks'].values()),f'prior column{n}')
        actual={key:sha(q.WORK/f'{prefix}-{n}.json.gz') for key,prefix in [('coefficients','coefficients'),('column','column')]}
        require(actual==old['input_sha256'],f'changed source column{n}')
        provenance.append({'n':n,'source_sha256':actual,'prior_report_sha256':sha(HERE/'finite-reconstruction-491'/f'column-{n}.json')})
    save(OUT/'provenance.json',{'columns':provenance,'prior_summary_sha256':sha(HERE/'finite-reconstruction-491.json'),'failures':[]})
    # Signed/large-integer exact native regression (independent Python products).
    aa=[[2,-3,7],[-4,0,5],[2**2500,1,-2**2400]]
    bb=[[6,-2,1],[-3,8,2],[2,-2**2100,3]]
    inp=('3 3\n'+'\n'.join(str(x) for a,b in zip(aa,bb) for x in a+b)+'\n').encode()
    actual=list(map(int,subprocess.check_output([str(EXE)],input=inp).split()))
    require(actual==[sum(x*y for x,y in zip(aa[i],bb[j])) for i in range(3) for j in range(i,3)],'native regression')
    # Independent interval operations and LDL must reject an indefinite matrix.
    require(mul((-3*G,4*G),(-8*G,-G))==(-32*G,24*G),'signed interval product')
    test=independent_ldl([[(2*G,2*G),(G//2,G//2)],[(G//2,G//2),(G,G)]])
    require(test['passed'],'positive LDL regression')
    rejected=False
    try:independent_ldl([[(G,G),(2*G,2*G)],[(2*G,2*G),(G,G)]])
    except RuntimeError:rejected=True
    require(rejected,'indefinite LDL regression')
    print('Provenance: all255 prior coefficient/column hashes match; signed native and interval/LDL regressions pass.',flush=True)
    with cf.ThreadPoolExecutor(max_workers=6) as pool:
        pieces=list(pool.map(audit_piece,[(s,j) for s in (-1,1) for j in range(3)]))
    signs=[audit_sign(s) for s in (-1,1)]
    failures=[f'{x["sign"]}/{x.get("piece","sign")}/{key}' for x in pieces+signs for key in x['failures']]
    result={'scope':'Exhaustive native input/product audit and full finite-sign reconstruction; shared GMP and reviewed scalar/action formulas.',
            'source_sha256':hashes,'prior_255_columns_bound':True,
            'native_input_integers_compared':sum(x['input_integer_count'] for x in pieces),
            'fresh_midpoint_products_compared':sum(x['product_count'] for x in pieces),
            'pieces':[{'sign':x['sign'],'piece':x['piece'],'evidence':f'native-audit-492/piece-{x["sign"]}-{x["piece"]}.json'} for x in pieces],
            'signs':signs,'failures':failures,'full_finite_two_sign_bound':not failures,
            'independent_integer_library':False,'independent_high_level_action_evaluator':False,
            'rh_conclusion':False,'elapsed_seconds':time.monotonic()-start}
    save(HERE/'native-audit-492.json',result)
    print(f'Complete: {result["native_input_integers_compared"]} input integers, {result["fresh_midpoint_products_compared"]}/195840 fresh products; '
          f'both finite bounds>=I/25; failures={failures}; evidence scripts/adjacent-neutral/native-audit-492.json',flush=True)
    require(not failures,'failed audit')

if __name__=='__main__':main()
