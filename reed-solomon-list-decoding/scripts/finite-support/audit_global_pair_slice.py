"""Independent full arithmetic reconstruction of the pair-slice obstruction.

No construction module is imported. This checks the finite certificate;
the PSD-kernel argument still needs its separate critical proof review.
"""
import json
from fractions import Fraction as Q
from math import factorial
from pathlib import Path

BASE = Path(__file__).parent
OUT = BASE/'global-pair-slice-audit-results.json'


def choose(n, k):
    if k < 0 or k > n:
        return 0
    product = 1
    for z in range(n-k+1, n+1):
        product *= z
    return product//factorial(k)


def dec(z):
    return Q(z['numerator'], z['denominator'])


def enc(z):
    return {'numerator': z.numerator, 'denominator': z.denominator}


def main():
    cert = json.loads((BASE/'global-pair-slice-results.json').read_text())
    ob = cert['exact_obstruction']
    failures = []
    checks = []

    def check(name, ok):
        checks.append({'name': name, 'passed': bool(ok)})
        if not ok:
            failures.append(name)

    rho = Q(2571353, choose(963, 7))
    mass = choose(1024, 68)*rho
    check('parameters', cert['parameters']['n'] == 1024
          and cert['parameters']['w'] == 68
          and dec(cert['parameters']['rho']) == rho
          and cert['parameters']['global_vertex_count'] == choose(1024, 68)
          and dec(cert['parameters']['required_constant_mass']) == mass
          and dec(cert['parameters']['ambient_threshold']) == Q(65537**28, 2**128))
    b = [dec(z) for z in ob['b_coordinates']]
    check('vector_lengths', len(b) == 69 and len(ob['distance_coordinates']) == 69
          and len(ob['spectral_sums']) == 69 and len(cert['q_matrix']) == 69
          and len(ob['core_rows']) == 61 and len(ob['core_residuals']) == 62)
    expected_fixed = [Q(1), Q(0), Q(0), Q(0), Q(0)]
    for i in range(5, 8):
        h = 7-i
        expected_fixed.append(Q([2442832,125664,2856][h],
                                choose(7,h)*choose(956,7-h)))
    val = [choose(68,i)*choose(956,i) for i in range(69)]
    a = [val[i]*b[i] for i in range(69)]
    for i in range(8):
        check(f'fixed_{i}', b[i] == expected_fixed[i]
              and dec(cert['fixed_distance_coordinates'][str(i)]) == a[i])
    for i in range(69):
        check(f'coordinate_{i}', b[i] >= 0 and a[i] == dec(ob['distance_coordinates'][i]))
    for r in range(61, -1, -1):
        t = 61-r
        coefficients = [choose(68-r, 7-l)*choose(895+r,l) for l in range(8)]
        total = sum(Q(c)*b[t+l] for l,c in enumerate(coefficients))
        check(f'core_equation_r{r}', total == 2571353
              and dec(ob['core_residuals'][t]) == 0)
        if t:
            row = ob['core_rows'][t-1]
            check(f'triangular_row_{t}', row['coefficients'] == coefficients
                  and row['pivot'] == coefficients[-1] > 0
                  and dec(row['new_b']) == b[t+7])
    spectra = []
    for j in range(69):
        # Polynomial convolution, rather than the constructor's hahn call.
        poly = [0]*69
        for r in range(69-j):
            c = choose(68-j,r)*choose(956-j,r)
            for h in range(j+1):
                if r+h <= 68:
                    poly[r+h] += c*((-1)**h)*choose(j,h)
        q = [Q(poly[i],val[i]) for i in range(69)]
        for i in range(69):
            check(f'coefficient_{j}_{i}', q[i] == dec(cert['q_matrix'][j][i]))
        eigen = sum(q[i]*a[i] for i in range(69))
        spectra.append(eigen)
        check(f'spectral_sum_{j}', eigen == dec(ob['spectral_sums'][j]))
    check('constant_zero', spectra[0] == mass and dec(ob['constant_schur_sum']) == 0)
    check('first_61_zero', all(z == 0 for z in spectra[1:62]))
    check('negative_63', spectra[63] == Q(-4972581118802,268545631575))
    check('negative_64', spectra[64] == Q(-4715156067501,3197483319953))
    check('complete_other_spectra_nonnegative', all(spectra[j] >= 0
          for j in range(69) if j not in (63,64)))
    check('zero_variance_identity', rho*choose(963,7) == 2571353
          and 1+2442832+125664+2856 == 2571353)
    result = {'checks': checks, 'checks_count': len(checks), 'failures': failures,
              'arithmetic_verified': not failures,
              'negative_spectral_sums': {str(j): enc(spectra[j]) for j in (63,64)},
              'required_spectral_lower_bound': 0,
              'constant_schur_sum': enc(spectra[0]-mass),
              'required_constant_mass': enc(mass),
              'ambient_threshold': enc(Q(65537**28,2**128))}
    OUT.write_text(json.dumps(result, indent=2)+'\n')
    print(f'Independent exact reconstruction: {len(checks)} checks; failures={failures}')
    print('Actual spectral sums j=63,64:', spectra[63], spectra[64], '; required >= 0')
    print('Constant Schur sum:', spectra[0]-mass, '; required >= 0')
    print('Slice mass / ambient threshold:', float(mass/Q(65537**28,2**128)))
    print('Full audit certificate:', OUT)


if __name__ == '__main__':
    main()
