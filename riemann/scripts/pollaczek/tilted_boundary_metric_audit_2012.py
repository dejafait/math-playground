#!/usr/bin/env python3
"""Independent exact replay of C029n's saved arithmetic, at N=6 only."""
from fractions import Fraction as F
from math import comb, factorial
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).parent
SOURCE = ROOT / 'tilted-boundary-metric-2010.json'
data = json.loads(SOURCE.read_text())
checks = {}


def check(name, condition):
    checks[name] = bool(condition)


# Sparse polynomials in x and s with s^2=2, independent of the original
# dense pair implementation. Every coefficient and endpoint is rational.
def add(*polys):
    out = {}
    for p in polys:
        for k, v in p.items():
            out[k] = out.get(k, F(0)) + v
    return {k: v for k, v in out.items() if v}


def scale(p, c):
    return {k: c*v for k, v in p.items() if c*v}


def mul(p, q):
    out = {}
    for (i, j), a in p.items():
        for (k, l), b in q.items():
            key = (i+k, (j+l) % 2)
            out[key] = out.get(key, F(0)) + a*b*2**((j+l)//2)
    return {k: v for k, v in out.items() if v}


def decode(p):
    return {(i, j): F(c[key]) for i, c in enumerate(p)
            for j, key in enumerate(('rational', 'sqrt2')) if F(c[key])}


def interval(obj):
    return F(obj['lower']), F(obj['upper'])


def times(a, b):
    values = [x*y for x in a for y in b]
    return min(values), max(values)


def plus(a, b):
    return a[0]+b[0], a[1]+b[1]


def stretch(a, c):
    return min(a[0]*c, a[1]*c), max(a[0]*c, a[1]*c)


def horner(p, x, s):
    out = (F(0), F(0))
    for k in range(max(i for i, _ in p), -1, -1):
        coefficient = plus((p.get((k, 0), F(0)),)*2,
                           stretch(s, p.get((k, 1), F(0))))
        out = plus(times(out, x), coefficient)
    return out


# Check every arctangent term, partial sum and remainder endpoint, not a
# preview or just the original program's reported boolean checks.
atans = []
for den, key in ((5, 'atan5'), (239, 'atan239')):
    entry = data[key]
    terms = [F((-1)**j, (2*j+1)*den**(2*j+1)) for j in range(48)]
    remainder = F(1, 97*den**97)
    partial = sum(terms, F(0))
    check(key+'_complete', entry['term_count'] == 48
          and F(entry['argument']) == F(1, den)
          and [F(t) for t in entry['terms']] == terms
          and F(entry['partial_sum']) == partial
          and F(entry['positive_remainder_upper']) == remainder)
    atans.append((partial, partial+remainder))
machin = plus(stretch(atans[0], 16), stretch(atans[1], -4))
x = interval(data['pi_interval'])
s = interval(data['sqrt2_interval'])
check('machin_interval_exact', machin == interval(data['pi_machin_interval']))
check('pi_contains_machin', x[0] <= machin[0] <= machin[1] <= x[1])
check('positive_sqrt2_bounds', 0 < s[0] and s[0]**2 < 2 < s[1]**2)
check('machin_tangent_and_branch',
      (F(120,119)-F(1,239))/(1+F(120,119)*F(1,239)) == 1
      and 4*(F(1,5)-F(1,375))-F(1,239) > 0 and F(4,5) < 1)

# Bernoulli recurrence and all source coefficients, including every odd n.
bern = [F(1)]
for m in range(1, 19):
    bern.append(-sum(F(comb(m+1,k))*bern[k] for k in range(m))/F(m+1))
check('all_bernoulli', bern == [F(b) for b in data['bernoulli_0_through_18']])
phase = [{(0,0): F(1)}, {(0,0): F(1), (0,1): F(1)},
         {(0,0): F(-1)}, {(0,0): F(-1), (0,1): F(-1)}]
u = []
for n in range(9):
    terms = []
    for h in range(n+1):
        factor = -F(factorial(n)*4**h*(4**(h+1)-1)*2**(h+1),
                    factorial(n-h)*factorial(2*h+2))*bern[2*h+2]
        terms.append(mul({(h+1,0): factor}, phase[(n-h) % 4]))
    u.append(add(*terms))
    check('u_'+str(n), u[-1] == decode(data['u_over_S_polynomials'][n]))
beta, a = [], []
for n in range(7):
    beta.append(add(scale(u[n], 8*n*n+12*n+7),
                    scale(u[n+2], (2*n+3)*(2*n+5)),
                    scale(u[n-2], 4*n*(n-1)) if n >= 2 else {}))
    weight = F(factorial(6), factorial(6-n)*6**n)
    a.append(scale(beta[-1], weight))
    check('beta_'+str(n), beta[-1] == decode(data['beta_over_S_polynomials'][n]))
    check('weight_and_a_'+str(n), weight == F(data['weights'][n])
          and a[-1] == decode(data['a_over_S_polynomials'][n]))
q = add(scale(mul(a[1], a[1]), F(3,2)), scale(mul(a[0], a[0]), -1),
        scale(mul(a[2], a[0]), F(-5,2)))
check('Q_all_coefficients', q == decode(data['Q_over_S_squared_polynomial']))

# Recompute and compare complete relevant endpoints, then certify the exact
# readable bounds printed in the proof. Equality checks inspect all digits.
for label, polys in (('u', u), ('beta', beta), ('a', a)):
    for n, p in enumerate(polys):
        check(label+'_endpoints_'+str(n), horner(p,x,s) ==
              interval(data[label+'_over_S_intervals'][n]))
qe = horner(q,x,s)
ai = [horner(p,x,s) for p in a]
qf = plus(plus(stretch(times(ai[1],ai[1]), F(3,2)),
               stretch(times(ai[0],ai[0]), -1)),
          stretch(times(ai[2],ai[0]), F(-5,2)))
check('Q_complete_endpoints', qe == interval(data['Q_over_S_squared_interval_expanded'])
      and qf == interval(data['Q_over_S_squared_interval_factored']))
actual = {'beta0_over_S': horner(beta[0],x,s),
          'beta6_over_S': horner(beta[6],x,s), 'a6_over_S': ai[6],
          'Q_over_S_squared': qe}
expected = {'beta0_over_S': ('2.789485175631','2.789485175632'),
            'beta6_over_S': ('-0.057944075431','-0.057944075430'),
            'a6_over_S': ('-0.000894198695','-0.000894198694'),
            'Q_over_S_squared': ('-9.200207003118','-9.200207003117')}
for name, bounds in expected.items():
    lo, hi = map(F, bounds)
    check(name+'_proof_bounds', lo <= actual[name][0] <= actual[name][1] <= hi
          and interval(data['readable_enclosures'][name]) == (lo,hi))
check('required_strict_signs', actual['beta0_over_S'][0] > 0
      and ai[6][1] < 0 and qe[1] < 0 and qf[1] < 0)

# Independently reconstruct adjacent squared D ratios backwards from D6=1.
d2 = [F(1)]
for k in range(1,6):
    d2.insert(0, F(2*k+1,2*k)*d2[0])
check('all_D_entries', d2 == list(map(F,data['D_squared'])) and all(t>0 for t in d2))
check('all_J_couplings', [F(k*(2*k+1),2) for k in range(5,0,-1)]
      == list(map(F,data['J_offdiagonal_squared'])))
check('K_radical_factors', d2[4] == F(3,2) and d2[5] == 1
      and F(5)*d2[3]/F(3,2) == F(25,4))

failures = [k for k,v in checks.items() if not v]
out = ROOT / 'tilted-boundary-metric-audit-2012.json'
report = {'scope': 'C029n N=6 arithmetic replay; paper matrix audit is canonical in C029n',
          'input_certificate': str(SOURCE.name),
          'input_sha256': hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
          'checks': checks, 'failures': failures,
          'actual_bounds': {k: {'lower': str(v[0]), 'upper': str(v[1])}
                            for k,v in actual.items()},
          'required_bounds': expected,
          'result': 'PASS' if not failures else 'FAIL'}
out.write_text(json.dumps(report, indent=2)+'\n')
print('Result:', report['result'], '; checks:', len(checks), '; failures:', failures)
for k,v in expected.items():
    print(k+': actual enclosure is contained in ['+', '.join(v)+']')
print('Required: a0/S>0, a6/S<0, Q/S^2<0, all scaling entries positive')
print('Full endpoints and comparisons:', out.relative_to(Path.cwd()))
if failures:
    raise SystemExit(1)
