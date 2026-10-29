"""Independent replay in the maximal-order basis; no producer import.

The square table is recomputed modulo eight with a multiplication tensor,
not the producer's exact pi-basis squaring. Every Hensel witness is checked
again with exact rational arithmetic.
"""
from fractions import Fraction as Q
from pathlib import Path
from hashlib import sha256
import json
import traceback
import verify_two_adic_filter as v

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'shukla-quartic-pair-conics-verification.json'
R=dict(completed=False,failures=[],bindings={},checks=0,classes=[],
       full_goodness_decided=False,pairing_computed=False)


def ck(b,name):
    R['checks']+=1
    assert b,name


def read(name):
    raw=(ROOT/name).read_bytes();R['bindings'][name]=sha256(raw).hexdigest()
    return json.loads(raw)


def plus(a,b):return [x+y for x,y in zip(a,b)]
def scale(a,c):return [x*c for x in a]
def mod8(a):return [v.residue(x,8) for x in a]


def main():
    C=read('shukla-quartic-pair-conics-certificate.json')
    ck(C['completed'] and not C['failures'],'producer complete')
    ck(sha256((ROOT/'shukla_quartic_pair_conics.py').read_bytes()).hexdigest()==C['source_sha256'],'producer hash')
    ck(sha256((ROOT/'two_adic_filter.py').read_bytes()).hexdigest()==C['helper_sha256'],'producer helper hash')
    inputs={n:read(n) for n in C['bindings']}
    ck(all(R['bindings'][n]==h for n,h in C['bindings'].items()),'all input bindings')
    two=inputs['two-adic-filter-certificate.json'];F=two['field']
    ck(C['field']==F,'actual dyadic field')
    base=read('quartic-class-certificate.json')
    ck(two['bindings']['quartic-class-certificate.json']==R['bindings']['quartic-class-certificate.json'],'maximal order binding')
    v.T=base['order']['table'];PO=F['pi_to_O'];OI=F['O_to_pi']
    toO=lambda x:v.mv(PO,v.vec(x))
    v.PI=v.vec(F['pi_O']);E=list(map(Q,F['pi_polynomial']))
    v.PIINV=toO([-E[i+1]/E[0] for i in range(4)])
    ck(v.times(v.PI,v.PIINV)==v.ONE,'pi inverse')
    def fv(a):return None if not any(a) else v.normalized(a)[0]
    def fev(h,t):
        z=[Q(0)]*4
        for a in reversed(h):z=v.plus(v.times(z,t),a)
        return z
    # Full factor identity over K; irreducibility is checked at the
    # selected degree-one maximal-order place, including every residue.
    field=C['global_pair_field'];A=field['A'];h=field['residual_cubic_alpha']
    ck(A==[-109375,-32500,150,64,1] and field['order_index']==937500,'actual global field')
    alpha=v.vec([0,1,0,0]);hp=[]
    for row in h:hp.append(fev([v.scale(v.ONE,Q(x)) for x in row],alpha))
    coeff=[v.scale(v.times(alpha,hp[0]),-1)]
    coeff += [v.plus(hp[j-1],v.scale(v.times(alpha,hp[j]),-1)) for j in range(1,4)]
    coeff += [hp[3]]
    ck(coeff==[v.scale(v.ONE,x) for x in A],'global deflation identity')
    pick=field['selected'];p=pick['p'];t=pick['alpha_residue']
    ck(p in (7,13,17,19,23,29,31,37,41) and all(p%d for d in range(2,int(p**0.5)+1)),'specialization prime')
    ck(937500%p and sum(a*t**i for i,a in enumerate(A))%p==0,'degree-one maximal-order prime')
    hh=[sum(a*t**i for i,a in enumerate(row))%p for row in h]
    vv=[sum(a*x**i for i,a in enumerate(hh))%p for x in range(p)]
    ck(hh==pick['cubic'] and vv==pick['all_values'] and 0 not in vv and hh[-1]==1,'complete irreducible cubic test')
    ck(field['degree_over_K']==3 and field['degree_over_Q']==12 and field['all_ordered_quartic_pairs']==12,'whole global quartic-pair orbit')
    # Replay the entire root-disk tree, including every exclusion.
    lh=[toO(x) for x in C['local_residual_cubic']]
    ck(lh[-1]==v.ONE and v.plus(v.scale(v.ONE,E[0]),v.times(v.PI,lh[0]))==[0]*4,'local deflation constant')
    for j in range(1,4):ck(v.plus(lh[j-1],v.scale(v.times(v.PI,lh[j]),-1))==v.scale(v.ONE,E[j]),'local deflation coefficient')
    dh=[v.scale(lh[j],j) for j in range(1,4)]
    queue=[([Q(0)]*4,0)]
    for row in C['root_disks']:
        center,n=queue.pop(0);ck(center==toO(row['center']) and n==row['depth'],'complete root disk tree')
        z,d=fev(lh,center),fev(dh,center);vz,vd=fv(z),fv(d)
        ck(z==toO(row['value']) and d==toO(row['derivative']) and [vz,vd]==[row['valuation'],row['derivative_valuation']],'all root disk evaluations')
        if row['decision']=='empty':ck(vz is not None and vz<n,'empty integral root disk')
        elif row['decision']=='split':
            ck(vz is None or vz>=n,'disk not excluded')
            queue += [(center,n+1),(v.plus(center,v.powr(v.PI,n)),n+1)]
        else:ck(False,'unexpected unresolved or root-containing disk')
    ck(not queue and not C['root_certificates'],'complete absence of other roots in F')
    P=C['actual_pair_completion'];u=[toO(x) for x in P['cubic_F'][:3]]
    pi=v.PI;pi2=v.times(pi,pi);pi3=v.times(pi2,pi)
    derivative=v.plus(v.scale(v.times(pi2,pi),4),v.plus(v.scale(pi2,3*E[3]),v.plus(v.scale(pi,2*E[2]),v.scale(v.ONE,E[1]))))
    ck(v.times(u[0],pi3)==derivative,'relative cubic constant')
    ck(v.times(u[1],pi2)==v.plus(v.scale(pi2,6),v.plus(v.scale(pi,3*E[3]),v.scale(v.ONE,E[2]))),'relative cubic linear')
    ck(v.times(u[2],pi)==v.plus(v.scale(pi,4),v.scale(v.ONE,E[3])),'relative cubic quadratic')
    ck([fv(x) for x in u]==[1,4,8],'relative Eisenstein valuations')
    ck(P['degree_over_F']==3 and P['degree_over_Q2']==12 and P['ramification']==12 and P['residue_degree']==1,'actual complete pair extension')
    def conv(a):return sum((toO(a[i:i+4]) for i in range(0,12,4)),[])
    def lift(a):return a+[Q(0)]*8
    one=lift(v.ONE);s=[Q(0)]*4+v.ONE[:]+[Q(0)]*4
    def mul(a,b):
        z=[[Q(0)]*4 for _ in range(5)]
        for i in range(3):
            for j in range(3):z[i+j]=v.plus(z[i+j],v.times(a[4*i:4*i+4],b[4*j:4*j+4]))
        for k in (4,3):
            for j in range(3):z[k-3+j]=v.plus(z[k-3+j],v.scale(v.times(z[k],u[j]),-1))
        return sum(z[:3],[])
    def power(a,n):
        z=one[:]
        for _ in range(n):z=mul(z,a)
        return z
    def lv(a):
        return min((3*fv(a[i:i+4])+i//4 for i in range(0,12,4) if any(a[i:i+4])),default=None)
    def fp(a):
        pi_coords=sum((v.mv(OI,a[i:i+4]) for i in range(0,12,4)),[])
        shift=0;result=0
        for k,x in enumerate(pi_coords):
            ck(not x or v.v2(x)>=0,'integral tower coordinates')
            bits=3 if k==0 else 2
            result+=v.residue(x,2**bits)*2**shift;shift+=bits
        return result
    def tev(poly,x):
        # Direct powers, independent of producer Horner evaluation.
        return [sum(Q(c)*power(x,j)[k] for j,c in enumerate(poly)) for k in range(12)]
    second=conv(P['second_pi'])
    ck(second==mul(lift(pi),plus(one,s)) and tev(E,second)==[0]*12,'exact second root')
    ck(lv(plus(second,scale(lift(pi),-1)))==4,'second root distinct')
    # Build an independent modular multiplication tensor in O_F[s].
    basis=[[Q(i==j) for i in range(12)] for j in range(12)]
    tensor=[[mod8(mul(a,b)) for b in basis] for a in basis]
    def mm(a,b):
        result=[0]*12
        for i,x in enumerate(a):
            if not x:continue
            for j,y in enumerate(b):
                if not y:continue
                for k,c in enumerate(tensor[i][j]):result[k]+=x*y*c
        return [x%8 for x in result]
    powers=[one]
    for i in range(1,25):powers.append(mul(powers[-1],s))
    mps=[mod8(z) for z in powers];rows=[];images=set()
    for bits in range(4096):
        root=mod8(one)
        for i in range(12):
            if bits>>i&1:root=[(x+y)%8 for x,y in zip(root,mps[i+1])]
        finger=fp(mm(root,root));rows.append(finger);images.add(finger)
    table=C['pair_unit_square_table']
    ck(rows==table['rows'] and len(images)==2048==table['image_size'],'every unit-square image independently recomputed')
    ck({int(x) for x in table['roots']}==images,'complete image dictionary')
    for finger,bits in table['roots'].items():ck(rows[bits]==int(finger),'each root dictionary witness')
    # s^-1 from the defining cubic, using recorded coordinates only after
    # exact inverse verification. Gaussian solve over F is unnecessary.
    # pi=s^3 times a unit, so obtain inverse by solving its rational matrix.
    def inverse(a):
        cols=[mul(a,b) for b in basis]
        m=[[cols[j][i] for j in range(12)]+[one[i]] for i in range(12)]
        for i in range(12):
            k=next(k for k in range(i,12) if m[k][i]);m[i],m[k]=m[k],m[i]
            t=m[i][i];m[i]=[x/t for x in m[i]]
            for k in range(12):
                if k!=i:
                    t=m[k][i];m[k]=[x-t*y for x,y in zip(m[k],m[i])]
        z=[row[-1] for row in m];ck(mul(a,z)==one,'independent tower inverse');return z
    si=inverse(s)
    def sp(n):return power(s if n>=0 else si,abs(n))
    def sqcheck(h,cert):
        n=lv(h)
        if n is None:
            ck(cert['square'] and cert['zero'],'zero square');return
        ck(n==cert['valuation'],'square-test valuation')
        if n%2:ck(not cert['square'],'odd valuation nonsquare');return
        finger=fp(mul(h,sp(-n)))
        ck(finger==cert['unit_fingerprint'] and cert['square']==(finger in images),'complete local square criterion')
        if not cert['square']:return
        bits=cert['root_bits'];root=one[:]
        for i in range(12):
            if bits>>i&1:root=plus(root,powers[i+1])
        root=mul(root,sp(n//2));error=plus(mul(root,root),scale(h,-1));ev=lv(error)
        ck(root==conv(cert['root_approx']) and error==conv(cert['residual']),'entire square witness')
        ck(ev==cert['residual_valuation'] and cert['derivative_valuation']==12+n//2 and cert['threshold']==24+n,'all Hensel valuations')
        ck(ev is None or ev>24+n,'strict Hensel inequality')
    ck([(r['label'],r['mask']) for r in C['actual_pair_tests']]==[('eta_class',132102),('nu',3109)],'exact two fixed classes')
    for rec in C['actual_pair_tests']:
        b=v.ONE[:];q=Q(1)
        for j,w in enumerate(two['witnesses']):
            if rec['mask']>>j&1:
                b=v.times(b,v.vec(w['source']['coefficients']));q*=Q(w['source']['inverse_norm'])
        ck(b==toO(rec['b_pi']) and q*v.norm(b)==1,'independent full representative')
        bi=lift(b);bj=tev(rec['b_pi'],second);ti=lift(toO(F['eta_pi']));tj=tev(F['eta_pi'],second)
        a,c=mul(bi,bj),mul(plus(ti,scale(tj,-1)),bj)
        ck([bi,bj,ti,tj,a,c]==[conv(rec[k]) for k in ('bi','bj','theta_i','theta_j','a','c')],'entire actual conic coefficients')
        va,vc=lv(a),lv(c);ka,kc=va//2,vc//2
        ck([va,vc,ka,kc]==[rec[k] for k in ('a_valuation','c_valuation','a_scale','c_scale')],'all valuations and normalizations')
        aa,cc=mul(a,sp(-2*ka)),mul(c,sp(-2*kc))
        ck(aa==conv(rec['normalized_a']) and cc==conv(rec['normalized_c']),'exact square normalizations')
        sqcheck(aa,rec['a_square_test']);passed=rec['a_square_test']['square']
        for j,t in enumerate(rec['attempts']):
            ck(t['scale']==(0,1,-1,2,-2)[j//32] and t['bits']==j%32,'complete ordered candidate domain')
            root=[Q(0)]*12
            for i in range(5):
                if t['bits']>>i&1:root=plus(root,powers[i])
            root=mul(root,sp(t['scale']));h=plus(mul(aa,mul(root,root)),cc)
            sqcheck(h,t)
            if t['square']:
                ck(j==len(rec['attempts'])-1,'stop on first success');passed=True
        ck(passed and rec['soluble'] is True and len(rec['attempts'])<=160,'actual local conic certified')
        R['classes'].append(dict(label=rec['label'],soluble=True,candidates=len(rec['attempts'])))
    R['bounds']=C['bounds'];R['helper_checks']=v.R['checks'];R['max_rational_bits']=v.R['max_rational_bits']
    R['source_sha256']=sha256(Path(__file__).read_bytes()).hexdigest()
    R['completed']=True


if __name__=='__main__':
    try:main()
    except Exception as e:R['failures'].append(dict(message=str(e),traceback=traceback.format_exc()))
    OUT.write_text(json.dumps(R,indent=2,default=str)+'\n')
    print(json.dumps(dict(completed=R['completed'],failures=[e['message'] for e in R['failures']],
        checks=R['checks'],helper_checks=R.get('helper_checks'),classes=R['classes'],
        max_rational_bits=R.get('max_rational_bits'),required_bit_cap=8192,path=str(OUT))))
    raise SystemExit(0 if R['completed'] else 1)
