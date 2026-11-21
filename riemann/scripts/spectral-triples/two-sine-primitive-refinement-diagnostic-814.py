"""Uncertified direction selection only; not evidence for a sign."""
import cmath, math, json
from pathlib import Path
pi=math.pi

def coeff(c):
    out={}
    def add(k,a=0,b=0):
        u,v=out.get(k,(0j,0j));out[k]=(u+a,v+b)
    for a,ca in c.items():
        for b,cb in c.items():
            z=ca*cb
            if a+b==0: add(a,2*z,-z)
            else:
                z*=(-1)**(a+b)/(1j*(a+b)*pi)
                add(-b,z);add(a,-z)
    return out

def corr(r,y):return sum((a+b*y)*cmath.exp(1j*k*pi*y) for k,(a,b) in r.items()).real

def lap(r,b):
    total=0j
    for k,(u,v) in r.items():
        z=b-1j*k*pi; e=math.exp(-2*b)
        total+=u*(1-e)/z+v*((1-e)/(z*z)-2*e/z)
    return total.real

def pole(c):
    def ff(sign):
        return sum(v*2*cmath.sinh(sign/2+1j*k*pi)/(sign/2+1j*k*pi) for k,v in c.items()).real
    return 2*ff(1)*ff(-1)

rows=[]
for t in [.3,.35,.375,.4,.425,.45,.475]:
    f={1:-.5j,-1:.5j,2:-.5j*t,-2:.5j*t}
    g={0:-1+t/2,1:-.5,-1:-.5,2:-t/4,-2:-t/4}
    n=1+t*t; h=3-2*t+.75*t*t
    rf,rg=coeff(f),coeff(g)
    K=4096
    arch=-2*sum(lap(rg,2*k+.5)/h-lap(rf,2*k+.5)/n for k in range(K))
    pd=pole(g)/h-pole(f)/n
    pr=-2*sum(math.log(p)/math.sqrt(m)*(corr(rg,math.log(m))/h-corr(rf,math.log(m))/n) for m,p in [(2,2),(3,3),(4,2),(5,5),(7,7)])
    # relative input energy to s1; common norm constant cancels
    r1=coeff({1:-.5j,-1:.5j})
    qrel=-2*sum(lap(rf,2*k+.5)/n-lap(r1,2*k+.5) for k in range(K))+pole(f)/n-pole({1:-.5j,-1:.5j})-2*sum(math.log(p)/math.sqrt(m)*(corr(rf,math.log(m))/n-corr(r1,math.log(m))) for m,p in [(2,2),(3,3),(4,2),(5,5),(7,7)])
    rows.append(dict(t=t,n=n,h=h,arch=arch,pole=pd,prime=pr,defect=arch+pd+pr,input_relative_to_first=qrel))
out=Path(__file__).with_suffix('.json');out.write_text(json.dumps({'kind':'UNCERTIFIED diagnostic only','K':K,'rows':rows},indent=2)+'\n')
print('Uncertified diagnostic: t, defect, input relative to first sine')
for r in rows:print(r['t'],r['defect'],r['input_relative_to_first'])
print('Full diagnostic:',out)
