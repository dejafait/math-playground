"""Independent complete arithmetic audit of C759f; original artifacts preserved.
Fraction interval operations use integer outward rounding (100 significant
figures); transcendental endpoints use Decimal at 120 digits. Correlations
are directly bilinear, trig uses unreduced arguments and 120 terms.
Analytic proof and software qualifications are canonical in C759f.
"""
from contextlib import redirect_stdout
from decimal import Decimal, Context, ROUND_FLOOR, ROUND_CEILING, localcontext
from fractions import Fraction as F
from pathlib import Path
from math import comb
import decimal as decimal_module
import hashlib
import io
import json
import runpy
import sys

BASE = Path(__file__).resolve().parent
SOURCE = BASE/'two-sine-primitive-814.py'
SAVED = SOURCE.with_suffix('.json')
OUT = BASE/'audit-816'
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
    """Unreduced real argument; tail ratios <169/(240*241)<1/2."""
    assert x.absupper() < 13
    square = x*x
    st, ct = x, R(1)
    sn, cs = st, ct
    for k in range(1, 120):
        st = -st*square/((2*k)*(2*k+1))
        ct = -ct*square/((2*k-1)*(2*k))
        sn += st
        cs += ct
    se = 2*(st*square/(240*241)).absupper()
    ce = 2*(ct*square/(239*240)).absupper()
    return sn+R(-se, se), cs+R(-ce, ce), R(se), R(ce)


class C:
    def __init__(self, r=0, i=0):
        if isinstance(r, C): self.r, self.i = r.r, r.i
        else: self.r, self.i = R(r), R(i)
    def __add__(a,b):
        b=C(b); return C(a.r+b.r,a.i+b.i)
    __radd__=__add__
    def __neg__(a): return C(-a.r,-a.i)
    def __sub__(a,b): return a+-C(b)
    def __mul__(a,b):
        b=C(b); return C(a.r*b.r-a.i*b.i,a.r*b.i+a.i*b.r)
    __rmul__=__mul__
    def __truediv__(a,b):
        b=C(b); den=b.r*b.r+b.i*b.i
        return C((a.r*b.r+a.i*b.i)/den,(a.i*b.r-a.r*b.i)/den)
    def conj(a): return C(a.r,-a.i)


def directed_cross(u,v):
    # Direct integration of u(x+y)*v(x); no (u+v)^2 polarization.
    result={k:[C(),C()] for k in range(-2,3)}
    for a,ca in u.items():
        for b,cb in v.items():
            z=ca*cb
            if a+b == 0:
                result[a][0] += 2*z
                result[a][1] -= z
            else:
                factor=z/C(0,(a+b)*pi)
                if (a+b)%2: factor=-factor
                result[-b][0] += factor
                result[a][0] -= factor
    return result


def symmetric_cross(u,v):
    uv,vu=directed_cross(u,v),directed_cross(v,u)
    return {k:[(uv[k][j]+vu[k][j])/2 for j in (0,1)] for k in uv}


def moment_basis(b,e):
    # Complex reciprocal and integration by parts, rather than the source's
    # expanded real denominator formulas. Both negative frequencies kept.
    result={}
    for k in range(-2,3):
        z=C(b,-k*pi)
        zeroth=C(1-e)/z
        first=(zeroth-C(2*e))/z
        result[k]=(zeroth,first)
    return result


def laplace(coeff,basis):
    total=C()
    for k in range(-2,3):
        total += coeff[k][0]*basis[k][0]+coeff[k][1]*basis[k][1]
    return total.r


copy=OUT/SOURCE.name
copy.write_bytes(SOURCE.read_bytes())
with localcontext() as ambient, redirect_stdout(io.StringIO()) as replay_log:
    ambient.prec=7
    replay_namespace=runpy.run_path(str(copy),run_name='__main__')
(OUT/'replay.txt').write_text(replay_log.getvalue())
replayed=json.loads(copy.with_suffix('.json').read_text())
check('unchanged_replay_all_fields',replayed == saved)
check('source_hash',source_hash == saved['script_sha256'])
check('saved_checks',len(saved['checks']) == 7 and all(saved['checks'].values()))
check('saved_failures',saved['failures'] == [])
check('parameters',saved['parameters'] == {'K':8192,'precision':60,'half_width':1,
                                        'energy_cap':'1/250','center':'43/100'})
