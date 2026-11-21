#!/usr/bin/env python3
"""Unenclosed complete-covariance Schur locator; never a certificate.

Uses analytic exponential Legendre moments, the exact neutral graph
formula, and the full logarithmic/Hankel/reflection action. All matrices
and eigenvalues are saved. Quadrature and the Q_n recurrence are NOT
enclosed; even a positive Schur value proves no sign theorem.
"""
import json
import math
from pathlib import Path

import numpy as np
from numpy.polynomial.legendre import leggauss, legvander

ELL = math.log(3) / 2
D = math.log(2)
A = D / math.sqrt(2)
GAMMA = 0.577215664901532860606512090082402431


def basis(x, degree):
    return legvander(2 * x / ELL - 1, degree) * np.sqrt(
        (2 * np.arange(degree + 1) + 1) / ELL)


def gauss(lo, hi, order):
    x, w = leggauss(order)
    return lo + (x + 1) * (hi - lo) / 2, w * (hi - lo) / 2


def moment_ratios(degree):
    # i_n(t)=t^n/(2n+1)!! times a positive entire series.
    t = ELL / 4
    values = []
    leading = 1.0
    for n in range(degree + 1):
        if n:
            leading *= t / (2 * n + 1)
        term = total = 1.0
        for k in range(32):
            term *= t * t / (2 * (k + 1) * (2 * n + 2 * k + 3))
            total += term
        values.append(leading * total)
    return np.array([math.sqrt((2*n+1)/(2*(n % 2)+1)) *
                     values[n] / values[n % 2] for n in range(degree + 1)])


def carleman_actions(x, degree):
    # Integral p_n(y)/(x+y)dy = 2*(-1)^n*sqrt((2n+1)/ell)*Q_n(1+2x/ell).
    # Continued-fraction backward recurrence. Its finite stopping error is
    # intentionally not certified; extra depth only supplies a locator.
    rows = []
    for value in x:
        z = 1 + 2 * value / ELL
        depth = degree + int(math.ceil(32 / math.acosh(z))) + 32
        ratios = np.empty(degree + 1)
        next_ratio = 0.0
        for n in range(depth, 0, -1):
            next_ratio = n / ((2*n+1)*z - (n+1)*next_ratio)
            if n <= degree:
                ratios[n] = next_ratio
        q = np.empty(degree + 1)
        q[0] = math.log1p(ELL / value) / 2
        for n in range(1, degree + 1):
            q[n] = q[n-1] * ratios[n]
        rows.append(q)
    return 2 * np.array(rows) * ((-1.0)**np.arange(degree+1)) * np.sqrt(
        (2*np.arange(degree+1)+1)/ELL)


