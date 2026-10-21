"""Bounded search for two disjoint, simultaneously recovered d-tag triples.

Exact F_97 arithmetic. Stops at the first gated pair; does not count twelve
candidates or certify all labelings. Full selected witness is saved to disk.
"""
from itertools import combinations
from collections import Counter
from pathlib import Path
import json

P = 97
H = tuple(x for x in range(1, P) if pow(x, 16, P) == 1)
INV = {x: pow(x, -1, P) for x in range(1, P)}
V = {x: tuple(pow(x, j, P) for j in range(1, 9)) for x in H}
OUT = Path(__file__).with_name("disjoint-d-pair-result.json")


def ev(roots, x):
    value = 1
    for a in roots:
        value = value * (x - a) % P
    return value


def moments(word):
    return [sum(word.get(x, 0) * V[x][j] for x in H) % P for j in range(8)]


def recover(support, target):
    # First four moments only; independently check the other four afterward.
    a = [[V[x][i] for x in support] + [target[i]] for i in range(4)]
    for j in range(4):
        k = next(k for k in range(j, 4) if a[k][j])
        a[j], a[k] = a[k], a[j]
        scale = INV[a[j][j]]
        a[j] = [z * scale % P for z in a[j]]
        for i in range(4):
            if i != j:
                scale = a[i][j]
                a[i] = [(z - scale * w) % P for z, w in zip(a[i], a[j])]
    omega = [a[i][4] for i in range(4)]
    actual = moments(dict(zip(support, omega)))
    return omega, actual, actual == target


def verify(h, d, ys, zs, w, s, ss, mu, nu, p, q):
    b = {h, d, *ys, *zs}
    c = {x: ev([a for a in H if a not in b | set(w)], x) for x in b | set(w)}
    rho = next(rho for rho in range(2, P)
               if all((rho - (1-rho)*m) % P for m in (mu, nu)))
    for r in range(2, P):
        records = []
        for m, outside in ((mu, s), (nu, ss)):
            n = {x: -m * c[x] % P for x in ys}
            n.update({x: c[x] for x in zs})
            n[h] = c[h] * (q - m*p) % P
            n[d] = c[d] * (1 - (1+m)*r) % P
            support = tuple(sorted((d, *outside)))
            target = moments(n)
            omega, actual, ok = recover(support, target)
            assert ok, ("failed full moments", support, m)
            e = (rho - (1-rho)*m) % P
            t = rho * INV[e] % P
            error = {x: a*INV[e] % P for x, a in zip(support, omega)}
            records.append({"mu": m, "S": outside, "K": support, "E": e,
                            "T": t, "N_moments": target, "omega": omega,
                            "recovered_moments": actual, "all_eight_moments": ok,
                            "full_weight": all(omega), "actual_error": error})
        if all(row["full_weight"] for row in records):
            break
    else:
        raise AssertionError("no full-weight r for selected pair")
    assert p*q*(1-p-q)*r*(1-r) % P
    e0 = {h: c[h]*p*INV[(1-rho) % P] % P,
          d: c[d]*r*INV[(1-rho) % P] % P}
    e0.update({x: c[x]*INV[(1-rho) % P] % P for x in ys})
    e1 = {h: c[h]*q*INV[rho] % P, d: c[d]*(1-r)*INV[rho] % P}
    e1.update({x: c[x]*INV[rho] % P for x in zs})
    e2 = {h: -c[h]*(1-p-q) % P}
    e2.update({x: -c[x] % P for x in w})
    m0, m1, m2 = moments(e0), moments(e1), moments(e2)
    slope = [(a-b) % P for a, b in zip(m1, m0)]
    pencil = lambda t: [(a+t*b) % P for a, b in zip(m0, slope)]
    assert pencil(rho) == m2
    for row in records:
        assert row["T"] not in (0, 1, rho)
        assert moments(row["actual_error"]) == pencil(row["T"])
    assert records[0]["T"] != records[1]["T"]
    assert all(all(word.values()) for word in (e0, e1, e2))
    return {"h": h, "d": d, "Y": ys, "Z": zs, "W": w,
            "p_q_r": [p, q, r], "gamma": [0, 1, rho], "lambda": 1,
            "c": c, "original_errors": [e0, e1, e2],
            "syndrome_intercept": m0, "syndrome_slope": slope,
            "candidate_records": records, "triple_gates": True,
            "original_triple_moments": True, "candidate_pencil_moments": True,
            "disjoint_outside_triples": not set(s) & set(ss)}


