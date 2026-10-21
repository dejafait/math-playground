"""Fixed, bounded full finite-group witness; no third-party packages."""
import json
from math import isqrt
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def build():
    trials = []
    tested = []
    for ell in range(11, 501):
        remainders = [[d, ell % d] for d in range(2, isqrt(ell) + 1)]
        prime = all(r for _, r in remainders)
        trials.append({"integer": ell, "remainders": remainders, "prime": prime})
        if not prime or ell == 389:
            continue
        p = ell

        def on(A):
            return A is None or (A[1]**2 + A[1] - A[0]**3 - A[0]**2 + 2*A[0]) % p == 0

        def add(A, B):
            assert on(A) and on(B)
            row = {"left": A, "right": B}
            if A is None:
                C, branch = B, "left_identity"
            elif B is None:
                C, branch = A, "right_identity"
            else:
                x, y = A
                u, v = B
                if x == u and (y+v+1) % p == 0:
                    C, branch = None, "inverse"
                else:
                    if x == u:
                        assert y == v
                        d = (2*y+1) % p
                        sn, nn = 3*x*x+2*x-2, -x**3-2*x-y
                        branch = "tangent"
                    else:
                        d = (u-x) % p
                        sn, nn = v-y, y*u-v*x
                        branch = "chord"
                    inv = pow(d, -1, p)
                    m, n = sn*inv % p, nn*inv % p
                    z = (m*m-1-x-u) % p
                    C = [z, (-m*z-n-1) % p]
                    row.update(denominator=d, inverse=inv, slope=m, intercept=n)
            assert on(C)
            row.update(branch=branch, output=C)
            return C, row

        def seven(A):
            B, r1 = add(A, A)
            C, r2 = add(B, A)
            D, r3 = add(C, C)
            E, r4 = add(D, A)
            return {"point": A, "rows": [r1, r2, r3, r4], "image": E}

        x_rows = [{"x": x, "ys": [y for y in range(p) if on([x, y])]} for x in range(p)]
        points = [None] + [[r["x"], y] for r in x_rows for y in r["ys"]]
        images = [seven(A) for A in points]
        P, Q = [0, 0], [1, 0]
        twice, r1 = add(P, P)
        four, r2 = add(twice, twice)
        negfour = [four[0], (-four[1]-1) % p] if four is not None else None
        R, r3 = add(Q, negfour)
        outside = all(item["image"] != R for item in images)
        good = {"ell": p, "delta_mod_ell": 389 % p, "x_rows": x_rows,
                "points": points, "seven": images,
                "target_rows": [r1, r2, r3], "four_P": four,
                "negative_four_P": negfour, "R": R, "outside_full_image": outside}
        tested.append(good)
        if outside:
            break
    cert = {"schema": "BSD-global-reduction-377-v1", "model": [0, 1, 1, -2, 0],
            "P": [0, 0], "Q": [1, 0], "scalar": 7,
            "bounds": [11, 500], "excluded_bad_prime": 389,
            "integer_trials": trials, "tested": tested,
            "witness_prime": tested[-1]["ell"] if tested[-1]["outside_full_image"] else None}
    path = ROOT / "certificate.json"
    path.write_text(json.dumps(cert, indent=2) + "\n")
    print(json.dumps({"certificate": str(path), "tested_primes": len(tested),
                      "witness_prime": cert["witness_prime"], "required": "R outside full [7] image"}))


if __name__ == "__main__":
    build()
