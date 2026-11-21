#!/usr/bin/env python3
"""Uncertified complete K65536 mixed-column locator for assessment562.

No mathematical certificate: FFT, entry, predictor and two tail errors
are not paid by this diagnostic. Keep all artifacts separate from564.
"""
import hashlib
import importlib.util
import json
from pathlib import Path
import numpy as np

BASE = Path(__file__).resolve().parent
N, K, F, E = 512, 65536, 510, 1020
spec = importlib.util.spec_from_file_location('entries565', BASE/'residual-certificate-532.py')
old = importlib.util.module_from_spec(spec)
spec.loader.exec_module(old)
con = old.constants()
ell, pi = con['ell'], con['pi']
n = np.arange(K)
k = n*pi/ell
nu = np.full(K, np.sqrt(2/ell)); nu[0] /= np.sqrt(2)
d = np.ones(K); d[0] /= np.sqrt(2)
p = np.where(n % 2 == 0, 1., -1.)
source = json.loads((BASE/'response-prefix-stop-546.json').read_text())
remote = [(float(r['delta']['lo']) if r['n'] != 2187 else 0.,
           float(r['weight']['lo'])) for r in source['remote']['primes']]
shifts = list(zip(con['deltas'], con['weights']))


def aggregate(terms, size=K):
    sp, sm, dg = np.zeros(size), np.zeros(size), np.zeros(size)
    for delta, a in terms:
        sn, cs = old.sincos(k[:size]*delta, pi)
        if delta > 0: sp += a*sn
        elif delta < 0: sm += a*sn
        value = (1-abs(delta)/ell)*cs
        value[1:] -= np.sign(delta)*sn[1:]/(ell*k[1:size])
        dg += a*value
    return sp, sm, dg


s7, t7, diag7 = aggregate(shifts)
s14, t14, diag14 = aggregate(remote)


def rectangle(rows, sp, sm):
    a, b = n[rows, None], n[None, :N]
    sign = p[rows, None]*p[None, :N]
    num = -sign*a*sp[rows, None]+b*sp[None, :N]
    num += a*sm[rows, None]-sign*b*sm[None, :N]
    return (2/pi)*d[rows, None]*d[None, :N]*num/(a*a-b*b)


def continuous_columns(separation):
    minus, plus, scales = [], [], []
    for j in range(1, 8):
        c = 2*j+.5
        decay = 3.**(-j)/con['fourth']
        minus.append(nu*c*(1-p*decay)/(c*c+k*k))
        plus.append(nu*c*(p-decay)/(c*c+k*k))
        scales.append(np.exp(-(separation-1)*ell*c))
    return np.array(minus).T, np.array(plus).T, np.array(scales)


cm7, cp7, scale7 = continuous_columns(7)
cm14, cp14, scale14 = continuous_columns(14)
with np.load(BASE/'complete-covariance-532.npz') as z:
    m0, t0 = z['m0'], z['mc']+z['mg']
with np.load(BASE/'response-prefix-remote-546.npz') as z:
    u0 = z['remote_prime']
u0 = u0+(cm14[:N]*scale14)@cp14[:N].T
with np.load(BASE/'neutral-head-covariance-559.npz') as z:
    zh, g, sol, mc = z['z'], z['predictor_raw'], z['head_solution'], z['comparison_lower']
vhead = g+sol
vpath = BASE/'signed-mixed-inverse-output-565.npy'
wpath = BASE/'signed-mixed-columns-565.npy'
v = np.lib.format.open_memmap(vpath, mode='w+', dtype='float64', shape=(K,E))
w = np.lib.format.open_memmap(wpath, mode='w+', dtype='float64', shape=(2,K,E))
v[:N] = 0
w[0,:N] = np.hstack((m0@zh,-u0.T@zh))-t0.T@vhead
w[1,:N] = np.hstack((-u0@zh,m0@zh))-t0@vhead
imag, _ = old.psi_imag(k,pi)
bpsi = k*imag/2
yy = k/2
hdiag = np.log(64.25**2+yy*yy)/2-64.25/(2*(64.25**2+yy*yy))-con['logpi']
for j in range(64): hdiag -= (j+.25)/((j+.25)**2+yy*yy)
mom = np.array([nu*c*(p*(con['fourth'] if c>0 else 1/con['fourth'])-1)/
                (c*c+k*k) for c in [.5,-.5]])
for start in range(N,K,N):
    rows = slice(start,start+N)
    kn,km=k[rows,None],k[None,:N]
    ss=(bpsi[rows,None]-bpsi[None,:N])/(kn*kn-km*km)
    for j in range(64):
        c=2*j+.5
        ss-=(3.**(-j)/con['fourth'])*p[rows,None]*c*c/((c*c+kn*kn)*(c*c+km*km))
    ss*=2*nu[rows,None]*nu[None,:N]*(p[rows,None]==p[None,:N])
    ll=ss+256*mom[:,rows].T@mom[:,:N]
    tt=rectangle(rows,s7,t7)+(cm7[rows]*scale7)@cp7[:N].T
    ts=rectangle(rows,-t7,-s7)+(cp7[rows]*scale7)@cm7[:N].T
    uu=rectangle(rows,s14,t14)+(cm14[rows]*scale14)@cp14[:N].T
    us=rectangle(rows,-t14,-s14)+(cp14[rows]*scale14)@cm14[:N].T
    lz=ll@zh
    v[rows]=(2/hdiag[rows,None])*(np.hstack((tt@zh,ts@zh))-ll@g)
    w[0,rows]=np.hstack((lz,-us@zh))-ts@vhead
    w[1,rows]=np.hstack((-uu@zh,lz))-tt@vhead
    if start%8192==0: print('Complete direct rows through',start+N-1,flush=True)
