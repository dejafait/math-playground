"""Exact rational checks supporting L124; standard library only."""
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
exps=[(i,j,k,5-i-j-k,0,0) for i in range(6) for j in range(6-i) for k in range(6-i-j)]
basis=[{e:F(1)} for e in exps]
binexps=[(i,5-i,0,0,0,0) for i in range(6)]
jetexps=[(i,4-i,0,0,int(j==0),int(j==1)) for i in range(5) for j in range(2)]
bases=[x+[{},{}],[{},{}]+x,x+x]
samples=[('orthogonal_equal',1,1,0,0),('generic_nonorthogonal',2,3,F(1,3),F(1,2)),('order_zero_exception_nonreal',1,1,F(-1,2),F(1,2)),('order_zero_exception_real',1,1,F(-1,2),0)]
records=[]; failures=[]
for name,a,b,s,r in samples:
    a,b,s,r=map(F,(a,b,s,r)); Q=[[s,-r],[r,s]]; Qt=[[s,r],[-r,s]]
    t=a+b+2*s; C=mscale(Q,1/a); D=mscale(Qt,1/b); H=mscale(madd(mscale(I,a),Qt),1/t)
    normals=[matvec(mscale(C,-1),u)+u,u+matvec(mscale(D,-1),u),matvec(madd(I,mscale(H,-1)),u)+matvec(mscale(H,-1),u)]
    N=sum([matrix([directional(f,p,n) for f in basis],jetexps) for p,n in zip(bases,normals)],[])
    R=sum([matrix([substitute(f,p+u) for f in basis],binexps) for p in bases],[])
    nr=rank(N); jr=rank(N+R)
    checks={'positive_metric':a>0 and b>0 and a*b>s*s+r*r,'normal_rank':nr==30,'full_jet_rank':jr==48,'restriction_rank':jr-nr==18}
    records.append({'name':name,'a':str(a),'b':str(b),'q_real':str(s),'q_imaginary_length':str(r),'normal_rank_actual':nr,'normal_rank_required':30,'full_jet_rank_actual':jr,'full_jet_rank_required':48,'restriction_rank_actual':jr-nr,'restriction_rank_required':18,'normal_matrix':serialize(N),'restriction_matrix':serialize(R),'checks':checks})
    failures += [name+': '+k for k,v in checks.items() if not v]
mixed=[f for e,f in zip(exps,basis) if e[0]+e[1] in (2,3)]
value_matrix=matrix([substitute(f,x+x+u) for f in mixed],binexps)
derivative_matrix=matrix([directional(f,x+x,u+[{},{}]) for f in mixed],jetexps)
interpolation=value_matrix+derivative_matrix
ir=rank(interpolation)
det=add(mul(x[0],y[1]),scale(mul(x[1],y[0]),-1))
cubic21=[{(i,2-i,j,1-j,0,0):F(1)} for i in range(3) for j in range(2)]
corrections=[mul(det,f) for f in cubic21]
correction_matrix=matrix([directional(f,x+x,u+[{},{}]) for f in corrections],jetexps)
checks={'interpolation_rank_sixteen':ir==16,'interpolation_kernel_eight':len(mixed)-ir==8,'corrections_have_zero_value':all(not substitute(f,x+x+u) for f in corrections),'correction_derivative_rank_four':rank(correction_matrix)==4,'corrections_radial_zero':all(not directional(f,x+x,x+[{},{}]) for f in corrections)}
jvals=[scale(x[1],-1),x[0],scale(y[1],-1),y[0]]+u
checks['odd_quaternionic_square_minus_one']=all(substitute(substitute(f,jvals),jvals)==scale(f,-1) for f in basis)
failures += [k for k,v in checks.items() if not v]
certificate={'scope':'Exact rational sample matrices supporting the uniform real proof in L124; each matrix is for one complex H component, not a real dimension certificate. No actual K3 jet or metric germ is certified.','samples':records,'interpolation':{'matrix':serialize(interpolation),'rank_actual':ir,'rank_required':16,'correction_matrix':serialize(correction_matrix),'checks':checks},'failures':failures,'passed':not failures}
out=Path(__file__).with_name('three_line_first_derivative_certificate.json')
out.write_text(json.dumps(certificate,indent=2)+'\n')
for z in records: print(f"{z['name']}: normal rank {z['normal_rank_actual']}/30; full jet rank {z['full_jet_rank_actual']}/48; complex restriction range {z['restriction_rank_actual']}/18")
print(f'Interpolation rank: {ir}/16; correction rank: {rank(correction_matrix)}/4; checks: {all(checks.values())}; failures: {failures}; certificate: {out}')
raise SystemExit(bool(failures))
