#!/usr/bin/env python3
"""Fixed known division-polynomial construction; exact Fraction arithmetic."""
from fractions import Fraction as Q
from pathlib import Path
import json
import time

ROOT = Path(__file__).resolve().parent

def trim(a):
    a = list(a)
    while len(a)>1 and a[-1]==0: a.pop()
    return a or [Q(0)]

def add(a,b):
    return trim([(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0)
                 for i in range(max(len(a),len(b)))])

def scale(a,c): return trim([v*c for v in a])
def sub(a,b): return add(a,scale(b,-1))

def mul(a,b):
    out=[Q(0)]*(len(a)+len(b)-1)
    for i,u in enumerate(a):
        if u:
            for j,v in enumerate(b):
                if v: out[i+j]+=u*v
    return trim(out)

def divmodq(a,b):
    a=trim(a); b=trim(b)
    if b==[0]: raise ZeroDivisionError
    out=[Q(0)]*max(1,len(a)-len(b)+1)
    while a!=[0] and len(a)>=len(b):
        k=len(a)-len(b); z=a[-1]/b[-1]; out[k]=z
        for j,v in enumerate(b): a[j+k]-=z*v
        a=trim(a)
    return trim(out),a

def bezout(a,b):
    r,s=a,b; u,v=[Q(1)],[Q(0)]; w,z=[Q(0)],[Q(1)]
    while s!=[0]:
        q,t=divmodq(r,s)
        r,s=s,t; u,v=v,sub(u,mul(q,v)); w,z=z,sub(w,mul(q,z))
    c=1/r[-1]
    return scale(r,c),scale(u,c),scale(w,c)

def inverse(m):
    n=len(m)
    a=[list(row)+[Q(int(i==j)) for j in range(n)] for i,row in enumerate(m)]
    for j in range(n):
        pivot=next((i for i in range(j,n) if a[i][j]),None)
        if pivot is None: return None
        a[j],a[pivot]=a[pivot],a[j]
        c=a[j][j]; a[j]=[v/c for v in a[j]]
        for i in range(n):
            if i!=j and a[i][j]:
                c=a[i][j]; a[i]=[u-c*v for u,v in zip(a[i],a[j])]
    return [r[n:] for r in a]

def mv(m,v): return [sum((a*b for a,b in zip(r,v)),Q(0)) for r in m]
def encode(a):
    if isinstance(a,Q): return str(a)
    if isinstance(a,list): return [encode(v) for v in a]
    if isinstance(a,dict): return {k:encode(v) for k,v in a.items()}
    return a

def mtrim(a):
    while len(a)>1 and a[-1]==0:a.pop()
    return a

def madd(a,b,p,sign=1):
    return mtrim([((a[i] if i<len(a) else 0)+sign*(b[i] if i<len(b) else 0))%p
                  for i in range(max(len(a),len(b)))])

def mdiv(a,b,p):
    a=a[:]; out=[0]*max(1,len(a)-len(b)+1)
    inv=pow(b[-1],-1,p)
    while a!=[0] and len(a)>=len(b):
        k=len(a)-len(b); c=a[-1]*inv%p; out[k]=c
        for j,v in enumerate(b):a[k+j]=(a[k+j]-c*v)%p
        mtrim(a)
    return mtrim(out),a

def mmul(a,b,p):
    out=[0]*(len(a)+len(b)-1)
    for i,u in enumerate(a):
        for j,v in enumerate(b):out[i+j]=(out[i+j]+u*v)%p
    return mtrim(out)

def mpow(a,k,h,p):
    out=[1]
    while k:
        if k&1:out=mdiv(mmul(out,a,p),h,p)[1]
        a=mdiv(mmul(a,a,p),h,p)[1]; k//=2
    return out

def mbez(a,b,p):
    r,s=a,b; u,v=[1],[0]; w,z=[0],[1]
    while s!=[0]:
        q,t=mdiv(r,s,p)
        r,s=s,t; u,v=v,madd(u,mmul(q,v,p),p,-1)
        w,z=z,madd(w,mmul(q,z,p),p,-1)
    c=pow(r[-1],-1,p)
    return tuple(mtrim([x*c%p for x in a]) for a in [r,u,w])

def prime(p): return p>=2 and all(p%d for d in range(2,int(p**.5)+1))

def modular_test(h,p):
    if any(c.denominator%p==0 for c in h):return {"prime":p,"excluded":"denominator"}
    f=[int(c.numerator*pow(c.denominator,-1,p)%p) for c in h]
    derivative=[i*f[i]%p for i in range(1,len(f))]
    g,u,v=mbez(f,mtrim(derivative),p)
    if len(g)>1:return {"prime":p,"squarefree":False,"gcd_degree":len(g)-1}
    seq=[[0,1]]
    for _ in range(48):seq.append(mpow(seq[-1],p,f,p))
    witnesses=[]
    for d in [16,24]:
        diff=madd(seq[d],[0,1],p,-1); g,u,v=mbez(f,diff,p)
        if g!=[1]:return {"prime":p,"squarefree":True,"failed_test":d,"gcd_degree":len(g)-1}
        witnesses.append({"index":d,"u":u,"v":v})
    if seq[48]!=[0,1]:return {"prime":p,"squarefree":True,"failed_test":48}
    return {"prime":p,"irreducible":True,"reduction":f,"frobenius":seq,
            "gcd_witnesses":witnesses}

