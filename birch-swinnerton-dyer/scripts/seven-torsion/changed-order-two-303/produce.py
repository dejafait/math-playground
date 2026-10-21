"""Single changed-order producer; both stages run inside the aggregate runner."""
from pathlib import Path
from fractions import Fraction as F
from functools import reduce
import hashlib, json, math, sys, time
import numpy as np
sys.set_int_max_str_digits(0)
OUT=Path(__file__).resolve().parent
ROOT=OUT.parents[2]
OLD=ROOT/'scripts/seven-torsion/nonmonic-order-283'
PREV=ROOT/'scripts/seven-torsion/radical-overorder-295'
START=time.monotonic(); N=48; P=2; CAP=134217728
REPORT={'status':'INCOMPLETE','phase':'inputs','input_product_slots':0,'action_slots':0,'failures':[]}
I=[[int(i==j) for j in range(N)] for i in range(N)]
def need(ok,label):
    if not ok: raise ArithmeticError(label)

def save(name,x):
    raw=(json.dumps(x,separators=(',',':'))+'\n').encode()
    need(sum(p.stat().st_size for p in OUT.iterdir() if p.is_file())+len(raw)+65536<=CAP,'byte_cap')
    with (OUT/name).open('xb') as f:f.write(raw)

def inventory():
    paths=[ROOT/'scripts/seven-torsion/certificate.json']
    for d in (OLD,PREV,ROOT/'scripts/seven-torsion/radical-overorder-audit-297', ROOT/'scripts/seven-torsion/enlarged-order-test-299', ROOT/'scripts/seven-torsion/enlarged-order-audit-301'):
        paths += [p for p in d.iterdir() if p.is_file()]
    return {str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(paths)}

def mm(a,b):
    cols=list(zip(*b))
    return [[sum(x*y for x,y in zip(row,col) if x and y) for col in cols] for row in a]

def strings(a):return [[str(x) for x in r] for r in a]
def rational(a):return [[F(x) for x in r] for r in a]
def transpose(a):return [list(r) for r in zip(*a)]

def eliminate(matrix):
    a=[[x%P for x in r] for r in matrix]; ops=[]; piv=[]; r=0
    if not a:return {'matrix':[], 'rref':[], 'operations':[], 'pivots':[], 'rank':0, 'kernel':I}
    for c in range(len(a[0])):
        s=next((i for i in range(r,len(a)) if a[i][c]),None)
        if s is None:continue
        if s!=r:a[s],a[r]=a[r],a[s];ops.append(['swap',r,s])
        q=pow(a[r][c],-1,P)
        if q!=1:a[r]=[x*q%P for x in a[r]];ops.append(['scale',r,q])
        for i in range(len(a)):
            if i!=r and a[i][c]:
                q=(-a[i][c])%P
                a[i]=[(x+q*y)%P for x,y in zip(a[i],a[r])]
                ops.append(['add',i,r,q])
        piv.append(c);r+=1
        if r==len(a):break
    free=[c for c in range(len(a[0])) if c not in piv]
    kernel=[]
    for c in free:
        v=[0]*len(a[0]);v[c]=1
        for k,j in enumerate(piv):v[j]=-a[k][c]%P
        kernel.append(v)
    return {'matrix':matrix,'rref':a,'operations':ops,'pivots':piv,'rank':r,'kernel':kernel}

def lattice(kernel,name):
    red=eliminate(kernel)
    rows=red['rref'][:red['rank']]; piv=red['pivots'];d=len(rows)
    need(d==len(kernel),name+'_independent_kernel')
    S=transpose(rows+[[P*x for x in row] for row in I])
    # J consists of actual S columns, in coordinate-pivot order.
    chosen=[piv.index(k) if k in piv else d+k for k in range(N)]
    J=[[S[i][j] for j in chosen] for i in range(N)]
    need(all(J[i][i]>0 and all(J[i][j]==0 for j in range(i+1,N)) for i in range(N)),name+'_lower_triangular')
    def solve(v,integral=False):
        out=[]
        for i in range(N):
            z=F(v[i])-sum(J[i][j]*out[j] for j in range(i))
            z/=J[i][i]
            if integral:need(z.denominator==1,name+'_integral_preimage')
            out.append(int(z) if integral else z)
        return out
    inverse=transpose([solve(row) for row in I])
    C=[[int(i==chosen[j]) for j in range(N)] for i in range(N+d)]
    D=transpose([solve(col,True) for col in transpose(S)])
    need(mm(S,C)==J and mm(J,D)==S,name+'_two_sided_integral_generation')
    need(mm(J,inverse)==I and mm(inverse,J)==I,name+'_both_inverse_identities')
    save(name+'.json',{'kernel_reduction':red,'S':S,'basis':J,'C':C,'D':D,
                     'inverse':strings(inverse),'selected_columns':chosen,'rank':48})
    return J,inverse,solve


