"""Approved 256-panel actual-Xi quadrature and four C030z trials only.

Uses L917/L036/L037, without changing the old uniform certificate.
Full finite-integration records and all failed/undecided trials go to disk.
"""
import hashlib
import importlib.util
import json
import platform
from decimal import DivisionByZero, InvalidOperation, Overflow, Underflow, Subnormal
from fractions import Fraction as F
from math import factorial
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
SOURCE = HERE.parent / 'heat/low-time-h2-uniform-195.py'
spec = importlib.util.spec_from_file_location('l917_producer', SOURCE)
p = importlib.util.module_from_spec(spec)
spec.loader.exec_module(p)
base, I = p.base, p.I
OUT = HERE / 'actual-singleton-certificate-1307.json'
TRIALS = (F(-2), F(-1), F(0), F(1, 2))


def scalar_trial(s, x):
    A, B, C, D, E = (s[n] for n in range(2, 7))
    k = A/(2*C)
    one = I(1)
    L = -E*k*(one+x)+E*x*B/D+(one-x)*B**2/(2*A)
    N = A*(x**2+x+one)/3-E*k**2*(one+x)**2
    result = {'x': x.data(), 'k': k.data(), 'L': L.data(), 'N': N.data()}
    if L.lo <= 0 <= L.hi:
        # A zero-containing interval is not an exact identity.
        result.update(status='undecided_L_contains_zero',
                      exact_L_zero_proved=False, exact_N_zero_proved=False,
                      exceptional_branch='L=N=0 retains free positive p; not decided')
        return result
    param = N/L
    V = param-k*(one+x)
    J = V-x*B/D
    H = param*J-x*V*C/E+(one-x)*param*B**2/(2*A*E)
    values = {'p': param, 'V': V, 'J': J, 'H': H}
    failed = [name for name, val in values.items() if val.hi <= 0]
    undecided = [name for name, val in values.items() if val.lo <= 0 < val.hi]
    result.update(values={name: val.data() for name, val in values.items()},
                  failed_strict_inequalities=failed, undecided_inequalities=undecided,
                  status=('rejected' if failed else 'undecided' if undecided else 'certified'),
                  p_definition='exact N(x)/L(x) in the actual constants, not an interval midpoint',
                  equality='pL=N holds by definition because L excludes zero',
                  tau=((one-x)/A).data())
    return result


