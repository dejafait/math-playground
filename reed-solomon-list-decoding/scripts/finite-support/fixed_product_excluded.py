"""One immutable excluded-anchor five/six test; exact whole-box intervals.

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
OUT = B/'fixed-product-excluded.json'


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
             'fixed-product-coupled-verification.json', 'l116-critical-audit.json']
    paths = [B/n for n in names]
    paths += [ROOT/'lemmas'/n for n in [
        'L021-basic-delsarte-support-lp-optimum.md',
        'L098-exact-cardinality-normalized-control-obstruction.md',
        'L112-enclosed-product-root-passes-distance-five-capacity.md',
        'L113-enclosed-product-root-passes-all-upper-capacities.md',
        'L114-fixed-product-box-passes-Boolean-lower-rows.md',
        'L115-fixed-product-distance-five-shell-psd.md',
        'L116-fixed-product-coupled-five-six-psd.md']]
    report['input_sha256'] = {str(p.relative_to(ROOT)):sha(p) for p in paths}
    save()
    for name,code in [('l112-l113-critical-audit.json','critical_audit_l112_l113.py'),
                      ('l114-critical-audit.json','critical_audit_l114.py'),
                      ('l115-critical-audit.json','critical_audit_l115.py'),
                      ('l116-critical-audit.json','critical_audit_l116.py')]:
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
    # Check the entire anchor before deleting its zero coordinate.
    anchor=[]
    for l,m in [(0,0),(0,5),(5,0),(0,6),(6,0)]:
        y=c[max(l,m)]
        v=c[l+m]-y
        ck('zero_anchor_'+str((l,m)),v==0)
        anchor.append(dict(layers=[l,m],orbit=[l,m,0,0],h=l+m,
                           pair=enc(c[l+m]),y=enc(y),affine=enc(v),
                           D=choose(68,m)*choose(956,m) if l==0 else 1))
    lower=json.loads((B/'l114-critical-audit.json').read_text())
    ck('complete_retained_lower_rows',len(lower['rows'])==64)
    for i,row in enumerate(lower['rows'],5):
        ck('retained_lower_row_'+str(i),row['i']==i and
           F(row['pair_numerator'],row['denominator'])==c[i] and
           row['reconstructed_minimum_numerator']==2*row['pair_numerator'] and
           row['distinct_lower_sum_numerator']==row['required']==0)
    entries={}
    records=[]
    for l,m in [(5,5),(5,6),(6,6)]:
        table={}
        for t in range(min(l,m)+1):
            for s in range(min(l,m)+1):
                h=l+m-t-s
                y=((c[l],c[l]) if h==0 else (F(0),F(0)) if h<5 else
                       (box[l][0]*box[m][0]*box[h][0],box[l][1]*box[m][1]*box[h][1]))
                value=(c[h]-y[1],c[h]-y[0])
                ck('affine_nonnegative_'+str((l,m,t,s)),value[0]>=0)
                if h==0:
                    ck('Boolean_diagonal_'+str(l),value==(1-c[l],)*2)
                D=choose(l,t)*choose(68-l,m-t)*choose(l,s)*choose(956-l,m-s)
                ck('actual_positive_D_'+str((l,m,t,s)),D>0)
                table[t,s]=value
                records.append(dict(layers=[l,m],intersections=[t,s],h=h,D=D,
                                    pair=enc(c[h]),y_interval=ei(y),interval=ei(value)))
        entries[l,m]=table
    mult={n:[choose(n,k)-choose(n,k-1) for k in range(7)] for n in (68,956)}
    ck('complete_dimensions',all(v>0 for n in mult for v in mult[n]) and
       sum(mult[68][:6])*sum(mult[956][:6])==g[5] and
       sum(mult[68])*sum(mult[956])==g[6])
    included=json.loads((B/'fixed-product-coupled.json').read_text())
    modes=[]
    for aa in range(7):
        for bb in range(7):
            layers=[5,6] if aa<=5 and bb<=5 else [6]
            D={l:choose(68-2*aa,l-aa)*choose(956-2*bb,l-bb) for l in layers}
            ck('positive_scalings_'+str((aa,bb)),min(D.values())>0)
            blocks={}
            pair_blocks={}
            y_blocks={}
            for l in layers:
                for m in layers:
                    if l>m:
                        continue
                    v=(F(0),F(0))
                    for (t,s),interval in entries[l,m].items():
                        w=beta(68,l,m,aa,t)*beta(956,l,m,bb,s)
                        v=add(v,scale(interval,w))
                    pair=sum(beta(68,l,m,aa,t)*beta(956,l,m,bb,s)*c[l+m-t-s]
                             for t,s in entries[l,m])
                    blocks[l,m]=v
                    pair_blocks[l,m]=pair
                    y_blocks[l,m]=(pair-v[1],pair-v[0])
                    previous=tuple(F(*e) for e in included['modes'][7*aa+bb]['blocks'][str(l)+str(m)])
                    corr=c[l]*c[m]*g[l]*g[m] if aa==bb==0 else F(0)
                    ck('recover_included_y_'+str((aa,bb,l,m)),
                       y_blocks[l,m]==add(previous,(corr,corr)))
            six=scale(blocks[6,6],F(1,D[6]))
            remaining=six
            oldnorm=cross=None
            if 5 in layers:
                oldnorm=scale(blocks[5,5],F(1,D[5]))
                cross=blocks[5,6]
                ck('positive_old_pivot_'+str((aa,bb)),oldnorm[0]>0)
                cost=mul(square(cross),(1/blocks[5,5][1],1/blocks[5,5][0]))
                remaining=scale(add(blocks[6,6],scale(cost,-1)),F(1,D[6]))
            verdict='positive' if remaining[0]>0 else 'unresolved'
            # A fixed rational vector chosen once from the block midpoint.
            # Its sign is certified throughout the box, never at the midpoint alone.
            direction=[F(1)]
            quadratic=six
            if 5 in layers:
                q=-sum(cross)/sum(blocks[5,5])
                direction=[q,F(1)]
                quadratic=scale(add(add(scale(blocks[5,5],q*q),scale(cross,2*q)),blocks[6,6]),
                                F(1,D[6]))
            if quadratic[1]<0:
                verdict='negative'
            modes.append(dict(a=aa,b=bb,layers=layers,multiplicity=mult[68][aa]*mult[956][bb],
                              scaling={str(k):v for k,v in D.items()},
                              blocks={str(l)+str(m):ei(v) for (l,m),v in blocks.items()},
                              pair_blocks={str(l)+str(m):enc(v) for (l,m),v in pair_blocks.items()},
                              y_blocks={str(l)+str(m):ei(v) for (l,m),v in y_blocks.items()},
                              five_normalized=ei(oldnorm) if oldnorm else None,
                              six_normalized=ei(six),remainder_normalized=ei(remaining),
                              direction=list(map(enc,direction)),quadratic_normalized=ei(quadratic),verdict=verdict))
    counts=Counter(m['verdict'] for m in modes)
    verdict='FIXED_PRODUCT_EXCLUDED' if counts['negative'] else 'EXCLUDED_ANCHOR_PASSES' if counts['positive']==49 else 'INCONCLUSIVE'
    report.update(stage='complete',N=N,H=H,rho=enc(F(N,H)),c=list(map(enc,c)),
                  endpoints=[dict(i=i,interval=ei(box[i])) for i in range(5,69)],
                  sizes={str(i):g[i] for i in (5,6)},multiplicities={str(n):v for n,v in mult.items()},
                  anchor_cases=anchor,entries=records,modes=modes,summary=dict(counts=dict(counts),verdict=verdict,
                      negative_modes=[[m['a'],m['b']] for m in modes if m['verdict']=='negative'],
                      unresolved_modes=[[m['a'],m['b']] for m in modes if m['verdict']=='unresolved']))
    save()
    print('Actual/required relations: 121/121; modes: 49/49; block sizes: 36 two-by-two, 13 one-by-one')
    print('Zero anchor cases: 5/5; no included-anchor subtraction')
    print('Whole-box block signs:',dict(counts),'; required PSD in every block; verdict:',verdict)
    worst=min(modes,key=lambda m:F(*m['remainder_normalized'][0]))
    v=F(*worst['remainder_normalized'][0]); k=v*10**6//1
    print('Minimum normalized remainder lower at',(worst['a'],worst['b']),
          'in ['+str(k)+'/10^6,'+str(k+1)+'/10^6); required >=0')
    print('Checks:',report['checks'],'; failures:',report['failures'],'; full certificate:',OUT.relative_to(ROOT))


if __name__=='__main__':
    main()
