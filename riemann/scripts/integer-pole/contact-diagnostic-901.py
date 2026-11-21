#!/usr/bin/env python3
"""Finite-product floating diagnostic only; no rigorous sign certificate."""
import cmath
import itertools
import json
from pathlib import Path

OUT = Path(__file__).with_suffix('.json')
N = 48
rates = [1, 3+1j, 3-1j] + [2**n for n in range(1, N+1)]
residues = []
for i, r in enumerate(rates):
    a = r
    for j, q in enumerate(rates):
        if i != j:
            a /= 1-r/q
    residues.append(a)

def det3(a, b, c):
    return (a[0]*(b[1]*c[2]-b[2]*c[1])
            -a[1]*(b[0]*c[2]-b[2]*c[0])
            +a[2]*(b[0]*c[1]-b[1]*c[0]))

def evaluate(x):
    q = [sum(a*(-r)**j*cmath.exp(-(r-1)*x)
             for r, a in zip(rates, residues)).real for j in range(6)]
    d2 = q[1]**2-q[0]*q[2]
    d3 = -det3(q[:3], q[1:4], q[2:5])
    # q entries here are exp(x)*p^(j), not jets of exp(x)*p.
    dp3 = -det3(q[:3], q[1:4], q[3:6])
    return dict(x=x, exp_x_p=q[0], D2_over_p2=d2/q[0]**2,
                D3_over_p3=d3/q[0]**3,
                D3prime_over_p3=dp3/q[0]**3)

rows = [evaluate(k/32) for k in range(1, 513)]
crossings = [(a['x'],b['x']) for a,b in zip(rows, rows[1:])
             if a['D3_over_p3']*b['D3_over_p3']<0]
report = dict(status='NONRIGOROUS_DIAGNOSTIC', finite_product_N=N,
              crossings=crossings, rows=rows)
OUT.write_text(json.dumps(report, indent=2)+'\n')
print('Diagnostic only; D3 sign-change brackets:',crossings)
print('Sampled D2 minimum:', min(r['D2_over_p2'] for r in rows))
print('Full output:',OUT)