context_info={}
for name in ('LO','HI'):
    ctx=replay_namespace[name]
    context_info[name]={'precision':ctx.prec,'Emin':ctx.Emin,'Emax':ctx.Emax,
                       'rounding':ctx.rounding,
                       'flags':{k.__name__:v for k,v in ctx.flags.items()}}
    check('context/'+name+'/range',ctx.Emin == -999999 and ctx.Emax == 999999)
    for flag in (decimal_module.InvalidOperation,decimal_module.DivisionByZero,
                 decimal_module.Overflow,decimal_module.Underflow,decimal_module.Subnormal,
                 decimal_module.Clamped):
        check('context/'+name+'/'+flag.__name__,not ctx.flags[flag])

pi=16*atan(5)-4*atan(239)
enclosure('constants/pi',pi)
s1={1:C(0,F(-1,2)),-1:C(0,F(1,2))}
s2={2:C(0,F(-1,2)),-2:C(0,F(1,2))}
g1={0:C(-1),1:C(F(-1,2)),-1:C(F(-1,2))}
g2={0:C(F(1,2)),2:C(F(-1,4)),-2:C(F(-1,4))}
pairs=[('A12',s1,s2,F(0),F(2)),('A22',s2,s2,F(1),F(4)),
       ('B11',g1,g1,F(3),F(1)),('B12',g1,g2,F(-1),F(1)),
       ('B22',g2,g2,F(3,4),F(1))]
ref=symmetric_cross(s1,s1)
relative={}
for name,u,v,h,d in pairs:
    coeff=symmetric_cross(u,v)
    coeff={k:[coeff[k][j]-h*ref[k][j] for j in (0,1)] for k in coeff}
    relative[name]=coeff
    path='entries/'+name
    enclosure(path+'/metric',R(h))
    enclosure(path+'/derivative_product_over_pi2',R(d))
    for k,uv in coeff.items():
        for j,z in enumerate(uv):
            for part in ('real','imag'):
                enclosure(f'{path}/relative_correlation_coefficients/{k}/{j}/{part}',
                          z.r if part == 'real' else z.i)

partial={name:R(0) for name,*_ in pairs}
check('complete_series_rows',len(saved['series_terms']) == 8192)
small_exp=F(1,10**150)
for j in range(8192):
    b=F(4*j+1,2)
    path=f'series_terms/{j}'
    check(path+'/index',saved['series_terms'][j]['j'] == j)
    enclosure(path+'/b',R(b))
    # Verify each tiny exponential directly as Decimal, avoiding 14000-digit
    # rational denominators. For integration, [0,10^-150] is enough once
    # the separately enclosed upper exponential is below this threshold.
    arg=Decimal(-4*j-1)
    el=LOW.next_minus(LOW.exp(arg)); eh=HIGH.next_plus(HIGH.exp(arg))
    original=saved['series_terms'][j]['exp_minus_2b']
    ep=path+'/exp_minus_2b'; checked_intervals.add(ep)
    check(ep,Decimal(original[0]) <= el <= eh <= Decimal(original[1]),[str(el),str(eh)])
    if eh < Decimal('1e-150'):
        e=R(0,small_exp)
    else:
        e=R(F(el),F(eh))
    basis=moment_basis(b,e)
    for name,*_ in pairs:
        value=laplace(relative[name],basis)
        enclosure(path+'/relative_laplace/'+name,value)
        partial[name]+=value

b=F(32769,2)
r3=b**(-3)+b**(-2)/4
enclosure('analytic_tail/B',R(b)); enclosure('analytic_tail/R3',R(r3))
sh=(transc(F(1,2),'exp')-transc(F(-1,2),'exp'))/2
# Independently integrated real sine/constant/cosine formulas at both poles.
den1=pi*pi+F(1,4); den2=4*pi*pi+F(1,4)
s1pole=2*pi*sh/den1; s2pole=-4*pi*sh/den2
g1pole=-4*sh+sh/den1; g2pole=2*sh-sh/(2*den2)
poles={id(s1):[s1pole,-s1pole],id(s2):[s2pole,-s2pole],
       id(g1):[g1pole,g1pole],id(g2):[g2pole,g2pole]}
