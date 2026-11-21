"""Audit the unchanged C750c certificate; preserve previous artifacts.

Instrument domains, replay inherited constants, and independently check
exact-dyadic projection and error accounting. This is not an independent
FFT library; analytic justification is recorded in C750c.
"""
import json
from fractions import Fraction as F
from math import isqrt
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parent
BASE = ROOT.parent / 'corrected-ims'
source = (ROOT / 'certificate-872.cpp').read_text().replace(
    '#include "../corrected-ims/certificate-315.cpp"',
    (BASE / 'certificate-315.cpp').read_text())

def replace(old, new, count=1):
    global source
    assert source.count(old) == count, old
    source = source.replace(old, new)

replace('#include <algorithm>', '#include <algorithm>\n#include <cfenv>')
replace('struct I { double l,h; I(double x=0):l(x),h(x){} I(double a,double b):l(a),h(b){} };', '''struct I { double l,h;
 I(double x=0):l(x),h(x){if(!isfinite(x))throw runtime_error("nonfinite point");}
 I(double a,double b):l(a),h(b){if(!isfinite(a)||!isfinite(b)||a>b)throw runtime_error("invalid interval");}
};
double max_trig=0,max_atan=0,max_exp_base=0,max_delay_width=0;
double min_log_base=2,max_log_base=1,min_delay_cell_margin=1;
int delay_calls=0;''')
replace('I v(z),sum(1),term(1);', 'max_exp_base=max(max_exp_base,abs(z));if(abs(z)>.125)throw runtime_error("exp base");I v(z),sum(1),term(1);')
replace('I logUnit(I x){I t=', 'I logUnit(I x){if(x.l<1||x.h>2)throw runtime_error("log base");min_log_base=min(min_log_base,x.l);max_log_base=max(max_log_base,x.h);I t=')
replace('I atanSmall(I x){I t=', 'I atanSmall(I x){max_atan=max(max_atan,max(abs(x.l),abs(x.h)));if(max_atan>.25)throw runtime_error("atan domain");I t=')
for fn in ('sinSmall', 'cosSmall'):
    replace(f'I {fn}(I x){{I term', f'I {fn}(I x){{max_trig=max(max_trig,max(abs(x.l),abs(x.h)));if(max_trig>4)throw runtime_error("trig domain");I term')
replace('I u=I(1)/I(a);if(u.l<k)', 'if(a<=0||k<2||k>4)throw runtime_error("eta endpoint domain");I u=I(1)/I(a);if(u.l<k)')
replace('int m=(int)floor((u.l+u.h)/2);I corr(0);', '''int m=(int)floor((u.l+u.h)/2);
 if(floor(u.l)!=m||floor(u.h)!=m)throw runtime_error("delay crosses cell");
 delay_calls++;max_delay_width=max(max_delay_width,up(u.h-u.l));
 min_delay_cell_margin=min(min_delay_cell_margin,min(dn(u.l-m),dn(m+1-u.h)));
 I corr(0);''', count=2)
replace('if(!numeric_limits<double>::is_iec559)', '''if(fegetround()!=FE_TONEAREST||numeric_limits<double>::digits!=53||numeric_limits<double>::radix!=2)throw runtime_error("binary64 environment");
 volatile double tiny=numeric_limits<double>::denorm_min(),one=1;
 if(!(tiny*one>0))throw runtime_error("subnormals flushed");
 if(!numeric_limits<double>::is_iec559)''')
replace('const int nm=65536,n=262144;', '''const int nm=65536,n=262144;
 if(nm%2||n<=0||(n&(n-1)))throw runtime_error("grid counts");
 if((DELTA-I(64)/I(n)).l<=0||(T+I(128)/I(n)).h>=9)throw runtime_error("interpolant support");''')
replace('cerr<<"Status "<<(reject?', '''ofstream audit("scripts/neutral-scalar-preflight/domains-873.json");audit<<setprecision(17);
 audit<<"{\\"status\\":\\"PASS\\",\\"max_trig_abs\\":"<<max_trig<<",\\"trig_required\\":4,\\"max_atan_abs\\":"<<max_atan<<",\\"atan_required\\":0.25,\\"max_exp_base_abs\\":"<<max_exp_base<<",\\"exp_required\\":0.125,\\"log_base_range\\":["<<min_log_base<<","<<max_log_base<<"],\\"log_required\\":[1,2],\\"max_delay_interval_width\\":"<<max_delay_width<<",\\"min_delay_cell_margin\\":"<<min_delay_cell_margin<<",\\"required_cell_margin\\":0,\\"delay_calls\\":"<<delay_calls<<",\\"binary64_round_to_nearest_subnormals\\":true,\\"interpolant_support_checked\\":true,\\"simpson_subintervals\\":"<<nm<<",\\"failures\\":[]}\\n";
 cerr<<"Status "<<(reject?''')
