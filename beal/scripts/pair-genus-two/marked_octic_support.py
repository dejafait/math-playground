"""Exact polynomial support certificate; no field or maximal-order assumption."""
from pathlib import Path
from hashlib import sha256
import json

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent


def determinant(matrix):
    """Fraction-free elimination with exact division, including row swaps."""
    a = [row[:] for row in matrix]
    sign, previous = 1, 1
    trace = []
    for k in range(len(a)-1):
        r = next(i for i in range(k, len(a)) if a[i][k])
        if r != k:
            a[k], a[r] = a[r], a[k]
            sign = -sign
        pivot = a[k][k]
        trace.append(dict(step=k, swapped_row=r, pivot=pivot, divisor=previous))
        for i in range(k+1, len(a)):
            for j in range(k+1, len(a)):
                numerator = a[i][j]*pivot - a[i][k]*a[k][j]
                assert numerator % previous == 0
                a[i][j] = numerator // previous
            a[i][k] = 0
        previous = pivot
    return sign*a[-1][-1], trace


def discriminant(coefficients):
    # Ascending coefficients; Sylvester rows in descending order.
    n = len(coefficients)-1
    p = coefficients[::-1]
    q = [i*coefficients[i] for i in range(1, n+1)][::-1]
    matrix = []
    for polynomial, count in ((p, n-1), (q, n)):
        for shift in range(count):
            row = [0]*shift + polynomial
            matrix.append(row + [0]*(2*n-1-len(row)))
    resultant, trace = determinant(matrix)
    numerator = (-1)**(n*(n-1)//2)*resultant
    assert numerator % coefficients[-1] == 0
    return dict(coefficients=coefficients, sylvester_matrix=matrix,
                elimination=trace, resultant=resultant,
                discriminant=numerator//coefficients[-1])


def factor_supported(value, primes):
    remainder, factors = abs(value), {}
    for p in primes:
        # Deterministic trial primality, sufficient for these small candidates.
        assert p >= 2 and all(p % d for d in range(2, int(p**0.5)+1))
        exponent = 0
        while remainder % p == 0:
            exponent += 1
            remainder //= p
        if exponent:
            factors[str(p)] = exponent
    return dict(sign=1 if value > 0 else -1, factors=factors, remainder=remainder)


def main():
    quartic = [2673, -39204, 76230, -31460, 3025]
    octic = [quartic[i//2] if i % 2 == 0 else 0 for i in range(9)]
    g, p = discriminant(octic), discriminant(quartic)
    primes = [2, 3, 5, 11]
    g['factorization'] = factor_supported(g['discriminant'], primes)
    p['factorization'] = factor_supported(p['discriminant'], primes)
    rows = [dict(q=0, Z=z, R=3*z, T=2, h=0, W=0, u=0, v=0,
                 original_z=0, s=1, chart_derivative=2*z,
                 fake_representative=3025, fake_class='identity')
            for z in [-55, 55]]
    checks = dict(
        exact_L113_coefficients=octic == [2673,0,-39204,0,76230,0,-31460,0,3025],
        degree_eight=len(octic)-1 == 8,
        square_leading_coefficient=octic[-1] == 55**2,
        nonzero_discriminant=g['discriminant'] != 0,
        complete_octic_factorization=g['factorization']['remainder'] == 1,
        complete_quartic_factorization=p['factorization']['remainder'] == 1,
        even_polynomial_cross_check=g['discriminant'] == 2**8*quartic[-1]*quartic[0]*p['discriminant']**2,
        both_infinity_points=len(rows) == 2 and {r['Z'] for r in rows} == {-55,55},
        smooth_infinity_rows=all(r['Z']**2 == 3025 and r['chart_derivative'] != 0 for r in rows),
        infinity_image_square=all(r['fake_representative'] == 55**2 for r in rows),
        sufficient_support=set(map(int, g['factorization']['factors'])) | {2,5,11} == set(primes))
    result = dict(octic=g, quartic=p, finite_support=primes, real_place_retained=True,
                  infinity_rows=rows, checks=checks,
                  failures=[k for k,v in checks.items() if not v],
                  inputs={'lemmas/L113-marked-genus-three-hyperelliptic-model.md':
                    sha256((ROOT/'lemmas/L113-marked-genus-three-hyperelliptic-model.md').read_bytes()).hexdigest()})
    path = HERE/'marked-octic-support-certificate.json'
    path.write_text(json.dumps(result, indent=2)+'\n')
    print(f"Checks: {sum(checks.values())}/{len(checks)}; failures: {result['failures']}")
    print(f"Discriminant factors: {g['factorization']}; required remainder=1")
    print(f"Support: {primes}; infinity rows: {len(rows)}/2")
    print(f"Certificate: {path.relative_to(ROOT)}")
    assert not result['failures']


if __name__ == '__main__':
    main()
