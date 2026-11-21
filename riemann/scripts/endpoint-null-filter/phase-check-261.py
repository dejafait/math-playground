"""Finite diagnostic for the approved M=2 phase coefficient; not a proof."""
from decimal import Decimal as D, localcontext
from pathlib import Path
import json

PI_TEXT = '3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679'


def cos(x, pi):
    x = x % (2*pi)
    if x > pi:
        x -= 2*pi
    term = total = D(1)
    for k in range(1, 500):
        term *= -x*x / ((2*k-1)*(2*k))
        total += term
        if abs(term) < D('1e-85'):
            return total
    raise ArithmeticError('cosine series did not terminate')


def laguerre(n, x):
    prev, cur = D(1), 3-x
    if n == 0:
        return prev
    for k in range(1, n):
        prev, cur = cur, ((2*k+3-x)*cur-(k+2)*prev)/(k+1)
    return cur


def main():
    rows = []
    with localcontext() as ctx:
        ctx.prec = 90
        pi, root3 = D(PI_TEXT), D(3).sqrt()
        gamma = {
            1: -55*root3/432+45/(8*(3*root3+2*pi)),
            2: -D(5)/6+15/(8*(2+pi)),
        }
        for n in (64, 128, 256, 512, 1024):
            for r in (1, 2):
                # The endpoint amplitude is evaluated at the exact scaled t.
                nu, x = D(4*n+6), D(r*n)
                t = x/nu
                denom = 4*(t.ln()*D('1.25')+(1-t).ln()/4).exp()
                amplitude = (2/(pi*nu)).sqrt()/denom
                normalized = laguerre(n, x)*(-x/2).exp()/amplitude
                base = (n*(root3/2+pi/3)-3*pi/4 if r == 1
                        else n*(1+pi/2)-pi/2)
                approximation = cos(base+gamma[r]/n, pi)
                inferred = n*(cos(base, pi)-normalized)/cos(base-pi/2, pi)
                rows.append({'n': n, 'endpoint_multiple': r,
                             'scaled_value': str(normalized),
                             'phase_approximation': str(approximation),
                             'n_squared_residual': str(n*n*(normalized-approximation)),
                             'proposed_phase_coefficient': str(gamma[r]),
                             'finite_inferred_phase_coefficient': str(inferred)})
        norm_limit = (125+810*root3/(3*root3+2*pi)-405/(2+pi))/(pi*pi)
        result = {'purpose': 'Finite coefficient diagnostic only; no rigorous enclosure or asymptotic verification',
                  'required': 'Bounded n^2 residual is a consistency diagnostic, not proof of the source remainder',
                  'precision_digits': 90, 'rows': rows,
                  'proposed_integer_limit': str(norm_limit),
                  'max_abs_n_squared_residual': str(max(abs(D(row['n_squared_residual'])) for row in rows)),
                  'failures': [],
                  'mathematical_status': 'INCONCLUSIVE: second-order coefficient consistency unresolved; no rigorous source refutation',
                  'warning': 'The n^2 residual is about 36.64 at n=512,r=2 and -73.19 at n=1024,r=2. Do not use the proposed coefficient for nonvanishing until its source normalization is checked.'}
    path = Path(__file__).with_suffix('.json')
    path.write_text(json.dumps(result, indent=2)+'\n')
    print('Finite M=2 coefficient diagnostic; not a rigorous certificate.')
    print('Actual max |n^2 residual|:', result['max_abs_n_squared_residual'][:24])
    print('Required asymptotic bound: O(1); a valid analytic proof is still required.')
    print('Proposed integer limit:', result['proposed_integer_limit'][:24])
    print('Execution failures:', result['failures'])
    print('Mathematical status:', result['mathematical_status'])
    print('Full diagnostic:', path)


if __name__ == '__main__':
    main()
