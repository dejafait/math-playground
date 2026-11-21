#!/usr/bin/env python3
"""Audit the saved L923 evidence; no theta integration or sign search."""
from fractions import Fraction as F
from hashlib import sha256
from itertools import product
from math import factorial
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[2]
OLD = ROOT / "scripts/heat/weighted-cubic-floor-222.json"
MASS = ROOT / "scripts/heat/low-time-h2-uniform-195.json"
OUT = ROOT / "scripts/heat/weighted-cubic-audit-224.json"
old = json.loads(OLD.read_bytes())
mass = json.loads(MASS.read_bytes())
checks = {}


def check(name, condition):
    checks[name] = bool(condition)


def terms(text):
    """Parse the producer's explicit rational monomial serialization."""
    out = {}
    for term in text.split(" + "):
        pieces = term.split("*")
        coeff = F(pieces[0])
        powers = {}
        for factor in pieces[1:]:
            name, _, power = factor.partition("^")
            powers[name] = powers.get(name, 0) + int(power or "1")
        key = tuple(sorted(powers.items()))
        out[key] = out.get(key, F(0)) + coeff
    return {k: v for k, v in out.items() if v}


def evaluate(polynomial, point):
    return sum(coeff * product_value(point[name] ** power for name, power in key)
               for key, coeff in polynomial.items())


def product_value(values):
    ans = F(1)
    for val in values:
        ans *= val
    return ans


check("source_hash", old["source"]["sha256"] == sha256(MASS.read_bytes()).hexdigest())
check("source_path", old["source"]["path"] == str(MASS.relative_to(ROOT)))
check("producer_passed", old["status"] == "passed" and old["failures"] == []
      and len(old["checks"]) == 281 and all(old["checks"].values()))
records = old["source"]["all_mass_records"]
check("all_256_panels", len(records) == len(mass["panels"]) == 256)
full_mass_checks = []
for i, (record, panel) in enumerate(zip(records, mass["panels"])):
    interval = [F(i, 5120), F(i + 1, 5120)]
    mlo, mhi = [F(panel["moments"]["0"][s]) for s in ("lower", "upper")]
    ok = (record["index"] == panel["index"] == i
          and list(map(F, record["lambda"])) == interval
          and [F(panel["lambda"][s]) for s in ("lower", "upper")] == interval
          and F(record["mass_lower"]) == mlo and F(record["mass_upper"]) == mhi
          and 0 < mlo <= mhi < F(499, 1000) < F(1, 2))
    full_mass_checks.append(ok)
check("every_complete_mass_endpoint", all(full_mass_checks))
maximum = max(range(256), key=lambda i: F(records[i]["mass_upper"]))
maxval = F(records[maximum]["mass_upper"])
check("maximum", maximum == old["source"]["maximum_upper_index"] == 255
      and maxval == F(old["source"]["maximum_upper"]) < F(498274, 1000000)
      and F(old["source"]["required_mass_upper"]) == F(1, 2))
pilo, pihi = [F(mass["pi"][s]) for s in ("lower", "upper")]
check("pi_endpoints", list(map(F, old["source"]["pi"])) == [pilo, pihi]
      and 3 < pilo < pihi < 4)


def exponential_bounds(x):
    # Reconstruct all terms directly, independently of producer's recurrence.
    partial = sum(x**j / factorial(j) for j in range(101))
    return partial, partial + x**101 / factorial(101) / (1 - x / 102)


exps = {}
for name, x in [("e", F(1)), ("exp_167_over_20", F(167, 20)), ("exp_5_over_2", F(5, 2))]:
    pair = exponential_bounds(x)
    exps[name] = pair
    check("full_exponential_" + name, list(pair) == list(map(F, old["exponentials"][name])))
check("kernel_scalar_bounds", pilo * exps["e"][0] > F(17, 2)
      and pihi * exps["e"][1] < F(43, 5) and exps["exp_167_over_20"][1] < 4500)
