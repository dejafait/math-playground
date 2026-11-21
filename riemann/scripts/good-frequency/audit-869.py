"""Independent rational inspection and alternate enclosure of C750b.

Reads the complete867 certificate without executing/importing its producer.
Fraction arithmetic checks every record. A192-bit, different-series,
shift512 computation supplies an independent enclosing scalar evaluation.
"""
from fractions import Fraction as F
from math import factorial, isqrt
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / 'exterior-delay-certificate-867.json'
raw = SOURCE.read_bytes()
old = json.loads(raw)
checks, failures = [], []


def check(name, condition):
    checks.append({'check': name, 'pass': bool(condition)})
    if not condition:
        failures.append(name)


def floor(x):
    return x.numerator // x.denominator


def ceil(x):
    return -floor(-x)


class Box:
    """Fraction endpoints rounded after each operation, no producer code."""
    bits = 128

    def __init__(self, lo, hi=None):
        lo, hi = F(lo), F(lo if hi is None else hi)
        assert lo <= hi
        scale = 2**self.bits
        self.lo, self.hi = F(floor(lo*scale), scale), F(ceil(hi*scale), scale)

    def __add__(self, other):
        return Box(self.lo+other.lo, self.hi+other.hi)

    def __neg__(self):
        return Box(-self.hi, -self.lo)

    def __sub__(self, other):
        return self + (-other)

    def __mul__(self, other):
        ends = [x*y for x in (self.lo, self.hi) for y in (other.lo, other.hi)]
        return Box(min(ends), max(ends))

    def __truediv__(self, other):
        assert other.lo > 0 or other.hi < 0
        if other.hi < 0:
            return (-self)/(-other)
        return self * Box(1/other.hi, 1/other.lo)

    def square(self):
        return Box(0 if self.lo <= 0 <= self.hi else min(self.lo**2, self.hi**2),
                   max(self.lo**2, self.hi**2))

    def sqrt(self):
        assert self.lo >= 0
        scale = 2**self.bits
        # Bounds obtained directly from rational radicands, then checked.
        l = isqrt(floor(self.lo*scale**2))
        u = isqrt(ceil(self.hi*scale**2))
        if F(u*u, scale**2) < self.hi:
            u += 1
        assert F(l*l, scale**2) <= self.lo <= self.hi <= F(u*u, scale**2)
        return Box(F(l, scale), F(u, scale))

    def power(self, n):
        out = Box(1)
        for _ in range(n):
            out = out*self
        return out

    def widen(self, radius):
        assert radius.lo >= 0
        return Box(self.lo-radius.hi, self.hi+radius.hi)

    def record(self):
        scale = 2**self.bits
        return {'denominator': str(scale),
                'numerators': [str(int(self.lo*scale)), str(int(self.hi*scale))]}


def q(n, d=1):
    return Box(F(n, d))


def stored(rec):
    return tuple(F(int(n), 2**128) for n in rec['dyadic_numerators'])


def exact(name, box, rec):
    check(name, (box.lo, box.hi) == stored(rec))
    # Check the complete displayed decimal enclosure as an exact rational.
    a, b = map(F, rec['decimal_enclosure'])
    l, u = stored(rec)
    check(name+' decimal', a <= l <= u <= b)


domain = {'log_unit_calls': 0, 'cosine_calls': 0, 'atan_calls': 0,
          'max_abs_log_series_argument_numerator': 0,
          'max_abs_cosine_argument_numerator': 0,
          'max_abs_atan_argument_numerator': 0}


def note(kind, x, bound):
    a = max(abs(x.lo), abs(x.hi))
    assert a <= bound
    key = {'log': 'log_unit_calls', 'cosine': 'cosine_calls', 'atan': 'atan_calls'}[kind]
    domain[key] += 1
    key = {'log': 'max_abs_log_series_argument_numerator',
           'cosine': 'max_abs_cosine_argument_numerator',
           'atan': 'max_abs_atan_argument_numerator'}[kind]
    domain[key] = max(domain[key], int(a*2**Box.bits))


def logbase(x, alternate=False):
    assert 1 <= x.lo <= x.hi <= 2
    v = (x-q(1))/(x+q(1))
    note('log', v, F(1, 2))
    count = 100 if alternate else 80
    if alternate:
        total = q(0)
        for j in range(count):
            total = total+v.power(2*j+1)/q(2*j+1)
    else:
        term, total = v, q(0)
        v2 = v.square()
        for j in range(count):
            total = total+term/q(2*j+1)
            term = term*v2
    tail = F(2)*F(1, 2)**(2*count+1)/((2*count+1)*(1-F(1, 4)))
    bound = F(1, 2**(200 if alternate else 160))
    assert tail < bound
    return (q(2)*total).widen(Box(bound))


def log(x, log2, alternate=False):
    def endpoint(value):
        # Exact rational comparisons select the scaling independently.
        e, r = 0, value
        while r < 1:
            e, r = e-1, r*2
        while r >= 2:
            e, r = e+1, r/2
        return logbase(Box(r), alternate)+q(e)*log2
    return Box(endpoint(x.lo).lo, endpoint(x.hi).hi)


