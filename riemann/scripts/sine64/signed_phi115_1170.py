"""One fixed complete signed scalar; exact outward integer intervals only.

Canonical analytic error proof: lemmas/C750o-signed-phi115-compensation.md.
Reuse the independently audited1166 elementary interval primitives.
"""
from fractions import Fraction as F
from pathlib import Path
from math import isqrt
import json
from negative_loss_witness_1166 import (
    I, SCALE, PI, log_interval, sine_or_cosine, sinc_small, qstr,
)


def sinc(x):
    if max(abs(x.lo), abs(x.hi)) <= 4*SCALE:
        return sinc_small(x)
    assert x.lo*x.hi > 0
    return sine_or_cosine(x)/x


def main():
    L = log_interval(101)
    b = L/2
    alpha = 115*PI/L
    aa = alpha*alpha
    powers = {}
    for p in range(2, 101):
        if all(p % d for d in range(2, isqrt(p)+1)):
            n = p
            while n < 101:
                powers[n] = p
                n *= p
    terms = []
    prime = I(0)
    A = I(0)
    for n, p in sorted(powers.items()):
        ell = log_interval(n)
        c = 2*log_interval(p)/I(n).sqrt()
        corr = (1-ell/L)*sine_or_cosine(alpha*ell, cosine=True)
        corr += sine_or_cosine(alpha*ell)/(L*alpha)
        contribution = c*corr
        prime += contribution
        A += c
        terms.append(dict(n=n, p=p, c=c.record(), ell=ell.record(),
                          correlation=corr.record(), contribution=contribution.record()))

    root101 = I(101).sqrt()
    cosh_b = (root101+1/root101)/2
    pole = 4*aa*(cosh_b+1)/(b*(aa+F(1,4))*(aa+F(1,4)))
    # Complete [1,512] log-symbol expectation. Apparent Fourier poles
    # are enclosed by sinc's continuous Taylor polynomial.
    h = F(1,100)
    count = 51100
    integral = I(0)
    cells = []
    for k in range(count):
        t = I(1+F(2*k+1,200))
        u, v = b*t-F(115,2)*PI, b*t+F(115,2)*PI
        G = sinc(u)+sinc(v)
        logval = log_interval(t/(2*PI))
        contribution = I(h)*logval*b*G*G/PI
        integral += contribution
        cells.append(dict(k=k, midpoint=qstr(t.lo), G=G.record(),
                          log_symbol=logval.record(), contribution=contribution.record()))

    quad_error = I(F(186,80000))
    low_error = 44*aa/(PI*b*(aa-1)*(aa-1))
    asym_error = 128/(9*PI*b*aa)+8/aa
    B = 512
    log_tail = (64*aa/(9*PI*b))*((log_interval(I(B)/(2*PI))+F(1,3))/(3*B**3))
    # Tail log-symbol is positive; m-log discrepancy is paid by asym_error.
    gamma = integral + I(-quad_error.hi,quad_error.hi,raw=True)
    gamma += I(-low_error.hi,low_error.hi,raw=True)
    gamma += I(-asym_error.hi,asym_error.hi,raw=True)
    gamma += I(0,log_tail.hi,raw=True)
    energy = gamma-prime+pole
    # The accepted comparison and full tail bound give 0<=E-R<10^-8.
    reduced = energy-I(0,F(1,10**8))
    checks = {
        'exactly35_prime_powers': len(terms)==35,
        '2_lt_b_lt_5_over_2': 2*SCALE<b.lo and b.hi<5*SCALE//2,
        '2_lt_alpha_lt_80': 2*SCALE<alpha.lo and alpha.hi<80*SCALE,
        'A_lt_34': A.hi<34*SCALE,
        'all_cells_cover_1_512': count*h==511,
        'width_at_most_1_over_50': 50*(reduced.hi-reduced.lo)<=SCALE,
        'positive_lower_endpoint': reduced.lo>0,
    }
    cert = dict(scope='Only fixed phi115: no full lower spectral bound or Xi transfer.',
                method='Audited integer intervals; complete signed correlations/pole; paid gamma and cutoff errors.',
                scale=str(SCALE), index=115, unchanged_projection_rank=64,
                parameters=dict(pi=PI.record(),L=L.record(),b=b.record(),alpha=alpha.record(),A=A.record()),
                positive_frequency_interval=[1,512],mesh=str(h),
                errors=dict(midpoint=quad_error.record(),gamma_0_1=low_error.record(),
                            gamma_asymptotic=asym_error.record(),log_tail=log_tail.record(),
                            E_minus_R_upper='1/100000000'),
                complete_midpoint_sum=integral.record(),prime_expectation=prime.record(),
                full_pole=pole.record(),gamma_expectation=gamma.record(),
                full_E=energy.record(),full_R=reduced.record(),
                required_width='1/50',checks=checks,
                failures=[key for key,ok in checks.items() if not ok],
                prime_powers=terms,cells=cells)
    path=Path(__file__).with_name('signed-phi115-1170.json')
    path.write_text(json.dumps(cert,indent=2)+'\n')
    print('Complete R interval:',qstr(reduced.lo),qstr(reduced.hi))
    print('Actual width:',qstr(reduced.hi-reduced.lo),'required <=1/50.')
    print('Checks:',sum(checks.values()),'/',len(checks),'failures:',cert['failures'])
    print('Certificate:',path.relative_to(Path.cwd()))
    raise SystemExit(bool(cert['failures']))


if __name__=='__main__':
    main()
