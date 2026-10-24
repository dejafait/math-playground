"""Independent full actual-union and signed-subset-action reconstruction.

Imports no constructor; consumes every saved entry, block and endpoint.
The finite signed action checks both rectangular directions coherently.
"""
import gzip
import hashlib
import json
from collections import Counter
from fractions import Fraction as F
from itertools import combinations, permutations, product
from math import factorial
from pathlib import Path

B=Path(__file__).resolve().parent
ROOT=B.parent.parent
SOURCE=B/'fixed-product-three-shell.json'
OUT=B/'fixed-product-three-shell-verification.json'


def choose(n,k):
    return factorial(n)//factorial(k)//factorial(n-k) if 0<=k<=n else 0


def enc(v):
    return [v.numerator,v.denominator]


def pack(v):
    return [enc(w) for w in v]


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def plus(v,w):
    return v[0]+w[0],v[1]+w[1]


def times(v,q):
    return (q*v[0],q*v[1]) if q>=0 else (q*v[1],q*v[0])


def interval_product(v,w):
    corners=[a*b for a,b in product(v,w)]
    return min(corners),max(corners)


def interval_square(v):
    return (min(a*a for a in v) if v[0]*v[1]>0 else F(0),max(a*a for a in v))


def main():
    saved=json.loads(SOURCE.read_text())
    counts=Counter()
    report=dict(stage='in_progress',failures=[],source_sha256=sha(SOURCE),code_sha256=sha(Path(__file__)))

    def save():
        report.update(checks=sum(counts.values()),checks_by_kind=dict(counts))
        OUT.write_text(json.dumps(report,indent=2)+'\n')

    def ck(kind,ok,detail=None):
        counts[kind]+=1
        if not ok:
            report['failures'].append(dict(kind=kind,detail=detail))
            report['stage']='failed'
            save()
            raise AssertionError((kind,detail))

    ck('constructor_code_binding',saved['code_sha256']==sha(B/'fixed_product_three_shell.py'))
    for p,h in saved['input_sha256'].items():
        ck('every_input_binding',sha(ROOT/p)==h,p)
    # Bind every retained audit, rather than taking a success count as evidence.
    for name,code in [('l112-l113-critical-audit.json','critical_audit_l112_l113.py'),
                      ('l114-critical-audit.json','critical_audit_l114.py'),
                      ('l115-critical-audit.json','critical_audit_l115.py'),
                      ('l116-critical-audit.json','critical_audit_l116.py'),
                      ('l117-critical-audit.json','critical_audit_l117.py')]:
        audit=json.loads((B/name).read_text())
        ck('retained_audit',audit['stage']=='verified' and not audit['failures'] and
           audit['code_sha256']==sha(B/code),name)
        for p,h in audit['input_sha256'].items():
            ck('every_audit_binding',sha(ROOT/p)==h,p)
        replays=audit.get('replay_sha256',{})
        if isinstance(replays,str):
            replays={'l115-critical-reverification.json':replays}
        for p,h in replays.items():
            ck('every_audit_replay',sha(B/p)==h,p)
    with gzip.open(B/'positive-factor-enclosure.json.gz','rt') as f:
        z=json.load(f)
    lp=json.loads((B/'delsarte-lp-results.json').read_text())
    N=65537**28//2**128+1
    H=choose(1024,68)
    U=F(choose(1024,64),choose(68,64))
    a=[F(v['numerator'],v['denominator']) for v in lp['exact']['primal']]
    g=[choose(68,i)*choose(956,i) for i in range(69)]
    c=[F(1)]+[F(0)]*4+[(N-1)*a[i-5]/((U-1)*g[i]) for i in range(5,69)]
    ck('canonical_data',len(a)==64 and min(a)>0 and sum(a)==U-1 and
       list(map(enc,c))==saved['c']==z['c'] and saved['N']==z['N']==N and
       saved['H']==z['H']==H and F(*saved['rho'])==F(N,H)>0 and
       sum(g[i]*c[i] for i in range(69))==N and all(0<x<=1 for x in c[5:]) and
       (N-1)*2**128<=65537**28<N*2**128)
    ck('box_contract',z['Q']==10**70 and z['radius']==10**25 and
       len(z['point'])==len(z['scale_powers'])==len(saved['endpoints'])==64 and
       z['box']==[[v-10**25,v+10**25] for v in z['point']])
    box={}
    for i in range(5,69):
        k=i-5
        scale=F(10**z['scale_powers'][k]) if z['scale_powers'][k]>=0 else F(1,10**(-z['scale_powers'][k]))
        box[i]=tuple(scale*F(z['point'][k]+sign*10**25,10**70) for sign in (-1,1))
        ck('all_original_endpoints',saved['endpoints'][k]==dict(i=i,interval=pack(box[i])) and
           0<box[i][0]<box[i][1],i)
    margins=[min(l+10**25,10**25-u) for l,u in z['krawczyk_image']]
    root_audit=json.loads((B/'l112-l113-critical-audit.json').read_text())
    ck('all_root_margins',len(margins)==64 and min(margins)>0 and
       margins==z['inclusion_margins'] and min(margins)==root_audit['minimum_margin_units'])
    lower=json.loads((B/'l114-critical-audit.json').read_text())
    ck('complete_lower_rows',len(lower['rows'])==64)
    for i,row in enumerate(lower['rows'],5):
        ck('retained_lower_input',row['i']==i and F(row['pair_numerator'],row['denominator'])==c[i] and
           row['reconstructed_minimum_numerator']==2*row['pair_numerator'] and
           row['distinct_lower_sum_numerator']==row['required']==0,i)

    # Actual complete sets, including all six presentations of each relation.
    A=set(range(68))
    dictionary=[]
    entry={}
    collisions={}
    repetitions=Counter()
    index=0
    for l,m in [(l,m) for l in (5,6,7) for m in (5,6,7) if l<=m]:
        X=set(range(l)); Y=set(range(68,68+l)); P=(A-X)|Y
        for t,s in product(range(min(l,m)+1),repeat=2):
            XX=set(range(t))|set(range(l,l+m-t))
            YY=set(range(68,68+s))|set(range(68+l,68+l+m-s))
            Q=(A-XX)|YY
            words=[A,P,Q]
            atoms=[sum(sum(1<<j for j,W in enumerate(words) if v in W)==mask for v in range(1024))
                   for mask in range(8)]
            ck('actual_complete_atoms',sum(atoms)==1024 and min(atoms)>=0 and
               all(len(W)==68 for W in words) and len(A-P)==l and len(A-Q)==m and
               len((A-P)&(A-Q))==t and len((P-A)&(Q-A))==s,[l,m,t,s])
            presentation=[]
            values=[]
            for order in permutations(range(3)):
                R,S,T=[words[j] for j in order]
                i,j,h=len(R-S),len(R-T),len(S-T)
                tt,ss=len((R-S)&(R-T)),len((S-R)&(T-R))
                D=choose(i,tt)*choose(68-i,j-tt)*choose(i,ss)*choose(956-i,j-ss)
                head=factorial(68)//(factorial(i-tt)*factorial(j-tt)*factorial(tt)*factorial(68-i-j+tt))
                tail=factorial(956)//(factorial(i-ss)*factorial(j-ss)*factorial(ss)*factorial(956-i-j+ss))
                ck('six_actual_source_presentations',D>0 and h==i+j-tt-ss and tt-ss==t-s and
                   head*tail==g[i]*D,[l,m,t,s,list(order)])
                if min(i,j,h)==0:
                    value=(c[max(i,j,h)],)*2
                    repetitions['coincident' if i==0 else 'first' if j==0 else 'second']+=1
                    ck('both_endpoint_repetitions',D==(g[j] if i==0 else 1),[l,m,t,s,order])
                elif min(i,j,h)<5:
                    value=(F(0),F(0))
                    ck('null_capacity',min(c[i],c[j],c[h])==0,[i,j,h])
                else:
                    value=tuple(box[i][k]*box[j][k]*box[h][k] for k in (0,1))
                values.append(value)
                presentation.append(dict(order=list(order),orbit=[i,j,tt,ss],h=h,D=D,full_count=g[i]*D,
                                         opposite_pair=enc(c[h]),union_interval=pack(value)))
            D0=choose(l,t)*choose(68-l,m-t)*choose(l,s)*choose(956-l,m-s)
            ck('all_six_counts_and_entries',len(set(values))==1 and
               all(p['full_count']==g[l]*D0 for p in presentation),[l,m,t,s])
            expected=dict(layers=[l,m],intersections=[t,s],h=l+m-t-s,D=D0,interval=pack(values[0]))
            ck('every_saved_source_entry',saved['entries'][index]==expected,index)
            entry[l,m,t,s]=values[0]
            key=min(tuple(sum(sum(1<<j for j in range(3) if v in words[order[j]])==mask for v in range(1024))
                          for mask in range(8)) for order in permutations(range(3)))
            ck('full_key_collisions',key not in collisions or collisions[key]==values[0],[l,m,t,s])
            collisions[key]=values[0]
            dictionary.append(dict(**expected,atoms=atoms,presentations=presentation,canonical_key=list(key)))
            index+=1
    ck('complete_relations_and_repetitions',len(saved['entries'])==index==270 and
       sum(len(d['presentations']) for d in dictionary)==1620 and
       repetitions==dict(coincident=6,first=6,second=6))

    # Harmonic signed pair differences: evaluate at an l-set containing all
    # positive partners, no negative partners, and l-k ordinary points.
    # Every m-set with nonzero function chooses exactly one of each pair.
    # The coefficient counts complete subsets, independently of beta.
    actions={}
    records=[]
    for n in (68,956):
        for l,m in product((5,6,7),repeat=2):
            for k in range(min(l,m)+1):
                val=[0]*(min(l,m)+1)
                terms=[]
                for zneg in range(k+1):
                    for b in range(l-k+1):
                        t=k-zneg+b
                        v=(-1)**zneg*choose(k,zneg)*choose(l-k,b)*choose(n-l-k,m-k-b)
                        if v:
                            ck('valid_subset_intersection',0<=t<=min(l,m),[n,l,m,k,zneg,b])
                            val[t]+=v
                        terms.append(dict(negative_choices=zneg,ordinary_intersection=b,t=t,signed_count=v))
                Dl=choose(n-2*k,l-k)
                ck('positive_harmonic_norm',Dl>0,[n,l,k])
                betas=[]
                for t in range(min(l,m)+1):
                    source=sum((-1)**(u-t)*choose(u,t)*choose(n-2*k,u-k)*
                               choose(n-k-u,l-u)*choose(n-k-u,m-u)
                               for u in range(max(k,t),min(l,m)+1))
                    ck('signed_beta_normalization',source==Dl*val[t],[n,l,m,k,t])
                    betas.append(source)
                actions[n,l,m,k]=val
                records.append(dict(n=n,l=l,m=m,k=k,D=Dl,norm=2**k*Dl,terms=terms,
                                    action=val,beta=betas))
        for l,m in combinations((5,6,7),2):
            for k in range(l+1):
                for t in range(l+1):
                    ck('both_signed_rectangular_directions',
                       choose(n-2*k,l-k)*actions[n,l,m,k][t]==
                       choose(n-2*k,m-k)*actions[n,m,l,k][t],[n,l,m,k,t])
    mult={n:[choose(n,k)-choose(n,k-1) for k in range(8)] for n in (68,956)}
    ck('every_multiplicity_and_dimension',saved['multiplicities']=={str(n):v for n,v in mult.items()} and
       all(v>0 for n in mult for v in mult[n]) and saved['sizes']=={str(l):g[l] for l in (5,6,7)} and
       all(sum(mult[68][:l+1])*sum(mult[956][:l+1])==g[l] for l in (5,6,7)))
    old=json.loads((B/'fixed-product-coupled.json').read_text())
    frozen=json.loads((B/'fixed-product-three-shell-frozen-input.json').read_text())
    ck('entire_frozen_original',frozen=={key:z[key] for key in frozen})
    anchor=[]
    for l,m in [(0,0)]+[(l,m) for k in (5,6,7) for l,m in [(0,k),(k,0)]]:
        value=c[max(l,m)]
        DD=g[m] if l==0 else 1
        ck('included_anchor_source',value==c[l]*c[m] if min(l,m)==0 else False,[l,m])
        anchor.append(dict(layers=[l,m],orbit=[l,m,0,0],D=DD,h=l+m,value=enc(value),opposite_pair=enc(c[l+m])))
    modes=[]; all_minors=[]
    trace_coefficients={l:{h:F(0) for h in range(5,2*l+1)} for l in (5,6,7)}
    trace_diagonal={l:F(0) for l in (5,6,7)}
    trace_anchor={l:F(0) for l in (5,6,7)}
    for aa,bb in product(range(8),repeat=2):
        layers=[l for l in (5,6,7) if l>=max(aa,bb)]
        D={l:choose(68-2*aa,l-aa)*choose(956-2*bb,l-bb) for l in layers}
        blocks={}; corrections={}; poly={}
        multiplicity=mult[68][aa]*mult[956][bb]
        for l,m in [(l,m) for l in layers for m in layers if l<=m]:
            v=(F(0),F(0)); coeff={h:0 for h in range(5,l+m+1)}; diag=0
            for t,s in product(range(min(l,m)+1),repeat=2):
                w=D[l]*actions[68,l,m,aa][t]*actions[956,l,m,bb][s]
                v=plus(v,times(entry[l,m,t,s],w))
                h=l+m-t-s
                if h>=5: coeff[h]+=w
                if h==0: diag+=w
            linear=(sum(w*box[h][0 if w>=0 else 1] for h,w in coeff.items()),
                    sum(w*box[h][1 if w>=0 else 0] for h,w in coeff.items()))
            collected=plus(interval_product(interval_product(box[l],box[m]),linear),(diag*c[l],)*2)
            ck('independent_collected_enclosure',v[0]<=collected[0]<=collected[1]<=v[1],[aa,bb,l,m])
            correction=c[l]*c[m]*g[l]*g[m] if aa==bb==0 else F(0)
            blocks[l,m]=plus(v,(-correction,-correction)); corrections[l,m]=correction
            poly[l,m]=dict(constant=enc(diag*c[l]),coefficients=coeff)
            if l==m:
                for h,w in coeff.items(): trace_coefficients[l][h]+=F(multiplicity*w,D[l])
                trace_diagonal[l]+=F(multiplicity*diag,D[l])*c[l]
                trace_anchor[l]+=F(multiplicity,D[l])*correction
        if max(aa,bb)<=6:
            previous=old['modes'][7*aa+bb]
            ck('entire_L116_restriction',all(pack(v)==previous['blocks'][str(l)+str(m)]
               for (l,m),v in blocks.items() if m<=6),[aa,bb])
        # Independently verify every interval LDL stage, with no inversion
        # unless the entire denominator interval is strictly positive.
        current=dict(blocks); stages=[]; pivots=[]
        for pos,l in enumerate(layers):
            pp=current[l,l]
            pivots.append(dict(layer=l,interval=pack(pp),normalized=pack(times(pp,1/(c[l]*D[l])))))
            stages.append({str(i)+str(j):pack(v) for (i,j),v in current.items()})
            if pp[0]<=0: break
            inv=(1/pp[1],1/pp[0]); after={}
            for i,j in combinations(layers[pos+1:],2):
                cost=interval_product(interval_product(current[l,i],current[l,j]),inv)
                after[i,j]=plus(current[i,j],times(cost,-1))
            for i in layers[pos+1:]:
                cost=interval_product(interval_square(current[l,i]),inv)
                after[i,i]=plus(current[i,i],times(cost,-1))
            current=after
        if max(aa,bb)<=6:
            ck('all_old_pivots',all(p['normalized']==previous['five_normalized' if p['layer']==5 else 'remainder_normalized']
               for p in pivots if p['layer']<=6),[aa,bb])
        positive=len(pivots)==len(layers) and all(F(*p['interval'][0])>0 for p in pivots)
        verdict='positive' if positive else 'unresolved'
        direction=None; quadratic=None
        if not positive:
            # Verify an actually recorded fixed vector, rather than trusting
            # its midpoint proposal or repeating its construction.
            raw=saved['modes'][8*aa+bb]['direction']
            if raw is not None:
                direction=[F(*q) for q in raw]
                ck('nonzero_fixed_rational_direction',len(direction)==len(layers) and any(direction),[aa,bb])
                quadratic=(F(0),F(0))
                for i,l in enumerate(layers):
                    for j,m in enumerate(layers):
                        quadratic=plus(quadratic,times(blocks[min(l,m),max(l,m)],direction[i]*direction[j]))
                quadratic=times(quadratic,1/(c[7]*D[7]))
                if quadratic[1]<0: verdict='negative'
        mode=dict(a=aa,b=bb,layers=layers,multiplicity=multiplicity,scaling={str(l):v for l,v in D.items()},
            blocks={str(l)+str(m):pack(v) for (l,m),v in blocks.items()},
            anchor_correction={str(l)+str(m):enc(v) for (l,m),v in corrections.items()},
            elimination_stages=stages,pivots=pivots,direction=list(map(enc,direction)) if direction else None,
            quadratic_normalized=pack(quadratic) if quadratic else None,verdict=verdict)
        ck('every_full_block_stage_pivot_and_verdict',mode==saved['modes'][8*aa+bb],[aa,bb])
        if aa==bb==0:
            ck('one_full_constant_anchor',all(corrections[l,m]==c[l]*g[l]*c[m]*g[m] for l,m in corrections)
               and all(D[l]==g[l] for l in layers) and len(corrections)==6)
        else: ck('no_nonconstant_anchor',not any(corrections.values()),[aa,bb])
        # A second PSD certificate: all nonempty principal determinants,
        # directly expanded over permutations of each complete block.
        for size in range(1,len(layers)+1):
            for subset in combinations(layers,size):
                det=(F(0),F(0))
                for perm in permutations(range(size)):
                    inversions=sum(perm[i]>perm[j] for i in range(size) for j in range(i+1,size))
                    term=(F(1),F(1))
                    for i,j in enumerate(perm):
                        l,m=sorted((subset[i],subset[j]))
                        term=interval_product(term,blocks[l,m])
                    det=plus(det,times(term,(-1)**inversions))
                denominator=F(1)
                for l in subset: denominator*=c[l]*D[l]
                normalized=times(det,1/denominator)
                all_minors.append(dict(mode=[aa,bb],layers=list(subset),interval=pack(det),normalized=pack(normalized)))
        modes.append(mode)
    for l in (5,6,7):
        ck('every_diagonal_polynomial_trace',all(v==0 for v in trace_coefficients[l].values()) and
           trace_diagonal[l]==g[l]*c[l] and trace_anchor[l]==g[l]*c[l]**2,l)
    ck('all_source_modes',len(saved['modes'])==len(modes)==64 and
       Counter(len(m['layers']) for m in modes)=={3:36,2:13,1:15} and len(all_minors)==306)
    signs=Counter(m['verdict'] for m in modes)
    verdict='FIXED_PRODUCT_EXCLUDED' if signs['negative'] else 'THREE_SHELL_PASSES' if signs['positive']==64 else 'INCONCLUSIVE'
    summary=dict(counts=dict(signs),verdict=verdict,
        negative_modes=[[m['a'],m['b']] for m in modes if m['verdict']=='negative'],
        unresolved_modes=[[m['a'],m['b']] for m in modes if m['verdict']=='unresolved'])
    ck('complete_saved_summary',saved['summary']==summary and saved['stage']=='complete' and not saved['failures'])
    minimum=min((F(*p['normalized'][0]),m['a'],m['b'],p['layer']) for m in modes for p in m['pivots'])
    per_layer={}
    for l in (5,6,7):
        vv=min((F(*p['normalized'][0]),m['a'],m['b']) for m in modes for p in m['pivots'] if p['layer']==l)
        kk=vv[0]*10**6//1
        ck('exact_layer_minimum_bracket',F(kk,10**6)<=vv[0]<F(kk+1,10**6),l)
        per_layer[str(l)]=dict(mode=list(vv[1:]),value=enc(vv[0]),bracket=[enc(F(kk,10**6)),enc(F(kk+1,10**6))])
    ck('all_positive_pivots_and_minors',sum(len(m['pivots']) for m in modes)==149 and
       all(F(*p['interval'][0])>0 for m in modes for p in m['pivots']) and
       all(F(*v['interval'][0])>0 for v in all_minors))
    minminor=min(F(*v['normalized'][0]) for v in all_minors)
    report.update(stage='verified',dictionary=dictionary,signed_actions=records,modes=modes,summary=summary,
        anchor=anchor,principal_minors=all_minors,repetitions=dict(repetitions),
        trace_coefficients={str(l):{str(h):enc(v) for h,v in row.items()} for l,row in trace_coefficients.items()},
        trace_diagonal={str(l):enc(v) for l,v in trace_diagonal.items()},
        trace_anchor={str(l):enc(v) for l,v in trace_anchor.items()},
        minimum_normalized_pivot=dict(mode=list(minimum[1:3]),layer=minimum[3],value=enc(minimum[0])),
        minimum_normalized_minor=enc(minminor),per_layer_minimum_pivot=per_layer,
        principal_minor_counts=dict(Counter('positive' if F(*v['interval'][0])>0 else 'negative' if F(*v['interval'][1])<0 else 'unresolved' for v in all_minors)))
    save()
    q=minimum[0]*10**6//1
    print('Independent checks:',sum(counts.values()),'; failures:',report['failures'])
    print('Actual/required relations 270/270; presentations 1620/1620; modes 64/64; signs:',dict(signs))
    print('Both signed orientations of all three rectangles and entire L116 restriction recovered.')
    print('Minimum normalized pivot lower at',minimum[1:],'in [',q,',',q+1,')/10^6; required >0')
    print('Layer-wise pivot lower brackets /10^6:',{l:[F(*v['bracket'][0])*10**6,F(*v['bracket'][1])*10**6] for l,v in per_layer.items()})
    print('Complete principal minors:',report['principal_minor_counts'],'/ required 306 PSD; verdict:',verdict)
    print('Full certificate:',OUT.relative_to(ROOT))


if __name__=='__main__':
    main()
