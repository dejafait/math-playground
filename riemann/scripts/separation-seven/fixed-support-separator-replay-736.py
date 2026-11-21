#!/usr/bin/env python3
"""Exact original-atom cardinal-polynomial diagnostic after the736 stop.

No constructor import, Decimal assumption, inverse or moment enclosure.
Every original atom is evaluated by both integer product and Horner.
"""
from pathlib import Path
from hashlib import sha256
from fractions import Fraction as F
import json
import sys

sys.set_int_max_str_digits(0)
HERE = Path(__file__).resolve()
INPUT = HERE.with_name('fixed-support-gram-weights-736.json')
ANCHOR = HERE.with_name('fixed-support-shared-734.json')
OUT = HERE.with_suffix('.json')
data, anchor = [json.loads(p.read_text()) for p in [INPUT, ANCHOR]]
b = data['blocks'][0]
assert b['k']==11
J, labels = 2048, data['parameters']['labels']
indices = [J+(label*(J-1))//128 for label in labels]
chosen = min(range(35),key=lambda i:F(b['weights'][i]))
node = indices[chosen]
others = [j for i,j in enumerate(indices) if i!=chosen]
denom = 1
poly = [1]
for root in others:
    denom *= node-root
    nxt = [0]*(len(poly)+1)
    for a,c in enumerate(poly):
        nxt[a] -= root*c
        nxt[a+1] += c
    poly = nxt


def horner(j):
    value = 0
    for c in reversed(poly):
        value = value*j+c
    return value


cardinal = [F(horner(j),denom) for j in indices]
checks = {
    'numerical_script_hash':data['script_sha256']==sha256(HERE.with_name('fixed-support-gram-weights-736.py').read_bytes()).hexdigest(),
    'anchor_hash':data['input_hashes'][ANCHOR.name]==sha256(ANCHOR.read_bytes()).hexdigest(),
    'same_fixed35_labels':labels==anchor['parameters']['labels'] and len(set(labels))==35,
    'all_floor_indices_match':indices==b['indices'],
    'original_nodes_distinct_and_in_block':len(set(indices))==35 and all(J<=j<2*J for j in indices),
    'degree34_nonzero_denominator':len(poly)==35 and denom!=0,
    'all35_exact_cardinal_values':cardinal==[F(int(i==chosen)) for i in range(35)],
    'all2048_product_horner_values_agree':True}
I, norm2 = F(0), F(0)
values = []
for j in range(J,2*J):
    product = 1
    for root in others:
        product *= j-root
    value = horner(j)
    checks['all2048_product_horner_values_agree'] &= product==value
    p = F(value,denom)
    mass = F(16*J,(4*j+1)**2)
    I += mass*p
    norm2 += mass*p*p
    values.append(str(value))
checks['original_integral_below_minus_1_over1000'] = I < -F(1,1000)
checks['original_norm_squared_positive'] = norm2>0
checks['original_norm_squared_below_one'] = norm2<1
eps2 = I*I/norm2
checks['all_nonnegative_rules_residual_exceeds_1e_minus3'] = I<0 and eps2>F(1,1000)**2
checks['all_nonnegative_rules_exceed_required_residual'] = I<0 and eps2>F(5,10**19)**2
upper = F(b['weights'][chosen])+F(b['box_radii'][chosen])
checks['exact_integral_enclosed_by_numerical_solution_box'] = (
    F(b['weights'][chosen])-F(b['box_radii'][chosen]) <= I <= upper)
checks['solution_box_upper_below_minus_1_over1000'] = upper < -F(1,1000)
report = {
    'scope':'fixed35 labels at k11 only; exact nonnegative-rule residual obstruction',
    'script_sha256':sha256(HERE.read_bytes()).hexdigest(),
    'input_sha256':sha256(INPUT.read_bytes()).hexdigest(),
    'chosen_coordinate':chosen, 'chosen_label':labels[chosen], 'chosen_original_index':node,
    'polynomial_in_original_index':{'integer_coefficients_ascending':list(map(str,poly)),
        'common_denominator':str(denom), 'all35_cardinal_values':list(map(str,cardinal))},
    'original_atoms':{'first':J,'last':2*J-1,'count':J,
        'all_integer_polynomial_numerators':values},
    'exact_original_integral':str(I), 'exact_original_norm_squared':str(norm2),
    'exact_residual_squared_lower':str(eps2),
    'rigorous_small_bounds':{'integral_strict_upper':'-1/1000',
        'norm_squared_strict_upper':'1','all_nonnegative_rules_residual_strict_lower':'1/1000',
        'required_residual':'5/10000000000000000000'},
    'checks':checks,'failed_checks':[name for name,ok in checks.items() if not ok],
    'complete_work_upper':None,'peak_bytes_upper':None}
OUT.write_text(json.dumps(report,indent=2)+'\n')
print('Exact cardinal polynomial: coordinate',chosen,'label',labels[chosen],'; original node',node)
print('Original atoms verified:',J,'; candidate cardinal values:35; checks:',sum(checks.values()),'/',len(checks))
print('Certified I<-1/1000, 0<norm^2<1; every nonnegative rule on SAME35 nodes has epsilon>1/1000')
print('Required epsilon<=5e-19; failures:',report['failed_checks'])
print('Certificate:',OUT.relative_to(HERE.parents[2]),'; bytes:',OUT.stat().st_size,'; full cost/storage upper UNPAID')
if report['failed_checks']:
    raise SystemExit(1)
