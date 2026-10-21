"""Step 201: rational full-response coefficients; no float proof decisions."""
import argparse
import json
from pathlib import Path
from fractions import Fraction as F
from check_response_modulus_second_moment import (
    add, sub, mul, div, exact, encode, round_iv, primes_to, DEN)


def local_t(p, degree):
    u, v = F(1, p**3), F(1, p**5)
    if degree == 2:
        return ((1+v)/(1-v)**3 * (1+u)/(1-u)
                + 2*u/((1-u)**2*(1-v)**2))
    assert degree == 3
    return ((1+4*v+v*v)/(1-v)**5 * (1+u)/(1-u)
            + 3*(1+v)/(1-v)**4 * u/(1-u)**2
            + 1/(1-v)**3 * u*(1+u)/(1-u)**3)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--cutoff', type=int, default=200)
    parser.add_argument('--order', type=int, default=40)
    args = parser.parse_args()
    P, E = args.cutoff, args.order
    assert (P, E) in [(200, 40), (1000, 80)]
    ps = primes_to(P)
    tails, locals_c, locals_t, c, z, t = {}, {}, {}, {}, {}, {}
    for j in [1, 2, 3, 13, 14, 15, 16, 17]:
        val, records = exact(1), []
        for p in ps:
            term = total = F(1)
            for e in range(1, E+1):
                term *= F((j+e-1)**2, e*e*p**5)
                total += term
            ratio = F((j+E)**2, (E+1)**2*p**5)
            assert ratio < 1
            rem = term*ratio/(1-ratio)
            fac = round_iv(total, total+rem)
            records.append(dict(p=p, factor=encode(fac),
                                local_tail_upper=str(rem), next_ratio=str(ratio)))
            val = mul(val, fac)
        r = F(j*j, 4*P**4)/(1-F(j*j, (P+1)**5))
        assert 0 < r < 1
        tails[f'C{j}'] = str(r)
        c[j] = mul(val, (F(1), 1/(1-r)))
        locals_c[j] = records
    for s in [3, 5, 6]:
        val = exact(1)
        for p in ps:
            val = mul(val, exact(1/(1-F(1, p**s))))
        r = F(1, (s-1)*P**(s-1))/(1-F(1, (P+1)**s))
        assert 0 < r < 1
        tails[f'zeta{s}'] = str(r)
        z[s] = mul(val, (F(1), 1/(1-r)))
    S = div(mul(z[5], mul(z[3], z[3])), z[6])
    for degree in [2, 3]:
        val, records = exact(1), []
        for p in ps:
            fac = local_t(p, degree)
            val = mul(val, exact(fac))
            records.append(dict(p=p, factor=str(fac)))
        # T2 <= (1-u)^-4(1-v)^-4; T3 <= (1-u)^-6(1-v)^-9.
        a, b = (4, 4) if degree == 2 else (6, 9)
        r = (F(a, 2*P**2)/(1-F(1, (P+1)**3))
             + F(b, 4*P**4)/(1-F(1, (P+1)**5)))
        assert 0 < r < 1
        tails[f'T{degree}'] = str(r)
        t[degree] = mul(val, (F(1), 1/(1-r)))
        locals_t[degree] = records
    theta, b2, b3, ratios = {}, {}, {}, {}
    for k in [13, 14]:
        ratios[k] = div(c[k+1], c[k])
        theta[k] = div(sub(S, c[1]), sub(ratios[k], c[1]))
        b2[k] = add(c[2], mul(theta[k], sub(div(c[k+2], c[k]), c[2])))
        b3[k] = add(c[3], mul(theta[k], sub(div(c[k+3], c[k]), c[3])))
    alpha = div(sub(b2[14], t[2]), sub(b2[14], b2[13]))
    # Keep the shared alpha in the exact convex identity. Independent
    # boxes for alpha and 1-alpha unnecessarily lose their cancellation.
    law3_independent_box = add(mul(alpha, b3[13]), mul(sub(exact(1), alpha), b3[14]))
    law3 = add(b3[14], mul(alpha, sub(b3[13], b3[14])))
    gap = sub(law3, t[3])
    checks = dict(S_above_C1=S[0]>c[1][1], R13_above_S=ratios[13][0]>S[1],
                  R14_above_S=ratios[14][0]>S[1],
                  B13_below_T2=b2[13][1]<t[2][0],
                  T2_below_B14=t[2][1]<b2[14][0],
                  alpha_in_unit_interval=0<alpha[0]<=alpha[1]<1,
                  actual_minus_law_exceeds_7_over_1000=gap[1]<-F(7, 1000))
    bounds = {'S': encode(S), 'T2': encode(t[2]), 'T3': encode(t[3]),
              'B13': encode(b2[13]), 'B14': encode(b2[14]),
              'D13': encode(b3[13]), 'D14': encode(b3[14]),
              'alpha': encode(alpha), 'law3': encode(law3), 'law3_minus_T3': encode(gap),
              'law3_independent_box': encode(law3_independent_box),
              'C': {j: encode(v) for j, v in c.items()},
              'theta': {j: encode(v) for j, v in theta.items()}}
    failures = [key for key, ok in checks.items() if not ok]
    out = dict(status='EXACT_RATIONAL_INTERVAL_CERTIFICATE', prime_cutoff=P,
               local_order=E, denominator=DEN, primes=ps, bounds=bounds,
               checks=checks, failures=failures, required_gap='actual-law > 7/1000',
               log_tail_upper_bounds=tails, C_local_factors=locals_c,
               T_local_factors=locals_t)
    path = Path(__file__).with_name(f'response-cubic-modulus-second-moment-{P}-{E}.json')
    path.write_text(json.dumps(out, indent=2)+'\n')
    for key in ['T3', 'law3', 'law3_minus_T3', 'alpha']:
        print(key, bounds[key]['decimal_preview'])
    print('Required gap: actual-law > 7/1000; failures:', failures)
    print('Certificate:', path)


if __name__ == '__main__':
    main()
