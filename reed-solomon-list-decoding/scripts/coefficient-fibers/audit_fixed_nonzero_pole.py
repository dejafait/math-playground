"""Independent, exact audit of unchanged L102; no bound search or retuning."""
from fractions import Fraction as F
from hashlib import sha256
from itertools import combinations, product
from math import comb, factorial, gcd, prod
from pathlib import Path
import json
import os
import subprocess
import sys

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "fixed-nonzero-pole-results.json"
OUT = HERE / "fixed-nonzero-pole-critical-audit.json"
checks = []


def check(name, value):
    checks.append({"name": name, "passed": bool(value)})


def rational(value):
    return F(value["numerator"], value["denominator"])


def pack(value):
    value = F(value)
    return {"numerator": value.numerator, "denominator": value.denominator}


# Preserve the original evidence before rerunning the specified constructor.
before = SOURCE.read_bytes()
(HERE / "fixed-nonzero-pole-critical-source.json").write_bytes(before)
run = subprocess.run(
    [sys.executable, str(HERE / "fixed_nonzero_pole.py")],
    env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"},
    capture_output=True, text=True,
)
(HERE / "fixed-nonzero-pole-critical-constructor.log").write_text(
    run.stdout + run.stderr
)
check("constructor exit", run.returncode == 0)
check("complete constructor reproduction", before == SOURCE.read_bytes())
saved = json.loads(before)
check("constructor check count", len(saved["checks"]) == saved["check_count"] == 5853)
check("all constructor checks", all(row["passed"] for row in saved["checks"]))
check("constructor failure list", saved["failures"] == [])

Q, n, s, B = 65537, 1024, 67, 769
D = (Q - 1) * Q * Q
T = F(Q**28, 2**128)
check("parameters", saved["parameters"] == {
    "Q": Q, "n": n, "s": s, "B": B, "full_group_order": D})
check("prime by trial division", all(Q % p for p in range(2, 257)))
powers = []
x = 1
for exponent in range(Q - 1):
    powers.append(x)
    x = x * 3 % Q
check("full primitive orbit", x == 1 and len(set(powers)) == Q - 1)
H = set(powers[::64])
check("exact H generator and minus one", len(H) == n and powers[64] == 19139
      and Q - 1 in H and 3 not in H and 0 not in H)

# Exact cyclotomic arithmetic in Z[zeta_64], zeta_64^32 = -1.
def root_vector(e):
    e %= 64
    out = [0] * 32
    out[e % 32] = 1 if e < 32 else -1
    return out


indicator = []
for residue in range(64):
    v = [sum(root_vector(t * residue)[i] for t in range(64))
         for i in range(32)]
    indicator.append(v)
    check(f"complete twist sum residue {residue}",
          v == [64 if residue == 0 else 0] + [0] * 31)
for e, x in enumerate(powers):
    # -1 = 3^32768; the minus sign preserves the residue modulo 64.
    check(f"subgroup indicator exponent {e}",
          indicator[(e + 32768) % 64][0] == 64 * (x in H))

excluded = []
for x in range(Q):
    is_nonunit = (x * (x - 3)) % Q == 0
    check(f"joint modulus nonunit {x}", is_nonunit == (x in (0, 3)))
    if is_nonunit:
        excluded.append({"evaluation": x, "all_positive_powers_zero": True})

exceptional_complete_sums = []
for twist in range(64):
    if twist == 0:
        v = [Q - 2] + [0] * 31
    else:
        v = [-c for c in root_vector(twist * (32768 + 1))]
    exceptional_complete_sums.append(v)
check("principal-power complete twist average",
      [sum(v[i] for v in exceptional_complete_sums) for i in range(32)]
      == [64 * n] + [0] * 31)

check("character multiplicity total",
      1 + (Q - 1) * (Q**2 - 1) + sum(2**(a - 1) for a in range(1, 17)) == D)
check("strict Weil rounding", 9 * Q < B**2)
nonconstant_schedule = []
for j in range(1, s + 1):
    inverse = pow(j, -1, Q)
    check(f"nonconstant power invertible {j}", j * inverse % Q == 1)
    # CRT independence and this inverse handle every nonzero (alpha,beta),
    # not merely a sampled additive character. The proof is in L102.
    nonconstant_schedule.append({
        "power": j, "inverse_mod_Q": inverse,
        "joint_principal_by_twist": [False] * 64,
        "cycle_allowance": B,
    })

