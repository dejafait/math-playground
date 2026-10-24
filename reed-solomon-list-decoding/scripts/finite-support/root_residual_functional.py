"""One frozen residual-corrected scalar enclosure; no solve or box update."""
import gzip
import hashlib
import json
import sys
from collections import Counter, defaultdict
from fractions import Fraction as F
from pathlib import Path

sys.set_int_max_str_digits(0)
B = Path(__file__).resolve().parent
ROOT = B.parent.parent
OUT = B/'root-residual-functional.json.gz'
T = 10**120  # Fixed absolute outward arithmetic grid; root data are untouched.


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def enc(v):
    return [v.numerator, v.denominator]


def interval(v):
    return (v.numerator*T//v.denominator,
            -((-v.numerator*T)//v.denominator))


def add(a, b):
    return (a[0]+b[0], a[1]+b[1])


def mul(a, b):
    p = [x*y for x in a for y in b]
    return (min(p)//T, -((-max(p))//T))


def main():
    report = dict(stage='in_progress', failures=[], checks=0,
                  code_sha256=sha(Path(__file__)), arithmetic_grid=T)

    def save():
        with gzip.open(OUT, 'wt') as f:
            json.dump(report, f)

    def ck(label, ok):
        report['checks'] += 1
        if not ok:
            report['stage'] = 'failed'
            report['failures'].append(label)
            save()
            raise AssertionError(label)

    names = ['positive-factor-enclosure.json.gz', 'positive-factor-enclosure-verification.json',
             'l112-l113-critical-audit.json', 'l114-critical-audit.json',
             'full-product-global-comparison.json', 'full-product-global-comparison-verification.json',
             'l120-critical-audit.json', 'delsarte-lp-results.json']
    paths = [B/n for n in names]
    paths += [ROOT/'lemmas'/n for n in [
        'L021-basic-delsarte-support-lp-optimum.md',
        'L098-exact-cardinality-normalized-control-obstruction.md',
        'L112-enclosed-product-root-passes-distance-five-capacity.md',
        'L113-enclosed-product-root-passes-all-upper-capacities.md',
        'L114-fixed-product-box-passes-Boolean-lower-rows.md',
        'L120-full-product-global-comparison-inconclusive.md']]
    paths += [ROOT/'foundations'/n for n in [
        '09-global-pair-johnson-source.md', '12-global-degree-three-moment-source.md',
        '13-fixed-cardinality-marginal-source.md', '14-validated-nonlinear-enclosure-source.md']]
    report['input_sha256'] = {str(p.relative_to(ROOT)):sha(p) for p in paths}
    save()
    for name, code in [('l112-l113-critical-audit.json', 'critical_audit_l112_l113.py'),
                       ('l114-critical-audit.json', 'critical_audit_l114.py'),
                       ('l120-critical-audit.json', 'critical_audit_l120.py')]:
        a = json.loads((B/name).read_text())
        ck('retained_'+name, a['stage']=='verified' and not a['failures'] and
           a['code_sha256']==sha(B/code))
        for p,h in a['input_sha256'].items():
            ck('audit_binding_'+p, sha(ROOT/p)==h)
    with gzip.open(B/names[0], 'rt') as f:
        root = json.load(f)
    old = json.loads((B/'full-product-global-comparison.json').read_text())
    audited = json.loads((B/'l120-critical-audit.json').read_text())
    ck('all_original_polynomials', root['coefficients']==audited['contraction_coefficients'] and
       len(root['coefficients'])==64 and sum(map(len,root['coefficients']))==81355)
    ck('frozen_data', old['frozen']=={k:root[k] for k in old['frozen']} and
       root['Q']==10**70 and root['radius']==10**25 and root['inclusion'] and
       root['box']==[[q-root['radius'],q+root['radius']] for q in root['point']])
    Q = root['Q']
    scales = [F(10)**p for p in root['scale_powers']]
    a = [F(q,Q) for q in root['point']]
    boxes = [tuple(F(q,Q) for q in pair) for pair in root['box']]
    radius = F(root['radius'],Q)
    C = [[F(q,Q) for q in row] for row in root['preconditioner']]
    ck('all_positive_original_endpoints', len(C)==len(a)==64 and
       all(len(row)==64 for row in C) and all(0<l<u for l,u in boxes))
    c = [F(*v) for v in root['c']]
    R0 = c[5]/(scales[0]*boxes[0][1])**2
    ck('fixed_reference', R0>0 and enc(R0)==old['comparison']['reference'])
    P = old['eigenmatrix'][1][5:]
    w = [F(p)*s/R0 for p,s in zip(P,scales)]
    z = [sum(C[i][k]*w[i] for i in range(64)) for k in range(64)]
    constant = 1+sum(z)
    demands = [F(*v) for v in root['demands']]
    coeff = defaultdict(F)
    for i,row in enumerate(root['coefficients']):
        for j,h,A in row:
            b = F(A)*scales[i]*scales[j]*scales[h]/demands[i]
            coeff[tuple(sorted((i,j,h)))] -= z[i]*b
    cubics = [[list(key), enc(value), list(interval(value))]
              for key,value in sorted(coeff.items())]
    derivative = [[] for _ in range(64)]
    for idx,(key,_,_) in enumerate(cubics):
        for k,m in Counter(key).items():
            remaining = list(key)
            remaining.remove(k)
            derivative[k].append([*remaining,idx,m])
    ai = [interval(v) for v in a]
    bi = [(interval(l)[0],interval(u)[1]) for l,u in boxes]
    ck('exact_point_and_box_on_grid', all(l==u for l,u in ai) and
       all(F(l,T)==x and F(u,T)==y for (l,u),(x,y) in zip(bi,boxes)))
    ha = interval(constant)
    for wi,vi in zip(w,ai):
        ha = add(ha,mul(interval(wi),vi))
    for key,_,cv in cubics:
        term = tuple(cv)
        for k in key:
            term = mul(term,ai[k])
        ha = add(ha,term)
    gradients = []
    for k,row in enumerate(derivative):
        value = interval(w[k])
        for p,q,idx,m in row:
            cv = cubics[idx][2]
            term = mul(mul((m*cv[0],m*cv[1]),bi[p]),bi[q])
            value = add(value,term)
        gradients.append(value)
    # Scalar mean-value form h(a)+Dh(B)*(B-a); keep the original E.
    ei = interval(radius)
    ck('exact_original_radius', ei[0]==ei[1] and F(ei[0],T)==radius)
    error = (0,0)
    for grad in gradients:
        error = add(error,mul(grad,(-ei[1],ei[1])))
    result = add(ha,error)
    verdict = 'MODE_ONE_PASSES' if result[0]>=0 else 'MODE_ONE_REJECTED' if result[1]<0 else 'STRICT_STRADDLE'
    grid = 10**6
    bracket = [result[0]*grid//T,-((-result[1]*grid)//T)]
    report.update(stage='complete', frozen={k:root[k] for k in [
        'N','H','Q','radius','point','scale_powers','box','preconditioner']},
        rho=old['rho'], c=root['c'], reference=enc(R0), johnson_mode_one=P,
        w=list(map(enc,w)), z=list(map(enc,z)), constant=enc(constant),
        cubics=cubics, derivative=derivative, point_value=list(ha),
        gradient_bounds=list(map(list,gradients)), error_interval=list(error),
        result_interval=list(result), result_fraction=[enc(F(v,T)) for v in result],
        required='lower endpoint >= 0', verdict=verdict,
        normalized_grid=grid, normalized_bracket=bracket)
    save()
    print('Actual/required: 64/64 equations; 81355/81355 original coefficients; 64/64 derivatives; required lower >=0')
    print('Enclosure of (lambda_1+R0)/R0 in [%s,%s]/%s; verdict: %s' % (*bracket,grid,verdict))
    print('Collected cubics:',len(cubics),'; checks:',report['checks'],'; failures:',len(report['failures']),'; certificate:',OUT)


if __name__=='__main__':
    main()
