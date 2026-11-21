#!/usr/bin/env python3
"""Replay all saved expanded-block products and interval LDL operations.

This checks every relevant saved operand, not just a preview, and does
not independently audit analytic lemmas or reconstruct coefficient maps.
"""
import hashlib
import importlib.util
import json
from fractions import Fraction as F
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('matrix488',HERE/'matrix-enclosure-488.py')
p = importlib.util.module_from_spec(spec)
spec.loader.exec_module(p)
m, B, S = p.m, p.B, p.S
data = json.loads((HERE/'matrix-enclosure-488.json').read_text())
old = json.loads((HERE/'matrix-enclosure-487.json').read_text())
indices = data['indices']
size = len(indices)
checks = {
    'exact_indices':indices==list(p.INDICES),
    'same_precision':int(data['interval_denominator'])==S and data['precision_bits']==2048,
    'both_complete_signs':data['completed_signs']==['-1','1'],
    'coefficient_artifact_sha256':hashlib.sha256(
        (HERE.parent.parent/data['coefficient_artifact']).read_bytes()).hexdigest()
        ==data['coefficient_artifact_sha256'],
    'source_coefficient_artifact_sha256':hashlib.sha256(
        (HERE/'matrix-coefficients-487.json.gz').read_bytes()).hexdigest()
        ==data['source_coefficient_artifact_sha256'],
}
def decode(matrix):
    return [[p.ball(x) for x in row] for row in matrix]

def overlap(x,y):
    return x.lo<=y.hi and y.lo<=x.hi

bounds = {}
for sign in ('-1','1'):
    d = data['signs'][sign]
    projected, head, gram, cov, schur = [decode(d[key]) for key in
        ('projected_moments','unsymmetrized_head','total_gram','complete_covariance','schur')]
    checks[sign+'_all_257_projection_rows'] = len(projected)==size and all(
        len(row)==257 for row in projected)
    checks[sign+'_all_17_by_17_operands'] = all(len(mat)==size and all(
        len(row)==size for row in mat) for mat in (head,gram,cov,schur))
    ratios = [p.ball(x) for x in data['ratios']]
    head_replay = [[projected[j][n]-ratios[i]*projected[j][n%2]
                    for j in range(size)] for i,n in enumerate(indices)]
    cov_replay = [[gram[i][j]-m.interval_dot(projected[i],projected[j])
                   for j in range(size)] for i in range(size)]
    schur_replay = [[(head_replay[i][j]+head_replay[j][i]).integer_div(2)
                     -cov_replay[i][j]*B.rational(250,171)
                     for j in range(size)] for i in range(size)]
    for key,computed,saved in (('head',head_replay,d['unsymmetrized_head']),
                               ('covariance',cov_replay,d['complete_covariance']),
                               ('schur',schur_replay,d['schur'])):
        checks[sign+'_every_'+key+'_endpoint'] = p.encode(computed)==saved
    checks[sign+'_symmetric_enclosures'] = all(
        schur[i][j].json()==schur[j][i].json() for i in range(size) for j in range(size))
    ldl = p.shifted_ldl(schur,B.rational(1,25))
    checks[sign+'_every_ldl_operand'] = ldl==d['shifted_ldl']
    checks[sign+'_every_ldl_pivot_positive'] = ldl['passed'] and len(ldl['pivots'])==size and all(
        p.ball(x).lo>0 for x in ldl['pivots'])
    # Report exact interval operands; no decimal pivot decides a check.
    width = F(max(x.hi-x.lo for mat in (head,gram,cov,schur) for row in mat for x in row),S)
    pivot = F(min(p.ball(x).lo for x in ldl['pivots']),S)
    checks[sign+'_exact_width_operand'] = m.scalar.frac_json(width)==d['maximum_matrix_interval_width']
    checks[sign+'_exact_minimum_pivot_operand'] = m.scalar.frac_json(pivot)==d['minimum_pivot_lower']
    checks[sign+'_arithmetic_width_below_1e_minus_30'] = width<F(1,10**30)
    checks[sign+'_reported_width_below_1_046e_minus_236'] = width<F(1046,10**239)
    checks[sign+'_reported_conservative_pivot_lower'] = pivot>(
        F(2947,10000) if sign=='-1' else F(6492,10000))
    checks[sign+'_all_old_projection_endpoints'] = all(
        projected[indices.index(n)][k].json()==old['signs'][sign]['projected_moments'][i][k]
        for i,n in enumerate(old['indices']) for k in range(257))
    checks[sign+'_all_old_matrix_entries_overlap'] = all(
        overlap(mat[indices.index(n)][indices.index(other)],p.ball(old['signs'][sign][key][i][j]))
        for key,mat in (('unsymmetrized_head',head),('total_gram',gram),
                        ('complete_covariance',cov),('schur',schur))
        for i,n in enumerate(old['indices']) for j,other in enumerate(old['indices']))
    bounds[sign] = {'minimum_pivot_lower':m.scalar.frac_json(pivot),
                   'maximum_matrix_width':m.scalar.frac_json(width),
                   'certified_principal_lower_bound':m.scalar.frac_json(F(1,25))}
    print(f'sign{sign}: all17 shifted pivots positive={ldl["passed"]}; '
          f'min pivot lower={float(pivot):.12g}; width<={m.scalar.up(width)}')
result = {'scope':'Every saved17 by17 matrix operation and LDL operand; not analytic input proofs.',
    'checks':checks,'exact_bounds':bounds,'failures':[k for k,v in checks.items() if not v],
    'full_two_sign_margin_certified':False}
path = Path(__file__).with_suffix('.json')
path.write_text(json.dumps(result,indent=2)+'\n')
print(f'Expanded matrix replay: {sum(checks.values())}/{len(checks)}; failures {result["failures"]}')
print(f'Principal lower bounds1/25 only; full255-dimensional threshold remains unpaid. Evidence: {path}')
if result['failures']:
    raise SystemExit(1)
