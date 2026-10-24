"""Independent integer-polynomial reconstruction and exact bound verification."""
import gzip
import hashlib
import json
from collections import Counter
from fractions import Fraction as F
from functools import lru_cache
from math import factorial
from pathlib import Path

B = Path(__file__).resolve().parent
ROOT = B.parent.parent
SOURCE = B/'full-product-global-comparison.json'
OUT = B/'full-product-global-comparison-verification.json'


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


@lru_cache(None)
def choose(n,k):
    return factorial(n)//factorial(k)//factorial(n-k) if 0<=k<=n else 0


def enc(q):
    return [q.numerator,q.denominator]


def main():
    s = json.loads(SOURCE.read_text())
    counts = Counter()
    report = dict(stage='in_progress',failures=[],source_sha256=sha(SOURCE),
                  code_sha256=sha(Path(__file__)))

    def save():
        report.update(checks=sum(counts.values()),checks_by_kind=dict(counts))
        OUT.write_text(json.dumps(report,indent=2)+'\n')

    def ck(kind,ok,detail=None):
        counts[kind] += 1
        if not ok:
            report['stage']='failed'
            report['failures'].append(dict(kind=kind,detail=detail))
            save()
            raise AssertionError((kind,detail))

    ck('constructor',s['stage']=='complete' and not s['failures'] and
       s['code_sha256']==sha(B/'full_product_global_comparison.py'))
    for p,h in s['input_sha256'].items():
        ck('input_binding',sha(ROOT/p)==h,p)
    for name,code in [('l112-l113-critical-audit.json','critical_audit_l112_l113.py'),
                      ('l114-critical-audit.json','critical_audit_l114.py')]:
        a = json.loads((B/name).read_text())
        ck('audit_status',a['stage']=='verified' and not a['failures'] and a['code_sha256']==sha(B/code))
        for p,h in a['input_sha256'].items():
            ck('audit_input_binding',sha(ROOT/p)==h,p)
    with gzip.open(B/'positive-factor-enclosure.json.gz','rt') as f:
        z = json.load(f)
    rv = json.loads((B/'positive-factor-enclosure-verification.json').read_text())
    ck('root_status',z['stage']=='exact_complete' and z['inclusion'] and rv['stage']=='verified' and
       not rv['failures'] and rv['input_sha256']==sha(B/'positive-factor-enclosure.json.gz'))
    ck('frozen_contract',s['frozen']=={k:z[k] for k in s['frozen']} and
       set(s['frozen'])=={'N','H','Q','radius','point','scale_powers','box'} and
       z['Q']==10**70 and z['radius']==10**25 and
       len(z['point'])==len(z['scale_powers'])==len(z['box'])==len(z['krawczyk_image'])==64)
    for j,(q,(lo,hi),(kl,ku)) in enumerate(zip(z['point'],z['box'],z['krawczyk_image'])):
        ck('each_original_box_margin',[lo,hi]==[q-10**25,q+10**25] and lo>0 and
           min(kl+10**25,10**25-ku)==z['inclusion_margins'][j]==rv['inclusion_margins'][j]>0,j)
    lp = json.loads((B/'delsarte-lp-results.json').read_text())
    av = [F(v['numerator'],v['denominator']) for v in lp['exact']['primal']]
    N,H = 65537**28//2**128+1, choose(1024,68)
    U = F(choose(1024,64),choose(68,64))
    g = [choose(68,i)*choose(956,i) for i in range(69)]
    c = [F(1)]+[F(0)]*4+[(N-1)*av[i-5]/((U-1)*g[i]) for i in range(5,69)]
    ck('canonical_data',len(av)==64 and min(av)>0 and sum(av)==U-1 and
       s['N']==z['N']==N and s['H']==z['H']==H and s['rho']==enc(F(N,H)) and
       list(map(enc,c))==z['c']==s['c'] and sum(g[i]*c[i] for i in range(69))==N>1)
    box = {}
    ck('endpoint_length',len(s['endpoints'])==64)
    for i in range(5,69):
        k = i-5
        power = z['scale_powers'][k]
        scale = F(10**power) if power>=0 else F(1,10**(-power))
        box[i] = [scale*F(z['point'][k]+e*10**25,10**70) for e in (-1,1)]
        ck('each_endpoint',s['endpoints'][k]==dict(i=i,interval=list(map(enc,box[i]))) and
           0<box[i][0]<box[i][1],i)
    # Polynomial (1-z)^j * sum_r binom(68-j,r)binom(956-j,r) z^r.
    # Multiplication, rather than the constructor's per-coefficient formula.
    matrix = []
    ck('matrix_shapes',len(s['eigenmatrix'])==len(s['modes'])==len(s['multiplicities'])==69)
    for j in range(69):
        poly = [choose(68-j,r)*choose(956-j,r) for r in range(69-j)]
        for _ in range(j):
            prev = poly
            poly = [0]*(len(prev)+1)
            for k,v in enumerate(prev):
                poly[k] += v
                poly[k+1] -= v
        ck('polynomial_length',len(poly)==69,j)
        for i,value in enumerate(poly):
            ck('every_integer_coefficient',value==s['eigenmatrix'][j][i],[j,i])
        matrix.append(poly)
    mult = [choose(1024,j)-choose(1024,j-1) for j in range(69)]
    ck('all_multiplicities',s['multiplicities']==mult and min(mult)>0 and sum(mult)==H)
    ck('constant_mode_valencies',matrix[0]==g and sum(g)==H)
    for i in range(69):
        ck('all_coefficient_traces',sum(mult[j]*matrix[j][i] for j in range(69))==(H if i==0 else 0),i)
    bounds = []
    for j in range(69):
        poslo = sum(w*box[i][0] for i,w in enumerate(matrix[j]) if i>=5 and w>0)
        neghi = sum(w*box[i][1] for i,w in enumerate(matrix[j]) if i>=5 and w<0)
        poshi = sum(w*box[i][1] for i,w in enumerate(matrix[j]) if i>=5 and w>0)
        neglo = sum(w*box[i][0] for i,w in enumerate(matrix[j]) if i>=5 and w<0)
        pair = [poslo+neghi,poshi+neglo]
        ck('each_signed_sum',pair[0]<=pair[1] and s['modes'][j]==dict(j=j,multiplicity=mult[j],interval=list(map(enc,pair))),j)
        bounds.append(pair)
    deltas = []
    ck('correction_length',len(s['corrections'])==64)
    for i in range(5,69):
        pair = [c[i]/(box[i][1]*box[i][1]),c[i]/(box[i][0]*box[i][0])]
        ck('each_correction',0<pair[0]<pair[1] and s['corrections'][i-5]==dict(i=i,interval=list(map(enc,pair))),i)
        deltas.append(pair)
    mn = [min(b[k] for b in bounds) for k in (0,1)]
    dn = [min(d[k] for d in deltas) for k in (0,1)]
    result = [mn[k]+dn[k] for k in (0,1)]
    t = s['comparison']
    ck('both_minima_and_sum',t['kernel_min_interval']==list(map(enc,mn)) and
       t['correction_min_interval']==list(map(enc,dn)) and t['interval']==list(map(enc,result)))
    for k,key in enumerate(['lower','upper']):
        ck('minimizers',t[key+'_mode']==[j for j in range(69) if bounds[j][k]==mn[k]] and
           t[key+'_correction']==[i for i in range(5,69) if deltas[i-5][k]==dn[k]])
    reference = c[5]/box[5][1]**2
    normalized = [r/reference for r in result]
    grid = 10**6
    bracket = [normalized[0].numerator*grid//normalized[0].denominator,
               -((-normalized[1].numerator*grid)//normalized[1].denominator)]
    verdict = 'SUFFICIENT_COMPARISON_PASSES' if result[0]>=0 else 'SUFFICIENT_COMPARISON_PARKED' if result[1]<0 else 'INCONCLUSIVE'
    ck('summary',t['reference']==enc(reference) and t['normalized_interval']==list(map(enc,normalized)) and
       t['normalized_grid']==grid and t['normalized_bracket']==bracket and t['verdict']==verdict)
    ck('strict_straddle',result[0]<0<result[1])
    report.update(stage='verified',eigenmatrix=matrix,multiplicities=mult,
                  modes=[dict(j=j,interval=list(map(enc,pair))) for j,pair in enumerate(bounds)],
                  corrections=[dict(i=i,interval=list(map(enc,deltas[i-5]))) for i in range(5,69)],
                  comparison=t)
    save()
    print('Verified 4761/4761 integer coefficients, 69/69 modes, 64/64 corrections at the original box')
    print('Comparison/reference in [%s,%s]/%s; required >=0; verdict: %s' % (*bracket,grid,verdict))
    print('Checks:',sum(counts.values()),'; failures:',len(report['failures']),'; certificate:',OUT)


if __name__=='__main__':
    main()
