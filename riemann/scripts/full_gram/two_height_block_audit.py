#!/usr/bin/env python3
"""Independent Hermite-alternant audit of L636's complete finite certificate.

No notebook calculation module is imported. Exact arithmetic in Q[i,E,E^-1]
keeps E=exp(i) formal until rigorous trigonometric interval evaluation.
The analytic, growing-dimension argument is audited in the canonical lemma.
"""
from fractions import Fraction as F
from itertools import permutations, product
from math import factorial
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent
SOURCE = HERE / 'two_height_block_certificate.json'
OUT = HERE / 'two_height_block_audit_certificate.json'


def add(*polys):
    out = {}
    for poly in polys:
        for key, val in poly.items():
            out[key] = out.get(key, F(0)) + val
    return {key: val for key, val in out.items() if val}


def atom(value=1, e=0, i=0):
    value = F(value) * (-1 if i % 4 >= 2 else 1)
    return {(e, i % 2): value} if value else {}


def mul(a, b):
    out = {}
    for (e, i), x in a.items():
        for (f, j), y in b.items():
            key = (e + f, (i + j) % 2)
            out[key] = out.get(key, F(0)) + x*y*(-1 if i+j == 2 else 1)
    return {key: val for key, val in out.items() if val}


def scale(poly, scalar):
    return mul(poly, atom(scalar))


PERMS = [(p, (-1)**sum(p[i] > p[j] for i in range(4) for j in range(i+1, 4)))
         for p in permutations(range(4))]


def det(rows):
    terms = []
    for perm, sign in PERMS:
        term = atom(sign)
        for i, j in enumerate(perm):
            term = mul(term, rows[i][j])
        terms.append(term)
    return add(*terms)


def wedge(a, b):
    # (x-y)m_ab(x,y) as a sum of x^r y^s-x^s y^r.
    return [(a+1, b, 1)] if a == b else [(a+1, b, 1), (a, b+1, -1)]


def zero_row(powers, order):
    # Taylor coefficients of (e^(ix)x^r,e^(ix)x^s,x^u,x^v) at zero.
    return [atom(F(1, factorial(order-r)), i=order-r) if order >= r else {}
            for r in powers[:2]] + [atom(int(order == r)) for r in powers[2:]]


def point_row(powers, point, derivative=False):
    out = []
    for column, r in enumerate(powers):
        value = atom(point**r, e=point if column < 2 else 0)
        if derivative:
            polynomial_part = atom(r*point**(r-1), e=point if column < 2 else 0) if r else {}
            value = add(polynomial_part, mul(value, atom(i=1))) if column < 2 else polynomial_part
        out.append(value)
    return out


def hermite_weight(nu, diagonal):
    result = {}
    for r, s, left_sign in wedge(*nu[:2]):
        for u, v, right_sign in wedge(*nu[2:]):
            powers = (r, s, u, v)
            z = [zero_row(powers, j) for j in range(4)]
            last = [point_row(powers, 1),
                    point_row(powers, 1, True) if diagonal else point_row(powers, -1)]
            combination = add(det([z[0], z[3], *last]),
                              scale(det([z[1], z[2], *last]), -1),
                              scale(det([z[0], z[1], *last]), 2))
            scalar = (-1 if diagonal else F(1, 2))*left_sign*right_sign*(-1)**sum(nu[2:])
            phase = atom(scalar, e=-1 if diagonal else 0, i=sum(nu))
            result = add(result, mul(combination, phase))
    real, imag = [F(0)]*3, [F(0)]*3
    for (e, i), value in result.items():
        assert e in (-1, 0, 1), (nu, e)
        if e == 0:
            (imag if i else real)[0] += value
        elif i == 0:
            real[1] += value
            imag[2] += e*value
        else:
            imag[1] += value
            real[2] -= e*value
    return real, imag


def alternating_interval(sine, terms):
    partial = sum((F((-1)**j, factorial(2*j+int(sine))) for j in range(terms)), F(0))
    next_partial = partial + F((-1)**terms, factorial(2*terms+int(sine)))
    return min(partial, next_partial), max(partial, next_partial)


def interval_eval(coeff, cos, sin):
    lower = upper = coeff[0]
    for factor, interval in zip(coeff[1:], [cos, sin]):
        values = [factor*x for x in interval]
        lower += min(values)
        upper += max(values)
    return lower, upper


def convolve(a, b, degree):
    return [sum((a[j]*b[k-j] for j in range(k+1)), F(0)) for k in range(degree+1)]


def strings(value):
    if isinstance(value, F):
        return str(value)
    if isinstance(value, dict):
        return {key: strings(val) for key, val in value.items()}
    if isinstance(value, (tuple, list)):
        return [strings(val) for val in value]
    return value


