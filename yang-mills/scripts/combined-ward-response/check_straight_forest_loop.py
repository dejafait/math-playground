"""Independent finite covariance checks for L026; the proof is analytic.

Dense incidence checks use small meshes, whether or not the Ward generator's
supported stencil is admitted. Spectral samples use the same relative box at
larger meshes. No probe contraction or full cutoff coefficient is evaluated.
Writes a full certificate and prints bounds, failures, and its path.
"""

import json
from itertools import combinations, product
from pathlib import Path

import numpy as np


def shifted(v, mu):
    w = list(v)
    w[mu] += 1
    return tuple(w)


def dense_check(n):
    def interior(v):
        return all(0 < k < n for k in v)

    vertices = list(product(range(n + 1), repeat=4))
    iv = [v for v in vertices if interior(v)]
    vi = {v: k for k, v in enumerate(iv)}
    edges = [(mu, v) for mu in range(4) for v in vertices if v[mu] < n
             and (interior(v) or interior(shifted(v, mu)))]
    ei = {e: k for k, e in enumerate(edges)}
    faces = [(mu, nu, v) for mu, nu in combinations(range(4), 2)
             for v in vertices if v[mu] < n and v[nu] < n
             and all(0 < v[r] < n for r in range(4) if r not in (mu, nu))]
    d0 = np.zeros((len(edges), len(iv)))
    for k, (mu, v) in enumerate(edges):
        if v in vi:
            d0[k, vi[v]] -= 1
        if shifted(v, mu) in vi:
            d0[k, vi[shifted(v, mu)]] += 1
    d1 = np.zeros((len(faces), len(edges)))
    traversals = []
    for k, (mu, nu, v) in enumerate(faces):
        signed = [((mu, v), 1), ((nu, shifted(v, mu)), 1),
                  ((mu, shifted(v, nu)), -1), ((nu, v), -1)]
        traversals.append(signed)
        for e, sign in signed:
            if e in ei:
                d1[k, ei[e]] = sign
    delta = d1.T @ d1 + d0 @ d0.T
    sigma = np.linalg.inv(delta)
    path = np.zeros((len(iv), len(edges)))
    for v, k in vi.items():
        for ell in range(v[0]):
            tail = (ell, *v[1:])
            path[k, ei[(0, tail)]] = 1
    retract = np.eye(len(edges)) - d0 @ path
    remaining = [k for k, (mu, v) in enumerate(edges)
                 if mu != 0 or v[0] == n - 1]
    restricted = d1[:, remaining]
    sigma_f = np.linalg.inv(restricted.T @ restricted)
    lifted = retract @ sigma @ retract.T
    direct = np.zeros_like(lifted)
    direct[np.ix_(remaining, remaining)] = sigma_f
    max_lift_error = float(np.max(np.abs(lifted - direct)))
    max_complex_error = float(np.max(np.abs(d1 @ d0)))
    eigenvalues = np.linalg.eigvalsh(delta)
    edge_values = []
    failures = []
    for k, (mu, v) in enumerate(edges):
        if mu == 0 or not (interior(v) and interior(shifted(v, mu))):
            continue
        j = v[0]
        direct_variance = float(sigma[k, k])
        total = float(direct[k, k])
        path_row = (d0 @ path)[k]
        path_variance = float(path_row @ sigma @ path_row)
        bounds = [j / 8, j + 8]
        ok = (bounds[0] - 1e-10 <= total <= bounds[1] + 1e-10
              and path_variance <= j + 1e-10 and direct_variance <= 8 + 1e-10
              and abs(total - direct_variance - path_variance) < 1e-10
              and abs(float(path_row @ path_row) - 2 * j) < 1e-10)
        edge_values.append({"direction_1based": mu + 1, "tail": list(v),
                            "variance": total, "direct_variance": direct_variance,
                            "path_variance": path_variance, "required_bounds": bounds,
                            "passed": bool(ok)})
        if not ok:
            failures.append({"edge": [mu, list(v)]})
    face_values = []
    for face, signed in zip(faces, traversals):
        mu, nu, v = face
        corners = [v, shifted(v, mu), shifted(v, nu), shifted(shifted(v, mu), nu)]
        if not all(interior(w) for w in corners):
            continue
        jp = np.zeros((4, len(edges)))
        for row, (e, sign) in enumerate(signed):
            jp[row, ei[e]] = sign
        cp = jp @ direct @ jp.T
        norm = float(np.linalg.eigvalsh(cp)[-1])
        j = v[0]
        bounds = [j / 8, 4 * (j + 9)]
        ok = bounds[0] - 1e-10 <= norm <= bounds[1] + 1e-10
        face_values.append({"plane_1based": [mu + 1, nu + 1], "tail": list(v),
                            "one_color_norm": norm, "required_bounds": bounds,
                            "passed": bool(ok)})
        if not ok:
            failures.append({"face": [mu, nu, list(v)]})
    identity_ok = (max_lift_error < 1e-10 and max_complex_error == 0
                   and eigenvalues[0] > 0 and eigenvalues[-1] <= 16 + 1e-10)
    if not identity_ok:
        failures.append({"identity": "lift/complex/spectrum"})
    summary = {"N": n, "edge_checks": len(edge_values), "face_checks": len(face_values),
               "lift_max_error": max_lift_error, "complex_max_error": max_complex_error,
               "laplacian_eigenvalue_range": [float(eigenvalues[0]), float(eigenvalues[-1])],
               "required_eigenvalue_range": [0, 16], "failures": failures,
               "passed": not failures}
    return summary, {"summary": summary, "edges": edge_values, "faces": face_values}


