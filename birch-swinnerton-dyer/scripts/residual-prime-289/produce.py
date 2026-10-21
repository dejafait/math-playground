"""One bounded exact producer; ascending coefficient arrays throughout."""
import hashlib, json, math, random, signal, sys, time
from fractions import Fraction
from pathlib import Path

sys.set_int_max_str_digits(0)
ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
START = time.monotonic()
STATE = {'status': 'INCOMPLETE', 'phase': 'inputs', 'failures': []}
signal.signal(signal.SIGALRM, lambda *_: (_ for _ in ()).throw(TimeoutError('180_second_cap')))
signal.alarm(180)

def save(name, value):
    raw = (json.dumps(value, separators=(',', ':'))+'\n').encode()
    assert sum(f.stat().st_size for f in OUT.rglob('*') if f.is_file())+len(raw) <= 67108864
    with (OUT/name).open('xb') as f: f.write(raw)

def read(path):
    raw = (ROOT/path).read_bytes()
    INPUTS[path] = hashlib.sha256(raw).hexdigest()
    return json.loads(raw)

INPUTS = {}

def trim(a):
    while len(a)>1 and a[-1]==0: a.pop()
    return a
def add(a,b): return trim([((a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0))%P for i in range(max(len(a),len(b)))])
def scale(a,c): return trim([x*c%P for x in a])
def sub(a,b): return add(a,scale(b,-1))
def mul(a,b):
    r=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): r[i+j]=(r[i+j]+x*y)%P
    return trim(r)
def div(a,b):
    a=a[:]; q=[0]*max(1,len(a)-len(b)+1); u=pow(b[-1],-1,P)
    while a!=[0] and len(a)>=len(b):
        k=len(a)-len(b); c=a[-1]*u%P; q[k]=c
        for i,v in enumerate(b): a[k+i]=(a[k+i]-c*v)%P
        trim(a)
    return trim(q),a
def monic(a): return scale(a,pow(a[-1],-1,P))
def gcd(a,b):
    while b!=[0]: a,b=b,div(a,b)[1]
    return monic(a)
def egcd(a,b):
    u,v,s,t=[1],[0],[0],[1]
    while b!=[0]:
        q,r=div(a,b); a,b=b,r; u,s=s,sub(u,mul(q,s)); v,t=t,sub(v,mul(q,t))
    c=pow(a[-1],-1,P)
    return scale(a,c),scale(u,c),scale(v,c)
def power(a,n,f):
    r=div([1],f)[1]; a=div(a,f)[1]
    while n:
        if n&1: r=div(mul(r,a),f)[1]
        a=div(mul(a,a),f)[1]; n//=2
    return r
def exact(a,b):
    q,r=div(a,b); assert r==[0]; return q
