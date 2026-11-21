#!/usr/bin/env python3
"""Static mandatory-work certificate for the unchanged731 numerical loops.

This does not run NNLS, assume its success, generate quadrature weights,
or claim a lower bound for optimized/different algorithms. A successful
61-block extension preserving these loops necessarily exceeds the cap.
"""
import ast
from hashlib import sha256
import json
from pathlib import Path

HERE = Path(__file__).resolve()
SOURCE = HERE.with_name('support-grid-nnls-731.py')
OUT = HERE.with_suffix('.json')
source = SOURCE.read_text()
tree = ast.parse(source)
checks = []


def check(name, condition):
    checks.append({'name': name, 'passed': bool(condition)})


def expression(node):
    return ast.unparse(node)


def same(node, text):
    return ast.dump(node, include_attributes=False) == ast.dump(
        ast.parse(text, mode='eval').body, include_attributes=False)


def one(nodes):
    assert len(nodes) == 1, 'source shape changed; static argument must be reviewed'
    return nodes[0]


parameters = one([n for n in tree.body if isinstance(n, ast.Assign)
                  and expression(n.targets[0]) == '(J, DEG, NC, PREC)'])
check('fixed degree34 candidate129 precision80',
      same(parameters.value, '(2 ** K, 34, 129, 80)'))
dim_assignment = one([n for n in tree.body if isinstance(n, ast.Assign)
                      and expression(n.targets[0]) == 'dim'])
check('validation dimension is degree plus one', same(dim_assignment.value, 'DEG + 1'))
solve = one([n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == 'solve'])
n_assignment = one([n for n in solve.body if isinstance(n, ast.Assign)
                    and expression(n.targets[0]) == 'n'])
check('solve dimension is active list length', same(n_assignment.value, 'len(active)'))
kloop = one([n for n in solve.body if isinstance(n, ast.For)
             and expression(n.target) == 'k'])
iloop = one([n for n in kloop.body if isinstance(n, ast.For)
             and expression(n.target) == 'i'])
jloop = one([n for n in iloop.body if isinstance(n, ast.For)
             and expression(n.target) == 'j'])
check('elimination outer range', same(kloop.iter, 'range(n)'))
check('elimination row range', same(iloop.iter, 'range(k + 1, n)'))
check('elimination column range includes rhs', same(jloop.iter, 'range(k + 1, n + 1)'))
update = one([n for n in jloop.body if isinstance(n, ast.AugAssign)
              and expression(n.target) == 'a[i][j]'])
check('one multiply subtract store per inner update',
      isinstance(update.op, ast.Sub) and same(update.value, 'factor * a[k][j]'))
check('no conditional or early loop exit in successful elimination',
      not any(isinstance(n, (ast.Break, ast.Continue, ast.Return, ast.If))
              for n in ast.walk(iloop)))
inverse = one([n for n in ast.walk(tree) if isinstance(n, ast.Assign)
               and expression(n.targets[0]) == 'inverse_columns'])
expected = '[solve(hd, [D(int(i == j)) for i in range(dim)], list(range(dim))) for j in range(dim)]'
check('inverse repeats full dimension solve for every column', same(inverse.value, expected))
gram_loop = one([n for n in ast.walk(tree) if isinstance(n, ast.For)
                 and expression(n.target) == 'j' and same(n.iter, 'range(i + 1)')])
gram_value = one([n for n in gram_loop.body if isinstance(n, ast.Assign)
                 and expression(n.targets[0]) == 'value'])
check('candidate gram entry sums35 scalar products', same(
    gram_value.value, 'sum((a[i][k] * a[j][k] for k in range(DEG + 1)), D(0))'))
gram_parent = one([n for n in ast.walk(tree) if isinstance(n, ast.For)
                  and gram_loop in n.body])
check('candidate gram has129 triangular rows', same(gram_parent.iter, 'range(NC)'))

d, nc = 35, 129
per_solve = sum(1 for k in range(d) for i in range(k+1, d)
                for j in range(k+1, d+1))
closed = d*(d-1)*(d+1)//3
check('enumerated elimination updates match closed form', per_solve == closed == 14280)
inverse_updates = d*per_solve
all_blocks = list(range(8, 72))
remaining = list(range(11, 72))
check('three completed plus61 remaining blocks cover all64',
      list(range(8, 11))+remaining == all_blocks and len(remaining) == 61)
