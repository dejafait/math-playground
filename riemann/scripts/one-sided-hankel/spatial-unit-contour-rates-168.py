"""Exact auxiliary rate certificate for L711; not an analytic-proof audit.

Whole segments/cells and complete quadrature/log remainders are retained.
Only arithmetic function definitions from step 166 are reused.
"""
import ast
from fractions import Fraction as F
import hashlib
import json
from math import isqrt, factorial
from pathlib import Path

helper = Path(__file__).with_name('spatial-complex-phase-166.py')
source = helper.read_text()
names = {'ceildiv', 'fixed', 'log_unit', 'logq', 'q_squared', 'derivative', 'simpson'}
definitions = [node for node in ast.parse(source).body
               if isinstance(node, ast.FunctionDef) and node.name in names]
assert {node.name for node in definitions} == names
ns = dict(F=F, SCALE=1 << 100, TERMS=40, PANELS=64,
          d=F(5,4), R=F(11,8), U=F(121,64), A=F(27,10), Y=F(9,20))
exec(compile(ast.Module(body=definitions, type_ignores=[]), str(helper), 'exec'), ns)
ns['LOG2'] = ns['log_unit'](2,1)
simpson, logq, scale = ns['simpson'], ns['logq'], ns['SCALE']
d, R, U, A, Y = [ns[key] for key in ('d','R','U','A','Y')]

def enc(value):
    value = F(value)
    return dict(numerator=value.numerator, denominator=value.denominator,
                decimal_preview=float(value))

checks = {}
def check(name, actual, relation, required):
    actual, required = F(actual), F(required)
    passed = {'<': actual < required, '>': actual > required,
              '<=': actual <= required}[relation]
    checks[name] = dict(actual=enc(actual), relation=relation,
                        required=enc(required), passed=passed)

def dc_simpson(x,c):
    lo = hi = 0
    for j in range(ns['PANELS']+1):
        t = F(j,ns['PANELS'])
        D=d+c
        v=D*(t*t/(t*t*D*D+(U/2-t*x)**2)
              -1/(D*D+(t/2-x)**2))
        vl,vh=ns['fixed'](v)
        wt=1 if j in (0,ns['PANELS']) else (4 if j%2 else 2)
        lo+=wt*vl; hi+=wt*vh
    error=F(512,45*ns['PANELS']**4)
    return F(lo,3*ns['PANELS']*scale)-error, F(hi,3*ns['PANELS']*scale)+error

omega = tuple(A*(F(logq(F(9,5))[k],scale)-F(4,5)
                 +F(121,100)*F(logq(F(201,121))[k],scale)) for k in (0,1))
frequency_upper = omega[1]+F(1,3000)
check('bump_frequency_upper',frequency_upper,'<',F(543,500))
check('frequency_over_A',frequency_upper/A,'<',F(403,1000))

# L709's derivative bounds continue to this explicitly checked rectangle.
Dmin=F(57,50)
check('third_affine_factor_min_squared',
      (U/2)**2*Dmin**2/(Dmin**2+F(51,100)**2),'>',F(4,5)**2)
fourth=6*((F(1,2)/d)**4+(d/(U/2))**4
          +((F(7,5)**2+1)/F(4,5)**2)**2+(F(1,2)/Dmin)**4)
check('log_fourth_t_derivative',fourth,'<',256)
check('affine_slope_squared',F(7,5)**2+1,'<',F(7,4)**2)
der4=24*(U/2)*F(7,4)**3/F(4,5)**5+24*F(1,2)**4/Dmin**5
check('both_gradient_fourth_t_derivatives',der4,'<',512)
check('real_halfline_reduction',1+R+U/4,'>',F(7,5)**2)

