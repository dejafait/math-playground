"""Independent L825 finite audit; exact endpoints, no grid or Q import.

Only degrees 2/3. Inherited analytic/transcendental contracts remain inputs.
Full certificates are saved; original programs and evidence are preserved.
"""
import hashlib
import importlib.util
import json
import math
import sys
from fractions import Fraction as F
from pathlib import Path

BASE = Path(__file__).resolve().parent
ROOT = BASE.parent.parent
OUT = BASE / 'audit-631'
checks, failures = [], []
evidence = {}


def check(name, passed):
    checks.append(dict(name=name, passed=bool(passed)))
    if not passed:
        failures.append(name)


def read(path):
    return json.loads((ROOT / path).read_text())


def digest(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


class I:
    """Exact rational endpoint arithmetic; no operation rounds."""
    def __init__(self, lo, hi=None):
        self.lo, self.hi = F(lo), F(lo if hi is None else hi)
        if self.lo > self.hi:
            raise ValueError('reversed endpoints')

    def __add__(self, b):
        b = iv(b)
        return I(self.lo+b.lo, self.hi+b.hi)

    __radd__ = __add__

    def __neg__(self):
        return I(-self.hi, -self.lo)

    def __sub__(self, b):
        return self + (-iv(b))

    def __mul__(self, b):
        b = iv(b)
        endpoints = [x*y for x in (self.lo, self.hi) for y in (b.lo, b.hi)]
        return I(min(endpoints), max(endpoints))

    __rmul__ = __mul__

    def __truediv__(self, b):
        b = iv(b)
        if b.lo <= 0 <= b.hi:
            raise ValueError('denominator includes zero')
        return self * I(1/b.hi, 1/b.lo)

    def __rtruediv__(self, b):
        return iv(b)/self

    def sq(self):
        lo = 0 if self.lo <= 0 <= self.hi else min(self.lo**2, self.hi**2)
        return I(lo, max(self.lo**2, self.hi**2))

    def pair(self):
        return [str(self.lo), str(self.hi)]


def iv(x):
    return x if isinstance(x, I) else I(x)


def includes(a, b):
    return a.lo <= b.lo <= b.hi <= a.hi


# Sparse multivariate rational polynomials. Sorted variable-name tuples are
# monomials, the empty tuple is 1. This independently expands all coefficients.
def const(x):
    return {} if x == 0 else {(): F(x)}


def var(x):
    return {(x,): F(1)}


def add(*polys):
    result = {}
    for p in polys:
        for m, c in p.items():
            result[m] = result.get(m, F(0)) + c
    return {m: c for m, c in result.items() if c}


def mul(p, q):
    result = {}
    for m, c in p.items():
        for n, d in q.items():
            key = tuple(sorted(m+n))
            result[key] = result.get(key, F(0)) + c*d
    return {m: c for m, c in result.items() if c}


def scale(c, p):
    return mul(const(c), p)


def power(p, n):
    out = const(1)
    for _ in range(n):
        out = mul(out, p)
    return out


def translate(co, h):
    # co is in ascending powers of y; expand (y+h)^k by binomial theorem.
    return [add(*(scale(math.comb(k, j), mul(co[k], power(h, k-j)))
                  for k in range(j, len(co)))) for j in range(len(co))]


def self_convolution(co):
    d = len(co)-1
    result = [{} for _ in co]
    for k in range(d+1):
        for i in range(k+1):
            j = k-i
            weight = F(math.factorial(d-i)*math.factorial(d-j),
                       math.factorial(d)*math.factorial(d-k))
            result[d-k] = add(result[d-k], scale(weight, mul(co[d-i], co[d-j])))
    return result


def serial_poly(p):
    return {'*'.join(m) or '1': str(c) for m, c in sorted(p.items())}


def algebra():
    a, b, c, h, s, t, w = [var(x) for x in ('a', 'b', 'c', 'h', 's', 't', 'w')]
    quad = self_convolution([b, a, const(1)])
    cub = self_convolution([c, b, a, const(1)])
    expected2 = [add(scale(2, b), scale(F(1, 2), power(a, 2))), scale(2, a), const(1)]
    expected3 = [add(scale(2, c), scale(F(2, 3), mul(a, b))),
                 add(scale(2, b), scale(F(2, 3), power(a, 2))), scale(2, a), const(1)]
    center2 = translate([s, scale(-2, h), const(1)], h)
    center3 = translate([scale(-1, w), scale(3, t), scale(-3, h), const(1)], h)
    centered2 = [add(s, scale(-1, power(h, 2))), {}, const(1)]
    centered3 = [add(scale(-1, w), scale(3, mul(t, h)), scale(-2, power(h, 3))),
                 add(scale(3, t), scale(-3, power(h, 2))), {}, const(1)]
    for label, actual, expected in [('quadratic convolution', quad, expected2),
                                    ('cubic convolution', cub, expected3),
                                    ('quadratic translation', center2, centered2),
                                    ('cubic translation', center3, centered3)]:
        for j, (x, y) in enumerate(zip(actual, expected)):
            check(f'{label} coefficient y^{j}', x == y)
        evidence[label] = [serial_poly(p) for p in actual]
    u, v, z = var('u'), var('v'), var('z')
    q2, q3 = [scale(F(1, 2), u), {}, const(1)], [scale(F(1, 2), z), scale(F(1, 2), v), {}, const(1)]
    for d, co, target in [(2, q2, [u, {}, const(1)]), (3, q3, [z, v, {}, const(1)])]:
        for j, (x, y) in enumerate(zip(self_convolution(co), target)):
            check(f'factor existence degree {d} coefficient {j}', x == y)
    defect = [add(scale(j+1, q3[j+1]), scale(-3, q2[j])) for j in range(3)]
    expected = [add(scale(F(1, 2), v), scale(F(-3, 2), u)), {}, {}]
    for j, (x, y) in enumerate(zip(defect, expected)):
        check(f'entire derivative defect coefficient {j}', x == y)
    evidence['symbolic_defect_ascending'] = [serial_poly(p) for p in defect]


def numerical():
    oldpath = 'scripts/central-jacobi/centered-appell-629.json'
    data_path = 'scripts/central-jacobi/fixed-model-certificate-476.json'
    source_path = 'scripts/actual-fredholm/fixed-pair-certificate-431.json'
    old, data, source_record = read(oldpath), read(data_path), read(source_path)
    source = source_record['evaluation']
    a478 = read('scripts/central-jacobi/audit-478/audit-report.json')
    a433 = read('scripts/actual-fredholm/audit-433/audit-report.json')
    replay433 = read('scripts/actual-fredholm/audit-433/fixed-pair-certificate-431.json')
    hashes = {path: digest(path) for path in old['evidence']['input_hashes']}
    evidence['original_hashes'] = {**hashes, oldpath: digest(oldpath)}
    for path, expected in old['evidence']['input_hashes'].items():
        check('step629 hash '+path, hashes[path] == expected)
    for path in (data_path, source_path):
        check('step478 hash '+path, hashes[path] == a478['original_hashes'][path])
    check('source hash L791', hashes[source_path] == data['source_sha256'])
    check('source hash step433', hashes[source_path] == a433['original_sha256'])
    check('complete evaluator equals audited replay', source == replay433['evaluation'])
    for name, report in [('629', old), ('478', a478), ('433', a433)]:
        # Step433 records successful check descriptions as strings; steps
        # 478/629 use explicit name/passed records. No string is a new test.
        entries_valid = (all(isinstance(x, str) and bool(x) for x in report['checks'])
                         if name == '433' else all(x['passed'] is True for x in report['checks']))
        check('saved report passes '+name, report['status'] == 'PASS' and report['failures'] == []
              and bool(report['checks']) and entries_valid)
    check('complete step629 finite-check count', len(old['checks']) == 27)
    check('uniform analytic disk', source['uniform_disk_radius'] == 1600)
    eg = I(*source['uniform_G_error'])
    check('positive complete analytic error', 0 < eg.lo <= eg.hi < F('3.141e-48'))
    check('same error in inherited and new certificates',
          data['uniform_G_error'] == source['uniform_G_error']
          and eg.pair() == old['evidence']['uniform_G_error'])
    gamma, input_records = [], []
    for j in range(4):
        co = I(*source['coefficients'][j])
        err = eg.hi / 1600**j
        actual = co + I(-err, err)
        saved_a, saved_g = I(*data['actual_a'][j]), I(*data['gamma'][j])
        rec = old['evidence']['coefficient_inputs'][j]
        computed_g = saved_a*(8*4**j*math.factorial(j))
        check(f'full original coefficient input {j}', rec['j'] == j
              and I(*rec['evaluator']).pair() == co.pair()
              and I(*rec['actual_a']).pair() == saved_a.pair()
              and I(*rec['gamma']).pair() == saved_g.pair()
              and F(rec['coefficient_error']) == err)
        check(f'Cauchy error retained {j}', includes(saved_a, actual))
        check(f'saved rational Cauchy recomputation {j}', includes(I(*rec['recomputed_actual_a']), actual))
        check(f'gamma scaling and positive denominator {j}', includes(saved_g, computed_g) and saved_g.lo > 0)
        check(f'saved rational gamma recomputation {j}', includes(I(*rec['recomputed_gamma']), computed_g))
        input_records.append(dict(j=j, coefficient=co.pair(), coefficient_error=str(err),
                                  actual_a_exact=actual.pair(), actual_a=saved_a.pair(),
                                  gamma_exact=computed_g.pair(), gamma=saved_g.pair()))
        gamma.append(saved_g)
    evidence['coefficient_inputs'] = input_records
    r1, r2, r3 = [g/gamma[0] for g in gamma[1:]]
    h2, h3 = r1/r2, r2/r3
    u2 = 1/r2 - h2.sq()
    u3 = 3*r1/r3 - 3*h3.sq()
    v3 = -1/r3 + 3*r1*h3/r3 - 2*h3.sq()*h3
    q2, q3, qc3 = u2/2, u3/2, v3/2
    defect = q3-3*q2
    alternative = 3*(r1/r3-h3.sq()-1/r2+h2.sq())/2
    vals = dict(R1=r1, R2=r2, R3=r3, h2=h2, h3=h3, u2=u2, u3=u3, v3=v3,
                Q2_constant=q2, Q3_linear=q3, Q3_constant=qc3,
                derivative_defect=defect, rearranged_defect=alternative)
    for name, value in vals.items():
        check('full saved interval encloses independent exact arithmetic '+name,
              includes(I(*old['evidence']['intervals'][name]), value))
        check('six-place outward display '+name,
              includes(I(*old['evidence']['outward_decimal_displays'][name]), value))
    check('strict defect bound', F('9.582501') < defect.lo <= defect.hi < F('9.582502'))
    check('rearranged strict defect bound', F('9.582501') < alternative.lo <= alternative.hi < F('9.582502'))
    check('exact compatibility threshold', old['evidence']['required_defect_for_compatibility'] == '0 exactly')
    saved_def = old['evidence']['full_derivative_defect_coefficients_descending']
    check('all saved polynomial defect coefficients', saved_def[:2] == ['0', '0']
          and includes(I(*saved_def[2]), defect))
    evidence['independent_exact_intervals'] = {k: v.pair() for k, v in vals.items()}
    evidence['required_defect'] = '0 exactly'
    # Same-code replay is explicitly separate from independent arithmetic.
    sys.path.insert(0, str(BASE))
    spec = importlib.util.spec_from_file_location('centered629_replay', BASE/'centered_appell_629.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    module.run()
    replay = dict(scope=old['scope'], contracts=old['contracts'], rational_grid='1/10^100',
                  status='FAIL' if module.failures else 'PASS', checks=module.checks,
                  failures=module.failures, evidence=module.evidence)
    (OUT/'centered-appell-629-replay.json').write_text(json.dumps(replay, indent=2)+'\n')
    check('complete same-code replay equals original', replay == old)
    for path, expected in evidence['original_hashes'].items():
        check('original preserved '+path, digest(path) == expected)


def main():
    OUT.mkdir(exist_ok=True)
    try:
        algebra()
        numerical()
    except Exception as exc:
        failures.append(type(exc).__name__+': '+str(exc))
    result = dict(scope='Independent finite L825 audit; inherited L778/L791 contracts',
                  method='exact Fraction endpoints, sparse rational coefficient expansion, separate same-code replay',
                  status='FAIL' if failures else 'PASS', checks=checks, failures=failures, evidence=evidence)
    target = OUT/'audit-report.json'
    target.write_text(json.dumps(result, indent=2)+'\n')
    print('status:', result['status'], 'checks:', len(checks), 'failures:', failures)
    print('actual defect: strictly inside (9.582501, 9.582502)' if not failures else 'actual bound: see certificate')
    print('required defect: 0 exactly; full certificate:', target.relative_to(ROOT))
    raise SystemExit(bool(failures))


if __name__ == '__main__':
    main()
