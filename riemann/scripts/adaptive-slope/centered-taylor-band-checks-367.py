"""Exact scalar certificate for C997r; not a numerical asymptotic proof."""
from fractions import Fraction as F
import json
from pathlib import Path


checks = {}


def check(name, actual, relation, required):
    passed = {">": actual > required, "<": actual < required,
              "=": actual == required, ">=": actual >= required}[relation]
    checks[name] = {"actual": str(actual), "relation": relation,
                    "required": str(required), "passed": passed}


check("exp_5_06_upper", F(11, 4)**5 * F(50, 47), "<", F(168))
check("rho_positive_margin", F(3, 50)/24, "=", F(1, 400))
check("e_series_upper", F(5, 2)+F(2, 9), "<", F(11, 4))
theta_min = F(1, 32)-F(1, 8192)
check("window_modulus_floor", theta_min-theta_min**3/24, ">", F(31, 1000))
check("upper_theta", F(1, 32)+F(17, 16*32768), "<", F(1, 16))
check("moving_c_lower", F(17, 8)-F(16, 32768), ">", F(53, 25))
ratio = F(1, 24)/(F(7, 2)*F(31, 1000))
check("previous_term_ratio", ratio, "=", F(250, 651))
check("tail_disk_radius", ratio/(1-ratio), "=", F(250, 401))
check("tail_modulus_floor", 1-F(250, 401), "=", F(151, 401))
check("sine_disk_angle_margin", F(7, 10)-F(7, 10)**3/6, ">", F(250, 401))
check("carrier_phase_lower", F(15, 4)*F(53, 25), ">", F(79, 10))
check("carrier_phase_upper", (F(15, 4)+F(1, 96))*F(17, 8), "<", F(8))
check("phase_lower", F(79, 10)-F(14, 10), "=", F(13, 2))
check("phase_upper", F(8)+F(14, 10), "=", F(47, 5))
check("distance_above_2pi", F(13, 2)-F(44, 7), ">", F(1, 50))
check("distance_below_3pi", 3*F(157, 50)-F(47, 5), "=", F(1, 50))
check("phase_sine_floor", F(1, 50)-F(1, 50)**3/6, ">", F(1, 100))
check("bulk_phase_derivative_squared", F(15, 68), ">", F(4, 25))
check("peak_phase_length", F(32, 5), ">", F(44, 7))
check("weighted_growth_rate", F(17, 8)/8-F(1, 4), "=", F(1, 64))
check("moving_point_exponent_loss", F(16, 8), "=", F(2))

failures = [key for key, value in checks.items() if not value["passed"]]
certificate = {
    "step": "2026-11-11-centered-taylor-band-obstruction-367",
    "scope": "Exact rational margins only; C997r supplies the all-n proof and imported uniform bulk theorem.",
    "checks": checks,
    "thresholds": {
        "required_tv": "subexponential in n for the same measures",
        "actual_high_order_tv_lower": "7 exp(rho*n)/(10 e n), rho=(log168-5)/24>1/400, m>=n/24",
        "required_defect": "O(exp(-n/64))",
        "actual_low_order_defect_lower": "c n^(-3/2) exp(n/64), m<n/24, eventually uniformly in m",
        "boundary": "Retained; not estimated, since TV or complete D already violates simultaneous admissibility.",
        "full_grid_family": "Unresolved; only the fixed centered Taylor rule is excluded."
    },
    "failures": failures,
    "passed": not failures,
}
output = Path(__file__).with_suffix(".json")
output.write_text(json.dumps(certificate, indent=2)+"\n")
print(f"Exact scalar checks: {len(checks)-len(failures)}/{len(checks)} passed; failures={failures}")
print("Actual bounds: TV >= 7 exp(rho*n)/(10 e n), rho>1/400; or d >= c n^(-3/2) exp(n/64).")
print("Required bounds: subexponential TV and d=O(exp(-n/64)); Taylor subclass only.")
print(f"Certificate: {output.relative_to(Path.cwd())}")
raise SystemExit(bool(failures))
