"""Audit all relevant saved finite evidence for L028, without rewriting it.

Finite transcription checks do not prove the all-horizon/real-B claim.
See canonical L028 for that proof and its critical audit.
"""
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import json
import re

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
endpoint_path = HERE / 'certificate.json'
anchor_path = HERE.parent / 'odd-run-coalescence/certificate.json'
endpoint = json.loads(endpoint_path.read_text())
anchor = json.loads(anchor_path.read_text())
failures = []


def require(ok, context):
    if not ok:
        failures.append(context)


def T(n):
    return n // 2 if n % 2 == 0 else (3*n+1) // 2


def rational(value):
    return [value.numerator, value.denominator]


require(endpoint['failures'] == [], 'producer endpoint failures')
slope_results = []
require([c['L'] for c in endpoint['slope_cases']] == [6, 12, 24, 48],
        'all four slope cases present')
for case in endpoint['slope_cases']:
    L = case['L']
    records = {(r['s'], r['t'], r['a']): r
               for r in case['slope_above_one_records']}
    require(len(records) == len(case['slope_above_one_records']),
            f'unique slope records L={L}')
    keys = set()
    maximum, checked = Q(0), 0
    counts = dict.fromkeys(['h_negative', 'nonnegative_exponents', 'j_negative'], 0)
    for t in range(L+1):
        odd_count = t - int(t >= 5)
        for s in range(L+1):
            for a in range(s+1):
                checked += 1
                # Start from forward slopes on both paths, then divide.
                slope = Q(3**odd_count, 2**t) / Q(3**a, 2**s)
                if slope <= 1:
                    continue
                key = (s, t, a)
                keys.add(key)
                ratio = 2**s / (slope-1)
                require(ratio <= 4**L, f'ratio bound {L}/{key}')
                maximum = max(maximum, ratio)
                h, j = s-t, odd_count-a
                kind = ('h_negative' if h < 0 else
                        'nonnegative_exponents' if j >= 0 else 'j_negative')
                counts[kind] += 1
                intermediate = (2**t if h < 0 else
                                2**s if j >= 0 else 2**s * 3**(-j))
                lower = (slope-1)*(4**L+1)+slope-2**s
                require(lower > 0 and ratio <= intermediate <= 4**L,
                        f'offset/size margin {L}/{key}')
                row = records.get(key)
                require(row is not None, f'missing record {L}/{key}')
                if row is not None:
                    require(row['case'] == kind and Q(*row['slope']) == slope
                            and Q(*row['ratio']) == ratio
                            and Q(*row['intermediate_bound']) == intermediate
                            and Q(*row['strict_order_lower_bound']) == lower,
                            f'exact record {L}/{key}')
    require(keys == set(records), f'complete slope coverage L={L}')
    require(checked == case['all_exponent_triples_checked']
            and counts == case['case_counts']
            and maximum == Q(*case['maximum_ratio'])
            and case['required_ratio_upper_bound'] == 4**L,
            f'slope summary L={L}')
    slope_results.append({'L': L, 'triples_checked': checked,
                          'above_one_records_checked': len(keys),
                          'actual_maximum_ratio': rational(maximum),
                          'required_ratio_at_most': 4**L, 'case_counts': counts})

root_results = []
require([c['B'] for c in endpoint['root_cases']] == [[0, 1], [1, 1], [5, 2], [10, 1]],
        'all four root cases present')
