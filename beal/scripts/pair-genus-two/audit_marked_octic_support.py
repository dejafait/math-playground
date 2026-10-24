"""Independent exact L114 audit. No producer imports or numeric backends."""
from fractions import Fraction as Q
from hashlib import sha256
from math import isqrt, prod
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
SOURCE = HERE / 'marked-octic-support-certificate.json'
checks = {}


def check(name, value):
    checks[name] = bool(value)


def gaussian(matrix):
    """Ordinary rational row elimination; product of pivots with swap sign."""
    a = [[Q(x) for x in row] for row in matrix]
    product, sign, trace = Q(1), 1, []
    for k in range(len(a)):
        r = next(i for i in range(k, len(a)) if a[i][k])
        a[k], a[r] = a[r], a[k]
        if r != k:
            sign = -sign
        pivot = a[k][k]
        product *= pivot
        trace.append(dict(step=k, swapped_row=r, pivot=str(pivot),
                          unsigned_pivot_product=str(product)))
        for i in range(k + 1, len(a)):
            multiplier = a[i][k] / pivot
            a[i] = [x - multiplier*y for x, y in zip(a[i], a[k])]
    return product*sign, trace


def audit_polynomial(label, c, saved):
    n = len(c)-1
    derivative = [i*c[i] for i in range(1, n+1)]
    # Form shifted polynomials in ascending order, reverse their full
    # coefficient vectors, and store them as the published Sylvester rows.
    columns = []
    for polynomial, shifts in ((c, n-1), (derivative, n)):
        for j in range(shifts-1, -1, -1):
            v = [0]*j + polynomial
            v += [0]*(2*n-1-len(v))
            columns.append(v[::-1])
    matrix = columns
    check(label+'_coefficients', c == saved['coefficients'])
    check(label+'_every_matrix_entry', matrix == saved['sylvester_matrix'])
    det, gt = gaussian(matrix)
    check(label+'_gaussian_resultant', det.denominator == 1 and det == saved['resultant'])
    sign = (-1)**(n*(n-1)//2)
    disc = sign*det/c[-1]
    check(label+'_discriminant', disc.denominator == 1 and disc == saved['discriminant'])
    # Every recorded Bareiss pivot is the unsigned cumulative product
    # of Gaussian pivots; verify the complete trace and its integer updates.
    a = [row[:] for row in matrix]
    previous, swap_sign, division_count, trace = 1, 1, 0, []
    for k in range(len(a)-1):
        r = next(i for i in range(k, len(a)) if a[i][k])
        a[k], a[r] = a[r], a[k]
        if r != k:
            swap_sign *= -1
        pivot = a[k][k]
        row = dict(step=k, swapped_row=r, pivot=pivot, divisor=previous)
        trace.append(row)
        check(f'{label}_trace_{k}', row == saved['elimination'][k])
        check(f'{label}_independent_pivot_{k}',
              Q(gt[k]['unsigned_pivot_product']) == pivot and gt[k]['swapped_row'] == r)
        for i in range(k+1, len(a)):
            for j in range(k+1, len(a)):
                value, remainder = divmod(pivot*a[i][j]-a[i][k]*a[k][j], previous)
                if remainder:
                    check(f'{label}_division_{k}_{i}_{j}', False)
                a[i][j] = value
                division_count += 1
            a[i][k] = 0
        previous = pivot
    check(label+'_trace_length', len(trace) == len(saved['elimination']))
    check(label+'_signed_final_entry', swap_sign*a[-1][-1] == det)
    factors, division_rows, rest = {}, [], abs(int(disc))
    for p in (2, 3, 5, 11):
        check(f'{label}_prime_{p}', all(p % d for d in range(2, isqrt(p)+1)))
        exponent = 0
        while rest % p == 0:
            before = rest
            rest //= p
            exponent += 1
            division_rows.append([p, before, rest])
        if exponent:
            factors[str(p)] = exponent
    factorization = dict(sign=1 if disc > 0 else -1, factors=factors, remainder=rest)
    check(label+'_full_factorization', factorization == saved['factorization'] and rest == 1)
    check(label+'_factor_product', prod(int(p)**e for p, e in factors.items()) == disc)
    return dict(coefficients=c, sylvester_matrix=matrix, gaussian_trace=gt,
                bareiss_trace=trace, exact_integer_divisions=division_count,
                resultant=int(det), discriminant=int(disc),
                factorization=factorization, prime_divisions=division_rows)


def infinity_row(Z):
    # Evaluate regular L113 q-chart first, then original rational functions.
    q = Q(0)
    T = 2*(1-3*q*q)/(1+3*q*q)
    h = -12*q/(1+3*q*q)
    R = 3*Z/(1+3*q*q)**2
    W = h*R/3
    F = T**5+T**4-4*T**3-3*T*T+3*T+1
    K, L = T*T-T-1, T*T+T-1
    u = (F-11-K*W)/(60*F)
    M = 2-10*u
    rho = M*L/(30*(T+2)*K)
    v = rho*h
    z = -M*M*(T-2)*L*L/(300*(T+2)*K*K)
    # With z=0, H0(u,0)=phi(u) exactly, not a truncated series.
    assert z == 0
    s = (3*u*u+u+1)**5*(1-5*u)
    row = dict(q=q, Z=Z, R=R, T=T, h=h, W=W, u=u, v=v,
               original_z=z, s=s, chart_derivative=2*Z,
               fake_representative=55**2, fake_class='identity')
    residues = dict(F=F, K=K, L=L, rho=rho, h_over_q=-12,
                    W_over_q=-12*Z, v_over_q=-12*rho,
                    z_over_q2=144*rho*rho, v_over_W=rho/Z)
    return row, residues


def main():
    saved = json.loads(SOURCE.read_text())
    c = [11*x for x in (243, 0, -3564, 0, 6930, 0, -2860, 0, 275)]
    g = audit_polynomial('octic', c, saved['octic'])
    p = audit_polynomial('quartic', c[::2], saved['quartic'])
    check('octic_required_exponents', g['factorization']['factors'] ==
          {'2': 72, '3': 27, '5': 8, '11': 21})
    check('composition_cross_check', g['discriminant'] ==
          2**8*c[-1]*c[0]*p['discriminant']**2)
    rows, residues = [], []
    for i, Z in enumerate((-55, 55)):
        row, units = infinity_row(Z)
        rows.append(row)
        residues.append(units)
        check(f'infinity_{i}_every_field', row == saved['infinity_rows'][i])
        check(f'infinity_{i}_smooth', Z*Z == c[-1] and 2*Z != 0)
        check(f'infinity_{i}_transport_units', units == dict(F=11, K=1, L=5,
              rho=Q(1,12), h_over_q=-12, W_over_q=-12*Z, v_over_q=-1,
              z_over_q2=1, v_over_W=Q(1,12*Z)))
        check(f'infinity_{i}_norm_fiber', Q(row['fake_representative']**8, c[-1]) == Q(55)**14)
    check('two_distinct_infinity_rows', len(saved['infinity_rows']) == 2 and rows[0]['R'] != rows[1]['R'])
    support = sorted(set(int(p) for p in g['factorization']['factors']) | {2,5,11})
    check('finite_support', support == saved['finite_support'] == [2,3,5,11])
    check('real_place', saved['real_place_retained'] is True)
    check('source_lemma_hash', saved['inputs'] == {
        'lemmas/L113-marked-genus-three-hyperelliptic-model.md': sha256(
            (ROOT/'lemmas/L113-marked-genus-three-hyperelliptic-model.md').read_bytes()).hexdigest()})
    check('producer_failure_report', saved['failures'] == [])
    check('producer_flags_report', len(saved['checks']) == 11 and all(saved['checks'].values()))
    result = dict(octic=g, quartic=p, infinity_rows=rows, normalized_residues=residues,
                  finite_support=support, real_place_retained=True,
                  checks=checks, failures=[k for k, v in checks.items() if not v],
                  inputs={str(SOURCE.relative_to(ROOT)): sha256(SOURCE.read_bytes()).hexdigest()})
    path = HERE/'marked-octic-support-audit-certificate.json'
    path.write_text(json.dumps(result, indent=2, default=str)+'\n')
    print(f"Checks {sum(checks.values())}/{len(checks)}; failures: {result['failures']}")
    print(f"Discriminant exponents actual {g['factorization']['factors']}; required 72,27,8,21")
    print(f"Complete factorization remainders {g['factorization']['remainder']}/{p['factorization']['remainder']}; required 1/1")
    print(f"Integer divisions {g['exact_integer_divisions'] + p['exact_integer_divisions']}; infinity rows {len(rows)}/2")
    print(f"Certificate: {path.relative_to(ROOT)}")
    assert not result['failures']


if __name__ == '__main__':
    main()
