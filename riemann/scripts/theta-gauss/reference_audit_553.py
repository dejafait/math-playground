"""Independent exact replay of L808; no previous implementation is imported.

Positive endpoint powers reconstruct moments. Taylor rectangles are linear
interval combinations of exact rational complex point powers. No numpy,
theta evaluator, root search, or old certificate generator is run.
"""
from fractions import Fraction as R
from hashlib import sha256
from itertools import combinations
from math import comb, factorial
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).with_name('reference-audit-certificate-553.json')
checks, failures, evidence = [], [], {}


def check(name, condition):
    checks.append({'name': name, 'passed': bool(condition)})
    if not condition:
        failures.append(name)


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def load(name):
    return json.loads((ROOT / name).read_text())


def interval(value):
    a, b = map(R, value)
    if a > b:
        raise ValueError('reversed interval')
    return a, b


def scaled(a, t):
    p, q = a[0]*t, a[1]*t
    return min(p, q), max(p, q)


def sums(values):
    values = list(values)
    return sum((a[0] for a in values), R(0)), sum((a[1] for a in values), R(0))


def point_product(a, b):
    return a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0]


def magnitude_component(a):
    low, high = a
    return (R(0) if low <= 0 <= high else min(abs(low), abs(high)),
            max(abs(low), abs(high)))


def freeze(value):
    if isinstance(value, R):
        return str(value)
    if isinstance(value, (tuple, list)):
        return [freeze(x) for x in value]
    if isinstance(value, dict):
        return {k: freeze(v) for k, v in value.items()}
    return value


