"""Fixed approved 40-pair grid; exact rational Rouche certificates.

numpy supplies centers only. All acceptance tests and hinge bounds use
fractions.Fraction. Full coefficients, disks, Taylor coefficients and
strict comparison margins are saved for independent replay.
"""
from fractions import Fraction as Q
from math import comb
from pathlib import Path
import json
import numpy as np

OUT = Path(__file__).with_suffix('.json')
SCALES = [Q(1, 4), Q(1, 2), Q(1), Q(2), Q(4)]
THRESHOLDS = [Q(0), Q(1, 8), Q(1, 4), Q(1, 2), Q(1), Q(2), Q(4), Q(8)]
F = [Q(8984777, 463347), Q(3685712, 51483), Q(5490857, 51483),
     Q(4353808, 51483), Q(1947736, 51483), Q(1188, 131), Q(1)]
R = Q(1, 10**7)
DEN = 10**12
ZERO = (Q(0), Q(0))


def add(a, b):
    return a[0]+b[0], a[1]+b[1]


def mul(a, b):
    return a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0]


def scale(a, b):
    return a[0]*b, a[1]*b


def upper(a):
    return abs(a[0])+abs(a[1])


def lower(a):
    return max(abs(a[0]), abs(a[1]))


def encode(a):
    return [str(a[0]), str(a[1])]


def certify(p):
    seeds = np.roots([float(x) for x in reversed(p)])
    centers = sorted([(Q(round(float(z.real)*DEN), DEN),
                       Q(round(float(z.imag)*DEN), DEN)) for z in seeds])
    disks = []
    for c in centers:
        powers = [(Q(1), Q(0))]
        for _ in range(6):
            powers.append(mul(powers[-1], c))
        taylor = []
        for k in range(7):
            total = ZERO
            for j in range(k, 7):
                total = add(total, scale(powers[j-k], comb(j, k)*p[j]))
            taylor.append(total)
        main = lower(taylor[1])*R
        error = upper(taylor[0])+sum((upper(taylor[k])*R**k
                                              for k in range(2, 7)), Q(0))
        real = c[1] == 0
        lo = Q(0) if real else max(Q(0), abs(c[1])-R)
        hi = Q(0) if real else abs(c[1])+R
        disks.append({'center': encode(c), 'radius': str(R),
                      'taylor_coefficients_complex': [encode(z) for z in taylor],
                      'linear_lower_bound': str(main),
                      'error_upper_bound': str(error),
                      'strict_margin': str(main-error), 'rouche_pass': main > error,
                      'real_by_conjugation_if_certified': real,
                      'absolute_imaginary_bounds': [str(lo), str(hi)]})
    separations = []
    for i in range(6):
        for j in range(i+1, 6):
            dx, dy = centers[i][0]-centers[j][0], centers[i][1]-centers[j][1]
            separations.append({'indices': [i, j],
                                'distance_squared': str(dx*dx+dy*dy),
                                'required_strict_lower_bound': str((2*R)**2),
                                'pass': dx*dx+dy*dy > (2*R)**2})
    ok = (len(p) == 7 and p[-1] == 1 and len(disks) == 6
          and all(d['rouche_pass'] for d in disks)
          and all(v['pass'] for v in separations))
    return {'coefficients_ascending': [str(v) for v in p], 'degree': 6,
            'disks': disks, 'pairwise_separations': separations,
            'complete_simple_root_certificate': ok}


def hinge(cert, a):
    lows, highs = zip(*[(Q(d['absolute_imaginary_bounds'][0]),
                        Q(d['absolute_imaginary_bounds'][1])) for d in cert['disks']])
    return (sum((max(Q(0), v-a) for v in lows), Q(0)),
            sum((max(Q(0), v-a) for v in highs), Q(0)))


grids, failures = [], []
for s in SCALES:
    p = [c*s**(6-j) for j, c in enumerate(F)]
    image = [p[j]+(j+1)*p[j+1] if j+1 <= 6 else p[j] for j in range(7)]
    for j in range(5):
        image[j] += Q(5, 18)*(j+2)*(j+1)*p[j+2]
    inp, out = certify(p), certify(image)
    if not inp['complete_simple_root_certificate'] or not out['complete_simple_root_certificate']:
        failures.append('incomplete root certification at scale '+str(s))
    rows = []
    for a in THRESHOLDS:
        il, iu = hinge(inp, a)
        ol, ou = hinge(out, a)
        dl, du = ol-iu, ou-il
        status = ('certified_violation' if dl > 0 else
                  'certified_nonpositive' if du <= 0 else 'undecided')
        if not inp['complete_simple_root_certificate'] or not out['complete_simple_root_certificate']:
            status = 'uncertified'
        rows.append({'threshold': str(a), 'input_hinge_bounds': [str(il), str(iu)],
                     'output_hinge_bounds': [str(ol), str(ou)],
                     'deficit_bounds': [str(dl), str(du)], 'status': status})
    grids.append({'scale': str(s), 'input': inp, 'output': out, 'pairs': rows})

rows = [r for g in grids for r in g['pairs']]
min_margin = min(Q(d['strict_margin']) for g in grids for k in ['input', 'output']
                 for d in g[k]['disks'])
min_separation = min(Q(v['distance_squared']) for g in grids for k in ['input', 'output']
                     for v in g[k]['pairwise_separations'])
uniform_checks = {'all_60_margins_exceed_1_over_5000000000': min_margin > Q(1, 5000000000),
                  'all_150_squared_separations_exceed_1_over_1000000':
                  min_separation > Q(1, 1000000),
                  'exactly_40_pairs': len(rows) == 40}
failures.extend(k for k, ok in uniform_checks.items() if not ok)
counts = {status: sum(r['status'] == status for r in rows) for status in
          ['certified_violation', 'certified_nonpositive', 'undecided', 'uncertified']}
certificate = {'scope': 'Only the five approved scales and eight approved thresholds',
               'operator_coefficients_ascending': ['1', '1', '5/18'],
               'center_selection_only': 'numpy.roots; rounded to denominator 10^12',
               'radius': str(R), 'grids': grids, 'pair_count': len(rows),
               'counts': counts, 'uniform_checks': uniform_checks, 'failures': failures,
               'qualifications': ['Exact rational Rouche inequalities certify each disk.',
                 'Six pairwise disjoint single-root disks exhaust each sextic.',
                 'Real-centered disks contain a real root by conjugation and uniqueness.',
                 'No universal contraction, Xi realization, payment or RH conclusion.']}
OUT.write_text(json.dumps(certificate, indent=2)+'\n')
print('Complete polynomial certificates actual/required:',
      sum(g[k]['complete_simple_root_certificate'] for g in grids for k in ['input', 'output']), '/10')
print('Pairs actual/required:', len(rows), '/40; statuses:', counts)
for g in grids:
    print('scale', g['scale'], '; deficit intervals [lower,upper] in threshold order:')
    print([(r['threshold'], [float(Q(v)) for v in r['deficit_bounds']], r['status']) for r in g['pairs']])
print('Required violation threshold: lower deficit > 0')
print('Uniform exact checks:', uniform_checks)
print('Failures:', failures)
print('Full certificate:', OUT)
if failures:
    raise SystemExit(1)
