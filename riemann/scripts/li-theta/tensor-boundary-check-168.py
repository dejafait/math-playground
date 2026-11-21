#!/usr/bin/env python3
"""Exact n=2,3 tensor/face and compensated-ray checks for L967.

Only fractions and polynomial arithmetic are used. Analytic convergence,
the ray limit, and its restricted implication are proved in L967.
"""

from fractions import Fraction as F
from itertools import permutations, product
from math import comb, factorial
from pathlib import Path
import json


def add(*polys):
    out = {}
    for poly in polys:
        for key, value in poly.items():
            out[key] = out.get(key, F(0)) + value
            if not out[key]:
                del out[key]
    return out


def scale(poly, value):
    return {key: coefficient * value for key, coefficient in poly.items()
            if coefficient * value}


def mul(left, right):
    out = {}
    for x, a in left.items():
        for y, b in right.items():
            key = tuple(u + v for u, v in zip(x, y))
            out[key] = out.get(key, F(0)) + a * b
    return {key: value for key, value in out.items() if value}


def monomial(exponents, coefficient=F(1)):
    return {tuple(exponents): F(coefficient)} if coefficient else {}


def mp(index=None, coefficient=F(1)):
    # Moments: a0,a1,a2,c0,c1.
    exponents = [0] * 5
    if index is not None:
        exponents[index] = 1
    return monomial(exponents, coefficient)


def ep(rate=F(0), degree=0, kappa=0, coefficient=F(1)):
    # Exponential polynomial: coefficient*kappa^kappa*t^degree*exp(rate*t).
    return monomial((F(rate), degree, kappa), coefficient)


def derivative(poly):
    out = {}
    for (rate, degree, kp), coefficient in poly.items():
        out = add(out, ep(rate, degree, kp, coefficient * rate))
        if degree:
            out = add(out, ep(rate, degree - 1, kp, coefficient * degree))
    return out


def at_zero(poly):
    out = {}
    for (_, degree, kp), coefficient in poly.items():
        if degree == 0:
            out = add(out, ep(kappa=kp, coefficient=coefficient))
    return out


def H(q, r):
    # Closed forms for partial_x^r cosh(sqrt(x)*t), x=q^2.
    if r == 0:
        return add(ep(q, coefficient=F(1, 2)), ep(-q, coefficient=F(1, 2)))
    if r == 1:
        return add(ep(q, 1, coefficient=1/(4*q)),
                   ep(-q, 1, coefficient=-1/(4*q)))
    if r == 2:
        return add(ep(q, 2, coefficient=1/(8*q*q)),
                   ep(q, 1, coefficient=-1/(8*q**3)),
                   ep(-q, 2, coefficient=1/(8*q*q)),
                   ep(-q, 1, coefficient=1/(8*q**3)))
    if r == 3:
        return add(ep(q, 3, coefficient=1/(16*q**3)),
                   ep(q, 2, coefficient=-3/(16*q**4)),
                   ep(q, 1, coefficient=3/(16*q**5)),
                   ep(-q, 3, coefficient=-1/(16*q**3)),
                   ep(-q, 2, coefficient=-3/(16*q**4)),
                   ep(-q, 1, coefficient=-3/(16*q**5)))
    raise ValueError(r)


def coefficients(n):
    h, b = F(64 * 9**n), F(1, 4)
    delta = h - b
    p = (n - 1)//2
    v = [F(comb(n, 2*i+1), 4**i) for i in range(p+1)]
    w = [sum((v[i]*v[s-i] for i in range(p+1)
              if 0 <= s-i <= p), F(0)) for s in range(2*p+1)]
    D = [sum((w[s]*comb(n-1-s, r)*b**(n-1-s-r)
              for s in range(min(2*p, n-1-r)+1)), F(0)) for r in range(n)]
    d = [F(0)] + [h*sum((D[r]/delta**(n-k-r+1)
                          for r in range(n-k+1)), F(0)) for k in range(1,n+1)]
    expected = ([F(0), 4*h*h/delta**2, h/delta] if n == 2 else
                [F(0), h*(3*delta+1)**2/delta**3,
                 h*(6*delta+1)/delta**2, h/delta])
    return h, delta, D, d, expected


def partitions(k):
    for counts in product(range(k+1), repeat=k):
        if sum((i+1)*count for i,count in enumerate(counts)) == k:
            yield counts


