"""Exact common-denominator scalar recombination for L219(2).

No floating point or quadrature. Full polynomial certificates are saved.
The common denominator is L^2, L=X+Y+Z, X_j=2-2cos(theta_j).
"""
from fractions import Fraction as F
from itertools import permutations
from pathlib import Path
from math import comb
import json
import hashlib


class P:
    def __init__(self, value=0):
        self.c = (value if isinstance(value, dict)
                  else {(0, 0, 0): F(value)} if value else {})
        self.c = {e: F(c) for e, c in self.c.items() if c}

    def __add__(self, other):
        other = other if isinstance(other, P) else P(other)
        out = self.c.copy()
        for e, c in other.c.items():
            out[e] = out.get(e, F(0)) + c
        return P(out)

    __radd__ = __add__

    def __neg__(self):
        return P({e: -c for e, c in self.c.items()})

    def __sub__(self, other):
        return self + (-other if isinstance(other, P) else -P(other))

    def __rsub__(self, other):
        return P(other) + (-self)

    def __mul__(self, other):
        other = other if isinstance(other, P) else P(other)
        out = {}
        for e, c in self.c.items():
            for h, v in other.c.items():
                k = tuple(a+b for a, b in zip(e, h))
                out[k] = out.get(k, F(0)) + c*v
        return P(out)

    __rmul__ = __mul__

    def __truediv__(self, scalar):
        return self * (1/F(scalar))

    def __pow__(self, n):
        out = P(1)
        for _ in range(n):
            out = out*self
        return out

    def permute(self, p):
        return P({tuple(e[j] for j in p): c for e, c in self.c.items()})

    def sym(self):
        return sum((self.permute(p) for p in permutations(range(3))), P())/6

    def derivative(self, j):
        out = {}
        for e, c in self.c.items():
            if e[j]:
                h = list(e)
                h[j] -= 1
                out[tuple(h)] = c*e[j]
        return P(out)

    def data(self):
        return [{'powers': list(e), 'coefficient': str(c)}
                for e, c in sorted(self.c.items())]


X, Y, Z = [P({tuple(int(k == j) for k in range(3)): 1}) for j in range(3)]
v = [X, Y, Z]
L = X+Y+Z
a, b, c = 1-X/4, 1-Y/4, 1-Z/4
filters = [a, b, c]
# All entries are NUMERATORS over L^2. Gx,Gy are L154's Green
# differences; X,Y,Z here always denote frequency energies instead.
scalars = {
    'Gx': ((X+Y)/2-X*Y/4)*L,
    'Gy': (1-X/2)*(1-Y/2)*Z*L/2,
    'g': -X*Y*(X-Y)**2/4,
    'gamma': (L*sum((v[j]*filters[j]**2 for j in range(3)), P())
              -sum((v[j]*filters[j] for j in range(3)), P())**2)/3,
    'aQ': 4*a*Y*L,
    'tax': 4*(L**2*sum((f**2 for f in filters), P())
              -2*L*sum((v[j]*filters[j]**2 for j in range(3)), P())
              +sum((v[j]*filters[j] for j in range(3)), P())**2)/3,
    'hD': X*(4+Z)*b**2*L/2-2*a*b*Z*(b*(X+Z)+c*Y),
    'hX': a*b*Z*((b+c)*(X+Z)+2*c*Y),
    'tau': -a*b*Z*(Y*L+(Y-Z)*(X+Z)/2),
    'xi': a*Y*Z*(Z-Y)**2/8,
}
scalars['hA'] = 2*a*(b*Y+c*Z)*L-scalars['hD']-2*scalars['hX']
s = scalars
coefficients = {
    'P_D': F(17, 2)*L**2-45*s['Gx']+F(15, 2)*s['Gy']
           +F(3, 2)*s['tax']-3*s['aQ']+3*s['hD']+3*s['tau']-F(3, 2)*s['g'],
    'P_A': -F(9, 2)*L**2+39*s['Gx']-F(9, 2)*s['Gy']-3*s['aQ']+3*s['hA'],
    'P_X': -L**2+3*s['Gx']+F(3, 2)*s['Gy']+3*s['hX']-F(3, 2)*s['tau'],
    'P_C': 6*L**2-30*s['Gx']-15*s['Gy']+3*s['xi']+6*s['tau'],
    'B_R': 14*L**2-72*s['Gx']+6*s['Gy']-3*s['g'],
    'D': 12*s['gamma']+3*s['g'],
}
result = {
    'scope': 'L219(2), exact linked full coefficients; no numerical evaluation',
    'denominator': '(X+Y+Z)^2',
    'scalar_numerators': {k: p.data() for k, p in scalars.items()},
    'coefficient_numerators': {k: p.data() for k, p in coefficients.items()},
    'permutation_averages': {k: p.sym().data() for k, p in coefficients.items()},
    'failures': [],
}


