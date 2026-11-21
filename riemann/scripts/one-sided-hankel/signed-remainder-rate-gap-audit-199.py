"""Independent exact audit of all L722 nodes, bounds, provenance and replay.

Uses rational complex factor operations and an 80-term exact atanh sum,
then outward dyadic rounding at 2^180, independently of the 2^100 helper.
Only the original script's output destination is changed for replay.
"""
import ast
import contextlib
from fractions import Fraction as F
import hashlib
import io
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / 'signed-remainder-rate-gap-197.py'
HELPER = ROOT / 'spatial-complex-phase-166.py'
ORIGINAL = SOURCE.with_suffix('.json')
REPLAY = ROOT / 'signed-remainder-rate-gap-replay-199.json'
OUTPUT = Path(__file__).with_suffix('.json')
SCALE = 1 << 180
TERMS = 80
N = 64
checks, failures = {}, []

def enc(x):
    x = F(x)
    return {'numerator': x.numerator, 'denominator': x.denominator}

def dec(x):
    return F(x['numerator'], x['denominator'])

def check(name, passed, evidence=None):
    checks[name] = {'passed': bool(passed), 'evidence': evidence}
    if not passed:
        failures.append(name)

def outward(x, upper=False):
    x *= SCALE
    n = -(-x.numerator // x.denominator) if upper else x.numerator // x.denominator
    return F(n, SCALE)

def unit_log(q):
    assert 1 <= q <= 2
    z = (q-1)/(q+1)
    power, total = z, F(0)
    for j in range(TERMS):
        total += 2*power/(2*j+1)
        power *= z*z
    tail = 2*power/((2*TERMS+1)*(1-z*z))
    return [total, total+tail], {'z': enc(z), 'terms': TERMS,
                                'finite_sum': enc(total), 'tail_upper': enc(tail)}

LOG2, LOG2_EVIDENCE = unit_log(F(2))

def logarithm(q):
    original, exponent = q, 0
    while q < 1:
        q *= 2
        exponent -= 1
    while q > 2:
        q /= 2
        exponent += 1
    interval, evidence = unit_log(q)
    for k in (0, 1):
        interval[k] += exponent*LOG2[k if exponent >= 0 else 1-k]
    interval = [outward(interval[0]), outward(interval[1], True)]
    return interval, {'argument': enc(original), 'binary_exponent': exponent,
                      'reduced_argument': enc(q), 'series': evidence}

def mul(z, w):
    return z[0]*w[0]-z[1]*w[1], z[0]*w[1]+z[1]*w[0]

def affine(z, w, t):
    return z[0]+w[0]*t, z[1]+w[1]*t

def norm2(z):
    return z[0]**2+z[1]**2

old = json.loads(ORIGINAL.read_text())
source, helper = SOURCE.read_text(), HELPER.read_text()
check('original_script_hash', old['script_sha256'] == hashlib.sha256(SOURCE.read_bytes()).hexdigest())
check('original_helper_hash', old['helper_sha256'] == hashlib.sha256(HELPER.read_bytes()).hexdigest())
check('original_helper_path', Path(old['helper_path']).resolve() == HELPER)
helper_ast = ast.parse(helper)
source_ast = ast.parse(source)
helper_defs = [x for x in helper_ast.body if isinstance(x, ast.FunctionDef)
               and x.name in {'ceildiv', 'fixed', 'log_unit', 'logq'}]
check('unique_four_helper_definitions', len(helper_defs) == 4 and
      {x.name for x in helper_defs} == {'ceildiv', 'fixed', 'log_unit', 'logq'})
assignments = {x.targets[0].id: ast.unparse(x.value) for x in helper_ast.body
               if isinstance(x, ast.Assign) and isinstance(x.targets[0], ast.Name)}
check('helper_global_values', assignments['SCALE'] == '1 << 100' and assignments['TERMS'] == '40'
      and assignments['LOG2'] == 'log_unit(2, 1)', assignments)
check('invocation_global_values', 'ns = dict(F=F, SCALE=1 << 100, TERMS=40)' in source
      and 'ns["LOG2"] = ns["log_unit"](2, 1)' in source)
check('original_parameters', old['parameters'] == {
    'panels': N, 'comparison_s_real': {**enc(F(73,40)), 'decimal_preview': float(F(73,40))},
    'comparison_s_imag': {**enc(-F(73,40)), 'decimal_preview': float(-F(73,40))}, 'scale': 1 << 100})

# Replay the actual code, redirecting only the certificate destination.
rewrites = 0
for node in source_ast.body:
    if isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name) and node.targets[0].id == 'path':
        assert ast.unparse(node.value) == "Path(__file__).with_suffix('.json')"
        node.value = ast.Call(func=ast.Name(id='Path', ctx=ast.Load()),
                              args=[ast.Constant(str(REPLAY))], keywords=[])
        rewrites += 1
