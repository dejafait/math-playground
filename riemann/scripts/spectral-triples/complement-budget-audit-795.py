"""Audit C759a: unchanged replay plus exact-rational interval verification.

Only transcendental endpoints use Decimal (90 digits, outward expanded).
All subsequent arithmetic and containment tests are exact Fractions.
This checks the full finite certificate; analytic tails are justified in C759a.
The original artifacts are read-only. No spectral inequality is inferred.
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
SOURCE = BASE / 'complement-budget-793.py'
SAVED = BASE / 'complement-budget-793.json'
OUT = BASE / 'audit-795'
OUT.mkdir(exist_ok=True)
saved = json.loads(SAVED.read_text())
failures, evidence = [], []
FLOOR = Context(prec=90, rounding=ROUND_FLOOR)
CEIL = Context(prec=90, rounding=ROUND_CEILING)


class R:
    def __init__(self, a=0, b=None):
        if isinstance(a, R):
            self.lo, self.hi = a.lo, a.hi
        else:
            self.lo, self.hi = F(a), F(a if b is None else b)
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
        ends = [x*y for x in (a.lo, a.hi) for y in (b.lo, b.hi)]
        return R(min(ends), max(ends))

    __rmul__ = __mul__

    def __truediv__(a, b):
        b = R(b)
        assert not b.lo <= 0 <= b.hi
        return a * R(1/b.hi, 1/b.lo)

    def __rtruediv__(a, b):
        return R(b)/a

    def __pow__(a, n):
        assert isinstance(n, int) and n >= 0
        v = R(1)
        for _ in range(n):
            v = v*a
        return v


def dec(q, ctx):
    return ctx.divide(Decimal(q.numerator), Decimal(q.denominator))


def transc(x, name):
    x = R(x)
    lower, upper = dec(x.lo, FLOOR), dec(x.hi, CEIL)
    if name in ('ln', 'sqrt'):
        assert lower > 0
    a = FLOOR.next_minus(getattr(FLOOR, name)(lower))
    b = CEIL.next_plus(getattr(CEIL, name)(upper))
    return R(F(a), F(b))


def display(x):
    x = R(x)
    return [str(dec(x.lo, FLOOR)), str(dec(x.hi, CEIL))]


def check(name, condition, detail=None):
    evidence.append({'name': name, 'passed': bool(condition), 'detail': detail})
    if not condition:
        failures.append(name)


def enclosure(path, value):
    node = saved
    for key in path.split('/'):
        node = node[int(key)] if isinstance(node, list) else node[key]
    outer = R(*node)
    value = R(value)
    check(path, outer.lo <= value.lo <= value.hi <= outer.hi, display(value))


def atan(k):
    center = sum((F((-1)**j, (2*j+1)*k**(2*j+1)) for j in range(60)), F(0))
    radius = F(1, 121*k**121)
    return R(center-radius, center+radius)


# Unchanged bytes and hostile ambient Decimal precision check the replay.
copy = OUT / SOURCE.name
copy.write_bytes(SOURCE.read_bytes())
with localcontext() as ambient, redirect_stdout(io.StringIO()) as replay_log:
    ambient.prec = 7
    runpy.run_path(str(copy), run_name='__main__')
(OUT / 'replay.txt').write_text(replay_log.getvalue())
replayed = json.loads(copy.with_suffix('.json').read_text())
check('unchanged_replay_all_fields', replayed == saved)
check('source_hash', hashlib.sha256(SOURCE.read_bytes()).hexdigest() == saved['script_sha256'])
check('saved_failures_empty', saved['failures'] == [])
check('saved_checks_all_true', all(saved['checks'].values()))
check('fixed_dimensions', saved['N'] == 120 and saved['series_K'] == 512)

pi = 16*atan(5)-4*atan(239)
gamma_center = R(sum((F(1, j) for j in range(1,129)), F(0)))
gamma_center = gamma_center-transc(128, 'ln')-F(1,256)+F(1,12*128**2)
gamma = gamma_center+R(-F(1,60*128**4), F(1,60*128**4))
m_floor = -transc(4*pi,'ln')-4
edge = 121*pi
for key, value in [('pi',pi), ('gamma',gamma), ('m_floor',m_floor),
                   ('first_omitted_frequency',edge)]:
    enclosure('constants/'+key,value)

prime_norm, prime_trial = R(0), R(0)
for i,(n,p) in enumerate([(2,2),(3,3),(4,2),(5,5),(7,7)]):
    delay = transc(n,'ln')
    weight = transc(p,'ln')/transc(n,'sqrt')
    chain = transc(2,'sqrt') if n == 2 else R(1)
    check(f'prime_rows/{i}/integers', saved['prime_rows'][i]['n'] == n and saved['prime_rows'][i]['p'] == p)
    for key,val in [('delay',delay),('weight',weight),('chain_norm',chain)]:
        enclosure(f'prime_rows/{i}/{key}',val)
    prime_norm += chain*weight
    prime_trial += weight*(2-delay)

s = (transc(F(1,2),'exp')-transc(F(-1,2),'exp'))/2
pole_tail = 8*s*s/(pi*pi*120)
p100 = 400/(pi**3*120*(1-(100/edge)**2)**2)
h100 = transc(100/(2*pi),'ln')-F(1,5000)
arch100 = (1-p100)*h100+p100*m_floor
ell100 = arch100-prime_norm-pole_tail
low = transc(100/(2*pi),'ln')-prime_norm
high = (1-p100)*transc(F(121,2),'ln')-5*p100-prime_norm

Bpartial,Dpartial = R(0),R(0)
check('all_512_terms_present',len(saved['trial_details']['terms']) == 512)
for k in range(512):
    b = F(4*k+1,2)
    e = transc(-2*b,'exp')
    bt = (1-e)/b-(1-transc(-2*(b+F(1,2)),'exp'))/(b+F(1,2))
    dt = (1-e)/(b*b)-2*e/b
    check(f'term/{k}/index',saved['trial_details']['terms'][k]['k'] == k)
    enclosure(f'trial_details/terms/{k}/B',bt)
    enclosure(f'trial_details/terms/{k}/D0',dt)
    check(f'term/{k}/positive_integrals',bt.lo > 0 and dt.lo > 0)
    Bpartial += bt
    Dpartial += dt
b = F(2049,2)
tail = 1/(b*b)+1/(2*b)
B = Bpartial+R(0,tail/2)
D0 = Dpartial+R(0,tail)
exp2 = transc(2,'exp')
tanh1 = (exp2-1)/(exp2+1)
arch = -gamma-transc(4*pi*tanh1,'ln')-2*B+D0
pole = 16*s*s
trial = arch+pole-prime_trial
for key,value in [('B_partial',Bpartial),('D0_partial',Dpartial),
                  ('tail_sum_inverse_square_upper',R(tail)),('B',B),('D0',D0),
                  ('arch',arch),('pole',pole),('prime',prime_trial)]:
    enclosure('trial_details/'+key,value)
for key,value in [('prime_norm',prime_norm),('pole_tail',pole_tail),('p100',p100),
                  ('arch100',arch100),('lower100_unshifted',ell100),
                  ('case_low_upper',low),('case_high_upper',high),('trial',trial)]:
    enclosure('bounds/'+key,value)
check('all_thresholds_ceiling',max(low.hi,high.hi) <= F(saved['bounds']['all_thresholds_upper']))

# Check the published decimal claims, stronger than several generator flags.
for key,a,b in [('prime_norm','3.12925','3.12926'),
                ('pole_tail','0.0018341','0.0018343'),
                ('lower100_unshifted','-1.517752','-1.517751'),
                ('trial','0.052852','0.053831')]:
    v = R(*saved['bounds'][key])
    check('published/'+key,F(a)<v.lo and v.hi<F(b))
check('published/uniform', F(saved['bounds']['all_thresholds_upper']) < F('-0.1561'))
check('published/two_cases',F(saved['bounds']['case_low_upper'][1]) < F('-0.3619')
      and F(saved['bounds']['case_high_upper'][1]) < F('-0.1561119'))
check('published/trial_shift', F(saved['bounds']['trial'][1]) < F('0.054') < F('0.055'))
check('continuum_prerequisites',transc(7,'ln').hi < 2 < transc(8,'ln').lo
      and (2*transc(2,'ln')).hi < 2 < (3*transc(2,'ln')).lo
      and transc(3,'ln').lo > 1 and m_floor.hi < -5 and 0<p100.lo<p100.hi<1
      and (transc(1/(2*pi),'ln')-2).lo > m_floor.hi)
first = json.loads((BASE/'complement-budget-793-first-pass.json').read_text())
check('retained_first_pass_failure', first['failures'] == ['prime_norm_above_3_13'])
check('first_pass_decisive_bound_unchanged',
      first['bounds']['all_thresholds_upper'] == saved['bounds']['all_thresholds_upper'])

result = {
    'task':'C759a conceptual arithmetic audit, not a spectral certificate',
    'audit_script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'source_sha256':hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
    'saved_certificate_sha256':hashlib.sha256(SAVED.read_bytes()).hexdigest(),
    'method':'exact rational interval arithmetic; 90-digit outward Decimal transcendental endpoints',
    'replay':'audit-795/complement-budget-793.json',
    'complete_series_rows_checked':512,
    'check_count':len(evidence), 'checks':evidence, 'failures':failures,
    'bounds': {k:saved['bounds'][k] for k in ('trial','prime_norm','pole_tail','lower100_unshifted','all_thresholds_upper')},
    'required_shifted_lower':'>0', 'U':'0.054','tau':'0.055',
    'conclusion':'C759a numerical claims verified' if not failures else 'audit failed',
    'limitations':['Analytic domain and remainder audit is in C759a.',
                  'Decimal/libmpdec and Python arithmetic remain software trust assumptions.',
                  'No full odd spectral floor, parity ordering, Schur sign or Xi transfer is proved.'],
}
path = BASE/'complement-budget-audit-795.json'
path.write_text(json.dumps(result,indent=2)+'\n')
print('Full certificate: 512 series rows;',len(evidence),'checks; failures:',failures)
for key,value in result['bounds'].items():
    print(key,value)
print('Required shifted lower >0; U=0.054; tau=0.055')
print('Audit:',path.relative_to(BASE.parent.parent),'replay:',copy.with_suffix('.json').relative_to(BASE.parent.parent))
if failures:
    raise SystemExit(1)
