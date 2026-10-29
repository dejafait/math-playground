"""Bounded exact branch-form test for L110. Run from the notebook root.

Operations count public polynomial operations, not internal integer steps.
The persistent ledger charges repeated executions cumulatively. No backend.
"""
from fractions import Fraction as Q
from math import comb, gcd, isqrt
from pathlib import Path
import hashlib
import json

BASE = Path(__file__).resolve().parent
ROOT = BASE.parent.parent
CERT = BASE / 'involution-eligibility-certificate.json'
LEDGER = BASE / 'involution-eligibility-ledger.json'
CAPS = dict(divisor_trials=10000, work=200000, degree=64, bits=4096)
ledger = json.loads(LEDGER.read_text()) if LEDGER.exists() else dict(
    caps=CAPS, used=dict(divisor_trials=0, work=0), runs=[])
assert ledger['caps'] == CAPS
run = dict(status='IN_PROGRESS', start=ledger['used'].copy())
ledger['runs'].append(run)
cert = dict(status='IN_PROGRESS', failures=[])
max_degree = 0
max_bits = 0


def save():
    LEDGER.write_text(json.dumps(ledger, indent=2) + '\n')


def charge(kind='work', n=1):
    if ledger['used'][kind] + n > CAPS[kind]:
        raise RuntimeError('CAP_STOP: ' + kind)
    ledger['used'][kind] += n


def poly(values):
    global max_degree, max_bits
    p = [Q(v) for v in values]
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    if not p:
        p = [Q(0)]
    degree = len(p) - 1
    bits = max(max(abs(v.numerator).bit_length(), v.denominator.bit_length()) for v in p)
    if degree > CAPS['degree'] or bits > CAPS['bits']:
        raise RuntimeError('CAP_STOP: polynomial size')
    max_degree = max(max_degree, degree)
    max_bits = max(max_bits, bits)
    return p


def add(p, q):
    charge()
    return poly([(p[i] if i < len(p) else 0) + (q[i] if i < len(q) else 0)
                 for i in range(max(len(p), len(q)))])


def scale(p, c):
    charge()
    return poly([v*c for v in p])


def sub(p, q):
    return add(p, scale(q, -1))


def mul(p, q):
    charge()
    out = [Q(0)]*(len(p)+len(q)-1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i+j] += a*b
    return poly(out)


def divrem(p, q):
    charge()
    assert q != [0]
    r = p[:]
    out = [Q(0)]*max(1, len(p)-len(q)+1)
    while r != [0] and len(r) >= len(q):
        d = len(r)-len(q)
        a = r[-1]/q[-1]
        out[d] += a
        r = sub(r, poly([0]*d + scale(q, a)))
    return poly(out), poly(r)


def xgcd(p, q):
    a, b, c, d = poly([1]), poly([0]), poly([0]), poly([1])
    while q != [0]:
        v, r = divrem(p, q)
        p, q = q, r
        a, b = b, sub(a, mul(v, b))
        c, d = d, sub(c, mul(v, d))
    k = 1/p[-1]
    return scale(p, k), scale(a, k), scale(c, k)


def evaluate(p, x):
    charge()
    r = Q(0)
    for a in reversed(p):
        r = r*x+a
        poly([r])  # Enforce the rational size cap on every Horner value.
    return r


def checked(name, condition):
    charge()  # Coefficient/matrix/check row.
    cert.setdefault('checks', []).append(dict(name=name, ok=bool(condition)))
    if not condition:
        cert['failures'].append(name)
        raise AssertionError(name)