check("gaussian_scalar_bound", exps["exp_5_over_2"][1] < 15)
floor = old["floor"]
ell = F(3, 16)
epsilon = ell**7 / (40 * 2800)
check("complete_floor_record", floor == {
    "kernel_at_half_lower": str(F(476, 4500)), "weighted_density_lower": "1/40",
    "interval_length": str(ell), "monic_cubic_lebesgue_minimum": str(ell**7 / 2800),
    "epsilon": str(epsilon)})
check("actual_floor_threshold", F(119, 4500) > F(1, 40)
      and epsilon == F(2187, 30064771072000) > F(727, 10**13))

# Exact tensor-grid identity certificate. Every expression below has separate
# degrees at most (2,4,2,2,1) in (p,q,b,r,h). All 270 grid nodes therefore
# determine it; no sampling or generic-random-polynomial argument is used.
algebra = old["algebra"]
beta_poly = terms(algebra["B_divided_by_c2_squared"])
flux_poly = terms(algebra["flux_divided_by_c2_squared"])
s_polys = [terms(z) for z in algebra["S4_S5_S6"]]
bn_polys = [terms(z) for z in algebra["b2_through_b6"]]
degree_bounds = dict(p=2, q=4, b=2, r=2, h=1, s7=1)
check("saved_degree_bounds", all(name in degree_bounds and power <= degree_bounds[name]
      for pol in [beta_poly, flux_poly, *s_polys, *bn_polys] for key in pol for name, power in key))
check("separate_s7_term", flux_poly.get((("s7", 1),)) == -156
      and {k: v for k, v in flux_poly.items() if k != (("s7", 1),)} == beta_poly)
grid_failures = []
for p, q, b, r, h in product(range(3), range(5), range(3), range(3), range(2)):
    point = dict(p=F(p), q=F(q), b=F(b), r=F(r), h=F(h), s7=F(0))
    c = [F(p), F(q), F(1)]
    s = [F(0), F(h), F(b), F(r), -p*b-q*r,
         p*q*b+(q*q-p)*r, (p*p-p*q*q)*b+(2*p*q-q**3)*r, F(0)]
    ds = {n: -2*n*(2*n+1)*s[n+1] + 4*n*sum(s[a]*s[n+1-a] for a in range(1,n+1))
          for n in range(2, 7)}
    flux = sum(c[i]*c[j]*ds[i+j+2] for i in range(3) for j in range(3))
    beta = (-280*p*p*q*b+124*p*p*r+148*p*q**3*b-428*p*q*q*r
            -8*p*q*b*b-32*p*b*r+148*q**4*r-8*q*r*r)
    ok = (flux == beta == evaluate(beta_poly, point)
          and all(sum(c[j]*s[i+j+2] for j in range(3)) == 0 for i in range(3))
          and [evaluate(z, point) for z in s_polys] == s[4:7]
          and [evaluate(z, point) for z in bn_polys] == [p*p,2*p*q,q*q+2*p,2*q,1])
    if not ok:
        grid_failures.append([p,q,b,r,h])
check("complete_identity_grid", not grid_failures)
check("saved_null_rows", algebra["all_null_rows"] == ["0", "0", "0"])
check("seventh_flux_factor", F(156*7, factorial(14)) == F(6, factorial(12)))

