"""One bounded Q_(2,5) certificate, using audited boxes and exact Fractions.

Numpy supplies one candidate list only. All conclusions use strict rational
Pellet inequalities, not the approximate roots. No theta evaluation occurs.
"""
from fractions import Fraction as F
from itertools import product
from math import comb, factorial
from pathlib import Path
import hashlib
import json
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).with_name('reference-roots-certificate-551.json')
checks, failures = [], []


def check(name, passed):
    checks.append({'name': name, 'passed': bool(passed)})
    if not passed:
        failures.append(name)


def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def box(a):
    a = tuple(map(F, a))
    if len(a) != 2 or a[0] > a[1]:
        raise ValueError('invalid interval')
    return a


def pt(x):
    return F(x), F(x)


def add(a, b):
    return a[0]+b[0], a[1]+b[1]


def neg(a):
    return -a[1], -a[0]


def mul(a, b):
    v = [x*y for x, y in product(a, b)]
    return min(v), max(v)


def power(a, n):
    out = pt(1)
    for _ in range(n):
        out = mul(out, a)
    return out


def serial(a):
    return [str(x) for x in a]


def coarse(a):
    scale = 10**40
    lo = (a[0]*scale).__floor__()
    hi = -(-a[1]*scale).__floor__()
    result = F(lo, scale), F(hi, scale)
    check('outward coarsening', result[0] <= a[0] <= a[1] <= result[1])
    return result


def cadd(a, b):
    return add(a[0], b[0]), add(a[1], b[1])


def cmul(a, b):
    return add(mul(a[0], b[0]), neg(mul(a[1], b[1]))), add(mul(a[0], b[1]), mul(a[1], b[0]))


def cpow(a, n):
    out = pt(1), pt(0)
    for _ in range(n):
        out = cmul(out, a)
    return out


def absbounds(a):
    lo = 0 if a[0] <= 0 <= a[1] else min(abs(a[0]), abs(a[1]))
    return F(lo), max(abs(a[0]), abs(a[1]))


def modulus_bounds(a):
    # max(|Re|,|Im|) <= |z| <= |Re|+|Im|, no floating sqrt.
    real, imag = absbounds(a[0]), absbounds(a[1])
    return max(real[0], imag[0]), real[1]+imag[1]


def decade_below(x):
    if x <= 0:
        raise ValueError('positive comparison required')
    value = F(1)
    while value > x:
        value /= 10
    while 10*value <= x:
        value *= 10
    return value


def pellet(coeff, center, radius):
    m = pt(center[0]), pt(center[1])
    taylor, mods = [], []
    for k in range(6):
        value = pt(0), pt(0)
        for j in range(k, 6):
            term = cmul((mul(pt(comb(j, k)), coeff[j]), pt(0)), cpow(m, j-k))
            value = cadd(value, term)
        taylor.append(value)
        mods.append(modulus_bounds(value))
    lower = mods[1][0]*radius
    terms = [mods[k][1]*radius**k if k != 1 else F(0) for k in range(6)]
    upper = sum(terms)
    simple_lower = decade_below(lower) if lower > 0 else F(0)
    simple_upper = 10*decade_below(upper) if upper > 0 else F(0)
    return {'center': serial(center), 'radius': str(radius), 'k': 1, 'K': 1,
            'taylor_coefficients': [[serial(v[0]), serial(v[1])] for v in taylor],
            'modulus_bounds': [serial(v) for v in mods],
            'dominant_lower': str(lower), 'other_upper_terms': list(map(str, terms)),
            'other_upper_sum': str(upper), 'strict_margin': str(lower-upper),
            'simple_comparison': {'dominant_lower_at_least': str(simple_lower),
                                  'other_upper_less_than': str(simple_upper),
                                  'bounds_verified': lower >= simple_lower and upper < simple_upper,
                                  'strictly_decisive': simple_lower > simple_upper},
            'accepted': lower > upper}


