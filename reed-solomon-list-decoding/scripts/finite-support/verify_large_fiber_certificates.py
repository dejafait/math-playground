"""Verify every saved propagation step and complete graph/color certificate.

This reads the binary traces directly and checks forced additions by the
incidence formula, without running the production closure queue. Full
traces use the proved 411-line stopping certificate; proper traces are
also checked for complete closure. No sampling is used.
"""
import csv
import hashlib
import json
import struct
from collections import Counter
from fractions import Fraction
from pathlib import Path

Q = 137
N = Q*Q
T = [16, 64, 70, 102, 112, 118, 121]
ROOT = Path("scripts/finite-support")


def lines_of(p):
    u, v = p % Q, p // Q
    return [(j, (u+t*v) % Q) for j, t in enumerate(T)]


def check_trace(trace, seeds, full):
    assert all(0 <= p < N for p in trace)
    seeds = list(dict.fromkeys(seeds))
    assert trace[:len(seeds)] == seeds
    active, seen = set(), set()
    for i, p in enumerate(trace):
        assert p not in seen
        lines = lines_of(p)
        if i >= len(seeds):
            assert sum(l in active for l in lines) >= 3, (p, "unforced")
        seen.add(p)
        active.update(lines)
    if full:
        assert len(active) >= 411
    else:
        incidence = Counter()
        for j, y in active:
            for v in range(Q):
                incidence[((y-T[j]*v) % Q)+Q*v] += 1
        assert {p for p, count in incidence.items() if count >= 3} == seen
    return len(active)


def read16(f, count):
    data = f.read(2*count)
    assert len(data) == 2*count, "short certificate"
    return list(struct.unpack("<" + "H"*count, data))


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify_pair():
    path = ROOT / "large-fiber-pair-traces.u16"
    with (ROOT / "large-fiber-pair-results.tsv").open() as g:
        rows = list(csv.DictReader(g, delimiter="\t"))
    assert len(rows) == N
    counts = Counter()
    max_proper = 0
    with path.open("rb") as f:
        for c in range(N):
            seed, full, length = read16(f, 3)
            assert seed == c and full in (0, 1)
            trace = read16(f, length)
            active_count = check_trace(trace, [0, 258, c], full)
            row = rows[c]
            assert [int(row[k]) for k in ("seed_C", "forces_full", "trace_points")] == [c, full, length]
            if full:
                assert int(row["active_lines"]) == 411 <= active_count
            else:
                assert int(row["active_lines"]) == active_count
                max_proper = max(max_proper, length)
            counts[full] += 1
        assert not f.read(1), "trailing certificate data"
    summary = json.loads((ROOT / "large-fiber-pair-summary.json").read_text())
    assert summary["exceptional_seeds"] == counts[0]
    assert summary["full_seeds"] == counts[1]
    assert summary["max_proper_closure"] == max_proper
    assert summary["pair_bound_pass"] == (counts[0] <= 272)
    return dict(records=N, full=counts[1], exceptional=counts[0],
                max_proper_closure=max_proper, threshold_pass=counts[0] <= 272,
                trace_sha256=digest(path))


def verify_collinear():
    path = ROOT / "large-fiber-collinear-traces.u16"
    with (ROOT / "large-fiber-collinear-results.tsv").open() as g:
        rows = list(csv.DictReader(g, delimiter="\t"))
    assert len(rows) == len(T)*Q
    bad = [set() for _ in T]
    full_counts = []
    with path.open("rb") as f:
        for j, t in enumerate(T):
            count = 0
            for r in range(Q):
                jj, rr, full, length = read16(f, 4)
                assert (jj, rr) == (j, r) and full in (0, 1)
                trace = read16(f, length)
                active_count = check_trace(trace, [0, Q+Q-t, (-t*r) % Q+Q*r], full)
                row = rows[j*Q+r]
                assert [int(row[k]) for k in ("direction_index", "parameter", "forces_full", "trace_points")] == [j, r, full, length]
                if full:
                    assert int(row["active_lines"]) == 411 <= active_count
                    count += 1
                else:
                    assert int(row["active_lines"]) == active_count
                    bad[j].add(r)
            full_counts.append(count)
        assert not f.read(1), "trailing certificate data"
    return bad, dict(records=len(T)*Q, full_by_direction=full_counts,
                     exceptional_by_direction=[len(b) for b in bad],
                     trace_sha256=digest(path))


