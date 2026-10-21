"""One bounded exact specialization of the covered paired Vélu formulas."""
from fractions import Fraction as F
from pathlib import Path
import hashlib,json,signal,sys,time
R=Path(__file__).resolve().parent; U=R.parent
sys.path.insert(0,str(U))
import build_certificate as P

def main():
    start=time.monotonic(); signal.signal(signal.SIGALRM,lambda *_: (_ for _ in ()).throw(TimeoutError('180-second production cap')));signal.alarm(180)
    journal={'phase':'initialization','checks':[]}
    def save(name,v):
        data=json.dumps(P.encode(v),separators=(',',':'))+'\n'
        assert sum(p.stat().st_size for p in R.rglob('*') if p.is_file())+len(data.encode())<=134217728,'byte cap'
        with (R/name).open('x') as f:f.write(data)
    try:
        d=json.loads((U/'compressed-249/direction.json').read_text())
        h=list(map(F,d['h'])); q=[P.trim(list(map(F,p))) for p in d['cubic']]
        zero=[F(0)];one=[F(1)]
        def add(a,b):return P.add(a,b)
        def neg(a):return P.scale(a,-1)
        def mul(a,b):return P.divmodq(P.mul(a,b),h)[1]
        def scale(a,k):return P.scale(a,k)
        constant_inverses={}
        def inv(a):
            g,u,v=P.bezout(a,h);assert g==one,'nonunit constant'
            ans=P.divmodq(u,h)[1];assert mul(a,ans)==one
            constant_inverses[json.dumps(P.encode(a))]={'value':a,'inverse':ans}
            return ans
        def trim(p):
            p=list(p)
            while len(p)>1 and p[-1]==zero:p.pop()
            return p or [zero]
        def plus(p,r):return trim([add(p[i] if i<len(p) else zero,r[i] if i<len(r) else zero) for i in range(max(len(p),len(r)))])
        def minus(p,r):return plus(p,[neg(a) for a in r])
        def times(p,r):
            out=[zero for _ in range(len(p)+len(r)-1)]
            for i,a in enumerate(p):
                for j,b in enumerate(r):
                    if a!=zero and b!=zero:out[i+j]=add(out[i+j],mul(a,b))
            return trim(out)
        def sc(p,k):return trim([scale(a,k) for a in p])
        def derivative(p):return trim([scale(p[i],i) for i in range(1,len(p))])
        def division(p,r):
            out=[zero for _ in range(max(1,len(p)-len(r)+1))];p=list(p);ri=inv(r[-1])
            while p!=[zero] and len(p)>=len(r):
                k=len(p)-len(r);a=mul(p[-1],ri);out[k]=a
                p=minus(p,[zero]*k+[mul(a,b) for b in r])
            return trim(out),p
        def inverse_mod(p):
            a,b=q,p;v,w=[zero],[one]
            while b!=[zero]:
                quot,rem=division(a,b);a,b=b,rem;v,w=w,minus(v,times(quot,w))
            assert len(a)==1 and a[0]!=zero,'polynomial nonunit'
            return division([mul(z,inv(a[0])) for z in v],q)[1]
        x=[zero,one];a=F(-3024);b=F(46224);c=[[b],[a],zero,one]
        journal['phase']='quotient maps';s1=neg(q[2]);s2=add(mul(s1,s1),scale(q[1],-2))
        s3=add(add(mul(s1,s2),neg(mul(q[1],s1))),scale(q[0],-3))
        t=add(scale(s2,6),[6*a]);w=add(add(scale(s3,10),scale(s1,6*a)),[12*b])
        ap=add([a],scale(t,-5));bp=add([b],scale(w,-7))
        qp=derivative(q);qpp=derivative(qp);q2=times(q,q)
        N=plus(minus(times([scale(s1,-2),[F(7)]],q2),times([[2*a],zero,[F(6)]],times(qp,q))),sc(times(c,minus(times(qp,qp),times(q,qpp))),4))
        M=minus(times(derivative(N),q),sc(times(N,qp),2))
        journal['phase']='unit witnesses';invqp=inverse_mod(qp);invc=inverse_mod(c)
        disc=scale(add(scale(mul(mul(ap,ap),ap),4),scale(mul(bp,bp),27)),-16);invdisc=inv(disc)
        for k in [2,3,4,5,6,7,16]:inv([F(k)])
        save('quotient.json',{'schema':'389-direction-seven-quotient-v1','direction_sha256':hashlib.sha256((U/'compressed-249/direction.json').read_bytes()).hexdigest(),
             'h':h,'q':q,'source_a':a,'source_b':b,'target_a':ap,'target_b':bp,'x_numerator':N,'x_denominator':q2,
             'y_multiplier_numerator':M,'y_multiplier_denominator':times(q2,q),'qprime_inverse_mod_q':invqp,'c_inverse_mod_q':invc,
             'target_discriminant':disc,'target_discriminant_inverse':invdisc,'constant_inverses':list(constant_inverses.values()),
             'convention':'three inverse pairs; forward quotient; (N/q^2,Y M/q^3); short model only'})
        journal.update(passed=True,phase='complete',seconds=time.monotonic()-start,required_seconds=180,failures=[])
    except Exception as e:
        journal.update(passed=False,seconds=time.monotonic()-start,required_seconds=180,failures=[type(e).__name__+': '+str(e)])
    finally:
        signal.alarm(0);save('production-report.json',journal)
    print(json.dumps({k:v for k,v in journal.items() if k!='checks'}))
    return 0 if journal['passed'] else 1
if __name__=='__main__':sys.exit(main())
