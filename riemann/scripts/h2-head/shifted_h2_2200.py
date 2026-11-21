"""Frozen onset-4/cutoff-100 rational comparison; no zero computation."""
from decimal import Decimal, localcontext
from fractions import Fraction as F
import json
from pathlib import Path
import platform


def exact(q):
    q = F(q)
    return {"numerator": str(q.numerator), "denominator": str(q.denominator)}


def display(q):
    with localcontext() as ctx:
        ctx.prec = 24
        return str(Decimal(q.numerator) / Decimal(q.denominator))


def main():
    cutoff, onset = 100, 4
    selected_upper = F(51, 2)
    beta_lower = selected_upper ** -2
    gram_denominator_cap = 700000000
    head = beta_lower ** (2 * onset) / gram_denominator_cap
    components = [F(1), F(200**2, cutoff**4), F(40000**2, cutoff**8)]
    vector_factor = sum(components, F(0))
    power = 4 * onset + 4
    # L467: 18 log(n+2); log(n+2)<=n, n>=100.
    # For p=power-1>1: sum n^-p <=100^-p + int_100^inf x^-p dx.
    shell_power = power - 1
    first_shell = F(1, cutoff**shell_power)
    integral = F(1, (shell_power - 1) * cutoff**(shell_power - 1))
    shell_sum_upper = first_shell + integral
    exterior = 18 * vector_factor * shell_sum_upper
    difference = head - exterior
    head_step = beta_lower**2
    tail_step = F(1, cutoff**4)
    relative_step = tail_step / head_step
    checks = {
        "frozen_parameters": (cutoff, onset) == (100, 4),
        "gram_weights_positive": beta_lower > 0,
        "summation_exponent_gt_one": shell_power > 1,
        "component_identity": vector_factor == F(6252501, 6250000),
        "complete_tail_budget_positive": exterior > 0,
        "strict_onset_separation": difference > 0,
        "all_integer_shifts_ratio": 0 < relative_step < 1,
        "ratio_identity": relative_step == F(51, 200)**4,
    }
    failures = [name for name, ok in checks.items() if not ok]
    cert = {
        "target": "H_(2,r) positive definite for every integer r>=4",
        "parameters": {"cutoff": cutoff, "onset": onset, "D": [1, 200, 40000]},
        "arithmetic": {"python": platform.python_version(), "proof_values": "CPython int/Fraction; Decimal display only"},
        "inputs": ["L018", "L024", "L025", "L030", "L467", "L058", "C919e", "C919f", "Platt2017 Theorem5.1"],
        "selected_x_upper": exact(selected_upper),
        "beta_lower": exact(beta_lower),
        "head_lower_r4": exact(head),
        "tail_vector_component_bounds": [exact(q) for q in components],
        "tail_vector_factor": exact(vector_factor),
        "shell_exponents": {"zero_power": power, "after_log_bound": shell_power},
        "first_shell_after_log": exact(first_shell),
        "integral_after_log": exact(integral),
        "shell_sum_upper": exact(shell_sum_upper),
        "complete_tail_upper_r4": exact(exterior),
        "required_head_minus_tail": exact(F(0)),
        "actual_head_minus_tail": exact(difference),
        "strict_integer_cross_product": str(head.numerator * exterior.denominator - exterior.numerator * head.denominator),
        "head_over_tail": exact(head / exterior),
        "all_r": {
            "k": "arbitrary integer r-4>=0; not a finite sample",
            "head_multiplier": "head_step^k",
            "tail_multiplier": "tail_step^k",
            "head_step": exact(head_step),
            "tail_step": exact(tail_step),
            "relative_step": exact(relative_step),
            "conclusion": "h_r-t_r >= head_step^k * (h4-t4)>0; requires analytic bounds in C919h",
        },
        "checks": checks,
        "failures": failures,
        "limits": "Rational specialization only; no independent source/placement audit, no all-degree or RH conclusion.",
    }
    destination = Path(__file__).with_suffix(".json")
    destination.write_text(json.dumps(cert, indent=2) + "\n")
    print(f"head_lower_r4={display(head)}; complete_tail_upper_r4={display(exterior)}")
    print(f"actual head-tail={display(difference)}; required>0; head/tail={display(head/exterior)}")
    print(f"all-r tail/head step={relative_step}<1; failures={failures}")
    print(f"certificate={destination.relative_to(Path.cwd())}")
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
