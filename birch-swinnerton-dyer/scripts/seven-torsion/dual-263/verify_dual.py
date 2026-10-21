"""Independent polynomial replay: imports no producer or producer arithmetic."""
from pathlib import Path
from fractions import Fraction as F
import sys,json,time,signal,hashlib,copy
R=Path(__file__).resolve().parent;U=R.parent
sys.path.insert(0,str(U));import verify_certificate as V
start=time.monotonic();checks=[];report={'passed':False,'phase':'initialization','required_seconds':180,'failures':[]}
def timeout(*_):raise TimeoutError('180-second independent replay cap')
signal.signal(signal.SIGALRM,timeout);signal.alarm(180)
def encode(x):
    if isinstance(x,F):return str(x)
    if isinstance(x,list):return [encode(a) for a in x]
    if isinstance(x,dict):return {k:encode(a) for k,a in x.items()}
    return x
def save(name,x):
    data=json.dumps(encode(x),separators=(',',':'))+'\n'
    assert sum(p.stat().st_size for p in R.rglob('*') if p.is_file())+len(data.encode())<=134217728,'byte cap'
    with (R/name).open('x') as f:f.write(data)
def need(ok,label):
    if not ok:raise ValueError(label)
    checks.append(label)
try:
    c=json.loads((R/'dual.json').read_text());old=json.loads((U/'quotient-254/quotient.json').read_text());h=list(map(F,old['h']))
    zero=[];one=[F(1)]
    def da(a,b,s=1):return V.plus(a,b,s)
    def dm(a,b):return V.remainder(V.times(a,b),h)
    def ds(a,k):return V.scalar(a,k)
    def dc(a):
        a=V.clean(list(map(F,a)));need(len(a)<=8,'eight_field_coordinates');return a
    def read(p):return {i:v for i,a in enumerate(p) if (v:=dc(a))}
    def pa(p,q,s=1):
        out=dict(p)
        for i,a in q.items():
            v=da(out.get(i,zero),a,s)
            if v:out[i]=v
            else:out.pop(i,None)
        return out
    def pc(p,k):return {i:v for i,a in p.items() if (v:=ds(a,k))}
    def pm(p,q):
        out={}
        for i,a in p.items():
            for j,b in q.items():
                v=da(out.get(i+j,zero),dm(a,b))
                if v:out[i+j]=v
                else:out.pop(i+j,None)
        return out
    def pp(p,n):
        out={0:one}
        for _ in range(n):out=pm(out,p)
        return out
    def pd(p):return {i-1:ds(a,i) for i,a in p.items() if i}
    def array(p):return [p.get(i,zero) for i in range(max(p,default=0)+1)]
    def scalarpoly(a):return {0:a} if a else {}
    x={1:one}
    A=dc(old['target_a']);B=dc(old['target_b']);a=[F(-3024)];b=[F(46224)]
    norm=json.loads((R/'normalization.json').read_text())
    need(norm['J_x']==49 and norm['J_y']==343 and norm['J_differential']=='1/7' and norm['J_inverse_x']=='1/49' and norm['J_inverse_y']=='1/343' and norm['actual_dual_differential']==7,'model_change_and_inverse_scalings')
    need(dc(norm['source_a'])==A and dc(norm['source_b'])==B and dc(norm['normalized_target_a'])==ds(a,7**4) and dc(norm['normalized_target_b'])==ds(b,7**6),'full_normalization_coefficients')
    need(343**2==49**3 and 49*7**4==343**2 and 7**6==343**2,'model_change_curve_and_differential')
    k=read(c['k']);kp=pd(k);k2=pp(k,2);k3=pp(k,3);cc={0:B,1:A,3:one}
    N=read(c['normalized_N']);M=read(c['normalized_M'])
    def preliminary(obj):
        need(obj['x_divisor']==49 and obj['y_divisor']==343,'actual_dual_normalization')
        mm=read(obj['normalized_M']);nn=read(obj['normalized_N'])
        need(mm==pa(pm(pd(nn),k),pc(pm(nn,kp),2),-1),'actual_dual_differential_seven')
    preliminary(c)
    need(c['schema']=='389-dual-kernel-v1' and list(map(F,c['h']))==h,'whole_field_schema')
    need(c['quotient_sha256']==hashlib.sha256((U/'quotient-254/quotient.json').read_bytes()).hexdigest(),'audited_quotient_hash')
    need(max(k)==3 and k[3]==one,'monic_degree_three')
    need(read(c['k2'])==k2 and read(c['k3'])==k3,'complete_denominators')
    def rem(p):
        p=dict(p)
        while p and max(p)>=3:
            i=max(p);v=p[i];p=pa(p,{j+i-3:dm(v,w) for j,w in k.items()},-1)
        return p
    need(rem(pm(kp,read(c['kprime_inverse'])))=={0:one},'kernel_squarefree_unit')
    need(rem(pm(cc,read(c['curve_inverse'])))=={0:one},'both_signs_disjoint_from_two_torsion')
    for i,u in enumerate(c['unit_witnesses']):need(dm(dc(u['value']),dc(u['inverse']))==one,'reconstruction_unit_'+str(i))
    # Explicit noncancellation witnesses from the independently checked units.
    ni=pc(pm(read(c['curve_inverse']),pp(read(c['kprime_inverse']),2)),F(1,4))
    mi=pc(pm(ni,read(c['kprime_inverse'])),F(-1,2))
    need(rem(pm(N,ni))=={0:one},'x_numerator_unit_at_every_kernel_point')
    need(rem(pm(M,mi))=={0:one},'y_numerator_unit_at_every_kernel_point')
    need(max(N)==7 and N[7]==one and max(M)==9 and M[9]==one,'exact_degree_and_O_extension')
    # Direct normalized and actual curve identities, without producer formula.
    rhs=pa(pa(pp(N,3),pm(scalarpoly(ds(a,7**4)),pm(N,pp(k,4)))),pm(scalarpoly(ds(b,7**6)),pp(k,6)))
    curve_res=pa(pm(cc,pp(M,2)),rhs,-1)
    need(not curve_res,'full_normalized_and_scaled_curve_identity')
    save('basic-identities.json',{'curve_residual':array(curve_res),'N_inverse_mod_k':array(rem(ni)),'M_inverse_mod_k':array(rem(mi)),'derivative_residual':array(pa(M,pa(pm(pd(N),k),pc(pm(N,kp),2),-1),-1))})
    report['phase']='division polynomials and both compositions'
    def seven(aa,bb,label):
        cub={0:bb,1:aa,3:one};aa2=dm(aa,aa);aa3=dm(aa2,aa)
        p3={0:ds(aa2,-1),1:ds(bb,12),2:ds(aa,6),4:[F(3)]};p3={i:v for i,v in p3.items() if v}
        p4={0:da(ds(aa3,-1),ds(dm(bb,bb),-8)),1:ds(dm(aa,bb),-4),2:ds(aa2,-5),3:ds(bb,20),4:ds(aa,5),6:one};p4={i:v for i,v in p4.items() if v}
        # p4 is psi4/(4Y); p6 and p8 below are psi_even/Y.
        p5=pa(pc(pm(pp(cub,2),p4),32),pp(p3,3),-1)
        p6=pc(pm(p3,pa(p5,pc(pp(p4,2),4),-1)),2)
        p7=pa(pm(p5,pp(p3,3)),pc(pm(pp(cub,2),pp(p4,3)),128),-1)
        p8=pc(pm(p4,pa(pm(p6,pp(p3,2)),pc(pp(p5,2),2),-1)),2)
        p9=pa(pc(pm(pp(cub,2),pm(p6,pp(p4,3))),64),pm(p3,pp(p5,3)),-1)
        xn=pa(pm(x,pp(p7,2)),pm(cub,pm(p6,p8)),-1)
        ym=pc(pa(pm(p9,pp(p6,2)),pm(p5,pp(p8,2)),-1),F(1,4))
        # Independent pair-ring recurrence retains Y, reducing only Y^2=cub.
        # No producer arithmetic or compressed even-index normalization is used.
        def ba(u,v,sign=1):return (pa(u[0],v[0],sign),pa(u[1],v[1],sign))
        def bm(u,v):return (pa(pm(u[0],v[0]),pm(cub,pm(u[1],v[1]))),pa(pm(u[0],v[1]),pm(u[1],v[0])))
        def bw(u,n):
            ans=({0:one},{})
            for _ in range(n):ans=bm(ans,u)
            return ans
        def divide2Y(u,index):
            r=dict(u[0]);quot={}
            while r and max(r)>=3:
                deg=max(r);lead=r[deg];quot[deg-3]=lead
                r=pa(r,{j+deg-3:dm(lead,w) for j,w in cub.items()},-1)
            need(not r,label+'_psi'+str(index)+'_exact_division_by_2Y')
            return (pc(u[1],F(1,2)),pc(quot,F(1,2)))
        ps={1:({0:one},{}),2:({},{0:[F(2)]}),3:(p3,{}),4:({},pc(p4,4))}
        for idx in range(5,10):
            m=idx//2
            if idx%2:ps[idx]=ba(bm(ps[m+2],bw(ps[m],3)),bm(ps[m-1],bw(ps[m+1],3)),-1)
            else:ps[idx]=divide2Y(bm(ps[m],ba(bm(ps[m+2],bw(ps[m-1],2)),bm(ps[m-2],bw(ps[m+1],2)),-1)),idx)
        compressed={5:(p5,{}),6:({},p6),7:(p7,{}),8:({},p8),9:(p9,{})}
        recurrence={}
        for idx in range(5,10):
            residual=ba(compressed[idx],ps[idx],-1)
            recurrence[str(idx)]={'even_residual':array(residual[0]),'odd_residual':array(residual[1])}
            need(not any(residual),label+'_psi'+str(idx)+'_full_pair_ring_normalization')
        phi=ba(bm((x,{}),bw(ps[7],2)),bm(ps[8],ps[6]),-1)
        omega4Y=ba(bm(ps[9],bw(ps[6],2)),bm(ps[5],bw(ps[8],2)),-1)
        need(phi==(xn,{}) and omega4Y==(pc(pm(cub,ym),4),{}),label+'_both_multiplication_coordinates_normalized')
        degrees={'psi7':[max(p7),p7[max(p7)]],'x_numerator':[max(xn),xn[max(xn)]],'y_multiplier_numerator':[max(ym),ym[max(ym)]],'required':{'psi7':[24,[7]],'x_numerator':[49,[1]],'y_multiplier_numerator':[72,[1]]}}
        save(label+'-recurrence.json',{'all_five_residuals':recurrence,'actual_and_required_degrees':degrees})
        need(max(p7)==24 and p7[24]==[7] and max(xn)==49 and xn[49]==one and max(ym)==72 and ym[72]==one,label+'_division_degrees')
        # Multiplication differential is an additional independent identity.
        need(pa(pm(pd(xn),p7),pc(pm(xn,pd(p7)),2),-1)==pc(ym,7),label+'_multiplication_differential')
        return p7,xn,ym
    def hom(p,n,A,B):
        powersA=[{0:one}];powersB=[{0:one}]
        for i in range(n):powersA.append(pm(powersA[-1],A));powersB.append(pm(powersB[-1],B))
        out={}
        for j,v in p.items():out=pa(out,pm(scalarpoly(v),pm(powersA[j],powersB[n-j])))
        return out
    q=read(old['q']);Q2=read(old['x_denominator']);NN=read(old['x_numerator']);MM=read(old['y_multiplier_numerator'])
    for label,aa,bb,innerN,innerD,innerK,innerM,outerN,outerK,outerM in [
        ('dual_after_quotient',a,b,NN,Q2,q,MM,N,k,M),
        ('quotient_after_dual',A,B,N,pc(k2,49),k,M,NN,q,MM)]:
        report['phase']=label
        p7,xn,ym=seven(aa,bb,label)
        kh=hom(outerK,3,innerN,innerD)
        den=pc(pm(innerK,kh),7)
        num=hom(outerN,7,innerN,innerD)
        ynum=pm(innerM,hom(outerM,9,innerN,innerD))
        resd=pa(den,p7,-1);resx=pa(num,xn,-1);resy=pa(ynum,ym,-1)
        save(label+'.json',{'psi7':array(p7),'multiplication_x_numerator':array(xn),'multiplication_y_multiplier_numerator':array(ym),'composition_denominator_root':array(den),'composition_x_numerator':array(num),'composition_y_multiplier_numerator':array(ynum),'denominator_residual':array(resd),'x_residual':array(resx),'y_residual':array(resy)})
        need(not resd,label+'_exact_denominator');need(not resx,label+'_full_x_composition');need(not resy,label+'_full_y_composition')
    report['phase']='reconstruction evidence'
    rec=json.loads((R/'reconstruction.json').read_text());root=read(rec['square_root_reversed']);den=read(rec['denominator_reversed']);num=read(rec['numerator_reversed'])
    need(pp(root,2)==den,'exact_reconstruction_denominator_square')
    need(array(k)==list(reversed(array(root))),'kernel_reversal')
    series=json.loads((R/'series.json').read_text());uu=read(series['U']);tt=read(series['T'])
    def trunc(p,n):return {i:v for i,v in p.items() if i<n}
    need(series['precision_S']==52 and series['precision_T']==26,'conservative_BMSS_precision')
    need(trunc(pm(uu,den),26)==num and max(num)<=7 and max(den)<=6,'all_26_Pade_coefficients')
    need(trunc(pm(pp(tt,2),uu),26)=={0:one},'full_reciprocal_series')
    deriv={i:ds(v,2*i+1) for i,v in tt.items()}
    ode=pa(pm({0:one,2:A,3:B},pp(deriv,2)),pa({0:one},pa({i+2:ds(v,-3024*7**4) for i,v in pp(tt,4).items()},{i+3:ds(v,46224*7**6) for i,v in pp(tt,6).items()})),-1)
    need(not trunc(ode,26),'all_26_ODE_coefficients')
    report['phase']='complete algebra basis and multiplication'
    # Successive monic division proves the full basis; retain all 36 products.
    basis=[({i:one},{}) for i in range(3)]+[({},{i:one}) for i in range(3)]
    table=[]
    for u in basis:
        row=[]
        for v in basis:
            even=rem(pa(pm(u[0],v[0]),pm(cc,pm(u[1],v[1]))))
            odd=rem(pa(pm(u[0],v[1]),pm(u[1],v[0])))
            row.append([array(even),array(odd)])
        table.append(row)
    save('algebra.json',{'basis_D':c['basis_D'],'basis_Q':c['basis_Q'],'monic_relations':{'k':array(k),'V_squared':array(rem(cc))},'multiplication_table':table,'kprime_unit_residual':array(pa(rem(pm(kp,read(c['kprime_inverse']))),{0:one},-1)),'curve_unit_residual':array(pa(rem(pm(cc,read(c['curve_inverse']))),{0:one},-1))})
    need(c['basis_D']==['1','T','T^2','V','TV','T^2V'] and c['basis_Q']=='Z^j T^i V^e; 0<=j<8,0<=i<3,0<=e<2','complete_monic_algebra_basis')
    report['phase']='rejections and preservation'
    rejects=[]
    for label in ['wrong-normalization','lost-sign','late-coefficient']:
        bad=copy.deepcopy(c)
        if label=='wrong-normalization':bad['x_divisor']=7
        elif label=='lost-sign':bad['normalized_M']=[[str(-F(v)) for v in row] for row in bad['normalized_M']]
        else:bad['normalized_N'][-1][0]=str(F(bad['normalized_N'][-1][0])+1)
        save(label+'.json',bad)
        try:preliminary(bad)
        except ValueError as e:rejects.append({'case':label,'rejected_at':str(e)})
        else:raise ValueError('accepted '+label)
    manifest=json.loads((R/'input-manifest.json').read_text())
    need(all(hashlib.sha256((U/p).read_bytes()).hexdigest()==v for p,v in manifest.items()),'unchanged_complete_input_bytes')
    original=json.loads((R/'original-manifest.json').read_text())
    preserved={name:hashlib.sha256((U/'dual-262'/name).read_bytes()).hexdigest()==digest for name,digest in original.items()}
    need(all(preserved.values()),'all_original_stopped_files_preserved')
    save('preservation.json',{'original_files':len(preserved),'matches':preserved})
    save('rejections.json',rejects)
    report.update(passed=True,phase='complete',etale_basis_D_dimension=6,etale_basis_Q_dimension=48,geometric_direction_fibers=8,signs_per_root=2)
except Exception as e:report['failures']=[type(e).__name__+': '+str(e)]
finally:
    signal.alarm(0);report.update(seconds=time.monotonic()-start,checks=checks);save('replay-report.json',report)
print(json.dumps({k:v for k,v in report.items() if k!='checks'}));sys.exit(0 if report['passed'] else 1)
