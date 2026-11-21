"""Independent exact-dyadic arithmetic checks of certificate872's final bounds.

This verifies accounting and the rational rejection, not the original
interval elementary functions, FFT enclosures or analytic error theorems.
"""
import json
from fractions import Fraction as F
from pathlib import Path

root=Path(__file__).parent
c=json.loads((root/'certificate-872.json').read_text())
checks={}
def iv(v): return tuple(F.from_float(x) for x in v)
def encl(a,b): return a[0]<=b[0] and b[1]<=a[1]
def add(a,b): return (a[0]+b[0],a[1]+b[1])
def sub(a,b): return (a[0]-b[1],a[1]-b[0])
def mul(a,b):
    v=[x*y for x in a for y in b]
    return min(v),max(v)
def div(a,b):
    assert b[0]*b[1]>0
    return mul(a,(1/b[1],1/b[0]))
E=c['energies']
for name,val in E.items():
    total=sub(iv(val['periodic_archimedean_head']),iv(val['all_prime_delays']))
    radius=sum(iv(val[key])[1] for key in ('fourier_tail_bound','periodic_images_bound','interpolation_energy_bound'))
    checks[name+'_energy_accounting']=encl(iv(val['smooth_energy']),(total[0]-radius,total[1]+radius))
    checks[name+'_positive_norm_and_errors']=val['q_norm_squared'][0]>0 and all(val[k][0]>=0 for k in ('fourier_tail_bound','periodic_images_bound','interpolation_energy_bound'))
ev,ez,ey,es=(iv(E[k]['smooth_energy']) for k in ('v','z','y','v_plus_y'))
cross=sub(sub(es,ev),ey)
cross=(cross[0]/2,cross[1]/2)
checks['cross_polarization']=encl(iv(c['cross']),cross)
checks['rayleigh_upper_enclosure']=encl(iv(c['d_plus_enclosure']),div(ez,iv(c['norm_z'])))
checks['norm_z_gt_99_100']=iv(c['norm_z'])[0]>F(99,100)
checks['norm_y_lt_1']=0<iv(c['norm_y'])[0]<=iv(c['norm_y'])[1]<1
checks['retained_energy_lt_7_500']=ev[1]<F(7,500)
checks['floor_energy_lt_253_500000']=ez[1]<F(253,500000)
checks['cross_gt_9_250']=iv(c['cross'])[0]>F(9,250)
checks['rayleigh_upper_lt_1_1000']=iv(c['d_plus_enclosure'])[1]<F(1,1000)
prime_powers=[]
for n in range(2,81):
    for p in range(2,n+1):
        if any(p%q==0 for q in range(2,int(p**.5)+1)): continue
        k=p
        while k<n: k*=p
        if k==n: prime_powers.append(n)
checks['all_31_prime_powers']=len(prime_powers)==31 and prime_powers==c['prime_powers']
G=[[iv(x) for x in row] for row in c['gram']]
m=[iv(x) for x in c['moments']]
b=[(-m[1][1],-m[1][0]),(F(1),F(1))]+[(F(0),F(0))]*4
b[0]=div(b[0],m[0])
d=[(-m[2][1],-m[2][0]),(F(0),F(0)),(F(1),F(1))]+[(F(0),F(0))]*3
d[0]=div(d[0],m[0])
def dot(a,b):
    s=(F(0),F(0))
    for i in range(6):
        for j in range(6): s=add(s,mul(mul(a[i],G[i][j]),b[j]))
    return s
h00,h01,h11=dot(b,b),dot(b,d),dot(d,d)
det=sub(mul(h00,h11),mul(h01,h01))
checks['retained_even_gram_det_positive']=det[0]>0
bound=F(7,500)-F(9,250)**2/F(1,1000)
checks['rational_upper_lt_minus_32_25']=bound<F(-32,25)
out={'status':'PASS' if all(checks.values()) else 'FAIL', 'checks':checks,
     'actual_rational_upper':str(bound),'required_upper':str(F(-32,25)),
     'retained_gram_determinant_enclosure':[str(x) for x in det],
     'failures':[k for k,v in checks.items() if not v],
     'scope':'Exact dyadic endpoint accounting and rational comparison only; not an independent FFT replay.'}
path=root/'check-872.json'
path.write_text(json.dumps(out,indent=2)+'\n')
print(out['status'],len(checks),'checks; actual upper',bound,'required <',F(-32,25),'; failures:',out['failures'],'; path:',path)