instrumented = ROOT / 'instrumented-873.cpp'
instrumented.write_text(source)
binary = '/private/tmp/riemann-neutral-scalar-instrumented-873'
subprocess.run(['clang++', '-O2', '-std=c++17', '-ffp-contract=off', str(instrumented), '-o', binary], check=True)
with (ROOT / 'instrumented-873.json').open('w') as out, (ROOT / 'instrumented-873.log').open('w') as log:
    subprocess.run([binary], stdout=out, stderr=log, check=True)
constbin = '/private/tmp/riemann-neutral-scalar-constants-873'
subprocess.run(['clang++', '-O2', '-std=c++17', '-ffp-contract=off', str(BASE / 'constants-315.cpp'), '-o', constbin], check=True)
with (ROOT / 'constants-873.json').open('w') as out, (ROOT / 'constants-873.log').open('w') as log:
    subprocess.run([constbin], stdout=out, stderr=log, check=True)

def read(name): return json.loads((ROOT / name).read_text())
c = read('certificate-872.json')
domains = read('domains-873.json')
constants = read('constants-873.json')
checks = {
    'unmodified_replay_identical': c == read('replay-873.json'),
    'instrumented_replay_identical': c == read('instrumented-873.json'),
    'all_fourteen_constants_pass': len(constants['checks']) == 14 and all(x['pass'] for x in constants['checks']),
    'constants_replay_identical': constants == json.loads((BASE / 'constants-315.json').read_text()),
    'all_124_delays_checked': domains['delay_calls'] == 4*31,
    'strict_delay_cell_margin': domains['min_delay_cell_margin'] > 0,
}

# Exact rational interval operations, independent of C++ rounding.
def iv(x): return tuple(F(v) for v in x)
def point(x): return (F(x), F(x))
def neg(a): return (-a[1], -a[0])
def add(a,b): return (a[0]+b[0], a[1]+b[1])
def sub(a,b): return add(a,neg(b))
def mul(a,b):
    p = [x*y for x in a for y in b]
    return (min(p), max(p))
def square(a):
    return (0 if a[0]<=0<=a[1] else min(x*x for x in a), max(x*x for x in a))
def div(a,b):
    assert b[0]*b[1]>0
    return mul(a,(1/b[1],1/b[0]))
def encl(a,b): return a[0]<=b[0] and b[1]<=a[1]
def sumiv(xs):
    s=point(0)
    for x in xs: s=add(s,x)
    return s
def vadd(a,b): return [add(x,y) for x,y in zip(a,b)]
def scale(x,a): return [mul(point(x),t) for t in a]
G=[[iv(x) for x in row] for row in c['gram']]
m=[iv(x) for x in c['moments']]
def dot(a,b): return sumiv(mul(mul(a[i],G[i][j]),b[j]) for i in range(6) for j in range(6))
def neutral(i):
    a=[point(0) for _ in range(6)]
    a[i]=point(1)
    a[0]=div(neg(m[i]),m[0])
    return a
b,d=neutral(1),neutral(2)
h00,h01,h11=dot(b,b),dot(b,d),dot(d,d)
det=sub(mul(h00,h11),square(h01))
checks['retained_gram_determinant_positive']=det[0]>0
def project(r):
    p0,p1=dot(r,b),dot(r,d)
    a=div(sub(mul(h11,p0),mul(h01,p1)),det)
    e=div(sub(mul(h00,p1),mul(h01,p0)),det)
    return vadd(r,vadd([mul(neg(a),t) for t in b],[mul(neg(e),t) for t in d]))
v=vadd(scale(F(23,100),b),scale(F(58,100),d))
z=project(vadd(vadd(scale(F(38,100),neutral(3)),scale(F(-52,100),neutral(4))),scale(F(19,100),neutral(5))))
y=project(vadd(vadd(scale(F(32,100),neutral(3)),scale(F(42,100),neutral(4))),scale(F(50,100),neutral(5))))
for name,a in [('v',v),('z',z),('y',y)]:
    stored=[iv(x) for x in c['directions'][name]]
    checks[name+'_exact_coordinate_enclosure']=all(encl(x,t) for x,t in zip(stored,a))
    checks[name+'_original_metric_norm_enclosure']=encl(iv(c['norm_'+name]),dot(stored,stored))

