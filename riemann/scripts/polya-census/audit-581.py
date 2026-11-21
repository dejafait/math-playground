"""Bounded audit of the preserved census579; never runs its census loop."""
import ast
from decimal import Decimal, Context, ROUND_FLOOR, ROUND_CEILING
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import platform
import decimal
import sys

BASE = Path(__file__).resolve().parent
ROOT = BASE.parent.parent
SOURCE = BASE / 'census-579.py'
CERT = BASE / 'census-579.json'
OUT = BASE / 'audit-581.json'
saved = json.loads(CERT.read_text())
tree = ast.parse(SOURCE.read_text(), filename=str(SOURCE))
prefix = []
for node in tree.body:
    if isinstance(node, ast.Assign) and any(
        isinstance(t, ast.Name) and t.id == 'start' for t in node.targets
    ):
        break
    prefix.append(node)
else:
    raise AssertionError('census loop boundary missing')
ns = {'__name__': 'census579_prefix'}
exec(compile(ast.Module(body=prefix, type_ignores=[]), str(SOURCE), 'exec'), ns)
I = ns['I']
original_pow = I.__pow__
records = []

def checked_pow(self, n):
    assert isinstance(n, int) and n > 0 and n % 2 == 1
    assert 0 <= self.a <= self.b
    result = original_pow(self, n)
    # Fraction(Decimal) is the exact finite decimal rational. All powers
    # and comparisons here use Python's arbitrary-size integer arithmetic.
    exact_lower = Fraction(self.a) ** n
    exact_upper = Fraction(self.b) ** n
    records.append(dict(
        base=self.data(), exponent=n, returned=result.data(),
        lower_outward=Fraction(result.a) <= exact_lower,
        upper_outward=Fraction(result.b) >= exact_upper,
    ))
    return result

I.__pow__ = checked_pow
pi_replay = 16 * ns['atan'](5) - 4 * ns['atan'](239)
I.__pow__ = original_pow
audit_start = b'<!-- BEGIN STEP581 AUDIT -->\n'
audit_end = b'<!-- END STEP581 AUDIT -->\n\n'
hashes = {}
current_hashes = {}
reconstructed = []
for p in saved['input_sha256']:
    data = (ROOT / p).read_bytes()
    current_hashes[p] = hashlib.sha256(data).hexdigest()
    # The canonical lemma retains the exact original text, with one clearly
    # marked new audit section. Remove only that section for historical
    # provenance checking; never mutate either source or original certificate.
    if p == 'lemmas/L815-polya-census-real-path-tail-bounds.md' and audit_start in data:
        assert data.count(audit_start) == data.count(audit_end) == 1
        before, remaining = data.split(audit_start)
        _, after = remaining.split(audit_end)
        data = before + after
        reconstructed.append(p)
    hashes[p] = hashlib.sha256(data).hexdigest()
hash_matches = {p: hashes[p] == h for p, h in saved['input_sha256'].items()}
reciprocals = []
for q in (5, 239):
    z = I(1) / q
    reciprocals.append(dict(q=q, interval=z.data(),
        contains_exact=Fraction(z.a) <= Fraction(1, q) <= Fraction(z.b)))
power_failures = [i for i, row in enumerate(records)
                  if not (row['lower_outward'] and row['upper_outward'])]
