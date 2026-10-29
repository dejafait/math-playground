#!/usr/bin/env python3
"""Independent selected-prime replay: Horner residues and Bezout identity.

Imports accounting only, never producer arithmetic. Earlier unsuccessful
primes are not load-bearing and are not rerun. All selected-prime rows are.
"""
import json
from itertools import product
from degree_three_budget import Budget, ROOT


def run():
    b = Budget()
    b.phase('independent-replay')
    cert = json.loads((ROOT / 'degree-three-branch-certificate.json').read_text())
    out = dict(status='INCOMPLETE', checks=0, failures=[])
    p = cert['selected_prime']

    def check(label, condition):
        b.charge()  # scalar check / processed verification row
        out['checks'] += 1
        if not condition:
            out['failures'].append(label)
            raise AssertionError(label)

    def canon(v):
        b.charge()  # polynomial reduction/normalization
        b.polynomial(v)
        v = [c % p for c in v]
        while len(v) > 1 and v[-1] == 0:
            v.pop()
        b.polynomial(v)
        return v

    def add(a, d):
        b.charge()
        return canon([(a[i] if i < len(a) else 0) +
                      (d[i] if i < len(d) else 0)
                      for i in range(max(len(a), len(d)))])

    def neg(a):
        b.charge()
        return canon([-x for x in a])

    def mul(a, d):
        b.charge()
        b.polynomial(a)
        b.polynomial(d)
        v = [0]*(len(a)+len(d)-1)
        for i, x in enumerate(a):
            for j, y in enumerate(d):
                v[i+j] += x*y
        return canon(v)

    def divide(a, d):
        b.charge()
        a, d = canon(a), canon(d)
        q = [0]*max(1, len(a)-len(d)+1)
        while a != [0] and len(a) >= len(d):
            shift = len(a)-len(d)
            scalar = a[-1]*pow(d[-1], -1, p) % p
            q[shift] = scalar
            term = [0]*shift + [scalar]
            a = add(a, neg(mul(term, d)))
        return canon(q), a

    try:
        check('successful input status', cert['status'] == 'QUARTIC_IRREDUCIBLE_GOOD_REDUCTION')
        check('empty producer failures', cert['failures'] == [])
        check('prime range', isinstance(p, int) and 3 <= p <= 97)
        for d in range(2, p):
            b.scalar(d, p % d)
            check('prime divisor ' + str(d), p % d != 0)
        b.charge('prime_visits')
        b.charge()
        Q = [7, 52, -6, -64, -25]
        F = [-308, -2288, 341, 3388, 1034, -704, -275]
        check('quartic input', cert['quartic'] == Q)
        check('sextic input', cert['sextic'] == F)
        # Independent integer coefficient convolution, before modular reduction.
        b.charge()
        expanded = [sum(([-44, 0, 11][j]*Q[i-j]
            if 0 <= i-j < 5 else 0) for j in range(3)) for i in range(7)]
        b.polynomial(expanded)
        check('integer expansion', expanded == F == cert['input_expansion'])
        rows = [r for r in cert['primes'] if r['prime'] == p]
        check('unique selected row', len(rows) == 1)
        row = rows[0]
        f, q = canon(F), canon(Q)
        check('full reduced sextic', row['sextic'] == f and len(f) == 7)
        check('full reduced quartic', row['quartic'] == q and len(q) == 5)
        check('nonzero leading coefficients', row['leading_coefficients_nonzero'])
        b.charge()
        df = canon([i*f[i] for i in range(1, 7)])
        check('sextic derivative', row['sextic_derivative'] == df)
        # Extended Euclid; retain full independent Bezout witness.
        a, d = f, df
        u0, u1, v0, v1 = [1], [0], [0], [1]
        while d != [0]:
            quotient, remainder = divide(a, d)
            a, d = d, remainder
            u0, u1 = u1, add(u0, neg(mul(quotient, u1)))
            v0, v1 = v1, add(v0, neg(mul(quotient, v1)))
        check('gcd constant', len(a) == 1 and a[0] != 0)
        scale = [pow(a[0], -1, p)]
        u, v = mul(u0, scale), mul(v0, scale)
        residual = add(mul(u, f), mul(v, df))
        check('complete squarefree Bezout identity', residual == [1])
        check('producer gcd', row['squarefree_gcd'] == [1])
        out['squarefree_bezout'] = dict(u=u, v=v, identity=residual)
        trials = row['divisor_trials']
        check('required trial count', len(trials) == p + p*p)
        k = 0
        for degree in (1, 2):
            for lower in product(range(p), repeat=degree):
                b.charge('divisor_trials')
                b.charge()  # candidate check
                expected = list(lower) + [1]
                # Horner in F_p[X]/(X^degree + lower), with fixed-size vectors.
                residue = [0]*degree
                for c in reversed(q):
                    b.charge()  # one quotient-ring multiply by X and scalar add
                    high = residue[-1]
                    residue = [c] + residue[:-1]
                    residue = [(residue[j] - high*lower[j]) % p
                               for j in range(degree)]
                    b.polynomial(residue)
                residue = canon(residue)
                item = trials[k]
                b.charge()  # processed full certificate row
                check('divisor row ' + str(k), item['divisor'] == expected)
                check('full remainder row ' + str(k), item['remainder'] == residue)
                check('nonzero remainder row ' + str(k), residue != [0])
                k += 1
        check('all rows processed', k == len(trials))
        check('exhaustion flags', row['found_divisor'] is None and
              row['complete_monic_linear_quadratic_test'] is True)
        check('projective infinity not branch', F[-1] != 0)
        out['selected_prime'] = p
        out['complete_divisor_rows_verified'] = k
        out['status'] = 'PASS'
    except Exception as exc:
        if str(exc) not in out['failures']:
            out['failures'].append(str(exc))
        raise
    finally:
        out['budget'] = b.summary()
        path = ROOT / 'degree-three-branch-verification.json'
        path.write_text(json.dumps(out, indent=2) + '\n')
        print(json.dumps(dict(status=out['status'], checks=out['checks'],
            failures=out['failures'], budget=b.summary(), verification=str(path)), indent=2))


if __name__ == '__main__':
    run()
