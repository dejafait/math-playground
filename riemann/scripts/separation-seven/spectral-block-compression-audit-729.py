#!/usr/bin/env python3
"""Independent moment/recurrence regeneration and a static work lower bound.

This audits the fixed 728 construction, not a new compression algorithm.
Full interval evidence goes to disk. Decimal arithmetic retains its inherited
correct-rounding contract. Source-level work units are defined in the report.
"""
from decimal import Decimal, Context, ROUND_FLOOR, ROUND_CEILING
from fractions import Fraction as Q
from hashlib import sha256
from math import comb
from pathlib import Path
import json

HERE = Path(__file__).resolve()
BASE = HERE.parent
SOURCE = BASE / 'spectral-block-compression-728.json'
OUT = HERE.with_suffix('.json')
data = json.loads(SOURCE.read_text())
dn = Context(prec=320, rounding=ROUND_FLOOR)
up = Context(prec=320, rounding=ROUND_CEILING)
D = Decimal
ZERO = (D(0), D(0))
ONE = (D(1), D(1))
checks = []
failures = []


def check(name, value):
    checks.append({'name': name, 'passed': bool(value)})
    if not value:
        failures.append(name)


def rational(q):
    q = Q(q)
    return (dn.divide(D(q.numerator), D(q.denominator)),
            up.divide(D(q.numerator), D(q.denominator)))


def add(a, b):
    return dn.add(a[0], b[0]), up.add(a[1], b[1])


def neg(a):
    return a[1].copy_negate(), a[0].copy_negate()


def mul(a, b):
    return (min(dn.multiply(x, y) for x in a for y in b),
            max(up.multiply(x, y) for x in a for y in b))


def div(a, b):
    assert b[0] > 0
    return mul(a, (dn.divide(D(1), b[1]), up.divide(D(1), b[0])))


def isum(terms):
    result = ZERO
    for item in terms:
        result = add(result, item)
    return result


def contained(saved, fresh):
    return D(saved[0]) <= fresh[0] <= fresh[1] <= D(saved[1])


def export(a):
    return list(map(str, a))


bern = [Q(1)]
for n in range(1, 129):
    bern.append(-sum(Q(comb(n+1, j))*bern[j] for j in range(n))/Q(n+1))
C = abs(bern[128]) + sum(Q(comb(128, j))*abs(bern[j]) for j in range(129))


def new_moments(J):
    if J < 256:
        raw = [rational(sum((Q(4*j+1, 4*J)**(p-2)/J
                             for j in range(J, 2*J)), Q(0)))
               for p in range(35)]
    else:
        u, v = Q(4*J+1, 4), Q(8*J+1, 4)
        z = rational((v-u)/(v+u))
        z2 = mul(z, z)
        term, logsum = z, ZERO
        for i in range(256):
            logsum = add(logsum, div(term, rational(2*i+1)))
            term = mul(term, z2)
        logtail = rational(Q(2, 513*3**513)*Q(9, 8))[1]
        logbox = add(mul(rational(2), logsum), (D(0), logtail))
        # Exact rational EM corrections and remainder; only the log is rounded.
        correction1 = (1/u-1/v)/2 + sum(
            bern[2*r]/(2*r)*(u**(-2*r)-v**(-2*r)) for r in range(1, 64))
        center2 = 1/u-1/v+(u**-2-v**-2)/2 + sum(
            bern[2*r]*(u**(-2*r-1)-v**(-2*r-1)) for r in range(1, 64))
        error1, error2 = C*u**-128/128, C*u**-129
        raw = [(rational(J*(center2-error2))[0], rational(J*(center2+error2))[1]),
               add(logbox, (rational(correction1-error1)[0], rational(correction1+error1)[1]))]
        sums = []
        for q in range(33):
            sums.append((v**(q+1)-u**(q+1)-sum(
                Q(comb(q+1, p))*sums[p] for p in range(q)))/(q+1))
            raw.append(rational(sums[-1]/J**(q+1)))
    return [isum(mul(rational(comb(n, q)*2**q*(-3)**(n-q)), raw[q])
                 for q in range(n+1)) for n in range(35)]


def dot(poly, mu, shift=0):
    return isum(mul(mul(a, b), mu[i+j+shift])
                for i, a in enumerate(poly) for j, b in enumerate(poly))


def new_recurrence(mu):
    polynomials, norms = [], []
    prev, p = [ZERO], [ONE]
    for n in range(17):
        h = dot(p, mu)
        assert h[0] > 0
        polynomials.append(p)
        norms.append(h)
        alpha = div(dot(p, mu, 1), h)
        beta = div(h, norms[-2]) if n else ZERO
        nxt = [ZERO]+p
        for i in range(len(p)):
            nxt[i] = add(nxt[i], neg(mul(alpha, p[i])))
        if n:
            for i in range(len(prev)):
                nxt[i] = add(nxt[i], neg(mul(beta, prev[i])))
        prev, p = p, nxt
    return polynomials, norms, p


constructor = BASE / 'spectral-block-compression-728.py'
replay = BASE / 'spectral-block-compression-replay-728.py'
prior_replay = json.loads(replay.with_suffix('.json').read_text())
check('constructor source hash matches original certificate',
      sha256(constructor.read_bytes()).hexdigest() == data['source_sha256'])
check('prior exact replay is bound to this constructor certificate',
      prior_replay['source_sha256'] == sha256(SOURCE.read_bytes()).hexdigest())
check('prior replay source hash matches saved script',
      prior_replay['replay_script_sha256'] == sha256(replay.read_bytes()).hexdigest())
