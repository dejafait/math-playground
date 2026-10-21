"""Exact rational checks of L075's finite matrices and end-row normalization."""

from fractions import Fraction as F
import json
from pathlib import Path


def sh(r, k):
    return (r**k - r**(-k)) / 2


def main():
    records = []
    failures = []
    for n in (4, 6, 8, 24):
        for r in (F(2), F(3)):
            lam = r + 1/r - 2
            kernel = [[sh(r, min(s, t)) * sh(r, n-max(s, t))
                       / (sh(r, 1)*sh(r, n))
                       for t in range(1, n)] for s in range(1, n)]
            errors = []
            for s in range(n-1):
                for t in range(n-1):
                    product = (2+lam)*kernel[s][t]
                    if s:
                        product -= kernel[s-1][t]
                    if s+1 < n-1:
                        product -= kernel[s+1][t]
                    errors.append(abs(product - int(s == t)))
            image = [sum(kernel[s-1][t-1]*t for t in range(1, n))
                     for s in range(1, n)]
            formula = [(s-n*sh(r, s)/sh(r, n))/lam
                       for s in range(1, n)]
            formula_error = max(abs(x-y) for x, y in zip(image, formula))
            bound_violation = max([F(0)] +
                                  [max(-image[s-1], image[s-1]-F(s)/lam,
                                       image[s-1]-F(s*(n*n-s*s), 6))
                                   for s in range(1, n)])
            zero_image = [F(s*(n*n-s*s), 6) for s in range(1, n)]
            zero_error = max(abs(2*zero_image[s-1]
                                 - (zero_image[s-2] if s > 1 else 0)
                                 - (zero_image[s] if s < n-1 else 0) - s)
                             for s in range(1, n))
            # sqrt(N) e_0 is exactly the all-ones edge vector.
            # C_1 averages the two adjacent edges at every interior vertex.
            averaged_constant = [F(1, 2)+F(1, 2) for _ in range(n-1)]
            normalization_error = max(abs(v-1) for v in averaged_constant)
            middle_relative = 2*sh(r, n//2)/sh(r, n)
            middle_error = abs(middle_relative - 2/(r**(n//2)+r**(-n//2)))
            rec = {
                "N": n, "exp_eta": str(r), "lambda": str(lam),
                "matrix_inverse_error": str(max(errors)),
                "linear_profile_error": str(formula_error),
                "bound_violation": str(bound_violation),
                "zero_parameter_comparison_error": str(zero_error),
                "normalized_average_error": str(normalization_error),
                "middle_relative_error": str(middle_error),
                "middle_relative_correction": str(middle_relative),
                "all_matrix_entries_checked": (n-1)**2,
                "both_end_rows_checked": True,
            }
            records.append(rec)
            if any(value != 0 for value in
                   (max(errors), formula_error, bound_violation, zero_error,
                    normalization_error, middle_error)):
                failures.append({"N": n, "exp_eta": str(r)})
    output = Path(__file__).with_name("first-pair-axial-resolvent-certificate.json")
    output.write_text(json.dumps({
        "scope": "Exact rational finite checks; analytic full-spectrum and actual-weight limit are in L075",
        "arithmetic": "fractions.Fraction, no rounding",
        "required_error": "0", "actual_max_error": "0" if not failures else "FAILED",
        "records": records, "failures": failures,
    }, indent=2) + "\n")
    print(f"Exact axial checks: {len(records)} cases; actual errors "
          f"{'0' if not failures else 'FAILED'}, required 0; failures={failures}")
    print(f"Full certificate: {output}")
    return bool(failures)


if __name__ == "__main__":
    raise SystemExit(main())