RNG=random.Random(289)
def equal(f,d):
    if len(f)-1==d: return [f]
    while True:
        a=trim([RNG.randrange(P) for _ in range(len(f)-1)])
        g=gcd(f,sub(power(a,(P**d-1)//2,f),[1]))
        if 1<len(g)<len(f): return equal(g,d)+equal(exact(f,g),d)
def factor(f):
    f=monic(f)
    if len(f)==1: return []
    derivative=trim([i*f[i]%P for i in range(1,len(f))] or [0])
    if derivative==[0]:
        assert all(not x or i%P==0 for i,x in enumerate(f))
        return factor(f[::P])*P
    g=gcd(f,derivative)
    if len(g)>1: return factor(g)+factor(exact(f,g))
    result=[]; x=[0,1]; h=x; d=1
    while 2*d<=len(f)-1:
        h=power(h,P,f); g=gcd(f,sub(h,x))
        if len(g)>1:
            result+=equal(g,d); f=exact(f,g)
            if len(f)==1: return result
            h=div(h,f)[1]
        d+=1
    return result+[f]
def z_mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]+=x*y
    return c
def prime_divisors(n):
    return [q for q in range(2,n+1) if n%q==0 and all(q%d for d in range(2,math.isqrt(q)+1))]

def main():
    global P
    support=read('scripts/order-discriminant-support-286/certificate.json')
    discpath='scripts/seven-torsion/nonmonic-order-283/discriminant.json'
    disc=read(discpath)['order_discriminant']
    assert support['source']==discpath and support['source_sha256']==INPUTS[discpath]
    assert disc<0 and support['input_sign']==-1 and support['input_abs']==-disc
    r=-disc; reconstruction=1
    assert [v['prime'] for v in support['primes']]==[2,3,7,389]
    for row in support['primes']:
        p=row['prime']; assert all(p%d for d in range(2,math.isqrt(p)+1))
        assert row['prime_trial'] and row['exponent']==len(row['divisions'])
        for step in row['divisions']:
            q,s=divmod(r,p)
            assert step=={'before':r,'quotient':q,'remainder':s} and s==0
            r=q
        assert r==row['residual'] and r%p==row['terminal_remainder']!=0
        reconstruction*=p**row['exponent']
    assert r==support['cofactor']>1 and reconstruction*r==support['reconstruction']==-disc
    assert support['outcome']=='REFUTED' and all(support['replay'].values())
    basis=read('scripts/seven-torsion/nonmonic-order-283/basis.json')
    old=read('scripts/seven-torsion/certificate.json'); H=basis['H']
    assert basis['source_sha256']==INPUTS['scripts/seven-torsion/certificate.json']
    assert len(H)==49 and H[-1]==343 and H==old['primitive_integer_factors'][0]
    assert all(Fraction(a)==343*Fraction(b) for a,b in zip(H,old['h'])) and len(old['h'])==49
    assert math.gcd(*H)==1
    STATE['phase']='prime_search'
    sieve=[True]*10001; sieve[0]=sieve[1]=False
    for i in range(2,101):
        if sieve[i]:
            for j in range(i*i,10001,i): sieve[j]=False
    primes=[i for i in range(2,10001) if sieve[i]]
    assert primes==[i for i in range(2,10001) if all(i%d for d in range(2,math.isqrt(i)+1))]
    trials=[]; selected=None
    for p in primes:
        q,s=divmod(r,p); trials.append({'p':p,'q':q,'r':s})
        if s==0: selected=p; break
    certificate={'inputs':INPUTS,'bound':10000,'primes':primes,'residual':r,'trials':trials,'selected':selected,'H':H}
    save('selection.json',certificate)
    if selected is None:
        STATE.update(status='NO_DIVISOR',tested_bound=10000,prime_count=len(primes),gcd_degree=None)
        return
    P=selected; assert 343%P and P>2
    STATE.update(phase='factorization',selected=P)
    hb=trim([a%P for a in H]); factors=factor(hb)
    counts={}
    for f in factors: counts[tuple(f)]=counts.get(tuple(f),0)+1
    fac=[]; product=[343%P]; H1=[1]
    for ft,e in sorted(counts.items()):
        f=list(ft); n=len(f)-1; chain=[[0,1]]
        for _ in range(n): chain.append(power(chain[-1],P,f))
        assert chain[-1]==div([0,1],f)[1]
        witnesses=[]
        for ell in prime_divisors(n):
            a=sub(chain[n//ell],[0,1]); g,u,v=egcd(f,a); assert g==[1]
            witnesses.append({'ell':ell,'u':u,'v':v})
        fac.append({'f':f,'multiplicity':e,'frobenius':chain,'bezout':witnesses})
        H1=z_mul(H1,f)
        for _ in range(e): product=mul(product,f)
    assert product==hb
    H2=[343%P]
    for item in fac:
        for _ in range(item['multiplicity']-1): H2=z_mul(H2,item['f'])
    hp=z_mul(H1,H2); assert len(hp)==49
    delta=[hp[i]-H[i] for i in range(49)]; assert all(a%P==0 for a in delta)
    H3=[a//P for a in delta]; reductions=[trim([a%P for a in h]) for h in (H1,H2,H3)]
    a,b,c=reductions; d,u,v=egcd(a,b); G,s,t=egcd(d,c)
    coeff=[mul(s,u),mul(s,v),t]
    quotients=[exact(f,G) for f in reductions]
    assert add(add(mul(coeff[0],a),mul(coeff[1],b)),mul(coeff[2],c))==G
    save('dedekind.json',{'p':P,'factors':fac,'H1':H1,'H2':H2,'H3':H3,'degrees':[len(H1)-1,len(H2)-1,48],'reductions':reductions,'G':G,'quotients':quotients,'bezout':coeff,'verdict':'P_MAXIMAL' if G==[1] else 'NOT_P_MAXIMAL'})
    STATE.update(status='VERDICT',gcd_degree=len(G)-1,verdict='P_MAXIMAL' if G==[1] else 'NOT_P_MAXIMAL')

try:
    main()
except Exception as e:
    STATE.update(status='FAILED'); STATE['failures'].append(type(e).__name__+': '+str(e))
finally:
    signal.alarm(0); STATE['seconds']=time.monotonic()-START; STATE['inputs']=INPUTS
    save('producer-report.json',STATE)
    print(json.dumps({k:v for k,v in STATE.items() if k!='inputs'}))
