"""Independent exact finite audit of L969; analytic limits remain in the lemma.

Uses only the standard library, no construction/audit utilities or old certificate.
Reconstructs tensors from the formal logarithm and enumerates all labeled faces.
"""
from fractions import Fraction as F
from itertools import combinations, permutations, product
from math import comb, factorial
from pathlib import Path
import json

NAMES = ("a0", "a1", "a2", "c0", "c1")
ZERO = (0,) * len(NAMES)


def const(c):
    return {ZERO: F(c)} if c else {}


def var(i):
    return {tuple(int(j == i) for j in range(len(NAMES))): F(1)}


def add(*ps):
    out = {}
    for p in ps:
        for e, c in p.items():
            out[e] = out.get(e, F(0)) + c
    return {e: c for e, c in out.items() if c}


def scale(p, c):
    return {e: v * c for e, v in p.items() if v * c}


def mul(p, r):
    out = {}
    for e, c in p.items():
        for f, d in r.items():
            key = tuple(x + y for x, y in zip(e, f))
            out[key] = out.get(key, F(0)) + c * d
    return {e: c for e, c in out.items() if c}


def prod(ps):
    out = const(1)
    for p in ps:
        out = mul(out, p)
    return out


def serial(p):
    return [{"powers": list(e), "coefficient": str(c)} for e, c in sorted(p.items())]


checks = []


def equal(label, actual, required):
    checks.append({"label": label, "passed": actual == required,
                   "actual": actual, "required": required})


