"""Exact rational checks for C034h; no floating-point sign certificate.

The analytic estimates, domains and limit arguments are in C034h.
This verifies only its finite scalar thresholds. All arithmetic here
uses fractions and integers, including lower exponential series.
"""
from fractions import Fraction as F
import json
from pathlib import Path


def exp_lower(x, degree):
    term = total = F(1)
    for k in range(1, degree+1):
        term *= x/k
        total += term
    return total


def encode(q):
    q = F(q)
    return {'numerator': str(q.numerator), 'denominator': str(q.denominator)}


def main():
    checks, bounds, exponentials = {}, {}, {}

    def check(name, actual, required, direction='<'):
        a, b = F(actual), F(required)
        ok = a < b if direction == '<' else a > b
        checks[name] = ok
        bounds[name] = {'actual': encode(a), 'required': encode(b), 'relation': direction}

    for name,x,n,threshold in [
        ('exp3',F(3),8,20),
        ('exp169over8',F(169,8),100,1490000000),
        ('exp49over2',F(49,2),100,43000000000),
    ]:
        value = exp_lower(x,n)
        floor = value.numerator//value.denominator
        exponentials[name] = {'argument':encode(x), 'degree':n,
                              'sum':encode(value), 'floor':str(floor),
                              'required_lower':str(threshold)}
        check(name, value, threshold, '>')

    check('e_upper',F(65,24)+F(1,100),F(11,4))
    check('sqrt2_upper_squared',2,F(100,49))
    for p, limit in [(4,F(3,100)),(6,F(3,25))]:
        check(f'low_origin_endpoint_p{p}', F(5*14**(p+1),96*16**7),limit)
        check(f'low_midpoint_endpoint_p{p}', F(5*14*2**p,96*400),limit)
        check(f'negative_translate_p{p}',F(5*14**p,48*(p-1)*16**8),F(1,1000))
    check('I4_bound',F(10,7)+F(3,100)+F(1,1000),F(3,2))
    check('I6_bound',F(25,7)+F(3,25)+F(1,1000),F(15,4))

    def fn(k,u):
        poly = {0:F(1), 1:F(u,4), 2:F(u*u,16)+F(1,4),
                4:F(u**4,256)+F(3*u*u,32)+F(3,16)}[k]
        exponential_denominator = 1490000000 if u == 13 else 43000000000
        return F(5,24)*poly/exponential_denominator

    def mn(k):
        return (fn(k,13)+fn(k,14))/2

    check('alpha1_scaled',14**6*(F(9,4)*mn(2)+2*fn(0,14)),F(1,50))
    check('alphaR_scaled',14**6*(F(5,2)*mn(2)+F(4,3)*fn(0,14)),F(1,50))
    check('beta1_scaled',14**8*(F(9,4)*mn(4)+2*fn(2,14)+4*mn(1)+10*mn(0)),40)
    check('betaR_scaled',14**8*(F(5,2)*mn(4)+F(4,3)*fn(2,14)
                                 +F(32,9)*mn(1)+F(284,27)*mn(0)),40)
    check('nonreal_alpha_scaled',F(35*100**8,16**300),F(1,50))
    check('nonreal_beta_scaled',F(37*100**12,16**300),40)

    # Bounds on complex rational functions for x>=13, |Im v|<=1/2.
    t = F(169)
    check('complex_Q1',4*(3+1/t),13)
    check('complex_R',8*(5+9/t+2/t**2),45)
    check('complex_Q1_second',24*(10+5/t+4/t**2+1/t**3),260)
    check('complex_Q2_second',48*(10+10/t+16/t**2+8/t**3),520)
    check('H1_scaled',13*F(3,2),20)
    check('HR_scaled',45*F(15,4),200)
    check('W1_scaled',260*F(15,4),1000)
    check('W2_scaled',520*F(15,4),2000)

    check('normalized_core_factor',F(111,121)*F(213,242),F(4,5),'>')
    check('core_kernel_coefficient',4965*F(16,25),3100,'>')
    check('half_core_mass',F(11,27),F(2,5),'>')
    correction = 50+F(800,2)+F(8000,392)+F(8,5*392)
    check('pair_correction_coefficient',correction,471)
    check('remaining_pair_margin',496-correction,25,'>')

    failures = [k for k,v in checks.items() if not v]
    result = {'arithmetic':'exact fractions and integers',
              'scope':'finite scalar checks only; analytic proof is C034h, pending audit',
              'checks':checks,'bounds':bounds,'exponential_lower_bounds':exponentials,
              'summary':{'check_count':len(checks),'failures':failures,
                         'core_coefficient':496,'correction_upper':471,
                         'claimed_margin':25,'required_margin':0,
                         'unresolved':'independent conceptual audit; no actual-divisor assembly or RH conclusion'}}
    path=Path(__file__).with_suffix('.json')
    path.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result['summary']))
    print('Full exact certificate:',path)
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
