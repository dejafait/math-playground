"""Bounded approved local-image specialization; all exact evidence is saved."""
from fractions import Fraction
from pathlib import Path
from itertools import permutations
from math import prod
import json
import hashlib
import traceback

ROOT = Path(__file__).resolve().parent
OUT = ROOT/'two-adic-filter-certificate.json'
D = dict(completed=False, failures=[], bindings={}, checks=[],
         bounds=dict(rational_bits_cap=8192, max_rational_bits=0,
                     residue_table_cap=2**20, residue_table_actual=512,
                     disk_cap=200000, recursion_disks_processed=0, depth_cap=64,
                     max_recursion_depth=0, sample_cap=200000, samples_tested=0,
                     max_sample_parameter=0, columns_actual=39, columns_cap=39,
                     matrix_cap=39), samples=[], generators=[])

class Q(Fraction):
    """Enforce the bit cap on every exact rational arithmetic result."""
    def __new__(cls,*args):
        x=super().__new__(cls,*args)
        n=max(abs(x.numerator).bit_length(),x.denominator.bit_length())
        D['bounds']['max_rational_bits']=max(D['bounds']['max_rational_bits'],n)
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

def observe(x):
    if isinstance(x, (int,Q)):
        x=Q(x)
        n=max(abs(x.numerator).bit_length(),x.denominator.bit_length())
        D['bounds']['max_rational_bits']=max(D['bounds']['max_rational_bits'],n)
        assert n<=8192, 'rational bit cap'
    elif isinstance(x,(list,tuple)):
        for a in x: observe(a)
    return x

def check(name,x):
    D['checks'].append(dict(name=name,passed=bool(x)))
    assert x,name

def read(name):
    raw=(ROOT/name).read_bytes()
    D['bindings'][name]=hashlib.sha256(raw).hexdigest()
    return json.loads(raw)

def matvec(m,a):
    return observe([sum(Q(x)*y for x,y in zip(row,a)) for row in m])

def invmat(m):
    a=[[Q(x) for x in row]+[Q(int(i==j)) for j in range(4)] for i,row in enumerate(m)]
    for i in range(4):
        k=next(k for k in range(i,4) if a[k][i])
        a[i],a[k]=a[k],a[i]
        a[i]=[x/a[i][i] for x in a[i]]
        for j in range(4):
            if j!=i:
                t=a[j][i]; a[j]=[x-t*y for x,y in zip(a[j],a[i])]
        observe(a)
    return [r[4:] for r in a]

def determinant(m):
    return observe(sum((-1)**sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))*
                       prod(m[i][p[i]] for i in range(4)) for p in permutations(range(4))))

def ordermul(a,b):
    return observe([sum(a[i]*b[j]*TABLE[i][j][k] for i in range(4) for j in range(4)) for k in range(4)])

def add(a,b): return observe([x+y for x,y in zip(a,b)])
def scale(a,c): return observe([x*c for x in a])
def mul(a,b):
    z=[Q(0)]*7
    for i in range(4):
        for j in range(4): z[i+j]+=a[i]*b[j]
    for j in range(6,3,-1):
        for i in range(4): z[j-4+i]-=z[j]*E[i]
    return observe(z[:4])

ONE=[Q(1),Q(0),Q(0),Q(0)]
PI=[Q(0),Q(1),Q(0),Q(0)]
def power(a,n):
    r=ONE[:]
    while n:
        if n%2:r=mul(r,a)
        a=mul(a,a);n//=2
    return r

def norm(a):
    return determinant([[mul(a,[Q(int(k==j)) for k in range(4)])[i] for j in range(4)] for i in range(4)])

def v2(x):
    x=Q(x);assert x
    n,d=x.numerator,x.denominator;v=0
    while n%2==0:n//=2;v+=1
    while d%2==0:d//=2;v-=1
    return v

