"""BMSS fastElkies' fixed specialization, full direction field, bounded stage."""
from fractions import Fraction as F
from pathlib import Path
import sys,json,time,signal,hashlib
R=Path(__file__).resolve().parent; U=R.parent
sys.path.insert(0,str(U));import build_certificate as B
start=time.monotonic(); report={'phase':'initialization','passed':False,'required_seconds':180,'failures':[]}
def timeout(*_):raise TimeoutError('180-second production cap')
signal.signal(signal.SIGALRM,timeout);signal.alarm(180)
def save(name,obj):
    data=json.dumps(B.encode(obj),separators=(',',':'))+'\n'
    assert sum(p.stat().st_size for p in R.rglob('*') if p.is_file())+len(data.encode())<=134217728,'128 MiB cap'
    with (R/name).open('x') as f:f.write(data)
try:
    cert=json.loads((U/'quotient-254/quotient.json').read_text());h=list(map(F,cert['h']))
    z=[F(0)];o=[F(1)]
    def add(a,b):return B.add(a,b)
    def sub(a,b):return B.sub(a,b)
    def sc(a,k):return B.scale(a,k)
    def mul(a,b):return B.divmodq(B.mul(a,b),h)[1]
    units=[]
    def inv(a):
        g,u,_=B.bezout(a,h);assert g==o,'nonunit field coefficient';v=B.divmodq(u,h)[1]
        assert mul(a,v)==o;units.append({'value':a,'inverse':v});return v
    def trim(p):
        p=list(p)
        while len(p)>1 and p[-1]==z:p.pop()
        return p or [z]
    def pa(p,q):return trim([add(p[i] if i<len(p) else z,q[i] if i<len(q) else z) for i in range(max(len(p),len(q)))])
    def ps(p,q):return pa(p,[sc(a,-1) for a in q])
    def pc(p,k):return trim([sc(a,k) for a in p])
    def pm(p,q,n=None):
        size=len(p)+len(q)-1
        if n is not None:size=min(size,n)
        r=[z]*size
        for i,a in enumerate(p):
            if a!=z:
                for j,b in enumerate(q[:max(0,size-i)]):
                    if b!=z:r[i+j]=add(r[i+j],mul(a,b))
        return trim(r)
    def pw(p,k,n=None):
        r=[o]
        for _ in range(k):r=pm(r,p,n)
        return r
    def si(p,n):
        assert p[0]==o
        r=[o]
        for i in range(1,n):r.append(sc(sumfield([mul(p[j],r[i-j]) for j in range(1,min(i+1,len(p)))]),-1))
        return trim(r)
    def sumfield(v):
        r=z
        for a in v:r=add(r,a)
        return r
    def pd(p):return trim([sc(a,i) for i,a in enumerate(p) if i])
    def div(p,q):
        r=list(p);out=[z]*max(1,len(p)-len(q)+1);qi=inv(q[-1])
        while r!=[z] and len(r)>=len(q):
            i=len(r)-len(q);v=mul(r[-1],qi);out[i]=v;r=ps(r,[z]*i+[mul(v,a) for a in q])
        return trim(out),r
    def imod(p,q):
        a,b=q,p;u,v=[z],[o]
        while b!=[z]:
            d,r=div(a,b);a,b=b,r;u,v=v,ps(u,pm(d,v))
        assert len(a)==1 and a[0]!=z
        return div([mul(t,inv(a[0])) for t in u],q)[1]
    A=list(map(F,cert['target_a'])); BB=list(map(F,cert['target_b']))
    A2=[F(-3024*7**4)];B2=[F(46224*7**6)]
    # J: E -> E'' is (49 X,343 Y). J^*omega''=omega/7.
    assert sc([F(-3024)],7**6)==sc(A2,49) and sc([F(46224)],7**6)==B2
    normalization={'source_a':A,'source_b':BB,'normalized_target_a':A2,'normalized_target_b':B2,'J_x':49,'J_y':343,'J_differential':'1/7','J_inverse_x':'1/49','J_inverse_y':'1/343','actual_dual_differential':7}
    save('normalization.json',normalization)
    report['phase']='BMSS Newton series'
    T=[o,z,sc(sub(A2,A),F(1,10)),sc(sub(B2,BB),F(1,14))]
    C=si([o,z,A,BB],26);prec=4;iterates=[]
    while prec<26:
        n=min(2*prec,26);D=[sc(a,2*i+1) for i,a in enumerate(T)]
        p4=pw(T,4,n);p6=pw(T,6,n)
        G=pm(C,pa([o],pa([z,z]+[mul(A2,a) for a in p4],[z,z,z]+[mul(B2,a) for a in p6])),n)
        dG=pm(C,pa([z,z]+[sc(mul(A2,a),4) for a in pw(T,3,n)],[z,z,z]+[sc(mul(B2,a),6) for a in pw(T,5,n)]),n)
        Di=pc(si(D,n),F(1,2));aa=pm(dG,Di,n);bb=pm(ps(G,pm(D,D,n)),Di,n)
        W=[]
        for k in range(n):
            rhs=bb[k] if k<len(bb) else z
            for j in range(1,min(k+1,len(aa))):rhs=add(rhs,mul(aa[j],W[k-j]))
            W.append(sc(rhs,F(1,2*k+1)))
        T=pa(T,W)[:n];iterates.append({'precision_t':n,'T':T});prec=n
        save('newton-'+str(n)+'.json',iterates[-1])
    UU=si(pm(T,T,26),26)
    save('series.json',{'precision_S':52,'precision_T':26,'precision_U':26,'T':T,'U':UU,'newton':iterates})
    report['phase']='rational reconstruction'
    # Denominator d0=1. Coefficients 8,...,13 vanish after multiplication.
    mat=[[UU[k-j] if k-j<len(UU) else z for j in range(1,7)]+[sc(UU[k],-1)] for k in range(8,14)]
    for j in range(6):
        pivot=next(i for i in range(j,6) if mat[i][j]!=z);mat[j],mat[pivot]=mat[pivot],mat[j]
        ii=inv(mat[j][j]);mat[j]=[mul(a,ii) for a in mat[j]]
        for i in range(6):
            if i!=j and mat[i][j]!=z:
                v=mat[i][j];mat[i]=[sub(a,mul(v,b)) for a,b in zip(mat[i],mat[j])]
    den=[o]+[mat[i][-1] for i in range(6)];num=pm(den,UU,26)
    assert len(trim(num))<=8,'full 26-term Pade residual'
    root=[o]
    for k in range(1,4):root.append(sc(sub(den[k],sumfield([mul(root[i],root[k-i]) for i in range(1,k)])),F(1,2)))
    assert pm(root,root)==trim(den),'exact denominator square'
    kernel=list(reversed(root));assert kernel[-1]==o and len(kernel)==4
    save('reconstruction.json',{'numerator_reversed':num,'denominator_reversed':den,'square_root_reversed':root,'kernel':kernel,'bounds':[7,6],'unit_witnesses':units})
    report['phase']='kernel units and dual maps'
    k=kernel;kp=pd(k);kpp=pd(kp);k2=pm(k,k);k3=pm(k2,k)
    c=[BB,A,z,o];s1=sc(k[2],-1)
    N=pa(ps(pm([sc(s1,-2),[F(7)]],k2),pm([sc(A,2),z,[F(6)]],pm(kp,k))),pc(pm(c,ps(pm(kp,kp),pm(k,kpp))),4))
    M=ps(pm(pd(N),k),pc(pm(N,kp),2))
    iq=imod(kp,k);ic=imod(c,k)
    save('dual.json',{'schema':'389-dual-kernel-v1','h':h,'k':k,'normalized_N':N,'normalized_M':M,'k2':k2,'k3':k3,'x_divisor':49,'y_divisor':343,'kprime_inverse':iq,'curve_inverse':ic,'basis_D':['1','T','T^2','V','TV','T^2V'],'basis_Q':'Z^j T^i V^e; 0<=j<8,0<=i<3,0<=e<2','quotient_sha256':hashlib.sha256((U/'quotient-254/quotient.json').read_bytes()).hexdigest(),'unit_witnesses':units})
    report.update(passed=True,phase='production complete; independent verification required')
except Exception as e:report['failures']=[type(e).__name__+': '+str(e)]
finally:
    signal.alarm(0);report['seconds']=time.monotonic()-start;save('production-report.json',report)
print(json.dumps(report));sys.exit(0 if report['passed'] else 1)
