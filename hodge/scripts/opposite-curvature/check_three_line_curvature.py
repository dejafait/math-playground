"""Exact rational checks supporting L123; standard library only."""
import json
from fractions import Fraction as F
from itertools import product
from math import comb
from pathlib import Path

# Polynomials in x0,x1,y0,y1,u0,u1.
zero=(0,)*6
def add(*ps):
    d={}
    for p in ps:
        for e,c in p.items(): d[e]=d.get(e,F(0))+c
    return {e:c for e,c in d.items() if c}
def scale(p,c): return {e:v*c for e,v in p.items() if v*c}
def mul(p,q):
    d={}
    for e,a in p.items():
        for f,b in q.items():
            k=tuple(x+y for x,y in zip(e,f)); d[k]=d.get(k,F(0))+a*b
    return {e:c for e,c in d.items() if c}
def power(p,n):
    v={zero:F(1)}
    for _ in range(n): v=mul(v,p)
    return v
def derivative(p,j):
    d={}
    for e,c in p.items():
        if e[j]:
            f=list(e); f[j]-=1; d[tuple(f)]=c*e[j]
    return d
Z=[{tuple(int(i==j) for i in range(6)):F(1)} for j in range(6)]
x=Z[:2]; y=Z[2:4]; u=Z[4:]
def substitute(p,values):
    out={}
    for e,c in p.items():
        term={zero:c}
        for v,n in zip(values,e): term=mul(term,power(v,n))
        out=add(out,term)
    return out
def directional(p,base,direction):
    return substitute(add(*(mul(derivative(p,j),direction[j]) for j in range(4))),base+u)
def matvec(A,v): return [add(*(scale(p,c) for p,c in zip(v,row))) for row in A]
def mscale(A,c): return [[v*c for v in row] for row in A]
def madd(A,B): return [[v+w for v,w in zip(a,b)] for a,b in zip(A,B)]
I=[[F(1),F(0)],[F(0),F(1)]]
def op(p,Q): return add(*(mul(derivative(p,j),v) for j,v in enumerate(matvec(Q,x))))
def rank(rows):
    a=[list(row) for row in rows]; r=0
    for j in range(len(a[0])):
        piv=next((k for k in range(r,len(a)) if a[k][j]),None)
        if piv is None: continue
        a[r],a[piv]=a[piv],a[r]; v=a[r][j]; a[r]=[t/v for t in a[r]]
        for k in range(r+1,len(a)):
            v=a[k][j]
            if v: a[k]=[t-v*w for t,w in zip(a[k],a[r])]
        r+=1
        if r==len(a): break
    return r

