#!/usr/bin/env python3
"""Independent finite evidence for C998q audit703; no source is overwritten.

Analytic bounds and qualifications are canonical in C998q Section5.
The independent scalar evaluations use the retained Decimal/basic-operation
contracts. A separate formula reconstruction is a cross-check, not a new
unconditional validation of the runtime or of original source contracts.
"""
from pathlib import Path
from fractions import Fraction as F
from decimal import Decimal as D, localcontext, ROUND_CEILING
import hashlib
import json
import numpy as np

B = Path(__file__).resolve().parent
OUT = B/'shifted-band-audit-703.json'
source = B/'shifted-finite-band-701.py'
saved_path = B/'shifted-finite-band-701.json'
checks, failures = [], []
report = dict(result='INCOMPLETE', checks=checks, failures=failures,
              qualification='C998q retained source/core/operator/arithmetic contracts; no Gamma/E, S3 or RH conclusion.')

def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def ck(v, s):
    checks.append(dict(check=s, passed=bool(v)))
    if not v: raise AssertionError(s)
def f(x): return F.from_float(float(x))
def ratmat(a): return [[f(x) for x in row] for row in a]
def serialize(x):
    if isinstance(x, F): return str(x)
    if isinstance(x, D): return str(x)
    if isinstance(x, np.ndarray): return x.tolist()
    raise TypeError(type(x).__name__)
def exact_product(a, weights=None):
    # Independently accumulate integer-scaled columns, then lift to Fraction.
    aa=ratmat(a); ss=[max(t[j].denominator for t in aa) for j in range(3)]
    zz=[[int(t[j]*ss[j]) for j in range(3)] for t in aa]
    if weights is None:
        return [[F(sum(t[i]*t[j] for t in zz),ss[i]*ss[j]) for j in range(3)] for i in range(3)]
    ww=[f(x) for x in weights]; sd=max(t.denominator for t in ww)
    wi=[int(t*sd) for t in ww]
    return [[F(sum(t[i]*t[j]*w for t,w in zip(zz,wi)),ss[i]*ss[j]*sd) for j in range(3)] for i in range(3)]
def determinant(a):
    if len(a)==1: return a[0][0]
    return sum(((-1)**j*a[0][j]*determinant([r[:j]+r[j+1:] for r in a[1:]]) for j in range(len(a))),F(0))
def minors(a): return [determinant([r[:i] for r in a[:i]]) for i in [1,2,3]]
def sqnorm(a): return sum((f(x)**2 for x in a),F(0))
def upper(x):
    return F(x.quantize(D('1e-12'),rounding=ROUND_CEILING))
def fd(x): return D(x.numerator)/D(x.denominator)
def sqrtup(x): return upper(fd(x).sqrt()+D('1e-60'))

