"""Floating diagnostic only; does not certify a survivor or a mass bound."""
import json
import math
from pathlib import Path

A = 1 / 16
T = 1 / 1920
H = 1 / 2209


def bump(s):
    return math.exp(-1 / (1 - s * s)) if abs(s) < 1 else 0.0


def moment(k, n=8192):
    return 2 / (3 * n) * sum(
        (1 if j in (0, n) else 4 if j % 2 else 2)
        * (j / n) ** k * bump(j / n) for j in range(n + 1)
    )


def rhs(y):
    lo, hi, v, loss = y
    if lo <= v * v or lo <= 0 or hi <= 0:
        raise ValueError("comparison region exhausted")
    gap = math.sqrt(lo) - v
    p = 2 / gap ** 2 + 1 / (4 * lo)
    return (
        -4 * lo / (lo - v * v) - 2 - 82 * lo,
        -6 / (1 + H) + 82 * hi,
        6 * (v + H * math.sqrt(hi)) / (lo - v * v) + 41 * math.sqrt(hi),
        27 * H * p + 246,
    )


def screen(r, v, n=512):
    y = (r * r, r * r, v, 0.0)
    dt = T / n
    try:
        for _ in range(n):
            k1 = rhs(y)
            k2 = rhs(tuple(a + dt * b / 2 for a, b in zip(y, k1)))
            k3 = rhs(tuple(a + dt * b / 2 for a, b in zip(y, k2)))
            k4 = rhs(tuple(a + dt * b for a, b in zip(y, k3)))
            y = tuple(a + dt * (b + 2*c + 2*d + e) / 6
                      for a, b, c, d, e in zip(y, k1, k2, k3, k4))
        lo, hi, w, loss = y
        if lo <= w * w:
            raise ValueError("terminal comparison region exhausted")
        density = (math.cos(19/64) * math.exp(-15/64-loss)
                   * (2*r*(r*r-v*v)) * (2*math.sqrt(lo)*(lo-w*w)))
        return {"passes_diagnostic": True, "density_over_exp_minus_H0": density,
                "terminal_R_lower": lo, "terminal_v_upper": w,
                "terminal_gap_lower": math.sqrt(lo)-w, "log_ratio_loss": loss}
    except (ValueError, OverflowError, ZeroDivisionError) as error:
        return {"passes_diagnostic": False, "failure": str(error)}


def main():
    m0, m2, m4 = (moment(k) for k in (0, 2, 4))
    initial = 6*(m0*m2*m4-m2**3)*(A/2)**9*math.exp(15/256)
    rlo, rhi, vmax, nr, nv = .058, .06249, .0012, 32, 24
    dr, dv = (rhi-rlo)/nr, vmax/nv
    cells = []
    total = 0.0
    for i in range(nr):
        for j in range(nv):
            r, v = rlo+(i+.5)*dr, (j+.5)*dv
            result = screen(r, v)
            result.update(r=r, v=v)
            if result["passes_diagnostic"] and A-r-v/3 > 0:
                contribution = 48*(A-r-v/3)*dr*dv*result["density_over_exp_minus_H0"]
                total += contribution
                result["midpoint_mass_contribution"] = contribution
            cells.append(result)
    output = {"status": "NONRIGOROUS_DIAGNOSTIC_ONLY",
              "initial_mass_diagnostic_upper_expression": initial,
              "initial_moments_simpson": [m0, m2, m4],
              "reserve_midpoint_diagnostic": total,
              "diagnostic_ratio": total/initial,
              "survivor_equations_and_mass_bound": "Not yet proved or interval-verified",
              "grid": {"rlo": rlo, "rhi": rhi, "vmax": vmax, "nr": nr, "nv": nv},
              "passing_cells": sum(c["passes_diagnostic"] for c in cells), "cells": cells}
    path = Path(__file__).with_suffix(".json")
    path.write_text(json.dumps(output, indent=2)+"\n")
    print(f"NONRIGOROUS ONLY: reserve={total:.9g}, required initial={initial:.9g}, ratio={total/initial:.6g}")
    print(f"passing cells={output['passing_cells']}/{len(cells)}; failed cells retained; path={path}")


if __name__ == "__main__":
    main()