def sqrt_upper(x):
    # Rational upper square root with absolute gap <= 2^-160.
    assert x>=0
    n=1<<160
    k=isqrt((x.numerator*n*n)//x.denominator)
    return F(k+1,n)
E=c['energies']
for name,val in E.items():
    q,eps,ew,qw,cp=(iv(val[k]) for k in ('q_norm_squared','error_L2_squared_bound','error_W_squared_bound','q_W_squared_bound','C_prime'))
    interp=2*sqrt_upper(qw[1]*ew[1])+ew[1]+cp[1]*(2*sqrt_upper(q[1]*eps[1])+eps[1])
    checks[name+'_full_interpolation_upper']=iv(val['interpolation_energy_bound'])[1]>=interp
    checks[name+'_L2_error_upper']=eps[1]>=F(1,4096)**4*iv(val['smooth_second_derivative_squared_bound'])[1]
    total=sub(iv(val['periodic_archimedean_head']),iv(val['all_prime_delays']))
    radius=sum(iv(val[k])[1] for k in ('fourier_tail_bound','periodic_images_bound','interpolation_energy_bound'))
    checks[name+'_complete_energy_accounting']=encl(iv(val['smooth_energy']),(total[0]-radius,total[1]+radius))
ev,ez,ey,es=[iv(E[k]['smooth_energy']) for k in ('v','z','y','v_plus_y')]
cross=div(sub(sub(es,ev),ey),point(2))
checks['real_polarization_enclosure']=encl(iv(c['cross']),cross)
checks['rayleigh_enclosure']=encl(iv(c['d_plus_enclosure']),div(ez,iv(c['norm_z'])))
checks['norm_y_between_zero_and_one']=0<iv(c['norm_y'])[0] and iv(c['norm_y'])[1]<1
checks['norm_z_gt_99_100']=iv(c['norm_z'])[0]>F(99,100)
checks['retained_energy_lt_7_500']=ev[1]<F(7,500)
checks['cross_gt_9_250']=iv(c['cross'])[0]>F(9,250)
checks['rayleigh_upper_lt_1_1000']=0<iv(c['d_plus_enclosure'])[1]<F(1,1000)
checks['floor_energy_sign_unresolved']=ez[0]<0<ez[1]
sharp=ev[1]-iv(c['cross'])[0]**2/(iv(c['norm_y'])[1]*iv(c['d_plus_enclosure'])[1])
checks['tighter_comparison_upper_enclosed']=iv(c['retained_upper_comparison'])[1]>=sharp
checks['tighter_comparison_negative']=sharp<0
def prime_power(n):
    p=next((j for j in range(2,isqrt(n)+1) if n%j==0),n)
    while n%p==0: n//=p
    return n==1
expected=[n for n in range(2,81) if prime_power(n)]
checks['all_31_prime_powers_exactly_once']=len(expected)==31 and expected==c['prime_powers']
bound=F(7,500)-F(9,250)**2/F(1,1000)
checks['strict_rational_rejection']=bound==F(-641,500)<F(-32,25)
summary={
    'status':'PASS' if all(checks.values()) else 'FAIL',
    'checks':checks, 'actual_rational_upper':str(bound), 'required_upper':str(F(-32,25)),
    'retained_upper_comparison':c['retained_upper_comparison'], 'd_plus_enclosure':c['d_plus_enclosure'],
    'cross':c['cross'], 'retained_gram_determinant':[str(x) for x in det],
    'exact_coordinate_enclosures':{name:[[str(x) for x in t] for t in a] for name,a in [('v',v),('z',z),('y',y)]},
    'failures':[name for name,ok in checks.items() if not ok],
    'scope':'Unchanged C750c target; exact-dyadic checks and instrumented replay, not an independent FFT library.'
}
path=ROOT/'audit-873.json'
path.write_text(json.dumps(summary,indent=2)+'\n')
print(summary['status'],len(checks),'checks; actual rational upper',bound,'required <',F(-32,25))
print('Failures:',summary['failures'],'; full evidence:',path.relative_to(Path.cwd()))
print('Implementation domains:',(ROOT/'domains-873.json').relative_to(Path.cwd()))
raise SystemExit(0 if all(checks.values()) else 1)
