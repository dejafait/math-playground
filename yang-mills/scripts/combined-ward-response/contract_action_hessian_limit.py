"""Exact finite-row contraction of L173(8); no numerical heat evaluation.

Coordinates are positive-edge tails in Z^4, directions 0..3. The scalar
Green values remain formal symbols modulo coordinate signs/permutations.
All rational records and verification failures are written to disk.
"""
from collections import defaultdict
from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations, product
from pathlib import Path
import json

ZERO = (0,)*4
PLANES = tuple(combinations(range(4), 2))

def shift(z, mu, n=1):
    return tuple(v + (n if j == mu else 0) for j, v in enumerate(z))

def clean(row):
    return {k: v for k, v in row.items() if v}

def add_to(out, row, factor=F(1)):
    for key, value in row.items():
        out[key] += factor*value

@lru_cache(None)
def curl(z, mu, nu):
    if mu == nu:
        return {}
    return {(z, nu): F(-1), (shift(z, mu), nu): F(1),
            (z, mu): F(1), (shift(z, nu), mu): F(-1)}

@lru_cache(None)
def clover(z, mu, nu):
    out = defaultdict(F)
    for a, b in product((0, -1), repeat=2):
        add_to(out, curl(shift(shift(z, mu, a), nu, b), mu, nu), F(1, 4))
    return clean(out)

@lru_cache(None)
def laplace(edge):
    z, mu = edge
    out = defaultdict(F)
    for rho in range(4):
        if rho == mu:
            continue
        for corner in (z, shift(z, rho, -1)):
            row = curl(corner, rho, mu)
            add_to(out, row, row[edge])
    return clean(out)

def vertex_value(z, rho, j, center):
    return F(1) if j is None else F(z[j])-center[j]

def generator(edge, rho, j, center):
    z, mu = edge
    if rho == mu:
        return {}
    out = defaultdict(F)
    for v in (z, shift(z, mu)):
        add_to(out, clover(v, rho, mu), vertex_value(v, rho, j, center)/2)
    return clean(out)

@lru_cache(None)
def generator_column_support(edge):
    """Possible k output edges, obtained from exact translated row supports."""
    z, mu = edge
    output = set()
    for nu in range(4):
        for rho in range(4):
            # Use uncollected vertex supports; an affine coefficient must not
            # lose an entry that cancels only for constant displacement.
            for v in (ZERO, shift(ZERO, nu)):
                for (t, sigma) in clover(v, rho, nu):
                    if sigma == mu:
                        output.add((tuple(a-b for a, b in zip(z, t)), nu))
    return tuple(sorted(output))

def residual_generator(edge, rho, j):
    z, mu = edge
    center = tuple(F(v)+F(k == mu, 2) for k, v in enumerate(z))
    out = defaultdict(F)
    for b, coefficient in laplace(edge).items():
        add_to(out, generator(b, rho, j, center), coefficient/2)
    for b in generator_column_support(edge):
        coefficient = generator(b, rho, j, center).get(edge, F(0))
        if coefficient:
            add_to(out, laplace(b), coefficient/2)
    return clean(out)

def insertion(edge, rho, j):
    """Constant-strain Q3+Q6 for the gradient partial_j u_rho."""
    z, direction = edge
    out = defaultdict(F)
    if rho == j:
        for other in range(4):
            if other == direction or rho not in (other, direction):
                continue
            for corner in (z, shift(z, other, -1)):
                row = curl(corner, other, direction)
                add_to(out, row, row[edge])
    if rho != j:
        mu, nu = sorted((rho, j))
        vertices = set()
        for alpha in range(4):
            if alpha in (mu, nu):
                continue
            for first in (mu, nu):
                for (t, sigma) in clover(ZERO, first, alpha):
                    if sigma == direction:
                        vertices.add(tuple(a-b for a, b in zip(z, t)))
        for v in vertices:
            for alpha in range(4):
                if alpha in (mu, nu):
                    continue
                left, right = clover(v, mu, alpha), clover(v, nu, alpha)
                add_to(out, right, left.get(edge, F(0))/2)
                add_to(out, left, right.get(edge, F(0))/2)
    return clean(out)

