"""Fixed quartic/quartic gate: certified embedded dyadic pairs only.

No negative decision is made from a root or point search failure. The other
completions of the global degree-twelve pair field remain separate.
"""
from fractions import Fraction as Q
from pathlib import Path
from hashlib import sha256
import json
import traceback
import two_adic_filter as f

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'shukla-quartic-pair-conics-certificate.json'
D=dict(completed=False,failures=[],bindings={},checks=0,classes=[],
       root_disks=[],root_certificates=[],full_goodness_decided=False,
       pairing_computed=False,bounds=dict(root_depth_cap=32,root_disks_cap=8192,
       root_disks_actual=0,root_depth_actual=0,conic_candidates_cap_per_pair=2560,
       conic_candidates_actual=0,rational_bits_cap=8192))


def ck(ok,name):
    D['checks']+=1
    assert ok,name


def read(name):
    raw=(ROOT/name).read_bytes();D['bindings'][name]=sha256(raw).hexdigest()
    return json.loads(raw)


def val(a):
    return min((4*f.v2(x)+i for i,x in enumerate(a) if x),default=None)


def ppow(n):return f.power(f.PI if n>=0 else f.PIINV,abs(n))
def neg(a):return f.scale(a,-1)
def sub(a,b):return f.add(a,neg(b))


def ev(h,t):
    z=[Q(0)]*4
    for a in reversed(h):z=f.add(f.mul(z,t),a)
    return z


def inv(a):
    cols=[f.mul(a,[Q(i==j) for i in range(4)]) for j in range(4)]
    m=[[cols[j][i] for j in range(4)] for i in range(4)]
    z=[sum(row[j]*f.ONE[j] for j in range(4)) for row in f.invmat(m)]
    ck(f.mul(a,z)==f.ONE,'exact inverse')
    return z


def finite_factor():
    # A(X)=(X-alpha)h(X), with coefficients in ascending order.
    A=[-109375,-32500,150,64,1]
    h=[[-32500,150,64,1],[150,64,1,0],[64,1,0,0],[1,0,0,0]]
    # A root modulo a prime not dividing the order index gives a residue
    # degree-one maximal-order place. Irreducible monic reduction of h
    # there proves h irreducible over K.
    scans=[];selected=None
    for p in (7,13,17,19,23,29,31,37,41):
        roots=[t for t in range(p) if sum(a*t**i for i,a in enumerate(A))%p==0]
        for t in roots:
            coeff=[sum(a*t**i for i,a in enumerate(row))%p for row in h]
            values=[sum(a*x**i for i,a in enumerate(coeff))%p for x in range(p)]
            rec=dict(p=p,alpha_residue=t,cubic=coeff,all_values=values,
                     derivative=sum(i*A[i]*t**(i-1) for i in range(1,5))%p)
            scans.append(rec)
            if 0 not in values and rec['derivative'] and 937500%p:
                selected=rec;break
        if selected:break
    ck(selected is not None,'degree-preserving irreducible cubic specialization')
    D['global_pair_field']=dict(A=A,residual_cubic_alpha=h,
        order_index=937500,irreducibility_scans=scans,selected=selected,
        degree_over_K=3,degree_over_Q=12,
        all_ordered_quartic_pairs=12)


