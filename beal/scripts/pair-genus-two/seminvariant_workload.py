#!/usr/bin/env python3
"""One fixed seminvariant sieve feasibility test; no descent enumeration.

Run from beal. All interval arithmetic and progression counts are exact.
The work ledger includes table construction, CRT trials and floor counts.
"""
from collections import Counter
from fractions import Fraction as Q
from hashlib import sha256
from math import gcd, prod
from pathlib import Path
import json

OUT = Path('scripts/pair-genus-two/seminvariant-workload-certificate.json')
ASSESSMENT = 'drafts/literature/2026-10-25-marked-elliptic-seminvariant-enumeration.md'
I, J = 8624880, -46962471600
CAP, EXPANDED_CAP = 200000, 2000000
PRIMES = (5, 7, 11, 13)  # Fixed before execution; no parameter search.
ledger = Counter()
checks = {}


def check(name, condition):
    checks[name] = bool(condition)
    if not condition:
        raise AssertionError(name)


class WorkLimit(Exception):
    pass


def charge(kind):
    if sum(ledger.values()) == CAP:
        raise WorkLimit(kind)
    ledger[kind] += 1


def f(t):
    return t**3-3*I*t+J


def syzygy(a, p):
    return p**3-48*I*a*a*p-64*J*a**3


def square_interval(bounds):
    lo, hi = bounds
    return (0 if lo <= 0 <= hi else min(lo*lo, hi*hi),
            max(lo*lo, hi*hi))


def multiply(k, interval):
    x, y = (k*v for v in interval)
    return min(x, y), max(x, y)


root_strings = [
    ('-3562.729358095299', '-3562.729358095298'),
    ('-2262.749518242581', '-2262.749518242580'),
    ('5825.478876337878', '5825.478876337879')]
roots = [tuple(map(Q, interval)) for interval in root_strings]
root_evidence = [dict(interval=v, endpoint_values=[f(v[0]), f(v[1])]) for v in roots]
check('root_brackets_have_opposite_endpoint_signs',
      all(f(lo)*f(hi) < 0 for lo, hi in roots))
check('root_brackets_disjoint_ordered',
      roots[0][1] < roots[1][0] < roots[1][1] < roots[2][0])
phi3, phi2, phi1 = roots
sq2lo, sq2hi = square_interval(phi2)
D = (Q(4, 3)*(I-sq2hi), Q(4, 3)*(I-sq2lo))
region_spec = [('type1_positive', 1, 1043),
               ('type2_positive', 1, 898),
               ('type2_negative', -1, 144)]
regions = []
for name, sign, maximum in region_spec:
    for m in range(1, maximum+1):
        charge('signed_region_interval_preparations')
        a = sign*m
        if name == 'type1_positive':
            low, high = multiply(-4*a, phi1), multiply(-4*a, phi2)
        else:
            low = multiply(-4*a, phi3 if a > 0 else phi1)
            term = multiply(-4*a, phi2)
            high = (D[0]+term[0], D[1]+term[1])
        outer = (low[0].__ceil__(), high[1].__floor__())
        inner = (low[1].__ceil__(), high[0].__floor__())
        check(f'{name}_{a}_integer_endpoints_unambiguous', outer == inner)
        regions.append(dict(type=name, a=a, real_lower=low, real_upper=high,
                            outer_integer_interval=outer, inner_integer_interval=inner))
check('all_signed_regions_prepared', len(regions) == 1043+898+144)

# Exact divisibility: both coefficient terms vanish modulo 27.
check('syzygy_mod27_reduces_to_p_cubed', (48*I) % 27 == 0 and (64*J) % 27 == 0)
divisibility_table = []
for p in range(27):
    charge('divisibility_residue_cells')
    v = p**3 % 27 == 0
    divisibility_table.append(v)
    check(f'div27_compression_{p}', v == (p % 3 == 0))

# The 64 sieve is independent of a; compress its full predicate to mod 8.
check('syzygy_mod64_reduces_to_p_cubed', (48*I) % 64 == 0)
square_images = {}
square_tables = {}
for modulus in (64,)+PRIMES:
    values = []
    for r in range(modulus):
        charge('square_image_residue_cells')
        values.append(27*r*r % modulus)
    square_tables[str(modulus)] = values
    square_images[modulus] = set(values)
mod64_predicate = []
for p in range(64):
    charge('mod64_predicate_cells')
    v = p**3 % 64 in square_images[64]
    mod64_predicate.append(v)
    check(f'mod64_compression_{p}', v == (p % 8 in (0, 3, 4)))

modulus_product = 3*8*prod(PRIMES)
check('crt_moduli_pairwise_coprime',
      all(gcd(x, y) == 1 for n, x in enumerate((3, 8)+PRIMES)
          for y in ((3, 8)+PRIMES)[n+1:]))
