#!/usr/bin/env python3
"""Exact first variations of four simple boundary roots; no branch solve.

Uses only C031c's first tangent and the unchanged fixed1307 boxes.
Rational arithmetic throughout; decimal displays are non-proof summaries.
"""
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import importlib.util
import json

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
OUT = HERE / 'boundary-variation-certificate-1320.json'
ENGINE = HERE / 'quadratic-defect-1314.py'
spec = importlib.util.spec_from_file_location('polynomial1320', ENGINE)
old = importlib.util.module_from_spec(spec)
spec.loader.exec_module(old)
P = old.P


def cmul(x, y):
    return (x[0]*y[0]-x[1]*y[1], x[0]*y[1]+x[1]*y[0])


def cpow(x, n):
    y = (Q(1), Q(0))
    for _ in range(n):
        y = cmul(x, y)
    return y


def cdiv(x, y):
    norm = y[0]**2+y[1]**2
    assert norm > 0
    p = cmul(x, (y[0], -y[1]))
    return (p[0]/norm, p[1]/norm)


def add(x, y):
    return (x[0]+y[0], x[1]+y[1])


def neg(x):
    return (-x[0], -x[1])


def scale(x, n):
    return (n*x[0], n*x[1])


def interval_mul(x, y):
    vals = [a*b for a in x for b in y]
    return min(vals), max(vals)


def interval_add(x, y):
    return x[0]+y[0], x[1]+y[1]


def interval_scale(x, n):
    return interval_mul(x, (Q(n), Q(n)))


def enc_interval(x):
    return {'lower': str(x[0]), 'upper': str(x[1])}