def green_key(t):
    return tuple(sorted(abs(v) for v in t[1:]))

def endpoint_kernel(edge, other, slope=False):
    z, mu = edge
    t, nu = other
    center1 = F(z[0])+F(mu == 0, 2)
    out = defaultdict(F)
    for v, w in product((t, shift(t, nu)), (z, shift(z, mu))):
        delta = tuple(a-b for a, b in zip(v, w))
        coefficient = (F(v[0]+w[0], 2)-center1) if slope else F(1)
        out[green_key(delta)] += coefficient
    return clean(out)

def encoded(row):
    return {','.join(map(str, key)): str(value) for key, value in sorted(row.items()) if value}

def contract(row, edge, nu, moment=None, slope=False):
    out = defaultdict(F)
    z, mu = edge
    for other, coefficient in row.items():
        t, sigma = other
        if sigma != nu:
            continue
        if moment is not None:
            coefficient *= F(t[moment]-z[moment])+F(sigma == moment, 2)-F(mu == moment, 2)
        add_to(out, endpoint_kernel(edge, other, slope), coefficient)
    return clean(out)

def row_moment(row, j):
    return sum(value*(F(t[j])+F(mu == j, 2)) for (t, mu), value in row.items())

records, checks, full_rows = [], [], []

def encode_edge_row(row):
    return {','.join(map(str, t+(mu,))): str(v) for (t, mu), v in sorted(row.items())}

def gauge_check(row, label):
    vertex = defaultdict(F)
    for (t, mu), value in row.items():
        vertex[t] -= value
        vertex[shift(t, mu)] += value
    error = clean(vertex)
    checks.append(dict(name=label, actual=encoded(error), required={}, passed=not error))

for mu in range(1, 4):
    edge = (ZERO, mu)
    for rho in range(4):
        principal = residual_generator(edge, rho, None)
        full_rows.append(dict(kind='principal', mu=mu+1, rho=rho+1, row=encode_edge_row(principal)))
        gauge_check(principal, f'principal-gauge-{mu+1}-{rho+1}')
        for nu in range(1, 4):
            frozen = contract(principal, edge, nu)
            checks.append(dict(name=f'frozen-{mu+1}-{nu+1}-u{rho+1}', actual=encoded(frozen), required={}, passed=not frozen))
            records.append(dict(kind='slope', mu=mu+1, nu=nu+1, rho=rho+1,
                                coefficients=encoded(contract(principal, edge, nu, slope=True))))
            for j in range(4):
                records.append(dict(kind='exterior', mu=mu+1, nu=nu+1, rho=rho+1, j=j+1,
                                    coefficients=encoded(contract(principal, edge, nu, moment=j))))
        for j in range(4):
            row = defaultdict(F)
            gen, qrow = residual_generator(edge, rho, j), insertion(edge, rho, j)
            add_to(row, gen)
            add_to(row, qrow, F(-1))
            row = clean(row)
            full_rows.append(dict(kind='affine', mu=mu+1, rho=rho+1, j=j+1,
                                  generator_row=encode_edge_row(gen), insertion_row=encode_edge_row(qrow), row=encode_edge_row(row)))
            gauge_check(row, f'affine-gauge-{mu+1}-{rho+1}-{j+1}')
            # Residual annihilates constant smooth fields for trace-free strain.
            # Full affine-generator rows, including non-trace-free test gradients,
            # remain saved; div u=0 is used only in the subsequent reduction.
            for nu in range(1, 4):
                records.append(dict(kind='strain', mu=mu+1, nu=nu+1, rho=rho+1, j=j+1,
                                    coefficients=encoded(contract(row, edge, nu))))

# Include the original coefficient -6 exactly once.
for row in records:
    row['coefficients'] = {k: str(-6*F(v)) for k, v in row['coefficients'].items()}

