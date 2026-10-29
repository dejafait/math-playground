"""Complete fixed-family incidence certificate; integer counts, no solver."""
from itertools import combinations
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).with_name('forty-support-compatibility.json')
S = [1, 8, 12, 18, 22, 27, 33]
J = [47, 50, 64, 70, 75, 79, 85, 89, 96]
FIXED = [35, 522, 477, 566]
B = [145,147,148,149,160,161,171,174,
     325,327,328,329,340,341,351,354,
     577,581,582,583,595,596,609,610,
     649,653,654,655,667,668,681,682,
     723,724,726,727,748,749,751,752]


def main():
    universe = [(list(i), list(k)) for i in combinations(S, 2)
                for k in combinations(J, 2)]
    records = []
    for label in FIXED + B:
        i, k = universe[label]
        records.append(dict(label=label, I=i, K=k, support=sorted(i+k)))
    supports = {r['label']: set(r['support']) for r in records}
    intersections = [dict(labels=[a,b], intersection=sorted(supports[a] & supports[b]))
                     for a,b in combinations(FIXED+B, 2)]
    fixed_degrees = {str(x): sum(x in supports[a] for a in FIXED) for x in S+J}
    candidate_degrees = {str(x): sum(x in supports[a] for a in B) for x in S+J}
    common = sorted(set.intersection(*(supports[a] for a in B)))
    failures = []
    if len(B) != 40 or len(set(B)) != 40:
        failures.append('candidate universe not forty distinct labels')
    if any(len(supports[a] & supports[b]) > 1 for a,b in combinations(FIXED,2)):
        failures.append('fixed rows not pairwise linear')
    if any(len(supports[a] & supports[b]) > 1 for a in B for b in FIXED):
        failures.append('candidate not eligible against all fixed rows')
    if common != [27] or fixed_degrees['27'] != 1:
        failures.append('claimed common-coordinate obstruction fails')
    obstruction = dict(coordinate=27, fixed_degree=fixed_degrees['27'],
                       candidate_count=40, requested_additions=8,
                       degree_for_requested_additions=fixed_degrees['27']+8,
                       required_degree_at_most=4,
                       additions_at_most=4-fixed_degrees['27'],
                       total_rows_at_most=4+4-fixed_degrees['27'])
    sources = ['lemmas/L162-explicit-four-row-infinite-family.md',
               'lemmas/L163-l162-complete-additional-row-parameter-loci.md']
    certificate = dict(S=S, J=J, fixed_labels=FIXED, candidate_labels=B,
                       source_sha256={p: hashlib.sha256((ROOT/p).read_bytes()).hexdigest()
                                      for p in sources},
                       original_label_count=len(universe), records=records,
                       pair_intersections=intersections, fixed_degrees=fixed_degrees,
                       candidate_universe_degrees=candidate_degrees,
                       common_candidate_coordinates=common, obstruction=obstruction,
                       feasible=False if not failures else None, failures=failures)
    OUT.write_text(json.dumps(certificate, indent=2)+'\n')
    print(f'Universe: {len(B)} candidates, {len(FIXED)} fixed; original labels: {len(universe)}')
    print(f'Complete pair intersections retained: {len(intersections)}')
    print('Coordinate 27: fixed degree 1; any eight additions give 9; required <=4')
    print('Additions <=3; total rows <=7 (upper bound only, no attainment claim)')
    print(f'Failures: {failures}; certificate: {OUT.relative_to(ROOT)}')
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
