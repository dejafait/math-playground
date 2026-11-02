#!/usr/bin/env python3
"""Independent full-leaf rational replay of C645t's saved certificate.

Does not import/execute the generating script and does not modify its evidence.
Reconstructs each binary cell, recomputes its interval bounds, and checks a
complete binary tree rather than relying on the saved sibling reduction.
The analytic proof obligations are documented in C645t, not decided here.
"""

from dataclasses import dataclass
from fractions import Fraction as F
from hashlib import sha256
import json
from pathlib import Path


@dataclass(frozen=True)
class I:
    lo: F
    hi: F

    @staticmethod
    def point(x):
        return I(F(x), F(x))

    def __add__(self, other):
        other = other if isinstance(other, I) else I.point(other)
        return I(self.lo + other.lo, self.hi + other.hi)

    def __sub__(self, other):
        other = other if isinstance(other, I) else I.point(other)
        return I(self.lo - other.hi, self.hi - other.lo)

    def __mul__(self, other):
        other = other if isinstance(other, I) else I.point(other)
        ends = (self.lo * other.lo, self.lo * other.hi,
                self.hi * other.lo, self.hi * other.hi)
        return I(min(ends), max(ends))

    def __truediv__(self, other):
        other = other if isinstance(other, I) else I.point(other)
        if other.lo <= 0 <= other.hi:
            raise ZeroDivisionError("zero in interval denominator")
        return self * I(1 / other.hi, 1 / other.lo)

    def sq(self):
        lower = 0 if self.lo <= 0 <= self.hi else min(self.lo**2, self.hi**2)
        return I(F(lower), max(self.lo**2, self.hi**2))


def encode(value):
    if isinstance(value, F):
        return str(value)
    if isinstance(value, I):
        return [str(value.lo), str(value.hi)]
    if isinstance(value, dict):
        return {key: encode(val) for key, val in value.items()}
    if isinstance(value, (list, tuple)):
        return [encode(val) for val in value]
    return value


R, d, h, Q = F(11, 8), F(5, 4), F(237, 200), F(21, 20)
U, r, s = R * R, F(27, 50), F(13, 200)


def anchor_square(t, c):
    numerator = (I.point(d*d) + t.sq() + t*c*(2*d)) * U
    denominator = I.point(U*U) + t.sq()*(d*d) + t*c*(2*U*d)
    return numerator / denominator


def evaluate(t, c):
    a = t.sq()*(h/U) + t*c
    b = (I.point(1) - t.sq()/U) * R
    cc = I.point(h) + t*c
    k = anchor_square(t, c) * anchor_square(t + F(1, 2), c) / (Q*Q)
    lhs = cc - a*k
    return {"K": k, "C_minus_AK": lhs, "squared_gap": lhs.sq() - b.sq()*k}


def reconstruct(address):
    bounds = [[F(0), F(1, 2)], [F(-1), F(1)]]
    for depth, digit in enumerate(address):
        if digit not in "01":
            raise ValueError("nonbinary address")
        axis = depth % 2
        lo, hi = bounds[axis]
        midpoint = (lo + hi) / 2
        bounds[axis] = [lo, midpoint] if digit == "0" else [midpoint, hi]
    return tuple(I(*axis) for axis in bounds)


base = Path(__file__).parent
source = base / "angular-outer-half-certificate.json"
raw = source.read_bytes()
saved = json.loads(raw)
failures, replayed, checks = [], [], {}


def check(name, condition):
    checks[name] = bool(condition)
    if not condition:
        failures.append(name)


