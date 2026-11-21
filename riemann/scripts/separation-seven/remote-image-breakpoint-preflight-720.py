#!/usr/bin/env python3
"""Exact preflight of ONE direct overlap-primitive prescription; no scalar batch."""
from fractions import Fraction
from hashlib import sha256
from pathlib import Path
import json

BASE = Path(__file__).resolve().parent
OUT = BASE / 'remote-image-breakpoint-preflight-720.json'
WITNESS = BASE / 'defect-window-fixed-pair-707-witness.json'
PIN = '99ebc79ed3d82771ad0b5567356ba953e0d123d86aecdfe07d8e57f6fb9c634a'
checks = []


def check(name, predicate):
    checks.append(dict(name=name, passed=bool(predicate)))


def factor(n):
    factors = []
    d = 2
    while d*d <= n:
        exponent = 0
        while n % d == 0:
            n //= d
            exponent += 1
        if exponent:
            factors.append((d, exponent))
        d += 1
    if n > 1:
        factors.append((n, 1))
    return factors


raw = json.loads(WITNESS.read_text())
alpha = [Fraction(s) for s in raw['alpha_free']]
check('unchanged complete witness', sha256(WITNESS.read_bytes()).hexdigest() == PIN)
check('all510 alpha free coordinates nonzero', len(alpha) == 510 and all(alpha))
check('enumeration window covers active squared interval',
      1024**2 < 3**13 and 4096**2 > 3**15)
active = []
for n in range(1025, 4096):
    if 3**13 < n*n < 3**15:
        factors = factor(n)
        if len(factors) == 1:
            p, exponent = factors[0]
            active.append(dict(n=n, p=p, exponent=exponent))
ns = [a['n'] for a in active]
check('all334 shifts retained', len(ns) == 334)
check('identity2187 and structural3125 retained', 2187 in ns and 3125 in ns)

# Independent enumeration by sieve and powers, rather than trial factoring.
sieve = [True]*4096
sieve[0:2] = [False, False]
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
check('entire list agrees with sieve-power enumeration', sorted(independent) == ns)

rows = []
for i, a in enumerate(ns):
    overlap, disjoint = [], []
    for b in ns[i+1:]:
        (overlap if b*b < 3*a*a else disjoint).append(b)
    rows.append(dict(a=a, positive_length_later=overlap, disjoint_later=disjoint))
overlap_pairs = sum(len(r['positive_length_later']) for r in rows)
disjoint_pairs = sum(len(r['disjoint_later']) for r in rows)
check('all unordered distinct pairs accounted',
      overlap_pairs+disjoint_pairs == len(ns)*(len(ns)-1)//2)
check('no boundary equality hidden by strict comparison',
      all(b*b != 3*a*a for i, a in enumerate(ns) for b in ns[i+1:]))

# Independent monotone-window overlap count, indexed by the larger shift.
first = 0
window_count = 0
for j, b in enumerate(ns):
    while first < j and 3*ns[first]*ns[first] <= b*b:
        first += 1
    window_count += j-first
check('entire pair count agrees with monotone window', window_count == overlap_pairs)
check('identity overlaps every other active shift',
      all(max(n, 2187)**2 < 3*min(n, 2187)**2 for n in ns))

free = len(alpha)
off_terms = overlap_pairs*free*free
self_terms = (len(ns)-1)*free*(free+1)//2  # Identity self term uses orthonormality.
minimum_accumulations = off_terms+self_terms
cap = 10**8
check('selected direct-primitive subtask exceeds cap', minimum_accumulations > cap)
check('even identity overlaps plus nonidentity self terms exceed cap',
      (len(ns)-1)*(free*free+free*(free+1)//2) > cap)
failures = [c['name'] for c in checks if not c['passed']]
result = dict(
    step='720', witness_sha256=PIN,
    source_script_sha256=sha256(Path(__file__).read_bytes()).hexdigest(),
    checks=checks, failures=failures, active_prime_powers=active, pair_partition=rows,
    work=dict(
        prescription='Direct cellwise shift-pair/cosine-mode-pair primitives for Cpp(0), exchange symmetry, identity self term orthonormal',
        active_shifts=len(ns), nonzero_free_modes=free,
        unordered_distinct_overlap_pairs=overlap_pairs,
        unordered_distinct_disjoint_pairs=disjoint_pairs,
        nonidentity_self_pairs=len(ns)-1,
        distinct_shift_free_mode_terms=off_terms,
        nonidentity_self_free_mode_terms=self_terms,
        mandatory_accumulation_lower_bound=minimum_accumulations,
        required_total_operation_cap=cap,
        excess_factor=str(Fraction(minimum_accumulations, cap)),
        total_operation_upper_bound=None, sufficient_precision_bits=None,
        sufficient_byte_storage=None,
        model='Each enumerated primitive term is separately added to a scalar accumulator. At least one arithmetic operation per term; primitive evaluation and all other work are additional. This is a lower count for this implementation only.',
    ),
    error=dict(required_total_absolute_error='1/1000000',
               proved_total_absolute_error=None, all_error_terms_paid=False),
    unpaid=[
        'C0 head-mode terms and every K14/projection mixed term',
        'Both exact moments, full K14, constants and support tail',
        'Correlation breakpoints and complex analytic panel bounds',
        'Diagonal omission, inner/outer quadrature, nodes and weights',
        'All preparation, rounding, sufficient precision and byte storage',
    ],
    decision='PARK selected direct pairwise-primitive preparation before panel design or a scalar batch',
    scalar_evaluated=False, gram_evaluated=False, quadrature_batch_executed=False,
    qualifications=[
        'No lower complexity bound for other representations or algorithms',
        'No scalar value, actual-error lower bound, sign, S3 or RH result',
        'C998t/C998s prose contains the analytic inputs; software checks only finite enumeration and counts',
        'Inherited analytic-response, neutral-core, IEEE754/Decimal and unreplayed c_star contracts persist',
    ],
)
OUT.write_text(json.dumps(result, indent=2)+'\n')
print(f'Checks: {len(checks)}; failures: {failures}')
print(f'Positive-length distinct-shift overlaps: {overlap_pairs}; disjoint: {disjoint_pairs}')
print(f'Mandatory direct accumulations: {minimum_accumulations}; total-operation cap: {cap}')
print('Decision: PARK this implementation; total error, precision, byte storage: UNPAID')
print('Scalar/Gram/quadrature batches: not run')
print(f'Certificate: {OUT.relative_to(BASE.parent.parent)}')
if failures:
    raise SystemExit(1)
