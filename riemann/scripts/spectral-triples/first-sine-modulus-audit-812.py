"""Complete independent scalar audit of C759e; analytic audit is canonical there.

Interval primitives copied from the independently reviewed step808 audit:
exact Fraction operations with integer outward rounding, 100 significant
figures, 120-digit Decimal transcendental endpoints. Original step810
artifacts are never overwritten. No parameter sweep or new test is run.
"""
from contextlib import redirect_stdout
from decimal import Decimal, Context, ROUND_FLOOR, ROUND_CEILING, localcontext
from fractions import Fraction as F
from pathlib import Path
import hashlib
import io
import json
import runpy

BASE = Path(__file__).resolve().parent
SOURCE = BASE / 'first-sine-modulus-810.py'
SAVED = BASE / 'first-sine-modulus-810.json'
OUT = BASE / 'audit-812'
OUT.mkdir(exist_ok=True)
saved = json.loads(SAVED.read_text())
source_hash = hashlib.sha256(SOURCE.read_bytes()).hexdigest()
saved_hash = hashlib.sha256(SAVED.read_bytes()).hexdigest()
LOW = Context(prec=120, rounding=ROUND_FLOOR)
HIGH = Context(prec=120, rounding=ROUND_CEILING)
checks, failures = [], []
checked_intervals = set()