orders = {}
for n in (2, 3):
    h, q, b = 64 * 9 ** n, 8 * 3 ** n, F(1, 4)
    delta = h - b
    p = (n - 1) // 2
    v = [F(comb(n, 2 * i + 1), 4 ** i) for i in range(p + 1)]
    w = [sum((v[i] * v[j] for i in range(p + 1)
              for j in range(p + 1) if i + j == s), F(0)) for s in range(2 * p + 1)]
    D = [sum((w[s] * comb(n - 1 - s, r) * b ** (n - 1 - s - r)
              for s in range(min(2 * p, n - 1 - r) + 1)), F(0)) for r in range(n)]
    d = {k: h * sum((D[r] / delta ** (n - k - r + 1)
                     for r in range(n - k + 1)), F(0)) for k in range(1, n + 1)}
    expected_d = ({1: 4 * h ** 2 / delta ** 2, 2: h / delta} if n == 2 else
                  {1: h * (3 * delta + 1) ** 2 / delta ** 3,
                   2: h * (6 * delta + 1) / delta ** 2, 3: h / delta})
    equal(f"n={n} coefficients", {k: str(x) for k, x in d.items()},
          {k: str(x) for k, x in expected_d.items()})

    # k*d_k [z^k] log(1+sum_{r>=1} I_r z^r/(r! I_0)),
    # multiplied by I_0(b)^n I_0(h); enumerate ordered compositions.
    tensors = {}
    for k in range(1, n + 1):
        for ell in range(1, k + 1):
            for rs in product(range(1, k + 1), repeat=ell):
                if sum(rs) != k:
                    continue
                c = k * d[k] * F((-1) ** (ell - 1), ell)
                for r in rs:
                    c /= factorial(r)
                factors = tuple(sorted([f"b{r}" for r in rs] + ["b0"] * (n - ell) + ["h0"]))
                tensors[factors] = tensors.get(factors, F(0)) + c
    tensors[tuple(["b0"] * n + ["h1"])] = -d[1]
    expected = {
        tuple(["b0"] * (n - 1) + ["b1", "h0"]): d[1],
        tuple(["b0"] * (n - 1) + ["b2", "h0"]): d[2],
        tuple(["b0"] * (n - 2) + ["b1", "b1", "h0"]): -d[2],
        tuple(["b0"] * n + ["h1"]): -d[1],
    }
    if n == 3:
        expected.update({("b0", "b0", "b3", "h0"): d[3] / 2,
                         ("b0", "b1", "b2", "h0"): -3 * d[3] / 2,
                         ("b1", "b1", "b1", "h0"): d[3]})
    equal(f"n={n} complete tensors", {str(k): str(v) for k, v in tensors.items()},
          {str(k): str(v) for k, v in expected.items()})

    a0, a1, a2, c0, c1 = map(var, range(5))
    live = {"b0": {}, "b1": scale(a0, 2), "b2": scale(a1, 4),
            "b3": scale(a2, 6), "h0": scale(c0, 2 * delta),
            "h1": add(scale(c0, 2), scale(c1, 2 * delta))}
    origin = {key: const(F(1, 2)) if key in ("b0", "h0") else {} for key in live}
    # The expected strata are L967(11)-(12), used as comparison data only.
    if n == 2:
        strata = [
            {},
            add(scale(a0, d[1]/2), scale(a1, d[2]), scale(c0, -d[1]/2), scale(c1, -d[1]*delta/2)),
            add(scale(mul(c0, a0), 2*delta*d[1]), scale(mul(c0, a1), 4*delta*d[2]), scale(mul(a0, a0), -2*d[2])),
            scale(prod([c0, a0, a0]), -8*delta*d[2]),
        ]
    else:
        strata = [
            {},
            add(scale(a0, d[1]/4), scale(a1, d[2]/2), scale(a2, 3*d[3]/8), scale(c0, -d[1]/4), scale(c1, -d[1]*delta/4)),
            add(scale(mul(c0, a0), delta*d[1]), scale(mul(c0, a1), 2*delta*d[2]), scale(mul(c0, a2), 3*delta*d[3]/2), scale(mul(a0, a0), -d[2]), scale(mul(a0, a1), -3*d[3])),
            add(scale(prod([c0, a0, a0]), -4*delta*d[2]), scale(prod([c0, a0, a1]), -12*delta*d[3]), scale(prod([a0, a0, a0]), 4*d[3])),
            scale(prod([c0, a0, a0, a0]), 16*delta*d[3]),
        ]
    faces = []
    for size in range(n + 2):
        for subset in combinations(range(n + 1), size):
            value = {}
            for factors, coefficient in tensors.items():
                for placement in permutations(factors):  # repeated factors included
                    term = prod([(live if i in subset else origin)[f] for i, f in enumerate(placement)])
                    value = add(value, scale(term, coefficient / factorial(n + 1)))
            required = scale(strata[size], F(1, comb(n + 1, size)))
            residual = add(value, scale(required, -1))
            equal(f"n={n} face {subset}", serial(residual), [])
            faces.append({"live_coordinates": list(subset), "moment": serial(value),
                          "restored_origin_count": n + 1 - size,
                          "restoration_multiplier": f"[2*gamma*(c0+c1)]^{n+1-size}",
                          "residual": serial(residual)})

    # Analytically verified leading exponential data, with gamma formal.
    leading = {"b0": (F(q), 1, F(1, 4*q), 1), "h0": (F(q), 1, F(1, 4*q), 1),
               "h1": (F(q), 1, delta / (2*q), 0),
               "b1": (F(1, 2), 0, F(1), 0), "b2": (F(1, 2), 1, F(2), 0),
               "b3": (F(1, 2), 2, F(3), 0)}
    rates = []
    for factors, coefficient in tensors.items():
        rate, degree, gamma_power = F(0), 0, 0
        for factor in factors:
            r, deg, c, gp = leading[factor]
            rate += r
            degree += deg
            coefficient *= c
            gamma_power += gp
        rates.append({"factors": list(factors), "rate": str(rate), "degree": degree,
                      "coefficient_without_gamma": str(coefficient), "gamma_power": gamma_power})
    retained = next(t for t in rates if "h1" in t["factors"])
    compensation_rate = max(F(t["rate"]) for t in rates if "h0" in t["factors"])
    formula = -d[1] * delta / (2*q) * F(1, 4*q) ** n
    required_scalar = -F(36, 20735) if n == 2 else -F(313457776129, 207992562237775872)
    equal(f"n={n} retained coefficient", retained["coefficient_without_gamma"], str(formula))
    equal(f"n={n} stated rational coefficient", str(formula), str(required_scalar))
    equal(f"n={n} retained degree", retained["degree"], n + 1)
    equal(f"n={n} retained gamma power", retained["gamma_power"], n)
    equal(f"n={n} retained rate", retained["rate"], str((n + 1) * q))
    equal(f"n={n} compensation rate", str(compensation_rate), str(n*q + F(1, 2)))
    equal(f"n={n} strict rate gap", compensation_rate < (n + 1)*q, True)
    equal(f"n={n} strict negative scalar", formula < 0, True)
    orders[str(n)] = {"h": h, "q": q, "delta": str(delta), "D": list(map(str, D)),
                      "d": {str(k): str(x) for k, x in d.items()}, "faces": faces,
                      "diagonal_term_leading_data": rates, "limit_without_gamma_power_n": str(formula),
                      "compensation_rate_bound": str(compensation_rate), "dominant_rate": str((n+1)*q)}

failures = [c for c in checks if not c["passed"]]
certificate = {"scope": "L969 independent finite audit at n=2,3 only",
               "analytic_premises": ["A is strictly positive and has L019 decay",
                  "gamma=1/[2(c0+c1)] is fixed, finite and positive",
                  "integral A Z=1/2; each restored origin multiplier equals 1",
                  "the exact hyperbolic formulas imply the stated leading data",
                  "normalized symmetrization equals the product on the diagonal"],
               "moment_variables": NAMES, "orders": orders, "checks": checks,
               "failures": failures, "passed": not failures,
               "limitations": "No numerical normalization or integrated sign. Analytic convergence is proved in L969."}
path = Path(__file__).with_suffix(".json")
path.write_text(json.dumps(certificate, indent=2) + "\n")
print(f"Exact checks: {len(checks)-len(failures)}/{len(checks)}; failures: {len(failures)}; certificate: {path}")
for n, order in orders.items():
    print(f"n={n}: faces={len(order['faces'])}; actual compensation rate={order['compensation_rate_bound']} < required dominant rate={order['dominant_rate']}; actual limit/gamma^{n}={order['limit_without_gamma_power_n']} < required 0")
if failures:
    print("Failed labels: " + ", ".join(c["label"] for c in failures))
    raise SystemExit(1)
