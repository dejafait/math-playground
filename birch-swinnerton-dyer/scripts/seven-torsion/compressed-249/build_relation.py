"""One whole compressed-relation stage; never resumes old action columns."""
from fractions import Fraction as F
from pathlib import Path
import json,signal,sys,time
R=Path(__file__).resolve().parent;U=R.parent
sys.path.insert(0,str(U))
import build_certificate as P
t=time.monotonic()
report={'status':'IN_PROGRESS','stage':'whole_compressed_relation','columns':0,'required_columns':336,'seconds_cap':180,'byte_cap':128*1024*1024,'failures':[],'verified':False}
class Cap(Exception):pass
def alarm(s,f):raise Cap('180-second whole-stage arithmetic cap')
signal.signal(signal.SIGALRM,alarm);signal.alarm(180)
def enc(x):
    if isinstance(x,F):return str(x)
    if isinstance(x,list):return [enc(z) for z in x]
    if isinstance(x,dict):return {k:enc(v) for k,v in x.items()}
    return x
def save(name,c):
    s=json.dumps(enc(c),separators=(',',':'))+'\n'
    if sum(p.stat().st_size for p in R.rglob('*') if p.is_file())+len(s.encode())>128*1024*1024:raise Cap('128-MiB cumulative certificate cap')
    (R/name).write_text(s)
def journal():
    report['seconds']=time.monotonic()-t
    report['certificate_bytes']=sum(p.stat().st_size for p in R.rglob('*') if p.is_file())
    save('relation-feasibility.json',report)
def main():
    d=json.loads((R/'direction.json').read_text());a=json.loads((U/'certificate.json').read_text());old=json.loads((U/'incidence-247/ordered-pairs.json').read_text())
    f=list(map(F,a['f']));cubic=[F(46224),F(-3024),F(0),F(1)]
    zero=[F(0)];one=[F(1)];x=[F(0),F(1)]
    def red(v):return P.divmodq(v,f)[1]
    def cm(v,w):return red(P.mul(v,w))
    def ev(p,z):
        out=zero
        for v in reversed(p):out=P.add(cm(out,z),v)
        return out
    def ct(p):
        p=list(p)
        while len(p)>1 and p[-1]==zero:p.pop()
        return p
    def ca(p,q,sign=1):return ct([P.add(p[i] if i<len(p) else zero,P.scale(q[i] if i<len(q) else zero,sign)) for i in range(max(len(p),len(q)))])
    def pm(p,q):
        out=[zero]*(len(p)+len(q)-1)
        for i,v in enumerate(p):
            if v!=zero:
                for j,w in enumerate(q):
                    if w!=zero:out[i+j]=P.add(out[i+j],cm(v,w))
        return ct(out)
    g=[list(map(F,p)) for p in old['g']];n=21
    def kr(p):
        p=list(p)
        for k in range(len(p)-1,n-1,-1):
            if p[k]!=zero:
                for j in range(n):p[k-n+j]=P.sub(p[k-n+j],cm(p[k],g[j]))
        return ct(p[:n])
    def km(p,q):return kr(pm(p,q))
    ko=[one];kz=[zero];kx=[x];ku=[zero,one]
    def kev(p,z):
        out=kz
        for v in reversed(p):out=ca(km(out,z),[v])
        return out
    zp=list(map(F,d['z']));h=list(map(F,d['h']))
    h7=[zero]*8;h7[-1]=one
    for j in range(6,-1,-1):h7[j]=P.add([h[j+1]],cm(zp,h7[j+1]))
    assert P.add([h[0]],cm(zp,h7[0]))==zero
    assert ca(pm([P.scale(zp,-1),one],h7),[[v] for v in h],-1)==[zero]
    derivative=[F(i)*h[i] for i in range(1,9)]
    der=ev([[v] for v in derivative],zp)
    gcd,s,di=P.bezout(f,der);assert gcd==one
    di=red(di);assert cm(der,di)==one
    e0=[cm(v,di) for v in h7]
    # Complete cubic factor for the omitted direction, not selected roots.
    cd=[ev([[v] for v in pol],zp) for pol in [list(map(F,v)) for v in d['cubic']]]
    assert pm(cd,g)==[[v] for v in f]
    # Entire compressed pullback Z -> z(U), with all 21 C-coefficients.
    zq=kr([[v] for v in zp]);assert kev(h7,zq)==kz
    save('compressed-domain.json',{'h7':h7,'direction_P':zp,'direction_Q':zq,'omitted_cubic':cd,'derivative':der,'derivative_inverse':di,'omitted_idempotent':e0,'whole_ambient_dimension':384,'omitted_dimension':48,'required_D_dimension':336,'verified':False})
    report['domain_identities_produced']=True;journal()
    cX=[cubic];cU=[[v] for v in cubic]
    def sm(p,q):
        out=[kz,kz,kz,kz]
        for i,v in enumerate(p):
            if v!=kz:
                for j,w in enumerate(q):
                    if w==kz:continue
                    z=km(v,w)
                    if i&j&1:z=km(z,cX)
                    if i&j&2:z=km(z,cU)
                    out[i^j]=ca(out[i^j],z)
        return out
    def ss(p,q):return [ca(v,w,-1) for v,w in zip(p,q)]
    inv=[list(map(F,v)) for v in old['secant_inverse']]
    PX=[kx,kz,kz,kz];PY=[kz,ko,kz,kz];QX=[ku,kz,kz,kz]
    lam=[kz,[P.scale(v,-1) for v in inv],inv,kz]
    xx=ss(ss(sm(lam,lam),PX),QX)
    yy=ss(sm(lam,ss(PX,xx)),PY)
    xx3=sm(sm(xx,xx),xx);rhs=[ca(v,[[F(-3024)*w for w in p] for p in q]) for v,q in zip(xx3,xx)]
    rhs[0]=ca(rhs[0],[[F(46224)]])
    assert sm(yy,yy)==rhs
    save('new-translation-generators.json',{'X_sum':xx,'Y_sum':yy,'verified':False,'scope':'new exact group-law generator identities, producer checks only'})
    report['new_curve_identity_produced']=True;journal()
    # Columns of the two pullbacks D -> S, difference only. Not an automorphism of D.
    zpow=[ko]
    for j in range(6):zpow.append(km(zpow[-1],zq))
    xp=[ko,kz,kz,kz]
    outpath=R/'relation-columns.jsonl'
    with outpath.open('x') as out:
        for i in range(24):
            if i:xp=sm(xp,xx)
            for e in range(2):
                moved=xp if e==0 else sm(xp,yy)
                for j in range(7):
                    image=[km(v,zpow[j]) for v in moved]
                    base=[km([[F(0)]*i+[F(1)]],zpow[j]),kz,kz,kz]
                    if e:base=[kz,base[0],kz,kz]
                    diff=ss(image,base)
                    s=json.dumps({'input':[i,j,e],'difference':enc(diff)},separators=(',',':'))+'\n'
                    if sum(p.stat().st_size for p in R.rglob('*') if p.is_file())+len(s.encode())>128*1024*1024:raise Cap('128-MiB cumulative certificate cap')
                    out.write(s);out.flush();report['columns']+=1;journal()
            print('X exponent',i,'columns',report['columns'],flush=True)
    report['status']='RELATION_PRODUCED_UNVERIFIED';journal()
try:main()
except Cap as e:report['status']='STOP_COMPRESSED_STAGE_CAP';report['failures'].append(str(e))
except Exception as e:report['status']='STOP_CHECK_FAILURE';report['failures'].append(type(e).__name__+': '+str(e))
finally:
    signal.alarm(0);journal();print(json.dumps(report),flush=True)