def rational_class(x):
    x=Q(x);v=v2(x);u=x/Q(2)**v
    residue=u.numerator*pow(u.denominator,-1,8)%8
    return dict(value=x,valuation=v,unit_mod8=residue,
                mask=(v%2)+{1:0,7:2,5:4,3:6}[residue])

def reduce_pi(a):
    """Nine uniformizer digits, valid for coefficients integral over Z_2."""
    a=list(map(Q,a));r=0
    for i in range(9):
        assert all(x==0 or v2(x)>=0 for x in a),'nonintegral digit input'
        digit=a[0].numerator%2
        r|=digit<<i
        a[0]-=digit
        a=mul(a,PIINV)
    return r

def from_digits(a):
    z=[Q(0)]*4
    for i in reversed(range(9)):
        z=mul(z,PI);z[0]+=(a>>i)&1
    return z

def ringmul(a,b): return reduce_pi(mul(REPS[a],REPS[b]))

def field_class(a):
    vals=[None if not c else 4*v2(c)+i for i,c in enumerate(a)]
    v=min(x for x in vals if x is not None)
    normalized=mul(a,power(PIINV if v>=0 else PI,abs(v)))
    residue=reduce_pi(normalized)
    assert residue%2
    return dict(coefficients=a,term_valuations=vals,valuation=v,
                normalized=normalized,unit_mod_pi9=residue,
                mask=(v%2)+(UNITMASK[residue]<<1))

def pair(q,b):
    r,f=rational_class(q),field_class(b)
    return dict(rational=r,quartic=f,mask=r['mask']+(f['mask']<<3))

def elim(columns):
    pivots={};kernel=[];trace=[]
    for j,x in enumerate(columns):
        z=x;c=1<<j;used=[]
        while z:
            p=z.bit_length()-1
            if p not in pivots:pivots[p]=(z,c);break
            z^=pivots[p][0];c^=pivots[p][1];used.append(p)
        if not z:kernel.append(c)
        trace.append(dict(input=x,reduced=z,coefficients=c,used=used))
    return dict(rank=len(pivots),pivots={str(k):list(v) for k,v in pivots.items()},kernel=kernel,trace=trace)

def reduce_mask(x,pivots):
    for k,(v,c) in sorted(((int(k),v) for k,v in pivots.items()),reverse=True):
        if (x>>k)&1:x^=v
    return x

def evaluate(p,x):
    z=0
    for c in reversed(p):z=observe(z*x+Q(c))
    return z

class Quadratic:
    """Explicit integral quadratic order, with authenticated local square test."""
    def __init__(self,name,c0,c1,unram=False):
        self.name,self.c0,self.c1,self.unram=name,Q(c0),Q(c1),unram
        self.pi=[Q(2),Q(0)] if unram else [Q(0),Q(1)]
        self.piinv=[Q(1,2),Q(0)] if unram else [-self.c1/self.c0,-1/self.c0]
        self.e=1 if unram else 2
        self.precision=2*self.e+1
        if unram:
            self.reps=[[Q(a),Q(b)] for a in range(8) for b in range(8)]
        else:
            self.reps=[]
            for n in range(32):
                a=[Q(0),Q(0)]
                for i in reversed(range(5)):
                    a=self.mul(a,self.pi);a[0]+=(n>>i)&1
                self.reps.append(a)
        self.squares={}
        self.square_rows=[]
        for a in self.reps:
            if self.val(a)!=0:continue
            b=self.reduce(self.mul(a,a))
            self.squares.setdefault(b,a)
            self.square_rows.append(dict(root=a,square=b))
        self.record=dict(name=name,polynomial=[self.c0,self.c1,1],unramified=unram,
                         ramification=self.e,residue_degree=2 if unram else 1,
                         precision=self.precision,representatives=self.reps,
                         square_rows=self.square_rows)

    def mul(self,a,b):
        return observe([a[0]*b[0]-self.c0*a[1]*b[1],
                        a[0]*b[1]+a[1]*b[0]-self.c1*a[1]*b[1]])

    def val(self,a):
        z=[self.e*v2(c)+(0 if self.unram else i) for i,c in enumerate(a) if c]
        return min(z) if z else None

    def reduce(self,a):
        if self.unram:
            assert all(not c or v2(c)>=0 for c in a)
            return tuple(c.numerator*pow(c.denominator,-1,8)%8 for c in a)
        a=a[:];r=0
        for i in range(5):
            assert all(not c or v2(c)>=0 for c in a)
            b=a[0].numerator%2;r|=b<<i;a[0]-=b;a=self.mul(a,self.piinv)
        return r

    def square(self,a):
        v=self.val(a)
        if v is None:return dict(square=True,zero=True)
        if v%2:return dict(square=False,valuation=v)
        u=a[:]
        for _ in range(abs(v)):u=self.mul(u,self.piinv if v>=0 else self.pi)
        residue=self.reduce(u)
        root=self.squares.get(residue)
        if root is None:return dict(square=False,valuation=v,residue=residue)
        delta=[x-y for x,y in zip(u,self.mul(root,root))]
        vd=self.val(delta)
        assert vd is None or vd>=self.precision
        return dict(square=True,valuation=v,normalized=u,residue=residue,
                    unit_root=root,error=delta,error_valuation=vd,
                    required_error_valuation=self.precision)

    def ev(self,p,x):
        z=[Q(0),Q(0)]
        for c in reversed(p):
            z=self.mul(z,x);z[0]+=c;observe(z)
        return z

