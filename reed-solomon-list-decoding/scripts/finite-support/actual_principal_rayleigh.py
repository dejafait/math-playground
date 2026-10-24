"""One fixed vector on the actual C, with complete ordered marked counts."""
import gzip
import hashlib
import json
from collections import defaultdict
from fractions import Fraction as F
from math import comb
from pathlib import Path

B = Path(__file__).resolve().parent
ROOT = B.parent.parent
OUT = B/'actual-principal-rayleigh.json.gz'


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def enc(q):
    return [q.numerator, q.denominator]


def choose(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def main():
    r = dict(stage='in_progress', failures=[], checks=0,
             code_sha256=sha(Path(__file__)))

    def save():
        with gzip.open(OUT, 'wt') as f:
            json.dump(r, f)

    def ck(name, ok):
        r['checks'] += 1
        if not ok:
            r['stage'] = 'failed'
            r['failures'].append(name)
            save()
            raise AssertionError(name)

    names = ['positive-factor-enclosure.json.gz', 'positive-factor-enclosure-verification.json',
             'delsarte-lp-results.json', 'l112-l113-critical-audit.json',
             'l114-critical-audit.json', 'l120-critical-audit.json',
             'full-product-global-comparison.json']
    r['input_sha256'] = {str((B/n).relative_to(ROOT)):sha(B/n) for n in names}
    for name, code in [('l112-l113-critical-audit.json','critical_audit_l112_l113.py'),
                       ('l114-critical-audit.json','critical_audit_l114.py'),
                       ('l120-critical-audit.json','critical_audit_l120.py')]:
        a = json.loads((B/name).read_text())
        ck('audit_status_'+name, a['stage']=='verified' and not a['failures']
           and a['code_sha256']==sha(B/code))
        for path, digest in a['input_sha256'].items():
            ck('audit_binding_'+path, sha(ROOT/path)==digest)
    with gzip.open(B/names[0], 'rt') as f:
        z = json.load(f)
    rv = json.loads((B/names[1]).read_text())
    audit = json.loads((B/'l120-critical-audit.json').read_text())
    ck('root', z['stage']=='exact_complete' and z['inclusion'] and
       rv['stage']=='verified' and not rv['failures'] and
       rv['input_sha256']==sha(B/names[0]))
    ck('all_equations', z['coefficients']==audit['contraction_coefficients'] and
       len(z['coefficients'])==64 and sum(map(len,z['coefficients']))==81355)
    ck('all_margins', z['inclusion_margins']==rv['inclusion_margins'] and
       len(z['inclusion_margins'])==64 and min(z['inclusion_margins'])>0 and
       z['inclusion_margins']==[min(l+z['radius'],z['radius']-u)
                               for l,u in z['krawczyk_image']])
    lp = json.loads((B/'delsarte-lp-results.json').read_text())
    av = [F(q['numerator'],q['denominator']) for q in lp['exact']['primal']]
    N,H = 65537**28//2**128+1,comb(1024,68)
    U = F(comb(1024,64),comb(68,64))
    g = [comb(68,i)*comb(956,i) for i in range(69)]
    c = [F(1)]+[F(0)]*4+[(N-1)*av[i-5]/((U-1)*g[i]) for i in range(5,69)]
    ck('pairs', min(av)>0 and sum(av)==U-1 and z['c']==list(map(enc,c))
       and z['N']==N and z['H']==H and sum(g[i]*c[i] for i in range(69))==N)
    ck('unchanged_box', z['Q']==10**70 and z['radius']==10**25 and
       len(z['point'])==len(z['box'])==len(z['scale_powers'])==64 and
       z['box']==[[q-10**25,q+10**25] for q in z['point']])
    box = {i:[F(10)**z['scale_powers'][i-5]*F(t,z['Q']) for t in z['box'][i-5]]
           for i in range(5,69)}
    ck('positive_endpoints', all(0<l<u for l,u in box.values()))
    r.update(N=N,H=H,rho=enc(F(N,H)),c=list(map(enc,c)),
             endpoints={str(i):list(map(enc,v)) for i,v in box.items()},
             frozen={k:z[k] for k in ['N','H','Q','radius','point','scale_powers','box']})
    save()
    table = [[choose(n,k) for k in range(69)] for n in range(957)]
    ni = {i:choose(66,67-i)*comb(956,i) for i in range(5,68)}
    rows, cubic = [],defaultdict(int)
    for i in range(5,68):
        for j in range(5,68):
            hist = [0]*69
            for a in range(max(0,68-i-j),min(67-i,67-j)+1):
                b = 67-j-a
                anchor = table[67-i][a]*table[i-1][b]
                for p in range(max(0,j-(956-i)),min(i,j)+1):
                    h = 67-a-p
                    hist[h] += anchor*table[i][p]*table[956-i][j-p]
            ck('positive_class_total',sum(hist)==ni[j])
            ck('coincidence',hist[0]==int(i==j))
            # Include both B signs; mark reversal exchanges the two C signs.
            signed = [2*ni[i]*(hist[h]-(hist[h-1] if h else 0)) for h in range(69)]
            ck('signed_total',sum(signed)==0)
            for h in range(5,69):
                cubic[tuple(sorted((i,j,h)))] += signed[h]
            rows.append(dict(i=i,j=j,positive_C_per_B=hist,ordered_signed=signed))
    for row in rows:
        i,j = row['i'],row['j']
        ck('ordered_symmetry',row['ordered_signed']==rows[(j-5)*63+i-5]['ordered_signed'])
    cubic = {k:v for k,v in cubic.items() if v}
    diagonal = 2*sum(ni[i]*c[i] for i in ni)
    lo=hi=diagonal
    terms=[]
    for key,w in sorted(cubic.items()):
        pl=F(w)
        pu=F(w)
        for i in key:
            pl *= box[i][0 if w>0 else 1]
            pu *= box[i][1 if w>0 else 0]
        lo += pl
        hi += pu
        terms.append(dict(key=list(key),coefficient=w,interval=list(map(enc,(pl,pu)))))
    ck('nonzero_vector',sum(ni.values())>0 and diagonal>0)
    ck('interval_order',lo<=hi)
    norm = [lo/diagonal,hi/diagonal]
    grid = [norm[0].numerator*10**6//norm[0].denominator,
            -((-norm[1].numerator*10**6)//norm[1].denominator)]
    verdict = 'NEGATIVE_DIRECTION' if hi<0 else 'VECTOR_PARKED_NONNEGATIVE' if lo>=0 else 'ESTIMATE_PARKED_STRADDLE'
    r.update(stage='complete',counts=rows,positive_layers=ni,cubic=terms,
             diagonal=enc(diagonal),quadratic_interval=list(map(enc,(lo,hi))),
             normalized_interval=list(map(enc,norm)),normalized_grid=grid,
             vector_norm_squared=2*sum(ni.values()),verdict=verdict)
    save()
    print(json.dumps(dict(verdict=verdict,checks=r['checks'],failures=r['failures'],
                          ordered_layer_pairs=len(rows),collected_cubics=len(terms),
                          actual_normalized_bounds=grid,grid_denominator=10**6,
                          required_negative_upper=0,path=str(OUT.relative_to(ROOT)))))


if __name__=='__main__':
    main()
