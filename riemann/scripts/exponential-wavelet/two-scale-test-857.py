"""Fixed approved test. Numerical diagnostic only until all errors are certified."""
import json, math, hashlib
from pathlib import Path
import numpy as np
from numpy.polynomial.legendre import leggauss

OUT=Path(__file__).with_suffix('.json')
T0=math.log(3)/16
L=4*math.log(3)
roots=(-.5,-.5,.5,.5)

def basic(y,a):
    y=np.asarray(y,dtype=np.longdouble)
    value=np.zeros_like(y)
    coeff=np.array([1,-4*np.cosh(a),4*np.cosh(a)**2+2,-4*np.cosh(a),1],dtype=np.longdouble)
    for j,c in enumerate(coeff):
        v=np.maximum(y-j,0)
        term=v**3/6
        total=term.copy()
        for k in range(1,14):
            term=term*((k+1)/k)*a*a*v*v/((2*k+2)*(2*k+3))
            total+=term
        value+=c*total
    return value

def construction(T):
    a=np.longdouble(T)/2
    nodes,weights=leggauss(32)
    corr=[]
    for k in range(4):
        val=np.longdouble(0)
        for j in range(k,4):
            y=j+(nodes.astype(np.longdouble)+1)/2
            val+=np.dot(weights.astype(np.longdouble),basic(y,a)*basic(y-k,a))/2
        corr.append(val)
    # A[k] normalized by norm of physical beta; the factor T cancels.
    auto={k:float(corr[abs(k)]/corr[0]) for k in range(-3,4)}
    h=np.array([1.])
    for root in roots:
        h=np.convolve(h,[1.,math.exp(T*root)])
    # Source G=-z H^*(-z^-1) A(-z); overall positive H scalar omitted.
    g={j:0. for j in range(-8,3)}
    for k,ak in auto.items():
        for ell,hl in enumerate(h):
            g[k-ell-1]+=-((-1.)**(k+ell))*ak*hl
    # One positive constant rescales the generator to unit L2 in the diagnostic.
    norm2=0.
    for j,gj in g.items():
        for k,gk in g.items():
            if abs(j-k)<=3: norm2+=gj*gk*auto[j-k]
    factor=math.sqrt(T*float(corr[0])*norm2)
    g={k:v/factor for k,v in g.items()}
    indices=[r for r in range(100) if 2*r-8>0 and (2*r+6)*T<L-1e-12]
    return {'T':T,'a':float(a),'auto':auto,'g':g,'indices':indices,'b_norm2_y':float(corr[0]),'raw_filter_norm2':norm2}

def fourier(t,c):
    T=c['T']
    z=t*T
    val=np.ones_like(t,dtype=np.complex128)*T
    for root in roots:
        s=T*root-1j*z
        val*=np.expm1(s)/s
    filt=sum(v*np.exp(-1j*z*k) for k,v in c['g'].items())
    return val*filt

def symbol(t):
    z=.25+.5j*t
    w=z+20
    bern=[1/6,-1/30,1/42,-1/30,5/66,-691/2730,7/6,-3617/510]
    value=np.log(w)-1/(2*w)
    for k,b in enumerate(bern,1):value-=b/(2*k*w**(2*k))
    for k in range(20):value-=1/(z+k)
    return value.real-math.log(math.pi)

def primepowers():
    out=[]
    for p in range(2,81):
        if any(p%d==0 for d in range(2,math.isqrt(p)+1)):continue
        n=p
        while n<81:
            out.append((n,p,math.log(p)/math.sqrt(n)))
            n*=p
    return sorted(out)

def run(order=20, panel=.1, cutoff=128):
    c=[construction(T0),construction(T0/2)]
    nodes,weights=leggauss(order)
    npan=math.ceil(cutoff/panel)
    h=cutoff/npan
    u=((np.arange(npan)[:,None]+.5)*h+nodes[None,:]*h/2).ravel()
    weights=np.broadcast_to(weights[None,:]*h/2,(npan,order)).ravel()/T0/math.pi
    t=u/T0
    pp=primepowers()
    m=symbol(t)-sum(2*w*np.cos(t*math.log(n)) for n,p,w in pp)
    transforms=[]
    for cc in c:
        f=fourier(t,cc)
        transforms.append(np.array([f*np.exp(-2j*t*cc['T']*r) for r in cc['indices']]).T)
    # Real generators: negative-frequency contribution is the conjugate.
    F=np.concatenate(transforms,axis=1)
    gram=(F.conj().T@((weights*m)[:,None]*F)).real
    gram=(gram+gram.T)/2
    n=len(c[0]['indices'])
    A,D,B=gram[:n,:n],gram[n:,n:],gram[:n,n:]
    ea,va=np.linalg.eigh(A);ed,vd=np.linalg.eigh(D)
    report={'claim_status':'UNVERIFIED NUMERICAL DIAGNOSTIC','parameters':{'T0':T0,'L':L,'order':order,'panel':h,'cutoff_u':cutoff,'quadrature_nodes':len(t)},'construction':c,'prime_powers':pp,'diagonal_eigenvalues':[ea.tolist(),ed.tolist()],'gram':gram.tolist(),'required_beta_upper':'strictly less than 1/2','failures':['No rigorous autocorrelation quadrature or floating-point enclosure','No rigorous full-Q quadrature and infinite-frequency tail enclosure','No verified matrix residual enclosure'],'source_assessment':'drafts/literature/2026-11-13-exponential-wavelet-two-scale-test-855.md'}
    if ea[0]>0 and ed[0]>0:
        cross=(va.T@B@vd)/np.sqrt(ea[:,None]*ed[None,:])
        s=np.linalg.svd(cross,compute_uv=False)
        report['beta_diagnostic']=float(s[0])
    report['script_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    OUT.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({'status':report['claim_status'],'dimensions':[n,len(c[1]['indices'])],'eigenvalue_min':[float(ea[0]),float(ed[0])],'beta':report.get('beta_diagnostic'),'required':'beta<0.5 and certified positive Q metrics','failures':report['failures'],'path':str(OUT)},indent=2))

if __name__=='__main__':run()
