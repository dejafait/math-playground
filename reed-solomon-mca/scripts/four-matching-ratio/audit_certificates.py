"""Independent exhaustive audit of L040's two existing certificates.

Use direct colored-edge products rather than edge-product classes, and
three-edge subsets rather than recursive generation of perfect matchings.
Read the original certificates without modifying them; save every case
comparison, every threshold completion and all failures in a new artifact.
"""
import hashlib
import itertools as it
import json
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
FILES = ['paired-ratio-result.json', 'threshold-completion-result.json']
raw = [(HERE / name).read_bytes() for name in FILES]
first, second = [json.loads(data) for data in raw]
failures = []


def check(condition, label, detail=None):
    if not condition:
        failures.append({'check': label, 'detail': detail})


# Construct the group differently from the original root test. The full
# nonzero orbit proves that 5 has order 96; its sixth powers give order 16.
check(set(pow(5, j, 97) for j in range(96)) == set(range(1, 97)),
      'primitive generator')
H = sorted(set(pow(5, 6*j, 97) for j in range(16)))
check(len(H) == 16 and all(pow(z, 16, 97) == 1 for z in H), 'group')
check(first['H'] == H and first['field'] == 97, 'original group')
saved_cases = {(r['q'], tuple(r['W'])): r['maximum'] for r in first['cases']}
check(len(saved_cases) == len(first['cases']) == 45045, 'case uniqueness')
saved_rows = {(r['q'], tuple(r['W']), tuple(r['K0']), r['rho']): r
              for r in second['rows']}
check(len(saved_rows) == len(second['rows']), 'threshold row uniqueness')

case_audits = []
critical = []
threshold_audits = []
table = []
histogram = Counter()
threshold_tests = 0
rho_tests = 0
seen_rows = set()
all_case_keys = set()
for q in H:
    if q == 1:
        continue
    labels = [z for z in H if z != 1 and z != q]
    # Fermat inverses, independently of pow(x,-1,97) in the originals.
    b = {z: ((1-z) * pow((q-z) % 97, 95, 97)) % 97 for z in labels}
    check(len(set(b.values())) == 14 and 0 not in b.values(), 'ratio injectivity', q)
    for W in it.combinations(labels, 6):
        key = (q, W)
        all_case_keys.add(key)
        colors = [a for a in labels if a not in W]
        edges = list(it.combinations(W, 2))
        counts = [[0 for _ in colors] for _ in range(97)]
        for ai, a in enumerate(colors):
            for w, t in edges:
                rho = b[a] * b[w] * b[t] % 97
                counts[rho][ai] += 1
        maxima = [sum(sorted(row)[-4:]) for row in counts[1:]]
        rho_tests += len(maxima)
        actual = max(maxima)
        histogram[actual] += 1
        check(saved_cases.get(key) == actual, 'case maximum', [q, W, actual])
        check(actual <= 8, 'relaxed bound', [q, W, actual])
        case_audits.append({'q': q, 'W': W, 'maximum': actual,
                            'saved_maximum': saved_cases.get(key),
                            'maxima_by_rho_1_through_96': maxima})
        if actual < 8:
            continue
        critical.append({'q': q, 'W': list(W), 'maximum': actual})
        # Every perfect matching is exactly a three-edge subset whose six
        # endpoints are distinct. This independently covers all completions.
        matchings = [m for m in it.combinations(edges, 3)
                     if len(set(it.chain.from_iterable(m))) == 6]
        check(len(matchings) == 15, 'perfect matching domain', [q, W])
        for rho in range(1, 97):
            good = {a: tuple((w, t) for w, t in edges
                             if b[a]*b[w]*b[t] % 97 == rho) for a in colors}
            for K0 in it.combinations(colors, 4):
                threshold_tests += 1
                profile = [len(good[a]) for a in K0]
                if sum(profile) < 8:
                    continue
                row_key = (q, W, K0, rho)
                seen_rows.add(row_key)
                check(profile == [2, 2, 2, 2], 'threshold profile', row_key)
                options = [[m for m in matchings if set(good[a]) <= set(m)] for a in K0]
                completions = []
                for ms in it.product(*options):
                    multiplicity = Counter(it.chain.from_iterable(ms))
                    repeated = sorted(e for e, n in multiplicity.items() if n > 1)
                    check(bool(repeated), 'no disjoint completion', row_key)
                    completions.append({'matchings': [[list(e) for e in m] for m in ms],
                                        'repeated_edges': [list(e) for e in repeated]})
                check(len(completions) == 1, 'unique completion', row_key)
                expected_row = {'p': 1, 'q': q, 'W': list(W), 'K0': list(K0), 'rho': rho,
                                'good_edges': {str(a): [list(e) for e in good[a]] for a in K0},
                                'counts': profile,
                                'reason': 'all perfect-matching extensions repeat an edge',
                                'extension_count': len(completions),
                                'disjoint_extension_count': sum(not c['repeated_edges'] for c in completions),
                                'extension_conflicts': completions}
                check(saved_rows.get(row_key) == expected_row, 'complete saved threshold row', row_key)
                threshold_audits.append(expected_row)
                if len(completions) == 1 and profile == [2, 2, 2, 2]:
                    def code(e):
                        return ''.join(str(W.index(z)) for z in e)
                    goods = ['.'.join(code(e) for e in good[a]) for a in K0]
                    forced = [tuple(z for z in W if all(z not in e for e in good[a])) for a in K0]
                    check(all(len(e) == 2 for e in forced), 'forced edges', row_key)
                    repeats = completions[0]['repeated_edges']
                    table.append(f"{q} | {','.join(map(str,W))} | {','.join(map(str,K0))} | {rho} | "
                                 + '/'.join(goods) + ' | ' + '/'.join(code(e) for e in forced)
                                 + ' | ' + '.'.join(code(e) for e in repeats))

