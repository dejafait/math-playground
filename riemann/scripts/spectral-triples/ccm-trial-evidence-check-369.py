"""Bounded complete-evidence consistency check, not an independent proof audit.

Reads every saved pivot and coefficient, repeats inertia via determinants,
and checks the power integrals by summing each support interval separately.
"""
import ast
from decimal import Decimal as D
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / 'ccm-trial-certificate-369.json'
GENERATOR = HERE / 'ccm-trial-certificate-369.py'
BASE = HERE / 'finite-parity-359.py'
OUTPUT = Path(__file__).with_suffix('.json')
data = json.loads(SOURCE.read_text())
ns, selected = {}, []
for node in ast.parse(BASE.read_text()).body:
    if isinstance(node, (ast.Import, ast.ImportFrom)):
        selected.append(node)
    elif isinstance(node, ast.Assign) and any(isinstance(t, ast.Name) and
            t.id in {'PREC', 'LO', 'HI'} for t in node.targets):
        selected.append(node)
    elif isinstance(node, ast.ClassDef) and node.name == 'I':
        selected.append(node)
    elif isinstance(node, ast.FunctionDef) and node.name in {'pm', 'sincos_reduced'}:
        selected.append(node)
exec(compile(ast.Module(body=selected, type_ignores=[]), str(BASE), 'exec'), ns)
I, LO, HI = [ns[x] for x in ['I', 'LO', 'HI']]
LO.prec = HI.prec = 280
report = dict(kind='complete evidence and alternative finite formulas; not independent audit',
              input_sha256=hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
              script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              checks={}, failures=[], determinant_counts={}, integral_checks={},
              outcome='IN_PROGRESS')


def save():
    OUTPUT.write_text(json.dumps(report, indent=2)+'\n')


def require(ok, name):
    report['checks'][name] = bool(ok)
    if not ok:
        report['failures'].append(name)
        save()
        raise ArithmeticError(name)


def pair(v):
    require(len(v) == 2 and D(v[0]).is_finite() and D(v[1]).is_finite()
            and D(v[0]) <= D(v[1]), 'finite_ordered_pairs')
    return I(*v)


def overlap(a, b):
    return max(a.lo, b.lo) <= min(a.hi, b.hi)


require(data['outcome'] == 'CERTIFIED_TRIAL_PROJECTION' and not data['failures']
        and all(data['checks'].values()), 'all_generator_checks_passed')
require(data['script_sha256'] == hashlib.sha256(GENERATOR.read_bytes()).hexdigest(), 'generator_hash')
require(data['interval_source_sha256'] == hashlib.sha256(BASE.read_bytes()).hexdigest(), 'interval_hash')
aa = list(map(pair, data['operator']['diagonal']))
bb = list(map(pair, data['operator']['off_diagonal_including_omitted_coupling']))
require(len(aa) == len(bb) == 112, 'complete_matrix')
for threshold, expected in [(80, 0), (82, 1), (723, 2), (726, 3)]:
    row = data['infinite_counts'][str(threshold)]
    require(row['infinite_negative'] == expected, 'saved_count_'+str(threshold))
    for side in ['upper', 'lower']:
        pivots = list(map(pair, row[side]['pivots']))
        require(len(pivots) == 112 and all(p.lo > 0 or p.hi < 0 for p in pivots)
                and sum(p.hi < 0 for p in pivots) == expected, 'all_saved_pivots_'+side+str(threshold))
        correction = pair(row[side]['last_diagonal_correction'])
        pp, previous, lastsign, changes = I(0), I(1), 1, 0
        determinants = []
        for k, diag in enumerate(aa):
            new = (diag-threshold-(correction if k == len(aa)-1 else I(0)))*previous
            if k:
                new -= bb[k-1]*bb[k-1]*pp
            require(new.lo > 0 or new.hi < 0, 'determinants_nonzero_'+side+str(threshold))
            sign = 1 if new.lo > 0 else -1
            changes += int(sign != lastsign)
            lastsign, pp, previous = sign, previous, new
            determinants.append(new.save())
        require(changes == expected, 'alternate_count_'+side+str(threshold))
        report['determinant_counts'][side+str(threshold)] = dict(count=changes, determinants=determinants)

