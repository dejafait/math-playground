"""Floating diagnostic of the exact L666 nonnegative cone; not a certificate.

All coefficients, sampled residuals, iteration diagnostics and parameters
are saved. No sampled result proves a continuous norm or an asymptotic rate.
"""
import json
from pathlib import Path
import numpy as np


def family(q, pattern):
    n = 12*q+3
    r = np.arange(-2*q, 2*q)
    k = np.where(r >= 0, r, -r-1)
    if pattern == "zero":
        e = np.zeros(len(r))
    elif pattern == "alternating":
        e = np.sign(r+0.5)*np.where(k % 2 == 0, 0.125, -0.125)
    elif pattern == "alternating_reverse":
        e = -np.sign(r+0.5)*np.where(k % 2 == 0, 0.125, -0.125)
    else:
        raise ValueError(pattern)
    return n, e, (27/(10*n))*(r+0.5+e)


def matrix(n, ys, count):
    x, U = -1.25, 121/64
    u = np.exp(2j*np.pi*np.arange(count)/count)
    t = np.arange(1, n)/n
    first = x-t[:, None]*u[None, :]
    second = U*u[None, :]-t[:, None]*x
    answer = np.empty((count, len(ys)), complex)
    for k, y in enumerate(ys):
        a = x+1j*y
        ratios = (first/(first+1j*y)
                  * (second-t[:, None]*1j*y)/second)
        answer[:, k] = (x/a)*np.prod(ratios, axis=0)
    return answer


def nnls(a, target):
    """Lawson-Hanson active set, with direct least-squares subproblems."""
    cols = a.shape[1]
    active = np.zeros(cols, dtype=bool)
    coeff = np.zeros(cols)
    tolerance = 2e-12
    iterations = 0
    issues = []
    last_singular = []
    while iterations < 12*cols:
        gradient = a.T @ (target-a@coeff)
        available = np.where(~active, gradient, -np.inf)
        if np.max(available) <= tolerance:
            break
        active[np.argmax(available)] = True
        while True:
            trial = np.zeros(cols)
            solution, _, rank, singular = np.linalg.lstsq(
                a[:, active], target, rcond=1e-13)
            trial[active] = solution
            last_singular = singular.tolist()
            iterations += 1
            if rank < np.sum(active):
                issues.append("rank-truncated active least squares")
            if np.all(trial[active] > 0):
                coeff = trial
                break
            invalid = active & (trial <= 0)
            fractions = coeff[invalid]/(coeff[invalid]-trial[invalid])
            step = np.min(fractions)
            coeff += step*(trial-coeff)
            release = active & (coeff <= 1e-14)
            coeff[release] = 0
            active[release] = False
            if iterations >= 12*cols:
                break
        if iterations >= 12*cols:
            issues.append("iteration cap reached")
            break
    residual = a@coeff-target
    gradient = a.T@residual
    return coeff, dict(
        iterations=iterations, active=np.flatnonzero(active).tolist(),
        kkt_negative_gradient=float(max(0, -np.min(gradient))),
        active_gradient=float(np.max(np.abs(gradient[active]))) if np.any(active) else 0,
        minimum_coefficient=float(np.min(coeff)),
        last_active_singular_values=last_singular,
        issues=issues)


rows = []
failures = []
for q in (1, 2, 4, 8, 16):
    for pattern in ("zero", "alternating", "alternating_reverse"):
        n, e, ys = family(q, pattern)
        w = matrix(n, ys, 1024)
        scales = np.sqrt(np.mean(abs(w)**2, axis=0))
        normalized = w/scales
        a = np.concatenate((normalized.real, normalized.imag))/32
        target = np.concatenate((-np.ones(1024), np.zeros(1024)))/32
        coefficients, diagnostics = nnls(a, target)
        b = coefficients/scales
        residual = 1+w@b
        fine_w = matrix(n, ys, 4096)
        fine = 1+fine_w@b
        norm = float(np.sqrt(np.mean(abs(fine)**2)))
        coarse_norm = float(np.sqrt(np.mean(abs(residual)**2)))
        row = dict(q=q, n=n, pattern=pattern, displacements=e.tolist(),
                   ordinates=ys.tolist(), coefficients=b.tolist(),
                   column_norms=scales.tolist(),
                   coarse_count=1024, fine_count=4096,
                   sampled_norm=norm, coarse_sampled_norm=coarse_norm,
                   sampled_loss_excess=(-np.log(norm)-n/100)/np.log(n),
                   sampled_sup=float(np.max(abs(fine))),
                   residual_real=fine.real.tolist(), residual_imag=fine.imag.tolist(),
                   diagnostics=diagnostics)
        rows.append(row)
        if not np.all(np.isfinite(b)) or np.min(b) < 0:
            failures.append(f"q={q}, {pattern}: invalid coefficients")
        if abs(coarse_norm-norm) > 1e-8*max(1, norm):
            failures.append(f"q={q}, {pattern}: mesh mismatch")
        if diagnostics["issues"]:
            failures.append(f"q={q}, {pattern}: solver issue")

path = Path(__file__).with_suffix(".json")
path.write_text(json.dumps(dict(
    status="FLOATING DIAGNOSTIC ONLY; NO CONTINUOUS OR ASYMPTOTIC CERTIFICATE",
    target_rate="1/100 with arbitrary polynomial prefactor and uniform onset",
    failures=failures, rows=rows), indent=2)+"\n")
for row in rows:
    print(f'n={row["n"]}, {row["pattern"]}: sampled norm={row["sampled_norm"]:.9g}, '
          f'excess/log n={row["sampled_loss_excess"]:.6g}, '
          f'active={len(row["diagnostics"]["active"])}')
print(f"Required: unbounded asymptotic excess, with continuous norm proof. Failures: {failures}")
print(f"Full diagnostic: {path}")
