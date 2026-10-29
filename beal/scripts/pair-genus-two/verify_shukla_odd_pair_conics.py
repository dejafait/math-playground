"""Independent O-basis replay of the odd root-pair certificate."""
from fractions import Fraction as Q
from math import comb
from pathlib import Path
from hashlib import sha256
import json
import traceback
import verify_odd_membership_35 as v

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'shukla-odd-pair-conics-verification.json'
R=dict(completed=False,failures=[],bindings={},checks=0,new_mixed_symbols=0,
       full_goodness_decided=False,pairing_computed=False)


def ck(ok,name):
    R['checks']+=1
    assert ok,name


def read(name):
    raw=(ROOT/name).read_bytes();R['bindings'][name]=sha256(raw).hexdigest()
    return json.loads(raw)


def ev(poly,x):return sum(Q(a)*x**j for j,a in enumerate(poly))


def main():
    C=read('shukla-odd-pair-conics-certificate.json')
    ck(C['completed'] and not C['failures'],'producer completed')
    ck([(x['label'],x['mask']) for x in C['classes']]==[('eta_class',132102),('nu',3109)],'exact fixed two-class domain')
    src={name:read(name) for name in C['bindings']}
    ck(all(R['bindings'][name]==h for name,h in C['bindings'].items()),'all input hashes')
    ck(sha256((ROOT/'shukla_odd_pair_conics.py').read_bytes()).hexdigest()==C['source_sha256'],'producer hash')
    ck(all(sha256((ROOT/name).read_bytes()).hexdigest()==h for name,h in C['helper_sha256'].items()),'helper hashes')
    base=src['quartic-class-certificate.json'];model=src['odd-model-support-certificate.json']
    v.T=base['order']['table'];B=model['field']['O_basis_in_alpha']
    rows=[[Q(B[i][j]) for i in range(4)] for j in range(4)]
    def toO(x):return v.coords(rows,list(map(Q,x)))
    alpha=toO([0,1,0,0]);one=v.ONE
    def fieldval(rec,power,P):
        ck(toO(rec['power'])==power,'full power/O coordinate equality')
        v.fieldcheck(rec['local'],power,P,P['source']['p'])
        r=rec['local'];vv=r['integral_class']['valuation']-P['rational_prime_class']['valuation']*r['denominator_valuation']
        ck(vv==r['valuation'],'full normalized valuation')
        return vv
    powers=[one,alpha]
    for _ in range(3):powers.append(v.times(powers[-1],alpha))
    def tay(poly,k):
        out=[Q(0)]*4
        for j in range(k,len(poly)):
            out=v.plus(out,v.scale(powers[j-k],Q(poly[j])*comb(j,k)))
        return out
    primes={P['index']:P for P in C['prime_records']}
    ck(list(primes)==[27,29,30,31,1],'exact new prime domain')
    ck([P['rational_prime_class']['valuation'] for P in primes.values()]==[3,1,1,2,4],'actual ramification indices')
    for ix,P in primes.items():
        p=P['source']['p'];ck(P['source']==base['generators'][ix],'maximal-order prime source')
        for n,lat in enumerate(P['powers']):
            rr=lat['rows'];ck(abs(v.det(rr))==p**n==lat['norm'],'ideal power index')
            gens=[[int(i==j) for i in range(4)] for j in range(4)] if n==0 else (
                P['source']['lattice']['columns'] if n==1 else
                [v.times(v.vec(a),v.vec(b)) for a in P['powers'][n-1]['rows'] for b in P['powers'][1]['rows']])
            ck(all(v.member(rr,g) for g in gens),'all power reverse containments')
            for co,row in zip(lat['forward'],rr):
                ck([sum(Q(c)*Q(g[k]) for c,g in zip(co,gens)) for k in range(4)]==v.vec(row),'all forward containments')
        pi=v.vec(P['uniformizer'])
        ck(v.member(P['powers'][1]['rows'],pi) and not v.member(P['powers'][2]['rows'],pi),'prime uniformizer')
        v.integralcheck(P['rational_prime_class'],[Q(p),0,0,0],P,p)
    A=model['field']['alpha_polynomial']
    for r,index in zip(C['roots'],[30,29]):
        poly=r['polynomial'];shift=r['shift'];scale=r['scale'];div=r['divisor']
        for k in range(5):
            ck(div*poly[k]==sum(A[j]*comb(j,k)*shift**(j-k)*scale**k for j in range(k,5)),'transformed polynomial coefficients')
        der=[j*poly[j] for j in range(1,5)];t=r['seed'];mod=5
        ck(ev(poly,t)%5==0 and ev(der,t)%5!=0,'root seed hypotheses')
        for n,step in enumerate(r['steps'],1):
            ck(t==step['root'] and n==step['precision'] and ev(poly,t)==step['value'] and ev(der,t)==step['derivative'],'all Hensel source evaluations')
            ck(ev(poly,t)%mod==0 and ev(der,t)%5!=0 and 0<=step['digit']<5,'every simple Hensel hypothesis')
            t+=step['digit']*mod;mod*=5
        ck(t==r['root'] and mod==5**24 and ev(poly,t)%mod==0,'final root disk')
        ck(r['alpha_approx']==shift+scale*t and r['alpha_precision']==24+v.val(Q(scale),5),'root coordinate/precision transport')
        ck(r['prime_index']==index and primes[index]['rational_prime_class']['valuation']==1,'rational branch degree')
        gap=v.plus(v.scale(one,r['alpha_approx']),v.scale(alpha,-1))
        ck(fieldval(r['alpha_gap'],gap,primes[index])>=r['alpha_precision'],'claimed root component')
    for ix,expected in [(27,[5,3,0,0]),(1,[3,2,1,0])]:
        vals=[fieldval(rec,tay(A,k),primes[ix]) for k,rec in enumerate(C['root_gap_coefficients'][str(ix)],1)]
        ck(vals==expected,'all root-gap coefficient valuations')
    ck(fieldval(C['eleven_denominator'],v.plus(alpha,v.scale(one,-50)),primes[1])==1,'theta denominator at eleven')
    ck(fieldval(C['three_alpha_residue'],v.plus(alpha,v.scale(one,-1)),primes[27])>0,'cubic residue one')
    traces=[]
    for a in powers[:4]:
        traces.append(sum(v.times(a,[Q(int(k==i)) for k in range(4)])[i] for i in range(4)))
    ck(traces==list(map(Q,C['power_traces'])),'independent multiplication traces')
    eta=toO(model['field']['eta_in_alpha'])
    ck(v.times(eta,v.plus(alpha,v.scale(one,-50)))==v.scale(one,-907500),'exact root map')
    for cl in C['classes']:
        b=one[:];q=Q(1)
        for j,w in enumerate(src['two-adic-filter-certificate.json']['witnesses']):
            if cl['mask']>>j&1:
                b=v.times(b,v.vec(w['source']['coefficients']));q*=Q(w['source']['inverse_norm'])
        ck(b==toO(cl['quartic_power']) and q==Q(cl['rational']),'entire full product rebuilt')
        for name,ix in [('three',27),('eleven',1)]:
            part=cl[name];P=primes[ix]
            bv=fieldval(part['b'],b,P)
            ts=[fieldval(r,tay(cl['quartic_power'],k),P) for k,r in enumerate(part['b_taylor'],1)]
            gap=Q(5,2) if ix==27 else Q(1)
            lower=min(x+(k+1)*gap for k,x in enumerate(ts))
            ck(lower==Q(part['difference_valuation_lower']),'independent difference bound')
            if ix==27 or cl['label']=='nu':ck(lower>bv,'strict principal-unit ratio bound')
            else:
                ck(bv==1 and part['theta_gap_valuation']==7 and part['a_valuation']==2 and part['c_valuation']==8,'eleven even valuations')
        P=primes[31];test=cl['five']['missing_mixed_test'];root=C['roots'][1];t=Q(root['alpha_approx'])
        bi=ev(cl['quartic_power'],t);ti=ev(model['field']['eta_in_alpha'],t)
        ck(bi==Q(test['first_d_approx']) and ti==Q(test['first_theta_approx']),'mixed first root evaluations')
        a=toO(test['quaternion_a_power']);c=toO(test['quaternion_c_power'])
        ck(v.times(a,b)==v.scale(one,bi),'mixed a identity')
        ck(v.times(c,b)==v.plus(v.scale(one,ti),v.scale(eta,-1)),'mixed c identity')
        am=v.fieldcheck(test['quaternion_a'],a,P,5);cm=v.fieldcheck(test['quaternion_c'],c,P,5)
        bv=fieldval(cl['five']['quadratic_b'],b,P);e=P['rational_prime_class']['valuation']
        for key,poly in [('a',cl['quartic_power']),('c',model['field']['eta_in_alpha'])]:
            err=e*(root['alpha_precision']+min(v.val(Q(z),5) for z in poly if Q(z)))-bv
            rr=test['quaternion_'+key];value=rr['integral_class']['valuation']-e*rr['denominator_valuation']
            ck(err==test[key+'_error_valuation_lower'] and err>value==rr['valuation'],'strict independent coefficient stability')
        symbol=(-1)**(((am&1)*(cm>>1)+(cm&1)*(am>>1))%2)
        ck(symbol==test['hilbert_symbol']==1,'independent remaining mixed Hilbert symbol')
        R['new_mixed_symbols']+=1
        trace=sum(Q(a)*z for a,z in zip(cl['quartic_power'],traces))
        approx=trace-sum(ev(cl['quartic_power'],Q(r['alpha_approx'])) for r in C['roots'])
        lower=min(e*(r['alpha_precision']+min(v.val(Q(z),5) for z in cl['quartic_power'] if Q(z))) for r in C['roots'])
        part=cl['five']
        ck(trace==Q(part['global_trace']) and approx==Q(part['quadratic_trace_approx']),'exact quadratic trace approximation')
        ck(e*v.val(approx,5)==part['quadratic_trace_valuation']>bv==1 and lower==part['quadratic_trace_error_lower']>bv,'strict trace cancellation')
        ck(cl['good'] is None and not cl['global_points_constructed'],'no constructive/goodness overclaim')
    out=C['outside_support'];disc=model['discriminants']
    ck(out['disc_H']==disc['H']['discriminant']==2**32*3**11*5**15*11**21,'actual quartic discriminant')
    ck(out['disc_G']==disc['G']['discriminant']==2**32*3**21*5**27*11**35,'actual quintic discriminant')
    ck(Q(out['resultant'])==ev(out['H'],Q(9075))==3**5*5**6*11**7,'resultant value')
    ck(out['disc_H']*Q(out['resultant'])**2==out['disc_G'],'factor discriminant identity')
    ck(not C['full_goodness_decided'] and not C['pairing_computed'],'scope retained')
    R.update(helper_checks=v.R['checks'],rational_bits_actual=v.R['max_rational_bits'],
             rational_bits_cap=8192,root_steps_actual=46,root_steps_required=46,
             prime_depth_actual=max(len(P['powers'])-1 for P in primes.values()),prime_depth_cap=64,
             completed=True)


if __name__=='__main__':
    try:main()
    except Exception as e:R['failures'].append(dict(message=str(e),traceback=traceback.format_exc()))
    OUT.write_text(json.dumps(R,indent=2)+'\n')
    print(json.dumps({**{k:x for k,x in R.items() if k not in ('bindings','failures')},
                      'failures':[x['message'] for x in R['failures']],'path':str(OUT)}))
    raise SystemExit(0 if R['completed'] else 1)