# Compact-support IBP turns d (partial_j u_rho) H_(nu mu) into
# -d u_rho (J_(nu mu;j)+J_(mu nu;j)) -delta_j1 u_rho H_(nu mu).
assembled = defaultdict(lambda: defaultdict(F))
for row in records:
    mu, nu, rho = row['mu'], row['nu'], row['rho']
    poly = {tuple(map(int, k.split(','))): F(v) for k, v in row['coefficients'].items()}
    if row['kind'] == 'strain':
        j = row['j']
        add_to(assembled[('derivative', rho, nu, mu, j)], poly, F(-1))
        add_to(assembled[('derivative', rho, mu, nu, j)], poly, F(-1))
        if j == 1:
            add_to(assembled[('value', rho, min(mu, nu), max(mu, nu))], poly, F(-1))
    elif row['kind'] == 'exterior':
        add_to(assembled[('derivative', rho, nu, mu, row['j'])], poly)
    else:
        add_to(assembled[('value', rho, min(mu, nu), max(mu, nu))], poly)

complete = {','.join(map(str, key)): encoded(poly) for key, poly in sorted(assembled.items()) if clean(poly)}

# Delta g = delta_0 at 000, 001, 011 and 111, with exact cubic symmetry.
# Coordinates of each triple are [constant, X, Y, g000].
GREEN = {(0,0,0): (0,0,0,1), (0,0,1): (F(-1,6),0,0,1),
         (0,0,2): (-1,4,0,1), (0,1,1): (0,-1,0,1),
         (0,1,2): (F(1,6),-2,1,1), (1,1,1): (0,-1,-1,1),
         (1,1,2): (0,-1,-2,1)}

def reduced(poly):
    return tuple(sum(value*GREEN[key][j] for key, value in poly.items()) for j in range(4))

expected = {
    'A': (16,-120,12,0), 'B': (8,-60,6,0),
    'C': (8,-120,-12,0), 'D': (-6,0,-48,0),
    'E': (-9,48,24,0), 'F': (3,-12,-6,0)}
required_assembled = {}
for r in range(2,5):
    required_assembled[('derivative',1,r,r,1)] = expected['A']
    required_assembled[('value',1,r,r)] = expected['B']
    required_assembled[('derivative',r,r,r,r)] = expected['C']
    for k in range(2,5):
        if k != r:
            required_assembled[('derivative',r,k,k,r)] = expected['D']
            required_assembled[('derivative',r,r,k,k)] = expected['E']
            required_assembled[('derivative',r,k,r,k)] = expected['F']
for key in set(assembled) | set(required_assembled):
    actual = reduced(clean(assembled[key]))
    required = required_assembled.get(key, (0,0,0,0))
    checks.append(dict(name='complete-tensor-'+','.join(map(str,key)), actual=list(map(str,actual)),
                       required=list(map(str,required)), passed=actual == required))

# Necessary Green recurrences are checked as affine symbolic identities.
for point, required in [((0,0,0), 1), ((0,0,1),0), ((0,1,1),0), ((1,1,1),0)]:
    row = defaultdict(F)
    row[point] += 6
    for j in range(3):
        for sign in (-1,1):
            neighbor = tuple(v+(sign if k == j else 0) for k,v in enumerate(point))
            row[tuple(sorted(map(abs, neighbor)))] -= 1
    actual = reduced(clean(row))
    needed = (required,0,0,0)
    checks.append(dict(name='Green-recurrence-'+','.join(map(str,point)), actual=list(map(str,actual)),
                       required=list(map(str,needed)), passed=actual == needed))

# Import L154's established full-cell Green intervals, not decimal previews.
source = Path(__file__).with_name('quartic-residual-coefficient-certificate.json')
bounds = json.loads(source.read_text())['bounds']
xy = {row['name']: (F(row['lower']), F(row['upper'])) for row in bounds}

