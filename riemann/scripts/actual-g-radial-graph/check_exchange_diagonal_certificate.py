"""Full saved-arc consistency checks and the explicit extension's bad point.

Exact Fraction checks inspect every saved arc and all 97 input intervals.
These checks do not independently replay Taylor-jet enclosure generation.
"""
import hashlib
import importlib.util
import json
import sys
from fractions import Fraction as Q
from pathlib import Path

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
CERT = HERE / 'exchange-diagonal-certificate.json'
OUT = HERE / 'exchange-diagonal-validation.json'
GENERATOR = HERE / 'exchange_diagonal_certificate.py'
BACKEND = ROOT / 'scripts/actual-fredholm/fixed_pair_431.py'
SOURCE = ROOT / 'scripts/actual-fredholm/fixed-pair-certificate-431.json'
checks, failures = [], []


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def check(name, good, **evidence):
    checks.append({'name': name, 'pass': bool(good), **evidence})
    if not good:
        failures.append(name)


data = json.loads(CERT.read_text())
inherited = json.loads(SOURCE.read_text())['evaluation']
check('generator hash matches', data['program_sha256'] == sha(GENERATOR))
for p in (SOURCE, BACKEND):
    check('input hash '+str(p.relative_to(ROOT)), data['inputs'][str(p.relative_to(ROOT))] == sha(p))
check('all coefficient intervals match audited input',
      data['inherited_coefficients'] == inherited['coefficients']
      and len(data['inherited_coefficients']) == 97)
check('uniform error matches audited input',
      data['inherited_uniform_G_error'] == inherited['uniform_G_error'])
mp = Q(data['polynomial_global_magnitude_upper'])
true_coefficient_bound = sum(max(abs(Q(a)), abs(Q(b)))*1600**n
                             for n, (a, b) in enumerate(inherited['coefficients']))
check('global polynomial bound rounded outward', mp >= true_coefficient_bound)
eg = Q(data['inherited_uniform_G_error'][1])
arc_checks = []
for index, rec in enumerate(data['arcs']):
    re, im = [tuple(map(Q, pair)) for pair in rec['f_box']]
    absolute_im_lower = max(Q(0), im[0], -im[1])
    margin = Q(rec['sector_margin_lower'])
    ratio = Q(rec['delta_over_256'][1])
    tail = Q(rec['polynomial_Taylor_tail'][1])
    total_error = Q(rec['Taylor_tail_plus_G_error'][1])
    zr, zi = [tuple(map(Q, pair)) for pair in rec['curve_box']]
    denominator_lower = max(Q(0), zr[0], -zr[1])**2 + max(Q(0), zi[0], -zi[1])**2
    local = {
        'arc': index,
        'sector_margin_rounded_outward': margin <= re[0]+absolute_im_lower/3,
        'coarse_sector_threshold': margin > Q(14, 10**9),
        'Cauchy_ratio': 0 <= ratio < 1,
        'complete_Taylor_tail': tail >= mp*ratio**9/(1-ratio),
        'complete_G_error': total_error >= tail+eg,
        'finite_ordered_f_intervals': re[0] <= re[1] and im[0] <= im[1],
        'division_rectangle_excludes_zero': denominator_lower > 0,
    }
    local['pass'] = all(v for k, v in local.items() if k != 'arc')
    arc_checks.append(local)
    if not local['pass']:
        failures.append('arc '+str(index))
check('all saved arcs satisfy exact consistency and coarse bounds',
      all(r['pass'] for r in arc_checks), inspected_arcs=len(arc_checks),
      required='sector margin > 14/10^9, exact outward inequalities')
for quad in range(4):
    arcs = [r for r in data['arcs'] if r['quadrant'] == quad]
    pairs = [tuple(map(Q, r['t'])) for r in arcs]
    check('exact full coverage quadrant '+str(quad),
          bool(pairs) and pairs[0][0] == 0 and pairs[-1][1] == 1
          and all(a < b for a, b in pairs)
          and all(pairs[j][1] == pairs[j+1][0] for j in range(len(pairs)-1)))
check('refinements retained', len(data['refinements']) == data['summary']['refinement_count'])
check('original claim has no failures', not data['failures'] and all(r['pass'] for r in data['checks']))

# A direct interval point evaluation; the same trusted backend is reused.
spec = importlib.util.spec_from_file_location('l778_point_backend', BACKEND)
backend = importlib.util.module_from_spec(spec)
spec.loader.exec_module(backend)
I, C = backend.I, backend.C
coeff, error = backend.load_coeff(inherited)
radius = I(200000).sqrt()
gplus = backend.geval(coeff, error, C(radius)).re
gminus = backend.geval(coeff, error, C(-radius)).re
q_over_C = -gplus*gminus/50000
check('extension antipodal point has negative density', q_over_C.hi < 0,
      actual=q_over_C.pair(), required='q(0,pi)/C < 0')
check('coarse extension negative interval',
      Q(-4546, 10**11) < Q(str(q_over_C.lo)) <= Q(str(q_over_C.hi)) < Q(-4545, 10**11),
      actual=q_over_C.pair(), required='-4.546e-8 < q(0,pi)/C < -4.545e-8')
check('both real G values are positive', gplus.lo > 0 and gminus.lo > 0,
      G_positive=gplus.pair(), G_negative=gminus.pair(), required='both > 0')

# The first certificate's chosen positive-real witness did not disprove
# Re f>0. Keep it; this separate exact rational point does.
z_bad_real = backend.circle(600, 1, I(1)/4)-400
f_bad_real = backend.geval(coeff, error, z_bad_real)/z_bad_real
check('stronger right-half-plane condition actually fails', f_bad_real.re.hi < 0,
      z=z_bad_real.pair(), actual_real_f=f_bad_real.re.pair(), required='<0')
result = {
    'status': 'PASS_PENDING_INDEPENDENT_AUDIT' if not failures else 'FAIL',
    'certificate_sha256': sha(CERT), 'program_sha256': sha(Path(__file__)),
    'checks': checks, 'arc_checks': arc_checks, 'failures': failures,
    'extension_point': {'radius': radius.pair(), 'G_positive': gplus.pair(),
                        'G_negative': gminus.pair(), 'q_over_C': q_over_C.pair()},
    'stronger_condition_counterexample': {'quadrant': 1, 't': '1/4',
                                         'z_box': z_bad_real.pair(), 'f_box': f_bad_real.pair()},
    'limitations': ['No independent regeneration of the 261 Taylor-jet enclosures.',
                   'New point evaluations reuse the audited L778 interval backend.',
                   'New mathematical application still awaits a separate conceptual audit.']}
OUT.write_text(json.dumps(result, indent=2)+'\n')
print(result['status'])
print('All arcs checked:', len(arc_checks), '; sector lower bound > 14/10^9 > 0')
print('Actual q(0,pi)/C:', q_over_C.pair(), '; required for obstruction: <0')
print('Stronger condition witness Re(G/z):', f_bad_real.re.pair(), '; required: <0')
print('Failures:', failures)
print('Full validation:', OUT.relative_to(ROOT))
if failures:
    raise SystemExit(1)
