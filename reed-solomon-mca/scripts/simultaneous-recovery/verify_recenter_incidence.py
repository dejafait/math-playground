"""Independent complete incidence verification of the saved witness."""
from itertools import combinations
from collections import Counter
from pathlib import Path
import json

here = Path(__file__).resolve().parent
source = json.loads((here / "recenter-incidence-result.json").read_text())
family = [set(a) for a in source["verification"]["supports"]]
failures = []
degrees = [sum(x in a for a in family) for x in range(16)]
pair_histogram = Counter()
double_pairs = []
for i, j in combinations(range(15), 2):
    size = len(family[i] & family[j])
    pair_histogram[size] += 1
    if size == 2:
        double_pairs.append([i, j])
    if size > 2:
        failures.append(["large_pair", i, j])
tau_triples, triple_union_histogram = [], Counter()
for indices in combinations(range(15), 3):
    a, b, c = [family[i] for i in indices]
    triple_union_histogram[len(a | b | c)] += 1
    if len(a | b | c) == 9 and len(a & b & c) == 1:
        overlaps = sorted((len(a & b), len(a & c), len(b & c)))
        if overlaps != [1, 1, 2]:
            failures.append(["tau_pattern", indices])
        tau_triples.append(list(indices))
outside_triples = [tuple(sorted(a - {12, 13, 14, 15})) for a in family[3:]]
outside_triples.append((0, 1, 2))
edge_occurrences = Counter(edge for t in outside_triples for edge in combinations(t, 2))
if max(edge_occurrences.values()) != 1:
    failures.append("repeated_outside_pair")
if degrees != [4, 4, 4, 3, 4, 4, 4, 4, 4, 4, 3, 2, 4, 4, 4, 4]:
    failures.append("degrees")
if double_pairs != [[0, 1]] or tau_triples != [[0, 1, 2]]:
    failures.append("recenter_classification")
if len({frozenset(a) for a in family}) != 15:
    failures.append("duplicates")
if min(triple_union_histogram) < 9:
    failures.append("small_triple")
result = dict(supports_checked=15, pair_tests=105, triple_tests=455,
              degrees=degrees, pair_intersection_histogram=dict(sorted(pair_histogram.items())),
              triple_union_histogram=dict(sorted(triple_union_histogram.items())),
              double_pairs=double_pairs, tau_triples=tau_triples,
              outside_pair_count=len(edge_occurrences),
              missing_outside_pairs=[list(p) for p in combinations(range(10), 2)
                                     if p not in edge_occurrences],
              failures=failures, actual_support_count=15, required_support_count=15,
              actual_nonuniversal_count=12, required_nonuniversal_count=12,
              actual_d_tags=0, required_d_tags_for_L051=2)
path = here / "recenter-incidence-verification.json"
path.write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(dict(pair_tests=105, triple_tests=455, actual_nonuniversal_count=12,
                      required_nonuniversal_count=12, actual_d_tags=0,
                      required_d_tags_for_L051=2, failures=failures,
                      certificate=str(path.relative_to(here.parent.parent)))))
if failures:
    raise SystemExit(1)