def verify_graphs(bad):
    path = ROOT / "large-fiber-collinear-graphs.json"
    cert = json.loads(path.read_text())
    assert cert["q"] == Q and len(cert["graphs"]) == len(T)
    line_bounds, edge_counts, color_counts = [], [], []
    for j, graph in enumerate(cert["graphs"]):
        assert graph["direction"] == T[j]
        assert graph["exceptional_parameters"] == sorted(bad[j])
        vertices = sorted(bad[j] - {0, 1})
        assert graph["vertices"] == vertices
        # Independent edge generation: check the two affine normalizations
        # by multiplying instead of using modular inversion from production.
        edges = []
        for i, r in enumerate(vertices):
            for s in vertices[i+1:]:
                first = any(r*z % Q == s for z in bad[j])
                second = any((1+(r-1)*z) % Q == s for z in bad[j])
                if first and second:
                    edges.append([r, s])
        assert graph["edges"] == edges
        classes = graph["color_classes"]
        assert sorted(r for group in classes for r in group) == vertices
        colors = {r: c for c, group in enumerate(classes) for r in group}
        assert all(colors[r] != colors[s] for r, s in edges)
        assert graph["colors"] == len(classes)
        assert graph["line_occupancy_bound"] == 2+len(classes)
        line_bounds.append(2+len(classes))
        edge_counts.append(len(edges))
        color_counts.append(len(classes))
    assert cert["max_line_bound"] == max(line_bounds)
    assert cert["line_bound_pass"] == (max(line_bounds) <= 8)
    all_bounds = []
    for j, record in enumerate(cert["incidence_bounds"]):
        reciprocal_sum = sum((Fraction(1, r) for i, r in enumerate(line_bounds) if i != j), Fraction())
        bound = Fraction(Q+5*line_bounds[j], 1) / reciprocal_sum
        assert record == dict(direction=T[j], reciprocal_sum=[reciprocal_sum.numerator, reciprocal_sum.denominator],
                              bound=[bound.numerator, bound.denominator],
                              integer_bound=bound.numerator//bound.denominator)
        all_bounds.append(bound)
    best_index = min(range(len(T)), key=lambda j: all_bounds[j])
    assert cert["best_incidence_bound"] == cert["incidence_bounds"][best_index]
    assert cert["asymmetric_bound_pass"] == (all_bounds[best_index] < 273)
    return dict(edge_counts=edge_counts, color_counts=color_counts, line_bounds=line_bounds,
                best_incidence_bound=cert["best_incidence_bound"],
                required_integer_bound=272, threshold_pass=all_bounds[best_index] < 273,
                graph_sha256=digest(path))


def main():
    pair = verify_pair()
    print(f"All {pair['records']} fixed-pair records verified; "
          f"exceptional bound {pair['exceptional']} versus 272 fails as recorded.", flush=True)
    bad, collinear = verify_collinear()
    print(f"All {collinear['records']} collinear traces verified, including every proper closure.", flush=True)
    graphs = verify_graphs(bad)
    result = dict(all_checks_pass=True, failures=[], pair_diagnostic=pair,
                  collinear=collinear, graphs=graphs,
                  qualifications=["No full-sheet coefficient counterassignment constructed.",
                                  "Fixed-pair and uniform-eight diagnostic thresholds fail.",
                                  "Asymmetric incidence certificate proves only the conditional large-fiber implication.",
                                  "Separate critical mathematical audit remains pending."])
    path = ROOT / "large-fiber-certificate-verification.json"
    path.write_text(json.dumps(result, indent=2) + "\n")
    bound = graphs["best_incidence_bound"]
    print(f"Complete graphs and colorings verified; cap {bound['bound'][0]}/{bound['bound'][1]} "
          f"gives {bound['integer_bound']} <=272. Failures: [].")
    print(f"Full verification record: {path}")


if __name__ == "__main__":
    main()
