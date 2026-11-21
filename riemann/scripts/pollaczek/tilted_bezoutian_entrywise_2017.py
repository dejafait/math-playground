#!/usr/bin/env python3
"""One approved fixed-input N=6 entrywise interval Leibniz pass.

No determinant-polynomial expansion, pivot division or precision fallback.
Run from riemann: python3 scripts/pollaczek/tilted_bezoutian_entrywise_2017.py
"""
from fractions import Fraction as F
from itertools import permutations
from math import factorial
from pathlib import Path
import hashlib
import json

import tilted_bezoutian_n6_2014 as alg

base = alg.base
ROOT = Path(__file__).parent
PINNED = {
    'tilted-bezoutian-n6-2014.json': '6870f303d2fa8bd6ec5bd9fcde2a197d6c9987f98b6bccf048a378f3ccdedd47',
    'tilted-boundary-metric-2010.json': '361e31b72ad348b17f6c2ac785c20f5ab73e27796025bd724af208543e0feaf7',
    'tilted_bezoutian_n6_2014.py': 'af87c4ec40ea6a93ddb0d9fe3915dd6c2fa403d4729e48639c1b94247ac42709',
    'tilted_boundary_metric_2010.py': '21cc4fb70b084fde19c62d74a7edb04a2bcdb38fe1a376ea5e7de6d3edbb58fc',
}


def decode_matrix(m):
    return [[alg.decode(p) for p in row] for row in m]


def readable(iv):
    """Short exact outward bounds, for inspection rather than arithmetic."""
    magnitude = max(abs(iv[0]), abs(iv[1]))
    if not magnitude:
        return {'power_of_ten': 0, 'scaled_interval': base.interval_json(iv)}
    exponent = len(str(magnitude.numerator))-len(str(magnitude.denominator))
    unit = F(10)**exponent
    while magnitude < unit:
        exponent, unit = exponent-1, unit/10
    while magnitude >= 10*unit:
        exponent, unit = exponent+1, unit*10
    outer = base.outward_grid((iv[0]/unit, iv[1]/unit), 6)
    assert outer[0]*unit <= iv[0] <= iv[1] <= outer[1]*unit
    return {'power_of_ten': exponent, 'scaled_interval': base.interval_json(outer)}


