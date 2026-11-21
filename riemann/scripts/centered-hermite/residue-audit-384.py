#!/usr/bin/env python3
"""Audit/replay L764; preserve the original script and step382 certificate.

Run from the notebook root: python3 scripts/centered-hermite/residue-audit-384.py
The exact original program is executed in two pieces at its definition/data
boundary, with context and interval-constructor observation installed between
them. Observers do not change an arithmetic operation or its rounding mode.
"""
import decimal
import hashlib
import json
import platform
import sys
from collections import Counter
from fractions import Fraction as F
from math import comb, factorial
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / 'residue-moment-382.py'
ORIGINAL = HERE / 'residue-moment-382.json'
REPLAY_DIR = HERE / 'replay-384'
REPORT = HERE / 'residue-audit-384.json'
REPLAY_DIR.mkdir(exist_ok=True)
source_bytes = SOURCE.read_bytes()
original_bytes = ORIGINAL.read_bytes()
source = source_bytes.decode()
boundary = 'alo,ahi=atan_bounds(5,50)'
assert source.count(boundary) == 1
definitions, calculations = source.split(boundary)
namespace = {'__name__': '__main__',
             '__file__': str(REPLAY_DIR / SOURCE.name)}
exec(compile(definitions, str(SOURCE), 'exec'), namespace)

contexts = Counter()
signals = Counter()
intervals = 0
min_adjusted = None
max_adjusted = None
original_localcontext = namespace['localcontext']
original_init = namespace['I'].__init__
initial_context = str(decimal.getcontext())

class ObservedContext:
    def __enter__(self):
        self.manager = original_localcontext()
        self.context = self.manager.__enter__()
        return self.context

    def __exit__(self, typ, value, traceback):
        ctx = self.context
        contexts[(ctx.prec, ctx.rounding, ctx.Emin, ctx.Emax, ctx.clamp)] += 1
        signals.update(signal.__name__ for signal, active in ctx.flags.items() if active)
        return self.manager.__exit__(typ, value, traceback)

def observed_init(self, lo, hi=None):
    global intervals, min_adjusted, max_adjusted
    original_init(self, lo, hi)
    intervals += 1
    for value in (self.lo, self.hi):
        assert value.is_finite(), 'Nonfinite interval endpoint'
        if value:
            exponent = value.adjusted()
            min_adjusted = exponent if min_adjusted is None else min(min_adjusted, exponent)
            max_adjusted = exponent if max_adjusted is None else max(max_adjusted, exponent)

namespace['localcontext'] = ObservedContext
namespace['I'].__init__ = observed_init
exec(compile(boundary + calculations, str(SOURCE), 'exec'), namespace)
replay_path = REPLAY_DIR / ORIGINAL.name
replay_bytes = replay_path.read_bytes()
cert = json.loads(replay_bytes)

# Independent exact symbolic division: polynomials in d, with the a and b
# factors separated. This checks identities, not a finite sample of degrees.
def add(*polys):
    out = [F(0)] * max(map(len, polys))
    for p in polys:
        for k, value in enumerate(p):
            out[k] += value
    while len(out) > 1 and not out[-1]:
        out.pop()
    return out

def scale(p, s):
    return [F(s) * value for value in p]

def mul(p, q):
    out = [F(0)] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i+j] += a*b
    return out

def factors(*roots):
    out = [F(1)]
    for root in roots:
        out = mul(out, [-F(root), F(1)])
    return out

checks = {}
def equal(name, left, right):
    checks[name] = add(left, scale(right, -1)) == [F(0)]

h2 = scale(factors(1, 2), F(-1, 4))
h4 = scale(factors(1, 2, 3, 4), F(1, 32))
p2_b2 = scale(factors(0, 1), F(1, 8))
p2_constant = scale(factors(0, 1), F(-1, 4))
p4_b2 = scale(factors(0, 1, 2, 3), F(-1, 32))
p4_constant = scale(factors(0, 1, 2, 3), F(1, 32))
equal('A_constant', add(p2_constant, scale(h2, -1)), scale(factors(1), F(-1, 2)))
equal('C_b2_coefficient', add(p4_b2, scale(mul(p2_b2, h2), -1)),
      scale(factors(0, 1, 2), F(1, 16)))
equal('C_constant', add(p4_constant, scale(mul(p2_constant, h2), -1),
                        mul(h2, h2), scale(h4, -1)), scale(factors(1, 2), F(-1, 4)))

# Independently differentiating the monomial expansion gives these exact
# fourth-derivative polynomials; the canonical proof supplies the recurrence.
expected_polys = [
    {1: F(-12), 2: F(8)},
    {1: F(-30), 2: F(60), 3: F(-16)},
    {1: F(-75), 2: F(330), 3: F(-224), 4: F(32)},
    {1: F(-375, 2), 2: F(1635), 3: F(-2116), 4: F(720), 5: F(-64)},
    {1: F(-1875, 4), 2: F(15465, 2), 3: F(-17024),
     4: F(10352), 5: F(-2112), 6: F(128)},
]
checks['all_derivative_polynomials'] = cert['derivative_polynomials'] == [
    {str(k): str(v) for k, v in p.items()} for p in expected_polys]
norms = [sum((abs(v)*factorial(k) for k, v in p.items()), F(0)) for p in expected_polys]
exact_bounds = [12*sum((F(comb(4, s)*factorial(p), factorial(p-s))
                       * 2**(p-s)*norms[4-s] for s in range(min(p, 4)+1)), F(0))
                for p in range(0, 9, 2)]
