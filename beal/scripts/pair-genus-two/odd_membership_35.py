"""Fixed 39-column Selmer entry gate at 3 and 5; no pairing backend.

Uses the audited maximal-order table and exact prime-power lattices.
All local generators are actual Q_p curve points or the rational branch.
"""
from fractions import Fraction as Q
from pathlib import Path
from math import lcm
from hashlib import sha256
import json
import traceback
import quartic_parity_generate as lattice

ROOT = Path(__file__).resolve().parent
OUT = ROOT/'odd-membership-35-certificate.json'
D = dict(completed=False, failures=[], bindings={}, places={}, checks=[],
         bounds=dict(tests_cap_per_place=200000, depth_cap=64,
                     rational_bits_cap=8192, max_rational_bits=0))


def obs(a):
    if isinstance(a, (tuple, list)):
        for x in a: obs(x)
    elif isinstance(a, (int, Q)):
        a=Q(a); n=max(abs(a.numerator).bit_length(), a.denominator.bit_length())
        D['bounds']['max_rational_bits']=max(n,D['bounds']['max_rational_bits'])
        assert n<=8192, 'rational coefficient cap'
    return a


def ck(name, value):
    D['checks'].append(dict(name=name, passed=bool(value)))
    assert value, name


def read(name):
    raw=(ROOT/name).read_bytes(); D['bindings'][name]=sha256(raw).hexdigest()
    return json.loads(raw)


ONE=[Q(1),Q(0),Q(0),Q(0)]


def mul(a,b): return obs(lattice.times(a,b))
def add(a,b): return obs([x+y for x,y in zip(a,b)])
def scale(a,t): return obs([x*t for x in a])


def inverse(m):
    a=[list(map(Q,row))+[Q(i==j) for j in range(4)] for i,row in enumerate(m)]
    for j in range(4):
        k=next(k for k in range(j,4) if a[k][j]);a[j],a[k]=a[k],a[j]
        a[j]=[x/a[j][j] for x in a[j]]
        for k in range(4):
            if k!=j:
                t=a[k][j];a[k]=[x-t*y for x,y in zip(a[k],a[j])]
        obs(a)
    return [row[4:] for row in a]


def mv(m,a): return obs([sum(x*y for x,y in zip(row,a)) for row in m])


def ev(poly,x):
    y=Q(0)
    for a in reversed(poly): y=obs(y*x+Q(a))
    return y


def vp(x,p):
    x=Q(x);assert x
    a,b=x.numerator,x.denominator;v=0
    while a%p==0:a//=p;v+=1
    while b%p==0:b//=p;v-=1
    return v


def residue(x,p):
    x=Q(x);assert x.denominator%p
    return x.numerator%p*pow(x.denominator,-1,p)%p


