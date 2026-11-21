#!/usr/bin/env python3
"""L938 fixed-budget audit. Originals are read-only; no sign refinement.

The transcendental producer is replayed after code/proof review under
its original Decimal contracts. The entire integer polynomial is checked
by a separate deterministic bounded-coefficient evaluation identity, not
by modular samples or by rerunning balanced-digit multiplication.
"""
from collections import defaultdict
from decimal import Decimal
from fractions import Fraction as F
from functools import reduce
from hashlib import sha256
import importlib.util
import json
from math import factorial
from pathlib import Path
import platform
import re
import sys
import time

sys.set_int_max_str_digits(0)
BASE = Path(__file__).resolve().parent
OUT = BASE / 'actual-h2-energy-cell-audit-50.json'
REPLAY = BASE / 'actual-h2-energy-cell-node-replay-50.json'
SOURCE = BASE / 'actual-h2-energy-cell-48.json'
POLY = BASE / 'actual-h2-energy-cell-polynomial-48.json'
PRODUCER = BASE / 'actual-h2-energy-cell-48.py'
LEMMA = BASE.parent.parent / 'lemmas/L938-actual-h2-fixed-energy-density-and-cell-test.md'
started = time.monotonic()
data = json.loads(SOURCE.read_text())
saved_poly = json.loads(POLY.read_text())
report = {
    'scope': 'Original degree256/257 nodes/theta8/precision200/32 cells; no refinement',
    'python': sys.version, 'platform': platform.platform(),
    'inputs_sha256': {p.name: sha256(p.read_bytes()).hexdigest()
                      for p in (SOURCE, POLY, PRODUCER)},
    'checks': [], 'failures': [], 'status': 'IN_PROGRESS',
}


def save():
    report['elapsed_seconds'] = round(time.monotonic() - started, 3)
    OUT.write_text(json.dumps(report, indent=2) + '\n')


def check(name, result):
    ok = bool(result)
    report['checks'].append({'name': name, 'passed': ok})
    if not ok:
        report['failures'].append(name)
        report['status'] = 'FAILED'
        save()
        raise AssertionError(name)


def interval(raw):
    return F(Decimal(raw['lower'])), F(Decimal(raw['upper']))


def add(*terms):
    out = defaultdict(F)
    for p in terms:
        for k, v in p.items():
            out[k] += v
    return {k: v for k, v in out.items() if v}


def mul(a, b):
    out = defaultdict(F)
    for ka, va in a.items():
        for kb, vb in b.items():
            out[tuple(x+y for x, y in zip(ka, kb))] += va*vb
    return {k: v for k, v in out.items() if v}


def scale(a, c):
    return {k: v*c for k, v in a.items() if v*c}


def product(items):
    return reduce(lambda a, b: a*b, items, 1)


zero = (0,)*6
one = {zero: F(1)}
q = [{}]
for n in range(1, 7):
    monomial = [0]*6
    monomial[n-1] = 1
    q.append({tuple(monomial): F((-1)**n)})

# Compute powers of the truncated series and the logarithm directly.
# This does not invoke the producer's Newton recurrence or algebra().
power = [one] + [{} for _ in range(6)]
logs = [{} for _ in range(7)]
for j in range(1, 7):
    nxt = [{} for _ in range(7)]
    for degree in range(1, 7):
        nxt[degree] = add(*(mul(power[degree-k], q[k])
                            for k in range(1, degree+1)))
    power = nxt
    logs = [add(logs[n], scale(power[n], F((-1)**(j+1), j)))
            for n in range(7)]
s = [scale(logs[n], -n) for n in range(7)]
# Leibniz determinant, avoiding the producer's five-term expansion.
from itertools import permutations
det = {}
for permutation in permutations(range(3)):
    inversions = sum(permutation[i] > permutation[j]
                     for i in range(3) for j in range(i+1, 3))
    term = one
    for i in range(3):
        term = mul(term, s[i+permutation[i]+2])
    det = add(det, scale(term, (-1)**inversions))
terms = sorted((tuple([12-sum(k), *k]), int(v)) for k, v in det.items())
check('all determinant coefficients are integers', all(v.denominator == 1 for v in det.values()))
check('34 terms and degree-six cancellation', len(terms) == 34 and max(map(sum, det)) == 6)
check('homogeneous and weighted degrees twelve',
      all(sum(a) == 12 and sum(k*v for k, v in enumerate(a)) == 12 for a, c in terms))
saved_terms = sorted((tuple(t['exponents_A0_to_A6']), t['coefficient'])
                     for t in data['algebra']['terms'])
check('entire saved coefficient table', terms == saved_terms)
table = sorted((tuple(map(int, row[1].split(','))), int(row[0]))
               for row in re.findall(r'^\| (-?\d+) \| \(([^)]+)\) \|$',
                                      LEMMA.read_text(), re.M))
check('entire canonical coefficient table', terms == table)
weight = sum((F(abs(c), product(factorial(k)**v for k, v in enumerate(a)))
              for a, c in terms), F(0))
check('absolute beta weight', weight == F(293, 540))
check('constant-kernel cancellation',
      sum((F(c, product(factorial(k)**v for k, v in enumerate(a)))
           for a, c in terms), F(0)) == 0)
