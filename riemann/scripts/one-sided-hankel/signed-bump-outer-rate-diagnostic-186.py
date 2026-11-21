"""Nonrigorous phase diagnostic; no fixed-bump integral is approximated.

Reuses the audited L716 moment enclosures to evaluate the limiting
phase, but uses binary64 Simpson quadrature and midpoint moments. It cannot
certify signed rates or a lower bound for the outer integral.
"""
from pathlib import Path
import hashlib
import json
import cmath
import math

base = Path(__file__).parent
source = base / 'resolvent-tail-certificate-181.json'
data = json.loads(source.read_text())
def rat(a):
    return a['numerator'] / a['denominator']
moments = [sum(rat(a) for a in row['moment_enclosure'])/2
           for row in data['moment_rows']]
U, A, d, c0 = 121/64, 27/10, 5/4, 1/8
u = complex(3,4)/10
omega = A*(math.log(9/5)-4/5+121/100*math.log(201/121))
def quad(f, count=2000):
    return (f(0)+f(1)+sum((4 if j%2 else 2)*f(j/count)
                          for j in range(1,count)))/(3*count)
C = 1+math.log(U)+quad(lambda t: cmath.log((d+u*t)/(U*u+d*t)))
WP = quad(lambda t: cmath.log((d+u*t)*(U*u+(d+c0)*t)
                             /((U*u+d*t)*(d+u*t+c0))))
def pack(z):
    return {'real':z.real,'imag':z.imag}
rows = []
for j in [-1,0,1]:
    v = omega+j/3000
    z = cmath.exp(-u*v/A)
    f = -sum(m*z**k/k for k,m in enumerate(moments,1))
    y = sum(m*z**k for k,m in enumerate(moments,1))
    phase = C-d*v/A+f
    deriv = (-d+u*y)/A
    rows.append({'v':v,'phase':pack(phase),
                 'derivative':pack(deriv),
                 'phase_series_tail_bound':abs(z)**81/(81*(1-abs(z))),
                 'derivative_series_tail_bound':abs(u)/A*abs(z)**81/(1-abs(z)),
                 'residue_rate_at_endpoint_v':WP.real+c0*v/A})
result = {'purpose':__doc__,'rigorous':False,
          'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
          'moment_source':str(source),
          'moment_source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
          'prefactor_rate':pack(C),'residue_product_rate':pack(WP),
          'rows':rows,'required':'Proved signed rate comparison of R_n=P_n+K_n, not a pointwise phase rate.',
          'failures':['No signed outer integral computed; fixed chi has no supplied endpoint law.',
                      'Quadrature and midpoint arithmetic are diagnostic only.']}
path = Path(__file__).with_suffix('.json')
path.write_text(json.dumps(result,indent=2)+'\n')
for row in rows:
    print('v='+str(row['v'])+': kernel rate='+str(row['phase']['real'])
          +'; derivative='+str(row['derivative'])
          +'; residue endpoint rate='+str(row['residue_rate_at_endpoint_v']))
print('Required:',result['required'])
print('Failures:',result['failures'])
print('Diagnostic only; full artifact:',path)