def divisors(n):
    assert n > 0
    if ledger['used']['divisor_trials'] + isqrt(n) > CAPS['divisor_trials']:
        raise RuntimeError('CAP_STOP: divisor preflight')
    out, trials = set(), []
    for d in range(1, isqrt(n)+1):
        charge('divisor_trials')
        r = n % d
        charge()  # Processed divisor certificate row.
        trials.append([d, r])
        if r == 0:
            out.update([d, n//d])
    return sorted(out), dict(integer=n, trials=trials, divisors=sorted(out))


def rational_roots(p):
    # Clear denominators and remove content for the full rational-root theorem.
    charge()
    common = 1
    for a in p:
        common = common*a.denominator//gcd(common, a.denominator)
    ints = [int(a*common) for a in p]
    content = 0
    for a in ints:
        content = gcd(content, abs(a))
    ints = [a//content for a in ints]
    checked('root_polynomial_nonzero_constant', ints[0] != 0)
    numerators, ncert = divisors(abs(ints[0]))
    denominators, dcert = divisors(abs(ints[-1]))
    rows, roots = [], set()
    for n in numerators:
        for d in denominators:
            for sign in [-1, 1]:
                charge()  # Raw candidate inspection, including nonreduced cases.
                if gcd(n, d) != 1:
                    continue
                x = Q(sign*n, d)
                value = evaluate(poly(ints), x)
                charge()  # Complete reduced candidate row.
                rows.append(dict(candidate=x, residual=value))
                if value == 0:
                    roots.add(x)
    return sorted(roots), dict(primitive_coefficients=ints,
        numerator_divisors=ncert, denominator_divisors=dcert,
        candidates=rows, roots=sorted(roots))


def serial(value):
    # Charge each serialized certificate node, including all coefficient rows.
    charge()
    if isinstance(value, Q):
        return str(value)
    if isinstance(value, dict):
        return {str(k): serial(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [serial(v) for v in value]
    return value


save()
try:
    f = [-308, -2288, 341, 3388, 1034, -704, -275]
    q4 = poly([7, 52, -6, -64, -25])
    checked('exact_twist_and_factorization',
            scale(mul(poly([-4, 0, 1]), q4), 11) == poly(f))
    roots, cert['quartic_rational_root_certificate'] = rational_roots(q4)
    checked('quartic_no_rational_root', roots == [])
    # F(rX-4Z,X-rZ), in ascending powers X^j Z^(6-j).
    g = [poly([0]) for _ in range(7)]
    for i, fi in enumerate(f):
        for p in range(i+1):
            for q in range(7-i):
                exponent = p+6-i-q
                coefficient = fi*comb(i, p)*(-4)**(i-p)*comb(6-i, q)*(-1)**(6-i-q)
                g[p+q] = add(g[p+q], poly([0]*exponent+[coefficient]))
    equations = [sub(scale(g[j], f[0]), scale(g[0], f[j])) for j in range(1, 7)]
    # Iterated extended gcd, retaining a full Bezout certificate for all six.
    h = equations[0]
    weights = [poly([1])]
    for e in equations[1:]:
        h, u, v = xgcd(h, e)
        weights = [mul(u, w) for w in weights]+[v]
    sum_bezout = poly([0])
    quotients = []
    for e, w in zip(equations, weights):
        sum_bezout = add(sum_bezout, mul(e, w))
        quotient, remainder = divrem(e, h)
        checked('equation_divisible_by_gcd', remainder == [0])
        quotients.append(quotient)
    checked('full_bezout_identity', sum_bezout == h)
    groots, rootcert = rational_roots(h)
    cert['affine_chart'] = dict(matrix=[['r', '-4'], ['1', '-r']],
        transformed_sextic_coefficients=g, proportionality_equations=equations,
        monic_gcd=h, bezout_coefficients=weights, exact_quotients=quotients,
        rational_root_certificate=rootcert)
    survivors = []
    exceptions = []
    for r in groots:
        k = r*r-4
        charge()  # Determinant/matrix check.
        values = [evaluate(v, r) for v in g]
        lam = values[0]/f[0]
        checked('root_full_sextic_identity', values == [lam*a for a in f])
        row = dict(r=r, square_matrix_scalar=k, determinant=-k,
                   sextic_multiplier=lam, full_coefficients=values)
        if k == 0:
            exceptions.append(row)
        else:
            # Retain actual twist and require both a rational lift and order two.
            square = lam >= 0 and isqrt(lam.numerator)**2 == lam.numerator \
                and isqrt(lam.denominator)**2 == lam.denominator
            lift = Q(isqrt(lam.numerator), isqrt(lam.denominator)) if square else None
            row.update(rational_lift=lift, order_two=bool(square and lam == k**3))
            survivors.append(row)
    # c=0 gives [1,0;0,-1]. Full sextic coefficients are f_j*(-1)^(6-j).
    infinity_values = [a*(-1)**(6-j) for j, a in enumerate(f)]
    charge()  # Matrix/coefficient check.
    infinity_multiplier = Q(infinity_values[0], f[0])
    infinity_residual = [a-infinity_multiplier*b for a, b in zip(infinity_values, f)]
    checked('projective_infinity_chart_fails', any(infinity_residual))
    cert['projective_infinity_chart'] = dict(matrix=[[1, 0], [0, -1]],
        full_coefficients=infinity_values, forced_multiplier=infinity_multiplier,
        proportionality_residual=infinity_residual)
    cert['singular_exceptions'] = exceptions
    cert['nonsingular_survivors'] = survivors
    checked('affine_only_singular_roots', survivors == [])
    cert['source_hashes'] = {name: hashlib.sha256((ROOT/name).read_bytes()).hexdigest()
        for name in ['lemmas/L110-explicit-pair-genus-two-model.md',
                     'drafts/literature/2026-10-25-pair-genus-two-involution-eligibility.md']}
    cert['coefficient_order'] = 'ascending parameter degree; binary coefficient j means X^j Z^(6-j)'
    cert['status'] = 'COMPLETE_NO_EXTRA_Q_INVOLUTION'
    cert['bounds'] = dict(caps=CAPS, max_degree=max_degree, max_bits=max_bits,
                          accounting='Public polynomial operations, candidate tests, matrix/check and certificate nodes; not internal elementary arithmetic.')
    output = serial(cert)
    CERT.write_text(json.dumps(output, indent=2)+'\n')
    run.update(status=cert['status'], end=ledger['used'].copy(),
               max_degree=max_degree, max_bits=max_bits, failures=cert['failures'])
except Exception as exc:
    run.update(status='INCOMPLETE', error=str(exc), end=ledger['used'].copy())
    cert.update(status='INCOMPLETE', error=str(exc))
    # Emergency serialization preserves evidence without further mathematics.
    CERT.write_text(json.dumps(cert, default=str, indent=2)+'\n')
    raise
finally:
    save()

print('Result:', cert['status'])
print('Quartic rational roots:', len(roots), '; coefficient gcd:', [str(v) for v in h])
print('Nonsingular affine survivors:', len(survivors), '; infinity chart: fails')
print('Cumulative actual/required bounds:', ledger['used'], '/', CAPS)
print('Maximum degree/bits:', max_degree, max_bits, '; failures:', cert['failures'])
print('Certificate:', CERT.relative_to(ROOT), '; ledger:', LEDGER.relative_to(ROOT))
