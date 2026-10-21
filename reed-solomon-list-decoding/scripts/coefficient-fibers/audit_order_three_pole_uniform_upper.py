"""Independent critical-audit arithmetic for L100; no source-bound reproof."""
from fractions import Fraction
from hashlib import sha256
from itertools import combinations
from math import factorial, gcd, isqrt, prod
from pathlib import Path
import json


def main():
    base = Path(__file__).resolve().parent
    original = base / "order-three-pole-uniform-upper-results.json"
    verified = base / "order-three-pole-uniform-upper-verification.json"
    saved, verification = (json.loads(p.read_text()) for p in (original, verified))
    checks, failures = [], []

    def check(name, condition):
        checks.append({"name": name, "passed": bool(condition)})
        if not condition:
            failures.append(name)

    def rational(x):
        return {"numerator": x.numerator, "denominator": x.denominator}

    q, n, s, B = 65537, 1024, 67, 513
    check("prime field", all(q % d for d in range(2, isqrt(q) + 1)))
    check("primitive generator", pow(3, (q-1)//2, q) == q-1)
    check("subgroup generator", pow(3, 64, q) == 19139)
    check("subgroup order and minus one",
          pow(19139, n, q) == 1 and pow(19139, n//2, q) == q-1)
    check("rounding and subset power range", 4*q < B*B and s < q)

    # An extension index is r+ell*n. All 64 extensions restrict to r;
    # exhaust the full constant character group, without complex arithmetic.
    extension_rows = []
    full_indices = set()
    for r in range(n):
        indices = [r + ell*n for ell in range(64)]
        ok = all((64*a) % (q-1) == 64*r for a in indices)
        check(f"all extensions of constant character {r}", ok)
        full_indices.update(indices)
        extension_rows.append({"restriction_index": r, "extension_indices": indices})
    check("extension exhaustion", full_indices == set(range(q-1)))
    twists = []
    for j in range(1, s+1):
        inverse = pow(j, -1, q)
        check(f"additive power {j} invertible", j*inverse % q == 1)
        for ell in range(64):
            # On h=t^64, the twist exponent ell*n contributes zero.
            check(f"power {j} twist {ell} restricts correctly",
                  (64*ell*n) % (q-1) == 0)
            twists.append({"power": j, "twist_index": ell*n,
                           "additive_multiplier": j, "inverse_multiplier": inverse,
                           "restricted_twist_exponent": 0})
    check("full twist coverage", len(twists) == 67*64)

    # Build unsigned Stirling numbers by inserting the last letter either
    # into an old cycle or into a new singleton cycle. This reconstructs the
    # permutation sum independently of both saved generating recurrences.
    stirling = [1]
    absolute, principal = [], []
    for k in range(s+1):
        if k:
            old = stirling
            stirling = [(k-1)*(old[c] if c < len(old) else 0)
                        + (old[c-1] if c else 0) for c in range(k+1)]
        check(f"permutation mass degree {k}", sum(stirling) == factorial(k))
        absolute.append(Fraction(sum(v*B**c for c, v in enumerate(stirling)),
                                 factorial(k)))
        principal.append(Fraction(sum((-1)**(k-c)*v*n**c
                                      for c, v in enumerate(stirling)), factorial(k)))
        check(f"saved absolute coefficient {k}",
              absolute[-1] == Fraction(saved["absolute_cycle_coefficients"][k]))
        falling = Fraction(prod(range(n-k+1, n+1)), factorial(k))
        check(f"signed principal normalization {k}", principal[-1] == falling)
    check("absolute coefficient coverage", len(saved["absolute_cycle_coefficients"]) == 68)
    C, error = principal[s], absolute[s]
    check("integer subset and error", C.denominator == error.denominator == 1)
    C, error = int(C), int(error)
    check("rising factorial coefficient",
          error*factorial(s) == prod(range(B, B+s)))

    exceptional = {}
    order_counts = {}
    for a in range(1, 11):
        d = 2**a
        order_counts[str(d)] = sum(n//gcd(r,n) == d for r in range(1,n))
        check(f"constant character count order {d}", order_counts[str(d)] == d//2)
        coeffs = []
        for k in range(s+1):
            l = k//d
            value = (0 if k % d else
                     (-1)**l*prod(range(n//d-l+1, n//d+1))//factorial(l))
            coeffs.append(value)
            check(f"exceptional order {d} coefficient {k}",
                  Fraction(saved["exceptional_cycle_coefficients"][str(d)][k]) == value)
        exceptional[str(d)] = coeffs
        check(f"exceptional order {d} length and terminal zero",
              len(saved["exceptional_cycle_coefficients"][str(d)]) == 68
              and coeffs[s] == 0 and s % d != 0)
    check("all exceptional orders", set(saved["exceptional_cycle_coefficients"]) == set(exceptional))
    check("all constant exceptions", sum(order_counts.values()) == n-1)

    D = n*q*q
    cap = Fraction(C+(D-n)*error, D)
    threshold = Fraction(q**28, 2**128)
    ratio = cap/threshold
    margin = q**28*cap.denominator - 2**128*cap.numerator
    lo_margin = 10**9*2**128*cap.numerator - 1571790*q**28*cap.denominator
    hi_margin = 1571791*q**28*cap.denominator - 10**9*2**128*cap.numerator
    fixed = {
        "Q": q, "n": n, "subset_size": s, "cycle_bound": B,
        "restricted_group_size": D, "nonconstant_character_count": D-n,
        "subset_count": C, "sieve_error": error,
        "mean": rational(Fraction(C,D)), "uniform_cap": rational(cap),
        "integer_cap": cap.numerator//cap.denominator,
        "threshold": rational(threshold), "cap_to_threshold": rational(ratio),
        "ratio_interval": [1571790,1571791,10**9],
        "positive_threshold_margin_cross_product": margin,
    }
    for key, value in fixed.items():
        check(f"full original fixed value {key}", saved["fixed"][key] == value)
    check("all original fixed fields", set(saved["fixed"]) == set(fixed))
    check("strict exact threshold", margin > 0 and cap < threshold)
    check("both strict ratio endpoints", lo_margin > 0 and hi_margin > 0)
    check("integer endpoint", Fraction(fixed["integer_cap"]) < threshold)
    check("Fourier count and index",
          D-n == n*(q*q-1) and (q-1)*q*q == 64*D)
    for key, expected in {
        "cap": rational(cap), "required_threshold": rational(threshold),
        "ratio_interval": fixed["ratio_interval"], "passing": True,
    }.items():
        check(f"full verification value {key}", verification[key] == expected)
    for name, data, count in (("constructor",saved,234), ("verification",verification,214)):
        check(f"{name} saved check record",
              data["checks"] == count == len(data["passed"]) and data["failures"] == [])

    # Rebuild all small subsets directly, with products over combinations for
    # elementary symmetric coefficients, and sum individual logarithmic jets.
    small = saved["small"]
    H = [pow(9,j,17) for j in range(8)]
    index = {x:j for j,x in enumerate(H)}
    check("small instance fixed", small["p"] == 17 and small["H"] == H
          and small["subset_size"] == 5)
    records = {tuple(sorted(r["roots"])):r for r in small["all_root_residues"]}
    expected_sets = {tuple(sorted(S)) for S in combinations(H,5)}
    check("complete unique small subset coverage",
          set(records) == expected_sets and len(small["all_root_residues"]) == 56)
    small_rebuilt, counts = [], {x:0 for x in H}
    for S in sorted(expected_sets):
        es = [sum(prod(J) for J in combinations(S,j)) % 17 for j in range(6)]
        c,b,a = -es[5] % 17, es[4], -es[3] % 17
        invs = [pow(x,-1,17) for x in S]
        u, v = -sum(invs) % 17, -9*sum(x*x for x in invs) % 17
        coords = [index[c],u,v]
        check(f"small full record {S}", records[S] ==
              {"roots": records[S]["roots"], "residue":[c,b,a], "coordinates":coords})
        check(f"small coordinate inverse {S}",
              c*u % 17 == b and c*(v+9*u*u) % 17 == a)
        counts[c] += 1
        small_rebuilt.append({"roots":list(S), "residue":[c,b,a], "coordinates":coords})
    check("complete constant distribution", {str(k):v for k,v in counts.items()} ==
          small["constant_fiber_counts"] and set(counts.values()) == {7})

    manuscript = (base.parent.parent / "lemmas/L100-order-three-pole-uniform-fiber-upper.md").read_text()
    check("manuscript full cap fraction",
          rf"\frac{{{cap.numerator}}}" in manuscript and
          f"{{{cap.denominator}}}" in manuscript)
    check("manuscript full safety margin", str(margin) in manuscript)
    check("manuscript strict ratio interval",
          r"\frac{1571790}{10^9}<\frac U T<\frac{1571791}{10^9}<1" in manuscript)
    out = base / "order-three-pole-uniform-upper-critical-audit.json"
    result = {
        "scope":"Independent L100 arithmetic; symbolic audit is canonical in L100.",
        "inputs":{p.name:sha256(p.read_bytes()).hexdigest() for p in (original,verified)},
        "checks":len(checks), "failures":failures, "check_records":checks,
        "fixed":fixed, "ratio_endpoint_margins":{"lower":lo_margin,"upper":hi_margin},
        "extension_rows":extension_rows, "twist_power_rows":twists,
        "absolute_coefficients":[str(x) for x in absolute],
        "principal_coefficients":[str(x) for x in principal],
        "exceptional_order_counts":order_counts, "exceptional_coefficients":exceptional,
        "small_records":small_rebuilt,
        "limitations":["No new character theorem or arbitrary-center safety.",
                       "All-m completeness uses L099's symbolic degree/root argument."],
    }
    out.write_text(json.dumps(result,indent=2)+"\n")
    print(f"critical audit checks={len(checks)}; failures={failures}")
    print("actual cap/T in (1571790,1571791)/10^9; required <=1")
    print(f"strict threshold and endpoint checks pass={margin > 0 and lo_margin > 0 and hi_margin > 0}")
    print(f"full certificate: {out.relative_to(Path.cwd())}")
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
