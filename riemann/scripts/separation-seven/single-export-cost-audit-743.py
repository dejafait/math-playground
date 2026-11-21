#!/usr/bin/env python3
"""Disjoint LOWER source-work certificate for fixed742 single-final export.

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

# Bind the changed source boundary, without running numerical production.
new_constructor = BASE/'single-export-fixed-743.py'
new_replay = BASE/'single-export-replay-743.py'
new_source = new_constructor.read_text()
new_tree = ast.parse(new_source)
new_rep_source = new_replay.read_text()
new_rep_tree = ast.parse(new_rep_source)
old_main = trees[names[0]].body[-1]
new_main = new_tree.body[-1]
check('both_entrypoints', isinstance(old_main,ast.If) and isinstance(new_main,ast.If))
class StripSaves(ast.NodeTransformer):
    def visit_Expr(self,node):
        if isinstance(node.value,ast.Call) and isinstance(node.value.func,ast.Name) and node.value.func.id in ('save','checkpoint'):
            return None
        return self.generic_visit(node)
import copy
check('entire_numerical_entrypoint_identical', ast.dump(StripSaves().visit(copy.deepcopy(old_main)),include_attributes=False)==ast.dump(StripSaves().visit(copy.deepcopy(new_main)),include_attributes=False))
num_functions = [n.name for n in trees[names[0]].body if isinstance(n,ast.FunctionDef)]
for name in num_functions:
    check('unchanged_function_'+name, ast.dump(function(trees[names[0]],name),include_attributes=False)==ast.dump(function(new_tree,name),include_attributes=False))
# Compare all original module setup (imports, parameters, contexts, COUNT)
# and numerical definitions; allow only docstring/new path/schedule/helper.
def module_core(tree):
    return ast.dump(ast.Module(body=[n for i,n in enumerate(tree.body) if i and not (isinstance(n,ast.FunctionDef) and n.name=='checkpoint') and not (isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id in ('SHORT','SCHEDULE') for t in n.targets))],type_ignores=[]),include_attributes=False)
old_clean=copy.deepcopy(trees[names[0]]); new_clean=copy.deepcopy(new_tree)
old_clean.body[-1]=StripSaves().visit(old_clean.body[-1]); new_clean.body[-1]=StripSaves().visit(new_clean.body[-1])
check('entire_constructor_except_allowed_boundary',module_core(old_clean)==module_core(new_clean))
expected_replay=sources[names[1]].replace('"""Independent original-moment and integer Gram/residual replay for740.', '"""Unchanged numerical replay with fixed742 source/artifact bindings.',1).replace("INPUT=HERE.with_name('lower-degree-fixed-740.json')","INPUT=HERE.with_name('single-export-fixed-743.json')",1)
check('entire_replay_except_doc_and_input_binding',new_rep_source==expected_replay)
check('replay_binds_new_constructor_source',has(new_rep_tree,"checks={'constructor_source_binding':doc['script_sha256']==sha256(INPUT.with_suffix('.py').read_bytes()).hexdigest(),'all61_blocks_present':[b['k'] for b in doc['blocks']]==list(range(11,72))}"))
full_calls=[x for x in ast.walk(new_main) if isinstance(x,ast.Call) and isinstance(x.func,ast.Name) and x.func.id=='save']
short_calls=[x for x in ast.walk(new_main) if isinstance(x,ast.Call) and isinstance(x.func,ast.Name) and x.func.id=='checkpoint']
check('single_terminal_full_save_outside_loop',len(full_calls)==1 and len(short_calls)==4 and isinstance(new_main.body[-2],ast.Expr) and new_main.body[-2].value is full_calls[0])
check('checkpoint_schema_and_output',has(function(new_tree,'checkpoint'),"short={'source_sha256':report['script_sha256'],'schedule':SCHEDULE,'state':report['state'],'last_completed_k':completed,'validation':{key:validation[key] for key in ('nonnegative','contraction_pass','residual_pass')} if validation else None,'failures':report['failures'][:],'counts_lower_subtotals':COUNT.copy()}") and has(function(new_tree,'checkpoint'),"SHORT.write_text(json.dumps(short,indent=2)+'\\n')"))
old_audit=json.loads((BASE/'degree28-cost-audit-741.json').read_text())
check('old_audit_all_checks_and_no_failures',all(old_audit['checks'].values()) and not old_audit['failures'])
check('old_audit_source_bound',old_audit['script_sha256']==digest(BASE/'degree28-cost-audit-741.py'))
check('all_seven_old_audit_input_hashes',all(digest(BASE/name)==h for name,h in old_audit['input_hashes'].items()))
old_docs={k:json.loads((BASE/('support-grid-nnls-731-k'+str(k)+'.json')).read_text()) for k in (8,9,10)}
check('three_old_productions_source_bound',all(d['script_sha256']==digest(BASE/'support-grid-nnls-731.py') for d in old_docs.values()))
check('three_old_productions_residual_checks',all(d['checks']['original_orthonormal_residual_within_fixed_budget'] and d['checks']['exactly35_strictly_positive_original_support_weights'] for d in old_docs.values()))

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
# Previously unpriced Fraction add/sub/mul calls. No division, power,
# conversion, gcd, integer primitive or source-level enclosing operation
# is charged here. Count each rational operation once, at lower19.
check('new_constructor_cheb_source',has(function(new_tree,'data'),'for n in range(2,DIM): a.append(2*t*a[-1]-a[-2])'))
check('new_constructor_residual_source',has(function(new_tree,'validate'),'exact=sum((F(x[i])*cols[i][n] for i in range(NC)),F(0))'))
check('constructor_exact_power_sum_source',has(function(new_tree,'moments'),'value=(v**(p+1)-u**(p+1)-sum((comb(p+1,l)*sums[l] for l in range(p)),F(0)))/(p+1)') and has(function(new_tree,'moments'),'for p in range(55):\n    value=(v**(p+1)-u**(p+1)-sum((comb(p+1,l)*sums[l] for l in range(p)),F(0)))/(p+1)\n    sums.append(value)\n    xm.append(q(value/J**(p+1)))'))
check('replay_exact_power_sum_source',has(function(new_rep_tree,'regenerate'),'for p in range(55):\n    val=(v**(p+1)-u**(p+1)-sum((comb(p+1,l)*h**(p-l)*power_sums[l] for l in range(p)),F(0)))/(p+1)\n    power_sums.append(val)'))
additional_fraction_counts={'constructor_support_chebyshev':61*35*27*3,'constructor_exact_residual':61*29*35*2,'constructor_power_sums':61*(2*sum(range(55))+2*55),'replay_power_sums':61*(3*sum(range(55))+2*55)}
# Independent enumeration from abstract loop indices, not the formulas.
independent_fraction_counts={'constructor_support_chebyshev':sum(3 for k in range(11,72) for i in range(35) for d in range(2,29)),'constructor_exact_residual':sum(2 for k in range(11,72) for d in range(29) for i in range(35)),'constructor_power_sums':sum(sum(2 for l in range(p))+2 for k in range(11,72) for p in range(55)),'replay_power_sums':sum(sum(3 for l in range(p))+2 for k in range(11,72) for p in range(55))}
check('new_fraction_counts_independently_enumerated',additional_fraction_counts==independent_fraction_counts)
new_fraction_lower=19*sum(additional_fraction_counts.values())
# Only count independently fixed gradient, triangular and Gram counters;
# omit the dot/update/rotation counters entirely from this NEW charge.
check('history_monotone_active_sets',all([(h['main'],h['secondary'],len(h['active'])) for h in b['solver']['history']]==[(i,i,i) for i in range(1,30)] for b in con['blocks']))
gradient=61*sum((35-p)*(29-p) for p in range(29))
triangular=61*sum(q*(q-1)//2 for q in range(1,30))
check('fixed_gradient_and_triangular_counts',gradient==681065==n['gradient_terms'] and triangular==247660==n['triangular_terms'])
check('independent_gradient_enumeration',gradient==sum(1 for k in range(11,72) for p in range(29) for j in range(p,35) for i in range(p,29)))
check('independent_triangular_enumeration',triangular==sum(1 for k in range(11,72) for q in range(1,30) for i in range(q-1,-1,-1) for h in range(i)))
for label,fn in [('gradient_terms','nnls'),('triangular_terms','triangular'),('gram_product_terms','validate')]:
    check('unchanged_counter_'+label,has(function(new_tree,fn),"COUNT['"+label+"']+=1"))
check('replay_product_counter',has(new_rep_tree,'product_terms+=1'))
# Each +=1 requires a distinct integer addition and destination store.
# Earlier five/nine/thirteen-unit loop charges excluded both.
instrumentation_counts={'constructor_gradient':gradient,'constructor_triangular':triangular,'constructor_gram':61*29**3,'replay_gram':61*29**3}
instrumentation_lower=2*sum(instrumentation_counts.values())
components={'prior_disjoint_lower':prior,'constructor_gram_parameter_bindings':parameter_lower,'previous_fraction_lower':fraction_lower,'old_inverse_entry_stores':old_store_lower,'old_candidate_gram_generator_bindings_advances':old_generator_lower,'additional_fraction_lower':new_fraction_lower,'selected_counter_additions_and_stores':instrumentation_lower}
total=sum(components.values());cap=10**8
check('no_export_charged',not any('export' in key for key in components))
check('above_cap',total==102628907 and total>cap)
check('same_fraction_runtime_as741',sys.version==old_audit['runtime']['version'] and digest(Path(fractions.__file__))==old_audit['runtime']['fractions_sha256'])
input_paths=[BASE/name for name in names]+[BASE/name for name in ('lower-degree-fixed-740.json','lower-degree-replay-740.json','lower-degree-ledger-740.json','degree28-cost-audit-741.py','degree28-cost-audit-741.json')]+[BASE/('support-grid-nnls-731-k'+str(k)+'.json') for k in (8,9,10)]+[new_constructor,new_replay]
report={'script_sha256':digest(HERE),'runtime':{'version':sys.version,'fractions_path':fractions.__file__,'fractions_sha256':digest(Path(fractions.__file__))},'input_hashes':{p.name:digest(p) for p in input_paths},'source_excerpts':{**sources,new_constructor.name:new_source,new_replay.name:new_rep_source},'fraction_source_excerpts':fraction_sources,'checks':checks,'failures':[k for k,v in checks.items() if not v],'work':{'convention':old_audit['work']['convention'],'components':components,'fraction_minimum_by_source_path':branch_costs,'previous_fraction_operation_counts':fraction_counts,'additional_fraction_operation_counts':additional_fraction_counts,'independent_additional_fraction_operation_counts':independent_fraction_counts,'selected_counter_occurrences':instrumentation_counts,'all_export_work_charged':0,'mandatory_disjoint_lower':total,'required_upper_cap':cap,'excess':total-cap,'complete_upper_bound':None,'decision':'STOP fixed742 single-final-export source bundle with unchanged731 production and numerical replay','unpriced':['ALL checkpoints and full-report export/JSON/string/file output','remaining moment/candidate/validation/control work','dot/update/rotation counter instrumentation','all integer/gcd/Decimal primitive internals','exact256 prefix, source binding, allocation, ledger production and peak bytes']},'storage':{'peak_working_bytes_upper':None,'reason':'Above-cap LOWER rejects this prescription without needing a memory bound; no storage pass.'},'boundary':{'numerical_production_rerun':False,'successful_path_evidence':'unchanged740 finite certificates, paid as production in the ledger','single_full_export':True,'constructor_output':'single-export-fixed-743.json (not produced)','short_checkpoint_output':'single-export-fixed-743-checkpoint.json (not produced)','replay_input':'single-export-fixed-743.json','resume':False},'scope':'Source-specific cost obstruction. No changed coefficient or numerical replay. Existing rank2130/error<7.291e-8 result survives. No source-independent complexity, sign or RH conclusion.'}
OUT.write_text(json.dumps(report,indent=2)+'\n')
print('WORK disjoint LOWER',total,'required complete UPPER <=',cap,'excess',total-cap,'STOP fixed742 prescription')
print('CHECKS',sum(checks.values()),'/',len(checks),'failures',report['failures'],'peak bytes UPPER unproved; certificate',OUT)