rows = []
cumulative_pairs = 0
partial = None
stop_reason = None
for region in regions:
    # Only a prefix of type one is needed if it proves over-cap work.
    a = region['a']
    row = dict(type=region['type'], a=a,
               interval=region['inner_integer_interval'], allowed_residues={},
               crt_stage_sizes=[], progressions=[], pair_count=0,
               work_before=sum(ledger.values()), complete=False)
    try:
        allowed = [(3, [0]), (8, [0, 3, 4])]
        for modulus in PRIMES:
            residues = []
            for p in range(modulus):
                charge('prime_predicate_residue_cells')
                if syzygy(a, p) % modulus in square_images[modulus]:
                    residues.append(p)
            allowed.append((modulus, residues))
        row['allowed_residues'] = {str(m): v for m, v in allowed}
        residues, M = [0], 1
        for modulus, local in allowed:
            charge('crt_inverse_preparations')
            inverse = pow(M, -1, modulus)
            joined = []
            for x in residues:
                for y in local:
                    charge('crt_combination_trials')
                    joined.append(x+M*((y-x)*inverse % modulus))
            M *= modulus
            # CRT is a bijection; no sorting, deduplication or hidden scan.
            residues = joined
            row['crt_stage_sizes'].append(dict(modulus=M, size=len(residues)))
        check(f'crt_product_{a}', M == modulus_product)
        lo, hi = row['interval']
        for residue in residues:
            charge('aggregate_progression_counts')
            upper_q = (hi-residue)//M
            lower_q = (lo-1-residue)//M
            count = max(0, upper_q-lower_q)
            row['progressions'].append([residue, lower_q, upper_q, count])
            row['pair_count'] += count
        row['complete'] = True
    except WorkLimit as exc:
        partial = dict(row=row, blocked_operation=str(exc))
        stop_reason = 'STOP_COUNTING_CAP_INCOMPLETE'
        break
    row['work_after'] = sum(ledger.values())
    cumulative_pairs += row['pair_count']
    row['cumulative_pair_count'] = cumulative_pairs
    rows.append(row)
    if cumulative_pairs > CAP:
        stop_reason = 'STOP_FIXED_SIEVE_PAIR_INSPECTIONS_OVER_CAP'
        break
else:
    stop_reason = 'COUNT_COMPLETE_NO_ENUMERATION_IMPLEMENTED'

check('counting_work_within_cap', sum(ledger.values()) <= CAP)
check('expanded_candidates_zero', ledger['expanded_candidates'] == 0)
check('explicit_pair_and_b_root_trials_zero',
      ledger['explicit_pair_inspections'] == 0 and ledger['b_root_trials'] == 0)
if stop_reason == 'STOP_FIXED_SIEVE_PAIR_INSPECTIONS_OVER_CAP':
    check('completed_prefix_exceeds_pair_inspection_cap', cumulative_pairs > CAP)
    check('prefix_uses_only_type_one_positive_a',
          all(v['type'] == 'type1_positive' for v in rows))

certificate = dict(
    target="Assess whether enumerating syzygy-admissible (a,p,r) and solving 3b² ≡ p (mod 8a) can replace L128's over-cap coefficient loops without increasing the saved caps.",
    assessment=ASSESSMENT,
    inputs={p: sha256(Path(p).read_bytes()).hexdigest() for p in
            ('lemmas/L128-marked-elliptic-quartic-workload.md', ASSESSMENT)},
    invariants=dict(I=I, J=J), roots=root_evidence, D_interval=D,
    fixed_sieve=dict(exact_divisibility=27, square_image_moduli=[64, *PRIMES],
                     compressed_crt_moduli=[3, 8, *PRIMES], product=modulus_product,
                     mod27_predicate=divisibility_table,
                     mod64_predicate=mod64_predicate,
                     mod64_compressed_allowed_residues=[0, 3, 4],
                     square_image_tables=square_tables),
    region_intervals=regions, completed_count_rows=rows, partial_row=partial,
    workload=dict(caps=dict(counting_work=CAP, expanded_candidates=EXPANDED_CAP),
                  actual_counting_work=sum(ledger.values()), ledger=dict(ledger),
                  prepared_signed_intervals=len(regions),
                  complete_prefix_rows=len(rows),
                  certified_sieve_pair_lower_bound=cumulative_pairs,
                  required_explicit_pair_inspections_at_least=cumulative_pairs,
                  full_pair_count_computed=len(rows) == len(regions),
                  exact_square_tests=0, reconstructed_quartics=0,
                  expanded_candidates=0, original_abc_triples=0,
                  reconstruction_failures=[],
                  reconstruction_failure_scope='Not attempted; empty is not a success claim.',
                  result=stop_reason),
    coverage=dict(signed_real_regions='All intervals prepared; only recorded prefix counted.',
                  actual_syzygy_squares='Not computed; modular pairs are not integer r solutions.',
                  b_roots='Not computed; conditional complete recovery is proved in L129.',
                  enumeration='Not performed, because feasibility was not established.'),
    limitations=['Stops only this fixed sieve and per-p exact-square traversal.',
                 'No lower bound on actual square syzygies, quartics, classes or Selmer size.',
                 'No rank upper bound, marked-point control or Beal exclusion.'],
    checks=checks, failures=[k for k, v in checks.items() if not v])


def encode(value):
    if isinstance(value, Q):
        return str(value)
    raise TypeError(type(value).__name__)


OUT.write_text(json.dumps(certificate, default=encode, indent=2)+'\n')
print('Result:', stop_reason)
print('Counting work:', sum(ledger.values()), '/', CAP, '; ledger:', dict(ledger))
print('Prepared intervals:', len(regions), '; complete prefix rows:', len(rows))
print('Certified modular pair lower bound:', cumulative_pairs,
      '; required explicit inspections <=', CAP)
print('Expanded candidates: 0 /', EXPANDED_CAP, '; exact square tests: 0')
print('Checks:', len(checks), '; failures:', certificate['failures'])
print('Certificate:', OUT)
