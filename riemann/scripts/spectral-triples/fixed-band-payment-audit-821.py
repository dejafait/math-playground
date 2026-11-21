"""Complete independent arithmetic audit of C759g, fixed input/bands/cap.

Reuse only the reviewed Fraction interval definitions in audit816; no old
matrix or certificate is executed. Exact rational terms, unreduced trig,
and independent pole/correlation formulas check every numerical interval.
"""
import ast
from contextlib import redirect_stdout
from decimal import Decimal, Context, ROUND_FLOOR, ROUND_CEILING, localcontext
from fractions import Fraction as F
from pathlib import Path
import decimal as decimal_module
import hashlib
import io
import json
import runpy
import sys

BASE = Path(__file__).resolve().parent
SOURCE = BASE/'fixed-band-payment-819.py'
ARITH = BASE/'two-sine-primitive-814.py'
INDEPENDENT = BASE/'two-sine-primitive-audit-816.py'
OUT = BASE/'audit-821'
OUT.mkdir(exist_ok=True)
saved = json.loads(SOURCE.with_suffix('.json').read_text())
LOW = Context(prec=120, rounding=ROUND_FLOOR)
HIGH = Context(prec=120, rounding=ROUND_CEILING)
checks, failures, checked_intervals = [], [], set()

# Read/compile definitions only; no top-level audit816 setup is run.
names = {'rounded', 'R', 'decimal', 'display', 'transc', 'atan', 'trig'}
nodes = [n for n in ast.parse(INDEPENDENT.read_text()).body
         if isinstance(n, (ast.FunctionDef, ast.ClassDef)) and n.name in names]
assert {n.name for n in nodes} == names
exec(compile(ast.Module(body=nodes, type_ignores=[]), str(INDEPENDENT), 'exec'))


def check(name, condition, detail=None):
    checks.append({'name': name, 'passed': bool(condition), 'detail': detail})
    if not condition:
        failures.append(name)


def enclosure(path, value):
    checked_intervals.add(path)
    node = saved
    for key in path.split('/'):
        node = node[int(key)] if isinstance(node, list) else node[key]
    x = R(value)
    check(path, F(node[0]) <= x.lo <= x.hi <= F(node[1]), display(x))


def scalar(path, value):
    node = saved
    for key in path.split('/'):
        node = node[int(key)] if isinstance(node, list) else node[key]
    check(path, node == value)


def intervals(node, prefix=''):
    if isinstance(node, list) and len(node) == 2 and all(isinstance(v, str) for v in node):
        try:
            F(node[0]); F(node[1])
        except ValueError:
            pass
        else:
            return {prefix}
    if isinstance(node, dict):
        return set().union(*(intervals(v, f'{prefix}/{k}'.strip('/')) for k, v in node.items()))
    if isinstance(node, list):
        return set().union(*(intervals(v, f'{prefix}/{i}'.strip('/')) for i, v in enumerate(node)))
    return set()


# Exact-byte replay copies preserve the originals. Only the recorded relative
# arithmetic path changes because the copy is nested one directory deeper.
copy = OUT/SOURCE.name
copy.write_bytes(SOURCE.read_bytes())
(OUT/ARITH.name).write_bytes(ARITH.read_bytes())
with localcontext() as ambient, redirect_stdout(io.StringIO()) as log:
    ambient.prec = 7
    replay_namespace = runpy.run_path(str(copy), run_name='__main__')
(OUT/'replay.txt').write_text(log.getvalue())
replayed = json.loads(copy.with_suffix('.json').read_text())
check('replay_expected_path', replayed['arithmetic_source']['path'] ==
      'spectral-triples/audit-821/two-sine-primitive-814.py')
replayed['arithmetic_source']['path'] = saved['arithmetic_source']['path']
check('replay_every_field_except_documented_path', replayed == saved)
check('generator_hash', hashlib.sha256(SOURCE.read_bytes()).hexdigest() == saved['script_sha256'])
check('arithmetic_hash', hashlib.sha256(ARITH.read_bytes()).hexdigest() == saved['arithmetic_source']['sha256'])
scalar('arithmetic_source/path', 'scripts/spectral-triples/two-sine-primitive-814.py')
check('original_checks', len(saved['checks']) == 12 and all(saved['checks'].values()))
check('original_failures', saved['failures'] == [])
check('parameters', saved['parameters'] == {'input':'s1=sin(pi*x)', 'half_width':1,
      'cap':'1/250', 'bands':[1,2], 'gamma_N':4096, 'psi_N':8192,
      'midpoint_N_each_interval':512, 'precision':60})
