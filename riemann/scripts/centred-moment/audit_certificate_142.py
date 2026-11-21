#!/usr/bin/env python3
"""Independent 320-bit enclosure audit of every step140 certificate record.

Does not import the original evaluator/helper. Uses longer elementary series
and separate even/odd exponential sequences for the Simpson sum. See L960,
step142, for the inclusion argument and the limits of this discriminating check.
"""
from fractions import Fraction
from functools import lru_cache
from math import isqrt
from pathlib import Path
import hashlib
import json
import time

BITS = 320
S = 1 << BITS
BASE = Path(__file__).parent
SOURCE = BASE / 'rational-replay-140.json'
OUTPUT = BASE / 'conceptual-audit-142.json'


class Box:
    def __init__(self, v=0, upper=None):
        if upper is not None:
            self.lo, self.hi = v, upper
        elif isinstance(v, Box):
            self.lo, self.hi = v.lo, v.hi
        else:
            r = Fraction(v) * S
            self.lo = r.numerator // r.denominator
            self.hi = -((-r.numerator) // r.denominator)
        if self.lo > self.hi:
            raise ArithmeticError('reversed box')

    def __add__(self, v):
        v = Box(v)
        return Box(self.lo + v.lo, self.hi + v.hi)
    __radd__ = __add__

    def __neg__(self):
        return Box(-self.hi, -self.lo)

    def __sub__(self, v):
        return self + -Box(v)

    def __rsub__(self, v):
        return Box(v) + -self

    def __mul__(self, v):
        v = Box(v)
        values = [x*y for x in (self.lo, self.hi) for y in (v.lo, v.hi)]
        return Box(min(values) // S, -((-max(values)) // S))
    __rmul__ = __mul__

    def __truediv__(self, v):
        v = Box(v)
        if v.lo <= 0 <= v.hi:
            raise ArithmeticError('zero divisor')
        lower, upper = Fraction(S*S, v.hi), Fraction(S*S, v.lo)
        reciprocal = Box(lower.numerator // lower.denominator,
                         -((-upper.numerator) // upper.denominator))
        return self * reciprocal

    def __rtruediv__(self, v):
        return Box(v) / self

    def __pow__(self, n):
        if n < 0 or not isinstance(n, int):
            raise ValueError('nonnegative integer power')
        # Small derivative powers only; left-to-right rather than binary power.
        answer = Box(1)
        for _ in range(n):
            answer = answer * self
        return answer

    def magnitude(self):
        m = max(abs(self.lo), abs(self.hi))
        return Box(m, m)

    def record(self):
        return {'lo': str(self.lo), 'hi': str(self.hi), 'bits': BITS}


@lru_cache(None)
def unit_log(value):
    value = Fraction(value)
    assert 1 <= value <= 2
    z = Box((value-1)/(value+1))
    z2 = z*z
    term, total = z, Box(0)
    for j in range(120):
        total += 2*term/(2*j+1)
        term *= z2
    tail = 2*term/(241*(1-z2))
    return Box(total.lo, (total+tail).hi)


@lru_cache(None)
def point_log(value):
    value = Fraction(value)
    assert value > 0
    power = 0
    while value < 1:
        value *= 2
        power -= 1
    while value >= 2:
        value /= 2
        power += 1
    return unit_log(value) + power*unit_log(Fraction(2))


def logarithm(value):
    value = Box(value)
    return Box(point_log(Fraction(value.lo, S)).lo,
               point_log(Fraction(value.hi, S)).hi)


def point_exp(value):
    value = Fraction(value)
    if value < 0:
        return 1/point_exp(-value)
    halvings = 0
    while value > Fraction(1, 8):
        value /= 2
        halvings += 1
    z, term, total = Box(value), Box(1), Box(1)
    for j in range(1, 96):
        term = term*z/j
        total += term
    omitted = term*z/96
    remainder = omitted/(1-z/97)
    answer = Box(total.lo, (total+remainder).hi)
    assert answer.lo > 0
    for _ in range(halvings):
        answer *= answer
    return answer


def exponential(value):
    value = Box(value)
    return Box(point_exp(Fraction(value.lo, S)).lo,
               point_exp(Fraction(value.hi, S)).hi)


def root(value):
    value = Box(value)
    assert value.lo >= 0
    lower, upper = isqrt(value.lo*S), isqrt(value.hi*S)
    return Box(lower, upper + (upper*upper < value.hi*S))


def machin():
    def arc(x, terms):
        total = sum(((-1)**j*x**(2*j+1)/(2*j+1)
                     for j in range(terms)), Fraction(0))
        other = total + (-1)**terms*x**(2*terms+1)/(2*terms+1)
        return Box(Box(min(total, other)).lo, Box(max(total, other)).hi)
    return 16*arc(Fraction(1, 5), 160)-4*arc(Fraction(1, 239), 48)


def quadrature(low, high, centre, a, b):
    mesh = 4096
    width = high-low
    assert width.lo > 0
    delta = width/mesh
    q = lambda u: a*u*u/4-b*u
    # Two independent sequences indexed by parity. For stride 2*delta:
    # R_i = exp(2*delta*(a*u_i/2-b)+a*delta^2), R_(i+2)/R_i=exp(2*a*delta^2).
    advance = exponential(2*a*delta*delta)
    sums = [Box(0), Box(0)]
    for parity in (0, 1):
        start = low+parity*delta
        e = exponential(q(start))
        ratio = exponential(2*delta*(a*start/2-b)+a*delta*delta)
        for i in range(parity, mesh+1, 2):
            u = low+i*delta
            weight = 1 if i in (0, mesh) else (4 if parity else 2)
            sums[0] += weight*e
            sums[1] += weight*(u-centre)*e
            if i+2 <= mesh:
                e *= ratio
                ratio *= advance
        if parity == 0:
            last = e
    si, st = (width*x/(3*mesh) for x in sums)
    domain = Box(low.lo, high.hi)
    r = (a*domain/2-b).magnitude()
    m = (domain-centre).magnitude()
    d = a/2
    em = Box(0, max(exponential(q(low)).hi, exponential(q(high)).hi))
    di = em*(r**4+6*d*r**2+3*d**2)
    dt = em*(m*(r**4+6*d*r**2+3*d**2)+4*(r**3+3*d*r))
    ei, et = width**5*di/(180*mesh**4), width**5*dt/(180*mesh**4)
    integral, tail = Box(si.lo-ei.hi, si.hi+ei.hi), Box(st.lo-et.hi, st.hi+et.hi)
    return integral, tail, {
        'width': width, 'h': delta, 'r_abs_upper': r,
        'u_minus_kappa_abs_upper': m, 'exp_upper': em,
        'I_fourth_derivative_bound': di, 'tail_fourth_derivative_bound': dt,
        'I_simpson': si, 'tail_simpson': st, 'I_error': ei, 'tail_error': et,
        'last_E_recurrence': last, 'last_E_direct': exponential(q(high))}


def main():
    begun = time.monotonic()
    stored = json.loads(SOURCE.read_text())
    failures, checks, records = [], [], []
    report = {'status': 'INCOMPLETE', 'source_sha256': hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
              'audit_script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'bits': BITS, 'series_terms': {'log': 120, 'exp': 96, 'atan5': 160, 'atan239': 48},
              'required_cap': '81/4', 'failures': failures, 'checks': checks, 'leaves': records,
              'qualification': 'Independent implementation plus informal code/proof audit; not a formal proof checker.'}
    def save():
        report['elapsed_seconds'] = time.monotonic()-begun
        OUTPUT.write_text(json.dumps(report, indent=2)+'\n')
    def need(test, label):
        checks.append({'check': label, 'passed': bool(test)})
        if not test:
            failures.append(label)
    def contained(new, old, label):
        need(old['denominator_power_two'] == 256, label+' precision')
        need(int(old['lo'])*(1 << 64) <= new.lo <= new.hi <= int(old['hi'])*(1 << 64),
             label+' independent enclosure contained in stored enclosure')
    def gate(name, fresh, old):
        need(name in stored['gates'] and stored['gates'][name] is True, name+' stored flag')
        if isinstance(fresh, bool):
            need(fresh and old == {'exact': True}, name+' exact predicate')
        else:
            need(fresh.lo > 0, name+' independently positive')
            need(int(old['positive_margin']['lo']) > 0, name+' stored positive')
            contained(fresh, old['positive_margin'], name)

    save()
    try:
        ends = [690988]
        while ends[-1] < 3100000:
            ends.append(min(3100000, ends[-1]*101//100))
        need(stored['domain'] == {'a': '98/625', 'T': '1/5', 'X': 6000000185827, 'W': 120000000000000}, 'exact rectangle')
        need(stored['closed_index_endpoints'] == ends and len(ends) == 152, 'all closed leaves')
        need(len(stored['leaves']) == 151 and len(stored['gates']) == 914, 'complete certificate counts')
        need(stored['failures'] == [] and stored['status'] == 'PASS', 'original completed status')
        need(stored['required_cap'] == '81/4' and stored['bits'] == 256, 'original cap and precision')
        a, t = Box(Fraction(98, 625)), Box(Fraction(1, 5))
        pi, centre, low = machin(), point_log(Fraction(32)), point_log(Fraction(128))
        for key, value in [('pi', pi), ('kappa', centre), ('logK', low)]:
            contained(value, stored['constants'][key], key)
        margins = {
            'positive_heat_band': 0 < Fraction(98, 625) < Fraction(1, 5) < Fraction(1, 2),
            'finite_natural_index_upper_wall': Box(3100001)**2-120000000000000/(4*pi)-t/16,
            'finite_natural_index_lower_wall': 6000000185827/(4*pi)+a/16-690988**2,
            'prefix_above_centre': 128 > 32,
            'centre_log_between_3_and_7_2': Box(min((centre-3).lo, (Box(Fraction(7, 2))-centre).lo), min((centre-3).hi, (Box(Fraction(7, 2))-centre).hi)),
            'cover_starts_at_C': ends[0] == 690988,
            'cover_ends_at_H': ends[-1] == 3100000,
            'cover_strictly_increasing': all(l < u for l, u in zip(ends, ends[1:]))}
        need(set(stored['global_evidence']) == set(margins), 'exact global gate names')
        for key, value in margins.items():
            gate(key, value, stored['global_evidence'][key])
        report['global_margins'] = {k: v.record() if isinstance(v, Box) else v for k, v in margins.items()}
        logs = [point_log(Fraction(n)) for n in range(1, 129)]
        need(logs[0].lo == logs[0].hi == 0, 'n=1 log exactly zero')
        for j, (left, right, old) in enumerate(zip(ends, ends[1:], stored['leaves']), 1):
            need((old['index'], old['left'], old['right']) == (j, left, right), f'leaf{j} exact placement')
            xl = Box(6000000185827) if j == 1 else 4*pi*(Box(left)**2-t/16)
            c = logarithm(root(1+xl*xl)/(4*pi))/4-1/(2*(1+xl*xl))
            sigma, high = Box(Fraction(1, 2))+a*c, point_log(Fraction(right))
            b = sigma-1
            g = lambda u: 1+(u-centre)*(a*u/2-sigma)
            prefix, terms = Box(0), []
            for n, u in enumerate(logs, 1):
                weight = Box(0) if n == 32 else centre-u if n < 32 else u-centre
                need(weight.lo > 0 if n != 32 else weight.lo == weight.hi == 0, f'leaf{j} absolute log term{n}')
                term = weight*exponential(a*u*u/4-sigma*u)
                prefix += term
                terms.append(term.record())
            integral, tail, detail = quadrature(low, high, centre, a, b)
            bound = prefix+tail
            values = {'x_left': xl, 'c_left': c, 'sigma': sigma, 'B': b, 'logU': high,
                      'g_low': g(low), 'g_high': g(high), 'prefix': prefix,
                      'I': integral, 'tail': tail, 'bound': bound}
            for key, value in values.items():
                contained(value, old[key], f'leaf{j} {key}')
            need(old['quadrature']['mesh'] == 4096, f'leaf{j} even mesh')
            for key, value in detail.items():
                # Point upper bounds are intentionally precision-dependent and
                # need only dominate the new bound, not contain its singleton.
                if key in ('r_abs_upper', 'u_minus_kappa_abs_upper'):
                    need(value.hi <= int(old['quadrature'][key]['hi'])*(1 << 64), f'leaf{j} {key} domination')
                else:
                    contained(value, old['quadrature'][key], f'leaf{j} {key}')
            leaf_margins = {
                'position_not_left_of_X': xl.lo == xl.hi == 6000000185827*S if j == 1 else xl-6000000185827,
                'all_coefficient_heat_exponents_nonpositive': 4*c-high,
                'convex_derivative_at_prefix_negative': -g(low),
                'convex_derivative_at_upper_negative': -g(high),
                'tail_integrals_positive': Box(min(integral.lo, tail.lo), min(integral.hi, tail.hi)),
                'complete_centred_moment_below_81_4': Box(Fraction(81, 4))-bound}
            need(set(old['gate_evidence']) == set(leaf_margins), f'leaf{j} exact gate names')
            for key, value in leaf_margins.items():
                gate(f'leaf_{j:03d}_{key}', value, old['gate_evidence'][key])
            # Check original charged errors and sums as identities, not just overlap.
            for endpoint in ('lo', 'hi'):
                need(int(old['bound'][endpoint]) == int(old['prefix'][endpoint])+int(old['tail'][endpoint]), f'leaf{j} original bound {endpoint}')
            for key in ('I', 'tail'):
                charge = int(old['quadrature'][key+'_error']['hi'])
                need(int(old[key]['lo']) == int(old['quadrature'][key+'_simpson']['lo'])-charge and int(old[key]['hi']) == int(old['quadrature'][key+'_simpson']['hi'])+charge, f'leaf{j} original {key} error charge')
            need(4*int(old['bound']['hi']) < 81*(1 << 256) and 4*bound.hi < 81*S, f'leaf{j} original and independent cap')
            records.append({'index': j, 'left': left, 'right': right,
                            'values': {k: v.record() for k, v in values.items()},
                            'quadrature': {k: v.record() for k, v in detail.items()},
                            'prefix_terms_1_through_128': terms,
                            'cap_margin': leaf_margins['complete_centred_moment_below_81_4'].record()})
            if j % 10 == 0:
                save()
        original_max = max(int(x['bound']['hi']) for x in stored['leaves'])
        new_max = max(int(x['values']['bound']['hi']) for x in records)
        need(stored['maximum_upper_endpoint'] == {'numerator': str(original_max), 'denominator_power_two': 256}, 'original maximum recomputed')
        need(stored['actual_uniform_bound'] == stored['maximum_upper_endpoint'], 'original uniform bound matches maximum')
        need(1000000*original_max < 20213859*(1 << 256), 'original display ceiling exact')
        report['original_maximum'] = stored['maximum_upper_endpoint']
        report['independent_maximum'] = {'numerator': str(new_max), 'bits': BITS}
        report['maximum_leaf'] = max(records, key=lambda x: int(x['values']['bound']['hi']))['index']
        report['max_tail_error'] = max((x['quadrature']['tail_error'] for x in records), key=lambda x: int(x['hi']))
        report['status'] = 'PASS' if not failures else 'FAIL'
    except Exception as error:
        failures.append(type(error).__name__+': '+str(error))
        report['status'] = 'FAIL'
    save()
    print(report['status'], 'leaves', len(records), '/151; checks', len(checks), 'failures', len(failures))
    print('Required <81/4; original maximum <20213859/1000000:', report.get('original_maximum'))
    print('Independent maximum:', report.get('independent_maximum'))
    print('Failures:', failures[:8], 'full evidence:', OUTPUT)
    return int(bool(failures))


if __name__ == '__main__':
    raise SystemExit(main())
