"""Independent L034 audit: exact interpolation checks and quotient-algebra norms.

No construction code is imported. Source coefficients were compared with FNS
Section 7.2 pp.26–27. Candidate coefficient lists are checked by enough exact
evaluations to prove equality; norms use 12 by 12 multiplication matrices and
ordinary rational Gaussian elimination, not Sylvester/Bareiss elimination.
"""
from fractions import Fraction as Q
from pathlib import Path
import json

root = Path(__file__).parent
original = json.loads((root / "norm-certificate.json").read_text())
p = original["polynomials_ascending"]


def value(coeffs, x):
    return sum(c * x**i for i, c in enumerate(coeffs))


def remainder(coeffs, modulus):
    r = list(coeffs)
    n = len(modulus)-1
    assert modulus[-1] == 1
    for k in range(len(r)-1, n-1, -1):
        c = r[k]
        for i in range(n+1):
            r[k-n+i] -= c*modulus[i]
    return (r+[0]*n)[:n]


def multiplication(coeffs, modulus):
    n = len(modulus)-1
    columns = [remainder([0]*k+list(coeffs), modulus) for k in range(n)]
    return [[columns[j][i] for j in range(n)] for i in range(n)]


def determinant(matrix):
    rows = [[Q(c) for c in row] for row in matrix]
    answer = Q(1)
    for k in range(len(rows)):
        pivot_row = next((i for i in range(k, len(rows)) if rows[i][k]), None)
        if pivot_row is None:
            return Q(0)
        if pivot_row != k:
            rows[k], rows[pivot_row] = rows[pivot_row], rows[k]
            answer = -answer
        pivot = rows[k][k]
        answer *= pivot
        for i in range(k+1, len(rows)):
            factor = rows[i][k]/pivot
            rows[i] = [a-factor*b for a, b in zip(rows[i], rows[k])]
    return answer


# Maximum degrees include both the candidate and reconstructed expression.
bounds = {"b_product":10, "g":3, "d":11, "J":11,
          "elimination":23, "x_norm":5, "F1":12, "G1":12}
samples = []
for x in range(25):
    a, b, g, d, h, J, F, G = (value(p[k], x) for k in
                              ["a", "b", "g", "d", "h", "jcoef",
                               "F_at_1", "f_numerator_at_1"])
    A, B = -4*x*x+30*x-55, x-4
    residuals = {"b_product":b-value(p["b1"],x)*value(p["b2"],x),
                 "g":g-(x**3-x*x-10*x-20), "d":d-(x-16)**11,
                 "J":J-(2*a-b), "elimination":a*a-a*b-b*b*g+d*h**3,
                 "x_norm":A*A-A*B-B*B*g+(x-5)**5,
                 "F1":F-(h**3+J-d), "G1":G-(A*b+B*(d-a))}
    samples.append({"x":x,"residuals":residuals})

F = p["F_at_1"]
derivative = [i*F[i] for i in range(1,len(F))]
matrices = {"denominator":multiplication(p["b"],F),
            "numerator":multiplication(p["f_numerator_at_1"],F),
            "derivative":multiplication(derivative,F)}
dets = {key:determinant(matrix) for key,matrix in matrices.items()}
fiber_norm = dets["numerator"]/dets["denominator"]
scalar = fiber_norm / 24729002**5
torsion = {}
for label,x,y in [("T",5,5),("2T",16,-61),("3T",16,60),("4T",5,-6)]:
    a,b,d = (value(p[key],x) for key in ["a","b","d"])
    entry = {"x":x,"y":y,"j_numerator":str(a+b*y),"b_value":str(b),
             "f":(x-4)*y-4*x*x+30*x-55}
    if d:
        entry["j"] = str(Q(a+b*y,d))
    torsion[label] = entry
h16 = value(p["h"],16)
torsion["2T"]["j_after_cancellation"] = str(Q(-h16**3,int(torsion["3T"]["j_numerator"])))

checks = {"exact_polynomial_identities": all(v == 0 for row in samples for v in row["residuals"].values()),
          "enough_distinct_evaluations": len(samples)>max(bounds.values()),
          "candidate_degree_bounds": all(len(p[k])-1<=bound for k,bound in
                [("a",11),("b1",5),("b2",5),("b",10),("g",3),("d",11),
                 ("h",4),("jcoef",11),("F_at_1",12),("f_numerator_at_1",12)]),
          "degree_12_monic": len(F)==13 and F[-1]==1,
          "norm_denominator_nonzero": dets["denominator"]!=0,
          "fiber_reduced":dets["derivative"]!=0,
          "fiber_avoids_x16":value(F,16)!=0,
          "all_torsion_values_match":torsion==original["torsion"],
          "cancellation_order_11":h16!=0 and torsion["2T"]["j_numerator"]=="0" and int(torsion["3T"]["j_numerator"])!=0,
          "simple_x_parameters":[(2*y+1)**2 for x,y in [(16,-61),(16,60)]]==[121**2,121**2],
          "O_leading_terms":p["a"][-1]==743 and p["b"][-1]==p["d"][-1]==1,
          "norm_matches":fiber_norm==11**22*24729002**5,
          "scalar_matches":scalar==11**22==121**11,
          "class_factorization":scalar==11**2*(11**4)**5,
          "gaussian_sign_control":determinant([[0,1],[1,0]])==-1}
for key,oldkey in [("denominator","resultant_denominator"),("numerator","resultant_numerator"),("derivative","discriminant_resultant")]:
    checks[key+"_matches_original_full_integer"] = dets[key]==int(original["fiber_at_1"][oldkey])
checks["F16_matches"] = value(F,16)==int(original["fiber_at_1"]["F_at_16"])
checks["norm_matches_original_full_integer"] = fiber_norm==int(original["fiber_at_1"]["norm"])
failures = [key for key,ok in checks.items() if not ok]
certificate = {"method":"quotient multiplication matrices; rational Gaussian elimination",
    "polynomial_identity_checks":{"degree_bounds":bounds,"distinct_points":25,"evaluations":samples},
    "multiplication_matrices":matrices,
    "determinants":{key:str(v) for key,v in dets.items()},
    "fiber":{"degree_actual":len(F)-1,"degree_required":12,"F_at_16":str(value(F,16)),
             "norm":str(fiber_norm),"required_norm":str(11**22*24729002**5),"scalar":str(scalar)},
    "torsion":torsion,"h16":str(h16),
    "decision":{"nonconstant_class_actual":False,"nonconstant_class_required":True,"class":"[11^2]"},
    "checks":checks,"failures":failures}
output = root / "audit-certificate.json"
output.write_text(json.dumps(certificate,indent=2)+"\n")
print(f"Audit checks: {sum(checks.values())}/{len(checks)}; failures: {failures}")
print("Polynomial zeros actual/required: 25/24; fiber degree actual/required: 12/12")
print(f"Norm: {fiber_norm}; scalar: {scalar} = 11^22")
print("Nonconstant class actual/required: false/true; compression remains parked")
print(f"Certificate: {output}")
if failures:
    raise SystemExit(1)