def bell_tensor(n, d):
    terms = []
    for k in range(1,n+1):
        for counts in partitions(k):
            ell = sum(counts)
            denom = 1
            for r, count in enumerate(counts, 1):
                denom *= factorial(count)*factorial(r)**count
            coefficient = (-1)**(ell-1)*k*d[k]*F(factorial(ell-1), denom)
            factors = [('b', 0)]*(n-ell)
            for r, count in enumerate(counts, 1):
                factors += [('b', r)]*count
            terms.append((coefficient, tuple(sorted(factors)) + (('h',0),)))
    terms.append((-d[1], (('b',0),)*n + (('h',1),)))
    return terms


def stated_tensor(n, d):
    if n == 2:
        specifications = [(d[1],(1,0),0), (d[2],(2,0),0),
                          (-d[2],(1,1),0), (-d[1],(0,0),1)]
    else:
        specifications = [(d[1],(1,0,0),0), (d[2],(2,0,0),0),
                          (-d[2],(1,1,0),0), (d[3]/2,(3,0,0),0),
                          (-3*d[3]/2,(2,1,0),0), (d[3],(1,1,1),0),
                          (-d[1],(0,0,0),1)]
    return [(coefficient, tuple(sorted(('b',r) for r in orders))+(('h',hr),))
            for coefficient,orders,hr in specifications]


def term_map(terms):
    return {factors: coefficient for coefficient,factors in terms}


def transfer_factor(factor, live, delta):
    tag, r = factor
    if not live:
        return mp(coefficient=F(1,2)) if r == 0 else {}
    if tag == 'b':
        return mp(r-1, 2*r) if r else {}
    if r == 0:
        return mp(3, 2*delta)
    if r == 1:
        return add(mp(3, 2), mp(4, 2*delta))
    raise ValueError(factor)


def tensor_faces(terms, n, delta):
    m = n+1
    faces = {}
    for mask in product((0,1), repeat=m):
        poly = {}
        for coefficient, factors in terms:
            # Repeated permutations are intentional: Sym is the 1/m! average.
            for perm in permutations(factors):
                term = mp(coefficient=coefficient/F(factorial(m)))
                for factor, live in zip(perm, mask):
                    term = mul(term, transfer_factor(factor,live,delta))
                poly = add(poly,term)
        faces[mask] = poly
    strata = {dimension: {} for dimension in range(m+1)}
    for mask,poly in faces.items():
        strata[sum(mask)] = add(strata[sum(mask)],poly)
    return faces,strata


def stated_strata(n, delta, d):
    a0,a1,a2,c0,c1 = [mp(i) for i in range(5)]
    if n == 2:
        return {
            0: {},
            1: add(scale(a0,d[1]/2), scale(a1,d[2]),
                   scale(c0,-d[1]/2), scale(c1,-d[1]*delta/2)),
            2: add(scale(mul(c0,a0),2*delta*d[1]),
                   scale(mul(c0,a1),4*delta*d[2]),
                   scale(mul(a0,a0),-2*d[2])),
            3: scale(mul(c0,mul(a0,a0)),-8*delta*d[2]),
        }
    return {
        0: {},
        1: add(scale(a0,d[1]/4),scale(a1,d[2]/2),scale(a2,3*d[3]/8),
               scale(c0,-d[1]/4),scale(c1,-d[1]*delta/4)),
        2: add(scale(mul(c0,a0),delta*d[1]),
               scale(mul(c0,a1),2*delta*d[2]),
               scale(mul(c0,a2),3*delta*d[3]/2),
               scale(mul(a0,a0),-d[2]),scale(mul(a0,a1),-3*d[3])),
        3: add(scale(mul(c0,mul(a0,a0)),-4*delta*d[2]),
               scale(mul(c0,mul(a0,a1)),-12*delta*d[3]),
               scale(mul(a0,mul(a0,a0)),4*d[3])),
        4: scale(mul(c0,mul(a0,mul(a0,a0))),16*delta*d[3]),
    }


def compensated_factor(factor,q,delta):
    tag,r = factor
    if tag == 'b':
        return mul(ep(kappa=1),H(F(1,2),0)) if r == 0 else scale(H(F(1,2),r-1),2*r)
    if r == 0:
        return add(mul(ep(kappa=1),H(F(1,2),0)),scale(H(q,0),2*delta))
    return add(scale(H(q,0),2),scale(H(q,1),2*delta))


def compensated_ray(terms,n,q,delta):
    result = {}
    for coefficient,factors in terms:
        for perm in permutations(factors):
            term = ep(coefficient=coefficient/F(factorial(n+1)))
            for index,factor in enumerate(perm):
                value = compensated_factor(factor,q,delta)
                term = mul(term,value if index == 0 else at_zero(value))
            result = add(result,term)
    return result


def serialize(poly):
    return [{"exponents": [str(x) for x in key],"coefficient": str(value)}
            for key,value in sorted(poly.items())]