def main():
    checks = {}

    def check(name, condition):
        checks[name] = bool(condition)

    hashes = {name: hashlib.sha256((ROOT/name).read_bytes()).hexdigest()
              for name in PINNED}
    for name in PINNED:
        check('pinned_'+name, hashes[name] == PINNED[name])
    # Changed inputs cannot silently receive this fixed-input assessment.
    if not all(checks.values()):
        raise RuntimeError('Pinned input changed; no calculation authorized')
    saved = json.loads((ROOT/'tilted-bezoutian-n6-2014.json').read_text())
    source = json.loads((ROOT/'tilted-boundary-metric-2010.json').read_text())
    pi_iv = tuple(F(source['pi_interval'][k]) for k in ('lower', 'upper'))
    sqrt_iv = tuple(F(source['sqrt2_interval'][k]) for k in ('lower', 'upper'))
    check('unchanged_pi_interval', saved['pi_interval'] == source['pi_interval'])
    check('unchanged_sqrt2_interval', saved['sqrt2_interval'] == source['sqrt2_interval'])
    check('fixed_input_widths', pi_iv[1]-pi_iv[0] == sqrt_iv[1]-sqrt_iv[0] == F(1,10**60))
    a = list(map(alg.decode, source['a_over_S_polynomials']))
    check('all_a_coefficients_match', a == list(map(alg.decode, saved['a_over_S_polynomials'])))
    check('actual_degree_six', base.peval(a[6], pi_iv, sqrt_iv)[1] < 0)

    # Reconstruct p_k, the monomial kernel and the exact basis conversion.
    p = [[F(1)]]
    for k in range(6):
        t = [F(0)]+p[k]
        if k:
            for j,c in enumerate(p[k-1]):
                t[j] -= F(2*k+1,2)*c
        p.append([c/F(k+1) for c in t])
    check('basis_matches', p == [list(map(F,row)) for row in saved['basis_p_0_to_6']])
    check('basis_degree_graded', all(p[k][k] == F(1,factorial(k)) for k in range(7)))
    b = [alg.add(*(alg.scale(a[k],p[k][i]) for k in range(i,7))) for i in range(7)]
    d = [alg.scale(b[i+1],i+1) for i in range(6)]+[[]]
    check('all_U_coefficients_match', b == list(map(alg.decode,saved['U_monomial_coefficients'])))
    check('all_derivative_coefficients_match', d == list(map(alg.decode,saved['derivative_coefficients'])))
    numerator = [[alg.add(alg.mul(b[i],d[j]),alg.scale(alg.mul(d[i],b[j]),-1))
                  for j in range(7)] for i in range(7)]
    kernel = [[[] for _ in range(6)] for _ in range(6)]
    for j in range(6):
        for i in range(j+1,7):
            for ell in range(i-j):
                kernel[i-1-ell][j+ell] = alg.add(kernel[i-1-ell][j+ell], numerator[i][j])
    check('all_kernel_coefficients_match', kernel == decode_matrix(saved['B_monomial']))
    # Verify the division-free numerator identity in every coefficient.
    reconstructed = [[[] for _ in range(7)] for _ in range(7)]
    for i in range(6):
        for j in range(6):
            reconstructed[i+1][j] = alg.add(reconstructed[i+1][j],kernel[i][j])
            reconstructed[i][j+1] = alg.add(reconstructed[i][j+1],alg.scale(kernel[i][j],-1))
    check('all_49_kernel_identity_coefficients', reconstructed == numerator)
    r = []
    for i in range(6):
        rem = [F(int(i==j)) for j in range(6)]
        row = [F(0)]*6
        for k in range(5,-1,-1):
            row[k] = rem[k]/p[k][k]
            for j,c in enumerate(p[k]):
                rem[j] -= row[k]*c
        check('conversion_remainder_'+str(i), not any(rem))
        r.append(row)
    rd = [[alg.rat([c]) for c in reversed(row)] for row in r]
    matrix = alg.matmul(alg.matmul(alg.transpose(rd),kernel),rd)
    check('all_36_stored_B_entries_match_construction', matrix == decode_matrix(saved['B_descending']))
    check('all_36_B_symmetry_entries', matrix == alg.transpose(matrix))

    # Check the evaluation orientation after clearing only the proven A_6.
    ct = [[[] for _ in range(6)] for _ in range(6)]
    for i in range(5):
        ct[i][i+1] = alg.scale(a[6],F(11-2*i,2))
        ct[i+1][i] = alg.scale(a[6],5-i)
    for j in range(6):
        ct[0][j] = alg.add(ct[0][j],alg.scale(a[5-j],-6))
    check('cleared_comrade_matches', ct == decode_matrix(saved['Ctilde']))
    check('all_36_cleared_left_metric_entries',
          alg.matmul(alg.transpose(ct),matrix) == alg.matmul(matrix,ct))
    d2 = list(map(F,source['D_squared']))
    check('positive_scaling_and_recurrence',
          d2 == list(map(F,saved['D_squared']))
          and d2 == [F(693,256),F(315,128),F(35,16),F(15,8),F(3,2),F(1)]
          and all(c>0 for c in d2)
          and all(F(11-2*i,2)*d2[i+1] == (5-i)*d2[i] for i in range(5)))
    if not all(checks.values()):
        raise RuntimeError('Construction check failed before interval pass')

    # Enclose entries first; never form an expanded determinant polynomial.
    entries = [[base.peval(poly,pi_iv,sqrt_iv) for poly in row] for row in matrix]
    check('all_entry_intervals_ordered', all(lo<=hi for row in entries for lo,hi in row))
    check('all_entry_intervals_symmetric', entries == alg.transpose(entries))
    minors = []
    for n in range(1,7):
        total = F(0),F(0)
        records = []
        for perm in permutations(range(n)):
            inversions = sum(perm[i]>perm[j] for i in range(n) for j in range(i+1,n))
            sign = (-1)**inversions
            product = F(1),F(1)
            for i,j in enumerate(perm):
                product = base.imul(product,entries[i][j])
            signed = base.iscale(product,sign)
            total = base.iadd(total,signed)
            records.append({'permutation_zero_based':list(perm), 'inversions':inversions,
                            'sign':sign, 'product_interval':base.interval_json(product),
                            'signed_product_interval':base.interval_json(signed)})
        check('complete_permutation_count_'+str(n), len(records) == factorial(n))
        sign = 1 if total[0]>0 else -1 if total[1]<0 else 0
        short = readable(total)
        minors.append({'minor':n, 'permutations':records,
                       'interval':base.interval_json(total), 'sign':sign,
                       'readable_outer_enclosure':short})
        print('Delta_'+str(n), 'sign:',sign, 'outer enclosure:',short, flush=True)
    failures = [name for name,value in checks.items() if not value]
    signs = [m['sign'] for m in minors]
    unresolved = [m['minor'] for m in minors if not m['sign']]
    complete = not failures and not unresolved
    seq = [1]+signs
    neg = sum(seq[i]!=seq[i+1] for i in range(6)) if complete else None
    inertia = {'positive':6-neg,'negative':neg,'zero':0} if complete else None
    result = ('CERTIFIED_N6_INDEX_AT_MOST_ONE' if neg<=1 else 'CERTIFIED_N6_INDEX_AT_LEAST_TWO') if complete else 'INCONCLUSIVE'
    report = {
        'target':'Fixed-input entrywise Leibniz test of C029o full T_6 Bezoutian',
        'reproduction':'python3 scripts/pollaczek/tilted_bezoutian_entrywise_2017.py',
        'method':'Exact Fraction entrywise Horner followed by literal signed permutation sums; one pass',
        'input_sha256':hashes, 'required_sha256':PINNED,
        'input_containment':'C029n audited Machin/isqrt proof; unchanged 60-decimal grid',
        'pi_interval':base.interval_json(pi_iv),'sqrt2_interval':base.interval_json(sqrt_iv),
        'B_descending':alg.matrix_json(matrix),
        'entry_intervals':[[base.interval_json(iv) for iv in row] for row in entries],
        'entry_readable_enclosures':[[readable(iv) for iv in row] for row in entries],
        'D_squared':list(map(str,d2)),
        'scaled_orientation':'G=D*B*D, A=D^-1*C*D; A^t*G-G*A=D*(C^t*B-B*C)*D=0',
        'minors':minors,'leading_determinant_signs':signs,
        'unresolved_determinants':unresolved,'actual_inertia':inertia,
        'required':'All six minor signs nonzero; desired negative index<=1 at N=6 only',
        'threshold_pass':neg<=1 if complete else None,
        'checks':checks,'failures':failures,'result':result,
        'scope':'Finite reproduction only; no eventual bound, compact convergence or RH conclusion',
    }
    out = ROOT/'tilted-bezoutian-entrywise-2017.json'
    out.write_text(json.dumps(report,indent=2)+'\n')
    print('Result:',result,'; inertia:',inertia,'; required:',report['required'])
    print('Unresolved:',unresolved,'; failures:',failures)
    print('Certificate:',out.relative_to(Path.cwd()))
    if failures:
        raise SystemExit(1)


if __name__=='__main__':
    main()
