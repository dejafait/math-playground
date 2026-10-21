"""Full L170 force/vector axial row, with exact rational certificates.

All rough link directions are restored. This computes finite Laurent
identities, not a numerical heat integral or a new mesh-limit argument.
"""
from collections import defaultdict
from fractions import Fraction as Q
from functools import lru_cache
from itertools import permutations, product
from pathlib import Path
import json
from check_quartic_residual_inversion import shift, word, clovers

ZERO = (0, 0, 0, 0)
Z3 = (0, 0, 0)


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
            rec(j + 1, remaining - n, factors + ((x, mu),) * n,
                coeff * Q(sign ** n, factorial))

    rec(0, m, (), Q(1))
    return tuple((k, v) for k, v in out.items() if v)


@lru_cache(None)
def clover(z, rho, nu, m):
    out = defaultdict(Q)
    if rho == nu:
        return ()
    for w in clovers(z, rho, nu):
        for ww, sign in ((w, 1), (inverse(w), -1)):
            for factors, coeff in jet(ww, m):
                out[factors] += Q(sign, 8) * coeff
    return tuple((k, v) for k, v in out.items() if v)


@lru_cache(None)
def force(nu, m):
    out = defaultdict(Q)
    for rho in range(4):
        if rho == nu:
            continue
        low, high = sorted((rho, nu))
        for corner in (ZERO, shift(ZERO, rho, -1)):
            w = word(corner, ((low, 1), (high, 1), (low, -1), (high, -1)))
            j = next(j for j, (x, mu, _) in enumerate(w) if (x, mu) == (ZERO, nu))
            sign = w[j][2]
            start = j if sign == 1 else (j + 1) % 4
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


def force_words(nu, rho, endpoint):
    out = defaultdict(Q)
    for m in (1, 2):
        for left, a in force(nu, m):
            for right, b in generator(nu, rho, endpoint, 3 - m):
                factors = left + right
                key = min(factors[j:] + factors[:j] for j in range(3))
                out[key] += -2 * a * b
    return {k: v for k, v in out.items() if v}


def clean(p):
    return {k: v for k, v in p.items() if v}


def polyadd(a, b, scale=Q(1)):
    out = defaultdict(Q, a)
    for k, v in b.items():
        out[k] += scale * v
    return clean(out)


def polymul(a, b):
    out = defaultdict(Q)
    for k, v in a.items():
        for l, w in b.items():
            out[tuple(x + y for x, y in zip(k, l))] += v * w
    return clean(out)


def mono(j, sign=1):
    k = [0] * 3
    k[j] = sign
    return {tuple(k): Q(1)}


def average(p):
    out = defaultdict(Q)
    for perm in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            for k, v in p.items():
                l = [0] * 3
                for j in range(3):
                    l[perm[j]] = signs[j] * k[j]
                out[tuple(l)] += v / 48
    return clean(out)


def serialize(p):
    return [dict(key=k, coefficient=str(v)) for k, v in sorted(p.items()) if v]


def in_laplacian_variables(p):
    """Even Laurent polynomial in X_j=2-e_j-e_j^-1, exactly."""
    def chebyshev(j, n):
        if n == 0:
            return {Z3: Q(1)}
        x = mono(j)
        linear = polyadd({Z3: Q(2)}, x, -1)
        a, b = {Z3: Q(2)}, linear
        for _ in range(2, n + 1):
            a, b = b, polyadd(polymul(linear, b), a, -1)
        return b

    out = {}
    for k, v in p.items():
        if any(n < 0 for n in k):
            continue
        term = {Z3: v}
        for j, n in enumerate(k):
            term = polymul(term, chebyshev(j, n))
        out = polyadd(out, term)
    return out


def from_laplacian_variables(p):
    xs = [polyadd(polyadd({Z3: Q(2)}, mono(j), -1), mono(j, -1), -1)
          for j in range(3)]
    out = {}
    for k, v in p.items():
        term = {Z3: v}
        for j, n in enumerate(k):
            for _ in range(n):
                term = polymul(term, xs[j])
        out = polyadd(out, term)
    return out


