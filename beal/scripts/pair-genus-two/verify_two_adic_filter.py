"""Independent replay in the audited integral basis; no producer imports."""
from fractions import Fraction
from pathlib import Path
from itertools import product
import json
import hashlib
import traceback

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'two-adic-filter-verification.json'
R=dict(completed=False,failures=[],checks=0,bindings={},max_rational_bits=0,
       rational_bits_cap=8192)

class Q(Fraction):
    def __new__(cls,*args):
        x=super().__new__(cls,*args)
        n=max(abs(x.numerator).bit_length(),x.denominator.bit_length())
        R['max_rational_bits']=max(R['max_rational_bits'],n)
        assert n<=8192,'rational arithmetic bit cap'
        return x

def checked_operator(name):
    def operation(self,*args):
        result=getattr(Fraction,name)(self,*args)
        return Q(result) if isinstance(result,Fraction) else result
    return operation

for _name in ('__add__','__radd__','__sub__','__rsub__','__mul__','__rmul__',
              '__truediv__','__rtruediv__','__pow__','__neg__','__pos__','__abs__','__mod__'):
    setattr(Q,_name,checked_operator(_name))

def ck(b,label):
    R['checks']+=1
    assert b,label

def obs(a):
    if isinstance(a,(list,tuple)):
        for x in a:obs(x)
    else:
        a=Q(a);n=max(abs(a.numerator).bit_length(),a.denominator.bit_length())
        R['max_rational_bits']=max(R['max_rational_bits'],n)
        assert n<=8192,'bit cap'
    return a

def read(name):
    raw=(ROOT/name).read_bytes();R['bindings'][name]=hashlib.sha256(raw).hexdigest()
    return json.loads(raw)

def vec(a):return list(map(Q,a))
ONE=vec([1,0,0,0])
def mv(m,a):return obs([sum(Q(x)*y for x,y in zip(row,a)) for row in m])
def times(a,b):
    z=[Q(0)]*4
    for k in range(4):
        for i in range(4):
            for j in range(4):z[k]+=a[i]*b[j]*T[i][j][k]
    return obs(z)
def plus(a,b):return obs([x+y for x,y in zip(a,b)])
def scale(a,n):return obs([x*n for x in a])
def powr(a,n):
    r=ONE[:]
    for _ in range(n):r=times(r,a)
    return r
def v2(x):
    x=Q(x);assert x
    return ((abs(x.numerator)&-abs(x.numerator)).bit_length()-1)-((x.denominator&-x.denominator).bit_length()-1)
def residue(x,m):
    x=Q(x);return x.numerator*pow(x.denominator,-1,m)%m
def integral(a):return all(not x or v2(x)>=0 for x in a)
def res(a):
    ck(integral(a),'integral input to residue')
    return sum(residue(x,2) for x in a)%2
def digits(a):
    a=a[:];z=0
    for k in range(9):
        t=res(a);z+=t*2**k;a[0]-=t;a=times(a,PIINV)
    return z
def normalized(a):
    # Integral-basis coefficients, rather than a weighted pi term minimum.
    k=min(v2(x) for x in a if x)
    z=scale(a,Q(2)**(-k));j=0
    while res(z)==0:
        z=times(z,PIINV);j+=1;ck(j<=64,'valuation division cap')
    n=4*k+j
    u=times(a,powr(PIINV if n>=0 else PI,abs(n)))
    ck(res(u)==1,'normalized unit')
    return n,u,digits(u)
def qclass(x):
    n=v2(x);u=Q(x)/Q(2)**n;r=residue(u,8)
    return n%2+{1:0,3:6,5:4,7:2}[r]
def fclass(a):
    n,u,d=normalized(a)
    return n%2+2*UM[d]
