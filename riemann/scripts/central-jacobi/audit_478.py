"""Audit the fixed L791 certificate only; no new coefficient or model search.

Independent integer/Fraction interval arithmetic, outward-rounded on a
10^-100 grid after each operation. The inherited transcendental evaluator
is the audited L778 input. Original artifacts are never overwritten.
"""
import hashlib
import importlib.util
import json
import math
from fractions import Fraction as F
from pathlib import Path

BASE = Path(__file__).resolve().parent
ROOT = BASE.parent.parent
OUT = BASE / 'audit-478'
SCALE = 10**100
checks, failures = [], []
report = dict(scope='L791 finite certificate; audited L778 analytic input and backend contracts retained',
              rational_grid='1/10^100', checks=checks, failures=failures)


class Q:
    def __init__(self, lo=0, hi=None):
        self.lo = F(lo)
        self.hi = F(lo if hi is None else hi)
        assert self.lo <= self.hi

    @staticmethod
    def rounded(lo, hi):
        return Q(F((lo*SCALE).__floor__(), SCALE),
                 F((hi*SCALE).__ceil__(), SCALE))

    def __add__(self, other):
        x = q(other)
        return Q.rounded(self.lo+x.lo, self.hi+x.hi)

    __radd__ = __add__

    def __neg__(self):
        return Q(-self.hi, -self.lo)

    def __sub__(self, other):
        return self + (-q(other))

    def __rsub__(self, other):
        return q(other) + (-self)

    def __mul__(self, other):
        x = q(other)
        products = [a*b for a in (self.lo, self.hi) for b in (x.lo, x.hi)]
        return Q.rounded(min(products), max(products))

    __rmul__ = __mul__

    def __truediv__(self, other):
        x = q(other)
        assert x.lo > 0 or x.hi < 0, 'zero denominator interval'
        return self * Q.rounded(1/x.hi, 1/x.lo)

    def __rtruediv__(self, other):
        return q(other)/self

    def square(self):
        low = 0 if self.lo <= 0 <= self.hi else min(self.lo**2, self.hi**2)
        return Q.rounded(F(low), max(self.lo**2, self.hi**2))

    def mag(self):
        return max(abs(self.lo), abs(self.hi))

    def pair(self):
        return [str(self.lo), str(self.hi)]


def q(x):
    return x if isinstance(x, Q) else Q(x)


def check(name, value):
    checks.append(dict(name=name, passed=bool(value)))
    if not value:
        failures.append(name)


def encloses(name, saved, result):
    s = Q(*saved)
    check(name, s.lo <= result.lo and result.hi <= s.hi)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def matrix_system(box, dd, qq):
    a,b,c = box
    residual, jac = [], []
    for k in range(3):
        v = (a+k)*(b+k+1)/((a+k+1)*(b+k))*(c+k)*(dd+k+1)/((c+k+1)*(dd+k))
        residual.append(v-qq[k])
        jac.append([v/((a+k)*(a+k+1)), -v/((b+k)*(b+k+1)), v/((c+k)*(c+k+1))])
    return residual, jac


