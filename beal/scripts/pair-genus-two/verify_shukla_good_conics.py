"""Replay partial conic evidence in the integral basis, without producer imports."""
from fractions import Fraction as Q
from pathlib import Path
from hashlib import sha256
import json
import traceback
import verify_odd_membership_35 as v

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'shukla-good-conics-verification.json'
R=dict(completed=False,failures=[],bindings={},checks=0,odd_tests=0,real_tests=0,
       full_goodness_decided=False,pairing_computed=False)


def ck(test,name):
    R['checks']+=1
    assert test,name


def read(name):
    raw=(ROOT/name).read_bytes();R['bindings'][name]=sha256(raw).hexdigest()
    return json.loads(raw)


def mv(B,x):return [sum(Q(a)*Q(b) for a,b in zip(row,x)) for row in B]


def ev(poly,x):return sum(Q(a)*x**j for j,a in enumerate(poly))


def interval(poly,lo,hi):
    # Direct interval powers rather than producer Horner intervals.
    lower=upper=Q(0)
    for j,c in enumerate(poly):
        powers=[lo**j,hi**j]
        if lo<=0<=hi and j%2==0:powers.append(Q(0) if j else Q(1))
        terms=[Q(c)*min(powers),Q(c)*max(powers)]
        lower+=min(terms);upper+=max(terms)
    return [lower,upper]


