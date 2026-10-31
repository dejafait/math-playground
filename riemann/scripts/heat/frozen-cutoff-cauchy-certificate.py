#!/usr/bin/env python3
"""Exact rational/Taylor checks for L494; no floating input or ledger imports."""
from fractions import Fraction as F
from decimal import Decimal, localcontext, ROUND_CEILING
from pathlib import Path
import json

D = 10**50
NTERMS = 180
evaluations = []
checks = []


def floor_grid(q):
    return F((q.numerator * D) // q.denominator, D)


def ceil_grid(q):
    return -floor_grid(-q)


def rat(q):
    return {"numerator": str(q.numerator), "denominator": str(q.denominator)}


def exp_interval(q):
    """Enclose exp(q) with a positive Taylor sum and a geometric tail.

    Each term is rounded outward on the rational 10^-50 grid. If a=abs(q),
    the tail after term n is <= upper_term_n*a/(n+1)/(1-a/(n+2)).
    Negative arguments use reciprocal endpoints, also rounded outward.
    """
    a = abs(q)
    assert a < NTERMS + 2
    term_lo = term_hi = F(1)
    sum_lo = sum_hi = F(1)
    for k in range(1, NTERMS + 1):
        term_lo = floor_grid(term_lo * a / k)
        term_hi = ceil_grid(term_hi * a / k)
        sum_lo += term_lo
        sum_hi += term_hi
    tail_hi = term_hi * a / (NTERMS + 1) / (1 - a / (NTERMS + 2))
    lo, hi = sum_lo, ceil_grid(sum_hi + tail_hi)
    if q < 0:
        lo, hi = floor_grid(1 / hi), ceil_grid(1 / lo)
    evaluations.append({
        "argument": rat(q), "terms_through": NTERMS,
        "positive_sum_lower": rat(sum_lo), "positive_sum_upper": rat(sum_hi),
        "last_term_lower": rat(term_lo), "last_term_upper": rat(term_hi),
        "tail_upper": rat(tail_hi), "lower": rat(lo), "upper": rat(hi),
    })
    return lo, hi


def check(name, actual, required):
    passed = actual < required
    checks.append({"name": name, "actual_upper": rat(actual),
                   "required_strict_upper": rat(required), "passed": passed})


def display(q):
    with localcontext() as ctx:
        ctx.prec = 19
        ctx.rounding = ROUND_CEILING
        return str(Decimal(q.numerator) / Decimal(q.denominator))


r, t0, t1 = F('.14142'), F('.16836'), F('.1718')
X, x0 = F(6 * 10**12), F('6000284561421.5')
l, U = F('26.89'), F('5.17') / t0 + F('1e-12')
pi_hi = F(22, 7)  # Classical Archimedean bounds 3 < pi < 22/7.
delta = F('1e-12')
emin = X / (4 * pi_hi)
check('disk real-part lower bound', X + r, x0)
check('log displacement', r / X, delta)
check('L lower bound: exp(l) < X/(4*pi_hi)', exp_interval(l)[1], emin)
check('local cutoff lower bound', F(690000)**2, emin)
check('local cutoff upper bound', exp_interval(U)[1] + t1 / 16, F(4700000)**2)
check('log(4700000) < 15.37', F(4700000), exp_interval(F('15.37'))[0])
check('local log-cutoff displacement', t1 / (32 * emin), delta)
check('source real-part correction', t1 / X**2, F('1e-24'))
check('saddle floor', F('1.6318') + F('1e-24'), F(1, 2) + t0 * l / 4)
chi_correction = delta / 2 + t1 * (U / 2 + delta) / (2 * (X - 6))
check('second chirality exponent correction', chi_correction, delta)
check('second chirality exponent nonpositive', F('.02') - l / 4 + delta, F(0))

a = F('1.6318') - F('5.17') / 8 - delta
sum_upper = 1 + (exp_interval((1-a) * F('15.37'))[1] - 1) / (1-a)
check('primitive coefficient sum', sum_upper, F(20))
d0 = ((F('5.17') + delta)**2 / 16 + F('.626')) / (X - F('6.66'))
ab = 40 * d0 / (1-d0)
check('Gaussian error upper', ab, F('1.6e-11'))
check('C-error y derivative negative', F('1.24') * 6 / (F(690000)-F('.125')), l/4)
check('sqrt(L^2+pi^2/4) < U+1', U**2 + pi_hi**2/4, (U+1)**2)
carg = -l/4-t0*l*l/16+F('2.48')/(F(690000)-F('.125'))+(3*(U+1)+F('10.44'))/(X-12)
ec = exp_interval(carg)[1]
check('C-error upper', ec, F('5.972e-7'))
check('E_global upper', ec + ab, F('6e-7'))

c = 3/X+(1+r)**2/(4*X**2)
d = (t1*U/4+F('3.21'))/(X-6)
A = U/2+d
check('prefactor real-part constant', c*(X-6)+t1*pi_hi/8+t1*c/2, F('3.21'))
g = exp_interval(r*A)[1]
check('reflection G', g, F('8.770232'))
eta = (t1/16+2*r/12)/emin
check('entering log-index displacement', eta/(2*(1-eta)), delta)
pair_correction = delta/2+t1*delta**2/4+t1*c*(U/2+delta)/2
check('real entering-pair exponent correction', pair_correction, F('1e-10'))
p = 2*exp_interval(-l/4-t0*l*l/16+F('1e-10'))[1]
check('unmollified real entering pair P', p, F('1.3e-6'))
growth = U/4+delta/2+d+t1*(U/2+delta)/(4*(X-6))
check('each chirality vertical logarithmic growth', growth, A)
derivative = F('1.9e-6') * F('8.770232') / r
check('Cauchy derivative upper', derivative, F('1.18e-4'))

out = Path(__file__).with_name('frozen-cutoff-cauchy-certificate.json')
certificate = {
    "result": "PASS" if all(c['passed'] for c in checks) else "FAIL",
    "method": "Exact Fraction arithmetic; outward rational Taylor terms and geometric exponential tail; classical 3 < pi < 22/7.",
    "scope": "L494 scalar reductions only; imported Polymath Theorem 1.3 and analytic argument must be checked separately; no coefficient ledger or collision exclusion.",
    "parameters": {k: rat(v) for k,v in dict(r=r,t0=t0,t1=t1,X=X,x0=x0,l=l,U=U,a=a,c=c,d=d,A=A).items()},
    "checks": checks, "exponential_evaluations": evaluations,
    "failures": [c['name'] for c in checks if not c['passed']],
}
out.write_text(json.dumps(certificate, indent=2) + '\n')
for item in checks:
    upper = F(int(item['actual_upper']['numerator']), int(item['actual_upper']['denominator']))
    required = F(int(item['required_strict_upper']['numerator']), int(item['required_strict_upper']['denominator']))
    print(f"{'PASS' if item['passed'] else 'FAIL'} {item['name']}: actual upper {display(upper)}; required < {display(required)}")
print(f"{certificate['result']}: {len(checks)} checks; failures={certificate['failures']}; certificate={out}")
raise SystemExit(0 if certificate['result'] == 'PASS' else 1)