# Rational polygon strictly inside the upper circular boundary.
# floor(10^5 sqrt(U-x^2))/10^5 - d - 1/5000.
nodes=[]
for j in range(101):
    x=F(-1,2)+F(j,100)
    square=U-x*x
    height=F(isqrt((square.numerator*10**10)//square.denominator),10**5)
    c=height-d-F(1,5000)
    nodes.append((x,c))
check('top_minimum_height',min(c for x,c in nodes),'>',F(3,100))
check('top_maximum_height',max(c for x,c in nodes),'<',F(1,8))
check('top_endpoint_height',nodes[0][1],'<',F(31,1000))
check('polygon_vertices_radius_squared',max(x*x+(d+c)**2 for x,c in nodes),'<',U)
top=[]
for j,((x0,c0),(x1,c1)) in enumerate(zip(nodes,nodes[1:])):
    x,c=(x0+x1)/2,(c0+c1)/2
    slope=(c1-c0)/(x1-x0)
    rad=(x1-x0)/2
    rate,dx=simpson(x,c)
    dc=dc_simpson(x,c)
    # Interval for derivative of Phi+c*frequency_upper/A along this segment.
    terms=[slope*v for v in dc]
    derivative=(dx[0]+min(terms)+slope*frequency_upper/A,
                dx[1]+max(terms)+slope*frequency_upper/A)
    # Hessian norm of the two logarithmic distances is <=2/(d+c_min)^2.
    remainder=(1+slope*slope)*rad*rad/(d+min(c0,c1))**2
    upper=rate[1]+c*frequency_upper/A+max(map(abs,derivative))*rad+remainder
    top.append(dict(segment=j, endpoints=[[enc(x0),enc(c0)],[enc(x1),enc(c1)]],
                    midpoint_rate=[enc(v) for v in rate],
                    midpoint_gradient_c=[enc(v) for v in dc],
                    directional_derivative=[enc(v) for v in derivative],
                    taylor_remainder=enc(remainder),whole_segment_upper=enc(upper)))
check('top_full_bump_rate',max(F(r['whole_segment_upper']['numerator'],r['whole_segment_upper']['denominator']) for r in top),'<',F(203,10000))

contours={}
for label,c,threshold in [('bottom_density',F(-1,20),F(49,1000)),
                          ('side_lower_density',F(-11,100),F(80,1000))]:
    rows=[]
    for j in range(200):
        rad=F(1,400); x=-1+F(2*j+1,400)
        rate,dx=simpson(x,c)
        upper=rate[1]+max(map(abs,dx))*rad+rad*rad/(d+c)**2
        rows.append(dict(cell=j,midpoint=enc(x),rate=[enc(v) for v in rate],
                         derivative=[enc(v) for v in dx],whole_cell_upper=enc(upper)))
    bound=max(F(row['whole_cell_upper']['numerator'],row['whole_cell_upper']['denominator']) for row in rows)
    check(label+'_global_rate',bound,'<',threshold)
    contours[label]=rows

# The small left strip is used on both bridge horizontal edges.
side_rows=[]
for j in range(20):
    x=F(-51,100)+F(2*j+1,2000); rad=F(1,2000)
    rate,dx=simpson(x,F(0))
    upper=rate[1]+max(map(abs,dx))*rad+rad*rad/d**2
    side_rows.append(dict(cell=j,midpoint=enc(x),whole_cell_upper=enc(upper)))
side_phi=max(F(row['whole_cell_upper']['numerator'],row['whole_cell_upper']['denominator']) for row in side_rows)
check('left_strip_real_rate',side_phi,'<',F(37,2000))

# Certify dc Phi<=-0.39 on X in [-.51,-.49], c in [0,.031].
# The gradient of dc Phi has norm <=2/d^2; use L1 cell radii.
gradient_rows=[]
for j in range(10):
    x=F(-51,100)+F(2*j+1,1000)
    for k in range(16):
        c=F(31,1000)*F(2*k+1,32)
        dc=dc_simpson(x,c)
        upper=dc[1]+2/d**2*(F(1,1000)+F(31,32000))
        gradient_rows.append(dict(cell=[j,k],midpoint=[enc(x),enc(c)],
                                  derivative=[enc(v) for v in dc],whole_cell_upper=enc(upper)))
check('left_positive_height_c_derivative',max(F(row['whole_cell_upper']['numerator'],row['whole_cell_upper']['denominator']) for row in gradient_rows),'<',F(-39,100))
check('left_positive_height_bump_rate',F(37,2000)+F(31,1000)*(F(403,1000)-F(39,100)),'<',F(19,1000))
right,_=simpson(F(49,100),F(-1,10))
check('right_strip_all_height_rate',right[1],'<',F(-1,10))
check('right_positive_height_bump_rate',F(-1,10)+F(31,1000)*F(403,1000),'<',F(0))

# For the left strip dc Phi>=-D/(D^2+(.49)^2), D>=1.15.
check('negative_height_tail_rate_monotonicity',F(9,4)/A-F(23,20)/(F(23,20)**2+F(49,100)**2),'>',0)
check('bottom_high_frequency_rate',F(49,1000)-F(9,4)/(20*A),'<',F(1,100))
check('side_lower_high_frequency_rate',F(80,1000)-F(11,100)*F(9,4)/A,'<',0)
check('upper_bump_remainder_rate',F(-41,1000)+F(543,500)/18,'<',F(1,50))
check('top_rate_vs_endpoint',F(203,10000),'<',F(51,2500))
check('real_envelope_vs_endpoint',F(24,1000)-F(51,2500),'<',F(1,250))
check('bridge_vertical_distance',F(49,100)-Y,'>',0)
cosh10_lower=sum(F(10**(2*k),factorial(2*k)) for k in range(5))
check('bridge_center_barrier',2/cosh10_lower,'<',F(1,1000))
check('final_unit_exponent',F(1,250000),'<',F(1,100000))

result=dict(purpose='L711 full unit-maximum contour: exact auxiliary rates only',
            helper=dict(path=helper.name,sha256=hashlib.sha256(source.encode()).hexdigest(),functions=sorted(names)),
            arithmetic=dict(scale=scale,log_terms=40,simpson_panels=64),
            omega=[enc(v) for v in omega],top_segments=top,contour_cells=contours,
            left_real_cells=side_rows,left_c_derivative_cells=gradient_rows,
            right_rate=[enc(v) for v in right],checks=checks,
            failures=[name for name,row in checks.items() if not row['passed']],
            qualifications=['Not an audit of contour, Fourier, physical-tail or maximum-principle arguments',
                            'No bump-transform lower bound or B_sp decision',
                            'No effective angular arc or onset'])
path=Path(__file__).with_suffix('.json')
path.write_text(json.dumps(result,indent=2)+'\n')
for name,row in checks.items():
    print(f"{name}: actual {row['actual']['decimal_preview']:.12g} {row['relation']} required {row['required']['decimal_preview']:.12g}; pass={row['passed']}")
print(f"Checks: {len(checks)}; failures: {result['failures']}; certificate: {path}")
if result['failures']:
    raise SystemExit(1)
