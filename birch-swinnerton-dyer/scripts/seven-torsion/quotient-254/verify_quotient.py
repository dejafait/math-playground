"""Independent exact replay. No producer arithmetic or producer import."""
from fractions import Fraction as F
from pathlib import Path
import hashlib,json,signal,sys,time
R=Path(__file__).resolve().parent;U=R.parent
sys.path.insert(0,str(U))
import verify_certificate as V

def verify(cert,checks):
    def need(ok,label):
        if not ok:raise ValueError(label)
        checks.append(label)
    d=json.loads((U/'compressed-249/direction.json').read_text())
    need(cert['schema']=='389-direction-seven-quotient-v1','schema')
    need(cert['direction_sha256']==hashlib.sha256((U/'compressed-249/direction.json').read_bytes()).hexdigest(),'audited_direction_hash')
    h=list(map(F,d['h']))
    def norm(a):return V.remainder(a,h)
    def da(a,b,sign=1):return V.plus(a,b,sign)
    def dm(a,b):return norm(V.times(a,b))
    def ds(a,k):return V.scalar(a,k)
    def de(a,n):
        out=[F(1)]
        for _ in range(n):out=dm(out,a)
        return out
    def dc(a):
        out=list(map(F,a));need(len(out)<=8,'D_coefficient_bound')
        return norm(out)
    def read(p):return {i:v for i,a in enumerate(p) if (v:=dc(a))}
    def pa(p,r,sgn=1):
        out=dict(p)
        for i,a in r.items():
            b=da(out.get(i,[]),a,sgn)
            if b:out[i]=b
            else:out.pop(i,None)
        return out
    def pm(p,r):
        out={}
        for i,a in p.items():
            for j,b in r.items():
                v=da(out.get(i+j,[]),dm(a,b))
                if v:out[i+j]=v
                else:out.pop(i+j,None)
        return out
    def ps(p,k):return {i:v for i,a in p.items() if (v:=ds(a,k))}
    def pp(p,n):
        r={0:[F(1)]}
        for _ in range(n):r=pm(r,p)
        return r
    def pd(p):return {i-1:ds(a,i) for i,a in p.items() if i}
    q=read(d['cubic']);need(read(cert['q'])==q and list(map(F,cert['h']))==h,'whole_audited_field_and_cubic')
    need(q.get(3)==[1] and max(q)==3,'monic_full_kernel_cubic')
    c={0:[F(46224)],1:[F(-3024)],3:[F(1)]};qp=pd(q)
    def rem(p):
        out=dict(p)
        while out and max(out)>=3:
            i=max(out);v=out[i];out=pa(out,{j+i-3:dm(v,a) for j,a in q.items()},-1)
        return out
    invqp=read(cert['qprime_inverse_mod_q']);invc=read(cert['c_inverse_mod_q'])
    need(max(invqp,default=0)<3 and rem(pm(qp,invqp))=={0:[1]},'full_cubic_squarefree_inverse')
    need(max(invc,default=0)<3 and rem(pm(c,invc))=={0:[1]},'full_kernel_disjoint_from_two_torsion')
    units=cert['constant_inverses'];need(bool(units),'constant_unit_witnesses_present')
    for i,w in enumerate(units):need(dm(dc(w['value']),dc(w['inverse']))==[1],'constant_unit_'+str(i))
    for k in [2,3,4,5,6,7,16]:need(any(dc(w['value'])==[k] for w in units),'rational_constant_'+str(k))
    need(F(cert['source_a'])==-3024 and F(cert['source_b'])==46224,'unchanged_short_source')
    ap=dc(cert['target_a']);bp=dc(cert['target_b'])
    disc=ds(da(ds(de(ap,3),4),ds(de(bp,2),27)),-16)
    need(dc(cert['target_discriminant'])==disc and dm(disc,dc(cert['target_discriminant_inverse']))==[1],'target_discriminant_unit')
    # Traces in the entire cubic algebra are obtained from multiplication
    # matrices on (1,u,u^2), not from the producer's symmetric-sum formulas.
    traces=[]
    for k in range(10):
        tr=[]
        for j in range(3):tr=da(tr,rem({k+j:[F(1)]}).get(j,[]))
        traces.append(tr)
    need(traces[0]==[3],'trace_rank_three')
    t=da(ds(traces[2],6),[F(-18144)])
    w=da(da(ds(traces[3],10),ds(traces[1],-18144)),[F(554688)])
    need(ap==da([F(-3024)],ds(t,5),-1) and bp==da([F(46224)],ds(w,7),-1),'paired_Velu_target_coefficients')
    N=read(cert['x_numerator']);M=read(cert['y_multiplier_numerator'])
    q2=pp(q,2);q3=pp(q,3)
    need(read(cert['x_denominator'])==q2 and read(cert['y_multiplier_denominator'])==q3,'both_complete_denominators')
    # Bivariate sparse arithmetic in free x,u. Coefficients are in full D.
    def ba(p,r,sgn=1):
        out=dict(p)
        for ij,a in r.items():
            v=da(out.get(ij,[]),a,sgn)
            if v:out[ij]=v
            else:out.pop(ij,None)
        return out
    def bm(p,r):
        out={}
        for (i,j),a in p.items():
            for (k,l),b in r.items():
                ij=(i+k,j+l);v=da(out.get(ij,[]),dm(a,b))
                if v:out[ij]=v
                else:out.pop(ij,None)
        return out
    def bs(p,k):return {ij:v for ij,a in p.items() if (v:=ds(a,k))}
    def bx(p):return {(i,0):a for i,a in p.items()}
    def bu(p):return {(0,i):a for i,a in p.items()}
    def trace(p):
        out={}
        for (i,j),a in p.items():out=pa(out,{i:dm(a,traces[j])})
        return out
    A={(2,0):[F(1)],(1,1):[F(1)],(0,2):[F(1)]}
    A=ba(ba(A,{(1,0):q.get(2,[]),(0,1):q.get(2,[])}),{(0,0):q.get(1,[])})
    need(ba(bm({(1,0):[F(1)],(0,1):[F(-1)]},A),bu(q))==bx(q),'full_divided_difference_identity')
    cu=bu(c);cx=bx(c);g={(0,2):[F(6)],(0,0):[F(-6048)]}
    paired_x=trace(ba(bm(bm(g,A),bx(q)),bs(bm(cu,bm(A,A)),4)))
    need(N==pa(pm({1:[F(1)]},q2),paired_x),'full_paired_Velu_x_sum')
    # Sum y(P+Q)+y(P-Q) directly from the secant law, divided by Y:
    # -2 + 2(2x+u)/(x-u) - (2c(x)+6c(u))/(x-u)^3.
    ycorr=bs(bx(q3),-2)
    ycorr=ba(ycorr,bs(bm(bm({(1,0):[F(2)],(0,1):[F(1)]},A),bx(q2)),2))
    ycorr=ba(ycorr,bm(ba(bs(cx,2),bs(cu,6)),bm(bm(A,A),A)),-1)
    need(M==pa(q3,trace(ycorr)),'full_both_signs_Velu_y_sum')
    need(pm(M,q)==pa(pm(pd(N),q2),pm(N,pd(q2)),-1),'normalized_differential_identity')
    # Use M=N'q-2Nq' as a separate polynomial identity too.
    need(M==pa(pm(pd(N),q),ps(pm(N,qp),2),-1),'derivative_multiplier_all_coefficients')
    rhs=pa(pa(pp(N,3),pm({0:ap},pm(N,pp(q,4)))),pm({0:bp},pp(q,6)))
    need(pm(c,pp(M,2))==rhs,'entire_cleared_target_curve_equation')
    nrem=rem(N);mrem=rem(M)
    need(nrem==rem(ps(pm(c,pp(qp,2)),4)),'kernel_x_leading_pole_coefficient')
    need(mrem==rem(ps(pm(N,qp),-2)),'kernel_y_leading_pole_coefficient')
    ninv=rem(ps(pm(invc,pp(invqp,2)),F(1,4)))
    need(rem(pm(N,ninv))=={0:[1]},'whole_numerator_denominator_coprimality')
    minv=rem(ps(pm(ninv,invqp),F(-1,2)))
    need(rem(pm(M,minv))=={0:[1]},'all_six_kernel_y_poles_nonzero')
    need(max(N)==7 and N[7]==[1] and max(q2)==6 and q2[6]==[1],'x_map_exact_degree_seven')
    need(max(M)==9 and M[9]==[1] and max(q3)==9 and q3[9]==[1],'O_leading_terms_and_differential_scale_one')
    return {'passed':True,'checks':checks,'failures':[],'field_degree':8,'required_field_degree':8,'x_map_degree':7,'required_degree':7,
            'finite_kernel_points':6,'required_finite_kernel_points':6,'kernel_including_O':7,'differential_scalar':'1',
            'exceptional_scope':'q squarefree; c,qprime,N,M units modulo q; local finite poles (2,3); O leading terms (x,Y)',
            'scope':'short-model fixed quotient only; separate critical audit pending'}

