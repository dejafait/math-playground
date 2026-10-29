"""Fixed good-element gate: exact rational-branch conics, no pairing.

The full condition also has quartic/quartic rows; a negative row suffices.
Uses accepted prime lattices with residue fields F_p, at odd support primes.
"""
from fractions import Fraction as Q
from pathlib import Path
from hashlib import sha256
import json
import traceback
import odd_membership_35 as local
import surviving_witness_span as field
import branch_annihilator as real

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'shukla-good-conics-certificate.json'
D=dict(completed=False,failures=[],bindings={},classes=[],checks=[],
       bounds=dict(classes_required=2,classes_tested=0,odd_primes=[3,5,11],
                   prime_depth_cap=64,rational_bits_cap=8192),
       full_goodness_decided=False,pairing_computed=False)


def ck(name,test):
    D['checks'].append(dict(name=name,passed=bool(test)))
    assert test,name


def read(name):
    raw=(ROOT/name).read_bytes();D['bindings'][name]=sha256(raw).hexdigest()
    return json.loads(raw)


def simple_root(p,seed,precision=24):
    A=field.A;der=[i*A[i] for i in range(1,5)]
    t=seed;mod=p;steps=[]
    ck('simple root seed',field.ev(A,t)%p==0 and field.ev(der,t)%p!=0)
    for n in range(1,precision):
        digit=(-field.ev(A,t)//mod*pow(field.ev(der,t),-1,p))%p
        steps.append(dict(precision=n,root=t,value=field.ev(A,t),derivative=field.ev(der,t),digit=digit))
        t+=digit*mod;mod*=p
        ck('exact Hensel digit',field.ev(A,t)%mod==0 and field.ev(der,t)%p!=0)
    return dict(p=p,seed=seed,precision=precision,root=t,modulus=mod,
                value=field.ev(A,t),derivative=field.ev(der,t),steps=steps)


def odd_symbol(P,aO,cO):
    ac=P.classify(aO);cc=P.classify(cO)
    va,ua=ac['mask']&1,ac['mask']>>1
    vc,uc=cc['mask']&1,cc['mask']>>1
    exponent=(va*vc*((P.p-1)//2)+va*uc+vc*ua)%2
    # Record full normalized valuations as well as parity/residue masks.
    for value in (ac,cc):
        value['valuation']=value['integral_class']['valuation']-value['denominator_valuation']*P.pclass['valuation']
    return dict(prime_index=P.index,p=P.p,quaternion_a=ac,quaternion_c=cc,
                hilbert_exponent=exponent,hilbert_symbol=(-1)**exponent)


def main():
    C=read('odd-membership-35-certificate.json')
    nu_cert=read('surviving-witness-span-certificate.json')
    for stem,cert in [('odd-membership-35',C),('surviving-witness-span',nu_cert)]:
        ck(stem+' complete',cert['completed'] and not cert['failures'])
        audit=read(stem+'-audit.json')
        ck(stem+' audit',audit['completed'] and not audit['failures'] and
           audit['bindings'][stem+'-certificate.json']==D['bindings'][stem+'-certificate.json'])
    base=read('quartic-class-certificate.json')
    model=read('odd-model-support-certificate.json')
    two=read('two-adic-filter-certificate.json')
    local.lattice.TABLE=base['order']['table']
    B=[[Q(x) for x in row] for row in model['field']['O_basis_in_alpha']]
    ck('basis matches field arithmetic',B==field.B)
    invB=local.inverse(B)
    eta=list(map(Q,model['field']['eta_in_alpha']))
    ck('actual field identification',field.mul(eta,[-50,1,0,0])==[-907500,0,0,0])
    ck('model rational root',model['model']['G']==[-477484407427500000000,
       191519916588000000,-29655931140000,2196150000,-76835,1])
    ck('rational-root quartic factor value',local.ev(model['model']['H'],Q(9075))==73990352390625)
    sources=two['witnesses']
    ck('whole 39-source order',len(sources)==39 and
       all(w['source']==C['places']['3']['witnesses'][j]['source'] for j,w in enumerate(sources)))
    primes=[local.Prime(p,i,P) for p in (3,5,11) for i,P in enumerate(base['generators']) if P['p']==p]
    ck('complete odd prime indices',[P.index for P in primes]==[27,28,29,30,31,1])
    ck('all residues have degree one',all(P.record['source']['lattice']['norm']==P.p for P in primes))
    D['prime_records']=[P.record for P in primes]
    D['simple_roots']=[simple_root(3,2),simple_root(5,1)]
    for label,mask in [('eta_class',132102),('nu',3109)]:
        q=Q(1);b=field.ONE[:]
        for j,w in enumerate(sources):
            if mask>>j&1:
                q*=Q(w['source']['inverse_norm'])
                b=field.mul(b,field.powercoords(w['source']['coefficients']))
        ck(label+' norm one',q*field.norm(b)==1)
        if label=='eta_class':
            saved=C['selected_pair'][1]
            ck('eta exact saved representative',q==Q(saved['rational']) and b==field.powercoords(saved['quartic_O']))
        else:
            saved=nu_cert['products'][3]
            ck('nu exact saved representative',saved['mask']==mask and q==Q(saved['rational']) and b==list(map(Q,saved['quartic_power'])))
        # b*u^2-q*v^2+(eta-r)*w^2=0. Equivalent quaternion
        # (q/b,(r-eta)/b), with coefficients a and c below.
        a=field.mul([q,0,0,0],field.inv(b))
        c=field.mul([Q(9075)-eta[0]]+[-x for x in eta[1:]],field.inv(b))
        aO=local.mv(invB,a);cO=local.mv(invB,c)
        rec=dict(label=label,mask=mask,rational=q,quartic_power=b,
                 row=dict(first_root=9075,second_root_power=eta,
                          conic='b*u^2-q*v^2+(eta-9075)*w^2=0',
                          quaternion_a_power=a,quaternion_c_power=c,
                          quaternion_a_O=aO,quaternion_c_O=cO),local_tests=[])
        D['classes'].append(rec)
        for P in primes:
            test=odd_symbol(P,aO,cO);rec['local_tests'].append(test)
            if test['hilbert_exponent']:
                rec.update(good=False,decisive_prime_index=P.index)
                break
        rec['mixed_simple_root_tests']=[]
        if 'good' not in rec:
            for root in D['simple_roots']:
                p,t,N=root['p'],root['root'],root['precision']
                bi=field.ev(b,Q(t));thetai=field.ev(eta,Q(t))
                for P in primes:
                    if P.p!=p:continue
                    gap=local.mv(invB,[Q(t),-1,0,0])
                    gapc=P.classify(gap)
                    gapv=gapc['integral_class']['valuation']-gapc['denominator_valuation']*P.pclass['valuation']
                    if gapv>=N:
                        ck('diagonal simple completion has degree one',P.pclass['valuation']==1)
                        continue
                    aa=field.mul([bi,0,0,0],field.inv(b))
                    cc=field.mul([thetai-eta[0]]+[-x for x in eta[1:]],field.inv(b))
                    test=odd_symbol(P,local.mv(invB,aa),local.mv(invB,cc))
                    bval=P.classify(local.mv(invB,b))
                    bv=bval['integral_class']['valuation']-bval['denominator_valuation']*P.pclass['valuation']
                    ea=P.pclass['valuation']*(N+min(local.vp(x,p) for x in b if x))-bv
                    ec=P.pclass['valuation']*(N+min(local.vp(x,p) for x in eta if x))-bv
                    ck('mixed coefficient a stable beyond leading digit',ea>test['quaternion_a']['valuation'])
                    ck('mixed coefficient c stable beyond leading digit',ec>test['quaternion_c']['valuation'])
                    test.update(first_alpha_approx=t,root_precision=N,second_alpha_gap=gapc,
                       second_alpha_gap_valuation=gapv,first_d_approx=bi,first_theta_approx=thetai,
                       quaternion_a_power=aa,quaternion_c_power=cc,
                       a_error_valuation_lower=ea,c_error_valuation_lower=ec)
                    rec['mixed_simple_root_tests'].append(test)
                    if test['hilbert_exponent']:
                        rec.update(good=False,decisive_prime_index=P.index)
                        break
                if 'good' in rec:break
        # Every ordered real pair is checked; interval signs alone suffice
        # for a real diagonal conic, with no finite point-search inference.
        boxes=[];roots=[dict(theta_interval=[Q(9075),Q(9075)],d_interval=[q,q])]
        for lo,hi in [(-48,-47),(-34,-33),(-4,-3),(20,21)]:
            lo,hi=Q(lo),Q(hi)
            ck('real root bracket',field.ev(field.A,lo)*field.ev(field.A,hi)<0)
            for _ in range(32):
                mid=(lo+hi)/2
                if field.ev(field.A,lo)*field.ev(field.A,mid)<0:hi=mid
                else:lo=mid
            boxes.append([lo,hi])
            di=real.interval(b,lo,hi);ti=real.interval(eta,lo,hi)
            ck('real nonzero d sign',di[0]>0 or di[1]<0)
            roots.append(dict(alpha_interval=[lo,hi],theta_interval=ti,d_interval=di))
        ck('four real roots exhaust quartic',len(boxes)==4)
        rec['real_roots']=roots;rec['real_pair_tests']=[]
        sign=lambda box:1 if box[0]>0 else -1 if box[1]<0 else 0
        for i,ri in enumerate(roots):
            for j,rj in enumerate(roots):
                if i==j:continue
                diff=[rj['theta_interval'][0]-ri['theta_interval'][1],
                      rj['theta_interval'][1]-ri['theta_interval'][0]]
                signs=[sign(rj['d_interval']),-sign(ri['d_interval']),sign(diff)]
                ck('real conic nondegenerate mixed signs',0 not in signs and min(signs)<0<max(signs))
                rec['real_pair_tests'].append(dict(first=i,second=j,constant_interval=diff,coefficient_signs=signs,split=True))
        if 'good' not in rec:
            rec.update(good=None,remaining='dyadic, unsampled quartic/quartic completions, global pair-field factorization, outside-support proof and compatible exact solutions')
        D['bounds']['classes_tested']+=1
    D['full_goodness_decided']=all(c['good'] is False for c in D['classes'])
    D['helper_checks_count']=len(local.D['checks'])
    D['helper_max_rational_bits']=max(local.D['bounds']['max_rational_bits'],field.R['bounds']['max_rational_bits'])
    D['bounds'].update(odd_conics_actual=sum(len(c['local_tests'])+len(c['mixed_simple_root_tests']) for c in D['classes']),
        real_ordered_pairs_actual=sum(len(c['real_pair_tests']) for c in D['classes']),
        root_precision_actual=24,root_precision_cap=24,
        prime_depth_actual=max(len(P.powers)-1 for P in primes))
    def certificate_bits(x):
        if isinstance(x,dict):return max([0]+[certificate_bits(z) for z in x.values()])
        if isinstance(x,(list,tuple)):return max([0]+[certificate_bits(z) for z in x])
        if isinstance(x,(int,Q)) and not isinstance(x,bool):
            z=Q(x);return max(abs(z.numerator).bit_length(),z.denominator.bit_length())
        return 0
    D['bounds']['saved_rational_bits_actual']=certificate_bits(D)
    ck('saved rational bound',D['bounds']['saved_rational_bits_actual']<=8192)
    D['source_sha256']=sha256(Path(__file__).read_bytes()).hexdigest()
    D['helper_sha256']={name:sha256((ROOT/name).read_bytes()).hexdigest() for name in
        ['odd_membership_35.py','quartic_parity_generate.py','surviving_witness_span.py','branch_annihilator.py']}
    D['completed']=True


if __name__=='__main__':
    try:main()
    except Exception as e:D['failures'].append(dict(message=str(e),traceback=traceback.format_exc()))
    OUT.write_text(json.dumps(D,indent=2,default=str)+'\n')
    print(json.dumps(dict(completed=D['completed'],failures=[e['message'] for e in D['failures']],
        classes=[dict(label=c['label'],good=c.get('good'),rational_row_odd_tests=len(c['local_tests']),
                      mixed_row_odd_tests=len(c.get('mixed_simple_root_tests',[])),real_ordered_pairs=len(c.get('real_pair_tests',[])),
                      decisive_prime=c.get('decisive_prime_index')) for c in D['classes']],
        full_goodness_decided=D['full_goodness_decided'],bounds=D['bounds'],path=str(OUT))))
    raise SystemExit(0 if D['completed'] else 1)
