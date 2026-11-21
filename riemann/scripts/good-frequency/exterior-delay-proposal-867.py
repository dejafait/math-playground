"""Bounded, nonrigorous proposal only; no output here is a certificate."""
import cmath
import json
import math
from pathlib import Path

primes = [p for p in range(2, 81)
          if all(p % d for d in range(2, math.isqrt(p) + 1))]
powers = sorted((p ** k, p) for p in primes for k in range(1, 7)
                if p ** k < 81)
T = 4 * math.log(3)


def base(t):
    z = complex(0.25, t / 2)
    Z = z + 256
    m = (cmath.log(Z) - 1 / (2 * Z)
         - sum(1 / (z + k) for k in range(256))).real - math.log(math.pi)
    w = m - 2 * sum(math.log(p) / math.sqrt(n) * math.cos(t * math.log(n))
                    for n, p in powers)
    return {"t": t, "w_approx": w, "h_approx": (t*t + 0.25)**2 * w}


# The fixed family is unchanged. This finite evaluation search stops at
# the first strict approximate negative sum. All nine phases occur once.
# Only the phase-zero evaluation is allowed the predeclared shifts 0,...,16.
rows = []
for shift in range(17):
    points = [dict(phase=j, period_shift=shift if j == 0 else 0,
                   **base(2 * math.pi / T * (shift if j == 0 else j / 9)))
              for j in range(-4, 5)]
    value = sum(p["h_approx"] for p in points) / 9
    rows.append({"zero_phase_shift": shift, "points": points,
                 "mean_h_approx": value})
    if value < -0.01:
        break
path = Path(__file__).with_name("exterior-delay-proposal-867.json")
path.write_text(json.dumps({"status": "NONRIGOROUS_PROPOSAL",
                            "finite_search_cap": 16, "rows": rows}, indent=2)+"\n")
print(f"Proposal only: shift={shift}, mean h approximately {value:.12g}; "
      f"required certified upper < 0; certificate not yet constructed.")
print(f"Full diagnostic: {path}")