pole_ref=-2*s1pole*s1pole
enclosure('constants/pole_reference',pole_ref)
trigs={}; trig_evidence=[]
for n,p in [(2,2),(3,3),(4,2),(5,5),(7,7)]:
    delay=transc(n,'ln'); weight=transc(p,'ln')/transc(n,'sqrt')
    values={}
    for k in (1,2):
        x=k*pi*delay
        sn,cs,se,ce=trig(x)
        values[k]=(sn,cs)
        trig_evidence.append({'n':n,'k':k,'argument':display(x),
                             'sine_tail':display(se),'cosine_tail':display(ce)})
    trigs[n]=(delay,weight,values)

entries={}; components={}
for name,u,v,h,d in pairs:
    path='entries/'+name
    radius=2*(d+abs(h))*pi*pi*r3
    enclosure(path+'/partial_laplace_sum',partial[name])
    enclosure(path+'/arch_tail_radius',radius)
    arch=-2*partial[name]+R(-radius.hi,radius.hi)
    fi,fj=poles[id(u)],poles[id(v)]
    pole=fi[0]*fj[1]+fj[0]*fi[1]-h*pole_ref
    for which,vals in [('i',fi),('j',fj)]:
        for index,value in enumerate(vals): enclosure(f'{path}/poles_{which}/{index}',value)
    enclosure(path+'/relative_pole',pole)
    prime=R(0)
    check(path+'/complete_prime_rows',len(saved['entries'][name]['primes']) == 5)
    for index,(n,p) in enumerate([(2,2),(3,3),(4,2),(5,5),(7,7)]):
        delay,weight,tv=trigs[n]
        pp=f'{path}/primes/{index}'; row=saved['entries'][name]['primes'][index]
        check(pp+'/integers',row['n'] == n and row['p'] == p)
        check(pp+'/complete_trig_rows',len(row['trigonometry']) == 2)
        for k in (1,2):
            tt=pp+'/trigonometry/'+str(k-1); tr=row['trigonometry'][k-1]
            check(tt+'/frequency',tr['k'] == k)
            check(tt+'/integer_shift',type(tr['shift']) is int)
            arg=pi*(k*delay-2*tr['shift'])
            check(tt+'/reduction_bound',arg.absupper() < 4)
            for key,value in [('argument',arg),('sin',tv[k][0]),('cos',tv[k][1])]:
                enclosure(tt+'/'+key,value)
        total=C()
        for k,(constant,linear) in relative[name].items():
            if k == 0: oscillation=C(1)
            elif k > 0: oscillation=C(tv[k][1],tv[k][0])
            else: oscillation=C(tv[-k][1],-tv[-k][0])
            total += (constant+linear*C(delay))*oscillation
        cv=total.r
        term=-2*weight*cv; prime+=term
        for key,value in [('delay',delay),('weight',weight),('relative_correlation',cv),('term',term)]:
            enclosure(pp+'/'+key,value)
    entries[name]=arch+pole+prime
    for key,value in [('archimedean',arch),('relative_prime',prime),('entry',entries[name])]:
        enclosure(path+'/'+key,value)
    components[name]={'archimedean':display(arch),'pole':display(pole),
                      'prime':display(prime),'tail_radius':display(radius),'entry':display(entries[name])}
    check(path+'/tail_budget',radius.hi < F('1e-7'))

A12,A22,B11,B12,B22=(entries[k] for k in ['A12','A22','B11','B12','B22'])
q=[B11,2*B12-6*A12,B11+B22+4*A12-3*A22,
   2*B12-F(3,2)*A12+2*A22,B22-F(3,4)*A22]
