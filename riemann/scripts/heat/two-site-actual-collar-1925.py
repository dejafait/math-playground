"""One fixed-box interval test; stop on the first unpaid divisor.

No site/radius sweep, subdivision, nonlinear solve or moment refinement.
Uses audited1921 rational interval operations and independently collected
five-variable Cramer polynomials. Input containment is conditional L917/L037.
"""
from fractions import Fraction as F
from hashlib import sha256
from math import factorial
from pathlib import Path
import importlib.util
import json

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
OUT = Path(__file__).with_suffix('.json')


def load(name, filename):
    spec = importlib.util.spec_from_file_location(name, HERE / filename)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


arith = load('rank1921', 'two-site-theta-jacobian-1921.py')
poly = load('check1921', 'two-site-theta-jacobian-check-1921.py')
I, D = arith.I, arith.D


def record(x):
    return {'trace_id': x.id, **arith.encode(x.pair)}


def power(x, n):
    """Sharp integer power range, also for even powers crossing zero."""
    lo, hi = x.pair
    if n == 0:
        pair = F(1), F(1)
    elif n % 2:
        pair = lo**n, hi**n
    else:
        pair = (F(0) if lo <= 0 <= hi else min(lo**n, hi**n),
                max(lo**n, hi**n))
    return I(arith.outward(pair), 'integer_power', (x.id, n))


def derivative(p, variable):
    result = {}
    for exponent, coefficient in p.items():
        e = list(exponent)
        c = coefficient * e[variable]
        if c:
            e[variable] -= 1
            result[tuple(e)] = c
    return result


def evaluate(p, variables):
    # Collect exactly at point sites BEFORE interval evaluation, as in1921.
    collected = {}
    for exponent, coefficient in p.items():
        e = list(exponent)
        for j, x in enumerate(variables):
            if x.pair[0] == x.pair[1]:
                coefficient *= x.pair[0]**e[j]
                e[j] = 0
        key = tuple(e)
        collected[key] = collected.get(key, F(0)) + coefficient
    result = I.lift(0)
    for exponent, coefficient in sorted(collected.items()):
        if coefficient:
            term = I.lift(coefficient)
            for x, n in zip(variables, exponent):
                if n:
                    term = term * power(x, n)
            result = result + term
    return result


def observables(c):
    c0, c1, c2, c3 = c
    p1 = -c3
    p2 = -(c3*p1+c2.scale(2))
    p3 = -(c3*p2+c2*p1+c1.scale(3))
    p4 = -(c3*p3+c2*p2+c1*p1+c0.scale(4))
    r1, r2, r3, r4 = [p.scale(F(1, 4)) for p in (p1, p2, p3, p4)]
    V = r2-r1**2
    T = r3-(r1*r2).scale(3)+(r1**3).scale(2)
    Q = r4-(r1*r3).scale(4)+(r1**2*r2).scale(6)-(r1**4).scale(3)
    if V.v.pair[0] <= 0:
        raise ArithmeticError('variance lower bound not positive')
    sqrt_v = V.v.sqrt()
    g, k = T.v/(V.v*sqrt_v), Q.v/(V.v**2)
    A = [V.v*dx-F(3, 2)*T.v*dv for dx, dv in ((T.a, V.a), (T.b, V.b))]
    B = [V.v*dx-2*Q.v*dv for dx, dv in ((Q.a, V.a), (Q.b, V.b))]
    J = [[x/(V.v**2*sqrt_v) for x in A], [x/(V.v**3) for x in B]]
    return {'variance': V.encode(), 'third': T.encode(), 'fourth': Q.encode(),
            'g': record(g), 'k': record(k),
            'jacobian': [[record(x) for x in row] for row in J]}, (g, k), J


