"""Finite-precision diagnostic, NOT a rigorous bound or counterexample.

Run from riemann: python3 scripts/paired-subdiagonal/sparse_pair_1231.py
Output: sparse-pair-1231.json in this directory. No external inputs.
The partial fractions and Hankel signs are justified in working1231.
"""
import json
from pathlib import Path
from decimal import Decimal as D, localcontext
from math import factorial


def cmul(z, w):
    return (z[0]*w[0]-z[1]*w[1], z[0]*w[1]+z[1]*w[0])


def cpow(z, k):
    if k < 0:
        norm = z[0]*z[0]+z[1]*z[1]
        return cpow((z[0]/norm, -z[1]/norm), -k)
    ans = (D(1), D(0))
    while k:
        if k % 2:
            ans = cmul(ans, z)
        z = cmul(z,z)
        k //= 2
    return ans


def cis(b):
    # b is exactly 1/4; alternating Taylor sums, rounded Decimal arithmetic.
    co, si = D(1), b
    tc, ts = co, si
    for k in range(1,10000):
        tc *= -b*b/D((2*k-1)*(2*k))
        ts *= -b*b/D((2*k)*(2*k+1))
        nc, ns = co+tc, si+ts
        if nc == co and ns == si:
            return co, si
        co, si = nc, ns
    raise ArithmeticError('trigonometric series did not converge')


def moments(n, delta, b, count):
    # Remove the common positive rate r and the product of all rates.
    # Neither changes beta. The remaining Laplace transform is
    # 1/[s^(n-2) ((s+delta)^2+b^2)], at x=1.
    N = n - 2
    scale = D(factorial(n - 1))
    if delta == 0:
        vals = []
        for v in range(count):
            total = D(0)
            for k in range(10000):
                power = D(1) if k == 0 else (-b*b)**k
                term = power / D(factorial(n + 2*k - 1 - v))
                new = total + term
                if new == total:
                    break
                total = new
            else:
                raise ArithmeticError('series did not converge')
            vals.append(scale * total)
        return vals
    a = []
    denom = delta*delta + b*b
    for k in range(N):
        a.append(((1 if k == 0 else 0)
                  - (2*delta*a[k-1] if k >= 1 else 0)
                  - (a[k-2] if k >= 2 else 0)) / denom)
    vals = []
    eb = cis(b) if b else None
    exponential = (-delta).exp()
    for v in range(count):
        poly = sum((a[N-j] / D(factorial(j-1-v))
                       for j in range(v+1, N+1)), D(0))
        if b:
            tail = exponential*cmul(eb, cpow((-delta,b),v-N))[1]/b
        else:
            p = -delta
            aa = p**(-N)
            bb = -N*p**(-N-1)
            tail = exponential*(p**v*(aa+bb)
                    + (v*p**(v-1)*aa if v else 0))
        vals.append(scale*(poly+tail))
    return vals


def coefficients(n, delta, b):
    d = n//2
    v = moments(n, delta, b, 2*d-1)
    H = [[v[j+k] for k in range(d)] for j in range(d)]
    pivots = []
    for j in range(d):
        pivot = H[j][j]
        if (-1)**j*pivot <= 0:
            raise ArithmeticError(f'wrong signed pivot: n={n}, j={j}')
        pivots.append(pivot)
        for k in range(j+1, d):
            fac = H[k][j]/pivot
            for ell in range(j+1, d):
                H[k][ell] -= fac*H[j][ell]
    return {i: (-pivots[i]/pivots[i-1]).sqrt()
            for i in sorted({1, 2, n//4, n//2-1})}


def run(dps):
    rows = []
    for n in (8, 16, 32, 64):
        for delta in sorted({D(0), *[sign*D(str(c))
                  for sign in (-1, 1)
                  for c in (n/4, n, 4*n, n*n)]}):
            with localcontext() as ctx:
                # Pay explicitly for the e^|delta| cancellation for slow pairs.
                ctx.prec = dps + int(abs(delta))//2 + 4*n
                phase = coefficients(n, delta, D(1)/4)
                real = coefficients(n, delta, D(0))
                for i in phase:
                    # x=1, M=1/16; a=1+max(delta,0), r=1+max(-delta,0).
                    ratio = 16*abs(phase[i]-real[i])
                    rows.append(dict(n=n, i=i, delta=str(delta),
                                     precision=ctx.prec,
                                     beta_b=format(phase[i], '.89E'),
                                     beta_0=format(real[i], '.89E'),
                                     normalized_difference=format(ratio, '.89E')))
    return rows


def main():
    path = Path(__file__).with_name('sparse-pair-1231.json')
    cert = dict(kind='FINITE_PRECISION_DIAGNOSTIC_NOT_PROOF',
                family='m=1, x=1, b=1/4, a=1+max(delta,0), r=1+max(-delta,0)',
                required='An absolute bound for every admissible parameter, or a rigorous divergent admissible sequence.',
                limitations=['Finite n and selected contrasts only.',
                             'Repeated precision is not interval certification.',
                             'A single active pair does not cover heterogeneous active pairs.'],
                setup_failures=['Initial mpmath import unavailable in system Python; implementation replaced by standard-library Decimal. No dependency installed.'],
                failures=[])
    try:
        low = run(420)
        high = run(520)
        with localcontext() as ctx:
            ctx.prec = 100
            reference_errors = [abs(D(r['beta_0'])/D(r['i']*(r['n']-r['i'])).sqrt()-1)
                                for r in high if D(r['delta']) == 0]
        discrepancies = [abs(D(a['normalized_difference'])
                             - D(b['normalized_difference']))
                         for a,b in zip(low,high)]
        cert.update(precisions=[420,520], rows=high,
                    common_rate_reference_maximum_relative_error=str(max(reference_errors)),
                    maximum_precision_discrepancy=str(max(discrepancies)),
                    per_dimension_maxima=[max((r for r in high if r['n']==n),
                            key=lambda r: D(r['normalized_difference']))
                            for n in (8,16,32,64)],
                    global_maximum=max(high, key=lambda r:D(r['normalized_difference'])),
                    checked_points=len(high))
        if max(discrepancies) > D('1e-60'):
            cert['failures'].append('precision discrepancy exceeds diagnostic tolerance 1e-60')
        if max(reference_errors) > D('1e-60'):
            cert['failures'].append('common-rate beta_0 disagrees with sqrt(i*(n-i))')
    except Exception as exc:
        cert['failures'].append(str(exc))
    path.write_text(json.dumps(cert, indent=2)+'\n')
    print('Diagnostic only; full output:', path)
    print('Required:', cert['required'])
    print('Failures:', cert['failures'])
    if 'global_maximum' in cert:
        r=cert['global_maximum']
        print('Actual sampled maximum:', r['normalized_difference'],
              'at n,i,delta =', r['n'],r['i'],r['delta'])
        print('Points:', cert['checked_points'],
              'precision discrepancy:',cert['maximum_precision_discrepancy'])
        print('Precision discrepancy required <= 1e-60 (diagnostic only).')
        print('Common-rate beta_0 relative error:',
              cert['common_rate_reference_maximum_relative_error'],
              '; required <= 1e-60 (diagnostic only).')


if __name__ == '__main__':
    main()