tree = {}
for index, leaf in enumerate(saved["leaves"]):
    address = leaf["address"]
    t, c = reconstruct(address)
    bounds = evaluate(t, c)
    conditions = {
        "endpoints_match_address": encode([t, c]) == [leaf["t"], leaf["c"]],
        "all_interval_endpoints_match": encode(bounds) == leaf["bounds"],
        "strict_inequalities": (bounds["K"].lo > 0 and bounds["K"].hi < 1
                                and bounds["C_minus_AK"].lo > 0
                                and bounds["squared_gap"].lo > 0),
    }
    if not all(conditions.values()):
        failures.append({"leaf": index, "address": address, "checks": conditions})
    replayed.append({"address": address, "t": t, "c": c,
                     "bounds": bounds, "checks": conditions})
    node = tree
    for digit in address:
        if "leaf" in node:
            failures.append({"overlap": address})
        node = node.setdefault(digit, {})
    if node:
        failures.append({"duplicate_or_prefix_overlap": address})
    node["leaf"] = index


def complete(node):
    if "leaf" in node:
        return set(node) == {"leaf"}
    return set(node) == {"0", "1"} and complete(node["0"]) and complete(node["1"])


check("all_leaf_replays_pass", all(all(v["checks"].values()) for v in replayed))
check("complete_binary_tree", complete(tree))
check("leaf_count_matches", len(replayed) == saved["leaf_count"] == 6322)
depth = max(len(v["address"]) for v in replayed)
check("depth_matches", depth == saved["maximum_depth_used"] == 16)
check("normalized_leaf_area_is_one", sum((F(1, 2**len(v["address"])) for v in replayed), F(0)) == 1)
minimum = {
    "K_lower": min(v["bounds"]["K"].lo for v in replayed),
    "K_upper": max(v["bounds"]["K"].hi for v in replayed),
    "C_minus_AK_lower": min(v["bounds"]["C_minus_AK"].lo for v in replayed),
    "squared_gap_lower": min(v["bounds"]["squared_gap"].lo for v in replayed),
}
check("all_extrema_match", encode(minimum) == saved["minimum_bounds"])
check("domain_matches", saved["domain"] == {
    "t": ["0", "1/2"], "c": ["-1", "1"], "Q": str(Q), "half_plane_h": str(h)})
check("source_has_no_failures", saved["failures"] == [])

radius2 = d*d + r*r
ellipse2 = radius2 + s*s*(1 + d*d/(r*r))
rho_log = F(13, 108)*F(100, 101)
arc_rate = F(47, 1000) - F(45, 3784)
error_rate = F(2, 3)*rho_log - F(1, 40)
geometry_checks = {
    "all_boxes_pass": checks["all_leaf_replays_pass"],
    "complete_dyadic_partition": checks["complete_binary_tree"],
    "K_strictly_between_zero_and_one": minimum["K_lower"] > 0 and minimum["K_upper"] < 1,
    "positive_unsquared_side": minimum["C_minus_AK_lower"] > 0,
    "positive_squared_gap": minimum["squared_gap_lower"] > 0,
    "pole_clearance": radius2 < (R-F(1, 100))**2,
    "arc_radius_lower": radius2 > F(34, 25)**2,
    "arc_denominator_margin": (U-radius2)/(2*R) > F(1, 100),
    "ellipse_denominator_margin": (U-ellipse2)/(2*R) > F(1, 300),
    "low_factor_minimum": R*(F(34, 25)-F(1, 2))/(U-F(34, 25)/2) == F(1892, 1937),
    "arc_rate_beats_7_over_200": arc_rate > F(7, 200),
    "square_root_upper": 1 + F(13, 108)**2 < F(101, 100)**2,
    "error_rate_beats_7_over_200": error_rate > F(7, 200),
    "seven_over_200_beats_target": F(7, 200) > F(1, 32),
    "outer_shift_derivative_bound": 1/(d-1) + d/(U-d) < 6,
    "quadrature_denominator_for_n_ge_15": F(2, 3)*15*rho_log > 1,
}
check("all_original_checks_recomputed", all(geometry_checks.values()))
check("all_original_check_values_match", geometry_checks == saved["checks"])
rates = {
    "arc_radius_squared": radius2, "ellipse_maximum_radius_squared": ellipse2,
    "arc_exponent_lower": arc_rate, "ellipse_log_rho_lower": rho_log,
    "quadrature_exponent_lower": error_rate,
    "claimed_response_exponent": F(7, 200), "required_exponent": F(1, 32),
    "exponent_margin": F(7, 200)-F(1, 32),
}
check("all_geometry_and_rates_match", encode(rates) == saved["rates_and_geometry"])
first_path = base / "angular-outer-half-certificate-first-pass.json"
first = json.loads(first_path.read_bytes())
check("n9_failure_retained_and_real", (F(2, 3)*9*rho_log < 1
      and first["checks"]["quadrature_denominator_for_n_ge_9"] is False))