def square(h,roots):
    n=val(h)
    if n is None:return dict(square=True,zero=True,root_approx=[Q(0)]*4)
    if n%2:return dict(square=False,valuation=n)
    u=f.mul(h,ppow(-n));r=f.reduce_pi(u)
    if str(r) not in roots:return dict(square=False,valuation=n,unit_residue=r)
    s=roots[str(r)];z=f.mul(ppow(n//2),f.from_digits(s))
    error=sub(f.mul(z,z),h);e=val(error);dv=4+n//2
    ck(e is None or e>2*dv,'strict square Hensel inequality')
    return dict(square=True,zero=False,valuation=n,unit_residue=r,
                digit_root=s,root_approx=z,residual=error,
                residual_valuation=e,derivative_valuation=dv,threshold=2*dv)


class Tower:
    """L=F[s], a cubic Eisenstein extension, in pi^j*s^i basis."""
    def __init__(self,h):
        self.h=h
        self.one=f.ONE[:]+[Q(0)]*8
        self.s=[Q(0)]*4+f.ONE[:]+[Q(0)]*4
        self.si=self.scale(self.h[1],-1)+self.scale(self.h[2],-1)+[-Q(1),0,0,0]
        self.si=self.fm(self.si,inv(self.h[0]))
        ck(self.mul(self.s,self.si)==self.one,'tower uniformizer inverse')
    @staticmethod
    def add(a,b):return [x+y for x,y in zip(a,b)]
    @staticmethod
    def scale(a,c):return [x*c for x in a]
    @staticmethod
    def fm(a,c):return sum((f.mul(a[i:i+4],c) for i in range(0,12,4)),[])
    @staticmethod
    def lift(a):return a+[Q(0)]*8
    def mul(self,a,b):
        z=[[Q(0)]*4 for _ in range(5)]
        for i in range(3):
            for j in range(3):z[i+j]=f.add(z[i+j],f.mul(a[4*i:4*i+4],b[4*j:4*j+4]))
        for k in (4,3):
            for j in range(3):z[k-3+j]=sub(z[k-3+j],f.mul(z[k],self.h[j]))
        return sum(z[:3],[])
    def power(self,a,n):
        z=self.one[:]
        while n:
            if n%2:z=self.mul(z,a)
            a=self.mul(a,a);n//=2
        return z
    def spow(self,n):return self.power(self.s if n>=0 else self.si,abs(n))
    @staticmethod
    def val(a):
        return min((12*f.v2(x)+3*(k%4)+k//4 for k,x in enumerate(a) if x),default=None)
    @staticmethod
    def fingerprint(a):
        # pi^j*s^i has weight 3j+i; unique weights 0,...,11.
        # Congruence modulo s^25 is coordinatewise modulo 8 (weight0)
        # and modulo4 (all other weights).
        z=0;shift=0
        for k,x in enumerate(a):
            modulus=8 if k==0 else 4
            ck(not x or f.v2(x)>=0,'integral tower residue input')
            digit=x.numerator*pow(x.denominator,-1,modulus)%modulus
            z|=digit<<shift;shift+=3 if k==0 else 2
        return z
    def eval(self,poly,t):
        z=[Q(0)]*12
        for x in reversed(poly):z=self.add(self.mul(z,t),self.scale(self.one,x))
        return z


def full_dyadic_pairs(two,old):
    pi=f.PI;pi2=f.mul(pi,pi);pi3=f.mul(pi2,pi)
    derivative=f.add(f.add(f.scale(f.mul(pi2,pi),4),f.scale(pi2,3*f.E[3])),f.add(f.scale(pi,2*f.E[2]),[f.E[1],0,0,0]))
    u0=f.mul(derivative,ppow(-3))
    u1=f.add([Q(6),0,0,0],f.add(f.scale(ppow(-1),3*f.E[3]),f.scale(ppow(-2),f.E[2])))
    u2=f.add([Q(4),0,0,0],f.scale(ppow(-1),f.E[3]))
    ck([val(u0),val(u1),val(u2)]==[1,4,8],'relative cubic Eisenstein valuations')
    T=Tower([u0,u1,u2])
    second=T.fm(T.add(T.one,T.s),pi)
    ck(T.eval(f.E,second)==[0]*12,'actual second E root')
    ck(T.val(T.add(second,T.scale(T.lift(pi),-1)))==4,'distinct second root gap')
    D['actual_pair_completion']=dict(cubic_F=[u0,u1,u2,f.ONE],
        coefficient_F_valuations=[1,4,8,0],degree_over_F=3,degree_over_Q2=12,
        ramification=12,residue_degree=1,uniformizer='s=(pi_second-pi)/pi',
        basis='pi^j*s^i, flattened i=0..2 then j=0..3',second_pi=second,
        square_precision=25,unit_root_precision=13)
    powers=[T.spow(i) for i in range(25)]
    squares={};rows=[]
    for bits in range(4096):
        z=T.one[:]
        for i in range(12):
            if bits>>i&1:z=T.add(z,powers[i+1])
        image=T.fingerprint(T.mul(z,z));squares.setdefault(image,bits)
        rows.append(image)
    ck(len(rows)==4096 and len(squares)==2048,'complete tower unit-square image')
    D['pair_unit_square_table']=dict(rows=rows,image_size=len(squares),roots=squares)

    def sq(h):
        n=T.val(h)
        if n is None:return dict(square=True,zero=True,root_approx=[Q(0)]*12)
        if n%2:return dict(square=False,valuation=n)
        normalized=T.mul(h,T.spow(-n));finger=T.fingerprint(normalized)
        if finger not in squares:return dict(square=False,valuation=n,unit_fingerprint=finger)
        bits=squares[finger];r=T.one[:]
        for i in range(12):
            if bits>>i&1:r=T.add(r,powers[i+1])
        r=T.mul(r,T.spow(n//2));error=T.add(T.mul(r,r),T.scale(h,-1))
        ev=T.val(error);dv=12+n//2
        ck(ev is None or ev>2*dv,'tower strict square Hensel')
        return dict(square=True,zero=False,valuation=n,unit_fingerprint=finger,
            root_bits=bits,root_approx=r,residual=error,residual_valuation=ev,
            derivative_valuation=dv,threshold=2*dv)

    for cl in old['classes']:
        b=f.matvec(two['field']['alpha_to_pi'],list(map(Q,cl['quartic_power'])))
        bi=T.lift(b);bj=T.eval(b,second)
        theta=list(map(Q,two['field']['eta_pi']))
        ti=T.lift(theta);tj=T.eval(theta,second)
        # Square-equivalent quaternion entries: multiply each by bj^2.
        a=T.mul(bi,bj);c=T.mul(T.add(ti,T.scale(tj,-1)),bj)
        va,vc=T.val(a),T.val(c);ka,kc=va//2,vc//2
        aa,cc=T.mul(a,T.spow(-2*ka)),T.mul(c,T.spow(-2*kc))
        rec=dict(label=cl['label'],mask=cl['mask'],b_pi=b,bi=bi,bj=bj,
            theta_i=ti,theta_j=tj,a=a,c=c,a_valuation=va,c_valuation=vc,
            a_scale=ka,c_scale=kc,normalized_a=aa,normalized_c=cc,
            a_square_test=sq(aa),attempts=[],soluble=None,good=None)
        D.setdefault('actual_pair_tests',[]).append(rec)
        if rec['a_square_test']['square']:
            rec.update(soluble=True,reason='a is a square; projective point at infinity')
            continue
        for scale in (0,1,-1,2,-2):
            for bits in range(32):
                v=[Q(0)]*12
                for i in range(5):
                    if bits>>i&1:v=T.add(v,powers[i])
                v=T.mul(v,T.spow(scale))
                h=T.add(T.mul(aa,T.mul(v,v)),cc);cert=sq(h)
                rec['attempts'].append(dict(scale=scale,bits=bits,**cert))
                if cert['square']:
                    rec.update(soluble=True,reason='strict Hensel conic point');break
            if rec['soluble']:break
        if rec['soluble'] is None:rec['reason']='bounded conic search inconclusive'
    D['bounds'].update(pair_unit_root_candidates_actual=4096,pair_unit_root_candidates_required=4096,
        pair_unit_square_precision_actual=25,pair_unit_square_precision_required=25,
        actual_pair_conic_candidates_cap_per_class=160,
        actual_pair_conic_candidates_actual=sum(len(r['attempts']) for r in D['actual_pair_tests']))


def main():
    old=read('shukla-good-conics-certificate.json')
    two=read('two-adic-filter-certificate.json')
    audit=read('two-adic-filter-audit.json')
    for c in (old,two,audit):ck(c['completed'] and not c['failures'],'accepted input')
    ck(audit['bindings']['two-adic-filter-certificate.json']==D['bindings']['two-adic-filter-certificate.json'],'dyadic audit binding')
    f.E=list(map(Q,two['field']['pi_polynomial']))
    f.PIINV=[-f.E[i+1]/f.E[0] for i in range(4)]
    ck(f.E==list(map(Q,[5850,-8442,1272,-64,1])),'actual field')
    ck(f.mul(f.PI,f.PIINV)==f.ONE,'uniformizer inverse')
    D['field']=two['field'];finite_factor()
    # Deflate E at pi by synthetic division in the exact quartic field.
    h=[None]*4;h[3]=f.ONE[:]
    for j in (2,1,0):h[j]=f.add([f.E[j+1],0,0,0],f.mul(f.PI,h[j+1]))
    ck(f.add([f.E[0],0,0,0],f.mul(f.PI,h[0]))==[0]*4,'exact local deflation')
    dh=[f.scale(h[j],j) for j in range(1,4)]
    D['local_residual_cubic']=h
    # All integral roots have a digit expansion. A certified disk is
    # removed when strict Hensel gives exactly one root in that disk.
    disks=[([Q(0)]*4,0)]
    while disks:
        t,n=disks.pop(0);D['bounds']['root_disks_actual']+=1
        ck(D['bounds']['root_disks_actual']<=8192,'root disk cap')
        D['bounds']['root_depth_actual']=max(n,D['bounds']['root_depth_actual'])
        z,d=ev(h,t),ev(dh,t);v,dv=val(z),val(d)
        rec=dict(center=t,depth=n,value=z,valuation=v,derivative=d,derivative_valuation=dv)
        D['root_disks'].append(rec)
        if v is not None and v<n:
            rec['decision']='empty';continue
        if dv is not None and (v is None or v>2*dv) and n>dv:
            err=None if v is None else v-dv
            ck(err is None or err>=n,'root error inside disk')
            gap=val(sub(t,f.PI))
            ck(gap is not None and (err is None or err>gap),'distinct root from original pi')
            rec.update(decision='one_root',root_error_lower=err,gap_valuation=gap)
            D['root_certificates'].append(rec.copy());continue
        if n==32:
            rec['decision']='unresolved_depth_cap';continue
        rec['decision']='split'
        disks.extend([(t,n+1),(f.add(t,ppow(n)),n+1)])
    ck(len(D['root_certificates'])<=3,'cubic root count')
    roots=two['square_table']['square_roots']
    for s,z in two['square_table']['square_rows']:
        ck(f.reduce_pi(f.mul(f.from_digits(s),f.from_digits(s)))==z,'accepted square row')
    ck(len(two['square_table']['square_rows'])==256 and len(roots)==8,'complete square table')
    transform=two['field']['alpha_to_pi'];eta=list(map(Q,two['field']['eta_pi']))
    for cl in old['classes']:
        q=Q(1);b=f.ONE[:]
        for j,w in enumerate(two['witnesses']):
            if cl['mask']>>j&1:
                q*=Q(w['source']['inverse_norm'])
                b=f.mul(b,f.matvec(two['field']['O_to_pi'],list(map(Q,w['source']['coefficients']))))
        ck(q==Q(cl['rational']) and b==f.matvec(transform,list(map(Q,cl['quartic_power']))),'full representative')
        rec=dict(label=cl['label'],mask=cl['mask'],rational=q,b_pi=b,pairs=[],good=None)
        D['classes'].append(rec)
        for j,root in enumerate(D['root_certificates']):
            t=list(map(Q,root['center']));error=root['root_error_lower']
            # Refine the actual other uniformizer root until coefficient
            # errors are beyond the complete square-class threshold.
            refinements=[]
            for k in range(4):
                bj=ev([[x,0,0,0] for x in b],t)
                tj=ev([[x,0,0,0] for x in eta],t)
                aa=f.mul(b,inv(bj));cc=f.mul(sub(eta,tj),inv(bj))
                va,vc,vb=val(aa),val(cc),val(bj)
                eb=None if error is None else error+min(f.v2(x)*4 for x in b if x)
                et=None if error is None else error+min(f.v2(x)*4 for x in eta if x)
                # b(t)-b(root) and eta(t)-eta(root) error bounds use
                # integral arguments. Inverse/product errors then follow.
                ea=None if eb is None else va+eb-vb
                ec=None if eb is None else min(et-vb,vc+eb-vb)
                stable=error is None or (eb>vb and ea>va+8 and ec>vc+8)
                refinements.append(dict(center=t,root_error_lower=error,bj=bj,tj=tj,
                    a=aa,c=cc,a_valuation=va,c_valuation=vc,bj_valuation=vb,
                    b_error_lower=eb,theta_error_lower=et,a_error_lower=ea,c_error_lower=ec,stable=stable))
                if stable:break
                z,d=ev(h,t),ev(dh,t);t=sub(t,f.mul(z,inv(d)))
                vz,vd=val(ev(h,t)),val(ev(dh,t))
                ck(vz is None or vz>2*vd,'Newton strict Hensel')
                error=None if vz is None else vz-vd
            test=dict(root_index=j,refinements=refinements,stable=stable,soluble=None,attempts=[])
            rec['pairs'].append(test)
            if not stable:continue
            ka,kc=va//2,vc//2
            a,c=f.mul(aa,ppow(-2*ka)),f.mul(cc,ppow(-2*kc))
            test.update(a_scale=ka,c_scale=kc,normalized_a=a,normalized_c=c)
            for scale in (0,1,-1,2,-2):
                for digit in range(512):
                    vv=f.mul(ppow(scale),f.from_digits(digit));hh=f.add(f.mul(a,f.mul(vv,vv)),c)
                    cert=square(hh,roots)
                    test['attempts'].append(dict(scale=scale,digit=digit,**cert))
                    D['bounds']['conic_candidates_actual']+=1
                    if cert['square']:
                        test['soluble']=True;break
                if test['soluble']:break
            # Passing refers to the exact root: a/aa and c/cc are squares
            # by the strict coefficient bounds and Local Square Theorem.
            test['meaning']='exact embedded conic soluble' if test['soluble'] else 'bounded point search inconclusive'
    full_dyadic_pairs(two,old)
    D['bounds']['helper_rational_bits_actual']=f.D['bounds']['max_rational_bits']
    def bits(x):
        if isinstance(x,dict):return max([0]+[bits(z) for z in x.values()])
        if isinstance(x,list):return max([0]+[bits(z) for z in x])
        try:
            if isinstance(x,bool):return 0
            z=Q(x)
            return max(abs(z.numerator).bit_length(),z.denominator.bit_length())
        except (ValueError,TypeError,ZeroDivisionError):return 0
    D['bounds']['saved_rational_bits_actual']=bits(D)
    ck(D['bounds']['saved_rational_bits_actual']<=8192,'entire saved rational bit cap')
    D['source_sha256']=sha256(Path(__file__).read_bytes()).hexdigest()
    D['helper_sha256']=sha256((ROOT/'two_adic_filter.py').read_bytes()).hexdigest()
    D['completed']=True


if __name__=='__main__':
    try:main()
    except Exception as e:D['failures'].append(dict(message=str(e),traceback=traceback.format_exc()))
    OUT.write_text(json.dumps(D,indent=2,default=str)+'\n')
    print(json.dumps(dict(completed=D['completed'],failures=[e['message'] for e in D['failures']],
        roots=len(D['root_certificates']),unresolved_disks=sum(r['decision']=='unresolved_depth_cap' for r in D['root_disks'] if 'decision' in r),
        classes=[dict(label=c['label'],pairs=[dict(root=p['root_index'],stable=p['stable'],soluble=p['soluble'],candidates=len(p['attempts'])) for p in c['pairs']]) for c in D['classes']],
        actual_pair_tests=[dict(label=c['label'],soluble=c['soluble'],reason=c['reason'],candidates=len(c['attempts'])) for c in D.get('actual_pair_tests',[])],
        bounds=D['bounds'],path=str(OUT))))
    raise SystemExit(0 if D['completed'] else 1)