def check(n):
    h,delta,D,d,expected_d = coefficients(n)
    q = F(8*3**n)
    failures = []
    if d != expected_d:
        failures.append('L966 coefficient mismatch')
    terms = bell_tensor(n,d)
    if term_map(terms) != term_map(stated_tensor(n,d)):
        failures.append('complete Bell tensor mismatch')
    faces,strata = tensor_faces(terms,n,delta)
    expected_strata = stated_strata(n,delta,d)
    residuals = {dim: add(strata[dim],scale(expected_strata[dim],-1)) for dim in strata}
    if any(residuals.values()):
        failures.append('stratum table mismatch')
    unequal_faces = [list(mask) for mask,poly in faces.items()
                     if poly != scale(strata[sum(mask)],F(1,comb(n+1,sum(mask))))]
    if unequal_faces:
        failures.append('symmetry-equivalent faces differ')
    derivative_checks = []
    for rate,orders in [(F(1,2),range(n+1)),(q,range(2))]:
        for r in orders:
            actual = add(scale(derivative(derivative(H(rate,r))),2),scale(H(rate,r),F(-1,2)))
            expected = scale(H(rate,r),2*(rate*rate-F(1,4)))
            if r:
                expected = add(expected,scale(H(rate,r-1),2*r))
            diff = add(actual,scale(expected,-1))
            origin = add(at_zero(H(rate,r)),scale(ep(),-int(r == 0)))
            normal = at_zero(derivative(H(rate,r)))
            if diff or origin or normal:
                failures.append(f'differential/boundary check q={rate},r={r}')
            derivative_checks.append({"q":str(rate),"r":r,"operator_residual":serialize(diff),
                                      "origin_value_residual":serialize(origin),
                                      "origin_normal_derivative":serialize(normal)})
    ray = compensated_ray(terms,n,q,delta)
    leading = {key:value for key,value in ray.items() if key[0] == q and key[1] >= 1}
    expected_leading = ep(q,1,n,-d[1]*delta/(2*q*(n+1)))
    ray_residual = add(leading,scale(expected_leading,-1))
    other_rates = sorted({key[0] for key in ray if key[0] != q})
    if ray_residual or max(other_rates,default=F(0)) >= q:
        failures.append('dominant compensated-ray coefficient mismatch')
    return {
        "n":n,"h":str(h),"delta":str(delta),"sqrt_h":str(q),
        "D":[str(x) for x in D],"d":[str(x) for x in d[1:]],
        "coefficient_residuals":[str(x-y) for x,y in zip(d[1:],expected_d[1:])],
        "raw_tensor":[{"coefficient":str(c),"factors":f} for c,f in terms],
        "bell_tensor_matches":term_map(terms) == term_map(stated_tensor(n,d)),
        "all_faces":[{"live_coordinates":[i+1 for i,x in enumerate(mask) if x],
                      "integrated_polynomial":serialize(poly)} for mask,poly in faces.items()],
        "stratum_checks":[{"dimension":dim,"summed_face_polynomial":serialize(strata[dim]),
                           "residual":serialize(residuals[dim])} for dim in strata],
        "unequal_symmetry_faces":unequal_faces,
        "derivative_checks":derivative_checks,
        "ray_check":{
            "variables":"exponents=(exponential_rate,t_degree,kappa_power); kappa>0",
            "full_ray_exponential_polynomial":serialize(ray),
            "dominant_coefficient_of_t_exp_sqrt_h_t":serialize(leading),
            "expected_dominant_coefficient":serialize(expected_leading),
            "dominant_residual":serialize(ray_residual),
            "other_exponential_rates":[str(x) for x in other_rates],
            "required_dominant_sign":"strictly negative for every kappa>0",
            "actual_dominant_sign":"strictly negative for every kappa>0"
        },
        "failures":failures,
    }


def main():
    cases = [check(n) for n in (2,3)]
    failures = [f"n={case['n']}: {message}" for case in cases for message in case['failures']]
    summary = {
        "cases":[2,3],"tensor_strata_including_interiors_and_intersections":sum(len(c['all_faces']) for c in cases),
        "max_exact_residual":"0" if not failures else "see failures",
        "required_residual":"0",
        "actual_ray_limit_sign":"negative at both orders for every kappa>0",
        "required_sign_for_pointwise_payment":"nonnegative everywhere",
        "failures":failures,
        "scope":"Refutes only this boundary-spreading pointwise rule; integrated L966(16) remains open.",
    }
    output = Path(__file__).with_suffix('.json')
    output.write_text(json.dumps({"summary":summary,"cases":cases},indent=2)+'\n')
    print(json.dumps(summary,sort_keys=True))
    print(f"Full certificate: {output.relative_to(Path.cwd())}")
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
