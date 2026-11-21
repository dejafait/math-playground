"""Audit L843 directly by signed permutations and ordered atom assignments.

No imports from the original generating script. Standard-library exact arithmetic.
"""
from collections import defaultdict
from fractions import Fraction as F
from itertools import product
from math import factorial, prod
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "three-atom-boundary-flux-20261106.json"
OUTPUT = ROOT / "l843-independent-audit-20261106.json"
ATOMS = (0, 1, 4)
SIGNED_PERMS = (((0, 1, 2), 1), ((1, 2, 0), 1), ((2, 0, 1), 1),
                ((0, 2, 1), -1), ((1, 0, 2), -1), ((2, 1, 0), -1))


def clean(p):
    return {k: v for k, v in p.items() if v}


def read_poly(records):
    # Duplicate coefficient slots would invalidate the input certificate.
    p = {tuple(row["a_b_c_powers"]): F(row["coefficient"]) for row in records}
    assert len(p) == len(records)
    return clean(p)


def serial(p):
    return [{"a_b_c_powers": list(k), "coefficient": str(v)}
            for k, v in sorted(p.items())]


def plus(*polys):
    out = defaultdict(F)
    for p in polys:
        for k, v in p.items():
            out[k] += v
    return clean(out)


def monomial(k, value):
    return clean({k: F(value)})


def square_terms(scale, shift, extra_c=False):
    # scale * (b - shift*c)^2, optionally multiplied by c.
    t = int(extra_c)
    return {(0, 2, t): F(scale), (0, 1, 1+t): F(-2*scale*shift),
            (0, 0, 2+t): F(scale*shift*shift)}


def main():
    old = json.loads(SOURCE.read_text())
    checks = {}
    q, dq = [], []
    for n in range(6):
        q.append(clean({tuple(int(i == j) for i in range(3)):
                        F(y**n, factorial(2*n)) for j, y in enumerate(ATOMS)}))
        dq.append(clean({tuple(int(i == j) for i in range(3)):
                         F(y**(n+1), factorial(2*n)) for j, y in enumerate(ATOMS)}))
    checks["all_q0_to_q5"] = q == list(map(read_poly, old["q0_through_q5"]))
    checks["all_q_dot0_to_q_dot5"] = dq == list(map(read_poly, old["q_dot_0_through_5"]))
    checks["all_five_shift_factors"] = all(
        dq[n] == clean({k: v*(2*n+2)*(2*n+1) for k, v in q[n+1].items()})
        for n in range(5))

    det, rows = defaultdict(F), [defaultdict(F) for _ in range(3)]
    contributions = []
    for perm, sign in SIGNED_PERMS:
        orders = tuple(2+i-perm[i] for i in range(3))
        for assignment in product(range(3), repeat=3):
            ys = tuple(ATOMS[j] for j in assignment)
            powers = tuple(assignment.count(j) for j in range(3))
            value = sign * prod(F(y**n, factorial(2*n)) for y, n in zip(ys, orders))
            det[powers] += value
            for i in range(3):
                rows[i][powers] += ys[i]*value
            contributions.append({"permutation": list(perm), "sign": sign,
                                  "orders": list(orders), "atoms": list(ys),
                                  "powers": list(powers), "coefficient": str(value)})
    det, rows = clean(det), list(map(clean, rows))
    D = 14515200
    expected = {(1, 2, 0): F(13,D), (1, 1, 1): F(-496,D),
                (1, 0, 2): F(53248,D), (0, 3, 0): F(313,D),
                (0, 2, 1): F(3117,D), (0, 1, 2): F(-84048,D),
                (0, 0, 3): F(1282048,D)}
    checks["all_ten_cubic_slots_including_three_zeros"] = det == expected
    checks["original_determinant"] = det == read_poly(old["B"])
    for i in range(3):
        checks[f"individual_row_derivative_{i}"] = rows[i] == read_poly(old["row_derivative_terms"][i])
    derivative = plus(*rows)
    checks["direct_exponential_weight_derivative"] = derivative == clean(
        {k: v*(k[1]+4*k[2]) for k, v in det.items()})
    checks["original_full_derivative"] = derivative == read_poly(old["B_prime"])
    Cterms = [square_terms(13,20), monomial((0,1,1),24), monomial((0,0,2),48048)]
    Fterms = [monomial((0,3,0),313), square_terms(3117,14,True),
              monomial((0,1,2),3228), monomial((0,0,3),671116)]
    C = {(0,2,0): F(13), (0,1,1): F(-496), (0,0,2): F(53248)}
    P = {(0,3,0): F(313), (0,2,1): F(3117),
         (0,1,2): F(-84048), (0,0,3): F(1282048)}
    checks["C_square_identity"] = plus(*Cterms) == C == read_poly(old["C_numerator"])
    checks["F_square_identity"] = plus(*Fterms) == P == read_poly(old["F_numerator"])
    checks["all_original_C_square_terms"] = Cterms == list(map(read_poly, old["C_positive_terms"]))
    checks["all_original_F_square_terms"] = Fterms == list(map(read_poly, old["F_positive_terms"]))
    checks["original_denominator"] = D == old["integer_denominator"]
    checks["original_checks_and_failure_status"] = (
        all(old["checks"].values()) and not old["failures"]
        and old["status"] == "FIXED_SUPPORT_NO_BOUNDARY")
    failures = [k for k,v in checks.items() if not v]
    result = {"status": "AUDIT_PASS" if not failures else "AUDIT_FAIL",
              "method": "six explicit signed permutations; 27 ordered atom assignments each",
              "checks": checks, "failures": failures,
              "q0_through_q5": list(map(serial,q)), "q_dot0_through_5": list(map(serial,dq)),
              "determinant": serial(det), "row_derivatives": list(map(serial,rows)),
              "derivative": serial(derivative), "C_square_terms": list(map(serial,Cterms)),
              "F_square_terms": list(map(serial,Fterms)),
              "all_162_assignment_contributions": contributions,
              "actual_bound": "B(0) >= 671116*c^3/14515200 > 0 for a,b,c>0",
              "required_bound": "B(0)=0 is necessary for the approved boundary witness",
              "scope": "fixed support {0,1,4}; no proper-minor, general-cone or actual-Xi sign claim"}
    OUTPUT.write_text(json.dumps(result,indent=2)+"\n")
    print(result["status"], "checks:",len(checks),"failures:",failures)
    print("Actual:",result["actual_bound"])
    print("Required:",result["required_bound"])
    print("Full certificate:",OUTPUT)
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