def matrix(columns,mons): return [[p.get(e,F(0)) for p in columns] for e in mons]
def serialize(M): return [[str(v) for v in row] for row in M]
exps=[(i,j,k,4-i-j-k,0,0) for i in range(5) for j in range(5-i) for k in range(5-i-j)]
basis=[{e:F(1)} for e in exps]
binexps=[(i,4-i,0,0,0,0) for i in range(5)]
binary=[{e:F(1)} for e in binexps]
jetexps=[(i,3-i,0,0,int(j==0),int(j==1)) for i in range(4) for j in range(2)]
bases=[x+[{},{}],[{},{}]+x,x+x]
samples=[('orthogonal_equal',1,1,0,0,5),('generic_nonorthogonal',2,3,F(1,3),F(1,2),5),('equal_angle_nonreal',1,1,F(-1,2),F(1,2),4),('equal_angle_real',1,1,F(-1,2),0,0)]
records=[]; failures=[]
for name,a,b,s,r,required in samples:
    a,b,s,r=map(F,(a,b,s,r)); Q=[[s,-r],[r,s]]; Qt=[[s,r],[-r,s]]
    t=a+b+2*s; C=mscale(Q,1/a); D=mscale(Qt,1/b); H=mscale(madd(mscale(I,a),Qt),1/t)
    normals=[matvec(mscale(C,-1),u)+u,u+matvec(mscale(D,-1),u),matvec(madd(I,mscale(H,-1)),u)+matvec(mscale(H,-1),u)]
    N=sum([matrix([directional(f,p,n) for f in basis],jetexps) for p,n in zip(bases,normals)],[])
    R=sum([matrix([substitute(f,p+u) for f in basis],binexps) for p in bases],[])
    rel=[]
    for k in range(15):
        A=binary[k] if k<5 else {}; B=binary[k-5] if 5<=k<10 else {}; T=binary[k-10] if k>=10 else {}
        rel.append(add(op(T,H),scale(T,-2),scale(A,-2),scale(op(A,C),-1),scale(B,2),op(B,D)))
    M=matrix(rel,binexps)
    MR=[[sum(m*R[k][j] for k,m in enumerate(row)) for j in range(35)] for row in M]
    nr=rank(N); jr=rank(N+R); cr=rank(M)
    checks={'positive_metric':a>0 and b>0 and a*b>s*s+r*r,'compatibility_rank':cr==required,'normal_rank':nr==19+required,'full_jet_rank':jr==34,'restriction_rank':jr-nr==15-required,'relation_vanishes_on_entire_normal_kernel':rank(N+MR)==nr}
    records.append({'name':name,'a':str(a),'b':str(b),'q_real':str(s),'q_imaginary_length':str(r),'normal_rank_actual':nr,'normal_rank_required':19+required,'restriction_rank_actual':jr-nr,'restriction_rank_required':15-required,'normal_matrix':serialize(N),'restriction_matrix':serialize(R),'compatibility_matrix':serialize(M),'checks':checks})
    failures += [name+': '+k for k,v in checks.items() if not v]

mixed=[f for e,f in zip(exps,basis) if e[0]+e[1]==2]
B=matrix([directional(f,x+x,u+[{},{}]) for f in mixed],jetexps)
det=add(mul(x[0],y[1]),scale(mul(x[1],y[0]),-1)); detsquare=power(det,2)
A=mul(power(x[0],2),power(x[1],2)); witness=add(A,mul(power(y[0],2),power(y[1],2)))
witness_normals=[[{},{}]+u,u+[{},{}],u+[scale(v,-1) for v in u]]
rho=substitute(witness,[scale(x[1],-1),x[0],scale(y[1],-1),y[0]]+u)
checks={'mixed_derivative_rank_eight':rank(B)==8,'determinant_square_in_kernel':not directional(detsquare,x+x,u+[{},{}]),'witness_all_normal_components_zero':all(not directional(witness,p,n) for p,n in zip(bases,witness_normals)),'witness_unit_restrictions':[scale(substitute(witness,p+u),F(1,f)) for p,f in zip(bases,[1,1,4])]==[A,A,scale(A,F(1,2))],'witness_quaternionic_reality':rho==witness}
failures += [k for k,v in checks.items() if not v]
external=8*74+10*comb(75,2)+4*comb(76,3)+comb(77,4)
certificate={'scope':'Exact samples; L123 contains arbitrary-angle and real-form proof. No actual K3 data or geometric existence certified.','initial_tool_failure':'Initial SymPy-based version could not import sympy; replaced by this standard-library exact rational implementation.','samples':records,'interpolation_and_witness':checks,'external_kernel_real_dimension':external,'failures':failures,'passed':not failures}
out=Path(__file__).with_name('three_line_curvature_certificate.json')
out.write_text(json.dumps(certificate,indent=2)+'\n')
for z in records: print(f"{z['name']}: normal rank {z['normal_rank_actual']}/{z['normal_rank_required']}; restriction range {z['restriction_rank_actual']}/{z['restriction_rank_required']}")
print(f'Interpolation and real nonzero witness: {all(checks.values())}; failures: {failures}; certificate: {out}')
raise SystemExit(bool(failures))
