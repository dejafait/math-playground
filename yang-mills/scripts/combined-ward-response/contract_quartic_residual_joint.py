"""Exact rational contraction of L152's finite words; no heat evaluation.

Projection entries stay symbolic. All output is saved, including the
surviving coefficients after compact-support integration by parts.
"""
from collections import defaultdict
from fractions import Fraction as Q
from functools import lru_cache
from itertools import combinations, permutations, product
from pathlib import Path
import json
from check_quartic_residual_inversion import shift, word, clovers

ZERO = (0, 0, 0, 0)


def add(target, key, value):
    target[key] += value


def inverse(w):
    return tuple((x, mu, -s) for x, mu, s in reversed(w))


@lru_cache(None)
def jet(w, m):
    out = defaultdict(Q)

    def rec(j, remaining, factors, coeff):
        if j == len(w):
            if remaining == 0:
                out[factors] += coeff
            return
        x, mu, sign = w[j]
        factorial = 1
        for n in range(remaining + 1):
            if n:
                factorial *= n
            if mu == 0 and n:
                continue
            rec(j + 1, remaining - n, factors + ((x, mu),) * n,
                coeff * Q(sign ** n, factorial))

    rec(0, m, (), Q(1))
    return tuple((k, v) for k, v in out.items() if v)


@lru_cache(None)
def clover(z, rho, nu, m):
    if rho == nu:
        return ()
    out = defaultdict(Q)
    for w in clovers(z, rho, nu):
        for ww, sign in ((w, 1), (inverse(w), -1)):
            for factors, coeff in jet(ww, m):
                out[factors] += Q(sign, 8) * coeff
    return tuple((k, v) for k, v in out.items() if v)


@lru_cache(None)
def force(nu, m):
    out = defaultdict(Q)
    edge = (ZERO, nu)
    for rho in range(4):
        if rho == nu:
            continue
        low, high = sorted((rho, nu))
        for corner in (ZERO, shift(ZERO, rho, -1)):
            w = word(corner, ((low, 1), (high, 1),
                              (low, -1), (high, -1)))
            at = [j for j, (x, mu, _) in enumerate(w)
                  if (x, mu) == edge]
            assert len(at) == 1
            j = at[0]
            sign = w[j][2]
            # Positive central edge first; negative central edge last.
            start = j if sign == 1 else (j + 1) % len(w)
            w = w[start:] + w[:start]
            for ww, invsign in ((w, 1), (inverse(w), -1)):
                for factors, coeff in jet(ww, m):
                    out[factors] += Q(sign * invsign, 2) * coeff
    return tuple((k, v) for k, v in out.items() if v)


@lru_cache(None)
def generator(nu, rho, endpoint, m):
    out = defaultdict(Q)
    z = ZERO if endpoint == 0 else shift(ZERO, nu)
    edge = (ZERO, nu)
    for s in range(1, m + 1):
        for r in range(m - s + 1):
            t = m - s - r
            if endpoint == 0 and (r or t):
                continue
            if nu == 0 and (r or t):
                continue
            factorial_r = 1
            factorial_t = 1
            for n in range(1, r + 1):
                factorial_r *= n
            for n in range(1, t + 1):
                factorial_t *= n
            for factors, coeff in clover(z, rho, nu, s):
                out[(edge,) * r + factors + (edge,) * t] += (
                    Q((-1) ** t, 2 * factorial_r * factorial_t) * coeff)
    return tuple((k, v) for k, v in out.items() if v)


def cyclic(factors):
    return min(factors[j:] + factors[:j] for j in range(4))


def force_words(nu, rho, endpoint):
    out = defaultdict(Q)
    for m in (1, 2, 3):
        for left, a in force(nu, m):
            for right, b in generator(nu, rho, endpoint, 4 - m):
                out[cyclic(left + right)] += -2 * a * b
    return {k: v for k, v in out.items() if v}