def nonsquare(x,p):
    assert x%p
    return int(pow(x%p,(p-1)//2,p)!=1)


def qclass(x,p):
    x=Q(x);v=vp(x,p);u=obs(x/Q(p)**v);r=residue(u,p)
    return dict(value=x,valuation=v,residue=r,mask=(v%2)|nonsquare(r,p)<<1)


def elim(columns):
    piv={};ker=[];trace=[]
    for j,x in enumerate(columns):
        z=x;c=1<<j
        while z:
            k=z.bit_length()-1
            if k not in piv:piv[k]=[z,c];break
            v,w=piv[k];z^=v;c^=w
        if not z:ker.append(c)
        trace.append(dict(input=x,reduced=z,coefficients=c))
    return dict(rank=len(piv),pivots={str(k):v for k,v in piv.items()},kernel=ker,trace=trace)


def red(x,piv):
    for k in sorted(map(int,piv),reverse=True):
        if x>>k&1:x^=piv[str(k)][0]
    return x


def combo(columns,c):
    z=0
    for j,x in enumerate(columns):
        if c>>j&1:z^=x
    return z


class Prime:
    def __init__(self,p,index,source):
        self.p=p;self.index=index
        rec=lattice.reduce_lattice(source['lattice']['columns'])
        self.powers=[lattice.reduce_lattice([[int(i==j) for i in range(4)] for j in range(4)]),rec]
        self.pigens=[ONE]
        self.record=dict(index=index,source=source,powers=self.powers)
        self.extend(2)
        self.pi=next(a for a in rec['rows'] if not self.member(a,2))
        self.record['uniformizer']=self.pi
        self.pigens.append(self.pi)
        self.pclass=self.integral([p,0,0,0])
        self.record['rational_prime_class']=self.pclass

    def extend(self,n):
        assert n<=64,'ideal depth cap'
        while len(self.powers)<=n:
            gens=[mul(a,b) for a in self.powers[-1]['rows'] for b in self.powers[1]['rows']]
            r=lattice.reduce_lattice(gens)
            ck('prime power norm',r['norm']==self.p**len(self.powers))
            self.powers.append(r)

    def member(self,a,n):
        self.extend(n)
        return lattice.coordinates(self.powers[n]['rows'],a)['member']

    def integral(self,a):
        assert all(Q(x).denominator==1 for x in a)
        v=0
        while self.member(a,v+1):v+=1
        while len(self.pigens)<=v:self.pigens.append(mul(self.pigens[-1],self.pi))
        pi=self.pigens[v]
        residues=[t for t in range(1,self.p) if self.member(add(a,scale(pi,-t)),v+1)]
        ck('unique normalized residue',len(residues)==1)
        t=residues[0]
        return dict(valuation=v,residue=t,mask=(v%2)|nonsquare(t,self.p)<<1)

    def classify(self,b):
        den=lcm(*(Q(x).denominator for x in b));a=scale(b,den)
        c=self.integral(a);d=vp(den,self.p);u=den//self.p**d
        mask=c['mask'] ^ (self.pclass['mask'] if d%2 else 0) ^ (nonsquare(u,self.p)<<1)
        return dict(integral=a,denominator=den,integral_class=c,denominator_valuation=d,
                    denominator_unit_residue=u%self.p,mask=mask)


class Place:
    def __init__(self,p,base):
        self.p=p;self.primes=[Prime(p,i,P) for i,P in enumerate(base['generators']) if P['p']==p]
        self.record=dict(primes=[P.record for P in self.primes],tests=0,
                         required_dimension=len(self.primes),generators=[],samples=[],rejected=[],witnesses=[])
        ck('all primes residue degree one',all(P.record['source']['lattice']['norm']==p for P in self.primes))
        ck('complete ramification degree',sum(P.pclass['valuation'] for P in self.primes)==4)
        self.record['ramification_indices']=[P.pclass['valuation'] for P in self.primes]
        self.record['local_factor_count']=1+len(self.primes)

    def pair(self,q,b):
        qr=qclass(q,self.p);fs=[P.classify(b) for P in self.primes]
        mask=qr['mask']
        for i,f in enumerate(fs):mask|=f['mask']<<(2+2*i)
        return dict(rational=qr,quartic=fs,mask=mask)

    def add_generator(self,record):
        old=elim([g['evaluation']['mask'] for g in self.record['generators']])
        if red(record['evaluation']['mask'],old['pivots']):self.record['generators'].append(record)

    def saturated(self):return len(self.record['generators'])==len(self.primes)


def main():
    base=read('quartic-class-certificate.json');model=read('odd-model-support-certificate.json')
    two=read('two-adic-filter-certificate.json');audit=read('two-adic-filter-audit.json')
    for name,C in [('quartic-class',base),('two-adic-filter',two)]:
        ck(name+' complete',C['completed'] and not C['failures'])
    ck('odd-model-support complete',model['status']=='PASS' and not model['failures'])
    ck('accepted dyadic binding',audit['completed'] and not audit['failures'] and
       audit['bindings']['two-adic-filter-certificate.json']==D['bindings']['two-adic-filter-certificate.json'])
    ck('same order basis',base['order']['basis']==model['field']['O_basis_in_alpha'])
    ck('fixed 39 witnesses',len(two['witnesses'])==39)
    lattice.TABLE=base['order']['table'];D['table']=lattice.TABLE
    orderinv=inverse(model['field']['O_basis_in_alpha'])
    eta=mv(orderinv,list(map(Q,model['field']['eta_in_alpha'])))
    G=model['model']['G'];H=model['model']['H'];r=Q(9075)
    h=ev(H,r);D['model']=dict(G=G,H=H,r=r,eta_O=eta,basis=model['field']['O_basis_in_alpha'])
    # Use accepted exact quotient columns without changing their target spaces.
    oldcols=[w['old_quotient']|(w['dyadic_quotient']<<9) for w in two['witnesses']]
    D['old_conditions']=elim(oldcols);ck('prior real/11/2 coefficient rank five',D['old_conditions']['rank']==5)
    for p in (3,5):
        place=Place(p,base);P=place.record;D['places'][str(p)]=P
        branch=place.pair(h,add(scale(ONE,r),scale(eta,-1)))
        place.add_generator(dict(type='rational_branch',X=r,evaluation=branch))
        seen=set()
        # Cluster-aware bounded grid, no enumeration of coefficient combinations.
        for k in range(-4,17):
            if place.saturated():break
            for center in (Q(0),r):
                if place.saturated():break
                for a in range(1,p**3):
                    x=obs(center+Q(p)**k*a)
                    if x in seen or x==r:continue
                    seen.add(x);P['tests']+=1
                    assert P['tests']<=200000 and abs(k)<=64
                    y2=ev(G,x)
                    if not y2:continue
                    square=qclass(y2,p)
                    if square['mask']:
                        P['rejected'].append(dict(X=x,Y_squared=y2,square_certificate=square));continue
                    v=place.pair(x-r,add(scale(ONE,x),scale(eta,-1)))
                    P['samples'].append(dict(X=x,Y_squared=y2,square_certificate=square,evaluation=v,grid_depth=k))
                    place.add_generator(dict(type='local_point',sample=len(P['samples'])-1,evaluation=v))
                    if place.saturated():break
        P['image']=elim([g['evaluation']['mask'] for g in P['generators']])
        P['image_complete']=place.saturated()
        if not P['image_complete']:
            P['stopping_gate']='local image not saturated in fixed rational grid'
            D['stopping_gate']=str(p)+'-adic image incomplete';return
        for w in two['witnesses']:
            src=w['source'];v=place.pair(Q(src['inverse_norm']),list(map(Q,src['coefficients'])))
            P['witnesses'].append(dict(id=w['id'],source=src,evaluation=v,quotient=red(v['mask'],P['image']['pivots'])))
        cols=[w['quotient'] for w in P['witnesses']]
        P['condition_on_old_kernel']=elim([combo(cols,c) for c in D['old_conditions']['kernel']])
    columns=[]
    for j,x in enumerate(oldcols):
        columns.append(x|(D['places']['3']['witnesses'][j]['quotient']<<18)|
                       (D['places']['5']['witnesses'][j]['quotient']<<24))
    D['all_conditions']=elim(columns)
    missing=[D['places']['3']['witnesses'][j]['quotient']|
             D['places']['5']['witnesses'][j]['quotient']<<6 for j in range(39)]
    restricted=[combo(missing,c) for c in D['old_conditions']['kernel']]
    D['combined_new_conditions']=elim(restricted)
    D['new_condition_witnesses']=[]
    for c,z in zip(D['old_conditions']['kernel'],restricted):
        if red(z,elim([w['quotient'] for w in D['new_condition_witnesses']])['pivots']):
            D['new_condition_witnesses'].append(dict(coefficients=c,quotient=z))
    # A nonzero local class proves a represented global class nonzero;
    # two independent local tuples certify independence without a global basis.
    detections=[]
    for j,w in enumerate(two['witnesses']):
        detections.append(w['real_mask']|(w['eleven_mask']<<5)|(w['local']['mask']<<9)|
            (D['places']['3']['witnesses'][j]['evaluation']['mask']<<18)|
            (D['places']['5']['witnesses'][j]['evaluation']['mask']<<24))
    pair=[]
    for c in sorted(D['all_conditions']['kernel'],key=lambda c:(c.bit_count(),c)):
        detect=combo(detections,c)
        if not red(detect,elim([a['local_detection'] for a in pair])['pivots']):continue
        b=ONE[:];q=Q(1)
        for j,w in enumerate(two['witnesses']):
            if c>>j&1:
                b=mul(b,list(map(Q,w['source']['coefficients'])))
                q=obs(q*Q(w['source']['inverse_norm']))
        pair.append(dict(coefficients=c,indices=[j for j in range(39) if c>>j&1],
                         rational=q,quartic_O=b,local_detection=detect))
        if len(pair)==2:break
    D['selected_pair']=pair if len(pair)==2 else []
    # Formal coefficient dimension only; no assertion of global independence.
    D['result']=dict(old_coefficient_dimension=39-D['old_conditions']['rank'],
                     all_membership_coefficient_dimension=39-D['all_conditions']['rank'],
                     all_membership_masks=D['all_conditions']['kernel'],
                     selmer_membership_certified=True,pair_selected=len(pair)==2,
                     selected_pair_independence_certified=len(pair)==2,
                     global_basis_certified=False,
                     additional_condition_rank_on_fixed_old_space=D['combined_new_conditions']['rank'],
                     supported_dimension_upper_constant=6-D['combined_new_conditions']['rank'],
                     rank_upper_constant=5-D['combined_new_conditions']['rank'],class_contribution_max=2,
                     rank_upper_bound=7-D['combined_new_conditions']['rank'],
                     rank_bound_improvement=D['combined_new_conditions']['rank'],
                     next_gate='odd/sextic class transport and compatible coverings uncomputed')
    D['completed']=True


if __name__=='__main__':
    try:main()
    except Exception as e:D['failures'].append(dict(type=type(e).__name__,message=str(e),traceback=traceback.format_exc()))
    D['source_sha256']=sha256(Path(__file__).read_bytes()).hexdigest()
    D['helper_sha256']=sha256((ROOT/'quartic_parity_generate.py').read_bytes()).hexdigest()
    OUT.write_text(json.dumps(D,indent=2,default=str)+'\n')
    print(json.dumps(dict(completed=D['completed'],failures=[f['message'] for f in D['failures']],
        places={p:dict(tests=r['tests'],image_rank=r.get('image',{}).get('rank'),required=r['required_dimension']) for p,r in D['places'].items()},
        result={k:v for k,v in D.get('result',{}).items() if k!='all_membership_masks'},
        stopping_gate=D.get('stopping_gate'),bounds=D['bounds'],path=str(OUT))))
    raise SystemExit(0 if D['completed'] else 1)
