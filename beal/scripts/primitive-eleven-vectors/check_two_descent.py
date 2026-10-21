"""Finite exact arithmetic for L085; uniform coverage is proved in the lemma."""
from pathlib import Path
import json

BASE = Path(__file__).resolve().parent


def g(x):
    return x**3 - 4*x*x - 160*x - 1264


def ev(coefficients, x):
    result = 0
    for c in reversed(coefficients):
        result = result*x + c
    return result


def main():
    polynomials = json.loads((BASE.parent / 'five-isogeny-modular-norm' /
                              'norm-certificate.json').read_text())['polynomials_ascending']
    checks = []

    def check(name, actual, required):
        checks.append(dict(name=name, actual=actual, required=required,
                           passed=actual == required))

    squares = sorted({x*x % 11 for x in range(1, 11)})
    check('nonzero residue squares', squares, [1, 3, 4, 5, 9])
    alpha = 8
    lifts = []
    for n, expected in [(1, 118), (2, 844)]:
        modulus = 11**(n+1)
        candidates = [alpha + k*11**n for k in range(11)
                      if g(alpha + k*11**n) % modulus == 0]
        check(f'unique alpha lift modulo {modulus}', candidates, [expected])
        alpha = candidates[0]
        lifts.append(dict(modulus=modulus, alpha=alpha, g_value=g(alpha)))
    check('simple derivative residue', (3*alpha*alpha - 8*alpha - 160) % 11, 1)
    center = ((4-alpha)*pow(2, -1, 1331)) % 1331
    check('center modulo 1331', center, 911)
    check('center offset from 64 divided by 121', (center-64)//121, 7)
    cases = []
    for s, z, v, expected_rhs in [(4, 4, 2, 8520), (10, 5, 8, 16330)]:
        check(f's={s}: cluster residue', pow(s-1, -1, 11), z)
        smooth_x = (5-s+s*s) % 11
        smooth_units = [(4*smooth_x-8) % 11, (4*smooth_x-9) % 11]
        cluster_units = [1, (4*z-7) % 11, (4*z-7) % 11]
        check(f's={s}: smooth residues', smooth_units, [5, 4] if s == 4 else [9, 8])
        check(f's={s}: cluster residues', cluster_units, [1, 9, 9] if s == 4 else [1, 2, 2])
        check(f's={s}: square characters',
              [int(u not in squares) for u in smooth_units + cluster_units],
              [0, 0, 0, 0, 0] if s == 4 else [0, 1, 0, 1, 1])
        x = 16+121*z
        rhs = 6*z+47*z*z+121*z**3
        check(f's={s}: curve constant', rhs, expected_rhs)
        check(f's={s}: Hensel residual', (v*v+v-rhs) % 11, 0)
        check(f's={s}: Hensel derivative', (2*v+1) % 11, 5 if s == 4 else 6)
        b = ev(polynomials['b'], x)
        numerator = ev(polynomials['a'], x)+60*b
        d = ev(polynomials['d'], x)
        check(f's={s}: exact scaling remainders',
              [b % 11**20, numerator % 11**22, d % 11**22], [0, 0, 0])
        residues = [b//11**20 % 11, numerator//11**22 % 11, d//11**22 % 11]
        check(f's={s}: reconstruction residues', residues, [1, 3, 4] if s == 4 else [1, 9, 5])
        check(f's={s}: common scalar residue',
              (residues[1]+residues[0]*v)*pow(residues[2], -1, 11) % 11, s)
        cases.append(dict(s=s, z=z, smooth_x=smooth_x, smooth_units=smooth_units,
                          cluster_units=cluster_units, x=x, V_residue=v,
                          V_equation_constant=rhs, exact_b=b,
                          exact_a_plus_60b=numerator, exact_d=d))
    certificate = dict(alpha_lifts=lifts, center_mod_1331=center, cases=cases,
                       checks=checks, failures=[c['name'] for c in checks if not c['passed']],
                       bounds=dict(cluster_difference_v11=2, root_separation_v11='5/2',
                                   required_strict_inequality='2 < 5/2',
                                   restricted_size=2, unrestricted_size=16))
    path = BASE / 'two-descent-certificate.json'
    path.write_text(json.dumps(certificate, indent=2)+'\n')
    print(f"Checks: {len(checks)}; failures: {certificate['failures']}")
    print('Actual/required: cluster valuation 2 < root separation 5/2; image 2 of 16.')
    print(f'Certificate: {path.relative_to(BASE.parent.parent)}')
    if certificate['failures']:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