def paircheck(record,q,b):
    qr,fr=record['rational'],record['quartic']
    ck(Q(qr['value'])==q,'rational evaluation')
    ck(vec(fr['coefficients'])==mv(OI,b),'complete pi evaluation coordinates')
    n,u,d=normalized(b)
    ck(fr['valuation']==n,'valuation independent division')
    ck(mv(PO,vec(fr['normalized']))==u,'complete normalized coordinates')
    ck(fr['unit_mod_pi9']==d,'independent nine digits')
    ck(qclass(q)==qr['mask'],'rational square class')
    ck(fclass(b)==fr['mask'],'quartic square class')
    m=qclass(q)+8*fclass(b)
    ck(m==record['mask'],'full pair mask')
    return m
def norm(a):
    m=[[times(a,[Q(int(k==j)) for k in range(4)])[i] for j in range(4)] for i in range(4)]
    det=Q(1)
    for i in range(4):
        j=next(j for j in range(i,4) if m[j][i])
        if i!=j:m[i],m[j]=m[j],m[i];det=-det
        t=m[i][i];det*=t;obs(det)
        for j in range(i+1,4):
            c=m[j][i]/t
            m[j]=[x-c*y for x,y in zip(m[j],m[i])];obs(m[j])
    return det
def rank(rows):
    piv={}
    for x in rows:
        z=x
        while z:
            p=(z&-z).bit_length()-1
            if p not in piv:piv[p]=z;break
            z^=piv[p]
    return len(piv)
def xorcombo(rows,c):
    z=0
    for j,x in enumerate(rows):
        if (c>>j)&1:z^=x
    return z
def tracecheck(e,cols):
    ck(rank(cols)==e['rank'],'independent rank')
    for row,x in zip(e['trace'],cols):
        ck(row['input']==x,'trace original')
        ck(xorcombo(cols,row['coefficients'])==row['reduced'],'full combination identity')
    ks=e['kernel'];ck(len(ks)==len(cols)-rank(cols) and rank(ks)==len(ks),'full independent kernel')
    ck(all(xorcombo(cols,c)==0 for c in ks),'every kernel identity')
    for p,(z,c) in e['pivots'].items():
        ck(xorcombo(cols,c)==z and z.bit_length()-1==int(p),'pivot identity')
def reduce(x,piv):
    for p,(v,c) in sorted(((int(k),v) for k,v in piv.items()),reverse=True):
        if x&(1<<p):x^=v
    return x
def ev(p,x):
    return obs(sum(Q(c)*x**i for i,c in enumerate(p)))

