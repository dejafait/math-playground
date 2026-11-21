"""Fixed complete distant cross-column test. No old artifact is overwritten.

Directed arithmetic and elementary tails follow C744b/C744e's contracts.
Full per-component evidence is saved; finite decimals proposing a witness
are not trusted until the direct directed quadratic check.
"""
import hashlib
import json
import math
import runpy
from decimal import Decimal, localcontext
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE/'distant-469.json'
inputs = ['certify-455.py', 'refined-464.json', 'compression-463.json',
          'certificate-455.json']
snap = {name: (HERE/name).read_bytes() for name in inputs}
assert hashlib.sha256(snap['certify-455.py']).hexdigest() == '064e75d04fb24d0d3c47720652672166df78255f97a298170bffd8eb2b574afd'
lib = runpy.run_path(str(HERE/'certify-455.py'))
I, A, PI, ELL, UP = (lib[k] for k in ('I','A','PI','ELL','UP'))
sc = lib['sincos']
old = json.loads(snap['compression-463.json'])
core = json.loads(snap['refined-464.json'])
base = json.loads(snap['certificate-455.json'])
D, Q, N, K, DEG, END = 64, 4096, 65536, 32, 192, 2**180
sv = lambda x: I(x['lo'],x['hi'])
mag = lambda x: max(x.lo.copy_abs(),x.hi.copy_abs())
ji = lambda xs: [x.json() for x in xs]
sym = lambda x: I(x.hi.copy_negate(),x.hi)


def pw(x,n):
    y=I(1)
    while n:
        if n%2: y*=x
        x=x.sq()
        n//=2
    return y


report = {'status':'IN_PROGRESS','parameters':{'core':D,'distant_start':Q,
          'approved_prefix_end':16384,'penalty':256,'response_rational_prefix':N,
          'geometric_terms':K,'dyadic_degree':DEG},
          'input_sha256':{name:hashlib.sha256(data).hexdigest() for name,data in snap.items()},
          'checks':[],'failures':[]}


def check(name,truth):
    report['checks'].append({'name':name,'passed':bool(truth)})
    if not truth:
        report['failures'].append(name)
        OUT.write_text(json.dumps(report,indent=2)+'\n')
        raise AssertionError(name)


def save(): OUT.write_text(json.dumps(report,indent=2)+'\n')


check('accepted core status',core['status']=='CERTIFIED_POSITIVE_COMPLETE_COMPRESSION')
check('same a',core['parameters']['a']==A.json())
check('same dimension and penalty',core['parameters']['dimension']==64 and core['parameters']['penalty']==256)
k=[q*PI/A for q in range(D)]+[Q*PI/A]
u=[x.sq() for x in k]
norm=[(1/A).sqrt()]+[(2/A).sqrt()]*D
M=[[sv(x) for x in row] for row in core['complete_matrix']]
B=[[sv(x) for x in row] for row in core['congruence']['B']]

