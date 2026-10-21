"""Independent exact check of every stored basic-LP coefficient and constraint."""
import json
from fractions import Fraction
from math import prod
from pathlib import Path

HERE = Path(__file__).parent
SOURCE = HERE / "delsarte-lp-results.json"
OUT = HERE / "delsarte-lp-audit-results.json"


def binomial(n, k):
    if k < 0 or k > n:
        return 0
    return prod(range(n-k+1, n+1)) // prod(range(1, k+1))


def decode(x):
    return Fraction(x["numerator"], x["denominator"])


def encode(x):
    return dict(numerator=x.numerator, denominator=x.denominator)


def main():
    saved = json.loads(SOURCE.read_text())
    params = saved["parameters"]
    assert (params["n"], params["w"], params["d"]) == (1024, 68, 10)
    assert params["threshold_numerator"] == 65537**28
    assert params["threshold_denominator"] == 2**128
    n, w = 1024, 68
    # The numerator is the coefficient of z^i in (1-z)^j times
    # sum_r C(w-j,r) C(n-w-j,r) z^r. This is the assessed formula
    # expanded independently by polynomial multiplication.
    matrix = []
    failures = []
    for j in range(1, w+1):
        polynomial = [0]*(w+1)
        for r in range(w-j+1):
            coefficient = binomial(w-j, r)*binomial(n-w-j, r)
            for h in range(j+1):
                polynomial[r+h] += coefficient*((-1)**h)*binomial(j, h)
        row = [Fraction(polynomial[i], binomial(w,i)*binomial(n-w,i))
               for i in range(5,w+1)]
        matrix.append(row)
        for c,v in enumerate(row):
            if v != decode(saved["q_matrix"][j-1][c]):
                failures.append(f"coefficient mismatch j={j}, i={c+5}")
    exact = saved["exact"]
    x = list(map(decode, exact["primal"]))
    y = list(map(decode, exact["dual"]))
    assert len(x) == 64 and len(y) == 68
    primal_slacks = [1+sum(q*v for q,v in zip(row,x)) for row in matrix]
    dual_slacks = [-sum(y[j]*matrix[j][c] for j in range(68))-1
                   for c in range(64)]
    for label, actual, recorded in [
            ("primal slack", primal_slacks, exact["primal_slacks"]),
            ("dual slack", dual_slacks, exact["dual_slacks"])]:
        if actual != list(map(decode, recorded)):
            failures.append(f"stored {label} does not match actual")
    if not all(v>=0 for v in x+y+primal_slacks+dual_slacks):
        failures.append("negative coefficient or slack")
    primal_value, dual_value = sum(x), sum(y)
    packing_ratio = Fraction(binomial(n,64),binomial(w,64))
    if primal_value != dual_value or 1+primal_value != packing_ratio:
        failures.append("objective equality or packing-ratio comparison failed")
    if decode(exact["primal_objective"]) != primal_value:
        failures.append("stored primal objective mismatch")
    if decode(exact["dual_objective"]) != dual_value:
        failures.append("stored dual objective mismatch")
    bound = 1+primal_value.__floor__()
    excess = (2**128)*bound-65537**28
    if excess <= 0 or excess != exact["primal_scaled_threshold_excess"]:
        failures.append("threshold excess check failed")
    if any(v != 0 for v in primal_slacks[:64]+dual_slacks+y[64:]):
        failures.append("claimed tightness or zero dual tail failed")
    ratio = Fraction(2**128*bound,65537**28)
    ratio_milli = (1000*ratio.numerator)//ratio.denominator
    if min(x) <= 0 or min(y[:64]) <= 0:
        failures.append("claimed strict positivity failed")
    result = dict(parameters=params, source=SOURCE.name,
        coefficient_checks=68*64, primal_constraint_checks=68,
        dual_constraint_checks=64, primal_nonnegative_checks=64,
        dual_nonnegative_checks=68,
        minimum_primal=encode(min(x)),
        minimum_positive_dual=encode(min(y[:64])),
        primal_slacks=[encode(v) for v in primal_slacks],
        dual_slacks=[encode(v) for v in dual_slacks],
        primal_positive_distances=[i+5 for i,v in enumerate(x) if v>0],
        dual_positive_rows=[j+1 for j,v in enumerate(y) if v>0],
        objective=encode(primal_value), packing_ratio=encode(packing_ratio),
        floor_bound=bound, scaled_threshold_excess=excess,
        threshold_ratio_milli_interval=[ratio_milli,ratio_milli+1],
        negative_primal_distances=[i+5 for i,v in enumerate(x) if v<0],
        negative_dual_rows=[j+1 for j,v in enumerate(y) if v<0],
        failed_primal_rows=[j+1 for j,v in enumerate(primal_slacks) if v<0],
        failed_dual_distances=[i+5 for i,v in enumerate(dual_slacks) if v<0],
        failures=failures)
    OUT.write_text(json.dumps(result,indent=2)+"\n")
    print(f"Exact audit: 4352 coefficients, 68 primal and 64 dual inequalities, 132 nonnegative variables")
    print(f"Verified LP floor bound={bound}; required <= {65537**28}/{2**128}")
    print(f"Ratio in [{ratio_milli}/1000,{ratio_milli+1}/1000); scaled excess={excess}")
    print(f"Failures: {failures}; full audit: {OUT}")
    assert not failures


if __name__ == "__main__":
    main()