def trace_evaluation(a,b,field,r,eta):
    z=add([a,0,0,0],scale(eta,-1))
    n=add(add(mul(z,z),scale(z,-field.c1*b)),[field.c0*b*b,0,0,0])
    q=(a-r)**2-field.c1*b*(a-r)+field.c0*b*b
    return pair(q,n)

def main():
    global TABLE,E,PIINV,REPS,UNITMASK
    real=read('real-kummer-certificate.json');eleven=read('eleven-adic-filter-certificate.json')
    model=read('odd-model-support-certificate.json');base=read('quartic-class-certificate.json')
    for name in ('real-kummer','eleven-adic-filter'):
        a=read(name+'-audit.json')
        check(name+' audit',a['completed'] and not a['failures'] and
              a['bindings'][name+'-certificate.json']==D['bindings'][name+'-certificate.json'])
    check('old certificates',real['completed'] and eleven['completed'] and not real['failures'] and not eleven['failures'])
    check('input bindings',all(D['bindings'][n]==h for n,h in real['bindings'].items() if n in D['bindings']) and
          eleven['bindings']['real-kummer-certificate.json']==D['bindings']['real-kummer-certificate.json'])
    check('39 fixed columns',len(real['witnesses'])==39)
    TABLE=base['order']['table']
    basis=[[Q(x) for x in row] for row in base['order']['basis']]
    check('actual integral basis',basis==[[Q(x) for x in row] for row in model['field']['O_basis_in_alpha']])
    pi=[1,0,1,0];cols=[ONE]
    for i in range(1,5):cols.append(ordermul(cols[-1],pi))
    change=[[cols[j][i] for j in range(4)] for i in range(4)]
    inverse=invmat(change)
    E=scale(matvec(inverse,cols[4]),-1)+[Q(1)]
    check('uniformizer Eisenstein polynomial',all(c.denominator==1 and c%2==0 for c in E[:4]) and v2(E[0])==1)
    check('pi basis determinant odd',v2(determinant(change))==0)
    PIINV=[-E[i+1]/E[0] for i in range(4)]
    check('pi inverse',mul(PI,PIINV)==ONE)
    # Both source bases are fully specified; invert alpha-coordinate order matrix.
    basis_inverse=invmat(basis)
    power_to_pi=observe([[sum(inverse[i][k]*basis_inverse[k][j] for k in range(4)) for j in range(4)] for i in range(4)])
    eta=matvec(power_to_pi,list(map(Q,model['field']['eta_in_alpha'])))
    alpha=matvec(power_to_pi,[0,1,0,0])
    check('eta transport',mul(eta,add(alpha,[-50,0,0,0]))==[-907500,0,0,0])
    check('H eta',all(x==0 for x in __import__('functools').reduce(lambda z,c:add(mul(z,eta),[Q(c),0,0,0]),reversed(model['model']['H']),[Q(0)]*4)))
    D['field']=dict(pi_O=pi,pi_polynomial=E,pi_to_O=change,O_to_pi=inverse,
                    alpha_to_pi=power_to_pi,eta_pi=eta,alpha_pi=alpha,
                    degree=4,ramification=4,residue_degree=1,local_factor_count=2,
                    required_image_dimension=3,precision=9,ord4=8,
                    prime=base['generators'][26])
    REPS=[from_digits(i) for i in range(512)]
    check('all residue representatives',all(reduce_pi(a)==i for i,a in enumerate(REPS)))
    squares={};square_rows=[]
    for a in range(1,512,2):
        b=ringmul(a,a);squares.setdefault(b,a);square_rows.append([a,b])
    UNITMASK={x:0 for x in squares};gens=[]
    for a in range(1,512,2):
        if a in UNITMASK:continue
        bit=1<<len(gens);gens.append(a)
        old=list(UNITMASK.items())
        for x,m in old:
            y=ringmul(a,x)
            check('unit coset disjoint',y not in UNITMASK)
            UNITMASK[y]=m|bit
    check('full unit quotient',len(UNITMASK)==256 and len(gens)==5 and len(squares)==8)
    D['square_table']=dict(representatives=REPS,square_rows=square_rows,
                           square_roots=squares,unit_generators=gens,
                           unit_masks=UNITMASK,unit_dimension=5,field_dimension=6)
    # Certify multiplication by quotient generators on every unit.
    for a in range(1,512,2):
        for j,g in enumerate(gens):check('unit coordinate homomorphism',UNITMASK[ringmul(a,g)]==UNITMASK[a]^(1<<j))
    r=Q(9075);H=model['model']['H'];G=model['model']['G']
    h=evaluate(H,r);branch=pair(h,add([r,0,0,0],scale(eta,-1)))
    check('branch norm',norm(add([r,0,0,0],scale(eta,-1)))==h)
    D['generators'].append(dict(type='branch',X=r,evaluation=branch))
    image=elim([branch['mask']])
    # These are authenticated actual Q_2 points, not an exhaustion claim.
    for depth in range(13):
        for k in range(2**depth):
            if depth and k%2==0:continue
            x=Q(k,2**max(0,depth-8))
            if x==r:continue
            D['bounds']['samples_tested']+=1;D['bounds']['max_sample_parameter']=depth
            assert D['bounds']['samples_tested']<=200000
            y2=evaluate(G,x)
            if not y2:continue
            rc=rational_class(y2)
            if rc['mask']:continue
            v=pair(x-r,add([x,0,0,0],scale(eta,-1)))
            D['samples'].append(dict(X=x,Y_squared=y2,square_certificate=rc,evaluation=v))
            if reduce_mask(v['mask'],image['pivots']):
                D['generators'].append(dict(type='local_point',sample=len(D['samples'])-1,evaluation=v))
                image=elim([v['evaluation']['mask'] for v in D['generators']])
            if image['rank']==3:break
        if image['rank']==3:break
    D['image']=image
    D['quadratic_fields']=[];D['quadratic_samples']=[]
    if image['rank']<3:
        for spec in [('unramified-5',-1,-1,True),('minus-one',2,-2,False),
                     ('two',-2,0,False),('minus-two',2,0,False),
                     ('minus-five',6,-2,False),('ten',-10,0,False),('minus-ten',10,0,False)]:
            field=Quadratic(*spec);D['quadratic_fields'].append(field.record)
            for a in range(32):
                for b in range(1,32):
                    D['bounds']['samples_tested']+=1
                    assert D['bounds']['samples_tested']<=200000
                    y2=field.ev(G,[Q(a),Q(b)]);sc=field.square(y2)
                    if not sc['square']:continue
                    v=trace_evaluation(Q(a),Q(b),field,r,eta)
                    D['quadratic_samples'].append(dict(field=field.name,X=[a,b],Y_squared=y2,
                                                       square_certificate=sc,evaluation=v))
                    if reduce_mask(v['mask'],image['pivots']):
                        D['generators'].append(dict(type='quadratic_trace',sample=len(D['quadratic_samples'])-1,evaluation=v))
                        image=elim([v['evaluation']['mask'] for v in D['generators']])
                    if image['rank']==3:break
                if image['rank']==3:break
            if image['rank']==3:break
    D['image']=image
    D['image_complete']=image['rank']==3
    check('dimension saturation',D['image_complete'])
    # Reuse exact old local masks; bind every witness by its full source record.
    D['witnesses']=[]
    # Real W is canonically span of masks 30 and 24.
    realp=elim([30,24])['pivots'];elevenp=elim([5])['pivots']
    check('eleven full input order',len(eleven['witnesses'])==39)
    oldcols=[]
    for j,w in enumerate(real['witnesses']):
        b=matvec(inverse,list(map(Q,w['coefficients'])))
        q=Q(w['inverse_norm']);v=pair(q,b)
        check('signed norm '+w['id'],norm(b)==Q(w['signed_norm']) and q*norm(b)==1)
        old=eleven['witnesses'][j]
        check('eleven witness full source '+w['id'],old['id']==w['id'] and old['source']==w)
        realmask=w['mask']
        elevenmask=old['pair']['mask']
        oldmask=reduce_mask(realmask,realp)|(reduce_mask(elevenmask,elevenp)<<5)
        oldcols.append(oldmask)
        D['witnesses'].append(dict(id=w['id'],source=w,local=v,real_mask=realmask,
                                  eleven_mask=elevenmask,old_quotient=oldmask,
                                  dyadic_quotient=reduce_mask(v['mask'],image['pivots'])))
    oldker=elim(oldcols);D['old_conditions']=oldker
    D['kernel_products']=[];quotients=[]
    for c in oldker['kernel']:
        b=ONE[:];q=Q(1);localmask=rm=em=0
        for j,w in enumerate(D['witnesses']):
            if (c>>j)&1:
                b=mul(b,w['local']['quartic']['coefficients']);q*=Q(w['source']['inverse_norm']);observe(q)
                localmask^=w['local']['mask'];rm^=w['real_mask'];em^=w['eleven_mask']
        v=pair(q,b)
        check('kernel product norm',q*norm(b)==1)
        check('kernel product localization',v['mask']==localmask)
        check('both old memberships',reduce_mask(rm,realp)==0 and reduce_mask(em,elevenp)==0)
        quotient=reduce_mask(v['mask'],image['pivots']);quotients.append(quotient)
        D['kernel_products'].append(dict(coefficients=c,pair=v,real_mask=rm,eleven_mask=em,quotient=quotient))
    D['additional_conditions']=elim(quotients)
    D['completed']=True

if __name__=='__main__':
    try:main()
    except Exception as e:
        D['failures'].append(dict(type=type(e).__name__,message=str(e),traceback=traceback.format_exc()))
    OUT.write_text(json.dumps(D,indent=2,default=str)+'\n')
    print(json.dumps(dict(completed=D['completed'],failures=[f['message'] for f in D['failures']],
                         image_rank=D.get('image',{}).get('rank'),required_image_rank=3,
                         additional_rank=D.get('additional_conditions',{}).get('rank'),
                         bounds=D['bounds'],path=str(OUT))))
    raise SystemExit(0 if D['completed'] else 1)
