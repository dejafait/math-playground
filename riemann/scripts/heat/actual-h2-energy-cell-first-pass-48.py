#!/usr/bin/env python3
"""One fixed full-theta energy-cell attempt; no adaptive refinement.

Exact polynomial algebra uses Python integers. Certificates are written
beside this script. The cell enclosure stage is specified below before
its single invocation; an algebra-only invocation is not a mass test.
"""
import argparse
from decimal import Decimal
from fractions import Fraction
from functools import reduce
import importlib.util
import json
from math import factorial
from pathlib import Path
import sys

sys.set_int_max_str_digits(0)
DEGREE = 256
PRECISION = 200
COEFF_DEN = 10**120
THETA_TERMS = 8
MACHIN_TERMS = 128
COSINE_TERMS = 128
BASE = Path(__file__).parent

ZERO = (0,) * 6


def add(*ps):
    out = {}
    for p in ps:
        for k, v in p.items():
            out[k] = out.get(k, 0) + v
    return {k: v for k, v in out.items() if v}


def scale(p, c):
    return {k: c * v for k, v in p.items() if c * v}


def mul(p, q):
    out = {}
    for a, x in p.items():
        for b, y in q.items():
            k = tuple(i + j for i, j in zip(a, b))
            out[k] = out.get(k, 0) + x * y
    return {k: v for k, v in out.items() if v}


def algebra():
    e = [{ZERO: 1}]
    for j in range(6):
        k = list(ZERO)
        k[j] = 1
        e.append({tuple(k): 1})
    q = [scale(p, (-1) ** j) for j, p in enumerate(e)]
    s = [{}]
    for n in range(1, 7):
        s.append(add(scale(q[n], -n),
                     *(scale(mul(s[k], q[n-k]), -1)
                       for k in range(1, n))))
    # A*C*E - A*D^2 - B^2*E + 2*B*C*D - C^3.
    a, b, c, d, ee = s[2:7]
    p = add(mul(mul(a, c), ee), scale(mul(a, mul(d, d)), -1),
            scale(mul(mul(b, b), ee), -1),
            scale(mul(mul(b, c), d), 2), scale(mul(mul(c, c), c), -1))
    # Independent finite-log extraction in the polynomial ring.
    h = [{}] + q[1:]
    power = [{ZERO: 1}] + [{} for _ in range(6)]
    log = [{} for _ in range(7)]
    for r in range(1, 7):
        power = [add(*(mul(power[j], h[n-j]) for j in range(n+1)))
                 for n in range(7)]
        log = [add(log[n], scale(power[n], Fraction((-1)**(r+1), r)))
               for n in range(7)]
    residuals = [add(s[n], scale(log[n], n)) for n in range(1, 7)]
    assert all(not r for r in residuals)
    assert all(sum((i+1)*a for i, a in enumerate(k)) == 12 for k in p)
    assert all(sum(k) <= 12 for k in p)
    terms = []
    gaussian = Fraction(0)
    for k, v in sorted(p.items()):
        exponents = [12 - sum(k), *k]
        terms.append({"coefficient": v, "exponents_A0_to_A6": exponents})
        # Constant K gives A_k = K sqrt(pi)/(2*4^k*k!) t^(-k-1/2).
        gaussian += Fraction(v, 4**12) / reduce(
            lambda x, z: x*z,
            (factorial(j)**exponents[j] for j in range(7)), 1)
    assert gaussian == 0
    return {
        "variables": "A_k=M_(2k)/(2k)!, k=0,...,6; P=M_0^12 det H2",
        "terms": terms,
        "term_count": len(terms),
        "weighted_degree": 12,
        "ordinary_degree_after_homogenization": 12,
        "maximum_degree_before_homogenization": max(map(sum, p)),
        "finite_log_residuals": [{} for _ in residuals],
        "constant_kernel_leading_coefficient": str(gaussian),
    }


def load_intervals():
    spec = importlib.util.spec_from_file_location(
        'h2_energy_interval_primitives', BASE.parent / 'hankel/certify_hankel.py')
    lib = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(lib)
    for context in (lib.DOWN, lib.UP, lib.NEAR):
        context.prec = PRECISION
        context.clear_flags()
    return lib


