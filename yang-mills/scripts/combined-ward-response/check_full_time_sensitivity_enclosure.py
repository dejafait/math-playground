"""Outward integer upper bound for L035's COMPLETE time integral.

No time quadrature: bound the initial nonnegative heat tensor and integrate
its spectral-gap exponential envelope. The input is L037's fixed hex table.
"""
import hashlib
import json
from fractions import Fraction as F
from functools import lru_cache
from math import isqrt
from pathlib import Path

import check_exact_fourier_quadrature as ar
from check_continuum_pure_sectors import operators
from check_continuum_tensor import product_terms

S, I = ar.S, ar.I
ONE, ZERO = I(S), I(0)
M = 112
ETA = F(1, 10**12)
ROOT = Path(__file__).parent
INPUT = ROOT / 'stored-fourier-enclosure-certificate.json'
OUTPUT = ROOT / 'full-time-sensitivity-enclosure-certificate.json'


def ceildiv(a, b):
    return -((-a)//b)


def mul(a, b):
    """Upper endpoints of nonnegative numbers, all scaled by S."""
    assert a >= 0 and b >= 0
    return ceildiv(a*b, S)


def rat(q):
    return I.rational(q)


def power(z, n):
    out = ONE
    for _ in range(n):
        out = out*z
    return out


def display(n):
    q = ceildiv(n*10**24, S)
    return f'{q//10**24}.{q%10**24:024d}'


def main():
    data = json.loads(INPUT.read_text())
    transforms = {}
    for row in data['transforms']:
        key = row['h'], row['n']
        assert key not in transforms
        transforms[key] = tuple(rat(F(float.fromhex(row[field])))
                                for field in ('stored_real_hex', 'stored_imag_hex'))
    assert set(transforms) == {(h, n) for h in (0, 1) for n in range(-224, 225)}
    # Rational alternating Machin enclosure, independent of machine pi.
    def atan(q):
        a = sum(((-1)**j*q**(2*j+1)/F(2*j+1) for j in range(80)), F(0))
        b = a+q**161/F(161)
        return I(rat(a).lo, rat(b).hi)
    pi = rat(16)*atan(F(1, 5))-rat(4)*atan(F(1, 239))
    omega = pi/rat(8)
    assert pi.lo > 3*S
    z = isqrt(S*S//8)
    zero_amplitude = I(z, z+1)
    assert 8*z*z <= S*S < 8*(z+1)**2
    heat = [ar.exp_negative(rat(F(1, 16))*omega*omega*rat(n*n)).hi
            for n in range(M+1)]
    assert all(0 <= x <= S for x in heat)
    features, terms = [], []
    totals = [0, 0]
    algebra = [operators(pair) for pair in ((0, 2), (1, 3))]
    products = {(alpha, i, c): product_terms(algebra[alpha][0][i], algebra[alpha][1], c)
                for alpha in range(2) for i in range(2) for c in range(4)}

    @lru_cache(None)
    def prefactor(t, positives, zeros):
        return power(omega, t)*rat(F(1, 4**positives))*power(zero_amplitude, zeros)

    @lru_cache(None)
    def weak(h, d, a, b, lc, rc, k, ell):
        lp, rp = (k if lc else k+1), (ell if rc else ell+1)
        if (h+d+a+b+lp+rp) % 2:
            return 0, 0
        if (k == 0 and (not lc or a)) or (ell == 0 and (not rc or b)):
            return 0, 0
        left = (0,) if k == 0 else (-k, k)
        right = (0,) if ell == 0 else (-ell, ell)
        value, multiplier = ZERO, 0
        for p in left:
            for q in right:
                # sine amplitude is -i sign/4; shifted phase is i**index.
                phase = p+q+a+b-d
                coefficient = p**a*q**b*(p+q)**d
                if not lc:
                    phase -= 1
                    coefficient *= 1 if p > 0 else -1
                if not rc:
                    phase -= 1
                    coefficient *= 1 if q > 0 else -1
                re, im = transforms[h, p+q]
                selected = (re, -im, -re, im)[phase % 4]
                value = value+rat(coefficient)*selected
                multiplier += abs(p)**a*abs(q)**b*abs(p+q)**d
        zeros = int(k == 0)+int(ell == 0)
        factor = prefactor(d+a+b, 2-zeros, zeros)
        enclosure = factor*value
        baseline = max(abs(enclosure.lo), abs(enclosure.hi))
        delta = (rat(ETA*(9 if h else 6)*multiplier)*factor).hi
        assert baseline >= 0 and delta >= 0
        return baseline, delta

    for alpha in range(2):
        for component in range(4):
            ops = [products[alpha, i, component] for i in range(2)]
            tables = []
            for axis in range(4):
                ks = [0] if axis == 0 else range(1, M+1)
                ls = range(0 if axis == component else 1, M+1)
                if axis == 0:
                    ls = [n for n in ls if n % 2 == 0]
                h = int(axis in ((0, 2), (1, 3))[alpha])
                table = {}
                for key in sorted({key[axis] for op in ops for key in op}):
                    first, second = key
                    base, error = 0, 0
                    for k in ks:
                        for ell in ls:
                            b1, d1 = weak(h, *first, axis == 0, axis == component, k, ell)
                            b2, d2 = weak(h, *second, axis == 0, axis == component, k, ell)
                            weight = heat[k]*heat[ell]
                            base += ceildiv(b1*b2*weight, S**3)
                            error += ceildiv((d1*b2+b1*d2+d1*d2)*weight, S**3)
                    table[key] = base, error
                    features.append(dict(alpha=alpha, component=component, axis=axis,
                                         key=key, baseline_upper=str(base), allowance_upper=str(error)))
                tables.append(table)
            for i, op in enumerate(ops):
                for key, coefficient in sorted(op.items()):
                    p, e = S, 0
                    for j in range(4):
                        b, d = tables[j][key[j]]
                        e, p = mul(e, b+d)+mul(p, d), mul(p, b)
                    v = abs(coefficient)
                    contribution = ceildiv(v.numerator*e, v.denominator)
                    totals[i] += contribution
                    terms.append(dict(alpha=alpha, component=component, probe=[3, 6][i],
                                      key=key, coefficient=str(coefficient),
                                      initial_allowance_upper=str(e), contribution_upper=str(contribution)))
            # Each cache is a complete local weak-mode table; release after use.
            weak.cache_clear()
            print(json.dumps(dict(completed_potential=alpha, component=component,
                                  feature_records=len(features), path=str(OUTPUT))), flush=True)
    factor = F(8)*(F(64, 27)**3)
    bounds = [ceildiv(x*factor.numerator, factor.denominator) for x in totals]
    budgets = [100, 1000]
    failures = [f'probe {i} sensitivity budget failed' for i, x, b in zip((3, 6), bounds, budgets)
                if x >= b*S]
    result = dict(scope='Certified upper bound of L035 full-time S at eta=1e-12, not signed tensor value.',
                  cutoff=M, eta=str(ETA), scale=str(S),
                  input_path=str(INPUT.relative_to(ROOT)), input_sha256=hashlib.sha256(INPUT.read_bytes()).hexdigest(),
                  pi_interval=dict(lo=str(pi.lo), hi=str(pi.hi)),
                  zero_amplitude_interval=dict(lo=str(z), hi=str(z+1)),
                  heat_upper=[str(x) for x in heat], feature_tables=features, collected_terms=terms,
                  initial_heat_allowance_upper=[str(x) for x in totals],
                  full_time_multiplier=str(factor), full_time_sensitivity_upper=[str(x) for x in bounds],
                  full_time_decimal_upper=[display(x) for x in bounds], required_budgets=budgets,
                  failures=failures, passed=not failures, signed_response_enclosed=False)
    OUTPUT.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(dict(actual_upper=result['full_time_decimal_upper'], required=budgets,
                          failures=failures, path=str(OUTPUT))), flush=True)
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
