"""Fixed L097 audit; never imports or executes the producer.

Full evidence is persisted. Any failed check exits nonzero, preserves
the original inventory and records the failure; no retries or range growth.
"""
import hashlib
import json
from pathlib import Path
import subprocess
import sys
from collections import Counter

HERE = Path(__file__).resolve().parent
BASE = HERE.parent.parent
OLD = BASE / "scripts/global-reduction-377"


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def save(name, value):
    (HERE / name).write_text(json.dumps(value, indent=2) + "\n")


def run():
    names = ["build_certificate.py", "verify_certificate.py",
             "certificate.json", "verification.json"]
    originals = HERE / "originals"
    originals.mkdir(exist_ok=False)
    hashes = {}
    for name in names:
        raw = (OLD / name).read_bytes()
        (originals / name).write_bytes(raw)
        hashes[name] = digest(raw)
    save("inventory.json", hashes)
    assert hashes["certificate.json"] == (
        "1a2fc0d80693278515ea44e10c9f4758b054463e476d9913ad8aff8b97be4858")
    result = subprocess.run(
        [sys.executable, "-B", str(OLD / "verify_certificate.py"),
         "--certificate", str(OLD / "certificate.json"),
         "--report", str(HERE / "fresh-replay.json")],
        capture_output=True, text=True, timeout=30)
    save("replay-execution.json", {"exit_code": result.returncode,
                                  "stdout": result.stdout, "stderr": result.stderr})
    assert result.returncode == 0
    c = json.loads((originals / "certificate.json").read_text())
    fresh = json.loads((HERE / "fresh-replay.json").read_text())
    assert fresh == json.loads((originals / "verification.json").read_text())
    assert fresh["tested_primes"] == [11, 13, 17, 19, 23]
    assert fresh["witness_prime"] == 23
    assert fresh["result"] == "PASS" and fresh["failures"] == []

    # Check the exact-model invariants and explicit polynomial translation.
    a1, a2, a3, a4, a6 = c["model"]
    b2 = a1*a1 + 4*a2
    b4 = 2*a4 + a1*a3
    b6 = a3*a3 + 4*a6
    b8 = a1*a1*a6 + 4*a2*a6 - a1*a3*a4 + a2*a3*a3 - a4*a4
    delta = -b2*b2*b8 - 8*b4**3 - 27*b6*b6 + 9*b2*b4*b6
    assert (b2, b4, b6, b8, delta) == (4, -4, 1, -3, 389)
    from fractions import Fraction as F
    # x=X-1/3, y=Y-1/2 gives Y^2=X^3-7X/3+107/108.
    s = F(-1, 3)
    coefficients = [s**3+s*s-2*s+F(1, 4), 3*s*s+2*s-2, 3*s+1, F(1)]
    assert coefficients == [F(107, 108), F(-7, 3), F(0), F(1)]
    assert all(delta % p and 6 % p for p in fresh["tested_primes"])

    # Distinct complete check: no call to either original arithmetic routine.
    # Enumerate by discriminant (2y+1)^2=4x^3+4x^2-8x+1.
    p = 23
    points = [None]
    for x in range(p):
        rhs = (4*x**3+4*x*x-8*x+1) % p
        for z in range(p):
            if z*z % p == rhs:
                # 12 is inverse of 2 modulo 23.
                points.append([x, (12*(z-1)) % p])
    points = [None] + sorted(points[1:])
    assert len(points) == 28 and len({tuple(A) for A in points[1:]}) == 27
    saved = c["tested"][-1]
    assert saved["ell"] == p and points == saved["points"]

    def key(A):
        return None if A is None else tuple(A)

    def neg(A):
        return None if A is None else [A[0], (-A[1]-1) % p]

    def divide(poly, root):
        # Ascending coefficients; exact synthetic division by T-root.
        q = [0]*(len(poly)-1)
        q[-1] = poly[-1] % p
        for i in range(len(q)-2, -1, -1):
            q[i] = (poly[i+1]+root*q[i+1]) % p
        assert (poly[0]+root*q[0]) % p == 0
        return q

    def intersection(A, B):
        row = {"left": A, "right": B}
        if A is None or B is None:
            row.update(branch="identity", output=B if A is None else A)
        elif B == neg(A):
            row.update(branch="vertical", output=None)
        else:
            x, y = A
            u, v = B
            if A == B:
                aa, bb = (-3*x*x-2*x+2) % p, (2*y+1) % p
                cc = (-aa*x-bb*y) % p
                branch = "tangent"
            else:
                aa, bb, cc = (y-v) % p, (u-x) % p, (x*v-u*y) % p
                branch = "secant"
            assert bb != 0
            assert (aa*x+bb*y+cc) % p == (aa*u+bb*v+cc) % p == 0
            # B^2 times the curve equation after substituting the line.
            poly = [(cc*cc-bb*cc) % p,
                    (2*aa*cc-bb*aa+2*bb*bb) % p,
                    (aa*aa-bb*bb) % p, -bb*bb % p]
            q1 = divide(poly, x)
            q2 = divide(q1, u)
            assert q2[1] != 0
            roots = [t for t in range(p) if (q2[0]+q2[1]*t) % p == 0]
            assert len(roots) == 1
            t = roots[0]
            ys = [w for w in range(p) if (aa*t+bb*w+cc) % p == 0]
            assert len(ys) == 1
            third = [t, ys[0]]
            assert third in points
            row.update(branch=branch, line=[aa, bb, cc],
                       polynomial=poly, first_quotient=q1, second_quotient=q2,
                       third_intersection=third, output=neg(third))
        assert row["output"] in points
        return row

    # Persist every input, exceptional branch and polynomial division.
    table, rows = {}, []
    for A in points:
        for B in points:
            row = intersection(A, B)
            table[(key(A), key(B))] = row["output"]
            rows.append(row)
    def add(A, B):
        return table[(key(A), key(B))]

    images, chains = [], []
    for A in points:
        two = add(A, A)
        four = add(two, two)
        six = add(four, two)
        seven = add(six, A)
        images.append(seven)
        chains.append({"point": A, "two": two, "four": four,
                       "six": six, "seven": seven})
    assert images == [item["image"] for item in saved["seven"]]
    assert images == fresh["reports"][-1]["full_image_in_domain_order"]
    target_chain = [[1, 0]]
    for _ in range(4):
        target_chain.append(add(target_chain[-1], neg([0, 0])))
    R = target_chain[-1]
    assert R == [4, 14] == saved["R"] == fresh["reports"][-1]["R"]
    unique = []
    for A in images:
        if A not in unique:
            unique.append(A)
    assert unique == [None, [18, 1], [18, 21], [13, 11]]
    assert R not in unique
    save("intersection-certificate.json", {
        "prime": p, "points": points, "all_addition_rows": rows,
        "seven_chains": chains, "full_image_in_domain_order": images,
        "distinct_image": unique, "Q_minus_P_four_times": target_chain,
        "target": R, "outside": R not in unique,
        "branch_counts": dict(Counter(row["branch"] for row in rows))})
    preserved = {name: digest((OLD / name).read_bytes()) == hashes[name]
                 and digest((originals / name).read_bytes()) == hashes[name]
                 for name in names}
    assert all(preserved.values())
    report = {
        "result": "PASS", "failures": [], "producer_executed": False,
        "input_sha256": hashes, "preserved": preserved,
        "fresh_report_exactly_matches_original": True,
        "tested_primes": fresh["tested_primes"],
        "actual": {
            "affine_pairs": sum(r["affine_pairs_checked"] for r in fresh["reports"]),
            "saved_operations": sum(r["saved_group_operations"] for r in fresh["reports"]),
            "sequential_operations": sum(r["independent_sequential_operations"] for r in fresh["reports"]),
            "distinct_addition_rows": len(rows), "domain_size_at_23": len(points),
            "distinct_image_at_23": unique, "target_at_23": R,
            "outside_full_image": R not in unique},
        "required": {"fixed_primes": [11, 13, 17, 19, 23],
                     "complete_domain_at_23": 28, "complete_addition_table": 784,
                     "outside_full_image": True, "originals_unchanged": True},
        "invariants": {"b2": b2, "b4": b4, "b6": b6, "b8": b8, "delta": delta},
        "evidence": ["fresh-replay.json", "intersection-certificate.json",
                     "inventory.json", "replay-execution.json"]}
    save("audit.json", report)
    print(json.dumps({"result": report["result"], "actual": report["actual"],
                      "required": report["required"], "failures": [],
                      "report": str(HERE / "audit.json")}))


if __name__ == "__main__":
    try:
        run()
    except Exception as exc:
        save("failure.json", {"result": "FAIL", "exception": type(exc).__name__,
                              "message": str(exc)})
        raise
