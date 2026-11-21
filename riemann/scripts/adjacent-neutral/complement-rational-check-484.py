#!/usr/bin/env python3
"""Exact rational checks used in C744j; no floating-point sign evidence."""
from fractions import Fraction as F
import json
import math
from pathlib import Path


def pair(x):
    return {"numerator": str(x.numerator), "denominator": str(x.denominator)}


def main():
    h64 = sum((F(1,j) for j in range(1,65)),F(0))
    h257 = sum((F(1,j) for j in range(1,258)),F(0))
    log2_partial = 2*sum((F(1,(2*k+1)*3**(2*k+1)) for k in range(5)),F(0))
    log2_tail_upper = F(2,11*3**11)/(1-F(1,9))
    exp11_partial = sum((F(11,10)**k/math.factorial(k) for k in range(6)),F(0))
    exp055_partial = sum((F(11,20)**k/math.factorial(k) for k in range(7)),F(0))
    c_upper = F(586,1000)+F(11,20)+F(11,80)+F(22,7)+F(283,200)*F(347,500)
    epsilon_sq_upper = F(72*515,7**512)
    floor_lower = F(49,8)-F(27,5)*F(10001,10000)
    checks = {
        "log2_lower":log2_partial>F(693,1000),
        "log2_upper":log2_partial+log2_tail_upper<F(694,1000),
        "h64_upper":h64<F(4744,1000),
        "gamma_upper":F(4744,1000)-6*F(693,1000)==F(586,1000),
        "ell_upper":exp11_partial>3,
        "log_pi_ell_upper":exp055_partial>F(121,70),
        "sqrt2_upper":F(283,200)**2>2,
        "tail_constant_upper":c_upper<F(27,5),
        "h257_lower":h257>F(49,8),
        "moment_graph_tail_upper":epsilon_sq_upper<F(1,10000),
        "positive_complement_floor":floor_lower>F(18,25),
    }
    output = Path(__file__).with_suffix(".json")
    output.write_text(json.dumps({
        "method":"Exact Fraction arithmetic for C744j elementary comparisons",
        "qualification":"Uses the named Archimedes bound pi<22/7 and standard series identities justified in C744j; certifies only the complementary floor.",
        "checks":checks,
        "values":{key:pair(value) for key,value in {
            "H64":h64,"H257":h257,"log2_partial":log2_partial,
            "log2_tail_upper":log2_tail_upper,"exp_1_1_partial":exp11_partial,
            "exp_0_55_partial":exp055_partial,"c_upper":c_upper,
            "epsilon_squared_upper":epsilon_sq_upper,
            "tail_floor_lower":floor_lower,"required_floor":F(18,25),
        }.items()},
        "failed_checks":[key for key,value in checks.items() if not value],
    },indent=2)+"\n")
    print(f"Exact comparisons: {sum(checks.values())}/{len(checks)} passed")
    print(f"Tail floor > {floor_lower} = {float(floor_lower):.8g}; required >18/25=0.72")
    print("Failures:", [key for key,value in checks.items() if not value])
    print(f"Full certificate: {output}")
    if not all(checks.values()):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
