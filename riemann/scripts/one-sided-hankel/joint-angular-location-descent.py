"""Finite, nonrigorous pole-location descent for the approved joint target.

No optimizer package is required. All original residues are one; an anchor
is fixed at zero ordinate, and every other ordinate is paired with its
negative. The descent uses the complete first-M moment vector on a sampled
angular grid. No bound or asymptotic conclusion follows from this script.
"""
import json
from pathlib import Path

import numpy as np

X, R = -1.25, 1.375
U = R * R
BOUND = 0.54


def evaluate(n, positive_y, angular_count, gradient=True):
    ys = np.concatenate(([0.0], positive_y, -positive_y))
    aa = X + 1j * ys
    mass = len(aa)
    angles = np.arange(angular_count) * (2 * np.pi / angular_count)
    u = np.exp(1j * angles)
    w = np.broadcast_to((X / aa)[:, None], (mass, angular_count)).copy()
    ell = np.broadcast_to((1 / aa)[:, None], (mass, angular_count)).copy()
    for j in range(1, n):
        t = j / n
        w *= (X - t * u) / (aa[:, None] - t * u)
        w *= (U * u - t * aa[:, None]) / (U * u - t * X)
        ell += 1 / (aa[:, None] - t * u) + t / (U * u - t * aa[:, None])
    orders = np.arange(mass)
    v = (aa[:, None] / R) ** orders[None, :] / R
    response = w.T @ v
    energy = float(np.mean(np.sum(np.abs(response) ** 2, axis=1)))
    gaps = U - np.abs(aa) ** 2
    diagonal = float(np.mean(np.sum(np.abs(w) ** 2 / gaps[:, None], axis=0)))
    value = float(np.log(energy / diagonal))
    if not gradient:
        return value, energy, diagonal
    # dc_k/dy_a = i W_a (a/R)^k/R * (k/a - ell_a).
    conjugate_response = np.conj(response).T
    base = v @ conjugate_response
    differentiated = (v * (orders[None, :] / aa[:, None])) @ conjugate_response
    ds = 2 * np.real(np.mean(1j * w * (differentiated - ell * base), axis=1))
    dd = np.mean(np.abs(w) ** 2 * (
        2 * np.imag(ell) / gaps[:, None]
        + 2 * ys[:, None] / gaps[:, None] ** 2), axis=1)
    complete_gradient = ds / energy - dd / diagonal
    half = len(positive_y)
    g = complete_gradient[1:half + 1] - complete_gradient[half + 1:]
    return value, energy, diagonal, g


records = []
gradient_checks = []
for n in (99, 195):
    mass, angular_count = n // 3, 512
    half = (mass - 1) // 2
    y = 0.3 * np.cos((2 * np.arange(half) + 1) * np.pi / (2 * mass))
    initial_y = y.copy()
    value, energy, diagonal, g = evaluate(n, y, angular_count)
    for index in (0, half // 2, half - 1):
        h = 1e-6
        yp, ym = y.copy(), y.copy()
        yp[index] += h
        ym[index] -= h
        finite_difference = (evaluate(n, yp, angular_count, False)[0]
                             - evaluate(n, ym, angular_count, False)[0]) / (2 * h)
        gradient_checks.append({
            "n": n, "coordinate": index, "analytic": float(g[index]),
            "centered_difference": float(finite_difference),
            "absolute_error": float(abs(g[index] - finite_difference)),
        })
    history = [{"iteration": 0, "log_ratio": value, "gradient_norm": float(np.linalg.norm(g))}]
    step = 1e-4
    stop = "iteration_limit"
    for iteration in range(1, 101):
        accepted = False
        for backtrack in range(24):
            candidate = np.clip(y - step * g, 0.0, BOUND)
            displacement = candidate - y
            new_value, new_energy, new_diagonal, new_g = evaluate(n, candidate, angular_count)
            if new_value <= value + 1e-4 * np.dot(g, displacement) and np.linalg.norm(displacement) > 0:
                accepted = True
                break
            step *= 0.5
        if not accepted:
            stop = "no_sampled_descent_after_24_backtracks"
            break
        y = candidate
        value, energy, diagonal, g = new_value, new_energy, new_diagonal, new_g
        history.append({"iteration": iteration, "log_ratio": value,
                        "gradient_norm": float(np.linalg.norm(g)), "accepted_step": step})
        step = min(1e-2, step * 1.3)
    comparisons = []
    for count in (1024, 2048):
        f, e, d = evaluate(n, y, count, False)
        comparisons.append({"angular_count": count, "sampled_S_n": e,
                            "sampled_D_single_n": d, "log_ratio": f,
                            "apparent_squared_loss_rate": -f / n,
                            "log_scaled_target_ratio": n / 16 + f})
    row = {"n": n, "M": mass, "angular_count_during_descent": angular_count,
           "required_squared_loss_rate": 1 / 16,
           "initial_positive_ordinates": initial_y.tolist(),
           "final_positive_ordinates": y.tolist(), "descent_stop": stop,
           "history": history, "finer_grid_diagnostics": comparisons}
    records.append(row)
    print('NONRIGOROUS', {'n': n, 'iterations': len(history) - 1, 'stop': stop,
                           **comparisons[-1], 'required_squared_loss_rate': 1 / 16}, flush=True)
output = Path(__file__).with_suffix('.json')
output.write_text(json.dumps({
    "status": "NONRIGOROUS_SCREEN_ONLY", "gradient_checks": gradient_checks,
    "records": records, "limitations": [
        "No floating-point or quadrature enclosures; grid agreement is not a proof.",
        "The numerical descent has no global optimality certificate.",
        "The finite pole lists do not specify an asymptotic countersequence.",
        "Any coincident poles must be merged with their integer residues for formal use.",
        "The first M spatial moments are complete; the target follows only via L651 and a uniform bound.",
    ],
}, indent=2) + '\n')
print('No certified conclusion; full diagnostic:', output)
