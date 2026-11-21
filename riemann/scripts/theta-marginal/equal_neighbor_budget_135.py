"""One approved full-marginal J test; L904 gives all analytic bounds.

Reuses L037's Decimal arithmetic, Machin pi and trig Taylor contracts.
No binary floating-point input, quadrature heuristic or parameter sweep.
"""

import argparse
import json
from fractions import Fraction
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts" / "laguerre"))
from certify_conditional_cosine import sin_cos  # noqa: E402
from certify_hankel import I, PRECISION, pi_bounds, self_check  # noqa: E402


def nonnegative(value):
    if value.hi < 0:
        raise ArithmeticError("Positive kernel enclosed strictly below zero")
    return I(max(value.lo, 0), value.hi)


def symmetric(radius):
    return I(radius.hi.copy_negate(), radius.hi)


def certify(mesh):
    if mesh < 1:
        raise ValueError("Positive integer mesh required")
    pi = pi_bounds()
    h = pi / (64 * mesh)
    nt, nq = 32 * mesh, 5 * mesh
    kernel_cache = {}

    def kernel(lo, hi):
        # Absolute image of a possibly reflected interval; no differentiation.
        if hi < 0:
            lo, hi = -hi, -lo
        elif lo < 0:
            lo, hi = 0, max(-lo, hi)
        key = (lo, hi)
        if key not in kernel_cache:
            u = I((h * lo).lo, (h * hi).hi)
            e2 = (2 * u).exp()
            total = I(0)
            for n in range(1, 5):
                v = pi * (n*n) * e2
                total = total + (8*v*v - 12*v) * (-v).exp()
            value = nonnegative((u / 2).exp() * total)
            # L312's bound applies also to this positive finite head.
            if value.lo > 16:
                raise ArithmeticError("Kernel bound conflicts with L312")
            kernel_cache[key] = I(value.lo, min(value.hi, 16))
        return kernel_cache[key]

    # Integrals of 2 t^2 on t boxes. All quantities enclose the exact pi grid.
    t_weights = [2*h**3*((i+1)**3-i**3)/3 for i in range(nt)]
    sines = [sin_cos(pi*j/(2*mesh), pi)[0] for j in range(nq+1)]
    # Exact endpoint values avoid gratuitous endpoint noise.
    for j, exact in [(0, 0), (mesh, 1), (2*mesh, 0),
                     (3*mesh, -1), (4*mesh, 0), (5*mesh, 1)]:
        if not sines[j].lo <= exact <= sines[j].hi:
            raise ArithmeticError("Trig enclosure misses exact endpoint")
        sines[j] = I(exact)
    q_weights = [(sines[j+1]-sines[j])/16 for j in range(nq)]
    lobes = [I(0), I(0), I(0)]
    cell_sign_counts = {"positive": 0, "negative": 0}
    for j in range(nq):
        sign = -1 if mesh <= j < 3*mesh else 1
        qw = q_weights[j]
        if (sign > 0 and qw.lo <= 0) or (sign < 0 and qw.hi >= 0):
            raise ArithmeticError("Cosine cell weight not strictly signed")
        cell_sign_counts["positive" if sign > 0 else "negative"] += 1
        transverse = I(0)
        for i in range(nt):
            kp = kernel(i+j, i+j+2)
            km = kernel(i-j-1, i-j+1)
            transverse = transverse + t_weights[i]*kp*km
        which = 0 if j < mesh else (1 if j < 3*mesh else 2)
        lobes[which] = lobes[which] + transverse*qw

    eps = 160000 * I(-75).exp()
    # Density error on the finite t box: 2 int_0^T t^2 * 32 eps <512 eps/3.
    theta_density_error = I.rational(Fraction(512, 3))*eps
    # T=pi/2>3/2; t=3/2+w gives exponent <=-106-231w.
    spatial_density_error = 131072*I(-106).exp()*I.rational(
        Fraction(9, 4*231) + Fraction(3, 231**2) + Fraction(2, 231**3))
    widths = [pi/32, pi/16, pi/16]
    errors = [w*(theta_density_error+spatial_density_error) for w in widths]
    full_lobes = [value+symmetric(error) for value, error in zip(lobes, errors)]
    # I0's half of the full symmetric lobe already became [0,b], weight one.
    finite_numerator = lobes[0]+lobes[1]+lobes[2]/2
    full_numerator = full_lobes[0]+full_lobes[1]+full_lobes[2]/2
    weighted_tail_error = errors[0]+errors[1]+errors[2]/2

    moments = {0: I(0), 2: I(0)}
    for i in range(nt):
        value = kernel(i, i+1)
        moments[0] = moments[0]+h*value
        moments[2] = moments[2]+h**3*((i+1)**3-i**3)/3*value
    moment_spatial = {
        0: 256*I(-53).exp()/115,
        2: 256*I(-53).exp()*I.rational(
            Fraction(9, 4*115)+Fraction(3, 115**2)+Fraction(2, 115**3)),
    }
    moment_theta = {0: 2*eps, 2: I.rational(Fraction(8, 3))*eps}
    full_moments = {r: value+I(0, (moment_spatial[r]+moment_theta[r]).hi)
                    for r, value in moments.items()}
    normalizer = 2*full_moments[0]*full_moments[2]
    if normalizer.lo <= 0:
        raise ArithmeticError("A0 not certified strictly positive")
    budget = full_numerator/normalizer
    # Enclosures are always saved; zero-straddling is a legitimate failed test.
    decision = "NEGATIVE" if budget.hi < 0 else (
        "POSITIVE" if budget.lo > 0 else "INCONCLUSIVE")
    return {
        "scope": "Only equal-neighbor first-negative-lobe J at x=16,y=0",
        "arithmetic_contract": "L037; documented Decimal trusted, not formally verified",
        "precision": PRECISION,
        "mesh": mesh, "t_cells": nt, "q_cells": nq, "box_count": nt*nq,
        "theta_terms": 4, "t_cutoff": "pi/2", "h": h.data(), "pi": pi.data(),
        "method": "real-box inclusion with exactly integrated signed cosine and 2t^2 weights",
        "cell_sign_counts": cell_sign_counts,
        "bounds": {
            "kernel_uniform_theta_error": eps.data(),
            "theta_density_error": theta_density_error.data(),
            "spatial_density_error": spatial_density_error.data(),
            "lobe_full_tail_errors": [v.data() for v in errors],
            "weighted_numerator_tail_error": weighted_tail_error.data(),
            "normalizer_spatial_errors": {str(r): v.data() for r, v in moment_spatial.items()},
            "normalizer_theta_errors": {str(r): v.data() for r, v in moment_theta.items()},
        },
        "result": {
            "finite_signed_lobes": [v.data() for v in lobes],
            "complete_signed_lobes": [v.data() for v in full_lobes],
            "finite_numerator": finite_numerator.data(),
            "complete_numerator": full_numerator.data(),
            "moments": {str(r): v.data() for r, v in full_moments.items()},
            "positive_normalizer_A0": normalizer.data(),
            "J": budget.data(),
            "required_threshold": "J>=0",
            "negative_rational_bound": "J<-1/1000" if Fraction(budget.hi) < Fraction(-1,1000) else None,
            "decision": decision,
            "failures": [] if decision != "INCONCLUSIVE" else ["Enclosure straddles zero"],
        },
        "kernel_cache": {f"{lo}:{hi}": v.data() for (lo, hi), v in sorted(kernel_cache.items())},
        "cosine_integrated_weights": [v.data() for v in q_weights],
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mesh", type=int, default=32)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    self_check()
    result = certify(args.mesh)
    args.output.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({"decision": result["result"]["decision"],
                      "J": result["result"]["J"],
                      "required": "J>=0", "failures": result["result"]["failures"],
                      "certificate": str(args.output), "boxes": result["box_count"]}))
