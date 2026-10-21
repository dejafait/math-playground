#!/usr/bin/env python3
"""Independent exact replay. No import of build_certificate or its helpers."""
import argparse
from fractions import Fraction
from pathlib import Path
import hashlib
import json
import math
import time

F=Fraction
COUNTS={}

def require(ok,label):
    if not ok:raise ValueError(label)
    COUNTS[label]=True

def clean(p):
    p=list(p)
    while p and p[-1]==0:p.pop()
    return p

def plus(p,q,sign=1):
    out=[F(0)]*max(len(p),len(q))
    for i,c in enumerate(p):out[i]+=c
    for i,c in enumerate(q):out[i]+=sign*c
    return clean(out)

def times(p,q):
    out=[F(0)]*max(0,len(p)+len(q)-1)
    for i,c in enumerate(p):
        for j,d in enumerate(q):
            if c and d:out[i+j]+=c*d
    return clean(out)

def scalar(p,c):return clean([c*v for v in p])

def remainder(p,q):
    out=list(p)
    for i in range(len(out)-1,len(q)-2,-1):
        z=out[i]/q[-1]
        if z:
            for j,v in enumerate(q):out[i-len(q)+1+j]-=z*v
    return clean(out[:len(q)-1])

def evalmod(p,z,mod):
    r=[]
    for c in reversed(p):r=remainder(plus(times(r,z),[c]),mod)
    return r

def readpoly(v):return [F(c) for c in v]
def fixed(p,n):return p+[F(0)]*(n-len(p))

# A bivariate dictionary, reduced only by Y^2=X^3+aX+b. This does
# not use the division polynomial or the 48-dimensional power matrix.
def bpadd(p,q,sgn=1):
    r=p.copy()
    for ij,c in q.items():r[ij]=r.get(ij,F(0))+sgn*c
    return {ij:c for ij,c in r.items() if c}

def bpmul(p,q):
    r={}
    for (i,j),c in p.items():
        for (k,l),d in q.items():r[i+k,j+l]=r.get((i+k,j+l),F(0))+c*d
    return {ij:c for ij,c in r.items() if c}

def bppow(p,n):
    r={(0,0):F(1)}
    for _ in range(n):r=bpmul(r,p)
    return r

