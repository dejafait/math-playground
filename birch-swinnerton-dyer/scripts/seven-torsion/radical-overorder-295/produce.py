"""One bounded full-radical/full-action construction; original inputs read-only."""
from pathlib import Path
from fractions import Fraction as F
from functools import reduce
import hashlib, json, math, signal, sys, time
import numpy as np

sys.set_int_max_str_digits(0)
OUT=Path(__file__).resolve().parent
ROOT=OUT.parents[2]
OLD=ROOT/'scripts/seven-torsion/nonmonic-order-283'
START=time.monotonic(); N=48; P=31; CAP=134217728
REPORT={'status':'INCOMPLETE','phase':'inputs','old_product_slots':0,
        'action_slots':0,'new_product_slots':0,'failures':[]}
I=[[int(i==j) for j in range(N)] for i in range(N)]

def need(ok,label):
    if not ok: raise ArithmeticError(label)

def save(name,x):
    raw=(json.dumps(x,separators=(',',':'))+'\n').encode()
    need(sum(p.stat().st_size for p in OUT.iterdir() if p.is_file())+len(raw)+65536<=CAP,'byte_cap')
    with (OUT/name).open('xb') as f:f.write(raw)

def inventory():
    paths=[ROOT/'scripts/seven-torsion/certificate.json']
    for d in (OLD,ROOT/'scripts/residual-prime-289'):
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
    old=json.loads((ROOT/'scripts/seven-torsion/certificate.json').read_text())
    H=b['H'];bases=b['basis'];bp=b['basis_to_power']
    need(len(H)==49 and H[-1]==343 and H==old['primitive_integer_factors'][0]
         and [F(x,343) for x in H]==list(map(F,old['h'])) and reduce(math.gcd,H)==1,'original_H')
    need(b['source_sha256']==before['scripts/seven-torsion/certificate.json'],'original_L067_hash')
    need(bases==[[1]+[0]*47]+[[H[48-i+k] if k<=i else 0 for k in range(N)] for i in range(1,N)],'original_basis')
    need(bp==transpose(bases),'original_power_transport')
    pb=rational(b['power_to_basis']);to=rational(b['basis_to_L067']);fr=rational(b['L067_to_basis'])
    need(mm(bp,pb)==I and mm(pb,bp)==I and mm(to,fr)==I and mm(fr,to)==I,'old_inverse_both')
    need(mm(rational(old['matrix']),bp)==to and mm(pb,rational(old['inverse']))==fr,'old_full_L067_transports')
    ded=json.loads((ROOT/'scripts/residual-prime-289/dedekind.json').read_text())
    need(ded['G']==[24,0,1],'original_gcd')
    U=[0]*47;w=[x%P for x in H]
    for k in range(48,1,-1):
        q=w[k];U[k-2]=q;w[k]=0;w[k-2]=(w[k-2]-24*q)%P
    need(not any(w) and U[-1]==2,'degree46_U_source_convention')
    save('source.json',{'H':H,'prime':P,'G':[24,0,1],'U':U,'degree_U':46,
        'source_identification':'Stevenhagen section 9 and Del Corso--Dvornicich--Simon Theorem 2(ii); no B power is computed'})

    def remainder(poly):
        p=list(poly)+[0]*max(0,95-len(poly))
        for k in range(len(p)-1,47,-1):
            q,r=divmod(p[k],343);need(r==0,'exact_original_H_division')
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
    def coordinates(p):
        p=remainder(p);out=[0]*N
        for k in range(47,0,-1):
            q,r=divmod(p[k],343);need(r==0,'old_order_coordinates_integral');out[k]=q
            if q:
                for j in range(k+1):p[j]-=q*bases[k][j]
        out[0]=p[0];return out
    table=[];REPORT['phase']='original_product_identities'
    for i in range(N):
        row=json.loads((OLD/('product-%02d.json'%i)).read_text())
        need(len(row)==48 and all(len(v)==48 and all(type(x) is int for x in v) for v in row),'old_product_shape')
        for j,v in enumerate(row):
            need(coordinates(polyprod(bases[i],bases[j]))==v,'every_original_product_slot')
            REPORT['old_product_slots']+=48
        table.append(row)
    need(table[0]==I and all(table[i][0]==I[i] for i in range(N)),'old_identity_both')
    REPORT['phase']='frobenius'
    tmod=np.array(table,dtype=object)%P
    tmod=tmod.astype(np.int64)
    def mulmod(a,b):
        # At most 2304 summands, each <=30^3, strictly below 2^63.
        return np.einsum('i,j,ijk->k',a,b,tmod,optimize=False)%P
    def power(v,e):
        a=np.array(I[0],dtype=np.int64);v=np.array(v,dtype=np.int64)
        while e:
            if e&1:a=mulmod(a,v)
            e//=2
            if e:v=mulmod(v,v)
        return a.tolist()
    first=transpose([power(v,31) for v in I])
    second=[[x%P for x in r] for r in mm(first,first)]
    fc=eliminate(second);save('frobenius.json',{'first':first,'second':second,'elimination':fc,'iterate':2,'dimension':48,'exponent':961})
    REPORT.update(frobenius_rank=fc['rank'],radical_dimension=len(fc['kernel']))
    need(fc['rank']==46 and len(fc['kernel'])==2,'full_radical_rank46_dimension2')
    J,Jinv,solve=lattice(fc['kernel'],'radical-lattice')
    REPORT['phase']='full_integral_action'
    actions=[]
    for i in range(N):
        W=mm(transpose(table[i]),J)
        A=transpose([solve(v,True) for v in transpose(W)])
        need(mm(J,A)==W,'action_exact_basis_change')
        save('action-%02d.json'%i,A);actions.append(A);REPORT['action_slots']+=N*N
    stacked=[[actions[i][k][j]%P for i in range(N)] for j in range(N) for k in range(N)]
    ac=eliminate(stacked);save('action-kernel.json',ac)
    REPORT.update(action_rank=ac['rank'],action_kernel_dimension=len(ac['kernel']))
    need(ac['rank']==46 and len(ac['kernel'])==2,'full_action_rank46_dimension2')
    Q,Qinv,_=lattice(ac['kernel'],'numerator-lattice')
    REPORT['phase']='overorder_basis'
    M=[[F(x,P) for x in row] for row in Q]
    C=[[x*P for x in row] for row in Qinv]
    need(all(x.denominator==1 for row in C for x in row),'integral_old_inclusion')
    C=[[int(x) for x in row] for row in C]
    need(mm(M,C)==I and mm(C,M)==I,'new_basis_both_inverse_identities')
    need(all(C[i][j]==0 for i in range(N) for j in range(i+1,N)),'full_inclusion_lower_triangular')
    determinant=math.prod(C[i][i] for i in range(N))
    need(abs(determinant)==961,'index961')
    nto=mm(to,M);nfr=mm(C,fr)
    need(mm(nto,nfr)==I and mm(nfr,nto)==I,'new_full_L067_transports_inverse_both')
    save('basis.json',{'numerator':Q,'M':strings(M),'inverse':C,'to_L067':strings(nto),
                     'from_L067':strings(nfr),'index':abs(determinant),'inclusion_determinant':determinant,
                     'identity_coordinates':[C[i][0] for i in range(N)],'rank':48})
    REPORT.update(index=abs(determinant),phase='new_products')
    polys=transpose(mm(bp,Q))
    for i in range(N):
        row=[]
        for j in range(N):
            v=coordinates(polyprod(polys[i],polys[j]));new=[]
            for r in C:
                q,rem=divmod(sum(x*y for x,y in zip(r,v) if x and y),961)
                need(rem==0,'all_new_product_coefficients_integral');new.append(q)
            row.append(new);REPORT['new_product_slots']+=48
        save('product-%02d.json'%i,row)
    need(inventory()==before,'original_hashes_preserved')
    save('preservation-producer.json',{'before':before,'after':inventory(),'equal':True})
    REPORT.update(status='PASS',phase='complete',original_files=len(before),rank=48,
        source_identification='full radical and full I/31I action preimage; cited multiplier-order theorem')

def alarm(*args):raise TimeoutError('internal_180_second_cap')
signal.signal(signal.SIGALRM,alarm);signal.setitimer(signal.ITIMER_REAL,180)
try:main()
except Exception as e:REPORT.update(status='STOP',failure=type(e).__name__+': '+str(e),failures=[type(e).__name__+': '+str(e)])
finally:
    signal.setitimer(signal.ITIMER_REAL,0)
    REPORT.update(seconds=time.monotonic()-START,required_seconds=180,required_old_product_slots=110592,
        required_action_slots=110592,required_new_product_slots=110592,required_index=961,byte_limit=CAP)
    save('producer-report.json',REPORT)
    print(json.dumps(REPORT))
sys.exit(0 if REPORT['status']=='PASS' else 1)
