"""Independent order-basis replay; no producer import or numerical proposals."""
from fractions import Fraction as Q
from hashlib import sha256
from itertools import permutations
from math import isqrt
from pathlib import Path
import json
import traceback

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'surviving-witness-span-verification.json'
R=dict(completed=False,failures=[],checks=0,bindings={},max_rational_bits=0)
ONE=list(map(Q,[1,0,0,0]))


def ck(ok,name):
    R['checks']+=1
    assert ok,name


def read(n):
    raw=(ROOT/n).read_bytes();R['bindings'][n]=sha256(raw).hexdigest()
    return json.loads(raw)


def obs(x):
    if isinstance(x,(tuple,list)):
        for v in x:obs(v)
    elif isinstance(x,(int,Q)):
        x=Q(x);bits=max(abs(x.numerator).bit_length(),x.denominator.bit_length())
        R['max_rational_bits']=max(bits,R['max_rational_bits'])
        ck(bits<=8192,'coefficient bound')
    return x


def multiply(a,b):
    return obs([sum(Q(T[i][j][k])*a[i]*b[j] for i in range(4) for j in range(4)) for k in range(4)])


def to_order(p):
    a,b,c,d=map(Q,p);w3=18750*d;w2=50*(c-Q(239,18750)*w3)
    w1=b-Q(7,25)*w2-Q(179,750)*w3
    w0=a-w2/2-Q(31,30)*w3
    return obs([w0,w1,w2,w3])


def determinant(m):
    # Leibniz on the order multiplication matrix, not a polynomial resultant.
    ans=Q(0)
    for perm in permutations(range(4)):
        x=Q((-1)**sum(perm[i]>perm[j] for i in range(4) for j in range(i+1,4)))
        for i in range(4):x*=m[i][perm[i]]
        ans+=x
    return obs(ans)


def norm(b):
    cols=[multiply(b,[Q(i==j) for i in range(4)]) for j in range(4)]
    return determinant([[cols[j][i] for j in range(4)] for i in range(4)])


def combination(cols,k):
    v=0
    while k:
        low=k&-k;v^=cols[low.bit_length()-1];k-=low
    return v


def rank(cols):
    piv={}
    for v in cols:
        while v:
            low=v&-v
            if low not in piv:piv[low]=v;break
            v^=piv[low]
    return len(piv)