def atan(x, alternate=False):
    note('atan', x, F(1, 4))
    count = 80 if alternate else 64
    total, term, x2 = q(0), x, x.square()
    for j in range(count):
        if alternate:
            v = x.power(2*j+1)/q(2*j+1)
        else:
            v = term/q(2*j+1)
            term = term*x2
        total = total+(v if j % 2 == 0 else -v)
    bound = F(1, 2**(320 if alternate else 256))
    assert F(1, 4)**(2*count+1)/(2*count+1) < bound
    return total.widen(Box(bound))


def cos(x, alternate=False):
    note('cosine', x, 4)
    if alternate:
        total = q(0)
        for j in range(41):
            term = x.power(2*j)/q(factorial(2*j))
            total = total+(term if j % 2 == 0 else -term)
        assert F(4**82, factorial(82)) < F(1, 2**220)
        return total.widen(q(1, 2**220))
    term, total, x2 = q(1), q(1), x.square()
    for j in range(1, 33):
        term = -(term*x2)/q((2*j-1)*2*j)
        total = total+term
    assert F(4**66, factorial(66)) < F(1, 2**150)
    return total.widen(q(1, 2**150))


# Independent integer factorization: classify every integer in [2,80].
pps = []
for n in range(2, 81):
    ds = [d for d in range(2, n+1) if n % d == 0]
    p, residual = ds[0], n
    while residual % p == 0:
        residual //= p
    if residual == 1:
        pps.append((n, p))
check('exact31 prime powers', len(pps) == 31 and pps == [
    (r['n'], r['prime']) for r in old['prime_powers']])


def compute(alternate):
    log2 = logbase(q(2), alternate)
    pi = q(16)*atan(q(1, 5), alternate)-q(4)*atan(q(1, 239), alternate)
    T = q(4)*log(q(3), log2, alternate)
    logpi = log(pi, log2, alternate)
    if not alternate:
        for name, val in [('pi', pi), ('log2', log2), ('T', T)]:
            exact('constant '+name, val, old['constants'][name])
    weights = []
    for i, (n, p) in enumerate(pps):
        weight = log(q(p), log2, alternate)/q(n).sqrt()
        delay = log(q(n), log2, alternate)
        if not alternate:
            exact(f'weight {n}', weight, old['prime_powers'][i]['weight'])
            exact(f'log {n}', delay, old['prime_powers'][i]['log_n'])
        weights.append((weight, delay))
    nodes, total = [], q(0)
    for j, rec in enumerate(old['nodes']):
        t = q(2*j)*pi/(q(9)*T)
        den = q(F(1, 4)+(512 if alternate else 256)).square()+(t/q(2)).square()
        a = q(F(1, 4)+(512 if alternate else 256))
        main = log(den, log2, alternate)/q(2)-a/(q(2)*den)-logpi
        recurrence = q(0)
        if not alternate:
            check(f'node{j} index/multiplicity/shift', rec['j'] == j and
                  rec['multiplicity'] == (1 if j == 0 else 2) and
                  rec['archimedean']['shift'] == 256 and
                  len(rec['archimedean']['recurrence_terms']) == 256)
            exact(f'node{j} t', t, rec['t'])
            exact(f'node{j} norm2', den, rec['archimedean']['squared_modulus'])
            exact(f'node{j} main', main, rec['archimedean']['shifted_main_minus_logpi'])
        for r in range(512 if alternate else 256):
            x = q(4*r+1, 4)
            term = x/(x.square()+(t/q(2)).square())
            recurrence = recurrence+term
            if not alternate:
                exact(f'node{j} recurrence{r}', term, rec['archimedean']['recurrence_terms'][r])
        error = q(1)/(q(4)*den)
        m = (main-recurrence).widen(error)
        arithmetic = q(0)
        for i, ((n, p), (weight, delay)) in enumerate(zip(pps, weights)):
            angle = t*delay
            cosine = cos(angle, alternate)
            term = q(2)*weight*cosine
            arithmetic = arithmetic+term
            if not alternate:
                v = rec['arithmetic_terms'][i]
                check(f'node{j} prime{n}', v['n'] == n and v['prime'] == p)
                for label, value in [('angle', angle), ('cosine', cosine), ('complete_term', term)]:
                    exact(f'node{j} prime{n} '+label, value, v[label])
        w = m-arithmetic
        factor = (t.square()+q(1, 4)).square()
        h = factor*w
        if not alternate:
            check(f'node{j}31 terms', len(rec['arithmetic_terms']) == 31)
            for label, value in [('recurrence_sum', recurrence),
                                 ('absolute_remainder_bound', error), ('m', m)]:
                exact(f'node{j} '+label, value, rec['archimedean'][label])
            for label, value in [('arithmetic_sum', arithmetic), ('w', w),
                                 ('primitive_factor', factor), ('h', h)]:
                exact(f'node{j} '+label, value, rec[label])
        else:
            # Alternate enclosure must fit strictly inside the original
            # digamma-error dominated final interval, not merely overlap it.
            l, u = stored(rec['h'])
            check(f'alternate node{j} strict containment', l < h.lo <= h.hi < u)
        nodes.append({'j': j, 't': t.record(), 'm': m.record(),
                      'arithmetic': arithmetic.record(), 'h': h.record(),
                      'recurrence_count': 512 if alternate else 256})
        total = total+q(1 if j == 0 else 2)*h
    return total/q(9), nodes