def main():
    p.SPATIAL_PANELS = 256
    p.checks()
    pi = base.pi_bounds()
    spatial, theta, tail = p.tilted_tail()
    report = {'status': 'running', 'python': platform.python_version(),
              'scope': 'lambda=0; finite mixed degree <=6 only; not univalence or RH',
              'precision': 100, 'spatial_panels': 256, 'theta_terms': 4,
              'spatial_cutoff': 2, 'taylor_remainder_order': 8,
              'lambda': I(0).data(), 'pi': pi.data(),
              'tails': {k:v.data() for k,v in zip(('spatial','theta','total'),(spatial,theta,tail))},
              'input_sha256': {str(f.relative_to(ROOT)): hashlib.sha256(f.read_bytes()).hexdigest()
                               for f in (Path(__file__), SOURCE, HERE.parent/'hankel/certify_hankel.py')},
              'panels': []}
    OUT.write_text(json.dumps(report, indent=2)+'\n')
    cached, weights, remainder_weight = p.prepare(pi)
    report['weights'] = {str(j): val.data() for j,val in weights.items()}
    report['remainder_weight'] = remainder_weight.data()
    totals, errors = {k:I(0) for k in p.ORDERS}, {k:I(0) for k in p.ORDERS}
    for index, (center, domain, midpoint, rectangle) in enumerate(cached):
        record = {'index': index, 'center': center.data(), 'domain': domain.data(), 'orders': {}}
        for order in p.ORDERS:
            polynomial = sum((midpoint[order][j]*weights[j] for j in (0,2,4,6)), I(0))
            error = I(rectangle[order][8].magnitude())*remainder_weight
            totals[order] = totals[order]+polynomial+I(error.hi.copy_negate(), error.hi)
            errors[order] = errors[order]+error
            record['orders'][str(order)] = {
                'midpoint_even_coefficients': {str(j):midpoint[order][j].data() for j in (0,2,4,6)},
                'full_eighth_coefficient': rectangle[order][8].data(),
                'polynomial_integral': polynomial.data(), 'remainder_bound': error.data()}
        report['panels'].append(record)
    moments = {k:total+I(0,tail.hi) for k,total in totals.items()}
    report['finite_moments'] = {str(k):v.data() for k,v in totals.items()}
    report['moments'] = {str(k):v.data() for k,v in moments.items()}
    report['quadrature_error_bounds'] = {str(k):v.data() for k,v in errors.items()}
    assert all(v.lo > 0 for v in moments.values()), 'Nonpositive moment box: stop, no refinement'
    e = [I(1)]+[moments[2*n]/(factorial(2*n)*moments[0]) for n in range(1,7)]
    # L917's finite logarithm polynomials, with the audited signs.
    a,b,c,d,e5,f = e[1:]
    sums = [a, a**2-2*b, a**3-3*a*b+3*c,
            a**4-4*a**2*b+2*b**2+4*a*c-4*d,
            a**5-5*a**3*b+5*a*b**2+5*a**2*c-5*b*c-5*a*d+5*e5,
            a**6-6*a**4*b+9*a**2*b**2-2*b**3+6*a**3*c-12*a*b*c+3*c**2
            -6*a**2*d+6*b*d+6*a*e5-6*f]
    s = dict(enumerate(sums,1))
    report['normalized_coefficients'] = {str(n):v.data() for n,v in enumerate(e[1:],1)}
    report['S'] = {str(n):v.data() for n,v in s.items()}
    if all(s[n].lo > 0 for n in range(2,7)):
        report['trials'] = [scalar_trial(s, I.rational(x)) for x in TRIALS]
    else:
        report['trials'] = [{'x_exact':str(x), 'status':'undecided_actual_sum_denominator'} for x in TRIALS]
    signals = (DivisionByZero, InvalidOperation, Overflow, Underflow, Subnormal)
    report['arithmetic'] = {name:{'precision':ctx.prec, 'rounding':ctx.rounding,
                                 'traps':{sig.__name__:ctx.traps[sig] for sig in signals},
                                 'exceptional_flags':{sig.__name__:ctx.flags[sig] for sig in signals}}
                            for name,ctx in (('DOWN',base.DOWN),('UP',base.UP),('NEAR',base.NEAR))}
    assert all(ctx.traps[sig] and not ctx.flags[sig]
               for ctx in (base.DOWN,base.UP,base.NEAR) for sig in signals)
    report['summary'] = {'strict_S2_through_S6':all(s[n].lo>0 for n in range(2,7)),
                         'trial_statuses': [r['status'] for r in report['trials']],
                         'certified_witnesses':sum(r['status']=='certified' for r in report['trials']),
                         'required': 'x<1 and p,V,J,H>0; pL=N exactly; all d_j,tau>0',
                         'all_other_x_and_exceptional_branches': 'untested, no global decision',
                         'exceptional_arithmetic':False}
    report['status'] = 'completed'
    OUT.write_text(json.dumps(report, indent=2)+'\n')
    for n in range(2,7):
        print(f'S{n}: [{s[n].lo:.9E}, {s[n].hi:.9E}], required lower >0')
    for x,row in zip(TRIALS,report['trials']):
        print(f'x={x}: {row["status"]}')
        for name,val in row.get('values',{}).items():
            print(f'  {name}: [{val["lower"]}, {val["upper"]}], required lower >0')
    print(f'Complete certificate: {OUT.relative_to(ROOT)}')


if __name__ == '__main__':
    main()
