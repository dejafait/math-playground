#!/usr/bin/env python3
"""Complete smooth diagonal, exact corner, included Young exterior form.

Standard-library computation. Elementary boxes are reused unchanged from
the step142 auditor; no quadrature or previous numerical certificate enters.
The complete certificate is written incrementally. See L961 for mathematics.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
import sys
import time

BASE = Path(__file__).resolve().parent
HELPER = BASE.parent / 'centred-moment' / 'audit_certificate_142.py'
sys.path.insert(0, str(HELPER.parent))
from audit_certificate_142 import (Box, BITS, S, point_log, logarithm,
                                    exponential, root, machin)

OUT = BASE / 'certificate-144.json'
PRIMES = (2, 3, 5, 7)


def midpoint(v):
    return F(v.lo + v.hi, 2*S)


def main():
    start = time.monotonic()
    data = {'status': 'IN_PROGRESS', 'target':
            'Complete {2,3,5,7}-smooth diagonal at t=98/625,x=6000000185827',
            'bits': BITS, 'inputs': {'t': '98/625', 'x': 6000000185827,
                                     'primes': list(PRIMES)},
            'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'helper_sha256': hashlib.sha256(HELPER.read_bytes()).hexdigest(),
            'gates': {}, 'failures': []}

    def save():
        data['elapsed_seconds'] = time.monotonic()-start
        OUT.write_text(json.dumps(data, indent=2)+'\n')

    def gate(name, condition, evidence=None):
        data['gates'][name] = {'passed': bool(condition)}
        if evidence is not None:
            data['gates'][name]['evidence'] = evidence
        if not condition:
            data['failures'].append(name)
            data['status'] = 'INCONCLUSIVE'
            save()
            raise ArithmeticError(name)

    save()
    try:
        t, x = Box(F(98, 625)), Box(6000000185827)
        pi = machin()
        radicand = x/(4*pi)+t/16
        # Integer candidate from the included lower bound, then both exact gates.
        from math import isqrt
        nmax = isqrt(radicand.lo//S)
        low, high = radicand-nmax*nmax, (nmax+1)**2-radicand
        gate('natural_index_lower_strict', low.lo > 0, low.record())
        gate('natural_index_upper_strict', high.lo > 0, high.record())
        cpol = logarithm(root(1+x*x)/(4*pi))/4-1/(2*(1+x*x))
        sigma = Box(F(1, 2))+t*cpol
        data['natural_index'] = nmax
        data['constants'] = {k: v.record() for k, v in
                             [('pi', pi), ('radicand', radicand),
                              ('c_pol', cpol), ('sigma', sigma)]}
        terms = []

        def enumerate_support(j, n, exponents):
            if j == len(PRIMES):
                terms.append({'n': n, 'exponents': exponents,
                              'omega': sum(exponents)})
                return
            exponent = 0
            while n <= nmax:
                enumerate_support(j+1, n, exponents+[exponent])
                exponent += 1
                n *= PRIMES[j]

        enumerate_support(0, 1, [])
        terms.sort(key=lambda a: a['n'])
        # Independently sieve the integer interval for support completeness.
        independent = []
        for n in range(1, nmax+1):
            residual = n
            for p in PRIMES:
                while residual % p == 0:
                    residual //= p
            if residual == 1:
                independent.append(n)
        gate('support_matches_independent_integer_sieve',
             [v['n'] for v in terms] == independent)
        gate('support_no_duplicates', len({v['n'] for v in terms}) == len(terms))
        gate('support_factorization', all(
            v['n'] == 2**v['exponents'][0]*3**v['exponents'][1]*
            5**v['exponents'][2]*7**v['exponents'][3] for v in terms))
        degree = max(v['omega'] for v in terms)
        data.update(degree=degree, support_count=len(terms), terms=terms)
        save()
        logs = [point_log(F(p)) for p in PRIMES]
        data['prime_logs'] = [v.record() for v in logs]
        coefficients = [Box(0) for _ in range(degree+1)]
        for term in terms:
            u = sum((e*v for e, v in zip(term['exponents'], logs)), Box(0))
            a = exponential(t*u*u/4-sigma*u)
            gate('positive_term_'+str(term['n']), a.lo > 0)
            term['log_n'] = u.record()
            term['a_n'] = a.record()
            coefficients[term['omega']] += a
        gate('constant_exactly_one', coefficients[0].lo == coefficients[0].hi == S)
        gate('nonconstant_degree_and_positive_leading', degree >= 1 and coefficients[-1].lo > 0)
        data['coefficients'] = [v.record() for v in coefficients]
        data['status'] = 'COEFFICIENTS_COMPLETE'
        save()
        # S is the upper shift; (Q(S)^*Q(S))_ij sums over k<=min(i,j).
        h = [[sum((coefficients[i-k]*coefficients[j-k]
                   -coefficients[degree-i+k]*coefficients[degree-j+k]
                   for k in range(min(i, j)+1)), Box(0))
              for j in range(degree)] for i in range(degree)]
        data['exterior_form'] = [[v.record() for v in row] for row in h]
        ell = [[Box(int(i == j)) for j in range(degree)] for i in range(degree)]
        pivots = []
        data['pivots'] = []
        for j in range(degree):
            pivot = h[j][j]-sum((ell[j][k]*ell[j][k]*pivots[k]
                                 for k in range(j)), Box(0))
            pivots.append(pivot)
            data['pivots'].append(pivot.record())
            if pivot.lo <= 0:
                data['failed_pivot'] = j
                # Construct an exact rational candidate for a negative witness.
                # L^{-T}e_j from rational midpoints, then enclose v*H*v.
                v = [F(0) for _ in range(degree)]
                v[j] = F(1)
                for i in range(j-1, -1, -1):
                    v[i] = -sum((midpoint(ell[k][i])*v[k]
                                  for k in range(i+1, j+1)), F(0))
                form = sum((Box(v[i])*h[i][k]*Box(v[k])
                            for i in range(degree) for k in range(degree)), Box(0))
                data['witness'] = {'vector': [str(q) for q in v], 'form': form.record()}
                data['status'] = 'CLOSED_DISK_ZERO' if form.hi < 0 else 'INCONCLUSIVE'
                data['failures'].append('strict_positive_LDL_pivot_'+str(j))
                break
            for i in range(j+1, degree):
                ell[i][j] = (h[i][j]-sum((ell[i][k]*pivots[k]*ell[j][k]
                                          for k in range(j)), Box(0)))/pivot
        else:
            data['status'] = 'CLOSED_DISK_ZERO_FREE'
        data['lower_factor'] = [[v.record() for v in row] for row in ell]
        data['minimum_pivot_lower_dyadic'] = str(min(v.lo for v in pivots))
        data['required_pivot_lower'] = '0 (strictly exceeded by every pivot)'
        if data['status'] == 'CLOSED_DISK_ZERO_FREE':
            gate('all_19_pivot_lower_bounds_above_67_over_100',
                 len(pivots) == 19 and all(100*v.lo > 67*S for v in pivots))
        data['minimum_pivot_lower_exact'] = str(F(min(v.lo for v in pivots), S))
        save()
    except Exception as exc:
        data['exception'] = repr(exc)
        if data['status'] != 'INCONCLUSIVE':
            data['status'] = 'INCONCLUSIVE'
        save()
        raise
    print(json.dumps({'status': data['status'], 'N': data['natural_index'],
                      'support_count': data['support_count'], 'degree': data['degree'],
                      'pivots_completed': len(data['pivots']),
                      'minimum_pivot_lower_display': min(float(F(int(p['lo']), S))
                                                         for p in data['pivots']),
                      'required_pivot_lower': '>0 for all',
                      'certified_common_lower_bound': '67/100' if data['status'] == 'CLOSED_DISK_ZERO_FREE' else None,
                      'failures': data['failures'], 'certificate': str(OUT),
                      'seconds': data['elapsed_seconds']}, indent=2))


if __name__ == '__main__':
    main()