def main():
    before=inventory();save('input-hashes.json',before)
    b=json.loads((OLD/'basis.json').read_text())
    original=json.loads((ROOT/'scripts/seven-torsion/certificate.json').read_text())
    nb=json.loads((PREV/'basis.json').read_text())
    H=b['H'];bp=b['basis_to_power'];bases=b['basis']
    need(H==original['primitive_integer_factors'][0] and H[-1]==343 and len(H)==49
         and [F(x,343) for x in H]==list(map(F,original['h'])) and reduce(math.gcd,H)==1,'original_H')
    M=rational(nb['M']);C=nb['inverse'];Q=nb['numerator']
    need(mm(M,C)==I and mm(C,M)==I and [[31*x for x in r] for r in M]==Q,'changed_basis_inverse_both')
    to=rational(b['basis_to_L067']);fr=rational(b['L067_to_basis'])
    need(mm(rational(original['matrix']),bp)==to and mm(rational(b['power_to_basis']),rational(original['inverse']))==fr,'original_transports')
    nto=rational(nb['to_L067']);nfr=rational(nb['from_L067'])
    need(mm(to,M)==nto and mm(C,fr)==nfr and mm(nto,nfr)==I and mm(nfr,nto)==I,'full_changed_transports')
    identity=nb['identity_coordinates']
    need(identity==[C[i][0] for i in range(N)] and mm(M,transpose([identity]))==transpose([I[0]]),'actual_identity')
    polys=transpose(mm(bp,Q))
    save('input-basis.json',{'H':H,'M':strings(M),'inverse':C,'scaled_polynomials':polys,
        'to_L067':strings(nto),'from_L067':strings(nfr),'identity':identity,'scale':31})
    def remainder(poly):
        p=list(poly)
        for k in range(len(p)-1,47,-1):
            q,r=divmod(p[k],343);need(r==0,'exact_H_reduction')
            if q:
                for j,z in enumerate(H):p[k-48+j]-=q*z
        return p[:48]
    def polyprod(a,b):
        p=[0]*95
        for i,x in enumerate(a):
            if x:
                for j,y in enumerate(b):
                    if y:p[i+j]+=x*y
        return p
    def oldcoordinates(p):
        p=remainder(p);out=[0]*N
        for k in range(47,0,-1):
            q,r=divmod(p[k],343);need(r==0,'original_coordinates_integral');out[k]=q
            if q:
                for j in range(k+1):p[j]-=q*bases[k][j]
        out[0]=p[0];return out
    table=[];REPORT['phase']='complete_changed_order_table'
    for i in range(N):
        row=json.loads((PREV/('product-%02d.json'%i)).read_text())
        need(len(row)==48 and all(len(v)==48 and all(type(x) is int for x in v) for v in row),'table_shape')
        for j,v in enumerate(row):
            old=oldcoordinates(polyprod(polys[i],polys[j]));actual=[]
            for r in C:
                q,rem=divmod(sum(x*y for x,y in zip(r,old) if x and y),961)
                need(rem==0,'changed_product_integrality');actual.append(q)
            need(actual==v,'all_changed_product_coefficients');REPORT['input_product_slots']+=48
        table.append(row)
    need([sum(identity[i]*table[i][j][k] for i in range(N)) for j in range(N) for k in range(N)]==[x for r in I for x in r],'left_identity')
    need([sum(identity[j]*table[i][j][k] for j in range(N)) for i in range(N) for k in range(N)]==[x for r in I for x in r],'right_identity')
    REPORT['phase']='frobenius'
    tmod=(np.array(table,dtype=object)%P).astype(np.int64)
    def mulmod(a,b):
        # Reduced operands: 48^2*(2-1)^3=2304 < 2^63.
        return np.einsum('i,j,ijk->k',a,b,tmod,optimize=False)%P
    def power(v,e):
        a=np.array([x%P for x in identity],dtype=np.int64);v=np.array(v,dtype=np.int64)
        while e:
            if e&1:a=mulmod(a,v)
            e//=2
            if e:v=mulmod(v,v)
        return a.tolist()
    first=transpose([power(v,P) for v in I])
    iterates=[first]
    for step in range(1,6):
        iterates.append([[x%P for x in r] for r in mm(first,iterates[-1])])
    fc=eliminate(iterates[-1])
    save('frobenius.json',{'iterates':iterates,'elimination':fc,'iterate':6,'dimension':48,'exponent':64,'prime':P})
    REPORT.update(frobenius_rank=fc['rank'],radical_dimension=len(fc['kernel']),frobenius_iterates=6,frobenius_slots=13824,required_frobenius_slots=13824,exponent=64,prime=P)
    J,Jinv,solve=lattice(fc['kernel'],'radical-lattice')
    REPORT['phase']='full_integral_action';actions=[]
    for i in range(N):
        W=mm(transpose(table[i]),J)
        A=transpose([solve(v,True) for v in transpose(W)])
        need(mm(J,A)==W,'action_exact_basis_change')
        save('action-%02d.json'%i,A);actions.append(A);REPORT['action_slots']+=N*N
    stacked=[[actions[i][k][j]%P for i in range(N)] for j in range(N) for k in range(N)]
    ac=eliminate(stacked);save('action-kernel.json',ac)
    REPORT.update(action_rank=ac['rank'],action_kernel_dimension=len(ac['kernel']))
    Q,Qinv,_=lattice(ac['kernel'],'numerator-lattice')
    multiplier=[[F(x,P) for x in r] for r in Q]
    T=[[x*P for x in r] for r in Qinv]
    need(all(x.denominator==1 for r in T for x in r),'integral_old_inclusion')
    T=[[int(x) for x in r] for r in T]
    need(mm(multiplier,T)==I and mm(T,multiplier)==I,'multiplier_inverse_both')
    need(all(T[i][j]==0 for i in range(N) for j in range(i+1,N)),'full_triangular_determinant_input')
    det=math.prod(T[i][i] for i in range(N));index=abs(det)
    need(index==P**len(ac['kernel']),'index_matches_full_kernel')
    if index==1:
        need(all(x%P==0 for r in Q for x in r),'N_contained_in_2R')
        equality=[[x//P for x in r] for r in Q]
        need(mm(Q,T)==[[P*x for x in r] for r in I] and mm([[P*x for x in r] for r in I],equality)==Q,'both_equality_containments')
        witness=None;decision='2_MAXIMAL'
    else:
        col=next(j for j in range(N) if any(Q[i][j]%P for i in range(N)))
        w=[Q[i][col] for i in range(N)]
        W=[[sum(w[i]*actions[i][k][j] for i in range(N)) for j in range(N)] for k in range(N)]
        need(all(x%P==0 for r in W for x in r),'strict_witness_preserves_full_radical')
        witness={'numerator':w,'column':col,'radical_action':[[x//P for x in r] for r in W]}
        equality=None;decision='NOT_2_MAXIMAL'
    save('decision.json',{'decision':decision,'numerator':Q,'M':strings(multiplier),'inverse':T,
        'determinant_diagonal':[T[i][i] for i in range(N)],'determinant':det,'index':index,
        'kernel_dimension':len(ac['kernel']),'equality_forward':equality,'equality_reverse':T,
        'strict_witness':witness,'identity_in_multiplier':[sum(T[i][j]*identity[j] for j in range(N)) for i in range(N)]})
    need(inventory()==before,'all_inputs_preserved')
    save('preservation-producer.json',{'before':before,'after':inventory(),'equal':True})
    REPORT.update(status='PASS',phase='complete',decision=decision,index=index,original_files=len(before))

try:main()
except Exception as e:REPORT.update(status='STOP',failure=type(e).__name__+': '+str(e),failures=[type(e).__name__+': '+str(e)])
finally:
    REPORT.update(seconds=time.monotonic()-START,required_input_product_slots=110592,required_action_slots=110592)
    save('producer-report.json',REPORT);print(json.dumps(REPORT))
sys.exit(0 if REPORT['status']=='PASS' else 1)
