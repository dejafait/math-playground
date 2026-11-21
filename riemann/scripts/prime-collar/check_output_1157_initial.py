#!/usr/bin/env python3
"""Current-step exact rational checks of the whole saved rectangle sum.

This is calculation verification, not the later independent proof audit.
"""
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path

here = Path(__file__).resolve().parent
source = here/'certificate-1157.json'
c = json.loads(source.read_text())
nodes = c['nodes']
P = c['quadrature']['panels_per_octave']
first, last = c['quadrature']['first_exponent'], c['quadrature']['last_exponent']
checks = {
    'expected_mesh':(first,last,P)==(-24,4,2048),
    'complete_node_count':len(nodes)==(last-first)*P+1==57345,
    'no_original_verification_failure':c['verification_failures']==[],
    'all_original_claims':all(c['claims'].values()),
    'decision_positive':c['decision']=='STRICT_POSITIVE_MINIMUM',
}
lo_sums, hi_sums = [F(0)]*4, [F(0)]*4
node_intervals_ordered = True
node_values_positive = True
mesh_exact = True
blocks_valid = True
previous_values = [tuple(map(F,v)) for v in nodes[0]['values']]
mesh_exact = tuple(map(F,nodes[0]['s'])) == (F(1,2**24),)*2
index = 0
for exp in range(first,last):
    scale = F(2)**exp
    width = scale/P
    for panel in range(1,P+1):
        index += 1
        node = nodes[index]
        expected_s = scale*(P+panel)/P
        mesh_exact = mesh_exact and tuple(map(F,node['s']))==(expected_s,expected_s)
        values = [tuple(map(F,v)) for v in node['values']]
        for j, ((lo,hi),(prev_lo,prev_hi)) in enumerate(zip(values,previous_values)):
            node_intervals_ordered = node_intervals_ordered and lo<=hi
            node_values_positive = node_values_positive and lo>0
            lo_sums[j] += width*lo
            hi_sums[j] += width*prev_hi
        previous_values = values
    block = c['cumulative_octave_bounds'][exp-first]
    blocks_valid = blocks_valid and block['octave_exponent']==exp
    for j in range(4):
        b_lo = F(block['cumulative_lower'][j][0])
        b_hi = F(block['cumulative_upper'][j][1])
        blocks_valid = blocks_valid and b_lo<=lo_sums[j]<=hi_sums[j]<=b_hi
checks.update(all_mesh_nodes_exact=mesh_exact, all_node_intervals_ordered=node_intervals_ordered,
              all_node_values_positive=node_values_positive, all_28_cumulative_blocks_valid=blocks_valid)

EE, EM, MM = [tuple(map(F,v)) for v in (c['matrix'][0][0],c['matrix'][0][1],c['matrix'][1][1])]
threshold = tuple(map(F,c['required_threshold']))
# Printed endpoints were themselves rounded outward. Compute independently
# with these slightly wider rational input intervals, never binary64.
minimum_lo = EE[0]-EM[0]**2/MM[0]-threshold[1]
minimum_hi = EE[1]-EM[1]**2/MM[1]-threshold[0]
checks.update(
    matrix_symmetric=c['matrix'][0][1]==c['matrix'][1][0],
    response_strict_positive=MM[0]>0,
    cross_strict_negative=EM[1]<0,
    exact_minimum_lower_gt_00083852=minimum_lo>F('0.00083852'),
    exact_minimum_upper_lt_00092782=minimum_hi<F('0.00092782'),
    minimum_dump_lower_gt_00083852=F(c['minimum_margin'][0])>F('0.00083852'),
    minimum_dump_upper_lt_00092782=F(c['minimum_margin'][1])<F('0.00092782'),
    small_domain_w=F(c['geometry']['w'][0])>F(1,2**24),
    small_domain_middle=F(c['geometry']['middle_length'][0])>F(1,2**24),
)
for name, interval, lo, hi in [
    ('EE',EE,'0.29695626','0.29704288'),
    ('EM',EM,'-0.11841990','-0.11837759'),
    ('MM',MM,'4.26144969','4.26187214'),
    ('threshold',threshold,'0.29282701','0.29282702'),
    ('amplitude',tuple(map(F,c['minimizing_amplitude'])),'0.02777596','0.02778865')]:
    checks[name+'_display_bound'] = F(lo)<interval[0]<=interval[1]<F(hi)
failures = [name for name,ok in checks.items() if not ok]
output = {
    'scope':'Current-step complete exact-rational output/sum check; independent conceptual audit remains pending.',
    'certificate_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
    'check_script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'checked_nodes':len(nodes),'checked_panels':len(nodes)-1,
    'checked_integrand_intervals':4*len(nodes), 'checked_cumulative_blocks':len(c['cumulative_octave_bounds']),
    'checks':checks,'failures':failures,
    'independent_exact_rational_minimum_bounds':{
        'lower_numerator':str(minimum_lo.numerator),'lower_denominator':str(minimum_lo.denominator),
        'upper_numerator':str(minimum_hi.numerator),'upper_denominator':str(minimum_hi.denominator)},
    'display_minimum':['0.00083852','0.00092782'],
    'required_allocation_margin':'>=0',
}
path=here/'certificate-output-check-1157.json'
path.write_text(json.dumps(output,indent=2)+'\n')
print('Exact rational checks:',sum(checks.values()),'required:',len(checks),'; failures:',failures)
print('Checked all',len(nodes),'nodes and',len(c['cumulative_octave_bounds']),'cumulative blocks.')
print('Minimum margin strictly between 0.00083852 and 0.00092782; required >=0.')
print('Full output-check certificate:',path)
if failures:
    raise SystemExit(1)
