#!/usr/bin/env python3
"""Exploratory floating-point quadrature, not an interval certificate."""
import json
import math
import numpy as np


def variance(u, order):
    x, w = np.polynomial.legendre.leggauss(order)
    x = 1.5 + x / 2
    return math.exp(math.pi**2 / 8) * (2 * math.pi)**1.5 * np.dot(
        w / 2, x**-4 * np.exp(-2 * (np.log(x) - math.log(u) / 2)**2))


def sample(left, h, lam, z, count):
    total1 = total2 = 0.0
    for start in range(0, count, 2048):
        t = left + (np.arange(start, min(start + 2048, count)) + .5) * h / count
        s = np.sum(np.exp(1j * (t[:, None] - math.pi / 2) * lam) * z, axis=1)
        y = np.abs(s)
        total1 += np.sum(y)
        total2 += np.dot(y, y)
    return float(total1 / count), float(total2 / count)


def main():
    rows = []
    for N in (16, 32, 64, 128):
        T = 2 * math.pi * N**2
        J = math.ceil(T**.25)
        h = T / J
        n = np.arange(N, 2 * N + 1, dtype=float)
        lam = np.log(n / N)
        for j in sorted({0, J // 2, J - 1}):
            left = T + j * h
            c = left + h / 2
            u = c / T
            v = variance(u, 64)
            assert abs(v - variance(u, 128)) < 1e-11 * v
            z = math.exp(math.pi**2 / 16) * T**.75 * n**-2 * np.exp(
                -(lam - math.log(u) / 2)**2) / math.sqrt(v)
            omega = lam[:, None] - lam[None, :]
            exact2 = float(np.sum(z[:, None] * z[None, :] *
                np.cos((c - math.pi / 2) * omega) * np.sinc(h * omega / (2 * math.pi))))
            count = math.ceil(h / .1)
            coarse1, coarse2 = sample(left, h, lam, z, count)
            fine1, fine2 = sample(left, h, lam, z, 2 * count)
            lip = float(np.dot(z, lam))
            error1 = h / (2 * count) * lip / 4
            # |Z|^2 has Lipschitz constant at most 2(sum z)(sum z lambda).
            error2 = h / (2 * count) * 2 * float(sum(z)) * lip / 4
            assert abs(fine1 - coarse1) <= 3 * error1 + 1e-10
            assert abs(fine2 - exact2) <= error2 + 1e-10
            rows.append(dict(N=N, T=T, block=j, blocks=J, u=u,
                first=fine1, midpoint_error_bound=error1,
                mesh_difference=abs(fine1-coarse1), second=exact2,
                second_mesh_error=abs(fine2-exact2)))
    print(json.dumps(dict(qualification='Exploratory floats; bounds omit roundoff and variance quadrature error', rows=rows), indent=2))


if __name__ == '__main__':
    main()
