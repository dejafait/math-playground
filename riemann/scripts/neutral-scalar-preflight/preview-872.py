"""Unvalidated finite-block preview, solely to choose directions, no certificate."""
import json
from pathlib import Path
import numpy as np

T = 4*np.log(3.)
P = 64.
N = 131072
dx = P/N
x = np.arange(N)*dx
def theta(s):
    s = np.clip(s, 1e-15, 1-1e-15)
    a, b = np.exp(-1/s), np.exp(-1/(1-s))
    return a/(a+b)
chi = theta(40*x/T-1)*theta(39-40*x/T)
chi[(x <= T/40) | (x >= 39*T/40)] = 0
phi = chi[:,None]*np.sin(np.pi*x[:,None]*np.arange(1,13)/T)
mom = dx*(np.exp(np.minimum(x,T)/2)@phi)
# Each column is EXACTLY defined by the integrals approximated by mom,
# with the numerical values used ONLY in this preview.
B = np.zeros((12,10))
for j,k in enumerate(range(2,12)):
    pivot = k%2
    B[k,j], B[pivot,j] = 1, -mom[k]/mom[pivot]
H = dx*phi.T@phi
L = np.linalg.cholesky(B[:,:4].T@H@B[:,:4])
V = B[:,:4]@np.linalg.inv(L.T)
Z0 = B[:,4:]-V@(V.T@H@B[:,4:])
L = np.linalg.cholesky(Z0.T@H@Z0)
Z = Z0@np.linalg.inv(L.T)
M = np.column_stack((V,Z))
t = 2*np.pi*np.fft.rfftfreq(N, d=dx)
z = .25+.5j*t
zz = z+256
# Asymptotic recurrence, ordinary floats: deliberately NOT rigorous.
m = (np.log(zz)-1/(2*zz)-1/(12*zz**2)+1/(120*zz**4)).real-np.log(np.pi)
for j in range(256):
    m -= ((z+j)**-1).real
pp=[]
for p in range(2,81):
    if any(p%q==0 for q in range(2,int(p**.5)+1)): continue
    n=p
    while n<81:
        pp.append((n,p))
        n*=p
pp.sort()
symbol=m.copy()
for n,p in pp: symbol-=2*np.log(p)/np.sqrt(n)*np.cos(t*np.log(n))
F=dx*np.fft.rfft(phi, axis=0)
weights=2*symbol/P
weights[0]/=2
weights[-1]/=2
E=(F.conj().T@(weights[:,None]*F)).real
Q=M.T@E@M
A,C,G=Q[:4,:4],Q[:4,4:],Q[4:,4:]
dg,ug=np.linalg.eigh(G)
dp=float(dg[0])
S=A-C@C.T/dp
ds,us=np.linalg.eigh(S)
v=V@us[:,0]
# One covariance direction aligns with C* the selected v.
c=Z@(C.T@us[:,0])
c/=np.sqrt(c@H@c)
floor=Z@ug[:,0]
out={
    'status':'UNVALIDATED_PREVIEW_ONLY', 'N':N, 'period':P,
    'prime_powers':pp, 'moments':mom.tolist(),
    'gram_error':float(np.max(np.abs(M.T@H@M-np.eye(10)))),
    'retained_eigenvalues':np.linalg.eigvalsh(A).tolist(),
    'complement_eigenvalues':dg.tolist(),
    'candidate_scalar_matrix_eigenvalues':ds.tolist(),
    'full_finite_eigenvalues':np.linalg.eigvalsh(Q).tolist(),
    'directions':{'retained':v.tolist(),'floor':floor.tolist(),'coupling':c.tolist()},
    'trial_values':{'E_v':float(v@E@v),'E_floor':float(floor@E@floor),
                    'E_coupling':float(c@E@c),'E_cross':float(v@E@c)},
    'failures':['No rounding, quadrature, exact-moment, projection or tail enclosures; this is not evidence of a sign.']}
path=Path(__file__).with_name('preview-872.json')
path.write_text(json.dumps(out,indent=2)+'\n')
print('UNVALIDATED_PREVIEW_ONLY; min candidate S =',ds[0],'; d_Ritz =',dp,
      '; min finite E =',np.linalg.eigvalsh(Q)[0],'; required rejection: <0 with all errors; failures: unvalidated; path:',path)
