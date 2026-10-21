"""Bounded floating-point screen of the leading six-state transport test.

This is not an interval certificate, an actual-height average, or a proof
that the discontinuous basis commutes with the H limit. Full grid summaries
and the algorithm are retained for inspection.
"""
import json
from pathlib import Path
import numpy as np

K = np.array([[1., 0., -1/12], [0., 1/12, 0.], [-1/12, 0., 1/80]])
eigenvalues, eigenvectors = np.linalg.eigh(K)
SK = (eigenvectors * np.sqrt(eigenvalues)) @ eigenvectors.T


def rotate_to_mean(A):
    n = A.shape[0]
    tau = np.trace(A) / n
    diagonal = np.diag(A)
    equal = np.flatnonzero(diagonal == tau)
    if len(equal):
        i = int(equal[0])
        first = np.eye(n)[:, i]
        rest = np.eye(n)[:, [j for j in range(n) if j != i]]
    else:
        i, j = next((i, j) for i in range(n) for j in range(n)
                    if diagonal[i] < tau < diagonal[j])
        off = A[i, j]
        lo, hi = tau-diagonal[i], diagonal[j]-tau
        rad = np.sqrt(off*off+hi*lo)
        eta = lo/(rad+off) if off >= 0 else (rad-off)/hi
        first = (np.eye(n)[:, i]+eta*np.eye(n)[:, j])/np.hypot(1, eta)
        second = (-eta*np.eye(n)[:, i]+np.eye(n)[:, j])/np.hypot(1, eta)
        rest = np.column_stack([second] + [np.eye(n)[:, k]
                                         for k in range(n) if k not in (i, j)])
    if n == 2:
        return np.column_stack([first, rest])
    return np.column_stack([first, rest @ rotate_to_mean(rest.T @ A @ rest)])


def transport(v):
    a, b, d = v[..., 0], v[..., 1], v[..., 2]
    return np.exp(-a*a-b*b)*(b*b*(1-2*a*a)+a*d*(1-2*b*b))


phase_count = 2048
phases = (np.arange(phase_count)+.5)*2*np.pi/phase_count
vectors = []
max_diagonal_error = 0.
F = np.array([[0., 0., -.5], [0., 1., 0.], [-.5, 0., 0.]])
for angle in phases:
    aa, hh = np.cos(angle), np.sin(angle)
    bv = np.array([aa/4, -hh, -aa])
    J = np.outer(bv, bv)-F  # 4 C = 1 after c^2 W is removed
    A = SK @ J @ SK
    basis = rotate_to_mean(A)
    max_diagonal_error = max(max_diagonal_error,
                            float(np.max(np.abs(np.diag(basis.T @ A @ basis)-np.trace(A)/3))))
    vectors.append((np.sqrt(3)*SK @ basis).T)
vectors = np.array(vectors)
rows = []
for g in np.geomspace(.001, 100., 101):
    values = transport(np.sqrt(g)*vectors).mean(axis=1)
    rows.append(dict(g=float(g), phase_mean=float(values.mean()),
                     phase_min=float(values.min()), phase_max=float(values.max()),
                     phase_mean_first_half=float(values[:phase_count//2].mean())))
result = dict(status="EXPLORATORY_NOT_PROOF", phase_count=phase_count,
              hypotheses="Leading J only; Sigma/ell=g K; m=0; no actual-height averaging",
              required="Nonvanishing actual full-law defect beyond complete transport budget",
              failures=["No rigorous quadrature remainder", "No branch-transition limit control",
                        "No actual response-modulus distribution or actual-height average"],
              max_diagonal_residual=max_diagonal_error, rows=rows)
path = Path(__file__).with_name("gaussian-jet-transport-exploration.json")
path.write_text(json.dumps(result, indent=2)+"\n")
means = [r['phase_mean'] for r in rows]
print(json.dumps(dict(status=result['status'], g_range=[.001,100.],
                      phase_mean_range=[min(means),max(means)],
                      max_diagonal_residual=max_diagonal_error,
                      required=result['required'], failures=result['failures'], path=str(path))))
