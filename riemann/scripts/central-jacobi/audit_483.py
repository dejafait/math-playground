"""Independent finite L792 audit. Exact Fraction intervals, no rounding.

Does not execute production programs or overwrite their artifacts. L791's
existence and L778's analytic/software contracts are inherited premises.
"""
import hashlib
import json
import math
from fractions import Fraction as F
from pathlib import Path

BASE = Path(__file__).resolve().parent
ROOT = BASE.parent.parent
OUT = BASE / 'audit-483'


class I:
    def __init__(self, lo=0, hi=None):
        self.lo, self.hi = F(lo), F(lo if hi is None else hi)
        assert self.lo <= self.hi

    def __add__(self, v):
        v = interval(v)
        return I(self.lo + v.lo, self.hi + v.hi)
    __radd__ = __add__

    def __neg__(self):
        return I(-self.hi, -self.lo)

    def __sub__(self, v):
        return self + (-interval(v))

    def __mul__(self, v):
        v = interval(v)
        p = [a*b for a in (self.lo, self.hi) for b in (v.lo, v.hi)]
        return I(min(p), max(p))
    __rmul__ = __mul__

    def __truediv__(self, v):
        v = interval(v)
        assert v.lo > 0 or v.hi < 0, 'denominator contains zero'
        return self * I(1/v.hi, 1/v.lo)

    def __pow__(self, n):
        assert n >= 0
        if n == 0:
            return I(1)
        if n % 2:
            return I(self.lo**n, self.hi**n)
        return I(0 if self.lo <= 0 <= self.hi else min(self.lo**n, self.hi**n),
                 max(self.lo**n, self.hi**n))

    def pair(self):
        return [str(self.lo), str(self.hi)]


def interval(v):
    return v if isinstance(v, I) else I(v)


def prod(vs):
    out = I(1)
    for v in vs:
        out = out * v
    return out


def expanded(cs, x):
    return sum((v * x**j for j, v in enumerate(cs)), I(0))


def horner(cs, x):
    out = I(0)
    for v in reversed(cs):
        out = out*x + v
    return out


