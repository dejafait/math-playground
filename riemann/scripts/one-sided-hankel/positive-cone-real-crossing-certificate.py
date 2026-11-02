"""Exact constants for C673a's fixed-gauge real-crossing obstruction.

Only rational arithmetic enters the certificate. The analytic derivative
and Jordan-domain arguments are in C673a; this script checks their constants,
not those proofs or the actual cone distance. No sample is a proof input.
"""
from fractions import Fraction as Q
from pathlib import Path
import json


TERMS = 12
checks = []
failures = []


def check(name, actual, relation, required):
    passed = {"<": actual < required, ">": actual > required,
              "=": actual == required}[relation]
    checks.append(dict(name=name, actual=str(actual), relation=relation,
                       required=str(required), passed=passed))
    if not passed:
        failures.append(name)


def log_unit(v):
    assert 1 <= v <= 2
    z = (v-1)/(v+1)
    terms = [2*z**(2*j+1)/(2*j+1) for j in range(TERMS)]
    lower = sum(terms, Q(0))
    tail = 2*z**(2*TERMS+1)/((2*TERMS+1)*(1-z*z))
    return (lower, lower+tail), dict(argument=str(v), z=str(z),
        terms=[str(t) for t in terms], lower=str(lower),
        tail_upper=str(tail), upper=str(lower+tail))


log2, log2_record = log_unit(Q(2))


def log_positive(v):
    original, exponent = v, 0
    assert v >= 1
    while v > 2:
        v /= 2
        exponent += 1
    interval, record = log_unit(v)
    result = tuple(interval[i]+exponent*log2[i] for i in (0, 1))
    return result, dict(argument=str(original), power_of_two=exponent,
        reduced=record, lower=str(result[0]), upper=str(result[1]))


def atan_small(v):
    assert 0 < v <= Q(1, 2)
    terms = [(-1)**j*v**(2*j+1)/(2*j+1) for j in range(TERMS)]
    partial = sum(terms, Q(0))
    error = v**(2*TERMS+1)/(2*TERMS+1)
    interval = partial-error, partial+error
    return interval, dict(argument=str(v), terms=[str(t) for t in terms],
        partial=str(partial), error=str(error),
        lower=str(interval[0]), upper=str(interval[1]))


log5, log5_record = log_positive(Q(5))
log_ratio, log_ratio_record = log_positive(Q(121, 41))
a5, a5_record = atan_small(Q(1, 5))
a239, a239_record = atan_small(Q(1, 239))
pi = (16*a5[0]-4*a239[1], 16*a5[1]-4*a239[0])
check("log 5 lower", log5[0], ">", Q(1609, 1000))
check("log (121/41) lower", log_ratio[0], ">", Q(541, 500))
check("pi upper", pi[1], "<", Q(22, 7))

d, U, r = Q(5, 4), Q(121, 64), Q(9, 20)
check("U/d^2", U/d**2, "=", Q(121, 100))
check("U/(U-d)", U/(U-d), "=", Q(121, 41))
check("first second-derivative integral", 1/(d*(d-1)), "=", Q(16, 5))
check("negative second-derivative integral bound",
      1/(3*(U-d)**2), "=", Q(4096, 5043))
check("kernel second-derivative lower",
      Q(20, 27)*r/(r*r+Q(1, 4)**2), "=", Q(200, 159))

derivative_lower = (Q(1609, 1000)+Q(121, 100)*Q(541, 500)
                    -Q(4, 5)-Q(20, 27)*Q(22, 7))
curvature_lower = Q(16, 5)-Q(4096, 5043)+Q(200, 159)-Q(6, 5)
check("right derivative lower", derivative_lower, ">", -Q(21, 100))
check("curvature lower", curvature_lower, ">", Q(12, 5))

linear, quadratic = Q(21, 100), Q(6, 5)
center = linear/(2*quadratic)
minimum = -linear**2/(4*quadratic)
check("completed-square center", center, "=", Q(7, 80))
check("completed-square minimum", minimum, "=", -Q(147, 16000))
check("barrier exceeds required exponent", minimum, ">", -Q(1, 100))
margin = minimum+Q(1, 100)
check("barrier margin", margin, "=", Q(13, 16000))

report = dict(
    status="EXACT CONSTANT CERTIFICATE; ANALYTIC PROOF IN C673a",
    scope="L673 fixed gauge; E(s,-1), 0<s<1/4; contours in |x+z|>1. No lower bound on kappa or the signed integral.",
    series_terms=TERMS,
    logarithms=dict(log2=log2_record, log5=log5_record,
                   log121over41=log_ratio_record),
    pi=dict(atan_one_fifth=a5_record, atan_one_239=a239_record,
            lower=str(pi[0]), upper=str(pi[1]),
            identity="pi=16 atan(1/5)-4 atan(1/239)"),
    summary=dict(derivative_lower=str(derivative_lower),
                 required_derivative="-21/100",
                 curvature_lower=str(curvature_lower), required_curvature="12/5",
                 exponent_lower=str(minimum), target_upper="-1/100",
                 strict_margin=str(margin)),
    checks=checks, failures=failures)
out = Path(__file__).with_suffix(".json")
out.write_text(json.dumps(report, indent=2)+"\n")
print(f"Exact checks: {len(checks)}; failures: {failures}")
print(f"Derivative > {derivative_lower} > -21/100; curvature >= {curvature_lower} > 12/5.")
print(f"Exponent > {minimum}; required upper <= -1/100; obstruction margin {margin}.")
print(f"Full certificate: {out}")
if failures:
    raise SystemExit(1)
