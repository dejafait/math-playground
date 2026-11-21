"""Exact rate-gap certificate for L722; no sampled saddle is a premise."""
import ast
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path

helper = Path(__file__).with_name("spatial-complex-phase-166.py")
source = helper.read_text()
names = {"ceildiv", "fixed", "log_unit", "logq"}
definitions = [node for node in ast.parse(source).body
               if isinstance(node, ast.FunctionDef) and node.name in names]
assert {node.name for node in definitions} == names
ns = dict(F=F, SCALE=1 << 100, TERMS=40)
exec(compile(ast.Module(body=definitions, type_ignores=[]), str(helper), "exec"), ns)
ns["LOG2"] = ns["log_unit"](2, 1)
logq, scale = ns["logq"], ns["SCALE"]
d, U, A, p, beta, c = F(5, 4), F(121, 64), F(27, 10), F(3, 10), F(2, 5), F(1, 8)
s0, panels = F(73, 40), 64  # complex comparison point s0*(1-i)

def enc(value):
    value = F(value)
    return {"numerator": value.numerator, "denominator": value.denominator,
            "decimal_preview": float(value)}

def interval(values):
    return [enc(value) for value in values]

def saddle_squared(t):
    return (((d+p*t)**2+(beta*t)**2)*((U+s0*t)**2+(s0*t)**2)
            / (((U*p+d*t)**2+(U*beta)**2)*((s0+t)**2+s0**2)))

def residue_squared(t):
    return (((d+p*t)**2+(beta*t)**2)*((U*p+(d+c)*t)**2+(U*beta)**2)
            / (((U*p+d*t)**2+(U*beta)**2)*((d+c+p*t)**2+(beta*t)**2)))

def integrate_log_modulus(squared, fourth_bound):
    sums = [0, 0]
    rows = []
    for j in range(panels+1):
        t = F(j, panels)
        weight = 1 if j in (0, panels) else 4 if j % 2 else 2
        value = squared(t)
        logs = logq(value)
        rows.append({"j": j, "t": enc(t), "squared_modulus": enc(value),
                     "log_squared_modulus": interval(F(x, scale) for x in logs),
                     "weight": weight})
        for k in (0, 1):
            sums[k] += weight*logs[k]
    # Elementary two-cell cubic Taylor remainder, proved in L722.
    error = F(fourth_bound, 45*panels**4)
    bounds = [F(sums[0], 6*panels*scale)-error,
              F(sums[1], 6*panels*scale)+error]
    return bounds, rows, error

checks = {}
def check(name, actual, relation, required):
    actual, required = F(actual), F(required)
    passed = {"<": actual < required, ">": actual > required}[relation]
    checks[name] = {"actual": enc(actual), "relation": relation,
                    "required": enc(required), "passed": passed}

omega = [A*(F(logq(F(9, 5))[k], scale)-F(4, 5)
            +F(121, 100)*F(logq(F(201, 121))[k], scale)) for k in (0, 1)]
# |s0*(1-i)| < 3; all affine factors remain in the right half-plane.
check("comparison_point_modulus_squared", 2*s0**2, "<", 9)
check("saddle_fourth_derivative_bound",
      6*((F(1, 2)/d)**4+(d/(U/2))**4+(3/U)**4+F(5, 9)**4), "<", 100)
check("residue_fourth_derivative_bound",
      6*((F(1, 2)/d)**4+(d/(U/2))**4+((d+c)/(U/2))**4
         +(F(1, 2)/(d+c))**4), "<", 100)
check("phase_second_derivative_bound", F(25, 81)+1/(3*U**2), "<", F(1, 2))
check("omega_positive", omega[0], ">", 1)

saddle_integral, saddle_rows, saddle_error = integrate_log_modulus(saddle_squared, 100)
residue_integral, residue_rows, residue_error = integrate_log_modulus(residue_squared, 100)
linear = (p+beta)*s0-d
check("comparison_phase_linear_coefficient", linear, ">", 0)
comparison_rate = [saddle_integral[k]+linear*omega[k]/A for k in (0, 1)]
# Every point of L719's certified saddle rectangle is within squared
# distance 2*(1/40)^2=1/800 of the comparison point.
phase_loss = F(1, 2)*F(1, 2)*F(1, 800)
saddle_rate_lower = comparison_rate[0]-phase_loss
residue_rate_upper = residue_integral[1]+c*(omega[1]+F(1, 3000))/A
check("comparison_rate_lower", comparison_rate[0], ">", F(11, 2000))
check("saddle_rate_lower", saddle_rate_lower, ">", F(1, 200))
check("residue_rate_upper", residue_rate_upper, "<", F(1, 5000))
check("strict_rate_gap", saddle_rate_lower-residue_rate_upper, ">", F(3, 625))

result = {"purpose": __doc__, "arithmetic": "Exact fractions and outward fixed point 2^100",
          "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
          "helper_path": str(helper), "helper_sha256": hashlib.sha256(source.encode()).hexdigest(),
          "parameters": {"panels": panels, "comparison_s_real": enc(s0),
                         "comparison_s_imag": enc(-s0), "scale": scale},
          "bounds": {"omega": interval(omega), "saddle_integral": interval(saddle_integral),
                     "residue_integral": interval(residue_integral),
                     "comparison_rate": interval(comparison_rate), "phase_loss": enc(phase_loss),
                     "saddle_rate_lower": enc(saddle_rate_lower),
                     "residue_rate_upper": enc(residue_rate_upper),
                     "saddle_quadrature_error": enc(saddle_error),
                     "residue_quadrature_error": enc(residue_error)},
          "saddle_rows": saddle_rows, "residue_rows": residue_rows, "checks": checks,
          "failures": [name for name, row in checks.items() if not row["passed"]],
          "qualifications": ["L719's audited rectangle and phase identity are mathematical inputs.",
                             "L721 supplies the signed limsup, not this certificate.",
                             "No full limit, eventual nonvanishing, full-response or RH conclusion."]}
path = Path(__file__).with_suffix(".json")
path.write_text(json.dumps(result, indent=2)+"\n")
for name, row in checks.items():
    print(f"{name}: actual {row['actual']['decimal_preview']:.12g} {row['relation']} "
          f"required {row['required']['decimal_preview']:.12g}; pass={row['passed']}")
print("Failures:", result["failures"], "Full certificate:", path)
if result["failures"]:
    raise SystemExit(1)
