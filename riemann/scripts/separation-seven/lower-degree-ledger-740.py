#!/usr/bin/env python3
"""Incomplete but explicit source-work/storage inventory. No cost pass.

Only disjoint source operations are counted; integer/Decimal internals,
allocation, output, other control and replay/old production remain unpaid.
File bytes are actual disk sizes, not peak working-memory upper bounds.
"""
from pathlib import Path
from hashlib import sha256
from fractions import Fraction as F
from decimal import Decimal as D, Context
import json
HERE=Path(__file__).resolve(); OUT=HERE.with_suffix('.json')
CON=HERE.with_name('lower-degree-fixed-740.json')
REP=HERE.with_name('lower-degree-replay-740.json')
c=json.loads(CON.read_text()); r=json.loads(REP.read_text())
n=c['counts_lower_subtotals']
# Five per scalar dot/update: multiply, add/subtract, accumulator/entry
# store, loop-variable binding and successful loop advance.
# Nine per Gram term: four directed arithmetic, scale's c binding,
# sign comparison, k binding+advance, and outer value binding.
constructor=5*sum(n[k] for k in ('householder_dot_tail_terms','householder_update_tail_terms','gradient_terms','triangular_terms'))+9*n['gram_product_terms']
# Replay term: c,r,a,b bindings4; advance1; two sign tests2;
# two multiplications+two additions4; lo,hi stores2.
replay=13*r['gram_product_terms']
# C998w Section4 source-only production lower bounds for the3 retained
# rules; inverse updates and candidate Gram arithmetic are disjoint.
old=3*(4*499800+578565)
subtotal=constructor+replay+old
assert subtotal==51546118
ctx=Context(prec=16)
def scientific(s):
    f=F(s); return str(ctx.divide(D(f.numerator),D(f.denominator)))
files=[CON,REP]+[HERE.with_name('support-grid-nnls-731-k'+str(k)+'.json') for k in (8,9,10)]
report={'script_sha256':sha256(HERE.read_bytes()).hexdigest(),'input_hashes':{p.name:sha256(p.read_bytes()).hexdigest() for p in files},'work':{'new_constructor_disjoint_lower':constructor,'new_independent_replay_disjoint_lower':replay,'old_three_rules_production_disjoint_lower':old,'mandatory_disjoint_lower_subtotal':subtotal,'required_upper_cap':10**8,'complete_upper_bound':None,'decision':'UNRESOLVED: a lower subtotal below cap is neither a pass nor a stop','unpriced':['all original moment and Bernoulli preparation','remaining NNLS/Gram/inverse/residual arithmetic and control','integer/Fraction/Decimal internals','256 retained atoms and all earlier coefficient production outside the displayed old subtotal','allocation, copying, output, source binding, replay and ledger work','all byte-storage peak bounds']},'storage':{'certificate_file_bytes':{p.name:p.stat().st_size for p in files},'these_file_bytes_sum':sum(p.stat().st_size for p in files),'new_constructor_retained_gram_error_endpoints':61*29*29*2,'new_constructor_retained_moment_endpoints':61*57*2,'new_rule_weights':61*35,'peak_entries_upper':None,'peak_working_bytes_upper':None,'qualification':'actual certificate sizes and retained entry subinventory only; no complete working-memory bound'},'result_summary':{'blocks':61,'positive_nodes_each':29,'kernel_rank':2130,'uniform_B2_error_upper':'7.291e-8','required_uniform_B2_error':'1e-7','epsilon_squared_max':scientific(r['extrema_exact']['epsilon_squared']),'required_epsilon_squared':'2.5e-37','contraction_max':scientific(r['extrema_exact']['contraction']),'required_contraction':'<1','checks':r['checks'],'replay_failures':r['failures']}}
OUT.write_text(json.dumps(report,indent=2)+'\n')
print('WORK disjoint LOWER',subtotal,'required UPPER <=',10**8,'decision UNRESOLVED; full/peak bytes upper unknown')
print('STORAGE actual certificate bytes',report['storage']['these_file_bytes_sum'],'paths',OUT)
print('RESIDUAL actual squared max',report['result_summary']['epsilon_squared_max'],'required <=2.5e-37; all61 certified; B^2 error<7.291e-8 required<=1e-7')
