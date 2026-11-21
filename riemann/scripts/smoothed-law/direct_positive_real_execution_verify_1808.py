"""Check complete saved1808 prefix evidence with integer identities.

This does not verify the analytic theorem or any unevaluated scalar. Polynomial
values are reconstructed by a common-denominator integer sum rather than the
evaluator's rational Horner implementation. Moments and the saved Ihat prefix
are compared against an integer common-denominator sum.
"""
from fractions import Fraction as F
from math import factorial, gcd, lcm
import hashlib
import json

from direct_positive_real_execution_1808 import ROOT, OUT, SUMMARY, write_json
from direct_positive_real_execution_remaining_1808 import read, RESULT


def polynomial_power_matches(z, degree, squarings, value):
    n, d = z.numerator, z.denominator
    fac = factorial(degree)
    den = fac*d**degree
    num = sum(n**k*d**(degree-k)*(fac//factorial(k)) for k in range(degree+1))
    num = min(den, max(0, num))
    exponent = 2**squarings
    return num**exponent*value.denominator == value.numerator*den**exponent


def integer_sum_matches(values, expected):
    denominator = lcm(*(v.denominator for v in values))
    numerator = sum(v.numerator*(denominator//v.denominator) for v in values)
    return numerator*expected.denominator == expected.numerator*denominator


def main():
    prefix = json.loads(SUMMARY.read_text())
    remaining = json.loads(RESULT.read_text())
    assert remaining["status"] != "RUNNING_REMAINING_EXACT_CONSTRUCTORS"
    checks = {}
    for item in prefix["artifacts"] + remaining["artifacts"]:
        path = ROOT.parent.parent / item["path"]
        checks["hash:"+path.name] = hashlib.sha256(path.read_bytes()).hexdigest() == item["sha256"]
    nodes = read("inner_nodes")["nodes_and_weights"]
    a = read("moment_inputs")["a"]
    v = read("moment_inputs")["v"]
    for j, (x, omega) in enumerate(nodes):
        sample = read(f"gaussian_{j:02d}")
        checks[f"Gaussian{j}:node_weight"] = sample["x"] == x and sample["omega"] == omega
        checks[f"Gaussian{j}:integer_polynomial_power"] = polynomial_power_matches(-(x*x)/16, 40, 4, sample["value"])
        checks[f"Gaussian{j}:range"] = 0 <= sample["value"] <= 1
        checks[f"Gaussian{j}:moment_input"] = a[j] == omega*sample["value"] and v[j] == x/4
    for k in range(prefix["moments_completed"]):
        expected = read(f"moment_{k:02d}")["value"]
        checks[f"M{k}:integer_common_denominator_identity"] = integer_sum_matches(
            [aj*vj**k for aj, vj in zip(a, v)], expected)
    partial_terms = []
    r14 = read("reference_rule14")
    for index in range(remaining["Ihat_samples_completed"]):
        sample = read(f"Ihat_sample_{index:03d}")
        x, omega, A, u, h = [sample[key] for key in ("x", "omega", "A", "u", "h")]
        panel, j = divmod(index, 14)
        checks[f"Ihat{index}:node_weight"] = (
            x == panel+(1+r14["nodes"][j])/2 and omega == r14["weights"][j]/2)
        checks[f"Ihat{index}:A_integer_polynomial_power"] = polynomial_power_matches(-(x*x)/256, 20, 8, A)
        checks[f"Ihat{index}:u_integer_polynomial_power"] = polynomial_power_matches(-x/16, 20, 3, u)
        checks[f"Ihat{index}:denominator"] = sample["denominator"] == 1-u**4 > F(1, 512)
        checks[f"Ihat{index}:combined_quotient"] = h*sample["denominator"] == (A-u)*u
        partial_terms.append(omega*h)
    if partial_terms:
        partial = read("Ihat_partial")
        checks["Ihat_prefix:count"] = partial["summands_completed"] == len(partial_terms)
        checks["Ihat_prefix:integer_common_denominator_identity"] = integer_sum_matches(partial_terms, partial["value"])
    failures = [name for name, passed in checks.items() if not passed]
    report = {"status": "PASS_COMPLETE_SAVED_PREFIX_ONLY" if not failures else "FAIL",
              "checks": checks, "check_count": len(checks), "failures": failures,
              "Gaussian_inputs_checked": len(nodes),
              "moments_checked": prefix["moments_completed"],
              "Ihat_summands_checked": len(partial_terms),
              "scalars_certified": 0,
              "scope": "Integer identities for complete saved prefix; no scalar radius, full evaluator cost or analytic-source verification"}
    path = ROOT / "direct_positive_real_execution_verify_1808.json"
    write_json(path, report)
    print(f"Saved exact prefix: {len(checks)} checks; failures: {failures}")
    print(f"Gaussian inputs {len(nodes)}/48; moments {prefix['moments_completed']}/29; Ihat prefix {len(partial_terms)}/224; scalar certificates0/8")
    print(f"Certificate: {path.relative_to(ROOT.parent.parent)}")
    assert not failures, failures


if __name__ == "__main__":
    main()