def affine_interval(coefficient):
    result = [F(coefficient[0])]*2
    for scale, name in zip(coefficient[1:3], ('X','Y')):
        l, h = xy[name]
        result[0] += min(scale*l, scale*h)
        result[1] += max(scale*l, scale*h)
    return result

physical_coefficients = {'D': (17,-90,15), 'A': (-10,78,-9),
                         'X': (F(-3,2),6,3), 'C': (12,-60,-30)}
form_transform = {
    'D': {'A':F(1,2),'D':F(-1,2),'E':F(-1,2),'F':F(1,2)},
    'A': {'C':F(-1,2),'D':F(1,2),'E':F(1,2),'F':F(1,2)},
    'X': {'F':F(-1,2)}, 'C': {'E':F(-1),'F':F(1)},
    'B_R': {'A':F(-1,2),'B':F(1)}}
for label, transformation in form_transform.items():
    actual = tuple(sum(scale*expected[key][j] for key,scale in transformation.items()) for j in range(4))
    required = physical_coefficients.get(label,(0,0,0))+(0,)
    checks.append(dict(name='physical-form-'+label, actual=list(map(str,actual)),
                       required=list(map(str,required)), passed=actual == required))
heat = {
    3: {'D': ('2359.1','2359.2'), 'A': ('19170.0','19170.1'), 'X': ('29198.8','29198.9'), 'C': ('1024.8','1024.9')},
    6: {'D': ('703.6','703.7'), 'A': ('-4195.9','-4195.8'), 'X': ('69177.0','69177.1'), 'C': ('3218.2','3218.3')}}
intervals = {key: affine_interval(c) for key,c in physical_coefficients.items()}
enclosures = []
for i in (3,6):
    lower = upper = F(0)
    for key, (l,h) in intervals.items():
        values = [x*F(y) for x in (l,h) for y in heat[i][key]]
        lower += min(values)
        upper += max(values)
    desired = (F(84000),F(100000)) if i == 3 else (F(-47000),F(-38000))
    passed = desired[0] < lower <= upper < desired[1]
    enclosures.append(dict(probe=i, exact_lower=str(lower), exact_upper=str(upper), required=list(map(str,desired)), passed=passed))
    checks.append(dict(name=f'qualified-actual-probe-{i}', actual=[str(lower),str(upper)], required=list(map(str,desired)), passed=passed))

certificate = dict(description='L173 full finite rows before and after compact-support IBP; formal scalar Green coefficients',
                   arithmetic='exact Fraction rows/recombination; existing qualified heat intervals are imported premises', outside_factor=-6,
                   records=records, full_rows=full_rows, checks=checks, assembled=complete,
                   reduced_six_form_coefficients={k: list(map(str,v)) for k,v in expected.items()},
                   physical_coefficients={k: list(map(str,v)) for k,v in physical_coefficients.items()},
                   imported_Green_bounds=bounds, imported_heat_intervals=heat,
                   qualification='Enclosures import L133 full heat bounds under its IEEE assumptions; no independent heat/cell audit here.',
                   enclosures=enclosures,
                   all_checks_passed=all(row['passed'] for row in checks))
path = Path(__file__).with_name('action-hessian-limit-contraction-certificate.json')
path.write_text(json.dumps(certificate, indent=2)+'\n')
print(f'Exact row/tensor/Green/qualified-interval checks: {sum(r["passed"] for r in checks)}/{len(checks)}; required all pass')
print(f'Complete records: {len(records)}; nonzero assembled tensors: {len(complete)}')
for row in enclosures:
    print(f'Probe {row["probe"]}: actual [{float(F(row["exact_lower"])):.6f}, {float(F(row["exact_upper"])):.6f}], required {row["required"]}; pass={row["passed"]}')
print('Failures:', [row['name'] for row in checks if not row['passed']])
print(f'Certificate: {path}')
if not certificate['all_checks_passed']:
    raise SystemExit('FAIL: frozen parity row check')