assert rewrites == 1
ast.fix_missing_locations(source_ast)
with contextlib.redirect_stdout(io.StringIO()) as captured:
    exec(compile(source_ast, str(SOURCE), 'exec'), {'__file__': str(SOURCE), '__name__': '__main__'})
replay = json.loads(REPLAY.read_text())
check('complete_replay_matches_original', replay == old)

D, U, A, C = F(5,4), F(121,64), F(27,10), F(1,8)
u, s, alpha = (F(3,10), F(2,5)), (F(73,40), -F(73,40)), F(11,8)
real = lambda x: (x, F(0))
Uu = (U*u[0], U*u[1])
all_rows, independent_integrals = {}, {}
sharp_error, saved_error = F(100,180*N**4), F(100,45*N**4)
for label in ('saddle', 'residue'):
    rows = old[label+'_rows']
    check(label+'_complete_grid', len(rows) == N+1 and [r['j'] for r in rows] == list(range(N+1)))
    aggregate = [F(0), F(0)]
    audited = []
    for j, row in enumerate(rows):
        t = F(j,N)
        f1 = affine(real(D), u, t)
        f3 = affine(Uu, real(D), t)
        if label == 'saddle':
            f2, f4 = affine(real(U), s, t), affine(s, real(1), t)
        else:
            f2, f4 = affine(Uu, real(alpha), t), affine(real(alpha), u, t)
        numerator, denominator = mul(f1,f2), mul(f3,f4)
        assert norm2(denominator) > 0
        q = norm2(numerator)/norm2(denominator)
        bounds, evidence = logarithm(q)
        saved = [dec(x) for x in row['log_squared_modulus']]
        weight = 1 if j in (0,N) else (4 if j%2 else 2)
        passed = (dec(row['t']) == t and dec(row['squared_modulus']) == q and
                  row['weight'] == weight and saved[0] <= bounds[0] <= bounds[1] <= saved[1])
        check(f'{label}_node_{j:02d}', passed)
        audited.append({'j': j, 't': enc(t), 'complex_factors': [[enc(x) for x in z] for z in (f1,f2,f3,f4)],
                        'squared_modulus': enc(q), 'weight': weight,
                        'original_log_interval': [enc(x) for x in saved],
                        'independent_log_interval': [enc(x) for x in bounds],
                        'logarithm_evidence': evidence, 'passed': passed})
        for k in (0,1):
            aggregate[k] += weight*bounds[k]/(6*N)
    bounds = [aggregate[0]-sharp_error, aggregate[1]+sharp_error]
    independent_integrals[label] = bounds
    saved = [dec(x) for x in old['bounds'][label+'_integral']]
    check(label+'_integral_contains_independent', saved[0] <= bounds[0] <= bounds[1] <= saved[1],
          {'saved': [enc(x) for x in saved], 'independent': [enc(x) for x in bounds]})
    # Reconstruct precisely the original sum and its conservative error.
    reconstructed = [sum((r['weight']*dec(r['log_squared_modulus'][k]) for r in rows), F(0))/(6*N)
                     +(-saved_error if k == 0 else saved_error) for k in (0,1)]
    check(label+'_original_aggregation', saved == reconstructed)
    check(label+'_original_error', dec(old['bounds'][label+'_quadrature_error']) == saved_error)
    all_rows[label] = audited

l9, e9 = logarithm(F(9,5))
l201, e201 = logarithm(F(201,121))
omega = [A*(l9[k]-F(4,5)+F(121,100)*l201[k]) for k in (0,1)]
saved_omega = [dec(x) for x in old['bounds']['omega']]
check('omega_independently_enclosed', saved_omega[0] <= omega[0] <= omega[1] <= saved_omega[1])
linear = (u[0]+u[1])*s[0]-D
loss = F(1,4)*2*F(1,40)**2
saved_comparison = [dec(x) for x in old['bounds']['comparison_rate']]
expected_comparison = [dec(old['bounds']['saddle_integral'][k])+linear*saved_omega[k]/A for k in (0,1)]
check('comparison_rate_assembly', saved_comparison == expected_comparison)
saved_lower = saved_comparison[0]-loss
saved_upper = dec(old['bounds']['residue_integral'][1])+C*(saved_omega[1]+F(1,3000))/A
check('bound_assembly', dec(old['bounds']['phase_loss']) == loss and
      dec(old['bounds']['saddle_rate_lower']) == saved_lower and
      dec(old['bounds']['residue_rate_upper']) == saved_upper)
