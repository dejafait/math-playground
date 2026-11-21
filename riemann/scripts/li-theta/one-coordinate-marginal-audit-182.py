#!/usr/bin/env python3
"""Independent labeled-factor deletion audit of C969a (no construction import).

The analytic hypotheses and all-point convergence are checked in C969a.
This certificate checks the entire contraction and complete scaled limit.
"""
from collections import defaultdict
from fractions import Fraction as F
import json
from pathlib import Path

OUT = Path(__file__).with_suffix('.json')
b, h, q = F(1, 4), F(5184), F(72)
D = h - b
d1, d2 = 4*h*h/D**2, h/D
moment = {'B0': 'm0', 'B1': 'm1', 'B2': 'm2', 'C0': 'v0', 'C1': 'v1'}
tensors = [
    ('first', d1, ('B1', 'B0', 'C0')),
    ('second', d2, ('B2', 'B0', 'C0')),
    ('even', -d2, ('B1', 'B1', 'C0')),
    ('distant', -d1, ('B0', 'B0', 'C1')),
]

# Work with 3J. Delete each labeled factor once. The two remaining
# orderings average to S; equal function names still have distinct labels.
actual = defaultdict(F)
deletions = []
for name, coefficient, factors in tensors:
    for label in range(3):
        remaining = tuple(sorted(factors[:label] + factors[label+1:]))
        key = (moment[factors[label]],) + remaining
        actual[key] += coefficient
        deletions.append({'tensor': name, 'integrated_label': label,
                          'moment': key[0], 'remaining_pair': list(remaining),
                          'coefficient_in_3J': str(coefficient)})

# Independent reading of all ten contributions in C969a(2).
expected_terms = [
    (d1, 'm1', 'B0', 'C0'), (d2, 'm2', 'B0', 'C0'),
    (d1, 'm0', 'B1', 'C0'), (-2*d2, 'm1', 'B1', 'C0'),
    (d2, 'm0', 'B2', 'C0'), (d1, 'v0', 'B1', 'B0'),
    (d2, 'v0', 'B2', 'B0'), (-d2, 'v0', 'B1', 'B1'),
    (-2*d1, 'm0', 'B0', 'C1'), (-d1, 'v1', 'B0', 'B0'),
]
expected = defaultdict(F)
for coefficient, m, f, g in expected_terms:
    expected[(m,) + tuple(sorted((f, g)))] += coefficient
residual = {key: actual[key]-expected[key]
            for key in actual.keys() | expected.keys()
            if actual[key] != expected[key]}

# Sparse commutative polynomials, monomials are sorted variable-name tuples.
def poly(value):
    return {(): F(value)} if value else {}

def variable(name):
    return {(name,): F(1)}

def add(*ps):
    result = defaultdict(F)
    for p in ps:
        for monomial, coefficient in p.items():
            result[monomial] += coefficient
    return {m: c for m, c in result.items() if c}

def times(p, r):
    result = defaultdict(F)
    for m, c in p.items():
        for n, d in r.items():
            result[tuple(sorted(m+n))] += c*d
    return {m: c for m, c in result.items() if c}

def scale(p, c):
    return times(p, poly(c))

def substitute(p, values):
    result = {}
    for monomial, coefficient in p.items():
        term = poly(coefficient)
        for name in monomial:
            term = times(term, values.get(name, variable(name)))
        result = add(result, term)
    return result

def records(p):
    return [{'monomial': list(m), 'coefficient': str(c)} for m, c in sorted(p.items())]

# Ratios to E, additionally divided by g=gamma/(4q); s=1/gamma.
leading = {'B0': poly(1), 'B1': {}, 'B2': {}, 'C0': poly(1),
           'C1': scale(variable('s'), 2*D)}
raw = {}
per_tensor = {}
for name, coefficient, factors in tensors:
    value = {}
    for label in range(3):
        others = factors[:label] + factors[label+1:]
        term = times(variable(moment[factors[label]]),
                     times(leading[others[0]], leading[others[1]]))
        value = add(value, scale(term, coefficient/d1))
    per_tensor[name] = records(value)
    raw = add(raw, value)

