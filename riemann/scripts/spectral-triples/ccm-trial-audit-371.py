"""Independent directed-Decimal reconstruction of every L761 enclosure.

No code is imported from the generator. Exact saved rational candidates
are the only candidate input. Analytic justification is in L761 section 6.
The output retains all reconstructed intervals; stdout is only a summary.
"""
from decimal import Decimal as D, Context, ROUND_FLOOR, ROUND_CEILING
from fractions import Fraction
from math import comb
from pathlib import Path
import hashlib
import json
import time

HERE = Path(__file__).resolve().parent
SOURCE = HERE / 'ccm-trial-certificate-369.json'
GENERATOR = HERE / 'ccm-trial-certificate-369.py'
BASE = HERE / 'finite-parity-359.py'
OUTPUT = Path(__file__).with_suffix('.json')
down = Context(prec=320, rounding=ROUND_FLOOR)
up = Context(prec=320, rounding=ROUND_CEILING)
started = time.monotonic()
data = json.loads(SOURCE.read_text())
report = dict(outcome='IN_PROGRESS', failures=[], checks={},
              input_sha256=hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
              script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              precision=320, interval_implementation='independent; no AST imports',
              constants={}, operator={}, counts={}, modes={}, trial={}, projection={})


def save():
    report['elapsed_seconds'] = time.monotonic() - started
    OUTPUT.write_text(json.dumps(report, indent=2) + '\n')


def require(condition, name):
    report['checks'][name] = bool(condition)
    if not condition:
        report['failures'].append(name)
        save()
        raise ArithmeticError(name)


class Ball:
    def __init__(self, a=0, b=None):
        if isinstance(a, Ball):
            self.a, self.b = a.a, a.b
        else:
            self.a, self.b = D(a), D(a if b is None else b)
        assert self.a.is_finite() and self.b.is_finite() and self.a <= self.b

    def __add__(self, other):
        other = Ball(other)
        return Ball(down.add(self.a, other.a), up.add(self.b, other.b))

    __radd__ = __add__

    def __neg__(self):
        return Ball(self.b.copy_negate(), self.a.copy_negate())

    def __sub__(self, other):
        return self + -Ball(other)

    def __rsub__(self, other):
        return Ball(other) - self

    def __mul__(self, other):
        other = Ball(other)
        return Ball(min(down.multiply(x, y) for x in (self.a, self.b)
                        for y in (other.a, other.b)),
                    max(up.multiply(x, y) for x in (self.a, self.b)
                        for y in (other.a, other.b)))

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = Ball(other)
        assert other.a > 0 or other.b < 0
        return Ball(min(down.divide(x, y) for x in (self.a, self.b)
                        for y in (other.a, other.b)),
                    max(up.divide(x, y) for x in (self.a, self.b)
                        for y in (other.a, other.b)))

    def __rtruediv__(self, other):
        return Ball(other) / self

    def sq(self):
        aa = [down.multiply(x, x) for x in (self.a, self.b)]
        bb = [up.multiply(x, x) for x in (self.a, self.b)]
        return Ball(0 if self.a <= 0 <= self.b else min(aa), max(bb))

    def sqrt(self):
        assert self.a >= 0
        return Ball(max(D(0), down.next_minus(down.sqrt(self.a))),
                    up.next_plus(up.sqrt(self.b)))

    def ln(self):
        assert self.a > 0
        return Ball(down.next_minus(down.ln(self.a)), up.next_plus(up.ln(self.b)))

    def absmax(self):
        return max(self.a.copy_abs(), self.b.copy_abs())

    def inflate(self, e):
        e = Ball(e).absmax()
        return Ball(down.subtract(self.a, e), up.add(self.b, e))

    def pair(self):
        return [str(self.a), str(self.b)]


def readpair(pair):
    assert len(pair) == 2
    return Ball(*pair)


def contained(new, old, name):
    old = readpair(old)
    require(old.a <= new.a <= new.b <= old.b, name)


def norm(vec):
    return sum((x.sq() for x in vec), Ball()).sqrt()


def atan_inverse(k):
    z = Ball(1)/k
    power, total = z, Ball()
    for n in range(620):
        total += (power if n % 2 == 0 else -power)/(2*n+1)
        power *= z.sq()
    return total.inflate(power/1241)


