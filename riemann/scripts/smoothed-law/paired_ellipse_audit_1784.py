"""Complete exact C033u certificate audit; no quadrature or observable."""
from collections import Counter
from fractions import Fraction
from hashlib import sha256
from pathlib import Path
import json


def factor(n):
    """Full factorization, without using the generator's prime sieve."""
    factors = {}
    d = 2
    while d*d <= n:
        while n % d == 0:
            factors[d] = factors.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    return factors


def main():
    root = Path(__file__).parent
    source = root / "paired_ellipse_preflight_1782.json"
    raw = source.read_bytes()
    cert = json.loads(raw)
    tail = cert["prime_tail"]
    cutoff = tail["cutoff"]
    expected = []
    for n in range(2, cutoff+1):
        factors = factor(n)
        if len(factors) == 1:
            p, a = next(iter(factors.items()))
            expected.append([n, p, a])
    stored = tail["complete_prime_powers"]
    histogram = dict(sorted(Counter(a for _, _, a in expected).items()))
    lo, hi = Fraction(56, 81), Fraction(25, 36)
    allowance = Fraction(1, 2**114)
    degrees = list(range(1, 68))
    accepted_degrees = [n for n in degrees if Fraction(819200, 4**n) <= allowance]
    cutoff_tests = [
        {"k": k, "rational_lower": str(k*k*lo - 122 - Fraction(k, 2)),
         "rational_upper": str(k*k*hi - 122 - Fraction(k, 2)),
         "verdict": "accept" if k*k*lo >= 122+Fraction(k, 2) else
                    "reject" if k*k*hi < 122+Fraction(k, 2) else "undecided"}
        for k in range(2, 15)
    ]
    nodes = 128*67
    cost = nodes*len(expected)
    prime_cost = nodes*histogram[1]
    checks = {
        "specified_cutoff": cutoff == 2**14,
        "all_16383_integers_factored": cutoff-1 == 16383,
        "complete_tuple_list_matches": stored == expected,
        "unique_strictly_ordered_values": [x[0] for x in stored] == sorted({x[0] for x in stored}),
        "all_stored_bases_and_exponents_exact": all(p**a == n and factor(p) == {p: 1} for n, p, a in stored),
        "histogram_matches": {str(k): v for k, v in histogram.items()} == tail["by_exponent"],
        "counts_match": len(expected) == tail["prime_power_count"] == 1961 and histogram[1] == tail["prime_count"] == 1900,
        "first_accepted_degree_67": accepted_degrees == [67],
        "first_accepted_cutoff_14": [t["verdict"] for t in cutoff_tests] == ["reject"]*12+["accept"],
        "stored_degree_and_nodes_match": cert["quadrature"]["degree"] == 67 and cert["quadrature"]["panels"] == 128 and cert["quadrature"]["rho"] == 2 and cert["quadrature"]["nodes"] == nodes,
        "stored_quadrature_rationals_match": Fraction(cert["quadrature"]["error_allowance"]) == Fraction(819200, 4**67) and Fraction(cert["quadrature"]["required"]) == allowance,
        "stored_cutoff_exponent_matches": tail["least_accepted_dyadic_exponent"] == 14,
        "stored_log_bounds_match": cert["log2_bounds"] == {"lower": str(lo), "upper": str(hi)},
        "ellipse_strip": Fraction(3, 2)*hi < Fraction(11, 10),
        "cosine_lower_bound": 1-Fraction(11, 10)**2/2 == Fraction(79, 200),
        "cancellation_majorant": 34**2*200 < 64**2*79,
        "cost_and_excess_match": cert["cost"]["actual_prime_terms_one_width_one_mass"] == cost == 16817536 and cert["cost"]["excess"] == cost-10**7,
        "aggregate_threshold_matches": cert["cost"]["required_aggregate_maximum"] == 10**7,
        "both_cost_counts_exceed_budget": cost > 10**7 and prime_cost > 10**7,
        "all_original_checks_true": all(x is True for x in cert["checks"].values()),
    }
    failures = [name for name, ok in checks.items() if not ok]
    output = {
        "input": str(source), "input_sha256": sha256(raw).hexdigest(),
        "scope": "Exact full certificate audit only; analytic proof is canonical in C033u.",
        "checks": checks, "failures": failures,
        "complete_expected_prime_powers": expected,
        "by_exponent": histogram, "dyadic_tests": cutoff_tests,
        "quadrature": {"first_accepted_degree": accepted_degrees[0], "nodes": nodes,
                       "actual_bound": str(Fraction(819200, 4**67)), "required_bound": str(allowance)},
        "cost": {"prime_powers": cost, "primes_only": prime_cost,
                 "required_maximum": 10**7, "excess": cost-10**7},
        "not_certified": cert["not_certified"],
    }
    path = Path(__file__).with_suffix(".json")
    path.write_text(json.dumps(output, indent=2)+"\n")
    print(f"Complete tuples: {len(stored)} checked; every integer 2..{cutoff} factored")
    print(f"Gauss allowance: {Fraction(819200, 4**67)}; required <= {allowance}")
    print(f"Cost: {cost}; primes only: {prime_cost}; required <= {10**7}: FAIL")
    print(f"Audit checks: {len(checks)-len(failures)}/{len(checks)}; failures: {failures}")
    print(f"Full certificate: {path}")
    assert not failures


if __name__ == "__main__":
    main()