# Independently expand -7[t^7]log(1+sum q_j t^j) by multiplicity partitions.
log7 = {}
for mult in product(*(range(7//j+1) for j in range(1,8))):
    if sum(j*m for j,m in enumerate(mult,1)) != 7:
        continue
    k = sum(mult)
    coefficient = F(-7 * (-1)**(k+1) * factorial(k-1), product_value(factorial(m) for m in mult))
    coefficient *= product_value(F((-1)**j, factorial(2*j))**m for j,m in enumerate(mult,1))
    key = tuple((f"y{j}",m) for j,m in enumerate(mult,1) if m)
    log7[key] = coefficient
check("complete_seventh_log_polynomial", log7 == terms(algebra["S7_raw"]))
check("seventh_moment_sign", log7[(("y7",1),)] == F(7,factorial(14)))

# Direct integration-by-parts moment recurrence, with no matrix inversion code.
g = old["diagnostic"]
y = [F(1)]
for j in range(1,8):
    y.append(y[-1]*F(2*j-1,20))
pc = [F(-21,1600),F(21,80),F(-21,20),F(1)]
orth = [sum(pc[j]*y[j+i+1] for j in range(4)) for i in range(3)]
norm = sum(pc[i]*pc[j]*y[i+j+1] for i in range(4) for j in range(4))
projection = -sum(pc[i]*y[i+4] for i in range(3))
qraw = [(-1)**j * y[j]/factorial(2*j) for j in range(8)]
sg = [F(0)]
for n in range(1,8):
    sg.append(-n*qraw[n]-sum(sg[k]*qraw[n-k] for k in range(1,n)))
T = F(factorial(14),7)*sum(sg[k]*qraw[7-k] for k in range(1,7))
check("gaussian_moments_and_rows", list(map(F,g["moments_0_through_7"])) == y
      and list(map(F,g["S1_through_S7"])) == sg[1:] == [F(1,40),0,0,0,0,0,0]
      and g["c"] == [0,0,1])
check("gaussian_full_block", [[F(z) for z in row] for row in g["W"]]
      == [[y[i+j+1] for j in range(3)] for i in range(3)] and list(map(F,g["v"])) == y[4:7])
check("gaussian_minimizer", terms(g["monic_minimizer"]) == terms(
    "-21/1600*x^0 + 21/80*x^1 + -21/20*x^2 + 1*x^3")
      and orth == list(map(F,g["orthogonality"])) == [0,0,0])
check("gaussian_exact_comparison", norm == F(63,16000000)
      == F(g["actual_norm"]) == F(g["required_norm"]) == T-projection
      and projection == F(g["projection"]) == F(26019,256000000)
      and T == y[7] == F(27027,256000000) and F(g["flux"]) == 0)
check("gaussian_density", F(g["Z_upper"]) == F(129,260) < F(1,2)
      and F(g["weighted_density_lower"]) == F(1,30) > F(1,40))
check("gaussian_floor_gap", F(g["fixed_floor"]) == epsilon
      and F(g["unpaid_floor_gap"]) == norm-epsilon == F(14797231137,3758096384000000)
      and F(g["required_over_floor"]) == norm/epsilon == F(1644167168,30375) > 54000)

failures = [name for name, ok in checks.items() if not ok]
result = {
    "status": "passed" if not failures else "failed", "checks": checks, "failures": failures,
    "inputs": {str(p.relative_to(ROOT)): sha256(p.read_bytes()).hexdigest() for p in (OLD,MASS)},
    "mass_endpoint_checks": full_mass_checks,
    "mass": {"maximum_panel": maximum, "complete_maximum": str(maxval), "required_upper": "1/2"},
    "exact_scalar_enclosures": {k: list(map(str,v)) for k,v in exps.items()},
    "identity": {"grid_size": 270, "degree_bounds": degree_bounds, "grid_failures": grid_failures,
                 "S7_multinomial_coefficients": {str(k): str(v) for k,v in log7.items()}},
    "comparison": {"actual_theta_norm_floor": str(epsilon), "required_actual_theta_D_upper": "unpaid",
                   "gaussian_norm_and_D": str(norm), "gaussian_flux": "0", "gaussian_ratio": str(norm/epsilon)},
    "qualification": "Finite evidence audit plus canonical analytic argument; L917 arithmetic and exponential library contract retained. No new moment evaluation or actual sign test."
}
OUT.write_text(json.dumps(result, indent=2)+"\n")
print("status:", result["status"], "; audit checks:",len(checks), "; failures:",failures)
print("mass: all 256 complete records checked; maximum <0.498274, required <0.5")
print("algebra: 270 exact determining nodes; complete S7 coefficients checked")
print("actual floor:",epsilon,"; actual D upper: unpaid; diagnostic D:",norm,"; flux: 0")
print("certificate:",OUT.relative_to(ROOT))
if failures:
    raise SystemExit(1)
