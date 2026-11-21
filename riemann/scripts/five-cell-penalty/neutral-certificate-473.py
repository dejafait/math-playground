"""Directed fixed64+20 minimum-L2 graph test; never overwrites old evidence.

Exact consistency follows from reflection and positive definiteness of
the reduced5-row Gram, not from an interval-small numerical residual.
Full response sums use C744e's saved inverse powers and remainder method.
"""
import hashlib
import json
import runpy
from decimal import Decimal, localcontext
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE/'neutral-certificate-473.json'
names = ['certify-455.py', 'refined-464.json', 'compression-463.json']
raw = {n:(HERE/n).read_bytes() for n in names}
assert hashlib.sha256(raw['certify-455.py']).hexdigest() == '064e75d04fb24d0d3c47720652672166df78255f97a298170bffd8eb2b574afd'
lib = runpy.run_path(str(HERE/'certify-455.py'))
I,A,PI,ELL,UP = (lib[n] for n in ('I','A','PI','ELL','UP'))
sc = lib['sincos']
core = json.loads(raw['refined-464.json'])
old = json.loads(raw['compression-463.json'])
assert core['status'] == 'CERTIFIED_POSITIVE_COMPLETE_COMPRESSION'
assert core['parameters']['a'] == A.json()
D, D0, N, K = 84,64,512,32
sv = lambda x:I(x['lo'],x['hi'])
jm = lambda m:[[x.json() for x in row] for row in m]
sym = lambda x:I(x.hi.copy_negate(),x.hi)
mag = lambda x:max(x.lo.copy_abs(),x.hi.copy_abs())
report = {'status':'IN_PROGRESS', 'input_sha256':{n:hashlib.sha256(b).hexdigest() for n,b in raw.items()},
 'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'assessment':'drafts/literature/2026-11-11-five-cell-neutral-middle-correction-471.md',
 'ids':['L744','C744b','C744c','C744e'],
 'parameters':{'core':64,'reservoir':[64,83],'penalty':256,'threshold':'1/2','a':A.json(),
               'response_rational_prefix':N,'geometric_terms':K},'checks':[],'failures':[]}

def save(): OUT.write_text(json.dumps(report,indent=2)+'\n')
def check(name,truth):
    report['checks'].append({'name':name,'passed':bool(truth)})
    if not truth:
        report['failures'].append(name); save(); raise AssertionError(name)
def pw(x,n):
    y=I(1)
    while n:
        if n%2:y*=x
        x=x.sq(); n//=2
    return y
def mm(a,b):
    return [[sum((a[r][t]*b[t][s] for t in range(len(b))),I(0))
             for s in range(len(b[0]))] for r in range(len(a))]
def tr(a): return [list(x) for x in zip(*a)]

k = [q*PI/A for q in range(D)]
u = [x.sq() for x in k]
norm = [(1/A).sqrt()]+[(2/A).sqrt()]*(D-1)
full = [x/I(2).sqrt() for x in norm]
trig = {(q,e):sc(q*e*PI/5) for q in range(D) for e in (-5,-3,-1,1,3,5)}
C=[]
for cell in range(5):
    le,re=2*cell-5,2*cell-3
    for sigma in (1,-1):
        beta=I(sigma)/2
        el,er=(-sigma*ELL/4).exp(),(sigma*ELL/4).exp()
        row=[]
        for q in range(D):
            sl,cl=trig[q,le]; sr,cr=trig[q,re]
            row.append(full[q]*(er*(beta*cr+k[q]*sr)-el*(beta*cl+k[q]*sl))/(beta.sq()+u[q]))
        C.append(row)
check('all old ten moment entries replay exactly',
      all(C[j][q].json()==old['all_ten_moment_rows'][j]['row'][q] for j in range(10) for q in range(D0)))
reps=[0,1,2,3,4]
AA=[[C[j][q] for q in range(D0,D)] for j in reps]
C0=[[C[j][q] for q in range(D0)] for j in reps]
G=mm(AA,tr(AA))
L=[[I(0) for _ in range(5)] for _ in range(5)]; piv=[]
for j in range(5):
    p=G[j][j]-sum((L[j][t].sq()*piv[t] for t in range(j)),I(0))
    report['range_gram_partial_pivots']=[x.json() for x in piv]+[p.json()]
    check('positive restricted Gram pivot '+str(j),p.lo>0)
    piv.append(p); L[j][j]=I(1)
    for i in range(j+1,5):
        L[i][j]=(G[i][j]-sum((L[i][t]*L[j][t]*piv[t] for t in range(j)),I(0)))/p

def solve(rhs):
    z=[]
    for j in range(5):z.append(rhs[j]-sum((L[j][t]*z[t] for t in range(j)),I(0)))
    z=[z[j]/piv[j] for j in range(5)]
    for j in range(4,-1,-1):z[j]-=sum((L[t][j]*z[t] for t in range(j+1,5)),I(0))
    return z