for mode, limit in [('0', '2.645e-97'), ('4', '4.034e-93')]:
    row = data['modes'][mode]
    require(len(row['normalized_candidate']) == 112
            and len(row['raw_exact_decimal_vector']) == 112
            and len(row['residual_including_tail']) == 113, 'complete_mode_'+mode)
    for key in ['normalized_candidate', 'residual_including_tail']:
        for v in row[key]:
            pair(v)
    r = pair(row['residual_norm'])
    sep = I(row['separation_lower'])
    require(r.lo >= 0 and sep.lo > r.hi
            and (2*I(r.hi)/sep).hi <= D(row['unit_L2_error_upper'])
            and D(row['unit_L2_error_upper']) < D(limit), 'residual_bound_'+mode)

pi, L, lam = [pair(data['constants'][x]) for x in ['pi', 'L', 'lam']]
ns['PI'] = pi
coeff = list(map(pair, data['trial']['monomial_coefficients_H_lambda_x']))
require(len(coeff) == 223 and all(v.lo == v.hi == 0 for v in coeff[1::2]), 'even_additive_polynomial')
err = I(data['trial']['full_projected_vector_L2_error_upper'])
require(err.hi < D('1.276e-91'), 'vector_error_budget')
exact = data['projection']['exact_trial_coefficients']
polynomial = data['projection']['polynomial_coefficients']
require(set(exact) == set(polynomial) == set(map(str, range(-120, 121))), 'complete_241_directions')
for j in range(-120, 121):
    for component in ['real', 'imag']:
        v, p = pair(exact[str(j)][component]), pair(polynomial[str(j)][component])
        require((v.hi-v.lo) < D('2.552e-91'), 'all_rectangular_widths')
        if j == 0 and component == 'imag':
            require(v.lo == v.hi == 0, 'real_zeroth_coefficient')
        else:
            # Check that the complete polynomial interval was inflated by err.
            require(v.lo <= LO.subtract(p.lo, err.hi)
                    and v.hi >= HI.add(p.hi, err.hi), 'all_error_inflations')

# A differently grouped antiderivative checks each support endpoint/phase.
for j in [0, 1, 120]:
    omega = 2*pi*j/L
    re, im = I(0), I(0)
    for r in range(1, 13):
        sine, cosine = ((I(0), I(1)) if j == 0 or r == 1 else
                        ns['sincos_reduced'](j*I(r).ln()/L))
        upper_weight = (lam/r).sqrt()
        lower_power = 1/lam.sqrt()
        interval_re, interval_im = I(0), I(0)
        for m in range(len(coeff)):
            if m % 2 == 0:
                a = I(m)+I(1)/2
                dr, di = upper_weight*cosine-lower_power, upper_weight*sine
                denom = a*a+omega*omega
                interval_re += coeff[m]*(a*dr-omega*di)/denom
                interval_im += coeff[m]*(omega*dr+a*di)/denom
            lower_power *= I(r)/13
        re += interval_re/L.sqrt()
        im += interval_im/L.sqrt()
    require(overlap(re, pair(polynomial[str(j)]['real'])) and
            overlap(im, pair(polynomial[str(j)]['imag'])), 'support_integral_agreement_'+str(j))
    report['integral_checks'][str(j)] = dict(real=re.save(), imag=im.save())
report['outcome'] = 'CONSISTENCY_CHECKS_PASSED'
save()
print('All 896 pivots, 226 residual coordinates and 241 coefficient rectangles inspected.')
print('Alternative determinant counts and separate-support integrals j=0,1,120 agree.')
print('Mode errors < 2.645e-97, 4.034e-93; component radii < 1.276e-91 (required < 1e-65).')
print('Failures:', report['failures'])
print('Evidence:', OUTPUT.relative_to(HERE.parent.parent))
