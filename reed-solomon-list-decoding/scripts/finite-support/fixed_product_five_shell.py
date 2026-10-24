"""One unchanged-box shell test; exact endpoints, no solves or refinement."""
import gzip
import hashlib
import json
from collections import Counter
from fractions import Fraction as F
from math import comb
from pathlib import Path

B = Path(__file__).resolve().parent
ROOT = B.parent.parent
OUT = B / 'fixed-product-five-shell.json'


def enc(x):
    return [x.numerator, x.denominator]


def choose(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def factor(n):
    return [[sum((-1)**h*choose(a,h)*choose(5-a,r-h)*choose(n-5-a,r-h)
                 for h in range(r+1)) for r in range(6)] for a in range(6)]


def main():
    report = dict(stage='in_progress', failures=[], checks=0,
                  code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())

    def save():
        OUT.write_text(json.dumps(report, indent=2)+'\n')

    def ck(label, condition):
        report['checks'] += 1
        if not condition:
            report['failures'].append(label)
            report['stage'] = 'failed'
            save()
            raise AssertionError(label)

    names = ['positive-factor-enclosure.json.gz', 'positive-factor-enclosure-verification.json',
             'delsarte-lp-results.json', 'l112-l113-critical-audit.json', 'l114-critical-audit.json']
    paths = [B/name for name in names]
    paths += [ROOT/'lemmas'/name for name in [
        'L021-basic-delsarte-support-lp-optimum.md',
        'L098-exact-cardinality-normalized-control-obstruction.md',
        'L112-enclosed-product-root-passes-distance-five-capacity.md',
        'L113-enclosed-product-root-passes-all-upper-capacities.md',
        'L114-fixed-product-box-passes-Boolean-lower-rows.md']]
    report['input_sha256'] = {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
                              for p in paths}
    save()
    for name in ['l112-l113-critical-audit.json', 'l114-critical-audit.json']:
        audit = json.loads((B/name).read_text())
        ck('retained_audit_'+name, audit['stage'] == 'verified' and audit['failures'] == [])
        for path, digest in audit['input_sha256'].items():
            ck('audit_binding_'+path, hashlib.sha256((ROOT/path).read_bytes()).hexdigest() == digest)
    with gzip.open(B/names[0], 'rt') as f:
        z = json.load(f)
    rv = json.loads((B/names[1]).read_text())
    ck('root_binding', rv['stage'] == 'verified' and not rv['failures'] and
       rv['input_sha256'] == report['input_sha256']['scripts/finite-support/'+names[0]])
    ck('strict_root_inclusion', z['stage'] == 'exact_complete' and z['inclusion'] and
       rv['inclusion_margins'] == z['inclusion_margins'] and len(z['inclusion_margins']) == 64
       and min(z['inclusion_margins']) > 0)
    lp = json.loads((B/'delsarte-lp-results.json').read_text())
    a = [F(v['numerator'],v['denominator']) for v in lp['exact']['primal']]
    N, H = 65537**28//2**128+1, comb(1024,68)
    U = F(comb(1024,64),comb(68,64))
    g = [comb(68,i)*comb(956,i) for i in range(69)]
    c = [F(1)]+[F(0)]*4+[(N-1)*a[i-5]/((U-1)*g[i]) for i in range(5,69)]
    ck('canonical_pairs', len(a) == 64 and min(a)>0 and sum(a)==U-1 and
       c == [F(*v) for v in z['c']] and N==z['N'] and H==z['H'])
    ck('normalization', sum(g[i]*c[i] for i in range(69)) == N and 0<N<H)
    ck('box_contract', z['Q']==10**70 and z['radius']==10**25 and
       len(z['point'])==len(z['scale_powers'])==64 and
       z['box']==[[p-z['radius'],p+z['radius']] for p in z['point']])
    intervals = {i: (F(10)**z['scale_powers'][i-5]*F(z['box'][i-5][0],z['Q']),
                      F(10)**z['scale_powers'][i-5]*F(z['box'][i-5][1],z['Q']))
                 for i in range(5,69)}
    ck('positive_box', all(0<l<u for l,u in intervals.values()))
    entries = []
    for r in range(6):
        row = []
        for q in range(6):
            h = r+q
            value = ((c[5],c[5]) if h==0 else (F(0),F(0)) if h<5 else
                     tuple(intervals[5][k]**2*intervals[h][k] for k in (0,1)))
            row.append(value)
        entries.append(row)
    factors = {n:factor(n) for n in (68,956)}
    mult = {n:[choose(n,k)-choose(n,k-1) for k in range(6)] for n in (68,956)}
    S = comb(68,5)*comb(956,5)
    modes = []
    for a0 in range(6):
        for b0 in range(6):
            lo=hi=F(0)
            coefficients = [0]*11
            for r in range(6):
                for q in range(6):
                    w = factors[68][a0][r]*factors[956][b0][q]
                    l,u = entries[r][q]
                    lo += w*(l if w>=0 else u)
                    hi += w*(u if w>=0 else l)
                    if r+q>=5:
                        coefficients[r+q] += w
            correction = S*c[5]**2 if a0==b0==0 else F(0)
            sl,su = lo-correction,hi-correction
            verdict = ('negative' if su<0 else 'positive' if sl>0 else
                       'zero' if sl==su==0 else 'unresolved')
            modes.append(dict(a=a0,b=b0,multiplicity=mult[68][a0]*mult[956][b0],
                              product_coefficients=coefficients[5:],shell=[enc(lo),enc(hi)],
                              correction=enc(correction),schur=[enc(sl),enc(su)],
                              schur_over_c5=[enc(sl/c[5]),enc(su/c[5])],verdict=verdict))
    ck('complete_dimension', len(modes)==36 and sum(m['multiplicity'] for m in modes)==S)
    for h in range(5,11):
        ck('trace_coefficient_'+str(h), sum(m['multiplicity']*m['product_coefficients'][h-5]
                                           for m in modes)==0)
    counts = Counter(m['verdict'] for m in modes)
    negative = [[m['a'],m['b']] for m in modes if m['verdict']=='negative']
    verdict = ('FIXED_PRODUCT_EXCLUDED' if negative else 'INCONCLUSIVE' if counts['unresolved']
               else 'SHELL_PASSES')
    report.update(stage='complete', N=N,H=H,c=[enc(x) for x in c],rho=enc(F(N,H)),size=S,
                  endpoints=[dict(i=i,interval=[enc(l),enc(u)]) for i,(l,u) in intervals.items()],
                  entries=[[[enc(l),enc(u)] for l,u in row] for row in entries],
                  factors=[dict(n=n,eigenmatrix=factors[n],multiplicities=mult[n]) for n in (68,956)],
                  modes=modes,summary=dict(counts=dict(counts),negative_modes=negative,verdict=verdict,
                                          required='all 36 Schur coordinates nonnegative'))
    save()
    print('Actual/required modes: 36/36; dimension:',S)
    print('Whole-box signs:',dict(counts),'; PSD requires all >= 0; verdict:',verdict)
    print('Checks:',report['checks'],'; failures:',len(report['failures']),'; certificate:',OUT)


if __name__=='__main__':
    main()
