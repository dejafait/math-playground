#!/usr/bin/env python3
"""Fixed-model diagnostic. Decimal arithmetic is NOT interval arithmetic.

Run: python3 scripts/gamma-geometric/contact-diagnostic-895.py
No sampled sign, replay agreement, or analytic tail estimate certifies
the unsampled prefix or the rounding/asymptotic evaluation error.
"""
import json
from decimal import Decimal as D, localcontext
from pathlib import Path

OUT = Path(__file__).with_suffix('.json')
BETA = D('0.5')


def falling(j):
    v = D(1)
    for k in range(j):
        v *= BETA-k
    return v


def jets(x, precision=100, terms=32, asymptotic_terms=160):
    with localcontext() as ctx:
        ctx.prec = precision
        result = [D(0) for _ in range(6)]
        coefficient = D(2)
        for n in range(1, terms+1):
            b = D(2**n-1)
            t = b*x
            if t <= 512:
                power, total, k = D(1), D(1), 0
                while True:
                    k += 1
                    power *= t/k
                    add = power/(2*k+1)
                    total += add
                    if k > t and add < abs(total)*D(10)**(-precision-8):
                        break
                base = x.sqrt()/b*(1-(-t).exp()*total)
                js = [base]
                for j in range(1, 6):
                    js.append(falling(j-1)*x**(BETA-(j-1))-b*js[-1])
            else:
                js = []
                for j in range(6):
                    term = falling(j)
                    total = term
                    for k in range(asymptotic_terms-1):
                        term *= -(BETA-j-k)/t
                        total += term
                    js.append(x**(BETA-j)/b*total)
            for j in range(6):
                result[j] += coefficient*js[j]
            coefficient *= -D(2)/(2**n-1)
        return result


def det3(a, b, c):
    return (a[0]*(b[1]*c[2]-b[2]*c[1])
            -a[1]*(b[0]*c[2]-b[2]*c[0])
            +a[2]*(b[0]*c[1]-b[1]*c[0]))


def evaluate(x, precision=100, terms=32, asymptotic_terms=160):
    with localcontext() as ctx:
        ctx.prec = precision
        q = jets(x, precision, terms, asymptotic_terms)
        f = -det3(q[:3], q[1:4], q[2:5])
        fp = -det3(q[:3], q[1:4], q[3:6])
        z = f/q[0]**3
        zp = fp/q[0]**3-3*z*q[1]/q[0]
        k = (q[1]**2-q[0]*q[2])/q[0]**2
        return {'x':str(x), 'Q':str(q[0]), 'D2_over_Q2':str(k),
                'D3_over_Q3':str(z), 'normalized_D3_derivative':str(zp),
                'D3':str(f), 'D3_derivative':str(fp)}


def tail_bounds(left, right, terms=32):
    """Analytic bounds for omitted series terms, before decimal rounding.

    The canonical proof gives these expressions as exact upper bounds.
    Values stored here are decimal evaluations, not outward enclosures.
    """
    with localcontext() as ctx:
        ctx.prec=100
        n=terms+1
        coefficient=D(2**n)
        for m in range(1,n):
            coefficient/=2**m-1
        b=D(2**n-1)
        bounds=[]
        for j in range(6):
            bound=b**j*D(2)/3*right**D('1.5')
            for r in range(j):
                exponent=BETA-r
                max_power=max(left**exponent,right**exponent)
                bound+=b**(j-1-r)*abs(falling(r))*max_power
            rho=D(2*3**j)/(2**n-1)
            bounds.append(str(coefficient*bound/(1-rho)))
        return bounds


def main():
    with localcontext() as ctx:
        ctx.prec=100
        grid=[D(k)/32 for k in range(1,513)]
        rows=[evaluate(x) for x in grid]
        sample_summary={
            'D2_nonpositive_samples':[r['x'] for r in rows if D(r['D2_over_Q2'])<=0],
            'D3_positive_samples':sum(D(r['D3_over_Q3'])>0 for r in rows),
            'D3_zero_samples':sum(D(r['D3_over_Q3'])==0 for r in rows),
            'D3_negative_samples':sum(D(r['D3_over_Q3'])<0 for r in rows),
            'minimum_positive_sample_D3_over_Q3':str(min(D(r['D3_over_Q3']) for r in rows
                                                         if D(r['D3_over_Q3'])>0))}
        brackets=[]
        for a,b in zip(rows,rows[1:]):
            if D(a['D3_over_Q3'])*D(b['D3_over_Q3'])<0:
                brackets.append([a['x'],b['x']])
        candidate=None
        if brackets:
            lo,hi=map(D,brackets[0])
            for _ in range(55):
                mid=(lo+hi)/2
                if D(evaluate(mid)['D3_over_Q3'])>0:
                    lo=mid
                else:
                    hi=mid
            center=(lo+hi)/2
            replay=evaluate(center,140,40,220)
            candidate={'sample_bisection_bracket':[str(lo),str(hi)],
                       'left':evaluate(lo), 'right':evaluate(hi),
                       'center':evaluate(center), 'higher_precision_replay':replay,
                       'replay_abs_difference_Z':str(abs(D(replay['D3_over_Q3'])-
                                                      D(evaluate(center)['D3_over_Q3'])))}
        payload={
            'status':'DIAGNOSTIC_ONLY_NOT_A_PROOF',
            'model':'gamma(shape=3/2,rate=1) + sum Exp(rate=2^n), n>=1',
            'normalization':'Q=Gamma(3/2)*exp(x)*p(x)/K; K=product(1-2^-n)^-1',
            'method':{'decimal_precision':100,'series_terms':32,
                      'asymptotic_terms':160,'series_asymptotic_switch':512,
                      'rounding_enclosed':False,'asymptotic_remainder_enclosed':False},
            'requirements':{'D3_positive_on_entire_prefix':True,
                            'strict_negative_derivative_at_first_zero':True},
            'analytic_series_tail':{'interval':['0.03125','16'],
                                    'orders_0_to_5':tail_bounds(D(1)/32,D(16)),
                                    'decimal_evaluation_not_outward':True},
            'sample_count':len(rows), 'observed_sign_change_brackets':brackets,
            'sample_summary':sample_summary,
            'coarse_contact_endpoints':[evaluate(D(139)/32),evaluate(D(35)/8)],
            'candidate':candidate, 'samples':rows,
            'failures':['No effective positive endpoint interval joined to the grid.',
                        'No enclosures between sample points; earlier tangencies not excluded.',
                        'No outward rounding or certified asymptotic evaluation remainder.',
                        'Bisection and precision replay do not certify a zero or its derivative.']}
        OUT.parent.mkdir(parents=True,exist_ok=True)
        OUT.write_text(json.dumps(payload,indent=2)+'\n')
        print('DIAGNOSTIC ONLY:',len(rows),'samples; sign-change brackets:',brackets)
        if candidate:
            print('Candidate x:',candidate['center']['x'])
            print('Normalized derivative:',candidate['center']['normalized_D3_derivative'])
            print('Precision replay |delta Z|:',candidate['replay_abs_difference_Z'])
        print('Required: full positive prefix and strictly negative first-zero derivative.')
        print('Analytic omitted-series bounds, derivative orders 0..5 (decimal evaluations):',
              payload['analytic_series_tail']['orders_0_to_5'])
        print('Unmet: endpoint join, interval coverage, rounding and evaluation bounds.')
        print('Full diagnostic:',OUT)


if __name__=='__main__':
    main()