def main():
    start=time.monotonic(); ROOT.mkdir(exist_ok=True)
    a=Q(-3024); b=Q(46224); cubic=[b,a,Q(0),Q(1)]
    psi3=[-a*a,12*b,6*a,Q(0),Q(3)]
    a4=[-a**3-8*b*b,-4*a*b,-5*a*a,20*b,5*a,Q(0),Q(1)]
    # psi2=2Y, psi4=4Y*a4; exact elimination of Y^2=cubic.
    psi5=sub(scale(mul(mul(cubic,cubic),a4),32),mul(mul(psi3,psi3),psi3))
    psi7=sub(mul(psi5,mul(mul(psi3,psi3),psi3)),
             scale(mul(mul(cubic,cubic),mul(mul(a4,a4),a4)),128))
    assert len(psi7)==25 and psi7[-1]==7
    f=scale(psi7,Q(1,7)); derivative=[i*f[i] for i in range(1,len(f))]
    g,u,v=bezout(f,derivative); assert g==[1]
    g,s,t=bezout(f,cubic); assert g==[1]
    print("division polynomial: degree 24; both rational gcds 1",flush=True)

    def red(z):return divmodq(z,f)[1]+[Q(0)]*(24-len(divmodq(z,f)[1]))
    def ringmul(z,w):
        z0,z1=z[:24],z[24:]; w0,w1=w[:24],w[24:]
        return red(add(mul(z0,w0),mul(cubic,mul(z1,w1))))+red(add(mul(z0,w1),mul(z1,w0)))
    one=[Q(1)]+[Q(0)]*47
    x=[Q(0),Q(1)]+[Q(0)]*46; y=[Q(0)]*24+[Q(1)]+[Q(0)]*23
    tests=[]
    for k in range(65):
        tt=[u+k*v for u,v in zip(y,x)]; powers=[one]
        for _ in range(48):powers.append(ringmul(powers[-1],tt))
        matrix=[list(r) for r in zip(*powers[:48])]
        inv=inverse(matrix)
        tests.append({"k":k,"invertible":inv is not None})
        print("separation k=",k,"full power basis:",inv is not None,flush=True)
        if inv is not None:break
    cert={"schema":"389-full-seven-v1","original_model":[0,1,1,-2,0],
          "short_a":a,"short_b":b,"transport":{"X":[12,36],"Y":[108,216]},
          "psi3":psi3,"psi4_over_4Y":a4,"psi5":psi5,"psi7":psi7,"f":f,
          "squarefree_bezout":{"u":u,"v":v},"cubic_bezout":{"u":s,"v":t},
          "separation_tests":tests,"k_cap":64,"prime_cap":200}
    # Avoid loop-variable shadowing of Bezout witnesses.
    _,uu,vv=bezout(f,derivative);cert["squarefree_bezout"]={"u":uu,"v":vv}
    if inv is None:
        cert["status"]="NO_POWER_BASIS_WITHIN_CAP"
    else:
        # Keep the zero coefficient of t^47; trimming before appending
        # the leading coefficient would change the polynomial degree.
        h=[-v for v in mv(inv,powers[48])]+[Q(1)]
        assert len(h)==49
        xp=mv(inv,x);yp=mv(inv,y)
        cert.update({"k":k,"matrix":matrix,"inverse":inv,"h":h,
                     "X_of_t":xp,"Y_of_t":yp,
                     "original_x_of_t":scale(sub(xp,[Q(12)]),Q(1,36)),
                     "original_y_of_t":scale(sub(yp,[Q(108)]),Q(1,216))})
        modtests=[]
        for p in range(2,201):
            if not prime(p):continue
            trial=modular_test(h,p);modtests.append(trial)
            print("modular prime",p, {q:v for q,v in trial.items() if q not in ["reduction","frobenius","gcd_witnesses"]},flush=True)
            if trial.get("irreducible"):break
        cert["modular_tests"]=modtests
        if modtests[-1].get("irreducible"):
            # One irreducible factor; product and CRT maps are identities.
            from math import lcm,gcd
            den=lcm(*(c.denominator for c in h)); integers=[int(c*den) for c in h]
            content=0
            for c in integers:content=gcd(content,abs(c))
            integers=[c//content for c in integers]
            cert.update({"status":"FIELD_CERTIFICATE_PRODUCED","factors":[h],
                "primitive_integer_factors":[integers],"factor_denominator":den//content,
                "product_maps":{"to_factors":[[Q(0),Q(1)]],"idempotents":[[Q(1)]]}})
        else:cert["status"]="FAITHFUL_ALGEBRA_ONLY_FIELD_UNCERTIFIED"
    path=ROOT/"certificate.json"
    path.write_text(json.dumps(encode(cert),separators=(",",":"))+"\n")
    print(json.dumps({"status":cert["status"],"dimension":48,"required_dimension":48,
                      "k":cert.get("k"),"caps":[64,200],"certificate":str(path),
                      "seconds":round(time.monotonic()-start,2)}))

if __name__=="__main__":main()
