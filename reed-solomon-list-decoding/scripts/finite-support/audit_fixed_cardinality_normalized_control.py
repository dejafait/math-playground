"""Critical audit of L098's complete frozen-control certificates.

No constructor imports, optimization, or changed witness. Source endpoint
matrices/congruences are separately replayed by their independent auditors.
Here every stored mixed entry, singleton endpoint, pair/scalar endpoint,
factored coefficient record and original verification residual is checked.
"""
import hashlib
import json
import sys
from collections import Counter
from fractions import Fraction as Q
from functools import lru_cache
from math import comb
from pathlib import Path

sys.set_int_max_str_digits(0)
BASE = Path(__file__).parent
OUT = BASE / "fixed-cardinality-critical-audit.json"


def enc(x):
    x = Q(x)
    return [x.numerator, x.denominator]


@lru_cache(None)
def c(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def main():
    names = [
        "fixed-cardinality-normalized-control-results.json",
        "fixed-cardinality-normalized-control-verification.json",
        "fixed-cardinality-critical-contraction-replay.json",
        "fixed-cardinality-critical-batch-source.json",
        "fixed-cardinality-critical-zero-source.json",
        "free-pair-shell-batch-results.json", "full-zero-block-results.json",
        "delsarte-lp-results.json", "full-scalar-results.json",
    ]
    data = {name: json.loads((BASE / name).read_text()) for name in names}
    z, verification, replay, batch_audit, full_audit, batch, full, lp, scalar = (
        data[name] for name in names
    )
    failures, counts = [], Counter()

    def check(ok, kind, context=None):
        counts[kind] += 1
        if not ok:
            failures.append({"kind": kind, "context": context})

    for name, digest in z["input_sha256"].items():
        check(hashlib.sha256((BASE / name).read_bytes()).hexdigest() == digest,
              "frozen_input_hash", name)
    g = [c(68, i) * c(956, i) for i in range(69)]
    H = c(1024, 68)
    p = [Q(1)] + [Q(0)] * 4 + [
        Q(r["numerator"], r["denominator"]) / (2 * g[i])
        for i, r in zip(range(5, 69), lp["exact"]["primal"])
    ]
    N = 65537**28 // 2**128 + 1
    T = Q(65537**28, 2**128)
    M = (Q(c(1024, 64), c(68, 64)) + 1) / 2
    alpha = Q(N - 1, M - 1)
    cp = [alpha * a + (1 - alpha) * (i == 0) for i, a in enumerate(p)]
    check(1 < N < M < H and 0 < alpha < 1, "normalization")
    for name, actual, expected in [
        ("N", z["N"], N), ("T", Q(*z["T"]), T),
        ("M", Q(*z["M"]), M), ("alpha", Q(*z["alpha"]), alpha),
        ("p", list(map(lambda a: Q(*a), z["p"])), p),
        ("control_p", list(map(lambda a: Q(*a), z["control_p"])), cp),
        ("objective", Q(*z["objective"]), N),
    ]:
        check(actual == expected, "frozen_definition", name)
    check(sum(g[i] * p[i] for i in range(69)) == M, "endpoint_objective")
    check(sum(g[i] * cp[i] for i in range(69)) == N, "control_objective")
    check(all(p[i] > 0 and cp[i] > 0 for i in range(5, 69)),
          "strict_pair_positivity")
    for endpoint in (batch, full, scalar):
        check(endpoint["p"] == list(map(enc, p)), "same_endpoint_pairs")

    # Compare every coefficient and sign, not the constructor's summary.
    check(len(z["pair_rows"]) == 68, "pair_coverage")
    for label, r in enumerate(z["pair_rows"], 1):
        coeff = [
            sum((-1)**h * c(label, h) * c(68-label, i-h)
                * c(956-label, i-h) for h in range(i+1))
            for i in range(5, 69)
        ]
        old = 1 + sum(b * p[i] for i, b in zip(range(5, 69), coeff))
        new = 1 + sum(b * cp[i] for i, b in zip(range(5, 69), coeff))
        check(r == {"label": label, "coefficients": coeff,
                    "z_slack": enc(old), "control_slack": enc(new)},
              "complete_pair_record", label)
        check(old >= 0 and new == alpha * old + 1-alpha and new >= 0,
              "pair_convexity", label)
        if label <= 64:
            check(old == Q(1, 2), "defining_pair_equation", label)

    expected = [(k, l, [0, 5, 6, 7, 8, 68] if k == l == 0
                 else list(range(max(5, k, l), 9)))
                for k in range(9) for l in range(9)]
    expected.extend([(33, 33, [33, 34, 35]), (34, 34, [34])])
    check([(b["k"], b["l"], b["indices"]) for b in batch["blocks"]] == expected,
          "complete_retained_support")
    blocks = [(k, l, inds, b["families"])
              for (k, l, inds), b in zip(expected, batch["blocks"])]
    blocks.append((0, 0, list(range(69)), full["families"]))
    psd_records = []
    check(len(z["PSD_convex_certificates"]) == 168, "control_matrix_coverage")
    ix = 0
    for k, l, inds, families in blocks:
        for family, endpoint in enumerate(families):
            r = z["PSD_convex_certificates"][ix]
            check((r["k"], r["l"], r["indices"], r["family"]) ==
                  (k, l, inds, family), "control_matrix_identity", ix)
            # In the source beta sum t=i forces u=i: all other terms
            # contain binom(u,i)=0 or binom(n-k-u,i-u)=0.
            diag = [Q(int(k == l == i == 0)) if family == 0 else
                    Q(c(68-2*k, i-k) * c(956-2*l, i-l)
                      - int(k == l == i == 0)) for i in inds]
            check(r["singleton_diagonal"] == list(map(enc, diag)) and
                  all(x >= 0 for x in diag), "singleton_diagonal", ix)
            a = [[Q(*x) for x in row] for row in endpoint["matrix"]]
            mixed = [[Q(*x) for x in row] for row in r["control_matrix"]]
            check(len(mixed) == len(inds) and all(len(row) == len(inds)
                  for row in mixed), "control_dimensions", ix)
            for row in range(len(inds)):
                for col in range(len(inds)):
                    check(mixed[row][col] == alpha*a[row][col] +
                          (1-alpha)*(diag[row] if row == col else 0),
                          "every_convex_matrix_entry", [ix, row, col])
            # The endpoint auditor multiplies every congruence entry.
            audited = (batch_audit["PSD_certificates"][ix] if ix < 166
                       else full_audit["families"][family])
            d = [Q(*x) for x in endpoint["certificate"]["diagonal"]]
            check(audited["diagonal"] == list(map(enc, d)) and
                  all(x >= 0 for x in d), "all_endpoint_pivots", ix)
            check(audited["positive_pivots"] == sum(x > 0 for x in d)
                  and audited["zero_pivots"] == sum(x == 0 for x in d),
                  "singular_pivot_counts", ix)
            psd_records.append({"index": ix, "k": k, "l": l, "family": family,
                                "indices": inds, "singleton_diagonal": list(map(enc, diag)),
                                "endpoint_diagonal": list(map(enc, d)),
                                "checked_entries": len(inds)**2})
            ix += 1

    yd, cd = z["scalar_denominator_z"], z["scalar_denominator_control"]
    check(yd > 0 and cd > 0, "positive_scalar_denominators")
    orbit_total = repeat_total = forbidden_total = 0
    for r in z["scalar_values"]:
        i, j, h = r["distances"]
        forbidden = any(0 < b < 5 for b in (i, j, h))
        repeated = min(i, j, h) == 0
        value = (Q(0) if forbidden else p[sorted((i, j, h))[1]]
                 if repeated else p[i]*p[j]*p[h]/p[68])
        e = int(i == j == h == 0)
        control = alpha*value + (1-alpha)*e
        old = [value, p[i]-value, 1+value-p[i]-p[j]]
        single = [e, int(i == 0)-e, 1+e-int(i == 0)-int(j == 0)]
        new = [control, cp[i]-control, 1+control-cp[i]-cp[j]]
        check(Q(r["z_numerator"], yd) == value and r["singleton_value"] == e,
              "scalar_endpoint_values", [i, j, h])
        check(all(a >= 0 for a in old+single+new) and
              all(b == alpha*a+(1-alpha)*s for a, s, b in zip(old, single, new))
              and new == [Q(a, cd) for a in r["control_slack_numerators"]],
              "every_scalar_endpoint_convexity", [i, j, h])
        orbit_total += r["orbits"]
        repeat_total += repeated*r["orbits"]
        forbidden_total += forbidden*r["orbits"]
    check((orbit_total, repeat_total, forbidden_total) == (1500625, 205, 10232),
          "full_scalar_coverage")
    seen = set()
    for r in z["coefficient_entries"]:
        i, j = r["i"], r["j"]
        check((i, j) not in seen, "unique_coefficient_entry", [i, j])
        seen.add((i, j))
        check(r["inside_factors"] == [c(i, t)*c(68-i, j-t) for t in r["t"]]
              and r["outside_factors"] == [c(i, s)*c(956-i, j-s) for s in r["s"]],
              "all_individual_factors", [i, j])
        check(sum(a for h, a in r["h_coefficients"]) == g[j],
              "all_shell_counts", [i, j])
    check(seen == {(i, j) for i in range(69) for j in range(69)},
          "full_ordered_entry_coverage")
    check(len(z["contractions"]) == len(verification["independent_rows"]) ==
          len(replay["independent_rows"]) == 69, "all_residual_rows_present")
    exact_rows, ratios = [], []
    for i, r in enumerate(z["contractions"]):
        lhs, rhs, residual = (Q(*r[name]) for name in ("lhs", "rhs", "residual"))
        check(r["i"] == i and rhs == N*cp[i] and residual == lhs-rhs
              and r["holds"] == (residual == 0), "residual_identity", i)
        check(r["ordered_pair_count"] == H*g[i] and
              r["third_support_count"] == H, "universe_counts", i)
        check(r["repetition_orbits"] == ([] if i == 0 else
              [[0, 0, 0, 1], [i, i, i, 1]]), "both_repetitions", i)
        row = {"i": i, "residual": enc(residual), "source_row_sum_lhs": enc(lhs)}
        check(verification["independent_rows"][i] == row ==
              replay["independent_rows"][i], "both_complete_verification_rows", i)
        ratio = lhs/rhs if rhs else None
        check(r["lhs_over_rhs"] == (enc(ratio) if ratio is not None else None),
              "exact_recorded_ratio", i)
        if i >= 5:
            check(residual > 0 and Q(1383, 1000) < ratio < Q(1384, 1000),
                  "discriminating_strict_bound", i)
            ratios.append(ratio)
        else:
            check(residual == 0, "zero_distance_controls", i)
        exact_rows.append({**row, "rhs": enc(rhs),
                           "lhs_over_rhs": enc(ratio) if ratio is not None else None})
    # These flags are consistency checks after the independent source
    # programs performed full reconstructions, never substitutes for them.
    for name, audit in [(names[1], verification), (names[2], replay),
                        (names[3], batch_audit), (names[4], full_audit)]:
        check(audit["verified"] and not audit["failures"], "source_replay_completed", name)
    check(replay["coefficient_products"] == verification["coefficient_products"] == 1500625
          and replay["complete_source_matrix_entries"] ==
          verification["complete_source_matrix_entries"] == 4761,
          "both_coefficient_reconstruction_counts")
    result = {
        "verified": not failures, "failures": failures, "checks": dict(counts),
        "total_checks": sum(counts.values()), "N": N, "M": enc(M),
        "alpha": enc(alpha), "required_contraction_ratio": [1, 1],
        "actual_min_ratio": enc(min(ratios)), "actual_max_ratio": enc(max(ratios)),
        "strict_ratio_interval": [[1383, 1000], [1384, 1000]],
        "PSD_controls": psd_records, "complete_residuals": exact_rows,
        "input_sha256": {name: hashlib.sha256((BASE/name).read_bytes()).hexdigest()
                         for name in names},
        "scope": "L098 frozen-control audit only; other moments and RS safety unresolved",
    }
    OUT.write_text(json.dumps(result, separators=(",", ":")) + "\n")
    print("Critical checks:", sum(counts.values()), "; failures:", len(failures))
    print("168 convex PSD controls; 64/64 nonzero residuals positive.")
    print("Actual LHS/RHS in (1.383,1.384); required 1; exact endpoints on disk.")
    print("Complete audit:", OUT)
    if failures:
        print("Failure records:", failures[:10])
        raise SystemExit(1)


if __name__ == "__main__":
    main()
