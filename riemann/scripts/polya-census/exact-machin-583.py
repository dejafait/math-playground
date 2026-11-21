"""Exact aggregate pi repair only; never imports or executes census579."""
from fractions import Fraction
import ast
import hashlib
import json
from pathlib import Path
import platform
import sys

BASE = Path(__file__).resolve().parent
ROOT = BASE.parent.parent
OUT = BASE / 'exact-machin-583.json'


def sha(data):
    return hashlib.sha256(data).hexdigest()


def rational(value):
    return dict(numerator=str(value.numerator), denominator=str(value.denominator))


saved_bytes = (BASE / 'census-579.json').read_bytes()
saved = json.loads(saved_bytes)
audit_bytes = (BASE / 'audit-581.json').read_bytes()
audit = json.loads(audit_bytes)
source_bytes = (BASE / 'census-579.py').read_bytes()
# Check the exact finite expression being replaced without evaluating it.
tree = ast.parse(source_bytes)
atan = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == 'atan')
pi_assignment = next(n for n in tree.body if isinstance(n, ast.Assign)
                     and any(isinstance(t, ast.Name) and t.id == 'pi' for t in n.targets))
expected_atan = ast.parse('''def atan(q):
 z=I(1)/q; s=I(0)
 for k in range(120):s=s+((-1)**k)*(z**(2*k+1))/(2*k+1)
 return s+sym(z**241/241)
''').body[0]
expected_pi = ast.parse('pi=16*atan(5)-4*atan(239)').body[0]
hashes = {}
audit_start = b'<!-- BEGIN STEP581 AUDIT -->\n'
audit_end = b'<!-- END STEP581 AUDIT -->\n\n'
for name, original in saved['input_sha256'].items():
    data = (ROOT / name).read_bytes()
    current = sha(data)
    reconstructed = False
    if name == 'lemmas/L815-polya-census-real-path-tail-bounds.md':
        assert data.count(audit_start) == data.count(audit_end) == 1
        before, remaining = data.split(audit_start)
        _, after = remaining.split(audit_end)
        data = before + after
        reconstructed = True
    hashes[name] = dict(current_sha256=current, original_sha256=original,
                       reconstructed_sha256=sha(data), annotation_removed=reconstructed,
                       original_matches=sha(data) == original)

series = {}
for q in (5, 239):
    terms = [Fraction((-1) ** k, (2 * k + 1) * q ** (2 * k + 1))
             for k in range(120)]
    partial = sum(terms, Fraction(0))
    remainder = Fraction(1, 241 * q ** 241)
    series[q] = dict(q=q, first_index=0, last_index=119, terms=120,
                     partial_sum=rational(partial), next_index=120,
                     symmetric_remainder=rational(remainder),
                     next_term_sign='positive',
                     finite_magnitudes_decrease=all(abs(terms[k+1]) < abs(terms[k])
                                                   for k in range(119)),
                     next_smaller_than_last=remainder < abs(terms[-1]),
                     exact_terms=[rational(t) for t in terms])
    series[q]['_partial'] = partial
    series[q]['_remainder'] = remainder

center = 16 * series[5]['_partial'] - 4 * series[239]['_partial']
error = 16 * series[5]['_remainder'] + 4 * series[239]['_remainder']
lower, upper = center - error, center + error
stored_lower, stored_upper = map(Fraction, saved['pi'])
margin_lower, margin_upper = lower - stored_lower, stored_upper - upper


def integer_comparison(left, right):
    # Exact cross products make the relevant inclusion inequality explicit.
    lhs = left.numerator * right.denominator
    rhs = right.numerator * left.denominator
    return dict(left=rational(left), right=rational(right),
                cross_left=str(lhs), cross_right=str(rhs),
                cross_difference=str(rhs-lhs), holds=lhs <= rhs)


def grid_bounds(value, exponent):
    # Small reported bounds, independently checked as exact rationals.
    unit = Fraction(1, 10 ** exponent)
    scaled = value / unit
    floor = scaled.numerator // scaled.denominator
    ceil = -(-scaled.numerator // scaled.denominator)
    return dict(unit=f'1/10^{exponent}', lower_integer=str(floor),
                upper_integer=str(ceil),
                verified=floor*unit <= value <= ceil*unit)


checks = dict(
    original_input_hashes_match=all(h['original_matches'] for h in hashes.values()),
    audit_original_hashes_match=all(audit['original_hashes'][n] == h
                                    for n, h in saved['input_sha256'].items()),
    saved_certificate_hash_matches_step581=sha(saved_bytes) == audit['saved_certificate_sha256'],
    saved_pi_matches_step581=saved['pi'] == audit['pi'],
    source_atan_expression_matches=ast.dump(atan) == ast.dump(expected_atan),
    source_machin_expression_matches=ast.dump(pi_assignment) == ast.dump(expected_pi),
    positive_ordered_saved_endpoints=0 < stored_lower < stored_upper,
    finite_magnitudes_decrease=all(s['finite_magnitudes_decrease']
                                  and s['next_smaller_than_last'] for s in series.values()),
    saved_lower_le_exact_lower=stored_lower <= lower,
    exact_upper_le_saved_upper=upper <= stored_upper,
)
for s in series.values():
    del s['_partial'], s['_remainder']
failures = [name for name, ok in checks.items() if not ok]
report = dict(
    step='583', scope='saved pi aggregate only; no census execution',
    arithmetic='Python Fraction over arbitrary-size integers; exact string endpoint parsing',
    python=platform.python_version(),
    provenance=dict(saved_certificate_sha256=sha(saved_bytes),
                    audit581_certificate_sha256=sha(audit_bytes),
                    audit581_script_sha256=sha((BASE/'audit-581.py').read_bytes()),
                    this_script_sha256=sha(Path(__file__).read_bytes()),
                    original_inputs=hashes),
    saved_pi=saved['pi'], series=list(series.values()),
    aggregate=dict(center=rational(center), symmetric_error=rational(error),
                   lower=rational(lower), upper=rational(upper)),
    comparisons=dict(lower=integer_comparison(stored_lower, lower),
                     upper=integer_comparison(upper, stored_upper)),
    margins=dict(lower=rational(margin_lower), upper=rational(margin_upper)),
    readable_exact_bounds=dict(lower_margin=grid_bounds(margin_lower, 50),
                               upper_margin=grid_bounds(margin_upper, 50),
                               symmetric_error=grid_bounds(error, 170)),
    checks=checks, failures=failures,
    conclusion=('PASS: exact aggregate enclosure is contained in saved pi interval; '
                'only the initial pi premise is repaired.' if not failures else
                'FAIL: retain unsupported status; conservative noncontainment alone does not refute pi.'),
    remaining=['actual power inclusion counterexample is unchanged',
               'analytic tails, trig, normalization, grid and whole-cell audit',
               'all thirteen exclusions unverified; [6.5,40] unresolved',
               'unbounded domain, signs, common/multiple zeros and RH open'],
)
OUT.write_text(json.dumps(report, indent=2)+'\n')
print(json.dumps(dict(certificate=str(OUT.relative_to(ROOT)), checks=checks,
                     actual_exact_bounds=report['readable_exact_bounds'],
                     required='both endpoint margins >= 0', failures=failures)))
sys.exit(0 if not failures else 1)
