#!/usr/bin/env python3
"""Fixed B inverse, exact identity and rational Taylor-Rouche disks.

Complex floating arithmetic seeds disks only; every decisive inequality
uses Fraction endpoints from the unchanged C029n input certificate.
"""
from fractions import Fraction as F
from math import comb, factorial, cos, sin, pi
from pathlib import Path
import hashlib
import json

import tilted_bezoutian_n6_2014 as alg

base = alg.base
ROOT = Path(__file__).parent
OUT = ROOT / 'shift-inverse-halfplane-2034.json'
PINNED = {
    'tilted-boundary-metric-2010.json': '361e31b72ad348b17f6c2ac785c20f5ab73e27796025bd724af208543e0feaf7',
    'tilted_boundary_metric_2010.py': '21cc4fb70b084fde19c62d74a7edb04a2bcdb38fe1a376ea5e7de6d3edbb58fc',
    'tilted_bezoutian_n6_2014.py': 'af87c4ec40ea6a93ddb0d9fe3915dd6c2fa403d4729e48639c1b94247ac42709',
}


def cmul(a, b):
    return a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0]


def upper(iv):
    return max(abs(iv[0]), abs(iv[1]))


def lower(iv):
    return min(abs(iv[0]), abs(iv[1])) if iv[0]*iv[1] > 0 else F(0)


def seeds(coeff):
    """Durand-Kerner iterations are untrusted contour proposals only."""
    a = [float((v[0]+v[1])/2) for v in coeff]
    a = [v/a[-1] for v in a]
    n = len(a)-1
    radius = 1+max(abs(v) for v in a[:-1])
    z = [radius*complex(cos(2*pi*(j+.17)/n), sin(2*pi*(j+.17)/n)) for j in range(n)]
    for iteration in range(2000):
        new = []
        moves = []
        for j, v in enumerate(z):
            value = complex(a[-1])
            for c in reversed(a[:-1]):
                value = value*v+c
            den = complex(1)
            for k, w in enumerate(z):
                if k != j:
                    den *= v-w
            delta = value/den
            new.append(v-delta)
            moves.append(abs(delta))
        z = new
        if max(moves) < 1e-12:
            break
    return sorted(z, key=lambda v: (v.real, v.imag)), iteration+1


