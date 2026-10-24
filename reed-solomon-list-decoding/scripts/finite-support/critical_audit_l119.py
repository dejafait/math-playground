"""Bounded manuscript/evidence audit of L119; preserve every original.

Replay the full independent verifier, then use atom permutations and
closed determinant formulas as additional checks. No candidate generation.
"""
from collections import Counter
from fractions import Fraction as F
import gzip
import hashlib
import importlib.util
from itertools import combinations, permutations, product
import json
from math import comb, factorial
from pathlib import Path

B = Path(__file__).resolve().parent
ROOT = B.parent.parent
OUT = B/'l119-critical-audit.json'


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def read(n):
    return json.loads((B/n).read_text())


def enc(q):
    return [q.numerator, q.denominator]


def pack(v):
    return list(map(enc, v))


def unpack(v):
    return tuple(F(*q) for q in v)


def choose(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def add(*vs):
    return sum(v[0] for v in vs), sum(v[1] for v in vs)


def neg(v):
    return -v[1], -v[0]


def mul(*vs):
    vals = [F(1)]
    for v in vs:
        vals = [q*r for q in vals for r in v]
    return min(vals), max(vals)


def sq(v):
    return (F(0) if v[0] <= 0 <= v[1] else min(q*q for q in v), max(q*q for q in v))


def divide_positive(v, p):
    assert p[0] > 0 and p[1] >= p[0]
    return mul(v, (1/p[1], 1/p[0]))


def congruence(K, T):
    n = len(K)
    return [[sum(T[u][i]*K[u][v]*T[v][j] for u in range(n) for v in range(n))
             for j in range(n)] for i in range(n)]


def main():
    counts = Counter()
    report = dict(stage='in_progress', failures=[], code_sha256=sha(Path(__file__)))

    def save():
        report.update(checks=sum(counts.values()), checks_by_kind=dict(counts))
        OUT.write_text(json.dumps(report, indent=2)+'\n')

    def ck(kind, ok, detail=None):
        counts[kind] += 1
        if not ok:
            report['failures'].append(dict(kind=kind, detail=detail))
            report['stage'] = 'failed'
            save()
            raise AssertionError((kind, detail))

    source = read('fixed-product-excluded-three-shell.json')
    paths = set(source['input_sha256'])
    paths.update('scripts/finite-support/'+n for n in [
        'fixed-product-excluded-three-shell.json','fixed-product-excluded-three-shell-verification.json',
        'fixed_product_excluded_three_shell.py','verify_fixed_product_excluded_three_shell.py'])
    report['input_sha256'] = {p:sha(ROOT/p) for p in sorted(paths)}
    save()
    spec = importlib.util.spec_from_file_location('l119_replay', B/'verify_fixed_product_excluded_three_shell.py')
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    mod.OUT = B/'l119-critical-reverification.json'
    mod.main()
    replay = read('l119-critical-reverification.json')
    ck('complete_replay_equality', replay == read('fixed-product-excluded-three-shell-verification.json'))
    ck('complete_constructor_mode_equality', replay['modes'] == source['modes'])

    with gzip.open(B/'positive-factor-enclosure.json.gz', 'rt') as f:
        z = json.load(f)
    frozen = read('fixed-product-three-shell-frozen-input.json')
    ck('frozen_required_fields', set(frozen) >= {'point','scale_powers','box','N','H','Q','radius'})
    ck('lossless_frozen_extraction', frozen == {k:z[k] for k in frozen})
    N, H = 65537**28//2**128+1, comb(1024,68)
    U = F(comb(1024,64),comb(68,64))
    g = [choose(68,i)*choose(956,i) for i in range(69)]
    lp = read('delsarte-lp-results.json')
    av = [F(v['numerator'],v['denominator']) for v in lp['exact']['primal']]
    c = [F(1)]+[F(0)]*4+[(N-1)*av[i-5]/((U-1)*g[i]) for i in range(5,69)]
    ck('exact_N_pairs_normalization', source['N'] == z['N'] == N and source['H'] == z['H'] == H and
       F(*source['rho']) == F(N,H) > 0 and list(map(enc,c)) == source['c'] == z['c'] and
       len(av) == 64 and min(av)>0 and sum(av)==U-1 and sum(g[i]*c[i] for i in range(69))==N)
    ck('all_box_lengths', len(z['point']) == len(z['scale_powers']) == len(z['box']) ==
       len(source['endpoints']) == 64 and z['Q']==10**70 and z['radius']==10**25)
    box = {}; endpoints = []
    for i in range(5,69):
        q,p = z['point'][i-5],z['scale_powers'][i-5]
        v = tuple(F(10)**p*F(q+sgn*10**25,10**70) for sgn in (-1,1))
        ck('each_original_point_scale_endpoint', z['box'][i-5]==[q-10**25,q+10**25] and
           source['endpoints'][i-5]==dict(i=i,interval=pack(v)) and 0<v[0]<v[1],i)
        box[i]=v
        endpoints.append(dict(i=i,point=q,scale_power=p,interval=pack(v)))

    pairs = list(combinations((5,6,7),2))
    layerpairs = [(l,m) for l in (5,6,7) for m in (5,6,7) if l<=m]
    dictionary = replay['dictionary']
    ck('complete_dictionary_order', [(r['layers'],r['intersections']) for r in dictionary] ==
       [([l,m],[t,s]) for l,m in layerpairs for t,s in product(range(l+1),repeat=2)])
    repeats=Counter(); nulls=Counter()
    for row in dictionary:
        l,m=row['layers']; t,s=row['intersections']
        atoms=[956-l-m+s,t,l-s,m-t,m-s,l-t,s,68-l-m+t]
        ck('manuscript_atoms', row['atoms']==atoms and min(atoms)>=0 and sum(atoms)==1024,[l,m,t,s])
        ck('all_six_orders', [r['order'] for r in row['presentations']]==list(map(list,permutations(range(3)))))
        for r in row['presentations']:
            q=[0]*8
            for mask,v in enumerate(atoms):
                q[sum(1<<j for j,old in enumerate(r['order']) if mask & (1<<old))]=v
            i,j,tt,ss,h=q[1]+q[5],q[1]+q[3],q[1],q[6],q[2]+q[3]
            D=choose(i,tt)*choose(68-i,j-tt)*choose(i,ss)*choose(956-i,j-ss)
            denom=1
            for size in q: denom*=factorial(size)
            full=F(factorial(68)*factorial(956),denom)
            ck('every_source_presentation', r['orbit']==[i,j,tt,ss] and r['h']==h==i+j-tt-ss and
               tt-ss==t-s and r['D']==D>0 and r['full_count']==full==g[i]*D==g[l]*row['D'],
               [l,m,t,s,r['order']])
            if min(i,j,h)==0:
                repeats['coincident' if i==0 else 'first' if j==0 else 'second']+=1
                val=(c[max(i,j,h)],)*2
                ck('Boolean_multiplicity',D==(g[j] if i==0 else 1))
            elif min(i,j,h)<5:
                val=(F(0),)*2
                nulls['opposite' if h<5 else 'anchored']+=1
                ck('null_capacity', min(c[i],c[j],c[h])==0)
            else:
                val=tuple(box[i][e]*box[j][e]*box[h][e] for e in (0,1))
            ck('own_opposite_and_shared_union', r['opposite_pair']==enc(c[h]) and
               r['union_interval']==pack(val)==row['y_interval'] and
               r['affine_interval']==pack((c[h]-val[1],c[h]-val[0])))
    ck('complete_repeated_cases',repeats==replay['repetitions']==dict(coincident=6,first=6,second=6))

    ck('complete_null_split',nulls==dict(opposite=136,anchored=272))

    action={}
    ck('complete_action_order',[(r['n'],r['l'],r['m'],r['k']) for r in replay['signed_actions']]==
       [(n,l,m,k) for n in (68,956) for l,m in product((5,6,7),repeat=2) for k in range(min(l,m)+1)])
    for r in replay['signed_actions']:
        n,l,m,k=r['n'],r['l'],r['m'],r['k']
        terms=[dict(negative_choices=z,ordinary_intersection=b,t=k-z+b,
                    signed_count=(-1)**z*choose(k,z)*choose(l-k,b)*choose(n-l-k,m-k-b))
               for z in range(k+1) for b in range(l-k+1)]
        eta=[sum(v['signed_count'] for v in terms if v['t']==t) for t in range(min(l,m)+1)]
        d=choose(n-2*k,l-k)
        ck('every_signed_term_and_norm',r['terms']==terms and r['D']==d>0 and
           r['norm']==2**k*d and r['action']==eta and r['beta']==[d*v for v in eta],[n,l,m,k])
        action[n,l,m,k]=eta
    for n,(l,m) in product((68,956),pairs):
        for k,t in product(range(l+1),repeat=2):
            ck('all_three_coherent_rectangles', choose(n-2*k,l-k)*action[n,l,m,k][t]==
               choose(n-2*k,m-k)*action[n,m,l,k][t],[n,l,m,k,t])

    anchors=[(0,0)]+[p for l in (5,6,7) for p in [(0,l),(l,0)]]
    ck('all_anchor_cases',len(replay['anchor'])==7)
    for r,(l,m) in zip(replay['anchor'],anchors):
        ck('full_anchor_source',r==dict(layers=[l,m],orbit=[l,m,0,0],D=g[m] if l==0 else 1,
           h=l+m,pair=enc(c[l+m]),y=enc(c[max(l,m)]),affine=enc(F(0))) and
           c[l+m]-c[max(l,m)]==0)
    ck('all_mode_order',[(r['a'],r['b']) for r in replay['modes']]==list(product(range(8),repeat=2)))
    dimensions=1; pivot_records=[]; minor_records=[]; minimum={}; shapes=Counter()
    required={5:F(60833905223164487,10**6),6:F(62140756033549750,10**6),7:F(62119685418336245,10**6)}
    old=read('fixed-product-excluded.json')
    included=read('fixed-product-three-shell.json')
    for r in replay['modes']:
        a,b=r['a'],r['b']; layers=[l for l in (5,6,7) if l>=max(a,b)]
        d={l:choose(68-2*a,l-a)*choose(956-2*b,l-b) for l in layers}
        mult=(choose(68,a)-choose(68,a-1))*(choose(956,b)-choose(956,b-1))
        ck('full_mode_scaling_multiplicity',r['layers']==layers and r['multiplicity']==mult>0 and
           r['scaling']=={str(l):v for l,v in d.items()} and min(d.values())>0,[a,b])
        dimensions+=mult*len(layers); shapes[len(layers)]+=1
        block={k:unpack(v) for k,v in r['blocks'].items()}
        for key,corr in r['anchor_correction'].items():
            l,m=map(int,key)
            ck('no_anchor_subtraction',F(*corr)==0,[a,b,key])
            pair=F(*r['pair_blocks'][key]); union=unpack(r['y_blocks'][key])
            ck('complete_pair_minus_union',block[key]==(pair-union[1],pair-union[0]),[a,b,key])
            restore=c[l]*c[m]*g[l]*g[m] if a==b==0 else F(0)
            old_union=unpack(included['modes'][8*a+b]['blocks'][key])
            ck('included_transform_identity_only',union==tuple(v+restore for v in old_union),[a,b,key])
        # Keep the zero anchor outside all pivot inversions. Check the
        # generic shell Schur congruence with it explicitly adjoined,
        # using every independent entry endpoint as an identity test.
        keys=list(block)
        for corner in product((0,1),repeat=len(keys)):
            C={key:block[key][e] for key,e in zip(keys,corner)}
            nn=len(layers)
            K=[[F(0)]*(nn+1)]+[[F(0)]+[C[str(min(l,m))+str(max(l,m))]
                for m in layers] for l in layers]
            T=[[F(i==j) for j in range(nn+1)] for i in range(nn+1)]
            pp=K[1][1]
            ck('congruence_positive_shell_pivot',pp>0,[a,b,corner])
            for j in range(2,nn+1): T[1][j]=-K[1][j]/pp
            target=[[F(0)]*(nn+1) for _ in range(nn+1)]
            target[1][1]=pp
            for i in range(2,nn+1):
                for j in range(2,nn+1): target[i][j]=K[i][j]-K[i][1]*K[1][j]/pp
            ck('zero_anchor_shell_congruence_identity',congruence(K,T)==target,[a,b,corner])
        current=dict(block)
        ck('all_stages_pivots_present',len(r['elimination_stages'])==len(r['pivots'])==len(layers))
        for pos,l in enumerate(layers):
            pivot=current[str(l)*2]; scale=c[l]*d[l]
            ck('each_preupdate_stage',r['elimination_stages'][pos]=={k:pack(v) for k,v in current.items()},[a,b,l])
            ck('positive_division_and_threshold',0<pivot[0]<=pivot[1] and
               pivot[0]>=required[l]*scale>0,[a,b,l])
            norm=tuple(v/scale for v in pivot)
            ck('each_full_pivot',r['pivots'][pos]==dict(layer=l,interval=pack(pivot),normalized=pack(norm)),[a,b,l])
            minimum.setdefault(l,[]).append((norm[0],a,b))
            rec=dict(mode=[a,b],layer=l,interval=pack(pivot),normalized=pack(norm),required=enc(required[l]))
            future=layers[pos+1:]; following={}
            for i,j in combinations(future,2):
                following[str(i)+str(j)]=add(current[str(i)+str(j)],neg(divide_positive(
                    mul(current[str(l)+str(i)],current[str(l)+str(j)]),pivot)))
            for i in future:
                v=current[str(l)+str(i)]; q=sq(v); vdiag=current[str(i)*2]
                following[str(i)*2]=add(vdiag,neg(divide_positive(q,pivot)))
                # The final comparison uses no reciprocal: denominator sign
                # is checked independently, then clear it exactly.
                lhs=vdiag[0]*pivot[0]-q[1]
                rhs=required[i]*c[i]*d[i]*pivot[0]
                ck('division_free_next_diagonal',lhs>=rhs>0,[a,b,l,i])
                rec.setdefault('division_free',[]).append(dict(next_layer=i,lhs=enc(lhs),rhs=enc(rhs),slack=enc(lhs-rhs)))
            pivot_records.append(rec)
            current=following
        if max(a,b)<=6:
            previous=old['modes'][7*a+b]
            ck('entire_old_restriction',all(v==previous['blocks'][k] for k,v in r['blocks'].items() if int(k[1])<=6) and
               all(p['normalized']==pack(tuple(v/c[p['layer']] for v in
                   unpack(previous['five_normalized' if p['layer']==5 else 'remainder_normalized'])))
                   for p in r['pivots'] if p['layer']<=6),[a,b])
        for size in range(1,len(layers)+1):
            for sub in combinations(layers,size):
                diag=[block[str(l)*2] for l in sub]
                if size==1: det=diag[0]
                elif size==2:
                    cross=block[''.join(map(str,sub))]
                    det=add(mul(*diag),neg(sq(cross)))
                else:
                    A,C,G=diag; D,E,J=block['56'],block['57'],block['67']
                    # det [[A,D,E],[D,C,J],[E,J,G]]
                    det=add(mul(A,C,G),mul((F(2),F(2)),D,E,J),neg(mul(A,sq(J))),
                            neg(mul(C,sq(E))),neg(mul(G,sq(D))))
                scale=F(1)
                for l in sub: scale*=c[l]*d[l]
                normalized=tuple(v/scale for v in det)
                ck('closed_form_principal_minor',0<det[0]<=det[1] and scale>0,[a,b,list(sub)])
                saved=replay['principal_minors'][len(minor_records)]
                slo,shi=unpack(saved['interval'])
                ck('all_saved_minor_order_and_enclosure',saved['mode']==[a,b] and saved['layers']==list(sub) and
                   0<slo<=det[0]<=det[1]<=shi and
                   saved['normalized']==pack((slo/scale,shi/scale)),[a,b,list(sub)])
                minor_records.append(dict(mode=[a,b],layers=list(sub),interval=pack(det),normalized=pack(normalized)))
    ck('full_source_exhaustion',dimensions==1+g[5]+g[6]+g[7] and shapes=={3:36,2:13,1:15} and
       len(pivot_records)==149 and len(minor_records)==len(replay['principal_minors'])==306)
    minima={}
    for l,vals in minimum.items():
        v=min(q[0] for q in vals)
        ck('unique_claimed_minimum_and_bracket',[(a,b) for q,a,b in vals if q==v]==[(4,0)] and
           required[l]<=v<required[l]+F(1,10**6) and replay['per_layer_minimum_pivot'][str(l)]==
           dict(mode=[4,0],value=enc(v),bracket=pack((required[l],required[l]+F(1,10**6)))),l)
        minima[str(l)]=dict(mode=[4,0],value=enc(v),bracket=pack((required[l],required[l]+F(1,10**6))))
    for p,h in report['input_sha256'].items(): ck('unchanged_original',sha(ROOT/p)==h,p)
    report.update(stage='verified',replay_checks=replay['checks'],
        replay_sha256={'l119-critical-reverification.json':sha(B/'l119-critical-reverification.json')},
        endpoints=endpoints,relations=270,presentations=1620,repetitions=dict(repeats),null_presentations=dict(nulls),
        signed_action_records=len(replay['signed_actions']),dimension=dimensions,mode_shapes=dict(shapes),
        pivots=pivot_records,principal_minors=minor_records,per_layer_minimum_pivot=minima,
        scope='Unchanged-box L119 excluded-anchor layers 0,5,6,7 only; no full PSD or realization conclusion.')
    save()
    print('L119 audit:',sum(counts.values()),'additional checks; replay:',replay['checks'],'; failures:',report['failures'])
    print('Actual/required relations 270/270, presentations 1620/1620, modes 64/64, pivots 149/149, minors 306/306.')
    print('Layer pivot lower bounds >= 60833905223164487,62140756033549750,62119685418336245 divided by 10^6; required >0.')
    print('All unique minimum modes (4,0), each below its displayed bound plus 10^-6.')
    print('Full certificate:',OUT.relative_to(ROOT))


if __name__=='__main__':
    main()
