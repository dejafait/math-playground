"""Exact rate obstruction to absolute horizontal-contour residue isolation.

This certifies the auxiliary inequalities proved and applied in L713.
It does not bound the signed contour integral or the actual Jensen defect.
"""
import ast
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path

helper = Path(__file__).with_name('spatial-complex-phase-166.py')
source = helper.read_text()
names = {'ceildiv', 'fixed', 'log_unit', 'logq'}
definitions = [node for node in ast.parse(source).body
               if isinstance(node, ast.FunctionDef) and node.name in names]
assert {node.name for node in definitions} == names
ns = dict(F=F, SCALE=1 << 100, TERMS=40)
exec(compile(ast.Module(body=definitions, type_ignores=[]), str(helper), 'exec'), ns)
ns['LOG2'] = ns['log_unit'](2, 1)
logq, scale = ns['logq'], ns['SCALE']
d, R, U, A = F(5,4), F(11,8), F(121,64), F(27,10)
p, q, pole_c, test_x = F(3,10), F(2,5), F(1,8), F(-1,5)
panels = 64

def enc(value):
    value = F(value)
    return dict(numerator=value.numerator, denominator=value.denominator,
                decimal_preview=float(value))

checks = {}
def check(name, actual, relation, required):
    actual, required = F(actual), F(required)
    passed = {'<': actual < required, '>': actual > required,
              '=': actual == required, '<=': actual <= required}[relation]
    checks[name] = dict(actual=enc(actual), relation=relation,
                        required=enc(required), passed=passed)

def q_squared(t,x,c):
    D=d+c
    return (((d+p*t)**2+(q*t)**2)*((U*p+D*t)**2+(U*q-x*t)**2)
            / (((U*p+d*t)**2+(U*q)**2)*((D+p*t)**2+(q*t-x)**2)))

def rate(x,c):
    lo=hi=0
    for j in range(panels+1):
        weight=1 if j in (0,panels) else 4 if j%2 else 2
        ll,lh=logq(q_squared(F(j,panels),x,c))
        lo+=weight*ll
        hi+=weight*lh
    error=F(400,45*panels**4)
    return (F(lo,6*panels*scale)-error,
            F(hi,6*panels*scale)+error)

# At c=1/8 and x in {-1/5,0}, lower moduli of the four affine
# t factors are d, U/2, U/2, R. Their slope moduli are at most
# 1/2, d, 7/5, 1/2, respectively.
check('third_slope_squared', R**2+test_x**2, '<', F(7,5)**2)
fourth=6*((F(1,2)/d)**4+(d/(U/2))**4
          +(F(7,5)/(U/2))**4+(F(1,2)/R)**4)
check('log_fourth_t_derivative',fourth,'<',400)
omega=tuple(A*(F(logq(F(9,5))[k],scale)-F(4,5)
               +F(121,100)*F(logq(F(201,121))[k],scale)) for k in (0,1))
peak_product=rate(F(0),pole_c)
line_product=rate(test_x,pole_c)
peak_rate=(peak_product[0]+pole_c*omega[0]/A,
           peak_product[1]+pole_c*omega[1]/A)
line_rate=(line_product[0]+pole_c*omega[0]/A,
           line_product[1]+pole_c*omega[1]/A)
bump_peak_upper=peak_rate[1]+pole_c*F(1,3000)/A
check('candidate_bump_residue_upper_rate',bump_peak_upper,'<',F(1,5000))
check('horizontal_line_witness_lower_rate',line_rate[0],'>',F(7,1000))

# Enclose the full double rectangle, not just point samples.
# Positive t,c factors make the following interval quotients valid.
nt=256
nc=176
c_lo,c_hi=pole_c,F(3,2)
rows=[]
for j in range(nc):
    cl=c_lo+(c_hi-c_lo)*F(j,nc)
    ch=c_lo+(c_hi-c_lo)*F(j+1,nc)
    Dl,Dh=d+cl,d+ch
    total=F(0)
    pieces=[]
    for k in range(nt):
        tl,th=F(k,nt),F(k+1,nt)
        positive_lower=tl*(U*p+Dl*tl)/((U*p+Dh*th)**2+(U*q+th/5)**2)
        negative_upper=(Dh+p*th)/((Dl+p*tl)**2+(q*tl+F(1,5))**2)
        lower=F(ns['fixed'](positive_lower-negative_upper)[0],scale)
        total+=lower/nt
        pieces.append(enc(lower))
    lower=total+omega[0]/A
    rows.append(dict(c_interval=[enc(cl),enc(ch)],
                     integrated_derivative_lower=enc(lower),
                     t_cell_integrand_lower=pieces))
monotone_min=min(F(row['integrated_derivative_lower']['numerator'],
                   row['integrated_derivative_lower']['denominator']) for row in rows)
check('whole_rectangle_centered_rate_derivative',monotone_min,'>',F(1,100))
check('all_c_ge_3_over_2_derivative',omega[0]/A-1/(d+F(3,2)),'>',F(1,100))
check('certified_absolute_rate_gap',F(7,1000)-F(1,5000),'>',F(3,500))

result=dict(purpose=__doc__,
            arithmetic='Exact Fractions and integer-directed rational logarithms; no floating-point decisions',
            helper=dict(path=helper.name,sha256=hashlib.sha256(source.encode()).hexdigest(),
                        functions=sorted(names)),
            parameters=dict(center=[enc(p),enc(q)],test_x=enc(test_x),pole_height=enc(pole_c),
                            simpson_panels=panels,t_cells=nt,c_cells=nc),
            rate_enclosures=dict(omega=[enc(v) for v in omega],
                                 peak_product=[enc(v) for v in peak_product],
                                 line_product=[enc(v) for v in line_product],
                                 peak_centered=[enc(v) for v in peak_rate],
                                 line_centered=[enc(v) for v in line_rate]),
            monotonicity_cells=rows,checks=checks,
            failures=[name for name,row in checks.items() if not row['passed']],
            qualifications=['Only an absolute-contour certificate obstruction',
                            'No lower bound for the signed contour integral',
                            'No asymptotic for complete G_n or positive lower bound for J_sp',
                            'All limiting and fixed-profile arguments are written in L713'])
path=Path(__file__).with_suffix('.json')
path.write_text(json.dumps(result,indent=2)+'\n')
for name,row in checks.items():
    print(f"{name}: actual {row['actual']['decimal_preview']:.12g} "
          f"{row['relation']} required {row['required']['decimal_preview']:.12g}; pass={row['passed']}")
print(f"Checks: {len(checks)}; failures: {result['failures']}; full certificate: {path}")
if result['failures']:
    raise SystemExit(1)
