"""Exact integer polynomial and complete regular-fiber norm certificate.

Coefficients are ascending. No symbolic algebra package or external arithmetic
data is required. The divisor and fiber-specialization arguments are in L034.
"""
from fractions import Fraction
from pathlib import Path
import json


def trim(p):
    p = list(p)
    while len(p) > 1 and not p[-1]:
        p.pop()
    return p


def add(p, q):
    r = [0] * max(len(p), len(q))
    for i, c in enumerate(p):
        r[i] += c
    for i, c in enumerate(q):
        r[i] += c
    return trim(r)


def scale(p, c):
    return trim([c * v for v in p])


def mul(p, q):
    r = [0] * (len(p) + len(q) - 1)
    for i, c in enumerate(p):
        for k, d in enumerate(q):
            r[i+k] += c*d
    return trim(r)


def power(p, n):
    r = [1]
    for _ in range(n):
        r = mul(r, p)
    return r


def ev(p, x):
    r = 0
    for c in reversed(p):
        r = r*x+c
    return r


def resultant(p, q):
    """Sylvester determinant via exact Bareiss elimination, with row swaps."""
    m, n = len(p)-1, len(q)-1
    size = m+n
    rows = []
    for i in range(n):
        rows.append([0]*i+list(reversed(p))+[0]*(n-i-1))
    for i in range(m):
        rows.append([0]*i+list(reversed(q))+[0]*(m-i-1))
    previous, sign = 1, 1
    for k in range(size-1):
        if not rows[k][k]:
            swap = next((i for i in range(k+1, size) if rows[i][k]), None)
            if swap is None:
                return 0
            rows[k], rows[swap] = rows[swap], rows[k]
            sign = -sign
        pivot = rows[k][k]
        for i in range(k+1, size):
            for l in range(k+1, size):
                num = pivot*rows[i][l]-rows[i][k]*rows[k][l]
                quotient, rem = divmod(num, previous)
                if rem:
                    raise ArithmeticError("inexact Bareiss division")
                rows[i][l] = quotient
            rows[i][k] = 0
        previous = pivot
    return sign*rows[-1][-1]


a = [-39176677684144739,108160113602504237,74593328129816300,
     420015065507429,-14545268641576841,-1895608370650736,
     576036867160006,82165362766027,2536749758583,19162005343,
     21559874,743]
b1 = [-707351591,271927184,65058492,1304157,4518,1]
b2 = [-37315543,-37789861,-3406817,3626752,192189,1]
b = mul(b1, b2)
g = [-20,-10,-1,1]
d = power([-16,1],11)
h = [9789217,4971236,1333262,-52820,1]
jcoef = [-104748564078368391,199736619430410535,159480622275659333,
         6839041777752481,-29669709666741936,-4074814667347831,
         1134855511654843,164063633585170,5072626276355,38323813979,
         43119747,1486]
A, B = [-55,30,-4], [-4,1]
residuals = {
    "linear_elimination": add(add(scale(a,2),scale(b,-1)),scale(jcoef,-1)),
    "constant_elimination": add(add(add(mul(a,a),scale(mul(a,b),-1)),
                                   scale(mul(mul(b,b),g),-1)),mul(d,power(h,3))),
    "descent_x_norm": add(add(add(mul(A,A),scale(mul(A,B),-1)),
                              scale(mul(mul(B,B),g),-1)),power([-5,1],5)),
}
torsion = {}
for label, x, y in [("T",5,5),("2T",16,-61),("3T",16,60),("4T",5,-6)]:
    numerator = ev(a,x)+ev(b,x)*y
    torsion[label] = {"x":x,"y":y,"j_numerator":str(numerator),
                      "b_value":str(ev(b,x)),"f":ev(A,x)+ev(B,x)*y}
    if x != 16:
        torsion[label]["j"] = str(Fraction(numerator,ev(d,x)))
torsion["2T"]["j_after_cancellation"] = str(Fraction(-ev(h,16)**3,
                                                        int(torsion["3T"]["j_numerator"])))
# The complete fiber j=1 is presented by the monic F1 of degree twelve.
F1 = add(add(power(h,3),jcoef),scale(d,-1))
f_numerator = add(mul(A,b),mul(B,add(d,scale(a,-1))))
den_resultant = resultant(F1,b)
num_resultant = resultant(F1,f_numerator)
discriminant_resultant = resultant(F1,[i*F1[i] for i in range(1,len(F1))])
scalar = 121**11
fiber_norm = Fraction(num_resultant,den_resultant)
expected = scalar*(1+24729001)**5
checks = {key: value == [0] for key,value in residuals.items()}
checks.update({
    "j_T": torsion["T"]["j"] == "-24729001",
    "O_leading_coefficients": b[-1] == 1 and len(b)-1 == 10 and len(a)-1 == 11,
    "cusp_3T_numerator_nonzero": int(torsion["3T"]["j_numerator"]) != 0,
    "2T_cancellation_exact_order_11": int(torsion["2T"]["j_numerator"]) == 0
                                        and ev(h,16) != 0,
    "fiber_degree_12_monic": len(F1)-1 == 12 and F1[-1] == 1,
    "fiber_no_x16": ev(F1,16) != 0,
    "fiber_y_reconstructible": den_resultant != 0,
    "fiber_reduced": discriminant_resultant != 0,
    "complete_fiber_norm_matches_scalar": fiber_norm == expected,
    "scalar_constant_class": scalar == 11**2*(11**4)**5,
    "resultant_implementation_control": resultant([-2,1],[-3,1]) == -1,
})
failures = [key for key, ok in checks.items() if not ok]
certificate = {
    "source": "FNS June 10 2019 manuscript Section 7.2 pp.25-27; equations for j and (7.4)",
    "polynomials_ascending": {"a":a,"b1":b1,"b2":b2,"b":b,"g":g,"d":d,
                               "h":h,"jcoef":jcoef,"F_at_1":F1,"f_numerator_at_1":f_numerator},
    "residuals":residuals,"torsion":torsion,
    "fiber_at_1": {"degree_actual":12,"degree_required":12,
                   "F_at_16":str(ev(F1,16)),"resultant_denominator":str(den_resultant),
                   "resultant_numerator":str(num_resultant),
                   "discriminant_resultant":str(discriminant_resultant),
                   "norm":str(fiber_norm),"required_norm":str(expected)},
    "conclusion":{"norm":"11^22*(j+24729001)^5","scalar":str(scalar),
                  "fifth_power_class":"[11^2]","nonconstant_class_actual":False,
                  "nonconstant_class_required":True},
    "checks":checks,"failures":failures,
}
path = Path(__file__).with_name("norm-certificate.json")
path.write_text(json.dumps(certificate,indent=2)+"\n")
print(f"Checks: {sum(checks.values())}/{len(checks)}; failures: {failures}")
print("Fiber degree actual/required: 12/12; norm: 11^22*(j+24729001)^5")
print("Class: [11^2]; nonconstant-class actual/required: false/true")
print(f"Certificate: {path}")
if failures:
    raise SystemExit(1)
