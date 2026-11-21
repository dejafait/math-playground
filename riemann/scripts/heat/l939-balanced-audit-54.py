"""Independent exact algebra audit for L939; no analytic/numerical tail claim."""
from fractions import Fraction as F
from math import factorial, prod
from pathlib import Path
import ast
import hashlib
import json

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / 'lemmas/L938-actual-h2-fixed-energy-density-and-cell-test.md'
OLD = ROOT / 'scripts/heat/l938-balanced-coefficient-52.json'
OUT = Path(__file__).with_suffix('.json')
zero = (0,) * 6

def weight(a):
    return sum((i + 1) * x for i, x in enumerate(a))

def add(*parts):
    out = {}
    for p in parts:
        for a, c in p.items():
            out[a] = out.get(a, F(0)) + c
    return {a: c for a, c in out.items() if c}

def scale(p, c):
    return {a: c * v for a, v in p.items() if c * v}

def mul(p, q, cap=12):
    out = {}
    for a, c in p.items():
        for b, d in q.items():
            ab = tuple(x + y for x, y in zip(a, b))
            if weight(ab) <= cap:
                out[ab] = out.get(ab, F(0)) + c * d
    return {a: c for a, c in out.items() if c}

# Truncated formal log, not the producer's Newton recurrence.
h = {tuple(int(i == k) for i in range(6)): F((-1) ** (k + 1))
     for k in range(6)}
power = {zero: F(1)}
logarithm = {}
for j in range(1, 7):
    power = mul(power, h, 6)
    logarithm = add(logarithm, scale(power, F((-1) ** (j + 1), j)))
S = [{a: -n * c for a, c in logarithm.items() if weight(a) == n}
     for n in range(1, 7)]
a, b, c, d, e = S[1:]
determinant = add(mul(mul(a, c), e), scale(mul(a, mul(d, d)), -1),
                  scale(mul(mul(b, b), e), -1),
                  scale(mul(mul(b, c), d), 2), scale(mul(mul(c, c), c), -1))
derived = {(12 - sum(alpha),) + alpha: value for alpha, value in determinant.items()}
rows = []
for line in SOURCE.read_text().splitlines():
    fields = [v.strip() for v in line.split('|')]
    if len(fields) == 4 and fields[1].lstrip('-').isdigit() and fields[2].startswith('('):
        rows.append((int(fields[1]), ast.literal_eval(fields[2])))
old = json.loads(OLD.read_text())
checks = {}
def check(name, passed):
    checks[name] = bool(passed)
check('all_34_unique_rows', len(rows) == len(dict((a, c) for c, a in rows)) == 34)
check('formal_log_determinant_matches_entire_table', derived == dict((a, F(c)) for c, a in rows))
record = []
for i, (coefficient, alpha) in enumerate(rows):
    denominator = prod(factorial(2 * k) ** v for k, v in enumerate(alpha))
    term = F(coefficient, denominator)
    oldrow = old['rows'][i]
    check(f'row_{i}_degree', sum(alpha) == 12 and sum(k*v for k,v in enumerate(alpha)) == 12)
    check(f'row_{i}_saved_evidence', tuple(oldrow['alpha']) == alpha and
          oldrow['coefficient'] == coefficient and
          int(oldrow['factorial_denominator']) == denominator and F(oldrow['term']) == term)
    record.append({'alpha': alpha, 'coefficient': coefficient,
                   'denominator': str(denominator), 'term': str(term)})
def evaluate(p):
    return sum((c / prod(factorial(2*(k+1)) ** v for k,v in enumerate(a))
                for a,c in p.items()), F(0))
values = [evaluate(p) for p in S]
total = sum((F(v['term']) for v in record), F(0))
absolute = sum((abs(F(v['term'])) for v in record), F(0))
check('positive_exact_coefficient', total == F(1, 371319795000) and total > 0)
check('independent_log_value', evaluate(determinant) == total)
check('six_saved_newton_values', values == list(map(F, old['newton_S1_to_S6'])))
check('saved_coefficient_and_determinant', total == F(old['coefficient_C']) == F(old['newton_determinant']))
check('saved_absolute_sum', absolute == F(old['absolute_sum']))
check('cancellation_ratio', absolute / total == F(3893731, 1024) == F(old['absolute_to_signed_ratio']))
check('simplex_value', total / 12**12 == F(old['simplex_polynomial_at_balance']))
failures = [name for name, passed in checks.items() if not passed]
out = {'scope': 'Exact finite algebra only; analytic audit is canonical in L939.',
       'source': str(SOURCE.relative_to(ROOT)),
       'source_sha256': hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
       'old_certificate_sha256': hashlib.sha256(OLD.read_bytes()).hexdigest(),
       'method': 'Six-variable truncated formal log, determinant, homogenization; complete table and saved row comparison.',
       'rows': record, 'log_values_S1_to_S6': list(map(str, values)),
       'coefficient': str(total), 'required_coefficient': '1/371319795000 > 0',
       'absolute_sum': str(absolute), 'absolute_to_signed_ratio': str(absolute / total),
       'checks': checks, 'passed': sum(checks.values()), 'required': len(checks), 'failures': failures}
OUT.write_text(json.dumps(out, indent=2) + '\n')
print(f'Exact checks {sum(checks.values())}/{len(checks)}; rows {len(rows)}/34; failures={failures}')
print(f'C={total}; required=1/371319795000 > 0; absolute/signed={absolute / total}')
print(f'certificate={OUT.relative_to(ROOT)}')
if failures:
    raise SystemExit(1)