check('consecutive block inventory', [r['k'] for r in data['blocks']] == list(range(5, 72)))
rows = []
for saved in data['blocks']:
    k, J = saved['k'], saved['J']
    check(f'block{k} dyadic size and shape', J == 2**k and
          len(saved['moments_t']) == 35 and len(saved['norms']) == 17 and
          [len(p) for p in saved['orthogonal_polynomials']] == list(range(1, 18)) and
          len(saved['degree17_polynomial']) == 18)
    mu = new_moments(J)
    pp, hh, final = new_recurrence(mu)
    for n, a in enumerate(mu):
        check(f'block{k} moment{n} independently enclosed', contained(saved['moments_t'][n], a))
    for n, (p, h) in enumerate(zip(pp, hh)):
        check(f'block{k} norm{n} independently enclosed', contained(saved['norms'][n], h))
        for j, a in enumerate(p):
            check(f'block{k} polynomial{n} coefficient{j} independently enclosed',
                  contained(saved['orthogonal_polynomials'][n][j], a))
    for j, a in enumerate(final):
        check(f'block{k} final coefficient{j} independently enclosed',
              contained(saved['degree17_polynomial'][j], a))
    rows.append({'k': k, 'J': J, 'moments_t': list(map(export, mu)),
                 'orthogonal_polynomials': [[export(a) for a in p] for p in pp],
                 'norms': list(map(export, hh)), 'degree17_polynomial': list(map(export, final))})

# On (-1,1), rounding in the two directed midpoint operations is less
# than1e-254. Each child width is >=parent_width/2-1e-254, so accumulated
# width loss after any number of halvings is <2e-254. This proves the
# iteration lower bound without assuming exact finite-decimal midpoints.
# Check the actual saved widths independently as additional evidence.
initial = Q(1, 5_000_000)
threshold = Q(1, 10**40)
iterations = 111
final_width = initial/2**iterations
check('exact bisection threshold requires111 iterations',
      initial/2**(iterations-1) > threshold >= final_width)
check('roundoff robust lower bound requires at least111 iterations',
      initial/2**(iterations-1)-Q(2, 10**254) > threshold)
check('every saved final bracket has exactly that width',
      all(Q(node['root_bracket'][1])-Q(node['root_bracket'][0]) == final_width
          for row in data['blocks'] for node in row['nodes']))
check('all output midpoint rates positive',
      all(Q(node['rate']) > 0 and Q(node['weight']) > 0
          for row in data['blocks'] for node in row['nodes']))

# Count only the successful body iterations, and only the operations listed.
unit_count = {'directed_decimal_arithmetic': 10, 'decimal_comparisons': 8,
              'explicit_bindings_or_stores': 22, 'successful_loop_advances': 13}
horner_steps = 67*17*iterations*17
work_lower = horner_steps*sum(unit_count.values())
check('mandatory root bisection work alone exceeds all-work cap', work_lower > 10**8)
theory = Q(30*2**46, 5**34)+Q(2**46, 4*2**72-3)
coefficient = sum((Q(row['coefficient_kernel_error_upper']) for row in data['blocks']), Q(0))*2**46
check('published rounded total bound includes coefficients', theory+coefficient < Q(7353, 10**12))
check('published coefficient bound', coefficient < Q(3, 10**25))

# Replay the existing exact root/weight checks without overwriting728 evidence.
replay_out = BASE / 'spectral-block-compression-enclosure-replay-729.json'
source = replay.read_text()
old_line = "OUT = HERE.with_suffix('.json')"
assert source.count(old_line) == 1
modified = source.replace(old_line, 'OUT = HERE.with_name('+repr(replay_out.name)+')')
exec(compile(modified, str(replay), 'exec'), {'__file__': str(replay), '__name__': '__main__'})
replayed = json.loads(replay_out.read_text())
check('fresh exact replay passes all4764 finite checks',
      replayed['all_checks_pass'] and len(replayed['checks']) == 4764)

report = {'scope': 'C998v moment/recurrence/error audit and fixed728 implementation work stop',
          'audit_script_sha256': sha256(HERE.read_bytes()).hexdigest(),
          'constructor_certificate_sha256': sha256(SOURCE.read_bytes()).hexdigest(),
          'precision_decimal_digits': 320, 'regenerated_blocks': rows,
          'checks': checks, 'failed_checks': failures, 'all_checks_pass': not failures,
          'weighted_error': {'exact_upper': str(theory+coefficient), 'rounded_upper': '7.353e-9', 'required': '1e-7'},
          'work': {'model': 'one scalar arithmetic/comparison, explicit binding/store, or successful loop advance; all other costs zero',
                   'operations_per_interval_horner_step': unit_count,
                   'bisect_iterations_per_root': iterations, 'mandatory_horner_steps': horner_steps,
                   'lower_bound': work_lower, 'required_all_work_cap': 10**8,
                   'passes_cap': False,
                   'qualification': 'specific728 source prescription; not a high-level-arithmetic-only or universal algorithm lower bound'},
          'replay_certificate': str(replay_out.relative_to(BASE.parent.parent)),
          'memory_upper_bound_certified': False,
          'unresolved': ['other implementations', 'density and local term', 'full scalar', 'signed S3', 'H2', 'Xi/global transfer']}
OUT.write_text(json.dumps(report, indent=2)+'\n')
print('Audit checks:', len(checks)-len(failures), '/', len(checks), '; failures:', failures)
print('Weighted uniform error <7.353e-9; required <=1e-7')
print('Mandatory source-operation lower bound:', work_lower, '; required all-work cap:', 10**8)
print('Certificate:', OUT.relative_to(BASE.parent.parent))
if failures:
    raise SystemExit(1)