def main():
    global T,PI,PIINV,PO,OI,UM
    C=read('two-adic-filter-certificate.json')
    ck(C['completed'] and not C['failures'],'producer completion')
    inputs={n:read(n) for n in C['bindings']}
    ck(all(R['bindings'][n]==h for n,h in C['bindings'].items()),'all source bindings')
    base=inputs['quartic-class-certificate.json'];model=inputs['odd-model-support-certificate.json']
    real=inputs['real-kummer-certificate.json'];eleven=inputs['eleven-adic-filter-certificate.json']
    T=base['order']['table'];F=C['field'];PO=[[Q(x) for x in row] for row in F['pi_to_O']]
    OI=[[Q(x) for x in row] for row in F['O_to_pi']]
    PI=vec([1,0,1,0]);ck(F['pi_O']==[1,0,1,0],'fixed pi')
    for j in range(4):
        ck(mv(PO,[Q(int(i==j)) for i in range(4)])==powr(PI,j),'every pi basis column')
        ck(mv(OI,mv(PO,[Q(int(i==j)) for i in range(4)]))==[int(i==j) for i in range(4)],'basis inverses')
    E=vec(F['pi_polynomial'])
    ck(E==vec([5850,-8442,1272,-64,1]),'printed uniformizer polynomial')
    ck(all(c%2==0 for c in E[:4]) and v2(E[0])==1,'Eisenstein coefficients')
    ck([sum(E[j]*powr(PI,j)[i] for j in range(5)) for i in range(4)]==[0]*4,'polynomial annihilation')
    PIINV=mv(PO,[-E[j+1]/E[0] for j in range(4)])
    ck(times(PI,PIINV)==ONE,'inverse pi in integral basis')
    # Full order is locally Z_2[pi]: both basis maps have odd denominators.
    ck(all(integral(row) for row in PO+OI),'both local lattices integral')
    B=[[Q(x) for x in row] for row in model['field']['O_basis_in_alpha']]
    AtoPI=[[Q(x) for x in row] for row in F['alpha_to_pi']]
    for j in range(4):
        o=mv(PO,[Q(int(i==j)) for i in range(4)])
        ck(mv(AtoPI,mv(B,o))==[int(i==j) for i in range(4)],'alpha pi transport')
    eta=mv(PO,vec(F['eta_pi']));alpha=vec([0,1,0,0])
    ck(times(eta,plus(alpha,[-50,0,0,0]))==[-907500,0,0,0],'actual eta map')
    ck(sum(residue(x,2) for x in PI)%2==0,'pi lies in actual prime')
    ck(F['prime']==base['generators'][26],'actual dyadic prime identity')
    for col in F['prime']['lattice']['columns']:ck(res(vec(col))==0,'prime reduction')
    S=C['square_table'];reps=[]
    pi_powers=[powr(PI,j) for j in range(9)]
    for a in range(512):
        z=[sum(((a>>j)&1)*pi_powers[j][i] for j in range(9)) for i in range(4)]
        ck(mv(PO,vec(S['representatives'][a]))==z,'entire residue representative')
        ck(digits(z)==a,'entire residue enumeration');reps.append(z)
    sq={}
    ck([row[0] for row in S['square_rows']]==list(range(1,512,2)),'complete unit-root domain')
    for a,b in S['square_rows']:
        ck(digits(times(reps[a],reps[a]))==b,'independent unit square');sq[b]=a
    ck(len(sq)==8,'square subgroup size')
    UM={int(k):v for k,v in S['unit_masks'].items()};gens=S['unit_generators']
    ck(gens==[3,5,7,9,11] and set(UM)==set(range(1,512,2)),'whole unit quotient domain')
    independent={}
    for bits in product((0,1),repeat=5):
        g=ONE[:];mask=0
        for j,b in enumerate(bits):
            if b:g=times(g,reps[gens[j]]);mask+=1<<j
        for s in sq:
            a=digits(times(g,reps[s]))
            ck(a not in independent,'cosets disjoint')
            independent[a]=mask
    ck(independent==UM,'all independent unit coordinates')
    G=model['model']['G'];r=Q(9075);H=model['model']['H'];h=ev(H,r)
    b=plus([r,0,0,0],scale(eta,-1));ck(norm(b)==h,'branch norm')
    paircheck(C['generators'][0]['evaluation'],h,b)
    # Authenticate every point included by the producer, with exact G value.
    for s in C['samples']:
        x=Q(s['X']);y2=ev(G,x)
        ck(y2==Q(s['Y_squared']) and qclass(y2)==0,'Q2 point existence')
        paircheck(s['evaluation'],x-r,plus([x,0,0,0],scale(eta,-1)))
    ck(len(C['quadratic_fields'])==1 and C['quadratic_fields'][0]['polynomial']==['-1','-1',1],
       'only unramified field needed')
    def qt(a,b):return obs([a[0]*b[0]+a[1]*b[1],a[0]*b[1]+a[1]*b[0]+a[1]*b[1]])
    for s in C['quadratic_samples']:
        x=vec(s['X']);z=[Q(0),Q(0)]
        # Summation of powers rather than producer Horner evaluation.
        xx=[Q(1),Q(0)]
        for c in G:
            z=[z[i]+Q(c)*xx[i] for i in range(2)];xx=qt(xx,x)
        ck(z==vec(s['Y_squared']),'full quadratic evaluation')
        sc=s['square_certificate'];v=sc['valuation'];u=[q/Q(2)**v for q in z]
        ck(v==min(v2(q) for q in z if q) and v%2==0,'quadratic even valuation')
        ck(u==vec(sc['normalized']),'quadratic unit normalization')
        root=vec(sc['unit_root']);err=[u[i]-qt(root,root)[i] for i in range(2)]
        ck(min(v2(q) for q in root if q)==0,'quadratic unit root')
        ck(err==vec(sc['error']) and min(v2(q) for q in err if q)>=3,'Hensel square certificate')
        a,b=x
        zz=plus([a,0,0,0],scale(eta,-1))
        nb=plus(plus(times(zz,zz),scale(zz,b)),[-b*b,0,0,0])
        nq=(a-r)**2+b*(a-r)-b*b
        paircheck(s['evaluation'],nq,nb)
        # Full algebra norm is square, as required for a traced point.
        ck(qclass(nq*norm(nb))==0,'trace product norm')
    cols=[g['evaluation']['mask'] for g in C['generators']]
    for g in C['generators'][1:]:
        source=C['samples'][g['sample']] if g['type']=='local_point' else C['quadratic_samples'][g['sample']]
        ck(g['evaluation']==source['evaluation'],'generator full source')
    tracecheck(C['image'],cols);ck(rank(cols)==3 and F['required_image_dimension']==3,'dimension saturation')
    ip=C['image']['pivots'];realcols=[30,24];elevenp={'2':[5,1]};realp={'4':[30,1],'2':[6,3]}
    oldcols=[];dycols=[]
    for j,w in enumerate(C['witnesses']):
        src=real['witnesses'][j];ck(w['source']==src==eleven['witnesses'][j]['source'],'full fixed witness binding')
        b=vec(src['coefficients']);q=Q(src['inverse_norm'])
        ck(q*norm(b)==1,'signed inverse norm')
        mask=paircheck(w['local'],q,b);dycols.append(mask)
        rm=src['mask'];em=eleven['witnesses'][j]['pair']['mask']
        ck(w['real_mask']==rm and w['eleven_mask']==em,'old complete masks')
        old=reduce(rm,realp)|(reduce(em,elevenp)<<5)
        ck(old==w['old_quotient'],'joint old quotient');oldcols.append(old)
        ck(w['dyadic_quotient']==reduce(mask,ip),'dyadic quotient')
    tracecheck(C['old_conditions'],oldcols);ck(C['old_conditions']['rank']==3,'old quotient rank three')
    qs=[]
    ck([p['coefficients'] for p in C['kernel_products']]==C['old_conditions']['kernel'],'all 36 kernel products')
    for p in C['kernel_products']:
        c=p['coefficients'];b=ONE[:];q=Q(1);rm=em=0
        for j,src in enumerate(real['witnesses']):
            if (c>>j)&1:
                b=times(b,vec(src['coefficients']));q*=Q(src['inverse_norm']);obs(q)
                rm^=src['mask'];em^=eleven['witnesses'][j]['pair']['mask']
        ck(q*norm(b)==1,'kernel full signed norm')
        mask=paircheck(p['pair'],q,b)
        ck(mask==xorcombo(dycols,c),'localization multiplicative')
        ck(rm==p['real_mask'] and em==p['eleven_mask'],'old product masks')
        ck(reduce(rm,realp)==reduce(em,elevenp)==0,'both old memberships')
        z=reduce(mask,ip);ck(z==p['quotient'],'kernel quotient');qs.append(z)
    tracecheck(C['additional_conditions'],qs);ck(rank(qs)==2,'two independent new conditions')
    R.update(completed=True,image_rank=3,required_image_rank=3,old_rank=3,
             old_kernel_dimension=36,additional_rank=2,
             sufficient_rank_bound=1,derived_rank_bound='5+c <= 7',
             residue_elements_actual=512,residue_elements_cap=2**20,
             fixed_columns_actual=39,fixed_columns_cap=39)

if __name__=='__main__':
    try:main()
    except Exception as e:R['failures'].append(dict(type=type(e).__name__,message=str(e),traceback=traceback.format_exc()))
    OUT.write_text(json.dumps(R,indent=2,default=str)+'\n')
    print(json.dumps(dict(completed=R['completed'],checks=R['checks'],failures=[x['message'] for x in R['failures']],
                         image_actual=R.get('image_rank'),image_required=3,additional_actual=R.get('additional_rank'),
                         bits_actual=R['max_rational_bits'],bits_cap=8192,path=str(OUT))))
    raise SystemExit(0 if R['completed'] else 1)
