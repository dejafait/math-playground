"""Nonrigorous direction selection for the fixed 120-mode S_d test.

The complementary slice only LOWER-approximates K; it does not change V.
No printed value is a certificate. Full diagnostic arrays are saved.
"""
import hashlib
import json
import math
from pathlib import Path
import numpy as np

N, J, K = 120, 240, 4096
pi = math.pi
ns = np.arange(J+1)
a = pi*ns
b = 2*np.arange(K)+0.5
e = np.exp(-2*b)
den = b[:, None]**2+a[None, :]**2
ss = np.sum(a[None, :]*(1-e[:, None])/den, axis=0)
cc = -np.sum(a[None, :]**2*(1-e[:, None])/(b[:, None]*den), axis=0)
dd = np.sum((1-e[:, None])*(b[:, None]**2-a[None, :]**2)/den**2
            -2*e[:, None]*b[:, None]/den, axis=0)
# Integral tails, adequate only for diagnostic direction selection.
b0 = 2*K+0.5
ss += 0.5*np.arctan(a/b0)
cc -= 0.25*np.log1p((a/b0)**2)
dd += 0.5*b0/(b0*b0+a*a)
base = np.sum((1-e)/b-(1-e/math.e)/(b+0.5))
base += 0.5*math.log1p(0.5/b0)
diag = 0.5772156649015329+math.log(4*pi*math.tanh(1))
g = np.array([0]+[-2*(-1)**n*n*pi*math.sinh(0.5)/((n*pi)**2+0.25)
                  for n in range(1,J+1)])
primes = [(2,2),(3,3),(4,2),(5,5),(7,7)]
def entry(n,m):
    sign = (-1)**(n+m)
    if n == m:
        arch = diag+2*(cc[n]-dd[n]/2+base)+ss[n]/(pi*n)
    else:
        arch = (ss[m]-ss[n])/(pi*(n-m))+(ss[m]+ss[n])/(pi*(n+m))
    val = -sign*arch-2*g[n]*g[m]
    for k,p in primes:
        t = math.log(k)
        sn,sm = math.sin(pi*n*t),math.sin(pi*m*t)
        q = 2*(1-t/2)*math.cos(pi*n*t) if n == m else (sm-sn)/(pi*(n-m))
        q += (sm+sn)/(pi*(n+m))
        val -= sign*math.log(p)/math.sqrt(k)*q
    return val
A = np.array([[entry(n,m) for m in range(1,N+1)] for n in range(1,N+1)])
A -= 0.055*np.eye(N)
B = np.array([[entry(n,m) for m in range(N+1,J+1)] for n in range(1,N+1)])
S = A-B@B.T/0.2859
ev,vec = np.linalg.eigh(S)
v = vec[:,0]
out = {"certified":False,"N":N,"complementary_slice":[N+1,J],
       "series_K":K,"d":0.2859,"tau":0.055,"eigenvalues":ev.tolist(),
       "minimum_diagonal":float(np.min(np.diag(S))),"witness":v.tolist(),
       "A":A.tolist(),"B_slice":B.tolist(),
       "quadratic_A":float(v@A@v),"squared_coupling_slice":float(np.linalg.norm(v@B)**2),
       "failures":["Floating-point diagnostic with uncertified integral tails"],
       "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
path=Path(__file__).with_suffix('.json')
path.write_text(json.dumps(out,indent=2)+'\n')
print('DIAGNOSTIC ONLY: smallest finite-slice S value',ev[0],
      '; required positivity >0; minimum diagonal',out['minimum_diagonal'])
print('witness A',out['quadratic_A'],'coupling slice',out['squared_coupling_slice'])
print('Full diagnostic:',path)
