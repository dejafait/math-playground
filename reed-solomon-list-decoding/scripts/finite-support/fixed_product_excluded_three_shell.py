"""One immutable excluded-anchor five/six/seven test; exact whole-box intervals.

No nonlinear solve, optimizer, scan, retuning, or box refinement.
"""
import gzip
import hashlib
import json
from collections import Counter
from fractions import Fraction as F
from math import comb
from pathlib import Path

B = Path(__file__).resolve().parent
ROOT = B.parent.parent
OUT = B/'fixed-product-excluded-three-shell.json'


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def enc(x):
    return [x.numerator, x.denominator]


def ei(v):
    return list(map(enc, v))


def choose(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def beta(n, l, m, a, t):
    return sum((-1)**(u-t)*choose(u,t)*choose(n-2*a,u-a)*
               choose(n-a-u,l-u)*choose(n-a-u,m-u)
               for u in range(max(a,t),min(l,m,n-a)+1))


def add(x, y):
    return x[0]+y[0], x[1]+y[1]


def scale(v, w):
    return min(w*v[0],w*v[1]), max(w*v[0],w*v[1])


def mul(x, y):
    corners = [a*b for a in x for b in y]
    return min(corners), max(corners)


def square(x):
    return (F(0) if x[0] <= 0 <= x[1] else min(v*v for v in x),
            max(v*v for v in x))


def main():
    report = dict(stage='in_progress', failures=[], checks=0, code_sha256=sha(Path(__file__)))

    def save():
        OUT.write_text(json.dumps(report,indent=2)+'\n')

    def ck(label, ok):
        report['checks'] += 1
        if not ok:
            report['failures'].append(label)
            report['stage'] = 'failed'
            save()
            raise AssertionError(label)

    names = ['positive-factor-enclosure.json.gz','positive-factor-enclosure-verification.json',
             'delsarte-lp-results.json','l112-l113-critical-audit.json','l114-critical-audit.json',
             'l115-critical-audit.json','fixed-product-five-shell.json',
             'fixed-product-five-shell-verification.json', 'fixed-product-coupled.json',
             'fixed-product-coupled-verification.json', 'l116-critical-audit.json',
             'fixed-product-excluded.json', 'fixed-product-excluded-verification.json',
             'l117-critical-audit.json', 'fixed-product-three-shell-frozen-input.json',
             'fixed-product-three-shell.json','fixed-product-three-shell-verification.json','l118-critical-audit.json']
    paths = [B/n for n in names]
    paths += [ROOT/'lemmas'/n for n in [
        'L021-basic-delsarte-support-lp-optimum.md',
        'L098-exact-cardinality-normalized-control-obstruction.md',
        'L112-enclosed-product-root-passes-distance-five-capacity.md',
        'L113-enclosed-product-root-passes-all-upper-capacities.md',
        'L114-fixed-product-box-passes-Boolean-lower-rows.md',
        'L115-fixed-product-distance-five-shell-psd.md',
        'L116-fixed-product-coupled-five-six-psd.md',
        'L117-fixed-product-excluded-five-six-psd.md',
        'L118-fixed-product-included-five-six-seven-psd.md']]
    report['input_sha256'] = {str(p.relative_to(ROOT)):sha(p) for p in paths}
    save()
    for name,code in [('l112-l113-critical-audit.json','critical_audit_l112_l113.py'),
                      ('l114-critical-audit.json','critical_audit_l114.py'),
                      ('l115-critical-audit.json','critical_audit_l115.py'),
                      ('l116-critical-audit.json','critical_audit_l116.py'),
                      ('l117-critical-audit.json','critical_audit_l117.py'),
                      ('l118-critical-audit.json','critical_audit_l118.py')]:
        audit = json.loads((B/name).read_text())
        ck('audit_status_'+name,audit['stage']=='verified' and not audit['failures'] and
           audit['code_sha256']==sha(B/code))
        for p,h in audit['input_sha256'].items():
            ck('audit_binding_'+name+'_'+p,sha(ROOT/p)==h)
        replays=audit.get('replay_sha256',{})
        if isinstance(replays,str):
            ck('audit_replay_'+name,sha(B/'l115-critical-reverification.json')==replays)
        else:
            for p,h in replays.items():
                ck('audit_replay_'+name+'_'+p,sha(B/p)==h)
    with gzip.open(B/names[0],'rt') as f:
        z=json.load(f)
    rv=json.loads((B/names[1]).read_text())
    margins=[min(l+z['radius'],z['radius']-u) for l,u in z['krawczyk_image']]
    ck('root_binding_and_all_margins',rv['stage']=='verified' and not rv['failures'] and
       rv['input_sha256']==sha(B/names[0]) and z['stage']=='exact_complete' and z['inclusion'] and
       margins==z['inclusion_margins']==rv['inclusion_margins'] and len(margins)==64 and min(margins)>0)
    lp=json.loads((B/'delsarte-lp-results.json').read_text())
    a=[F(v['numerator'],v['denominator']) for v in lp['exact']['primal']]
    N,H=65537**28//2**128+1,comb(1024,68)
    U=F(comb(1024,64),comb(68,64))
    g=[comb(68,i)*comb(956,i) for i in range(69)]
    c=[F(1)]+[F(0)]*4+[(N-1)*a[i-5]/((U-1)*g[i]) for i in range(5,69)]
    ck('canonical_pairs',len(a)==64 and min(a)>0 and sum(a)==U-1 and
       c==list(map(lambda v:F(*v),z['c'])) and z['N']==N and z['H']==H and
       sum(g[i]*c[i] for i in range(69))==N and 0<N<H)
    ck('unchanged_box_contract',z['Q']==10**70 and z['radius']==10**25 and
       len(z['point'])==len(z['scale_powers'])==64 and
       z['box']==[[v-10**25,v+10**25] for v in z['point']])
    box={i:tuple(F(10)**z['scale_powers'][i-5]*F(v,10**70) for v in z['box'][i-5])
         for i in range(5,69)}
    ck('positive_original_box',all(0<l<u for l,u in box.values()))
    lower=json.loads((B/'l114-critical-audit.json').read_text())
    ck('complete_retained_lower_rows',len(lower['rows'])==64)
    for i,row in enumerate(lower['rows'],5):
        ck('retained_lower_row_'+str(i),row['i']==i and
           F(row['pair_numerator'],row['denominator'])==c[i] and
           row['reconstructed_minimum_numerator']==2*row['pair_numerator'] and
           row['distinct_lower_sum_numerator']==row['required']==0)
    frozen=json.loads((B/'fixed-product-three-shell-frozen-input.json').read_text())
    ck('complete_frozen_input',frozen=={k:z[k] for k in frozen})
    anchor=[]
    for l,m in [(0,0)]+[(l,m) for k in (5,6,7) for l,m in [(0,k),(k,0)]]:
        y=c[max(l,m)]
        v=c[l+m]-y
        ck('zero_anchor_'+str((l,m)),v==0)
        anchor.append(dict(layers=[l,m],orbit=[l,m,0,0],h=l+m,
                           pair=enc(c[l+m]),y=enc(y),affine=enc(v),
                           D=g[m] if l==0 else 1))
    pairs=[(l,m) for l in (5,6,7) for m in (5,6,7) if l<=m]
    entries={}; records=[]
    for l,m in pairs:
        table={}
        for t in range(min(l,m)+1):
            for s in range(min(l,m)+1):
                h=l+m-t-s
                y=((c[l],c[l]) if h==0 else (F(0),F(0)) if h<5 else
                       (box[l][0]*box[m][0]*box[h][0],box[l][1]*box[m][1]*box[h][1]))
                value=(c[h]-y[1],c[h]-y[0])
                ck('affine_nonnegative_'+str((l,m,t,s)),value[0]>=0)
                if h==0: ck('Boolean_diagonal_'+str(l),value==(1-c[l],)*2)
                D=choose(l,t)*choose(68-l,m-t)*choose(l,s)*choose(956-l,m-s)
                ck('actual_positive_D_'+str((l,m,t,s)),D>0)
                table[t,s]=value
                records.append(dict(layers=[l,m],intersections=[t,s],h=h,D=D,pair=enc(c[h]),y_interval=ei(y),interval=ei(value)))
        entries[l,m]=table
    mult={n:[choose(n,k)-choose(n,k-1) for k in range(8)] for n in (68,956)}
    ck('complete_dimensions',all(v>0 for n in mult for v in mult[n]) and
       all(sum(mult[68][:l+1])*sum(mult[956][:l+1])==g[l] for l in (5,6,7)))
    old=json.loads((B/'fixed-product-excluded.json').read_text())
    included=json.loads((B/'fixed-product-three-shell.json').read_text())
    modes=[]
    for aa in range(8):
        for bb in range(8):
            layers=[l for l in (5,6,7) if max(aa,bb)<=l]
            D={l:choose(68-2*aa,l-aa)*choose(956-2*bb,l-bb) for l in layers}
            ck('positive_scalings_'+str((aa,bb)),min(D.values())>0)
            blocks={}; corrections={}; pairsums={}; ys={}
            for l in layers:
                for m in layers:
                    if l>m: continue
                    v=(F(0),F(0))
                    for (t,s),interval in entries[l,m].items():
                        w=beta(68,l,m,aa,t)*beta(956,l,m,bb,s)
                        v=add(v,scale(interval,w))
                    pair=sum(beta(68,l,m,aa,t)*beta(956,l,m,bb,s)*c[l+m-t-s]
                             for t,s in entries[l,m])
                    blocks[l,m]=v; corrections[l,m]=F(0); pairsums[l,m]=pair
                    ys[l,m]=(pair-v[1],pair-v[0])
                    corr=c[l]*c[m]*g[l]*g[m] if aa==bb==0 else F(0)
                    raw=tuple(F(*e)+corr for e in included['modes'][8*aa+bb]['blocks'][str(l)+str(m)])
                    ck('recover_included_y_'+str((aa,bb,l,m)),ys[l,m]==raw)
            if max(aa,bb)<=6:
                prev=old['modes'][7*aa+bb]
                ck('every_L117_block_'+str((aa,bb)),all(ei(v)==prev['blocks'][str(l)+str(m)]
                   for (l,m),v in blocks.items() if m<=6))
            current=dict(blocks); stages=[]; pivots=[]
            for k,l in enumerate(layers):
                pivot=current[l,l]
                pivots.append(dict(layer=l,interval=ei(pivot),normalized=ei(scale(pivot,1/(c[l]*D[l])))))
                stages.append({str(i)+str(j):ei(v) for (i,j),v in current.items()})
                if pivot[0]<=0: break
                inverse=(1/pivot[1],1/pivot[0])
                future=layers[k+1:]; following={}
                for i in future:
                    for j in future:
                        if i>j: continue
                        numerator=square(current[l,i]) if i==j else mul(current[l,i],current[l,j])
                        following[i,j]=add(current[i,j],scale(mul(numerator,inverse),-1))
                current=following
            if max(aa,bb)<=6:
                for q in pivots:
                    if q['layer']==5:
                        ck('L117_old_five_pivot_'+str((aa,bb)),q['normalized']==ei(scale(tuple(F(*e) for e in prev['five_normalized']),1/c[5])))
                    if q['layer']==6:
                        ck('L117_old_six_pivot_'+str((aa,bb)),q['normalized']==ei(scale(tuple(F(*e) for e in prev['remainder_normalized']),1/c[6])))
            verdict='positive' if len(pivots)==len(layers) and all(F(*v['interval'][0])>0 for v in pivots) else 'unresolved'
            direction=None; quadratic=None
            if verdict!='positive':
                # Single fixed direction proposal from the old midpoint block.
                # Any rejection uses only the whole-box enclosure below.
                mid={key:sum(v)/2 for key,v in blocks.items()}
                if len(layers)==1: direction=[F(1)]
                elif len(layers)==2 and mid[layers[0],layers[0]]!=0:
                    i=layers[0]; direction=[-mid[i,7]/mid[i,i],F(1)]
                elif len(layers)==3:
                    A0,B0,D0=mid[5,5],mid[5,6],mid[6,6]
                    det=A0*D0-B0*B0
                    if det!=0:
                        C0,E0=mid[5,7],mid[6,7]
                        direction=[(B0*E0-D0*C0)/det,(B0*C0-A0*E0)/det,F(1)]
                if direction is not None:
                    quadratic=(F(0),F(0))
                    for i,l in enumerate(layers):
                        for j,m in enumerate(layers[i:],i):
                            quadratic=add(quadratic,scale(blocks[l,m],direction[i]*direction[j]*(1 if i==j else 2)))
                    quadratic=scale(quadratic,1/(c[7]*D[7]))
                    if quadratic[1]<0: verdict='negative'
            modes.append(dict(a=aa,b=bb,layers=layers,multiplicity=mult[68][aa]*mult[956][bb],
                scaling={str(l):v for l,v in D.items()},
                blocks={str(l)+str(m):ei(v) for (l,m),v in blocks.items()},
                pair_blocks={str(l)+str(m):enc(v) for (l,m),v in pairsums.items()},
                y_blocks={str(l)+str(m):ei(v) for (l,m),v in ys.items()},
                anchor_correction={str(l)+str(m):enc(v) for (l,m),v in corrections.items()},
                elimination_stages=stages,pivots=pivots,
                direction=list(map(enc,direction)) if direction else None,
                quadratic_normalized=ei(quadratic) if quadratic else None,verdict=verdict))
    signs=Counter(m['verdict'] for m in modes)
    verdict='FIXED_PRODUCT_EXCLUDED' if signs['negative'] else 'EXCLUDED_THREE_SHELL_PASSES' if signs['positive']==64 else 'INCONCLUSIVE'
    report.update(stage='complete',N=N,H=H,rho=enc(F(N,H)),c=list(map(enc,c)),
        endpoints=[dict(i=i,interval=ei(box[i])) for i in range(5,69)],
        sizes={str(l):g[l] for l in (5,6,7)},multiplicities={str(n):v for n,v in mult.items()},
        anchor_cases=anchor,entries=records,modes=modes,summary=dict(counts=dict(signs),verdict=verdict,
            negative_modes=[[m['a'],m['b']] for m in modes if m['verdict']=='negative'],
            unresolved_modes=[[m['a'],m['b']] for m in modes if m['verdict']=='unresolved']))
    save()
    worst=min(((F(*p['normalized'][0]),m['a'],m['b'],p['layer']) for m in modes for p in m['pivots']))
    q=worst[0]*10**6//1
    print('Actual/required relations:',len(records),'/270; modes:',len(modes),'/64; whole-box signs:',dict(signs))
    print('Minimum normalized pivot lower at',worst[1:],'in [',q,',',q+1,')/10^6; required >0')
    print('Zero anchor cases: 7/7; no included-anchor subtraction')
    print('Verdict:',verdict,'; checks:',report['checks'],'; failures:',report['failures'])
    print('Full certificate:',OUT.relative_to(ROOT))


if __name__=='__main__':
    main()
