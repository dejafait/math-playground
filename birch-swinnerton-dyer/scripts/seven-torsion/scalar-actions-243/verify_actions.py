#!/usr/bin/env python3
"""Independent replay: old verifier arithmetic only, no producer imports.
Symbolic bivariate identities precede faithful two-coordinate quotient checks.
Every matrix product is checked at all 2304 positions using integer scaling.
"""
from fractions import Fraction as F
from pathlib import Path
from math import lcm
import argparse,hashlib,json,sys,time
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
import verify_certificate as V
ROOT=Path(__file__).resolve().parent
CHECKS=[]
def need(ok,label):
    if not ok:raise ValueError(label)
    CHECKS.append(label)
def poly(x):return V.clean([F(v) for v in x])
def pair(x):
    need(isinstance(x,list) and len(x)==2,'pair_shape_'+str(len(CHECKS)))
    return (poly(x[0]),poly(x[1]))
def matrix(x):
    need(len(x)==48 and all(len(r)==48 for r in x),'matrix_shape_'+str(len(CHECKS)))
    return [[F(v) for v in r] for r in x]
def bivar(u):return {(i,j):z for j in range(2) for i,z in enumerate(u[j]) if z}
def frombp(u):
    need(all(j in (0,1) for i,j in u),'Y_degree_'+str(len(CHECKS)))
    return tuple(V.clean([u.get((i,j),F(0)) for i in range(max((i for i,k in u if k==j),default=-1)+1)]) for j in range(2))
def lin(M,v):return [sum((z*w for z,w in zip(r,v) if z and w),F(0)) for r in M]
def integer_matrix(M):
    d=lcm(*(z.denominator for r in M for z in r))
    return [[int(z*d) for z in r] for r in M],d
def compose_equal(L,R,S,label):
    # Unlike producer basis generation, exact dense integer matrix multiplication.
    A,da=integer_matrix(L);B,db=integer_matrix(R);C,dc=integer_matrix(S)
    cols=list(zip(*B)); count=0
    for i,row in enumerate(A):
        nz=[(k,z) for k,z in enumerate(row) if z]
        for j,col in enumerate(cols):
            val=sum(z*col[k] for k,z in nz)
            need(val*dc==C[i][j]*da*db,label+'_'+str(i)+'_'+str(j))
            count+=1
    return count

