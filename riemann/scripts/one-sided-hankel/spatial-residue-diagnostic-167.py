"""Nonrigorous rate screen for the full-resolvent test; never a certificate."""
import json
import math
from pathlib import Path

d, R, U, A = 1.25, 1.375, 121/64, 2.7
omega = A*(math.log(9/5)-4/5+121/100*math.log(201/121))

def phi(x, c):
    D = d+c
    terms = []
    for j in range(129):
        t = j/128
        ratio = ((d*d+t*t/4)*(t*t*D*D+(U/2-t*x)**2)
                 / ((d*d*t*t+U*U/4)*(D*D+(t/2-x)**2)))
        weight = 1 if j in (0, 128) else 4 if j % 2 else 2
        terms.append(weight*math.log(ratio)/2)
    return sum(terms)/(3*128)

rows = []
for radius in (1, 65/64):
    samples = []
    for j in range(401):
        x = -0.8+j/500
        c = math.sqrt((R/radius)**2-x*x)-d
        samples.append(dict(x=x, c=c, rate=phi(x,c)+c*omega/A))
    rows.append(dict(radius=radius, maximum_sample=max(samples,key=lambda a:a['rate']),
                     samples=samples))
result = dict(kind='DIAGNOSTIC ONLY: floating quadrature and samples, no enclosures',
              omega=omega, endpoint_rate=phi(-0.45,0), circles=rows,
              thresholds=dict(unit_endpoint_required=phi(-0.45,0),
                              larger_radius_must_exceed_complete_unit_upper=True),
              unresolved=['Complete signed contour and residue pairing',
                          'Bump cancellation', 'Uniform unit-disk upper bound',
                          'Rigorous rate enclosures and angular extension'])
path=Path(__file__).with_suffix('.json')
path.write_text(json.dumps(result,indent=2)+'\n')
for row in rows:
    print(f"DIAGNOSTIC radius={row['radius']}: {row['maximum_sample']}")
print(f"DIAGNOSTIC endpoint rate={result['endpoint_rate']}; not a proof")
print(f"Unresolved obligations: {len(result['unresolved'])}; evidence: {path}")
