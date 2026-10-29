"""Build and color necessary collinear compatibility graphs.

All edges/vertices/colors are saved; failed color bounds remain explicit.
The companion verifier checks propagation traces and the full coloring.
"""
import csv
import json
from fractions import Fraction
from pathlib import Path

Q = 137
T = [16, 64, 70, 102, 112, 118, 121]
ROOT = Path("scripts/finite-support")


def greedy_dsatur(vertices, adj):
    colors = {}
    while len(colors) < len(vertices):
        v = max((v for v in vertices if v not in colors),
                key=lambda v: (len({colors[w] for w in adj[v] if w in colors}),
                               len(adj[v]), -v))
        used = {colors[w] for w in adj[v] if w in colors}
        c = 0
        while c in used:
            c += 1
        colors[v] = c
    return colors


def main():
    bad = [set() for _ in T]
    with (ROOT / "large-fiber-collinear-results.tsv").open() as f:
        for row in csv.DictReader(f, delimiter="\t"):
            if int(row["forces_full"]) == 0:
                bad[int(row["direction_index"])].add(int(row["parameter"]))
    graphs = []
    for j, t in enumerate(T):
        vertices = sorted(bad[j] - {0, 1})
        adj = {r: set() for r in vertices}
        edges = []
        for i, r in enumerate(vertices):
            for s in vertices[i+1:]:
                # Normalize {0,r,s} and {1,r,s} in the same line parameter.
                z0 = s * pow(r, -1, Q) % Q
                z1 = (s-1) * pow(r-1, -1, Q) % Q
                if z0 in bad[j] and z1 in bad[j]:
                    adj[r].add(s)
                    adj[s].add(r)
                    edges.append([r, s])
        colors = greedy_dsatur(vertices, adj)
        classes = [[r for r in vertices if colors[r] == c]
                   for c in range(1 + max(colors.values(), default=-1))]
        assert all(colors[r] != colors[s] for r, s in edges)
        graphs.append(dict(direction=t, exceptional_parameters=sorted(bad[j]),
                           vertices=vertices, edges=edges, color_classes=classes,
                           colors=len(classes), line_occupancy_bound=2+len(classes)))
        print(f"Direction {t}: {len(vertices)} vertices, {len(edges)} edges, "
              f"{len(classes)} colors; line bound {2+len(classes)} (required <=8).")
    bound = max(g["line_occupancy_bound"] for g in graphs)
    incidence_bounds = []
    for j, graph in enumerate(graphs):
        reciprocal_sum = sum((Fraction(1, g["line_occupancy_bound"])
                              for i, g in enumerate(graphs) if i != j), Fraction())
        fiber_bound = Fraction(Q+5*graph["line_occupancy_bound"], 1) / reciprocal_sum
        incidence_bounds.append(dict(direction=graph["direction"],
                                     reciprocal_sum=[reciprocal_sum.numerator,
                                                     reciprocal_sum.denominator],
                                     bound=[fiber_bound.numerator, fiber_bound.denominator],
                                     integer_bound=fiber_bound.numerator//fiber_bound.denominator))
    best = min(incidence_bounds, key=lambda b: Fraction(*b["bound"]))
    result = dict(q=Q, required_line_bound=8, max_line_bound=bound,
                  line_bound_pass=bound <= 8,
                  proper_fiber_bound_numerator=bound*(Q+5*bound),
                  proper_fiber_bound_denominator=6,
                  required_fiber_bound=272, incidence_bounds=incidence_bounds,
                  best_incidence_bound=best,
                  asymmetric_bound_pass=best["integer_bound"] <= 272, graphs=graphs)
    path = ROOT / "large-fiber-collinear-graphs.json"
    path.write_text(json.dumps(result, indent=2) + "\n")
    print(f"Asymmetric incidence bound {best['bound'][0]}/{best['bound'][1]}, "
          f"integer cap {best['integer_bound']}; required <=272.")
    print(f"Full graph/color certificate: {path}")


if __name__ == "__main__":
    main()
