"""Independent exact verification of the saved failed reconstruction.

No constructor import or numerical solve. Rebuild all ordered incidences,
the lift, and every cardinality equation. A negative triple rejects only
the saved point, not the free-variable system.
"""
import hashlib
import json
import math
import time
from fractions import Fraction as F
from pathlib import Path

import numpy as np

BASE = Path(__file__).parent
PREFIX = "free-cardinality-zero-block-"
START = time.monotonic()


def main():
    def read(s):
        return json.loads((BASE/(PREFIX+s)).read_text())
    m, c, result = read("model.json"), read("reconstruction.json"), read("results.json")
    data = np.load(BASE/(PREFIX+"model.npz"))
    keys, orbits = data["keys"], data["orbit"]
    ni = c["scaled_rounded_integers"]
    den = c["common_denominator"]
    overrides = {int(q): F(*x) for q, x in c["exact_overrides"].items()}
    pe, ye = m["pair_variable_exponent"], m["triple_variable_exponent"]
    emin = min(0, pe, ye)-40
    assert den == 2**(-emin)
    nums = [v*2**((0 if q == 0 else pe if q < 69 else ye)-40-emin)
            for q, v in enumerate(ni)]
    nums[0] = den
    def value(q):
        return overrides.get(q, F(nums[q], den))
    assert value(0) == 1 and all(value(q) == 0 for q in range(1, 5))
    N = 65537**28//2**128+1
    G = [math.comb(68, i)*math.comb(956, i) for i in range(69)]
    assert N == m["parameters"]["N"] and G == m["G"]
    assert sum(G[i]*value(i) for i in range(69)) == N
    # Independent factorial binomial tables; choose INCLUDED points in
    # A\B and A intersection B, and added points outside A.
    fact = [math.factorial(i) for i in range(957)]
    def cb(n, k):
        return fact[n]//(fact[k]*fact[n-k]) if 0 <= k <= n else 0
    sums = [0]*69
    extras = [dict() for _ in range(69)]
    pivot_counts = [0]*69
    qlookup = {tuple(map(int, key)): q for q, key in enumerate(keys)}
    seen = set()
    off = 0
    actual_repetitions = forbidden = 0
    first_negative = None
    for i in range(69):
        for j in range(69):
            for t in range(max(0, i+j-68), min(i, j)+1):
                inside = cb(i, i-t)*cb(68-i, 68-i-j+t)
                for s in range(max(0, i+j-956), min(i, j)+1):
                    h = i+j-t-s
                    is_forbidden = any(1 <= z <= 4 for z in (i, j, h))
                    is_repeat = min(i, j, h) == 0
                    actual_repetitions += int(is_repeat)
                    forbidden += int(is_forbidden)
                    if is_forbidden:
                        q = 1
                    elif is_repeat:
                        q = max(i, j, h)
                    else:
                        q = qlookup[tuple(sorted((i, j, h)))+(t-s,)]
                        seen.add(q)
                    assert orbits[off].tolist() == [i, j, t, s, h, q]
                    d = inside*cb(i, s)*cb(956-i, j-s)
                    if q in overrides:
                        extras[i][q] = extras[i].get(q, 0)+d
                        if q >= 69:
                            assert tuple(keys[q]) == (i, i, i, i)
                            assert j == t == i and s == 0
                            pivot_counts[i] += 1
                    else:
                        sums[i] += d*nums[q]
                    if first_negative is None and value(q) < 0:
                        first_negative = dict(ordered_orbit=[i, j, t, s],
                                              coordinate=q,
                                              value=[value(q).numerator, value(q).denominator])
                    off += 1
    assert off == len(orbits) == 1500625
    assert len(seen) == len(keys)-69
    assert actual_repetitions == 205 and forbidden == 10232
    assert pivot_counts == c["pivot_counts"] == [0]*5+[1]*64
    residuals = [F(sums[i], den)+sum(d*overrides[q] for q, d in extras[i].items()) -
                 N*value(i) for i in range(69)]
    assert residuals == [F(*z) for z in c["all_69_contraction_residuals"]]
    assert all(z == 0 for z in residuals)
    assert first_negative is not None
    bad = result["exact_failure"]
    q = bad["coordinate"]
    assert value(q) == F(*bad["value"]) < 0
    assert keys[q].tolist() == bad["key"]
    i, j, t, s, h, qq = bad["ordered_orbit"]
    assert q == qq and h == i+j-t-s
    assert min(i-t, j-t, t, 68-i-j+t, i-s, j-s, s, 956-i-j+s) >= 0
    assert all(z == 0 or z >= 5 for z in (i, j, h))
    assert tuple(sorted((i, j, h)))+(t-s,) == tuple(keys[q])
    # Rank65 is certified by the triangular65-column submatrix,
    # with G68 and these64 nonzero diagonal entries.
    diagonal = [G[68]]+[cb(956-i, i) for i in range(5, 69)]
    assert all(d > 0 for d in diagonal)
    assert m["pivot_D"] == diagonal[1:]
    out = dict(verdict="SAVED_POINT_REJECTED_ONLY", failures=[],
               original_ordered_orbits_checked=off,
               source_lift_classes_checked=len(seen),
               repeated_orbits_including_forbidden=actual_repetitions,
               forbidden_orbits=forbidden, all_69_contraction_residuals=[[0, 1]]*69,
               equality_rank=65, triangular_diagonal=diagonal,
               first_negative=first_negative, saved_negative=bad,
               additional_source_orbit_visits=off,
               combined_source_orbit_visits=result["coefficient_visits"]+off,
               required_visit_cap=20000000,
               verification_seconds=time.monotonic()-START,
               input_sha256={s: hashlib.sha256((BASE/(PREFIX+s)).read_bytes()).hexdigest()
                             for s in ("model.npz", "model.json", "reconstruction.json", "results.json")},
               qualification="No feasibility or infeasibility verdict for the system; no omitted sign or PSD certification.")
    assert out["combined_source_orbit_visits"] <= out["required_visit_cap"]
    dest = BASE/(PREFIX+"verification.json")
    dest.write_text(json.dumps(out, indent=2)+"\n")
    print("Exact verification:", off, "orbits; 69/69 zero contractions;",
          "negative scalar retained; system UNDECIDED")
    print("Coefficient visits:", out["combined_source_orbit_visits"], "/ 20000000")
    print("Evidence:", dest)


if __name__ == "__main__":
    main()