expected = {
 'comparison_point_modulus_squared': (norm2(s), '<', F(9)),
 'saddle_fourth_derivative_bound': (6*((F(1,2)/D)**4+(D/(U/2))**4+(3/U)**4+F(5,9)**4), '<', F(100)),
 'residue_fourth_derivative_bound': (6*((F(1,2)/D)**4+(D/(U/2))**4+(alpha/(U/2))**4+(F(1,2)/alpha)**4), '<', F(100)),
 'phase_second_derivative_bound': (F(25,81)+1/(3*U**2), '<', F(1,2)),
 'omega_positive': (saved_omega[0], '>', F(1)),
 'comparison_phase_linear_coefficient': (linear, '>', F(0)),
 'comparison_rate_lower': (saved_comparison[0], '>', F(11,2000)),
 'saddle_rate_lower': (saved_lower, '>', F(1,200)),
 'residue_rate_upper': (saved_upper, '<', F(1,5000)),
 'strict_rate_gap': (saved_lower-saved_upper, '>', F(3,625))}
check('complete_comparison_set', set(old['checks']) == set(expected))
for name, (actual, relation, required) in expected.items():
    row = old['checks'][name]
    passes = actual < required if relation == '<' else actual > required
    check('exact_'+name, dec(row['actual']) == actual and row['relation'] == relation and
          dec(row['required']) == required and row['passed'] is True and passes,
          {'actual': enc(actual), 'relation': relation, 'required': enc(required)})
check('original_failure_list_empty', old['failures'] == [])
independent_lower = independent_integrals['saddle'][0]+linear*omega[0]/A-loss
independent_upper = independent_integrals['residue'][1]+C*(omega[1]+F(1,3000))/A
check('independent_phase_threshold', independent_lower > F(1,200), {'actual':enc(independent_lower),'required':enc(F(1,200))})
check('independent_residue_threshold', independent_upper < F(1,5000), {'actual':enc(independent_upper),'required':enc(F(1,5000))})

result = {'purpose': __doc__, 'original_script_sha256': hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
 'helper_sha256': hashlib.sha256(HELPER.read_bytes()).hexdigest(),
 'audit_script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'helper_definitions': {x.name: ast.unparse(x) for x in helper_defs},
 'replay': {'path': str(REPLAY.relative_to(ROOT.parent.parent)), 'ast_changes': 'Only path assignment redirected; original __file__ and hash preserved',
            'stdout': captured.getvalue(), 'complete_equality': replay == old},
 'independent_method': {'scale': SCALE, 'terms': TERMS, 'log2_evidence': LOG2_EVIDENCE,
                        'log2_interval': [enc(x) for x in LOG2], 'omega_log_evidence': [e9,e201]},
 'quadrature': {'N':N, 'C4_bound':100, 'standard_simpson_error':enc(sharp_error),
                'original_conservative_error':enc(saved_error)},
 'saddle_rows':all_rows['saddle'], 'residue_rows':all_rows['residue'],
 'independent_bounds': {'omega':[enc(x) for x in omega],
                        'phase_lower':enc(independent_lower),'residue_upper':enc(independent_upper)},
 'checks':checks, 'failures':failures,
 'qualifications':['Finite rational evidence only; analytic applicability and signed limsup logic are audited in L722.',
                   'L714/L719/L721 audited interfaces are inherited; no full-limit or complete-response conclusion.']}
OUTPUT.write_text(json.dumps(result,indent=2)+'\n')
print(f'Complete nodes: {len(all_rows["saddle"])} saddle + {len(all_rows["residue"])} residue; exact checks: {len(checks)}')
print(f'Phase lower {float(independent_lower):.12g} > required {float(F(1,200)):.12g}')
print(f'Residue upper {float(independent_upper):.12g} < required {float(F(1,5000)):.12g}')
print(f'Failures: {failures}; certificate: {OUTPUT.relative_to(ROOT.parent.parent)}; replay: {REPLAY.relative_to(ROOT.parent.parent)}')
if failures:
    raise SystemExit(1)
