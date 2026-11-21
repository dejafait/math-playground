"""One exact-rational propagation of L917 panel0 into C028s's H.

No quadrature is executed. Input inclusion is conditional on L917/L037.
The operation trace and full rational endpoints are saved to disk.
"""
from dataclasses import dataclass
from fractions import Fraction as Q
from hashlib import sha256
import json
from math import factorial
from pathlib import Path
import platform


ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "scripts/heat/low-time-h2-uniform-195.json"
OUTPUT = Path(__file__).with_suffix(".json")
TRACE = []


@dataclass(frozen=True)
class Box:
    lower: Q
    upper: Q

    def __post_init__(self):
        if self.lower > self.upper:
            raise ValueError("reversed interval")

    def record(self):
        return {"lower": str(self.lower), "upper": str(self.upper)}


def save(name, operation, inputs, result):
    TRACE.append({"name": name, "operation": operation, "inputs": inputs,
                  "interval": result.record()})
    return result


def scale(name, a_name, a, scalar):
    endpoints = (scalar * a.lower, scalar * a.upper)
    return save(name, "scale", [a_name, str(scalar)],
                Box(min(endpoints), max(endpoints)))


def add(name, a_name, a, b_name, b):
    return save(name, "add", [a_name, b_name],
                Box(a.lower + b.lower, a.upper + b.upper))


def subtract(name, a_name, a, b_name, b):
    return save(name, "subtract", [a_name, b_name],
                Box(a.lower - b.upper, a.upper - b.lower))


def multiply(name, a_name, a, b_name, b):
    endpoints = [x * y for x in (a.lower, a.upper)
                 for y in (b.lower, b.upper)]
    return save(name, "multiply", [a_name, b_name],
                Box(min(endpoints), max(endpoints)))


def square(name, a_name, a):
    lo = Q(0) if a.lower <= 0 <= a.upper else min(a.lower**2, a.upper**2)
    return save(name, "square", [a_name],
                Box(lo, max(a.lower**2, a.upper**2)))


def divide(name, a_name, a, b_name, b):
    if b.lower <= 0 <= b.upper:
        raise ValueError("zero-containing divisor")
    reciprocal = save(name + "_reciprocal", "reciprocal", [b_name],
                      Box(1 / b.upper, 1 / b.lower))
    return multiply(name, a_name, a, name + "_reciprocal", reciprocal)