# Reconstruct the unsigned cycle polynomial as a product of 67 separate
# exp(b_j*t^j/j) factors. Neither constructor coefficient method is reused.
orders = []
check("all sixteen order records", len(saved["exceptional_orders"]) == 16)
for a in range(1, 17):
    d = 2**a
    original = saved["exceptional_orders"][a - 1]
    check(f"order metadata {d}",
          original["order"] == d and original["multiplicity"] == d // 2)
    weights, schedule = [], []
    for j in range(1, s + 1):
        powered_order = d // gcd(d, j)
        theta_exponent = ((Q - 1) // d * j) % (Q - 1)
        flags = [(1024 * twist == 0 and theta_exponent == 0)
                 for twist in range(64)]
        expected = [(twist == 0 and j % d == 0) for twist in range(64)]
        check(f"all CRT twists order {d} power {j}", flags == expected)
        weight = n if powered_order == 1 else B
        weights.append(weight)
        schedule.append({"power": j, "powered_order": powered_order,
                         "principal_by_twist": flags, "cycle_allowance": weight})
    check(f"all saved cycle weights {d}", weights == original["cycle_weights"])
    coeff = [F(1)] + [F(0)] * s
    for j, weight in enumerate(weights, 1):
        next_coeff = [F(0)] * (s + 1)
        for repetitions in range(s // j + 1):
            factor = F(weight**repetitions, j**repetitions * factorial(repetitions))
            for k in range(s + 1 - j * repetitions):
                next_coeff[k + j * repetitions] += coeff[k] * factor
        coeff = next_coeff
    check(f"coefficient length {d}", len(original["coefficients"]) == s + 1)
    for k in range(s + 1):
        check(f"independent coefficient order {d} degree {k}",
              coeff[k] == rational(original["coefficients"][k]))
    check(f"subset coefficient {d}", coeff[s] == rational(original["subset_bound"]))
    if d > s:
        check(f"no exceptional cycle order {d}", coeff[s] == comb(B + s - 1, s))
    orders.append({"order": d, "multiplicity": d // 2, "schedule": schedule,
                   "coefficients": [pack(v) for v in coeff]})

principal = F(comb(n, s), D)
nonconstant = F((Q - 1) * (Q**2 - 1), D) * comb(B + s - 1, s)
constant = sum(F(row["multiplicity"], D) * rational(row["coefficients"][s])
               for row in orders)
U = principal + nonconstant + constant
values = {
    "threshold": T, "principal": principal, "nonconstant": nonconstant,
    "constant_only": constant, "uniform_upper": U, "ratio": U / T,
    "positive_failure_margin": U - T,
}
for name, value in values.items():
    check(f"complete saved rational {name}", rational(saved[name]) == value)
check("saved binomial", saved["binomial"] == comb(n, s))
check("saved nonconstant subset allowance", saved["nonconstant_subset_bound"] == comb(835, 67))
check("strict saved bracket", saved["strict_ratio_interval"] == [4780, 4781])
check("exact failed cap", 4780 * T < U < 4781 * T)
check("integer cap also fails", U.numerator // U.denominator > T)
check("nonconstant allowance fails independently", nonconstant > T)
check("manuscript numerator",
      U.numerator == 53044746895146418049153132401454442254356973583738869432485950492034551354853198737919018505853426586934259601547817580502080635966595)
check("manuscript denominator", U.denominator == 5192455316068781976820312591826944)

# Independent small enumeration in X coordinates. For each (f,a,b), solve
# for c separately at every evaluation point and group equal c values.
# This covers all scalar messages and all centers without using root
# products to generate the purported list.
q = 17
small_H = [x for x in range(1, q) if pow(x, 8, q) == 1]
small = saved["small_case"]
check("small parameters", {k: small[k] for k in
      ("field", "H", "pole", "k", "s", "centers_checked", "messages_per_center")}
      == {"field": 17, "H": small_H, "pole": 3, "k": 2, "s": 5,
          "centers_checked": 4624, "messages_per_center": 289})
actual = {(a, b, c): [] for a, b, c in product(range(q), range(q), range(1, q))}
for f0, f1, a, b in product(range(q), repeat=4):
    by_c = {}
    for x in small_H:
        z = (x - 3) % q
        c = (z**3 * (f0 + f1*x) - z**5 - a*z*z - b*z) % q
        by_c.setdefault(c, []).append(x)
    for c, support in by_c.items():
        if c and len(support) >= 5:
            actual[(a, b, c)].append({
                "message_in_Z": [(f0 + 3*f1) % q, f1], "support": support})

expected = {}
for S in combinations(small_H, 5):
    # Elementary symmetric coefficients in X, followed by Taylor shift.
    g = [sum((-1)**(5-k) * prod(part) for part in combinations(S, 5-k)) % q
         for k in range(6)]
    shifted = [sum(g[j] * comb(j, k) * 3**(j-k)
                   for j in range(k, 6)) % q for k in range(6)]
    c, b, a = shifted[:3]
    fZ = [(-shifted[3]) % q, (-shifted[4]) % q]
    expected.setdefault((a, b, c), []).append({"message_in_Z": fZ, "support": list(S)})
    # Coefficient-level quotient identity, including the leading cancellation.
    residual = [(shifted[i] + (fZ[i-3] if 3 <= i < 5 else 0)
                 - ({0: c, 1: b, 2: a, 5: 1}.get(i, 0))) % q
                for i in range(6)]
    check(f"small full polynomial identity {S}", residual == [0] * 6)

saved_fibers = {tuple(row["label_abc"]): row["list"] for row in small["occupied_fibers"]}
check("no duplicate saved occupied labels", len(saved_fibers) == len(small["occupied_fibers"]))
full_lists = []
for label, records in actual.items():
    records.sort(key=lambda row: row["message_in_Z"])
    expected_records = sorted(expected.get(label, []), key=lambda row: row["message_in_Z"])
    check(f"independent entire scalar list {label}", records == expected_records)
    check(f"complete saved small list {label}", records == saved_fibers.get(label, []))
    check(f"exact small agreement {label}", all(len(row["support"]) == 5 for row in records))
    full_lists.append({"label_abc": list(label), "list": records})
check("saved occupied label coverage", set(saved_fibers) == set(expected))
check("all 56 subsets counted", sum(map(len, actual.values())) == comb(8, 5) == 56)

certificate = {
    "target": "Unchanged L102 dictionary, full character cases and one failed upper allowance",
    "source_sha256": sha256(before).hexdigest(),
    "constructor_reproduced_exactly": before == SOURCE.read_bytes(),
    "scope": {"all_nonzero_additive_characters": "symbolic invertibility plus CRT proof in L102",
              "orders": 16, "powers_per_order": 67, "twists_per_power": 64,
              "ambient_tuple_width": "all m>=1 by L102 root/divisibility proof; not enumeration"},
    "indicator_vectors": indicator,
    "zero_extended_points": excluded,
    "principal_power_complete_sums": exceptional_complete_sums,
    "nonconstant_schedule": nonconstant_schedule,
    "orders": orders,
    "exact_values": {key: pack(value) for key, value in values.items()},
    "comparisons": {"actual_upper_over_T_interval": [4780, 4781], "required_upper_over_T": 1,
                    "floor_upper": U.numerator // U.denominator,
                    "floor_upper_minus_T": pack(U.numerator // U.denominator - T),
                    "lower_cross_margin": pack(U - 4780*T),
                    "upper_cross_margin": pack(4781*T - U)},
    "complete_small_lists": full_lists,
    "checks": checks, "check_count": len(checks),
    "failures": [row for row in checks if not row["passed"]],
}
OUT.write_text(json.dumps(certificate, indent=2) + "\n")
print(f"Independent checks: {len(checks)}; failures: {len(certificate['failures'])}")
print("Actual upper/T: (4780,4781); required: <=1; integer floor also fails.")
print(f"Full audit certificate: {OUT}")
if certificate["failures"]:
    print("Failed checks: " + ", ".join(row["name"] for row in certificate["failures"][:10]))
    raise SystemExit(1)
