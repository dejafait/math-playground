#!/usr/bin/env python3
"""Independent rational-endpoint replay of C998f; never imports generator667.

All quantization uses Fraction floor/ceil, rather than its integer endpoint
primitives. Analytic applicability and the scalar template audit are in C998f.
"""
from fractions import Fraction as F
from math import comb, isqrt
from collections import Counter
from hashlib import sha256
from pathlib import Path
import json
import numpy as np

B = Path(__file__).resolve().parent
S = 2**128
counts = Counter()
checks, pins = [], {}
endpoint_max_bits = 0

def ck(name, value):
    checks.append(dict(name=name, passed=bool(value)))

def read(name):
    raw = (B/name).read_bytes()
    pins[name] = sha256(raw).hexdigest()
    return json.loads(raw)

def rat(q):
    return F(int(q['numerator']), int(q['denominator']))

def down(x):
    return (x*S).__floor__()

def up(x):
    return (x*S).__ceil__()

class Box:
    def __init__(self, a, b=None):
        global endpoint_max_bits
        b = a if b is None else b
        low, high = down(a), up(b)
        endpoint_max_bits = max(endpoint_max_bits, abs(low).bit_length(), abs(high).bit_length())
        self.a, self.b = F(low, S), F(high, S)
        assert self.a <= self.b

    @classmethod
    def literal(cls, a, b=1):
        counts['rational_conversion'] += 1
        return cls(F(a, b))

    def __add__(self, other):
        counts['addition'] += 1
        return Box(self.a+other.a, self.b+other.b)

    def __sub__(self, other):
        counts['subtraction'] += 1
        return Box(self.a-other.b, self.b-other.a)

    def __neg__(self):
        counts['negation'] += 1
        return Box(-self.b, -self.a)

    def __mul__(self, other):
        counts['multiplication'] += 1
        v = [x*y for x in (self.a, self.b) for y in (other.a, other.b)]
        return Box(min(v), max(v))

    def __truediv__(self, other):
        counts['division'] += 1
        assert other.a > 0 or other.b < 0
        v = [x/y for x in (self.a, self.b) for y in (other.a, other.b)]
        return Box(min(v), max(v))

    def wide(self, error):
        counts['widening'] += 1
        radius = F(up(error), S)
        return Box(self.a-radius, self.b+radius)

    def endpoints(self):
        return [int(self.a*S), int(self.b*S)]

    def center(self):
        return down((self.a+self.b)/2)

    def radius_units(self):
        return up((self.b-self.a)/2)

old = read('higher-order-diagonal-667.json')
data = read('jump-log-h1-bounds-654.json')
prior_audit = read('jump-log-h1-audit-655.json')
archive = B/'frozen-reference-proposal-652.npz'
pins[archive.name] = sha256(archive.read_bytes()).hexdigest()
ck('all667 input pins match current bytes', all(pins[k] == v for k,v in old['input_sha256'].items()))
ck('frozen archive specified SHA256', pins[archive.name] == '2b770a8a689a972ae487b9dd718e2e6d47b6769a5530e7fec244a102c5c317c6')
ck('655 pins complete654, no failures', prior_audit['input_sha256']['jump-log-h1-bounds-654.json'] == pins['jump-log-h1-bounds-654.json'] and not prior_audit['failures'])
ck('667 generator pin', sha256((B/'higher-order-diagonal-667.py').read_bytes()).hexdigest() == old['script_sha256'])
one, two, zero = Box.literal(1), Box.literal(2), Box.literal(0)
odd = [Box.literal(1, 2*j+1) for j in range(100)]

def poly(t):
    square = t*t
    acc = odd[99]
    for j in reversed(range(99)):
        acc = acc*square+odd[j]
    return two*t*acc

def atan(d):
    x = Box.literal(1,d)
    square = -(x*x)
    acc = odd[99]
    for j in reversed(range(99)):
        acc = acc*square+odd[j]
    return (x*acc).wide(F(1,201*d**201))

pi = Box.literal(16)*atan(5)-Box.literal(4)*atan(239)
ln2 = poly(Box.literal(1,3)).wide(F(1,2**190))
ln3 = poly(Box.literal(1,2)).wide(F(1,2**190))
ell = ln3/two
reductions = []

