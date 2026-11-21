"""Independent finite L827 audit; no transcendental backend is imported.

All computations below use unrounded Fraction endpoints. Decimal output
is rounded outwards only when serializing the independent certificate.
The original program is also replayed into a separate output directory.
"""
import hashlib
import importlib.util
import itertools
import json
import math
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BASE = Path(__file__).resolve().parent
DEST = BASE / 'audit-641'
SCALE = 10**100


def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def interval(pair):
    lo, hi = map(F, pair)
    assert lo <= hi
    return lo, hi


def add(x, y):
    return x[0]+y[0], x[1]+y[1]


def neg(x):
    return -x[1], -x[0]


def sub(x, y):
    return add(x, neg(y))


def mul(x, y):
    products = [a*b for a in x for b in y]
    return min(products), max(products)


def div(x, y):
    assert y[0] > 0
    return mul(x, (1/y[1], 1/y[0]))


def scalar(n):
    return F(n), F(n)


def square_positive(x):
    assert x[0] > 0
    return x[0]**2, x[1]**2


def symmetric_minors(h):
    a, b, c = h[0]
    d, e, f = h[1][1], h[1][2], h[2][2]
    two = sub(mul(a, d), square_positive(b))
    # det = adf + 2bce - ae^2 - dc^2 - fb^2.
    three = add(mul(mul(a, d), f), mul(scalar(2), mul(mul(b, c), e)))
    for term in (mul(a, square_positive(e)), mul(d, square_positive(c)),
                 mul(f, square_positive(b))):
        three = sub(three, term)
    return [a, two, three]


def leibniz(h):
    """Unrounded check of the original expression, using saved matrix intervals."""
    n = len(h)
    value = scalar(0)
    for perm in itertools.permutations(range(n)):
        inversions = sum(perm[i] > perm[j] for i in range(n) for j in range(i+1, n))
        term = scalar((-1)**inversions)
        for i in range(n):
            term = mul(term, h[i][perm[i]])
        value = add(value, term)
    return value


def decimal_integer(n):
    sign = '-' if n < 0 else ''
    whole, fraction = divmod(abs(n), SCALE)
    return sign+str(whole)+'.'+str(fraction).zfill(100)


def encode(x):
    return [decimal_integer((x[0]*SCALE).__floor__()),
            decimal_integer((x[1]*SCALE).__ceil__())]