def main():
    checks = {}
    cert = {'status': 'STARTED', 'checks': checks,
            'target': 'B h=full U_6; count h zeros in Im(t)<-2 with multiplicity',
            'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'method': 'Exact polynomial identity; six rational Taylor-Rouche disks',
            'failed_seed_dependency': 'mpmath unavailable; no install attempted; native complex seeds only'}

    def check(name, ok):
        checks[name] = bool(ok)

    def save(status):
        cert['status'] = status
        cert['failures'] = [k for k, v in checks.items() if not v]
        OUT.write_text(json.dumps(cert, indent=2)+'\n')

    def guard(status):
        if not all(checks.values()):
            save(status)
            print('Result:', status, '; failures:', cert['failures'])
            print('Certificate:', OUT.relative_to(ROOT.parent.parent))
            raise SystemExit(1)

    cert['input_sha256'] = {name: hashlib.sha256((ROOT/name).read_bytes()).hexdigest() for name in PINNED}
    for name in PINNED:
        check('pinned_'+name, cert['input_sha256'][name] == PINNED[name])
    guard('INPUT_CHANGED')
    src = json.loads((ROOT/'tilted-boundary-metric-2010.json').read_text())
    piv = tuple(F(src['pi_interval'][k]) for k in ('lower', 'upper'))
    siv = tuple(F(src['sqrt2_interval'][k]) for k in ('lower', 'upper'))
    cert['pi_interval'], cert['sqrt2_interval'] = src['pi_interval'], src['sqrt2_interval']
    check('unchanged_widths', piv[1]-piv[0] == siv[1]-siv[0] == F(1, 10**60))
    check('sqrt2_endpoint_squares', 0 < siv[0]**2 < 2 < siv[1]**2)
    a = list(map(alg.decode, src['a_over_S_polynomials']))
    p = [[F(1)]]
    for k in range(6):
        row = [F(0)]+p[k]
        if k:
            for j, v in enumerate(p[k-1]):
                row[j] -= F(2*k+1, 2)*v
        p.append([v/F(k+1) for v in row])
    check('basis_degrees_leads', all(p[k][-1] == F(1, factorial(k)) and len(p[k]) == k+1 for k in range(7)))
    b = [alg.add(*(alg.scale(a[k], p[k][j]) for k in range(j, 7))) for j in range(7)]
    eigen = [F(4*k+3, 2) for k in range(7)]
    # Direct expansion of the fixed +/-2i operator, not a fitted matrix.
    matrix = [[F(0) for k in range(7)] for j in range(7)]
    for k in range(7):
        for l in range(k+1):
            if l % 2 == 0:
                matrix[k-l][k] += F(3, 2)*comb(k, l)*2**l*(-1)**(l//2)
            else:
                matrix[k-l+1][k] += comb(k, l)*2**l*(-1)**((l-1)//2)
    check('triangular_diagonal', all(matrix[j][k] == 0 for j in range(7) for k in range(j))
          and [matrix[k][k] for k in range(7)] == eigen)
    check('all_denominators_positive', all(v > 0 for v in eigen))
    for k in range(7):
        check('source_eigenidentity_'+str(k), all(
            sum((matrix[j][l]*p[k][l] for l in range(k+1)), F(0))
            == (eigen[k]*p[k][j] if j <= k else 0) for j in range(7)))
    c = [alg.add(*(alg.scale(a[k], p[k][j]/eigen[k]) for k in range(j, 7))) for j in range(7)]
    # Independently solve the triangular monomial system and compare.
    solved = [[] for _ in range(7)]
    for j in range(6, -1, -1):
        solved[j] = alg.scale(alg.add(b[j], *(alg.scale(solved[k], -matrix[j][k])
                               for k in range(j+1, 7))), 1/matrix[j][j])
    check('independent_triangular_inverse', solved == c)
    residual = [alg.add(*(alg.scale(c[k], matrix[j][k]) for k in range(7)), alg.scale(b[j], -1))
                for j in range(7)]
    check('all_seven_identity_coefficients', all(not v for v in residual))
    biv = [base.peval(v, piv, siv) for v in b]
    civ = [base.peval(v, piv, siv) for v in c]
    check('degree_U_and_h_six', biv[-1][1] < 0 and civ[-1][1] < 0)
    cert.update({'basis': [list(map(str, v)) for v in p], 'eigenvalues': list(map(str, eigen)),
                 'operator_matrix': [list(map(str, v)) for v in matrix],
                 'U_coefficients': list(map(alg.encode, b)), 'h_coefficients': list(map(alg.encode, c)),
                 'identity_residual': list(map(alg.encode, residual)),
                 'U_intervals': list(map(base.interval_json, biv)),
                 'h_intervals': list(map(base.interval_json, civ)),
                 'h_outer_12': [base.interval_json(base.outward_grid(v, 12)) for v in civ]})
    save('IDENTITY_READY')
    guard('IDENTITY_FAILED')
    approx, iterations = seeds(civ)
    cert['untrusted_seed_iterations'] = iterations
    cert['untrusted_seeds'] = [[v.real, v.imag] for v in approx]
    radius = F(1, 100000)
    grid = 10**8
    centers = [(F(round(v.real*grid), grid), F(round(v.imag*grid), grid)) for v in approx]
    disks = []
    for i, z in enumerate(centers):
        powers = [(F(1), F(0))]
        for k in range(6):
            powers.append(cmul(powers[-1], z))
        taylor = []
        for j in range(7):
            real, imag = (F(0), F(0)), (F(0), F(0))
            for k in range(j, 7):
                real = base.iadd(real, base.iscale(civ[k], comb(k, j)*powers[k-j][0]))
                imag = base.iadd(imag, base.iscale(civ[k], comb(k, j)*powers[k-j][1]))
            taylor.append((real, imag))
        # max(component lower bounds) <= modulus <= sum(component upper bounds).
        linear_lower = max(lower(taylor[1][0]), lower(taylor[1][1]))*radius
        remainder_upper = sum((upper(re)+upper(im))*radius**j
                              for j, (re, im) in enumerate(taylor) if j != 1)
        gap = linear_lower-remainder_upper
        below = z[1]+radius < -2
        above = z[1]-radius > -2
        disk = {'center': list(map(str, z)), 'radius': str(radius),
                'taylor': [{'real': base.interval_json(re), 'imag': base.interval_json(im)} for re, im in taylor],
                'linear_lower': str(linear_lower), 'remainder_upper': str(remainder_upper),
                'strict_gap': str(gap),
                'gap_outer_12': base.interval_json(base.outward_grid((gap, gap), 12)),
                'linear_lower_outer_12': base.interval_json(base.outward_grid((linear_lower, linear_lower), 12)),
                'remainder_upper_outer_12': base.interval_json(base.outward_grid((remainder_upper, remainder_upper), 12)),
                'below_line': below, 'above_line': above, 'multiplicity_count': 1 if gap > 0 else None}
        disk['linear_modulus_lower_outer_12'] = str(base.outward_grid(
            (linear_lower/radius, linear_lower/radius), 12)[0])
        disk['taylor_modulus_upper_outer_12'] = [str(base.outward_grid(
            (upper(re)+upper(im), upper(re)+upper(im)), 12)[1]) for re, im in taylor]
        # These compact rationals independently suffice for every Rouche test.
        compact_left = F(disk['linear_modulus_lower_outer_12'])*radius
        compact_right = sum(F(v)*radius**j for j, v in
                            enumerate(disk['taylor_modulus_upper_outer_12']) if j != 1)
        disk['compact_left'] = str(compact_left)
        disk['compact_right'] = str(compact_right)
        disks.append(disk)
        check('strict_rouche_'+str(i), gap > 0)
        check('compact_rouche_'+str(i), compact_left > compact_right)
        check('line_separated_'+str(i), below or above)
    separations = []
    for i in range(6):
        for j in range(i):
            distance_sq = sum((centers[i][k]-centers[j][k])**2 for k in (0, 1))
            separations.append({'i': i, 'j': j, 'distance_squared': str(distance_sq),
                                'required_strict_lower': str(4*radius**2)})
            check('disjoint_'+str(i)+'_'+str(j), distance_sq > 4*radius**2)
    cert['disks'], cert['separations'] = disks, separations
    cert['rouche_table'] = [{k: d[k] for k in ('center', 'radius',
        'linear_modulus_lower_outer_12', 'taylor_modulus_upper_outer_12',
        'compact_left', 'compact_right', 'below_line', 'above_line', 'multiplicity_count')}
        for d in disks]
    check('degree_coverage', len(disks) == 6 and sum(d['multiplicity_count'] or 0 for d in disks) == 6)
    save('CONTOURS_READY')
    guard('CONTOURS_INCONCLUSIVE')
    count = sum(d['multiplicity_count'] for d in disks if d['below_line'])
    cert['halfplane_count'], cert['required_maximum'] = count, 1
    cert['prefactor_zero'] = {'real': '0', 'imag': '3/2', 'lower_halfplane_count': 0}
    cert['real_part_identity'] = '2 Re[(3/4+it/2)h(t-2i)]=U_6(t) on the real axis'
    cert['result'] = 'PASS' if count <= 1 else 'FINITE_BASELINE_REJECTED'
    save('CERTIFIED')
    print('Result:', cert['result'], '; actual lower-halfplane count:', count, '; required <=', 1)
    print('Exact full identity verified; actual degrees U_6=h=6; six disjoint one-root disks.')
    for i, d in enumerate(disks):
        print('Disk', i, ': center', d['center'], '; r=', d['radius'],
              '; gap>=', d['gap_outer_12']['lower'], '; below line:', d['below_line'])
    print('Checks:', len(checks), '; failures:', cert['failures'])
    print('Certificate:', OUT.relative_to(ROOT.parent.parent))


if __name__ == '__main__':
    main()
