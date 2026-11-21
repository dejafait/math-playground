#!/usr/bin/env python3
"""Exact finite cross-checks for C028k, not a substitute for its general proof."""
from fractions import Fraction as Q
from pathlib import Path
import json

OUT = Path(__file__).with_name('feasibility-1596.json')
checks = []
def check(label, actual, required):
    checks.append(dict(label=label, actual=str(actual), required=str(required),
                       passed=actual == required))

def polynomial(d, lam, c, r, m):
    # Ascending coefficients, directly from the imported monic recurrence.
    prev, cur = [Q(0)], [Q(1)]
    for n in range(d):
        diagonal = m-(n+lam)*c
        beta = r*n*(n+2*lam-1)
        nxt = [Q(0)]*(len(cur)+1)
        for j, value in enumerate(cur):
            nxt[j] -= diagonal*value
            nxt[j+1] += value
        if n:
            for j, value in enumerate(prev):
                nxt[j] -= beta*value
        prev, cur = cur, nxt
    return cur

for d in (5, 6, 9, 17):
    for lam in (Q(1, 5), Q(1), Q(7, 2)):
        for c in (Q(-2), Q(0), Q(3, 2)):
            r, m = c*c/4+Q(1, 7), Q(2, 9)
            p = polynomial(d, lam, c, r, m)
            e1, e2, e3 = -p[d-1], p[d-2], -p[d-3]
            p2, p3 = e1*e1-2*e2, e1**3-3*e1*e2+3*e3
            mean = e1/d
            central2 = p2-d*mean**2
            central3 = p3-3*mean*p2+2*d*mean**3
            prefix = f'd={d},lambda={lam},c={c}'
            check(prefix+'/mean', mean, m-c*(lam+Q(d-1, 2)))
            check(prefix+'/central2', central2,
                  d*(d-1)*(c*c*Q(d+1, 12)+Q(2, 3)*r*(d+3*lam-2)))
            check(prefix+'/central3', central3,
                  -c*r*Q(d*(d-1)*(d-2), 2)*(d+2*lam-1))
            check(prefix+'/edge_sum',
                  sum((Q(n)*(n+2*lam-1)*(d-2*n) for n in range(1,d)), Q(0)),
                  -Q(d*(d-1)*(d-2), 6)*(d+2*lam-1))
    k0 = Q(d+1, 4*(d-2))
    V0 = Q(d+1, 12)+Q(2, 3)*k0*(d-2)
    maximum = Q((d-1)**2, (d+1)*(d-2)**2)
    check(f'd={d}/supremum_identity', k0*k0*(d-1)**2/(4*V0**3), maximum)
    check(f'd={d}/ceiling_bound', maximum <= Q(16, 9*(d+1)), True)
    for k in (Q(3, 10), Q(1), Q(5)):
        for lam in (Q(1, 5), Q(1), Q(7, 2)):
            V = Q(d+1, 12)+Q(2, 3)*k*(d+3*lam-2)
            numerator = 4*V-6*k*(d+2*lam-1)
            check(f'd={d},k={k},lambda={lam}/lambda_derivative', numerator,
                  (d+1-2*k*(5*d+6*lam-1))/3)
            check(f'd={d},k={k},lambda={lam}/derivative_negative', numerator < 0, True)

failed = [c for c in checks if not c['passed']]
report = dict(result='PASS' if not failed else 'FAIL',
              purpose='Exact finite recurrence/trace and optimization-algebra cross-checks; general proof in C028k.',
              degrees=[5,6,9,17], checks=checks, failures=failed,
              actual_bound='rho < (d-1)^2/((d+1)*(d-2)^2) <= 16/(9*(d+1))',
              required_condition='rho=tau^2/v^3 is fixed and strictly positive; unbounded feasibility would require ceilings bounded below by rho',
              limitations='Finite rational checks do not prove the all-degree inequalities, measure theorem, or sufficiency; read C028k in full.')
OUT.write_text(json.dumps(report, indent=2)+'\n')
print(f"{report['result']}: {len(checks)} exact checks; failures={len(failed)}")
print('Actual ceiling: rho < (d-1)^2/((d+1)*(d-2)^2) <= 16/(9*(d+1)); required rho=tau^2/v^3>0 fixed.')
print(f'Certificate: {OUT}')
if failed:
    for entry in failed:
        print(entry)
    raise SystemExit(1)
