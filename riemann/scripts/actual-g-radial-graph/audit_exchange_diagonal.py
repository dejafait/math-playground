"""L848 audit: complete replay comparison and a second Taylor caller.

The second caller forms Taylor coefficients by the binomial formula,
not the generator's Horner jets. Both use L778's reviewed interval
primitives and inherited polynomial; neither redoes theta quadrature.
All original files are read-only. Full evidence is saved, not printed.
"""
import hashlib
import importlib.util
import json
import math
import platform
import sys
from fractions import Fraction as Q
from pathlib import Path

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
SOURCE = ROOT / 'scripts/actual-fredholm/fixed-pair-certificate-431.json'
BACKEND = ROOT / 'scripts/actual-fredholm/fixed_pair_431.py'
ORIGINAL = HERE / 'exchange-diagonal-certificate.json'
REPLAY = HERE / 'exchange-diagonal-audit-replay.json'
VALIDATION = HERE / 'exchange-diagonal-validation.json'
OUTPUT = HERE / 'exchange-diagonal-conceptual-audit.json'
GENERATOR = HERE / 'exchange_diagonal_certificate.py'
if OUTPUT.exists():
    raise SystemExit('Preserve existing evidence: audit output already exists.')


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


protected = {str(p.relative_to(ROOT)): sha(p) for p in
             (SOURCE, BACKEND, ORIGINAL, VALIDATION, GENERATOR)}
spec = importlib.util.spec_from_file_location('audited_l778_primitives', BACKEND)
b = importlib.util.module_from_spec(spec)
spec.loader.exec_module(b)
I, C = b.I, b.C
for context in (b.DN, b.UP, b.RN):
    context.clear_flags()
data = json.loads(ORIGINAL.read_text())
replay = json.loads(REPLAY.read_text())
old_validation = json.loads(VALIDATION.read_text())
inherited = json.loads(SOURCE.read_text())['evaluation']
coeff, eg = b.load_coeff(inherited)
checks, failures, records = [], [], []


def check(name, ok, **evidence):
    checks.append({'name': name, 'pass': bool(ok), **evidence})
    if not ok:
        failures.append(name)


def rational(x):
    return I(x.numerator) / x.denominator


def box_contains(box, re, im):
    return (Q(box[0][0]) <= re <= Q(box[0][1]) and
            Q(box[1][0]) <= im <= Q(box[1][1]))


def exact_center(quad, t):
    x, y = 600*(1-t*t)/(1+t*t), 1200*t/(1+t*t)
    for _ in range(quad):
        x, y = -y, x
    return x-400, y


check('entire original certificate exactly replayed', replay == data,
      compared='all fields, all 261 accepted arcs and all five refinements')
check('all input hashes match', all(sha(ROOT / p) == digest for p, digest in data['inputs'].items()))
check('original generator hash matches', data['program_sha256'] == sha(GENERATOR))
check('all inherited coefficient intervals and full error match',
      len(coeff) == 97 and data['inherited_coefficients'] == inherited['coefficients']
      and data['inherited_uniform_G_error'] == inherited['uniform_G_error'])
check('inherited evaluator and geometry domains', inherited['uniform_disk_radius'] >= 1600
      and 1000+256 < 1600 and 200 > 0)
check('original checks and failures', not data['failures'] and all(x['pass'] for x in data['checks'])
      and not old_validation['failures'] and all(x['pass'] for x in old_validation['checks']))
mp_exact = sum(max(abs(Q(a)), abs(Q(c)))*1600**n
               for n, (a, c) in enumerate(inherited['coefficients']))
mp = sum((I(a.mag())*(I(1600)**n) for n, a in enumerate(coeff)), I(0))
check('global polynomial bound outward', Q(mp.hi) >= mp_exact
      and Q(data['polynomial_global_magnitude_upper']) >= mp_exact)
check('full analytic error retained', 0 <= eg.lo <= eg.hi < b.D('3.141e-48'))

