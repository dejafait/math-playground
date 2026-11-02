"""Floating necessary-crossing screen; no continuous or cone bound."""
import json
import math
from pathlib import Path
import numpy as np

d,U,r=1.25,121/64,.45
c=10*math.pi/27
v=complex(-99,20)/101

def S(w):
    return (1+(1/w-1)*np.log(1-w)).real

def F(z,u):
    a=-d+z
    return (np.log(d/np.abs(a))+S(u/a)-S(-u/d)
            +S(-d/(U*u))-S(a/(U*u)))

def J(s,y):
    return y*np.log(s*s+y*y)/2-y+s*np.arctan2(y,s)

def K(z):
    s,y=abs(z.real),z.imag
    return (10/27)*(2*r*(math.log(r)-1)-J(s,y+r)+J(s,y-r))

def gauge(z):
    return sum(F(e*z,u) for e in [-1,1] for u in [v,v.conjugate()])/4

rows=[]
for j in range(2501):
    s=j/10000
    if s==.25:
        continue # singular endpoint of the naive S formula; no enclosure
    z=complex(s)
    value=float(F(z,-1)-gauge(z)-c*s+K(z))
    rows.append(dict(s=s,exponent=value))
# Test the indicated height with the same fixed angle that stopped C673c.
horizontal=[]
for j in range(2701):
    s=j/10000
    z=complex(s,.15)
    value=float(F(z,v)-gauge(z)-c*s+K(z))
    horizontal.append(dict(s=s,exponent=value))
report=dict(status='FLOATING DESIGN ONLY; NOT A PROOF',
            required_upper=-.01,real_minimum=min(rows,key=lambda a:a['exponent']),
            horizontal_minimum=min(horizontal,key=lambda a:a['exponent']),
            real_samples=rows,horizontal_samples=horizontal,failures=[],
            qualifications='No continuous enclosure, finite-n replacement, signed-integral or cone-distance bound.')
Path(__file__).with_suffix('.json').write_text(json.dumps(report,indent=2)+'\n')
print('Real crossing sampled minimum:',report['real_minimum'])
print('Height-3/20 sampled minimum:',report['horizontal_minimum'])
print('Required upper: -0.01; failures:',report['failures'])
print('Full diagnostic:',Path(__file__).with_suffix('.json'))