def approx_kernel(lib):
    I = lib.I
    a = lib.arctan_bounds(5, MACHIN_TERMS)
    b = lib.arctan_bounds(239, MACHIN_TERMS)
    pl, ph = 16*a[0]-4*b[1], 16*a[1]-4*b[0]
    pi = I(I.rational(pl).lo, I.rational(ph).hi)
    assert 3 < pi.lo <= pi.hi < 4
    # For 0<=u<=3, every omitted positive summand is bounded;
    # e^3>20 gives a purely rational full-tail upper bound.
    tail = Fraction(256 * 9**4 * 10**6, 20**81)
    cosine_error = Fraction(4**(2*COSINE_TERMS+2), factorial(2*COSINE_TERMS+2))

    def cosine(t):
        assert 0 <= t.lo <= t.hi <= 4
        tt = t*t
        out = I.rational(Fraction((-1)**COSINE_TERMS, factorial(2*COSINE_TERMS)))
        for r in range(COSINE_TERMS-1, -1, -1):
            out = out*tt + I.rational(Fraction((-1)**r, factorial(2*r)))
        er = I.rational(cosine_error)
        return out + I(-er.hi, er.hi)

    def sqrt_interval(x):
        assert x.lo > 0
        lo = lib.NEAR.next_minus(lib.NEAR.sqrt(x.lo))
        hi = lib.NEAR.next_plus(lib.NEAR.sqrt(x.hi))
        # Exact rational checks remove any reliance on a sqrt rounding claim.
        assert 0 <= Fraction(lo)**2 <= Fraction(x.lo)
        assert Fraction(hi)**2 >= Fraction(x.hi)
        return I(lo, hi)

    n = DEGREE+1
    sums = [I(0) for _ in range(n)]
    nodes = []
    for j in range(n):
        theta = pi*I.rational(Fraction(2*j+1, 2*n))
        y = cosine(theta)
        x = 4+4*y
        u = sqrt_interval(x)
        assert 0 < u.lo <= u.hi < 3
        e2u, eh = (2*u).exp(), (u/2).exp()
        finite = I(0)
        for q in range(1, THETA_TERMS+1):
            v = pi*(q*q)*e2u
            finite += eh*(8*v*v-12*v)*(-v).exp()
        full = finite+I(0, I.rational(tail).hi)
        assert full.lo > 0
        tprev, tnow = I(1), y
        sums[0] += full
        sums[1] += full*tnow
        for k in range(2, n):
            tnext = 2*y*tnow-tprev
            sums[k] += full*tnext
            tprev, tnow = tnow, tnext
        nodes.append({"j": j, "energy": x.data(), "sqrt_energy": u.data(),
                      "kernel": full.data()})

    cheb_ints, coefficients, coefficient_error = [], [], Fraction(0)
    for k, total in enumerate(sums):
        ci = total*I.rational(Fraction(1 if k == 0 else 2, n))
        center = (Fraction(ci.lo)+Fraction(ci.hi))/2
        integer = round(center*COEFF_DEN)
        chosen = Fraction(integer, COEFF_DEN)
        error = max(abs(Fraction(ci.lo)-chosen), abs(Fraction(ci.hi)-chosen))
        coefficient_error += error
        cheb_ints.append(integer)
        coefficients.append({"k": k, "enclosure": ci.data(),
                             "chosen_numerator": str(integer),
                             "absolute_error": str(error)})

    analytic_error = Fraction(8*10**9 * 2**DEGREE, 3**DEGREE)
    epsilon = analytic_error+coefficient_error
    assert epsilon < Fraction(1, 10**34)

    # Exact change of basis. T_j(x/4-1), all denominators divide 4^DEGREE.
    one, previous = [Fraction(1)], [Fraction(1)]
    current = [Fraction(-1), Fraction(1, 4)]
    power = [Fraction(cheb_ints[0])] + [Fraction(0) for _ in range(DEGREE)]
    for k in range(1, n):
        tk = current
        for r, val in enumerate(tk):
            power[r] += cheb_ints[k]*val
        if k < DEGREE:
            nxt = [Fraction(0) for _ in range(len(tk)+1)]
            for r, val in enumerate(tk):
                nxt[r] -= 2*val
                nxt[r+1] += val/2
            for r, val in enumerate(previous):
                nxt[r] -= val
            previous, current = tk, nxt
    denominator = COEFF_DEN * 4**DEGREE
    power_ints = [int(v*4**DEGREE) for v in power]
    assert all(Fraction(v*4**DEGREE).denominator == 1 for v in power)
    # Exact endpoint comparison of both bases.
    assert sum(Fraction(cheb_ints[k]*(-1)**k) for k in range(n))*4**DEGREE == power_ints[0]
    assert sum(power_ints[k]*8**k for k in range(n)) == sum(cheb_ints)*4**DEGREE
    record = {
        "degree": DEGREE, "nodes": n, "precision": PRECISION,
        "theta_terms": THETA_TERMS, "machin_terms": MACHIN_TERMS,
        "cosine_terms": COSINE_TERMS, "pi": pi.data(),
        "full_theta_tail_bound": str(tail),
        "cosine_remainder": str(cosine_error),
        "complex_ellipse_bound": "1000000000", "rho": "3/2",
        "analytic_interpolation_error": str(analytic_error),
        "coefficient_error_sum": str(coefficient_error),
        "epsilon": str(epsilon),
        "epsilon_interval": I.rational(epsilon).data(),
        "epsilon_required_upper": "1e-34",
        "chebyshev_denominator": str(COEFF_DEN),
        "chebyshev_coefficients": coefficients,
        "power_denominator": str(denominator),
        "power_numerators": list(map(str, power_ints)),
        "node_enclosures": nodes,
    }
    return power_ints, denominator, epsilon, pi, record


