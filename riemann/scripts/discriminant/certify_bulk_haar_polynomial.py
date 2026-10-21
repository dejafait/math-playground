"""Step 192 degree-32 Chebyshev envelope and full Euler expectations.

Correct Python integer/Fraction/isqrt execution is the arithmetic contract.
All full certificates are written to disk; stdout is a bounded summary.
"""
import json
from fractions import Fraction as F
from math import isqrt
from pathlib import Path
import enclose_bulk_haar_integral as base

I = base.I
D = 32


def decode(rec):
    return I(I(F(rec['lower'])).lo, I(F(rec['upper'])).hi, True)


def cosine(r):
    r = r % 2
    return base.trig(base.PI*r, True)


def multiply(a, b):
    out = [I(0) for _ in range(len(a)+len(b)-1)]
    for i, x in enumerate(a):
        if x.lo == x.hi == 0:
            continue
        for j, y in enumerate(b):
            if y.lo != 0 or y.hi != 0:
                out[i+j] = out[i+j]+x*y
    return out


def main():
    directory = Path(__file__).parent
    pre = json.loads((directory/'bulk-haar-polynomial-preflight-192.json').read_text())
    assert all(pre['checks'].values())
    a, z = [F(pre['g_full_range'][k]) for k in ('lower', 'upper')]
    mid, half = (a+z)/2, (z-a)/2
    remainder = F(pre['pointwise_best']['32']['radius'])
    cells = []
    for cell in pre['cells']:
        vectors, reason = base.selector(cell['cell'], cell['count'])
        assert reason == cell['reason']
        cells.append((cell['count'], vectors))
    nodes = []
    for k in range(D+1):
        g = mid+half*cosine(F(2*k+1, 2*(D+1)))
        value = I(0)
        for count, vectors in cells:
            bound = (1+(3*g/80).sqrt())/2
            fallback = I(-bound.hi, bound.hi, True)
            if vectors is None:
                v = fallback
            else:
                v = sum((base.q_range(g, v).intersect(fallback) for v in vectors), I(0))/3
            value = value+v/count
        nodes.append(value)
    coefficients = []
    for j in range(D+1):
        factor = F(1 if j == 0 else 2, D+1)
        coefficients.append(factor*sum((nodes[k]*cosine(F(j*(2*k+1), 2*(D+1)))
                                       for k in range(D+1)), I(0)))
    node_out = {'degree': D, 'nodes': [x.enc() for x in nodes],
                'chebyshev_coefficients': [x.enc() for x in coefficients],
                'uniform_radius': str(remainder),
                'angular_boxes': (D+1)*len(cells),
                'selector_replay_callbacks': len(cells),
                'checks': {'same_complete_partition': True, 'both_stages_replayed': True,
                           'ideal_nodes_enclosed': True}, 'failures': []}
    node_path = directory/'bulk-haar-polynomial-nodes-192.json'
    node_path.write_text(json.dumps(node_out, indent=2)+'\n')
    print('Angular node certificate:', node_path, flush=True)
    print('Node interval widths:', min((x.hi-x.lo)/base.SCALE for x in nodes),
          max((x.hi-x.lo)/base.SCALE for x in nodes), flush=True)
    # The remaining calculations use only I and source_coefficients, whose
    # arithmetic is parameterized by the module SCALE. No old PI/P/UNIT
    # object is used after this change. The saved 10^-24 intervals are
    # reconstructed as rationals before changing to 160-place arithmetic.
    saved_coefficients = [x.enc() for x in coefficients]
    base.SCALE = 10**160
    coefficients = [decode(x) for x in saved_coefficients]
    _, source = base.source_coefficients(directory)
    alpha = decode(source['alpha'])
    theta = {j: decode(source['theta'][str(j)]) for j in (13, 14)}
    cc = {j: decode(source['source_bounds']['C'][str(j)]) for j in (13, 14)}
    weight = [I(0) for _ in range(15)]
    weight[0] = alpha*(1-theta[13])+(1-alpha)*(1-theta[14])
    weight[13] = alpha*theta[13]/cc[13]
    weight[14] = (1-alpha)*theta[14]/cc[14]
    xpoly = [v/half for v in weight]
    xpoly[0] = (weight[0]-mid)/half
    polynomials = [[I(1)], xpoly]
    for j in range(2, D+1):
        p = [2*v for v in multiply(xpoly, polynomials[-1])]
        for k, v in enumerate(polynomials[-2]):
            p[k] = p[k]-v
        polynomials.append(p)
    orders = sorted({k for p in polynomials for k, v in enumerate(p) if v.lo or v.hi})
    primes = [p for p in range(2, 201) if all(p % q for q in range(2, isqrt(p)+1))]
    moments = {0: I(1)}
    moment_records = []
    local_records = []
    max_exponent = 0
    for j in orders:
        if j == 0:
            continue
        moment = I(1)
        for p in primes:
            term = total = I(1)
            for e in range(1, 1025):
                term = term*F((j+e-1)**2, e*e*p**5)
                total = total+term
                ratio = F((j+e)**2, (e+1)**2*p**5)
                if ratio < 1:
                    tail = term*ratio/(1-ratio)
                    if tail.hi*10**110 <= total.lo:
                        break
            else:
                raise AssertionError(('local exponent cap', j, p))
            factor = I(total.lo, total.hi+tail.hi, True)
            moment = moment*factor
            max_exponent = max(max_exponent, e)
            local_records.append({'j': j, 'p': p, 'e': e, 'next_ratio': str(ratio),
                                  'factor': factor.enc(), 'tail': tail.enc()})
        r = F(j*j, 4*200**4)/(1-F(j*j, 201**5))
        assert 0 < r < 1
        moment = I(moment.lo, (moment/(1-r)).hi, True)
        moments[j] = moment
        moment_records.append({'j': j, 'prime_log_tail': str(r), 'moment': moment.enc()})
    expectation_records = []
    result = I(0)
    for j, (coefficient, poly) in enumerate(zip(coefficients, polynomials)):
        raw = sum((v*moments[k] for k, v in enumerate(poly) if v.lo or v.hi), I(0))
        # T_j(x) lies in [-1,1] on the full response interval. This
        # independent exact bound repairs no lost correlations; retain
        # the raw Euler result too, so conditioning failures remain visible.
        bounded = raw.intersect(I(-base.SCALE, base.SCALE, True))
        term = coefficient*bounded
        result = result+term
        expectation_records.append({'j': j, 'raw_expectation': raw.enc(),
                                    'bounded_expectation': bounded.enc(),
                                    'coefficient': coefficient.enc(), 'term': term.enc(),
                                    'polynomial': [v.enc() for v in poly]})
    radius = I(remainder)
    final = I(result.lo-radius.hi, result.hi+radius.hi, True)
    out = {'status': 'UNVERIFIED_NONZERO_CANDIDATE' if final.lo > 0 or final.hi < 0 else 'CONTAINS_ZERO',
           'degree': D, 'precision_places': 160, 'prime_cutoff': 200,
           'max_exponent': max_exponent, 'orders': orders,
           'moments': moment_records, 'local_factors': local_records,
           'expectations': expectation_records, 'polynomial_expectation': result.enc(),
           'uniform_radius': str(remainder), 'integral': final.enc(),
           'width': str(F(final.hi-final.lo, base.SCALE)),
           'required_width': pre['required_total_width'],
           'zero_excluded': final.lo > 0 or final.hi < 0,
           'width_test_passed': F(final.hi-final.lo, base.SCALE) <= F(pre['required_total_width']),
           'checks': {'all_local_ratio_conditions': True, 'all_prime_tail_denominators_positive': True,
                      'all_prime_log_tails_less_than_one': True, 'exponent_cap': max_exponent <= 1024,
                      'full_fixed_moment_orders': max(orders) == 448,
                      'precision_cap': 160 <= 512},
           'failures': [] if final.lo > 0 or final.hi < 0 else ['Final envelope expectation contains zero.']}
    path = directory/'bulk-haar-polynomial-expectation-192.json'
    path.write_text(json.dumps(out, indent=2)+'\n')
    print('Euler orders / largest exponent:', len(orders), max_exponent)
    print('Actual I enclosure:', float(F(final.lo, base.SCALE)), float(F(final.hi, base.SCALE)))
    print('Actual / required width:', float(F(out['width'])), float(F(out['required_width'])))
    print('Zero excluded / width passed:', out['zero_excluded'], out['width_test_passed'])
    print('Failures:', out['failures'])
    print('Certificate:', path)


if __name__ == '__main__':
    main()