def solve(columns, target):
    """Rational elimination; return a solution and full residual polynomial."""
    monomials = sorted(set(target.c).union(*(set(p.c) for p in columns)))
    rows = [[p.c.get(e, F(0)) for p in columns]+[target.c.get(e, F(0))]
            for e in monomials]
    pivots, row = [], 0
    for col in range(len(columns)):
        pivot = next((j for j in range(row, len(rows)) if rows[j][col]), None)
        if pivot is None:
            continue
        rows[row], rows[pivot] = rows[pivot], rows[row]
        d = rows[row][col]
        rows[row] = [x/d for x in rows[row]]
        for j in range(len(rows)):
            if j != row and rows[j][col]:
                d = rows[j][col]
                rows[j] = [x-d*y for x, y in zip(rows[j], rows[row])]
        pivots.append(col)
        row += 1
    ans = [F(0)]*len(columns)
    for j, col in enumerate(pivots):
        ans[col] = rows[j][-1]
    residual = target-sum((a*p for a, p in zip(ans, columns)), P())
    return ans, residual


# The full-torus integral of each basis entry divided by L^2 is zero.
# Divergences are derivatives of 2 sin(theta_2) p(X,Y,Z)/L,
# averaged over all permutations. Polynomial moments use
# integral (2-2cos(theta))^n = binomial(2n,n).
basis, names = [], []
for total in range(4):
    for i in range(total+1):
        for j in range(total-i+1):
            k = total-i-j
            p = X**i*Y**j*Z**k
            div = ((2-X)*L*p+X*(4-X)*(L*p.derivative(0)-p)).sym()
            basis.append(div)
            names.append(dict(kind='divergence', monomial=[i, j, k]))
            if total:
                moment = comb(2*i, i)*comb(2*j, j)*comb(2*k, k)
                basis.append((L**2*(p-moment)).sym())
                names.append(dict(kind='zero_mean_polynomial', monomial=[i, j, k],
                                  moment=str(moment)))
result['zero_integral_basis'] = [dict(**name, numerator=p.data())
                                 for name, p in zip(names, basis)]
result['integral_identity_checks'] = {}
for name, p in coefficients.items():
    solution, residual = solve(basis, p.sym())
    result['integral_identity_checks'][name] = dict(
        solution=[dict(index=j, coefficient=str(a)) for j, a in enumerate(solution) if a],
        complete_residual=residual.data(), passed=not residual.c)

# Fixed small identities used in the canonical proof, independently of
# which pivots the exploratory elimination above selected.
M1 = (L**2*(Z-2)).sym()
M2 = (L**2*(Y*Z-4)).sym()


def div(p):
    return ((2-X)*L*p+X*(4-X)*(L*p.derivative(0)-p)).sym()


