#!/usr/bin/env python3
"""Fixed scalar multiplication using symbolic division polynomials, exact Q arithmetic."""
from pathlib import Path
from fractions import Fraction as Q
import hashlib,json,sys,time
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
import build_certificate as P
ROOT=Path(__file__).resolve().parent
UP=ROOT.parent/'certificate.json'

def enc(v):
    if isinstance(v,Q):return str(v)
    if isinstance(v,(list,tuple)):return [enc(x) for x in v]
    if isinstance(v,dict):return {str(k):enc(x) for k,x in v.items()}
    return v

def main():
    start=time.monotonic(); upstream=json.loads(UP.read_text())
    f=list(map(Q,upstream['f'])); c=[Q(46224),Q(-3024),Q(0),Q(1)]
    def add(u,v):return [P.add(u[j],v[j]) for j in range(2)]
    def scale(u,k):return [P.scale(z,k) for z in u]
    def sub(u,v):return add(u,scale(v,-1))
    def mul(u,v):return [P.add(P.mul(u[0],v[0]),P.mul(c,P.mul(u[1],v[1]))),P.add(P.mul(u[0],v[1]),P.mul(u[1],v[0]))]
    zero=[[Q(0)],[Q(0)]];one=[[Q(1)],[Q(0)]];X=[[Q(0),Q(1)],[Q(0)]];Y=[[Q(0)],[Q(1)]]
    def power(u,n):
        z=one
        for _ in range(n):z=mul(z,u)
        return z
    divisions={}
    def divideY(u,k,label):
        q,r=P.divmodq(u[0],c);assert r==[0],label
        z=[P.scale(u[1],Q(1,k)),P.scale(q,Q(1,k))]
        assert mul(scale(Y,k),z)==u,label
        divisions[label]={'numerator':u,'denominator_multiple_Y':k,'quotient':z}
        return z
    psi={-1:scale(one,-1),0:zero,1:one,2:scale(Y,2),3:[list(map(Q,upstream['psi3'])),[Q(0)]],4:[[Q(0)],P.scale(list(map(Q,upstream['psi4_over_4Y'])),4)]}
    psi[5]=sub(mul(psi[4],power(psi[2],3)),power(psi[3],3))
    psi[6]=divideY(mul(psi[3],sub(mul(psi[5],power(psi[2],2)),mul(psi[1],power(psi[4],2)))),2,'psi6')
    psi[7]=sub(mul(psi[5],power(psi[3],3)),mul(psi[2],power(psi[4],3)))
    psi[8]=divideY(mul(psi[4],sub(mul(psi[6],power(psi[3],2)),mul(psi[2],power(psi[5],2)))),2,'psi8')
    phi={};omega={}
    for n in range(1,7):
        phi[n]=sub(mul(X,power(psi[n],2)),mul(psi[n+1],psi[n-1]))
        omega[n]=divideY(sub(mul(psi[n+2],power(psi[n-1],2)),mul(psi[n-2],power(psi[n+1],2))),4,'omega'+str(n))
    print('All symbolic recurrences and eight exact Y-divisions constructed',flush=True)
    def red(u):return [P.divmodq(z,f)[1] for z in u]
    def rm(u,v):return red(mul(u,v))
    def inv(u):
        # (a+bY)^(-1)=(a-bY)/(a^2-cb^2); full exact field norm inversion.
        norm=P.sub(P.mul(u[0],u[0]),P.mul(c,P.mul(u[1],u[1])))
        g,s,t=P.bezout(f,norm);assert g==[1]
        z=red([P.mul(u[0],t),P.scale(P.mul(u[1],t),-1)])
        assert rm(u,z)==one
        return z
    denominators={}
    def witness(key,value):
        value=red(value); denominators[key]={'value':value,'inverse':inv(value)}
        return denominators[key]['inverse']
    for k in [2,4,36,216]:witness('constant'+str(k),scale(one,k))
    for k in [2,4]:witness(str(k)+'Y',scale(Y,k))
    maps={}
    for n in range(1,7):
        ps=red(psi[n]);ps2=rm(ps,ps);ps3=rm(ps2,ps)
        iz=witness('psi'+str(n),ps)
        iz2=rm(iz,iz);iz3=rm(iz2,iz)
        denominators['psi'+str(n)+'^2']={'value':ps2,'inverse':iz2}
        denominators['psi'+str(n)+'^3']={'value':ps3,'inverse':iz3}
        xx=rm(red(phi[n]),iz2);yy=rm(red(omega[n]),iz3)
        ox=scale(sub(xx,scale(one,12)),Q(1,36));oy=scale(sub(yy,scale(one,108)),Q(1,216))
        def fixed(u):return u[0]+[Q(0)]*(24-len(u[0]))+u[1]+[Q(0)]*(24-len(u[1]))
        bx=[one]
        for _ in range(23):bx.append(rm(bx[-1],xx))
        cols=[fixed(v) for v in bx]+[fixed(rm(v,yy)) for v in bx]
        B=[list(row) for row in zip(*cols)]
        tp=[one]
        for _ in range(47):tp.append(rm(tp[-1],yy))
        N=[[Q(z) for z in r] for r in upstream['inverse']]
        tcols=[P.mv(N,fixed(v)) for v in tp]
        T=[list(row) for row in zip(*tcols)]
        maps[str(n)]={'X':xx,'Y':yy,'x':ox,'y':oy,'sigma_t':tcols[1], 'B_action':B,'T_action':T}
        print('scalar',n,': both coordinates, 48 B-basis and 48 t-basis images saved',flush=True)
    cert={'schema':'389-seven-scalars-v1','upstream_sha256':hashlib.sha256(UP.read_bytes()).hexdigest(),'scalars':list(range(1,7)), 'basis_dimension':48,'convention':'sigma_a(f)(P)=f([a]P)','psi':psi,'phi':phi,'omega':omega,'symbolic_divisions':divisions,'denominators':denominators,'maps':maps,'primitive_scalar':3,'primitive_powers_mod7':[pow(3,j,7) for j in range(7)]}
    path=ROOT/'actions.json';path.write_text(json.dumps(enc(cert),separators=(',',':'))+'\n')
    print(json.dumps({'status':'PRODUCED_UNVERIFIED','maps':6,'required_maps':6,'dimension':48,'required_dimension':48,'symbolic_divisions':len(divisions),'denominator_witnesses':len(denominators),'path':str(path),'seconds':round(time.monotonic()-start,2)}),flush=True)
if __name__=='__main__':main()
