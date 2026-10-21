"""All-record audit of L072 diagnostic enclosure, plus independent row checks.

Primitive integer evidence and every saved factor/term are inspected.
The floating implementation comparisons are checks, not sign premises.
"""
import hashlib
import json
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import numpy as np
import enclose_first_pair_diagnostic as en
from haar_contraction import RelativeBox, central, average_adj, PLANES
from check_first_pair_exterior_heat import pairing

ROOT = Path(__file__).parent
PATH = ROOT/'first-pair-retained-enclosure-certificate.json'
OUT = ROOT/'first-pair-retained-enclosure-audit.json'


def frac(x):
    return F(int(x['numerator']), int(x['denominator']))


def integer_interval(x):
    lo, hi = int(x['lo']), int(x['hi'])
    assert lo <= hi
    return en.I(lo, hi)


def pair(x):
    c, r = F(float.fromhex(x['center_hex'])), F(float.fromhex(x['radius_hex']))
    assert r >= 0
    return c, r


def main():
    data = json.loads(PATH.read_text())
    failures, checks = [], []
    def check(name, condition):
        checks.append(dict(name=name, passed=bool(condition)))
        if not condition: failures.append(name)
    check('generator hash', data['script_sha256'] == hashlib.sha256(Path(en.__file__).read_bytes()).hexdigest())
    check('fixed-point scale', int(data['precision_scale']) == en.S)
    for name,digest in data['support_sha256'].items():
        check(f'support hash {name}',hashlib.sha256((ROOT/name).read_bytes()).hexdigest()==digest)
    sw, ar = en.sw, en.ar
    sw.DEGREE = data['degree']
    check('rule degree and panel count', sw.DEGREE == 20 and len(data['panels']) == 16)
    roots = [integer_interval(row['root']) for row in data['roots']]
    weights = [integer_interval(row['weight']) for row in data['roots']]
    for j, (row, z, w) in enumerate(zip(data['roots'], roots, weights)):
        check(f'root {j} bracket', -en.S < z.lo < z.hi < en.S and
              sw.sign_at(z.lo) == row['sign_lo'] and sw.sign_at(z.hi) == row['sign_hi'] and
              row['sign_lo'] != row['sign_hi'] and (j == 0 or roots[j-1].hi < z.lo))
        p, pm = sw.legendre(z)
        derivative = en.rat(20)*(pm-z*p)/(en.rat(1)-z*z)
        expected = en.rat(2)/((en.rat(1)-z*z)*derivative*derivative)
        check(f'weight {j}', w.lo > 0 and w.lo == expected.lo and w.hi == expected.hi)
    panels = [(F(x), F(y)) for x,y in data['panels']]
    expected_panels = [(F(0), F(1,32))]+[(F(2)**j,F(2)**(j+1)) for j in range(-5,10)]
    check('exact panel coverage', panels == expected_panels)
    check('rule coverage', len(roots) == 20 and len(data['mapped_rule']) == 320 and
          {(r['panel'],r['root']) for r in data['mapped_rule']} == {(p,k) for p in range(16) for k in range(20)})
    lambdas = [integer_interval(z) for z in data['eigenvalues']]
    heat_count = 0
    check('heat row coverage',len(data['heat']) == 320)
    for index, row in enumerate(data['mapped_rule']):
        left,right = panels[row['panel']]; root = roots[row['root']]; weight = weights[row['root']]
        time = en.rat(en.T0+(left+right)/2)+en.rat((right-left)/2)*root
        wt = en.rat((right-left)/2)*weight
        check(f'mapped rule {index}', en.rec(time) == row['time'] and en.rec(wt) == row['weight'])
        check(f'heat row {index} width', len(data['heat'][index]) == 24)
        for k, lam in enumerate(lambdas):
            value = ar.exp_negative(time*lam)
            check(f'heat {index},{k}', en.rec(value) == data['heat'][index][k])
            heat_count += 1
    # Rebuild analytic sine/cosine and coefficient inputs with integer intervals.
    pi = en.rat(16)*sw.arctan_enclosure(F(1,5))-en.rat(4)*sw.arctan_enclosure(F(1,239))
    check('pi', en.rec(pi) == data['pi'])
    trig = {k: sw.sin_cos(pi*en.rat(F(k,48))) for k in range(96)}
    norm, zero = en.sqrt_rational(F(1,12)), en.sqrt_rational(F(1,24))
    for k in range(24):
        expected = en.rat(0) if k == 0 else en.rat(4)*trig[k][0]*trig[k][0]
        check(f'eigenvalue {k}', en.rec(expected) == data['eigenvalues'][k])
    for kind, rows in data['basis'].items():
        check(f'basis shape {kind}', len(rows) == (23 if kind == 'V' else 24) and all(len(r) == len(rows) for r in rows))
        for j,row in enumerate(rows):
            for k,value in enumerate(row):
                if kind == 'V': expected = norm*trig[(2*(j+1)*(k+1))%96][0]
                else: expected = zero if k == 0 else norm*trig[((2*j+1)*k)%96][1]
                check(f'basis {kind},{j},{k}', en.rec(expected) == value)
    check('rho coverage',len(data['rho']) == 23)
    for j,row in enumerate(data['rho'],1):
        x = -4+F(j,3)
        if abs(x) <= F(5,2): expected = en.rat(1)
        elif abs(x) >= 3: expected = en.rat(0)
        else:
            b1 = ar.exp_negative(en.rat(1)/en.rat(9-x*x))
            b2 = ar.exp_negative(en.rat(1)/en.rat(x*x-F(25,4)))
            expected = b1/(b1+b2)
        check(f'rho {j}', en.rec(expected) == row)
    path = ROOT/data['factor_archive']
    check('factor hash', hashlib.sha256(path.read_bytes()).hexdigest() == data['factor_archive_sha256'])
    terms = data['component_terms']
    check('component counts', {k:len(v) for k,v in terms.items()} == {'M':12,'Q3':24,'Q6':96})
    expected_keys = {'weights_c','weights_r','heat_c','heat_r'}
    for name, rows in terms.items():
        for k, (alpha,beta,_) in enumerate(rows):
            for j in range(4):
                shape = (24 if alpha == j else 23,24 if beta == j else 23)
                for form in ('physical','spectral'):
                    for side in ('c','r'): expected_keys.add(f'{name}_{k}_{j}_{form}_{side}')
    archive = np.load(path)
    check('archive complete keys', set(archive.files) == expected_keys)
    entries = 0
    for key in archive.files:
        value = archive[key]
        check(f'finite {key}', np.all(np.isfinite(value)))
        if key.endswith('_r'): check(f'nonnegative {key}',np.all(value >= 0))
        if '_physical_' in key or '_spectral_' in key:
            name, k, j, _, _ = key.split('_'); alpha,beta,_ = terms[name][int(k)]; j=int(j)
            check(f'shape {key}',value.shape == (24 if alpha==j else 23,24 if beta==j else 23))
        entries += value.size
    for j,row in enumerate(data['mapped_rule']):
        z=integer_interval(row['weight'])
        c,r=F(float(archive['weights_c'][j])),F(float(archive['weights_r'][j]))
        check(f'weight conversion {j}',c-r<=F(z.lo,en.S) and F(z.hi,en.S)<=c+r)
        for k,raw in enumerate(data['heat'][j]):
            z=integer_interval(raw)
            c,r=F(float(archive['heat_c'][j,k])),F(float(archive['heat_r'][j,k]))
            check(f'heat conversion {j},{k}',c-r<=F(z.lo,en.S) and F(z.hi,en.S)<=c+r)
    # Independent finite-array formulas retain upper/prefix rows and actual Qs.
    box = RelativeBox(24)
    box.u[1].fill(0); box.u[3].fill(0)
    box.w = [central(box.u[mu],mu,box.a) for mu in range(4)]
    box.s = {(mu,nu):central(box.u[nu],mu,box.a)+central(box.u[mu],nu,box.a) for mu,nu in PLANES}
    box.triplet_weights = {(mu,nu):average_adj(average_adj(box.w[mu]+box.w[nu],mu),nu) for mu,nu in PLANES}
    rng = np.random.default_rng(930024)
    def field():
        factors, values = [], []
        for shape in box.shapes:
            vecs = [rng.normal(size=n) for n in shape]
            vecs = [v/np.linalg.norm(v) for v in vecs]
            z = np.ones(shape)
            for j,v in enumerate(vecs):
                sh=[1]*4; sh[j]=len(v); z *= v.reshape(sh)
            factors.append(vecs); values.append(z)
        return factors, values
    xf,x = field(); yf,y=field()
    original = [pairing(box,x,y), *[box.dot(x,q) for q in box.probe_matrices(y)]]
    implementation = []
    for name, expected in zip(('M','Q3','Q6'),original):
        actual = 0.
        for k,(alpha,beta,coeff) in enumerate(terms[name]):
            value=float(F(coeff))
            for j in range(4): value *= xf[alpha][j] @ archive[f'{name}_{k}_{j}_physical_c'] @ yf[beta][j]
            actual += value
        error=abs(actual-expected); required=2e-10*max(1.,abs(expected))
        implementation.append(dict(operator=name,actual=float(actual),reference=float(expected),error=float(error),required=float(required),passed=bool(error<=required)))
        check(f'finite-array implementation {name}',error<=required)
    mterms=terms['M']
    expected_coverage={(probe,im,iq) for probe in (3,6) for im,(a,b,_) in enumerate(mterms)
                       for iq,(qa,qb,_) in enumerate(terms[f'Q{probe}']) if (qa,qb)==(b,a)}
    actual_coverage={(r['probe'],r['M'],r['Q']) for r in data['tensor_terms']}
    check('complete trace term coverage', len(actual_coverage)==len(data['tensor_terms']) and actual_coverage==expected_coverage)
    summaries=[]
    check('result coverage',[r['probe'] for r in data['results']]==[3,6])
    cg=F(factorial(20)**4,41*factorial(40)**3)
    epsq=cg*(1+15*factorial(41))
    actual_gap=3*F(lambdas[1].lo,en.S)
    epst=ar.exp_negative(en.rat(1024)*en.rat(actual_gap)).absolute_upper()
    check('quadrature and tail errors',epsq==frac(data['relative_quadrature_error']) and epst==frac(data['relative_tail_error']))
    bounds={k:F(v) for k,v in data['norm_bounds'].items()}
    check('norm constants', bounds==dict(BM=F(12)*F(1,3)*24*97*216,B3=F(16)*162,B6=F(192)*162,
          dimension=F(4)*24*23**3,gap=F(1,48),actual_gap_lower=actual_gap))
    for result in data['results']:
        probe=result['probe']; relevant=[r for r in data['tensor_terms'] if r['probe']==probe]
        sc,sr=F(0),F(0)
        for row in relevant:
            cm=F(mterms[row['M']][2]); cq=F(terms[f'Q{probe}'][row['Q']][2])
            check(f'coefficient {probe},{row["M"]},{row["Q"]}',F(row['coefficient'])==cm*cq)
            c,r=pair(row['integral']); sc+=c; sr+=r
        c,r=pair(result['retained'])
        check(f'term aggregation {probe}',abs(c-sc)+sr<=r and result['terms']==len(relevant))
        norm_error=bounds['dimension']*bounds['BM']*bounds[f'B{probe}']/bounds['gap']**2*(2*(epsq+epst)+(epsq+epst)**2)
        total=r+norm_error
        check(f'final budget {probe}',norm_error==frac(result['quadrature_and_tail_error']) and total==frac(result['total_error']) and total<=1)
        check(f'negative sign {probe}',c+total<0 and result['sign']=='negative' and
              frac(result['lower'])==c-total and frac(result['upper'])==c+total)
        lower,upper={3:(F('-200.408'),F('-200.362')),6:(F('-20.752'),F('-20.210'))}[probe]
        check(f'published outward endpoints {probe}',lower<c-total and c+total<upper)
        summaries.append(dict(probe=probe,center=float(c),arithmetic_radius=float(r),quadrature_tail_error=float(norm_error),
                              total_error=float(total),required_error=1,lower=float(c-total),upper=float(c+total),terms=len(relevant)))
    audit=dict(scope='Complete saved-record audit; generator induction supplies tensor propagation; independent finite-array checks are floating diagnostics',
               certificate_sha256=hashlib.sha256(PATH.read_bytes()).hexdigest(),checks=checks,failures=failures,
               heat_entries=heat_count,archive_entries=entries,trace_terms=len(data['tensor_terms']),
               implementation_checks=implementation,results=summaries)
    OUT.write_text(json.dumps(audit,indent=2)+'\n')
    print(f'Audit: {len(checks)} checks; {len(failures)} failures; {heat_count} heat entries; {entries} archive entries; {len(data["tensor_terms"])} trace terms')
    for r in summaries: print(f'Probe {r["probe"]}: [{r["lower"]:.12g}, {r["upper"]:.12g}]; error {r["total_error"]:.6g} <= 1')
    print('Full audit:',OUT)
    if failures: raise SystemExit(1)


if __name__=='__main__': main()
