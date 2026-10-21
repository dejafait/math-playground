"""Step 196: nonnegative monomial moments only; full rational evidence."""
import json
from fractions import Fraction as F
from math import isqrt
from pathlib import Path
import enclose_bulk_haar_integral as b


def main():
    directory = Path(__file__).parent
    b.SCALE = 10**160
    I = b.I
    _, source = b.source_coefficients(directory)
    def dec(r):
        return I(I(F(r['lower'])).lo, I(F(r['upper'])).hi, True)
    alpha = dec(source['alpha'])
    theta = {j: dec(source['theta'][str(j)]) for j in (13, 14)}
    cs = {j: dec(source['source_bounds']['C'][str(j)]) for j in (13, 14)}
    weight = {0: alpha*(1-theta[13])+(1-alpha)*(1-theta[14]),
              13: alpha*theta[13]/cs[13], 14: (1-alpha)*theta[14]/cs[14]}
    assert all(v.lo > 0 for v in weight.values())
    polys, poly = [], {0: I(1)}
    for r in range(1, 9):
        out = {}
        for k, v in poly.items():
            for j, w in weight.items():
                out[k+j] = out.get(k+j, I(0))+v*w
        poly = out
        polys.append(poly)
    orders = sorted({j for poly in polys for j in poly})
    primes = [p for p in range(2, 201) if all(p % q for q in range(2, isqrt(p)+1))]
    moments, records, locals_ = {0: I(1)}, [], []
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
                raise AssertionError(('exponent cap', j, p))
            factor = I(total.lo, total.hi+tail.hi, True)
            moment = moment*factor
            locals_.append({'j': j, 'p': p, 'e': e, 'ratio': str(ratio),
                            'sum': total.enc(), 'tail': tail.enc(), 'factor': factor.enc()})
        denominator = 1-F(j*j, 201**5)
        assert denominator > 0
        tail = F(j*j, 4*200**4)/denominator
        assert 0 < tail < 1
        moments[j] = I(moment.lo, (moment/(1-tail)).hi, True)
        records.append({'j': j, 'prime_log_tail': str(tail), 'moment': moments[j].enc()})
    outputs = []
    for r, poly in enumerate(polys, 1):
        value = sum((v*moments[j] for j, v in poly.items()), I(0))
        # E G=1 exactly, by the fixed calibration; retain the raw calculation.
        used = value.intersect(I(1)) if r == 1 else value
        outputs.append({'r': r, 'polynomial': {str(j): v.enc() for j, v in poly.items()},
                        'raw_moment': value.enc(), 'moment': used.enc()})
    out = {'step': 196, 'precision_places': 160, 'source': source,
           'positive_weight': {str(j): v.enc() for j, v in weight.items()},
           'orders': orders, 'local_factors': locals_, 'C': records, 'G_moments': outputs,
           'checks': {'all_coefficients_positive': True, 'all_ratio_and_tail_conditions': True,
                      'max_order_at_most_112': max(orders) <= 112,
                      'local_exponent_cap': max(r['e'] for r in locals_) <= 1024,
                      'full_prime_tail_retained': True}, 'failures': []}
    path = directory/'bulk-core-tail-moments-196.json'
    path.write_text(json.dumps(out, indent=2)+'\n')
    print('C orders / max / local factors / max exponent:', len(orders), max(orders), len(locals_), max(r['e'] for r in locals_))
    print('E G^r enclosures:', [[r['r'], *[float(F(r['moment'][k])) for k in ('lower', 'upper')]] for r in outputs])
    print('Failures:', out['failures'])
    print('Certificate:', path)


if __name__ == '__main__':
    main()