def insertion_words():
    out = defaultdict(Q)
    for mu, nu in combinations(range(4), 2):
        w = word(ZERO, ((mu, 1), (nu, 1), (mu, -1), (nu, -1)))
        for factors, coeff in jet(w, 4):
            for r in (mu, nu):
                out[(r, r, cyclic(factors))] += 4 * coeff
        for alpha in range(4):
            for m in (1, 2, 3):
                for left, a in clover(ZERO, mu, alpha, m):
                    for right, b in clover(ZERO, nu, alpha, 4 - m):
                        for r, j in ((nu, mu), (mu, nu)):
                            out[(r, j, cyclic(left + right))] += 2 * a * b
    return {k: v for k, v in out.items() if v}


@lru_cache(None)
def projection_key(first, second):
    """Canonical signed edge covariance under cubic isometries.

    P = gradient covariance, so each reversed edge contributes -1.
    Coordinates are positive-edge tails, not midpoint phase substitutes.
    """
    x, mu = first
    y, eta = second
    assert mu != 0 and eta != 0
    delta = tuple(y[j] - x[j] for j in (1, 2, 3))
    mu -= 1
    eta -= 1
    candidates = []
    for perm in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            # Coordinate k becomes coordinate perm[k], with sign signs[k].
            d = [0, 0, 0]
            for k in range(3):
                d[perm[k]] = signs[k] * delta[k]
            a, b = perm[mu], perm[eta]
            # Reflection takes a positive tail to R x - e_a.
            if signs[eta] < 0:
                d[b] -= 1
            if signs[mu] < 0:
                d[a] += 1
            sign = signs[mu] * signs[eta]
            candidates.append(((a, b, tuple(d)), sign))
            candidates.append(((b, a, tuple(-n for n in d)), sign))
    key = min(k for k, _ in candidates)
    possible = {s for k, s in candidates if k == key}
    return key, (0 if len(possible) == 2 else next(iter(possible)))


def pairings(factors):
    """12 K:H:P for one trace word, after all three colors.

    There are six choices of exterior positions, and coefficient 2.
    Tr(t_a t_b t_c t_d)=(delta_ab delta_cd-delta_ac delta_bd
                         +delta_ad delta_bc)/8.
    The crossing pair has color sum -3/8; either other pair has 9/8.
    """
    for ext in combinations(range(4), 2):
        internal = tuple(j for j in range(4) if j not in ext)
        pkey, sign = projection_key(*(factors[j] for j in internal))
        if not sign:
            continue
        crossing = ext in ((0, 2), (1, 3))
        weight = Q(-3 if crossing else 9, 4) * sign
        yield ext, internal, pkey, weight


def clean(rows):
    return {key: value for key, value in rows.items() if value}


def serial(rows):
    return [dict(key=key, coefficient=str(value))
            for key, value in sorted(clean(rows).items())]


def green_key(x):
    return tuple(sorted((abs(n) for n in x), reverse=True))


def green_coefficients(rows):
    """P_ab(delta)=G(delta+e_b-e_a)-G(delta-e_a)-G(delta+e_b)+G(delta)."""
    out = defaultdict(Q)
    for (a, b, delta), value in rows.items():
        for da, db, sign in ((-1, 1, 1), (-1, 0, -1),
                             (0, 1, -1), (0, 0, 1)):
            x = list(delta)
            x[a] += da
            x[b] += db
            out[green_key(x)] += value * sign
    return clean(out)


def scalar_group(rows, prefix):
    return {pk: value for key, value in clean(rows).items()
            if key[:-1] == prefix for pk in (key[-1],)}


def reduced_green(rows):
    # Output coordinates are (constant, x=G000-G110, y=G110-G111).
    # These substitutions use Delta G=delta at 000,100,110,111.
    g0 = (Q(0), Q(0), Q(0), Q(1))
    g1 = (Q(-1, 6), Q(0), Q(0), Q(1))
    g11 = (Q(0), Q(-1), Q(0), Q(1))
    g111 = (Q(0), Q(-1), Q(-1), Q(1))

    def combine(*terms):
        return tuple(sum(weight * v[j] for weight, v in terms) for j in range(4))

    substitution = {(0, 0, 0): g0, (1, 0, 0): g1,
                    (1, 1, 0): g11, (1, 1, 1): g111,
                    (2, 0, 0): combine((6, g1), (-1, g0), (-4, g11)),
                    (2, 1, 0): combine((3, g11), (-1, g1), (-1, g111)),
                    (2, 1, 1): combine((2, g111), (-1, g11))}
    return combine(*((v, substitution[k]) for k, v in rows.items()))