def main():
    source_path = ROOT/'scripts/theta-gauss/audit-certificate-542.json'
    audit = json.loads(source_path.read_text())
    before = {str(source_path.relative_to(ROOT)): digest(source_path)}
    check('audit542 PASS with 106 checks', audit['status'] == 'PASS' and
          len(audit['checks']) == 106 and all(c['passed'] for c in audit['checks']) and not audit['failures'])
    for name, expected in audit['evidence']['input_hashes'].items():
        before[name] = digest(ROOT/name)
        check('audited source hash '+name, before[name] == expected)
    before['scripts/theta-gauss/audit_542.py'] = digest(ROOT/'scripts/theta-gauss/audit_542.py')
    check('audit542 implementation hash', before['scripts/theta-gauss/audit_542.py'] == audit['program_sha256'])
    check('step540 exact known digest', before['scripts/theta-gauss/two-node-certificate-540.json'] ==
          'f007b42bb0a51a1a9b13c39c5ee3b6010c605b33c0c87d95a271754a54db9f63')
    check('actual moment exact known digest', before['scripts/central-jacobi/fixed-model-certificate-476.json'] ==
          '2b429e4029fd7f50b30ea61b43d1be5aa22155b4c680c69440a716ff26643b2e')
    full_nodes = [box(a) for a in audit['evidence']['independent_nodes']]
    full_weights = [box(a) for a in audit['evidence']['independent_weights']]
    nodes, weights = [coarse(a) for a in full_nodes], [coarse(a) for a in full_weights]
    check('positive distinct nodes and weights', 0 < nodes[0][0] <= nodes[0][1] < nodes[1][0] and
          all(a[0] > 0 for a in weights))
    moments, coeff = [], []
    factors = [F((-1)**j*comb(5, j)*factorial(j), factorial(2*j)) for j in range(6)]
    check('explicit factorial normalization', factors == list(map(F, ['1', '-5/2', '5/6', '-1/12', '1/336', '-1/30240'])))
    for j in range(6):
        moment = add(mul(weights[0], power(nodes[0], j)), mul(weights[1], power(nodes[1], j)))
        moments.append(moment)
        coeff.append(pt(1) if j == 0 else mul(pt(factors[j]), moment))
    # L805 proves sum weights=1 exactly; never infer it from box containment.
    check('constant enclosure consistent with exact weight sum', moments[0][0] <= 1 <= moments[0][1])
    check('degree exactly five', coeff[5][1] < 0)
    if failures:
        raise RuntimeError('input or normalization failure: '+repr(failures))
    mids = [float((a[0]+a[1])/2) for a in coeff]
    approx = sorted(np.roots(mids[::-1]), key=lambda z: (float(z.real), float(z.imag)))
    centers = [(F(str(round(float(z.real), 6))), F(str(round(float(z.imag), 6)))) for z in approx]
    # One region choice plus at most one global radius refinement, no new list.
    rounds = []
    selected = None
    for radius in (F(1, 100), F(1, 10)):
        tests = [pellet(coeff, c, radius) for c in centers]
        disjoint = all((a[0]-b[0])**2+(a[1]-b[1])**2 > (2*radius)**2
                       for i, a in enumerate(centers) for b in centers[i+1:])
        rounds.append({'radius': str(radius), 'tests': tests, 'pairwise_disjoint': disjoint})
        if all(t['accepted'] for t in tests) and disjoint:
            selected = rounds[-1]
            break
    geometry = []
    if selected:
        radius = F(selected['radius'])
        check('all five simple displayed comparisons verified and decisive', all(
            t['simple_comparison']['bounds_verified'] and t['simple_comparison']['strictly_decisive']
            for t in selected['tests']))
        check('all center squared separations exceed one', all(
            (a[0]-b[0])**2+(a[1]-b[1])**2 > 1
            for i, a in enumerate(centers) for b in centers[i+1:]))
        for c in centers:
            if abs(c[1]) > radius:
                kind = 'NONREAL'
            elif c[1] == 0 and c[0]-radius > 0:
                kind = 'SIMPLE_POSITIVE_REAL'
            elif c[1] == 0 and c[0]+radius < 0:
                kind = 'SIMPLE_NEGATIVE_REAL'
            else:
                kind = 'UNDECIDED_LOCATION'
            geometry.append(kind)
    outcome = 'INCONCLUSIVE'
    if selected and all(k == 'SIMPLE_POSITIVE_REAL' for k in geometry):
        outcome = 'FIVE_SIMPLE_POSITIVE_ROOTS'
    elif selected and any(k in ('NONREAL', 'SIMPLE_NEGATIVE_REAL') for k in geometry):
        outcome = 'REFERENCE_HYPERBOLICITY_REFUTED'
    check('all source artifacts unchanged', all(digest(ROOT/p) == h for p, h in before.items()))
    report = {'status': 'PASS' if not failures else 'FAIL', 'outcome': outcome,
              'checks': checks, 'failures': failures, 'input_hashes': before,
              'program_sha256': digest(Path(__file__)),
              'input_nodes_full': [serial(a) for a in full_nodes],
              'input_weights_full': [serial(a) for a in full_weights],
              'coarsened_nodes': [serial(a) for a in nodes], 'coarsened_weights': [serial(a) for a in weights],
              'quadrature_moments': [serial(a) for a in moments],
              'coefficient_factors': list(map(str, factors)), 'coefficients_ascending': [serial(a) for a in coeff],
              'constant_term_reason': 'L805 exact weight sum=1; not interval residual inference',
              'candidate_only': {'numpy_version': np.__version__, 'roots': [[float(z.real), float(z.imag)] for z in approx],
                                 'use': 'region selection only; not mathematical evidence'},
              'rounds': rounds, 'root_geometry': geometry,
              'requirements': 'Five disjoint k=1 strict Pellet disks; reality from conjugation for real-centered disks; positivity requires center-radius>0.',
              'inherited_qualifications': audit['evidence']['inherited_qualifications'],
              'scope': 'Q_(2,5) only; no actual P5, signed-margin, degree-uniform or RH conclusion'}
    OUT.write_text(json.dumps(report, indent=2)+'\n')
    print('status:', report['status'], '; outcome:', outcome, '; failures:', failures)
    print('coefficient construction: six outward rational boxes; degree5; constant1')
    print('candidate centers:', [serial(c) for c in centers])
    for row in rounds:
        print('radius:', row['radius'], '; accepted k=1 disks:', sum(t['accepted'] for t in row['tests']), '/5; disjoint:', row['pairwise_disjoint'])
        print('strict lower/upper ratios:', [round(float(F(t['dominant_lower'])/F(t['other_upper_sum'])), 3) for t in row['tests']], '; required >1')
    print('certified geometry:', geometry)
    print('full certificate:', OUT.relative_to(ROOT))
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