def main():
    old = json.loads(SOURCE.read_text())
    failures, rows = [], []
    expected = {nu for nu in product(range(9), repeat=4)
                if sum(nu) <= 8 and nu[0] >= nu[1] and nu[2] >= nu[3]}
    lookup = {tuple(row['nu']): row for row in old['rows']}
    if len(lookup) != len(old['rows']) or set(lookup) != expected:
        failures.append('complete_orbit_set')
    cos, sin = alternating_interval(False, 20), alternating_interval(True, 20)
    if list(map(F, old['trig']['cos'])) != list(cos) or list(map(F, old['trig']['sin'])) != list(sin):
        failures.append('trig_intervals')
    maxima = [F(0)]*9
    independent = {}
    for nu in sorted(expected):
        dr, di = hermite_weight(nu, True)
        cr, ci = hermite_weight(nu, False)
        orbit = (1 if nu[0] == nu[1] else 2)*(1 if nu[2] == nu[3] else 2)
        even = interval_eval([a+b for a,b in zip(dr,cr)], cos, sin)
        odd = interval_eval([a-b for a,b in zip(dr,cr)], cos, sin)
        mixed = interval_eval(di, cos, sin)
        ee, oo, mm = max(map(abs, even))*100/orbit, max(map(abs, odd))*3000/orbit, max(map(abs, mixed))*550/orbit
        bound = max(ee, oo)+mm
        row = {'nu':nu, 'orbit':orbit, 'diagonal_real':dr, 'diagonal_imag':di,
               'cross_real':cr, 'even_bound':ee, 'odd_bound':oo, 'mixed_bound':mm, 'bound':bound}
        rows.append(row)
        independent[nu] = dr, di, cr
        if any(ci):
            failures.append(f'cross_not_real:{nu}')
        if strings(row) != lookup.get(nu):
            failures.append(f'full_row_mismatch:{nu}')
        maxima[sum(nu)] = max(maxima[sum(nu)], bound)
    for nu, (dr,di,cr) in independent.items():
        if independent[nu[2:]+nu[:2]] != (dr, [-x for x in di], cr):
            failures.append(f'pair_exchange:{nu}')
    dr,di,cr = independent[(0,0,0,0)]
    eigen_even = interval_eval([a+b for a,b in zip(dr,cr)], cos,sin)
    eigen_odd = interval_eval([a-b for a,b in zip(dr,cr)], cos,sin)
    reference_ok = (dr == [F(13,6),F(-4),F(0)] and cr == [F(-4),F(3),F(17,6)]
                    and eigen_even[0] > F(1,100) and eigen_odd[0] > F(1,3000)
                    and F(1,550)**2 < F(1,100)*F(1,3000))
    if not reference_ok:
        failures.append('reference')
    for key, value in [('diagonal',dr),('cross',cr),('even_interval',eigen_even),('odd_interval',eigen_odd)]:
        if strings(value) != old['reference'][key]:
            failures.append('reference_field:'+key)
    rounded = [F(-(-x.numerator*1000//x.denominator),1000) for x in maxima]
    if strings(rounded) != old['rounded_degree_bounds']:
        failures.append('degree_bounds')
    # Independent truncated exponential via its powers, not the source recurrence.
    degree = 24
    exponent = [F(0)]+[F(4,factorial(k))+(2 if k == 1 else 0) for k in range(1,degree+1)]
    term = [F(1)]+[F(0)]*degree
    majorant = term.copy()
    for order in range(1,degree+1):
        term = [x/order for x in convolve(term, exponent, degree)]
        majorant = [a+b for a,b in zip(majorant,term)]
    if strings(majorant) != old['majorant']:
        failures.append('all_majorant_coefficients')
    costs = [rounded[k]*majorant[k]/100**k for k in range(1,9)]
    low = sum(costs,F(0))
    tail_series = sum((majorant[k]*F(3,200)**k for k in range(9,25)),F(0))+19683*F(3,200)**25
    tail = 2*420*6*256*6*3000*tail_series
    total = low+tail
    budget = {'low_degree_costs':costs,'low_total':low,'tail_series':tail_series,'tail_cost':tail,'total':total,'required':F(1)}
    if strings(budget) != old['budget']:
        failures.append('complete_budget')
    if total >= F(7,16):
        failures.append('seven_sixteenths_threshold')
    if sum(row['orbit'] for row in rows) != 495:
        failures.append('495_indices')
    # These are arithmetic checks of the stated analytic error exponents only.
    transfer = {'source_exponent':F(3,4)+F(1,100)+F(11,400)-1,
                'relative_source_exponent':-F(17,80)+F(1,20),
                'relative_curvature_exponent':-F(199,100)+F(1,20),
                'radial_SM':F(21,400),'radial_exponent_limit':F(63,10),
                'total_reserve':F(9,20)+F(1,20)}
    if transfer['source_exponent'] != -F(17,80) or transfer['relative_source_exponent'] != -F(13,80) or transfer['relative_curvature_exponent'] != -F(97,50) or transfer['radial_SM'] >= F(1,16) or transfer['total_reserve'] != F(1,2):
        failures.append('transfer_arithmetic')
    data = {'method':'Independent four-column alternant with confluent Hermite rows; complete exact certificate comparison',
            'source':SOURCE.name,'qualification':'Finite algebra only; canonical L636 Section 6 audits the analytic limits and source specialization.',
            'orbit_count':len(rows),'multi_index_count':sum(row['orbit'] for row in rows),
            'rows':rows,'reference':{'even_interval':eigen_even,'odd_interval':eigen_odd},
            'rounded_degree_bounds':rounded,'majorant':majorant,'budget':budget,'transfer_arithmetic':transfer,
            'failures':failures}
    OUT.write_text(json.dumps(strings(data),indent=2)+'\n')
    print(f'Complete Hermite reconstruction: {len(rows)} orbits, {sum(row["orbit"] for row in rows)} indices')
    print(f'Actual relative limsup bound {float(total):.12g}; required < 7/16 = 0.4375')
    print('Analytic final reserve: 9/20 + 1/20 = 1/2 (analytic justification in L636)')
    print('Failures:', failures)
    print('Certificate:', OUT.relative_to(HERE.parents[1]))
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
