"""Complete normalized paired-ratio relaxation; no pencil is constructed."""
import itertools
import json
from collections import Counter
from pathlib import Path

P = 97
H = sorted(x for x in range(1, P) if pow(x, 16, P) == 1)
assert len(H) == 16
inv = {x: pow(x, -1, P) for x in range(1, P)}
records = []
histogram = Counter()
maximum = -1
witness = None
for q in H:
    if q == 1:
        continue
    labels = [z for z in H if z not in (1, q)]
    b = {z: (1-z)*inv[(q-z) % P] % P for z in labels}
    assert len(set(b.values())) == 14 and all(b.values())
    for W in itertools.combinations(labels, 6):
        candidates = [z for z in labels if z not in W]
        edge_classes = {}
        for e in itertools.combinations(W, 2):
            edge_classes.setdefault(b[e[0]]*b[e[1]] % P, []).append(e)
        # Each class is a matching, by injectivity of b and nonzero values.
        assert all(len(set(itertools.chain.from_iterable(es))) == 2*len(es)
                   for es in edge_classes.values())
        by_rho = [[0]*8 for _ in range(P)]
        for ai, a in enumerate(candidates):
            for product, edges in edge_classes.items():
                by_rho[b[a]*product % P][ai] = len(edges)
        local_max = max(sum(sorted(counts, reverse=True)[:4]) for counts in by_rho[1:])
        histogram[local_max] += 1
        records.append({'q': q, 'W': list(W), 'maximum': local_max})
        if local_max > maximum:
            maximum = local_max
            rho = next(r for r in range(1, P)
                       if sum(sorted(by_rho[r], reverse=True)[:4]) == local_max)
            order = sorted(range(8), key=lambda i: (-by_rho[rho][i], candidates[i]))[:4]
            K0 = [candidates[i] for i in order]
            witness = {'p': 1, 'q': q, 'W': list(W), 'K0': K0, 'rho': rho,
                       'b': {str(z): b[z] for z in labels},
                       'good_edges': {str(a): [list(e) for e in edge_classes.get(rho*inv[b[a]] % P, [])]
                                      for a in K0},
                       'good_counts': [by_rho[rho][i] for i in order]}
result = {'scope': 'Necessary paired-ratio relaxation, not actual moment-compatible pencils',
          'field': P, 'H': H, 'normalized_pairs': 15, 'six_sets_per_pair': 3003,
          'case_count': len(records), 'rho_values_per_case': 96,
          'candidate_K0_count_per_case': 70, 'actual_maximum': maximum,
          'required_for_equality': 8, 'exclusion_requires_maximum_at_most': 7,
          'histogram': dict(sorted(histogram.items())), 'witness': witness,
          'cases': records, 'failures': []}
assert len(records) == 15*3003
path = Path(__file__).with_name('paired-ratio-result.json')
path.write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps({k: result[k] for k in ('case_count', 'actual_maximum', 'required_for_equality',
      'exclusion_requires_maximum_at_most', 'histogram', 'failures')}))
print(path.relative_to(Path.cwd()))
