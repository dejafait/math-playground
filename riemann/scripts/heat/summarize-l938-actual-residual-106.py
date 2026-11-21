#!/usr/bin/env python3
"""Interpret the fixed completed test; no new sign evaluation or refinement."""
import json
import sys
from decimal import Decimal,localcontext,ROUND_FLOOR,ROUND_CEILING
from fractions import Fraction as F
from pathlib import Path

sys.set_int_max_str_digits(0)
BASE=Path(__file__).resolve().parent
OUT=BASE/'l938-actual-residual-diagnostic-106.json'
r=json.loads((BASE/'l938-actual-residual-signed-integration-106.json').read_text())
audit=json.loads((BASE/'l938-actual-residual-signed-integration-check-106.json').read_text())
nodes=json.loads((BASE/'l938-actual-residual-nodes-106.json').read_text())['nodes']
assert not r['failures'] and not audit['failures'] and audit['status']=='PASSED'


def pair(obj):
    return F(obj['lower']),F(obj['upper'])


checks=[]
def display(v):
    with localcontext() as ctx:
        ctx.prec=16
        ctx.rounding=ROUND_FLOOR
        lo=str(Decimal(v.numerator)/Decimal(v.denominator))
        ctx.rounding=ROUND_CEILING
        hi=str(Decimal(v.numerator)/Decimal(v.denominator))
    checks.append(F(lo)<=v<=F(hi))
    return dict(lower=lo,upper=hi)


quad=pair(r['result']['signed_quadrature'])
vp_lo=F(r['analytic']['polynomial_endpoint_lower'])
values=dict(actual_lower=F(r['result']['actual_lower']),actual_upper=F(r['result']['actual_upper']),
    polynomial_endpoint_lower=vp_lo,signed_quadrature_lower=quad[0],signed_quadrature_upper=quad[1],
    signed_quadrature_center=(quad[0]+quad[1])/2,
    signed_quadrature_radius=(quad[1]-quad[0])/2,
    quadrature_radius_to_endpoint=(quad[1]-quad[0])/(2*vp_lo),
    analytic_quadrature_error=F(r['analytic']['quadrature_error']),
    pointwise_complement=F(r['analytic']['complement']),
    second_order=F(r['analytic']['second_order']))
maximum=max(nodes,key=lambda row:F(row['amplitude']['upper'])-F(row['amplitude']['lower']))
idx=maximum['j']
selected={name:maximum[name] for name in
          ('j','energy','kernel','polynomial','residual','response','amplitude')}
summary={k:display(v) for k,v in values.items()}
assert all(checks)
out=dict(status='COMPLETE',sign=r['result']['sign'],summary=summary,
    exact={k:str(v) for k,v in values.items()},widest_amplitude_node=selected,
    display_checks=len(checks),display_failures=[],
    interpretation='Complete signed quadrature radius exceeds endpoint margin. '
    'No actual residual size, density sign, or impossibility of other methods follows.')
OUT.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(dict(status=out['status'],sign=out['sign'],summary=summary,
    widest_amplitude_node=idx,failures=[],certificate=str(OUT)),indent=2))