for kind in ('arcs', 'refinements'):
    for index, rec in enumerate(data[kind]):
        quad = rec['quadrant']
        left, right = map(Q, rec['t'])
        mid = (left+right)/2
        z0 = b.circle(600, quad, rational(mid))-400
        zb = b.circle(600, quad, I(rational(left).lo, rational(right).hi))-400
        dz = zb-z0
        rho = I(dz.mag())/256
        # Independent finite binomial formula for normalized derivatives.
        powers = [C(1)]
        for n in range(96):
            powers.append(powers[-1]*z0)
        jet = [sum((powers[n-j]*(coeff[n]*math.comb(n, j))
                    for n in range(j, 97)), C()) for j in range(9)]
        val = jet[8]
        for j in range(7, -1, -1):
            val = val*dz+jet[j]
        tail = mp*(rho**9)/(1-rho)
        error = tail+eg
        gb = C(val.re+b.sym(error), val.im+b.sym(error))
        fb = gb/zb
        margin = fb.re+I(fb.im.lowabs())/3
        x, y = exact_center(quad, mid)
        # Exact Fraction checks use complete saved records, not previews.
        zr, zi = [tuple(map(Q, pair)) for pair in rec['curve_box']]
        re, im = [tuple(map(Q, pair)) for pair in rec['f_box']]
        sr = Q(rec['delta_over_256'][1])
        denlow = max(Q(0), zr[0], -zr[1])**2 + max(Q(0), zi[0], -zi[1])**2
        loc = {
            'parameter_and_depth': 0 <= quad < 4 and 0 <= left < right <= 1
                and right-left == Q(1, 64*2**rec['depth']) and 0 <= rec['depth'] <= 8,
            'exact_center_inside_box': box_contains(rec['center_box'], x, y),
            'exact_center_on_circle': (x+400)**2+y*y == 600**2,
            'center_and_curve_boxes_reproduced': rec['center_box'] == z0.pair() and rec['curve_box'] == zb.pair(),
            'delta_radius_reproduced': rec['delta_over_256'] == rho.pair(),
            'exact_delta_square_bound': (256*sr)**2 >=
                max(abs(zr[0]-Q(rec['center_box'][0][1])), abs(zr[1]-Q(rec['center_box'][0][0])))**2 +
                max(abs(zi[0]-Q(rec['center_box'][1][1])), abs(zi[1]-Q(rec['center_box'][1][0])))**2,
            'nonzero_division_and_Cauchy_ratio': denlow > 0 and 0 <= sr < 1,
            'saved_complete_Taylor_tail': Q(rec['polynomial_Taylor_tail'][1]) >=
                Q(data['polynomial_global_magnitude_upper'])*sr**9/(1-sr),
            'saved_complete_analytic_error': Q(rec['Taylor_tail_plus_G_error'][1]) >=
                Q(rec['polynomial_Taylor_tail'][1])+Q(eg.hi),
            'saved_margin_outward': Q(rec['sector_margin_lower']) <= re[0]+max(Q(0), im[0], -im[1])/3,
            'saved_f_intervals_ordered': re[0] <= re[1] and im[0] <= im[1],
            'binomial_caller_Cauchy_ratio': 0 <= rho.lo <= rho.hi < 1,
        }
        if kind == 'arcs':
            loc['original_threshold'] = Q(rec['sector_margin_lower']) > Q(14, 10**9)
            loc['binomial_caller_threshold'] = Q(margin.lo) > Q(14, 10**9)
        else:
            loc['retained_refinement_reason'] = Q(rec['sector_margin_lower']) <= 0
        ok = all(loc.values())
        if not ok:
            failures.append(f'{kind}/{index}: '+', '.join(k for k, v in loc.items() if not v))
        records.append({'kind': kind, 'index': index, 'quadrant': quad, 't': rec['t'],
                        'checks': loc, 'pass': ok, 'Taylor_coefficients': [a.pair() for a in jet],
                        'delta_box': dz.pair(), 'rho': rho.pair(),
                        'Taylor_tail': tail.pair(), 'full_error': error.pair(),
                        'G_box': gb.pair(), 'f_box': fb.pair(),
                        'sector_margin_lower': str(margin.lo)})
    print('Checked full', kind, len(data[kind]), flush=True)

all_nodes = {(r['quadrant'], *r['t']): r for r in data['arcs']+data['refinements']}
check('all subdivision nodes unique', len(all_nodes) == len(data['arcs'])+len(data['refinements']))
for quad in range(4):
    pairs = [tuple(map(Q, r['t'])) for r in data['arcs'] if r['quadrant'] == quad]
    check('exact complete partition '+str(quad), bool(pairs) and pairs[0][0] == 0
          and pairs[-1][1] == 1 and all(a < c for a, c in pairs)
          and all(pairs[j][1] == pairs[j+1][0] for j in range(len(pairs)-1)), actual_arcs=len(pairs))
