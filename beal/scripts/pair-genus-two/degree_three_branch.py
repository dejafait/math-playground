#!/usr/bin/env python3
"""Bounded full-sextic good-prime test and complete divisor certificate."""
import json
from itertools import product
from degree_three_budget import Budget, ROOT

Q = [7, 52, -6, -64, -25]  # ascending coefficients
F = [-308, -2288, 341, 3388, 1034, -704, -275]


def run():
    b = Budget(fresh=True)
    b.phase('producer')
    out = dict(status='INCOMPLETE', quartic=Q, sextic=F, primes=[],
               selected_prime=None, failures=[])

    def polyop(v):
        b.charge()
        b.polynomial(v)
        return v

    def trim(a):
        a = list(a)
        while len(a) > 1 and a[-1] == 0:
            a.pop()
        return a

    def rem(a, d, p):
        b.charge()
        b.polynomial(a)
        b.polynomial(d)
        a = trim([x % p for x in a])
        d = trim([x % p for x in d])
        inv = pow(d[-1], -1, p)
        while len(a) >= len(d) and a != [0]:
            c = a[-1] * inv % p
            shift = len(a)-len(d)
            for j, v in enumerate(d):
                a[j+shift] = (a[j+shift] - c*v) % p
            a = trim(a)
        return polyop(a)

    def gcd(a, d, p):
        b.charge()
        while d != [0]:
            a, d = d, rem(a, d, p)
        return polyop([(x*pow(a[-1], -1, p)) % p for x in a])

    try:
        # Exact input expansion is preprocessing, charged before execution.
        b.polynomial(Q)
        b.polynomial(F)
        expansion = [0]*7
        b.charge()  # polynomial multiplication and scalar multiplication
        for i, q in enumerate(Q):
            expansion[i] -= 44*q
            expansion[i+2] += 11*q
        b.polynomial(expansion)
        b.scalar(*expansion)
        assert expansion == F
        out['input_expansion'] = expansion
        # Applicability/exceptional-chart comparisons are scalar/row checks.
        b.charge(n=12)
        for p in range(3, 98):
            b.scalar(p)
            prime = True
            for d in range(2, p):
                b.scalar(p % d)
                if p % d == 0:
                    prime = False
                    break
            if not prime:
                continue
            # Up to 24 producer visits leaves one for independent replay.
            b.charge('prime_visits')
            b.charge()
            fp, qp = polyop([c % p for c in F]), polyop([c % p for c in Q])
            row = dict(prime=p, sextic=fp, quartic=qp,
                       leading_coefficients_nonzero=bool(fp[-1] and qp[-1]),
                       divisor_trials=[])
            out['primes'].append(row)
            b.charge()  # processed prime row
            if not row['leading_coefficients_nonzero']:
                row['skip'] = 'degree drop'
                continue
            der = polyop([i*fp[i] % p for i in range(1, 7)])
            g = gcd(fp, trim(der), p)
            row['sextic_derivative'] = der
            row['squarefree_gcd'] = g
            if g != [1]:
                row['skip'] = 'not squarefree'
                continue
            divisor = None
            for degree in (1, 2):
                for coeff in product(range(p), repeat=degree):
                    b.charge('divisor_trials')
                    b.charge()  # candidate check
                    d = list(coeff) + [1]
                    r = rem(qp, d, p)
                    row['divisor_trials'].append(dict(divisor=d, remainder=r))
                    b.charge()  # processed certificate row
                    if r == [0]:
                        divisor = d
                        break
                if divisor is not None:
                    break
            row['found_divisor'] = divisor
            if divisor is None:
                row['complete_monic_linear_quadratic_test'] = True
                out['selected_prime'] = p
                out['status'] = 'QUARTIC_IRREDUCIBLE_GOOD_REDUCTION'
                break
        if out['selected_prime'] is None:
            out['status'] = 'INCONCLUSIVE'
    except Exception as exc:
        out['failures'].append(str(exc))
        raise
    finally:
        out['budget'] = b.summary()
        path = ROOT / 'degree-three-branch-certificate.json'
        path.write_text(json.dumps(out, indent=2) + '\n')
        print(json.dumps(dict(status=out['status'], selected_prime=out['selected_prime'],
            failures=out['failures'], budget=b.summary(), certificate=str(path)), indent=2))


if __name__ == '__main__':
    run()
