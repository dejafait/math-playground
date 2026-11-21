#!/usr/bin/env python3
"""Diagnostic only: fixed approved family, no certified sign."""
import numpy as np
import json, hashlib
from pathlib import Path
B=Path(__file__).resolve().parent
with np.load(B/'original-galerkin-586.npz') as q:
    M,T,Ts,U,Z=[q[k] for k in ['local_matrix','t_entries','ts_entries','u_entries','neutral_coordinate_center']]
ZT=Z.copy()
A=Z.T@M@Z
F=np.hstack((T@ZT,Ts@ZT))
BB=Z.T@F
Y=np.linalg.solve(A,BB)
G=Z@Y
E0=np.block([[ZT.T@M@ZT,-ZT.T@U.T@ZT],[-ZT.T@U@ZT,ZT.T@M@ZT]])
E=E0-BB.T@Y-Y.T@BB+Y.T@A@Y
rho=F-M@G
with np.load(B/'complete-covariance-532.npz') as q:
    H=q['m0']-.00024*np.eye(512)-(100/307)*(q['cov00']+.0046*np.eye(512))
# Diagnostic diagonal centers; complete certification follows separately.
ell=np.log(3)/2
n=np.arange(512,1024)
d=np.log(n/(2*ell))-2*ell**2/(9*n*n)
# D from the original complete-entry generator is needed for exact weights;
# d only gives an UPPER covariance useful for this diagnostic.
C=rho[:512].T@np.linalg.solve(H,rho[:512])+rho[512:].T@((2/d[:,None])*rho[512:])
w=np.ones(2044)
comp=E-C
vals,vecs=np.linalg.eigh((comp+comp.T)/2)
p=B/'joint-galerkin-family-locator-598.npz'
np.savez_compressed(p,Z=Z,ZT=ZT,A=A,B=BB,Y=Y,G=G,E=E,rho_first1024=rho,comparison_first1024=comp,weights=w,eigenvalues=vals,lowest_free_direction=vecs[:,0])
r=dict(certified=False,first1024_comparison_minimum=float(vals[0]),first1024_comparison_maximum=float(vals[-1]),predictor_fro=float(np.linalg.norm(Y)),galerkin_residual_fro=float(np.linalg.norm(A@Y-BB)),first1024_residual_fro=float(np.linalg.norm(rho)),minimum_A_center=float(np.linalg.eigvalsh(A)[0]),archive_sha256=hashlib.sha256(p.read_bytes()).hexdigest(),failures=['Diagnostic only; all family entry, solve, covariance, arithmetic and infinite-output enclosures remain unpaid'])
out=B/'joint-galerkin-family-locator-598.json'
out.write_text(json.dumps(r,indent=2)+'\n')
print(json.dumps(r)); print(out)
