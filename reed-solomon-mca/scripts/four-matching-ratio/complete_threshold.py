"""Complete perfect-matching extension check of the paired-ratio threshold."""
import itertools
import json
from collections import Counter
from pathlib import Path

HERE = Path(__file__).parent
source = json.loads((HERE/'paired-ratio-result.json').read_text())
H = source['H']
assert source['field'] == 97 and source['actual_maximum'] == 8
assert len(source['cases']) == 45045
expected = {(q, W) for q in H if q != 1
            for W in itertools.combinations([z for z in H if z not in (1, q)], 6)}
assert {(r['q'], tuple(r['W'])) for r in source['cases']} == expected
assert len(expected) == len(source['cases'])
threshold_cases = [r for r in source['cases'] if r['maximum'] == 8]
rows = []
failures = []

def matchings(labels):
    if not labels:
        yield ()
        return
    first = labels[0]
    for second in labels[1:]:
        rest = tuple(z for z in labels if z not in (first, second))
        for m in matchings(rest):
            yield tuple(sorted(((min(first, second), max(first, second)),)+m))

for case in threshold_cases:
    q, W = case['q'], tuple(case['W'])
    labels = [z for z in H if z not in (1, q)]
    candidates = [z for z in labels if z not in W]
    b = {z: (1-z)*pow((q-z) % 97, -1, 97) % 97 for z in labels}
    all_matchings = list(matchings(W))
    assert len(all_matchings) == 15
    for rho in range(1, 97):
        good = {a: tuple(e for e in itertools.combinations(W, 2)
                        if b[a]*b[e[0]]*b[e[1]] % 97 == rho) for a in candidates}
        for K0 in itertools.combinations(candidates, 4):
            counts = [len(good[a]) for a in K0]
            if sum(counts) < 8:
                continue
            assert sum(counts) == 8
            row = {'p': 1, 'q': q, 'W': list(W), 'K0': list(K0), 'rho': rho,
                   'good_edges': {str(a): list(good[a]) for a in K0},
                   'counts': counts}
            if 0 in counts:
                row.update(reason='a color has three exceptions, but two tags permit at most two',
                           extension_count=0, disjoint_extension_count=0, extension_conflicts=[])
            else:
                options = {a: [m for m in all_matchings if set(good[a]).issubset(m)] for a in K0}
                conflicts = []
                positives = []
                for ms in itertools.product(*(options[a] for a in K0)):
                    edge_counts = Counter(itertools.chain.from_iterable(ms))
                    repeated = sorted(e for e, count in edge_counts.items() if count > 1)
                    if not repeated:
                        positives.append([list(m) for m in ms])
                    conflicts.append({'matchings': [list(m) for m in ms], 'repeated_edges': repeated})
                row.update(reason='all perfect-matching extensions repeat an edge' if not positives else 'SURVIVES',
                           extension_count=len(conflicts), disjoint_extension_count=len(positives),
                           extension_conflicts=conflicts)
                if positives:
                    failures.append({'case': row, 'surviving_extensions': positives})
            rows.append(row)
result = {'scope': 'Complete threshold test of a necessary condition, over all normalized H labels',
          'threshold_six_sets': len(threshold_cases), 'threshold_candidates': len(rows),
          'count_profiles': dict(Counter(','.join(map(str, sorted(r['counts']))) for r in rows)),
          'total_extensions_checked': sum(r['extension_count'] for r in rows),
          'disjoint_extensions': sum(r['disjoint_extension_count'] for r in rows),
          'required_good_edges': 8, 'relaxed_maximum': 8, 'failures': failures,
          'rows': rows}
table = []
for row in rows:
    assert row['counts'] == [2, 2, 2, 2] and row['extension_count'] == 1
    W = row['W']
    code = lambda e: ''.join(str(W.index(z)) for z in e)
    good_codes = ['.'.join(code(e) for e in row['good_edges'][str(a)]) for a in row['K0']]
    forced = row['extension_conflicts'][0]['matchings']
    remainder = [next(e for e in m if tuple(e) not in map(tuple, row['good_edges'][str(a)]))
                 for a, m in zip(row['K0'], forced)]
    repeated = row['extension_conflicts'][0]['repeated_edges']
    table.append(f"{row['q']} | {','.join(map(str,W))} | {','.join(map(str,row['K0']))} | {row['rho']} | "
                 + '/'.join(good_codes) + ' | ' + '/'.join(code(e) for e in remainder)
                 + ' | ' + '.'.join(code(e) for e in repeated))
result['complete_forced_table_columns'] = 'q | W sorted | K0 sorted | rho | good edge codes by K0 row | forced remaining edges | repeated edges; edge code ij means W[i],W[j], zero-based'
result['complete_forced_table'] = table
result['critical_six_sets'] = threshold_cases
path = HERE/'threshold-completion-result.json'
path.write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps({k: v for k, v in result.items() if k not in ('rows', 'failures', 'complete_forced_table', 'critical_six_sets')}))
print('failures:', len(failures))
print(path.relative_to(Path.cwd()))
