"""Exact finite checks for one analytically defined polynomial family.

This is not an asymptotic or continuum positivity certificate. Complete
coefficient vectors, norms, and rational point signs are saved to disk.
"""
from fractions import Fraction as Q
from pathlib import Path
import json
import math


def encode(v):
    if isinstance(v, Q):
        return f"{v.numerator}/{v.denominator}"
    if isinstance(v, list):
        return [encode(a) for a in v]
    if isinstance(v, dict):
        return {k: encode(a) for k, a in v.items()}
    return v


def product_series(factors, degree, constant=Q(1)):
    """Taylor coefficients of constant * product (a+b*z)/(1-c*z)."""
    coeff = [constant] + [Q(0)] * degree
    for a, b, c in factors:
        out = []
        for k in range(degree + 1):
            out.append(a * coeff[k] + (b * coeff[k-1] + c * out[k-1] if k else 0))
        coeff = out
    return coeff


def dot(a, b):
    return sum((x*y for x, y in zip(a, b)), Q(0))


def real_value(coeff, wr, wi):
    ar = ai = Q(0)
    for p in reversed(coeff):
        ar, ai = ar*wr-ai*wi+p, ar*wi+ai*wr
    return ar


def log_rational(a):
    return math.log(a.numerator) - math.log(a.denominator)


def check_n(n):
    J, s, R, d = n-1, Q(11,10), Q(11,8), Q(5,4)
    nodes = [Q(j,n)/R for j in range(1,n)]
    beta = product_series([(-z,Q(1),z) for z in nodes], J)
    inner = product_series([(-z/s,Q(1),z/s) for z in nodes], J)
    inverse_outer = product_series([(Q(1),-z*s,z/s) for z in nodes], J, s**(-J))
    at_zero = [sum((beta[l]*inverse_outer[k-l] for l in range(k+1)), Q(0)) for k in range(n)]
    S, C, T = dot(inner,inner), dot(inner,at_zero), dot(at_zero,at_zero)
    delta = S-C*C/T
    H = [(a-C*b/T)/delta for a,b in zip(inner,at_zero)]
    c = [sum((inverse_outer[k-l]*H[k] for k in range(l,n)), Q(0)) for l in range(n)]
    P = [Q(0)] + [beta[l]*s**l*c[l] for l in range(n)]
    checks = {
        'delta_positive': delta > 0,
        'anchor_value_one': sum(P) == 1,
        'prescribed_zero': sum((a*Q(10,11)**k for k,a in enumerate(P)),Q(0)) == 0,
        'norm_identity': dot(H,H) == 1/delta,
        'anchor_inner_identity': dot(H,inner) == 1,
        'zero_functional_identity': dot(H,at_zero) == 0,
        'prefix_mass_bound': S >= Q(1,n),
    }
    points=[]
    for a in [1,2,3,4,5,6]:
        y=Q(a,n)
        if y>Q(9,20):
            continue
        den=d*d+y*y
        value=real_value(P,d*d/den,d*y/den)
        lower=Q((1000*value).__floor__(),1000)
        upper=lower+Q(1,1000)
        points.append({'y':y, 'real_action':value, 'negative':value<0,
                       'enclosure':[lower,upper], 'enclosure_verified':lower<=value<upper})
    return {
        'n':n, 'checks':checks,
        'beta':beta, 'inner_coefficients':inner, 'inverse_outer_coefficients':inverse_outer,
        'zero_functional':at_zero, 'S':S, 'C':C, 'T':T, 'delta':delta,
        'H':H, 'moment_coefficients':c, 'P':P, 'norm_squared':1/delta,
        'norm_at_most_n':1/delta<=n*n,
        'norm_log_per_n_diagnostic':log_rational(1/delta)/(2*n),
        'required_exponential_rate':Q(1,100),
        'point_signs':points,
    }


def main():
    rows=[]
    failures=[]
    for n in [15,27,51]:
        row=check_n(n)
        rows.append(row)
        failures += [f'n={n}: {k}' for k,v in row['checks'].items() if not v]
        failures += [f'n={n}: enclosure at {p["y"]}' for p in row['point_signs'] if not p['enclosure_verified']]
        negatives=[str(p['y']) for p in row['point_signs'] if p['negative']]
        print(f"n={n}: exact identities={all(row['checks'].values())}; norm<=n={row['norm_at_most_n']}; log(norm)/n={row['norm_log_per_n_diagnostic']:.8g}; required asymptotic rate=0.01 with polynomial allowance; negative points={negatives}", flush=True)
    original_path=Path(__file__).with_name('polynomial-inner-inverse-check.json')
    original=json.loads(original_path.read_text())
    row=rows[0]
    comparison={
        'source':str(original_path.relative_to(Path.cwd())),
        'all_polynomial_coefficients_match':row['P']==[Q(a) for a in original['polynomial']],
        'all_inverse_coefficients_match_after_rotation':row['H']==[(-1)**k*Q(original['constrained_h'][14-k]) for k in range(15)],
        'schur_complement_matches':row['delta']==Q(original['gram']['delta']),
        'exact_norm_squared_matches':row['norm_squared']==Q(original['constrained_norm_squared']),
    }
    failures += [f'independent comparison: {k}' for k,v in comparison.items() if isinstance(v,bool) and not v]
    path=Path(__file__).with_suffix('.json')
    data={'type':'exact rational finite polynomial checks, no asymptotic sign conclusion',
          'rows':rows, 'independent_comparison':comparison, 'verification_failures':failures,
          'target_limitations':['negative points exclude these finite candidates only',
                                'no uniform onset or asymptotic norm rate certified',
                                'no assertion that this subspace contains every minimum-norm inverse']}
    path.write_text(json.dumps(encode(data),indent=2)+'\n')
    print(f'verification failures={failures}; certificate={path}')
    print(f'independent n=15 coefficient comparison={all(v for v in comparison.values() if isinstance(v,bool))}')
    raise SystemExit(bool(failures))


if __name__=='__main__':
    main()