def main():
    DEST.mkdir(exist_ok=True)
    program = BASE / 'six_moments_639.py'
    original = BASE / 'six-moment-certificate-639.json'
    source = ROOT / 'scripts/actual-fredholm/fixed-pair-certificate-431.json'
    audit433 = ROOT / 'scripts/actual-fredholm/audit-433/audit-report.json'
    replay433 = ROOT / 'scripts/actual-fredholm/audit-433/fixed-pair-certificate-431.json'
    model = ROOT / 'scripts/central-jacobi/fixed-model-certificate-476.json'
    paths = (program, original, source, audit433, replay433, model)
    hashes = {str(p.relative_to(ROOT)): digest(p) for p in paths}
    result = dict(step=641, status='INCOMPLETE', checks=[], failures=[],
                  arithmetic='Unrounded exact Fraction endpoints; serialization outward at 10^-100',
                  scope='L827 indices 0..5 only; inherited analytic and Decimal contracts trusted',
                  input_hashes=hashes, audit_program_sha256=digest(Path(__file__)))

    def check(name, condition):
        result['checks'].append(dict(name=name, passed=bool(condition)))
        if not condition:
            result['failures'].append(name)

    def contains(name, saved, calculated):
        lo, hi = interval(saved)
        check(name, lo <= calculated[0] <= calculated[1] <= hi)

    try:
        old = json.loads(original.read_text())
        src = json.loads(source.read_text())['evaluation']
        prior = json.loads(audit433.read_text())
        check('original result and failures', old['status'] == 'FINITE_STIELTJES_FEASIBLE' and old['failures'] == [])
        check('original program hash', old['program_sha256'] == digest(program))
        for path in (source, audit433, replay433, model):
            check('original input hash: '+str(path.relative_to(ROOT)),
                  old['input_hashes'][str(path.relative_to(ROOT))] == digest(path))
        check('L778 source hash', prior['original_sha256'] == digest(source))
        check('L791 source hash', json.loads(model.read_text())['source_sha256'] == digest(source))
        check('prior audit passed', prior['status'] == 'PASS' and prior['failures'] == [])
        check('complete evaluator equals audited replay', src == json.loads(replay433.read_text())['evaluation'])
        check('complex disk radius 1600', src['uniform_disk_radius'] == 1600)
        error = interval(src['uniform_G_error'])
        check('uniform error contracts', 0 < error[0] <= error[1] < F('3.141e-48'))
        check('all six coefficient sources exact', old['source_P0_coefficients'] == src['coefficients'][:6])
        check('full source error exact', old['source_uniform_G_error'] == src['uniform_G_error'])

        aa, gg, errors = [], [], []
        for j in range(6):
            eps = error[1]/1600**j
            errors.append((F(0), eps))
            a = add(interval(src['coefficients'][j]), (-eps, eps))
            g = mul(a, scalar(8*4**j*math.factorial(j)))
            aa.append(a)
            gg.append(g)
            contains('Cauchy error '+str(j), old['cauchy_error_upper_enclosures'][j], errors[-1])
            contains('actual a '+str(j), old['actual_a'][j], a)
            contains('gamma '+str(j), old['gamma'][j], g)
            check('positive a and denominator '+str(j), a[0] > 0 and g[0] > 0)
        ss = [scalar(1)]+[div(gg[0], gg[j]) for j in range(1, 6)]
        check('exact s0', interval(old['s'][0]) == scalar(1))
        for j, s in enumerate(ss):
            contains('s '+str(j), old['s'][j], s)
        result['cauchy_error_upper_enclosures'] = [encode(e) for e in errors]
        result['actual_a'] = [encode(a) for a in aa]
        result['gamma'] = [encode(g) for g in gg]
        result['s'] = [encode(s) for s in ss]
        result['matrices'], result['symmetric_leading_minors'] = {}, {}
        result['saved_expression_rechecks'] = {}
        result['coarse_claim_bounds'] = {
            'H0': [['1', '1'], ['140.1990173', '140.1990174'],
                   ['5334110.4436894', '5334110.4436896']],
            'H1': [['43.2806880', '43.2806882'], ['254353.281348', '254353.281350'],
                   ['396820791357.236416', '396820791357.236419']]}
        for shift in (0, 1):
            name = 'H'+str(shift)
            h = [[ss[i+j+shift] for j in range(3)] for i in range(3)]
            saved_h = [[interval(v) for v in row] for row in old['matrices'][name]]
            check(name+' full Hankel layout', old['matrices'][name] ==
                  [[old['s'][i+j+shift] for j in range(3)] for i in range(3)])
            check(name+' symmetry', all(saved_h[i][j] == saved_h[j][i] for i in range(3) for j in range(3)))
            minors = symmetric_minors(h)
            rerun = [leibniz([row[:k] for row in saved_h[:k]]) for k in (1, 2, 3)]
            for k in range(3):
                check(name+' independent minor '+str(k+1)+' > 0', minors[k][0] > 0)
                contains(name+' saved minor expression '+str(k+1), old['leading_principal_minors'][name][k], rerun[k])
                contains(name+' independent minor '+str(k+1), old['leading_principal_minors'][name][k], minors[k])
                contains(name+' displayed bounds '+str(k+1), result['coarse_claim_bounds'][name][k],
                         interval(old['leading_principal_minors'][name][k]))
            check(name+' reported positive definite', old['positive_definite'][name] is True)
            result['matrices'][name] = [[encode(v) for v in row] for row in h]
            result['symmetric_leading_minors'][name] = [encode(v) for v in minors]
            result['saved_expression_rechecks'][name] = [encode(v) for v in rerun]
        check('correct range vector', old['range_condition']['vector'] == old['s'][3:6])
        check('range reported verified', old['range_condition']['verified'] is True)
        result['theorem_hypotheses'] = dict(
            criterion='Curto–Fialkow (1991), Theorem 5.1 p625, k=2; exact moments',
            real_data=True, positive_zeroth_moment='s0=1 exactly',
            H0='positive definite by three strict leading minors and Sylvester',
            H1='positive definite by three strict leading minors and Sylvester',
            range='H0 invertible; (s3,s4,s5) belongs to R^3 = Ran(H0)',
            support='[0,infinity), zero allowed', total_mass='1',
            limits='No infinite moment law or sign-transfer conclusion')

        spec = importlib.util.spec_from_file_location('original_six_moments_639', program)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        module.OUT = DEST / 'six-moment-replay-639.json'
        module.main()
        fresh = json.loads(module.OUT.read_text())
        differences = [k for k in set(old) | set(fresh) if old.get(k) != fresh.get(k)]
        result['replay_differing_fields'] = differences
        check('fresh original replay exact semantic match', not [k for k in differences if k != 'python'])
        result['original_python'], result['replay_python'] = old['python'], fresh['python']
        for path in paths:
            check('preserved '+str(path.relative_to(ROOT)), digest(path) == hashes[str(path.relative_to(ROOT))])
    except Exception as exc:
        result['failures'].append(type(exc).__name__+': '+str(exc))
    result['status'] = 'PASS' if not result['failures'] else 'FAIL'
    report = DEST / 'audit-report.json'
    report.write_text(json.dumps(result, indent=2)+'\n')
    print('Independent audit:', result['status'], '; checks:', len(result['checks']))
    print('Required: all six positive leading minors; source error < 3.141e-48; positive divisions; equality/range/support conditions')
    for name, minors in result.get('symmetric_leading_minors', {}).items():
        for k, pair in enumerate(minors, 1):
            lo, hi = map(F, pair)
            print(name, 'minor', k, ':', (lo*10**6).__floor__(), '/ 10^6 <= actual <=',
                  (hi*10**6).__ceil__(), '/ 10^6; required > 0')
    print('Failures:', result['failures'])
    print('Certificate:', report.relative_to(ROOT))
    if result['status'] != 'PASS':
        raise SystemExit(1)


if __name__ == '__main__':
    main()