def main():
    start=time.monotonic();checks=[];report={'passed':False,'phase':'initialization'}
    signal.signal(signal.SIGALRM,lambda *_: (_ for _ in ()).throw(TimeoutError('180-second independent replay cap')));signal.alarm(180)
    def save(name,v):
        s=json.dumps(v,separators=(',',':'))+'\n'
        assert sum(p.stat().st_size for p in R.rglob('*') if p.is_file())+len(s.encode())<=134217728,'byte cap'
        with (R/name).open('x') as f:f.write(s)
    try:
        originals={str(p.relative_to(U)):hashlib.sha256(p.read_bytes()).hexdigest() for p in U.rglob('*') if p.is_file() and '__pycache__' not in p.parts and R not in p.parents}
        originals.update({str(p.relative_to(U)):hashlib.sha256(p.read_bytes()).hexdigest() for p in R.iterdir() if p.is_file() and p.name not in ['verify_quotient.log']})
        prior=json.loads((R/'production-input-manifest.json').read_text())
        if any(not (U/p).is_file() or hashlib.sha256((U/p).read_bytes()).hexdigest()!=v for p,v in prior.items()):raise ValueError('production changed upstream bytes')
        save('original-manifest.json',originals)
        cert=json.loads((R/'quotient.json').read_text());report=verify(cert,checks);save('complete-replay.json',report)
        rejects=[]
        for name,label,edit in [
            ('wrong-x','full_paired_Velu_x_sum',lambda c:c['x_numerator'][0].__setitem__(0,str(F(c['x_numerator'][0][0])+1))),
            ('wrong-discriminant-inverse','target_discriminant_unit',lambda c:c['target_discriminant_inverse'].__setitem__(0,str(F(c['target_discriminant_inverse'][0])+1)))]:
            fixture=json.loads(json.dumps(cert));edit(fixture);save(name+'.json',fixture)
            try:verify(fixture,[]);raise AssertionError('altered evidence accepted')
            except ValueError as e:
                if str(e)!=label:raise AssertionError('wrong rejection '+str(e))
                rejects.append({'fixture':name+'.json','expected':label,'actual':str(e),'passed':True})
        changed=[p for p,digest in originals.items() if not (U/p).exists() or hashlib.sha256((U/p).read_bytes()).hexdigest()!=digest]
        if changed:raise ValueError('original bytes changed: '+str(changed))
        save('rejections-and-preservation.json',{'passed':True,'rejections':rejects,'original_file_count':len(originals),'changed_or_missing':changed})
        report.update(rejections_passed=len(rejects),original_file_count=len(originals),seconds=time.monotonic()-start,required_seconds=180)
    except Exception as e:report={'passed':False,'checks':checks,'failures':[type(e).__name__+': '+str(e)],'seconds':time.monotonic()-start,'required_seconds':180}
    finally:signal.alarm(0);save('replay-stage-report.json',report)
    print(json.dumps({k:v for k,v in report.items() if k!='checks'}));return 0 if report['passed'] else 1
if __name__=='__main__':sys.exit(main())