def bpnormalize(p,a,b):
    r={}
    cubic={(3,0):F(1),(1,0):a,(0,0):b}
    for (i,j),c in p.items():
        r=bpadd(r,bpmul({(i,j%2):c},bppow(cubic,j//2)))
    return r

def asbp(p):return {(i,0):v for i,v in enumerate(p) if v}
def bpscale(p,c):return {ij:v*c for ij,v in p.items() if v*c}

def modreduce(a,h,p):
    a=[int(c)%p for c in a]
    for i in range(len(a)-1,len(h)-2,-1):
        c=a[i]*pow(h[-1],-1,p)%p
        for j,v in enumerate(h):a[i-len(h)+1+j]=(a[i-len(h)+1+j]-c*v)%p
    return [int(c) for c in clean(a[:len(h)-1])]

def modmul(a,b,p):
    out=[0]*max(0,len(a)+len(b)-1)
    for i,c in enumerate(a):
        for j,d in enumerate(b):out[i+j]=(out[i+j]+c*d)%p
    return [int(c) for c in clean(out)]

def modadd(a,b,p,sgn=1):return modclean(plus(a,b,sgn),p)

def modclean(a,p):return [int(c) for c in clean([int(c)%p for c in a])]

def modgcd(a,b,p):
    while b:a,b=b,modreduce(a,b,p)
    return [(c*pow(a[-1],-1,p))%p for c in a] if a else []

def run(cert):
    required=["schema","original_model","short_a","short_b","transport",
        "psi3","psi4_over_4Y","psi5","psi7","f","squarefree_bezout",
        "cubic_bezout","separation_tests","k_cap","prime_cap","k","matrix",
        "inverse","h","X_of_t","Y_of_t","original_x_of_t","original_y_of_t",
        "modular_tests","status","factors","primitive_integer_factors",
        "factor_denominator","product_maps"]
    require(all(k in cert for k in required),"required_fields")
    require(cert["schema"]=="389-full-seven-v1","schema")
    require(cert["original_model"]==[0,1,1,-2,0],"original_model")
    a,b=F(cert["short_a"]),F(cert["short_b"])
    require((a,b)==(-3024,46224),"short_coefficients")
    require(cert["transport"]=={"X":[12,36],"Y":[108,216]},"transport_coefficients")
    x={(1,0):F(1)};y={(0,1):F(1)};one={(0,0):F(1)}
    X=bpadd(bpscale(x,36),bpscale(one,12));Y=bpadd(bpscale(y,216),bpscale(one,108))
    lhs=bpadd(bpadd(bpadd(bppow(Y,2),bppow(X,3),-1),bpscale(X,a),-1),bpscale(one,b),-1)
    orig=bpadd(bpadd(bpadd(bpadd(bppow(y,2),y),bppow(x,3),-1),bppow(x,2),-1),bpscale(x,2))
    require(lhs==bpscale(orig,46656),"forward_equation_identity")
    ix=bpadd(bpscale(X,F(1,36)),bpscale(one,F(-1,3)))
    iy=bpadd(bpscale(Y,F(1,216)),bpscale(one,F(-1,2)))
    require(ix==x and iy==y,"inverse_substitution_identity")
    # Independent invariants for the original nonsingular model.
    require(112**3-(-856)**2==1728*389 and 389!=0,"nonsingularity")
    cubic=[b,a,F(0),F(1)]
    p3=[-a*a,12*b,6*a,F(0),F(3)]
    p4=[-a**3-8*b*b,-4*a*b,-5*a*a,20*b,5*a,F(0),F(1)]
    require(readpoly(cert["psi3"])==p3,"psi3_all_coefficients")
    require(readpoly(cert["psi4_over_4Y"])==p4,"psi4_all_coefficients")
    psi2={(0,1):F(2)};psi4=bpmul({(0,1):F(4)},asbp(p4))
    p5=bpnormalize(bpadd(bpmul(psi4,bppow(psi2,3)),bppow(asbp(p3),3),-1),a,b)
    require(p5==asbp(readpoly(cert["psi5"])),"psi5_odd_recurrence")
    p7=bpnormalize(bpadd(bpmul(p5,bppow(asbp(p3),3)),bpmul(psi2,bppow(psi4,3)),-1),a,b)
    psi7=readpoly(cert["psi7"]); f=readpoly(cert["f"])
    require(p7==asbp(psi7),"psi7_odd_recurrence")
    require(len(psi7)==25 and psi7[-1]==7 and scalar(f,7)==psi7,"degree24_exact_monic_division")
    derivative=[i*f[i] for i in range(1,25)]
    for label,rhs in [("squarefree",derivative),("cubic",cubic)]:
        data=cert[label+"_bezout"]
        value=plus(times(readpoly(data["u"]),f),times(readpoly(data["v"]),rhs))
        require(value==[1],label+"_complete_bezout")
    require(cert["k_cap"]==64 and cert["prime_cap"]==200,"caps")
    k=cert["k"]
    require(isinstance(k,int) and 0<=k<=64,"separating_parameter_bound")
    # This fixed production stops at the first candidate; no unverified
    # earlier singular-matrix labels are accepted.
    require(k==0 and cert["separation_tests"]==[{"k":0,"invertible":True}],"first_candidate")
    matrix=[[F(c) for c in row] for row in cert["matrix"]]
    inv=[[F(c) for c in row] for row in cert["inverse"]]
    require(len(matrix)==len(inv)==48 and all(len(r)==48 for r in matrix+inv),"full_matrix_shapes")
    for name,left,right in [("MN",matrix,inv),("NM",inv,matrix)]:
        for i in range(48):
            for j in range(48):
                total=sum((left[i][z]*right[z][j] for z in range(48) if left[i][z] and right[z][j]),F(0))
                require(total==int(i==j),f"inverse_{name}_{i}_{j}")
    print("transport, all division coefficients, Bezout identities and 4608 matrix entries passed",flush=True)

    def ring_product(v,w):
        # Distinct sparse monomial assembly, followed by independent
        # sequential reductions Y^2=cubic and monic f(X)=0.
        raw={}
        for i,c in enumerate(v):
            if not c:continue
            for j,d in enumerate(w):
                if d:
                    key=(i%24+j%24,i//24+j//24)
                    raw[key]=raw.get(key,F(0))+c*d
        normalized=bpnormalize(raw,a,b)
        parts=[]
        for parity in [0,1]:
            maxdegree=max((i for (i,j) in normalized if j==parity),default=-1)
            pol=[normalized.get((i,parity),F(0)) for i in range(maxdegree+1)]
            parts+=fixed(remainder(pol,f),24)
        return parts

    onevec=[F(1)]+[F(0)]*47
    xv=[F(0),F(1)]+[F(0)]*46;yv=[F(0)]*24+[F(1)]+[F(0)]*23
    tv=[u+k*v for u,v in zip(yv,xv)]; power=onevec; powers=[]
    for j in range(49):
        powers.append(power)
        if j<48:require([matrix[i][j] for i in range(48)]==power,f"power_column_{j}")
        power=ring_product(power,tv)
    h=readpoly(cert["h"])
    require(len(h)==49 and h[-1]==1,"h_monic_degree48")
    require(all(sum((h[j]*powers[j][i] for j in range(49)),F(0))==0 for i in range(48)),"h_annihilation_all_coordinates")
    xp=readpoly(cert["X_of_t"]);yp=readpoly(cert["Y_of_t"])
    require(len(xp)==len(yp)==48,"coordinate_map_lengths")
    for label,co,expected in [("X",xp,xv),("Y",yp,yv)]:
        require(all(sum((matrix[i][j]*co[j] for j in range(48)),F(0))==expected[i] for i in range(48)),label+"_inverse_map")
    # Verify complete generator multiplication on all 48 basis elements,
    # which determines multiplication by every element of this algebra.
    for label,vec,coordinate in [("X",xv,xp),("Y",yv,yp)]:
        for i in range(48):
            ei=[F(int(j==i)) for j in range(48)]
            actual=ring_product(vec,ei)
            transported=remainder(times(coordinate,[inv[z][i] for z in range(48)]),h)
            transported=fixed(transported,48)
            expected=[sum((matrix[j][z]*transported[z] for z in range(48)),F(0)) for j in range(48)]
            require(actual==expected,f"generator_product_{label}_{i}")
    print("all 49 powers and both coordinate inverses passed; checking defining equations in Q[t]/h",flush=True)
    require(evalmod(f,clean(xp),h)==[],"inverse_map_division_equation")
    require(remainder(plus(times(clean(yp),clean(yp)),evalmod(cubic,clean(xp),h),-1),h)==[],"inverse_map_short_equation")
    require(remainder(plus(plus(clean(yp),scalar(clean(xp),k)),[0,1],-1),h)==[],"inverse_map_primitive_element")
    ox=readpoly(cert["original_x_of_t"]);oy=readpoly(cert["original_y_of_t"])
    require(ox==scalar(plus(xp,[12],-1),F(1,36)),"original_x_map")
    require(oy==scalar(plus(yp,[108],-1),F(1,216)),"original_y_map")
    ex=remainder(plus(plus(times(oy,oy),oy),evalmod([0,-2,1,1],ox,h),-1),h)
    require(ex==[],"inverse_map_original_curve")
    print("all defining equations and original-model maps passed",flush=True)

    require(cert["status"]=="FIELD_CERTIFICATE_PRODUCED","producer_status")
    factors=[readpoly(p) for p in cert["factors"]]
    require(len(factors)==1 and factors[0]==h,"complete_factor_identity")
    integerf=cert["primitive_integer_factors"]
    require(len(integerf)==1 and all(isinstance(z,int) for z in integerf[0]),"integer_factor_format")
    integerf=integerf[0]
    require(len(integerf)==49 and integerf[-1]>0 and math.gcd(*integerf)==1,"primitive_integer_factor")
    require([F(c,integerf[-1]) for c in integerf]==h and cert["factor_denominator"]==integerf[-1],"gauss_primitive_scaling")
    require(cert["product_maps"]=={"to_factors":[["0","1"]],"idempotents":[["1"]]},"complete_single_factor_product_maps")
    trials=cert["modular_tests"]
    require([t["prime"] for t in trials]==[2,3,5],"bounded_first_success_prime_sequence")
    for trial in trials:
        p=trial["prime"]
        require(all(p%d for d in range(2,math.isqrt(p)+1)),f"prime_{p}")
        require(integerf[-1]%p!=0 and all(c.denominator%p for c in h),f"degree_preserving_reduction_{p}")
        hp=[c.numerator*pow(c.denominator,-1,p)%p for c in h]
        dp=modclean([i*hp[i] for i in range(1,49)],p)
        g=modgcd(hp,dp,p)
        if p in [2,3]:
            require(trial=={"prime":p,"squarefree":False,"gcd_degree":len(g)-1} and len(g)>1,f"failed_prime_{p}_complete_replay")
            continue
        require(g==[1] and trial.get("irreducible") is True,"mod5_squarefree")
        require(trial["reduction"]==hp,"mod5_all_coefficients")
        seq=trial["frobenius"]
        require(len(seq)==49 and seq[0]==[0,1],"mod5_full_frobenius_shape")
        for i in range(1,49):
            # Freshman dream and long reduction, instead of producer's
            # repeated-squaring modular exponentiation.
            raw=[0]*(p*(len(seq[i-1])-1)+1)
            for j,c in enumerate(seq[i-1]):raw[p*j]=c
            expected=modreduce(raw,hp,p)
            require(expected==seq[i],f"mod5_frobenius_{i}")
        require(seq[48]==[0,1],"rabin_final_power")
        witnesses=trial["gcd_witnesses"]
        require([w["index"] for w in witnesses]==[16,24],"rabin_all_prime_divisors_of_48")
        for w in witnesses:
            i=w["index"];diff=modadd(seq[i],[0,1],p,-1)
            result=modadd(modmul(w["u"],hp,p),modmul(w["v"],diff,p),p)
            require(result==[1],f"rabin_complete_bezout_{i}")
    return {"dimension":48,"required_dimension":48,"power_basis_rank":48,
        "coordinate_maps":2,"original_coordinate_maps":2,"field_factor_degrees":[48],
        "irreducibility_prime":5,"caps":{"k":64,"prime":200},
        "actual":{"k":0,"last_prime":5},"matrix_inverse_entries":4608,
        "power_columns":48,"frobenius_steps":48,"rabin_gcd_indices":[16,24],
        "basis_generator_products":96,"failures":[]}

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--certificate",type=Path,default=Path(__file__).with_name("certificate.json"))
    parser.add_argument("--report",type=Path,default=Path(__file__).with_name("verification.json"))
    args=parser.parse_args();start=time.monotonic();raw=args.certificate.read_bytes()
    try:
        result=run(json.loads(raw));result["status"]="PASS"
    except (ValueError,KeyError,IndexError,TypeError,ZeroDivisionError) as exc:
        result={"status":"REJECTED","failure":str(exc)}
    result.update({"certificate":str(args.certificate),"sha256":hashlib.sha256(raw).hexdigest(),
        "checks_passed":len(COUNTS),"seconds":round(time.monotonic()-start,3)})
    args.report.write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps({**result,"report":str(args.report)}))
    raise SystemExit(0 if result["status"]=="PASS" else 1)

if __name__=="__main__":main()
