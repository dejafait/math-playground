"""Independent full scalar audit of C759d, with original artifacts preserved.

Fraction arithmetic rounded outwards by integer division to 100 significant
decimal digits. Only monotone transcendental endpoints use Decimal (120
digits). Trigonometry uses unreduced arguments and 90 Taylor terms, rather
than the generator's reduced arguments and 60 terms. See C759d for analysis.
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
SOURCE = BASE / 'shifted-schur-stop-806.py'
SAVED = BASE / 'shifted-schur-stop-806.json'
OUT = BASE / 'audit-808'
OUT.mkdir(exist_ok=True)
saved = json.loads(SAVED.read_text())
LOW = Context(prec=120, rounding=ROUND_FLOOR)
HIGH = Context(prec=120, rounding=ROUND_CEILING)
checks, failures = [], []


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


# Replay exact bytes in a new directory, under a deliberately small ambient
# precision. This checks every stored field but is not the independent audit.
copy = OUT / SOURCE.name
copy.write_bytes(SOURCE.read_bytes())
with localcontext() as ambient, redirect_stdout(io.StringIO()) as replay_log:
    ambient.prec = 7
    runpy.run_path(str(copy), run_name='__main__')
(OUT / 'replay.txt').write_text(replay_log.getvalue())
replayed = json.loads(copy.with_suffix('.json').read_text())
check('unchanged_replay_all_fields', replayed == saved)
check('source_hash', hashlib.sha256(SOURCE.read_bytes()).hexdigest() == saved['script_sha256'])
check('saved_checks', len(saved['checks']) == 8 and all(saved['checks'].values()))
check('saved_failures', saved['failures'] == [])
check('parameters', saved['parameters'] == {'N':120, 'retained_direction':1,
      'K':512, 'precision':60, 'tau':'11/200', 'd':'2859/10000'})

pi = 16*atan(5)-4*atan(239)
gamma = R(sum((F(1,j) for j in range(1,129)), F(0)))
gamma = gamma-transc(128,'ln')-F(1,256)+F(1,12*128**2)
radius = F(1,60*128**4)
gamma += R(-radius,radius)
exp2 = transc(2,'exp')
tanh1 = (exp2-1)/(exp2+1)
sinh_half = (transc(F(1,2),'exp')-transc(F(-1,2),'exp'))/2
g1 = 2*pi*sinh_half/(pi*pi+F(1,4))
for key,value in [('pi',pi),('gamma',gamma),('tanh1',tanh1),
                  ('sinh_half',sinh_half),('g1',g1)]:
    enclosure('constants/'+key,value)

partial = {key:R(0) for key in ('S','C','D','B')}
check('all_series_rows_present',len(saved['series_terms']) == 512)
for k in range(512):
    b = F(4*k+1,2)
    e = transc(-2*b,'exp')
    den = b*b+pi*pi
    row = {'S':pi*(1-e)/den,
           'C':-pi*pi*(1-e)/(b*den),
           'D':(1-e)*(b*b-pi*pi)/(den*den)-2*b*e/den,
           'B':(1-e)/b-(1-transc(-2*(b+F(1,2)),'exp'))/(b+F(1,2))}
    check(f'series_terms/{k}/index',saved['series_terms'][k]['k'] == k)
    enclosure(f'series_terms/{k}/b',R(b))
    enclosure(f'series_terms/{k}/E',e)
    for key,value in row.items():
        enclosure(f'series_terms/{k}/{key}',value)
        partial[key] += value
for key,value in partial.items():
    enclosure('series_partial_sums/'+key,value)

b = F(2049,2)
r2, r3 = 1/(b*b)+1/(2*b), 1/(b**3)+1/(4*b*b)
et = transc(-2*b,'exp')/(1-transc(-4,'exp'))
drad = R(r2)+2*et/b
tails = {'S':R(0,(pi*r2).hi), 'C':R((-pi*pi*r3).lo,0),
         'D':R(-drad.hi,drad.hi), 'B':R(0,r2/2)}
for key,value in [('R2',R(r2)),('R3',R(r3)),('exponential_sum',et)]:
    enclosure('tail_majorants/'+key,value)
integrals = {}
for key,value in tails.items():
    enclosure('tails/'+key,value)
    integrals[key] = partial[key]+value
    enclosure('integrals/'+key,integrals[key])
S,C,D,B = (integrals[key] for key in ('S','C','D','B'))
arch = -gamma-transc(4*pi*tanh1,'ln')-2*C+D-2*B-S/pi
pole = -2*g1*g1

prime = R(0)
trig_evidence = []
check('all_prime_rows_present',len(saved['prime_terms']) == 5)
for i,(n,p) in enumerate([(2,2),(3,3),(4,2),(5,5),(7,7)]):
    delay = transc(n,'ln')
    weight = transc(p,'ln')/transc(n,'sqrt')
    x = pi*delay
    sn,cs,se,ce = trig(x)
    q = (2-delay)*cs+sn/pi
    term = -weight*q
    prime += term
    row = saved['prime_terms'][i]
    check(f'prime_terms/{i}/integers',row['n'] == n and row['p'] == p)
    shift = row['reduction_integer']
    check(f'prime_terms/{i}/integer_shift',type(shift) is int)
    reduced = pi*(delay-2*shift)
    check(f'prime_terms/{i}/argument_bound',reduced.absupper() < 4)
    for key,value in [('delay',delay),('weight',weight),('reduced_argument',reduced),
                      ('sin',sn),('cos',cs),('q',q),('term',term)]:
        enclosure(f'prime_terms/{i}/{key}',value)
    trig_evidence.append({'n':n, 'unreduced_argument':display(x),
                          'sine_tail_radius':display(se),'cosine_tail_radius':display(ce)})

Q = arch+pole+prime
A = Q-F(11,200)
for key,value in [('archimedean',arch),('pole',pole),('prime',prime)]:
    enclosure('components/'+key,value)
enclosure('result/Q_s1',Q)
enclosure('result/shifted_A11',A)
check('S_d_upper_bound', A.hi <= F(saved['result']['S_d_upper_bound']))
check('published_Q_lower', F('0.00168053281301474') < Q.lo)
check('published_Q_upper', Q.hi < F('0.00364123566126519') < F('0.004'))
check('published_S_upper', A.hi < F('-0.05135876433873481') < F('-0.051'))
check('required_shift', Q.hi < F('0.004') < F(11,200))
check('strictly_positive_d', F(2859,10000) > 0)
check('complete_prime_support',transc(7,'ln').hi < 2 < transc(8,'ln').lo)
check('pi_bounds', 3 < pi.lo <= pi.hi < 4)
report = {
    'task':'C759d conceptual and complete scalar audit',
    'method':'Exact Fraction interval operations; integer outward rounding at 100 significant digits; 120-digit outward Decimal transcendental endpoints; unreduced 90-term sine/cosine',
    'audit_script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'source_sha256':hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
    'saved_certificate_sha256':hashlib.sha256(SAVED.read_bytes()).hexdigest(),
    'replay':'scripts/spectral-triples/audit-808/shifted-schur-stop-806.json',
    'series_rows_checked':512, 'prime_rows_checked':5,
    'check_count':len(checks),'checks':checks,'failures':failures,
    'independent_trigonometric_errors':trig_evidence,
    'result':{'Q_s1':display(Q),'shifted_A11':display(A),
              'S_d_upper_bound':str(decimal(A.hi,HIGH)),
              'required_Q_upper':'0.004 < tau=0.055',
              'required_S_d_upper':'-0.051',
              'audit_pass':not failures},
    'limitations':['Analytic proof audit is canonical in C759d.',
                  'Python integer and Decimal/libmpdec correctness remain software trust assumptions.',
                  'Fixed-shift stop only; no even/odd ordering or Xi transfer.']}
path = BASE/'first-sine-schur-audit-808.json'
path.write_text(json.dumps(report,indent=2)+'\n')
print('Complete audit:',len(checks),'checks; 512 series rows; 5 prime rows; failures:',failures)
print('Q(s1):',display(Q),'; required upper <0.004<0.055')
print('S_d(e1) <=',decimal(A.hi,HIGH),'; required upper <-0.051')
print('Certificate:',path.relative_to(BASE.parent.parent))
if failures:
    raise SystemExit(1)
