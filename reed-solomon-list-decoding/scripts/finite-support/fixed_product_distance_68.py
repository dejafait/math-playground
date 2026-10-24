"""Complete endpoint shell at the original box; no solve or refinement."""
import gzip
import hashlib
import json
from collections import Counter
from fractions import Fraction as F
from math import comb
from pathlib import Path

B = Path(__file__).resolve().parent
ROOT = B.parent.parent
OUT = B/'fixed-product-distance-68.json'


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def enc(q):
    return [q.numerator, q.denominator]


def choose(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def main():
    report = dict(stage='in_progress', failures=[], checks=0, code_sha256=sha(Path(__file__)))

    def save():
        OUT.write_text(json.dumps(report, indent=2)+'\n')

    def ck(label, ok):
        report['checks'] += 1
        if not ok:
            report['failures'].append(label)
            report['stage'] = 'failed'
            save()
            raise AssertionError(label)

    names = ['positive-factor-enclosure.json.gz', 'positive-factor-enclosure-verification.json',
             'delsarte-lp-results.json', 'l112-l113-critical-audit.json', 'l114-critical-audit.json']
    paths = [B/n for n in names]
    paths += [ROOT/'lemmas'/n for n in [
        'L021-basic-delsarte-support-lp-optimum.md',
        'L098-exact-cardinality-normalized-control-obstruction.md',
        'L112-enclosed-product-root-passes-distance-five-capacity.md',
        'L113-enclosed-product-root-passes-all-upper-capacities.md',
        'L114-fixed-product-box-passes-Boolean-lower-rows.md']]
    report['input_sha256'] = {str(p.relative_to(ROOT)):sha(p) for p in paths}
    save()
    for name, code in [('l112-l113-critical-audit.json', 'critical_audit_l112_l113.py'),
                       ('l114-critical-audit.json', 'critical_audit_l114.py')]:
        audit = json.loads((B/name).read_text())
        ck('retained_audit_'+name, audit['stage']=='verified' and not audit['failures']
           and audit['code_sha256']==sha(B/code))
        for p, h in audit['input_sha256'].items():
            ck('audit_binding_'+p, sha(ROOT/p)==h)
    with gzip.open(B/names[0], 'rt') as f:
        z = json.load(f)
    rv = json.loads((B/names[1]).read_text())
    margins = [min(l+z['radius'], z['radius']-u) for l,u in z['krawczyk_image']]
    ck('root_binding_all_margins', rv['stage']=='verified' and not rv['failures'] and
       rv['input_sha256']==sha(B/names[0]) and z['stage']=='exact_complete' and z['inclusion'] and
       len(margins)==64 and min(margins)>0 and margins==z['inclusion_margins']==rv['inclusion_margins'])
    lp = json.loads((B/'delsarte-lp-results.json').read_text())
    av = [F(v['numerator'],v['denominator']) for v in lp['exact']['primal']]
    N, H, S = 65537**28//2**128+1, comb(1024,68), comb(956,68)
    U = F(comb(1024,64),comb(68,64))
    g = [comb(68,i)*comb(956,i) for i in range(69)]
    c = [F(1)]+[F(0)]*4+[(N-1)*av[i-5]/((U-1)*g[i]) for i in range(5,69)]
    ck('canonical_pairs', len(av)==64 and min(av)>0 and sum(av)==U-1 and
       list(map(enc,c))==z['c'] and z['N']==N and z['H']==H and sum(g[i]*c[i] for i in range(69))==N)
    ck('unchanged_box', z['Q']==10**70 and z['radius']==10**25 and
       len(z['point'])==len(z['scale_powers'])==64 and
       z['box']==[[p-10**25,p+10**25] for p in z['point']])
    box = {i:tuple(F(10)**z['scale_powers'][i-5]*F(v,z['Q']) for v in z['box'][i-5])
           for i in range(5,69)}
    ck('positive_original_box', all(0<l<u for l,u in box.values()))
    ck('positive_normalization', 0<N<H and S==g[68] and 0<c[68]<1)
    # The head has the sole full 68-set. Tail relation r has s=68-r.
    entries = [(c[68],c[68]) if r==0 else (F(0),F(0)) if r<5 else
               tuple(box[68][k]**2*box[r][k] for k in (0,1)) for r in range(69)]
    E = [[sum((-1)**h*choose(k,h)*choose(68-k,r-h)*choose(888-k,r-h)
              for h in range(r+1)) for r in range(69)] for k in range(69)]
    mult = [choose(956,k)-choose(956,k-1) for k in range(69)]
    valencies = [choose(68,r)*choose(888,r) for r in range(69)]
    ck('complete_spectrum', min(mult)>0 and sum(mult)==S and E[0]==valencies and
       all(row[0]==1 for row in E) and sum(valencies)==S)
    modes = []
    for k in range(69):
        lo = sum(w*(v[0] if w>=0 else v[1]) for w,v in zip(E[k],entries))
        hi = sum(w*(v[1] if w>=0 else v[0]) for w,v in zip(E[k],entries))
        correction = S*c[68]**2 if k==0 else F(0)
        sl, su = lo-correction, hi-correction
        sign = 'negative' if su<0 else 'positive' if sl>0 else 'zero' if sl==su==0 else 'unresolved'
        modes.append(dict(k=k, multiplicity=mult[k], shell=list(map(enc,(lo,hi))),
                          correction=enc(correction), schur=list(map(enc,(sl,su))),
                          schur_over_c68=[enc(sl/c[68]),enc(su/c[68])], verdict=sign))
    for r in range(69):
        ck('all_coefficient_traces_'+str(r), sum(mult[k]*E[k][r] for k in range(69))==(S if r==0 else 0))
    signs = Counter(m['verdict'] for m in modes)
    negatives = [m['k'] for m in modes if m['verdict']=='negative']
    verdict = 'FIXED_PRODUCT_EXCLUDED' if negatives else 'INCONCLUSIVE' if signs['unresolved'] else 'SHELL_PASSES'
    direction = None
    if negatives:
        # Fixed rational column of the k-th Johnson idempotent, scaled to
        # value 1 at its chosen base subset. First negative index, no search.
        k = negatives[0]
        radial = [F(E[k][r],valencies[r]) for r in range(69)]
        mass = sum(valencies[r]*radial[r] for r in range(69))
        norm = sum(valencies[r]*radial[r]**2 for r in range(69))
        ck('fixed_rational_direction_norm', radial[0]==1 and norm==F(S,mult[k])>0 and mass==(S if k==0 else 0))
        quadratic = [norm*F(*q) for q in modes[k]['schur']]
        ck('strict_whole_box_negative_direction', quadratic[1]<0)
        direction = dict(k=k,radial_values=list(map(enc,radial)),shell_sum=enc(mass),
                         shell_norm_squared=enc(norm),anchor_coordinate=enc(-c[68]*mass),
                         normalized_quadratic=list(map(enc,quadratic)),
                         raw_quadratic=[enc(F(N,H)*q) for q in quadratic])
    report.update(stage='complete', N=N,H=H,rho=enc(F(N,H)),c=list(map(enc,c)),size=S,
                  frozen={p:z[p] for p in ['N','H','Q','radius','point','scale_powers','box']},
                  endpoints=[dict(i=i,interval=list(map(enc,box[i]))) for i in range(5,69)],
                  entries=[dict(r=r,orbit=[68,68,68,68-r],h=r,D=valencies[r],interval=list(map(enc,v)))
                           for r,v in enumerate(entries)],
                  eigenmatrix=E,multiplicities=mult,valencies=valencies,modes=modes,direction=direction,
                  summary=dict(counts=dict(signs),negative_modes=negatives,verdict=verdict,
                               required='all 69 Schur coordinates nonnegative'))
    save()
    print('Actual/required relations and modes: 69/69; shell dimension:',S)
    print('Whole-box signs:',dict(signs),'; required all >=0; verdict:',verdict)
    print('Negative mode indices:',negatives)
    print('Checks:',report['checks'],'; failures:',len(report['failures']),'; certificate:',OUT)


if __name__=='__main__':
    main()
