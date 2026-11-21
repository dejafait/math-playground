"""Independent exact reconstruction of C919h; does not execute its generator."""
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import platform


BASE = Path(__file__).resolve().parent
SOURCE = BASE / "shifted_h2_2200.json"


def encode(q):
    q = F(q)
    return {"numerator": str(q.numerator), "denominator": str(q.denominator)}


def main():
    original_bytes = SOURCE.read_bytes()
    saved = json.loads(original_bytes)
    checks = {}
    reconstructed = {}

    def compare(key, value):
        reconstructed[key] = value
        checks["saved_" + key] = saved[key] == value

    # Reconstruct from x_max=51/2, w_i=200^i alpha^(-2i-2),
    # Gram floor=1/700000000 and shell count=18 log(n+2).
    scale = [200**i for i in range(3)]
    b = F(2, 51)**2
    h = F(2, 51)**16 / 700000000
    components = [F(scale[i]**2, 100**(4*i)) for i in range(3)]
    # Summing three component budgets separately also checks the factoring.
    first = F(1, 100**19)
    integral = F(1, 18 * 100**18)
    tail_terms = [18 * a * (first + integral) for a in components]
    t = sum(tail_terms, F(0))
    cross = h.numerator * t.denominator - t.numerator * h.denominator
    head_step = F(2, 51)**4
    tail_step = F(1, 100)**4
    ratio = F(51, 200)**4

    compare("parameters", {"cutoff": 100, "onset": 4, "D": scale})
    for key, q in {
        "selected_x_upper": F(51, 2), "beta_lower": b,
        "head_lower_r4": h, "tail_vector_factor": sum(components, F(0)),
        "first_shell_after_log": first, "integral_after_log": integral,
        "shell_sum_upper": first + integral, "complete_tail_upper_r4": t,
        "required_head_minus_tail": F(0), "actual_head_minus_tail": h-t,
        "head_over_tail": h/t,
    }.items():
        compare(key, encode(q))
    compare("tail_vector_component_bounds", [encode(a) for a in components])
    compare("shell_exponents", {"zero_power": 20, "after_log_bound": 19})
    compare("strict_integer_cross_product", str(cross))
    for key, q in {"head_step": head_step, "tail_step": tail_step,
                   "relative_step": ratio}.items():
        reconstructed["all_r/" + key] = encode(q)
        checks["saved_all_r_" + key] = saved["all_r"][key] == encode(q)

    checks["positive_denominators"] = h.denominator > 0 and t.denominator > 0
    checks["positive_tail"] = t > 0
    checks["strict_cross_product"] = cross > 0
    checks["strict_head_minus_tail"] = h-t > 0
    checks["tail_step_factorization"] = tail_step == head_step * ratio
    checks["positive_head_step"] = head_step > 0
    checks["uniform_ratio_between_zero_and_one"] = 0 < ratio < 1
    checks["original_all_eight_checks_true"] = (
        len(saved["checks"]) == 8 and all(v is True for v in saved["checks"].values())
    )
    checks["original_failures_empty"] = saved["failures"] == []
    failures = [name for name, value in checks.items() if not value]
    report = {
        "source_certificate": str(SOURCE.relative_to(Path.cwd())),
        "source_sha256": hashlib.sha256(original_bytes).hexdigest(),
        "source_generator_sha256": hashlib.sha256(
            (BASE / "shifted_h2_2200.py").read_bytes()).hexdigest(),
        "arithmetic_contract": "Correct CPython int/Fraction; no Decimal or original generator used",
        "runtime": {"implementation": platform.python_implementation(), "version": platform.python_version()},
        "reconstructed": reconstructed,
        "component_tail_budgets": [encode(q) for q in tail_terms],
        "bounds": {"actual_head": encode(h), "actual_tail": encode(t),
                   "actual_difference": encode(h-t), "required_difference": "strictly >0",
                   "all_r_ratio": encode(ratio), "required_ratio": "0<ratio<1"},
        "checks": checks, "failures": failures,
        "scope": "Exact certificate audit only. Occurrence accounting, analytic convergence and arbitrary integer shifts require the canonical C919h audit proof. Inherited C919f backend contracts retained.",
    }
    destination = BASE / "shifted_h2_audit_2202.json"
    destination.write_text(json.dumps(report, indent=2) + "\n")
    print(f"head={h}; tail={t}")
    print(f"actual cross-product={cross}; required>0")
    print(f"all-r ratio={ratio}; required 0<ratio<1")
    print(f"checks={len(checks)}; failures={failures}")
    print(f"certificate={destination.relative_to(Path.cwd())}")
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