for case in endpoint['root_cases']:
    p, q = case['B']
    L, n = case['L'], case['root']
    H, M = 4**L, 162*6**L
    upper = 163*6**L
    require(q > 0 and p >= 0 and L >= 6, f'root domains B={p}/{q}')
    require(2**(q*L) >= 163**q*12**p
            and (L == 6 or 2**(q*(L-1)) < 163**q*12**p),
            f'exact ceiling B={p}/{q}')
    require((n-47) % 3**(L+4) == 0 and (81*n+97) % 2**(L+1) == 0,
            f'root congruences L={L}')
    require(n > H and n-M <= H and n <= H+M < upper,
            f'first representative strictly above H L={L}')
    r = case['CRT_residue']
    require(0 <= r < M and n == r+M*case['CRT_multiplier']
            and case['CRT_modulus'] == M, f'CRT records L={L}')
    require(n > 47 and n % 243 == 47 and (n+1) % 32 == 16,
            f'root cylinder/valuation L={L}')
    actual_clock, required_clock = n**q * 12**p, 12**(q*L)
    require(actual_clock < required_clock, f'strict endpoint clock L={L}')
    require(case['required_strict_lower_bound'] == H
            and case['actual_upper_bound'] == H+M
            and case['required_strict_upper_bound'] == upper
            and case['clock_actual_exponentiated'] == actual_clock
            and case['clock_required_strict_upper_bound'] == required_clock,
            f'root bound records L={L}')
    path = case['actual_path']
    require(len(path) == L+1 and path[0] == n, f'complete path L={L}')
    for t, x in enumerate(path):
        K = Q(3**(t-int(t >= 5)), 2**t)
        shift = Q(1) if t <= 4 else Q(97, 81)
        require(x+1 == K*(n+shift), f'actual affine identity L={L}/t={t}')
        if t < L:
            require(x % 2 == int(t != 4) and T(x) == path[t+1],
                    f'actual path edge L={L}/t={t}')
    root_results.append({'B': [p, q], 'L': L, 'root': n,
                         'required_above': H, 'required_below': upper,
                         'actual_clock_exponentiated': actual_clock,
                         'required_clock_below': required_clock,
                         'actual_edges_checked': L, 'required_edges': L})

# Only the slope table and anchor orbit are essential from L026's finite
# evidence. Its inverse trees support transcription but are not premises.
rows = anchor['slope_comparisons']
require([r['h'] for r in rows] == list(range(1, 54)), 'all 53 anchor slopes')
for row in rows:
    h, b = row['h'], row['least_b']
    require(3**(b-1) <= 2**h < 3**b, f'least anchor exponent h={h}')
    require(row['strict_margin'] == 243*3**b-244*2**h > 0,
            f'anchor separation h={h}')
proof = (ROOT / 'lemmas/L026-fixed-valuation-residue47-coalescence-obstruction.md').read_text()
table = re.findall(r'^\| (\d+)–(\d+) \| ([\d,]+) \| (\d+) \|$', proof, re.M)
require(len(table) == 6, 'canonical anchor table coverage')
for low, high, exponents, margin in table:
    selected = rows[int(low)-1:int(high)]
    require([r['least_b'] for r in selected] == list(map(int, exponents.split(',')))
            and min(r['strict_margin'] for r in selected) == int(margin),
            f'canonical anchor table {low}-{high}')
orbit = anchor['anchor_orbit']
canonical_orbit = list(map(int, re.search(r'```text\n([\d,\s]+)\.\n```', proof).group(1).replace('\n', '').split(',')))
require(orbit == canonical_orbit, 'canonical entire anchor orbit')
require(len(orbit) == 67 and orbit[0] == 47 and orbit[59] == 40 and orbit[66] == 1,
        'anchor orbit indices')
for i, (x, y) in enumerate(zip(orbit, orbit[1:])):
    require(T(x) == y, f'anchor edge {i}')
require(T(1) == 2 and T(2) == 1 and max(orbit[59:]+[2]) == 40,
        'all later anchor iterates at most 40')

result = {
    'scope': 'Complete relevant finite evidence only; real-B/all-horizon proof audited in L028',
    'input_sha256': {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
                     for p in (endpoint_path, anchor_path)},
    'slope_cases': slope_results, 'root_cases': root_results,
    'anchor_slope_comparisons': rows, 'anchor_orbit': orbit,
    'anchor_rows_checked': len(rows), 'required_anchor_rows': 53,
    'anchor_edges_checked': len(orbit)-1, 'required_anchor_edges': 66,
    'actual_tail_bound': max(orbit[59:]+[2]), 'required_tail_bound_at_most': 40,
    'failures': failures,
}
out = HERE / 'audit-certificate.json'
out.write_text(json.dumps(result, indent=2)+'\n')
for case in slope_results:
    print(f'L={case["L"]}: {case["triples_checked"]} triples; maximum '
          f'{case["actual_maximum_ratio"]} <= required {case["required_ratio_at_most"]}.')
for case in root_results:
    print(f'B={case["B"]}: root {case["root"]} > {case["required_above"]}, '
          f'< {case["required_below"]}; exact clock below required L={case["L"]}; '
          f'{case["actual_edges_checked"]}/{case["required_edges"]} edges checked.')
print(f'Anchor: {len(rows)}/53 margins > 0; {len(orbit)-1}/66 edges; tail bound 40 <= 40.')
print('Failures:', failures)
print('Full audit certificate:', out)
raise SystemExit(bool(failures))
