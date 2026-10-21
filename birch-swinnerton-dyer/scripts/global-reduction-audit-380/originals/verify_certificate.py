"""Complete replay using a short model and a different scalar chain.

Does not import or execute the producer. Reports are written only after
all checks; assertion failure exits nonzero and is never called a PASS.
"""
import argparse
import hashlib
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def verify(c):
    assert c["schema"] == "BSD-global-reduction-377-v1"
    assert c["model"] == [0, 1, 1, -2, 0]
    assert c["P"] == [0, 0] and c["Q"] == [1, 0] and c["scalar"] == 7
    assert c["bounds"] == [11, 500] and c["excluded_bad_prime"] == 389
    assert c["tested"] and c["integer_trials"]
    last = c["integer_trials"][-1]["integer"]
    assert 11 <= last <= 500
    assert [r["integer"] for r in c["integer_trials"]] == list(range(11, last+1))
    good_primes = []
    for row in c["integer_trials"]:
        n = row["integer"]
        ds = []
        d = 2
        while d*d <= n:
            ds.append([d, n % d])
            d += 1
        assert row["remainders"] == ds
        is_prime = all(v != 0 for _, v in ds)
        assert row["prime"] is is_prime
        if is_prime and n != 389:
            good_primes.append(n)
    assert [r["ell"] for r in c["tested"]] == good_primes
    reports, branches = [], Counter()
    for entry in c["tested"]:
        p = entry["ell"]
        assert p != 389 and entry["delta_mod_ell"] == 389 % p != 0
        i2, i3 = pow(2, -1, p), pow(3, -1, p)
        a, b = -7*i3 % p, 107*pow(108, -1, p) % p

        def valid(A):
            if A is None:
                return True
            return (isinstance(A, list) and len(A) == 2
                    and all(type(v) is int and 0 <= v < p for v in A)
                    and (A[1]**2+A[1]-A[0]**3-A[0]**2+2*A[0]) % p == 0)

        def translate(A):
            assert valid(A)
            if A is None:
                return None
            X, Y = (A[0]+i3) % p, (A[1]+i2) % p
            assert (Y*Y-X**3-a*X-b) % p == 0
            return X, Y

        def short_add(A, B):
            U, V = translate(A), translate(B)
            if U is None:
                return B
            if V is None:
                return A
            x, y = U
            u, v = V
            if x == u and (y+v) % p == 0:
                return None
            if x == u:
                assert y == v and 2*y % p != 0
                m = (3*x*x+a)*pow(2*y, -1, p) % p
            else:
                m = (v-y)*pow(u-x, -1, p) % p
            z = (m*m-x-u) % p
            w = (m*(x-z)-y) % p
            C = [(z-i3) % p, (w-i2) % p]
            assert valid(C)
            return C

        def check_row(row, A, B):
            assert row["left"] == A and row["right"] == B
            assert valid(A) and valid(B) and valid(row["output"])
            C = short_add(A, B)
            assert row["output"] == C
            if A is None:
                branch = "left_identity"
            elif B is None:
                branch = "right_identity"
            elif A[0] == B[0] and (A[1]+B[1]+1) % p == 0:
                branch = "inverse"
            else:
                x, y = A
                u, v = B
                if x == u:
                    assert y == v
                    branch, d = "tangent", (2*y+1) % p
                else:
                    branch, d = "chord", (u-x) % p
                assert d != 0 and row["denominator"] == d
                inv, m, n = row["inverse"], row["slope"], row["intercept"]
                assert all(type(t) is int and 0 <= t < p for t in [inv, m, n])
                assert d*inv % p == 1
                assert (m*x+n-y) % p == 0 and (m*u+n-v) % p == 0
                if branch == "tangent":
                    assert ((2*y+1)*m-(3*x*x+2*x-2)) % p == 0
                z, w = C
                assert (m*z+n+w+1) % p == 0
                # Complete line-intersection identity, all coefficients.
                left = [(n*n+n) % p, (2*m*n+m+2) % p, (m*m-1) % p, -1 % p]
                right = [x*u*z % p, -(x*u+x*z+u*z) % p, (x+u+z) % p, -1 % p]
                assert left == right
            assert row["branch"] == branch
            keys = {"left", "right", "branch", "output"}
            if branch in {"chord", "tangent"}:
                keys |= {"denominator", "inverse", "slope", "intercept"}
            assert set(row) == keys
            branches[branch] += 1
            return C

        # Enumerate the full affine plane independently, and check smoothness.
        points = [None]
        x_rows = []
        for x in range(p):
            ys = []
            for y in range(p):
                if (y*y+y-x*x*x-x*x+2*x) % p == 0:
                    assert ((2*y+1) % p, (-3*x*x-2*x+2) % p) != (0, 0)
                    ys.append(y)
                    points.append([x, y])
            x_rows.append({"x": x, "ys": ys})
        # Unique point at infinity is [0:1:0]; homogeneous dF/dZ there is 1.
        assert entry["points"] == points and entry["x_rows"] == x_rows
        assert len(entry["seven"]) == len(points)
        sequential, outputs = [], []
        for A, item in zip(points, entry["seven"]):
            assert item["point"] == A and len(item["rows"]) == 4
            B = check_row(item["rows"][0], A, A)
            C = check_row(item["rows"][1], B, A)
            D = check_row(item["rows"][2], C, C)
            E = check_row(item["rows"][3], D, A)
            assert item["image"] == E
            seq, acc = [None], None
            for _ in range(7):
                acc = short_add(acc, A)
                seq.append(acc)
            assert seq[2] == B and seq[3] == C and seq[6] == D and seq[7] == E
            sequential.append({"point": A, "multiples_0_through_7": seq})
            outputs.append(E)

        P, Q = [0, 0], [1, 0]
        assert len(entry["target_rows"]) == 3
        two = check_row(entry["target_rows"][0], P, P)
        four = check_row(entry["target_rows"][1], two, two)
        neg = None if four is None else [four[0], (-four[1]-1) % p]
        assert entry["four_P"] == four and entry["negative_four_P"] == neg
        assert short_add(four, neg) is None
        R = check_row(entry["target_rows"][2], Q, neg)
        assert entry["R"] == R
        # Distinct sequential chain for four P, including all intermediates.
        seqP, acc = [None], None
        for _ in range(4):
            acc = short_add(acc, P)
            seqP.append(acc)
        assert acc == four
        outside = R not in outputs
        assert entry["outside_full_image"] is outside
        unique = []
        for A in outputs:
            if A not in unique:
                unique.append(A)
        reports.append({"ell": p, "point_count": len(points), "affine_pairs_checked": p*p,
                        "saved_group_operations": 4*len(points)+3,
                        "independent_sequential_operations": 7*len(points)+4,
                        "distinct_image": unique, "full_image_in_domain_order": outputs,
                        "R": R, "four_P": four, "four_P_sequential": seqP,
                        "sequential_seven_chains": sequential,
                        "outside_full_image": outside})
        # No further prime is allowed after the first successful witness.
        if outside:
            assert entry is c["tested"][-1]
    witness = reports[-1]["ell"] if reports[-1]["outside_full_image"] else None
    assert c["witness_prime"] == witness
    assert last == (witness if witness is not None else 500)
    return {"result": "PASS", "failures": [], "required": "R outside entire multiplication-by-seven image",
            "bounds": [11, 500], "tested_primes": good_primes, "witness_prime": witness,
            "branch_counts": dict(branches), "reports": reports}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--certificate", type=Path, default=ROOT / "certificate.json")
    parser.add_argument("--report", type=Path, default=ROOT / "verification.json")
    args = parser.parse_args()
    raw = args.certificate.read_bytes()
    report = verify(json.loads(raw))
    report["certificate_sha256"] = hashlib.sha256(raw).hexdigest()
    args.report.write_text(json.dumps(report, indent=2)+"\n")
    print(json.dumps({"result": report["result"], "failures": report["failures"],
                      "tested_primes": report["tested_primes"], "witness_prime": report["witness_prime"],
                      "required": report["required"],
                      "actual": [{"ell": r["ell"], "points": r["point_count"], "R": r["R"],
                                  "image_size": len(r["distinct_image"]), "outside": r["outside_full_image"]}
                                 for r in report["reports"]],
                      "report": str(args.report)}))