def spectral_sample(n):
    """Compute an interior direction-2 edge at j=N/2 by tensor modes."""
    j = n // 2
    tail = (j, j, j, j)
    eigen = 4 * np.sin(np.pi * np.arange(n) / (2 * n)) ** 2
    ks = [np.arange(n), *[np.arange(1, n) for _ in range(3)]]
    axial_weights = np.empty(n)
    for k in range(n):
        e = (np.ones(n) / np.sqrt(n) if k == 0 else
             np.sqrt(2 / n) * np.cos(np.pi * k * (np.arange(n) + .5) / n))
        axial_weights[k] = np.sum(e[:j]) ** 2
    transverse_difference = (np.sqrt(2 / n) *
                             (np.sin(np.pi * ks[1] * (j + 1) / n)
                              - np.sin(np.pi * ks[1] * j / n))) ** 2
    path_weights = [axial_weights, transverse_difference,
                    *[(np.sqrt(2 / n) * np.sin(np.pi * k * j / n)) ** 2 for k in ks[2:]]]
    path_eigen = sum(eigen[k].reshape(tuple(-1 if r == axis else 1 for r in range(4)))
                     for axis, k in enumerate(ks))
    path_numerator = np.ones(tuple(len(k) for k in ks))
    for axis, weight in enumerate(path_weights):
        path_numerator *= weight.reshape(tuple(-1 if r == axis else 1 for r in range(4)))
    path_variance = float(np.sum(path_numerator / path_eigen))
    direct_ks = [np.arange(1, n), np.arange(n), np.arange(1, n), np.arange(1, n)]
    direct_numerator = np.ones(tuple(len(k) for k in direct_ks))
    direct_eigen = np.zeros_like(direct_numerator)
    for axis, k in enumerate(direct_ks):
        shape = tuple(-1 if r == axis else 1 for r in range(4))
        if axis == 1:
            wave = np.sqrt(2 / n) * np.cos(np.pi * k * (j + .5) / n)
            wave[0] = 1 / np.sqrt(n)
        else:
            wave = np.sqrt(2 / n) * np.sin(np.pi * k * j / n)
        direct_numerator *= (wave ** 2).reshape(shape)
        direct_eigen += eigen[k].reshape(shape)
    direct_variance = float(np.sum(direct_numerator / direct_eigen))
    total = path_variance + direct_variance
    bounds = [j / 8, j + 8]
    ok = (bounds[0] <= total <= bounds[1] and path_variance <= j + 1e-10
          and direct_variance <= 8 and abs(np.sum(path_numerator) - 2 * j) < 1e-9)
    return {"N": n, "tail": list(tail), "variance": total,
            "path_variance": path_variance, "direct_variance": direct_variance,
            "variance_over_N": total / n, "required_bounds": bounds,
            "path_row_norm_squared": float(np.sum(path_numerator)),
            "required_path_row_norm_squared": 2 * j, "passed": bool(ok)}


def main():
    summaries, dense = [], []
    for n in (2, 4):
        summary, full = dense_check(n)
        summaries.append(summary)
        dense.append(full)
    samples = [spectral_sample(n) for n in (4, 8, 16, 32)]
    selected = next(row for row in dense[1]["edges"]
                    if row["direction_1based"] == 2 and row["tail"] == [2, 2, 2, 2])
    comparison_error = abs(selected["variance"] - samples[0]["variance"])
    comparison = {"dense_spectral_variance_error": comparison_error,
                  "required_error_less_than": 1e-10, "passed": comparison_error < 1e-10}
    checks = [*summaries, *samples, comparison]
    failures = [k for k, check in enumerate(checks) if not check["passed"]]
    result = {"qualification": "Finite checks support L026's analytic proof; no full response computed.",
              "checks": checks, "dense_full": dense, "failures": failures}
    destination = Path(__file__).with_name("straight-forest-loop-certificate.json")
    destination.write_text(json.dumps(result, indent=2) + "\n")
    for check in summaries:
        print(f"N={check['N']}: {check['edge_checks']} edge and {check['face_checks']} face bounds; "
              f"lift error {check['lift_max_error']:.3g}; passed={check['passed']}")
    for sample in samples:
        print(f"N={sample['N']}: variance={sample['variance']:.9g}, "
              f"required={sample['required_bounds']}, passed={sample['passed']}")
    print(f"Failures={failures}; certificate={destination}")
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
