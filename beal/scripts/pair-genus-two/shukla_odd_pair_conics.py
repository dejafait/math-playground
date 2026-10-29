"""Remaining odd quartic-pair conics; exact valuations, no pairing/point search."""
from fractions import Fraction as Q
from math import comb
from pathlib import Path
from hashlib import sha256
import json
import traceback
import shukla_good_conics as s

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'shukla-odd-pair-conics-certificate.json'
D=dict(completed=False,failures=[],bindings={},checks=0,classes=[],roots=[],
       prime_records=[],full_goodness_decided=False,pairing_computed=False,
       bounds=dict(root_precision_required=24,root_precision_actual=24,
                   prime_depth_cap=64,rational_bits_cap=8192,classes_required=2))


def ck(ok,name):
    D['checks']+=1
    assert ok,name


def read(name):
    raw=(ROOT/name).read_bytes();D['bindings'][name]=sha256(raw).hexdigest()
    return json.loads(raw)


def taylor(poly,k):
    z=[Q(0)]*4
    for j in range(k,len(poly)):
        pw=s.field.ONE[:]
        for _ in range(j-k):pw=s.field.mul(pw,[0,1,0,0])
        z=[x+Q(poly[j])*comb(j,k)*y for x,y in zip(z,pw)]
    return z


def local_record(P,poly,I):
    r=P.classify(s.local.mv(I,poly))
    r['valuation']=r['integral_class']['valuation']-r['denominator_valuation']*P.pclass['valuation']
    return dict(power=poly,local=r)


