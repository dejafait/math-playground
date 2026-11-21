"""Approved single-cell boundary denominator and complex observable test.

Integer interval arithmetic only; upstream audited input intervals retain
their complete mode, transport and ground errors. Full evidence is saved.
"""
from fractions import Fraction
from math import isqrt
from pathlib import Path
import hashlib
import json

HERE = Path(__file__).resolve().parent
OUT = Path(__file__).with_suffix('.json')
DIGITS = 340
S = 10**DIGITS
report = dict(outcome='IN_PROGRESS', failures=[], checks={},
              grid_digits=DIGITS, parameters=dict(lambda_squared=13, N=120, z='i/4'),
              inputs={}, constants={}, directions={})


def save():
    OUT.write_text(json.dumps(report, indent=2)+'\n')


def require(ok, name):
    report['checks'][name] = bool(ok)
    if not ok:
        report['failures'].append(name)
        raise ArithmeticError(name)


def ceiling(a, b):
    return -((-a)//b)


def decimal_string(n):
    sign = '-' if n < 0 else ''
    q, r = divmod(abs(n), S)
    return sign+str(q)+'.'+str(r).zfill(DIGITS)


class I:
    def __init__(self, a=0, b=None, *, raw=False):
        if isinstance(a, I):
            self.a, self.b = a.a, a.b
        elif raw:
            self.a, self.b = a, b
        else:
            lo, hi = Fraction(a), Fraction(a if b is None else b)
            self.a = (lo.numerator*S)//lo.denominator
            self.b = ceiling(hi.numerator*S, hi.denominator)
        assert self.a <= self.b

    def __add__(self, other):
        o = I(other)
        return I(self.a+o.a, self.b+o.b, raw=True)

    __radd__ = __add__

    def __neg__(self):
        return I(-self.b, -self.a, raw=True)

    def __sub__(self, other):
        return self+-I(other)

    def __rsub__(self, other):
        return I(other)+-self

    def __mul__(self, other):
        o = I(other)
        products = [x*y for x in (self.a, self.b) for y in (o.a, o.b)]
        return I(min(products)//S, ceiling(max(products), S), raw=True)

    __rmul__ = __mul__

    def __truediv__(self, other):
        o = I(other)
        if o.a <= 0 <= o.b:
            raise ZeroDivisionError('interval divisor contains zero')
        pairs = [(x*S, y) for x in (self.a, self.b) for y in (o.a, o.b)]
        return I(min(x//y for x, y in pairs),
                 max(ceiling(x, y) for x, y in pairs), raw=True)

    def __rtruediv__(self, other):
        return I(other)/self

    def sq(self):
        values = [self.a*self.a, self.b*self.b]
        return I(0 if self.a <= 0 <= self.b else min(values)//S,
                 ceiling(max(values), S), raw=True)

    def sqrt(self):
        assert self.a >= 0
        lo, hi = isqrt(self.a*S), isqrt(self.b*S)
        return I(lo, hi+(hi*hi < self.b*S), raw=True)

    def pair(self):
        return [decimal_string(self.a), decimal_string(self.b)]


def pair(value):
    assert len(value) == 2
    assert Fraction(value[0]) <= Fraction(value[1])
    return I(*value)


def cmul(u, v):
    a, b = u
    c, d = v
    return a*c-b*d, a*d+b*c


def csave(value):
    return dict(real=value[0].pair(), imag=value[1].pair())


def modulus(value):
    return (value[0].sq()+value[1].sq()).sqrt()


def load(name):
    p = HERE/name
    digest = hashlib.sha256(p.read_bytes()).hexdigest()
    report['inputs'][name] = digest
    return json.loads(p.read_text())


try:
    report['script_sha256'] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    trial = load('ccm-trial-certificate-369.json')
    ground = load('commutator-certificate-364.json')
    taudit = load('ccm-trial-audit-371.json')
    gaudit = load('commutator-audit-366.json')
    require(trial['outcome'] == 'CERTIFIED_TRIAL_PROJECTION' and not trial['failures']
            and all(trial['checks'].values()), 'upstream_trial')
    require(ground['outcome'] == 'CERTIFIED_FINITE_RATIO_AND_ANSATZ_TEST'
            and not ground['failures'] and all(ground['checks'].values()), 'upstream_ground')
    require(taudit['outcome'] == 'ALL_SAVED_ENCLOSURES_RECONSTRUCTED_AND_CONTAINED'
            and not taudit['failures'] and all(taudit['checks'].values()), 'trial_audit')
    require(gaudit['outcome'] == 'AUDIT_PASSED' and not gaudit['failures'], 'ground_audit')
    require(taudit['input_sha256'] == report['inputs']['ccm-trial-certificate-369.json'],
            'trial_audit_input_binding')
    require(gaudit['hashes']['commutator-certificate-364.json']
            == report['inputs']['commutator-certificate-364.json'], 'ground_audit_input_binding')
    require(trial['parameters'] == dict(lambda_squared=13, N=120, even_dimension=112,
            max_degree=222, interval_precision=260, candidate_precision=240), 'trial_parameters')
    L = pair(trial['constants']['L'])
    pi = pair(trial['constants']['pi'])
    rootL = L.sqrt()
    t = I(1)/4
    a = L/8
    require(0 < a.a <= a.b < S, 'sinh_argument_between_0_and_1')
    # Positive sinh series through degree199; the remaining ratios are <1/2.
    term, sinh = a, a
    for n in range(1, 100):
        term = term*a.sq()/((2*n)*(2*n+1))
        sinh = sinh+term
    next_term = term*a.sq()/(200*201)
    tail = 2*next_term
    sinh = I(sinh.a, sinh.b+tail.b, raw=True)
    prefactor = 2*sinh/rootL
    report['constants'] = dict(L=L.pair(), pi=pi.pair(), rootL=rootL.pair(),
                               sinh=sinh.pair(), sinh_tail_upper=decimal_string(tail.b),
                               prefactor=prefactor.pair())
    coeff = trial['projection']['exact_trial_coefficients']
    polynomial = trial['projection']['polynomial_coefficients']
    require(set(coeff) == {str(j) for j in range(-120, 121)}, 'complete_241_directions')
    error = Fraction(trial['trial']['full_projected_vector_L2_error_upper'])
    require(0 < error < Fraction('1.276e-91'), 'retained_trial_transport_error')
    b_re, b_im, e_re, e_im = I(), I(), I(), I()
    for j in range(-120, 121):
        saved = coeff[str(j)]
        re, im = pair(saved['real']), pair(saved['imag'])
        for component in ('real', 'imag'):
            old = list(map(Fraction, saved[component]))
            poly = list(map(Fraction, polynomial[str(j)][component]))
            require(old[0] <= old[1] and old[1]-old[0] < Fraction('2.552e-91'),
                    f'ordered_width_{j}_{component}')
            # The j=0 imaginary part is exactly zero by reality.
            if component == 'imag' and j == 0:
                require(old == [0, 0], 'exact_zero_frequency_imaginary_part')
            else:
                require(old[0] <= poly[0]-error and old[1] >= poly[1]+error,
                        f'complete_error_inflation_{j}_{component}')
        nu = 2*pi*j/L
        denominator = nu.sq()+t.sq()
        row = prefactor*t/denominator, -prefactor*nu/denominator
        ev = cmul(row, (re, im))
        bv = re/rootL, im/rootL
        b_re, b_im = b_re+bv[0], b_im+bv[1]
        e_re, e_im = e_re+ev[0], e_im+ev[1]
        report['directions'][str(j)] = dict(input=saved, fourier_row=csave(row),
                                           boundary_contribution=csave(bv),
                                           observable_contribution=csave(ev))
    boundary = b_re, b_im
    observable = e_re, e_im
    babs = modulus(boundary)
    report['boundary'] = csave(boundary)
    report['boundary_modulus'] = babs.pair()
    report['trial_observable'] = csave(observable)
    # A failed exclusion is inconclusive and never triggers division.
    if babs.a <= 0:
        report['outcome'] = 'INCONCLUSIVE_BOUNDARY_NOT_SEPARATED'
    else:
        require(babs.a > 0, 'boundary_excludes_zero_before_division')
        b2 = b_re.sq()+b_im.sq()
        numerator = cmul(observable, (b_re, -b_im))
        ratio = numerator[0]/b2, numerator[1]/b2
        g = pair(ground['row']['fourier_at_boundary_normalized_ground'])
        gabs = modulus((g, I()))
        normalizer = I(max(S, gabs.a), max(S, gabs.b), raw=True)
        discrepancy = modulus((ratio[0]-g, ratio[1]))/normalizer
        report['normalized_trial_observable'] = csave(ratio)
        report['ground_observable'] = g.pair()
        report['normalizer'] = normalizer.pair()
        report['discrepancy'] = discrepancy.pair()
        report['required_upper'] = '0.1'
        # A threshold miss is a mathematical result, not a software failure.
        report['threshold_pass'] = discrepancy.b <= S//10
        report['threshold_fail'] = discrepancy.a > S//10
        require(I('4.72968e-29').b < babs.a and babs.b < I('4.72969e-29').a,
                'reported_boundary_modulus_bracket')
        require(I('0.48616229937498').b < discrepancy.a
                and discrepancy.b < I('0.48616229937499').a,
                'reported_discrepancy_bracket')
        report['outcome'] = ('CERTIFIED_OBSERVABLE_PASS' if report['threshold_pass'] else
                             'CERTIFIED_OBSERVABLE_MISS' if report['threshold_fail'] else
                             'INCONCLUSIVE_THRESHOLD_STRADDLE')
except Exception as exc:
    report['outcome'] = 'FAILED'
    report['exception'] = repr(exc)
    if repr(exc) not in report['failures']:
        report['failures'].append(repr(exc))
finally:
    save()
    print('RESULT', report['outcome'])
    if report['checks'].get('reported_boundary_modulus_bracket'):
        print('4.72968e-29 < |b(v)| < 4.72969e-29; required |b(v)| > 0')
    if report['checks'].get('reported_discrepancy_bracket'):
        print('0.48616229937498 < discrepancy < 0.48616229937499')
    print('required discrepancy <= 1/10; failures:', report['failures'])
    print('Full certificate:', OUT.relative_to(HERE.parent.parent))
    if report['outcome'] == 'FAILED':
        raise SystemExit(1)
