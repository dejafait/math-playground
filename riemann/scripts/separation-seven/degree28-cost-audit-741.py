#!/usr/bin/env python3
"""Disjoint LOWER source-work certificate for the unchanged740 bundle.

No numerical rules are constructed, adapted or overwritten. Source work
means arithmetic/comparisons, explicit bindings (including parameters),
stores and successful loop advances, as in C998v Section5. This is not
CPU time or a bound on a redesigned implementation. Full certificate
contains source excerpts, branch counts, inventories and exclusions.
"""
import ast
import fractions
import hashlib
import inspect
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve()
OUT = HERE.with_suffix('.json')
BASE = HERE.parent
names = ['lower-degree-fixed-740.py', 'lower-degree-replay-740.py',
         'lower-degree-ledger-740.py', 'support-grid-nnls-731.py']
sources = {n: (BASE/n).read_text() for n in names}
trees = {n: ast.parse(s) for n, s in sources.items()}
con = json.loads((BASE/'lower-degree-fixed-740.json').read_text())
rep = json.loads((BASE/'lower-degree-replay-740.json').read_text())
ledger = json.loads((BASE/'lower-degree-ledger-740.json').read_text())
checks = {}
def check(name, condition):
    checks[name] = bool(condition)
    if not condition:
        raise AssertionError(name)
def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()
def function(tree, name):
    return next(n for n in ast.walk(tree) if isinstance(n, ast.FunctionDef) and n.name == name)
def canonical(s):
    return ast.dump(ast.parse(s), include_attributes=False)
def has(n, text):
    wanted = canonical(text)
    return any(canonical(ast.unparse(x)) == wanted for x in ast.walk(n) if isinstance(x, ast.stmt))

check('constructor_source_binding', con['script_sha256'] == digest(BASE/names[0]))
check('replay_source_binding', rep['script_sha256'] == digest(BASE/names[1]))
check('ledger_source_binding', ledger['script_sha256'] == digest(BASE/names[2]))
check('replay_input_binding', rep['input_sha256'] == digest(BASE/'lower-degree-fixed-740.json'))
check('all61_blocks', [b['k'] for b in con['blocks']] == list(range(11,72)))
check('successful_full_bundle', con['state'] == 'ALL_RESIDUALS_PASS_COST_UNCERTIFIED' and not con['failures'] and not rep['failures'])
check('all_solver_steps', all(b['solver']['main_visits'] == 30 and b['solver']['secondary_visits'] == 29 and b['solver']['state'] == 'RANK_LIMIT' for b in con['blocks']))

# Reproduce only the previously certified disjoint subtotal, not its
# numerical production. No new charge for these same operations below.
n = con['counts_lower_subtotals']
prior_constructor = 5*sum(n[k] for k in ('householder_dot_tail_terms','householder_update_tail_terms','gradient_terms','triangular_terms')) + 9*n['gram_product_terms']
prior_replay = 13*rep['gram_product_terms']
prior_old = 3*(4*499800+578565)
prior = prior_constructor + prior_replay + prior_old
check('old_subtotal_reproduced', prior == 51546118 == ledger['work']['mandatory_disjoint_lower_subtotal'])
check('gram_term_count', n['gram_product_terms'] == rep['gram_product_terms'] == 61*29**3)

# Every successful save exports every block already appended. The final
# else clause saves all61 blocks a second time. Ignore the initial empty
# report and all non-block report data. JSON preserves container shapes;
# exact Decimal/Fraction leaves became strings, not new containers.
export = function(trees[names[0]], 'export')
expected_export = '''
def export(v):
    if isinstance(v,(D,F)): return str(v)
    if isinstance(v,dict): return {k:export(x) for k,x in v.items()}
    if isinstance(v,(list,tuple)): return [export(x) for x in v]
    return v
'''
check('export_source_exact', ast.dump(export, include_attributes=False) == ast.dump(ast.parse(expected_export).body[0], include_attributes=False))
check('save_exports_whole_report', has(function(trees[names[0]], 'save'), "OUT.write_text(json.dumps(export(report),indent=2)+'\\n')"))
source = sources[names[0]]
check('save_order_exact', "block['validation']=validate(R,H,cm,cols,x)\n            checks=block['validation']\n            save(report)" in source and "else:\n            report['state']='ALL_RESIDUALS_PASS_COST_UNCERTIFIED'; save(report)" in source)

def export_count(value):
    # One parameter v per call. Dict: k,x plus successful advance =3.
    # List/tuple: x plus successful advance =2. Ignore type tests,
    # calls, allocations, conversions and string/JSON output.
    if isinstance(value, dict):
        return 1 + sum(3 + export_count(x) for x in value.values())
    if isinstance(value, list):
        return 1 + sum(2 + export_count(x) for x in value)
    return 1
