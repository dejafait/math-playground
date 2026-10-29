"""Bounded saved-image test. Only exact identities/obstructions decide classes.

Decimal roots are proposals, never negative evidence. Accepted source hashes
authenticate support and full local coordinates; products are rebuilt here.
"""
from fractions import Fraction as Q
from decimal import Decimal as D, localcontext
from hashlib import sha256
from itertools import permutations, product
from math import isqrt
from pathlib import Path
import json
import traceback

ROOT = Path(__file__).resolve().parent
OUT = ROOT/'surviving-witness-span-certificate.json'
R = dict(completed=False, failures=[], bindings={}, checks=0, products=[],
         comparisons=[], unresolved=[], bounds=dict(comparisons_actual=0,
         comparisons_cap=124, generators_required=31, generators_decided=0,
         trager_shifts_actual=0, trager_shift_cap=32,
         fallback_candidates_actual=0, fallback_candidate_cap_per_comparison=100000,
         proposal_patterns_cap_per_comparison=16, proposal_patterns_actual=0,
         rational_bits_cap=8192, max_rational_bits=0))
A = [-109375,-32500,150,64,1]
ONE = list(map(Q,[1,0,0,0]))
B = [[Q(1),Q(0),Q(1,2),Q(31,30)],
     [Q(0),Q(1),Q(7,25),Q(179,750)],
     [Q(0),Q(0),Q(1,50),Q(239,18750)],
     [Q(0),Q(0),Q(0),Q(1,18750)]]


def ck(ok, name):
    R['checks'] += 1
    assert ok, name


def obs(x):
    if isinstance(x,(list,tuple)):
        for t in x: obs(t)
    elif isinstance(x,(int,Q)):
        x=Q(x); bits=max(abs(x.numerator).bit_length(),x.denominator.bit_length())
        R['bounds']['max_rational_bits']=max(bits,R['bounds']['max_rational_bits'])
        ck(bits<=8192,'rational coefficient bit cap')
    return x


def read(name):
    raw=(ROOT/name).read_bytes(); R['bindings'][name]=sha256(raw).hexdigest()
    return json.loads(raw)


def bind(c):
    for name,h in c.get('bindings',{}).items():
        ck(sha256((ROOT/name).read_bytes()).hexdigest()==h,'binding '+name)
        R['bindings'][name]=h


def mul(a,b):
    v=[Q(0)]*7
    for i in range(4):
        for j in range(4): v[i+j]+=a[i]*b[j]
    for k in range(6,3,-1):
        for j in range(4): v[k-4+j]-=v[k]*A[j]
    return obs(v[:4])


def powercoords(v):
    return obs([sum(B[i][j]*Q(v[j]) for j in range(4)) for i in range(4)])


def solve(m,b):
    z=[list(row)+[v] for row,v in zip(m,b)]
    for j in range(4):
        k=next(k for k in range(j,4) if z[k][j])
        z[j],z[k]=z[k],z[j]; t=z[j][j]; z[j]=[x/t for x in z[j]]
        for k in range(4):
            if k!=j:
                t=z[k][j]; z[k]=[x-t*y for x,y in zip(z[k],z[j])]
    return [r[-1] for r in z]


def inv(a):
    cols=[mul(a,[Q(i==j) for i in range(4)]) for j in range(4)]
    v=obs(solve([[cols[j][i] for j in range(4)] for i in range(4)],ONE))
    ck(mul(v,a)==ONE,'field inverse'); return v


def norm(a):
    cols=[mul(a,[Q(i==j) for i in range(4)]) for j in range(4)]
    ans=Q(0)
    for p in permutations(range(4)):
        v=Q((-1)**sum(p[i]>p[j] for i in range(4) for j in range(i+1,4)))
        for j in range(4): v*=cols[j][p[j]]
        ans+=v
    return obs(ans)


def combo(cols,mask):
    v=0
    for j,x in enumerate(cols):
        if mask>>j&1:v^=x
    return v


def rank(cols):
    piv={}
    for v in cols:
        while v:
            k=v.bit_length()-1
            if k not in piv:piv[k]=v;break
            v^=piv[k]
    return len(piv)


