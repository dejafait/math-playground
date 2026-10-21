"""Exact certificate for the prescribed Derksen A(965,10,9) bound."""
import json
from math import comb, isqrt
from pathlib import Path

def factors(n):
    result = []
    for d in range(2, isqrt(n) + 1):
        if n % d == 0:
            exponent = 0
            while n % d == 0:
                n //= d
                exponent += 1
            result.append([d, exponent])
        if n == 1:
            break
    if n > 1:
        result.append([n, 1])
    return result

n, h, w, q = 965, 4, 9, 967
factorizations = {str(v): factors(v) for v in range(n - 1, q + 1)}
trial = {str(d): q % d for d in range(2, isqrt(q) + 1)}
N = comb(n, w)
D = (q - 1) ** (q - n) * (q * q - 1) ** ((n + h - q) // 2)
floor, remainder = divmod(N, D)
bound = floor + int(remainder > 0)
benchmark = 19800269675
checks = {
    "n_minus_one_not_prime_power": len(factorizations[str(n-1)]) > 1,
    "earlier_integers_not_prime_powers": all(len(factorizations[str(v)]) > 1 for v in range(n,q)),
    "q_prime_complete_trial_division": all(trial.values()),
    "degree_hypothesis": 0 < h < q,
    "distance": 2*h+2 == 10,
    "weight": 0 <= w <= n,
    "close_field_even_case": n < q < n+h and (n+h-q) % 2 == 0,
    "denominator": D == 872582977728,
    "euclidean_identity": N == floor*D + remainder and 0 < remainder < D,
    "ceiling": (bound-1)*D < N <= bound*D,
    "below_benchmark": bound < benchmark,
}
certificate = {
    "parameters": {"n":n,"h":h,"w":w,"q":q},
    "factorizations": factorizations,
    "q_primality_trial_remainders": trial,
    "branch": "n<q<n+h; n+h-q=2 even",
    "arithmetic": {"numerator":N,"denominator":D,"floor":floor,"remainder":remainder,"ceiling":bound,"benchmark":benchmark,"shortfall":benchmark-bound},
    "checks": checks,
    "failures": [name for name, good in checks.items() if not good],
}
output = Path(__file__).with_name("derksen-bound-results.json")
output.write_text(json.dumps(certificate, indent=2) + "\n")
# Reload and inspect the complete certificate, including every trial and check.
saved = json.loads(output.read_text())
assert saved == certificate
assert not saved["failures"]
print(f"checks: {len(checks)} passed; failures: {saved['failures']}")
print(f"actual lower bound: {bound}; required strict bound: >{benchmark}")
print(f"numerator: {N}; denominator: {D}; remainder: {remainder}")
print(f"certificate: {output}")