Z=tr([solve([C0[j][q] for j in range(5)]) for q in range(D0)])
Y=[[-x for x in row] for row in mm(tr(AA),Z)]
Ginv=tr([solve([I(int(i==j)) for i in range(5)]) for j in range(5)])
inverse_bound=max(sum((I(mag(x)) for x in row),I(0)).hi for row in Ginv)
ynorm=sum((x.sq() for row in Y for x in row),I(0)).sqrt()
residual=mm(AA,Y)
for j in range(5):
    for q in range(D0):residual[j][q]+=C0[j][q]
report['range']={'representative_rows':reps,'all_ten_rows':jm(C),'restricted_gram':jm(G),
 'unit_lower':jm(L),'positive_pivots':[x.json() for x in piv],'gram_inverse':jm(Ginv),
 'inverse_operator_norm_upper':str(inverse_bound),'minimum_L2_map':jm(Y),
 'map_frobenius_norm':ynorm.json(),'enclosed_residual_not_exactness_proof':jm(residual),
 'exactness':'Even reflection pairs rows (j,sigma) and (4-j,-sigma). Five positive Gram pivots prove surjectivity onto all five representatives. Y=-A* (AA*)^-1 C0 gives all ten exact equations by algebra. Penrose minimum-norm theorem applies.'}
save()
print('Restricted rank:5/5 certified; exact10-row consistency follows by reflection.',flush=True)
print('Correction operator norm <= Frobenius bound',ynorm.hi,'; Gram inverse norm <=',inverse_bound,flush=True)

# Reuse the accepted complete core, evaluating all new entries with exactly
# the same scalar/inverse-power method. Every frequency through83 is kept.
S={int(p):sv(x) for p,x in core['inverse_power_sums']['response'].items()}
gamma=sv(core['gamma']); h0=-gamma-PI/2-3*I(2).ln()-PI.ln()
powers=[[pw(x,m) for m in range(K+1)] for x in u]
cN=I(4*N+1)/2
R=u[-1]/cN.sq()
check('new geometric ratio below1',R.hi<1)
h=[sv(x) for x in core['h']]; herr=[]
for q in range(D0,D):
    value=h0+sum((2*u[q]/((I(4*j+1)/2)*((I(4*j+1)/2).sq()+u[q])) for j in range(N)),I(0))
    value+=sum((2*((-1)**m)*powers[q][m+1]*S[2*m+3] for m in range(K)),I(0))
    error=2*u[q]*pw(u[q]/cN.sq(),K)*S[3]
    h.append(value+sym(error)); herr.append(error.json())
gram=[[I(0) for _ in range(D)] for _ in range(D)]
for r in range(D0):
    for s in range(D0):gram[r][s]=sv(core['response_gram'][r][s])
for j in range(N):
    c=I(4*j+1)/2
    row=[norm[q]*((-1)**q)*c/(c.sq()+u[q]) for q in range(D)]
    factor=1-(-2*A*c).exp()
    for r in range(D):
        for s in range(max(r,D0),D):gram[r][s]+=row[r]*row[s]*factor
    if j==0:pole_row=[x*(factor.sqrt())*(A/2).exp()*(1-(-A).exp()).sqrt() for x in row]
gerr=S[2]*(K+1)*pw(R,K)/(1-R).sq()
eerr=(-2*A*cN).exp()*S[2]
for r in range(D):
    for s in range(max(r,D0),D):
        value=I(0)
        for m in range(K):
            poly=sum((powers[r][t]*powers[s][m-t] for t in range(m+1)),I(0))
            value+=((-1)**m)*poly*S[2*m+2]
        gram[r][s]+=norm[r]*norm[s]*((-1)**(r+s))*(value+sym(gerr+eerr))
        gram[s][r]=gram[r][s]
print('Complete84-mode response/diagonal enclosures paid.',flush=True)
prime=[[I(0) for _ in range(D)] for _ in range(D)]; components=[]
for n,p,_ in lib['PRIMES']:
    delay=I(n).ln(); b=A-delay/2
    factors=[]; cosines=[]
    for t in range(2*D-1):
        freq=t*PI/A
        factors.append(b if t==0 else sc(freq*b)[0]/freq)
        cosines.append(sc(freq*delay/2)[1])
    weight=-2*I(p).ln()/I(n).sqrt()
    m=[[I(0) for _ in range(D)] for _ in range(D)]
    for r in range(D):
        for s in range(r,D):
            x,y=abs(r-s),r+s
            m[r][s]=weight*full[r]*full[s]*(factors[x]*cosines[y]+factors[y]*cosines[x])
            m[s][r]=m[r][s]; prime[r][s]+=m[r][s]; prime[s][r]=prime[r][s]
    components.append({'n':n,'base_prime':p,'matrix':jm(m)})
E=[[prime[r][s]+gram[r][s]+pole_row[r]*pole_row[s]+(h[r] if r==s else 0)
    for s in range(D)] for r in range(D)]
H=[[sv(x) for x in row] for row in core['complete_matrix']]
penalty=[[sum((256*C[j][r]*C[j][s] for j in range(10)),I(0)) for s in range(D0)] for r in range(D0)]
check('fresh complete core intersects accepted complete core',
      all(max((E[r][s]+penalty[r][s]).lo,H[r][s].lo)<=min((E[r][s]+penalty[r][s]).hi,H[r][s].hi)
          for r in range(D0) for s in range(D0)))
