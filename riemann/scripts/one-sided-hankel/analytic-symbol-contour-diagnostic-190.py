"""Noncertifying contour screen; all values retained in the local JSON."""
import cmath
import json
import math
from pathlib import Path

U = 121 / 64
A = 27 / 10
u = complex(3 / 10, 4 / 10)
alpha = 11 / 8
x0 = math.log(9 / 5) - 4 / 5 + 121 / 100 * math.log(201 / 121)

def K(s):
    return cmath.log(1 + 1 / s) - 1 / s + U / s**2 * cmath.log(1 + s / U)

def Kp(s):
    return -1 / (s * (s + 1)) + 1 / s**2 - 2 * U / s**3 * cmath.log(1 + s / U) + U / (s**2 * (U + s))

def phase(s, x):
    return u * x * s + ((U + s) * cmath.log(U + s) - U * math.log(U)) / s - ((s + 1) * cmath.log(s + 1) - s * cmath.log(s))

def pair(z):
    return [z.real, z.imag]

roots = []
failures = []
for x in (x0 - 1 / (3000 * A), x0, x0 + 1 / (3000 * A)):
    s = complex(1, -1)
    for iteration in range(80):
        step = (K(s) - u * x) / Kp(s)
        s -= step
        if abs(step) < 1e-13:
            break
    residual = abs(K(s) - u * x)
    if residual > 1e-11:
        failures.append(f"Newton residual {residual}")
    # A real-centered circle through s: derivative at s vanishes by saddle.
    circles = []
    for center in (-0.5, 0.0, 0.5, 1.0):
        radius = abs(s - center)
        samples = []
        reference = phase(s, x).real
        for j in range(2000):
            theta = 2 * math.pi * (j + 0.5) / 2000
            w = center + radius * cmath.exp(1j * theta)
            samples.append([theta, phase(w, x).real - reference])
        circles.append({"center": center, "radius": radius,
                        "encloses_all_kernel_poles": radius > max(abs(center), abs(center + 1)),
                        "excludes_resolvent_pole": radius < abs(alpha / u - center),
                        "left_crossing": center - radius,
                        "samples": samples,
                        "maximum_sample_excess": max(row[1] for row in samples)})
    roots.append({"x": x, "s": pair(s), "residual": residual,
                  "hessian": pair(-Kp(s)), "phase": pair(phase(s, x)),
                  "resolvent_distance": abs(s - alpha / u), "circles": circles})

out = {"status": "NONCERTIFYING_DIAGNOSTIC", "required": "uniform contour phase gap, pole separation and factorial remainders",
       "x0": x0, "resolvent_pole": pair(alpha / u), "roots": roots, "failures": failures}
path = Path(__file__).with_suffix(".json")
path.write_text(json.dumps(out, indent=2) + "\n")
print("NONCERTIFYING diagnostic; no contour certificate or asymptotic proved.")
for row in roots:
    print("x=", row["x"], "s=", row["s"], "residual=", row["residual"],
          "circle sampled excesses=", [r["maximum_sample_excess"] for r in row["circles"]])
print("Required: uniform nonpositive phase excess with strict complementary gap.")
print("Numerical failures:", failures, "Full output:", path)
