"""Exact rational barriers for C467c; analytic implications require its proof.

All accepted tubes are saved and checked again from the saved certificate.
Rejected boxes are retained, and contribute zero to the reserve lower bound.
"""
from fractions import Fraction as F
from math import isqrt
from pathlib import Path
import json

GRID = 2**64
MASS_GRID = 10**40
A, T, H = F(1, 16), F(1, 1920), F(1, 2209)
STEPS = 256
DT = T / STEPS
COS_LOWER = 1 - F(19, 64)**2 / 2


def floor_grid(x, scale=GRID):
    return x.numerator * scale // x.denominator


def ceil_grid(x, scale=GRID):
    return -floor_grid(-x, scale)


def sqrt_lower(x):
    assert x >= 0
    return F(isqrt(x.numerator * GRID**2 // x.denominator), GRID)


def sqrt_upper(x):
    z = sqrt_lower(x)
    return z if z*z == x else z + F(1, GRID)


def record(x):
    return {"numerator": x.numerator, "denominator": x.denominator}


def value(x):
    return F(x["numerator"], x["denominator"])


def exp_negative_lower(x):
    # Odd Taylor polynomial is a global lower bound by the signed remainder.
    term = total = F(1)
    for k in range(1, 10):
        term *= -x / k
        total += term
    return total


def rates(lo, v, hi):
    assert lo > v*v and hi > 0
    root_hi = sqrt_upper(hi)
    decay = 4*lo/(lo-v*v) + 2 + 82*hi
    growth = 6*(v+H*root_hi)/(lo-v*v) + 41*root_hi
    gap = sqrt_lower(lo)-v
    assert gap > 0
    loss = 27*H*(2/(gap*gap)+1/(4*lo)) + 246
    return decay, growth, loss


def initial_bound():
    # Even step envelope for b(s), using only a positive exponential sum.
    n, terms, scale = 64, 24, 10**12
    rows = []
    moments = [F(0), F(0), F(0)]
    for j in range(n):
        left, right = F(j, n), F(j+1, n)
        x = 1/(1-left*left)
        term = partial = F(1)
        for k in range(1, terms+1):
            term *= x/k
            partial += term
        height_int = ceil_grid(1/partial, scale)
        height = F(height_int, scale)
        assert height*partial >= 1
        rows.append(height_int)
        for index, power in enumerate((0, 2, 4)):
            moments[index] += 2*height*(right**(power+1)-left**(power+1))/(power+1)
    m0, m2, m4 = moments
    integral = 6*(m0*m2*m4-m2**3)
    assert integral > 0
    bound = F(256, 241)*(A/2)**9*integral
    return {"bins": n, "exponential_terms": terms, "height_scale": scale,
            "heights": rows, "moments": [record(x) for x in moments],
            "upper_bound_over_exp_minus_H0": record(bound)}


def generate_box(rlo, rhi, vlo, vhi):
    margin = F(1, 10**6)
    m = A-rhi-vhi/3-margin
    result = {"rlo": record(rlo), "rhi": record(rhi), "vlo": record(vlo),
              "vhi": record(vhi), "center_half_width": record(m), "tubes": []}
    if m <= 0:
        result.update(accepted=False, failure="no interior center interval")
        return result
    lo_int = floor_grid(rlo*rlo)
    v_int = ceil_grid(vhi)
    loss_int = 0
    for j in range(STEPS):
        lo, v, loss = F(lo_int, GRID), F(v_int, GRID), F(loss_int, GRID)
        hi = rhi*rhi - F(567, 100)*j*DT
        try:
            decay, growth, _ = rates(lo, v, hi)
            guard_decay = F(2*ceil_grid(decay), GRID)
            guard_growth = F(2*ceil_grid(growth), GRID)
            tube_lo_int = floor_grid(lo-guard_decay*DT)
            tube_v_int = ceil_grid(v+guard_growth*DT)
            tube_lo, tube_v = F(tube_lo_int, GRID), F(tube_v_int, GRID)
            decay, growth, loss_rate = rates(tube_lo, tube_v, hi)
            if not (decay*DT < lo-tube_lo and growth*DT < tube_v-v):
                raise ArithmeticError("tube exit inequality not certified")
            lo_int = floor_grid(lo-decay*DT)
            v_int = ceil_grid(v+growth*DT)
            loss_int = ceil_grid(loss+loss_rate*DT)
            assert tube_lo_int <= lo_int and v_int <= tube_v_int
            result["tubes"].append([tube_lo_int, tube_v_int, lo_int, v_int, loss_int])
        except (AssertionError, ArithmeticError, ZeroDivisionError):
            result.update(accepted=False, failure="positive-gap tube not certified", failed_step=j)
            return result
    lo, v, loss = F(lo_int, GRID), F(v_int, GRID), F(loss_int, GRID)
    factor = COS_LOWER*exp_negative_lower(F(15, 64)+loss)
    if factor <= 0:
        result.update(accepted=False, failure="Taylor lower factor not positive")
        return result
    initial_delta = 2*rlo*(rlo*rlo-vhi*vhi)
    final_delta = 2*sqrt_lower(lo)*(lo-v*v)
    density = F(floor_grid(factor*initial_delta*final_delta, MASS_GRID), MASS_GRID)
    volume = 48*m*(rhi-rlo)*(vhi-vlo)
    result.update(accepted=True, density_lower=record(density), volume=record(volume),
                  mass_lower=record(density*volume), terminal_gap=record(sqrt_lower(lo)-v))
    return result


def verify_saved(data):
    assert value(data["constants"]["h"]) == H
    assert data["constants"]["steps"] == STEPS
    assert 40**2*(1+H) < 41**2
    assert 6/(1+H)-82*A*A > F(567, 100)
    assert 120*F(48, 47)+123 < 246
    assert data["initial"] == initial_bound()
    total, accepted, tube_count = F(0), 0, 0
    for box in data["boxes"]:
        if not box["accepted"]:
            continue
        rlo, rhi, vlo, vhi, m = (value(box[k]) for k in
                               ("rlo", "rhi", "vlo", "vhi", "center_half_width"))
        assert 0 <= vlo < vhi < rlo < rhi < A
        assert m > 0 and m+rhi+vhi/3 < A
        lo, v, loss = F(floor_grid(rlo*rlo), GRID), F(ceil_grid(vhi), GRID), F(0)
        assert len(box["tubes"]) == STEPS
        for j, row in enumerate(box["tubes"]):
            tube_lo, tube_v, next_lo, next_v, next_loss = (F(x, GRID) for x in row)
            hi = rhi*rhi-F(567, 100)*j*DT
            decay, growth, loss_rate = rates(tube_lo, tube_v, hi)
            assert tube_lo > tube_v*tube_v
            assert decay*DT < lo-tube_lo
            assert growth*DT < tube_v-v
            assert tube_lo <= next_lo <= lo-decay*DT
            assert v+growth*DT <= next_v <= tube_v
            assert next_loss >= loss+loss_rate*DT
            lo, v, loss = next_lo, next_v, next_loss
            tube_count += 1
        factor = COS_LOWER*exp_negative_lower(F(15, 64)+loss)
        density_bound = factor*(2*rlo*(rlo*rlo-vhi*vhi))*(2*sqrt_lower(lo)*(lo-v*v))
        density = value(box["density_lower"])
        volume = 48*m*(rhi-rlo)*(vhi-vlo)
        assert 0 < density <= density_bound
        assert value(box["volume"]) == volume
        assert value(box["mass_lower"]) == density*volume
        assert value(box["terminal_gap"]) == sqrt_lower(lo)-v > 0
        total += density*volume
        accepted += 1
    # Generated grid boxes have disjoint interiors in (r, |v|); all six
    # permutations are distinct ordered chambers. Verify the grid explicitly.
    keys = [(value(b["rlo"]), value(b["rhi"]), value(b["vlo"]), value(b["vhi"]))
            for b in data["boxes"]]
    assert len(keys) == len(set(keys))
    for i, (rl, rh, vl, vh) in enumerate(keys):
        for rl2, rh2, vl2, vh2 in keys[i+1:]:
            assert rh <= rl2 or rh2 <= rl or vh <= vl2 or vh2 <= vl
    required = value(data["initial"]["upper_bound_over_exp_minus_H0"])
    assert total > F(4, 10**16)
    assert required < F(8, 10**17)
    return {"accepted_boxes": accepted, "rejected_boxes": len(data["boxes"])-accepted,
            "verified_tubes": tube_count, "mass_lower_over_exp_minus_H0": record(total),
            "required_initial_upper_over_exp_minus_H0": record(required),
            "strict_margin": record(total-required), "ratio_lower": record(total/required),
            "chosen_reserve_floor": record(F(4, 10**16)),
            "chosen_initial_ceiling": record(F(8, 10**17)),
            "chosen_bounds_verified": True,
            "reserve_exceeds_initial": total > required, "verification_failures": []}


def main():
    boxes = [generate_box(F(580+2*i, 10000), F(582+2*i, 10000),
                          F(j, 10000), F(j+1, 10000))
             for i in range(22) for j in range(12)]
    data = {"scope": "Exact rational barriers only; analytic proof and independent audit are separate.",
            "constants": {"h": record(H), "T": record(T), "a": record(A),
                          "steps": STEPS, "grid": GRID, "mass_grid": MASS_GRID},
            "initial": initial_bound(), "boxes": boxes}
    path = Path(__file__).with_suffix(".json")
    path.write_text(json.dumps(data, separators=(",", ":"))+"\n")
    saved = json.loads(path.read_text())
    summary = verify_saved(saved)
    saved["summary"] = summary
    path.write_text(json.dumps(saved, separators=(",", ":"))+"\n")
    actual = value(summary["mass_lower_over_exp_minus_H0"])
    required = value(summary["required_initial_upper_over_exp_minus_H0"])
    print(f"Exact barriers: {summary['accepted_boxes']} accepted, {summary['rejected_boxes']} rejected boxes; {summary['verified_tubes']} tubes replayed")
    print(f"Mass/e^-H0: actual lower {float(actual):.12g}; required initial upper {float(required):.12g}; ratio >={float(actual/required):.9g}")
    print(f"Strict comparison: {'PASS' if actual > required else 'FAIL'}; replay failures: {summary['verification_failures']}")
    print(f"Certificate: {path.relative_to(Path.cwd())}")
    if actual <= required:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
