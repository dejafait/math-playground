"""Exploratory full-covariance bound for linear-in-second-state storages.

Floating-point output is a probe, not a certificate of incompatibility.
Run from the active notebook: python3 scripts/coupled-flux/completion_probe.py
"""
import json
from pathlib import Path
import numpy as np

out = Path(__file__).with_name("completion_probe.json")
nodes, weights = np.polynomial.legendre.leggauss(32)
u = nodes / 2
weights = weights / 2
spectral = np.stack([(1j * u) ** j * np.exp(1j * r * u)
                     for r in (0, 1) for j in (0, 1, 2)], axis=1)
K = np.real(np.einsum("n,ni,nj->ij", weights, spectral, spectral.conj()))
K0, D = K[:3, :3], K[:3, 3:]
M = np.linalg.solve(K0, D).T
T = K[3:, 3:] - M @ D
theta = 2 * np.pi * np.arange(128) / 128
theta = np.tile(theta, 2)
k = np.repeat([1 / 12, -7 / 60], 128)
p = np.repeat([1 / 6 / 128, 5 / 6 / 128], 128)
x, y = np.sqrt(2) * np.cos(theta), np.sin(theta) / np.sqrt(6)
z = k * x
b0 = np.stack([x, y, z], axis=1)
b1 = b0 @ M.T
alpha = y * (x + 12 * z) / 2
beta = np.sqrt(3) * (x * z - y * y)
hs, labels = [], []
for coordinate in (0, 1):
    for trig in ("cos", "sin"):
        phi = np.cos(3 * theta) if trig == "cos" else np.sin(3 * theta)
        prime = -3 * np.sin(3 * theta) if trig == "cos" else 3 * np.cos(3 * theta)
        derivative = alpha * phi + beta * prime
        h = np.zeros((len(theta), 3))
        h[:, coordinate] = derivative
        h[:, coordinate + 1] = phi
        hs.append(h)
        labels.append(f"r*{trig}(3theta)*{'x1' if coordinate == 0 else 'y1'}")
hs = np.array(hs)
d = np.einsum("n,ani,ni->a", p, hs, b1)
cross = np.einsum("n,ani,nj->aij", p, hs, b0)
projection = np.einsum("aij,jk,nk->ani", cross, np.linalg.inv(K0), b0)
hp = hs - projection
Q = np.einsum("n,ani,ij,bnj->ab", p, hp, T, hp)
c = np.linalg.solve(Q, d)
c /= np.max(np.abs(c))
main = float(d @ c)
bound = float(np.sqrt(3 * c @ Q @ c))
h = np.einsum("a,ani->ni", c, hp)
C = np.einsum("n,ni,nj->ij", p, h, h)
e, v = np.linalg.eigh(T)
sqrtT = (v * np.sqrt(np.maximum(e, 0))) @ v.T
sharp = float(np.sqrt(np.maximum(np.linalg.eigvalsh(sqrtT @ C @ sqrtT), 0)).sum())
result = {
    "status": "EXPLORATORY_FLOATING_POINT_ONLY",
    "method": "Cauchy-Schwarz after removing first-triple linear projection",
    "K": K.tolist(), "regression": M.tolist(), "schur": T.tolist(),
    "schur_eigenvalues": e.tolist(), "storage_basis": labels,
    "main_vector": d.tolist(), "error_quadratic_matrix": Q.tolist(),
    "candidate_coefficients": c.tolist(), "candidate_main": main,
    "candidate_error_bound": bound, "required_main": bound,
    "candidate_nuclear_bound": sharp,
    "ratio": main / bound,
    "fails_to_separate": bool(main <= bound),
    "qualification": "Global homogeneous cutoff and every analytic bound still need proof."
}
out.write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps({key: result[key] for key in
                 ("status", "candidate_main", "candidate_error_bound", "ratio", "fails_to_separate")}))
print(f"Full exploratory evidence: {out}")
