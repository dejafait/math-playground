"""Independent fixed C040d audit: positive exp series and reciprocal bounds.

No producer execution, parameter selection, or extra sample points.
For x>=0 and x<66, P64=sum(x**j/j!, j=0..64) and
R65=(x**65/65!)/(1-x/66) give P64 <= exp(x) <= P64+R65.
Reciprocation encloses exp(-x). Analytical identities are in C040d.
"""
from fractions import Fraction as Q
from hashlib import sha256
from math import factorial
from pathlib import Path
import json


def enc(v):
    if isinstance(v, Q):
        return f"{v.numerator}/{v.denominator}"
    if isinstance(v, dict):
        return {k: enc(x) for k, x in v.items()}
    if isinstance(v, (list, tuple)):
        return [enc(x) for x in v]
    return v


source_path = Path(__file__).with_name('continuous-floor-1178.json')
source_bytes = source_path.read_bytes()
source = json.loads(source_bytes)
checks = {}


def check(name, condition):
    checks[name] = bool(condition)


a, eta = Q(1, 20), Q(15287777, 250000000)
lam_lo, lam_hi = Q(4329, 1000), Q(4331, 1000)
args = dict(fast=Q(199, 40), half=Q(1, 40), unit=Q(1, 20),
            floor_at_lambda_lo=Q(4329, 20000),
            floor_at_lambda_hi=Q(4331, 20000))
check('fixed_parameters', source['parameters'] == enc(
    dict(a=a, eta=eta, **{'lambda': [lam_lo, lam_hi]})))
check('exactly_five_arguments', set(source['exponentials']) == set(args))
check('positive_eta_ordered_lambda', eta > 0 and 0 < lam_lo < lam_hi)
check('arguments_from_parameters', list(args.values()) == [
    Q(199, 2)*a, a/2, a, lam_lo*a, lam_hi*a])
independent, originals, term_residuals = {}, {}, {}
for name, x in args.items():
    old = source['exponentials'][name]
    check(name+'_argument', Q(old['x']) == x)
    # Direct powers/factorials avoid the producer's term recurrence.
    terms = [(-x)**j / factorial(j) for j in range(42)]
    stored = [Q(t) for t in old['terms_j_0_through_41']]
    check(name+'_all_42_terms', len(stored) == 42 and stored == terms)
    term_residuals[name] = [s-t for s, t in zip(stored, terms)]
    old_interval = [Q(old['lower']), Q(old['upper'])]
    check(name+'_original_bounds', old_interval == [sum(terms), sum(terms[:41])])
    check(name+'_geometric_tail_hypotheses', 0 <= x < 66)
    positive_sum = sum((x**j / factorial(j) for j in range(65)), Q(0))
    first_omitted = x**65 / factorial(65)
    tail_upper = first_omitted / (1-x/66)
    lo, hi = 1/(positive_sum+tail_upper), 1/positive_sum
    check(name+'_reciprocal_bounds_positive', 0 < lo <= hi)
    check(name+'_independent_inside_original', old_interval[0] <= lo <= hi <= old_interval[1])
    independent[name] = dict(x=x, positive_sum_64=positive_sum,
                             first_omitted_65=first_omitted,
                             tail_ratio_upper=x/66, tail_upper=tail_upper,
                             exp_minus_x=[lo, hi])
    originals[name] = old_interval


def assemble(intervals):
    density = [intervals['fast'][0]+intervals['half'][0]-intervals['unit'][1],
               intervals['fast'][1]+intervals['half'][1]-intervals['unit'][0]]
    floor = [eta*intervals['floor_at_lambda_hi'][0],
             eta*intervals['floor_at_lambda_lo'][1]]
    deficit = [density[0]-floor[1], density[1]-floor[0]]
    return dict(density_at_a=density, floor_uniform=floor, deficit_uniform=deficit)


old_assembly = assemble(originals)
new_assembly = assemble({k: v['exp_minus_x'] for k, v in independent.items()})
display = dict(density_at_a=['0.030989006467', '0.030989006468'],
               floor_uniform=['0.049244514531', '0.049249439230'],
               deficit_uniform=['-0.018260432763', '-0.018255508064'])
for name in old_assembly:
    old_lo, old_hi = old_assembly[name]
    new_lo, new_hi = new_assembly[name]
    check(name+'_original_exact_assembly', [Q(v) for v in source[name]] == [old_lo, old_hi])
    check(name+'_independent_inside_original', old_lo <= new_lo <= new_hi <= old_hi)
    check(name+'_display_literal', source['displayed_outward_enclosures'][name] == display[name])
    check(name+'_display_outward_exact', Q(display[name][0]) <= old_lo <= old_hi <= Q(display[name][1]))
check('threshold_literal_zero', Q(source['required_upper_threshold']) == 0)
check('original_uniform_upper_negative', old_assembly['deficit_uniform'][1] < 0)
check('independent_uniform_upper_negative', new_assembly['deficit_uniform'][1] < 0)
check('coarse_rational_negative_interval', Q(-184, 10000) < new_assembly['deficit_uniform'][0]
      <= new_assembly['deficit_uniform'][1] < Q(-181, 10000) < 0)
# Recompute all ten original predicates instead of trusting stored Booleans.
expected = dict(
    nonnegative_arguments=all(x >= 0 for x in args.values()),
    ordered_exponential_bounds=all(v[0] <= v[1] for v in originals.values()),
    positive_exponential_lower_bounds=all(v[0] > 0 for v in originals.values()),
    lambda_order_and_eta_positive=0 < lam_lo < lam_hi and eta > 0,
    ordered_density_bounds=old_assembly['density_at_a'][0] <= old_assembly['density_at_a'][1],
    ordered_floor_bounds=old_assembly['floor_uniform'][0] <= old_assembly['floor_uniform'][1],
    ordered_deficit_bounds=old_assembly['deficit_uniform'][0] <= old_assembly['deficit_uniform'][1],
    uniform_upper_below_required_zero=old_assembly['deficit_uniform'][1] < 0,
    uniform_deficit_in_minus_00184_minus_00181=Q(-184, 10000) < old_assembly['deficit_uniform'][0]
        <= old_assembly['deficit_uniform'][1] < Q(-181, 10000),
    displayed_decimal_enclosures_verified_as_exact_rationals=all(
        Q(display[k][0]) <= v[0] <= v[1] <= Q(display[k][1]) for k, v in old_assembly.items()))
check('all_original_predicates_recomputed', source['checks'] == expected and all(expected.values()))
check('original_failure_list_consistent', source['failures'] == [k for k, v in expected.items() if not v])
failures = [k for k, v in checks.items() if not v]
certificate = dict(target='Unchanged C040d fixed-model audit; five prescribed arguments only',
    source_path=str(source_path.relative_to(Path.cwd())), source_sha256=sha256(source_bytes).hexdigest(),
    method=__doc__, independent_exponentials=independent,
    original_term_residuals=term_residuals, original_assembly=old_assembly,
    independent_assembly=new_assembly, displayed_outward_enclosures=display,
    required_upper_threshold=Q(0), original_predicates_recomputed=expected,
    checks=checks, failures=failures)
out = Path(__file__).with_suffix('.json')
out.write_text(json.dumps(enc(certificate), indent=2)+'\n')
print(f'Independent exact checks: {sum(checks.values())}/{len(checks)}; failures: {failures}')
print('Uniform deficit is enclosed in [-0.018260432763, -0.018255508064]; required upper threshold: 0')
print('Coarse exact test: -184/10000 < D(lambda) < -181/10000 < 0')
print(f'Certificate: {out.relative_to(Path.cwd())}')
assert not failures, failures