def rational_square(q):
    n,d=isqrt(abs(q.numerator)),isqrt(q.denominator)
    yes=q>=0 and n*n==q.numerator and d*d==q.denominator
    return dict(value=q,numerator_floor=n,denominator_floor=d,
                square=yes,root=Q(n,d) if yes else None)


def ev(p,x):
    v=x*0
    for c in reversed(p):v=v*x+c
    return v


def proposal(b, roots):
    # Same standard proposal device as L148; exact modular squaring accepts.
    with localcontext() as ctx:
        ctx.prec=200
        dec=lambda x:D(x.numerator)/D(x.denominator)
        vals=[ev(list(map(dec,b)),a) for a in roots]
        if min(vals)<0:return None,0
        vals=[v.sqrt() for v in vals]
        for count,signs in enumerate(product([-1,1],repeat=4),1):
            coeff=solve([[a**j for j in range(4)] for a in roots],
                        [v*s for v,s in zip(vals,signs)])
            cand=obs([Q(c).limit_denominator(10**12) for c in coeff])
            if mul(cand,cand)==b:return cand,count
    return None,16


def main():
    C=read('odd-membership-35-certificate.json')
    V=read('odd-membership-35-verification.json')
    audit=read('odd-membership-35-audit.json')
    two=read('two-adic-filter-certificate.json')
    model=read('odd-model-support-certificate.json')
    branch=read('branch-annihilator-certificate.json')
    for c in (C,V,audit,two,model,branch):
        ck((c.get('completed') or c.get('status')=='PASS') and not c['failures'],'accepted input success');bind(c)
    for n in ('branch-annihilator-verification.json','branch-annihilator-audit.json',
              'two-adic-filter-verification.json','two-adic-filter-audit.json',
              'odd-model-support-verification.json','odd-model-support-audit.json'):
        c=read(n);ck((c.get('completed') or c.get('status')=='PASS') and not c['failures'],'accepted replay/audit '+n)
        # Audit texts may have been appended; bind the mathematical JSON inputs.
        for name,h in c.get('bindings',{}).items():
            if name.endswith('.json'):
                name=Path(name).name
                ck(sha256((ROOT/name).read_bytes()).hexdigest()==h,'accepted JSON binding '+name)
                R['bindings'][name]=h
    ck([list(map(Q,row)) for row in C['model']['basis']]==B,'full basis')
    ck(C['model']['G']==model['model']['G'] and C['model']['H']==model['model']['H'],'actual odd model')
    witnesses=two['witnesses'];ck(len(witnesses)==39,'fixed domain')
    kernel=C['all_conditions']['kernel']
    ck(len(kernel)==rank(kernel)==31,'all independent kernel generators')
    oldcols=[w['old_quotient']|(w['dyadic_quotient']<<9) for w in witnesses]
    cols=[x|(C['places']['3']['witnesses'][j]['quotient']<<18)|
          (C['places']['5']['witnesses'][j]['quotient']<<24) for j,x in enumerate(oldcols)]
    ck(rank(cols)==8,'complete quotient rank')
    ck(all(0<k<2**39 and combo(cols,k)==0 for k in kernel),'all 31 zero local quotient combinations')
    loc=[w['real_mask']|(w['eleven_mask']<<5)|(w['local']['mask']<<9)|
         (C['places']['3']['witnesses'][j]['evaluation']['mask']<<18)|
         (C['places']['5']['witnesses'][j]['evaluation']['mask']<<24) for j,w in enumerate(witnesses)]
    sources=[]
    for j,w in enumerate(witnesses):
        src=w['source'];b=powercoords(src['coefficients']);q=Q(src['inverse_norm'])
        ck(src==C['places']['3']['witnesses'][j]['source']==C['places']['5']['witnesses'][j]['source'],'whole ordered source')
        ck(w['id']==C['places']['3']['witnesses'][j]['id']==C['places']['5']['witnesses'][j]['id'],'ordered IDs')
        ck(q*norm(b)==1,'each full product norm one')
        if 'valuations' in src:
            ck(len(src['valuations'])==32 and all(v%2==0 for i,v in enumerate(src['valuations']) if i not in {1,26,27,28,29,30,31}),'accepted full outside-support parity')
        sources.append((q,b))
    def reconstruct(mask):
        q=Q(1);b=ONE[:]
        for j,(qj,bj) in enumerate(sources):
            if mask>>j&1:q=obs(q*qj);b=mul(b,bj)
        ck(q*norm(b)==1,'reconstructed norm one')
        return q,b
    refs=[]
    for k in [0,165,132102,165^132102]:
        q,b=reconstruct(k);refs.append((k,q,b,combo(loc,k)))
    for rec,ref in zip(C['selected_pair'],refs[1:3]):
        k,q,b,l=ref
        ck(rec['coefficients']==k and Q(rec['rational'])==q and powercoords(rec['quartic_O'])==b and rec['local_detection']==l,'both exact reference representatives')
    R.update(alpha_polynomial=A,order_basis=B,kernel=kernel,quotient_columns=cols,
             full_local_columns=loc,references=[dict(mask=k,rational=q,quartic_power=b,full_local=l) for k,q,b,l in refs])
    with localcontext() as ctx:
        ctx.prec=200;roots=[]
        for lo,hi in [(-48,-47),(-34,-33),(-4,-3),(20,21)]:
            lo,hi=D(lo),D(hi);ck(ev(A,lo)*ev(A,hi)<0,'proposal root bracket')
            for _ in range(750):
                mid=(lo+hi)/2
                if ev(A,lo)*ev(A,mid)<0:hi=mid
                else:lo=mid
            roots.append((lo+hi)/2)
    for index,k in enumerate(kernel):
        q,b=reconstruct(k);l=combo(loc,k)
        R['products'].append(dict(index=index,mask=k,rational=q,quartic_power=b,full_local=l,
                                  quotient=combo(cols,k),norm=norm(b),supported_by_accepted_columns=True))
        equal=False;inequalities=0
        for rk,rq,rb,rl in refs:
            R['bounds']['comparisons_actual']+=1
            ck(R['bounds']['comparisons_actual']<=124,'comparison cap')
            sq=rational_square(q/rq)
            rec=dict(generator_index=index,mask=k,reference_mask=rk,rational_test=sq,
                     local_difference=l^rl)
            R['comparisons'].append(rec)
            if l^rl:
                rec.update(decision='unequal',evidence='nonzero authenticated full localization');inequalities+=1;continue
            if not sq['square']:
                rec.update(decision='unequal',evidence='complete rational square test');inequalities+=1;continue
            ratio=mul(b,inv(rb));rec['quartic_ratio_power']=ratio
            root,count=proposal(ratio,roots)
            rec['proposal_patterns_actual']=count;R['bounds']['proposal_patterns_actual']+=count
            if root is not None:
                ck(mul(mul(root,root),rb)==b,'direct quartic equality')
                rec.update(decision='equal',evidence='exact componentwise square roots',quartic_root_power=root)
                equal=True;break
            rec.update(decision='unresolved',evidence='no exact proposed root; complete factorization evidence unavailable; no nonsquare conclusion')
            R['unresolved'].append(dict(generator_index=index,reference_mask=rk))
        if equal:R['bounds']['generators_decided']+=1
        elif inequalities==4:
            R.update(completed=True,outcome='outside',outside_generator_index=index,outside_mask=k)
            return
    R.update(completed=True,outcome='contained' if R['bounds']['generators_decided']==31 else 'partial')


if __name__=='__main__':
    try:main()
    except Exception as e:R['failures'].append(dict(message=str(e),traceback=traceback.format_exc()))
    R['source_sha256']=sha256(Path(__file__).read_bytes()).hexdigest()
    OUT.write_text(json.dumps(R,indent=2,default=str)+'\n')
    print(json.dumps(dict(completed=R['completed'],outcome=R.get('outcome'),checks=R['checks'],
         bounds=R['bounds'],unresolved=len(R['unresolved']),failures=[x['message'] for x in R['failures']],path=str(OUT))))
    raise SystemExit(0 if R['completed'] else 1)
