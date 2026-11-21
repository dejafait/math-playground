#!/usr/bin/env python3
"""Exact finite formal coefficient certificate; no floating arithmetic or API.

Run from the notebook: python3 scripts/grunsky/degree-six-deficit-1253.py
The polynomial ring has six variables; bivariate series are truncated by
total degree at six. The JSON retains every mixed coefficient, including
the interior Taylor formulas, reciprocal substitution and zero residuals.
"""
from fractions import Fraction as F
from pathlib import Path
import json

N = 6
ZERO_EXP = (0,) * N


def constant(value):
    return {ZERO_EXP: F(value)} if value else {}


def variable(index):
    exponents = list(ZERO_EXP)
    exponents[index] = 1
    return {tuple(exponents): F(1)}


def add(*polynomials):
    result = {}
    for p in polynomials:
        for exponents, coefficient in p.items():
            result[exponents] = result.get(exponents, F(0)) + coefficient
    return {e: c for e, c in result.items() if c}


def scale(p, coefficient):
    return {e: c * coefficient for e, c in p.items() if c * coefficient}


def multiply(p, q):
    result = {}
    for e, c in p.items():
        for d, v in q.items():
            exponent = tuple(a + b for a, b in zip(e, d))
            result[exponent] = result.get(exponent, F(0)) + c * v
    return {e: c for e, c in result.items() if c}


def power(p, exponent):
    result = constant(1)
    for _ in range(exponent):
        result = multiply(result, p)
    return result


def substitute(p, values):
    result = {}
    for e, c in p.items():
        term = constant(c)
        for value, exponent in zip(values, e):
            term = multiply(term, power(value, exponent))
        result = add(result, term)
    return result


def series_multiply(p, q):
    result = {}
    for (i, j), c in p.items():
        for (k, ell), d in q.items():
            key = (i + k, j + ell)
            if sum(key) <= N:
                result[key] = add(result.get(key, {}), multiply(c, d))
    return {e: c for e, c in result.items() if c}


def minus_log_one_plus(u):
    assert all(0 < sum(e) <= N for e in u)
    result = {}
    current = {(0, 0): constant(1)}
    for k in range(1, N + 1):
        current = series_multiply(current, u)
        for key, coefficient in current.items():
            result[key] = add(result.get(key, {}), scale(coefficient, F((-1) ** k, k)))
    return {e: c for e, c in result.items() if c}


def render(p, names):
    if not p:
        return "0"
    terms = []
    for exponents, coefficient in sorted(p.items(), reverse=True):
        factors = [str(abs(coefficient))]
        factors += [name + (f"^{e}" if e != 1 else "")
                    for name, e in zip(names, exponents) if e]
        terms.append(("-" if coefficient < 0 else "+", "*".join(factors)))
    first, *rest = terms
    return ("-" if first[0] == "-" else "") + first[1] + "".join(
        f" {sign} {term}" for sign, term in rest)


def encode(p, names):
    return {"expression": render(p, names), "terms": [
        {"exponents": list(e), "coefficient": str(c)} for e, c in sorted(p.items())]}