v.flush(); w.flush()


def cauchy(u, plus):
    """Finite off-diagonal (1/(n-m) +/- 1/(n+m)) product."""
    size=len(u)
    kernel=np.zeros(2*size)
    kernel[1:size]=1/np.arange(1,size)
    kernel[size+1:]=-1/np.arange(size-1,0,-1)
    ht=np.fft.irfft(np.fft.rfft(kernel)[:,None]*np.fft.rfft(u,n=2*size,axis=0),n=2*size,axis=0)[:size]
    hankel=np.zeros(2*size)
    hankel[1:2*size-1]=1/np.arange(1,2*size-1)
    hh=np.fft.irfft(np.fft.rfft(hankel)[:,None]*np.fft.rfft(u[::-1],n=2*size,axis=0),n=2*size,axis=0)[size-1:2*size-1]
    hh[1:]-=u[1:]/(2*np.arange(1,size)[:,None])
    return ht+hh if plus else ht-hh


def both_prime(u, sp,sm,dg):
    size=len(u)
    dn,pn=d[:size,None],p[:size,None]
    a=dn*u
    hp=cauchy(a,True); hpp=cauchy(pn*a,True)
    out=dn/pi*(-pn*sp[:,None]*hpp+cauchy(sp[:,None]*a,False)+
               sm[:,None]*hp-pn*cauchy(pn*sm[:,None]*a,False))+dg[:,None]*u
    adj=dn/pi*(pn*sm[:,None]*hpp-cauchy(sm[:,None]*a,False)-
               sp[:,None]*hp+pn*cauchy(pn*sp[:,None]*a,False))+dg[:,None]*u
    return out,adj


size=64
a=np.arange(size)[:,None]; b=np.arange(size)[None,:]
den=a*a-b*b; np.fill_diagonal(den,1)
sgn=p[:size,None]*p[None,:size]
direct=(2/pi)*d[:size,None]*d[None,:size]*(
    -sgn*a*s7[:size,None]+b*s7[None,:size]+a*t7[:size,None]-sgn*b*t7[None,:size])/den
np.fill_diagonal(direct,diag7[:size])
probe=np.random.default_rng(565).normal(size=(size,4))
ta,tb=both_prime(probe,s7[:size],t7[:size],diag7[:size])
replay=max(float(np.linalg.norm(ta-direct@probe)),float(np.linalg.norm(tb-direct.T@probe)))
print('UNCERTIFIED finite algebra replay discrepancy',replay,flush=True)
for start in range(0,E,24):
    cols=slice(start,min(start+24,E))
    vv=np.array(v[:,cols])
    tt,ts=both_prime(vv,s7,t7,diag7)
    tt+=(cm7*scale7)@(cp7.T@vv)
    ts+=(cp7*scale7)@(cm7.T@vv)
    w[0,:,cols]-=ts
    w[1,:,cols]-=tt
    if start%240==0:print('Complete inverse action head columns through',min(start+24,E)-1,flush=True)
w.flush()
dt=np.log(n[N:]/(2*ell))-2*ell*ell/(9*n[N:]**2)
rp=(.25+k[n[N:]%2]**2)/(.25+k[N:]**2)*np.where(n[N:]%2==0,np.sqrt(2),1.)
cov=np.zeros((E,E))
digest=hashlib.sha256()
for start in range(N,K,N):
    rows=slice(start,start+N)
    for side in range(2):
        ww=np.array(w[side,rows])-rp[start-N:start,None]*w[side,n[rows]%2]
        weighted=ww/np.sqrt(dt[start-N:start])[:,None]
        cov+=weighted.T@weighted
        digest.update(ww.tobytes())
chol=np.linalg.cholesky(mc)
white=np.linalg.solve(chol,cov)
white=np.linalg.solve(chol,white.T).T
eig,vec=np.linalg.eigh((white+white.T)/2)
x=np.linalg.solve(chol.T,vec[:,-1]); x/=np.linalg.norm(x)
out=BASE/'signed-mixed-complete-locator-565.npz'
np.savez_compressed(out,covariance=cov,comparison=mc,x=x,head_solution=sol,
                    sine_positive=s7,sine_negative=t7,diagonal_prime=diag7)
record=dict(certified=False,N=N,K=K,input_first=N,input_last=K-1,
            inverse_output_first=0,inverse_output_last=K-1,
            diagnostic_generalized_ratio=float(eig[-1]),required_ratio_upper=.25,
            algebra_replay_fro_discrepancy=replay,combined_columns_sha256=digest.hexdigest(),
            failures=['Input covariance n>=65536 unpaid','Inverse outputs n>=65536 unpaid',
                      'FFT and finite-entry arithmetic unpaid','Exact-predictor and head-solve errors unpaid'],
            arrays=[str(q.relative_to(BASE.parent.parent)) for q in [out,vpath,wpath]],
            source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
path=BASE/'signed-mixed-complete-locator-565.json'
path.write_text(json.dumps(record,indent=2)+'\n')
print('UNCERTIFIED full finite ratio',eig[-1],'; required <=.25; no budget conclusion',flush=True)
print('Report',path.relative_to(BASE.parent.parent),flush=True)