def export_count_iterative(value):
    stack = [value]; calls = de = le = 0
    while stack:
        x = stack.pop(); calls += 1
        if isinstance(x, dict):
            de += len(x); stack.extend(x.values())
        elif isinstance(x, list):
            le += len(x); stack.extend(x)
    return calls + 3*de + 2*le
per_block = [export_count(b) for b in con['blocks']]
check('all_block_counts_independently_replayed', all(export_count_iterative(b) == a for b,a in zip(con['blocks'], per_block)))
export_lower = sum((62-i)*v for i,v in enumerate(per_block))
enumerated_export = sum(sum(per_block[:r]) for r in range(1,62)) + sum(per_block)
check('save_multiplicities_independently_replayed', export_lower == enumerated_export == 21345120)

# These four parameter bindings were expressly not in ledger740's nine
# per Gram term. c=D(c), the coefficient test, k binding/advance and
# value store were already charged; do not charge them again.
scale = function(trees[names[0]], 'scale')
add = function(trees[names[0]], 'add')
check('gram_parameter_signatures', [a.arg for a in scale.args.args] == ['a','c'] and [a.arg for a in add.args.args] == ['a','b'])
check('gram_nested_calls', has(function(trees[names[0]], 'validate'), 'value=add(value,scale(H[k][j],R[i][k]))'))
parameter_lower = 4*61*29**3

# Bound Python Fraction's actually installed source, not C/gcd internals.
# Count every syntactically explicit argument parameter when its call is
# made; no charge for the call instruction. _from_coprime_ints costs6:
# cls,numerator,denominator bindings plus obj and two attribute stores.
F = fractions.Fraction
fraction_names = ['_add','_sub','_mul','_from_coprime_ints','_operator_fallbacks']
fraction_sources = {k: inspect.getsource(getattr(F,k)) for k in fraction_names}
import textwrap
ftrees = {k: ast.parse(textwrap.dedent(v)) for k,v in fraction_sources.items()}
helper = ftrees['_from_coprime_ints'].body[0]
check('fraction_helper_shape', ast.dump(helper,include_attributes=False) == ast.dump(ast.parse('''
@classmethod
def _from_coprime_ints(cls,numerator,denominator,/):
    """Convert a pair of ints to a rational number, for internal use.

    The ratio of integers should be in lowest terms and the denominator
    should be positive.
    """
    obj=super(Fraction,cls).__new__(cls)
    obj._numerator=numerator
    obj._denominator=denominator
    return obj
''').body[0],include_attributes=False))
# The docstring's spelling is not mathematical evidence; the structural
# comparison above binds the actual source's stores and formal arguments.
fallback = ftrees['_operator_fallbacks']
forward = function(fallback,'forward'); reverse = function(fallback,'reverse')
check('fraction_operator_wrapper_parameters', len(forward.args.args) == len(reverse.args.args) == 2)
check('fraction_forward_and_reverse_dispatch', 'return monomorphic_operator(a, b)' in ast.unparse(forward) and 'return monomorphic_operator(Fraction(a), b)' in ast.unparse(reverse))

def expr_cost(node):
    if isinstance(node, ast.BinOp):
        return 1 + expr_cost(node.left) + expr_cost(node.right)
    if isinstance(node, ast.UnaryOp):
        return 1 + expr_cost(node.operand)
    if isinstance(node, ast.Compare):
        return len(node.ops) + expr_cost(node.left) + sum(map(expr_cost,node.comparators))
    if isinstance(node, ast.Call):
        helper_cost = 6 if isinstance(node.func,ast.Attribute) and node.func.attr == '_from_coprime_ints' else 0
        return helper_cost + sum(map(expr_cost,node.args))
    return 0
def stores(node):
    return sum(map(stores,node.elts)) if isinstance(node,(ast.Tuple,ast.List)) else 1
def paths(stmts):
    result=[(0,False)]
    for node in stmts:
        if isinstance(node,ast.If):
            branch=[(expr_cost(node.test)+c,done) for body in (node.body,node.orelse) for c,done in paths(body)]
        elif isinstance(node,ast.Assign):
            branch=[(sum(map(stores,node.targets))+expr_cost(node.value),False)]
        elif isinstance(node,ast.AugAssign):
            branch=[(2+expr_cost(node.value),False)]
        elif isinstance(node,ast.Return):
            branch=[(expr_cost(node.value),True)]
        elif isinstance(node,ast.Expr):
            branch=[(0,False)]
        else:
            raise AssertionError('unhandled Fraction source '+ast.dump(node))
        result=[(a+b,end) for a,done in result for b,end in ([(0,True)] if done else branch)]
    return result
branch_costs={}
for name in ('_add','_sub','_mul'):
    fn=ftrees[name].body[0]
    check(name+'_two_parameters',len(fn.args.args)==2)
    branch_costs[name]=sorted({2+2+c for c,done in paths(fn.body) if done})
check('fraction_common_lower19', min(min(v) for v in branch_costs.values()) >= 19)