def run(cert,up):
    need(cert['schema']=='389-seven-scalars-v1','schema')
    need(cert['upstream_sha256']==hashlib.sha256((ROOT.parent/'certificate.json').read_bytes()).hexdigest(),'upstream_hash')
    need(cert['scalars']==list(range(1,7)) and cert['basis_dimension']==48,'full_six_scalars_dimension48')
    need(cert['convention']=='sigma_a(f)(P)=f([a]P)','forward_convention')
    a,b=F(-3024),F(46224);c=[b,a,F(0),F(1)];f=poly(up['f'])
    zero={};one={(0,0):F(1)};X={(1,0):F(1)};Y={(0,1):F(1)}
    def add(u,v):return V.bpadd(u,v)
    def sub(u,v):return V.bpadd(u,v,-1)
    def scale(u,k):return V.bpscale(u,k)
    def mul(u,v):return V.bpnormalize(V.bpmul(u,v),a,b)
    def power(u,n):
        z=one
        for _ in range(n):z=mul(z,u)
        return z
    divisions=cert['symbolic_divisions'];used=[]
    def exactY(numerator,k,label):
        need(label in divisions,'division_present_'+label)
        data=divisions[label];q=bivar(pair(data['quotient']))
        need(data['denominator_multiple_Y']==k,'division_constant_'+label)
        need(bivar(pair(data['numerator']))==numerator,'division_numerator_'+label)
        need(mul(scale(Y,k),q)==numerator,'exact_polynomial_division_'+label)
        used.append(label);return q
    psi={-1:scale(one,-1),0:zero,1:one,2:scale(Y,2),3:V.asbp([-a*a,12*b,6*a,F(0),F(3)]),4:V.bpmul(scale(Y,4),V.asbp([-a**3-8*b*b,-4*a*b,-5*a*a,20*b,5*a,F(0),F(1)]))}
    psi[5]=sub(mul(psi[4],power(psi[2],3)),power(psi[3],3))
    psi[6]=exactY(mul(psi[3],sub(mul(psi[5],power(psi[2],2)),mul(psi[1],power(psi[4],2)))),2,'psi6')
    psi[7]=sub(mul(psi[5],power(psi[3],3)),mul(psi[2],power(psi[4],3)))
    psi[8]=exactY(mul(psi[4],sub(mul(psi[6],power(psi[3],2)),mul(psi[2],power(psi[5],2)))),2,'psi8')
    need(set(cert['psi'])==set(map(str,range(-1,9))),'all_psi_indices')
    for n in range(-1,9):need(bivar(pair(cert['psi'][str(n)]))==psi[n],'psi_'+str(n)+'_all_coefficients')
    phi={};omega={}
    need(set(cert['phi'])==set(cert['omega'])==set(map(str,range(1,7))),'all_phi_omega_indices')
    for n in range(1,7):
        phi[n]=sub(mul(X,power(psi[n],2)),mul(psi[n+1],psi[n-1]))
        omega[n]=exactY(sub(mul(psi[n+2],power(psi[n-1],2)),mul(psi[n-2],power(psi[n+1],2))),4,'omega'+str(n))
        need(bivar(pair(cert['phi'][str(n)]))==phi[n],'phi_'+str(n)+'_all_coefficients')
        need(bivar(pair(cert['omega'][str(n)]))==omega[n],'omega_'+str(n)+'_all_coefficients')
    need(set(divisions)==set(used),'all_symbolic_divisions')
    print('Independent symbolic reconstruction: all 10 division polynomials and 8 exact divisions passed',flush=True)
    def red(u):
        z=frombp(u)
        return tuple(V.remainder(p,f) for p in z)
    def rm(u,v):
        ev=V.plus(V.times(u[0],v[0]),V.times(c,V.times(u[1],v[1])))
        od=V.plus(V.times(u[0],v[1]),V.times(u[1],v[0]))
        return (V.remainder(ev,f),V.remainder(od,f))
    def ra(u,v,sign=1):return tuple(V.plus(u[j],v[j],sign) for j in range(2))
    def rs(u,k):return tuple(V.scalar(p,k) for p in u)
    o=red(one);xx=red(X);yy=red(Y);zz=red(zero)
    expected={}
    for k in [2,4,36,216]:expected['constant'+str(k)]=rs(o,k)
    for k in [2,4]:expected[str(k)+'Y']=rs(yy,k)
    for n in range(1,7):
        v=red(psi[n]);v2=rm(v,v)
        expected.update({'psi'+str(n):v,'psi'+str(n)+'^2':v2,'psi'+str(n)+'^3':rm(v2,v)})
    need(set(cert['denominators'])==set(expected),'complete_required_denominators')
    inverses={}
    for key,val in expected.items():
        data=cert['denominators'][key];u=pair(data['value']);iv=pair(data['inverse'])
        need(all(len(p)<=24 for p in u+iv),'denominator_degree_'+key)
        need(u==val,'denominator_value_'+key)
        need(rm(u,iv)==o,'denominator_inverse_'+key)
        inverses[key]=iv
    def fixed(u):return V.fixed(u[0],24)+V.fixed(u[1],24)
    def getcol(M,i):return [r[i] for r in M]
    def unfix(v):return (V.clean(v[:24]),V.clean(v[24:]))
    def apply(M,u):return unfix(lin(M,fixed(u)))
    M=matrix(up['matrix']);N=matrix(up['inverse']);h=poly(up['h']);B={};T={};maps={}
    for n in range(1,7):
        data=cert['maps'][str(n)];nx=pair(data['X']);ny=pair(data['Y']);ox=pair(data['x']);oy=pair(data['y'])
        need(all(len(p)<=24 for u in [nx,ny,ox,oy] for p in u),'map_degree_'+str(n))
        need(rm(nx,expected['psi'+str(n)+'^2'])==red(phi[n]),'geometric_X_'+str(n))
        need(rm(ny,expected['psi'+str(n)+'^3'])==red(omega[n]),'geometric_Y_'+str(n))
        need(rs(ra(nx,rs(o,12),-1),F(1,36))==ox and rs(ra(ny,rs(o,108),-1),F(1,216))==oy,'original_transport_'+str(n))
        nx2=rm(nx,nx);nx3=rm(nx2,nx)
        need(rm(ny,ny)==ra(ra(nx3,rs(nx,a)),rs(o,b)),'short_equation_'+str(n))
        need(ra(rm(oy,oy),oy)==ra(ra(rm(rm(ox,ox),ox),rm(ox,ox)),rs(ox,2),-1),'original_equation_'+str(n))
        # Horner reduction of f(nx) and h(ny) in the entire etale algebra.
        for key,pol,z in [('f',f,nx),('h',h,ny)]:
            ev=zz
            for coeff in reversed(pol):ev=ra(rm(ev,z),rs(o,coeff))
            need(ev==zz,'defining_'+key+'_'+str(n))
        B[n]=matrix(data['B_action']);T[n]=matrix(data['T_action']);maps[n]=(nx,ny,ox,oy)
        p=o
        for j in range(24):
            need(getcol(B[n],j)==fixed(p),'full_B_even_'+str(n)+'_'+str(j))
            need(getcol(B[n],j+24)==fixed(rm(p,ny)),'full_B_odd_'+str(n)+'_'+str(j))
            p=rm(p,nx)
        p=o
        for j in range(48):
            need(lin(M,getcol(T[n],j))==fixed(p),'full_T_basis_'+str(n)+'_'+str(j))
            p=rm(p,ny)
        need([F(z) for z in data['sigma_t']]==getcol(T[n],1),'sigma_t_'+str(n))
        need(lin(M,[F(z) for z in data['sigma_t']])==fixed(ny),'sigma_t_geometric_'+str(n))
        # Both transports on the original coordinate functions are checked too.
        origx=rs(ra(xx,rs(o,12),-1),F(1,36));origy=rs(ra(yy,rs(o,108),-1),F(1,216))
        need(apply(B[n],origx)==ox and apply(B[n],origy)==oy,'original_coordinate_action_'+str(n))
        print('scalar',n,': all denominators, coordinates, defining relations and 96 basis images passed',flush=True)
    need(set(cert['maps'])==set(map(str,range(1,7))),'six_maps_only')
    I=[[F(int(i==j)) for j in range(48)] for i in range(48)]
    need(B[1]==T[1]==I and maps[1][0]==xx and maps[1][1]==yy,'identity_full_algebra')
    entries=0;comps=[]
    for u in range(1,7):
        for v in range(1,7):
            w=u*v%7
            for j,name in enumerate(['X','Y','x','y']):
                need(apply(B[u],maps[v][j])==maps[w][j],'coordinate_composition_'+str(u)+'_'+str(v)+'_'+name)
            entries+=compose_equal(B[u],B[v],B[w],'B_composition_'+str(u)+'_'+str(v))
            entries+=compose_equal(T[u],T[v],T[w],'T_composition_'+str(u)+'_'+str(v))
            comps.append({'a':u,'b':v,'product_mod7':w,'both_coordinate_models':True,'B_entries_checked':2304,'T_entries_checked':2304,'failures':[]})
        print('all full-basis compositions for scalar',u,'passed',flush=True)
    inverse_checks=[]
    for u in range(1,7):
        v=pow(u,-1,7)
        need(next(z for z in comps if z['a']==u and z['b']==v)['product_mod7']==1,'inverse_'+str(u))
        inverse_checks.append({'scalar':u,'inverse_mod7':v,'left_and_right_full_B_T_products':'identity'})
    need(cert['primitive_scalar']==3 and cert['primitive_powers_mod7']==[pow(3,j,7) for j in range(7)],'primitive_scalar_powers')
    need(set(cert['primitive_powers_mod7'][:6])==set(range(1,7)) and cert['primitive_powers_mod7'][6]==1,'primitive_scalar_order6')
    return {'status':'PASS','maps':6,'required_maps':6,'dimension':48,'required_dimension':48,'symbolic_divisions':8,'division_polynomials':10,'denominator_witnesses':len(expected),'basis_images':576,'coordinate_compositions':144,'scalar_compositions':comps,'inverse_checks':inverse_checks,'matrix_composition_entries_checked':entries,'matrix_composition_entries_required':36*2*48*48,'primitive_scalar':3,'primitive_order':6,'failures':[]}

def main():
    arg=argparse.ArgumentParser();arg.add_argument('--certificate',default=str(ROOT/'actions.json'));arg.add_argument('--report',default=str(ROOT/'verification.json'));args=arg.parse_args()
    start=time.monotonic();report={'status':'FAIL','failures':[]}
    try:report=run(json.loads(Path(args.certificate).read_text()),json.loads((ROOT.parent/'certificate.json').read_text()))
    except Exception as err:report['failures']=[str(err)]
    report.update({'certificate':str(Path(args.certificate)),'certificate_sha256':hashlib.sha256(Path(args.certificate).read_bytes()).hexdigest(),'checks_passed':len(CHECKS),'seconds':round(time.monotonic()-start,3)})
    Path(args.report).write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items() if k not in ['scalar_compositions','inverse_checks']}|{'report':args.report}),flush=True)
    return 0 if report['status']=='PASS' else 1
if __name__=='__main__':raise SystemExit(main())