witnesses = []
for i in power_failures:
    row = records[i]
    b = Decimal(row['base'][1])
    h = Decimal(row['returned'][1])
    n = row['exponent']
    b_tuple, h_tuple = b.as_tuple(), h.as_tuple()
    m = int(''.join(map(str, b_tuple.digits)))
    a = int(''.join(map(str, h_tuple.digits)))
    denominator_exponent = -b_tuple.exponent * n
    shift = denominator_exponent + h_tuple.exponent
    assert shift >= 0
    numerator = m ** n - a * 10 ** shift
    delta = Fraction(numerator, 10 ** denominator_exponent)
    assert delta == Fraction(b) ** n - Fraction(h) > 0
    assert 2 * 10 ** 591 < numerator < 3 * 10 ** 591
    ulp = Fraction(10) ** h_tuple.exponent
    lower_context = Context(prec=20, rounding=ROUND_FLOOR)
    upper_context = Context(prec=20, rounding=ROUND_CEILING)
    def enclosure(value):
        pair = [lower_context.divide(Decimal(value.numerator), Decimal(value.denominator)),
                upper_context.divide(Decimal(value.numerator), Decimal(value.denominator))]
        assert Fraction(pair[0]) <= value <= Fraction(pair[1])
        return list(map(str, pair))
    # Report exact rational bounds, including the ideal outward result.
    exact_scaled = Fraction(b) ** n / ulp
    ceiling_coefficient = -(-exact_scaled.numerator // exact_scaled.denominator)
    ideal_upper = Decimal((0, tuple(map(int, str(ceiling_coefficient))), h_tuple.exponent))
    actual_argument = Fraction(1, 239)  # The failed call is checked below.
    assert i == 127 and n == 13
    witnesses.append(dict(call_index=i, upper_base_coefficient=str(m),
        upper_base_exponent=b_tuple.exponent, returned_upper_coefficient=str(a),
        returned_upper_exponent=h_tuple.exponent, exponent=n,
        exact_positive_difference_numerator=str(numerator),
        exact_positive_difference_denominator_power_of_ten=denominator_exponent,
        integer_sandwich_verified='2*10^591 < numerator < 3*10^591',
        integer_comparison_shift=shift,
        difference_ulp_bounds=enclosure(delta / ulp),
        difference_absolute_bounds=enclosure(delta),
        difference_ulp_bounds_verified=True,
        ideal_ceiling_upper=str(ideal_upper),
        true_reciprocal_power_still_inside=(Fraction(Decimal(row['returned'][0]))
            <= actual_argument ** n <= Fraction(h))))
checks = dict(
    all_original_hashes_match=all(hash_matches.values()),
    backend_matches=(platform.python_version() == saved['backend']['python']
                     and decimal.__libmpdec_version__ == saved['backend']['decimal']),
    power_call_count=len(records) == 242,
    every_actual_power_outward=not power_failures,
    exact_reciprocals=all(r['contains_exact'] for r in reciprocals),
    pi_matches_saved=pi_replay.data() == saved['pi'],
)
report = dict(step='581', scope='actual power calls and provenance; no census rerun',
    backend=dict(python=platform.python_version(), libmpdec=decimal.__libmpdec_version__),
    saved_certificate_sha256=hashlib.sha256(CERT.read_bytes()).hexdigest(),
    original_hashes=hashes, current_input_hashes=current_hashes,
    original_text_reconstructed_by_removing_new_audit=reconstructed,
    hash_matches=hash_matches, checks=checks,
    power_call_count=len(records), endpoint_comparisons=2*len(records),
    power_failures=power_failures, failure_witnesses=witnesses,
    reciprocal_checks=reciprocals,
    pi=pi_replay.data(), power_calls=records)
report['affected_exclusions'] = [dict(index=i, x=row['x'], kind=row['kind'])
    for i, row in enumerate(saved['cells']) if row['kind'] != 'unresolved']
report['unperformed_audit'] = ['full analytic tail audit', 'full trigonometric inclusion audit',
    'normalization and whole-cell integral audit', 'validation of all thirteen exclusions']
report['conclusion'] = ('FAIL: an actual interval power is not an inclusion extension; '
    'stored pi and numerical exclusions are not disproved, but remain unsupported by this argument.')
OUT.write_text(json.dumps(report, indent=2)+'\n')
print(json.dumps(dict(certificate=str(OUT.relative_to(ROOT)), checks=checks,
    actual_power_calls=len(records), required_power_calls=242,
    endpoint_comparisons=2*len(records), failures=power_failures,
    failure_bounds=[dict(call_index=w['call_index'], actual_upper=records[w['call_index']]['returned'][1],
        required_ceiling_upper=w['ideal_ceiling_upper'], shortfall_ulp=w['difference_ulp_bounds'])
        for w in witnesses])))
sys.exit(0 if all(checks.values()) else 1)
