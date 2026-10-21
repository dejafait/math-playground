"""Exact scalar certificate; analytic assembly is in L045. No orbit claim."""
from fractions import Fraction as F
import json
from pathlib import Path


def rat(x):
    x = F(x)
    return {"numerator": str(x.numerator), "denominator": str(x.denominator)}


def log_bounds(t, m=64):
    x = F(t-1, t+1)
    low = 2*sum((x**(2*j+1)/F(2*j+1) for j in range(m)), F(0))
    return low, low+2*x**(2*m+1)/((2*m+1)*(1-x*x))


def main():
    records = []

    def check(name, actual, relation, required):
        actual, required = F(actual), F(required)
        passed = {"<": actual < required, ">": actual > required,
                  "=": actual == required, ">=": actual >= required}[relation]
        records.append(dict(name=name, actual=rat(actual), relation=relation,
                            required=rat(required), passed=passed))

    M, C = 225640000, 338460000
    R17, R18 = 2**17-1, 2**18-1
    A17 = F(399, 5)*R17
    rhs17 = 1668*R17+F(69*17, 1034)
    check("exp partial sum exceeds 27/10", F(163, 60), ">", F(27, 10))
    check("log17 below 3", 27**3, ">", 17*10**3)
    check("log C below 20", 27**20, ">", C*10**20)
    check("A17 below C", A17, "<", C)
    check("r17 conservative RHS below C", rhs17, "<", C)
    check("r17 margin exceeds 119833000", C-rhs17, ">", 119833000)
    check("log3/log2 exceeds 3/2", 3**2, ">", 2**3)
    js, hs, tails = [2]*18, [225639842]+[3]*17, [131990870]+[2]*17
    K, L, N, d = 225640001, 131990940, 357630941, 1
    for i, (j, h, a) in enumerate(zip(js, hs, tails)):
        check(f"J[{i}] lower guard", j, ">=", 2)
        check(f"H[{i}] lower guard", h, ">=", 3)
        check(f"a[{i}] lower guard", a, ">=", 0)
        check(f"a[{i}] congruence", a % 18, "=", 2)
    check("number of words", len(js), "=", 18)
    check("K word count", sum(3*j+h for j, h in zip(js, hs)), "=", K)
    check("L word count", sum(j+a for j, a in zip(js, tails)), "=", L)
    check("N word count", sum(4*j+h+a for j, h, a in zip(js, hs, tails)), "=", N)
    check("primitive odd scaling", d*K, "=", K)
    check("primitive even scaling", d*L, "=", L)
    check("K0 exceeds published M", K, ">", M)
    check("N exceeds C", N, ">", C)
    check("log N exceeds 17 using e<3", N, ">", 3**17)
    k_rhs_lower = F(15, 4)*R18*(F(133, 10)*17+9)
    n_rhs_lower = R18*(F(399, 5)*17+54)+F(69*18, 1034)
    check("K below aggregate bound lower estimate", K, "<", k_rhs_lower)
    check("N below assembled bound lower estimate", N, "<", n_rhs_lower)
    check("length conversion", N, "<", F(8, 5)*K+F(69*18, 1034))
    low2, high2 = log_bounds(2)
    low3, high3 = log_bounds(3)
    dl2, dh2 = F(6931471805599453, 10**16), F(6931471805599454, 10**16)
    dl3, dh3 = F(10986122886681096, 10**16), F(10986122886681097, 10**16)
    check("log2 decimal lower", dl2, "<", low2)
    check("log2 decimal upper", high2, "<", dh2)
    check("log3 decimal lower", dl3, "<", low3)
    check("log3 decimal upper", high3, "<", dh3)
    lam_low, lam_high = N*dl2-K*dh3, N*dh2-K*dl3
    check("lambda lower exceeds 1/2", lam_low, ">", F(1, 2))
    check("lambda upper below 53/100", lam_high, "<", F(53, 100))
    check("53/100 below r18 cap", F(53, 100), "<", F(23*18, 517))
    check("optional lower form dominated by 1/K", F(1, K), "<", F(1, 2))
    failures = [r["name"] for r in records if not r["passed"]]
    cert = {
        "scope": "Fixed factor-2 assembled scalar comparison, not individual heights, parity or closure.",
        "exclusion": {"last_r": 17, "R": R17, "M": M, "C": C,
                      "A": rat(A17), "rhs_upper": rat(rhs17), "margin_lower": rat(C-rhs17)},
        "first_failure": {"r": 18, "J": js, "H": hs, "a": tails,
                          "K": K, "L": L, "N": N, "d": d, "K0": K, "L0": L,
                          "K_rhs_lower": rat(k_rhs_lower), "N_rhs_lower": rat(n_rhs_lower),
                          "lambda_lower": rat(lam_low), "lambda_upper": rat(lam_high)},
        "log_evidence": {"method": "positive atanh series; 64 terms, geometric tail bound",
                         "log2_lower": rat(low2), "log2_upper": rat(high2),
                         "log3_lower": rat(low3), "log3_upper": rat(high3)},
        "checks": records, "summary": {"checks": len(records), "failures": failures}}
    path = Path(__file__).with_name("retained-range-certificate.json")
    path.write_text(json.dumps(cert, indent=2)+"\n")
    print(f"checks: {len(records)}; failures: {failures}")
    print(f"r17 RHS upper: {rhs17}; required: < {C}; margin lower: {C-rhs17}")
    print(f"r18 K: {K}; bound lower: {k_rhs_lower}; N: {N}; bound lower: {n_rhs_lower}")
    print(f"r18 lambda: ({lam_low}, {lam_high}); required: (0, {F(414,517)})")
    print(f"certificate: {path}")
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