context_info = {}
for name in ('LO', 'HI'):
    ctx = replay_namespace['namespace'][name]
    context_info[name] = {'precision':ctx.prec, 'rounding':ctx.rounding,
                         'Emin':ctx.Emin, 'Emax':ctx.Emax,
                         'flags':{k.__name__:v for k,v in ctx.flags.items()}}
    check('context/'+name+'/range', ctx.prec == 60 and ctx.Emin == -999999 and ctx.Emax == 999999)
    check('context/'+name+'/rounding', ctx.rounding == (ROUND_FLOOR if name == 'LO' else ROUND_CEILING))
    for flag in (decimal_module.InvalidOperation, decimal_module.DivisionByZero,
                 decimal_module.Overflow, decimal_module.Underflow,
                 decimal_module.Subnormal, decimal_module.Clamped):
        check('context/'+name+'/'+flag.__name__, not ctx.flags[flag])

pi = 16*atan(5)-4*atan(239)
sh = (transc(R(F(1,2)), 'exp')-transc(R(F(-1,2)), 'exp'))/2
d = pi*pi+F(1,4)
alpha = 2*pi*sh/d
enclosure('constants/pi', pi)
enclosure('constants/sinh_half', sh)
enclosure('constants/alpha', alpha)
# Direct real integration: Fg(i/2)=Fg(-i/2)=-4S+S/d.
fg = -4*sh+sh/d
ps, pg = -2*alpha**2, 2*fg**2
prime_s, prime_g = R(0), R(0)
enclosure('correction/pole_s', ps)
enclosure('correction/pole_g', pg)
enclosure('correction/relative_pole', pg/3-ps)
for i, (n,p) in enumerate(((2,2),(3,3),(4,2),(5,5),(7,7))):
    prefix = f'correction/prime_terms/{i}'
    y = transc(R(n), 'ln')
    weight = transc(R(p), 'ln')/transc(R(n), 'sqrt')
    sn, cs, _, _ = trig(pi*y)
    # Independent product-to-sum integrations of the real functions.
    c_s = ((2-y)*cs+sn/pi)/2
    c_g = (2-y)+2*sn/pi+((2-y)*cs-sn/pi)/2
    es, eg = -2*weight*c_s, -2*weight*c_g
    prime_s += es
    prime_g += eg
    row = saved['correction']['prime_terms'][i]
    scalar(prefix+'/n', n)
    scalar(prefix+'/prime_base', p)
    scalar(prefix+'/formulas_overlap', True)
    check(prefix+'/shift_integer', isinstance(row['shift'], int))
    reduced = pi*y-2*pi*row['shift']
    check(prefix+'/reduction_bound', reduced.absupper() < 4)
    for key, value in {'delay':y, 'weight':weight, 'sin':sn, 'cos':cs,
                       'reduced_argument':reduced, 'C_s':c_s, 'C_g':c_g,
                       'E_s_term':es, 'E_g_term':eg, 'relative_term':eg/3-es,
                       'simplified_relative_term':-2*weight*(2-y)*(1-cs)/3}.items():
        enclosure(prefix+'/'+key, value)
es, eg = ps+prime_s, pg+prime_g
residual = eg/3-es
for key,value in {'prime_s':prime_s, 'prime_g':prime_g, 'E_s':es,
                  'E_g':eg, 'relative_prime':prime_g/3-prime_s, 'R':residual}.items():
    enclosure('correction/'+key, value)
check('all_prime_powers', transc(R(7),'ln').hi < 2 < transc(R(8),'ln').lo)

harmonic_exact = F(0)
for k in range(1,4097):
    term = F(1,k)
    harmonic_exact += term
    enclosure(f'constants/harmonic_terms/{k-1}', R(term))
harmonic = R(harmonic_exact)
center = harmonic-transc(R(4096),'ln')
gamma = center+R(F(-1,4096),0)
enclosure('constants/harmonic_sum', harmonic)
enclosure('constants/gamma_center', center)
enclosure('constants/gamma', gamma)
symbols = {}
for t in (1,2):
    a,b = F(1,4), F(t,2)
    prefix = f'digamma/{t}'
    zeroth = -gamma-R(a/(a*a+b*b))
    partial = R(0)
    for k in range(1,8193):
        # Positive rational representation, avoiding subtractive cancellation.
        term = (a*(k+a)+b*b)/(k*((k+a)**2+b*b))
        partial += R(term)
        enclosure(prefix+f'/terms/{k-1}', R(term))
    tail = R(0,a/8192+b*b/(2*8192**2))
    psi = zeroth+partial+tail
    symbols[t] = psi-transc(pi,'ln')
    for key,value in {'a':R(a),'b':R(b),'zeroth':zeroth,'partial_sum':partial,
                      'tail':tail,'psi':psi,'m':symbols[t]}.items():
        enclosure(prefix+'/'+key,value)