checks['all_derivative_bounds'] = list(map(F, cert['derivative_bounds'])) == exact_bounds
exact_errors = [F(2, 180)*F(2, 65536)**4*bound for bound in exact_bounds]
checks['all_simpson_enclosures'] = all(F(pair[0]) <= error <= F(pair[1])
                                      for pair, error in zip(cert['simpson_errors'], exact_errors))
checks['simpson_error_upper'] = max(exact_errors) < F('4.895e-11')

# Re-evaluate coefficient cancellation independently with Fraction intervals,
# starting from the stored moments, not the already-centered Decimal output.
def qadd(a, b):
    return a[0]+b[0], a[1]+b[1]

def qneg(a):
    return -a[1], -a[0]

def qmul(a, b):
    values = [x*y for x in a for y in b]
    return min(values), max(values)

def qscale(a, s):
    return qmul(a, (F(s), F(s)))

def qpower(a, n):
    result = (F(1), F(1))
    for _ in range(n):
        result = qmul(result, a)
    return result

moments = [tuple(map(F, pair)) for pair in cert['moments']]
inv_mass = (1/moments[0][1], 1/moments[0][0])
g = [qmul(qscale(m, F(factorial(j), factorial(2*j))), inv_mass)
     for j, m in enumerate(moments)]
g[0] = F(1), F(1)
c = g[1]
b2 = qadd(g[2], qneg(qpower(c, 2)))
b3 = qadd(qadd(g[3], qscale(qmul(c, g[2]), -3)), qscale(qpower(c, 3), 2))
b4 = qadd(qadd(qadd(g[4], qscale(qmul(c, g[3]), -4)),
               qscale(qmul(qpower(c, 2), g[2]), 6)), qscale(qpower(c, 4), -3))
checks['rational_gamma_inside_decimal'] = all(
    F(pair[0]) <= interval[0] <= interval[1] <= F(pair[1])
    for pair, interval in zip(cert['normalized_gamma'], g))
checks['rational_centered_inside_decimal'] = all(
    F(cert['centered'][name][0]) <= interval[0] <= interval[1] <= F(cert['centered'][name][1])
    for name, interval in [('b2', b2), ('b3', b3), ('b4', b4)])
checks['required_coefficient_bounds'] = (
    F('-0.000038') < b2[0] <= b2[1] < F('-0.000037')
    and F('1.6e-10') < b4[0] <= b4[1] < F('1.8e-10'))
beta, epsilon, threshold = F('0.000038'), F('0.00000000016'), F(12000000)
margin_coefficient = epsilon*threshold/768-beta/16
margin = threshold*margin_coefficient-F(1, 4)
checks['threshold_coefficient'] = margin_coefficient == F(1, 8000000)
checks['threshold_margin'] = margin == F(5, 4)
checks['complete_certificate_byte_identical'] = replay_bytes == original_bytes
checks['original_source_preserved'] = SOURCE.read_bytes() == source_bytes
checks['original_certificate_preserved'] = ORIGINAL.read_bytes() == original_bytes
checks['no_exceptional_decimal_signals'] = not (set(signals) - {'Rounded', 'Inexact'})
checks['all_arithmetic_contexts_expected'] = all(
    key[0] == 60 and key[1] in {decimal.ROUND_FLOOR, decimal.ROUND_CEILING, decimal.ROUND_HALF_EVEN}
    and key[2:] == (-999999, 999999, 0) for key in contexts)
checks['original_claims_pass'] = all(cert['claims'].values()) and not cert['failures']
report = {
    'scope': 'L764 algebra and actual-theta certificate audit; not RH or hyperbolicity',
    'runtime': {'python': sys.version, 'implementation': platform.python_implementation(),
                'libmpdec': decimal.__libmpdec_version__, 'initial_context': initial_context},
    'original_source_sha256': hashlib.sha256(source_bytes).hexdigest(),
    'original_certificate_sha256': hashlib.sha256(original_bytes).hexdigest(),
    'replay_certificate_sha256': hashlib.sha256(replay_bytes).hexdigest(),
    'replay_certificate': str(replay_path.relative_to(HERE.parent.parent)),
    'observations': {'interval_count': intervals, 'nonzero_adjusted_exponent_range': [min_adjusted, max_adjusted],
                     'context_counts': [{'precision': k[0], 'rounding': k[1], 'Emin': k[2],
                                         'Emax': k[3], 'clamp': k[4], 'count': v} for k, v in contexts.items()],
                     'decimal_signals': dict(signals)},
    'exact_derivative_bounds': list(map(str, exact_bounds)),
    'exact_simpson_errors': list(map(str, exact_errors)),
    'exact_rational_centered': {name: list(map(str, interval)) for name, interval in [('b2', b2), ('b3', b3), ('b4', b4)]},
    'centered_decimal_enclosures': cert['centered'],
    'required': cert['required'],
    'threshold': {'d_min': 6, 'd_over_a_min': str(threshold),
                  'linear_coefficient': str(margin_coefficient), 'strict_margin_lower': str(margin)},
    'checks': checks, 'failures': [name for name, passed in checks.items() if not passed],
    'analytic_obligations': 'Reviewed in L764; replay alone does not prove tails, division or residue implication.',
}
REPORT.write_text(json.dumps(report, indent=2)+'\n')
print('audit checks:', len(checks), 'failures:', report['failures'])
print('threshold: d>=max{6,ceil(12000000a)}; strict normalized margin >', margin)
print('observed nonzero endpoint adjusted exponents:', min_adjusted, max_adjusted)
print('audit certificate:', REPORT)
assert not report['failures']
