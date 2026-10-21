#!/usr/bin/env python3
"""Exact Wilson cubic-action test on a pinned longitudinal input.

This evaluates actual relative-complex plaquette BCH coefficients. It
does not compute either full probe covariance or a cutoff asymptotic.
"""

from fractions import Fraction as F
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path


ZERO = (F(0),) * 3


def add(u, v):
    return tuple(a + b for a, b in zip(u, v))


def scale(c, v):
    return tuple(c * a for a in v)


def bracket(u, v):
    # t_c = i sigma_c/2: the Lie bracket is minus the cross product.
    return (u[2]*v[1] - u[1]*v[2],
            u[0]*v[2] - u[2]*v[0],
            u[1]*v[0] - u[0]*v[1])


def norm2(v):
    return sum(a*a for a in v)


def bch2(word):
    first, second = ZERO, ZERO
    for v in word:
        second = add(second, scale(F(1, 2), bracket(first, v)))
        first = add(first, v)
    return first, second


def check(n):
    spec = spec_from_file_location(
        "fixed_box", Path("scripts/fixed-box-gaussian/check.py"))
    fixed_box = module_from_spec(spec)
    spec.loader.exec_module(fixed_box)
    edges, faces = (fixed_box.cells(k, n) for k in (1, 2))
    lookup = {e: i for i, e in enumerate(edges)}
    rows = fixed_box.incidence(edges, faces)
    v = (n//2,) * 4
    w = (n//2 + 1,) + v[1:]
    phi = {v: (F(1), F(0), F(0)), w: (F(0), F(1), F(0))}
    x, y = [], []
    for (mu,), pos in edges:
        end = list(pos)
        end[mu] += 1
        left, right = phi.get(pos, ZERO), phi.get(tuple(end), ZERO)
        x.append(add(left, scale(-1, right)))
        y.append(scale(-F(1, 2), bracket(left, right)))

    dy, w2 = [], []
    grad_s3 = [ZERO for _ in edges]
    for ((mu, nu), pos), row in zip(faces, rows):
        upper_mu, upper_nu = list(pos), list(pos)
        upper_mu[mu] += 1
        upper_nu[nu] += 1
        oriented_edges = [((mu,), pos, 1),
                          ((nu,), tuple(upper_mu), 1),
                          ((mu,), tuple(upper_nu), -1),
                          ((nu,), pos, -1)]
        word = [scale(sign, x[lookup[(direction, p)]])
                if (direction, p) in lookup else ZERO
                for direction, p, sign in oriented_edges]
        first, second = bch2(word)
        assert first == ZERO
        circulation_y = ZERO
        for e, sign in row.items():
            circulation_y = add(circulation_y, scale(sign, y[e]))
            # S3=sum W1.W2; at W1=0 its exact derivative is D* W2.
            grad_s3[e] = add(grad_s3[e], scale(sign, second))
        assert second == scale(-1, circulation_y)
        dy.append(circulation_y)
        w2.append(second)

    dtdy = [ZERO for _ in edges]
    for row, val in zip(rows, dy):
        for e, sign in row.items():
            dtdy[e] = add(dtdy[e], scale(sign, val))
    assert [scale(-1, val) for val in grad_s3] == dtdy
    assert sum(norm2(val) for val in dy) == F(3, 2)
    selected_edge = lookup[((0,), v)]
    assert dtdy[selected_edge] == scale(6, y[selected_edge])
    assert any(val != ZERO for val in dtdy)

    # Independent BCH check of the inverse pinned gauge transformation:
    # exp(-g phi_v) exp(g x_e) exp(g phi_w) has second jet -y_e.
    for e, ((mu,), pos) in enumerate(edges):
        end = list(pos)
        end[mu] += 1
        left, right = phi.get(pos, ZERO), phi.get(tuple(end), ZERO)
        first, second = bch2([scale(-1, left), x[e], right])
        assert first == ZERO and second == scale(-1, y[e])

    # Core triplet coefficients (1,1,-1,-1) give j_(3,2)(y)=1.
    # For an admitted fine mesh with this local stencil in the core these
    # are the actual coefficients; coarse test meshes check the stencil only.
    weights = (1, 1, -1, -1)
    triplet = sum((weights[mu]+weights[nu])*norm2(val)
                  for ((mu, nu), _), val in zip(faces, dy))
    assert triplet == 1
    print(f"PASS N={n}: {len(edges)} links, {len(faces)} faces; "
          "Dx=0, W2=-Dy, -grad S3=D*Dy, ||Dy||^2=3/2; "
          "inverse gauge second jet=-y; core triplet=1.")


if __name__ == "__main__":
    for size in (4, 6):
        check(size)