MULTIPLICATIONS = []


def trim(p):
    while len(p)>1 and p[-1] == 0:
        p.pop()
    return p


def intpoly_add(a, b, scale_b=1):
    out = a[:]+[0]*max(0, len(b)-len(a))
    for j, c in enumerate(b):
        out[j] += scale_b*c
    return trim(out)


def eval_mod(p, x, prime):
    v = 0
    for c in reversed(p):
        v = (v*x+c) % prime
    return v


def intpoly_mul(a, b):
    if a == [0] or b == [0]:
        return [0]
    if len(a) == 1:
        return [a[0]*c for c in b]
    if len(b) == 1:
        return [b[0]*c for c in a]
    # Kronecker substitution with balanced digits. Every resulting
    # coefficient is strictly smaller than 2^(width-2) in absolute value.
    width = (max(abs(v) for v in a).bit_length()
             + max(abs(v) for v in b).bit_length()
             + min(len(a), len(b)).bit_length()+2)
    size = (width+7)//8
    width = 8*size
    base, half = 1 << width, 1 << (width-1)

    def pack(p):
        pos, neg = bytearray(len(p)*size), bytearray(len(p)*size)
        for j, c in enumerate(p):
            target = pos if c >= 0 else neg
            target[j*size:(j+1)*size] = abs(c).to_bytes(size, 'little')
        return int.from_bytes(pos, 'little')-int.from_bytes(neg, 'little')

    product = pack(a)*pack(b)
    sign = -1 if product < 0 else 1
    length = len(a)+len(b)-1
    raw = abs(product).to_bytes(length*size, 'little')
    carry, result = 0, []
    for j in range(length):
        digit = int.from_bytes(raw[j*size:(j+1)*size], 'little')+carry
        if digit >= half:
            digit -= base
            carry = 1
        else:
            carry = 0
        result.append(sign*digit)
    assert carry == 0
    assert max(abs(v) for v in result) < (1 << (width-2))
    checks = []
    for x, prime in ((3, 1000000007), (19, 1000000009)):
        ok = eval_mod(result, x, prime) == eval_mod(a, x, prime)*eval_mod(b, x, prime) % prime
        assert ok
        checks.append(ok)
    MULTIPLICATIONS.append({"input_lengths": [len(a), len(b)],
                            "output_length": length, "digit_bits": width,
                            "modular_sanity_checks": checks})
    return trim(result)


