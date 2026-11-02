"""Continuum diagnostic for step 42; not a certificate or finite cone test."""
import json
from pathlib import Path
import math

d, U, r = 5/4, 121/64, 9/20
y = 1/20
rows = []
for parameter in (1/12, 1/10, 1/8, 1/7, 1/6, 1/5):
    u = -(1-parameter**2)/(1+parameter**2)+2j*parameter/(1+parameter**2)
    a, x = -d+1j*y, -d
    count = 4096
    F = sum(math.log(abs((x-(j+.5)/count*u)/(a-(j+.5)/count*u)
                        *(U*u-(j+.5)/count*a)/(U*u-(j+.5)/count*x)))
            for j in range(count))/count
    K = (10/27)*(2*r*math.log(r)
        -(r-y)*math.log(r-y)-(r+y)*math.log(r+y))
    beta = K+3/5*y*y
    rows.append(dict(chart_parameter=str(parameter), u=str(u), F=str(F),
                     beta=str(beta), correction_rate=str(F+beta+1/200)))
report = dict(status="FLOATING CONTINUUM DIAGNOSTIC ONLY", y=str(y),
              rows=rows, required_correction_rate="greater than 1/100",
              failures=[], execution_history=["Initial mpmath import failed; replaced by standard-library midpoint diagnostic"],
              limitations=["No roundoff or integration enclosure", "Asymptotic weight and projection bounds still require proof"])
out = Path(__file__).with_suffix('.json')
out.write_text(json.dumps(report, indent=2)+'\n')
for row in rows:
    print('chart', row['chart_parameter'], 'rate', row['correction_rate'], 'required > 0.01')
print('Failures:', report['failures'], '; full diagnostic:', out)