def centered_row_formula(h, mu):
    """Return raw-tail Laurent row from its compact centered formula.

    Intermediate exponents use half-angle z_j; after removing the output
    center phase, all exponents are even and give integer tail phases.
    """
    one = {Z3: Q(1)}
    zp, zm = [mono(j) for j in range(3)], [mono(j, -1) for j in range(3)]
    eta = [polyadd(zp[j], zm[j]) for j in range(3)]
    difference = [polyadd(zp[j], zm[j], -1) for j in range(3)]
    xs = [polyadd(polyadd({Z3: Q(2)}, polymul(zp[j], zp[j]), -1),
                  polymul(zm[j], zm[j]), -1) for j in range(3)]
    if h == mu:
        row = {}
        for b in range(3):
            if b != mu:
                row = polyadd(row, polymul(xs[b], polyadd(xs[b], xs[mu], -3)))
        row = polyadd({}, polymul(eta[h], row), Q(1, 48))
    else:
        # d_h d_mu=-(z_h-z_h^-1)(z_mu-z_mu^-1).
        row = polymul(polymul(eta[h], difference[h]), difference[mu])
        row = polyadd({}, polymul(row, polyadd(xs[h], xs[mu], Q(-1, 2))), Q(-1, 12))
    row = polymul(row, zm[mu])
    assert all(all(n % 2 == 0 for n in k) for k in row)
    return {tuple(n // 2 for n in k): v for k, v in row.items()}


def independent_word_checks(words):
    """Direct SU(2) exponential-series convolution on full colored packets."""
    zero, one = (Q(0),) * 4, (Q(1), Q(0), Q(0), Q(0))
    def plus(a, b):
        return tuple(x + y for x, y in zip(a, b))
    def scale(a, s):
        return tuple(s * x for x in a)
    def mul(a, b):
        cross = (a[2]*b[3]-a[3]*b[2], a[3]*b[1]-a[1]*b[3], a[1]*b[2]-a[2]*b[1])
        return (a[0]*b[0]-sum(a[j]*b[j] for j in (1, 2, 3))/4,
                *(a[0]*b[j]+b[0]*a[j]-cross[j-1]/2 for j in (1, 2, 3)))
    def total(values):
        out = zero
        for value in values:
            out = plus(out, value)
        return out
    def conv(a, b):
        return [total(mul(a[j], b[m-j]) for j in range(m+1)) for m in range(4)]
    records = []
    for seed in (1, 2):
        def packet(edge):
            x, mu = edge
            return (Q(0), *(Q((seed*(c+2)*(mu+1)+sum((j+c+seed)*x[j] for j in range(4))) % 7-3)
                            for c in range(3)))
        @lru_cache(None)
        def exponential(edge, sign):
            out = [one]
            for m in range(1, 4):
                out.append(scale(mul(out[-1], packet(edge)), Q(sign, m)))
            return out
        @lru_cache(None)
        def loop(w):
            out = [one, zero, zero, zero]
            for x, mu, sign in w:
                out = conv(out, exponential((x, mu), sign))
            return out
        def cseries(z, rho, nu):
            out = [zero] * 4
            for w in clovers(z, rho, nu):
                left, right = loop(w), loop(inverse(w))
                out = [plus(out[m], scale(plus(left[m], scale(right[m], -1)), Q(1, 8)))
                       for m in range(4)]
            return out
        for (nu, rho, endpoint), local in words.items():
            g = [zero] * 4
            for b in range(4):
                if b == nu:
                    continue
                low, high = sorted((b, nu))
                for corner in (ZERO, shift(ZERO, b, -1)):
                    w = word(corner, ((low, 1), (high, 1), (low, -1), (high, -1)))
                    j = next(j for j, (x, mu, _) in enumerate(w) if (x, mu) == (ZERO, nu))
                    sign = w[j][2]
                    start = j if sign == 1 else (j+1) % 4
                    w = w[start:]+w[:start]
                    left, right = loop(w), loop(inverse(w))
                    g = [plus(g[m], scale(plus(left[m], scale(right[m], -1)), Q(sign, 2)))
                         for m in range(4)]
            z = ZERO if endpoint == 0 else shift(ZERO, nu)
            xseries = cseries(z, rho, nu)
            if endpoint:
                xseries = conv(conv(exponential((ZERO, nu), 1), xseries), exponential((ZERO, nu), -1))
            xseries = [scale(v, Q(1, 2)) for v in xseries]
            direct = -4*sum(mul(g[m], xseries[3-m])[0] for m in (1, 2))
            expanded = Q(0)
            for factors, coeff in local.items():
                value = one
                for edge in factors:
                    value = mul(value, packet(edge))
                expanded += 2*coeff*value[0]
            records.append(dict(key=[seed, nu, rho, endpoint], direct=str(direct),
                                expanded=str(expanded), error=str(direct-expanded)))
    return records


def main():
    rows = defaultdict(Q)
    word_counts = []
    words = {}
    for nu, rho, endpoint in product(range(4), range(4), range(2)):
        if nu == rho:
            continue
        local = force_words(nu, rho, endpoint)
        words[nu, rho, endpoint] = local
        word_counts.append([nu, rho, endpoint, len(local)])
        for factors, coefficient in local.items():
            for ext, axial, other in permutations(range(3)):
                h = factors[ext][1]
                if h == 0 or factors[axial][1] != 0:
                    continue
                colors = [None] * 3
                colors[ext], colors[axial], colors[other] = 0, 1, 2
                eps = (-1) ** sum(colors[i] > colors[j]
                                  for i in range(3) for j in range(i + 1, 3))
                x, _ = factors[axial]
                y, mu = factors[other]
                delta = tuple(y[j] - x[j] for j in range(4))
                rows[rho, h, mu, delta] += coefficient * Q(eps, 24)
    rows = clean(rows)
    centered_full = defaultdict(lambda: defaultdict(Q))
    for (rho, h, mu, delta), value in rows.items():
        doubled = [2*n for n in delta]
        doubled[mu] += 1
        doubled[0] -= 1
        centered_full[rho, h, mu][tuple(doubled)] += value
    parity_checks = []
    for key, values in sorted(centered_full.items()):
        values = clean(values)
        reversed_values = {tuple(-n for n in k): v for k, v in values.items()}
        parity_checks.append(dict(key=key, even=values == reversed_values,
                                  origin_value=str(sum(values.values()))))

    # theta_1=0. Raw positive-tail phases are kept throughout.
    axial_zero = defaultdict(lambda: defaultdict(Q))
    for (rho, h, mu, delta), value in rows.items():
        axial_zero[rho, h, mu][delta[1:]] += value
    axial_zero = {k: clean(v) for k, v in axial_zero.items()}
    one = {Z3: Q(1)}
    ds = [polyadd(mono(j), one, -1) for j in range(3)]
    dstar = [polyadd(mono(j, -1), one, -1) for j in range(3)]
    lam = {Z3: Q(6)}
    for j in range(3):
        lam = polyadd(polyadd(lam, mono(j), -1), mono(j, -1), -1)
    contractions = {}
    averaged = {}
    for rho, h, j in product(range(4), range(1, 4), range(1, 4)):
        numerator = {}
        for mu in range(1, 4):
            proj = polyadd(lam if mu == j else {}, polymul(ds[mu - 1], dstar[j - 1]), -1)
            numerator = polyadd(numerator, polymul(axial_zero.get((rho, h, mu), {}), proj))
        numerator = polymul(numerator, polyadd(one, mono(j - 1)))
        contractions[rho, h, j] = numerator
        averaged[rho, h, j] = average(numerator)
    target = averaged[0, 1, 1]
    failures = []
    failures.extend(f"full axial parity/origin {r['key']}" for r in parity_checks
                    if not r['even'] or r['origin_value'] != '0')
    formula_checks = []
    for rho, h, mu in product(range(4), range(1, 4), range(4)):
        actual = axial_zero.get((rho, h, mu), {})
        required = centered_row_formula(h-1, mu-1) if rho == 0 and mu else {}
        passed = actual == required
        formula_checks.append(dict(key=[rho, h, mu], passed=passed))
        if not passed:
            failures.append(f'complete centered row {rho,h,mu}')
    word_checks = independent_word_checks(words)
    failures.extend(f"direct word convolution {r['key']}" for r in word_checks if r['error'] != '0')
    for (rho, h, j), actual in averaged.items():
        required = target if rho == 0 and h == j else {}
        if actual != required:
            failures.append(f"scalar physical reduction {rho,h,j}")
    laplacian_numerator = in_laplacian_variables(target)
    if from_laplacian_variables(laplacian_numerator) != target:
        failures.append('complete Laplacian-variable reconstruction')
    xs = [mono(j) for j in range(3)]
    power = lambda p, n: ({Z3: Q(1)} if n == 0 else polymul(p, power(p, n-1)))
    sums = [polyadd(polyadd(power(xs[0], n), power(xs[1], n)), power(xs[2], n))
            for n in range(1, 5)]
    l, s2, s3, s4 = sums
    compact = polyadd({}, polymul(l, polyadd(polyadd({}, s2, 5), power(l, 2), -3)), Q(1, 36))
    quartic = polyadd(polyadd({}, polymul(l, s3), 3), power(s2, 2))
    quartic = polyadd(quartic, s4, -4)
    quartic = polyadd(quartic, polymul(l, polymul(polymul(xs[0], xs[1]), xs[2])), 4)
    compact = polyadd(compact, quartic, Q(1, 144))
    if compact != laplacian_numerator:
        failures.append('compact symmetric numerator identity')

    path = Path(__file__).with_name('third-trace-frozen-contraction-certificate.json')
    certificate = dict(
        scope='Exact finite full-link cubic force/vector row and projected Laurent contraction only. L170 limit imported; torus integration and actual heat values not certified here.',
        normalization='Tr(t_0 t_1 t_2)=1/4; third derivative/6; fixed exterior color; M axial color 1, other color 2; J_0[1,2]=1. Axial rough slots retained.',
        word_counts=word_counts, independent_word_checks=word_checks, centered_row_checks=formula_checks,
        full_axial_parity_origin_checks=parity_checks,
        full_axial_row=serialize(rows),
        axial_zero_row=[dict(key=k, polynomial=serialize(p)) for k, p in sorted(axial_zero.items())],
        projected_numerators=[dict(key=k, polynomial=serialize(p), averaged=serialize(averaged[k])) for k, p in sorted(contractions.items())],
        scalar_numerator=serialize(target), laplacian_numerator=serialize(laplacian_numerator), failures=failures,
        compact_numerator_identity_passed=compact == laplacian_numerator,
        actual_failure_count=len(failures), required_failure_count=0,
        bounds=dict(required='Complete response has zero cubic limit', actual='Full residual axial row extracted; scalar identity check only; mixed limits unresolved'))
    path.write_text(json.dumps(certificate, indent=2) + '\n')
    print(f'Full cubic words: {sum(w[3] for w in word_counts)}; axial row coefficients: {len(rows)}.')
    print(f'Averaged scalar numerator coefficients: {len(target)}.')
    print(f'Full centered-row comparisons: {len(formula_checks)}; independent full-color word comparisons: {len(word_checks)}.')
    print(f'Laplacian numerator terms: {len(laplacian_numerator)} (full coefficients saved).')
    print(f'Failures: actual={len(failures)}, required=0; {failures}.')
    print('Actual/required: finite tensor extraction / complete zero cubic limit; latter unresolved.')
    print(f'Certificate: {path.relative_to(Path.cwd())}')
    assert not failures


if __name__ == '__main__':
    main()
