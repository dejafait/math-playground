"""One fixed full-theta M14 enclosure and normalized L938 energy-mean test.

Run from riemann. L037 library contracts apply; no RH or full order claim.
Complete panel, row and arithmetic evidence is saved beside this file.
"""
import hashlib
import json
import re
import sys
from decimal import DivisionByZero, InvalidOperation, Overflow, Underflow, Subnormal
from fractions import Fraction as Q
from math import factorial
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'scripts/hankel'))
import certify_hankel as base

OUT = Path(__file__).with_suffix('.json')
SOURCE = ROOT / 'lemmas/L938-actual-h2-fixed-energy-density-and-cell-test.md'
ORDERS = tuple(range(0, 15, 2))
for ctx in (base.DOWN, base.UP, base.NEAR):
    ctx.prec = 100
    ctx.clear_flags()
I = base.I


def product(values):
    result = I(1)
    for value in values:
        result = result * value
    return result


def main():
    base.self_check()
    assert base.ORDER == 8
    # Exact witnesses for exp(4)>50 and exp(9)>32.
    assert sum((Q(4)**j/factorial(j) for j in range(8)), Q(0)) > 50
    assert sum((Q(9)**j/factorial(j) for j in range(5)), Q(0)) > 32
    pi = base.pi_bounds()
    coefficient = sum((Q(factorial(9), factorial(9-j))*Q(50**(9-j), 3**(j+1))
                       for j in range(10)), Q(0))
    spatial = 128 * I(-150).exp() * I.rational(coefficient)
    theta = 29030400000 * I(-74).exp()
    tail = spatial + theta
    totals = {k: I(0) for k in ORDERS}
    errors = {k: I(0) for k in ORDERS}
    panels = []
    h = I.rational(Q(1, 64))
    weights = {j: 2*h**(j+1)/(j+1) for j in (0, 2, 4, 6)}
    remainder_weight = 2*h**9/9
    for p in range(64):
        c = I.rational(Q(2*p+1, 64))
        domain = I(I.rational(Q(2*p, 64)).lo, I.rational(Q(2*p+2, 64)).hi)
        midkernel = base.theta_kernel_jet(c, pi)
        domkernel = base.theta_kernel_jet(domain, pi)
        record = {'index': p, 'center': c.data(), 'domain': domain.data(), 'orders': {}}
        for k in ORDERS:
            mid = base.moment_jet(c, k, midkernel)
            eighth = base.moment_jet(domain, k, domkernel)[8]
            poly = sum((mid[j]*weights[j] for j in weights), I(0))
            error = I(eighth.magnitude()) * remainder_weight
            integral = poly + I(error.hi.copy_negate(), error.hi)
            totals[k] = totals[k] + integral
            errors[k] = errors[k] + error
            record['orders'][str(k)] = {
                'midpoint_even_coefficients': {str(j): mid[j].data() for j in weights},
                'eighth_coefficient': eighth.data(), 'polynomial_integral': poly.data(),
                'error': error.data(), 'integral': integral.data()}
        panels.append(record)
    moments = {k: totals[k] + I(0, tail.hi) for k in ORDERS}
    assert all(v.lo > 0 for v in moments.values())
    A = [moments[2*k]/factorial(2*k) for k in range(7)]
    B = [moments[2*k+2]/factorial(2*k) for k in range(7)]
    rows = []
    masses = {'plus': I(0), 'minus': I(0)}
    firsts = {'plus': I(0), 'minus': I(0)}
    for coefficient_text, alpha_text in re.findall(
            r'^\| (-?\d+) \| \(([0-9,]+)\) \|$', SOURCE.read_text(), re.M):
        coefficient_row = int(coefficient_text)
        alpha = tuple(map(int, alpha_text.split(',')))
        assert len(alpha) == 7 and sum(alpha) == 12
        assert sum(k*a for k, a in enumerate(alpha)) == 12
        mass = product(A[k]**alpha[k] for k in range(7))
        terms = {}
        for k in range(7):
            if alpha[k]:
                terms[str(k)] = alpha[k]*B[k]*product(
                    A[j]**(alpha[j]-(j == k)) for j in range(7))
        first = sum(terms.values(), I(0))
        side = 'plus' if coefficient_row > 0 else 'minus'
        masses[side] = masses[side] + abs(coefficient_row)*mass
        firsts[side] = firsts[side] + abs(coefficient_row)*first
        rows.append({'coefficient': coefficient_row, 'alpha': alpha, 'side': side,
                     'mass': mass.data(), 'first_moment_terms': {k:v.data() for k,v in terms.items()},
                     'first_moment': first.data()})
    assert len(rows) == 34
    assert all(v.lo > 0 for v in masses.values())
    means = {side: firsts[side]/masses[side] for side in masses}
    delta = means['plus'] - means['minus']
    cross = firsts['plus']*masses['minus']-firsts['minus']*masses['plus']
    # A second safe expression, retaining dependence only as enclosure.
    cross_delta = cross/(masses['plus']*masses['minus'])
    assert max(delta.lo, cross_delta.lo) <= min(delta.hi, cross_delta.hi)
    decision = ('reject_normalized_order' if delta.hi < 0 else
                'mean_prerequisite_only_passes' if delta.lo >= 0 else 'inconclusive_stop')
    signals = (DivisionByZero, InvalidOperation, Overflow, Underflow, Subnormal)
    arithmetic = {name: {'precision':ctx.prec, 'rounding':ctx.rounding,
                        'traps':{s.__name__:ctx.traps[s] for s in signals},
                        'exceptional_flags':{s.__name__:ctx.flags[s] for s in signals}}
                  for name,ctx in (('DOWN',base.DOWN),('UP',base.UP),('NEAR',base.NEAR))}
    assert all(ctx.traps[s] and not ctx.flags[s]
               for ctx in (base.DOWN,base.UP,base.NEAR) for s in signals)
    result = {
        'scope': 'lambda=0; first-moment necessity only; no full order or determinant sign',
        'budget': {'precision':100, 'spatial_panels':64, 'cutoff':2, 'theta_terms':4, 'taylor_order':8},
        'inputs': {str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest()
                   for p in (SOURCE, Path(base.__file__), Path(__file__))},
        'pi':pi.data(), 'tails':{'spatial_coefficient':str(coefficient),
             'spatial':spatial.data(), 'theta':theta.data(), 'total':tail.data()},
        'panels':panels, 'finite_moments':{str(k):v.data() for k,v in totals.items()},
        'quadrature_error_bounds':{str(k):v.data() for k,v in errors.items()},
        'moments':{str(k):v.data() for k,v in moments.items()},
        'factor_masses':{str(k):v.data() for k,v in enumerate(A)},
        'factor_first_moments':{str(k):v.data() for k,v in enumerate(B)},
        'rows':rows, 'masses':{k:v.data() for k,v in masses.items()},
        'first_moments':{k:v.data() for k,v in firsts.items()},
        'means':{k:v.data() for k,v in means.items()}, 'delta':delta.data(),
        'cross_numerator':cross.data(), 'cross_delta':cross_delta.data(),
        'arithmetic':arithmetic, 'decision':decision, 'failures':[],
    }
    OUT.write_text(json.dumps(result, indent=2)+'\n')
    print(f'rows={len(rows)}/34; all moments and both normalizers strictly positive')
    print(f'delta=[{delta.lo}, {delta.hi}]; required >=0; decision={decision}')
    print(f'common discarded tail upper={tail.hi}; failures=[]')
    print(f'certificate={OUT.relative_to(ROOT)}')


if __name__ == '__main__':
    main()
