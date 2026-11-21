#!/usr/bin/env python3
"""Exact partition/work test for ONE pairwise common-frequency prescription.

No correlation, scalar, FFT or quadrature batch is evaluated. The work
count is implementation-specific; the canonical proof is C998t Section8.
"""
from fractions import Fraction
from hashlib import sha256
from pathlib import Path
import json

BASE = Path(__file__).resolve().parent
OUT = BASE / 'remote-image-frequency-preflight-722.json'
WITNESS = BASE / 'defect-window-fixed-pair-707-witness.json'
PIN = '99ebc79ed3d82771ad0b5567356ba953e0d123d86aecdfe07d8e57f6fb9c634a'
checks = []


def check(name, predicate):
    checks.append(dict(name=name, passed=bool(predicate)))


def prime_power(n):
    for d in range(2, n + 1):
        if n % d == 0:
            p, exponent = d, 0
            while n % d == 0:
                n //= d
                exponent += 1
            return (p, exponent) if n == 1 else None
    return None


raw = json.loads(WITNESS.read_text())
alpha = [Fraction(s) for s in raw['alpha_free']]
check('unchanged witness hash', sha256(WITNESS.read_bytes()).hexdigest() == PIN)
check('510 nonzero free modes, indices2 through511', len(alpha) == 510 and all(alpha))
check('enumeration window contains entire active interval',
      1024**2 < 3**13 and 4096**2 > 3**15)
active = []
for n in range(1025, 4096):
    if 3**13 < n*n < 3**15:
        fac = prime_power(n)
        if fac is not None:
            active.append(dict(n=n, prime=fac[0], exponent=fac[1]))
ns = [r['n'] for r in active]
# Independent prime sieve and power enumeration.
sieve = [True] * 4096
sieve[:2] = [False, False]
for p in range(2, 64):
    if sieve[p]:
        for n in range(p*p, 4096, p):
            sieve[n] = False
independent = []
for p in range(2, 4096):
    if sieve[p]:
        n = p
        while n < 4096:
            if 3**13 < n*n < 3**15:
                independent.append(n)
            n *= p
check('complete prime-power enumerations agree', sorted(independent) == ns)
check('334 shifts including identity2187', len(ns) == 334 and 2187 in ns)

# Store exp(2*x) at endpoints. Log is strictly increasing, so all
# partition and first-overlap comparisons below are exact rationals.
events = []
for n in ns:
    if n > 2187:
        events.append(dict(n=n, kind='entrance', exp2x=Fraction(n*n, 3**14)))
    elif n < 2187:
        events.append(dict(n=n, kind='exit', exp2x=Fraction(n*n, 3**13)))
events.sort(key=lambda r: r['exp2x'])
values = [r['exp2x'] for r in events]
check('333 distinct interior events', len(values) == len(set(values)) == 333)
check('every event strictly inside cell', all(1 < v < 3 for v in values))
bounds = [Fraction(1)] + values + [Fraction(3)]
pieces = list(zip(bounds[:-1], bounds[1:]))
check('334 positive-width pieces', len(pieces) == 334 and all(a < b for a, b in pieces))
rows, bad_pairs = [], []
for i, (ai, bi) in enumerate(pieces):
    eligible = 0
    for j, (aj, bj) in enumerate(pieces[:i]):
        # First overlap: v0=ai-bj; v1=min(ai-aj,bi-bj).
        # exp(2*v0), exp(2*v1) can be compared without logarithms.
        start, stop = ai/bj, min(ai/aj, bi/bj)
        if not (1 <= start < stop <= 3 and stop <= bi/aj <= 3):
            bad_pairs.append(dict(i=i, j=j, start=str(start), stop=str(stop)))
        else:
            eligible += 1
    rows.append(dict(later_piece=i, earlier_piece_count=eligible))
pairs = sum(r['earlier_piece_count'] for r in rows)
check('all distinct pairs have a positive first-overlap branch', not bad_pairs)
check('pair enumeration equals binomial count', pairs == len(pieces)*(len(pieces)-1)//2)
check('pair enumeration equals independent sum', pairs == sum(range(len(pieces))))

free_positive_modes = len(alpha)
products = pairs * free_positive_modes
real_multiplications = 4 * products
real_additions = 2 * products
operations = real_multiplications + real_additions
cap = 10**8
check('four-real-multiplication subtask alone exceeds cap', real_multiplications > cap)
check('six-real-operation resonant subtask exceeds cap', operations > cap)
failures = [c['name'] for c in checks if not c['passed']]
result = dict(
    step='722', witness_sha256=PIN,
    script_sha256=sha256(Path(__file__).read_bytes()).hexdigest(),
    checks=checks, failures=failures,
    active_prime_powers=active,
    interior_events=[dict(n=e['n'], kind=e['kind'], exp2x=str(e['exp2x'])) for e in events],
    pieces=[dict(index=i, exp2left=str(a), exp2right=str(b)) for i, (a, b) in enumerate(pieces)],
    pair_rows=rows, invalid_first_overlap_pairs=bad_pairs,
    work=dict(
        prescription='Endpoint Toeplitz transforms reused; separate piece-pair coefficient assembly, explicit resonant affine terms, positive frequencies only, classical complex products',
        pieces=len(pieces), distinct_positive_lag_piece_pairs=pairs,
        counted_positive_modes=free_positive_modes,
        prescribed_complex_resonant_products=products,
        real_multiplication_lower_bound=real_multiplications,
        real_addition_lower_bound=real_additions,
        scalar_operation_lower_bound=operations,
        required_total_operation_cap=cap,
        excess_factor=str(Fraction(operations, cap)),
        total_operation_upper_bound=None, sufficient_precision_bits=None,
        sufficient_byte_storage=None,
        limitations='Counts prescribed products even if an exact coefficient vanishes. No zero pruning, reassociation, jump aggregation or non-pairwise implementation is tested. FFT costs are favorable zero.',
    ),
    error=dict(required_total_absolute_error='1/1000000',
               proved_total_absolute_error=None, all_error_terms_paid=False),
    unpaid=[
        'All endpoint Toeplitz transforms, coefficient preparation, padding and roots',
        'Modes0 and1, self pairs, nonresonant coefficients and remaining overlap branches',
        'Full K14, both exact P0 moments, every mixed contribution and analytic panels',
        'Compensated diagonal, exact support tail, constants, quadrature and node uncertainty',
        'All rounding, sufficient precision and byte storage',
    ],
    decision='PARK this separately assembled piece-pair prescription before scalar evaluation',
    scalar_evaluated=False, gram_evaluated=False, fft_executed=False,
    qualifications=[
        'Only a fixed implementation fails the operation cap; no algorithm-independent lower bound',
        'No scalar value, absolute-error lower bound, sign, S3 or RH conclusion',
        'Finite enumeration/count only; canonical prose establishes the correlation formula',
        'Analytic-response, neutral-core, IEEE754/Decimal and unreplayed c_star contracts persist',
    ],
)
OUT.write_text(json.dumps(result, indent=2) + '\n')
print(f'Checks: {len(checks)}; failures: {failures}')
print(f'Pieces: {len(pieces)}; distinct positive-lag pairs: {pairs}')
print(f'Resonant products: {products}; scalar operations >= {operations}; cap: {cap}')
print(f'Real multiplications alone >= {real_multiplications}; cap: {cap}')
print('Decision: PARK selected prescription; error, precision and bytes: UNPAID')
print('Scalar/Gram/FFT/quadrature batches: not run')
print(f'Certificate: {OUT.relative_to(BASE.parent.parent)}')
if failures:
    raise SystemExit(1)
