"""Independent replay. Sparse polynomial dictionaries; no producer imports."""
import hashlib, json, math, signal, sys, time
from fractions import Fraction
from pathlib import Path
sys.set_int_max_str_digits(0)
R=Path(__file__).resolve().parent
ROOT=R.parents[1]
START=time.monotonic()
REPORT={'status':'INCOMPLETE','failures':[],'checks':0}
signal.signal(signal.SIGALRM,lambda *_: (_ for _ in ()).throw(TimeoutError('180_second_cap')))
signal.alarm(180)

def check(ok,name):
    if not ok: raise ArithmeticError(name)
    REPORT['checks']+=1
def read(p): return json.loads(p.read_bytes())
def digest(p):
    h=hashlib.sha256()
    with p.open('rb') as f:
        for b in iter(lambda:f.read(1048576),b''): h.update(b)
    return h.hexdigest()
def poly(a): return {i:x%P for i,x in enumerate(a) if x%P}
def plus(a,b):
    c=a.copy()
    for i,x in b.items():
        c[i]=(c.get(i,0)+x)%P
        if not c[i]: del c[i]
    return c
def times(a,b):
    c={}
    for i,x in a.items():
        for j,y in b.items(): c[i+j]=(c.get(i+j,0)+x*y)%P
    return {i:x for i,x in c.items() if x}
def remainder(a,b):
    c=a.copy(); n=max(b); inv=pow(b[n],-1,P)
    while c and max(c)>=n:
        k=max(c)-n; u=c[n+k]*inv%P
        for i,x in b.items():
            c[i+k]=(c.get(i+k,0)-u*x)%P
            if not c[i+k]: del c[i+k]
    return c
def exp(a,n,f):
    result=remainder({0:1},f); base=remainder(a,f)
    for bit in bin(n)[2:]:
        result=remainder(times(result,result),f)
        if bit=='1': result=remainder(times(result,base),f)
    return result
def prime(n): return n>=2 and all(n%d for d in range(2,math.isqrt(n)+1))