check(all_case_keys == set(saved_cases), 'complete case domain')
check(seen_rows == set(saved_rows), 'complete threshold domain')
check(critical == second['critical_six_sets'], 'complete critical six-set table')
check(table == second['complete_forced_table'], 'complete forced-edge table')
expected_first = {'normalized_pairs': 15, 'six_sets_per_pair': 3003,
                  'case_count': 45045, 'rho_values_per_case': 96,
                  'candidate_K0_count_per_case': 70, 'actual_maximum': max(histogram),
                  'required_for_equality': 8, 'exclusion_requires_maximum_at_most': 7,
                  'histogram': {str(k): v for k, v in sorted(histogram.items())}, 'failures': []}
for k, v in expected_first.items():
    check(first[k] == v, 'first summary ' + k)
expected_second = {'threshold_six_sets': len(critical), 'threshold_candidates': len(threshold_audits),
                   'count_profiles': dict(Counter(','.join(map(str, sorted(r['counts'])))
                                                  for r in threshold_audits)),
                   'total_extensions_checked': sum(r['extension_count'] for r in threshold_audits),
                   'disjoint_extensions': sum(r['disjoint_extension_count'] for r in threshold_audits),
                   'required_good_edges': 8, 'relaxed_maximum': max(histogram), 'failures': []}
for k, v in expected_second.items():
    check(second[k] == v, 'second summary ' + k)

# Verify the first file's separate extremal witness, including all b-values.
w = first['witness']
labels = [z for z in H if z not in (w['p'], w['q'])]
bs = {z: (w['p']-z)*pow((w['q']-z) % 97, 95, 97) % 97 for z in labels}
check(w['p'] == 1 and (w['q'], tuple(w['W'])) in all_case_keys, 'witness domain')
check(w['b'] == {str(z): bs[z] for z in labels}, 'witness ratios')
wg = {str(a): [list(e) for e in it.combinations(w['W'], 2)
               if bs[a]*bs[e[0]]*bs[e[1]] % 97 == w['rho']] for a in w['K0']}
check(wg == w['good_edges'], 'witness good edges')
check([len(wg[str(a)]) for a in w['K0']] == w['good_counts']
      and sum(w['good_counts']) == 8, 'witness counts')
check(len(critical) == 20 and len(threshold_audits) == 72, 'expected thresholds')
check(threshold_tests == 20*96*70 and rho_tests == 45045*96, 'exhaustive test totals')

summary = {'cases_checked': len(case_audits), 'rho_cases_checked': rho_tests,
           'relaxed_actual_maximum': max(histogram), 'required_good_edges': 8,
           'critical_six_sets': len(critical), 'four_set_ratio_tests': threshold_tests,
           'threshold_choices': len(threshold_audits),
           'complete_matching_extensions': expected_second['total_extensions_checked'],
           'edge_disjoint_survivors': expected_second['disjoint_extensions'],
           'required_survivors_for_equality': 1, 'failure_count': len(failures)}
result = {'scope': 'Independent exhaustive certificate audit for conditional L040; no arbitrary-pencil extraction',
          'source_sha256': {name: hashlib.sha256(data).hexdigest() for name, data in zip(FILES, raw)},
          'summary': summary, 'H': H, 'histogram': expected_first['histogram'],
          'case_audits': case_audits, 'critical_six_sets': critical,
          'threshold_audits': threshold_audits, 'complete_forced_table': table, 'failures': failures}
path = HERE / 'independent-audit-result.json'
path.write_text(json.dumps(result, separators=(',', ':')) + '\n')
print(json.dumps(summary, sort_keys=True))
print('certificate:', path.relative_to(Path.cwd()))
if failures:
    print('failure details: /failures in certificate')
    raise SystemExit(1)