masses = {}
for length in (1,2):
    prefix = f'quadrature/{length}'
    total = R(0)
    for j in range(512):
        t = R(F(length*(2*j+1),1024))
        sn, _, _, _ = trig(t)
        q = (2*pi*sn/(pi*pi-t*t))**2
        total += q
        row = saved['quadrature'][str(length)]['terms'][j]
        scalar(prefix+f'/terms/{j}/j', j)
        check(prefix+f'/terms/{j}/shift_integer', isinstance(row['shift'],int))
        reduced = t-2*pi*row['shift']
        check(prefix+f'/terms/{j}/argument_bound', reduced.absupper() < 4)
        for key,value in {'t':t,'sin_t':sn,'reduced_argument':reduced,'abs_F_squared':q}.items():
            enclosure(prefix+f'/terms/{j}/'+key,value)
    midpoint = total*F(length,512)
    error = R(F(4*length**3,24*512**2))
    integral = midpoint+R(-error.hi,error.hi)
    masses[length] = integral/pi
    scalar(prefix+'/second_derivative_bound',4)
    for key,value in {'midpoint_sum':midpoint,'full_quadrature_error':error,
                      'integral_0_L':integral,'mass_abs_t_le_L':masses[length]}.items():
        enclosure(prefix+'/'+key,value)
p1,p2 = masses[1],1-masses[2]
h = 3/pi**2
increment = symbols[2]-symbols[1]
resource = p1*p2/h*increment*F(3,4)
defect = residual-resource
results = {'h':h,'R':residual,'p1':p1,'p2':p2,'m1':symbols[1],
           'm2':symbols[2],'m_increment':increment,'B':resource,'R_minus_B':defect}
for key,value in results.items():
    enclosure('result/'+key,value)
derivative = R(F(4,3))+4/transc(R(5),'sqrt')
enclosure('analytic_bounds/q_second_derivative_actual_bound',derivative)
scalar('analytic_bounds/gamma_error','[-1/N,0]')
scalar('analytic_bounds/psi_tail','[0,a/N+b^2/(2*N^2)]')
scalar('analytic_bounds/quadrature_error','4*L^3/(24*N^2)')
scalar('analytic_bounds/infinite_fourier_complement','Plancherel: p2=1-mass(|t|<=2)')
scalar('result/required_threshold',0)
scalar('result/decision','STOP fixed-band sufficient estimate at eligible s1')
check('derivative_bound_below4',derivative.hi < 4)
check('compact_denominator_positive',(pi*pi-4).lo > 0)
check('eligibility_import_C759d',F('0.00364123566126519') < F(1,250))
check('probabilities',0 < p1.lo < p1.hi < 1 and 0 < p2.lo < p2.hi < 1)
check('h_positive',h.lo > 0)
check('increment_positive',increment.lo > 0)
check('residual_positive',defect.lo > 0)
check('published_residual_bounds',F('1.17039531') < defect.lo and defect.hi < F('1.17043653'))
published = {'R':('1.2337657779','1.2337657780'),
             'p1':('0.0397677932','0.0397681981'),
             'p2':('0.7475910562','0.7475942943'),
             'm1':('-2.025298776','-2.025024115'),
             'm2':('-1.161709680','-1.161435013'),
             'B':('0.0633292503','0.0633704662')}
for key,(lo,hi) in published.items():
    check('published/'+key,F(lo) < results[key].lo and results[key].hi < F(hi))
expected = intervals(saved)
check('interval_coverage',expected == checked_intervals,
      {'expected':len(expected),'checked':len(checked_intervals),
       'missing':sorted(expected-checked_intervals),'extra':sorted(checked_intervals-expected)})
certificate = {'kind':'C759g complete independent arithmetic audit; REPRODUCTION',
               'audit_script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
               'runtime':{'python':sys.version,'libmpdec':decimal_module.__libmpdec_version__},
               'sources':{p.name:hashlib.sha256(p.read_bytes()).hexdigest()
                          for p in (SOURCE,ARITH,INDEPENDENT,SOURCE.with_suffix('.json'))},
               'contexts':context_info,'parameters':saved['parameters'],
               'independent_results':{k:display(v) for k,v in results.items()},
               'coverage':{'expected':len(expected),'checked':len(checked_intervals),
                           'missing':sorted(expected-checked_intervals),'extra':sorted(checked_intervals-expected)},
               'checks':checks,'failures':failures,'required_threshold':0,
               'decision':'ACCEPT scoped fixed-band stop' if not failures else 'AUDIT FAILURE',
               'trust':'Python integer/Fraction/Decimal and reviewed endpoint primitives; not formal verification'}
out = Path(__file__).with_suffix('.json')
out.write_text(json.dumps(certificate,indent=2)+'\n')
print('Checks:',len(checks),'Intervals:',len(checked_intervals),'Failures:',len(failures))
print('R-B:',display(defect),'Required lower threshold: 0')
print('Decision:',certificate['decision'],'Full certificate:',out)
if failures:
    print('Failed check names:',failures)
    raise SystemExit(1)
