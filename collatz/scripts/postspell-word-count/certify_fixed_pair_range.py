#!/usr/bin/env python3
"""Certify the approved L051 predicate, stopping at its first failure."""
from fractions import Fraction as Q
from pathlib import Path
import json

BITS, TERMS = 192, 96
SCALE = 2**BITS
P, QDEN = 9809721694, 6189245291
THRESHOLD = 225640000
checks = []
logs = {}


def floorq(t):
    return t.numerator // t.denominator


def base_log(t):
    # All divisions and powers are integer/rational, including rounding.
    x = (t - 1) / (t + 1)
    assert 0 <= x <= Q(1, 3)
    partial = sum(floorq(SCALE * 2*x**(2*j+1)/(2*j+1))
                  for j in range(TERMS))
    lo = Q(partial, SCALE)
    # Uniform positive integral bound for 0<=x<=1/3 keeps operands compact.
    remainder = Q(9, 4*(2*TERMS+1)*3**(2*TERMS+1))
    hi = lo + Q(TERMS, SCALE) + remainder
    return lo, hi, dict(x=str(x), rounded_partial_integer=partial,
                       rounding_budget=str(Q(TERMS, SCALE)),
                       integral_remainder_upper=str(remainder))


ELL_LO, ELL_HI, ELL_DETAIL = base_log(Q(2))


def log_bounds(t, retain=False):
    t = Q(t)
    assert t >= 1
    k = t.numerator.bit_length() - t.denominator.bit_length()
    while t < 2**k:
        k -= 1
    while t >= 2**(k+1):
        k += 1
    assert k >= 0
    v = t / 2**k
    lo, hi, detail = base_log(v)
    result = lo + k*ELL_LO, hi + k*ELL_HI
    if retain:
        logs[str(t)] = dict(argument=str(t), binary_exponent=k,
                            reduced_argument=str(v), lower=str(result[0]),
                            upper=str(result[1]), detail=detail)
    return result


def positive(name, certified_lower):
    # Round a certified lower bound DOWN for concise complete sign evidence.
    margin = Q(floorq(certified_lower * 10**12), 10**12)
    passed = margin > 0
    checks.append(dict(name=name, actual=str(margin), relation='>',
                       required='0', passed=passed))
    if not passed:
        raise ArithmeticError(f'Unresolved or failed sign: {name}')


L3, U3 = log_bounds(3, retain=True)
EPS_LO, EPS_HI = QDEN*L3-P*ELL_HI, QDEN*U3-P*ELL_LO
positive('epsilon positive', EPS_LO)
positive('log2 exceeds 2/3', ELL_LO-Q(2, 3))

rows = []
for r in range(3, 100):
    start_check = len(checks)
    rho = Q(48, 25)
    R = sum((rho**j for j in range(r)), Q(0))
    assert R == (rho**r-1)/(rho-1)
    A = Q(399, 5)*R
    lr, ur = log_bounds(r, retain=True)
    BLO, BHI = (54+6*lr)*R+Q(69*r, 1034), (54+6*ur)*R+Q(69*r, 1034)

    def f_bounds(t, retain=False):
        lt, ut = log_bounds(t, retain=retain)
        return Q(t)-A*ut-BHI, Q(t)-A*lt-BLO

    def f_sign(t):
        low, high = f_bounds(t)
        if low > 0:
            return 1
        if high < 0:
            return -1
        raise ArithmeticError(f'Unresolved F_{r}({t})')

    first = floorq(A)+1
    if f_sign(first) > 0:
        M = first
    else:
        low, high = first, 2*first
        while f_sign(high) < 0:
            high *= 2
        while high-low > 1:
            mid = (low+high)//2
            if f_sign(mid) > 0:
                high = mid
            else:
                low = mid
        M = high

    fmlo, fmhi = f_bounds(M, retain=True)
    positive(f'r={r}: M>A', Q(M)-A)
    positive(f'r={r}: F(M)>0', fmlo)
    prev = M-1
    if prev > A:
        fplo, fphi = f_bounds(prev, retain=True)
        positive(f'r={r}: F(M-1)<0', -fphi)
        previous = dict(integer=prev, F_lower=str(fplo), F_upper=str(fphi))
    else:
        previous = dict(integer=prev, at_or_below_A=True)
        assert prev <= A

    guard_lo, guard_hi = ELL_LO-2*M*EPS_HI, ELL_HI-2*M*EPS_LO
    if guard_lo > 0:
        guard_pass = True
        positive(f'r={r}: half-log guard holds', guard_lo)
    elif guard_hi < 0:
        guard_pass = False
        positive(f'r={r}: half-log guard fails', -guard_hi)
    else:
        raise ArithmeticError(f'Unresolved half-log guard r={r}')

    D = Q(69*r*QDEN+23, 11)
    ld, ud = log_bounds(D, retain=True)
    TLO, THI = Q(15,4)*R*(1+ld), Q(15,4)*R*(1+ud)
    if THI <= THRESHOLD:
        odd_pass = True
        positive(f'r={r}: T below primitive threshold', THRESHOLD-THI)
    elif TLO > THRESHOLD:
        odd_pass = False
        positive(f'r={r}: T above primitive threshold', TLO-THRESHOLD)
    else:
        raise ArithmeticError(f'Unresolved odd-count comparison r={r}')
    row = dict(r=r, R=str(R), A=str(A), B_lower=str(BLO), B_upper=str(BHI),
               least_integer_ceiling=M, F_M_lower=str(fmlo), F_M_upper=str(fmhi),
               previous=previous, guard_lower=str(guard_lo), guard_upper=str(guard_hi),
               half_log_guard_pass=guard_pass, D=str(D), T_lower=str(TLO),
               T_upper=str(THI), odd_count_pass=odd_pass,
               success=guard_pass and odd_pass, checks=checks[start_check:])
    rows.append(row)
    if not row['success']:
        break
else:
    raise ArithmeticError('Search bound reached without first failure')

failures = [c for c in checks if not c['passed']]
result = dict(lemma='L051', scope='Only the approved fixed-pair sufficient predicate.',
              bits=BITS, terms=TERMS, p=P, q=QDEN,
              log2=dict(lower=str(ELL_LO), upper=str(ELL_HI), detail=ELL_DETAIL),
              epsilon_lower=str(EPS_LO), epsilon_upper=str(EPS_HI),
              primitive_threshold=THRESHOLD, rows=rows, logarithms=logs,
              checks=checks, failures=failures,
              successful_range=[3, rows[-1]['r']-1], first_failure=rows[-1]['r'])
output = Path(__file__).with_name('fixed-pair-range-certificate.json')
output.write_text(json.dumps(result, indent=2)+'\n')
print(f'checks={len(checks)}; failures={len(failures)}; success range={result["successful_range"]}; first failure={result["first_failure"]}')
for row in rows:
    tl = Q(floorq(Q(row['T_lower'])*100),100)
    tu = Q(floorq(Q(row['T_upper'])*100)+1,100)
    print(f'r={row["r"]}: least M={row["least_integer_ceiling"]}; half-log guard={row["half_log_guard_pass"]}; {tl}<T<{tu}, required T<=225640000; predicate={row["success"]}')
print(f'certificate: {output.relative_to(Path.cwd())}')
if failures:
    raise SystemExit(1)