def run():
    name551 = 'scripts/theta-gauss/reference-roots-certificate-551.json'
    name542 = 'scripts/theta-gauss/audit-certificate-542.json'
    name540 = 'scripts/theta-gauss/two-node-certificate-540.json'
    c, a, b = load(name551), load(name542), load(name540)
    before = {}
    maps = [('551', c['input_hashes']), ('542', a['evidence']['input_hashes']),
            ('540', b['provenance']), ('540 inherited', b['inherited_original_hashes'])]
    for label, hashes in maps:
        for path, expected in hashes.items():
            before[path] = digest(ROOT / path)
            check(label + ' source hash ' + path, before[path] == expected)
    for label, program, report in [
        ('551', 'scripts/theta-gauss/reference_roots_551.py', c),
        ('542', 'scripts/theta-gauss/audit_542.py', a)]:
        before[program] = digest(ROOT / program)
        check(label + ' program hash', before[program] == report['program_sha256'])
    before[name551] = digest(ROOT / name551)
    check('551 provenance keys precisely extend 542',
          set(c['input_hashes']) == set(a['evidence']['input_hashes']) |
          {name542, 'scripts/theta-gauss/audit_542.py'})
    check('fixed step540 digest', before[name540] ==
          'f007b42bb0a51a1a9b13c39c5ee3b6010c605b33c0c87d95a271754a54db9f63')
    check('fixed actual moment digest', before['scripts/central-jacobi/fixed-model-certificate-476.json'] ==
          '2b429e4029fd7f50b30ea61b43d1be5aa22155b4c680c69440a716ff26643b2e')
    check('reuse completed step542, not a recursive backend audit',
          a['status'] == 'PASS' and len(a['checks']) == 106 and
          all(x['passed'] for x in a['checks']) and a['failures'] == [])
    check('inherited contracts unchanged',
          c['inherited_qualifications'] == a['evidence']['inherited_qualifications'])
    nodes = list(map(interval, a['evidence']['independent_nodes']))
    weights = list(map(interval, a['evidence']['independent_weights']))
    check('complete input boxes match independent audited evidence',
          nodes == list(map(interval, c['input_nodes_full'])) and
          weights == list(map(interval, c['input_weights_full'])) and
          len(nodes) == len(weights) == 2)
    evidence['input_nodes_full'], evidence['input_weights_full'] = nodes, weights
    scale = 10**40
    coarse = []
    for i, (lo, hi) in enumerate(nodes + weights):
        # Integer quotient implements floor/ceiling without the old helper.
        p, q = lo*scale, hi*scale
        low = R(p.numerator // p.denominator, scale)
        high = R(-((-q.numerator) // q.denominator), scale)
        check('coarsening containment ' + str(i), low <= lo <= hi <= high)
        check('coarsening grid ' + str(i),
              (low*scale).denominator == (high*scale).denominator == 1)
        coarse.append((low, high))
    v, w = coarse[:2], coarse[2:]
    check('all complete and coarse inputs positive and nodes ordered',
          all(t[0] > 0 for t in nodes + weights + coarse) and
          v[0][1] < v[1][0] and all(t[1] < 1 for t in w))
    check('coarse boxes match saved evidence',
          v == list(map(interval, c['coarsened_nodes'])) and
          w == list(map(interval, c['coarsened_weights'])))
    factors = [R((-1)**j*comb(5, j)*factorial(j), factorial(2*j)) for j in range(6)]
    check('all six factorial factors', factors == list(map(R, c['coefficient_factors'])) ==
          list(map(R, ['1', '-5/2', '5/6', '-1/12', '1/336', '-1/30240'])))
    moments = [tuple(sum(w[i][end]*v[i][end]**j for i in range(2))
                     for end in (0, 1)) for j in range(6)]
    coeff = [(R(1), R(1))] + [scaled(moments[j], factors[j]) for j in range(1, 6)]
    for j in range(6):
        check('complete quadrature moment ' + str(j), moments[j] == interval(c['quadrature_moments'][j]))
        check('complete coefficient ' + str(j), coeff[j] == interval(c['coefficients_ascending'][j]))
    check('constant compatible with L805 exact weight sum', moments[0][0] <= 1 <= moments[0][1])
    check('degree five', coeff[5][1] < 0)
    evidence.update(coarsened_nodes=v, coarsened_weights=w,
                    coefficient_factors=factors, quadrature_moments=moments,
                    coefficients_ascending=coeff,
                    exact_constant_reason='L805 equations (5): numerator sum=v2-v1; denominator nonzero. Interval containment is not an identity proof.')
    centers = [(R('19.379606'), R(0)), (R('26.150079'), R('-18.380803')),
               (R('26.150079'), R('18.380803')), (R('123.335006'), R(0)),
               (R('216.169131'), R(0))]
    radius = R(1, 100)
    check('one original round, radius 1/100 and five tests', len(c['rounds']) == 1 and
          R(c['rounds'][0]['radius']) == radius and len(c['rounds'][0]['tests']) == 5)
    targets = [(R(1, 10**4), R(1, 10**7)), (R(1, 10**4), R(1, 10**6)),
               (R(1, 10**4), R(1, 10**6)), (R(1, 10**3), R(1, 10**6)),
               (R(1, 10**2), R(1, 10**5))]
    tests = []
    for i, (m, saved, target) in enumerate(zip(centers, c['rounds'][0]['tests'], targets)):
        check('center and test hypotheses ' + str(i), tuple(map(R, saved['center'])) == m and
              R(saved['radius']) == radius and saved['k'] == saved['K'] == 1)
        powers = [(R(1), R(0))]
        for j in range(5):
            powers.append(point_product(powers[-1], m))
        taylor, components, modulus = [], [], []
        for k in range(6):
            rectangle = tuple(sums(scaled(coeff[j], comb(j, k)*powers[j-k][axis])
                                  for j in range(k, 6)) for axis in (0, 1))
            taylor.append(rectangle)
            comp = tuple(magnitude_component(x) for x in rectangle)
            components.append(comp)
            mod = max(comp[0][0], comp[1][0]), comp[0][1]+comp[1][1]
            modulus.append(mod)
            check('complete Taylor rectangle %d/%d' % (i, k),
                  rectangle == tuple(map(interval, saved['taylor_coefficients'][k])))
            check('complete modulus bounds %d/%d' % (i, k), mod == interval(saved['modulus_bounds'][k]))
        lower = radius*modulus[1][0]
        terms = [R(0) if k == 1 else radius**k*modulus[k][1] for k in range(6)]
        upper = sum(terms, R(0))
        margin = lower-upper
        check('all six omitted-slot/radius terms ' + str(i), terms == list(map(R, saved['other_upper_terms'])))
        check('exact dominant/upper/margin ' + str(i),
              lower == R(saved['dominant_lower']) and upper == R(saved['other_upper_sum']) and
              margin == R(saved['strict_margin']))
        check('strict Pellet inequality ' + str(i), lower > upper and margin > 0)
        comparison = saved['simple_comparison']
        check('displayed table and saved simplified bounds ' + str(i), lower >= target[0] > target[1] > upper and
              lower >= R(comparison['dominant_lower_at_least']) >
              R(comparison['other_upper_less_than']) > upper)
        # Strict lower integer bound for L/U; no decimal approximation is evidence.
        ratio_floor = (lower/upper).numerator // (lower/upper).denominator
        check('integer ratio lower bound ' + str(i), lower > ratio_floor*upper and ratio_floor > 1)
        tests.append(dict(center=m, radius=radius, taylor_coefficients=taylor,
                          component_modulus_bounds=components, modulus_bounds=modulus,
                          radius_powers=[radius**k for k in range(6)],
                          dominant_lower=lower, other_upper_terms=terms,
                          other_upper_sum=upper, strict_margin=margin,
                          simple_lower=target[0], simple_upper=target[1],
                          ratio_strictly_greater_than=ratio_floor,
                          required_ratio_strictly_greater_than=1))
    pairs = []
    for i, j in combinations(range(5), 2):
        d2 = sum((centers[i][k]-centers[j][k])**2 for k in (0, 1))
        check('disk separation %d/%d' % (i, j), d2 > 1 > (2*radius)**2)
        pairs.append(dict(pair=[i, j], squared_distance=d2, required_strict_lower=(2*radius)**2))
    check('positive real centers and conjugate nonreal geometry',
          all(centers[i][1] == 0 and centers[i][0] > radius for i in (0, 3, 4)) and
          centers[1][0] == centers[2][0] and centers[1][1] == -centers[2][1] and
          abs(centers[1][1]) > radius and abs(centers[2][1]) > radius)
    check('degree exhaustion', len(centers) == len(coeff)-1 == 5)
    evidence.update(tests=tests, pairwise_separations=pairs,
                    source_hashes=before, saved_status_flags_not_numerical_proof=True,
                    inherited_qualifications=a['evidence']['inherited_qualifications'])
    check('all original inputs unchanged', all(digest(ROOT / p) == h for p, h in before.items()))


if __name__ == '__main__':
    try:
        run()
    except Exception as exc:
        failures.append(type(exc).__name__ + ': ' + str(exc))
    report = dict(status='FAIL' if failures else 'PASS', checks=checks, failures=failures,
                  evidence=evidence, program_sha256=digest(Path(__file__)),
                  scope='Independent finite L808 audit only; inherited L805/L778 contracts retained.')
    OUT.write_text(json.dumps(freeze(report), indent=2)+'\n')
    print('status:', report['status'], '; checks:', len(checks), '; failures:', failures)
    for i, row in enumerate(evidence.get('tests', [])):
        print('disk', i, ': L/U >', row['ratio_strictly_greater_than'], '; required >1;',
              'L >=', row['simple_lower'], '; U <', row['simple_upper'])
    print('full certificate:', OUT.relative_to(ROOT))
    if failures:
        raise SystemExit(1)