def main():
    h = 1
    stats = {"y_z_pair_choices": 0, "split_cubics_grouped": 0,
             "disjoint_pairs_tested": 0, "groups_at_least_three": 0}
    complete_groups = []
    histogram = Counter()
    for ys in combinations([x for x in H if x != h], 2):
        for zs in combinations([x for x in H if x not in (h, *ys)], 2):
            stats["y_z_pair_choices"] += 1
            outside = [x for x in H if x not in (h, *ys, *zs)]
            groups = {}
            for s in combinations(outside, 3):
                values = tuple(ev(s, x) for x in (*ys, *zs, h))
                key = (values[0]*INV[values[1]] % P,
                       values[2]*INV[values[3]] % P)
                groups.setdefault(key, []).append((s, values))
                stats["split_cubics_grouped"] += 1
            complete_groups.append({"Y": ys, "Z": zs,
                                    "groups": [[key, [s for s, _ in group]]
                                               for key, group in sorted(groups.items())]})
            histogram.update(len(group) for group in groups.values())
            for group in groups.values():
                if len(group) < 3:
                    continue
                stats["groups_at_least_three"] += 1
                for w, wv in group:
                    rows = []
                    for s, sv in group:
                        u = sv[2]*INV[wv[2]] % P
                        mu = -u*wv[0]*INV[sv[0]] % P
                        ah = u*wv[4]*INV[sv[4]] % P
                        if mu not in (0, P-1):
                            rows.append((s, mu, ah, u))
                    for first, second in combinations(rows, 2):
                        s, mu, ah, u = first
                        ss, nu, bh, uu = second
                        if mu == nu or set(s) & set(ss):
                            continue
                        stats["disjoint_pairs_tested"] += 1
                        p = (ah-bh)*INV[(nu-mu) % P] % P
                        q = (ah+mu*p) % P
                        if p*q*(1-p-q) % P == 0:
                            continue
                        used = {h, *ys, *zs, *w, *s, *ss}
                        d = next((x for x in H if x not in used), None)
                        if d is None:
                            continue
                        witness = verify(h, d, ys, zs, w, s, ss, mu, nu, p, q)
                        witness["cubic_scales"] = [u, uu]
                        result = {"scope": "bounded search stopped at first positive pair; not a twelve-candidate test",
                                  "prime": P, "H": H, "statistics": stats,
                                  "witness": witness,
                                  "summary": {"pair_found": True, "verified_candidate_count": 2,
                                              "refutation_threshold": 12, "uniform_bound_sought": 11,
                                              "all_labelings_checked": False,
                                              "all_eight_moments_verified": True,
                                              "full_weights_verified": True,
                                              "proves_eleven": False, "refutes_eleven": False,
                                              "failures": []}}
                        OUT.write_text(json.dumps(result, indent=2) + "\n")
                        print(json.dumps(result["summary"], sort_keys=True))
                        print(f"actual verified count 2; required refutation count 12; certificate {OUT}")
                        return
    result = {"scope": {"prime": P, "H": H, "h": h,
                         "d_ignored_overapproximation": True,
                         "cubics_per_pair_choice": 165,
                         "required_distinct_cubics": 3},
              "statistics": stats, "group_size_histogram": dict(sorted(histogram.items())),
              "complete_groups": complete_groups,
              "summary": {"pair_found": False,
                          "all_normalized_pair_choices_checked": True,
                          "actual_disjoint_eligible_pairs": stats["disjoint_pairs_tested"],
                          "required_for_pair": 1, "proves_eleven": False,
                          "independent_check_pending": True, "failures": []}}
    OUT.write_text(json.dumps(result, separators=(",", ":")) + "\n")
    print(json.dumps(result["summary"], sort_keys=True))
    print(f"certificate {OUT}")


if __name__ == "__main__":
    main()
