"""Independent complete replay of L068; imports no construction code."""
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
raw = (HERE / "order-certificate.json").read_bytes()
old = json.loads(raw)
checks = {}

def check(name, condition):
    checks[name] = bool(condition)

# Integer coefficients transcribed from L033, before any reduction.
a1, a2, a3, a4, a6 = 0, -1, 1, -7820, -263580
b2 = a1*a1 + 4*a2
b4 = 2*a4 + a1*a3
b6 = a3*a3 + 4*a6
b8 = a1*a1*a6 + 4*a2*a6 - a1*a3*a4 + a2*a3*a3 - a4*a4
c4, c6 = b2*b2-24*b4, -b2**3+36*b2*b4-216*b6
disc_numerator = c4**3-c6**2
check("discriminant_division_exact", disc_numerator % 1728 == 0)
disc = disc_numerator // 1728
invariants = dict(b2=b2,b4=b4,b6=b6,b8=b8,c4=c4,c6=c6,discriminant=disc)
check("all_invariants_match", invariants == old["invariants"])
check("smooth_over_algebraic_closure", disc == -11 and disc % 13 != 0)

# Completing the square supplies an independent form of the residual.
# 4*(y^2+y-rhs) = (2*y+1)^2 - (4*rhs+1).
table, points, singular = [], [], []
for x in range(13):
    rhs = x**3 + a2*x*x + a4*x + a6
    residues = [((2*y+1)**2-(4*rhs+1))*10 % 13 for y in range(13)]
    solutions = [y for y,r in enumerate(residues) if r == 0]
    table.append(dict(x=x,equation_residues_y_0_through_12=residues,solutions=solutions))
    points.extend([[x,y] for y in solutions])
    for y in solutions:
        if (2*y+1) % 13 == 0 and (3*x*x-2*x-7820) % 13 == 0:
            singular.append([x,y])
check("all_169_residues_and_solution_lists", table == old["enumeration"])
check("complete_affine_points", points == old["affine_points"])
check("all_affine_singular_points", singular == old["singular_affine_points"] == [])

# Normalize all projective points at infinity: [1:y:0] and [0:1:0].
infinity = [[1,y,0] for y in range(13)] + [[0,1,0]]
origin_points = [v for v in infinity if (-v[0]**3) % 13 == 0]
check("unique_projective_origin", origin_points == [old["projective_origin"]] == [[0,1,0]])
# F_Z = Y^2+2YZ+X^2+15640XZ+790740Z^2 at the origin is 1.
origin_gradient = [0,0,1]
N1 = len(points)+len(origin_points)
t = 13+1-N1
check("projective_base_order_and_trace", N1 == old["base_order"] == 10 and t == old["frobenius_trace"] == 4)

# Linear multiplication, independent of the original binary matrix powering.
M = [[t,-13],[1,0]]
powers = [[[1,0],[0,1]]]
for n in range(12):
    A = powers[-1]
    powers.append([[sum(A[i][k]*M[k][j] for k in range(2)) for j in range(2)] for i in range(2)])
traces = [A[0][0]+A[1][1] for A in powers]
# Also power the class u in Z[u]/(u^2-4u+13) directly.
# Trace(a+b*u)=2a+t*b; multiply by u via (a,b)->(-13b,a+tb).
quotient_powers, sums = [], []
a,b = 1,0
for n in range(13):
    quotient_powers.append([a,b])
    sums.append(2*a+t*b)
    a,b = -13*b,a+t*b
check("companion_matrix", M == old["companion_matrix"])
check("all_thirteen_full_matrix_powers", powers == old["binary_matrix_powers_n_0_through_12"])
check("all_quotient_traces", sums == traces == old["matrix_traces"] == old["power_sums_n_0_through_12"])
check("scalar_recurrence", sums[:2] == [2,4] and all(sums[n] == 4*sums[n-1]-13*sums[n-2] for n in range(2,13)))
orders = [1+13**n-sums[n] for n in range(1,13)]
check("all_twelve_extension_counts", orders == old["orders_n_1_through_12"])
N = orders[-1]
check("full_field_order", N == old["extension_order"] == 23298078211200)
check("exact_divisibility", N == 13*1792159862400 and N % 13 == old["remainder_mod_13"] == 0)
check("trace_mod_thirteen", sums[-1] % 13 == pow(4,12,13) == 1)
check("failed_premise_record", old["bruin_order_hypothesis"] == dict(required_remainder="1 through 12",actual_remainder=0,holds=False))
check("model_and_full_degree", old["model"] == "Y^2+Y=X^3-X^2-7820X-263580" and old["prime"] == 13 and old["extension_degree"] == 12)
check("original_check_records", len(old["checks"]) == 10 and all(old["checks"].values()) and old["failures"] == [])

failures = [name for name,ok in checks.items() if not ok]
out = dict(original_sha256=hashlib.sha256(raw).hexdigest(),
           model_coefficients=[a1,a2,a3,a4,a6], invariants=invariants,
           enumeration=table, affine_points=points, singular_affine_points=singular,
           all_normalized_infinity_candidates=infinity, infinity_points=origin_points,
           origin_gradient=origin_gradient, base_order=N1, trace=t,
           quotient_powers=quotient_powers, linear_matrix_powers=powers,
           power_sums=sums, extension_orders=orders, full_residue_degree=12,
           extension_order=N, required_remainder="1 through 12", actual_remainder=N%13,
           bruin_order_premise_holds=False, checks=checks, failures=failures)
path = HERE / "audit-certificate.json"
path.write_text(json.dumps(out,indent=2)+"\n")
print(f"Audit: {len(checks)-len(failures)}/{len(checks)} checks pass; failures: {failures}")
print(f"Projective orders: N1={N1}, N12={N}; actual remainder={N%13}, required=1 through 12")
print(f"Certificate: {path.relative_to(HERE.parent.parent)}")
raise SystemExit(bool(failures))