def logbox(x):
    m = 0
    while x.b > 2:
        counts['range_reduction_iteration'] += 1
        x = x/two
        m += 1
    assert F(1,2) <= x.a <= x.b <= 2
    reductions.append(m)
    t = (x-one)/(x+one)
    return poly(t).wide(F(1,2**190))+Box.literal(m)*ln2

logpi = logbox(pi)
# Independently form the exact Bernoulli numbers by binomial recurrence.
bern = [F(1)]
for m in range(1,17):
    bern.append(-sum((comb(m+1,j)*bern[j] for j in range(m)),F())/(m+1))
ck('all17 Bernoulli values', bern == [rat(q) for q in old['analytic']['exact_Bernoulli_numbers_B0_to_B16']])
coeff = [Box.literal((bern[2*j]/(2*j)).numerator,(bern[2*j]/(2*j)).denominator) for j in range(1,8)]
A = 512*abs(bern[16])/(16*F(65,4)**16)
ck('exact analytic bound and target', A == rat(old['analytic']['uniform_bound']) and A < F(1,2**45))
ck('worst elementary log tail', F(2,201)*F(1,2)**201/(1-F(1,4)) < F(1,2**190))

def product(a,b):
    return a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0]

ks, hs, mode_rows = [], [], []
for n in range(256):
    k = Box.literal(n)*pi/ell
    ks.append(k)
    y = k/two
    x = Box.literal(65,4)
    norm = x*x+y*y
    inv = x/norm, -(y/norm)
    inv2 = product(inv,inv)
    power, total = inv2, zero
    for j in range(7):
        total = total+coeff[j]*power[0]
        if j != 6:
            power = product(power,inv2)
    v = logbox(norm)/two-inv[0]/two-total
    for j in range(16):
        a = Box.literal(4*j+1,4)
        v = v-a/(a*a+y*y)
    v = v-logpi
    hs.append(v)
    saved = old['modes'][n]
    r = F(v.radius_units(),S)
    ck(f'mode{n}: all endpoints/center/radii and tolerance', saved['n'] == n and v.endpoints() == saved['numerical_interval_endpoints_over_S'] and v.center() == saved['h_center_numerator_over_S'] and r == rat(saved['nonanalytic_error']) and A == rat(saved['analytic_error_upper']) and A+r == rat(saved['total_error_upper']) and r <= F(1,2**47))
    mode_rows.append(dict(n=n,endpoints=v.endpoints(),center=v.center(),radius_units=v.radius_units()))

# isqrt is for independent verification, not an operation charged to667.
root = isqrt(2*S*S)
sqrt2 = Box(F(root,S),F(root+1,S))
counts['sqrt_bisection_iteration'] = 129
ck('sqrt2 endpoints exact and bracketed', sqrt2.endpoints() == old['arithmetic']['sqrt2_interval_over_S'] and root*root < 2*S*S < (root+1)**2)
quarter = Box.literal(1,4)
ratios = []
for n in range(2,256):
    p = n%2
    v = (quarter+ks[p]*ks[p])/(quarter+ks[n]*ks[n])
    ratios.append(sqrt2*v if p == 0 else v)
    ck(f'completion ratio{n} strict bounds', 0 < ratios[-1].a <= ratios[-1].b < 1)
with np.load(archive,allow_pickle=False) as archive_data:
    raw = archive_data['free_middle_dyadics'].copy()
ck('input dtype/shape',raw.dtype == np.dtype('float64') and raw.shape == (254,3))
ar = Box.literal(A.numerator,A.denominator)
columns = []
for j in range(3):
    q = [zero,zero]
    free = []
    for n in range(2,256):
        f = F.from_float(float(raw[n-2,j]))
        v = Box.literal(f.numerator,f.denominator)
        ck(f'column{j} free{n} exact654 and grid',f == rat(data['exact_free_middle_columns'][j][n-2]) and v.a == f == v.b)
        free.append(v)
        q[n%2] = q[n%2]-ratios[n-2]*v
    q += free
    d = [hs[n]*q[n] for n in range(256)]
    radii = []
    for n in range(256):
        counts['Dq_error_radius_assembly'] += 1
        amp = Box(F(),max(abs(q[n].a),abs(q[n].b)))
        radius = F(d[n].radius_units(),S)+(ar*amp).b
        radii.append(radius)
        saved = old['Dq_columns'][j]
        ck(f'Dq{j},{n}: q/output interval/center/total radius',q[n].endpoints() == saved['completed_q_intervals_over_S'][n] and d[n].endpoints() == saved['Dq_numeric_intervals_over_S'][n] and d[n].center() == saved['Dq_centers_over_S'][n] and radius == rat(saved['Dq_total_error_radii'][n]))
    columns.append(dict(column=j,q=[v.endpoints() for v in q],Dq=[v.endpoints() for v in d],centers=[v.center() for v in d],radius_units=[int(r*S) for r in radii]))