def audit():
    source = ROOT/'scripts/actual-fredholm/fixed-pair-certificate-431.json'
    original = BASE/'fixed-model-certificate-476.json'
    program = BASE/'fixed_model_476.py'
    hashes = {str(p.relative_to(ROOT)): digest(p) for p in (source,original,program)}
    data = json.loads(original.read_text())
    inherited = json.loads(source.read_text())['evaluation']
    prior_audit = json.loads((ROOT/'scripts/actual-fredholm/audit-433/audit-report.json').read_text())
    prior_replay = json.loads((ROOT/'scripts/actual-fredholm/audit-433/fixed-pair-certificate-431.json').read_text())
    check('inherited source hash matches L791', digest(source) == data['source_sha256'])
    check('inherited source hash matches L778 audit', digest(source) == prior_audit['original_sha256'])
    check('inherited evaluator equals complete audited replay', inherited == prior_replay['evaluation'])
    check('prior L778 audit passed', prior_audit['status'] == 'PASS' and not prior_audit['failures'])
    check('complex Cauchy radius', inherited['uniform_disk_radius'] == 1600)
    eg = Q(*inherited['uniform_G_error'])
    check('inherited error positive and below stated bound', 0 < eg.lo <= eg.hi < F('3.141e-48'))
    check('error interval retained unchanged', data['uniform_G_error'] == inherited['uniform_G_error'])
    aa = []
    for j in range(5):
        e = eg.hi/F(1600**j)
        actual = Q(*inherited['coefficients'][j])+Q(-e,e)
        encloses(f'actual_a {j}', data['actual_a'][j], actual)
        aa.append(Q(*data['actual_a'][j]))
    gg = [v*(8*4**j*math.factorial(j)) for j,v in enumerate(aa)]
    for j,v in enumerate(gg):
        encloses(f'gamma {j}',data['gamma'][j],v)
        check(f'gamma positivity {j}',v.lo>0)
    gg = [Q(*v) for v in data['gamma']]
    rr = [v/gg[0] for v in gg]
    for j,v in enumerate(rr):
        encloses(f'R {j}',data['R'][j],v)
    rr = [Q(*v) for v in data['R']]
    qq = [rr[k+1].square()/(rr[k]*rr[k+2]) for k in range(3)]
    for k,v in enumerate(qq):
        encloses(f'q {k}',data['q'][k],v)
    qq = [Q(*v) for v in data['q']]
    t = (qq[0]-1)/(qq[1]-1)
    aj = 2*qq[0]/(t-qq[0])
    bjden = qq[0]*(1+1/aj)-1
    bj = 1/bjden
    dd = bj/2
    stage = dict(T=t,T_minus_q0=t-qq[0],A_J=aj,B_J_denominator=bjden,B_J=bj,D=dd)
    for key,v in stage.items():
        encloses('first_stage '+key,data['first_stage'][key],v)
        check('first_stage positive '+key,v.lo>0)
    obligatory = dict(q0_minus_1=qq[0]-1,q1_minus_1=qq[1]-1,T_minus_q0=t-qq[0],A_J=aj,B_J=bj,D=dd)
    for key,v in obligatory.items():
        encloses('obligatory '+key,data['obligatory_bounds'][key],v)
        check('obligatory positive '+key,v.lo>0)
    dd = Q(*data['first_stage']['D'])
    check('one fixed box',len(data['attempts'])==1)
    rec = data['attempts'][0]
    r = F(rec['radius'])
    x = [F(v) for v in data['newton']['center']]
    box = [Q(*v) for v in rec['box']]
    check('radius exactly 1e-15', r == F('1e-15'))
    for i,v in enumerate(box):
        check(f'exact closed positive box {i}',v.lo==x[i]-r and v.hi==x[i]+r and v.lo>0)
    mm = [[F(v) for v in row] for row in data['preconditioner']]
    f0,_ = matrix_system([Q(v) for v in x],dd,qq)
    _,jac = matrix_system(box,dd,qq)
    disp = [-sum((mm[i][k]*f0[k] for k in range(3)),Q(0)) for i in range(3)]
    der = [[Q(int(i==j))-sum((mm[i][k]*jac[k][j] for k in range(3)),Q(0)) for j in range(3)] for i in range(3)]
    norms = [sum(v.mag() for v in row) for row in der]
    bounds = [disp[i].mag()+r*norms[i] for i in range(3)]
    for i in range(3):
        encloses(f'center residual {i}',rec['F_center'][i],f0[i])
        encloses(f'preconditioned residual {i}',rec['displacement'][i],disp[i])
        for j in range(3):
            encloses(f'whole-box derivative {i},{j}',rec['derivative'][i][j],der[i][j])
        check(f'saved row norm bounds recomputed row {i}',norms[i] <= F(rec['row_norms'][i][1]))
        check(f'saved selfmap bound covers recomputed value {i}',bounds[i] <= F(rec['selfmap_bounds'][i][1]))
        check(f'contraction {i}',norms[i]<1)
        check(f'selfmap {i}',bounds[i]<r)
    determinant = sum(mm[0][j]*(mm[1][(j+1)%3]*mm[2][(j+2)%3]-mm[1][(j+2)%3]*mm[2][(j+1)%3]) for j in range(3))
    # Cyclic 3x3 determinant formula: all three cyclic cofactors have + sign.
    check('exact preconditioner determinant nonzero', determinant != 0)
    check('stated contraction bound', max(norms)<F('4.240e-12'))
    check('stated center displacement bound', max(v.mag() for v in disp)<F('8.600e-22'))
    check('stated selfmap bound', max(bounds)<F('8.601e-22'))
    # Independently form each coefficient as a full Pochhammer product.
    a,b,c = box
    co = []
    for j in range(6):
        numerator,denominator = Q((-1)**j*math.comb(5,j)),Q(1)
        for k in range(j):
            numerator = numerator*(a+k)*(c+k)*dd
            denominator = denominator*a*c*(b+k)*(dd+k)
        co.append(numerator/denominator)
    check('degree exactly five', co[5].hi < 0)
    # Also check every saved recurrence coefficient, with the original order.
    recurrence=[Q(1)]
    for k in range(5):
        recurrence.append(-recurrence[-1]*(5-k)/(k+1)*(a+k)*(c+k)*dd/(a*c*(b+k)*(dd+k)))
    for j,v in enumerate(recurrence):
        encloses(f'model coefficient {j}',data['model_coefficients'][j],v)
    expected=[('5.87','5.88'),('10.26','10.27'),('14.27','14.28'),('18.76','18.77'),('23.63','23.64')]
    lower_claims=[('8.28e-5','1.38e-4'),('4.83e-5','4.09e-6'),('1.79e-5','1.91e-5'),('7.31e-7','6.21e-5'),('2.77e-4','5.49e-6')]
    roots=[]
    check('five brackets',len(data['root_brackets'])==5)
    for i,(left,right) in enumerate(expected):
        br=data['root_brackets'][i]
        check(f'bracket identity {i}',br['interval']==[left,right])
        check(f'positive disjoint bracket {i}',0<F(left)<F(right) and (i==0 or F(expected[i-1][1])<F(left)))
        endpoints=[]
        for side,y in enumerate((left,right)):
            yy=F(y)
            # Expanded sum, independent of the saved Horner evaluation.
            val=sum((co[j]*yy**j for j in range(6)),Q(0))
            expected_sign=(-1)**(i+side)
            margin=val.lo if expected_sign>0 else -val.hi
            check(f'independent endpoint strict sign {i},{side}',margin>F(lower_claims[i][side]))
            horner=Q(0)
            for v in reversed([Q(*v) for v in data['model_coefficients']]):
                horner=horner*yy+v
            encloses(f'saved endpoint {i},{side}',br['values'][side],horner)
            saved=Q(*br['values'][side])
            saved_margin=saved.lo if expected_sign>0 else -saved.hi
            check(f'saved endpoint claimed margin {i},{side}',saved_margin>F(lower_claims[i][side]))
            endpoints.append(dict(y=y,independent_value=val.pair(),strict_margin=str(margin),required_margin=lower_claims[i][side]))
        roots.append(dict(interval=[left,right],endpoints=endpoints))
    report['rational_evidence']=dict(inherited_error=eg.pair(),first_stage={k:v.pair() for k,v in stage.items()},
        box=[v.pair() for v in box],jacobian=[[v.pair() for v in row] for row in jac],
        center_residual=[v.pair() for v in f0],displacement=[v.pair() for v in disp],
        derivative=[[v.pair() for v in row] for row in der],row_norms=[str(v) for v in norms],
        contraction_upper=str(max(norms)),required_contraction='1',selfmap_bounds=[str(v) for v in bounds],
        selfmap_upper=str(max(bounds)),required_selfmap=str(r),preconditioner_determinant=str(determinant),
        independent_coefficients=[v.pair() for v in co],root_brackets=roots)
    # Replay the original program at a new path; its ROOT remains unchanged.
    spec=importlib.util.spec_from_file_location('central476',program)
    mod=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    mod.BASE=OUT
    mod.main()
    replay=json.loads((OUT/'fixed-model-certificate-476.json').read_text())
    check('complete same-code replay equals original',replay==data)
    report['original_hashes']=hashes
    for path,sha in hashes.items():
        check('original preserved '+path,digest(ROOT/path)==sha)
    report['runtime']=replay['runtime']
    report['summary']=dict(contraction_upper_display=format(float(max(norms)),'.12g'),
        required_contraction='1',selfmap_upper_display=format(float(max(bounds)),'.12g'),
        required_selfmap='1e-15',strict_root_endpoints=10,required_root_endpoints=10)


if __name__=='__main__':
    OUT.mkdir(exist_ok=True)
    try:
        audit()
    except Exception as exc:
        failures.append(type(exc).__name__+': '+str(exc))
    report['status']='PASS' if not failures else 'FAIL'
    path=OUT/'audit-report.json'
    path.write_text(json.dumps(report,indent=2)+'\n')
    print('audit:',report['status'],'checks:',len(checks),'failures:',failures)
    print('actual/required:',report.get('summary',{}))
    print('full certificate:',path.relative_to(ROOT))
    raise SystemExit(bool(failures))
