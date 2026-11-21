#!/usr/bin/env python3
"""Diagnostic only: full rational coefficients, floating sine values."""
from fractions import Fraction as Q
from math import comb, sin, fsum
from pathlib import Path
import json

def coefficients(n):
    p=(n-1)//2
    v=[Q(comb(n,2*i+1),4**i) for i in range(p+1)]
    w=[sum((v[i]*v[s-i] for i in range(p+1) if 0<=s-i<=p),Q(0))
       for s in range(2*p+1)]
    D=[sum((w[s]*comb(n-1-s,r)*Q(1,4)**(n-1-s-r)
            for s in range(min(2*p,n-1-r)+1)),Q(0)) for r in range(n)]
    h=64*9**n
    d=[h*sum((D[r]/(h-Q(1,4))**(n-k-r+1)
              for r in range(n-k+1)),Q(0)) for k in range(1,n+1)]
    return d

def main():
    rows=[]
    for n in range(2,49):
        d=coefficients(n)
        a=[value*2**m for m,value in enumerate(d)]
        mass=sum(a,Q(0))
        for theta in (Q(1,8),Q(1,4),Q(1,2)):
            t=float(theta)
            normalized_S=2*fsum([float(a[0]/mass)*t]+
                [float(a[m]/mass)*sin(m*t)/m for m in range(2,n,2)])
            error=2*t*33/992
            rows.append(dict(n=n,theta=str(theta),S_over_mass=normalized_S,
                             error_over_mass=error,upper_over_mass=normalized_S+error))
    best=min(rows,key=lambda row:row['upper_over_mass'])
    path=Path(__file__).with_suffix('.json')
    path.write_text(json.dumps(dict(rigorous=False,method='constant-G screen only',
                                   rows=rows,best=best),indent=2)+'\n')
    print(json.dumps(dict(rigorous=False,best=best,certificate=str(path))))

if __name__=='__main__':
    main()