# Independent ledger for explicit reduced rational triangle; no Fraction
# routine is counted as one arithmetic operation in the audited algorithm.
euclid_steps = reductions_count = triangles = 0
bern_register_bits = 0
def reduce_pair(a,b):
    global euclid_steps, reductions_count, bern_register_bits
    bern_register_bits = max(bern_register_bits,abs(a).bit_length(),b.bit_length())
    reductions_count += 1
    x,y = abs(a),b
    while y:
        x,y = y,x%y
        euclid_steps += 1
    return a//x,b//x
pairs = [(1,1)]
for m in range(1,17):
    aa,bb = 0,1
    for j in range(m):
        num,den = pairs[j]
        aa,bb = reduce_pair(aa*den+comb(m+1,j)*num*bb,bb*den)
        triangles += 1
    pairs.append(reduce_pair(-aa,bb*(m+1)))
for j in range(1,8):
    reduce_pair(pairs[2*j][0],pairs[2*j][1]*(2*j))
bern_work = 64*(reductions_count+triangles)+8*euclid_steps
work = 64*sum(counts.values())+bern_work+1000000
ck('every template count and exact total',dict(counts) == old['work']['interval_calls_by_kind'] and sum(counts.values()) == old['work']['interval_calls'])
ck('Bernoulli work independently counted',bern_work == old['work']['Bernoulli_generation_upper'])
ck('complete claimed upper and target',work == old['work']['complete_setup_upper'] == 8161000 and work < 10000000)
ck('all arithmetic constants',all(v.endpoints() == old['arithmetic'][key] for v,key in [(pi,'pi_interval_over_S'),(ell,'ell_interval_over_S'),(logpi,'logpi_interval_over_S')]))
max_units = max(v.radius_units() for v in hs)
ck('maximum radius102 ulps',max_units == 102 and F(max_units,S) == rat(old['arithmetic']['max_nonanalytic_error']))
ck('saved checks complete and passing',len(old['checks']) == 1282 and all(q['pass'] for q in old['checks']) and not old['failures'])
endpoint_bits = max(abs(x).bit_length() for row in mode_rows for x in row['endpoints'])
ck('interval endpoints below160bits',endpoint_max_bits < 160)
ck('Bernoulli reduced-call arguments below160bits',bern_register_bits < 160)
ck('largest exact atan-tail denominator1596bits',(201*239**201).bit_length() == 1596)
failures = [v['name'] for v in checks if not v['passed']]
report = dict(result='PASS' if not failures else 'FAIL',checks=checks,failures=failures,input_sha256=pins,script_sha256=sha256(Path(__file__).read_bytes()).hexdigest(),analytic_bound=dict(numerator=str(A.numerator),denominator=str(A.denominator)),max_radius_units=max_units,fractional_bits=128,modes=mode_rows,columns=columns,work=dict(counts=counts,Bernoulli_reductions=reductions_count,Bernoulli_Euclid_steps=euclid_steps,Bernoulli_triangle_steps=triangles,Bernoulli_upper=bern_work,complete_upper=work,required_upper=10000000,range_reduction_max=max(reductions)),scope='Independent finite arithmetic replay. Analytic inclusion, template expansion and register bounds require canonical prose audit; no residual Gram or signed S3 verified.',diagonal_endpoint_bits=endpoint_bits)
report['registers'] = dict(all_interval_endpoint_bits=endpoint_max_bits,Bernoulli_argument_bits=bern_register_bits,atan_tail_denominator_bits=1596,proved_work_register_bound=2048,required_cap=16384)
out = B/'higher-order-diagonal-audit-669.json'
out.write_text(json.dumps(report,indent=2)+'\n')
print(f"result={report['result']} checks={len(checks)} failures={failures}")
print(f'analytic={float(A):.9g} required<={2**-45:.9g}; arithmetic={max_units}/2^128 required<=2^-47')
print(f'complete setup upper={work} required<=10000000; certificate={out.relative_to(B.parent.parent)}')
if failures:
    raise SystemExit(1)
