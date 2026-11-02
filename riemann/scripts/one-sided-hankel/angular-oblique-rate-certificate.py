"""Exact rational bounds for the single oblique two-coefficient test."""
from fractions import Fraction as F
import json
from pathlib import Path


class I:
    def __init__(self, lo, hi=None):
        self.lo = F(lo)
        self.hi = self.lo if hi is None else F(hi)
        assert self.lo <= self.hi

    def __add__(self, other):
        other = other if isinstance(other, I) else I(other)
        return I(self.lo + other.lo, self.hi + other.hi)

    __radd__ = __add__

    def __neg__(self):
        return I(-self.hi, -self.lo)

    def __sub__(self, other):
        return self + -(other if isinstance(other, I) else I(other))

    def __rsub__(self, other):
        return I(other) + -self

    def __mul__(self, other):
        other = other if isinstance(other, I) else I(other)
        values = [a*b for a in (self.lo, self.hi)
                  for b in (other.lo, other.hi)]
        return I(min(values), max(values))

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = other if isinstance(other, I) else I(other)
        assert other.lo > 0
        return self * I(1/other.hi, 1/other.lo)


d, U, r, h, K = F(5, 4), F(121, 64), F(1, 2), F(23, 20), F(121, 100)
eps, scale, N = F(1, 10**6), 10**12, 4096
c = I(F(8660254037844386467, 10**19), F(8660254037844386468, 10**19))
assert c.lo*c.lo < F(3, 4) < c.hi*c.hi
failures, checks = [], []


def down(value):
    value *= scale
    return value.numerator // value.denominator


def check(name, actual, relation, required):
    passed = actual > required if relation == '>' else actual < required
    checks.append(dict(name=name, actual=str(actual), relation=relation,
                       required=str(required), passed=passed))
    if not passed:
        failures.append(name)


endpoint_cells = {'-1': [], '1': []}
ellipse_cells = []
for k in range(N):
    t = I(F(k, N), F(k+1, N))
    t2 = t*t
    D1x = d*d + 2*d*c*t + t2
    D2x = U*U + 2*U*d*c*t + d*d*t2
    for sign in (-1, 1):
        D1a = d*d + r*r + (2*d*c-sign*r)*t + t2
        D2a = U*U + U*(2*d*c-sign*r)*t + (d*d+r*r)*t2
        z = D1a*D2x/(D1x*D2a)
        if z.lo <= 1:
            failures.append(f'endpoint ratio not >1: sign={sign}, cell={k}')
        w = (z.lo-1)/(z.lo+1)
        endpoint_cells[str(sign)].append(down(w+w*w*w/3))

    # Q(y)=K*D1(v)*D2(x)-D1(x)*D2(v)=A*y^2-t*B*y+C at Re(v)=-h.
    A = K*D2x-t2*D1x
    B = K*D2x-U*D1x
    C = (K*(h*h+2*h*c*t+t2)*D2x
         -(U*U+2*U*h*c*t+h*h*t2)*D1x)
    discriminant_margin = 4*A*C-t2*B*B
    ellipse_cells.append([down(A.lo), down(discriminant_margin.lo)])
    if A.lo <= 0 or discriminant_margin.lo <= 0:
        failures.append(f'ellipse quadratic positivity: cell={k}')

endpoint_bounds = {sign: F(sum(rows), N*scale)
                   for sign, rows in endpoint_cells.items()}
for sign, bound in endpoint_bounds.items():
    check(f'endpoint integral lower bound, sign {sign}', bound, '>', F(9, 250))

# Uniform elementary margins used by the analytic proof, all rational.
check('cos lower enclosure', c.lo, '>', F(433, 500))
check('connector radius upper', F(53, 16), '<', F(73, 40)**2)
connector_ratio = ((F(7, 4)+F(433, 1000))/(F(7, 4))
                   * (U+F(433, 800))/(U+F(73, 80)))
connector_rate = (1-1/connector_ratio)/2
check('connector rate before angular loss', connector_rate, '>', F(3, 80))
check('rectangle p numerator lower', (U-1)*d*(U-F(1, 2)), '>', F(3, 2))
check('rectangle p denominator upper',
      (F(73, 40)+1)**2*(U+F(73, 40))**2, '<', F(111))
check('rectangle real p after angular loss', F(3, 222)-2*eps, '>', F(1, 100))
check('ellipse p numerator positive',
      (U-1)*h*(U-F(51, 100)), '>', F(0))
check('ellipse sqrt bound', F(26, 100), '<', F(51, 100)**2)
check('log rho lower comparison', 26*F(1961, 10000)**2, '<', F(1))
ellipse_rate = F(2, 3)*F(1961, 10000)-F(143, 1500)-4*eps
check('ellipse remainder rate', ellipse_rate, '>', F(7, 200))
check('endpoint rate after angular loss', F(9, 250)-4*eps, '>', F(7, 200))
check('connector rate after angular loss', F(3, 80)-4*eps, '>', F(7, 200))
check('coefficient upper decay exceeds target', F(7, 200), '>', F(1, 32))
check('angular log-factor bound', 1/h+2/U, '<', F(2))
check('angular p derivative bound', 1/(d*d)+1/U, '<', F(2))
check('uniform horizontal p bound', 1/d+1/U, '<', F(2))
check('finite-n endpoint quadrature Lipschitz bound', 2/d+(F(11, 8)+d)/U, '<', F(4))

certificate = {
    'kind': 'exact rational interval certificate; no floating-point premises',
    'scope': 'Oblique r=1/2 endpoint rates, ellipse quadratic and elementary margins only; analytic contour argument is separate.',
    'parameters': {'d': str(d), 'U': str(U), 'r': str(r), 'h': str(h),
                   'K': str(K), 'epsilon': str(eps),
                   'cos_interval': [str(c.lo), str(c.hi)],
                   'cos_squared_enclosure': [str(c.lo*c.lo), '3/4', str(c.hi*c.hi)]},
    'subintervals': N,
    'downward_rounding_scale': scale,
    'endpoint_integral_lower_bounds': {s: str(v) for s, v in endpoint_bounds.items()},
    'endpoint_required_lower_bound': '9/250',
    'endpoint_cell_lower_scaled': endpoint_cells,
    'ellipse_cell_lower_scaled': ellipse_cells,
    'ellipse_minimum_lower_bounds': {
        'A': str(F(min(v[0] for v in ellipse_cells), scale)),
        '4AC_minus_t2B2': str(F(min(v[1] for v in ellipse_cells), scale))},
    'auxiliary_rational_checks': checks,
    'failures': failures,
}
path = Path(__file__).with_suffix('.json')
path.write_text(json.dumps(certificate, indent=2)+'\n')
for sign, value in endpoint_bounds.items():
    print(f'Endpoint {sign}: lower rate {value} ({float(value):.12f}); required > 9/250 = .036')
print('Ellipse minima:', certificate['ellipse_minimum_lower_bounds'], '; required both > 0')
print(f'Finite-node decay: {ellipse_rate} ({float(ellipse_rate):.12f}); required > 7/200 = .035')
print(f'Checks passed: {sum(v["passed"] for v in checks)}/{len(checks)}; failures: {failures}; certificate: {path}')
if failures:
    raise SystemExit(1)
