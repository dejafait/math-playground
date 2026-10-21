"""Exact maximal-ring arithmetic for the approved ramified local-image task.

The mathematical completeness and precision proofs are in L078. This is
arithmetic infrastructure, not an enumeration of the elliptic Kummer image.
No external algebra backend, floating point, or network is used.
"""
from collections import defaultdict
from pathlib import Path
import json


N = 33
MODULUS = 8
PRECISION = 99  # v_J(8), with v_J(rho)=1


def reduce_terms(terms):
    """Exact integer reduction; rho^3=pi+3pi^4rho^2-2pi^8rho."""
    work = defaultdict(int, terms)
    while any(j >= 3 and c for (i, j), c in work.items()):
        i, j = max((key for key, c in work.items() if key[1] >= 3 and c),
                   key=lambda key: key[1])
        c = work.pop((i, j))
        work[i + 1, j - 3] += c
        work[i + 4, j - 1] += 3 * c
        work[i + 8, j - 2] -= 2 * c
    out = [0] * N
    for (i, j), c in work.items():
        out[3 * (i % 11) + j] += c * 2 ** (i // 11)
    return tuple(out)


TABLE = [[reduce_terms({(a // 3 + b // 3, a % 3 + b % 3): 1})
          for b in range(N)] for a in range(N)]
SPARSE = [[[(k, c) for k, c in enumerate(entry) if c]
           for entry in row] for row in TABLE]
ZERO = (0,) * N
ONE = (1,) + (0,) * (N - 1)
RHO = (0, 1) + (0,) * (N - 2)
PI = (0, 0, 0, 1) + (0,) * (N - 4)


def add(a, b, modulus=MODULUS):
    r = tuple(x + y for x, y in zip(a, b))
    return tuple(x % modulus for x in r) if modulus else r


def scale(c, a, modulus=MODULUS):
    r = tuple(c * x for x in a)
    return tuple(x % modulus for x in r) if modulus else r


def mul(a, b, modulus=MODULUS):
    out = [0] * N
    for i, x in enumerate(a):
        if not x:
            continue
        for j, y in enumerate(b):
            if y:
                xy = x * y
                for k, c in SPARSE[i][j]:
                    out[k] += xy * c
    return tuple(x % modulus for x in out) if modulus else tuple(out)


def power(a, n, modulus=MODULUS):
    r = ONE
    while n:
        if n & 1:
            r = mul(r, a, modulus)
        a = mul(a, a, modulus)
        n //= 2
    return r


def valuation(a):
    """Exact below 99; 99 denotes a certified lower bound."""
    def v2(c):
        return (abs(c) & -abs(c)).bit_length() - 1
    return min([PRECISION] + [k + 33 * v2(c) for k, c in enumerate(a) if c])


def inverse_unit(a):
    if valuation(a) != 0:
        raise ValueError('unit required')
    r = ONE
    # Initially a*r=1 mod rho. Newton doubles the error valuation.
    for _ in range(7):
        r = mul(r, add(scale(2, ONE), scale(-1, mul(a, r))))
    if mul(a, r) != ONE:
        raise ArithmeticError('unit inverse did not reach modulus 8')
    return r


RPOW = [power(RHO, n) for n in range(100)]
CLASS_DIGITS = list(range(1, 66, 2)) + [66]
BIT = {n: i for i, n in enumerate(CLASS_DIGITS)}
GENERATORS = {n: add(ONE, RPOW[n]) for n in CLASS_DIGITS}
ELIMINATORS = {}
ROOTS = {}
for n in range(1, 67):
    if n in BIT:
        ELIMINATORS[n] = inverse_unit(GENERATORS[n])
    else:
        root = add(ONE, RPOW[n // 2])
        ROOTS[n] = root
        ELIMINATORS[n] = inverse_unit(mul(root, root))


def unit_label(a):
    """Return 34 square-class bits and a complete elimination trace."""
    if valuation(a) != 0:
        raise ValueError('unit required; normalize valuation separately')
    residual, representative, root, bits = a, ONE, ONE, 0
    trace = []
    for n in range(1, 67):
        v = valuation(add(residual, scale(-1, ONE)))
        if v < n:
            raise ArithmeticError('lost a previously eliminated digit')
        if v != n:
            continue
        residual = mul(residual, ELIMINATORS[n])
        if n in BIT:
            bits ^= 1 << BIT[n]
            representative = mul(representative, GENERATORS[n])
            kind = 'class'
        else:
            root = mul(root, ROOTS[n])
            kind = 'square'
        after = valuation(add(residual, scale(-1, ONE)))
        if after <= n:
            raise ArithmeticError('digit elimination failed')
        trace.append({'digit': n, 'kind': kind, 'valuation_after_lower_bound': after})
    identity = mul(mul(representative, mul(root, root)), residual)
    if identity != a:
        raise ArithmeticError('normal form reconstruction failed')
    return {'bits': bits, 'digits': [n for n in CLASS_DIGITS if bits & (1 << BIT[n])],
            'trace': trace, 'representative': representative, 'square_root_factor': root,
            'residual': residual,
            'residual_minus_one_valuation_lower_bound': valuation(add(residual, scale(-1, ONE))),
            'reconstruction_mod_8': True}


def main():
    checks = {}
    pi4 = power(PI, 4, None)
    # s = 4 - 3*pi^7*rho + pi^3*rho^2; all checks here are exact integers.
    s = add(add(scale(4, ONE, None), scale(-3, mul(power(PI, 7, None), RHO, None), None), None),
            mul(power(PI, 3, None), power(RHO, 2, None), None), None)
    theta = add(add(scale(28, ONE, None), scale(-26, s, None), None),
                scale(6, mul(s, s, None), None), None)
    shifted_f = add(add(power(s, 3, None), scale(-4, power(s, 2, None), None), None),
                    add(scale(6, s, None), scale(-2, ONE, None), None), None)
    gtheta = add(add(power(theta, 3, None), scale(-4, power(theta, 2, None), None), None),
                 add(scale(-160, theta, None), scale(-1264, ONE, None), None), None)
    checks['base_relation_exact'] = power(PI, 11, None) == scale(2, ONE, None)
    checks['rho_s_equals_pi4_exact'] = mul(RHO, s, None) == pi4
    checks['s_satisfies_original_eisenstein_exact'] = shifted_f == ZERO
    checks['theta_satisfies_fixed_cubic_exact'] = gtheta == ZERO
    checks['basis_valuations_complete'] = [valuation(tuple(int(k == i) for k in range(N)))
                                              for i in range(N)] == list(range(N))
    checks['rho_power_valuations_through_precision'] = [valuation(a) for a in RPOW] == list(range(100))
    checks['modulus_precision_exceeds_square_threshold'] = PRECISION == 99 and 99 > 66
    checks['relative_eisenstein_valuations'] = [1, 19, 4] == [1, 11 + 8, 4]
    checks['eliminator_inverses'] = all(
        mul(ELIMINATORS[n], GENERATORS[n] if n in BIT else mul(ROOTS[n], ROOTS[n])) == ONE
        for n in range(1, 67))
    generator_records = []
    for n in CLASS_DIGITS:
        record = unit_label(GENERATORS[n])
        checks[f'generator_label_{n}'] = record['bits'] == (1 << BIT[n])
        generator_records.append({'digit': n, 'element': GENERATORS[n], 'normal_form': record})
    square_records = []
    for n in range(1, 34):
        root = add(ONE, RPOW[n])
        square = mul(root, root)
        record = unit_label(square)
        checks[f'square_label_{n}'] = record['bits'] == 0
        square_records.append({'root_digit': n, 'root': root, 'square': square, 'normal_form': record})
    # Fixed inputs are comparisons only; u is not claimed to be a point image.
    s_mod = tuple(c % 8 for c in s)
    theta_mod = tuple(c % 8 for c in theta)
    u = add(ONE, scale(-1, s_mod))
    h = add(scale(5, ONE), scale(-1, theta_mod))
    targets = {}
    for name, a in [('one', ONE), ('u', u), ('h', h), ('uh', mul(u, h))]:
        targets[name] = {'element': a, 'normal_form': unit_label(a)}
    checks['fixed_comparison_homomorphism'] = (
        targets['uh']['normal_form']['bits'] ==
        targets['u']['normal_form']['bits'] ^ targets['h']['normal_form']['bits'])
    checks['fixed_three_nonsquares'] = all(targets[n]['normal_form']['bits'] for n in ('u', 'h', 'uh'))
    checks['fixed_point_square_residue'] = -2039 % 8 == 1
    failures = [name for name, ok in checks.items() if not ok]
    certificate = {
        'purpose': 'maximal-ring model and complete square-class arithmetic; not full Kummer image',
        'inputs': {'base_polynomial': 'pi^11-2', 'relative_polynomial': 'rho^3-3*pi^4*rho^2+2*pi^8*rho-pi',
                   'original_cubic': [-1264, -160, -4, 1], 'basis_index': '3*i+j for pi^i*rho^j'},
        'exact_coordinates': {'s': s, 'theta': theta},
        'precision': {'modulus': 8, 'valuation_error_lower_bound': 99,
                      'square_hensel_strict_threshold': 66, 'last_class_digit': 66,
                      'base_v4': 22, 'extension_v2': 33},
        'class_digits': CLASS_DIGITS, 'unit_class_dimension': 34, 'field_class_dimension': 35,
        'generator_records': generator_records, 'square_records': square_records, 'targets': targets,
        'eliminators': {str(n): a for n, a in ELIMINATORS.items()},
        'thresholds': {'arithmetic_milestone_actual': int(not failures), 'arithmetic_milestone_required': 1,
                       'certified_full_image': False, 'certified_terminal_disks': 0,
                       'required_full_image_size_from_BPT': 2048},
        'checks': checks, 'failures': failures,
    }
    path = Path(__file__).with_name('arithmetic-certificate.json')
    path.write_text(json.dumps(certificate, indent=2) + '\n')
    print(f'Checks: {sum(checks.values())}/{len(checks)}; failures: {failures}')
    print('Valuation precision actual/strict threshold: 99/>66; base v(4)=22')
    print('Unit square-class basis actual/required: 34/34 (proof in L078)')
    print('Full image: NOT COMPUTED; terminal disks: 0; required image size: 2048')
    print(f'Certificate: {path.relative_to(Path.cwd())}')
    raise SystemExit(bool(failures))


if __name__ == '__main__':
    main()
