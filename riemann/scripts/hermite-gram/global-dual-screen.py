#!/usr/bin/env python2
"""Numerical discovery only; NEVER a rigorous coefficient certificate.

Uses the existing Anaconda Python 2 sympy.mpmath, without installation.
Full coefficients, sample values and convergence diagnostics go to JSON.
"""
from __future__ import print_function
from sympy import mpmath as mp
import os
import json
import time
import sys

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'global-dual-screen.json')
mp.mp.dps = 250
MAX_N = 256


def text(x):
    return mp.nstr(x, 245)


def coefficients():
    # Tanh-sinh on [0,4], reusing each preceding rule. Error estimates
    # from successive meshes are diagnostics, not interval remainders.
    rule = mp.calculus.quadrature.TanhSinh(mp.mp)
    total = [mp.mpf(0) for _ in range(MAX_N + 1)]
    previous = None
    results = []
    for degree in range(1, 11):
        if degree > 1:
            total = [s/2 for s in total]
        nodes = rule.calc_nodes(degree, mp.mp.prec)
        step = mp.mpf(2)**(-degree)
        for x, weight in nodes:
            u = 2*(x+1)
            eu = mp.exp(u/2)
            e2 = eu**4
            q = mp.exp(-mp.pi*e2)
            kernel = mp.mpf(0)
            for k in range(1, 25):
                kernel += 2*(2*mp.pi**2*k**4*eu**9-3*mp.pi*k**2*eu**5)*q**(k*k)
            term = 2*weight*step*mp.exp(-u*u/4)*kernel
            power = mp.mpf(1)
            u2 = u*u
            for n in range(MAX_N + 1):
                total[n] += term*power
                power *= u2
        if degree >= 9:
            # Factor 2 is full-line evenness; factor 2 above is
            # the [-1,1] to [0,4] Jacobian.
            b = [2*total[n]/(2**(2*n)*mp.factorial(2*n)) for n in range(MAX_N + 1)]
            results.append(b)
        print('quadrature degree', degree, 'new nodes', len(nodes))
        sys.stdout.flush()
    return results


def evaluate(b, t):
    # Complete sum, all three derivatives via H_j'=2j H_(j-1).
    hs = [mp.mpf(1), 2*t]
    for j in range(1, 2*MAX_N):
        hs.append(2*t*hs[-1]-2*j*hs[-2])
    p, dp, ddp = mp.mpf(0), mp.mpf(0), mp.mpf(0)
    answer = {}
    for n in range(MAX_N + 1):
        c = (-1)**n*b[n]
        j = 2*n
        p += c*hs[j]
        if j:
            dp += c*2*j*hs[j-1]
            ddp += c*4*j*(j-1)*hs[j-2]
        if n in (64, 128, 256):
            d = dp*dp-p*ddp
            norm = abs(dp*dp)+abs(p*ddp)
            answer[n] = (d, norm, p, dp, ddp)
    return answer


def main():
    start = time.time()
    if '--resample' in sys.argv:
        with open(OUT) as f:
            old = json.load(f)
        meshes = [[mp.mpf(v) for v in mesh] for mesh in old['coefficients']]
    else:
        meshes = coefficients()
    # An evaluation functional is nonnegative on every real square,
    # hence on every allowed square, without a numerical PSD test.
    rows = []
    negative = []
    minima = dict((n, (mp.inf, None)) for n in (64,128,256))
    for i in range(801):
        t = mp.mpf(i)/4
        low, high = [evaluate(b,t) for b in meshes]
        for n in (64,128,256):
            d,norm,p,dp,ddp = high[n]
            ratio = d/norm if norm else mp.mpf(0)
            agreement = abs(d-low[n][0])/norm if norm else mp.inf
            row = dict(N=n, t=str(t), D=text(d), cancellation_normalizer=text(norm),
                       normalized_D=text(ratio), mesh_disagreement=text(agreement),
                       P=text(p), derivative=text(dp), second_derivative=text(ddp))
            rows.append(row)
            if ratio < minima[n][0]:
                minima[n] = (ratio, str(t))
            if d < 0:
                negative.append(row)
    result = dict(status='NUMERICAL_PREVIEW_ONLY', precision_decimal=250,
                  cutoffs=[64,128,256], theta_terms=24, interval=[0,4],
                  quadrature_degrees=[9,10],
                  sample_grid=dict(start='0',end='200',step='1/4',point_count=801),
                  coefficients=[[text(b) for b in mesh] for mesh in meshes],
                  max_coefficient_relative_mesh_disagreement=text(max(
                      abs(x-y)/abs(y) for x,y in zip(*meshes))),
                  samples=rows, negative_samples=negative,
                  minima=dict((str(n),dict(value=text(v[0]), t=v[1])) for n,v in minima.items()),
                  certified_negative_pairings=0,
                  failures=['No rigorous quadrature enclosure or omitted-tail certificate.',
                            'Real evaluations screen a subclass of the full dual cone only.'],
                  required_threshold='Rigorous full pairing upper bound <0; every allowed square nonnegative.',
                  elapsed_seconds=time.time()-start)
    selected = {}
    for n, t in [(64, '40.75'), (128, '67.75'), (256, '111.75')]:
        selected[str(n)] = next(row for row in rows if row['N'] == n and row['t'] == t)
    result['selected_witnesses'] = selected
    result['software'] = dict(python=sys.version, mpmath=mp.__version__,
        note='Existing sympy.mpmath under Anaconda Python 2; no packages installed.')
    with open(OUT,'w') as f:
        json.dump(result,f,indent=2)
        f.write('\n')
    print('status:',result['status'])
    print('normalized minima:',dict((str(n), (mp.nstr(v[0],12),v[1])) for n,v in minima.items()))
    print('negative samples:',len(negative),'certified:',0)
    print('max coefficient mesh disagreement:',mp.nstr(mp.mpf(result['max_coefficient_relative_mesh_disagreement']),12))
    print('required:',result['required_threshold'])
    print('failures:',result['failures'])
    print('full diagnostic:',OUT)


if __name__ == '__main__':
    main()