# Independently check the only quantitative input needed from C645n.
log_records = []
for q in (F(11, 10), F(201, 121), F(9, 5)):
    v = (q-1)/(q+1)
    lower = 2*sum((v**(2*k+1)/F(2*k+1) for k in range(16)), F(0))
    upper = lower + 2*v**33/(33*(1-v*v))
    log_records.append({"argument": q, "lower": lower, "upper": upper})
lambda_lower = log_records[0]["lower"] + F(201, 80)*log_records[1]["lower"] - F(9, 4)*log_records[2]["upper"]
lambda_upper = log_records[0]["upper"] + F(201, 80)*log_records[1]["upper"] - F(9, 4)*log_records[2]["lower"]
check("anchor_lambda_exceeds_47_over_1000", lambda_lower > F(47, 1000))
anchor_path = base / "angular-inner-input-rate-check.json"
anchor = json.loads(anchor_path.read_bytes())


def decode_fraction(pair):
    return F(int(pair["numerator"]), int(pair["denominator"]))


check("anchor_lambda_endpoints_match", lambda_lower == decode_fraction(anchor["lambda"]["lower"])
      and lambda_upper == decode_fraction(anchor["lambda"]["upper"]))
check("anchor_log_endpoints_match", all(
    record["argument"] == decode_fraction(old["argument"])
    and record["lower"] == decode_fraction(old["lower"])
    and record["upper"] == decode_fraction(old["upper"])
    for record, old in zip(log_records, anchor["log_series_inputs"], strict=True)))

out = base / "angular-outer-half-audit.json"
report = {
    "status": "EXACT_RATIONAL_REPLAY_PASS" if not failures else "FAILED",
    "input_sha256": {source.name: sha256(raw).hexdigest(),
                     first_path.name: sha256(first_path.read_bytes()).hexdigest(),
                     anchor_path.name: sha256(anchor_path.read_bytes()).hexdigest()},
    "checks": checks, "original_checks_recomputed": geometry_checks,
    "leaf_count": len(replayed), "maximum_depth": depth,
    "minimum_bounds": minimum, "rates_and_geometry": rates,
    "anchor_rate": {"log_intervals": log_records,
                    "lambda_lower": lambda_lower, "lambda_upper": lambda_upper,
                    "required_lower_bound": F(47, 1000)},
    "failures": failures, "replayed_leaves": replayed,
    "limits": ["Analytic domains, level-circle implication and contour identities require the written audit.",
               "This certifies one input's full-response estimate, not an upper bound on the operator norm."]}
out.write_text(json.dumps(encode(report), indent=2) + "\n")
print("Independent exact leaf replays:", len(replayed), "/", saved["leaf_count"], "depth:", depth)
print("Audit checks:", sum(checks.values()), "/", len(checks), "; original checks:", sum(geometry_checks.values()), "/", len(geometry_checks))
print("Response rate:", F(7, 200), "; target:", F(1, 32), "; margin:", F(3, 800))
print("Arc rate:", arc_rate, "; quadrature rate:", error_rate, "; both required >", F(7, 200))
print("Anchor lambda >", F(47, 1000), ":", checks["anchor_lambda_exceeds_47_over_1000"])
print("Failures:", failures)
print("Full audit certificate:", out)
if failures:
    raise SystemExit(1)