def finite_check(failures):
    """Separate exact Pauli multiplication and matrix-series route.

    The matrix route uses convolution of exponential coefficients, not
    the compositions in jet(). Its deterministic packet checks the full
    degree-four force at every endpoint/displacement/edge placement.
    """
    one = (Q(1), Q(0), Q(0), Q(0))
    zero = (Q(0),) * 4

    def plus(a, b):
        return tuple(x + y for x, y in zip(a, b))

    def scale(a, b):
        return tuple(b * x for x in a)

    def mul(a, b):
        cross = (a[2]*b[3]-a[3]*b[2], a[3]*b[1]-a[1]*b[3],
                 a[1]*b[2]-a[2]*b[1])
        return (a[0]*b[0]-sum(a[j]*b[j] for j in (1, 2, 3))/4,
                *(a[0]*b[j]+b[0]*a[j]-cross[j-1]/2 for j in (1, 2, 3)))

    colors = [(Q(0), *(Q(int(c == j)) for j in range(3))) for c in range(3)]
    color_sums = []
    for arrangement, expected in (((0, 0, 1, 1), Q(9, 8)),
                                  ((0, 1, 0, 1), Q(-3, 8)),
                                  ((0, 1, 1, 0), Q(9, 8))):
        total = Q(0)
        for c in colors:
            for d in colors:
                result = one
                for j in arrangement:
                    result = mul(result, (c, d)[j])
                total += 2 * result[0]
        color_sums.append(dict(arrangement=arrangement, actual=str(total),
                               required=str(expected), passed=total == expected))
        if total != expected:
            failures.append("Pauli color contraction")

    def packet(edge):
        x, mu = edge
        if mu == 0:
            return zero
        return (Q(0), *(Q(((c + 2) * (mu + 1) +
                            sum((j + c + 1)*x[j] for j in range(4))) % 7 - 3)
                        for c in range(3)))

    def conv(a, b):
        return [sum_quaternions(mul(a[r], b[m-r]) for r in range(m+1))
                for m in range(5)]

    def sum_quaternions(values):
        out = zero
        for value in values:
            out = plus(out, value)
        return out

    @lru_cache(None)
    def exponential(edge, sign):
        result = [one]
        for m in range(1, 5):
            result.append(scale(mul(result[-1], packet(edge)), Q(sign, m)))
        return result

    @lru_cache(None)
    def loop(w):
        out = [one] + [zero]*4
        for x, mu, sign in w:
            out = conv(out, exponential((x, mu), sign))
        return out

    @lru_cache(None)
    def C(z, rho, nu):
        if rho == nu:
            return [zero]*5
        out = [zero]*5
        for w in clovers(z, rho, nu):
            left, right = loop(w), loop(inverse(w))
            out = [plus(out[m], scale(plus(left[m], scale(right[m], -1)), Q(1, 8)))
                   for m in range(5)]
        return out

    @lru_cache(None)
    def expanded_trace(factors):
        result = one
        for factor in factors:
            result = mul(result, packet(factor))
        return 2 * result[0]

    checks = []
    for nu in range(4):
        G = [zero]*5
        for rho in range(4):
            if rho == nu:
                continue
            low, high = sorted((rho, nu))
            for corner in (ZERO, shift(ZERO, rho, -1)):
                w = word(corner, ((low, 1), (high, 1), (low, -1), (high, -1)))
                j = next(j for j, (x, mu, _) in enumerate(w) if (x, mu) == (ZERO, nu))
                sign = w[j][2]
                start = j if sign == 1 else (j+1) % 4
                w = w[start:] + w[:start]
                left, right = loop(w), loop(inverse(w))
                G = [plus(G[m], scale(plus(left[m], scale(right[m], -1)), Q(sign, 2)))
                     for m in range(5)]
        for rho in range(4):
            if rho == nu:
                continue
            for endpoint in (0, 1):
                z = ZERO if endpoint == 0 else shift(ZERO, nu)
                X = C(z, rho, nu)
                if endpoint:
                    X = conv(conv(exponential((ZERO, nu), 1), X),
                             exponential((ZERO, nu), -1))
                X = [scale(v, Q(1, 2)) for v in X]
                actual = -4 * sum(mul(G[m], X[4-m])[0] for m in (1, 2, 3))
                expanded = sum(a * expanded_trace(f) for f, a in
                               force_words(nu, rho, endpoint).items())
                passed = actual == expanded
                checks.append(dict(placement=[nu, rho, endpoint], matrix=str(actual),
                                   word=str(expanded), passed=passed))
                if not passed:
                    failures.append(f"matrix force check {nu,rho,endpoint}")

    insertion_checks = []
    inserted = insertion_words()
    for r in range(4):
        for j in range(4):
            matrix = Q(0)
            for mu, nu in combinations(range(4), 2):
                if r == j and r in (mu, nu):
                    w = word(ZERO, ((mu, 1), (nu, 1), (mu, -1), (nu, -1)))
                    matrix += 8 * loop(w)[4][0]
                if (r, j) in ((mu, nu), (nu, mu)):
                    for alpha in range(4):
                        left, right = C(ZERO, mu, alpha), C(ZERO, nu, alpha)
                        matrix += 4 * sum(mul(left[m], right[4-m])[0] for m in (1, 2, 3))
            expanded = sum(a * expanded_trace(f) for (rr, jj, f), a in inserted.items()
                           if (rr, jj) == (r, j))
            passed = matrix == expanded
            insertion_checks.append(dict(derivative=[r, j], matrix=str(matrix),
                                         word=str(expanded), passed=passed))
            if not passed:
                failures.append(f"matrix insertion check {r,j}")
    return dict(color=color_sums, force=checks, insertion=insertion_checks)