def outward_decimal(box, places=22):
    denominator = 10**places
    lo = box.lower.numerator * denominator // box.lower.denominator
    hi = -((-box.upper.numerator * denominator) // box.upper.denominator)

    def render(integer):
        sign = "-" if integer < 0 else ""
        integer = abs(integer)
        return f"{sign}{integer // denominator}.{integer % denominator:0{places}d}"

    result = {"lower": render(lo), "upper": render(hi)}
    assert Q(result["lower"]) <= box.lower <= box.upper <= Q(result["upper"])
    return result


def main():
    raw = SOURCE.read_bytes()
    data = json.loads(raw)
    panel = data["panels"][0]
    selected = {"lambda": panel["lambda"],
                "moments": {str(k): panel["moments"][str(k)] for k in (0, 2, 4, 6)}}
    parameter = Box(Q(selected["lambda"]["lower"]), Q(selected["lambda"]["upper"]))
    assert parameter.lower == 0 and parameter.upper == Q(1, 5120)
    moments = []
    gamma = []
    for j, k in enumerate((0, 2, 4, 6)):
        source_box = selected["moments"][str(k)]
        assert isinstance(source_box["lower"], str) and isinstance(source_box["upper"], str)
        moment = Box(Q(source_box["lower"]), Q(source_box["upper"]))
        assert moment.lower > 0
        moments.append(save(f"M{k}", "input", [f"/panels/0/moments/{k}"], moment))
        gamma.append(scale(f"gamma{j}", f"M{k}", moment, Q(factorial(j), factorial(k))))
    g0, g1, g2, g3 = gamma

    g1sq = square("gamma1_squared", "gamma1", g1)
    g0g2 = multiply("gamma0_gamma2", "gamma0", g0, "gamma2", g2)
    a = subtract("A", "gamma1_squared", g1sq, "gamma0_gamma2", g0g2)
    g2sq = square("gamma2_squared", "gamma2", g2)
    g1g3 = multiply("gamma1_gamma3", "gamma1", g1, "gamma3", g3)
    b = subtract("B", "gamma2_squared", g2sq, "gamma1_gamma3", g1g3)
    g1g2 = multiply("gamma1_gamma2", "gamma1", g1, "gamma2", g2)
    g0g3 = multiply("gamma0_gamma3", "gamma0", g0, "gamma3", g3)
    c = subtract("C", "gamma1_gamma2", g1g2, "gamma0_gamma3", g0g3)
    ab = multiply("AB", "A", a, "B", b)
    four_ab = scale("four_AB", "AB", ab, Q(4))
    c_squared = square("C_squared", "C", c)
    h = subtract("H", "four_AB", four_ab, "C_squared", c_squared)

    # C028s's audited identity supplies a separate consistency expression.
    # Its interval must not narrow the primary H enclosure.
    bs = [divide(f"b{j}", f"gamma{j}", gamma[j], "gamma0", g0) for j in (1, 2, 3)]
    b1, b2, b3 = bs
    b1sq = square("b1_squared", "b1", b1)
    v = subtract("v", "b1_squared", b1sq, "b2", b2)
    b1b2 = multiply("b1_b2", "b1", b1, "b2", b2)
    three_b1b2 = scale("three_b1_b2", "b1_b2", b1b2, Q(3))
    b1cube = multiply("b1_cubed", "b1_squared", b1sq, "b1", b1)
    two_b1cube = scale("two_b1_cubed", "b1_cubed", b1cube, Q(2))
    w_partial = subtract("w_partial", "b3", b3, "three_b1_b2", three_b1b2)
    w_double = add("twice_w", "w_partial", w_partial, "two_b1_cubed", two_b1cube)
    w = scale("w", "twice_w", w_double, Q(1, 2))
    vsq = square("v_squared", "v", v)
    vcube = multiply("v_cubed", "v_squared", vsq, "v", v)
    wsq = square("w_squared", "w", w)
    difference = subtract("v_cubed_minus_w_squared", "v_cubed", vcube, "w_squared", wsq)
    four_difference = scale("four_difference", "v_cubed_minus_w_squared", difference, Q(4))
    g0sq = square("gamma0_squared", "gamma0", g0)
    g0fourth = square("gamma0_fourth", "gamma0_squared", g0sq)
    h_secondary = multiply("H_secondary", "gamma0_fourth", g0fourth,
                           "four_difference", four_difference)
    overlap = max(h.lower, h_secondary.lower) <= min(h.upper, h_secondary.upper)
    failures = [] if overlap else ["algebraically compatible enclosures are disjoint"]
    positive = h.lower > 0
    status = "positive_lower_bound" if positive else (
        "negative_upper_bound_requires_audit" if h.upper < 0 else "inconclusive_zero_containment")
    certificate = {
        "step": "2026-11-20-saved-moment-propagation-1917",
        "status": status,
        "source": str(SOURCE.relative_to(ROOT)),
        "source_sha256": sha256(raw).hexdigest(),
        "python": platform.python_version(),
        "arithmetic": "fractions.Fraction; exact decimal strings; no float; no quadrature",
        "qualification": "Input inclusion relies on L917/audit197 and L037 Decimal-library contracts.",
        "selected_inputs": selected,
        "parameter_exact": parameter.record(),
        "trace": TRACE,
        "H": h.record(),
        "H_outward_decimal": outward_decimal(h),
        "H_secondary": h_secondary.record(),
        "secondary_overlap_only": overlap,
        "required_lower_bound": "0",
        "strict_positive_certified_subject_to_input_contracts": positive,
        "failures": failures,
    }
    OUTPUT.write_text(json.dumps(certificate, indent=2) + "\n")
    print(f"H outward bound: [{certificate['H_outward_decimal']['lower']}, "
          f"{certificate['H_outward_decimal']['upper']}]; required lower(H)>0")
    print(f"Result: {status}; consistency overlap: {overlap}; failures: {failures}")
    print(f"Certificate: {OUTPUT.relative_to(ROOT)}")
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