report['algebra'] = {'terms': [{'exponents': list(a), 'coefficient': c} for a, c in terms],
                     'beta_weight': str(weight), 'log_and_determinant_residual': '0'}
save()
print('Independent finite-log/Leibniz table: all 34 terms match.', flush=True)

# Full fixed-budget replay. Same implementation, not an independent library.
spec = importlib.util.spec_from_file_location('l938_fixed_producer', PRODUCER)
producer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(producer)
lib = producer.load_intervals()
power_numerators, power_den, epsilon, pi, approximation = producer.approx_kernel(lib)
REPLAY.write_text(json.dumps(approximation, indent=2) + '\n')
check('entire node/coefficient/epsilon replay', approximation == data['approximation'])
check('unaltered fixed budget', (producer.DEGREE, producer.PRECISION, producer.THETA_TERMS,
                               approximation['nodes']) == (256, 200, 8, 257))
report['node_replay'] = {'file': REPLAY.name, 'identical_all_fields': True,
                       'independent_implementation': False,
                       'contracts': 'Reviewed interval code; documented Decimal arithmetic/exp still assumed'}

# Independent Chebyshev-to-power conversion by the closed formula
# T_n(y)=(n/2) sum_j (-1)^j (n-j-1)!/(j!(n-2j)!)*(2y)^(n-2j).
from math import comb
cheb = [int(c['chosen_numerator']) for c in approximation['chebyshev_coefficients']]
converted = [F(cheb[0])] + [F(0)]*256
for n in range(1, 257):
    for j in range(n//2+1):
        degree = n-2*j
        coefficient = F(n*(-1)**j*factorial(n-j-1)*2**degree,
                        2*factorial(j)*factorial(degree))*cheb[n]
        for ell in range(degree+1):
            converted[ell] += coefficient*F(comb(degree, ell)*(-1)**(degree-ell), 4**ell)
check('all 257 power coefficients by closed Chebyshev formula',
      all(converted[j]*4**256 == power_numerators[j] for j in range(257)))
check('power denominator', power_den == 10**120*4**256)
save()
print('All fixed-budget nodes replay identically; all power coefficients independently match.', flush=True)

# Rebuild every Q coefficient as a rational gamma weight, checking its
# integrality rather than applying unverified integer-floor divisions.
common = 2*factorial(12)*power_den*4**262
qq = []
for k in range(7):
    row = []
    for ell, a in enumerate(power_numerators):
        exact = F(common*a*factorial(2*(k+ell)),
                  2*power_den*factorial(2*k)*4**(k+ell)*factorial(k+ell))
        check(f'Q{k} coefficient {ell} exact integer', exact.denominator == 1)
        row.append(exact.numerator)
    qq.append(row)
rr = list(map(int, saved_poly['numerators']))
check('convolution degree3072 and common denominator', len(rr) == 3073 and rr[-1] != 0
      and int(saved_poly['denominator']) == common**12)

# ||R||_infinity <= ||R||_1 <= sum |c_alpha| product ||Q_k||_1^alpha_k.
# For D = saved_R - actual_R, every |D_l| <= bound+max_saved < base.
# If D(base)=0, reduction mod base forces D_0=0, then induction forces
# every coefficient zero. One exact equality therefore proves ALL coefficients.
qnorm = [sum(map(abs, row)) for row in qq]
bound = sum(abs(c)*product(qnorm[k]**a[k] for k in range(7)) for a, c in terms)
max_saved = max(map(abs, rr))
bits = (bound+max_saved).bit_length()+1
base = 1 << bits
check('deterministic coefficient separation', bound+max_saved < base//2)
report['integer_identity'] = {'degree': len(rr)-1, 'base_power_of_two': bits,
    'actual_polynomial_coefficient_bound': str(bound), 'saved_max_abs_coefficient': str(max_saved),
    'difference_bound_lt_half_base': True, 'residual': 'PENDING',
    'method': 'Exact integer evaluation plus coefficient bound; no modular inference'}
save()
print(f'Deterministic degree3072 identity: base2^{bits}; coefficient bound bits={bound.bit_length()}.', flush=True)


def evaluate(p):
    out = 0
    for coefficient in reversed(p):
        out = (out << bits) + coefficient
    return out


qvalues = list(map(evaluate, qq))
cache = {(k, 0): 1 for k in range(7)}


def qpower(k, exponent):
    if (k, exponent) not in cache:
        cache[(k, exponent)] = qvalues[k]**exponent
    return cache[(k, exponent)]


inner_value = 0
for alpha, coefficient in terms:
    exponents = list(alpha)
    exponents[0] -= 6
    factors = [qpower(k, n) for k, n in enumerate(exponents) if n]
    factors.sort(key=lambda v: abs(v).bit_length())
    inner_value += coefficient*product(factors)
expected_value = inner_value*qpower(0, 6)
actual_value = evaluate(rr)
check('full exact integer polynomial identity', actual_value == expected_value)
report['integer_identity']['residual'] = '0'
report['integer_identity']['evaluation_bits'] = abs(actual_value).bit_length()
del actual_value, expected_value, inner_value, qvalues, cache
save()
print('Complete integer polynomial identity verified; every coefficient covered.', flush=True)

# Rebuild each integrated coefficient by direct factorial division,
# independently of the producer's descending ratio/four recurrence.
# Evaluate by even/odd Horner splitting at EVERY endpoint.
test = data['mass_test']
denominator = int(test['common_polynomial_integral_denominator'])
check('primitive denominator', denominator == common**12*factorial(3090)*4**3090)
primitives = []
top_factorial = factorial(3090)
integrated = []
for ell, coefficient in enumerate(rr):
    quotient, remainder = divmod(top_factorial, factorial(18+ell))
    check(f'primitive coefficient {ell} factorial division', remainder == 0)
    integrated.append(coefficient*quotient*4**(3072-ell))
for j in range(33):
    parts = []
    for parity in (0, 1):
        total = 0
        for coefficient in reversed(integrated[parity::2]):
            total = total*j*j+coefficient
        parts.append(total)
    primitives.append((parts[0]+j*parts[1])*j**18)
    if j % 8 == 0:
        print(f'Exact primitive endpoints: {j+1}/33', flush=True)

pl, ph = interval(approximation['pi'])
common_error = F(12*8**11, 2**36*factorial(18))*epsilon*weight
check('entire error constant', common_error == F(test['common_error_without_pi6_or_cell_power']))
check('epsilon actual and required', 0 < epsilon < F(6664, 10**39) < F(1, 10**34))
signs = []
cell_records = []
for j, cell in enumerate(test['cells']):
    check(f'cell {j} index and endpoints', cell['j'] == j and cell['cell'] == [str(F(j, 4)), str(F(j+1, 4))])
    numerator = primitives[j+1]-primitives[j]
    check(f'cell {j} full primitive numerator', numerator == int(cell['polynomial_integral_numerator']))
    exact = F(numerator, denominator)
    lo, hi = interval(cell['polynomial_integral_interval'])
    required_lo, required_hi = sorted((exact*pl**6, exact*ph**6))
    check(f'cell {j} polynomial enclosure', lo <= required_lo <= required_hi <= hi)
    error = F(Decimal(cell['full_kernel_error_upper']))
    required_error = common_error*F((j+1)**18-j**18, 4**18)*ph**6
    check(f'cell {j} full error', error >= required_error > 0)
    full_lo, full_hi = interval(cell['full_mass_interval'])
    check(f'cell {j} final complete endpoints', full_lo <= lo-error <= hi+error <= full_hi)
    sign = 1 if full_lo > 0 else -1 if full_hi < 0 else 0
    check(f'cell {j} recorded sign', cell['certified_sign'] == sign)
    signs.append(sign)
    cell_records.append({'j': j, 'full_mass_interval': cell['full_mass_interval'],
                         'error_upper': cell['full_kernel_error_upper'], 'sign': sign})
check('all 32 signs', len(signs) == 32 and signs == [-1]*2+[1]*13+[0]*17 == test['summary']['signs'])
triples = [(i,j,k) for i in range(32) for j in range(i+1,32) for k in range(j+1,32)
           if signs[i] and signs[j] == -signs[i] and signs[k] == signs[i]]
check('no certified alternating triple', triples == test['summary']['alternating_triples'] == [])

contexts = {}
for name, context in [('down', lib.DOWN), ('up', lib.UP), ('near', lib.NEAR)]:
    raw = data['arithmetic'][name]
    check(name+' precision and rounding', context.prec == raw['precision'] == 200
          and context.rounding == raw['rounding'])
    for signal in context.traps:
        if signal.__name__ in ('InvalidOperation','DivisionByZero','Overflow','Underflow','Subnormal'):
            check(name+' '+signal.__name__+' saved and replay traps/flags',
                  context.traps[signal] and not context.flags[signal]
                  and raw['traps'][str(signal)] and not raw['flags'][str(signal)])
    contexts[name] = {'precision': context.prec, 'rounding': context.rounding,
                      'traps': {str(k): v for k, v in context.traps.items()},
                      'flags': {str(k): v for k, v in context.flags.items()}}
report['arithmetic_replay'] = contexts
report['cells'] = cell_records
report['status'] = 'PASSED'
report['summary'] = {'checks_passed': len(report['checks']), 'failures': report['failures'],
    'all_34_terms_match': True, 'all_257_nodes_replayed': True,
    'all_257_power_coefficients_checked': True, 'all_3073_convolution_coefficients_checked': True,
    'all_33_primitive_endpoints_checked': True, 'all_32_complete_cell_enclosures_checked': True,
    'signs': signs, 'alternating_triples_actual': len(triples), 'alternating_triples_required': 1,
    'epsilon_actual_upper': approximation['epsilon_interval']['upper'], 'epsilon_required': '1e-34',
    'limitation': 'Conditional Decimal/library contracts; no global crossing bound; 17 uncertain cells unchanged'}
save()
print(f"PASS: {len(report['checks'])} checks; 2 negative/13 positive/17 uncertain; triples0 required1; {OUT}", flush=True)
