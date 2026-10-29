"""Replay the complete dyadic evidence in the maximal-order basis.

No producer import. Valuations use repeated uniformizer division rather
than the producer's weighted minimum in pi coordinates.
"""
from fractions import Fraction as Q
from pathlib import Path
from hashlib import sha256
import json
import traceback
import verify_two_adic_filter as v

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'shukla-dyadic-conics-verification.json'
R=dict(completed=False,failures=[],bindings={},checks=0,classes=[],
       full_goodness_decided=False,pairing_computed=False,
       bounds=dict(classes_required=2,classes_actual=0,candidates_actual=0,
                   candidates_cap_per_class=2560,rational_bits_cap=8192))


def ck(test,name):
    R['checks']+=1
    assert test,name


def read(name):
    raw=(ROOT/name).read_bytes();R['bindings'][name]=sha256(raw).hexdigest()
    return json.loads(raw)


def ppow(n):return v.powr(v.PI if n>=0 else v.PIINV,abs(n))
def neg(a):return v.scale(a,-1)
def val(a):return None if not any(a) else v.normalized(a)[0]


def main():
    C=read('shukla-dyadic-conics-certificate.json')
    ck(C['completed'] and not C['failures'],'producer completion')
    ck(sha256((ROOT/'shukla_dyadic_conics.py').read_bytes()).hexdigest()==C['source_sha256'],'producer binding')
    ck(sha256((ROOT/'two_adic_filter.py').read_bytes()).hexdigest()==C['helper_sha256'],'helper binding')
    inputs={n:read(n) for n in C['bindings']}
    ck(all(R['bindings'][n]==h for n,h in C['bindings'].items()),'all input bindings')
    two=inputs['two-adic-filter-certificate.json'];F=two['field']
    base=read('quartic-class-certificate.json')
    ck(two['bindings']['quartic-class-certificate.json']==R['bindings']['quartic-class-certificate.json'],'same maximal order')
    ck(C['field']==F,'entire local field binding')
    v.T=base['order']['table'];v.PI=v.vec([1,0,1,0])
    PO=[list(map(Q,row)) for row in F['pi_to_O']]
    OI=[list(map(Q,row)) for row in F['O_to_pi']]
    E=list(map(Q,F['pi_polynomial']))
    v.PIINV=v.mv(PO,[-E[i+1]/E[0] for i in range(4)])
    toO=lambda z:v.mv(PO,v.vec(z))
    ck(v.times(v.PI,v.PIINV)==v.ONE,'actual pi inverse')
    for j in range(4):
        e=[Q(i==j) for i in range(4)]
        ck(toO(e)==ppow(j),'all basis powers')
        ck(v.mv(OI,toO(e))==e,'basis inverses')
    ck(E==list(map(Q,[5850,-8442,1272,-64,1])),'actual Eisenstein polynomial')
    ck(v.integral([E[0]/2]) and v.v2(E[0])==1 and all(c%2==0 for c in E[:4]),'Eisenstein')
    ck([sum(E[j]*ppow(j)[i] for j in range(5)) for i in range(4)]==[0]*4,'polynomial annihilation')
    ck(v.integral([x for row in PO+OI for x in row]),'whole local order identification')
    eta=toO(F['eta_pi'])
    ck(v.times(eta,v.plus([0,1,0,0],[-50,0,0,0]))==[-907500,0,0,0],'actual eta')
    gap=v.plus(v.scale(v.ONE,9075),neg(eta));outside=C['outside_support']
    ck(toO(outside['gap_pi'])==gap,'complete branch-gap coefficients')
    ck(v.norm(gap)==Q(outside['gap_norm'])==73990352390625==3**5*5**6*11**7,'independent gap norm support')
    ck(outside['gap_norm_factorization']=={'3':5,'5':6,'11':7} and outside['allowed_rational_primes']==[2,3,5,11],'exact outside-support domain')
    reps=[]
    for d in range(512):
        z=[sum(((d>>j)&1)*ppow(j)[i] for j in range(9)) for i in range(4)]
        ck(v.digits(z)==d,'all 512 residues independently enumerated')
        reps.append(z)
    squares={}
    ck(len(C['square_rows'])==256,'all unit roots required')
    for j,(s,d) in enumerate(C['square_rows']):
        ck(s==2*j+1,'complete unit-root domain')
        got=v.digits(v.times(reps[s],reps[s]));squares.setdefault(got,s)
        ck(got==d,'independent unit square')
    ck(len(squares)==8 and set(squares)=={int(x) for x in C['square_roots']},'complete unit-square image')
    for d,s in C['square_roots'].items():
        ck(v.digits(v.times(reps[s],reps[s]))==int(d),'every used residue root')
    old=inputs['shukla-good-conics-certificate.json']
    ck([(r['label'],r['mask']) for r in C['classes']]==[('eta_class',132102),('nu',3109)],'exact ordered domain')
    for rec,oldrec in zip(C['classes'],old['classes']):
        q=Q(1);b=v.ONE[:]
        for j,w in enumerate(two['witnesses']):
            if rec['mask']>>j&1:
                q*=Q(w['source']['inverse_norm']);b=v.times(b,v.vec(w['source']['coefficients']))
        ck(q==Q(rec['rational'])==Q(oldrec['rational']) and b==toO(rec['b_pi']),'independent full representative')
        ck(q*v.norm(b)==1,'norm one authentication')
        ck(q.numerator==1 and set(rec['q_denominator_factorization'])=={'2','3','5','11'},'exact rational support domain')
        denominator=1
        for p,e in rec['q_denominator_factorization'].items():
            ck(isinstance(e,int) and e>=0,'nonnegative factor exponents')
            denominator*=int(p)**e
        ck(denominator==q.denominator,'independent full rational factorization')
        a,c=toO(rec['a_pi']),toO(rec['c_pi'])
        ck(v.times(a,b)==v.scale(v.ONE,q),'a*b=q')
        ck(v.times(c,b)==v.plus(v.scale(v.ONE,9075),neg(eta)),'c*b=r-eta')
        va,vc=val(a),val(c);ka,kc=va//2,vc//2
        ck([va,vc,ka,kc]==[rec['a_valuation'],rec['c_valuation'],rec['a_scale_exponent'],rec['c_scale_exponent']],'independent full valuations/scales')
        aa,cc=toO(rec['normalized_a']),toO(rec['normalized_c'])
        ck(aa==v.times(a,ppow(-2*ka)) and cc==v.times(c,ppow(-2*kc)),'coefficient square normalization')
        ck(val(aa) in (0,1) and val(cc) in (0,1),'normalized coefficient integrality')
        ck(0<len(rec['attempts'])<=2560,'bounded nonempty domain')
        success=None
        for index,t in enumerate(rec['attempts']):
            ck(t['scale']==(0,1,-1,2,-2)[index//512] and t['digit']==index%512,'entire ordered tested domain')
            vv=v.times(ppow(t['scale']),reps[t['digit']])
            h=v.plus(v.times(aa,v.times(vv,vv)),cc);n=val(h)
            R['bounds']['candidates_actual']+=1
            if n is None:
                ck(t['square'] and t['zero'],'zero square case');success=(vv,h,t)
                continue
            ck(n==t['valuation'],'independent candidate valuation')
            if n%2:
                ck(not t['square'],'odd-valuation rejection');continue
            nn,u,d=v.normalized(h)
            ck(n==nn and t['unit_residue']==d,'independent candidate unit digits')
            ck(t['square']==(d in squares),'complete square decision')
            if not t['square']:continue
            ck(index==len(rec['attempts'])-1,'stopped on first success')
            ck(toO(t['normalized'])==u,'full square-normalized element')
            uu=toO(t['root_approx'])
            ck(uu==v.times(ppow(n//2),reps[t['digit_root']]),'exact root proposal')
            residual=v.plus(v.times(uu,uu),neg(h));derivative=v.scale(uu,2)
            ev,dv=val(residual),val(derivative)
            ck(residual==toO(t['residual']) and derivative==toO(t['derivative']),'entire residual and derivative')
            ck([ev,dv,2*dv]==[t['residual_valuation'],t['derivative_valuation'],t['hensel_threshold']],'all Hensel valuations')
            ck(n>=0 and v.integral(h) and v.integral(uu),'integral Hensel input')
            ck(ev is None or ev>=n+9>2*dv,'strict Hensel certificate')
            success=(vv,h,t)
        ck(success is not None and rec['soluble'] is True and rec['good'] is None,'partial local success only')
        vv,h,t=success;s=rec['solution'];uu=toO(s['U_approx'])
        ck(s['certificate']=={k:z for k,z in t.items() if k not in ('scale','digit')},'whole successful certificate')
        ck(toO(s['V'])==vv and s['original_w']==1,'exact V and affine chart')
        u0,v0=toO(s['original_u_approx']),toO(s['original_v'])
        ck(u0==v.times(ppow(kc),uu) and v0==v.times(ppow(kc-ka),vv),'coordinate recovery')
        error=v.plus(v.plus(v.times(u0,u0),neg(v.times(a,v.times(v0,v0)))),neg(c))
        normalized_error=v.plus(v.times(uu,uu),neg(h))
        ck(error==toO(s['original_residual']) and normalized_error==toO(s['normalized_residual']),'full conic residuals')
        ck(error==v.times(ppow(2*kc),normalized_error),'homogeneous conic transport')
        R['classes'].append(dict(label=rec['label'],soluble=True,good=None,
             candidates=len(rec['attempts']),a_valuation=va,c_valuation=vc,
             square_valuation=t.get('valuation'),residual_valuation=t.get('residual_valuation'),
             hensel_threshold=t.get('hensel_threshold')))
        R['bounds']['classes_actual']+=1
    ck(not C['full_goodness_decided'] and not C['pairing_computed'],'no expanded conclusion')
    ck(R['bounds']['candidates_actual']==C['bounds']['candidates_actual'],'actual complete attempt count')
    R['bounds']['rational_bits_actual']=v.R['max_rational_bits']
    R['helper_checks']=v.R['checks']
    R['source_sha256']=sha256(Path(__file__).read_bytes()).hexdigest()
    R['helper_sha256']=sha256((ROOT/'verify_two_adic_filter.py').read_bytes()).hexdigest()
    R['completed']=True


if __name__=='__main__':
    try:main()
    except Exception as e:R['failures'].append(dict(message=str(e),traceback=traceback.format_exc()))
    OUT.write_text(json.dumps(R,indent=2,default=str)+'\n')
    print(json.dumps(dict(completed=R['completed'],checks=R['checks'],helper_checks=R.get('helper_checks'),
        failures=[e['message'] for e in R['failures']],classes=R['classes'],bounds=R['bounds'],path=str(OUT))))
    raise SystemExit(0 if R['completed'] else 1)