def root(poly,seed,shift,scale,divisor):
    # poly(X)=A(shift+scale*X)/divisor, checked coefficientwise.
    coeff=[sum(s.field.A[j]*comb(j,k)*shift**(j-k)*scale**k
               for j in range(k,5)) for k in range(5)]
    ck(coeff==[divisor*x for x in poly],'exact transformed root polynomial')
    der=[j*poly[j] for j in range(1,5)]
    t=seed;mod=5;steps=[]
    ck(s.field.ev(poly,t)%5==0 and s.field.ev(der,t)%5!=0,'simple transformed seed')
    for n in range(1,24):
        value=s.field.ev(poly,t);slope=s.field.ev(der,t)
        digit=(-value//mod*pow(slope,-1,5))%5
        steps.append(dict(precision=n,root=t,value=value,derivative=slope,digit=digit))
        t+=digit*mod;mod*=5
        ck(s.field.ev(poly,t)%mod==0,'complete Hensel step')
    return dict(p=5,polynomial=poly,seed=seed,shift=shift,scale=scale,divisor=divisor,
                steps=steps,root=t,precision=24,alpha_approx=shift+scale*t,
                alpha_precision=24+s.local.vp(scale,5))


def bits(x):
    if isinstance(x,dict):return max([0]+[bits(v) for v in x.values()])
    if isinstance(x,(list,tuple)):return max([0]+[bits(v) for v in x])
    if isinstance(x,(int,Q)) and not isinstance(x,bool):
        x=Q(x);return max(abs(x.numerator).bit_length(),x.denominator.bit_length())
    return 0


def main():
    old=read('shukla-good-conics-certificate.json')
    dyad=read('shukla-quartic-pair-conics-certificate.json')
    base=read('quartic-class-certificate.json')
    model=read('odd-model-support-certificate.json')
    two=read('two-adic-filter-certificate.json')
    for c in (old,dyad,base,two):ck(c['completed'] and not c['failures'],'completed input')
    ck(not model['failures'] and all(r['pass'] for r in model['checks']),'actual model checks')
    # Do not regenerate the completed rational-row/dyadic evidence.
    for stem in ('shukla-good-conics','shukla-quartic-pair-conics'):
        v=read(stem+'-verification.json')
        ck(v['completed'] and not v['failures'] and
           v['bindings'][stem+'-certificate.json']==D['bindings'][stem+'-certificate.json'],
           'accepted complete input replay binding')
    s.local.lattice.TABLE=base['order']['table']
    B=[[Q(x) for x in row] for row in model['field']['O_basis_in_alpha']]
    ck(B==s.field.B,'actual integral basis');I=s.local.inverse(B)
    primes={i:s.local.Prime(p,i,base['generators'][i]) for p,i in [(3,27),(5,29),(5,30),(5,31),(11,1)]}
    D['prime_records']=[P.record for P in primes.values()]
    D['roots']=[root(s.field.A,1,0,1,1),root([33,308,990,1320,625],4,50,125,390625)]
    # Identify each Q_5 branch by exact maximal-order prime membership.
    for r,index in zip(D['roots'],[30,29]):
        P=primes[index]
        rec=local_record(P,[Q(r['alpha_approx']),-1,0,0],I)
        ck(P.pclass['valuation']==1 and rec['local']['valuation']>=r['alpha_precision'],
           'root belongs to claimed degree-one completion')
        r.update(prime_index=index,alpha_gap=rec)
    eta=list(map(Q,model['field']['eta_in_alpha']))
    ck(s.field.mul(eta,[-50,1,0,0])==[-907500,0,0,0],'actual theta map')
    D['root_gap_coefficients']={}
    for index in (27,1):
        P=primes[index]
        rows=[local_record(P,taylor(s.field.A,k),I) for k in range(1,5)]
        expected=[5,3,0,0] if index==27 else [3,2,1,0]
        ck([r['local']['valuation'] for r in rows]==expected,'complete root-gap coefficients')
        D['root_gap_coefficients'][str(index)]=rows
    D['eleven_denominator']=local_record(primes[1],[-50,1,0,0],I)
    ck(D['eleven_denominator']['local']['valuation']==1,'all conjugate theta denominators')
    D['three_alpha_residue']=local_record(primes[27],[-1,1,0,0],I)
    ck(D['three_alpha_residue']['local']['valuation']>0,'cubic roots reduce to one')
    traces=[]
    for j in range(4):
        pw=[Q(int(k==j)) for k in range(4)]
        traces.append(sum(s.field.mul(pw,[Q(int(k==i)) for k in range(4)])[i] for i in range(4)))
    D['power_traces']=traces
    for cl in old['classes']:
        mask=cl['mask'];q=Q(1);b=s.field.ONE[:]
        for j,w in enumerate(two['witnesses']):
            if mask>>j&1:
                q*=Q(w['source']['inverse_norm']);b=s.field.mul(b,s.field.powercoords(w['source']['coefficients']))
        ck(q==Q(cl['rational']) and b==list(map(Q,cl['quartic_power'])),'full representative authentication')
        rec=dict(label=cl['label'],mask=mask,rational=q,quartic_power=b,three={},five={},eleven={})
        D['classes'].append(rec)
        for name,index in [('three',27),('eleven',1)]:
            P=primes[index];part=rec[name]
            part['b']=local_record(P,b,I)
            part['b_taylor']=[local_record(P,taylor(b,k),I) for k in range(1,4)]
            gap=Q(5,2) if index==27 else Q(1)
            lower=min(x['local']['valuation']+(k+1)*gap for k,x in enumerate(part['b_taylor']))
            part['difference_valuation_lower']=lower
            bv=part['b']['local']['valuation']
            if index==27 or cl['label']=='nu':
                ck(lower>bv,'conjugate b ratio is a principal unit')
                part.update(soluble=True,reason='a=b_i*b_j is a square at every such pair')
            else:
                ck(bv==1,'eta eleven b valuation')
                # Each theta gap has valuation 4*v_11(907500)+1-2=7.
                gv=4*s.local.vp(907500,11)+1-2
                ck(gv==7 and (2*bv)%2==0 and (gv+bv)%2==0,'both quaternion valuations even')
                part.update(theta_gap_valuation=gv,a_valuation=2*bv,c_valuation=gv+bv,
                            soluble=True,reason='both quaternion entries have even valuations')
        # Missing rational-branch/quadratic-branch pair at five.
        r=D['roots'][1];P=primes[31];t=Q(r['alpha_approx'])
        bi=s.field.ev(b,t);ti=s.field.ev(eta,t)
        a=s.field.mul([bi,0,0,0],s.field.inv(b))
        c=s.field.mul([ti-eta[0]]+[-x for x in eta[1:]],s.field.inv(b))
        test=s.odd_symbol(P,s.local.mv(I,a),s.local.mv(I,c))
        bv=local_record(P,b,I)['local']['valuation'];e=P.pclass['valuation']
        ea=e*(r['alpha_precision']+min(s.local.vp(x,5) for x in b if x))-bv
        ec=e*(r['alpha_precision']+min(s.local.vp(x,5) for x in eta if x))-bv
        ck(ea>test['quaternion_a']['valuation'] and ec>test['quaternion_c']['valuation'],'strict coefficient error bounds')
        ck(test['hilbert_symbol']==1,'remaining mixed five pair splits')
        test.update(first_alpha_approx=t,first_d_approx=bi,first_theta_approx=ti,
                    quaternion_a_power=a,quaternion_c_power=c,
                    a_error_valuation_lower=ea,c_error_valuation_lower=ec)
        rec['five']['missing_mixed_test']=test
        # The two roots in the quadratic factor: trace(b)=b_i+b_j.
        total=sum(x*y for x,y in zip(b,traces))
        approx=total-sum(s.field.ev(b,Q(r['alpha_approx'])) for r in D['roots'])
        tracev=e*s.local.vp(approx,5)
        err=min(e*(r['alpha_precision']+min(s.local.vp(x,5) for x in b if x)) for r in D['roots'])
        ck(bv==1 and tracev>bv and err>bv,'quadratic conjugate ratio is minus a principal unit')
        ck(pow(2,2,5)==4,'minus one square in Q5 by Hensel')
        rec['five'].update(quadratic_b=local_record(P,b,I),global_trace=total,
            quadratic_trace_approx=approx,quadratic_trace_valuation=tracev,
            quadratic_trace_error_lower=err,quadratic_pair_soluble=True,
            reason='b_j/b_i has square residue -1; hence a is a square')
        rec.update(all_odd_pair_conics_soluble=True,good=None,global_points_constructed=False)
    H=model['model']['H'];G=model['model']['G']
    ck(G==[-477484407427500000000,191519916588000000,-29655931140000,2196150000,-76835,1],'actual quintic')
    gap=s.local.ev(H,Q(9075))
    ck(gap==3**5*5**6*11**7,'rational-quartic resultant')
    D['outside_support']=dict(support=[2,3,5,11],H=H,
        disc_H=2**32*3**11*5**15*11**21,
        disc_G=2**32*3**21*5**27*11**35,resultant=gap,
        uses_full_supportedness=True,all_root_gaps_units=True)
    ck(D['outside_support']['disc_H']*gap**2==D['outside_support']['disc_G'],'exact discriminant quotient')
    D['bounds'].update(classes_actual=len(D['classes']),root_lift_steps_actual=sum(len(r['steps']) for r in D['roots']),
        root_lift_steps_required=46,prime_depth_actual=max(len(P.powers)-1 for P in primes.values()))
    D['bounds']['rational_bits_actual']=bits(D)
    ck(D['bounds']['rational_bits_actual']<=8192,'rational bits cap')
    D['source_sha256']=sha256(Path(__file__).read_bytes()).hexdigest()
    D['helper_sha256']={name:sha256((ROOT/name).read_bytes()).hexdigest() for name in
        ['shukla_good_conics.py','odd_membership_35.py','quartic_parity_generate.py','surviving_witness_span.py']}
    D['completed']=True


if __name__=='__main__':
    try:main()
    except Exception as e:D['failures'].append(dict(message=str(e),traceback=traceback.format_exc()))
    OUT.write_text(json.dumps(D,indent=2,default=str)+'\n')
    print(json.dumps(dict(completed=D['completed'],checks=D['checks'],bounds=D['bounds'],
        failures=[x['message'] for x in D['failures']],path=str(OUT))))
    raise SystemExit(0 if D['completed'] else 1)
