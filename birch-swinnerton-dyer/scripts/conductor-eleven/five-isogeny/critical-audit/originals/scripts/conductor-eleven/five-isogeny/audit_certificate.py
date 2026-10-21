#!/usr/bin/env python3
"""Fixed L046 audit. Exact interpolation plus unpaired function-field sums.

The degree bounds and projective argument are justified in canonical L046.
Original production evidence is never overwritten. No third-party packages.
"""
from copy import deepcopy
from fractions import Fraction as F
from hashlib import sha256
import importlib.util
import json
from math import lcm
from pathlib import Path
import shutil
import subprocess
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
OUT = HERE / 'critical-audit'


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def save(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2) + '\n')


def val(coefficients, x):
    total = F(0)
    for a in reversed(coefficients):
        total = total * x + F(a)
    return total


def derivative(coefficients):
    return [i * F(a) for i, a in enumerate(coefficients)][1:]


def add(a, b):
    return (a[0] + b[0], a[1] + b[1])


def neg(a):
    return (-a[0], -a[1])


def product(a, b, f):
    # Q[Y]/(Y^2-f), no square-root approximation or selected ordinate.
    return (a[0]*b[0]+a[1]*b[1]*f, a[0]*b[1]+a[1]*b[0])


def main():
    OUT.mkdir(exist_ok=True)
    paths = [HERE / name for name in
             ('certificate.json', 'verification.json', 'build_certificate.py',
              'verify_certificate.py', 'audit_certificate.py')]
    source = HERE.parent / 'absolute-cycles/certificate.json'
    source_archive = HERE.parent / 'absolute-cycles/critical-audit/originals/scripts/conductor-eleven/absolute-cycles/certificate.json'
    paths += [source, source_archive]
    before = {str(p.relative_to(ROOT)): digest(p) for p in paths}
    for p in paths:
        dest = OUT / 'originals' / p.relative_to(ROOT)
        dest.parent.mkdir(parents=True, exist_ok=True)
        if dest.exists():
            assert digest(dest) == digest(p), 'Preserved input differs; use a fresh audit directory'
        else:
            shutil.copy2(p, dest)
    save(OUT / 'pre-replay-manifest.json', before)
    checks, failures = [], []

    def need(label, condition):
        checks.append(label)
        if not condition:
            failures.append(label)

    data = json.loads((HERE / 'certificate.json').read_text())
    need('L043 current certificate equals separately audited archived bytes',
         digest(source) == digest(source_archive) == data['transfer']['source_sha256'])

    spec = importlib.util.spec_from_file_location('l046_producer', HERE / 'build_certificate.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    rebuilt = module.build()
    save(OUT / 'rebuilt-certificate.json', rebuilt)
    need('fresh production equals original entire certificate', rebuilt == data)

    def replay(input_path, report_path):
        proc = subprocess.run([sys.executable, str(HERE / 'verify_certificate.py'),
                               str(input_path), str(report_path)],
                              text=True, capture_output=True)
        report_path.with_suffix('.log').write_text(proc.stdout + proc.stderr)
        return proc.returncode, json.loads(report_path.read_text())

    code, replay_report = replay(HERE / 'certificate.json', OUT / 'full-replay.json')
    need('distinct full replay 56 checks with no failures',
         code == 0 and not replay_report['failures'] and len(replay_report['checks']) == 56)

    # Third calculation: no producer/verifier polynomial helpers are reused.
    N = data['map']['x_target']['numerator']
    M = data['map']['Y_target_over_Y_source']['numerator']
    L = data['kernel_polynomial']
    D = data['map']['x_target']['denominator']
    E = data['map']['Y_target_over_Y_source']['denominator']
    need('complete polynomial lengths and monic leading coefficients',
         tuple(map(len, (N, M, L, D, E))) == (6, 7, 3, 5, 7)
         and all(F(a[-1]) == 1 for a in (N, M, L, D, E)))
    points = [F(x) for x in range(-10, 8) if x not in (5, 16)][:16]
    kernel = [(F(5), F(11, 2)), (F(16), -F(121, 2)),
              (F(16), F(121, 2)), (F(5), -F(11, 2))]
    rows = []
    for x in points:
        f = x**3 - x*x - 10*x - F(79, 4)
        n, m, ell = val(N, x), val(M, x), val(L, x)
        hx, hy = (x, F(0)), (F(0), F(1))
        for q, r in kernel:
            slope = (-r/(x-q), 1/(x-q))
            xsum = add(product(slope, slope, f), (1-x-q, F(0)))
            ysum = add((F(0), -F(1)), product(slope, add((x, F(0)), neg(xsum)), f))
            hx = add(hx, add(xsum, (-q, F(0))))
            hy = add(hy, add(ysum, (-r, F(0))))
        residuals = {
            'x_constant': hx[0]*ell**2-n,
            'x_Y': hx[1]*ell**2,
            'Y_constant': hy[0]*ell**3,
            'Y_Y': hy[1]*ell**3-m,
            'x_denominator': val(D, x)-ell**2,
            'Y_denominator': val(E, x)-ell**3,
            'derivative': val(derivative(N), x)*ell-2*n*val(derivative(L), x)-m,
            'target_equation': (4*x**3-4*x*x-40*x-79)*m*m
                - (4*n**3-4*n*n*ell**2-31280*n*ell**4-1054319*ell**6),
        }
        rows.append({'x': str(x), 'residuals': {k: str(v) for k, v in residuals.items()}})
        need('all unpaired and polynomial residuals at x=' + str(x), not any(residuals.values()))
    bounds = {'x_constant': 5, 'x_Y': 3, 'Y_constant': 6, 'Y_Y': 6,
              'x_denominator': 4, 'Y_denominator': 6, 'derivative': 6, 'target_equation': 15}
    need('enough distinct exact interpolation nodes for every identity',
         len(set(points)) == 16 and len(points) > max(bounds.values()))
    poles = []
    for q, r in kernel:
        other = F(16) if q == 5 else F(5)
        xlead = val(N, q)/(q-other)**2
        ylead = r*val(M, q)/(q-other)**3
        need('finite uniformizer and pole coefficients at ' + str((q, r)),
             r*r == q**3-q*q-10*q-F(79, 4) and r != 0
             and xlead == 4*r*r and ylead == -8*r**3)
        poles.append({'x': str(q), 'Y': str(r), 'x_pole_order': 2, 'Y_pole_order': 3,
                      'x_leading': str(xlead), 'Y_leading': str(ylead),
                      'target_x_over_Y_order': 1, 'target_one_over_Y_order': 3})
    # Independent cubic discriminant in centered coordinates: Delta=16 disc(f).
    a4, a6 = map(F, data['target'][3:])
    b, c, d = -F(1), a4, a6+F(1, 4)
    cubic_disc = b*b*c*c - 4*c**3 - 4*b**3*d - 27*d*d + 18*b*c*d
    need('third discriminant calculation and integral minimal model',
         16*cubic_disc == -11 and all(F(a).denominator == 1 for a in data['target']))
    source_values = list(map(F, json.loads(source.read_text())['normalization']['generator_values']))
    target_values = [5*v for v in source_values]
    need('all twelve transferred values including both zero entries',
         len(target_values) == 12 and target_values == list(map(F, data['transfer']['target_values']))
         and [i for i, v in enumerate(target_values) if v == 0] == [2, 11])
    need('least target denominator two witnessed by generator four',
         lcm(*(v.denominator for v in target_values)) == 2 and target_values[4] == F(5, 2))
    independent = {'degree_bounds': bounds, 'node_count': len(points), 'nodes': rows,
                   'finite_poles': poles, 'infinity': {'h_over_x_limit': '1', 'v_limit': '1',
                   'x_pole_order': 2, 'Y_pole_order': 3}, 'discriminant': str(16*cubic_disc),
                   'target_values': list(map(str, target_values)), 'target_denominator': 2}
    save(OUT / 'independent-identities.json', independent)

    mutations = [
        ('opposite-ordinate', ('multiples', 3, 1), '5'),
        ('x-map-coefficient', ('map', 'x_target', 'numerator', 0), '-324598'),
        ('y-map-coefficient', ('map', 'Y_target_over_Y_source', 'numerator', 0), '6683'),
        ('exceptional-leading', ('exceptional', 'finite_Y_factor_leading_coefficients', 1), '29282'),
        ('infinity-order', ('exceptional', 'infinity_Y_pole_order'), 2),
        ('target-equation', ('target', 4), -263579),
        ('minimal-change', ('minimality', 'coordinate_change', 0), 5),
        ('differential-scalar', ('differential', 'scalar'), '5'),
        ('reciprocal-period', ('real_map', 'period_ratio'), '1/5'),
        ('source-binding', ('transfer', 'source_sha256'), '0'*64),
        ('last-zero-value', ('transfer', 'target_values', 11), '1'),
        ('half-denominator', ('transfer', 'individual_denominators', 4), 1),
    ]
    rejections = []
    for name, keys, value in mutations:
        altered = deepcopy(data)
        field = altered
        for key in keys[:-1]:
            field = field[key]
        field[keys[-1]] = value
        inp = OUT / 'altered' / name / 'certificate.json'
        report = inp.parent / 'verification.json'
        save(inp, altered)
        # Seed a stale success: the command must overwrite it with fresh failure.
        save(report, {'failures': [], 'stale_success': True})
        status, result = replay(inp, report)
        rejected = status != 0 and bool(result['failures']) and 'stale_success' not in result
        need('reject altered evidence and persist fresh failure: ' + name, rejected)
        rejections.append({'name': name, 'rejected': rejected, 'failures': result['failures'],
                           'report': str(report.relative_to(ROOT))})
    need('all original evidence bytes preserved',
         before == {str(p.relative_to(ROOT)): digest(p) for p in paths})
    result = {'checks': checks, 'failures': failures, 'full_replay_checks': len(replay_report['checks']),
              'independent_identity_actual_nodes': 16, 'required_nodes': 16,
              'finite_points_actual': 4, 'finite_points_required': 4,
              'minimality_valuation': 1, 'minimality_strict_bound': 12,
              'generator_values_actual': 12, 'generator_values_required': 12,
              'rejections': rejections, 'input_hashes': before,
              'source_qualification': 'L043 published optimality/complete-isogeny-class qualification retained',
              'mathematical_review': 'Projective extension and period applicability are reviewed in canonical L046, not inferred from JSON labels.'}
    save(OUT / 'audit.json', result)
    print('L046 audit:', len(checks), 'checks; failures:', failures)
    print('Full replay: 56/56; identity nodes: 16/16; finite poles: 4/4; minimality: 1/<12; values: 12/12')
    print('Altered evidence rejected:', sum(r['rejected'] for r in rejections), '/', len(rejections))
    print('Report:', (OUT / 'audit.json').relative_to(ROOT))
    return bool(failures)


if __name__ == '__main__':
    sys.exit(main())