def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def main():
    names = ['signed-residual-first-pass-480.json', 'signed-residual-certificate-480.json',
             'fixed-model-certificate-476.json', 'signed_residual_480.py', 'audit_478.py']
    paths = [BASE/n for n in names] + [ROOT/'scripts/actual-fredholm/fixed-pair-certificate-431.json',
                                     BASE/'audit-478/audit-report.json']
    hashes = {str(p.relative_to(ROOT)): digest(p) for p in paths}
    first, saved, model = [json.loads((BASE/n).read_text()) for n in names[:3]]
    ev = json.loads(paths[-2].read_text())['evaluation']
    prior = json.loads(paths[-1].read_text())
    checks, failures, evidence = [], [], {}

    def check(name, ok):
        checks.append({'name': name, 'passed': bool(ok)})
        if not ok:
            failures.append(name)

    def encloses(name, pair, v):
        s = I(*pair)
        check(name, s.lo <= v.lo and v.hi <= s.hi)

    def quoted(name, v, lower, upper):
        check('published strict bounds '+name, F(lower) < v.lo <= v.hi < F(upper))

    check('inherited L791 audit passed', prior['status'] == 'PASS' and not prior['failures'])
    check('model unchanged since L791 audit', hashes[str(paths[2].relative_to(ROOT))] == prior['original_hashes'][str(paths[2].relative_to(ROOT))])
    check('source unchanged since model', hashes[str(paths[-2].relative_to(ROOT))] == model['source_sha256'])
    check('signed certificate input hashes', all(hashes[k] == v for k,v in saved['input_hashes'].items()))
    check('current production hash matches certificate', digest(BASE/names[3]) == saved['program_sha256'])
    check('L778 complex disk and full error', ev['uniform_disk_radius'] == 1600 and
          0 < F(ev['uniform_G_error'][0]) <= F(ev['uniform_G_error'][1]) < F('3.141e-48'))
    check('whole original box', [[F(v) for v in pair] for pair in saved['box']] ==
          [[F(v) for v in pair] for pair in model['attempts'][0]['box']])
    check('unchanged D', [F(v) for v in saved['D']] == [F(v) for v in model['first_stage']['D']])
    aa, gg = [], []
    for j in range(6):
        width = F(ev['uniform_G_error'][1]) / 1600**j
        a = I(*ev['coefficients'][j]) + I(-width, width)
        encloses(f'full coefficient plus Cauchy {j}', saved['actual_a'][j], a)
        g = a * (8 * 4**j * math.factorial(j))
        encloses(f'gamma normalization {j}', saved['gamma'][j], g)
        check(f'positive gamma {j}', g.lo > 0)
        aa.append(a)
        gg.append(g)
    for j in range(6):
        encloses(f'ratio {j}', saved['R'][j], I(*saved['gamma'][j])/I(*saved['gamma'][0]))
    a,b,c = [I(*v) for v in saved['box']]
    d = I(*saved['D'])
    check('positive full parameters', all(v.lo > 0 for v in [a,b,c,d]))
    ss = b * I(*saved['R'][1])
    encloses('scale S=B R1', saved['S'], ss)
    # Complete Pochhammer products instead of production's coefficient recurrence.
    pc = []
    for j in range(6):
        numerator = prod([a+k for k in range(j)]) * prod([c+k for k in range(j)]) * d**j
        denominator = a**j * c**j * prod([b+k for k in range(j)]) * prod([d+k for k in range(j)])
        v = ((-1)**j * math.comb(5,j)) * numerator / denominator
        encloses(f'Pochhammer coefficient {j}', saved['model_coefficients'][j], v)
        pc.append(I(*saved['model_coefficients'][j]))
        check(f'alternating coefficient {j}', pc[j].lo > 0 if j%2 == 0 else pc[j].hi < 0)
    ta = I(*saved['R'][5]) / I(*saved['S'])**5
    encloses('actual fifth no binomial factor', saved['actual_magnitude'], ta)
    # Algebraically cancelled alternative: R5/(B R1)^5 = gamma5 gamma0^4/(B^5 gamma1^5).
    alt = gg[5] * gg[0]**4 / (b**5 * gg[1]**5)
    encloses('cancelled actual coefficient formula', saved['actual_magnitude'], alt)
    ta,tm = I(*saved['actual_magnitude']), -pc[5]
    encloses('model magnitude', saved['model_magnitude'], tm)
    encloses('actual coefficient sign', saved['actual_coefficient'], -ta)
    encloses('model coefficient sign', saved['model_coefficient'], pc[5])
    delta = tm-ta
    encloses('actual-minus-model residual', saved['signed_coefficient_residual'], delta)
    check('positive signed residual', delta.lo > 0)
    fc = [I(0), pc[4], pc[3], pc[2], pc[1], I(1)]
    dc = [fc[j]*j for j in range(1,6)]
    for name,cs in [('f_coefficients',fc),('derivative_coefficients',dc)]:
        for j,v in enumerate(cs):
            encloses(name+str(j),saved[name][j],v)
    check('monic derivative normalization five', dc[4].lo == dc[4].hi == 5)
    values, roots = [], []
    for j,rec in enumerate(saved['critical_points']):
        x = I(*rec['interval'])
        check(f'positive disjoint critical bracket {j+1}', x.lo > 0 and x.lo < x.hi and
              (j == 0 or roots[-1].hi < x.lo))
        endpoints = [expanded(dc,I(x.lo)), expanded(dc,I(x.hi))]
        for k,v in enumerate(endpoints):
            encloses(f'complete saved critical endpoint {j+1}/{k}',rec['derivative_endpoints'][k],v)
            expected = (1 if j%2 == 0 else -1) * (1 if k == 0 else -1)
            check(f'independent critical endpoint sign {j+1}/{k}', v.lo > 0 if expected == 1 else v.hi < 0)
        val = horner(fc,x)
        encloses(f'whole bracket critical value {j+1}', rec['f_at_critical'],val)
        values.append(I(*rec['f_at_critical']))
        roots.append(x)
        evidence[f'critical_{j+1}'] = dict(interval=x.pair(), derivative_expanded=[v.pair() for v in endpoints],
                                        value_exact_horner=val.pair(),value_independent_expanded=expanded(fc,x).pair())
    check('exact lower active at x2', values[1].lo > values[3].hi and saved['critical_selection']['lower_x2'])
    check('exact upper active at x1', values[0].hi < values[2].lo and saved['critical_selection']['upper_x1'])
    low,up = values[1],values[0]
    encloses('exact lower collision boundary',saved['collision_lower'],low)
    encloses('exact upper collision boundary',saved['collision_upper'],up)
    check('nonempty positive interval', 0 < low.lo and low.hi < up.lo)
    results = {'actual_lower':ta-low,'actual_upper':up-ta,'model_lower':tm-low,'model_upper':up-tm}
    for key,v in results.items():
        who,side = key.split('_')
        encloses('distance '+key,saved[who+'_collision_distances'][side],v)
        check('strict positive distance '+key, v.lo > 0)
    encloses('degree drop t=0',saved['degree_drop_distance'],ta)
    for side,v in [('lower',-up),('upper',-low)]:
        encloses('coefficient admissible '+side,saved['coefficient_interval'][side],v)
    for side,v in [('lower',tm-up),('upper',tm-low)]:
        encloses('residual admissible '+side,saved['residual_interval'][side],v)
    # All bounds printed in the canonical claim, not just abbreviated previews.
    quoted('gamma5',I(*saved['gamma'][5]),'1.753923091213315303489e-9','1.753923091213315303490e-9')
    quoted('S',I(*saved['S']),'.266624456637090190929190401245','.266624456637090237139176632086')
    quoted('ta',ta,'2.618476695898151944906970e-6','2.618476695898154214011868e-6')
    quoted('tm',tm,'2.618771043315652128073166e-6','2.618771043315666560373924e-6')
    quoted('delta',delta,'2.94347417497914061298e-10','2.94347417514615466953e-10')
    value_bounds = [('2.623019569357062518698362e-6','2.623019569681543916731915e-6'),
                    ('2.613486880358151681436165e-6','2.613486880800946664045556e-6'),
                    ('2.640829182651894807223633e-6','2.640829183378282748565444e-6'),
                    ('1.731205359955270255291876e-6','1.731205362087381916741088e-6')]
    for j,(v,bounds) in enumerate(zip(values,value_bounds)):
        quoted('critical value '+str(j+1),v,*bounds)
    distance_bounds = dict(actual_lower=('4.989815097205280861414e-9','4.989815540002532575702e-9'),
                           actual_upper=('4.542873458908304686494e-9','4.542873783391971824945e-9'),
                           model_lower=('5.284162514705464027610e-9','5.284162957514878937758e-9'),
                           model_upper=('4.248526041395958324439e-9','4.248526365891788658749e-9'))
    for key,v in results.items():
        quoted(key,v,*distance_bounds[key])
    quoted_roots = [('50218208479/1073741824000','313863803/6710886400'),
                    ('33354338651/536870912000','66708677303/1073741824000'),
                    ('93616060701/1073741824000','46808030351/536870912000'),
                    ('16164792849/107374182400','161647928491/1073741824000')]
    for j,(v,bounds) in enumerate(zip(roots,quoted_roots)):
        check('printed critical bracket '+str(j+1),v.lo == F(bounds[0]) and v.hi == F(bounds[1]))
    # Compare every common mathematical field and explicitly validate additions
    # and the changed diagnostic label. Do not call the entire records identical.
    exclusions = {'program_sha256','checks','failures','outcome','critical_selection','summary'}
    additions = {'coefficient_interval','residual_interval'}
    check('exact added fields',set(saved)-set(first) == additions and not set(first)-set(saved))
    for key in sorted(set(first)-exclusions):
        check('first/final mathematical identity '+key,first.get(key) == saved[key])
    check('first active-bound diagnostic was nonactive x3',first['critical_selection'] ==
          {'lower_x2':True,'upper_x3':False})
    check('final active-bound diagnostic is x1',saved['critical_selection'] ==
          {'lower_x2':True,'upper_x1':True})
    check('exact added summary field',set(saved['summary'])-set(first['summary']) ==
          {'permitted_signed_residual_interval'} and not set(first['summary'])-set(saved['summary']))
    for key,v in first['summary'].items():
        check('first/final complete summary identity '+key,v == saved['summary'][key])
    check('first run sole failure',first['failures'] == ['strict negative coefficient residual'])
    check('first run both interior checks passed',all(next(v['passed'] for v in first['checks'] if v['name']==name)
          for name in ['strict actual interior','strict model interior']))
    old, new = first['checks'],saved['checks']
    changes = [(i,x,y) for i,(x,y) in enumerate(zip(old,new)) if x != y]
    check('only sign assertion changed',len(old)==len(new) and len(changes)==1 and
          changes[0][1] == {'name':'strict negative coefficient residual','passed':False} and
          changes[0][2] == {'name':'signed coefficient residual excludes zero','passed':True})
    check('final outcome and all checks',saved['outcome']=='CERTIFIED_STRICT_INTERIOR' and
          not saved['failures'] and all(v['passed'] for v in saved['checks']))
    for p in paths:
        check('input preserved '+str(p.relative_to(ROOT)),digest(p)==hashes[str(p.relative_to(ROOT))])
    evidence.update(coefficients=[v.pair() for v in pc],actual_a=[v.pair() for v in aa],
                    gamma=[v.pair() for v in gg],cancelled_actual_magnitude=alt.pair(),
                    signed_residual=delta.pair(),distances={k:v.pair() for k,v in results.items()},
                    first_final_check_changes=changes,
                    first_final_additions=sorted(additions),
                    first_final_critical_selection=[first['critical_selection'],saved['critical_selection']],
                    added_summary_field='permitted_signed_residual_interval')
    report = dict(status='PASS' if not failures else 'FAIL',checks=checks,failures=failures,
                  input_sha256=hashes,program_sha256=digest(Path(__file__)),evidence=evidence,
                  required='all four strict critical sign pairs, exact active boundaries, both actual distances >0',
                  limitations='L791/L778 and runtime trusted; original first-pass source not retained, certificate-data equality checked')
    OUT.mkdir(exist_ok=True)
    path = OUT/'audit-report.json'
    path.write_text(json.dumps(report,indent=2)+'\n')
    print(report['status'],len(checks),'checks; failures:',failures)
    for key,v in results.items():
        print(key,'>',format(float(v.lo),'.16g'),'; required > 0')
    print('signed residual >',format(float(delta.lo),'.16g'),'; required nonzero')
    print('full exact certificate:',path.relative_to(ROOT))
    return bool(failures)


if __name__ == '__main__':
    raise SystemExit(main())