for index, rec in enumerate(data['refinements']):
    left, right = map(Q, rec['t'])
    mid = (left+right)/2
    children = [all_nodes.get((rec['quadrant'], str(a), str(c))) for a, c in ((left, mid), (mid, right))]
    check('both refinement children retained '+str(index),
          all(r is not None and r['depth'] == rec['depth']+1 for r in children))
check('all expected arcs and refinements checked', len(data['arcs']) == 261 and len(data['refinements']) == 5
      and len(records) == 266 and all(r['pass'] for r in records))

# Independently sum the real polynomial by successive powers at both endpoints.
radius = I(200000).sqrt()
gpoints = []
for v in (radius, -radius):
    power, value = I(1), I(0)
    for a in coeff:
        value += a*power
        power *= v
    gpoints.append(value+b.sym(eg))
qp = -gpoints[0]*gpoints[1]/50000
check('sqrt encloses exact antipodal radius within domain',
      0 < Q(radius.lo)**2 <= 200000 <= Q(radius.hi)**2 < 1600**2)
check('independent real point G values positive', all(g.lo > 0 for g in gpoints),
      actual=[g.pair() for g in gpoints], required='both > 0')
check('independent antipodal negative interval', Q(-4546, 10**11) < Q(qp.lo) <= Q(qp.hi) < Q(-4545, 10**11),
      actual=qp.pair(), required='-4.546e-8 < q/C < -4.545e-8')
z_bad = b.circle(600, 1, I(1)/4)-400
f_bad = b.geval(coeff, eg, z_bad)/z_bad
check('retained stronger-sector failure reproduced', f_bad.re.hi < 0
      and old_validation['stronger_condition_counterexample']['f_box'] == f_bad.pair(), actual=f_bad.re.pair())
flags = {name: [flag.__name__ for flag, val in context.flags.items() if val]
         for name, context in (('down', b.DN), ('up', b.UP), ('nearest', b.RN))}
check('no exceptional arithmetic flags', all(set(vals) <= {'Inexact', 'Rounded'} for vals in flags.values()), actual=flags)
check('all original evidence unchanged', all(sha(ROOT / p) == val for p, val in protected.items()))
minimum = min(Q(r['sector_margin_lower']) for r in records if r['kind'] == 'arcs')
minimum_string = min((r['sector_margin_lower'] for r in records if r['kind'] == 'arcs'), key=Q)
report = {
    'status': 'PASS' if not failures else 'FAIL',
    'scope': 'L848 complete numerical audit; analytic review is canonical in L848',
    'software': {'python': platform.python_version(), 'decimal': b.decimal.__version__,
                 'libmpdec': b.decimal.__libmpdec_version__},
    'inputs_sha256': protected, 'replay_sha256': sha(REPLAY), 'program_sha256': sha(Path(__file__)),
    'checks': checks, 'failures': failures,
    'summary': {'accepted_arcs': len(data['arcs']), 'refinements': len(data['refinements']),
                'binomial_sector_lower': minimum_string, 'required_sector_lower': '14/10^9',
                'all_arc_thresholds_pass': minimum > Q(14, 10**9)},
    'records': records,
    'extension_point': {'radius': radius.pair(), 'G_positive': gpoints[0].pair(),
                        'G_negative': gpoints[1].pair(), 'q_over_C': qp.pair()},
    'limitations': ['Reuses the audited L778 coefficient intervals and analytic error; no theta regeneration.',
                   'Both numerical callers share the reviewed Decimal interval primitives and trusted runtime.',
                   'Not a formally verified certificate or a positive global graph.']}
OUTPUT.write_text(json.dumps(report, indent=2)+'\n')
print(report['status'], 'sector lower', minimum_string, '; required > 14/10^9')
print('Antipodal q/C:', qp.pair(), '; required (-4.546e-8,-4.545e-8)')
print('Failures:', failures)
print('Full evidence:', OUTPUT.relative_to(ROOT))
if failures:
    raise SystemExit(1)