def main():
    a = [variable(i) for i in range(N)]  # a_2 through a_7
    b = [variable(i) for i in range(N)]  # b_0 through b_5
    inside_u = {(k - 1 - j, j): a[k - 2]
                for k in range(2, 8) for j in range(k)}
    outside_u = {(i, k + 1 - i): scale(b[k], -1)
                 for k in range(1, 6) for i in range(1, k + 1)}
    inside = minus_log_one_plus(inside_u)
    outside = minus_log_one_plus(outside_u)
    mixed = [(m, n) for m in range(1, 6) for n in range(m, 6)
             if m + n <= N]
    assert len(mixed) == 9

    # Coefficients d_k of (1+a_2*t+...+a_7*t^6)^(-1).
    reciprocal = [constant(1)]
    for k in range(1, 7):
        reciprocal.append(scale(add(*(multiply(a[i - 1], reciprocal[k - i])
                                      for i in range(1, k + 1))), -1))
    b_of_a = reciprocal[1:]
    reciprocal_residuals = {f"{m},{n}": add(inside.get((m, n), {}), scale(
        substitute(outside.get((m, n), {}), b_of_a), -1)) for m, n in mixed}
    symmetry_residuals = {f"{m},{n}": add(outside.get((m, n), {}), scale(
        outside.get((n, m), {}), -1)) for m, n in mixed}
    assert not any(reciprocal_residuals.values())
    assert not any(symmetry_residuals.values())

    # Independent source identities from Teo Section 2.2, preprint p.5.
    source = {(1, n): b[n] for n in range(1, 6)}
    source[(2, 2)] = add(b[3], scale(power(b[1], 2), F(1, 2)))
    source[(2, 3)] = add(b[4], multiply(b[1], b[2]))
    source[(3, 3)] = add(b[5], multiply(b[1], b[3]), power(b[2], 2),
                         scale(power(b[1], 3), F(1, 3)))
    source_residuals = {f"{m},{n}": add(outside[(m, n)], scale(p, -1))
                        for (m, n), p in source.items()}
    assert not any(source_residuals.values())

    # Ring variables: tau,S_2,S_3,S_4,S_5,S_6. b_0 is immaterial.
    tau = variable(0)
    S = {k: variable(k - 1) for k in range(2, 7)}
    b_values = [{}, add(constant(1), scale(multiply(tau, S[2]), -1))]
    b_values += [scale(multiply(tau, S[k]), -1) for k in range(3, 7)]
    prescribed = {(m, n): add(constant(F(1, m) if m == n else 0),
                              scale(multiply(tau, S[m + n]), -1))
                  for m, n in mixed}
    deficit_residuals = {f"{m},{n}": add(substitute(outside[(m, n)], b_values),
                                          scale(prescribed[(m, n)], -1))
                         for m, n in mixed}
    x, y, z = b_values[1:4]
    required_residuals = {
        "2,2": scale(add(power(x, 2), constant(-1)), F(1, 2)),
        "2,3": multiply(x, y),
        "2,4": add(multiply(x, z), scale(power(y, 2), F(1, 2))),
        "3,3": add(multiply(x, z), power(y, 2),
                     scale(add(power(x, 3), constant(-1)), F(1, 3))),
    }
    for key, p in deficit_residuals.items():
        assert not add(p, scale(required_residuals.get(key, {}), -1))

    # Algebraic elimination without division by tau, S_k or x:
    # x^2-1=0 and x*y=0 imply y=x*(x*y)-y*(x^2-1)=0.
    # Then x*z=0 implies z=x*(x*z)-z*(x^2-1)=0.
    # The last equation leaves x^3-1=0; subtract x*(x^2-1) to get x-1=0.
    X, Y, Z = (variable(i) for i in range(3))
    e1 = add(power(X, 2), constant(-1))
    e2 = multiply(X, Y)
    e3 = add(multiply(X, Z), scale(power(Y, 2), F(1, 2)))
    e4 = add(multiply(X, Z), power(Y, 2),
             scale(add(power(X, 3), constant(-1)), F(1, 3)))
    elimination = {
        "y": add(multiply(X, e2), scale(multiply(Y, e1), -1), scale(Y, -1)),
        "z_given_y_zero": add(multiply(X, multiply(X, Z)),
                                 scale(multiply(Z, e1), -1), scale(Z, -1)),
        "x_minus_one_given_y_z_zero": add(power(X, 3), constant(-1),
                                           scale(multiply(X, e1), -1),
                                           scale(add(X, constant(-1)), -1)),
    }
    assert not any(elimination.values())

    # S_2=S_3=S_4=0 suffices algebraically through total degree six.
    degenerate_values = [tau, {}, {}, {}, S[5], S[6]]
    compatible_residuals = {key: substitute(p, degenerate_values)
                            for key, p in deficit_residuals.items()}
    assert not any(compatible_residuals.values())

    a_names = [f"a_{i}" for i in range(2, 8)]
    b_names = [f"b_{i}" for i in range(6)]
    s_names = ["tau"] + [f"S_{i}" for i in range(2, 7)]
    certificate = {
        "kind": "exact rational polynomial coefficient certificate",
        "cutoff": 6,
        "hypotheses": "real normalized a_2,...,a_7; tau>0; actual S_k from L025",
        "source": "Teo2003, hep-th/0305005v2, Section2.2, (2.3)-(2.4),(2.8)-(2.12), p5",
        "interior_mixed": {f"{m},{n}": encode(inside[(m, n)], a_names) for m, n in mixed},
        "exterior_mixed": {f"{m},{n}": encode(outside[(m, n)], b_names) for m, n in mixed},
        "reciprocal_b_of_a": {f"b_{i}": encode(p, a_names) for i, p in enumerate(b_of_a)},
        "verification": {
            "reciprocal_mixed_residuals": {k: encode(p, a_names) for k, p in reciprocal_residuals.items()},
            "symmetry_residuals": {k: encode(p, b_names) for k, p in symmetry_residuals.items()},
            "source_residuals": {k: encode(p, b_names) for k, p in source_residuals.items()},
            "elimination_residuals": {k: encode(p, ["x", "y", "z", "u", "v", "w"])
                                      for k, p in elimination.items()},
            "degenerate_sufficiency_residuals": {k: encode(p, s_names)
                                                  for k, p in compatible_residuals.items()},
        },
        "deficit_residuals": {k: encode(p, s_names) for k, p in deficit_residuals.items()},
        "necessary_and_sufficient_through_degree_six": "S_2=S_3=S_4=0 for tau>0; b_0 free",
        "exceptional_branches": {
            "x_plus_one": "tau*S_2=0; excluded for actual Xi by tau>0 and L027 S_2>0",
            "x_minus_one": "tau*S_2=2; degree5 requires S_3=0, excluded by L027 S_3>0",
            "tau_zero": "excluded hypothesis; diagonal coefficients are formally compatible",
        },
        "actual_Xi_result": "NO JET: L027 S_2,S_3>0 contradict degree<=5 compatibility",
        "actual_required": "degree4 requires tau*S_2=2; degree5 then requires S_3=0",
        "actual_available": "L027: S_2>0 and S_3>0, unconditionally, without numerical enclosures",
        "limitations": "No statement about RH, other Grunsky ansatzes, analytic univalence or all-degree positivity.",
        "failures": [],
    }
    destination = Path(__file__).with_name("degree-six-deficit-certificate-1253.json")
    destination.write_text(json.dumps(certificate, indent=2) + "\n")
    print("PASS: 9 exact mixed coefficients through degree 6; all reciprocal/source/symmetry/elimination residuals zero.")
    print("ACTUAL RESULT: no fixed-deficit real formal jet for any tau>0; contradiction already at degree 5.")
    print("REQUIRED: tau*S_2=2 then S_3=0. AVAILABLE: L027 S_2>0,S_3>0. No numerical bound required.")
    print("FAILURES: none. Full certificate:", destination)


if __name__ == "__main__":
    main()
