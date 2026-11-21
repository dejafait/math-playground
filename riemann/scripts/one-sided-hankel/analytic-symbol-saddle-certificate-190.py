"""Exact interval enclosure for the L719 saddle; not a symbol certificate."""
from fractions import Fraction as F
from math import comb, factorial
from pathlib import Path
import hashlib
import json

S = 1 << 120
U, A, p, b = F(121, 64), F(27, 10), F(3, 10), F(2, 5)
K, x0 = 80, F(4019, 10000)

def ceildiv(a, b):
    return -((-a) // b)

def fixed(x):
    x = F(x)
    return x.numerator * S // x.denominator, ceildiv(x.numerator * S, x.denominator)

def add(x, y):
    return x[0] + y[0], x[1] + y[1]

def neg(x):
    return -x[1], -x[0]

def mul(x, y):
    corners = [a * b for a in x for b in y]
    return min(corners) // S, ceildiv(max(corners), S)

def cmul(x, y):
    return (add(mul(x[0], y[0]), neg(mul(x[1], y[1]))),
            add(mul(x[0], y[1]), mul(x[1], y[0])))

def exp_minus(x):
    assert 0 <= x <= 1
    hi = sum(((-x)**j / F(factorial(j)) for j in range(41)), F(0))
    lo = hi - x**41 / F(factorial(41))
    return fixed(lo)[0], fixed(hi)[1]

def trig(x):
    assert 0 <= x <= 1
    cs = sum(((-1)**j * x**(2*j) / F(factorial(2*j)) for j in range(21)), F(0))
    sn = sum(((-1)**j * x**(2*j+1) / F(factorial(2*j+1)) for j in range(21)), F(0))
    return ((fixed(cs-x**42/F(factorial(42)))[0], fixed(cs)[1]),
            (fixed(sn-x**43/F(factorial(43)))[0], fixed(sn)[1]))

def log_interval(x):
    r = (x-1)/(x+1)
    assert 0 <= r < 1
    lo = 2*sum((r**(2*j+1)/F(2*j+1) for j in range(12)), F(0))
    return lo, lo+2*r**25/(25*(1-r*r))

def enc(x):
    x = F(x)
    return {"numerator": x.numerator, "denominator": x.denominator, "decimal_preview": float(x)}

def interval(x):
    return [enc(F(t, S)) for t in x]

moments, moment_rows = [], []
power, e0 = fixed(1), exp_minus(1/(2*U))
for k in range(1, K+1):
    e = [F(0)] + [F(k*(-1)**(l+1), l+2)/U**(l+1) for l in range(1, k)]
    h = [F(1)]
    for m in range(1, k):
        h.append(sum((l*e[l]*h[m-l] for l in range(1, m+1)), F(0))/m)
    ck = sum((comb(k, k-1-m)*h[m] for m in range(k)), F(0))/k
    power = mul(power, e0)
    moment = mul(fixed(ck), power)
    moments.append(moment)
    moment_rows.append({"k": k, "rational_coefficient": enc(ck), "moment": interval(moment)})

l1, l2 = log_interval(F(9, 5)), log_interval(F(201, 121))
omega = [A*(l1[j]-F(4, 5)+F(121, 100)*l2[j]) for j in (0, 1)]
xlo, xhi = (omega[0]-F(1, 3000))/A, (omega[1]+F(1, 3000))/A
distance = max(abs(x0-xlo), abs(xhi-x0))
tail, lip = 10*F(9, 10)**81, F(45)
error = tail + lip*distance
cosine, sine = trig(b*x0)
radius = exp_minus(p*x0)
z = mul(radius, cosine), neg(mul(radius, sine))
zk, total, rows = (fixed(1), fixed(0)), (fixed(0), fixed(0)), []
for k, m in enumerate(moments, 1):
    zk = cmul(zk, z)
    term = mul(m, zk[0]), mul(m, zk[1])
    total = add(total[0], term[0]), add(total[1], term[1])
    rows.append({"k": k, "real": interval(term[0]), "imag": interval(term[1])})
re_bounds = [F(total[0][0], S)-error, F(total[0][1], S)+error]
im_bounds = [F(total[1][0], S)-error, F(total[1][1], S)+error]
checks = {}

def check(name, actual, relation, required):
    actual, required = F(actual), F(required)
    passed = {"<": actual < required, ">": actual > required}[relation]
    checks[name] = {"actual": enc(actual), "relation": relation,
                    "required": enc(required), "passed": passed}

check("x_lower", xlo, ">", F(2, 5))
check("x_upper", xhi, "<", F(41, 100))
check("radius_upper", F(exp_minus(p*F(2, 5))[1], S), "<", F(9, 10))
check("cosine_lower", 1-(b*F(41, 100))**2/2, ">", F(9, 10))
check("s_real_lower", re_bounds[0], ">", F(9, 5))
check("s_real_upper", re_bounds[1], "<", F(37, 20))
check("s_imag_lower", im_bounds[0], ">", -F(37, 20))
check("s_imag_upper", im_bounds[1], "<", -F(9, 5))
check("s_radius_squared_lower", 2*F(9, 5)**2, ">", F(5, 2)**2)
check("s_radius_squared_upper", 2*F(37, 20)**2, "<", F(21, 8)**2)
check("concavity_radius_condition", F(5, 2)**2, ">", U)
check("resolvent_radial_separation", F(11, 4)-F(21, 8), ">", F(1, 9))
check("angular_hessian_lower", F(3, 20)*F(5, 2), ">", F(1, 3))
check("lower_arc_cosine_gap", (F(24, 35)-F(1, 10))*F(1, 10), ">", F(1, 20))
check("upper_arc_sine_lower_squared", 1-(F(37, 50)+F(1, 20))**2, ">", F(3, 5)**2)

result = {"purpose": __doc__, "arithmetic": "Exact rational; outward fixed point 2^120",
          "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
          "parameters": {"scale": S, "moment_cutoff": K, "x0": enc(x0)},
          "bounds": {"omega": [enc(x) for x in omega], "x": [enc(xlo), enc(xhi)],
                     "distance": enc(distance), "tail": enc(tail), "lipschitz": enc(lip),
                     "total_error": enc(error), "center_sum": [interval(t) for t in total],
                     "s_real": [enc(x) for x in re_bounds], "s_imag": [enc(x) for x in im_bounds]},
          "moment_rows": moment_rows, "sum_rows": rows, "checks": checks,
          "failures": [k for k, v in checks.items() if not v["passed"]],
          "qualifications": ["All of I is covered by the analytic tail and derivative bounds.",
                             "Complex-neighborhood extension and contour proof are in L719.",
                             "No factorial remainder, signed bump rate or RH conclusion."]}
path = Path(__file__).with_suffix(".json")
path.write_text(json.dumps(result, indent=2)+"\n")
for name, row in checks.items():
    print(f"{name}: actual {row['actual']['decimal_preview']:.12g} {row['relation']} required {row['required']['decimal_preview']:.12g}; pass={row['passed']}")
print("Failures:", result["failures"], "Full certificate:", path)
if result["failures"]:
    raise SystemExit(1)
