"""Untrusted proposal only. The directed certificate must decide all claims."""
import json
from pathlib import Path
import numpy as np

HERE = Path(__file__).resolve().parent
old = json.loads((HERE/'refined-464.json').read_text())
mid = lambda x: (float(x['lo'])+float(x['hi']))/2
a = 5*np.log(3)/4
ell = np.log(3)/2
d = 84
k = np.arange(d)*np.pi/a
u = k*k
norm = np.full(d, np.sqrt(2/a)); norm[0] = 1/np.sqrt(a)
full = norm/np.sqrt(2)
moments = []
for cell in range(5):
    le, re = 2*cell-5, 2*cell-3
    for sigma in (1,-1):
        beta = sigma/2
        left = np.exp(-sigma*ell/4)*(beta*np.cos(np.arange(d)*le*np.pi/5)
                +k*np.sin(np.arange(d)*le*np.pi/5))
        right = np.exp(sigma*ell/4)*(beta*np.cos(np.arange(d)*re*np.pi/5)
                +k*np.sin(np.arange(d)*re*np.pi/5))
        moments.append(full*(right-left)/(beta*beta+u))
C = np.array(moments)
reps = [0,1,2,3,4]
A = C[reps,64:]
Y = -A.T@np.linalg.solve(A@A.T, C[reps,:64])
R = np.vstack([np.eye(64),Y])
S = {int(p):mid(x) for p,x in old['inverse_power_sums']['response'].items()}
h = np.full(d, -mid(old['gamma'])-np.pi/2-3*np.log(2)-np.log(np.pi))
gram = np.zeros((d,d))
for j in range(512):
    c = 2*j+.5
    h += 2*u/(c*(c*c+u))
    row = norm*(-1.)**np.arange(d)*c/(c*c+u)
    gram += np.outer(row,row)*(1-np.exp(-2*a*c))
    if j==0:
        pole = row*np.sqrt(1-np.exp(-a))*np.exp(a/2)*np.sqrt(1-np.exp(-a))
for m in range(32):
    h += 2*(-1)**m*u**(m+1)*S[2*m+3]
    poly = sum(np.outer(u**t,u**(m-t)) for t in range(m+1))
    gram += np.outer(norm*(-1.)**np.arange(d),norm*(-1.)**np.arange(d))*((-1)**m)*poly*S[2*m+2]
prime = np.zeros((d,d))
r = np.arange(d)[:,None]; s = np.arange(d)[None,:]
for n,p in [(2,2),(3,3),(4,2),(5,5),(7,7),(8,2),(9,3),(11,11),(13,13)]:
    delay = np.log(n); b = a-delay/2
    def sd(t): return b*np.sinc(t*b/np.pi)
    prime += -2*np.log(p)/np.sqrt(n)*np.outer(full,full)*(
        sd(k[:,None]-k[None,:])*np.cos((k[:,None]+k[None,:])*delay/2)
        +sd(k[:,None]+k[None,:])*np.cos((k[:,None]-k[None,:])*delay/2))
E = np.diag(h)+prime+gram+np.outer(pole,pole)
H = E[:64,:64]+256*C[:,:64].T@C[:,:64]
F = R.T@E@R-H/2
eig,z = np.linalg.eigh((F+F.T)/2)
numerators = [int(round(x*2**40)) for x in z[:,0]]
out = {'status':'UNTRUSTED_PROPOSAL', 'gram_eigenvalues':np.linalg.eigvalsh(A@A.T).tolist(),
       'Y_norm_proposal':float(np.linalg.norm(Y,2)), 'difference_eigenvalues':eig.tolist(),
       'witness':{'numerators':numerators,'denominator':2**40},
       'energy_diagonal_proposals':np.diag(F).tolist(),
       'warning':'floating values are neither exact rank nor sign certificates'}
path = HERE/'neutral-screen-473.json'
path.write_text(json.dumps(out,indent=2)+'\n')
print('UNTRUSTED: Gram eigenvalues',out['gram_eigenvalues'])
print('UNTRUSTED: correction norm',out['Y_norm_proposal'],'; difference min/max',float(eig[0]),float(eig[-1]))
print('Proposal only:',path)