# All inverse even powers at the distant response cutoff. The exact centered
# moments, binomial polynomial, ratio remainder and final integral tail are
# those of C744e, now at N=65536. Every block and error is retained.
S={p:I(0) for p in range(2,2*K+3,2)}
blocks=[]
J=N
while J<END:
    moments=[J]
    for l in range(2,DEG+1,2):
        num=J**(l+1)-sum(math.comb(l+1,i)*moments[(l+1-i)//2]
                            for i in range(3,l+2,2))
        val,rem=divmod(num,l+1)
        check('exact centered moment J='+str(J)+' l='+str(l),rem==0 and val>=0)
        moments.append(val)
    C=I(6*J-1)/2
    rho=I(J-1)/C
    rp=pw(rho,DEG+1)
    den=I(1)
    normalized=[]
    for mom in moments:
        normalized.append(I(mom)/den)
        den*=C.sq()
    rec={'J':J,'powers':{}}
    for p in S:
        cp=pw(C.reciprocal(),p)
        value=cp*sum((math.comb(p+l-1,l)*normalized[l//2]
                         for l in range(0,DEG+1,2)),I(0))
        ratio=rho*I(p+DEG+1)/(DEG+2)
        check('binomial ratio '+str(J)+' '+str(p),ratio.hi<1)
        error=J*cp*math.comb(p+DEG,DEG+1)*rp/(1-ratio)
        enclosure=value+sym(error)
        S[p]+=enclosure
        rec['powers'][str(p)]={'polynomial':value.json(),'error':error.json(),'sum':enclosure.json()}
    blocks.append(rec)
    J*=2
final={}
for p in S:
    C=I(4*J+1)/2
    tail=pw(C.reciprocal(),p)+pw(C.reciprocal(),p-1)/(2*(p-1))
    S[p]+=I(0,tail.hi)
    final[str(p)]=tail.json()
report['distant_inverse_powers']={'blocks':blocks,'final_index':J,'final_tail':final,
                                'sums':{str(p):x.json() for p,x in S.items()}}
print('Distant inverse powers enclosed; full evidence saved.',flush=True)
save()

# T(u)=sum u/(c_j^2+u). Geometric remainder after K terms is bounded
# by u*(u/c_N^2)^K*S_2; denominator 1+u/c_j^2 >=1.
coreS={int(p):sv(x) for p,x in core['inverse_power_sums']['response'].items()}
T=[]
tdata=[]
for r in range(D+1):
    cutoff,sums=(512,coreS) if r<D else (N,S)
    val=I(0)
    for j in range(cutoff):
        c=I(4*j+1)/2
        val+=u[r]/(c.sq()+u[r])
    direct=val
    val+=sum((((-1)**m)*pw(u[r],m+1)*sums[2*m+2] for m in range(K)),I(0))
    ratio=u[r]/(I(4*cutoff+1)/2).sq()
    error=u[r]*pw(ratio,K)*sums[2]
    val+=sym(error)
    T.append(val)
    tdata.append({'label':r if r<D else Q,'direct':direct.json(),'cutoff':cutoff,
                  'ratio':ratio.json(),'error':error.json(),'T':val.json()})
report['T_values']=tdata
print('All 65 complete rational T values enclosed.',flush=True)
save()

# Restore exp(-2ac_j) for j<64 and bound every remaining term by
# exp(-2ac_64)*sum_(j>=64)c_j^-2, using the elementary integral bound.
response=[]
edata=[]
c64=I(257)/2
exp_tail=(-2*A*c64).exp()*(1/c64.sq()+1/(2*c64))
for r in range(D):
    rational=(T[-1]-T[r])/(u[-1]-u[r])
    correction=I(0)
    terms=[]
    for j in range(64):
        c=I(4*j+1)/2
        term=c.sq()*(-2*A*c).exp()/((c.sq()+u[r])*(c.sq()+u[-1]))
        correction+=term
        terms.append(term.json())
    f=rational-correction-I(0,exp_tail.hi)
    response.append(norm[r]*norm[-1]*((-1)**(r+Q))*f)
    edata.append({'r':r,'rational':rational.json(),'exponential_terms':terms,
                  'exponential_prefix':correction.json(),'F':f.json()})
report['response_data']={'entries':edata,'exponential_tail':exp_tail.json(),'column':ji(response)}

prime=[I(0) for _ in range(D)]
pdata=[]
for n,p,_ in lib['PRIMES']:
    delay=I(n).ln()
    half=A-delay/2
    weight=-2*I(p).ln()/I(n).sqrt()
    entries=[]
    for r in range(D):
        km,kp=(Q-r)*PI/A,(Q+r)*PI/A
        z=weight*norm[r]*norm[-1]/2*(
          sc(km*half)[0]/km*sc(kp*delay/2)[1]+
          sc(kp*half)[0]/kp*sc(km*delay/2)[1])
        entries.append(z)
        prime[r]+=z
    pdata.append({'n':n,'base_prime':p,'column':ji(entries)})
report['prime_components']=pdata
report['prime_column']=ji(prime)

moments=[]
penalty=[I(0) for _ in range(D)]
for row in old['all_ten_moment_rows']:
    cell,sigma=row['cell'],row['sigma']
    le,re=2*cell-5,2*cell-3
    sl,cl=sc(Q*le*PI/5)
    sr,cr=sc(Q*re*PI/5)
    beta=I(sigma)/2
    el,er=(-sigma*ELL/4).exp(),(sigma*ELL/4).exp()
    z=norm[-1]/I(2).sqrt()*(er*(beta*cr+k[-1]*sr)-el*(beta*cl+k[-1]*sl))/(beta.sq()+u[-1])
    for r in range(D): penalty[r]+=256*sv(row['row'][r])*z
    moments.append({'cell':cell,'sigma':sigma,'distant':z.json()})
report['physical_moments']=moments
report['penalty_column']=ji(penalty)
c=I(1)/2
rp=norm[-1]*((-1)**Q)*c/(c.sq()+u[-1])*(1-(-2*A*c).exp()).sqrt()
pole_q=rp*(A/2).exp()*(1-(-A).exp()).sqrt()
pole=[sv(x)*pole_q for x in old['pole_row']]
column=[prime[r]+penalty[r]+pole[r]+response[r] for r in range(D)]
report['pole_column']=ji(pole)
report['complete_column']=ji(column)
y=[sum((B[r][s]*column[s] for s in range(D)),I(0)) for r in range(D)]
report['B_column']=ji(y)
ynorm=sum((x.sq() for x in y),I(0))
floor=sv(base['complement_floors'][0]['floor'])
rho=sv(base['complement_floors'][0]['rho'])
ht,_,_=lib['h_interval'](k[-1])
t=ht-rho
report['weight']={'h':ht.json(),'rho':rho.json(),'t':t.json(),'accepted_floor':floor.json()}
report['transformed_column_norm_squared']=ynorm.json()
print('Complete q=4096: ||B c_q||^2 =',ynorm.json(),'; t_q =',t.json(),flush=True)

# Fix a rational x=B^T midpoint(Bc), scaled to max |x_i|=1 and rounded
# to 60 significant digits, then check its exact physical quadratic.
with localcontext() as ctx:
    ctx.prec=110
    mid=[(x.lo+x.hi)/2 for x in y]
    xp=[sum(B[r][s].lo*mid[r] for r in range(D)) for s in range(D)]
    scale=max(abs(z) for z in xp)
    xx=[format(z/scale,'.59E') for z in xp] if scale else ['0']*D
x=[I(z) for z in xx]
energy=sum(((1 if r==s else 2)*x[r]*x[s]*M[r][s]
           for r in range(D) for s in range(r,D)),I(0))
dot=sum((x[r]*column[r] for r in range(D)),I(0))
value=energy-dot.sq()/t
report['rational_direction']={'coefficients':xx,'core_energy':energy.json(),
                            'cross_dot':dot.json(),'prefix_comparison':value.json(),
                            'norm_squared':sum((z.sq() for z in x),I(0)).json()}
report['status']='CERTIFIED_NEGATIVE_PREFIX_DIRECTION' if value.hi<0 else 'ONE_COLUMN_INCONCLUSIVE'
if value.hi>=0: report['failures'].append('one-column direction does not certify negative complete comparison; full prefix and remainder unpaid')
report['script_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
check('old inputs preserved',all((HERE/name).read_bytes()==data for name,data in snap.items()))
save()
print('Result:',report['status'],'; comparison value',value.json(),'; required upper < 0')
print('Failures:',report['failures'],'; full certificate:',OUT)