def rounded(q, upper):
    """Exact outward rounding on a rational decimal grid; no Decimal use."""
    q = F(q)
    if not q:
        return q
    # The estimate of decimal order differs by at most one from floor(log10).
    # Either grid is safe; using the finer choice keeps at least 100 digits.
    order = len(str(abs(q.numerator))) - len(str(q.denominator))
    exponent = order - 100
    grid = F(10**exponent) if exponent >= 0 else F(1, 10**(-exponent))
    scaled = q/grid
    n, d = scaled.numerator, scaled.denominator
    integer = -((-n)//d) if upper else n//d
    return integer*grid


class R:
    def __init__(self, a=0, b=None):
        if isinstance(a, R):
            self.lo, self.hi = a.lo, a.hi
        else:
            self.lo = rounded(F(a), False)
            self.hi = rounded(F(a if b is None else b), True)
        assert self.lo <= self.hi

    def __add__(a, b):
        b = R(b)
        return R(a.lo+b.lo, a.hi+b.hi)

    __radd__ = __add__

    def __neg__(a):
        return R(-a.hi, -a.lo)

    def __sub__(a, b):
        return a + -R(b)

    def __rsub__(a, b):
        return R(b) + -a

    def __mul__(a, b):
        b = R(b)
        endpoints = [x*y for x in (a.lo, a.hi) for y in (b.lo, b.hi)]
        return R(min(endpoints), max(endpoints))

    __rmul__ = __mul__

    def __truediv__(a, b):
        b = R(b)
        assert not b.lo <= 0 <= b.hi
        return a*R(1/b.hi, 1/b.lo)

    def __rtruediv__(a, b):
        return R(b)/a

    def __pow__(a, n):
        assert isinstance(n, int) and n >= 0
        value = R(1)
        for _ in range(n):
            value *= a
        return value

    def absupper(a):
        return max(abs(a.lo), abs(a.hi))


def decimal(q, ctx):
    return ctx.divide(Decimal(q.numerator), Decimal(q.denominator))


def display(x):
    x = R(x)
    return [str(decimal(x.lo, LOW)), str(decimal(x.hi, HIGH))]


def transc(x, name):
    x = R(x)
    lower, upper = decimal(x.lo, LOW), decimal(x.hi, HIGH)
    if name in ('ln', 'sqrt'):
        assert lower > 0
    a = LOW.next_minus(getattr(LOW, name)(lower))
    b = HIGH.next_plus(getattr(HIGH, name)(upper))
    return R(F(a), F(b))


def check(name, condition, detail=None):
    checks.append({'name': name, 'passed': bool(condition), 'detail': detail})
    if not condition:
        failures.append(name)


def enclosure(path, x):
    checked_intervals.add(path)
    node = saved
    for key in path.split('/'):
        node = node[int(key)] if isinstance(node, list) else node[key]
    x = R(x)
    # Compare exact original decimal endpoints, not rounded copies.
    check(path, F(node[0]) <= x.lo <= x.hi <= F(node[1]), display(x))


def atan(k):
    value = sum((F((-1)**j, (2*j+1)*k**(2*j+1)) for j in range(80)), F(0))
    error = F(1, 161*k**161)
    return R(value-error, value+error)


def trig(x):
    """Unreduced real argument; tail ratios <49/(180*181)<1/2."""
    assert x.absupper() < 7
    square = x*x
    st, ct = x, R(1)
    sn, cs = st, ct
    for k in range(1, 90):
        st = -st*square/((2*k)*(2*k+1))
        ct = -ct*square/((2*k-1)*(2*k))
        sn += st
        cs += ct
    se = 2*(st*square/(180*181)).absupper()
    ce = 2*(ct*square/(179*180)).absupper()
    return sn+R(-se, se), cs+R(-ce, ce), R(se), R(ce)


# Exact-byte replay is separate from the independent interval calculation.
copy = OUT / SOURCE.name
copy.write_bytes(SOURCE.read_bytes())
with localcontext() as ambient, redirect_stdout(io.StringIO()) as replay_log:
    ambient.prec = 7
    runpy.run_path(str(copy), run_name='__main__')
(OUT / 'replay.txt').write_text(replay_log.getvalue())
replayed = json.loads(copy.with_suffix('.json').read_text())
check('unchanged_replay_all_fields', replayed == saved)
check('source_hash', source_hash == saved['script_sha256'])
check('saved_checks', len(saved['checks']) == 7 and all(saved['checks'].values()))
check('saved_failures', saved['failures'] == [])
check('parameters', saved['parameters'] ==
      {'K':512, 'precision':60, 'half_width':1, 'sign_threshold':0})

pi = 16*atan(5)-4*atan(239)
enclosure('constants/pi', pi)
partial = R(0)
check('all_series_rows_present', len(saved['series_terms']) == 512)
for j in range(512):
    b = F(4*j+1,2)
    exponential = transc(-b, 'exp')
    denominator = R(b*b)+pi*pi
    laplace = pi*(1+exponential)/denominator
    # Recompute the squared transform directly, not by squaring laplace.
    term = pi*pi*(1+exponential)**2/(denominator**2)
    check(f'series_terms/{j}/index', saved['series_terms'][j]['j'] == j)
    for key,value in [('b',R(b)), ('exp_minus_b',exponential),
                      ('laplace_u',laplace), ('term',term)]:
        enclosure(f'series_terms/{j}/{key}', value)
    partial += term
enclosure('series_partial_sum',partial)

b = F(2049,2)
r4 = b**(-4)+b**(-3)/6
unsigned_tail = 4*pi*pi*r4
gamma_tail = R(-4*unsigned_tail.hi, 0)
for key,value in [('B',R(b)), ('R4',R(r4)),
                  ('unsigned_tail_upper',unsigned_tail),
                  ('gamma_defect_tail',gamma_tail)]:
    enclosure('tail/'+key,value)
arch = -4*partial+gamma_tail

iplus = pi*(1+transc(F(1,2),'exp'))/(pi*pi+F(1,4))
iminus = pi*(1+transc(F(-1,2),'exp'))/(pi*pi+F(1,4))
enclosure('constants/I_plus',iplus)
enclosure('constants/I_minus',iminus)
# Independently use the signed products for odd and even vectors.
pole_even = 2*(iplus+iminus)**2
pole_odd = -2*(iplus-iminus)**2
pole = pole_even-pole_odd

prime = R(0)
trig_evidence = []
check('all_prime_rows_present',len(saved['prime_terms']) == 5)
for i,(n,p) in enumerate([(2,2),(3,3),(4,2),(5,5),(7,7)]):
    row = saved['prime_terms'][i]
    delay = transc(n,'ln')
    check(f'prime_terms/{i}/integers',row['n'] == n and row['p'] == p)
    check(f'prime_terms/{i}/support',0 < delay.lo <= delay.hi < 2)
    if delay.hi < 1:
        h,branch = delay,'d<1'
    else:
        check(f'prime_terms/{i}/upper_branch',delay.lo > 1)
        h,branch = 2-delay,'d>1'
    check(f'prime_terms/{i}/branch',row['branch'] == branch)
    # Unreduced Taylor argument, 90 terms instead of the generator's 60.
    x = pi*h
    sn,cs,se,ce = trig(x)
    correlation = (sn/pi-h*cs)/2
    weight = transc(p,'ln')/transc(n,'sqrt')
    term = -4*weight*correlation
    prime += term
    shift = row['reduction_integer']
    check(f'prime_terms/{i}/integer_shift',type(shift) is int)
    reduced = pi*(h-2*shift)
    check(f'prime_terms/{i}/reduced_argument_bound',reduced.absupper() < 4)
    for key,value in [('delay',delay), ('h',h), ('reduced_argument',reduced),
                      ('sin',sn), ('cos',cs), ('H',correlation),
                      ('weight',weight), ('term',term)]:
        enclosure(f'prime_terms/{i}/{key}',value)
    check(f'prime_terms/{i}/positive_H',correlation.lo > 0)
    trig_evidence.append({'n':n, 'unreduced_argument':display(x),
                          'sine_tail_radius':display(se),
                          'cosine_tail_radius':display(ce)})

for key,value in [('archimedean',arch),('pole',pole),('prime',prime)]:
    enclosure('components/'+key,value)
delta = arch+pole+prime
enclosure('result/Delta_1',delta)
# C759d's already audited conclusion is an input, not recomputed here.
q_sine = R(F('0.00168053281301474'),F('0.00364123566126519'))
enclosure('input/C759d_Q_sine',q_sine)
enclosure('result/Q_modulus_from_imported_Q_sine',q_sine+delta)
check('cap_as_stated',saved['input']['required_energy_cap'] == '1/250')
check('input_cap',q_sine.hi < F(1,250))
check('required_sign_as_stated',saved['result']['required_for_strict_modulus_lowering'] == 'Delta_1<0')
check('saved_sign',saved['result']['sign'] == 'positive')
check('published_defect_lower',F('0.00111835') < delta.lo)
check('published_defect_upper',delta.hi < F('0.00111838'))
check('required_sign_threshold',delta.lo > 0)
check('published_gamma_tail',gamma_tail.lo > -F('0.00000002461890'))
check('complete_prime_support',transc(7,'ln').hi < 2 < transc(8,'ln').lo)
check('pi_bounds',3 < pi.lo <= pi.hi < 4)
check('tail_below_original_budget',unsigned_tail.hi < F('0.00000001'))

# Ensure no stored numerical interval was skipped by the audit.
def interval_paths(node,path=''):
    if isinstance(node,list) and len(node) == 2 and all(isinstance(v,str) for v in node):
        try:
            F(node[0]); F(node[1])
        except ValueError:
            return set()
        return {path}
    if isinstance(node,dict):
        result = set()
        for key,value in node.items():
            result |= interval_paths(value,path+'/'+key if path else key)
        return result
    if isinstance(node,list):
        result = set()
        for i,value in enumerate(node):
            result |= interval_paths(value,path+'/'+str(i))
        return result
    return set()
all_intervals = interval_paths(saved)
check('all_saved_intervals_checked',all_intervals == checked_intervals,
      {'total':len(all_intervals),'checked':len(checked_intervals),
       'missing':sorted(all_intervals-checked_intervals),
       'extra':sorted(checked_intervals-all_intervals)})
check('source_unchanged',hashlib.sha256(SOURCE.read_bytes()).hexdigest() == source_hash)
check('saved_certificate_unchanged',hashlib.sha256(SAVED.read_bytes()).hexdigest() == saved_hash)

report = {
    'task':'C759e conceptual and complete scalar audit',
    'method':'Fraction interval arithmetic with integer outward rounding at 100 significant digits; 120-digit outward Decimal transcendental endpoints; 80-term exact Machin and unreduced 90-term sine/cosine',
    'audit_script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'source_sha256':source_hash, 'saved_certificate_sha256':saved_hash,
    'replay':'scripts/spectral-triples/audit-812/first-sine-modulus-810.json',
    'series_rows_checked':512,'prime_rows_checked':5,
    'saved_intervals_checked':len(checked_intervals),
    'check_count':len(checks),'checks':checks,'failures':failures,
    'independent_trigonometric_errors':trig_evidence,
    'components':{'archimedean':display(arch),'pole':display(pole),'prime':display(prime)},
    'result':{'Delta_1':display(delta),'gamma_defect_tail':display(gamma_tail),
              'input_Q_sine':display(q_sine),'required_input_cap':'1/250',
              'required_for_lowering':'Delta_1<0','audit_pass':not failures},
    'limitations':['Analytic and Fourier-convention audit is canonical in C759e.',
                  'C759d audited unit first-sine cap is an explicit imported input.',
                  'Python integer and Decimal/libmpdec correctness remain trust assumptions.',
                  'Fixed capped modulus stop only; no parity-infimum or Xi conclusion.']}
path = BASE/'first-sine-modulus-audit-812.json'
path.write_text(json.dumps(report,indent=2)+'\n')
print('Complete audit:',len(checks),'checks;',len(checked_intervals),'saved intervals; failures:',failures)
print('Delta_1:',display(delta),'; required for lowering: <0')
print('Gamma defect tail:',display(gamma_tail))
print('Input Q(s1) upper:',decimal(q_sine.hi,HIGH),'; required cap: 0.004')
print('Certificate:',path.relative_to(BASE.parent.parent))
if failures:
    raise SystemExit(1)
