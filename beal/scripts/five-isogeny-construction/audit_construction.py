"""Independent exact, degree-bounded audit of the arithmetic in L033.

Uses integer evaluation plus explicit polynomial degree bounds, not the
construction's polynomial implementation. Twenty distinct exact zeros prove
each asserted polynomial identity of degree at most nineteen.
"""
from fractions import Fraction as Q
from pathlib import Path
import json

ROOT = Path(__file__).parent
old = json.loads((ROOT / "construction-certificate.json").read_text())
N = [-324599, 170498, -30420, 2163, -42, 1]
D = [6400, -3360, 601, -42, 1]
H = [534560, 791998, 372028, 9668, -33811, -3084, 1404, -84, 1]


def at(cs, x):
    return sum(c*x**i for i, c in enumerate(cs))


def deriv_at(cs, x):
    return sum(i*c*x**(i-1) for i, c in enumerate(cs) if i)


def product(u, v, cubic):
    # In Q[y]/(y^2+y-cubic), at a fixed integer x.
    a, b = u
    c, d = v
    return a*c+b*d*cubic, a*d+b*c-b*d


rows = []
for x in range(20, 40):
    cubic = x**3-x*x-10*x-20
    den = (x-5)**2*(x-16)**2
    num = (x*den + 110*(x-5)*(x-16)**2 + 121*(x-16)**2
           + 1452*(x-16)*(x-5)**2 + 14641*(x-5)**2)
    hn = deriv_at(N, x)*at(D, x)-at(N, x)*deriv_at(D, x)
    a, b = -4*x*x+30*x-55, x-4
    lt, l2 = (20-5*x, 1), (6*x-35, 1)
    mc, my = product(product(lt, lt, cubic), l2, cubic)
    rows.append({
        "x": x,
        "D_residual": at(D, x)-den,
        "N_residual": at(N, x)-num,
        "H_residual": at(H, x)-hn,
        "quotient_residual": (4*cubic+1)*hn**2
          -(4*num**3*den-4*num**2*den**2-31280*num*den**3-1054319*den**4),
        "miller_constant_residual": mc-(x-16)**2*a,
        "miller_y_residual": my-(x-16)**2*b,
        "norm_residual": a*a-a*b-cubic*b*b+(x-5)**5,
        "T_line_residual": (5*x-20)**2+(5*x-20)-cubic+(x-5)**2*(x-16),
        "twoT_line_residual": (-6*x+35)**2+(-6*x+35)-cubic+(x-16)**2*(x-5),
    })

# Bounds before cancellation, for each polynomial tested above.
bounds = {"D_residual": 4, "N_residual": 5, "H_residual": 8,
          "quotient_residual": 19, "miller_constant_residual": 6,
          "miller_y_residual": 6, "norm_residual": 5,
          "T_line_residual": 3, "twoT_line_residual": 3}
identity_checks = {k: len(rows) > degree and all(r[k] == 0 for r in rows)
                   for k, degree in bounds.items()}

pts = [None, (Q(5), Q(5)), (Q(16), Q(-61)), (Q(16), Q(60)), (Q(5), Q(-6))]


def plus(p, q):
    if p is None:
        return q
    if q is None:
        return p
    x, y = p
    u, v = q
    if x == u and y+v == -1:
        return None
    m = (3*x*x-2*x-10)/(2*y+1) if p == q else (v-y)/(u-x)
    # Third intersection with the line; reflect to obtain the sum.
    rx = 1+m*m-x-u
    return rx, -1-y-m*(rx-x)


def f(p):
    x, y = p
    return (x-4)*y-4*x*x+30*x-55


addition = [{"i": i, "j": j, "matches": plus(p, q) == pts[(i+j) % 5]}
            for i, p in enumerate(pts) for j, q in enumerate(pts)]
exceptions = []
for n, r, fifth_root in [(0, 2, 1), (1, 2, -1), (2, 2, 1),
                          (3, 4, 11), (4, 3, -11)]:
    endpoint = (n+r) % 5
    good = r not in (0, 1) and endpoint not in (0, 1)
    value = f(pts[endpoint])/f(pts[r])
    exceptions.append({"n": n, "shift": r, "good": good,
                       "ratio": str(value), "expected_class": str(Q(1, 11**n)),
                       "fifth_root_of_ratio_to_expected_class": fifth_root,
                       "class_matches": value*11**n == fifth_root**5})

invariants = []
for a4, a6 in [(-10, -20), (-7820, -263580)]:
    c4 = 16-48*a4
    c6 = 64-288*a4-216*(1+4*a6)
    discriminant = Q(c4**3-c6**2, 1728)
    invariants.append({"c4": c4, "c6": c6, "discriminant": str(discriminant)})

checks = dict(identity_checks)
checks.update({
    "on_curve": all(y*y+y == x**3-x*x-10*x-20 for x, y in pts[1:]),
    "all_25_additions": all(r["matches"] for r in addition),
    "all_five_good_divisors": all(r["good"] and r["class_matches"] for r in exceptions),
    "coprime_N_D_and_degree": len(N)-1 == 5 and len(D)-1 == 4
        and at(N, 5) != 0 and at(N, 16) != 0,
    "discriminants": [r["discriminant"] for r in invariants] == [str(-11**5), "-11"],
    "old_coefficients_match": all([str(v) for v in values] == old["quotient"][key]
        for key, values in [("x_numerator", N), ("x_denominator", D), ("derivative_numerator", H)]),
    "old_torsion_values_match": [str(f(p)) for p in pts[1:]] == old["f"]["torsion_values"],
    "old_exceptional_ratios_match": [r["ratio"] for r in exceptions[1:]] == old["f"]["exceptional_ratios"],
})
cert = {"method": "Exact integer zeros with proven polynomial degree bounds; rational chord arithmetic",
        "checks": checks, "failures": [k for k, v in checks.items() if not v],
        "identity_degree_bounds": bounds, "evaluations": rows,
        "threshold": {"actual_distinct_nodes": 20, "required_nodes": 20, "maximum_degree": 19},
        "actual_order": 5 if checks["all_25_additions"] and checks["on_curve"] else None,
        "required_order": 5, "actual_map_degree": 5 if checks["coprime_N_D_and_degree"] else None,
        "required_map_degree": 5, "addition_table": addition, "exceptional_divisors": exceptions,
        "invariants": invariants, "N_at_kernel_x": {str(x): at(N, x) for x in (5, 16)},
        "structural_checks": "See L033: degree, divisors, dual pairing, unramified classes and FNS transport are proof/source checks, not certified by this script.",
        "not_computed": ["S-unit basis", "class group", "local images", "branch emptiness"]}
path = ROOT / "audit-certificate.json"
path.write_text(json.dumps(cert, indent=2)+"\n")
print(f"checks {sum(checks.values())}/{len(checks)}; failures {cert['failures']}")
print("distinct exact zeros actual=20 required=20; maximum polynomial degree=19")
print(f"order actual={cert['actual_order']} required=5; map degree actual={cert['actual_map_degree']} required=5")
print("all 25 additions and 5 exceptional divisors checked; classes/local images/emptiness not computed")
print(path)
if cert["failures"]:
    raise SystemExit(1)