def phase(turns, pi):
    # Any integer shift preserves the exact phase; avoid midpoint rounding.
    shift = int(turns.a)
    y = 2*pi*(turns-shift)
    # A floor-like shift gives |y|<2*pi, so use an explicit |y|<7 budget.
    require(y.absmax() < 7, 'all_reduced_angles_below_7')
    st, ct = y, Ball(1)
    ss, cs = st, ct
    yy = y.sq()
    for n in range(1, 320):
        st = -st*yy/((2*n)*(2*n+1))
        ct = -ct*yy/((2*n-1)*(2*n))
        ss += st
        cs += ct
    # Omitted ratios <=49/(639*640)<1/2.
    return ss.inflate(2*st*yy/(640*641)), cs.inflate(2*ct*yy/(639*640))


try:
    require(data['outcome'] == 'CERTIFIED_TRIAL_PROJECTION'
            and not data['failures'] and all(data['checks'].values()), 'source_checks')
    require(data['script_sha256'] == hashlib.sha256(GENERATOR.read_bytes()).hexdigest(),
            'generator_binding')
    require(data['interval_source_sha256'] == hashlib.sha256(BASE.read_bytes()).hexdigest(),
            'interval_source_binding')
    require(data['parameters'] == dict(lambda_squared=13, N=120, even_dimension=112,
            max_degree=222, interval_precision=260, candidate_precision=240), 'parameters')
    # tan(atan(1/2)+atan(1/3))=1 and the sum is in (0,pi/2).
    pi = 4*(atan_inverse(2)+atan_inverse(3))
    lam, L = Ball(13).sqrt(), Ball(13).ln()
    c2 = (26*pi).sq()
    for key, value in dict(pi=pi, lam=lam, L=L, c2=c2).items():
        contained(value, data['constants'][key], 'constant_'+key)
        report['constants'][key] = value.pair()
    aa, bb = [], []
    for k in range(112):
        j = 2*k
        aa.append(j*(j+1)+c2*(2*j*(j+1)-1)/((2*j+3)*(2*j-1)))
        bb.append(c2*(j+1)*(j+2)/((2*j+3)*Ball((2*j+1)*(2*j+5)).sqrt()))
    for name, values in [('diagonal', aa), ('off_diagonal_including_omitted_coupling', bb)]:
        require(len(data['operator'][name]) == 112, 'operator_length_'+name)
        for k, value in enumerate(values):
            contained(value, data['operator'][name][k], name+'_'+str(k))
        report['operator'][name] = [v.pair() for v in values]
    require(data['operator']['tail_floor'] == 224*225 == 50400, 'omitted_floor')
    for t, expected in [(80, 0), (82, 1), (723, 2), (726, 3)]:
        report['counts'][str(t)] = {}
        require(data['infinite_counts'][str(t)]['infinite_negative'] == expected,
                'saved_infinite_count_'+str(t))
        for side, correction in [('upper', Ball()), ('lower', bb[-1].sq()/(50400-t))]:
            saved = data['infinite_counts'][str(t)][side]
            contained(correction, saved['last_diagonal_correction'], side+'_correction_'+str(t))
            require(len(saved['pivots']) == 112, side+'_pivot_count_'+str(t))
            determinants, pivots = [], []
            previous, previous2, lastsign, changes = Ball(1), Ball(), 1, 0
            for k in range(112):
                current = (aa[k]-t-(correction if k == 111 else Ball()))*previous
                if k:
                    current -= bb[k-1].sq()*previous2
                require(current.a > 0 or current.b < 0, f'{side}_{t}_det_{k}_nonzero')
                pivot = current/previous
                contained(pivot, saved['pivots'][k], f'{side}_{t}_pivot_{k}')
                sign = 1 if current.a > 0 else -1
                changes += int(sign != lastsign)
                lastsign = sign
                previous2, previous = previous, current
                determinants.append(current.pair())
                pivots.append(pivot.pair())
            require(changes == saved['negative'] == expected, f'{side}_{t}_inertia')
            report['counts'][str(t)][side] = dict(count=changes,
                correction=correction.pair(), determinants=determinants, pivots=pivots)
    save()
    print('All 224 operator entries and 896 pivots reconstructed; infinite count inputs pass.', flush=True)
    modes = {}
    for label, low, high, limit in [('0', 80, 82, '2.645e-97'), ('4', 723, 726, '4.034e-93')]:
        saved = data['modes'][label]
        raw = [Ball(x) for x in saved['raw_exact_decimal_vector']]
        require(len(raw) == len(saved['normalized_candidate']) == 112, 'mode_length_'+label)
        raw_norm = norm(raw)
        contained(raw_norm, saved['raw_norm'], 'raw_norm_'+label)
        q = [x/raw_norm for x in raw]
        mu = Ball(saved['center'])
        residual = []
        for k in range(112):
            value = (aa[k]-mu)*q[k]
            if k: value += bb[k-1]*q[k-1]
            if k < 111: value += bb[k]*q[k+1]
            residual.append(value)
            contained(q[k], saved['normalized_candidate'][k], f'mode_{label}_q_{k}')
        residual.append(bb[-1]*q[-1])
        require(len(saved['residual_including_tail']) == 113, 'residual_length_'+label)
        for k, value in enumerate(residual):
            contained(value, saved['residual_including_tail'][k], f'mode_{label}_residual_{k}')
        contained(residual[-1], saved['omitted_coordinate_residual'], 'omitted_residual_'+label)
        r = norm(residual)
        contained(r, saved['residual_norm'], 'residual_norm_'+label)
        sep = min((mu-low).a, (high-mu).a)
        require(D(saved['separation_lower']) <= sep and sep > r.b, 'separation_'+label)
        error = 2*Ball(r.b)/Ball(sep)
        require(error.b <= D(saved['unit_L2_error_upper']) < D(limit), 'mode_error_'+label)
        contained(mu.inflate(r.b), saved['eigenvalue_enclosure'], 'eigenvalue_'+label)
        modes[label] = (q, error)
        report['modes'][label] = dict(raw_norm=raw_norm.pair(),
            normalized_candidate=[x.pair() for x in q],
            residual=[x.pair() for x in residual], residual_norm=r.pair(),
            separation_lower=str(sep), error_upper=str(error.b))
    q0, e0 = modes['0']
    q4, e4 = modes['4']
    require((q0[0]-e0).a > 0, 'I0_positive')
    root = (2*lam).sqrt()
    for label, q, err in [('0', q0, e0), ('4', q4, e4)]:
        contained(root*q[0], data['trial']['approximate_additive_integrals'][label], 'J_'+label)
        # Saved error intervals enclose an upper-bound computation, not the
        # actual unknown integral error, so compare upper bounds only.
        require((root*err).b <= D(data['trial']['exact_integral_errors'][label][1]),
                'integral_error_'+label)
    eh = 2*root*(e0+e4)
    transport = sum((1/Ball(r).sqrt() for r in range(1, 14)), Ball())
    vector_error = transport*eh
    require(eh.b <= D(data['trial']['additive_L2_error_upper']), 'additive_error')
    require(transport.b <= D(data['trial']['transport_norm_upper']), 'transport_norm')
    require(vector_error.b <= D(data['trial']['full_projected_vector_L2_error_upper'])
            < D('1.276e-91'), 'projected_error')
    # Different exact Legendre expansion: binomial closed coefficients.
    coeff = [Ball() for _ in range(223)]
    for k in range(1, 112):
        n = 2*k
        amp = Ball(2).sqrt()*(q4[0]*q0[k]-q0[0]*q4[k])*(Ball(n)+Ball(1)/2).sqrt()
        for l in range(k+1):
            rational_numerator = (-1)**l * comb(n, l)*comb(2*n-2*l, n)
            coeff[n-2*l] += amp*Ball(rational_numerator)/(2**n)
    require(len(data['trial']['monomial_coefficients_H_lambda_x']) == 223, 'polynomial_length')
    for m, value in enumerate(coeff):
        contained(value, data['trial']['monomial_coefficients_H_lambda_x'][m], 'polynomial_'+str(m))
    report['trial'] = dict(additive_error_upper=str(eh.b),
            transport_norm_upper=str(transport.b), projected_error_upper=str(vector_error.b),
            monomial_coefficients=[x.pair() for x in coeff])
    save()
    print('Both normalized modes, all 226 residual coordinates and polynomial coefficients pass.', flush=True)
    require(data['integration']['nonzero_support_indices'] == list(range(1, 13))
            and data['integration']['index_13_zero_length'] is True, 'support_indices')
    lower_sums = [Ball() for _ in range(223)]
    lower = {}
    for r in range(1, 13):
        powers, value = [], 1/lam.sqrt()
        for m in range(223):
            powers.append(value)
            lower_sums[m] += value
            value *= Ball(r)/13
        lower[r] = powers
    for m, value in enumerate(lower_sums):
        contained(value, data['integration']['lower_endpoint_sums'][m], 'lower_endpoint_'+str(m))
    exact, polynomial = data['projection']['exact_trial_coefficients'], data['projection']['polynomial_coefficients']
    require(set(exact) == set(polynomial) == set(map(str, range(-120, 121))), 'all_241_indices')
    log_r = {r: Ball(r).ln() for r in range(2, 13)}
    weights = {r: (lam/r).sqrt() for r in range(1, 13)}
    maxradius = Fraction(0)
    for j in range(121):
        omega = 2*pi*j/L
        re, im = Ball(), Ball()
        for r in range(1, 13):
            sn, cs = ((Ball(), Ball(1)) if j == 0 or r == 1 else
                      phase(-j*(L-log_r[r])/L, pi))
            partial_re, partial_im = Ball(), Ball()
            for m in range(0, 223, 2):
                a = Ball(m)+Ball(1)/2
                den = a.sq()+omega.sq()
                real, imag = weights[r]*cs-lower[r][m], weights[r]*sn
                partial_re += coeff[m]*(a*real-omega*imag)/den
                partial_im += coeff[m]*(omega*real+a*imag)/den
            re += partial_re/L.sqrt()
            im += partial_im/L.sqrt()
        if j == 0:
            require(im.a <= 0 <= im.b, 'zero_imaginary')
            im = Ball()
        for index, imag in ([(0, im)] if j == 0 else [(j, im), (-j, -im)]):
            report['projection'][str(index)] = dict(real=re.pair(), imag=imag.pair())
            for component, value in [('real', re), ('imag', imag)]:
                contained(value, polynomial[str(index)][component], f'projection_{index}_{component}')
                inflated = Ball() if index == 0 and component == 'imag' else value.inflate(vector_error.b)
                contained(inflated, exact[str(index)][component], f'exact_trial_{index}_{component}')
                saved = exact[str(index)][component]
                a, b = map(Fraction, saved)
                radius = (b-a)/2
                maxradius = max(maxradius, radius)
                require(radius < Fraction('1.276e-91') and radius < Fraction('1e-65'),
                        f'radius_{index}_{component}')
                if not (index == 0 and component == 'imag'):
                    pa, pb = map(Fraction, polynomial[str(index)][component])
                    e = Fraction(data['trial']['full_projected_vector_L2_error_upper'])
                    require(a <= pa-e and b >= pb+e, f'inflation_{index}_{component}')
        if j % 30 == 0:
            print('Projection directions through |j| =', j, 'checked.', flush=True)
            save()
    require(maxradius <= Fraction(data['projection']['every_real_imag_component_radius_upper']), 'saved_maxradius')
    require(data['projection']['required_radius'] == '1e-65', 'required_radius')
    report['max_component_radius_upper'] = str(up.divide(D(maxradius.numerator), D(maxradius.denominator)))
    report['advertised_radius_limit'] = '1.276e-91'
    report['required_radius_limit'] = '1e-65'
    report['checked_counts'] = dict(operator_entries=224, pivots=896,
            normalized_coordinates=224, residual_coordinates=226,
            polynomial_coefficients=223, projected_complex_coefficients=241)
    report['outcome'] = 'ALL_SAVED_ENCLOSURES_RECONSTRUCTED_AND_CONTAINED'
    save()
    print('All 241 complex coefficient enclosures pass containment, not just overlap.')
    print('Maximum radius <=', report['max_component_radius_upper'][:24],
          '*10^-91; advertised <1.276e-91, required <1e-65.')
    print('Failures:', report['failures'])
    print('Complete audit evidence:', OUTPUT.relative_to(HERE.parent.parent))
except Exception as exc:
    report['outcome'] = 'FAILED'
    report['exception'] = repr(exc)
    save()
    print('FAILED:', repr(exc), 'Evidence:', OUTPUT)
    raise
