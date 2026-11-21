#!/usr/bin/env python3
"""NONRIGOROUS diagnostic of the fixed approved four-dimensional kernel.

No value in this file is a sign certificate. Exact definitions and a later
validated bound, if obtained, must justify any mathematical conclusion.
"""
import json
import math
from pathlib import Path
import numpy as np

T = 8 * math.log(3)
ell = 6 * math.log(3)
delta = T / 40
r = ell / 12


def theta(x):
    x = np.asarray(x)
    y = np.zeros_like(x)
    y[x >= 1] = 1
    q = (x > 0) & (x < 1)
    z = x[q]
    a = np.exp(-1 / z)
    b = np.exp(-1 / (1-z))
    y[q] = a / (a+b)
    return y


def bump(x):
    z = 1 - (np.asarray(x)/r)**2
    out = np.zeros_like(z)
    q = z > 0
    out[q] = np.exp(-1/z[q])
    return out


def phi(x):
    x = np.asarray(x)
    chi = theta((x-delta)/delta)*theta((T-delta-x)/delta)
    return chi[..., None]*np.sin(x[..., None]*np.arange(1,7)*math.pi/T)


def quad(a,b,step=.04,degree=10):
    nodes, weights = np.polynomial.legendre.leggauss(degree)
    edges=np.linspace(a,b,max(2,math.ceil((b-a)/step)+1))
    mid=(edges[:-1]+edges[1:])/2
    half=np.diff(edges)/2
    return (mid[:,None]+half[:,None]*nodes).ravel(), (half[:,None]*weights).ravel()


def prime_powers(bound):
    primes=[]
    for p in range(2,bound):
        if all(p%q for q in primes if q*q<=p):
            primes.append(p)
    ans=[]
    for p in primes:
        n=p
        while n<bound:
            ans.append((n,math.log(p)/math.sqrt(n)))
            n*=p
    return sorted(ans)


def main():
    x,w=quad(0,T)
    moments=(w*np.exp(x/2))@phi(x)
    coeff=np.zeros((6,4))
    for j,k in enumerate([2,4,3,5]):
        anchor=0 if k%2==0 else 1
        coeff[k,j]=1
        coeff[anchor,j]=-moments[k]/moments[anchor]
    def f(x):
        return phi(x)@coeff
    corrected=[]
    correction_coeff=[]
    for j in range(2):
        a=j*2*math.log(3)
        c=a+np.array([ell/3,2*ell/3])
        def beta(x,c=c):
            return bump(np.asarray(x)[...,None]-c)
        def g(x,j=j):
            alpha=math.pi/2*theta((np.asarray(x)-3*math.log(3))/(2*math.log(3)))
            rho=np.cos(alpha) if j==0 else np.sin(alpha)
            return rho[...,None]*f(x)
        moments2=np.stack([w*np.exp(x/2),w*np.exp(-x/2)])
        H=moments2@beta(x)
        d=moments2@g(x)
        C=np.linalg.solve(H,d)
        correction_coeff.append(C.tolist())
        def v(x,g=g,beta=beta,C=C):
            return g(x)-beta(x)@C
        corrected.append(v)
    pp=prime_powers(6561)
    energies=[]
    for h in [f]+corrected:
        hx=h(x)
        N=hx.T@(w[:,None]*hx)
        u,wu=quad(0,T,step=.04,degree=10)
        q=np.zeros((4,4))
        for t,wt in zip(u,wu):
            xx,ww=quad(-t,T,step=.05,degree=8)
            diff=h(xx+t)-h(xx)
            q+=wt*math.exp(-t/2)/(-math.expm1(-2*t))*(diff.T@(ww[:,None]*diff))
        tail=sum(2*math.exp(-(2*k+.5)*T)/(2*k+.5) for k in range(20))
        m0=-np.euler_gamma-math.pi/2-3*math.log(2)-math.log(math.pi)
        A=(m0+tail)*N+q
        P=np.zeros((4,4))
        for n,b in pp:
            R=hx.T@(w[:,None]*h(x+math.log(n)))
            P+=b*(R+R.T)
        D=np.stack([w*np.exp(x/2),w*np.exp(-x/2)])@hx
        pole=np.outer(D[0],D[1])+np.outer(D[1],D[0])
        E=A-P+pole
        energies.append({'norm':N.tolist(),'archimedean':A.tolist(),'arithmetic':P.tolist(),'pole':pole.tolist(),'energy':E.tolist(),'moments':D.tolist()})
    mat=np.array(energies[0]['energy'])-np.array(energies[1]['energy'])-np.array(energies[2]['energy'])
    ev,vec=np.linalg.eigh(mat)
    result={'status':'DIAGNOSTIC_ONLY_NOT_CERTIFIED','T':T,'ell':ell,'prime_power_count':len(pp),'moments':moments.tolist(),'basis_coefficients':coeff.tolist(),'correction_coefficients':correction_coeff,'energies':energies,'defect':mat.tolist(),'eigenvalues':ev.tolist(),'eigenvectors':vec.tolist(),'required_certificate':'Exact neutral witness with rigorous Delta upper bound < 0, or complete restricted PSD certificate.'}
    out=Path(__file__).with_suffix('.json')
    out.write_text(json.dumps(result,indent=2)+'\n')
    print('DIAGNOSTIC ONLY:',ev.tolist())
    print('Required: rigorous upper bound < 0 on an exact-neutral witness, or full restricted PSD certificate.')
    print('Full diagnostic:',out)


if __name__=='__main__':
    main()