def convolution_polynomial(power, denominator, terms):
    # Gamma(k+l+1/2)=sqrt(pi)*(2k+2l)!/(4^(k+l)*(k+l)!).
    common = 2*factorial(12)*denominator*4**(DEGREE+6)
    q = []
    for k in range(7):
        q.append([a*(factorial(2*(k+l))//factorial(k+l))
                  *4**(DEGREE+6-k-l)*(factorial(12)//factorial(2*k))
                  for l, a in enumerate(power)])
    powers = {(k, 0): [1] for k in range(7)}
    for k in range(7):
        powers[(k, 1)] = q[k]

    def getpower(k, n):
        if (k, n) not in powers:
            left = getpower(k, n//2)
            right = getpower(k, n-n//2)
            powers[(k, n)] = intpoly_mul(left, right)
        return powers[(k, n)]

    # P has the exact A_0^6 factor. Use it once, without changing the
    # prescribed normalization or the signed density.
    inner = [0]
    for index, term in enumerate(terms):
        exponents = term['exponents_A0_to_A6'][:]
        exponents[0] -= 6
        factors = [getpower(k, n) for k, n in enumerate(exponents) if n]
        factors.sort(key=len)
        while len(factors)>1:
            a, b = factors.pop(0), factors.pop(0)
            factors.append(intpoly_mul(a, b))
            factors.sort(key=len)
        inner = intpoly_add(inner, factors[0], term['coefficient'])
        if index % 8 == 7:
            print(f"exact signed polynomial: {index+1}/{len(terms)} terms", flush=True)
    return intpoly_mul(inner, getpower(0, 6)), common**12


def cells(lib, r, den, epsilon, pi, terms):
    I = lib.I
    degree = len(r)-1
    last_fact = factorial(degree+18)
    # Integral polynomial: pi^6/den * sum r_n E^(18+n)/(18+n)!.
    # All 33 evaluations share this exact denominator.
    full_den = den * last_fact * 4**(degree+18)
    coefficients = [0]*(degree+1)
    ratio, four = 1, 1
    for n in range(degree, -1, -1):
        coefficients[n] = r[n]*ratio*four
        ratio *= n+18
        four *= 4
    values = []
    for j in range(33):
        value = 0
        for c in reversed(coefficients):
            value = value*j+c
        values.append(value*j**18)
    weight = sum((Fraction(abs(t['coefficient']), reduce(
        lambda x, y: x*y,
        (factorial(k)**a for k, a in enumerate(t['exponents_A0_to_A6'])), 1))
        for t in terms), Fraction(0))
    # |K|<=7, epsilon<1: telescoping 12 factors gives 12 epsilon 8^11.
    common_error = Fraction(12*8**11, 2**36*factorial(18))*epsilon*weight
    pi6 = pi**6
    records, signs = [], []
    for j in range(32):
        numerator = values[j+1]-values[j]
        approx = I.rational(Fraction(numerator, full_den))*pi6
        er = I.rational(common_error*Fraction((j+1)**18-j**18, 4**18))*pi6
        full = approx+I(-er.hi, er.hi)
        sign = 1 if full.lo>0 else -1 if full.hi<0 else 0
        signs.append(sign)
        records.append({"j": j, "cell": [str(Fraction(j, 4)), str(Fraction(j+1, 4))],
                        "polynomial_integral_numerator": str(numerator),
                        "polynomial_integral_interval": approx.data(),
                        "full_kernel_error_upper": str(er.hi),
                        "full_mass_interval": full.data(), "certified_sign": sign})
    triples = [[i, j, k] for i in range(32) for j in range(i+1, 32)
               for k in range(j+1, 32)
               if signs[i] and signs[j] == -signs[i] and signs[k] == signs[i]]
    return {
        "common_polynomial_integral_denominator": str(full_den),
        "absolute_beta_weight": str(weight),
        "common_error_without_pi6_or_cell_power": str(common_error),
        "cells": records,
        "summary": {"signs": signs, "positive_cells": signs.count(1),
                    "negative_cells": signs.count(-1), "uncertain_cells": signs.count(0),
                    "required": "i<j<k, nonzero alternating certified signs",
                    "alternating_triples": triples,
                    "nonzero_on_interval_certified": any(signs),
                    "global_crossing_bound": "not established"},
    }


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--algebra-only', action='store_true')
    args = parser.parse_args()
    record = {"algebra": algebra()}
    path = Path(__file__).with_suffix('.json')
    if not args.algebra_only:
        lib = load_intervals()
        power, den, epsilon, pi, approximation = approx_kernel(lib)
        record['approximation'] = approximation
        path.write_text(json.dumps(record, indent=2) + '\n')
        print(f"full-kernel polynomial enclosure saved; epsilon < 1e-34; {path}", flush=True)
        r, common_den = convolution_polynomial(power, den, record['algebra']['terms'])
        polynomial_path = BASE / 'actual-h2-energy-cell-polynomial-48.json'
        polynomial_path.write_text(json.dumps({"numerators": list(map(str, r)),
                                               "denominator": str(common_den),
                                               "multiplications": MULTIPLICATIONS})+'\n')
        print(f"exact convolution polynomial degree={len(r)-1}; {polynomial_path}", flush=True)
        record['convolution_polynomial_path'] = polynomial_path.name
        record['mass_test'] = cells(lib, r, common_den, epsilon, pi, record['algebra']['terms'])
        record['arithmetic'] = {
            name: {"precision": ctx.prec, "rounding": ctx.rounding,
                   "traps": {str(k): v for k, v in ctx.traps.items()},
                   "flags": {str(k): v for k, v in ctx.flags.items()}}
            for name, ctx in [('down', lib.DOWN), ('up', lib.UP), ('near', lib.NEAR)]}
        print(json.dumps(record['mass_test']['summary']), flush=True)
    path.write_text(json.dumps(record, indent=2) + '\n')
    print(f"exact terms={record['algebra']['term_count']}; "
          f"max denominator exponent={record['algebra']['maximum_degree_before_homogenization']}; "
          f"finite-log residuals=0; constant-kernel leading coefficient=0; {path}")