check('five complete nodes', len(old['nodes']) == 5)
check('certificate arithmetic metadata', old['arithmetic'] == {
    'bits': 128, 'common_denominator': str(2**128),
    'log_terms': 80, 'log_tail_bound': '2^-160',
    'atan_terms': 64, 'atan_tail_bound': '2^-256',
    'cos_terms': 33, 'cos_tail_bound': '2^-150',
    'floating_point_used_for_decisions': False})
mean, _ = compute(False)
exact('full mean', mean, old['result']['nine_point_mean'])
check('all original domain records', all(int(old['domains'][k]) == v for k, v in domain.items()))
original_domain = domain.copy()
check('reported original result', old['result']['failures'] == [] and
      old['result']['cosine_moments'] == [0]*8 and
      old['result']['positive_functional_mass'] == '1' and
      old['result']['required_strict_upper'] == '-49/50' and
      old['status'] == 'CERTIFIED_FIXED_FAMILY_INFEASIBLE')
check('original strict threshold', mean.hi < F(-49, 50))

# Independent polynomial product check, rather than long division.
check('eight annihilation records', len(old['annihilation']) == 8)
for k, rec in enumerate(old['annihilation'], 1):
    coeff = [0]*9
    for j in range(9):
        coeff[(k*j) % 9] += 1
    quotient = [3, 0, 0] if k in (3, 6) else [1, 1, 1]
    product = [sum(quotient[d-e] for e in (0, 3, 6) if 0 <= d-e < 3)
               for d in range(9)]
    check(f'exact cancellation k{k}', coeff == product == rec['phase_polynomial'] and
          rec['k'] == k and rec['quotient_by_Phi9'] == quotient and rec['remainder'] == [0]*9)

# Alternate independent enclosure: different precision, polynomial assembly,
# more terms, different recurrence shift. The same cited analytic theorem
# is used; this does not purport to be independent special-function theory.
Box.bits = 192
altmean, altnodes = compute(True)
check('alternate mean strictly nested', mean.lo < altmean.lo <= altmean.hi < mean.hi)
check('alternate strict threshold', altmean.hi < F(-49, 50))
table_lower = [F(s) for s in ['-2.254364', '-2.407616', '-2.526847', '-1.390252', '2.999439']]
table_upper = [F(s) for s in ['-2.254363', '-2.407614', '-2.526845', '-1.390249', '2.999443']]
for j, rec in enumerate(old['nodes']):
    l, u = stored(rec['h'])
    check(f'published table node{j}', table_lower[j] < l <= u < table_upper[j])
    t_bounds = [('0', '0'), ('0.158866714854', '0.158866714855'),
                ('0.317733429708', '0.317733429709'),
                ('0.476600144563', '0.476600144564'),
                ('0.635466859417', '0.635466859418')]
    tl, tu = stored(rec['t'])
    left, right = map(F, t_bounds[j])
    check(f'published node{j} position', left <= tl <= tu <= right)
tablemean = (table_upper[0]+2*sum(table_upper[1:]))/9
check('table exact rational comparison', tablemean == F(-8904893, 9000000) < F(-49, 50))

out = ROOT/'audit-869.json'
report = {'input': SOURCE.name, 'input_sha256': hashlib.sha256(raw).hexdigest(),
          'method': 'Independent Fraction enclosure; complete128-bit record check; alternate192-bit shift512',
          'checks': checks, 'failures': failures,
          'coverage': {'prime_powers': len(pps), 'arithmetic_terms': 155,
                       'original_recurrence_terms': 1280, 'moments': 8,
                       'original_domains': original_domain},
          'original_mean': old['result']['nine_point_mean'],
          'alternate': {'mean': altmean.record(), 'nodes': altnodes,
                        'bits': 192, 'shift': 512, 'log_terms': 100,
                        'atan_terms': 80, 'cosine_degree': 80,
                        'log_tail': '2^-200', 'atan_tail': '2^-320', 'cosine_tail': '2^-220'},
          'required_upper': '-49/50',
          'threshold_margin_lower_bound': str(F(-49, 50)-mean.hi),
          'verdict': 'PASS_FIXED_FAMILY_ONLY' if not failures else 'FAILED'}
out.write_text(json.dumps(report, indent=2)+'\n')
print(f'{report["verdict"]}: {len(checks)} checks; failures={failures}')
print(f'Original mean={old["result"]["nine_point_mean"]["decimal_enclosure"]}; required upper<-49/50.')
print(f'Full evidence: {out}')
if failures:
    raise SystemExit(1)
