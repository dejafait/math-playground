"""Exact endpoint/normalization checks for L093, not a probe asymptotic."""
from fractions import Fraction as F
from pathlib import Path
import json

from check_other_other_gradient_lift import multiply, transpose, serialize


def subtract(a, b):
    return [[x - y for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def main():
    records, failures = [], []
    for n_mesh in (2, 4, 6, 10):
        n = n_mesh - 1
        b = [[F(ell < s) for ell in range(n_mesh)] for s in range(1, n_mesh)]
        b0 = [[F((ell == s) - (ell == s - 1)) for ell in range(n_mesh)]
              for s in range(1, n_mesh)]
        avg = [[F((ell == s) + (ell == s - 1), 2) for ell in range(n_mesh)]
               for s in range(1, n_mesh)]
        derivative = [[-x for x in row] for row in transpose(b0)]
        central = multiply(avg, derivative)
        prefix_avg = multiply(b, transpose(avg))
        hav = [[F(2 * (i == j) + (i + 1 == j) + (i == j + 1), 4)
                for j in range(n)] for i in range(n)]
        boundary = [[F(j == 0, 2) for j in range(n)] for _ in range(n)]
        prefix_error = subtract(multiply(prefix_avg, central), subtract(hav, boundary))
        for profile in ("pinned_coefficient", "nonzero_lower_coefficient"):
            u = [F((j - 1) * (n - j) if profile == "pinned_coefficient" else j * j + 2 * j,
                   n_mesh * n_mesh) for j in range(1, n_mesh)]
            diag = [[u[i] if i == j else F(0) for j in range(n)] for i in range(n)]
            comm = subtract(multiply(diag, central), multiply(central, diag))
            rhs_local = multiply(subtract(hav, boundary), diag)
            rhs_comm = multiply(prefix_avg, comm)
            rhs = [[x + y for x, y in zip(ar, br)] for ar, br in zip(rhs_local, rhs_comm)]
            error = subtract(multiply(multiply(prefix_avg, diag), central), rhs)
            required_schur = max((abs(y - x) for x, y in zip(u, u[1:])), default=F(0))
            actual_schur = max([sum(map(abs, row), F(0)) for row in comm + transpose(comm)])
            values = [x for matrix in (prefix_error, error) for row in matrix for x in row]
            maximum = max(map(abs, values))
            record = dict(kind="prefix", N=n_mesh, profile=profile,
                          coefficients=list(map(str, u)), lower_coefficient=str(u[0]),
                          actual_max_error=str(maximum), required_max_error="0",
                          actual_schur_bound=str(actual_schur),
                          required_schur_bound=str(required_schur),
                          prefix_error=serialize(prefix_error), commutator_error=serialize(error))
            records.append(record)
            if maximum or actual_schur > required_schur:
                failures.append(dict(kind="prefix", N=n_mesh, profile=profile))

        ld, le = multiply(b0, transpose(b0)), multiply(transpose(b0), b0)
        for t in (F(1), F(3)):
            # One full transverse gradient mode with incidence t and energy t^2.
            gradient = [[t * F(i == j) for j in range(n)] for i in range(n)] + transpose(b0)
            size = n + n_mesh
            delta = [[F(0) for _ in range(size)] for _ in range(size)]
            for i in range(n):
                for j in range(n):
                    delta[i][j] = ld[i][j] + t * t * F(i == j)
            for i in range(n_mesh):
                for j in range(n_mesh):
                    delta[n + i][n + j] = le[i][j] + t * t * F(i == j)
            curl_energy = subtract(delta, multiply(gradient, transpose(gradient)))
            c = [[x / t for x in row] for row in b]
            left = multiply(c, curl_energy[n:])
            hg = [[F(i == j) for j in range(n)] + [t * x for x in b[i]] for i in range(n)]
            error = subtract(left, hg)
            maximum = max(abs(x) for row in error for x in row)
            records.append(dict(kind="generator_row", N=n_mesh, transverse_incidence=str(t),
                                actual_max_error=str(maximum), required_max_error="0",
                                row_error=serialize(error)))
            if maximum:
                failures.append(dict(kind="generator_row", N=n_mesh, transverse_incidence=str(t)))
    maximum = max(F(record["actual_max_error"]) for record in records)
    summary = dict(cases=len(records), actual_max_error=str(maximum), required_max_error="0",
                   failures=len(failures), all_schur_bounds_passed=not failures)
    path = Path(__file__).with_name("other-other-prefix-generator-certificate.json")
    path.write_text(json.dumps(dict(arithmetic="exact fractions", summary=summary,
                                   cases=records, failures=failures), indent=2) + "\n")
    print(f"cases={len(records)}; actual_max_error={maximum}; required_max_error=0; "
          f"Schur bounds passed={not failures}; failures={len(failures)}; certificate={path}")
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
