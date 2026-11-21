"""Exact finite preflight for C033u; no quadrature or observable evaluation."""
from fractions import Fraction
from math import isqrt
from pathlib import Path
import json


def main():
    log_lo = Fraction(56, 81)
    log_hi = Fraction(25, 36)
    budget = 10**7
    panels = 128
    degree = 67
    cutoff = 2**14
    # Sieve plus an independent trial-division characterization of prime powers.
    prime = bytearray(b"\x01") * (cutoff + 1)
    prime[0:2] = b"\x00\x00"
    for p in range(2, isqrt(cutoff) + 1):
        if prime[p]:
            for n in range(p*p, cutoff + 1, p):
                prime[n] = 0
    primes = [p for p in range(2, cutoff + 1) if prime[p]]
    powers = {}
    for p in primes:
        n, a = p, 1
        while n <= cutoff:
            assert n not in powers
            powers[n] = [p, a]
            n *= p
            a += 1

    independent = []
    for n in range(2, cutoff + 1):
        divisor = next((d for d in range(2, isqrt(n) + 1) if n % d == 0), n)
        remainder = n
        while remainder % divisor == 0:
            remainder //= divisor
        if remainder == 1:
            independent.append(n)
    assert independent == sorted(powers)

    q_error = Fraction(819200, 4**degree)
    allocation = Fraction(1, 2**114)
    counts = {str(a): sum(1 for _, exponent in powers.values() if exponent == a)
              for a in sorted({a for _, a in powers.values()})}
    nodes = panels * degree
    prime_terms = nodes * len(powers)
    checks = {
        "log_bounds_ordered": Fraction(69,100) < log_lo < log_hi < Fraction(7,10),
        "ellipse_inside_strip": Fraction(3,2)*log_hi < Fraction(11,10),
        "cos_lower_positive": 1-Fraction(11,10)**2/2 == Fraction(79,200),
        "difference_majorant_below_64": 34**2*200 < 64**2*79,
        "outer_quadrature_passes": q_error < allocation,
        "degree_66_rejected_by_displayed_allowance": Fraction(819200,4**66) > allocation,
        "cutoff_14_accepted": 14**2*log_lo > 122+Fraction(14,2),
        "all_lower_dyadic_cutoffs_rejected": all(k*k*log_hi < 122+Fraction(k,2) for k in range(2,14)),
        "independent_prime_power_count_matches": independent == sorted(powers),
        "prime_cost_alone_exceeds_budget": prime_terms > budget,
    }
    assert all(checks.values())
    certificate = {
        "scope": "Uniform dyadic prime cutoff at every node of the declared ellipse rule; sufficient certificate only.",
        "log2_bounds": {"lower": str(log_lo), "upper": str(log_hi)},
        "quadrature": {"panels": panels, "rho": 2, "degree": degree, "nodes": nodes,
                       "error_allowance": str(q_error), "required": str(allocation)},
        "prime_tail": {"cutoff": cutoff, "least_accepted_dyadic_exponent": 14,
                       "acceptance_test": "k^2*log(2) >= 122+k/2",
                       "prime_count": len(primes), "prime_power_count": len(powers),
                       "by_exponent": counts,
                       "complete_prime_powers": [[n, *powers[n]] for n in sorted(powers)]},
        "cost": {"actual_prime_terms_one_width_one_mass": prime_terms,
                 "required_aggregate_maximum": budget, "excess": prime_terms-budget,
                 "other_costs_granted_free": ["archimedean quadrature", "other widths", "other scalar integrals", "finite polynomial", "all arithmetic"]},
        "checks": checks,
        "failures": ["Aggregate cost fails before full evaluator or precision certification."],
        "not_certified": ["actual quadrature error", "optimal algorithmic cost", "512-bit implementation", "C033s/t analytic hypotheses", "external zero data", "observable or RH"],
    }
    path = Path(__file__).with_suffix(".json")
    path.write_text(json.dumps(certificate, indent=2) + "\n")
    print(f"Analytic quadrature allowance: {q_error}; required <= {allocation}: PASS")
    print(f"Prime powers <= {cutoff}: {len(powers)}; outer nodes: {nodes}")
    print(f"Prime terms alone: {prime_terms}; aggregate budget: {budget}: FAIL")
    print("Full 512-bit evaluator: NOT CERTIFIED; no numerical observable evaluated")
    print(f"Certificate: {path}")


if __name__ == "__main__":
    main()
