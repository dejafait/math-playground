"""Approved four-demand necessary Hall cuts only; see L905 and working137.

Real-box inclusion, L037 Decimal contracts, no total-transform sign input.
"""

import argparse
import itertools
import json
from fractions import Fraction
from pathlib import Path

from equal_neighbor_budget_135 import (
    I, PRECISION, nonnegative, pi_bounds, self_check, sin_cos, symmetric,
)


def certify(mesh):
    if mesh not in (64, 128):
        raise ValueError("Declared error budget permits M=64 or M=128 only")
    pi = pi_bounds()
    h = pi / (64 * mesh)
    nt, nq = 32 * mesh, 9 * mesh
    cache = {}

    def kernel(lo, hi):
        if hi < 0:
            lo, hi = -hi, -lo
        elif lo < 0:
            lo, hi = 0, max(-lo, hi)
        key = (lo, hi)
        if key not in cache:
            u = I((h * lo).lo, (h * hi).hi)
            e2 = (2 * u).exp()
            total = I(0)
            for n in range(1, 5):
                v = pi * (n*n) * e2
                total = total + (8*v*v - 12*v) * (-v).exp()
            value = nonnegative((u/2).exp() * total)
            if value.lo > 16:
                raise ArithmeticError("Conflict with L312 kernel bound")
            cache[key] = I(value.lo, min(value.hi, 16))
        return cache[key]

    tw = [2*h**3*((i+1)**3-i**3)/3 for i in range(nt)]
    sines = [sin_cos(pi*j/(2*mesh), pi)[0] for j in range(nq+1)]
    for k in range(10):
        j = k*mesh
        exact = (0, 1, 0, -1)[k % 4]
        if not sines[j].lo <= exact <= sines[j].hi:
            raise ArithmeticError("Trig misses exact endpoint")
        sines[j] = I(exact)
    qw = [(sines[j+1]-sines[j])/16 for j in range(nq)]
    lobes = [I(0) for _ in range(5)]
    counts = {"positive": 0, "negative": 0}
    for j in range(nq):
        ell = (j+mesh)//(2*mesh)
        sign = (-1)**ell
        if (sign > 0 and qw[j].lo <= 0) or (sign < 0 and qw[j].hi >= 0):
            raise ArithmeticError("Cell weight not strictly signed")
        counts["positive" if sign > 0 else "negative"] += 1
        transverse = I(0)
        for i in range(nt):
            transverse = transverse + tw[i]*kernel(i+j, i+j+2)*kernel(i-j-1, i-j+1)
        lobes[ell] = lobes[ell] + transverse*qw[j]

    eps = 160000*I(-75).exp()
    etheta = I.rational(Fraction(512, 3))*eps
    espace = 131072*I(-106).exp()*I.rational(
        Fraction(9, 4*231)+Fraction(3, 231**2)+Fraction(2, 231**3))
    errors = [(pi/(32 if j == 0 else 16))*(etheta+espace) for j in range(5)]
    full = [v+symmetric(e) for v, e in zip(lobes, errors)]

    # Independent positive normalizer, never a total cosine sign premise.
    moments = {0: I(0), 2: I(0)}
    for i in range(nt):
        value = kernel(i, i+1)
        moments[0] = moments[0]+h*value
        moments[2] = moments[2]+h**3*((i+1)**3-i**3)/3*value
    mspace = {
        0: 256*I(-53).exp()/115,
        2: 256*I(-53).exp()*I.rational(
            Fraction(9, 4*115)+Fraction(3, 115**2)+Fraction(2, 115**3)),
    }
    mtheta = {0: 2*eps, 2: I.rational(Fraction(8, 3))*eps}
    fm = {r: v+I(0, (mspace[r]+mtheta[r]).hi) for r, v in moments.items()}
    a0 = 2*fm[0]*fm[2]
    if a0.lo <= 0:
        raise ArithmeticError("Normalizer not positive")

    # Exact reflection: central resource is 2 B0; each other complete
    # resource/demand is one full positive-q lobe, not half of one.
    resource_lobe = {-2: 4, -1: 2, 0: 0, 1: 2, 2: 4}
    demand_lobe = {-2: 3, -1: 1, 0: 1, 1: 3}
    cuts = []
    for size in range(1, 5):
        for subset in itertools.combinations((-2, -1, 0, 1), size):
            neighbors = sorted({j for k in subset for j in (k, k+1)})
            coefficients = [0]*5
            for j in neighbors:
                coefficients[resource_lobe[j]] += 2 if j == 0 else 1
            for k in subset:
                # B1,B3 are negative signed integrals; adding them subtracts demand.
                coefficients[demand_lobe[k]] += 1
            raw = sum((c*v for c, v in zip(coefficients, full)), I(0))
            normalized = raw/a0
            decision = "NEGATIVE" if raw.hi < 0 else (
                "PASS" if raw.lo >= 0 else "INCONCLUSIVE")
            cuts.append({"S": list(subset), "T": neighbors,
                         "B_coefficients": coefficients,
                         "raw_A0_H": raw.data(), "H": normalized.data(),
                         "decision": decision})
    failed = [c["S"] for c in cuts if c["decision"] == "NEGATIVE"]
    unresolved = [c["S"] for c in cuts if c["decision"] == "INCONCLUSIVE"]
    decision = "NEGATIVE_CUT" if failed else ("INCONCLUSIVE" if unresolved else "FINITE_PASS")
    resources = {str(j): ((2 if j == 0 else 1)*full[ell]/a0).data()
                 for j, ell in resource_lobe.items()}
    demands = {str(k): (-full[ell]/a0).data() for k, ell in demand_lobe.items()}
    return {
        "scope": "x=16,y=0; F={-2,-1,0,1}; all 15 necessary cuts only",
        "arithmetic_contract": "L037; trusted Python Decimal, not formally verified",
        "precision": PRECISION, "mesh": mesh, "t_cells": nt, "q_cells": nq,
        "box_count": nt*nq, "theta_terms": 4, "h": h.data(), "pi": pi.data(),
        "domain": {"t": "[0,pi/2] plus complete tails", "q": "[0,9pi/32] and exact reflection"},
        "method": "whole real boxes, exactly integrated signed cosine and 2t^2 weights",
        "cell_sign_counts": counts,
        "bounds": {"epsilon": eps.data(), "theta_density_error": etheta.data(),
                   "spatial_density_error": espace.data(),
                   "lobe_tail_errors": [e.data() for e in errors],
                   "normalizer_spatial_errors": {str(r): v.data() for r, v in mspace.items()},
                   "normalizer_theta_errors": {str(r): v.data() for r, v in mtheta.items()}},
        "result": {"decision": decision, "required": "H(S)>=0 for every S",
                   "finite_B": [v.data() for v in lobes],
                   "complete_B": [v.data() for v in full],
                   "moments": {str(r): v.data() for r, v in fm.items()},
                   "A0": a0.data(), "resources": resources, "demands": demands,
                   "cuts": cuts, "negative_cuts": failed,
                   "unresolved_cuts": unresolved,
                   "failures": ["Zero-containing cut enclosure"] if unresolved else []},
        "kernel_cache": {f"{lo}:{hi}": v.data() for (lo, hi), v in sorted(cache.items())},
        "integrated_cosine_weights": [v.data() for v in qw],
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mesh", type=int, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    self_check()
    result = certify(args.mesh)
    args.output.write_text(json.dumps(result, indent=2)+"\n")
    cuts = result["result"]["cuts"]
    print(json.dumps({"decision": result["result"]["decision"],
                      "required": result["result"]["required"],
                      "raw_cut_bounds": [{"S": c["S"], "A0_H": c["raw_A0_H"]} for c in cuts],
                      "failures": result["result"]["failures"],
                      "certificate": str(args.output), "boxes": result["box_count"]}))
