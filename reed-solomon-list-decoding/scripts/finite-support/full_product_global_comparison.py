"""One global Johnson comparison at the immutable L112 box; no root solve."""
import gzip
import hashlib
import json
from fractions import Fraction as F
from math import comb
from pathlib import Path

B = Path(__file__).resolve().parent
ROOT = B.parent.parent
OUT = B/'full-product-global-comparison.json'


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def enc(q):
    return [q.numerator, q.denominator]


def choose(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def main():
    report = dict(stage='in_progress', failures=[], checks=0,
                  code_sha256=sha(Path(__file__)))

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
    N, H = 65537**28//2**128+1, comb(1024,68)
    U = F(comb(1024,64),comb(68,64))
    g = [comb(68,i)*comb(956,i) for i in range(69)]
    c = [F(1)]+[F(0)]*4+[(N-1)*av[i-5]/((U-1)*g[i]) for i in range(5,69)]
    ck('canonical_pairs', len(av)==64 and min(av)>0 and sum(av)==U-1 and
       list(map(enc,c))==z['c'] and z['N']==N and z['H']==H and
       sum(g[i]*c[i] for i in range(69))==N and N>1)
    ck('unchanged_box', z['Q']==10**70 and z['radius']==10**25 and
       len(z['point'])==len(z['scale_powers'])==64 and
       z['box']==[[p-10**25,p+10**25] for p in z['point']])
    box = {i:tuple(F(10)**z['scale_powers'][i-5]*F(v,z['Q']) for v in z['box'][i-5])
           for i in range(5,69)}
    ck('positive_original_box', all(0<l<u for l,u in box.values()))
    E = [[sum((-1)**h*choose(j,h)*choose(68-j,i-h)*choose(956-j,i-h)
              for h in range(i+1)) for i in range(69)] for j in range(69)]
    mult = [choose(1024,j)-choose(1024,j-1) for j in range(69)]
    ck('complete_spectrum', min(mult)>0 and sum(mult)==H and E[0]==g and
       all(row[0]==1 for row in E) and sum(g)==H)
    for i in range(69):
        ck('coefficient_trace_'+str(i), sum(mult[j]*E[j][i] for j in range(69))==(H if i==0 else 0))
    modes = []
    for j in range(69):
        lo = sum(E[j][i]*box[i][0 if E[j][i]>=0 else 1] for i in range(5,69))
        hi = sum(E[j][i]*box[i][1 if E[j][i]>=0 else 0] for i in range(5,69))
        ck('mode_order_'+str(j),lo<=hi)
        modes.append(dict(j=j, multiplicity=mult[j], interval=list(map(enc,(lo,hi)))))
    corrections = [dict(i=i, interval=list(map(enc,(c[i]/box[i][1]**2,c[i]/box[i][0]**2))))
                   for i in range(5,69)]
    ml = min(F(*m['interval'][0]) for m in modes)
    mu = min(F(*m['interval'][1]) for m in modes)
    dl = min(F(*d['interval'][0]) for d in corrections)
    du = min(F(*d['interval'][1]) for d in corrections)
    lower,upper = ml+dl,mu+du
    verdict = 'SUFFICIENT_COMPARISON_PASSES' if lower>=0 else 'SUFFICIENT_COMPARISON_PARKED' if upper<0 else 'INCONCLUSIVE'
    # A fixed positive rational reference aids printing without altering the test.
    ref = c[5]/box[5][1]**2
    norm = lower/ref,upper/ref
    grid = 10**6
    bracket = [norm[0].numerator*grid//norm[0].denominator,
               -((-norm[1].numerator*grid)//norm[1].denominator)]
    report.update(stage='complete', N=N,H=H,rho=enc(F(N,H)),c=list(map(enc,c)),
                  frozen={p:z[p] for p in ['N','H','Q','radius','point','scale_powers','box']},
                  endpoints=[dict(i=i,interval=list(map(enc,box[i]))) for i in range(5,69)],
                  eigenmatrix=E,multiplicities=mult,modes=modes,corrections=corrections,
                  comparison=dict(interval=list(map(enc,(lower,upper))),
                                  kernel_min_interval=list(map(enc,(ml,mu))),
                                  correction_min_interval=list(map(enc,(dl,du))),
                                  lower_mode=[m['j'] for m in modes if F(*m['interval'][0])==ml],
                                  upper_mode=[m['j'] for m in modes if F(*m['interval'][1])==mu],
                                  lower_correction=[d['i'] for d in corrections if F(*d['interval'][0])==dl],
                                  upper_correction=[d['i'] for d in corrections if F(*d['interval'][1])==du],
                                  reference=enc(ref),normalized_interval=list(map(enc,norm)),
                                  normalized_grid=grid, normalized_bracket=bracket,
                                  required='lower endpoint >= 0',verdict=verdict))
    save()
    print('Actual/required: 69/69 global modes, 64/64 diagonal corrections; required comparison >=0')
    print('Comparison/reference in [%s,%s]/%s; reference=c5/u5^2>0' % (*bracket,grid))
    print('Verdict:',verdict,'; extremal modes:',report['comparison']['lower_mode'],report['comparison']['upper_mode'])
    print('Checks:',report['checks'],'; failures:',len(report['failures']),'; certificate:',OUT)


if __name__=='__main__':
    main()