a0, a1, c0, c1 = [variable(s) for s in ('a0', 'a1', 'c0', 'c1')]
values = {'m0': poly(F(1, 2)), 'm1': scale(a0, 2), 'm2': scale(a1, 4),
          'v0': add(poly(F(1, 2)), scale(c0, 2*D)),
          'v1': add(scale(c0, 2), scale(c1, 2*D)),
          's': scale(add(c0, c1), 2)}
normalized = substitute(raw, values)
claimed = add(scale(a0, 2), scale(a1, D/h),
              scale(c0, -(2+4*D)), scale(c1, -6*D))
upper = add(scale(c0, -4*D), scale(c1, -D*(6-1/h)))
gap = add(scale(add(c0, scale(a0, -1)), 2),
          scale(add(c1, scale(a1, -1)), D/h))
normalization_residual = add(normalized, scale(claimed, -1))
domination_residual = add(upper, scale(normalized, -1), scale(gap, -1))
checks = {
    'all_12_labeled_deletions': len(deletions) == 12,
    'entire_contraction_matches': not residual,
    'normalization_matches': not normalization_residual,
    'domination_identity_matches': not domination_residual,
    'q_squared_is_h': q*q == h,
    'b_prescribed': b == F(1, 4),
    'd2_over_d1': d2/d1 == D/(4*h),
    'limit_prefactor': d1/(48*q*q) == h/(12*D*D),
    'strict_sign_parameters': D > 0 and 6-1/h > 0,
}
failures = [name for name, passed in checks.items() if not passed]
certificate = {
    'scope': 'C969a fixed n=2, complete L969(5), exact actual normalization',
    'method': 'Delete each of three labeled factors; average the remaining pair. No construction imports.',
    'parameters': {k: str(v) for k, v in [('b', b), ('h', h), ('q', q), ('Delta', D), ('d1', d1), ('d2', d2)]},
    'deletions': deletions,
    'contraction_3J': [{'moment': k[0], 'pair': list(k[1:]), 'coefficient': str(v)}
                       for k, v in sorted(actual.items()) if v],
    'scaling': 'per-tensor limits and raw sum are 3L/(d1*g^2), g=gamma/(4q), s=1/gamma',
    'per_tensor_limits': per_tensor,
    'raw_limit': records(raw), 'actual_moment_substitution': {k: records(v) for k, v in values.items()},
    'normalized_limit': records(normalized), 'strict_upper_bracket': records(upper),
    'upper_minus_actual': records(gap),
    'residuals': {'contraction': [{'key': list(k), 'value': str(v)} for k, v in sorted(residual.items())],
                  'normalization': records(normalization_residual), 'domination': records(domination_residual)},
    'analytic_requirements': ['A continuous and positive; all fixed slices and products absolutely integrable',
                              'Fixed gamma=1/[2(c0+c1)]>0; all five factor limits',
                              'c0>=a0>0 and c1>=a1>0 by entire nonnegative-series comparison',
                              'Finite negative limit and continuity; no limit under an integral'],
    'actual_bound': 'L <= -h*gamma^2/(12*Delta) [4*c0+(6-1/h)*c1] < 0',
    'required_bound': 'A globally nonnegative marginal would require L>=0',
    'checks': checks, 'failures': failures,
}
OUT.write_text(json.dumps(certificate, indent=2)+'\n')
print(f'Checks: {sum(checks.values())}/{len(checks)}; labeled deletions: {len(deletions)}; failures: {failures}')
print(f'Actual sign: L<0; required pointwise limit: L>=0. Delta={D}>0; 6-1/h={6-1/h}>0.')
print('Contraction, normalization and domination residuals:', len(residual), len(normalization_residual), len(domination_residual))
print('Certificate:', OUT.relative_to(Path(__file__).resolve().parents[2]))
raise SystemExit(bool(failures))