def main():
    global T
    C=read('surviving-witness-span-certificate.json')
    ck(C['completed'] and not C['failures'] and C['outcome']=='outside','completed outside result')
    ck(C['source_sha256']==sha256((ROOT/'surviving_witness_span.py').read_bytes()).hexdigest(),'producer binding')
    for n,h in C['bindings'].items():
        ck(sha256((ROOT/n).read_bytes()).hexdigest()==h,'full binding '+n)
    old=read('odd-membership-35-certificate.json');two=read('two-adic-filter-certificate.json')
    base=read('quartic-class-certificate.json');model=read('odd-model-support-certificate.json')
    T=base['order']['table'];ck(old['table']==T,'authenticated order table')
    ck(C['alpha_polynomial']==model['field']['alpha_polynomial'],'same field')
    witnesses=two['witnesses'];ck(len(witnesses)==39,'39 source columns')
    qcols=[];lcols=[];source=[]
    for j,w in enumerate(witnesses):
        p3=old['places']['3']['witnesses'][j];p5=old['places']['5']['witnesses'][j]
        ck(w['source']==p3['source']==p5['source'] and w['id']==p3['id']==p5['id'],'complete ordered source equality')
        masks=[w['real_mask'],w['eleven_mask'],w['local']['mask'],p3['evaluation']['mask'],p5['evaluation']['mask']]
        ck(all(0<=x<2**width for x,width in zip(masks,[5,4,9,6,8])),'full local widths')
        quot=[w['old_quotient'],w['dyadic_quotient'],p3['quotient'],p5['quotient']]
        ck(all(0<=x<2**width for x,width in zip(quot,[9,9,6,8])),'quotient widths')
        qcols.append(quot[0]+(quot[1]<<9)+(quot[2]<<18)+(quot[3]<<24))
        lcols.append(sum(x<<shift for x,shift in zip(masks,[0,5,9,18,24])))
        b=list(map(Q,w['source']['coefficients']));q=Q(w['source']['inverse_norm'])
        ck(q*norm(b)==1,'each source exact norm one')
        ck(bool(q) and any(b),'source nonzero')
        if 'valuations' in w['source']:
            vals=w['source']['valuations'];ck(len(vals)==32,'full supported valuation record')
            ck(all(v%2==0 for i,v in enumerate(vals) if i not in {1,26,27,28,29,30,31}),'outside-support parity')
        else:
            ck(j>=34 and b in [list(map(Q,[v,0,0,0])) for v in [-1,2,3,5,11]],'prescribed rational appended source')
        source.append((q,b))
    ker=old['all_conditions']['kernel']
    ck(C['kernel']==ker and len(ker)==rank(ker)==31 and rank(qcols)==8,'entire kernel equality/completeness')
    ck(C['quotient_columns']==qcols and C['full_local_columns']==lcols,'entire full and quotient localization columns')
    for k in ker:ck(0<k<2**39 and combination(qcols,k)==0,'every kernel vector and local membership')
    def reconstruct(k):
        q=Q(1);b=ONE[:]
        for j,(qj,bj) in enumerate(source):
            if k>>j&1:q=obs(q*qj);b=multiply(b,bj)
        ck(q*norm(b)==1,'product norm one')
        return q,b
    refs={}
    for rec,k in zip(C['references'],[0,165,132102,132259]):
        q,b=reconstruct(k);l=combination(lcols,k)
        ck(rec['mask']==k and Q(rec['rational'])==q and to_order(rec['quartic_power'])==b and rec['full_local']==l,'reference full product')
        refs[k]=(q,b,l)
    ck(len(C['references'])==4,'all four reference classes')
    for rec in old['selected_pair']:
        q,b,l=refs[rec['coefficients']]
        ck(Q(rec['rational'])==q and list(map(Q,rec['quartic_O']))==b and rec['local_detection']==l,'accepted pair reconstructed')
    ck(rank([refs[165][2],refs[132102][2]])==2,'reference independence')
    products={}
    ck(C['outside_generator_index']==3 and C['outside_mask']==3109 and len(C['products'])==4,'first outside index and stopping point')
    for index,rec in enumerate(C['products']):
        k=ker[index];q,b=reconstruct(k);l=combination(lcols,k)
        ck(rec['index']==index and rec['mask']==k and Q(rec['rational'])==q and to_order(rec['quartic_power'])==b,'entire tested product')
        ck(rec['full_local']==l and rec['quotient']==combination(qcols,k)==0 and Q(rec['norm'])==norm(b),'norm and all local membership')
        products[index]=(q,b,l)
    decisions={i:[] for i in range(4)}
    for rec in C['comparisons']:
        i=rec['generator_index'];k=rec['reference_mask'];q,b,l=products[i];rq,rb,rl=refs[k]
        ck(rec['mask']==ker[i],'comparison source')
        t=q/rq;n,d=isqrt(abs(t.numerator)),isqrt(t.denominator)
        sq=rec['rational_test'];yes=t>=0 and n*n==t.numerator and d*d==t.denominator
        ck(Q(sq['value'])==t and sq['numerator_floor']==n and sq['denominator_floor']==d and sq['square']==yes,'complete rational square decision')
        ck(n*n<=abs(t.numerator)<(n+1)**2 and d*d<=t.denominator<(d+1)**2,'strict consecutive-square bounds')
        ck(rec['local_difference']==l^rl,'full localization difference')
        if rec['decision']=='equal':
            qr=Q(sq['root']);root=to_order(rec['quartic_root_power'])
            ck(yes and qr*qr*rq==q,'exact rational equality')
            ck(multiply(multiply(root,root),rb)==b,'exact quartic equality, all four coordinates')
            ratio=to_order(rec['quartic_ratio_power'])
            ck(multiply(ratio,rb)==b and multiply(root,root)==ratio,'saved ratio and root')
            ck(1<=rec['proposal_patterns_actual']<=16,'bounded proposal count')
        else:
            ck(rec['decision']=='unequal' and (l^rl or not yes),'conclusive inequality; no failed proposal inference')
        decisions[i].append((k,rec['decision']))
    expected={0:[(0,'unequal'),(165,'unequal'),(132102,'equal')],
              1:[(0,'unequal'),(165,'equal')],2:[(0,'equal')],
              3:[(k,'unequal') for k in [0,165,132102,132259]]}
    ck(decisions==expected,'complete ordered comparison domain and early stopping')
    bounds=C['bounds'];ck(len(C['comparisons'])==bounds['comparisons_actual']==10<=124,'actual versus approved comparison cap')
    ck(bounds['generators_decided']==3 and bounds['generators_required']==31,'three contained before first outside; no complete containment claim')
    ck(not C['unresolved'] and bounds['trager_shifts_actual']==0 and bounds['fallback_candidates_actual']==0,'no unresolved or factorization inference')
    # Each of these four rational ratios alone is a conclusive nonsquare.
    outside=[]
    for k,(rq,rb,rl) in refs.items():
        t=products[3][0]/rq;n,d=isqrt(t.numerator),isqrt(t.denominator)
        ck(n*n!=t.numerator or d*d!=t.denominator,'independent rational-only outside certificate')
        outside.append(dict(reference_mask=k,rational_ratio=t,numerator_floor=n,denominator_floor=d))
    R.update(completed=True,outcome='outside',outside_mask=3109,
             outside_rational_comparisons=outside,all_kernel_vectors_checked=31,
             products_checked=4,comparisons_actual=10,comparisons_required_for_outside=4,
             comparisons_cap=124,independent_selmer_classes_at_least=3)


if __name__=='__main__':
    try:main()
    except Exception as e:R['failures'].append(dict(message=str(e),traceback=traceback.format_exc()))
    OUT.write_text(json.dumps(R,indent=2,default=str)+'\n')
    print(json.dumps(dict(completed=R['completed'],checks=R['checks'],outcome=R.get('outcome'),
         outside_mask=R.get('outside_mask'),comparisons_actual=R.get('comparisons_actual'),
         kernel_vectors_checked=R.get('all_kernel_vectors_checked'),kernel_vectors_required=31,
         outside_comparisons_actual=len(R.get('outside_rational_comparisons',[])),outside_comparisons_required=4,
         comparisons_cap=124,max_rational_bits=R['max_rational_bits'],required_bit_cap=8192,
         failures=[v['message'] for v in R['failures']],path=str(OUT))))
    raise SystemExit(0 if R['completed'] else 1)
