"""Exact polynomial IBP test for L171; full rational certificate on disk."""
import json
from fractions import Fraction as F
from pathlib import Path

ZERO = (0, 0, 0)


def add(*ps):
    out = {}
    for p in ps:
        for m, c in p.items():
            out[m] = out.get(m, F(0)) + c
    return {m: c for m, c in out.items() if c}


def scale(p, c):
    return {m: c*v for m, v in p.items() if c*v}


def mul(p, q):
    out = {}
    for a, c in p.items():
        for b, d in q.items():
            m = tuple(x+y for x, y in zip(a, b))
            out[m] = out.get(m, F(0)) + c*d
    return {m: c for m, c in out.items() if c}


def power(p, n):
    out = {ZERO: F(1)}
    for _ in range(n):
        out = mul(out, p)
    return out


def deriv(p, j):
    out = {}
    for m, c in p.items():
        if m[j]:
            a = list(m)
            a[j] -= 1
            out[tuple(a)] = c*m[j]
    return out


def data(p):
    return [[list(m), str(c)] for m, c in sorted(p.items())]


def main():
    one = {ZERO: F(1)}
    xs = [{tuple(int(k == j) for k in range(3)): F(1)} for j in range(3)]
    lam = add(*xs)
    s2, s3, s4 = [add(*(power(x, n) for x in xs)) for n in (2, 3, 4)]
    e2 = add(*(mul(xs[j], xs[k]) for j in range(3) for k in range(j+1, 3)))
    prod = mul(mul(xs[0], xs[1]), xs[2])
    required = add(scale(mul(lam, add(scale(s2, 5), scale(power(lam, 2), -3))), F(1, 2)),
                   scale(add(scale(mul(lam, s3), 3), power(s2, 2), scale(s4, -4),
                             scale(mul(lam, prod), 4)), F(1, 8)))
    gn = scale(add(*(mul(mul(xs[j], xs[k]), power(add(xs[j], scale(xs[k], -1)), 2))
                     for j in range(3) for k in range(j+1, 3))), F(-1, 12))
    names = ['1', 'lambda', 'S2', 'e2', 'g_G']
    columns = [mul(power(lam, 2), q) for q in (one, lam, s2, e2)] + [gn]
    moments = [F(1), F(6), F(18), F(12)]
    ps = [[] for _ in range(7)]
    for j, x in enumerate(xs):
        other = [xs[k] for k in range(3) if k != j]
        ysum = add(*other)
        bases = [one, x, ysum, power(x, 2), mul(x, ysum),
                 add(*(power(y, 2) for y in other)), mul(*other)]
        for p, basis in zip(ps, bases):
            p.append(basis)
    for name, pvec in zip(('1', 'Xj', 'sum_other', 'Xj2', 'Xj_sum_other',
                           'S2_other', 'product_other'), ps):
        terms = []
        for j, (x, p) in enumerate(zip(xs, pvec)):
            terms.append(add(mul(mul(add(scale(one, 2), scale(x, -1)), p), lam),
                             mul(mul(x, add(scale(one, 4), scale(x, -1))),
                                 add(mul(lam, deriv(p, j)), scale(p, -1)))))
        names.append('IBP_'+name)
        columns.append(add(*terms))
    mons = sorted(set(required).union(*(set(c) for c in columns)))
    matrix = [[c.get(m, F(0)) for c in columns]+[required.get(m, F(0))] for m in mons]
    r = 0
    pivots = []
    for c in range(len(columns)):
        pivot = next((i for i in range(r, len(matrix)) if matrix[i][c]), None)
        if pivot is None:
            continue
        matrix[r], matrix[pivot] = matrix[pivot], matrix[r]
        v = matrix[r][c]
        matrix[r] = [x/v for x in matrix[r]]
        for i in range(len(matrix)):
            if i != r and matrix[i][c]:
                v = matrix[i][c]
                matrix[i] = [x-v*y for x, y in zip(matrix[i], matrix[r])]
        pivots.append(c)
        r += 1
    failures = []
    if any(not any(row[:-1]) and row[-1] for row in matrix):
        failures.append('no identity in the tested polynomial span')
        coeffs = None
        actual = {}
        constant = None
    else:
        coeffs = [F(0)]*len(columns)
        for i, c in enumerate(pivots):
            coeffs[c] = matrix[i][-1]
        actual = add(*(scale(c, a) for c, a in zip(columns, coeffs)))
        constant = sum((a*m for a, m in zip(coeffs[:4], moments)), F(0))
    residual = add(actual, scale(required, -1))
    if coeffs is not None and residual:
        failures.append('nonzero polynomial residual')
    # Independently construct the compact identity used in the proof.
    # D/lambda^2 = sum_j d/dtheta_j (2 sin(theta_j) S2/lambda).
    divergence = add(mul(add(scale(lam, 10), scale(power(lam, 2), -1)), s2),
                     scale(mul(lam, s3), -2), power(s2, 2))
    compact_actual = add(mul(power(lam, 2), add(scale(s2, F(1, 2)),
                                               scale(lam, F(-3, 2)))),
                         scale(gn, F(-9, 2)), scale(divergence, F(1, 4)))
    compact_residual = add(compact_actual, scale(required, -1))
    if compact_residual:
        failures.append('compact IBP identity residual')
    # Exact constant Fourier coefficient of X^m=(2-e-e^-1)^m.
    def moment(n):
        p = {0: F(1)}
        for _ in range(n):
            out = {}
            for k, c in p.items():
                for shift, a in ((0, 2), (1, -1), (-1, -1)):
                    out[k+shift] = out.get(k+shift, F(0))+c*a
            p = out
        return p[0]
    x_moments = [moment(n) for n in range(3)]
    if x_moments != [F(1), F(2), F(6)] or F(3, 2)*x_moments[2]-F(9, 2)*x_moments[1]:
        failures.append('polynomial mean not zero')
    scalar_interval = (F(387, 2000), F(549, 2000))
    imported_g = (F(-61, 1000), F(-43, 1000))
    if tuple(sorted(F(-9, 2)*v for v in imported_g)) != scalar_interval:
        failures.append('scalar endpoint mismatch')
    physical_bounds = {3: (F('1228.1260684'), F('1228.1260686')),
                       6: (F('451.5469823'), F('451.5469825'))}
    imported_r = {3: (F('-74.916'), F('-52.809')),
                  6: (F('-27.545'), F('-19.416'))}
    expected_z = {3: (F('237.6405'), F('337.122')),
                  6: (F('87.372'), F('123.9525'))}
    expected_ee = {3: (F('316.854'), F('449.496')),
                   6: (F('116.496'), F('165.27'))}
    results = []
    for i, r_bounds in imported_r.items():
        z_bounds = tuple(sorted(F(-9, 2)*v for v in r_bounds))
        ee_bounds = tuple(sorted(-6*v for v in r_bounds))
        b_products = [a*b for a in scalar_interval for b in physical_bounds[i]]
        # Both independent imported enclosures imply the declared endpoints.
        if z_bounds != expected_z[i] or ee_bounds != expected_ee[i]:
            failures.append(f'probe-{i}-endpoint mismatch')
        if not z_bounds[0] < min(b_products) <= max(b_products) < z_bounds[1]:
            failures.append(f'probe-{i}-physical product containment')
        if not z_bounds[0] > 0 or not ee_bounds[0] > 0:
            failures.append(f'probe-{i}-zero not excluded')
        results.append(dict(probe=i, imported_R=list(map(str, r_bounds)),
                            imported_B=list(map(str, physical_bounds[i])),
                            direct_B_products=list(map(str, b_products)),
                            third_trace=list(map(str, z_bounds)),
                            EE=list(map(str, ee_bounds))))
    cert = dict(required=data(required), columns=[dict(name=n, polynomial=data(c))
                for n, c in zip(names, columns)], row_monomials=[list(m) for m in mons],
                rref=[[str(x) for x in row] for row in matrix], pivots=pivots,
                coefficients=None if coeffs is None else dict(zip(names, map(str, coeffs))),
                actual=data(actual), residual=data(residual),
                polynomial_moments=list(map(str, moments)),
                resulting_constant=None if constant is None else str(constant),
                resulting_g_coefficient=None if coeffs is None else str(coeffs[4]),
                compact_identity=dict(divergence_numerator=data(divergence),
                                      actual=data(compact_actual), residual=data(compact_residual)),
                exact_X_moments=list(map(str, x_moments)),
                imported_g=list(map(str, imported_g)),
                scalar_interval=list(map(str, scalar_interval)), results=results,
                failures=failures, qualification='Exact algebra only; IBP regularity justified in canonical proof.')
    path = Path(__file__).with_name('third-trace-scalar-ibp-certificate.json')
    path.write_text(json.dumps(cert, separators=(',', ':'))+'\n')
    print('Exact numerator comparison; monomials', len(mons), 'rank', r,
          'constant', constant, 'g coefficient', None if coeffs is None else coeffs[4],
          'failures', failures, 'path', path)
    if coeffs is not None:
        print('Identity coefficients', cert['coefficients'])
    print('z_Z required positive; exact interval', cert['scalar_interval'])
    for result in results:
        print('Probe', result['probe'], 'third trace', result['third_trace'],
              'E,E', result['EE'], 'required: excludes zero')
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