source_units = {'scalar_multiplication': 1, 'scalar_subtraction': 1,
                'successful_inner_loop_advance': 1,
                'inner_loop_variable_binding': 1}
work_remaining = len(remaining)*inverse_updates*sum(source_units.values())
work_all = len(all_blocks)*inverse_updates*sum(source_units.values())
check('remaining61 inverse subtask alone above cap', work_remaining > 10**8)
# Independently, omit every source control/store cost. Count only the
# 35 products and at least34 additions in each candidate Gram entry,
# and two arithmetic operations per elimination inner update.
gram_entries = nc*(nc+1)//2
arithmetic_gram = gram_entries*(d+(d-1))
arithmetic_inverse = 2*inverse_updates
arithmetic_all = len(all_blocks)*(arithmetic_gram+arithmetic_inverse)
check('all64 selected arithmetic alone above cap', arithmetic_all > 10**8)

report = {
    'scope': 'specific731 Gram and repeated-inverse loops; conditional on successful full-block extension preserving these loops; not a universal complexity lower bound',
    'audit_script_sha256': sha256(HERE.read_bytes()).hexdigest(),
    'source_sha256': sha256(SOURCE.read_bytes()).hexdigest(),
    'source_excerpts': {
        'solve': ast.get_source_segment(source, solve),
        'inverse_columns': ast.get_source_segment(source, inverse),
        'candidate_gram_loop': ast.get_source_segment(source, gram_parent),
        'parameter_assignment': ast.get_source_segment(source, parameters),
        'dimension_assignment': ast.get_source_segment(source, dim_assignment)},
    'parameters': {'degree': 34, 'dimension': d, 'candidates': nc,
                   'all_blocks_k': all_blocks, 'remaining_blocks_k': remaining,
                   'required_complete_work_cap': 10**8},
    'source_work': {
        'convention': 'C998v Section5: one scalar arithmetic/comparison, explicit binding/store, or successful loop advance is at least one unit',
        'updates_per_dimension35_solve': per_solve,
        'separate_full_solves_per_inverse': d,
        'updates_per_block_inverse': inverse_updates,
        'distinct_counted_units_per_inner_update': source_units,
        'remaining61_lower_bound': work_remaining,
        'all64_lower_bound': work_all,
        'required_cap': 10**8, 'passes_cap': False,
        'excluded': ['matrix entry update stores', 'solve_steps counter instrumentation', 'pivot search and guards',
                     'division for factors', 'back substitution', 'all other loops and stores',
                     'moment preparation', 'NNLS candidate solves', 'inverse residual validation',
                     'prefix generation', 'storage reporting replay and scalar work']},
    'independent_arithmetic_only': {
        'triangular_gram_entries': gram_entries,
        'products_per_gram_entry': d, 'conservative_additions_per_gram_entry': d-1,
        'gram_arithmetic_per_block': arithmetic_gram,
        'inverse_inner_arithmetic_per_block': arithmetic_inverse,
        'all64_lower_bound': arithmetic_all, 'required_cap': 10**8,
        'passes_cap': False},
    'mathematical_status': {
        'large_block_moments_or_weights_generated': False,
        'existing_three_rules_revalidated': False,
        'all_block_residual_or_actual_error_claimed': False,
        'byte_storage_upper_bound_certified': False,
        'three_existing_rules_are_invalidated': False,
        'all_residual_constructions_are_excluded': False},
    'checks': checks, 'failed_checks': [v['name'] for v in checks if not v['passed']]}
OUT.write_text(json.dumps(report, indent=2)+'\n')
print('Static source/count checks:', sum(v['passed'] for v in checks), '/', len(checks))
print('Remaining61 inverse-only source-work lower bound:', work_remaining, '; cap:', 10**8)
print('All64 conservative selected-arithmetic lower bound:', arithmetic_all, '; cap:', 10**8)
print('Failures:', report['failed_checks'])
print('Certificate:', OUT.relative_to(HERE.parents[2]))
print('Large-block residuals and memory unverified; three prior certificates preserved.')
if report['failed_checks']:
    raise SystemExit(1)
