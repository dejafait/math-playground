"""Independent exact audit of every field of L041's arithmetic certificate.

No import or execution of the original generator. Binomials use Pascal
addition; each division is also checked by its Euclidean inequalities.
"""

import json
from fractions import Fraction as Q
from pathlib import Path


def choose(n, k):
    row = [1] + [0] * k
    for _ in range(n):
        for j in range(k, 0, -1):
            row[j] += row[j - 1]
    return row[k]


def rat(x):
    return {"numerator": x.numerator, "denominator": x.denominator}


def main():
    source = Path(__file__).with_name("fifty-nine-core-threshold-results.json")
    saved = json.loads(source.read_text())
    failures, comparisons = [], []

    def verify(name, condition):
        if not condition:
            failures.append(name)

    def division(a, d):
        v = a // d
        r = a - d * v
        verify(f"division:{a}/{d}", d > 0 and d * v <= a < d * (v + 1))
        return v, r

    N, D = choose(1024, 59), choose(68, 59)
    c, e = choose(965, 5), choose(9, 5)
    a, z = 65537 ** 28, 1 << 128
    T = Q(a, z)
    M, tr = division(a, z)
    endpoint = D * (M + 1)
    b, br = division(endpoint - 1, N)
    ordinary, ore = division(c, e)
    stages, value = [], 1
    for mult, den in [(961, 5), (962, 6), (963, 7), (964, 8), (965, 9)]:
        num = mult * value
        out, rem = division(num, den)
        stages.append(dict(i=9-den, input=value, multiplier=mult,
                           denominator=den, numerator=num, quotient=out, remainder=rem))
        value = out
    nested = value
    global_values = {}
    for name, cap in dict(benchmark=b, adjacent=b+1, ordinary=ordinary, nested=nested).items():
        num = cap * N
        out, rem = division(num, D)
        global_values[name] = dict(local_cap=cap, numerator=num, quotient=out,
                                  remainder=rem, threshold_integer_slack=M-out,
                                  strict_endpoint_slack=endpoint-num,
                                  safe_certificate=Q(out) <= T,
                                  unfloored_ratio_to_threshold=rat(Q(num, D)/T))

    # Full independent numerical reconstruction, including all old flag meanings.
    ratio = Q(N*c, D*e)
    sr = Q(choose(1024, 64), choose(68, 64))
    nr = Q(N*nested, D)/T
    # Multiplicative binomial identity cross-checks Pascal counts without factorials.
    def product_choose(n, k):
        x = Q(1)
        for j in range(1, k+1):
            x *= Q(n+1-j, j)
        return x

    checks = {
        "N_factorial": N == product_choose(1024, 59),
        "D_factorial": D == product_choose(68, 59),
        "ordinary_numerator_factorial": c == product_choose(965, 5),
        "ordinary_denominator_factorial": e == product_choose(9, 5),
        "threshold_division": M*z+tr == a,
        "threshold_fractional_part": 0 < tr < z,
        "threshold_bracket": (1 << 320)*z < a < (1 << 321)*z,
        "cap_division": N*b+br+1 == endpoint and 0 <= br < N,
        "greatest_cap_lower": N*b <= endpoint-1,
        "greatest_cap_upper": N*(b+1) > endpoint-1,
        "benchmark_pass": Q(global_values["benchmark"]["quotient"]) <= T,
        "adjacent_fail": Q(global_values["adjacent"]["quotient"]) > T,
        "nonuniform_last_pass": M*D <= endpoint-1 < (M+1)*D,
        "nonuniform_first_fail": endpoint == (M+1)*D,
        "ordinary_division": ordinary*e <= c < (ordinary+1)*e and ore == c-ordinary*e,
        "nested_divisions": all(s["quotient"]*s["denominator"] <= s["numerator"] < (s["quotient"]+1)*s["denominator"] and s["remainder"] == s["numerator"]-s["quotient"]*s["denominator"] for s in stages),
        "nested_expanded_formula": nested == (965 * ((964 * ((963 * ((962 * (961 // 5)) // 6)) // 7)) // 8)) // 9,
        "nested_improves_ordinary": nested <= ordinary,
        "ordinary_fail": Q(global_values["ordinary"]["quotient"]) > T,
        "nested_fail": Q(global_values["nested"]["quotient"]) > T,
        "ambient_marked_subset_identity": N*c == choose(1024, 64)*choose(64, 59),
        "support_marked_subset_identity": D*e == choose(68, 64)*choose(64, 59),
        "support_ratio_reproduced": ratio == sr,
        "nested_ratio_interval": 2763*D*a < 1000*N*nested*z < 2764*D*a,
        "real_endpoint_exceeds_conservative": Q(endpoint, N) > T*D/N,
    }
    for name, entry in global_values.items():
        v, r, num = entry["quotient"], entry["remainder"], entry["numerator"]
        checks[name+"_global_division"] = v*D+r == num and 0 <= r < D
        checks[name+"_floor_endpoint_equivalence"] = (Q(v) <= T) == (num < endpoint)
    for name, passed in checks.items():
        verify("recomputed:"+name, passed)
    expected = {
        "scope": "Arithmetic only; no admissible-family maximum, label symmetry or RS safety asserted.",
        "parameters": dict(n=1024, k=64, agreement=68, core=59, residual_ground=965, block=9, strength=5),
        "counts": dict(N=N, D=D, ordinary_numerator=c, ordinary_denominator=e),
        "threshold": dict(q=a, T=rat(T), M=M, remainder=tr),
        "local_caps": dict(benchmark=b, adjacent=b+1, benchmark_division_remainder=br,
                           ordinary=ordinary, ordinary_remainder=ore, nested=nested,
                           nested_stages=stages, real_strict_endpoint=rat(Q(endpoint, N)),
                           real_conservative_endpoint=rat(T*D/N)),
        "nonuniform_endpoint": dict(first_failing_sum=endpoint, last_passing_sum=endpoint-1,
                                    last_passing_quotient=(endpoint-1)//D, first_failing_quotient=endpoint//D),
        "global_transfer": global_values,
        "unfloored_ordinary_ratio": rat(ratio), "original_support_ratio": rat(sr),
        "checks": checks, "failures": [],
    }

    def compare(old, new, path=""):
        if isinstance(new, dict):
            verify(path+":keys", isinstance(old, dict) and old.keys() == new.keys())
            for k, v in new.items():
                compare(old.get(k) if isinstance(old, dict) else None, v, path+"/"+k)
        elif isinstance(new, list):
            verify(path+":length", isinstance(old, list) and len(old) == len(new))
            for i, v in enumerate(new):
                compare(old[i] if isinstance(old, list) and len(old)>i else None, v, path+"/"+str(i))
        else:
            passed = type(old) is type(new) and old == new
            comparisons.append(dict(path=path, passed=passed))
            verify("compare:"+path, passed)

    compare(saved, expected)
    verify("quoted benchmark", b == 19800268651)
    verify("quoted ordinary", ordinary == 54774358874)
    verify("quoted nested", nested == 54717350548)
    verify("all four global remainders zero", all(v["remainder"] == 0 for v in global_values.values()))
    output = source.with_name("fifty-nine-core-threshold-audit-results.json")
    result = dict(scope="Independent arithmetic audit only; symbolic membership is in L041.",
                  source=str(source.relative_to(Path.cwd())), reconstructed=expected,
                  comparisons=comparisons, recomputed_checks=len(checks),
                  scalar_fields_compared=len(comparisons), failures=failures)
    output.write_text(json.dumps(result, indent=2)+"\n")
    print(f"Independent audit: {len(comparisons)} scalar fields; {len(checks)} recomputed obligations; failures {failures}")
    print(f"Sufficient uniform cap <= {b}; adjacent {b+1} fails; ordinary nested {nested}")
    print(f"Nested transfer / required threshold in (2.763, 2.764): {Q(2763,1000) < nr < Q(2764,1000)}")
    print(f"Certificate: {output.relative_to(Path.cwd())}")
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
