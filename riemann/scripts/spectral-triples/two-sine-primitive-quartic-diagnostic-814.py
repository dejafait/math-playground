"""Uncertified quartic selection only."""
import runpy,json,math
from pathlib import Path
m=runpy.run_path(str(Path(__file__).with_name('two-sine-primitive-diagnostic-814.py')))
coeff,lap,corr,pole=(m[k] for k in ['coeff','lap','corr','pole'])
pi=math.pi
ref={1:-.5j,-1:.5j}; rr=coeff(ref)
def energy(c,h):
    r=coeff(c)
    return -2*sum(lap(r,2*k+.5)-h*lap(rr,2*k+.5) for k in range(8192))+pole(c)-h*pole(ref)-2*sum(math.log(p)/math.sqrt(n)*(corr(r,math.log(n))-h*corr(rr,math.log(n))) for n,p in [(2,2),(3,3),(4,2),(5,5),(7,7)])
f2={2:-.5j,-2:.5j};fs={1:-.5j,-1:.5j,2:-.5j,-2:.5j}
g1={0:-1,1:-.5,-1:-.5};g2={0:.5,2:-.25,-2:-.25};gs={0:-.5,1:-.5,-1:-.5,2:-.25,-2:-.25}
A22=energy(f2,1); A12=(energy(fs,2)-A22)/2
B11=energy(g1,3);B22=energy(g2,.75);B12=(energy(gs,1.75)-B11-B22)/2
# defect numerator B(t)*(1+t^2)-A(t)*(3-2t+.75t^2)
q=[B11,2*B12-6*A12,B11+B22+4*A12-3*A22,2*B12-1.5*A12+2*A22,B22-.75*A22]
a=[-x for x in q];center=.43
shift=[sum(math.comb(k,j)*a[k]*center**(k-j) for k in range(j,5)) for j in range(5)]
res=dict(kind='UNCERTIFIED diagnostic only',A12=A12,A22=A22,B11=B11,B12=B12,B22=B22,defect_coefficients=q,negative_defect_shift=shift,center=center)
p=Path(__file__).with_suffix('.json');p.write_text(json.dumps(res,indent=2)+'\n')
print('Quartic diagnostic:',res);print('Full artifact:',p)
