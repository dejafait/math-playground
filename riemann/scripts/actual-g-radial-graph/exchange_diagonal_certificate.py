"""Certify one sector on |z+400|=600 using the audited L778 evaluator.

No theta recomputation, zero assumption, or floating-point sign test.
Every accepted arc and every refinement is retained in the output.
"""
import argparse
import hashlib
import importlib.util
import json
import platform
import sys
from fractions import Fraction as Q
from pathlib import Path

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[2]
BACKEND = ROOT / 'scripts/actual-fredholm/fixed_pair_431.py'
INPUT = ROOT / 'scripts/actual-fredholm/fixed-pair-certificate-431.json'
spec = importlib.util.spec_from_file_location('l778_interval_backend', BACKEND)
backend = importlib.util.module_from_spec(spec)
spec.loader.exec_module(backend)
I, C, D = backend.I, backend.C, backend.D


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def rational(x):
    return I(x.numerator)/x.denominator


def curve(quadrant, t):
    return backend.circle(600, quadrant, t)-400


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', default='exchange-diagonal-certificate.json')
    args = parser.parse_args()
    out = Path(__file__).with_name(args.output)
    if out.exists():
        raise SystemExit('Preserve existing evidence; choose a fresh --output name.')
    data = json.loads(INPUT.read_text())['evaluation']
    coeff, eg = backend.load_coeff(data)
    checks, failures, records, refinements = [], [], [], []

    def check(name, ok, **evidence):
        checks.append({'name': name, 'pass': bool(ok), **evidence})
        if not ok:
            failures.append(name)

    check('all degree-96 coefficient intervals loaded', len(coeff) == 97,
          actual=len(coeff), required=97)
    check('inherited uniform disk radius', Q(str(data['uniform_disk_radius'])) >= 1600,
          actual=data['uniform_disk_radius'], required='>=1600')
    check('inherited analytic G error', 0 <= eg.lo <= eg.hi < D('3.141e-48'),
          actual=eg.pair(), required='0 <= error < 3.141e-48')
    # The exact circle has |z| in [200,1000]; the radius-256 Taylor
    # disks centered on it lie in |z|<=1256<1600.
    check('geometric evaluator and Cauchy domains', 1000+256 < 1600,
          actual={'radial_range': [200, 1000], 'Taylor_disk_outer_radius': 1256},
          required={'nonzero_radial_lower': '>0', 'outer_radius': '<1600'})
    if failures:
        raise RuntimeError('Inherited input contract failed: '+str(failures))
    mp = sum((I(a.mag())*(I(1600)**n) for n, a in enumerate(coeff)), I(0))
    order, base, maxdepth = 8, 64, 8

    def segment(quad, left, right, depth):
        tl, tr, tm = rational(left), rational(right), rational((left+right)/2)
        z0 = curve(quad, tm)
        zb = curve(quad, I(tl.lo, tr.hi))
        delta = zb-z0
        ratio = I(delta.mag())/256
        assert ratio.hi < 1
        jet = [C() for _ in range(order+1)]
        for a in reversed(coeff):
            for j in range(order, 0, -1):
                jet[j] = jet[j]*z0+jet[j-1]
            jet[0] = jet[0]*z0+a
        val = jet[-1]
        for a in reversed(jet[:-1]):
            val = val*delta+a
        tail = mp*(ratio**(order+1))/(1-ratio)
        error = eg+tail
        gb = C(val.re+backend.sym(error), val.im+backend.sym(error))
        fb = gb/zb
        # This encloses Re f+|Im f|/3 from below on the whole arc.
        margin = fb.re+I(fb.im.lowabs())/3
        rec = {'quadrant': quad, 't': [str(left), str(right)], 'depth': depth,
               'center_box': z0.pair(), 'curve_box': zb.pair(),
               'delta_over_256': ratio.pair(), 'G_box': gb.pair(),
               'f_box': fb.pair(), 'polynomial_Taylor_tail': tail.pair(),
               'Taylor_tail_plus_G_error': error.pair(),
               'sector_margin_lower': str(margin.lo)}
        if margin.lo > 0:
            records.append(rec)
        elif depth < maxdepth:
            refinements.append(rec)
            mid = (left+right)/2
            segment(quad, left, mid, depth+1)
            segment(quad, mid, right, depth+1)
        else:
            records.append(rec)
            failures.append('sector unproved at quadrant '+str(quad)+' t='+str(rec['t']))

    for quad in range(4):
        for j in range(base):
            segment(quad, Q(j, base), Q(j+1, base), 0)
        print('Completed circle quadrant', quad+1, 'of 4;',
              len(records), 'accepted/terminal arcs', flush=True)
    for quad in range(4):
        arcs = [r for r in records if r['quadrant'] == quad]
        endpoints = [(Q(r['t'][0]), Q(r['t'][1])) for r in arcs]
        covered = (bool(endpoints) and endpoints[0][0] == 0 and endpoints[-1][1] == 1
                   and all(a < b for a, b in endpoints)
                   and all(endpoints[j][1] == endpoints[j+1][0]
                           for j in range(len(endpoints)-1)))
        check('complete quadrant '+str(quad)+' coverage', covered,
              actual_arcs=len(arcs), required='exact disjoint partition of [0,1]')
    lowest = min(D(r['sector_margin_lower']) for r in records)
    check('uniform sector inequality', lowest > 0,
          actual_lower=str(lowest), required='Re(G(z)/z)+|Im(G(z)/z)|/3 > 0 on all arcs')
    check('all Cauchy ratios below one', all(D(r['delta_over_256'][1]) < 1 for r in records),
          actual_max=str(max(D(r['delta_over_256'][1]) for r in records)), required='<1')
    # A point test also retains the diagnostic's failed stronger condition.
    witness_t = Q(1, 2)
    witness_z = curve(1, rational(witness_t))
    witness_f = backend.geval(coeff, eg, witness_z)/witness_z
    result = {
        'status': 'PASS_PENDING_INDEPENDENT_AUDIT' if not failures else 'FAIL',
        'claim': 'Re(G(z)/z)+|Im(G(z)/z)|/3 > 0 for every |z+400|=600',
        'circle': {'center': -400, 'radius': 600},
        'software': {'python': platform.python_version(),
                     'decimal': backend.decimal.__version__,
                     'libmpdec': backend.decimal.__libmpdec_version__},
        'inputs': {str(p.relative_to(ROOT)): digest(p) for p in (INPUT, BACKEND)},
        'program_sha256': digest(Path(__file__)),
        'inherited_coefficients': data['coefficients'],
        'inherited_uniform_G_error': eg.pair(),
        'polynomial_global_magnitude_upper': str(mp.hi),
        'Taylor_order': order, 'base_subdivision': base, 'maximum_refinement_depth': maxdepth,
        'checks': checks, 'failures': failures,
        'summary': {'arc_count': len(records), 'refinement_count': len(refinements),
                    'uniform_sector_margin_lower': str(lowest),
                    'required_sector_margin_lower': '>0',
                    'max_Taylor_tail_plus_G_error': str(max(D(r['Taylor_tail_plus_G_error'][1]) for r in records))},
        'stronger_real_part_test': {'quadrant': 1, 't': str(witness_t),
                                    'z_box': witness_z.pair(), 'f_box': witness_f.pair(),
                                    'negative_real_part_certified': witness_f.re.hi < 0,
                                    'not_needed_for_sector_claim': True},
        'arcs': records, 'refinements': refinements,
        'limitations': ['Inherits the audited L778 analytic polynomial and software contracts.',
                       'This script does not re-evaluate the theta coefficients.',
                       'Sector certificate alone does not prove positivity of a two-variable pullback.',
                       'Independent audit of this new application is pending.']}
    out.write_text(json.dumps(result, indent=2)+'\n')
    print(result['status'])
    print('Actual uniform sector lower:', lowest, '; required: > 0')
    print('Failures:', failures)
    print('Full certificate:', out.relative_to(ROOT))
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
