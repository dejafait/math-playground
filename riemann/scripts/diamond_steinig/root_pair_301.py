"""Exact finite checks for C999a; its general rate proof is in the lemma."""
from fractions import Fraction
from math import factorial
from pathlib import Path
import json

from collected_mass_299 import exact


def add_term(poly, parts, value):
    poly[parts] = poly.get(parts, Fraction(0)) + value
    if not poly[parts]:
        del poly[parts]


def product(left, right):
    result = {}
    for p, cp in left.items():
        for q, cq in right.items():
            add_term(result, tuple(sorted(p + q)), cp * cq)
    return result


def newton_polynomial(n):
    # E'/E=-sum_(m>=1) p_m*t^(m-1); compare coefficients of E'.
    # p_m=-m*a_m-sum_(j=1)^(m-1) a_j*p_(m-j), a_j=Y_j/j!.
    powers = {}
    for m in range(1, 2 * n + 1):
        current = {(m,): Fraction(-m, factorial(m))}
        for j in range(1, m):
            for parts, value in powers[m - j].items():
                add_term(current, tuple(sorted((j,) + parts)),
                         -value / factorial(j))
        powers[m] = current
    result = product(powers[n], powers[n])
    for parts, value in powers[2 * n].items():
        add_term(result, parts, -value)
    return result


def partition_count(m):
    counts = [1] + [0] * m
    for part in range(1, m + 1):
        for total in range(part, m + 1):
            counts[total] += counts[total - part]
    return counts[m]


def rows(poly):
    return [{"parts": list(parts), "coefficient": str(value)}
            for parts, value in sorted(poly.items())]


def main():
    failures = []
    scalar_bound = Fraction(97, 9) + Fraction(4, 9) / (1 - Fraction(4, 25))
    pair_squared_bound = scalar_bound / 16
    if not (scalar_bound == Fraction(2137, 189) < 12 < 16
            and pair_squared_bound < Fraction(3, 4) < 1):
        failures.append("Scalar root-pair threshold failed")
    checks = []
    for n in range(1, 9):
        direct_row = exact(n)
        direct = {tuple(row["parts"]): Fraction(row["value"])
                  for row in direct_row["coefficients"] if Fraction(row["value"])}
        full = newton_polynomial(n)
        retained = {p: c for p, c in full.items() if len(p) <= n}
        differences = {}
        for parts in direct.keys() | retained.keys():
            add_term(differences, parts,
                     direct.get(parts, Fraction(0)) - retained.get(parts, Fraction(0)))
        mass = sum(map(abs, retained.values()), Fraction(0))
        count = partition_count(2 * n)
        squared_bound = (2 * n * (2 * n - 1) * count) ** 2 * Fraction(3, 4) ** n
        valid = (not differences and mass == Fraction(direct_row["C_n"])
                 and mass > 0 and mass ** 2 <= squared_bound
                 and all(sum(p) == 2 * n for p in full)
                 and len(retained) <= count)
        if not valid:
            failures.append(f"n={n}: identity, support or finite bound failed")
        checks.append({
            "n": n, "actual_C_n": str(mass), "partition_count": count,
            "actual_C_n_squared": str(mass ** 2),
            "required_upper_bound_squared": str(squared_bound),
            "complete_newton_polynomial": rows(full),
            "complete_retained_polynomial": rows(retained),
            "complete_direct_polynomial": rows(direct),
            "complete_coefficient_differences": rows(differences),
            "direct_ordered_pairs": direct_row["ordered_pairs"],
            "all_checks_pass": valid,
        })
    path = Path(__file__).with_name("root_pair_301_certificate.json")
    path.write_text(json.dumps({
        "scope": "Exact finite checks only; C999a supplies the all-n proof",
        "scalar_series_upper_bound": str(scalar_bound),
        "required_scalar_bound_for_contraction": "16",
        "certified_stronger_scalar_bound": "12",
        "pair_modulus_squared_upper_bound": str(pair_squared_bound),
        "chosen_rho_squared": "3/4",
        "required_asymptotic_log_max_rate": "0",
        "checks": checks, "failures": failures,
    }, indent=2) + "\n")
    print(f"Scalar series <= {scalar_bound} < 12 < 16 (contraction threshold).")
    print(f"Pair modulus squared <= {pair_squared_bound} < rho^2=3/4 < 1.")
    for row in checks:
        print(f"n={row['n']}: C_n={row['actual_C_n']}; full coefficient identity, "
              f"support and squared upper bound pass={row['all_checks_pass']}")
    print("Required asymptotic rate: 0; finite checks do not prove a rate.")
    print(f"Failures: {len(failures)}. Certificate: {path}")
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
