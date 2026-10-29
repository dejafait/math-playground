"""Independent arithmetic replay: Gaussian lattice coordinates, low-bit F2 pivots."""
from fractions import Fraction as Q
from pathlib import Path
from hashlib import sha256
from itertools import permutations
from math import lcm
import json
import traceback

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'odd-membership-35-verification.json'
R=dict(completed=False,failures=[],checks=0,bindings={},max_rational_bits=0)


def ck(b,name):
    R['checks']+=1
    assert b,name


def obs(a):
    if isinstance(a,(list,tuple)):
        for x in a:obs(x)
    elif isinstance(a,(int,Q)):
        a=Q(a);n=max(abs(a.numerator).bit_length(),a.denominator.bit_length())
        R['max_rational_bits']=max(R['max_rational_bits'],n)
        ck(n<=8192,'rational cap')
    return a


def read(name):
    raw=(ROOT/name).read_bytes();R['bindings'][name]=sha256(raw).hexdigest()
    return json.loads(raw)


def vec(a):return list(map(Q,a))
ONE=vec([1,0,0,0])
def plus(a,b):return obs([x+y for x,y in zip(a,b)])
def times(a,b):return obs([sum(a[i]*b[j]*T[i][j][k] for i in range(4) for j in range(4)) for k in range(4)])
def scale(a,n):return obs([x*n for x in a])


def det(m):
    z=Q(0)
    for s in permutations(range(4)):
        a=Q((-1)**sum(s[i]>s[j] for i in range(4) for j in range(i+1,4)))
        for i in range(4):a*=Q(m[i][s[i]])
        z+=a
    return obs(z)


def coords(rows,v):
    a=[[Q(rows[j][i]) for j in range(4)]+[Q(v[i])] for i in range(4)]
    for j in range(4):
        k=next(k for k in range(j,4) if a[k][j]);a[j],a[k]=a[k],a[j]
        t=a[j][j];a[j]=[x/t for x in a[j]]
        for k in range(4):
            if k!=j:
                t=a[k][j];a[k]=[x-t*y for x,y in zip(a[k],a[j])]
        obs(a)
    return [r[4] for r in a]


def member(rows,v):return all(x.denominator==1 for x in coords(rows,v))


def val(x,p):
    x=Q(x);ck(bool(x),'nonzero');v=0
    while x.numerator%p==0:x/=p;v+=1
    while x.denominator%p==0:x*=p;v-=1
    return v


def ns(r,p):
    ck(r%p!=0,'unit residue')
    return int(r%p not in {a*a%p for a in range(1,p)})


def qcheck(rec,x,p):
    x=Q(x);v=val(x,p);u=obs(x/Q(p)**v);r=u.numerator%p*pow(u.denominator,-1,p)%p
    mask=v%2+2*ns(r,p)
    ck(Q(rec['value'])==x and rec['valuation']==v and rec['residue']==r and rec['mask']==mask,'Qp class')
    return mask


def integralcheck(rec,a,P,p):
    v=rec['valuation'];pi=vec(P['uniformizer']);power=ONE[:]
    for _ in range(v):power=times(power,pi)
    rows=P['powers'][v+1]['rows']
    ck(member(P['powers'][v]['rows'],a) and not member(rows,a),'exact ideal valuation')
    t=rec['residue'];ck(1<=t<p and member(rows,plus(a,scale(power,-t))),'full normalized residue')
    mask=v%2+2*ns(t,p);ck(rec['mask']==mask,'integral mask');return mask


def fieldcheck(rec,b,P,p):
    den=lcm(*(x.denominator for x in b));a=scale(b,den);d=val(den,p);u=den//p**d
    ck(vec(rec['integral'])==a and rec['denominator']==den,'full denominator')
    mask=integralcheck(rec['integral_class'],a,P,p)
    mask^=P['rational_prime_class']['mask'] if d%2 else 0
    mask^=2*ns(u,p)
    ck(rec['denominator_valuation']==d and rec['denominator_unit_residue']==u%p and rec['mask']==mask,'field denominator class')
    return mask


def paircheck(rec,q,b,P,p):
    mask=qcheck(rec['rational'],q,p)
    for i,pr in enumerate(P['primes']):mask|=fieldcheck(rec['quartic'][i],b,pr,p)<<(2*i+2)
    ck(rec['mask']==mask,'full product mask');return mask


def rank(columns):
    piv={}
    for x in columns:
        while x:
            k=(x&-x).bit_length()-1
            if k not in piv:piv[k]=x;break
            x^=piv[k]
    return len(piv)


