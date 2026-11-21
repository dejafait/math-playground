#!/usr/bin/env python3
"""Exact scalar checks for C466m; not a density or whole-proof certificate."""
from fractions import Fraction as F
from pathlib import Path
import json


checks = []


def check(name, actual, required, reason):
    actual, required = F(actual), F(required)
    passed = actual < required
    checks.append({"name": name, "actual_upper_bound": str(actual),
                   "required_strict_upper_bound": str(required),
                   "passed": passed, "justification": reason})
    print(f"{name}: upper={actual}; required < {required}; {'PASS' if passed else 'FAIL'}")


L = 65536
check("gamma_shift", F(1, 8) + F(9, 112), F(1, 4),
      "|q|>=4 and |1/(2q)|<=1/8 in the logarithmic power-series bound.")
check("whole_completion_remainder", F(1, 3)+F(1, 4)+F(1, 12)+2, 3,
      "Sum of Gamma, fixed shift, polynomial and Euler-logarithm bounds, in units 1/|q|.")
check("horizontal_G_derivative", F(1, 8)+F(7, 8)/F(8, 3)+F(7, 8)/(4*F(8, 3)), 1,
      "Coefficient of log(v)/sqrt(v), using log(v)>=8/3 and sqrt(v)>=4.")
check("growth_envelope", F(12, 256)+F(7, 2**32)+F(32, 2**32*256)+F(32, 2**64), F(1, 10),
      "v>=exp(256); weaker rational lower bounds sqrt(v)>2^32 and v>2^64 suffice.")
check("second_derivative", F(3*(L+7), 16*L)+F(7, 2*2**64*L), 2,
      "Coefficient of log(r)/r^(3/2) on [r/2,3r/2]; 2^(3/2)<3, sqrt(r)>2^64.")
check("second_difference_remainder_coefficient", 20+F(12, L), 24,
      "Coefficient of log(r)/sqrt(r); sqrt(2)<3/2.")
check("second_difference_remainder", F(24*L, 2**64), 1,
      "At log(r)=65536 use exp(L/2)>2^64; L exp(-L/2) decreases thereafter.")
check("compact_second_difference", F(2*L, 2**64), 1,
      "2T^2 L exp(-3L/2), T=exp(256); exp(3L/2-512)>2^64 at L=65536, decreasing thereafter.")
check("small_range_deficit", F(16, 32768), F(1, 32),
      "epsilon=2^-10, log(1/epsilon)<7, and kappa/4>1/32.")
check("comparable_error", F(160, L)+F(120, 2**64)+F(800, 2**64*L), F(1, 128),
      "Uniform error divided by kappa*sqrt(r)*log(r); all three terms decrease for r>=R0.")
check("comparable_endpoint", F(1, 64), F(31, 1024),
      "f(epsilon)>=sqrt(epsilon)-epsilon=31/1024; the stated minimum uses concavity.")
check("far_range_squared_comparison", 121, 128,
      "8*sqrt(2)>11; hence 9/5-11/(5sqrt(2))>1/5.")
check("local_integral_log_threshold", 6+5*10, F(7*1024, 16),
      "At L=1024, log(40)+5log(L)<6+50; logarithmic difference has positive derivative.")
check("tail_integral_log_threshold", 9+10, F(1024, 16),
      "At L=1024, log(256(L+8))<log(512L)<19; difference has positive derivative.")

certificate = {
    "scope": "Exact rational arithmetic supporting the thresholds in C466m; analytic implications, inherited inputs and p(S) are not machine-verified.",
    "summary": {"checks": len(checks), "passed": sum(c["passed"] for c in checks),
                "failures": [c["name"] for c in checks if not c["passed"]],
                "density_lower_bound_certified": False,
                "requested_m_R_pair_complete": False},
    "checks": checks,
}
destination = Path(__file__).with_name("effective-tail-936.json")
destination.write_text(json.dumps(certificate, indent=2)+"\n")
print(f"Certificate: {destination}; failures={certificate['summary']['failures']}")
print("Required p(S)>=m>0: no numerical m certified; requested pair remains incomplete.")
raise SystemExit(bool(certificate["summary"]["failures"]))