def main():
    global P
    sel=read(R/'selection.json'); prod=read(R/'producer-report.json')
    check(prod['status'] in ('NO_DIVISOR','VERDICT'),'producer_complete')
    before={p:digest(ROOT/p) for p in sel['inputs']}
    check(before==sel['inputs']==prod['inputs'],'all_original_hashes_before')
    c=read(ROOT/'scripts/order-discriminant-support-286/certificate.json')
    dpath='scripts/seven-torsion/nonmonic-order-283/discriminant.json'
    D=read(ROOT/dpath)['order_discriminant']; v=abs(D)
    check(D<0 and c['input_sign']==-1 and c['input_abs']==v,'signed_discriminant')
    check(c['source']==dpath and c['source_sha256']==before[dpath],'support_source')
    check([row['prime'] for row in c['primes']]==[2,3,7,389],'four_original_primes')
    reconstruction=1; divisions=0
    for row in c['primes']:
        p=row['prime']; check(prime(p) and row['prime_trial'],'original_prime')
        for step in row['divisions']:
            check(step['before']==v and step['remainder']==0 and v==p*step['quotient'],'complete_original_division')
            v=step['quotient']; divisions+=1
        check(row['residual']==v and v%p==row['terminal_remainder']!=0,'original_terminal')
        check(len(row['divisions'])==row['exponent'],'original_exponent')
        reconstruction*=p**row['exponent']
    check(v==c['cofactor']==sel['residual'] and v>1,'residual_matches')
    check(reconstruction*v==c['reconstruction']==-D and c['outcome']=='REFUTED' and all(c['replay'].values()),'complete_reconstruction')
    basis=read(ROOT/'scripts/seven-torsion/nonmonic-order-283/basis.json')
    oldpath='scripts/seven-torsion/certificate.json'; old=read(ROOT/oldpath)
    H=sel['H']
    check(basis['source_sha256']==before[oldpath],'L067_source_hash')
    check(H==basis['H']==old['primitive_integer_factors'][0] and len(H)==len(old['h'])==49,'all_H_coefficients')
    check(H[-1]==343 and math.gcd(*H)==1 and all(Fraction(a)==343*Fraction(b) for a,b in zip(H,old['h'])),'primitive_original_H')
    # Trial division of every integer establishes completeness independently of the sieve.
    primes=[i for i in range(2,10001) if prime(i)]
    check(sel['bound']==10000 and sel['primes']==primes,'complete_prime_list')
    found=None
    for i,row in enumerate(sel['trials']):
        p=primes[i]; check(row['p']==p and 0<=row['r']<p and v==row['q']*p+row['r'],'exact_search_division')
        if not row['r']:
            check(i==len(sel['trials'])-1,'stop_at_first_divisor'); found=p
    check(sel['selected']==found,'selected_matches')
    if found is None:
        check(len(sel['trials'])==len(primes) and prod['status']=='NO_DIVISOR','full_bounded_exclusion')
        REPORT.update(status='VERIFIED_NO_DIVISOR',tested_bound=10000,prime_count=len(primes),gcd_degree=None,original_divisions=divisions)
    else:
        P=found; check(P>2 and 343%P!=0 and prime(P),'selected_prime_and_leading_unit')
        cert=read(R/'dedekind.json'); check(cert['p']==P,'dedekind_prime')
        product={0:343%P}; distinct=[]; expected_H1=[1]; expected_H2=[343%P]
        def zmul(a,b):
            result=[0]*(len(a)+len(b)-1)
            for i,x in enumerate(a):
                for j,y in enumerate(b): result[i+j]+=x*y
            return result
        for item in cert['factors']:
            arr=item['f']; f=poly(arr); n=len(arr)-1; e=item['multiplicity']
            check(n>0 and arr[-1]==1 and e>0 and all(0<=x<P for x in arr),'factor_shape')
            check(arr not in distinct,'distinct_factors'); distinct.append(arr)
            chain=item['frobenius']; check(len(chain)==n+1 and chain[0]==[0,1],'full_frobenius_chain')
            for k in range(n): check(poly(chain[k+1])==exp(poly(chain[k]),P,f),'frobenius_step')
            check(poly(chain[-1])==remainder({1:1},f),'rabin_terminal')
            ds=[ell for ell in range(2,n+1) if n%ell==0 and prime(ell)]
            check([w['ell'] for w in item['bezout']]==ds,'all_rabin_prime_divisors')
            for w in item['bezout']:
                a=plus(poly(chain[n//w['ell']]),{1:P-1})
                check(plus(times(poly(w['u']),f),times(poly(w['v']),a))=={0:1},'rabin_bezout')
            for _ in range(e): product=times(product,f)
            expected_H1=zmul(expected_H1,arr)
            for _ in range(e-1): expected_H2=zmul(expected_H2,arr)
        check(product==poly(H),'full_factorization_with_leading_unit')
        check(cert['H1']==expected_H1 and cert['H2']==expected_H2,'all_integer_lifts')
        h1,h2,h3=cert['H1'],cert['H2'],cert['H3']; hp=zmul(h1,h2)
        check(len(hp)==len(h3)==49 and all(hp[i]-H[i]==P*h3[i] for i in range(49)),'full_integer_H3_identity')
        deg=[len(h1)-1,len(h2)-1,48]
        check(cert['degrees']==deg and sum(deg[:2])==48 and h1[-1]%P and h2[-1]%P and H[-1]%P,'homogeneous_degrees_no_infinity')
        polys=[poly(h) for h in (h1,h2,h3)]; G=poly(cert['G'])
        check(G and cert['G'][-1]==1 and [poly(a) for a in cert['reductions']]==polys,'reductions_and_monic_gcd')
        check(len(cert['quotients'])==len(cert['bezout'])==3,'full_gcd_witnesses')
        combined={}
        for f,q,b in zip(polys,cert['quotients'],cert['bezout']):
            check(times(G,poly(q))==f,'gcd_exact_division'); combined=plus(combined,times(poly(b),f))
        check(combined==G,'gcd_three_way_bezout')
        verdict='P_MAXIMAL' if G=={0:1} else 'NOT_P_MAXIMAL'
        check(cert['verdict']==prod['verdict']==verdict and prod['gcd_degree']==max(G),'verdict_matches')
        REPORT.update(status='VERIFIED_VERDICT',selected=P,gcd_degree=max(G),verdict=verdict,original_divisions=divisions)
    check({p:digest(ROOT/p) for p in before}==before,'all_original_hashes_after')
    REPORT['original_hashes']=before
    check(sum(p.stat().st_size for p in R.rglob('*') if p.is_file())<67108864,'aggregate_byte_cap')

try:
    main()
except Exception as e:
    REPORT['status']='FAILED'; REPORT['failures'].append(type(e).__name__+': '+str(e))
finally:
    signal.alarm(0); REPORT['seconds']=time.monotonic()-START
    with (R/'verification-report.json').open('x') as f: json.dump(REPORT,f)
    print(json.dumps({k:v for k,v in REPORT.items() if k!='original_hashes'}))
