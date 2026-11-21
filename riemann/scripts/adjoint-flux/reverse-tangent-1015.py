#!/usr/bin/env python3
"""Exact arithmetic for C467g; does not verify its analytic arguments."""
from fractions import Fraction as F
from pathlib import Path
import json

a, b, r, eta = F(101, 100), F(1, 32), F(9, 10), F(1, 96)
d2, d3, d4, d5, d6 = F(40), F(400, 9), F(8000, 81), F(80000, 243), F(3200000, 2187)
v1 = d2*a
v2 = d3*a*a+d2*b
v3 = d4*a**3+3*d3*a*b
f4 = d4*a**4+6*d3*a*a*b+3*d2*b*b
f5 = d5*a**5+10*d4*a**3*b+15*d3*a*b*b
f6 = d6*a**6+15*d5*a**4*b+45*d4*a*a*b*b+15*d3*b**3
vB = v2+r*v3/2
EE = [
    [3*d2, 3*eta*d2+vB, v3/2],
    [3*eta*d2+vB, 3*eta**2*d2+2*eta*vB+(r*r*f6+10*r*f5+20*f4)/120,
     eta*v3/2+(r*f6+5*f5)/120],
    [v3/2, eta*v3/2+(r*f6+5*f5)/120, f6/120],
]
EP = [
    [d2, F(19,10)*d2, F(4,5)*d2],
    [eta*d2+vB/3, eta*F(19,10)*d2+2*v1+5*r*v2/2+r*r*v3/2,
     eta*F(4,5)*d2+F(2,5)*v2+F(9,50)*v3],
    [v3/6, 3*v2/2+r*v3/2, 3*v1+3*r*v2+v3/5],
]
frobsq = lambda mat: sum(x*x for row in mat for x in row)
W = F(1,64)
sing4, sing5, sing6 = 128*6*W**4, 128*24*W**5, 128*120*W**6
SEE = [
    [F(0),F(0),F(0)],
    [F(0),(r*r*sing6+10*r*sing5+20*sing4)/120,(r*sing6+5*sing5)/120],
    [F(0),(r*sing6+5*sing5)/120,sing6/120],
]
t1,t2,t3 = 128*W, 128*2*W**2, 128*6*W**3
SEP = [
    [F(0),F(0),F(0)],
    [F(0),t2+r*t3/2,2*t1+5*r*t2/2+r*r*t3/2],
    [F(0),t3/2,3*t2/2+r*t3/2],
]
background_PP = 40*F(133,75)
singular_PP = 256*F(1,16)*F(21,5)
growth = F(211)+2*F(392,5)+F(139,25)
horizon = growth/1920
checks = []
def check(name, actual, required):
    checks.append({'name':name,'actual':str(actual),'required_strict_upper':str(required),'passed':actual<required})
check('background_EE_Frobenius_squared', frobsq(EE), F(210**2))
check('background_EP_Frobenius_squared', frobsq(EP), F(387**2))
check('singular_EE_Frobenius_squared', frobsq(SEE), F(1))
check('singular_EP_Frobenius_squared', frobsq(SEP), F(25))
check('total_PP', background_PP+singular_PP, F(139))
check('Riccati_growth', growth, F(384))
check('horizon_graph_derivative', horizon, F(1,5))
check('scaled_W',F(119,7680),W)
check('scaled_product_squared',F(4,125),F(9,50)**2)
check('sum_abs_s_squared',F(18,5),F(19,10)**2)
check('phase_bound',F(95951,64000),F(3,2))

def encode(value):
    if isinstance(value,F): return str(value)
    if isinstance(value,list): return [encode(x) for x in value]
    if isinstance(value,dict): return {k:encode(v) for k,v in value.items()}
    return value
certificate = encode({
    'scope':'Exact rational majorant arithmetic only; analytic identities, ODE continuation and source hypotheses require the canonical proof.',
    'derivative_bounds':{'a':a,'b':b,'r':r,'eta':eta,'d2':d2,'d3':d3,'d4':d4,'d5':d5,'d6':d6,
                         'v1':v1,'v2':v2,'v3':v3,'f4':f4,'f5':f5,'f6':f6},
    'background':{'EE_entry_bounds':EE,'EP_entry_bounds':EP,'EE_Frobenius_squared':frobsq(EE),
                  'EP_Frobenius_squared':frobsq(EP),'PP_operator_bound':background_PP},
    'singular':{'EE_entry_bounds':SEE,'EP_entry_bounds':SEP,'EE_Frobenius_squared':frobsq(SEE),
                'EP_Frobenius_squared':frobsq(SEP),'PP_operator_bound':singular_PP},
    'total':{'EE_operator_bound':211,'EP_operator_bound':392,'PP_operator_bound':139,
             'growth_bound':growth,'horizon_graph_bound':horizon,'required_graph_bound':F(1,5)},
    'checks':checks,'failures':[x['name'] for x in checks if not x['passed']],
})
out=Path(__file__).with_suffix('.json')
out.write_text(json.dumps(certificate,indent=2)+'\n')
print(f"Checks: {len(checks)}; failures: {len(certificate['failures'])}")
for x in checks:
    print(f"{x['name']}: actual={x['actual']}; required < {x['required_strict_upper']}; passed={x['passed']}")
print(f'Certificate: {out}')
if certificate['failures']: raise SystemExit(1)