def main():
    # D: d (partial_j u_r) H_mueta; J: d u_r partial_first_j H_mueta.
    # S: u_r H_mueta from the local axial covariance slope.
    D, J, S, frozen = (defaultdict(Q) for _ in range(4))
    word_counts = []
    for nu in range(4):
        for rho in range(4):
            if rho == nu:
                continue
            for endpoint in (0, 1):
                words = force_words(nu, rho, endpoint)
                word_counts.append([nu, rho, endpoint, len(words)])
                for factors, coeff in words.items():
                    for ext, internal, pk, weight in pairings(factors):
                        a, b = (factors[j] for j in ext)
                        mu, eta = a[1], b[1]
                        sym = tuple(sorted((mu, eta)))
                        value = coeff * weight
                        frozen[(rho, *sym, pk)] += value
                        D[(rho, nu, *sym, pk)] += value * Q(2 * endpoint - 1, 2)
                        for j in range(4):
                            ha = Q(a[0][j]) + Q(int(mu == j), 2) - Q(int(nu == j), 2)
                            hb = Q(b[0][j]) + Q(int(eta == j), 2) - Q(int(nu == j), 2)
                            J[(rho, j, mu, eta, pk)] += value * ha
                            J[(rho, j, eta, mu, pk)] += value * hb
                        c, e = (factors[j] for j in internal)
                        slope = Q(c[0][0] + e[0][0] - int(nu == 0), 2)
                        S[(rho, *sym, pk)] += value * slope

    insertions = insertion_words()
    for (r, j, factors), coeff in insertions.items():
        for ext, _, pk, weight in pairings(factors):
            mu, eta = (factors[n][1] for n in ext)
            D[(r, j, *sorted((mu, eta)), pk)] += coeff * weight

    # Compact-support IBP: integral d du H = -integral u [d dH + delta_j0 H].
    for (r, j, mu, eta, pk), value in list(D.items()):
        J[(r, j, mu, eta, pk)] -= value
        J[(r, j, eta, mu, pk)] -= value
        if j == 0:
            S[(r, mu, eta, pk)] -= value

    failures = []
    if clean(frozen):
        failures.append("complete frozen force contraction is not zero")
    groups = {"A": scalar_group(J, (0, 0, 1, 1)),
              "B": scalar_group(S, (0, 1, 1)),
              "C": scalar_group(J, (1, 1, 1, 1)),
              "D": scalar_group(J, (1, 1, 2, 2)),
              "E": scalar_group(J, (1, 2, 1, 2)),
              "F": scalar_group(J, (1, 2, 2, 1))}
    predicted_J, predicted_S = defaultdict(Q), defaultdict(Q)
    for mu in (1, 2, 3):
        for pk, value in groups["A"].items():
            predicted_J[(0, 0, mu, mu, pk)] += value
        for pk, value in groups["B"].items():
            predicted_S[(0, mu, mu, pk)] += value
        for r in (1, 2, 3):
            for pk, value in groups["C" if r == mu else "D"].items():
                predicted_J[(r, r, mu, mu, pk)] += value
    for r, j in permutations((1, 2, 3), 2):
        for pk, value in groups["E"].items():
            predicted_J[(r, j, r, j, pk)] += value
        for pk, value in groups["F"].items():
            predicted_J[(r, j, j, r, pk)] += value
    if clean(predicted_J) != clean(J) or clean(predicted_S) != clean(S):
        failures.append("six-scalar reconstruction")
    checks = finite_check(failures)
    reduced = {name: reduced_green(green_coefficients(rows)) for name, rows in groups.items()}
    expected_reduced = {"A": (Q(-8), Q(60), Q(-6), Q(0)),
                        "B": (Q(10), Q(-42), Q(3), Q(0)),
                        "C": (Q(-4), Q(60), Q(6), Q(0)),
                        "D": (Q(3), Q(0), Q(24), Q(0)),
                        "E": (Q(9, 2), Q(-24), Q(-12), Q(0)),
                        "F": (Q(-3, 2), Q(6), Q(3), Q(0))}
    if reduced != expected_reduced:
        failures.append("Green harmonic reduction")
    certificate = dict(
        scope="Exact finite-word contraction of L152(8), with symbolic phase-correct infinite transverse projection entries; no actual-probe or torus integration",
        word_counts=word_counts, insertion_word_count=len(insertions),
        frozen_force=serial(frozen), displacement_and_insertion=serial(D),
        after_ibp_exterior_derivative=serial(J), after_ibp_slope=serial(S),
        actual_failure_count=len(failures), required_failure_count=0,
        failures=failures,
        coefficient_convention="Includes L149 factor twelve and all three colors once; projection symmetry is exact, but gradient-projection identities beyond cubic covariance are not used.",
        color_pair_weights={"noncrossing": "9/4", "crossing": "-3/4"},
        exact_matrix_checks=checks,
        six_scalar_projection={name: serial(rows) for name, rows in groups.items()},
        six_scalar_green={name: serial(green_coefficients(rows)) for name, rows in groups.items()},
        six_scalar_reduced={name: dict(constant=str(v[0]), x=str(v[1]), y=str(v[2]),
                                      G000=str(v[3])) for name, v in reduced.items()},
        reduced_target_table_passed=reduced == expected_reduced,
        six_scalar_reconstruction=dict(actual_rows=[len(clean(J)), len(clean(S))],
                                       reconstructed_rows=[len(clean(predicted_J)), len(clean(predicted_S))],
                                       passed=clean(predicted_J) == clean(J) and clean(predicted_S) == clean(S)),
        bounds={"required_zero_limit": "Lambda_3=Lambda_6=0",
                "actual_proved_bound": "Not evaluated; L152 finite real limits retained"},
    )
    path = Path(__file__).with_name("quartic-residual-joint-contraction-certificate.json")
    path.write_text(json.dumps(certificate, indent=2) + "\n")
    print(f"Exact force trace words: {sum(row[3] for row in word_counts)}; insertion words: {len(insertions)}.")
    print(f"Frozen rows: {len(clean(frozen))}; IBP derivative rows: {len(clean(J))}; IBP slope rows: {len(clean(S))}.")
    print(f"Failures: actual={len(failures)}, required=0; {failures}.")
    print("Actual/required bound: finite limits known / both limits zero sought; values unevaluated.")
    print(f"Certificate: {path.relative_to(Path.cwd())}")
    assert not failures


if __name__ == "__main__":
    main()
