"""Independent C029v replay: standard-library exact arithmetic, no local imports.

Polynomials use sparse (t, x, y) powers, reduced by y**2=2; x is pi.
Original certificates are read only after the independent construction.
"""
from fractions import Fraction as F
from math import factorial, isqrt
from pathlib import Path
import hashlib
import json


def const(a):
    return {(0, 0, 0): F(a)} if a else {}


def add(*args):
    out = {}
    for arg in args:
        for key, value in arg.items():
            out[key] = out.get(key, F(0)) + value
    return {k: v for k, v in out.items() if v}


def scale(a, f):
    return {k: v * f for k, v in a.items() if v * f}


def mul(a, b):
    out = {}
    for (i, j, k), v in a.items():
        for (l, m, n), w in b.items():
            key = (i + l, j + m, (k + n) % 2)
            out[key] = out.get(key, F(0)) + v*w*2**((k+n)//2)
    return {k: v for k, v in out.items() if v}


def tcoef(a, degree):
    return {(0, j, k): v for (i, j, k), v in a.items() if i == degree}


def field_encoding(a):
    assert all(i == 0 for i, _, _ in a)
    top = max((j for _, j, _ in a), default=0)
    return [{"rational": str(a.get((0, j, 0), F(0))),
             "sqrt2": str(a.get((0, j, 1), F(0)))} for j in range(top+1)]


def field_decode(data):
    if isinstance(data, str):
        return const(F(data))
    out = {}
    for j, row in enumerate(data):
        for k, label in enumerate(("rational", "sqrt2")):
            v = F(row[label])
            if v:
                out[0, j, k] = v
    return out


# Independent Bernoulli construction using Stirling numbers of the second kind:
# B_n = sum_j (-1)^j j! S(n,j)/(j+1), including B_1=-1/2.
stirling = [[1]]
for n in range(1, 19):
    prev = stirling[-1]
    stirling.append([(prev[j-1] if j else 0)
                     + j*(prev[j] if j < len(prev) else 0)
                     for j in range(n+1)])
bernoulli = [sum((F((-1)**j * factorial(j) * stirling[n][j], j+1)
                  for j in range(n+1)), F(0)) for n in range(19)]

t = {(1, 0, 0): F(1)}
q = add(const(1), {(2, 0, 0): F(4)})
phase = [const(1), add(const(1), {(0, 0, 1): F(1)}),
         const(-1), add(const(-1), {(0, 0, 1): F(-1)})]
u = []
for n in range(9):
    terms = []
    for h in range(n+1):
        factor = -F(factorial(n)*4**h*(4**(h+1)-1)*2**(h+1),
                    factorial(n-h)*factorial(2*h+2))*bernoulli[2*h+2]
        terms.append(mul({(0, h+1, 0): factor}, phase[(n-h) % 4]))
    u.append(add(*terms))
beta = [add(scale(u[k-2], 4*k*(k-1)) if k >= 2 else {},
            scale(u[k], 8*k*k+12*k+7),
            scale(u[k+2], (2*k+3)*(2*k+5))) for k in range(7)]

basis = [const(1)]
for n in range(10):
    basis.append(scale(add(mul(t, basis[n]),
                           scale(basis[n-1], -F(2*n+1, 2)) if n else {}),
                       F(1, n+1)))


def coordinates(a):
    remainder = dict(a)
    answer = [{} for _ in range(11)]
    for degree in range(10, -1, -1):
        value = scale(tcoef(remainder, degree), factorial(degree))
        answer[degree] = value
        remainder = add(remainder, scale(mul(value, basis[degree]), -1))
    if remainder:
        raise ArithmeticError("Nonzero change-of-basis remainder")
    return answer


weights = [F(factorial(6), factorial(6-k)*6**k) if k <= 6 else F(0)
           for k in range(11)]
A = add(*(mul(u[k], basis[k]) for k in range(9)))
qA_monomial = mul(q, A)
qA = coordinates(qA_monomial)
JqA = [scale(a, weights[k]) for k, a in enumerate(qA)]
T6 = [scale(beta[k], weights[k]) if k <= 6 else {} for k in range(11)]
Ju = [scale(u[k], weights[k]) for k in range(9)]
JA = add(*(mul(Ju[k], basis[k]) for k in range(9)))
qJA = coordinates(mul(q, JA))
R = [add(a, scale(b, -1)) for a, b in zip(JqA, qJA)]
numerator_residual = [add(a, scale(b, -1)) for a, b in zip(JqA, T6)]

# Construct the source-(9) columns separately for comparison with recurrence.
direct_columns = [coordinates(mul(q, basis[n])) for n in range(9)]
formula_columns = []
for n in range(9):
    column = [{} for _ in range(11)]
    column[n+2] = const(4*(n+1)*(n+2))
    column[n] = const(8*n*n+12*n+7)
    if n >= 2:
        column[n-2] = const((2*n-1)*(2*n+1))
    formula_columns.append(column)


# Regenerate precisely the fixed C029n inputs, with exact rational endpoints.
def arctangent_input(denominator):
    v = F(1, denominator)
    terms = [(-1)**j*v**(2*j+1)/(2*j+1) for j in range(48)]
    return {"argument": str(v), "term_count": 48,
            "terms": [str(a) for a in terms],
            "partial_sum": str(sum(terms, F(0))),
            "positive_remainder_upper": str(v**97/97)}


atan5, atan239 = arctangent_input(5), arctangent_input(239)
r5, e5 = F(atan5["partial_sum"]), F(atan5["positive_remainder_upper"])
r239, e239 = F(atan239["partial_sum"]), F(atan239["positive_remainder_upper"])
machin = (16*r5-4*(r239+e239), 16*(r5+e5)-4*r239)


def outward(interval, places):
    grid = 10**places
    lo, hi = interval
    return (F((lo*grid).__floor__(), grid), F((hi*grid).__ceil__(), grid))


pi_bounds = outward(machin, 60)
root_integer = isqrt(2*10**120)
sqrt_bounds = (F(root_integer, 10**60), F(root_integer+1, 10**60))


def isum(a, b):
    return (a[0]+b[0], a[1]+b[1])


def iproduct(a, b):
    products = [x*y for x in a for y in b]
    return (min(products), max(products))


def horner(a):
    highest = max((j for _, j, _ in a), default=0)
    acc = (F(0), F(0))
    for j in range(highest, -1, -1):
        rational = a.get((0, j, 0), F(0))
        radical = a.get((0, j, 1), F(0))
        term = isum((rational, rational),
                    iproduct((radical, radical), sqrt_bounds))
        acc = isum(iproduct(acc, pi_bounds), term)
    return acc


def interval_encoding(pair):
    return {"lower": str(pair[0]), "upper": str(pair[1])}


# Independent transcription of C029v's three displayed polynomials and bounds.
displayed_coefficients = {
    2: [(0, 0), (F(-101,6), 0), (F(-140,3), F(-140,3)),
        (112, 0), (F(544,3), F(544,3)), (F(-3968,27), 0)],
    3: [(0, 0), (F(-211,12), F(-211,12)), (F(437,6), 0),
        (F(2200,9), F(2200,9)), (F(-37400,63), 0),
        (F(-545600,567), F(-545600,567)), (F(442240,567), 0)],
    4: [(0, 0), (F(3515,648), 0), (F(9275,162), F(9275,162)),
        (F(-23158,81), 0), (F(-1653080,1701), F(-1653080,1701)),
        (F(12057760,5103), 0), (F(19547008,5103), F(19547008,5103)),
        (F(-47532544,15309), 0)]}
required = {2: (F('-22.184393875256'), F('-22.184393875255')),
            3: (F('-6.599923769988'), F('-6.599923769987')),
            4: (F('-2.675150248313'), F('-2.675150248312'))}

# No earlier script is imported or executed. Read saved comparison data now.
here = Path(__file__).resolve().parent
old_path = here/'jensen-quadratic-endpoint-2044.json'
input_path = here/'tilted-boundary-metric-2010.json'
old = json.loads(old_path.read_text())
input_data = json.loads(input_path.read_text())
checks = {}


def check(name, condition):
    checks[name] = bool(condition)


def compare_vector(name, values, stored):
    check(name+'_length', len(values) == len(stored))
    for k, value in enumerate(values):
        check(name+f'_{k}', value == field_decode(stored[k]))


check('Bernoulli_all_19_original', bernoulli == list(map(F, old['bernoulli_0_through_18'])))
check('Bernoulli_all_19_input', bernoulli == list(map(F, input_data['bernoulli_0_through_18'])))
for label, data in [('original', old), ('input', input_data)]:
    for key, value in [('atan5', atan5), ('atan239', atan239)]:
        # Normalize rational strings rather than require an encoding convention.
        obj = data[key]
        check(f'{label}_{key}_all_terms', list(map(F, obj['terms'])) == list(map(F, value['terms'])))
        check(f'{label}_{key}_count', obj['term_count'] == 48)
        for field in ['argument', 'partial_sum', 'positive_remainder_upper']:
            check(f'{label}_{key}_{field}', F(obj[field]) == F(value[field]))
    for key, value in [('pi_interval', pi_bounds), ('sqrt2_interval', sqrt_bounds),
                       ('pi_machin_interval', machin)]:
        check(f'{label}_{key}', (F(data[key]['lower']), F(data[key]['upper'])) == value)
check('sqrt2_strict_squared_bounds', 0 < sqrt_bounds[0]**2 < 2 < sqrt_bounds[1]**2)
check('pi_positive', 0 < pi_bounds[0] <= pi_bounds[1])
check('basis_degree_and_leading_all_11', all(tcoef(basis[k], k) == const(F(1, factorial(k)))
                                            and max(i for i, _, _ in basis[k]) == k
                                            for k in range(11)))
for k in range(11):
    check(f'basis_all_monomials_{k}', all(F(c) == basis[k].get((i,0,0), F(0))
                                          for i,c in enumerate(old['p_basis_monomial'][k]))
          and len(old['p_basis_monomial'][k]) == k+1)
check('weights_all_11', weights == list(map(F, old['weights'])))
compare_vector('u_original', u, old['u_over_S'])
compare_vector('u_input', u, input_data['u_over_S_polynomials'])
compare_vector('beta_original', beta, old['beta_over_S'])
compare_vector('beta_input', beta, input_data['beta_over_S_polynomials'])
for n in range(9):
    check(f'multiplication_direct_formula_{n}', direct_columns[n] == formula_columns[n])
    compare_vector(f'multiplication_direct_original_{n}', direct_columns[n], old['multiplication_direct_columns'][n])
    compare_vector(f'multiplication_formula_original_{n}', formula_columns[n], old['multiplication_formula_columns'][n])
vectors = {'qA_over_S': qA, 'qA_direct_over_S': qA,
           'qA_monomial_over_S': [tcoef(qA_monomial,k) for k in range(11)],
           'JqA_over_S': JqA, 'Ju_over_S': Ju, 'qJu_over_S': qJA,
           'R_over_S': R, 'T6_over_S': T6,
           'numerator_identity_residual': numerator_residual}
for name, values in vectors.items():
    compare_vector(name, values, old[name])
check('full_numerator_identity', all(not a for a in numerator_residual))
check('R_modes_9_10_zero', not R[9] and not R[10])

bulk = {}
for k in [2,3,4]:
    displayed = {(0,j,l): F(v) for j,pair in enumerate(displayed_coefficients[k])
                 for l,v in enumerate(pair) if v}
    check(f'bulk_{k}_displayed_polynomial', R[k] == displayed)
    bounds = horner(R[k])
    outer = outward(bounds, 12)
    check(f'bulk_{k}_required_enclosure', required[k][0] <= bounds[0] <= bounds[1] <= required[k][1])
    check(f'bulk_{k}_required_rounding', outer == required[k])
    check(f'bulk_{k}_strict_negative', bounds[1] < 0)
    prior = old['bulk'][str(k)]
    check(f'bulk_{k}_original_polynomial', R[k] == field_decode(prior['polynomial_over_S']))
    check(f'bulk_{k}_original_full_endpoints', bounds == (F(prior['interval_over_S']['lower']), F(prior['interval_over_S']['upper'])))
    check(f'bulk_{k}_original_outer_endpoints', outer == (F(prior['readable_outer_interval_over_S']['lower']), F(prior['readable_outer_interval_over_S']['upper'])))
    bulk[str(k)] = {'polynomial': field_encoding(R[k]), 'full_interval': interval_encoding(bounds),
                    'outer_interval': interval_encoding(outer), 'required': interval_encoding(required[k])}

failures = [name for name, value in checks.items() if not value]
artifact = {'target': "Independent fixed N=6 audit of C029v; no uniform or RH claim",
            'method': 'Sparse rational (t,x,y) polynomial arithmetic modulo y^2=2; Stirling Bernoulli construction; direct monomial multiplication and triangular basis conversion; independent interval Horner',
            'encoding': 'Ascending x=pi powers, rational+sqrt2*sqrt(2); vectors ascending p_k',
            'input_hashes': {str(p.relative_to(here.parent.parent)): hashlib.sha256(p.read_bytes()).hexdigest()
                             for p in [old_path,input_path,Path(__file__)]},
            'bernoulli': list(map(str,bernoulli)), 'u_over_S': list(map(field_encoding,u)),
            'beta_over_S': list(map(field_encoding,beta)),
            'basis': [[str(b.get((j,0,0),F(0))) for j in range(k+1)] for k,b in enumerate(basis)],
            'weights': list(map(str,weights)),
            'multiplication_direct': [[field_encoding(a) for a in col] for col in direct_columns],
            'multiplication_formula': [[field_encoding(a) for a in col] for col in formula_columns],
            'atan5': atan5, 'atan239': atan239,
            'pi_machin_interval': interval_encoding(machin),
            'pi_interval': interval_encoding(pi_bounds), 'sqrt2_interval': interval_encoding(sqrt_bounds),
            'vectors': {name:list(map(field_encoding,values)) for name,values in vectors.items()},
            'bulk':bulk, 'checks':checks, 'failures':failures,
            'result':'PASS' if not failures else 'FAIL'}
output_path = here/'jensen-quadratic-endpoint-audit-2046.json'
output_path.write_text(json.dumps(artifact, indent=2)+'\n')
print(f"{artifact['result']}: {len(checks)-len(failures)}/{len(checks)} exact checks; failures={failures}")
print('Full numerator residual: all 11 coefficients zero =', all(not a for a in numerator_residual))
for k in [2,3,4]:
    print(f'c_{k}: actual outer interval {bulk[str(k)]["outer_interval"]}; required {bulk[str(k)]["required"]}; strict upper<0={checks[f"bulk_{k}_strict_negative"]}')
print('Complete certificate:',output_path.relative_to(here.parent.parent))
raise SystemExit(bool(failures))
