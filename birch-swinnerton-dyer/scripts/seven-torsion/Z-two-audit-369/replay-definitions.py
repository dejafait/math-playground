"""Complete V table: full fixed inputs, one production, independent original-H replay."""
from pathlib import Path
from fractions import Fraction as F
import hashlib,json,subprocess,sys,time
sys.set_int_max_str_digits(0)
D=Path(__file__).resolve().parent;ROOT=D.parents[2];S=D.parent;START=time.monotonic()
def read(p):return json.loads(p.read_text())
def need(x,s):
    if not x:raise ArithmeticError(s)
def save(n,x):
    with (D/n).open('x') as f:json.dump(x,f,separators=(',',':'));f.write('\n')
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def tr(a):return [list(r) for r in zip(*a)]
def mm(a,b):
    cols=list(zip(*b))
    return [[sum(x*y for x,y in zip(r,c) if x and y) for c in cols] for r in a]
def run(n,r):
    with (D/(n+'.log')).open('x') as log:
        rc=subprocess.run([sys.executable,'-B',str(D/n)],stdout=log,stderr=subprocess.STDOUT).returncode
    need(rc==0,'first_failure_'+n+'_exit_'+str(rc))
    report=read(D/r);need(report['status']=='PASS' and not report['failures'],'complete_'+r)
    return report
def divisions(prefix,basis,table,radical=None,folder=None,action_prefix='old-U-'):
    folder=(OLD if prefix.startswith(('original343-','original347-')) else D) if folder is None else folder
    V=basis['scaled_polynomials'];H=basis['H'];scale=basis['scale'];count=0
    if radical is not None:W=tr(mm(tr(V),radical))
    for i in range(48):
        cert=read(folder/(prefix+'%02d.json'%i))
        need(type(cert['i']) is int and cert['i']==i and len(cert['products'])==48,'full_division_row')
        if radical is not None:
            A=read(D/(action_prefix+'action-%02d.json'%i));JA=mm(radical,A)
            need(JA==mm(tr(table[i]),radical),'all_persisted_action_coordinate_slots')
            expansion=tr(mm(tr(V),JA))
        for j,e in enumerate(cert['products']):
            need(type(e['j']) is int and e['j']==j and len(e['dividend'])==95
                and all(type(x) is int for x in e['dividend']) and len(e['quotient'])==47
                and len(e['remainder'])==95 and all(type(x) is str for x in e['quotient']+e['remainder']),
                'all_exact_division_shapes_and_types')
            actual=[0]*95;right=V[j] if radical is None else W[j]
            for a,x in enumerate(V[i]):
                if x:
                    for b,y in enumerate(right):
                        if y:actual[a+b]+=x*y
            if radical is None:
                for k,c in enumerate(table[i][j]):
                    if c:
                        for a,x in enumerate(V[k]):
                            if x:actual[a]-=scale*c*x
            else:
                for a,x in enumerate(expansion[j]):actual[a]-=scale*x
            need(actual==e['dividend'],'actual_dividend_'+str((prefix,i,j)))
            q=list(map(F,e['quotient']));rem=list(map(F,e['remainder']))
            need(not any(rem),'all_95_remainder_positions_zero')
            reconstructed=rem[:]
            for a,x in enumerate(q):
                if x:
                    for b,h in enumerate(H):
                        if h:reconstructed[a+b]+=x*h
            need(actual==reconstructed,'full_H_division_'+str((prefix,i,j)));count+=1
    need(count==2304,'entire_division_set');return count

def shape(a,h,w):
    need(type(a) is list and len(a)==h and all(type(r) is list and len(r)==w for r in a),'integer_matrix_shape')
    need(all(type(x) is int for r in a for x in r),'all_integer_entries')
def rat(a):
    need(all(type(x) in (str,int) for r in a for x in r),'no_float_rationals')
    return [[F(x) for x in r] for r in a]
