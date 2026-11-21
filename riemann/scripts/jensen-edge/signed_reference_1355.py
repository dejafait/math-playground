"""Exact rational enclosures for the three C019f Airy reference values.

No floating-point value is used in any assertion. See C019f for the
Gamma-integral, Airy-series and finite-tail justifications.
"""
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import json

SCALE = 10**60


def outward(lo, hi):
    assert lo <= hi
    return (F((lo * SCALE).__floor__(), SCALE),
            F((hi * SCALE).__ceil__(), SCALE))


def point(x):
    return (F(x), F(x))


def add(a, b):
    return outward(a[0] + b[0], a[1] + b[1])


def neg(a):
    return (-a[1], -a[0])


def mul(a, b):
    v = [x * y for x in a for y in b]
    return outward(min(v), max(v))


def div(a, b):
    assert b[0] * b[1] > 0
    return mul(a, outward(1 / b[1], 1 / b[0]))


def pack(a):
    return [str(a[0]), str(a[1])]


def cube_root(n):
    lo, hi = 0, 2 * SCALE
    target = n * SCALE**3
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if mid**3 <= target:
            lo = mid
        else:
            hi = mid
    assert lo**3 <= target <= hi**3
    return (F(lo, SCALE), F(hi, SCALE))


def atan_reciprocal(q):
    n = 100
    s = sum((F((-1)**k, (2*k+1) * q**(2*k+1))
             for k in range(n+1)), F(0))
    e = F(1, (2*n+3) * q**(2*n+3))
    return outward(s-e, s+e)


def gamma_third(m):
    # Gamma((m+1)/3) = 3 int_0^infinity u^m exp(-u^3) du.
    n = 320
    s = sum((F(3 * (-1)**k * 4**(3*k+m+1),
               factorial(k) * (3*k+m+1)) for k in range(n+1)), F(0))
    err = F(3 * 4**(3*(n+1)+m+1),
            factorial(n+1) * (3*(n+1)+m+1))
    tail = F(1, 2**64)
    interval = outward(s-err, s+err+tail)
    assert interval[0] > 0
    return interval, {"m": m, "N": n, "cutoff_u": 4,
                      "integrated_sum": str(s),
                      "integrated_taylor_error": str(err),
                      "positive_tail_upper": str(tail),
                      "enclosure": pack(interval)}


def airy_basis(z, residue):
    # DLMF9.4.1: the two entire series with degrees 3k and 3k+1.
    n = 100
    z3 = mul(mul(z, z), z)
    term = point(1) if residue == 0 else z
    total = term
    terms = [pack(term)]
    bound = F(11**residue)
    for k in range(n):
        den = (3*k+residue+3) * (3*k+residue+2)
        term = div(mul(term, z3), point(den))
        total = add(total, term)
        terms.append(pack(term))
        bound *= F(11**3, den)
    rho = F(11**3, (3*n+residue+3) * (3*n+residue+2))
    assert 0 < rho < 1
    first_omitted = bound * rho
    remainder = first_omitted / (1-rho)
    result = add(total, (-remainder, remainder))
    return result, {"residue": residue, "last_k": n,
                    "term_enclosures": terms, "partial_sum": pack(total),
                    "absolute_argument_bound": 11,
                    "first_omitted_upper": str(first_omitted),
                    "tail_ratio_upper": str(rho),
                    "tail_upper": str(remainder), "enclosure": pack(result)}


def main():
    pi = add(mul(point(16), atan_reciprocal(5)),
             neg(mul(point(4), atan_reciprocal(239))))
    c3, c4 = cube_root(3), cube_root(4)
    g1, g1cert = gamma_third(0)
    g2, g2cert = gamma_third(1)
    ai0 = div(point(1), mul(mul(c3, c3), g2))
    aip0 = neg(div(point(1), mul(c3, g1)))
    beta = div(mul(point(16), c4), mul(pi, pi))
    values = {}
    for x in (1, 2, 4):
        z = neg(mul(beta, point(x)))
        assert -11 < z[0] <= z[1] < 0
        s0, cert0 = airy_basis(z, 0)
        s1, cert1 = airy_basis(z, 1)
        ai = add(mul(ai0, s0), mul(aip0, s1))
        ref = mul(c4, ai)
        # A separate coarser rational enclosure for inspection and proof text.
        coarse = (F((ref[0]*1000).__floor__(), 1000),
                  F((ref[1]*1000).__ceil__(), 1000))
        values[str(x)] = {"argument": pack(z), "basis0": cert0,
                          "basis1": cert1, "Ai": pack(ai),
                          "reference": pack(ref), "coarse": pack(coarse)}
    checks = {
        "F1_negative": F(values['1']['reference'][1]) < 0,
        "F2_positive": F(values['2']['reference'][0]) > 0,
        "F4_negative": F(values['4']['reference'][1]) < 0,
        "all_reference_widths_below_1e-6": all(
            F(v['reference'][1])-F(v['reference'][0]) < F(1, 10**6)
            for v in values.values()),
        "gamma_taylor_errors_below_1e-60": all(
            F(v['integrated_taylor_error']) < F(1, 10**60)
            for v in (g1cert, g2cert)),
        "airy_series_tails_below_1e-60": all(
            F(v[b]['tail_upper']) < F(1, 10**60)
            for v in values.values() for b in ('basis0', 'basis1')),
    }
    summary = {"coarse_reference_enclosures": {
        x: v['coarse'] for x, v in values.items()},
        "reference_width_upper_bounds": {
            x: str(F(((F(v['reference'][1])-F(v['reference'][0]))
                       * 10**12).__ceil__(), 10**12))
            for x, v in values.items()},
        "required_reference_width_upper_bound": "1/1000000",
        "checks": checks,
        "opposite_endpoint_signs_required": True,
        "opposite_endpoint_signs_obtained": False,
        "failures": ["The target's opposite endpoint signs fail: F(1)<0 and F(4)<0."],
        "arithmetic": "Python integers/Fraction, outward grid 10^-60; no floating assertions"}
    certificate = {"summary": summary, "constants": {
        "pi": pack(pi), "cube_root_3": pack(c3), "cube_root_4": pack(c4),
        "gamma_1_3": g1cert, "gamma_2_3": g2cert,
        "Ai_0": pack(ai0), "Ai_prime_0": pack(aip0), "beta": pack(beta)},
        "values": values}
    path = Path(__file__).with_name('signed-reference-1355.json')
    path.write_text(json.dumps(certificate, indent=2) + '\n')
    print(json.dumps(summary, indent=2))
    print('Full exact certificate:', path.relative_to(Path.cwd()))
    assert all(checks.values()), 'Required enclosure verification failed; inspect certificate.'


if __name__ == '__main__':
    main()