def main():
    C=read('shukla-good-conics-certificate.json')
    ck(C['completed'] and not C['failures'],'producer completion')
    sources={name:read(name) for name in C['bindings']}
    ck(all(R['bindings'][name]==h for name,h in C['bindings'].items()),'all input bindings')
    ck(sha256((ROOT/'shukla_good_conics.py').read_bytes()).hexdigest()==C['source_sha256'],'producer binding')
    ck(all(sha256((ROOT/name).read_bytes()).hexdigest()==h for name,h in C['helper_sha256'].items()),'all helper bindings')
    base=sources['quartic-class-certificate.json'];model=sources['odd-model-support-certificate.json']
    v.T=base['order']['table'];B=model['field']['O_basis_in_alpha']
    toO=lambda x:v.coords([[Q(B[i][j]) for i in range(4)] for j in range(4)],list(map(Q,x)))
    one=v.ONE;alpha=toO([0,1,0,0]);eta=toO(model['field']['eta_in_alpha'])
    primes={P['index']:P for P in C['prime_records']}
    ck(list(primes)==[27,28,29,30,31,1],'exact partial domain primes')
    for index,P in primes.items():
        p=P['source']['p'];ck(P['source']==base['generators'][index],'prime source')
        for n,lat in enumerate(P['powers']):
            rows=lat['rows'];ck(abs(v.det(rows))==p**n==lat['norm'],'all ideal indices')
            gens=([list(map(int,one))]+[[int(i==j) for i in range(4)] for j in range(1,4)]) if n==0 else (
                P['source']['lattice']['columns'] if n==1 else [v.times(v.vec(a),v.vec(b)) for a in P['powers'][n-1]['rows'] for b in P['powers'][1]['rows']])
            ck(all(v.member(rows,g) for g in gens),'all ideal reverse containments')
            for co,row in zip(lat['forward'],rows):
                ck([sum(Q(c)*Q(g[k]) for c,g in zip(co,gens)) for k in range(4)]==v.vec(row),'all ideal forward containments')
        pi=v.vec(P['uniformizer'])
        ck(v.member(P['powers'][1]['rows'],pi) and not v.member(P['powers'][2]['rows'],pi),'uniformizer')
        v.integralcheck(P['rational_prime_class'],v.vec([p,0,0,0]),P,p)
    A=model['field']['alpha_polynomial'];der=[i*A[i] for i in range(1,5)]
    roots={}
    for r in C['simple_roots']:
        p=r['p'];t=r['seed'];mod=p
        for n,s in enumerate(r['steps'],1):
            ck(s['root']==t and s['precision']==n and ev(A,t)==s['value'] and ev(der,t)==s['derivative'],'complete Hensel source values')
            ck(ev(A,t)%mod==0 and ev(der,t)%p!=0 and 0<=s['digit']<p,'simple Hensel hypotheses')
            t+=s['digit']*mod;mod*=p
        ck(t==r['root'] and mod==r['modulus']==p**r['precision'] and ev(A,t)%mod==0,'Hensel final certificate')
        roots[p]=r
    for rec in C['classes']:
        mask=rec['mask'];q=Q(1);b=one[:]
        for j,w in enumerate(sources['two-adic-filter-certificate.json']['witnesses']):
            if mask>>j&1:
                q*=Q(w['source']['inverse_norm']);b=v.times(b,v.vec(w['source']['coefficients']))
        ck(q==Q(rec['rational']) and b==toO(rec['quartic_power']),'independent full product reconstruction')
        ck(q*v.det([v.times(b,[Q(i==j) for i in range(4)]) for j in range(4)])==1,'independent norm one')
        sets=[rec['local_tests'],rec['mixed_simple_root_tests']]
        ck([t['prime_index'] for t in sets[0]]==[27,28,29,30,31,1],'all six rational-row odd tests')
        ck([t['prime_index'] for t in sets[1]]==[27,29,31],'three mixed partial tests')
        for kind,tests in enumerate(sets):
            for t in tests:
                P=primes[t['prime_index']];p=t['p'];e=P['rational_prime_class']['valuation']
                if kind==0:
                    a=toO(rec['row']['quaternion_a_power']);c=toO(rec['row']['quaternion_c_power'])
                    ck(v.times(a,b)==v.scale(one,q),'rational-row a identity')
                    ck(v.times(c,b)==v.plus(v.scale(one,9075),v.scale(eta,-1)),'rational-row c identity')
                else:
                    root=roots[p];x=Q(root['root']);N=root['precision']
                    bi=ev(rec['quartic_power'],x);ti=ev(model['field']['eta_in_alpha'],x)
                    ck(bi==Q(t['first_d_approx']) and ti==Q(t['first_theta_approx']),'mixed exact evaluations')
                    a=toO(t['quaternion_a_power']);c=toO(t['quaternion_c_power'])
                    ck(v.times(a,b)==v.scale(one,bi),'mixed-row a identity')
                    ck(v.times(c,b)==v.plus(v.scale(one,ti),v.scale(eta,-1)),'mixed-row c identity')
                    gap=v.plus(v.scale(one,x),v.scale(alpha,-1))
                    v.fieldcheck(t['second_alpha_gap'],gap,P,p)
                    g=t['second_alpha_gap'];gv=g['integral_class']['valuation']-e*g['denominator_valuation']
                    ck(gv==0==t['second_alpha_gap_valuation'],'distinct local branches')
                    # Independent evaluation of v_P(b) through determinant
                    # lattice membership of the exact integral representative.
                    den=1
                    from math import lcm
                    for z in b:den=lcm(den,z.denominator)
                    bb=v.scale(b,den);valb=0
                    while v.member(P['powers'][valb+1]['rows'],bb):valb+=1
                    valb-=e*v.val(den,p)
                    ea=e*(N+min(v.val(Q(z),p) for z in rec['quartic_power'] if Q(z)))-valb
                    ec=e*(N+min(v.val(Q(z),p) for z in model['field']['eta_in_alpha'] if Q(z)))-valb
                    ck(ea==t['a_error_valuation_lower'] and ec==t['c_error_valuation_lower'],'independent error bounds')
                    ck(ea>t['quaternion_a']['valuation'] and ec>t['quaternion_c']['valuation'],'strict leading-unit stability')
                am=v.fieldcheck(t['quaternion_a'],a,P,p);cm=v.fieldcheck(t['quaternion_c'],c,P,p)
                for s in ('quaternion_a','quaternion_c'):
                    z=t[s];ck(z['valuation']==z['integral_class']['valuation']-e*z['denominator_valuation'],'full local valuation')
                va=am%2;vc=cm%2
                # Legendre factors from explicit nonsquare enumeration.
                ua=-1 if am//2 else 1;uc=-1 if cm//2 else 1
                symbol=(-1 if p%4==3 else 1)**(va*vc)*ua**vc*uc**va
                ck(symbol==t['hilbert_symbol']==1 and t['hilbert_exponent']==0,'independent odd Hilbert value')
                R['odd_tests']+=1
        rs=rec['real_roots'];ck(len(rs)==5,'five real roots')
        signs=[];theta_boxes=[]
        for i,ri in enumerate(rs):
            if i==0:
                theta_boxes.append([Q(9075)]*2);signs.append(1);ck(q>0,'positive rational coefficient')
                continue
            lo,hi=map(Q,ri['alpha_interval']);ck(ev(A,lo)*ev(A,hi)<0,'real root isolation')
            if i>1:ck(Q(rs[i-1]['alpha_interval'][1])<lo,'disjoint root intervals')
            db=interval(rec['quartic_power'],lo,hi)
            tb=interval(model['field']['eta_in_alpha'],lo,hi)
            ck(db[0]>0 or db[1]<0,'independently established coefficient sign')
            signs.append(1 if db[0]>0 else -1);theta_boxes.append(tb)
        ck(len(rec['real_pair_tests'])==20 and len({(t['first'],t['second']) for t in rec['real_pair_tests']})==20,'all ordered real pairs')
        for t in rec['real_pair_tests']:
            i,j=t['first'],t['second'];ck(i!=j,'off diagonal')
            diff=[theta_boxes[j][0]-theta_boxes[i][1],theta_boxes[j][1]-theta_boxes[i][0]]
            cs=1 if diff[0]>0 else -1 if diff[1]<0 else 0
            s=[signs[j],-signs[i],cs]
            ck(s==t['coefficient_signs'] and 0 not in s and min(s)<0<max(s) and t['split'],'complete real mixed signs')
            R['real_tests']+=1
        ck(rec['good'] is None,'no unjustified goodness decision')
    ck(R['odd_tests']==18 and R['real_tests']==40,'exact partial domain count')
    ck(C['full_goodness_decided'] is False and C['pairing_computed'] is False,'unfinished boundary retained')
    R['helper_checks']=v.R['checks'];R['max_rational_bits']=v.R['max_rational_bits']
    R['completed']=True


if __name__=='__main__':
    try:main()
    except Exception as e:R['failures'].append(dict(message=str(e),traceback=traceback.format_exc()))
    OUT.write_text(json.dumps(R,indent=2)+'\n')
    print(json.dumps(dict(completed=R['completed'],checks=R['checks'],helper_checks=R.get('helper_checks'),
         odd_tests=R['odd_tests'],real_tests=R['real_tests'],failures=[x['message'] for x in R['failures']],
         full_goodness_decided=False,path=str(OUT))))
    raise SystemExit(0 if R['completed'] else 1)