rhs = {
    'P_D': F(3, 2)*M1+F(9, 16)*M2,
    'P_A': -F(3, 2)*M1-F(3, 16)*M2,
    'P_X': -F(3, 2)*M1+F(3, 16)*M2,
    'P_C': 3*M1+M2/8+div(Y*Z**2)/4+div(X*Y*Z)/8,
    'B_R': 6*M1-3*div(Z**2)-F(3, 2)*div(Y*Z)-F(3, 4)*M2,
    'D': P(),
}
result['fixed_identity_checks'] = {
    k: dict(actual_numerator=coefficients[k].sym().data(),
            required_numerator=p.data(),
            complete_defect=(coefficients[k].sym()-p).data(),
            passed=not (coefficients[k].sym()-p).c)
    for k, p in rhs.items()}

# Reconstruct the common-denominator coefficients directly from the
# imported group formulas, before cancellations. Include B_G explicitly.
groups = {
    'Lambda': {
        'P_D': -F(17, 2)*L**2+45*s['Gx']-F(15, 2)*s['Gy'],
        'P_A': 5*L**2-39*s['Gx']+F(9, 2)*s['Gy'],
        'P_X': F(3, 4)*L**2-3*s['Gx']-F(3, 2)*s['Gy'],
        'P_C': -6*L**2+30*s['Gx']+15*s['Gy'],
        'B_R': 14*L**2-72*s['Gx']+6*s['Gy']},
    'T': {
        'P_D': 17*L**2-90*s['Gx']+15*s['Gy'],
        'P_A': -10*L**2+78*s['Gx']-9*s['Gy'],
        'P_X': -F(3, 2)*L**2+6*s['Gx']+3*s['Gy'],
        'P_C': 12*L**2-60*s['Gx']-30*s['Gy']},
    'Vmix': {'B_G': -3*s['g'], 'D': 3*s['g'],
             'B_R': F(3, 2)*s['g'], 'P_D': -F(3, 2)*s['g']},
    '3ax': {'P_D': F(3, 2)*s['tax']},
    '-3Q': {'P_D': -3*s['aQ'], 'P_A': -3*s['aQ']+L**2/2,
             'P_X': -L**2/4},
    '3G': {'B_G': 3*s['g']},
    '-9R/2': {'B_R': -F(9, 2)*s['g']},
    '3tr': {'P_D': 3*s['hD']+3*s['tau'],
             'P_A': 3*s['hA'], 'P_X': 3*s['hX']-F(3, 2)*s['tau'],
             'P_C': 3*s['xi']+6*s['tau']},
    '12gammaD': {'D': 12*s['gamma']},
}
result['assembly_checks'] = {}
for name in [*coefficients, 'B_G']:
    actual = sum((g.get(name, P()) for g in groups.values()), P())
    wanted = coefficients.get(name, P())
    result['assembly_checks'][name] = dict(
        complete_defect=(actual-wanted).data(), passed=not (actual-wanted).c)
result['failures'] = [section+'/'+name
                      for section in ('assembly_checks', 'fixed_identity_checks',
                                      'integral_identity_checks')
                      for name, check in result[section].items() if not check['passed']]
result['required'] = 'all 19 assembly and scalar checks pass with zero complete defects'
result['actual'] = {'assembly_checks': len(result['assembly_checks']),
                    'fixed_identity_checks': len(result['fixed_identity_checks']),
                    'integral_identity_checks': len(result['integral_identity_checks']),
                    'failure_count': len(result['failures'])}
result['script_sha256'] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()

if __name__ == '__main__':
    dest = Path(__file__).with_name('complete-linked-coefficient-certificate.json')
    dest.write_text(json.dumps(result, indent=2)+'\n')
    for k, p in coefficients.items():
        print(k, 'permutation-averaged numerator terms:', len(p.sym().c),
              '; exact divergence/moment residual terms:',
              len(result['integral_identity_checks'][k]['complete_residual']),
              '; required for cancellation: 0')
    print('Full certificate:', dest)
    print('Actual checks:', result['actual'], '; required failures: 0')
    print('Failures:', result['failures'])
    if result['failures']:
        raise SystemExit(1)