# Use accepted tight core intervals; all new complete mixed terms stay.
for r in range(D0):
    for s in range(D0):E[r][s]=H[r][s]-penalty[r][s]
cross=mm([row[D0:] for row in E[:D0]],Y)
yy=mm(tr(Y),mm([row[D0:] for row in E[D0:]],Y))
F=[[H[r][s]/2-penalty[r][s]+cross[r][s]+cross[s][r]+yy[r][s]
    for s in range(D0)] for r in range(D0)]
report['energy']={'h':[x.json() for x in h],'new_h_errors':herr,
 'response_gram':jm(gram),'response_ratio':R.json(),'response_error_before_normalization':gerr.json(),
 'response_exponential_error':eerr.json(),'nine_prime_components':components,'prime_matrix':jm(prime),
 'pole_row':[x.json() for x in pole_row],'complete_unpenalized_matrix':jm(E),
 'core_H':jm(H),'core_penalty':jm(penalty),'cross_E01Y':jm(cross),'reservoir_YE11Y':jm(yy),
 'half_energy_difference':jm(F)}
save()
print('Entire graph half-energy difference enclosed, including every mixed term.',flush=True)

# High-precision point LDL is a proposal only. A nonpositive pivot supplies
# an exact finite-decimal direction, checked against directed F below.
with localcontext() as ctx:
    ctx.prec=110
    point=[[(x.lo+x.hi)/2 for x in row] for row in F]
    low=[[Decimal(0) for _ in range(D0)] for _ in range(D0)]; dp=[]; bad=None
    for j in range(D0):
        p=point[j][j]-sum(low[j][t]**2*dp[t] for t in range(j))
        if p<=0:bad=j; break
        dp.append(p); low[j][j]=Decimal(1)
        for i in range(j+1,D0):
            low[i][j]=(point[i][j]-sum(low[i][t]*low[j][t]*dp[t] for t in range(j)))/p
    report['point_LDL_proposal']={'positive_pivots':[str(x) for x in dp],'first_nonpositive':bad,
                                  'warning':'not a certificate'}
    if bad is not None:
        v=[Decimal(0) for _ in range(D0)]; v[bad]=1
        for j in range(bad-1,-1,-1):v[j]=-sum(low[t][j]*v[t] for t in range(j+1,bad+1))
        scale=max(abs(x) for x in v)
        frozen=[format(x/scale,'.60E') for x in v]
        z=[I(x) for x in frozen]
        value=sum(((1 if r==s else 2)*z[r]*z[s]*F[r][s] for r in range(D0) for s in range(r,D0)),I(0))
        report['direction']={'exact_decimal_coefficients':frozen,'half_energy_difference':value.json(),
                             'norm_squared':sum((x.sq() for x in z),I(0)).json()}
        report['status']='CERTIFIED_NEGATIVE_HALF_ENERGY_DIRECTION' if value.hi<0 else 'INCONCLUSIVE'
        print('Proposed pivot',bad,'; directed difference',value.json(),'; required upper <0',flush=True)
    else:
        # Point positive factorization proposes a congruence, all of whose
        # entries are then frozen exact decimals and checked outward.
        root=[x.sqrt() for x in dp]
        chol=[[low[r][s]*root[s] for s in range(D0)] for r in range(D0)]
        b=[[Decimal(0) for _ in range(D0)] for _ in range(D0)]
        for i in range(D0):
            b[i][i]=1/chol[i][i]
            for j in range(i):b[i][j]=-sum(chol[i][t]*b[t][j] for t in range(j,i))/chol[i][i]
        B=[[I(format(x,'.64E')) if s<=r else I(0) for s,x in enumerate(row)] for r,row in enumerate(b)]
        BF=mm(B,F)
        residual=[[I(0) for _ in range(D0)] for _ in range(D0)]
        for r in range(D0):
            for s in range(r,D0):
                value=sum((BF[r][t]*B[s][t] for t in range(s+1)),I(0))-(1 if r==s else 0)
                residual[r][s]=value; residual[s][r]=value
        rows=[sum((I(mag(x)) for x in row),I(0)) for row in residual]
        bound=max(x.hi for x in rows)
        report['congruence']={'B':jm(B),'residual':jm(residual),'row_bounds':[x.json() for x in rows],
                              'operator_norm_upper':str(bound),'required':'<1'}
        report['status']='CERTIFIED_POSITIVE_HALF_ENERGY_GRAPH' if bound<1 else 'INCONCLUSIVE'
        print('Directed congruence residual norm <=',bound,'; required <1',flush=True)
if report['status']=='INCONCLUSIVE':report['failures'].append('half-energy sign not certified; no sign follows from point LDL or failed enclosure')
report['scope']='Fixed64+20 graph only. No middle complement, graph-distant, odd, neutral smooth-core, propagation or RH sign.'
save()
print('Result:',report['status'],'; failures:',report['failures'],'; full certificate:',OUT,flush=True)