def main():
    source_path = HERE / 'low-time-h2-uniform-195.json'
    audit_path = HERE / 'low-time-h2-audit-197.json'
    source, audit = [json.loads(p.read_bytes()) for p in (source_path, audit_path)]
    assert audit['status'] == 'passed' and audit['failures'] == []
    hashes = {name: sha256((ROOT/name).read_bytes()).hexdigest() == expected
              for name, expected in audit['input_sha256'].items()}
    assert all(hashes.values())
    selected = {str(k): source['panels'][0]['moments'][str(k)] for k in (0, 2, 4, 6, 8)}
    assert all(value == audit['panels'][0]['moments'][k] for k, value in selected.items())
    assert arith.box(source['panels'][0]['lambda']) == (F(0), F(1, 5120))
    raw = {k: I(arith.box(value), 'input', ('/panels/0/moments/'+k,))
           for k, value in selected.items()}
    assert raw['0'].pair[0] > 0
    mu = {k: raw[str(k)]/raw['0'] for k in (2, 4, 6, 8)}
    bj = {j: mu[2*j]*F(factorial(j), factorial(2*j)) for j in range(1, 5)}
    b1, b2, b3, b4 = [bj[j] for j in range(1, 5)]
    S2 = b1**2-b2
    q2 = -6*S2
    q3 = 4*(b3-3*b1*b2+2*b1**3)
    q4 = b4-4*b1*b3+6*b1**2*b2-3*b1**4
    Vactual = -q2/2
    Tactual = -3*q3/4
    Qactual = q2**2/2-q4
    assert Vactual.pair[0] > 0
    gamma = Tactual/(Vactual*Vactual.sqrt())
    kurtosis = Qactual/(Vactual**2)
    actual = {'b': {str(j): record(x) for j, x in bj.items()},
              'centered_coefficients': [record(x) for x in (q2, q3, q4)],
              'variance': record(Vactual), 'third': record(Tactual),
              'fourth': record(Qactual), 'gamma': record(gamma),
              'k': record(kurtosis)}

    moments = []
    for j in range(8):
        base = poly.constant(1) if j == 0 else {}
        if j in (2, 4, 6):
            e = [0]*5
            e[j//2-1] = 1
            base = {tuple(e): F(1)}
        for site in (3, 4):
            e = [0]*5
            e[site] = j
            base = poly.padd(base, {tuple(e): F(1)})
        moments.append(base)
    gram = [[moments[i+j] for j in range(4)] for i in range(4)]
    expressions = {'gram_det': poly.det(gram)}
    for j in range(4):
        matrix = [row.copy() for row in gram]
        for i in range(4):
            matrix[i][j] = poly.pneg(moments[i+4])
        expressions['numerator_c'+str(j)] = poly.det(matrix)
    components = {name: {'value': p, 'da': derivative(p, 3), 'db': derivative(p, 4)}
                  for name, p in expressions.items()}

    def reference(sites):
        variables = [mu[k] for k in (2, 4, 6)] + sites
        evaluated = {name: D(*(evaluate(part[key], variables) for key in ('value', 'da', 'db')))
                     for name, part in components.items()}
        saved = {'cramer': {name: x.encode() for name, x in evaluated.items()}}
        denominator = evaluated['gram_det']
        if denominator.v.pair[0] <= 0 <= denominator.v.pair[1]:
            saved['blocked_divisor'] = record(denominator.v)
            saved['required'] = 'Gram determinant interval excludes0 (positive lower bound suffices)'
            return saved, None, None
        coeff = [evaluated['numerator_c'+str(j)].divide(denominator) for j in range(4)]
        saved['coefficients'] = [x.encode() for x in coeff]
        try:
            obs, values, J = observables(coeff)
        except ArithmeticError as exc:
            saved['blocked'] = str(exc)
            return saved, None, None
        saved.update(obs)
        return saved, values, J

    point, fpoint, Jpoint = reference([I.lift(0), I.lift(1)])
    assert fpoint is not None
    midpoint = [[sum(x.pair)/2 for x in row] for row in Jpoint]
    a, b = midpoint[0]
    c, d = midpoint[1]
    det = a*d-b*c
    assert det != 0
    Rplus = [[d/det, -b/det], [-c/det, a/det]]
    collar, fbox, Jbox = reference([I((F(-1, 4), F(1, 4)), 'box_input', ('a',)),
                                  I((F(3, 4), F(5, 4)), 'box_input', ('b',))])
    orientations = {}
    for sign in (1, -1):
        R = [[row[0]*sign, row[1]] for row in Rplus]
        result = {'R': [[str(x) for x in row] for row in R],
                  'point_residual': [record(sign*fpoint[0]-gamma), record(fpoint[1]-kurtosis)]}
        if fbox is None:
            result['status'] = 'inconclusive_unpaid_collar_divisor'
            result['krawczyk_evaluated'] = False
            result['range_exclusion_evaluated'] = False
        else:
            residual = [sign*fbox[0]-gamma, fbox[1]-kurtosis]
            J = [[x*sign for x in Jbox[0]], Jbox[1]]
            z = [sign*fpoint[0]-gamma, fpoint[1]-kurtosis]
            X = [I((F(-1, 4), F(1, 4)), 'box_input', ('X'+str(j),)) for j in range(2)]
            K = [-sum((R[i][j]*z[j] for j in range(2)), I.lift(0)) +
                 sum(((int(i == j)-sum((R[i][l]*J[l][j] for l in range(2)), I.lift(0)))*X[j]
                      for j in range(2)), I.lift(0)) for i in range(2)]
            included = all(F(-1, 4) < x.pair[0] <= x.pair[1] < F(1, 4) for x in K)
            excluded = any(not x.pair[0] <= 0 <= x.pair[1] for x in residual)
            result.update({'range': [record(x) for x in residual], 'K': [record(x) for x in K],
                           'strict_inclusion': included, 'range_exclusion': excluded,
                           'status': 'included' if included else ('excluded' if excluded else 'inconclusive'),
                           'krawczyk_evaluated': True, 'range_exclusion_evaluated': True})
        orientations[str(sign)] = result
    result = {'status': 'fixed_collar_test_completed',
              'qualification': 'Conditional L917/L037 inputs; failure of sufficient bounds is not nonexistence',
              'fixed_box': [['-1/4', '1/4'], ['3/4', '5/4']],
              'selected_inputs': selected, 'accepted_audit_hash_checks': hashes,
              'input_sha256': {str(p.relative_to(ROOT)): sha256(p.read_bytes()).hexdigest()
                               for p in (source_path, audit_path, Path(__file__),
                                         HERE/'two-site-theta-jacobian-1921.py',
                                         HERE/'two-site-theta-jacobian-check-1921.py')},
              'actual': actual,
              'polynomials': {name: {key: [{'exponents': list(e), 'coefficient': str(c)}
                                          for e, c in sorted(p.items())]
                                    for key, p in part.items()} for name, part in components.items()},
              'point': point, 'point_midpoint_det': str(det), 'collar': collar,
              'orientations': orientations, 'trace': arith.TRACE, 'divisors': arith.DIVISORS,
              'failures': [], 'required': 'strict K interior inclusion or residual range excluding0',
              'certificate': str(OUT.relative_to(ROOT))}
    OUT.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'status': {key: x['status'] for key, x in orientations.items()},
                      'actual_gamma': arith.encode(gamma.pair), 'actual_k': arith.encode(kurtosis.pair),
                      'blocked_divisor': collar.get('blocked_divisor'),
                      'required': result['required'], 'failures': [],
                      'certificate': result['certificate']}))


if __name__ == '__main__':
    main()
