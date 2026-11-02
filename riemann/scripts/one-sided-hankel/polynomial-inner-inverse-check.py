#!/usr/bin/env python3
"""Exact n=15 test of the inner-factor polynomial inverse; no asymptotic claim."""
from fractions import Fraction as F
from pathlib import Path
import json


def multiply(a, b, length):
    c = [F(0)] * length
    for i, x in enumerate(a[:length]):
        for j, y in enumerate(b[:length-i]):
            c[i+j] += x*y
    return c


def factor_series(zero, pole, length):
    # (u-zero)/(1-pole*u)
    return [-zero] + [(1-zero*pole)*pole**(k-1) for k in range(1, length)]


def dot(a, b):
    return sum((x*y for x, y in zip(a, b)), F(0))


def complex_multiply(a, b):
    return (a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0])


def evaluate(p, z):
    value = (F(0), F(0))
    for c in reversed(p):
        value = complex_multiply(value, z)
        value = (value[0]+c, value[1])
    return value


def encode(value):
    if isinstance(value, F):
        return str(value)
    if isinstance(value, dict):
        return {k: encode(v) for k, v in value.items()}
    if isinstance(value, (tuple, list)):
        return [encode(v) for v in value]
    return value


def main():
    n, lam, r = 15, F(-11, 10), F(10, 11)
    J = n-1
    beta, inner, inverse_outer = [F(1)], [F(1)], [F(1)]
    for j in range(1, n):
        s = F(8*j, 11*n)
        alpha, gamma = s/lam, s*lam
        beta = multiply(beta, factor_series(s, s, n), n)
        inner = multiply(inner, factor_series(alpha, alpha, n), n)
        ratio = [F(1)] + [(alpha-gamma)*alpha**(k-1) for k in range(1, n)]
        inverse_outer = multiply(inverse_outer, ratio, n)

    def action(h):
        d = multiply(inverse_outer, h, n)
        return [F(0)] + [lam**(k-J)*beta[k]*d[J-k] for k in range(n)]

    v = inner[::-1]
    at_r = multiply(inverse_outer, [beta[k]*(-1)**k for k in range(n)], n)
    z = [r*lam**(-J)*value for value in at_r[::-1]]
    a, b, c = dot(v, v), dot(z, z), dot(v, z)
    delta = a-c*c/b
    normalized_h = [value/a for value in v]
    constrained_h = [(v[i]-c*z[i]/b)/delta for i in range(n)]
    p = action(constrained_h)
    checks = []

    def check(name, actual, relation, required):
        passed = {'=': lambda: actual == required,
                  '>': lambda: actual > required,
                  '<=': lambda: actual <= required}[relation]()
        checks.append(dict(name=name, actual=actual, relation=relation,
                           required=required, passed=passed))

    for i in range(n):
        h = [F(int(i == j)) for j in range(n)]
        coeff = action(h)
        check(f'anchor vector coefficient {i}', evaluate(coeff, (F(1), F(0)))[0], '=', v[i])
        check(f'zero vector coefficient {i}', evaluate(coeff, (r, F(0)))[0], '=', z[i])
    check('anchor energy lower bound', a, '>', F(1, n))
    check('independent value constraints', delta, '>', F(0))
    check('normalized construction norm squared', dot(normalized_h, normalized_h), '=', 1/a)
    check('normalized construction polynomial norm bound', 1/a, '<=', F(n))
    check('constrained norm identity', dot(constrained_h, constrained_h), '=', 1/delta)
    check('P(0)', p[0], '=', F(0))
    check('P(1)', evaluate(p, (F(1), F(0)))[0], '=', F(1))
    check('P(10/11)', evaluate(p, (r, F(0)))[0], '=', F(0))

    # Every row is an exact rational evaluation, not a continuum certificate.
    samples = []
    for k in range(19):
        y = F(k, 40)
        t = 4*y/5
        w = (1/(1+t*t), t/(1+t*t))
        value = evaluate(p, w)[0]
        samples.append(dict(y=y, real_part=value, nonnegative=value >= 0))
    check('negative witness lower enclosure', samples[4]['real_part'], '>', F(-17, 500))
    check('negative witness upper enclosure', samples[4]['real_part'], '<=', F(-33, 1000))
    failures = [row['name'] for row in checks if not row['passed']]
    negative = [row for row in samples if not row['nonnegative']]
    certificate = dict(
        result='PASS' if not failures else 'FAIL', n=n,
        scope='Exact finite construction and rational-point signs only; no uniform or continuum sign claim.',
        checks=checks, failures=failures,
        vectors=dict(anchor=v, zero=z),
        gram=dict(a=a, b=b, c=c, delta=delta),
        normalized_norm_squared=1/a, constrained_norm_squared=1/delta,
        constrained_h=constrained_h, polynomial=p, samples=samples,
        sign_constraint_failures=negative,
        required=dict(segment='|y|<=9/20', sign='nonnegative at every point',
                      asymptotic_norm='exp(n/100)*n^C with fixed C and onset'),
    )
    path = Path(__file__).with_suffix('.json')
    path.write_text(json.dumps(encode(certificate), indent=2)+'\n')
    print(f"{certificate['result']}: {len(checks)} exact algebra checks; failures={failures}")
    print(f'Norm squared: normalization only {float(1/a):.9g} <= {n}; with zero {float(1/delta):.9g}')
    print(f'Exact negative sampled points: {len(negative)}; required: no negative point on the full segment')
    if negative:
        first = negative[0]
        print(f"First negative witness y={first['y']}, Re P approximately {float(first['real_part']):.9g}; full rational stored")
    print(f'Certificate: {path.relative_to(Path.cwd())}')
    raise SystemExit(bool(failures))


if __name__ == '__main__':
    main()