# Count only old731's original Chebyshev table, moments and original_q,
# and new740 REPLAY's Chebyshev/residual loops. None belongs to the old
# inverse/candidate-Gram subcount, new constructor subcount or integer
# Gram replay subcount. Even zero-weight multiplications execute.
old = trees[names[3]]; replay_tree = trees[names[1]]
check('old_chebyshev_recurrence', has(function(old,'cheb'),'v.append(2*t*v[-1]-v[-2])'))
check('old_degree34', 'J, DEG, NC, PREC = 2**K, 34, 129, 80' in sources[names[3]])
check('old_all_original_table', has(old,'original_values = [cheb(t, 2*DEG) for t in ts]'))
check('old_all_moment_products', has(old,'moments = [sum((mass*row[k] for mass, row in zip(masses, original_values)), F(0)) for k in range(2*DEG+1)]'))
check('old_original_q_products', has(old,'original_q = [sum((c*v for c, v in zip(q, row)), F(0)) for row in original_values]'))
check('old_q_length35', has(old,'q = [F(v) for v in residual]') and has(old,'residual = [sum((a[i][k]*x[i] for i in range(NC)), D(0))-b[k] for k in range(DEG+1)]'))
check('replay_cheb_and_residual_loops', has(replay_tree,'for d in range(2,29): vals.append(2*t*vals[-1]-vals[-2])') and has(replay_tree,'for d in range(29): residual[d]+=w*vals[d]'))
atoms = sum(2**k for k in (8,9,10))
fraction_counts = {'old_chebyshev':atoms*67*3,'old_moments':atoms*69*2,'old_original_q':atoms*35*2,'new_replay_chebyshev':61*35*27*3,'new_replay_residual':61*35*29*2}
fraction_lower = 19*sum(fraction_counts.values())

# One extra entry store per old inverse update (explicitly excluded732).
# Two extra units per old Gram generator term: k binding and advance.
check('old_inverse_entry_store',has(function(old,'solve'),'a[i][j] -= factor*a[k][j]'))
check('old_candidate_gram_generator',has(old,'value = sum((a[i][k]*a[j][k] for k in range(DEG+1)), D(0))'))
inverse_updates = sum((34-k)*(35-k) for k in range(35))*35
check('old_inverse_count_independent',inverse_updates == 499800)
old_store_lower = 3*inverse_updates
old_generator_lower = 3*(129*130//2)*35*2
components = {'prior_disjoint_lower':prior,'repeated_export_bindings_advances':export_lower,'new_constructor_gram_parameter_bindings':parameter_lower,'previously_unpriced_fraction_calls':fraction_lower,'old_inverse_entry_stores':old_store_lower,'old_candidate_gram_generator_bindings_advances':old_generator_lower}
total=sum(components.values()); cap=10**8
check('above_cap',total == 101666571 and total > cap)
input_paths=[BASE/n for n in names]+[BASE/n for n in ('lower-degree-fixed-740.json','lower-degree-replay-740.json','lower-degree-ledger-740.json')]
report={'script_sha256':digest(HERE),'runtime':{'version':sys.version,'fractions_path':fractions.__file__,'fractions_sha256':digest(Path(fractions.__file__))},'input_hashes':{p.name:digest(p) for p in input_paths},'source_excerpts':sources,'fraction_source_excerpts':fraction_sources,'checks':checks,'failures':[k for k,v in checks.items() if not v],'work':{'convention':'Each scalar arithmetic/comparison, explicit source parameter/local binding/store, successful loop advance costs at least one unit; no call instruction or integer/gcd internals charged. Not elapsed time or optimized code.','components':components,'fraction_minimum_by_source_path':branch_costs,'fraction_operation_counts':fraction_counts,'export_per_block':per_block,'export_block_multiplicities':[62-i for i in range(61)],'mandatory_disjoint_lower':total,'required_upper_cap':cap,'excess':total-cap,'complete_upper_bound':None,'decision':'STOP unchanged740 production/replay/export bundle with original731 production of the three retained rules','unpriced':['new original moments and most other exact arithmetic','remaining solver, validation, replay and reporting','all integer/gcd/Decimal primitive internals','JSON formatting/string copying/disk output','exact256 prefix production, allocation and peak bytes']},'storage':{'peak_working_bytes_upper':None,'reason':'Not needed to reject this above-cap implementation; no storage pass asserted.'},'scope':'Source-specific cost obstruction only. The rank2130/error<7.291e-8 numerical result survives. No lower bound for altered save schedules, other production of the earlier rules, other degree28 rules, compiled code or the scalar.'}
OUT.write_text(json.dumps(report,indent=2)+'\n')
print('WORK certified disjoint LOWER',total,'required complete UPPER <=',cap,'excess',total-cap,'STOP unchanged source bundle')
print('CHECKS',sum(checks.values()),'/',len(checks),'failures',report['failures'],'peak bytes unproved; certificate',OUT)
