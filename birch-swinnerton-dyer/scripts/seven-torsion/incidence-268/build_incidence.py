"""Single capped construction; whole monic quotient-fiber tower, exact Q arithmetic."""
from fractions import Fraction as Q
from pathlib import Path
import sys,json,time,signal,hashlib
R=Path(__file__).resolve().parent; U=R.parent
sys.path.insert(0,str(U)); import build_certificate as P
START=time.monotonic(); report={'passed':False,'phase':'inputs','checks':[],'failures':[],'required_seconds':180}
def encode(v):
    if isinstance(v,Q):return str(v)
    if isinstance(v,(list,tuple)):return [encode(a) for a in v]
    if isinstance(v,dict):return {str(k):encode(a) for k,a in v.items()}
    return v
def save(name,v):
    s=json.dumps(encode(v),separators=(',',':'))+'\n'
    assert sum(p.stat().st_size for p in R.rglob('*') if p.is_file())+len(s.encode())<=134217728,'128-MiB cap'
    with (R/name).open('x') as f:f.write(s)
def need(ok,label):
    if not ok:raise ValueError(label)
    report['checks'].append(label)
def phase(s):
    report['phase']=s
    print(s,flush=True)
def timeout(*_):raise TimeoutError('180-second construction cap')
signal.signal(signal.SIGALRM,timeout);signal.alarm(180)
try:
    paths={'point':'certificate.json','direction':'compressed-249/direction.json','quotient':'quotient-254/quotient.json','dual':'dual-263/dual.json'}
    inp={n:json.loads((U/p).read_text()) for n,p in paths.items()}
    old=inp['quotient'];dual=inp['dual'];point=inp['point']
    h=list(map(Q,old['h'])); dz=[Q(0)];do=[Q(1)]
    def da(a,b):return P.add(a,b)
    def dn(a):return P.scale(a,-1)
    def dm(a,b):return P.divmodq(P.mul(a,b),h)[1]
    def ds(a,c):return P.scale(a,c)
    def dp(p):return [P.trim(list(map(Q,a))) for a in p]
    k=dp(dual['k']);q=dp(old['q']);N=dp(old['x_numerator']);M=dp(old['y_multiplier_numerator'])
    def ring(z,o,add,neg,mul,mod):
        def tr(a):
            a=list(a)
            while len(a)>1 and a[-1]==z:a.pop()
            return a or [z]
        def plus(a,b):return tr([add(a[i] if i<len(a) else z,b[i] if i<len(b) else z) for i in range(max(len(a),len(b)))])
        def minus(a):return tr([neg(v) for v in a])
        def times(a,b):
            out=[z for _ in range(len(a)+len(b)-1)]
            for i,c in enumerate(a):
                if c!=z:
                    for j,d in enumerate(b):
                        if d!=z:out[i+j]=add(out[i+j],mul(c,d))
            for i in range(len(out)-1,len(mod)-2,-1):
                v=out[i]
                if v!=z:
                    for j,c in enumerate(mod[:-1]):
                        if c!=z:out[i-len(mod)+1+j]=add(out[i-len(mod)+1+j],neg(mul(v,c)))
            return tr(out[:len(mod)-1])
        return tr,plus,minus,times
    lz=[dz];lo=[do]
    lt,la,ln,lm=ring(dz,do,da,dn,dm,k)
    def lc(a):return [a]
    T=[dz,do]
    A=list(map(Q,old['target_a']));B=list(map(Q,old['target_b']))
    cp=lt([da(B,dn(k[0])),da(A,dn(k[1])),dn(k[2])])
    cpinv=dp(dual['curve_inverse'])
    need(lm(cp,cpinv)==lo,'full_dual_cubic_unit')
    # F=N-T q^2 is monic, in (D[T]/k)[X].
    def dxadd(a,b):
        return [da(a[i] if i<len(a) else dz,b[i] if i<len(b) else dz) for i in range(max(len(a),len(b)))]
    def dxmul(a,b):
        out=[dz for _ in range(len(a)+len(b)-1)]
        for i,c in enumerate(a):
            for j,d in enumerate(b):out[i+j]=da(out[i+j],dm(c,d))
        return out
    q2=dxmul(q,q)
    fib=[lt([N[i] if i<len(N) else dz,dn(q2[i]) if i<len(q2) else dz]) for i in range(max(len(N),len(q2)))]
    need(len(fib)==8 and fib[-1]==lo,'whole_degree_seven_monic_fiber')
    ez=[lz];eo=[lo]
    et,ea,en,em=ring(lz,lo,la,ln,lm,fib)
    def ec(a):return [a]
    def lift(p):return et([lc(a) for a in p])
    def ep(a,n):
        out=eo
        for _ in range(n):out=em(out,a)
        return out
    def esc(a,n):return et([[ds(c,n) for c in v] for v in a])
    def sub(a,b):return ea(a,en(b))
    def red(p):
        out=ez
        for c in reversed(p):out=ea(em(out,X),[c])
        return out
    X=[lz,lo];eq=lift(q);eN=red([lc(a) for a in N]);eM=red([lc(a) for a in M])
    c=lift([[Q(46224)],[Q(-3024)],dz,do])
    save('fiber.json',{'h':h,'k':k,'cprime':cp,'F':fib,'rational_basis':'Z^j T^i V^e X^r; j fastest, 0<=j<8, 0<=i<3, 0<=e<2, 0<=r<7','B_basis':['1','X','X^2','X^3','X^4','X^5','X^6'],'dimension_Q':336,'rank_B':7,'input_hashes':{n:hashlib.sha256((U/p).read_bytes()).hexdigest() for n,p in paths.items()}})
    phase('full quotient denominator inverse')
    # H=N_inverse mod q from the already audited kernel units.
    dq=q
    tr,ad,ne,mu=ring(dz,do,da,dn,dm,dq)
    H=[ds(a,Q(1,4)) for a in mu(dp(old['c_inverse_mod_q']),mu(dp(old['qprime_inverse_mod_q']),dp(old['qprime_inverse_mod_q'])))]
    NH=dxadd(dxmul(N,H),[[-Q(1)]])
    # Exact monic division (N H-1)/q.
    rem=list(NH);W=[dz]*max(1,len(rem)-len(q)+1)
    while len(rem)>=len(q):
        while len(rem)>1 and rem[-1]==dz:rem.pop()
        if len(rem)<len(q):break
        i=len(rem)-len(q);v=rem[-1];W[i]=v
        for j,a in enumerate(q):rem[i+j]=da(rem[i+j],dn(dm(v,a)))
        while len(rem)>1 and rem[-1]==dz:rem.pop()
    need(rem==[dz],'whole_N_inverse_exact_division')
    qi=sub(em(ec(T),em(eq,lift(H))),red([lc(a) for a in W]))
    need(em(eq,qi)==eo,'full_quotient_q_unit')
    save('q-unit.json',{'H':H,'W':W,'q_inverse':qi})
    phase('full y multiplier and separability units')
    cpI=ec(cpinv)
    qi3=ep(qi,3);qi6=em(qi3,qi3)
    Mi=em(em(em(c,eM),cpI),qi6)
    need(em(eM,Mi)==eo,'full_y_multiplier_unit')
    deriv=red([[ds(v,i) for v in fib[i]] for i in range(1,8)])
    di=em(eq,Mi)
    need(em(deriv,di)==eo,'full_fiber_derivative_unit')
    yfactor=em(ep(eq,3),Mi)
    need(em(ec(cp),em(yfactor,yfactor))==c,'full_source_curve_both_signs')
    need(em(yfactor,eM)==ep(eq,3),'whole_y_recovery_equation')
    need(sub(eN,em(ec(T),ep(eq,2)))==ez,'whole_x_projection_equation')
    save('units-and-y.json',{'M_inverse':Mi,'derivative_inverse':di,'y_V_factor':yfactor,'q_inverse':qi})
    phase('full source relations and point basis')
    f=list(map(Q,point['f']))
    fp=red([lc([v]) for v in f]);need(fp==ez,'entire_source_seven_division_polynomial')
    # Each incidence element is (even part, V times odd part), with E0 coefficients.
    def flat(a,b):
        return [((a if e==0 else b)[r][i][j] if r<len(a if e==0 else b) and i<len((a if e==0 else b)[r]) and j<len((a if e==0 else b)[r][i]) else Q(0)) for r in range(7) for e in range(2) for i in range(3) for j in range(8)]
    powers=[eo]
    for i in range(1,24):powers.append(em(powers[-1],X))
    std=[flat(p,ez) for p in powers]+[flat(ez,em(p,yfactor)) for p in powers]
    sourceM=[[Q(a) for a in row] for row in point['matrix']]
    sourceI=[[Q(a) for a in row] for row in point['inverse']]
    def transport(cols,mat):
        out=[]
        for j in range(48):
            v=[Q(0)]*336
            for i in range(48):
                a=mat[i][j]
                if a:
                    for n,b in enumerate(cols[i]):
                        if b:v[n]+=a*b
            out.append(v)
        return out
    phase('both complete 48-coordinate point transports')
    tp=transport(std,sourceM)
    need(transport(tp,sourceI)==std,'both_full_point_coordinate_transports')
    # B inclusion is the seven-basis constant component, all 48 columns.
    line=[]
    for e in range(2):
        for i in range(3):
            for j in range(8):
                v=[Q(0)]*336;v[e*24+i*8+j]=Q(1);line.append(v)
    save('pullbacks.json',{'point_standard_columns':std,'point_power_columns':tp,'line_columns':line,'point_original_x':flat(esc(sub(X,lift([[Q(12)]])),Q(1,36)),ez),'point_original_y':flat(lift([[-Q(1,2)]]),esc(yfactor,Q(1,216))),'full_ranks':{'point':48,'line':48},'point_rank_reason':'unital map from audited L067 field; full source relations checked','line_rank_reason':'distinct constant-X normal-form basis vectors','basis_transport':'successive monic normal forms; inverse is ordered flatten/unflatten'}})
    report.update(passed=True,phase='construction complete; independent replay required',dimension_Q=336,required_dimension_Q=336,rank_B=7,required_rank_B=7)
except Exception as e:report['failures']=[type(e).__name__+': '+str(e)]
finally:
    signal.alarm(0);report['seconds']=time.monotonic()-START;save('production-report.json',report)
print(json.dumps(report));sys.exit(0 if report['passed'] else 1)
