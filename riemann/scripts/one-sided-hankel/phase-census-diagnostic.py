"""Nonrigorous limiting-product diagnostic; no bound or certificate of truth."""
import cmath
import json
import math
from pathlib import Path

d, U = 5 / 4, 121 / 64
panels = 2000
grid = [(j + 0.5) / panels for j in range(panels)]


def phase(y):
    return sum(math.atan(y / (d - t)) + math.atan(t * y / (U - d * t))
               for t in grid) / panels


def log_mod(y, theta):
    u = cmath.exp(1j * theta)
    return sum(math.log(abs((1 - 1j * t * y / (U * u + d * t)) /
                           (1 - 1j * y / (d + t * u))))
               for t in grid) / panels


rows = []
for mesh in [math.pi / 2, math.pi, 3 * math.pi / 2]:
    lo, hi = 0.0, math.sqrt((273 / 200) ** 2 - d ** 2)
    wanted = mesh / 6
    for _ in range(50):
        mid = (lo + hi) / 2
        if phase(mid) < wanted:
            lo = mid
        else:
            hi = mid
    endpoint = (lo + hi) / 2
    values = [(log_mod(endpoint, j * math.pi / 120), j * math.pi / 120)
              for j in range(241)]
    peak, theta = max(values)
    rows.append({"phase_mesh": mesh, "limiting_endpoint": endpoint,
                 "target_phase": wanted, "endpoint_phase": phase(endpoint),
                 "u1_endpoint_log_mod": log_mod(endpoint, 0),
                 "sampled_endpoint_max_log_mod": peak,
                 "sampled_max_theta": theta})

output = {"status": "DIAGNOSTIC_ONLY_NO_ERROR_ENCLOSURE",
          "method": "2000 midpoint panels; 241 endpoint angles; bisection",
          "purpose": "Select exact endpoint test for the proposed phase census",
          "rows": rows, "required_squared_rate": 1 / 16,
          "failures": ["No quadrature, maximization or floating-point error enclosure",
                       "No finite-family response or diagonal computed"]}
factor_peaks = []
for j in range(201):
    t = j / 200
    peak = 1.0
    for l in range(2001):
        c = -1 + l / 1000
        s2 = 1 - c * c
        N0, D0 = d * d + t * t + 2 * d * t * c, U * U + d * d * t * t + 2 * U * d * t * c
        determinant_N = (d + t * c) ** 2
        determinant_D = t * t * (U * c + d * t) ** 2
        trace_term = t * t * N0 + D0 - 2 * U * t * t * s2
        eigenvalue = (trace_term + math.sqrt(max(0, trace_term ** 2 - 4 * determinant_N * determinant_D))) / (2 * determinant_N)
        peak = max(peak, eigenvalue * N0 / D0)
    factor_peaks.append({"t": t, "sampled_squared_peak": peak})
output["single_factor_peaks"] = factor_peaks
output["sampled_factor_integral_rate"] = sum(math.log(v["sampled_squared_peak"]) / 2 for v in factor_peaks[:-1]) / 200
path = Path(__file__).with_suffix(".json")
path.write_text(json.dumps(output, indent=2) + "\n")
for row in rows:
    print("mesh/pi={:.2f}, endpoint={:.6f}, u=1 log-rate={:.6f}, "
          "sampled endpoint max={:.6f}".format(
              row["phase_mesh"] / math.pi, row["limiting_endpoint"],
              row["u1_endpoint_log_mod"], row["sampled_endpoint_max_log_mod"]))
print("Required squared rate: 0.0625; diagnostic has no rigorous bounds.")
print("Sampled all-real-y factor-envelope integral rate:", output["sampled_factor_integral_rate"])
print("Failures: no error enclosure; no full response or diagonal.")
print(path)