def run(degree, order):
    # Split the outer integral at the jump of the full partial reflection.
    x1, w1 = gauss(0, D-ELL, order)
    x2, w2 = gauss(D-ELL, ELL, order)
    x, w = np.r_[x1, x2], np.r_[w1, w2]
    y, wy = gauss(0, ELL, order)
    bx, by = basis(x, degree), basis(y, degree)
    ratios = moment_ratios(degree)
    graph = np.eye(degree+1)[:, 2:]
    for n in range(2, degree+1):
        graph[n % 2, n-2] = -ratios[n]
    head = bx @ graph
    wb = wy[:, None] * by
    dist = np.abs(x[:, None] - y[None, :])
    # No equal quadrature nodes occur generically. Use Taylor near zero.
    regular = np.empty_like(dist)
    small = dist < 1e-5
    regular[small] = 0.5 - dist[small]/24 - dist[small]**2/16
    t = dist[~small]
    regular[~small] = 2*np.exp(-t/2)/(-np.expm1(-2*t)) - 1/t
    summed = x[:, None] + y[None, :]
    hk = np.empty_like(summed)
    small = summed < 1e-5
    # k_1(t)-1/(2t)=-3/4+(23/48)t+O(t^2).
    hk[small] = -0.75 + 23*summed[small]/48
    t = summed[~small]
    hk[~small] = np.exp(-2.5*t)/(-np.expm1(-2*t)) - 1/(2*t)
    hankel = 0.5*carleman_actions(x, degree) + hk @ wb
    reflect = np.zeros_like(bx)
    reflect[len(x1):] = basis(D-x2, degree)
    potential = -GAMMA-math.log(2*math.pi)-np.log(x*(ELL-x))/2
    harmonic = np.r_[0.0, np.cumsum(1/np.arange(1, degree+2))]
    base = bx * harmonic[:degree+1] + potential[:, None]*bx - regular @ wb/2
    interaction = 2*(hankel + A*reflect)
    # Analytic coarse tail floor; exact epsilon correction is bounded below.
    c = GAMMA + math.log(math.pi*ELL) + ELL/4 + math.pi + 2*A
    # The elementary tail bound in the canonical reduction is far below
    # floating point at these degrees. Record a logarithmic upper bound.
    n = degree+1
    t = ELL/4
    # r_n <= sqrt(2n+1)*t^(n-1)/(2n+1)!! * exp(t^2/6)*3,
    # also bounds the even case; subsequent squared terms ratio <1/2.
    log_double_factorial = sum(math.log(2*j+1) for j in range(1,n+1))
    log_eps_sq_bound = (math.log(2)+2*(math.log(3)+0.5*math.log(2*n+1)
                          +(n-1)*math.log(t)-log_double_factorial+t*t/6))
    epsilon_sq_bound = math.exp(log_eps_sq_bound) if log_eps_sq_bound > -740 else 0.0
    tail_floor = harmonic[degree+1] - c*(1+epsilon_sq_bound)
    signs = []
    for sign in (-1, 1):
        action = (base + sign*interaction) @ graph
        finite = head.T @ (w[:, None]*action)
        symmetry_residual = float(np.max(np.abs(finite-finite.T)))
        finite = (finite+finite.T)/2
        projected = bx.T @ (w[:, None]*action)
        total_cov = action.T @ (w[:, None]*action)
        covariance = total_cov-projected.T@projected
        covariance = (covariance+covariance.T)/2
        schur = finite-covariance/tail_floor
        eig = np.linalg.eigvalsh(schur)
        finite_eig = np.linalg.eigvalsh(finite)
        cov_eig = np.linalg.eigvalsh(covariance)
        conservative_minimum = None
        if degree == 256:
            # The analytic floor is >0.72. Reserving 5% would give
            # rho=0.95, but the covariance itself is still unenclosed.
            conservative_minimum = float(np.linalg.eigvalsh(
                finite-covariance/(0.95*0.72))[0])
        signs.append({
            "sign": sign,
            "finite_symmetry_residual": symmetry_residual,
            "finite_minimum": float(finite_eig[0]),
            "covariance_minimum": float(cov_eig[0]),
            "covariance_maximum": float(cov_eig[-1]),
            "schur_minimum": float(eig[0]),
            "schur_locator_at_floor_0_72_rho_0_95": conservative_minimum,
            "schur_eigenvalues": eig.tolist(),
            "finite_matrix": finite.tolist(),
            "full_unweighted_covariance": covariance.tolist(),
            "schur_matrix": schur.tolist(),
        })
    return {"degree": degree, "outer_order_per_piece": order,
            "inner_order": order, "tail_subtraction_constant": c,
            "tail_floor_locator": float(tail_floor),
            "log_moment_graph_tail_norm_squared_upper_bound": log_eps_sq_bound,
            "neutral_graph_coefficients": ratios.tolist(),
            "signs": signs, "certified": False,
            "limitations": ["Unenclosed quadrature and backward recurrence.",
                "Tail moment-graph contribution to covariance not enclosed.",
                "No certified Schur eigenvalue or all-space positive margin."]}


def main():
    runs = []
    for degree, order in ((128,512), (256,768), (256,1024)):
        record = run(degree,order)
        runs.append(record)
        print(f"degree={degree}, order={order}, tail floor locator="
              f"{record['tail_floor_locator']:.9g}; required>0")
        for sign in record["signs"]:
            print(f" sign={sign['sign']:+d}: finite={sign['finite_minimum']:.9g}, "
                  f"Schur={sign['schur_minimum']:.9g}; required>0; certified=False")
            if sign["schur_locator_at_floor_0_72_rho_0_95"] is not None:
                print(" floor=0.72, rho=0.95: Schur locator="
                      f"{sign['schur_locator_at_floor_0_72_rho_0_95']:.9g}; "
                      "required>0; certified=False")
    output = Path(__file__).with_suffix(".json")
    output.write_text(json.dumps({"certified":False,"runs":runs},indent=2)+"\n")
    print("Failures: quadrature/recurrence, covariance and eigenvalue enclosures unpaid.")
    print(f"Full diagnostic: {output}")


if __name__ == "__main__":
    main()