def main():
    source = HERE / 'quadratic-tangent-certificate-1316.json'
    branch = HERE / 'divided-residual-certificate-1318.json'
    full = HERE / 'quadratic-defect-certificate-1314.json'
    saved = json.loads(source.read_text())
    saved_branch = json.loads(branch.read_text())
    saved_full = json.loads(full.read_text())
    xs = [old.var(j) for j in range(len(old.NAMES))]
    A, B, C, D, E = xs[5:10]
    W, denom = 160000*C-A, 2*C**2
    nums = [-A*C**2, -400*B*C**2, -W*C**2,
            400*B*C**2-400*W*D*C, 160000*C**3-W**2*E]
    checks = {
        'tangent_numerators_match_1316': all(
            n.record() == row for n, row in zip(nums, saved['tangent']['witness']['tangent_numerators'])),
        'tangent_numerators_match_1318': all(
            n.record() == row for n, row in zip(nums, saved_branch['base']['a_numerators'])),
    }
    rows = {}
    expected_vectors = {'pole_i': [-1, 0, 1, 0, -1],
                        'pole_minus_i': [-1, 0, 1, 0, -1],
                        'critical_plus1': [-1, -2, -3, -4, -5],
                        'critical_minus1': [-1, 2, -3, 4, -5]}
    # Expected radial formulas multiplied by the positive 2*C^2.
    common = -4*A*C**2-2*W*C**2+5*W**2*E
    asym = -800*B*C**2+1600*W*D*C
    expected_numerators = {'pole_i': W**2*E-2*W*C**2,
                           'pole_minus_i': W**2*E-2*W*C**2,
                           'critical_plus1': common+asym,
                           'critical_minus1': common-asym}
    roots = [('pole_i', (Q(0), Q(1)), 1),
             ('pole_minus_i', (Q(0), Q(-1)), 1),
             ('critical_plus1', (Q(1), Q(0)), -1),
             ('critical_minus1', (Q(-1), Q(0)), -1)]
    for name, z, sign in roots:
        z2 = cpow(z, 2)
        base = add((Q(1), Q(0)), scale(z2, sign))
        dz = scale(z, 2*sign)
        jac = [[dz[0], -dz[1]], [dz[1], dz[0]]]
        det = jac[0][0]*jac[1][1]-jac[0][1]*jac[1][0]
        # P_tau=sum a_j*z^(j+1); N_tau=-sum j*a_j*z^(j+1).
        dt = [scale(cpow(z, j+1), 1 if sign == 1 else -j) for j in range(1, 6)]
        velocity = [cdiv(neg(x), dz) for x in dt]
        radial = [2*cmul((z[0], -z[1]), x)[0] for x in velocity]
        num = sum((r*a for r, a in zip(radial, nums)), P())
        residual = num-expected_numerators[name]
        pbase = add((Q(1), Q(0)), z2)
        checks[name+'_simple_base_root'] = base == (0, 0) and det == 4
        checks[name+'_radial_vector'] = radial == expected_vectors[name]
        checks[name+'_implicit_velocity_residual'] = all(
            add(cmul(dz, vel), rhs) == (0, 0) for vel, rhs in zip(velocity, dt))
        checks[name+'_reduced_radial_formula'] = not residual.t
        checks[name+'_noncancellation_base'] = (z != (0, 0) if sign == 1 else pbase == (2, 0))
        rows[name] = {
            'base_root_re_im': list(map(str, z)),
            'root_equation_base_value_re_im': list(map(str, base)),
            'root_equation_z_derivative_re_im': list(map(str, dz)),
            'real_dependent_Jacobian': [[str(x) for x in row] for row in jac],
            'Jacobian_determinant': str(det),
            'tau_derivative_a_coefficients_re_im': [list(map(str, x)) for x in dt],
            'root_velocity_a_coefficients_re_im': [list(map(str, x)) for x in velocity],
            'squared_modulus_derivative_a_coefficients': list(map(str, radial)),
            'radial_common_denominator': denom.record(),
            'radial_numerator': num.record(), 'reduction_residual': residual.record(),
            'denominator_base_value_re_im': list(map(str, pbase)),
            'numerator_base_value_re_im': list(map(str, z)),
        }
    boxes = {k: tuple(map(Q, pair)) for k, pair in saved['bounds']['input_boxes'].items()}
    checks['fixed_boxes_match_1314'] = all(
        pair == (Q(saved_full['necessary_test']['outer_boxes'][k]['lower']),
                 Q(saved_full['necessary_test']['outer_boxes'][k]['upper'])) for k, pair in boxes.items())
    checks['all_boxes_positive'] = all(0 < lo <= hi for lo, hi in boxes.values())
    aa, bb, cc, dd, ee = [boxes[str(j)] for j in range(2, 7)]
    vv = (160000-aa[1]/cc[0], 160000-aa[0]/cc[1])
    checks['v0_positive'] = 103935 < vv[0] <= vv[1] < 103936
    vc, v2e = interval_mul(vv, cc), interval_mul(interval_mul(vv, vv), ee)
    pole = interval_add(interval_scale(vc, -1), interval_scale(v2e, Q(1, 2)))
    base_radial = interval_add(interval_add(interval_scale(aa, -2), interval_scale(vc, -1)),
                               interval_scale(v2e, Q(5, 2)))
    odd = interval_add(interval_scale(bb, -400), interval_scale(interval_mul(vv, dd), 800))
    critical_plus = interval_add(base_radial, odd)
    critical_minus = interval_add(base_radial, interval_scale(odd, -1))
    ranges = {'pole_i': pole, 'pole_minus_i': pole,
              'critical_plus1': critical_plus, 'critical_minus1': critical_minus}
    simple_bounds = {'pole_i': (Q('0.000016'), Q('0.000018')),
                     'pole_minus_i': (Q('0.000016'), Q('0.000018')),
                     'critical_plus1': (Q('0.00049'), Q('0.00051')),
                     'critical_minus1': (Q('0.00007'), Q('0.00009'))}
    for name, r in ranges.items():
        lo, hi = simple_bounds[name]
        checks[name+'_strict_outward_bound'] = 0 < lo < r[0] <= r[1] < hi
        rows[name]['exact_radial_interval'] = enc_interval(r)
        rows[name]['strict_simple_enclosure'] = enc_interval((lo, hi))
    failures = [key for key, value in checks.items() if not value]
    cert = {
        'status': 'passed' if not failures else 'failed', 'checks': checks, 'failures': failures,
        'scope': 'u=400, C031c first tangent only, four simple base boundary roots; no global sufficiency',
        'input_hashes': {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
                         for p in (ENGINE, source, branch, full, Path(__file__))},
        'base_denominator': '1+z^2', 'base_derivative_numerator': '1-z^2',
        'quotient_derivative_identity': "f'=(P-zP')/P^2; N=1-sum(j*b_j*z^(j+1))",
        'input_boxes': {k: enc_interval(v) for k, v in boxes.items()},
        'v0_interval': enc_interval(vv),
        'radial_interval_components': {'vC': enc_interval(vc), 'v_squared_E': enc_interval(v2e),
                                       'critical_common': enc_interval(base_radial),
                                       'critical_odd': enc_interval(odd)},
        'roots': rows, 'inward_threshold': 'strictly less than 0',
        'conclusion': 'No inward first variation: all four derivatives strictly positive. Whole-disk univalence undecided.',
        'inherited_contracts': 'fixed1307 actual inclusion and L019,L021,L025,L027,L036,L037,L917; Decimal qualifications retained',
    }
    OUT.write_text(json.dumps(cert, indent=2)+'\n')
    print(f"{cert['status']}: {len(checks)} checks; failures={failures}; {OUT.relative_to(ROOT)}")
    for name, r in ranges.items():
        lo, hi = simple_bounds[name]
        print(f'{name}: exact interval inside ({lo},{hi}); required inward threshold <0; failed to certify inward motion')
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