a=[sum((-q[k])*comb(k,j)*F(43,100)**(k-j) for k in range(j,5)) for j in range(5)]
curvature=a[2]-a[3]*a[3]/(4*a[4])
floor=a[0]-a[1]*a[1]/(4*curvature)
for index,value in enumerate(q): enclosure('result/defect_numerator_coefficients/'+str(index),value)
for index,value in enumerate(a): enclosure('result/negative_numerator_centered_coefficients/'+str(index),value)
enclosure('result/square_completion_curvature',curvature)
enclosure('result/square_completion_floor',floor)
check('published_leading_bound',a[4].lo > F('0.01015845'))
check('published_curvature_bound',curvature.lo > F('0.02212839'))
check('published_floor_bound',floor.lo > F('0.00001114243') > 0)
check('projective_endpoint',q[4].hi < 0)
check('metric_positive_definite',3*F(3,4)-1 == F(5,4) > 0)
check('first_sine_eligible_import',F('0.00364123566126519') < F(1,250))
check('complete_prime_support',transc(7,'ln').hi < 2 < transc(8,'ln').lo)
coarse=[('-0.006188067','-0.006187992'),('0.011738308','0.011738493'),
        ('-0.007875443','-0.007875295'),('0.002390640','0.002390714'),
        ('-0.001354786','-0.001354721')]
for (name,value),(lo,hi) in zip(entries.items(),coarse):
    check('published_matrix/'+name,F(lo)<value.lo<=value.hi<F(hi))

# Verify exact polynomial identity of the displayed double square completion
# by coefficient algebra in the proof, and independently evaluate interval
# margins above. No direction sample is used.
def interval_paths(node,path=''):
    if isinstance(node,list) and len(node)==2 and all(isinstance(v,str) for v in node):
        try: Decimal(node[0]); Decimal(node[1])
        except decimal_module.InvalidOperation: return set()
        return {path}
    if isinstance(node,dict):
        return set().union(*(interval_paths(v,path+'/'+k if path else k) for k,v in node.items()))
    if isinstance(node,list):
        return set().union(*(interval_paths(v,path+'/'+str(i)) for i,v in enumerate(node)))
    return set()
all_intervals=interval_paths(saved)
check('all_saved_intervals_checked',all_intervals == checked_intervals,
      {'total':len(all_intervals),'checked':len(checked_intervals),
       'missing':sorted(all_intervals-checked_intervals),'extra':sorted(checked_intervals-all_intervals)})
check('source_unchanged',hashlib.sha256(SOURCE.read_bytes()).hexdigest()==source_hash)
check('saved_certificate_unchanged',hashlib.sha256(SAVED.read_bytes()).hexdigest()==saved_hash)
report={'task':'C759f conceptual and complete scalar audit; REPRODUCTION',
 'method':'100-digit integer-rounded Fraction intervals; 120-digit Decimal transcendental endpoints; direct bilinear correlations; full complex Laplace integrals; real pole formulas; unreduced 120-term trigonometry',
 'runtime':{'python':sys.version,'libmpdec':decimal_module.__libmpdec_version__,'contexts':context_info},
 'audit_script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'source_sha256':source_hash,'saved_certificate_sha256':saved_hash,
 'replay':'scripts/spectral-triples/audit-816/two-sine-primitive-814.json',
 'series_rows_checked':8192,'prime_rows_checked':25,'saved_intervals_checked':len(checked_intervals),
 'check_count':len(checks),'checks':checks,'failures':failures,
 'independent_trigonometric_errors':trig_evidence,'components':components,
 'result':{'leading':display(a[4]),'curvature':display(curvature),'floor':display(floor),
           'required_floor':'0','projective_endpoint_coefficient':display(q[4]),'audit_pass':not failures},
 'limitations':['Analytic audit is canonical in C759f; no infinite-domain comparison.',
               'C759d supplies the independently audited eligible first sine.',
               'Python integer and Decimal/libmpdec correctness remain trusted.',
               'No parity-infimum, ground-state, other-window or Xi conclusion.']}
path=BASE/'two-sine-primitive-audit-816.json'
path.write_text(json.dumps(report,indent=2)+'\n')
print('Complete audit:',len(checks),'checks;',len(checked_intervals),'intervals; failures:',failures)
print('Leading:',display(a[4]),'; required >0')
print('Curvature:',display(curvature),'; required >0')
print('Floor:',display(floor),'; required >0')
print('Certificate:',path.relative_to(BASE.parent.parent))
if failures: raise SystemExit(1)