def combo(cols,c):
    z=0
    for j,x in enumerate(cols):
        if c>>j&1:z^=x
    return z


def echeck(e,cols):
    ck(e['rank']==rank(cols),'independent rank')
    ker=e['kernel'];ck(rank(ker)==len(ker)==len(cols)-rank(cols),'complete kernel')
    ck(all(combo(cols,c)==0 for c in ker),'all kernel combinations')
    for j,t in enumerate(e['trace']):
        ck(t['input']==cols[j] and combo(cols,t['coefficients'])==t['reduced'],'all elimination trace identities')


def reduce(x,piv):
    for k in sorted(map(int,piv),reverse=True):
        if x>>k&1:x^=piv[str(k)][0]
    return x


def evaluate(poly,x):
    return obs(sum(Q(c)*x**j for j,c in enumerate(poly)))


def main():
    global T
    C=read('odd-membership-35-certificate.json')
    sources={n:read(n) for n in C['bindings']}
    ck(all(R['bindings'][n]==h for n,h in C['bindings'].items()),'all full source hashes')
    ck(sha256((ROOT/'odd_membership_35.py').read_bytes()).hexdigest()==C['source_sha256'],'producer binding')
    ck(sha256((ROOT/'quartic_parity_generate.py').read_bytes()).hexdigest()==C['helper_sha256'],'helper binding')
    base=sources['quartic-class-certificate.json'];two=sources['two-adic-filter-certificate.json']
    model=sources['odd-model-support-certificate.json'];T=base['order']['table']
    ck(T==C['table'],'entire table');M=C['model'];eta=vec(M['eta_O']);r=Q(M['r']);G=M['G'];H=M['H']
    ck(G==model['model']['G'] and H==model['model']['H'] and r==9075,'actual polynomials')
    B=[[Q(x) for x in row] for row in M['basis']]
    ck([sum(B[i][j]*eta[j] for j in range(4)) for i in range(4)]==vec(model['field']['eta_in_alpha']),'full eta order transport')
    oldcols=[w['old_quotient']|(w['dyadic_quotient']<<9) for w in two['witnesses']]
    echeck(C['old_conditions'],oldcols);ck(C['old_conditions']['rank']==5,'old rank')
    report={}
    for p in (3,5):
        P=C['places'][str(p)];primes=P['primes']
        ck([pr['source'] for pr in primes]==[pr for pr in base['generators'] if pr['p']==p],'complete prime list')
        for pr in primes:
            powers=pr['powers'];ck(len(powers)<=65,'depth cap')
            for n,lat in enumerate(powers):
                rows=lat['rows'];ck(abs(det(rows))==p**n==lat['norm'],'all ideal determinants')
                gens=([list(map(int,ONE))]+[[int(i==j) for i in range(4)] for j in range(1,4)]) if n==0 else (
                    pr['source']['lattice']['columns'] if n==1 else [times(vec(a),vec(b)) for a in powers[n-1]['rows'] for b in powers[1]['rows']])
                ck(all(member(rows,g) for g in gens),'full reverse ideal containment')
                ck(len(lat['forward'])==4,'forward size')
                for a,row in zip(lat['forward'],rows):
                    ck([sum(Q(c)*Q(g[k]) for c,g in zip(a,gens)) for k in range(4)]==vec(row),'forward ideal containment')
            pi=vec(pr['uniformizer'])
            ck(member(powers[1]['rows'],pi) and not member(powers[2]['rows'],pi),'uniformizer valuation exactly one')
            integralcheck(pr['rational_prime_class'],vec([p,0,0,0]),pr,p)
        ck(sum(pr['rational_prime_class']['valuation'] for pr in primes)==4,'total local degree')
        masks=[]
        branchb=plus(scale(ONE,r),scale(eta,-1));branchh=evaluate(H,r)
        for rec in P['samples']:
            x=Q(rec['X']);y2=evaluate(G,x)
            ck(y2==Q(rec['Y_squared']) and qcheck(rec['square_certificate'],y2,p)==0,'actual lifted local point')
            paircheck(rec['evaluation'],x-r,plus(scale(ONE,x),scale(eta,-1)),P,p)
        for rec in P['rejected']:
            x=Q(rec['X']);y2=evaluate(G,x)
            ck(y2==Q(rec['Y_squared']) and qcheck(rec['square_certificate'],y2,p)!=0,'all rejected square tests')
        for gen in P['generators']:
            if gen['type']=='rational_branch':
                mask=paircheck(gen['evaluation'],branchh,branchb,P,p)
            else:
                ck(gen['evaluation']==P['samples'][gen['sample']]['evaluation'],'authentic sample generator')
                mask=gen['evaluation']['mask']
            masks.append(mask)
        echeck(P['image'],masks)
        ck(rank(masks)==len(primes)==P['required_dimension'] and P['image_complete'],'dimension saturation')
        ck(P['tests']==len(P['samples'])+len(P['rejected'])<=200000,'actual versus test cap')
        for j,w in enumerate(P['witnesses']):
            src=two['witnesses'][j]['source'];ck(w['source']==src,'whole fixed witness source')
            q=Q(src['inverse_norm']);b=vec(src['coefficients'])
            norm=det([times(b,[Q(i==j) for i in range(4)]) for j in range(4)])
            ck(norm==Q(src['signed_norm']) and q*norm==1,'actual signed norm')
            mask=paircheck(w['evaluation'],q,b,P,p)
            ck(w['quotient']==reduce(mask,P['image']['pivots']),'all quotient columns')
        cols=[w['quotient'] for w in P['witnesses']]
        echeck(P['condition_on_old_kernel'],[combo(cols,c) for c in C['old_conditions']['kernel']])
        report[str(p)]=dict(actual_image_rank=rank(masks),required_image_rank=len(primes),tests=P['tests'],tests_cap=200000,max_ideal_depth=max(len(pr['powers'])-1 for pr in primes))
    allcols=[x|(C['places']['3']['witnesses'][j]['quotient']<<18)|(C['places']['5']['witnesses'][j]['quotient']<<24) for j,x in enumerate(oldcols)]
    echeck(C['all_conditions'],allcols)
    missing=[C['places']['3']['witnesses'][j]['quotient']|
             C['places']['5']['witnesses'][j]['quotient']<<6 for j in range(39)]
    restricted=[combo(missing,c) for c in C['old_conditions']['kernel']]
    echeck(C['combined_new_conditions'],restricted)
    for a in C['new_condition_witnesses']:
        ck(combo(oldcols,a['coefficients'])==0 and combo(missing,a['coefficients'])==a['quotient'],'actual old-space quotient witness')
    ck(rank([a['quotient'] for a in C['new_condition_witnesses']])==rank(restricted)==3,'three independent additional conditions')
    ck(C['result']['rank_upper_bound']==7-rank(restricted)==4,'rank deduction constants')
    detections=[w['real_mask']|(w['eleven_mask']<<5)|(w['local']['mask']<<9)|
        (C['places']['3']['witnesses'][j]['evaluation']['mask']<<18)|
        (C['places']['5']['witnesses'][j]['evaluation']['mask']<<24) for j,w in enumerate(two['witnesses'])]
    for a in C['selected_pair']:
        c=a['coefficients'];ck(combo(allcols,c)==0,'selected all-place membership')
        b=ONE[:];q=Q(1)
        for j,w in enumerate(two['witnesses']):
            if c>>j&1:b=times(b,vec(w['source']['coefficients']));q=obs(q*Q(w['source']['inverse_norm']))
        ck(b==vec(a['quartic_O']) and q==Q(a['rational']),'full selected representative')
        norm=det([times(b,[Q(i==j) for i in range(4)]) for j in range(4)])
        ck(q*norm==1,'selected exact norm root one')
        ck(combo(detections,c)==a['local_detection'],'selected entire local detection')
    ck(rank([a['local_detection'] for a in C['selected_pair']])==2,'selected pair globally independent by localization')
    ck(C['completed'] and not C['failures'],'producer completed')
    R.update(completed=True,places=report,old_coefficient_dimension=39-rank(oldcols),
             all_coefficient_dimension=39-rank(allcols),pair_masks=[a['coefficients'] for a in C['selected_pair']],
             selected_pair_independent=True,additional_condition_rank=rank(restricted),
             rank_bound_improvement=rank(restricted),rank_upper_bound=7-rank(restricted))


if __name__=='__main__':
    try:main()
    except Exception as e:R['failures'].append(dict(message=str(e),traceback=traceback.format_exc()))
    OUT.write_text(json.dumps(R,indent=2,default=str)+'\n')
    print(json.dumps({**R,'bindings':'saved in certificate','path':str(OUT)}))
    raise SystemExit(0 if R['completed'] else 1)