try:
    saved=json.loads(saved_path.read_text())
    preserved=[source,saved_path]+[B/n for n in saved['input_sha256']]
    before={p.name:digest(p) for p in preserved}
    report['input_sha256']=before
    ck(before[source.name]==saved['script_sha256'],'entire701 source hash')
    ck(all(before[n]==h for n,h in saved['input_sha256'].items()),'all original701 input hashes')
    ck(before['frozen-reference-proposal-652.npz']=='2b770a8a689a972ae487b9dd718e2e6d47b6769a5530e7fec244a102c5c317c6','frozen652 archive pin')
    body=source.read_text()
    old="OUT = B / 'shifted-finite-band-701.json'"
    ck(body.count(old)==1,'exactly one replay output substitution')
    body=body.replace(old,"OUT = B / 'shifted-finite-band-replay-703.json'")
    ns={'__file__':str(source),'__name__':'audit703_replay'}
    exec(compile(body,str(source),'exec'),ns)
    replay=json.loads((B/'shifted-finite-band-replay-703.json').read_text())
    ck(replay==saved,'complete replay equality including all530 assertions,1536 centers,512 weights and ledgers')
    ck(not replay['failures'] and replay['certified'],'replay certified under retained contracts')
    power_checks=[]
    for exponent in range(64):
        relative=abs(f(3.**(-exponent))*3**exponent-1)
        ck(relative<F(1,2**52),'exact current float-power relative error exponent'+str(exponent))
        power_checks.append(dict(exponent=exponent,relative_error=relative,required=F(1,2**52)))
    report['exact_float_power_checks']=power_checks

    with localcontext() as ctx:
        ctx.prec=100
        # Independent constants: Machin with alternating remainder <1e-110.
        def atan_series(t,N):
            return sum(((-1)**j*t**(2*j+1)/D(2*j+1) for j in range(N)),D(0))
        pi=16*atan_series(D(1)/5,100)-4*atan_series(D(1)/239,100)
        el=D(3).ln()/2; a=el/2
        kk=[D(n)*pi/el for n in range(1024)]
        nv=[(1/el).sqrt()]+[(2/el).sqrt()]*1023
        kn=np.array([float(t) for t in kk]); nu=np.array([float(t) for t in nv])
        signs=np.array([(-1)**n for n in range(1024)])
        witness=json.loads((B/'neutral-reference-rank-obstruction-640.json').read_text())['witness']
        ww=witness['integer_columns_by_row']
        ck(len(ww)==32 and all(len(t)==3 for t in ww),'all96 witness integers')
        X=np.zeros((2044,3)); X[witness['support_indices_zero_based']]=np.array(ww)/2**24
        with np.load(B/'frozen-reference-proposal-652.npz',allow_pickle=False) as z: Y=z['free_middle_dyadics'].copy()
        def completion(free):
            arr=[[D.from_float(float(t)) for t in row] for row in free]
            top=[]
            for p in [0,1]:
                top.append([-sum((nv[n]/nv[p]*(D('.25')+kk[p]**2)/(D('.25')+kk[n]**2)*arr[n-2][j]
                                 for n in range(2,len(arr)+2) if n%2==p),D(0)) for j in range(3)])
            full=top+arr
            rounded=np.array([[float(t) for t in row] for row in full])
            err=max(sum((abs(D.from_float(float(rounded[n,j]))-full[n][j]) for n in range(len(full))),D(0)) for j in range(3))
            ck(err<D('1e-12'),'complete neutral coefficient conversion L1 error <1e-12 at length'+str(len(full)))
            for j in range(3):
                for c in [D('.5'),D('-.5')]:
                    moment=sum((nv[n]*c*(D((-1)**n)*(c*el).exp()-1)/(c*c+kk[n]**2)*full[n][j] for n in range(len(full))),D(0))
                    ck(abs(moment)<D('1e-85'),'independent exact-formula neutral moment at length'+str(len(full))+' column'+str(j)+' sign'+str(c))
            return rounded
        ff,hh,qq=completion(X[:16]),completion(X[1022:1038]),completion(Y)
        ck(np.array_equal(ff,ns['f']) and np.array_equal(hh,ns['h']) and np.array_equal(qq,ns['q']),'all complete coefficients agree with independent100-digit formulas')

        # Independent trigonometry on reduced Decimal arguments. 45 Taylor
        # terms on [-pi/4,pi/4] give remainder <1e-145; roundoff <1e-90.
        def dsincos(x):
            q=int((x/(pi/2)).to_integral_value()); r=x-D(q)*pi/2
            si=ts=r; co=tc=D(1)
            for j in range(1,45):
                ts=-ts*r*r/D(2*j*(2*j+1)); tc=-tc*r*r/D((2*j-1)*2*j)
                si+=ts; co+=tc
            return [(si,co),(co,-si),(-si,-co),(-co,si)][q%4]
        # Direct complex-log formula evaluated entirely with Decimal; arctan
        # uses half-angle reduction six times and100 terms.
        def datan(t):
            inv=t>1
            if inv: t=1/t
            for _ in range(6): t=t/(1+(1+t*t).sqrt())
            v=64*atan_series(t,100)
            return pi/2-v if inv else v
        bv=[]
        for t in kk:
            y=t/2; aa=D('64.25')
            im=datan(y/aa)+y/(2*(aa*aa+y*y))
            im+=sum((y/((D(j)+D('.25'))**2+y*y) for j in range(64)),D(0))
            bv.append(float(t*im/2))
        bvec=np.array(bv); nr=kn[512:,None]; nc=kn[None,:256]
        diff=nr*nr-nc*nc
        sexp=np.zeros((512,256))
        for j in range(64):
            c=D(2*j)+D('.5'); factor=float((-el*c).exp()*c*c)
            sexp+=factor/((float(c*c)+nr*nr)*(float(c*c)+nc*nc))
        resp=((bvec[512:,None]-bvec[None,:256])/diff-signs[512:,None]*sexp)
        resp*=2*np.outer(nu[512:],nu[:256])*(signs[512:,None]==signs[None,:256])
        tmat=np.zeros((512,18)); tstar=tmat.copy()
        for primepower,prime in [(29,29),(31,31),(32,2),(37,37),(41,41),(43,43),(47,47),(49,7),(53,53),(59,59),(61,61),(64,2),(67,67),(71,71),(73,73),(79,79)]:
            dl=7*el-D(primepower).ln(); wt=float(D(prime).ln()/D(primepower).sqrt())
            for shift,ans in [(dl,tmat),(-dl,tstar)]:
                sn=np.array([float(dsincos(t*shift)[0]) for t in kk])
                sig=signs[512:,None]*signs[None,:18]
                num=(-sig*kn[512:,None]*sn[512:,None]+kn[None,:18]*sn[None,:18]) if shift>0 else (kn[512:,None]*sn[512:,None]-sig*kn[None,:18]*sn[None,:18])
                ans+=wt*num/(kn[512:,None]**2-kn[None,:18]**2)*np.outer(nu[512:],nu[:18])
        for j in range(1,8):
            c=D(2*j)+D('.5'); ev=float((-c*el).exp()); cc=float(c)
            minus=nu*cc*(1-signs*ev)/(cc*cc+kn*kn)
            plus=nu*cc*(signs-ev)/(cc*cc+kn*kn)
            pref=float((-6*c*el).exp())
            tmat+=pref*np.outer(minus[512:],plus[:18]); tstar+=pref*np.outer(plus[512:],minus[:18])
        report['original_entry_crosscheck_max_abs']={name:float(np.max(abs(arr-ns[key]))) for name,arr,key in [('S',resp,'S'),('T',tmat,'T'),('Tstar',tstar,'Ts')]}
        ck(all(t<1e-12 for t in report['original_entry_crosscheck_max_abs'].values()),'all149504 original entries independently reconstructed to1e-12')
        original=tmat@ff+tstar@hh-resp@qq

        service=[]
        def smooth(M):
            # Exact phases n*j*pi/(2M), avoiding old k*edge range reduction.
            table=np.array([float(dsincos(D(j)*pi/D(2*M))[0]) for j in range(4*M)])
            edges=np.arange(M+1,dtype=np.int64)
            def ints(indices):
                sin=table[(indices[:,None]*edges[None,:])%(4*M)]
                ans=np.diff(sin,axis=1)/np.where(indices[:,None]==0,1,kn[indices,None])
                if 0 in indices: ans[indices==0]=float(a/D(M))
                return ans*(np.sqrt(2)*nu[indices]*signs[indices])[:,None]
            inp=ints(np.arange(256)); out=ints(np.arange(512,1024))
            oldin=ns['integrals'](np.arange(256),M); oldout=ns['integrals'](np.arange(512,1024),M)
            imax=float(max(np.max(abs(inp-oldin)),np.max(abs(out-oldout))))
            ck(imax<1e-13,'all basis-cell integrals agree within1e-13 on mesh'+str(M))
            hv=[]
            for j in range(1,2*M):
                u=D(j)*a/D(M)
                hv.append(float((-u/2).exp()/(1-(-2*u).exp())-1/(2*u)))
            hv=np.array(hv); answer=np.zeros((512,3))
            for p in [0,1]:
                i=np.arange(p,256,2); o=np.arange(p,512,2)
                ci=inp[i].T@qq[i]; action=np.zeros_like(ci)
                for begin in range(0,M,64):
                    rr=np.arange(begin,min(M,begin+64))
                    action[rr]=hv[rr[:,None]+np.arange(M)[None,:]]@ci
                answer[o]=out[o]@action
            service.append(dict(mesh=M,basis_integrals_checked=768*M,max_abs_basis_difference=imax))
            return answer
        coarse=smooth(286); fine=smooth(4096)
        ecorr=np.zeros((512,3)); eterms=[]
        for l in range(14,80):
            c=D(2*l)+D('.5'); ex=(-c*a).exp(); b=ex*ex
            p=[]; z=[]
            for n in range(1024):
                sn=D([0,1,0,-1][n%4]); co=D([1,0,-1,0][n%4]); nn=D(2).sqrt()*nv[n]*D((-1)**n); k=kk[n]
                p.append(float(nn*(c+ex*(-c*co+k*sn))/(c*c+k*k)))
                z.append(float(nn*(ex*(c*co+k*sn)-b*c)/(c*c+k*k)))
            p=np.array(p);z=np.array(z);term=np.zeros((512,3))
            for parity,eps in [(0,1),(1,-1)]:
                i=np.arange(parity,256,2); o=np.arange(512+parity,1024,2)
                pv=p[i]@qq[i];zv=z[i]@qq[i]
                # Regroup independently: both orientations and all products.
                term[o-512]=(p[o,None]*(eps*float(b)*pv+eps*zv)+z[o,None]*(zv+eps*pv))/float(1-D(eps)*b)
            ecorr+=term; eterms.append(float(np.max(abs(term))))
        centers=original-coarse+fine+ecorr
        delta=centers-ns['center']
        report['independent_reconstruction']=dict(service=service,centers=centers.tolist(),
            every_center_difference=delta.tolist(),column_difference_L2=[float(np.linalg.norm(delta[:,j])) for j in range(3)],
            finite_E_term_max_abs=eterms)
        ck(all(sqnorm(delta[:,j])<F(1,10**20) for j in range(3)),'all1536 independent coefficient centers: column difference <1e-10')

        # Independent full moment projection and all512 weight intervals.
        gw=(el.exp()-1,el,1-(-el).exp()); det=gw[0]*gw[2]-gw[1]**2
        ck(det>D(1)/192,'moment Gram determinant >1/192')
        vv=[]; weight_intervals=[]
        for n in range(512,1024):
            moms=[nv[n]*c*(D((-1)**n)*(c*el).exp()-1)/(c*c+kk[n]**2) for c in [D('.5'),D('-.5')]]
            v=(gw[2]*moms[0]**2-2*gw[1]*moms[0]*moms[1]+gw[0]*moms[1]**2)/det
            vv.append(v)
            row_bound=F(saved['projection']['each_basis_projection_norm_upper'][n-512])
            ck(fd(row_bound)**2>v+D('1e-80'),'full projection summand bound row'+str(n))
            y=kk[n]/2; aa=D('64.25')
            hv=(aa*aa+y*y).ln()/2-aa/(2*(aa*aa+y*y))-pi.ln()-sum(((D(j)+D('.25'))/((D(j)+D('.25'))**2+y*y) for j in range(64)),D(0))
            er=D(2).sqrt()/(6*(aa*aa+y*y))+D('1e-70')
            low=1/D('.219999')-1/((hv-er)/2-D('.02'))-D('1e-70')
            high=1/D('.219999')-1/((hv+er)/2-D('.02'))+D('1e-70')
            wc=D.from_float(saved['weights']['centers_as_exact_binary64'][n-512]); rad=fd(F(saved['weights']['individual_absolute_error'][n-512]))
            ck(wc-rad<low<high<wc+rad and 4<low and high<5,'weight enclosure and(4,5) row'+str(n))
            weight_intervals.append([str(low),str(high)])
        trace=sum(vv,D(0)); pb=F(saved['projection']['ambient_Pband_PW_norm_upper'])
        ck(fd(pb)**2>trace+D('1e-70'),'entire projection trace dominated by saved rational p squared')
        report['projection_independent']=dict(trace=str(trace),norm=str(trace.sqrt()),bound=str(pb),all_summands=[str(v) for v in vv])
        report['weights_independent']=weight_intervals

        norms={}
        for name,arr in [('f',ff),('h',hh),('q',qq)]:
            norms['s'+name]=[sum((abs(f(t)) for t in arr[:,j]),F(0))+F(1,10**12) for j in range(3)]
            norms['n'+name]=[sqrtup(sqnorm(arr[:,j]))+F(1,10**12) for j in range(3)]
        ck({k:[str(t) for t in v] for k,v in norms.items()}==saved['coefficient_norm_upper'],'all18 rational norm upper values')
        eps=[]; rebuilt=[]
        for j in range(3):
            eo=F(181,10**9)*norms['nq'][j]+23*(F(1,10**7)*norms['sq'][j]+F(21,10**8)*(norms['sf'][j]+norms['sh'][j]))+F(1001,10**9)
            eh=F(2727,6553600)*norms['nq'][j]
            ee=18*F(2,3)**80*norms['nq'][j]
            gn=5*(norms['nf'][j]+norms['nh'][j])+45*norms['nq'][j]
            epsilon=eo+eh+ee+pb*gn+F(1,100000);eps.append(epsilon)
            terms=dict(column=j,original_entry_and_action_error=str(eo),smooth_quadrature_error=str(eh),E_suffix_error=str(ee),full_unprojected_norm_upper=str(gn),full_projection_error=str(pb*gn),new_arithmetic_error='1/100000',complete_band_error=str(epsilon))
            rebuilt.append(terms)
        ck(rebuilt==saved['error_ledger'],'all rational complete-error ledger terms')
        # Check new scalar ledger using a separately collected formula.
        smooth_bounds=[23*(24*M*(21*F(1,10**13)+F(3,M*10**12))+F(24,10**11)+12*M*F(1,10**13)+F(3,10**11)) for M in [286,4096]]
        new=sum(smooth_bounds,F(0))+F(23*66*5,10**10)+F(1,10**8)
        ck(new==F(saved['new_arithmetic_ledger']['entire_bound'])<F(1,100000),'independent new arithmetic rational sum and1e-5 limit')
        ck(all(t<F(1,200) for t in eps),'all complete errors <fixed1/200')
        eop=sqrtup(sum((t*t for t in eps),F(0)))
        ck(eop==F(saved['exact_PSD_certificate']['complete_operator_error_upper']),'full operator perturbation bound')

    A=np.array(saved['coefficients']['centers_as_exact_binary64'])
    G=exact_product(A); XG=exact_product(X); K=exact_product(A,saved['weights']['centers_as_exact_binary64'])
    def fm(a): return [[F(t) for t in row] for row in a]
    ck(G==fm(saved['matrix']['coefficient_center_gram']),'all9 exact center Gram entries')
    ck(XG==fm(saved['matrix']['XstarX']),'all9 exact full96-integer XstarX entries')
    ck(K==fm(saved['matrix']['K_center']),'all9 exact weighted Gram centers')
    with localcontext() as ctx:
        ctx.prec=100
        cn=[sqrtup(G[j][j])+F(1,10**12) for j in range(3)]
    radii=[[F(1,10**8)*cn[i]*cn[j]+5*(cn[i]*eps[j]+cn[j]*eps[i]+eps[i]*eps[j]) for j in range(3)] for i in range(3)]
    ck(radii==fm(saved['matrix']['K_entry_radius']),'all9 rational K-entry radii including correlations')
    s=F(1,125); Gshift=[[G[i][j]-(s*s if i==j else 0) for j in range(3)] for i in range(3)]
    gm=minors(Gshift); saving=4*(s-eop)**2
    M=[[saving*(i==j)-XG[i][j]/10**6 for j in range(3)] for i in range(3)]; mm=minors(M)
    ck(gm==[F(t) for t in saved['exact_PSD_certificate']['center_gram_shifted_leading_minors']] and all(t>0 for t in gm),'all3 exact shifted center Gram minors')
    ck(M==fm(saved['exact_PSD_certificate']['threshold_matrix']),'entire rational threshold matrix')
    ck(mm==[F(t) for t in saved['exact_PSD_certificate']['threshold_leading_minors']] and all(t>0 for t in mm),'all3 exact threshold minors')
    ck(s>eop and saving==F(saved['exact_PSD_certificate']['K_isotropic_lower']),'strict singular perturbation and exact isotropic saving')
    report['exact_evidence']=dict(center_gram=G,shifted_center_gram=Gshift,shifted_center_minors=gm,XstarX=XG,
        operator_error=eop,singular_lower=s,singular_margin=s-eop,saving=saving,threshold_matrix=M,threshold_minors=mm,
        K_center=K,K_radii=radii)
    report['bounds']=dict(column_errors=eps,required_column_error=F(1,200),new_arithmetic=new,required_new_arithmetic=F(1,100000),
        projection_norm_bound=pb,operator_error=eop,singular_lower=s,saving=saving,required_matrix_factor=F(1,10**6))
    ck(all(digest(p)==before[p.name] for p in preserved),'all701 and direct inputs preserved')
    report['result']='CONDITIONAL_C998q_FINITE_EVIDENCE_UPHELD'
except Exception as exc:
    failures.append(type(exc).__name__+': '+str(exc)); report['result']='AUDIT_INCOMPLETE_OR_FAILED'
report['audit_script_sha256']=digest(Path(__file__))
OUT.write_text(json.dumps(report,default=serialize,indent=2)+'\n')
print('Audit result:',report['result'],'; checks:',len(checks),'; failures:',failures)
if 'bounds' in report:
    print('Column errors:',[float(t) for t in eps],'; required <',float(F(1,200)))
    print('Operator error:',float(eop),'; singular lower:',float(s),'; isotropic saving:',float(saving))
print('Full audit certificate:',OUT.relative_to(B.parent.parent))
