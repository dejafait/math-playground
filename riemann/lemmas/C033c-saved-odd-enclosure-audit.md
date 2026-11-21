# Corollary C033c: saved compact O enclosure, audited specialization

## Hypotheses

Use C032m's actual-divisor normalization and entire primitive, for real
1<=sigma<=2:

    z_rho=gamma_rho-i*delta_rho,
    G_sigma(z)=(4*pi*sigma)^(-1/2)*exp(-z^2/(4*sigma)),
    p_sigma(z)=(1/2)*sum_(rho in Z+)
                     [G_sigma(z-z_rho)+G_sigma(z+z_rho)],
    O_sigma(w)=2*pi*integral_0^w p_sigma(i*t) dt.

Z+ is the actual positive-ordinate nontrivial zeta divisor, with
multiplicity; gamma>14, |delta|<1/2 and N(T)=O(T*log(T+2)). Retain
the no-ordinate-zero convention and the finite-zero, heat, counting
and fixed-v1 qualifications of C032j/m/s. In particular the effective
numerical inputs used here are

    N(100)<40,
    sum_(gamma>100) gamma^(-2)<3/25.                    (1)

Their source-wide correctness and finite-zero data are not independently
verified by this audit. The first-ordinate input supplies gamma>14;
the additional facts that the low zeros are real in the z coordinate
and that some ordinate is in (14,15) are retained qualifications but
are not used in this upper bound. No individual zero coordinates,
profile positivity, RH, lower profile bound, probability-law positivity
or R/E estimate is an operational premise of the O estimate.

## Conclusion

Put b=3/8, epsilon=10^(-100), and

    A=3*(40*b^18+epsilon).

On the entire closed domain 1<=sigma<=2, |w|<=2,

    |O_sigma(w)| <= 8*|w|*A <= 16*A < 1/8192 < 1/16.   (2)

Thus zero is already a conditional uniform approximation to O with
absolute error strictly below 1/16. This audits only the O-relevant
part of calculation1571(1)-(3). It makes a construction whose sole
purpose is that unweighted allowance redundant. It is not a direct
prime-side implementation of C032w, a certificate for its 10000000-term
full procedure, a coefficient-weighted kappa error, or a residual<1/2
certificate for dictionary1570. No positivity or unsmoothed-Xi transfer
follows, and no other part of calculation1571 is audited here.

## Proof

### Imported inputs and scope of the replay

Reuse C032m(1),(8), including its audited straight-segment primitive.
Its integration input is Friedrich Haslinger, *Complex Analysis*,
Section 2.7, Theorem 2.39 and proof, printed pp.67-68,
https://www.mat.univie.ac.at/~has/scriptneu.pdf . C032m has checked the
uniform Gaussian convergence and domination hypotheses. No integration
theorem or admissible-kernel theorem is reproved here. Its fixed-v1
source is Suvrit Sra, *Some positivity properties of Riemann Xi under
smoothing*, 2611.00345v1, Lemma A.4 and proof p.13, Gaussian convention
Section 3.1 p.5, https://hexagonmath.org/pdf/2611.00345v1 .

For (1), reuse the exact count/tail consequences recorded in C032s(8)
and calculation1564: fixed 2610.00584v1, Section 2.1, (2.1)-(2.3),
printed p.3, and Appendix B.1, printed p.17,
https://hexagonmath.org/pdf/2610.00584v1 . The source attributes its
counting input to Bellotti-Wong (2025), Theorem 1.1. No independent
reproof of that theorem or source-wide verification is claimed. In
particular the retained consequence is

    |N(y)-M(y)|<=4+log(y+2)/8,
    M(y)=y/(2*pi)*(log(y/(2*pi))-1).

It gives N(100)<100/3+37/8=911/24<40: use pi>3,
log(100/(2*pi))<3 and log(102)<5. The logarithm comparisons follow
from e>8/3, since (8/3)^3>100/6 and (8/3)^5>102. If the bracket
in M is negative the stated upper bound for M holds immediately;
otherwise bound its two positive factors separately. The tail input is
sum_(gamma>100)gamma^(-2)<=2*(log(100)+1)/100<3/25.
All counts include multiplicity. The finite group is gamma<=100 and
the complementary group is gamma>100, so an ordinate at 100 is covered.

This replay is necessary because a general qualitative compact-disk
bound alone gives no numerical 1/16 allowance. It checks the saved
local constants, not a new analytic mechanism or a result beyond the
assessed sources.

### Full-divisor Gaussian bound

C032m(1), with M=2, states

    sup_(sigma,|z|<=2)|p_sigma(z)| <= A_2,
    A_2=c_2*sum_rho exp(-(gamma_rho-2)^2/8),
    c_2=exp(25/16)/sqrt(4*pi).

Here gamma>14 removes the positive-part notation. The modulus estimate
allows every complex z in the disk and every |delta|<1/2. Explicitly,
its positive exponent is bounded using |Im(z)+/-delta|<=5/2,
1/(4*sigma)<=1/4; its negative exponent uses 1/(4*sigma)>=1/8.
Both inequalities include sigma=1,2. The two Gaussian translates
each have the same sum majorant and their factor 1/2 leaves one copy,
not two. Thus off-line zeros require no extra reality assumption.

Since 25/16<2, e<3 and sqrt(4*pi)>3, we have c_2<9/3=3.
For each gamma<=100, (gamma-2)^2/8>18, so its summand is
less than e^(-18)<b^18. There are fewer than 40 such occurrences,
with multiplicity. For gamma>100, gamma-2>=gamma/2, giving

    sum_(gamma>100) exp(-(gamma-2)^2/8)
      <=sum_(gamma>100) exp(-gamma^2/32)
      <=(3/25)*100^2*exp(-10000/32)
      <1200*b^312<epsilon.                            (3)

For the middle bound, y^2*exp(-y^2/32) decreases for y>=100,
because its logarithmic derivative is 2/y-y/16<0. Bound that factor
by its value at 100 and sum the reciprocal squares using (1). Since
10000/32=312.5>312 and e>8/3, the next comparison is strict.
For a fully elementary check of the last comparison,

    b^6=729/262144<1/256,
    1200*b^312<1200/2^416<1/2^400<10^(-120)<epsilon.

The last two steps use 1200<2^16 and 2^10>10^3. This bounds the
complete high divisor, including multiplicity and arbitrary allowed
off-line displacements; no high summand is declared positive.
The same tail argument in calculation1571(1) also allows its recorded
0<=M<=13/4, since gamma-M>=gamma/2 for gamma>100, but no larger disk
constant is needed here. We obtain A_2<A, uniformly in sigma.

### Primitive, boundary cases, and exact allowance

The established entire primitive has the exact representation

    O_sigma(w)=2*pi*w*integral_0^1 p_sigma(i*v*w) dv.

For |w|<=2 the whole straight path i*v*w lies in |z|<=2.
Consequently |O_sigma(w)|<=2*pi*|w|*A_2<=8*|w|*A.
For nonzero w the last comparison is strict; at w=0 the integral is
exactly zero and the non-strict form in (2) is valid. No contour,
principal value, removable R quotient, or R/E bound is involved.
The estimate covers every complex direction, |w|=2 and both width
endpoints, with a single width-independent constant.

Finally, b^18<(1/256)^3 and
48*epsilon<1/131072, the latter because
48*131072=6291456<10^100. Hence

    16*A=1920*b^18+48*epsilon
        <15/131072+1/131072=1/8192<1/16.

This proves the exact required comparison. A standalone rational
replay is scripts/smoothed-law/saved_odd_enclosure_audit_1618.py,
with full certificate
scripts/smoothed-law/saved_odd_enclosure_audit_1618.json.
Run it with python3 from this notebook. It also checks equality with
the saved A2 fraction in certificate1571. The certificate verifies
rational arithmetic only; the preceding proof justifies the analytic
reductions and does not certify the external source inputs.

The relevant downstream error in dictionary1570 also depends on E,
coefficient amplification and actual residual control. None is bounded
by an unweighted 1/16 estimate for O. Independent signed cancellation
and actual-Xi realization gaps remain unresolved.

## Mathlib

Full matching coverage is unchecked and unknown. No Mathlib theorem
is invoked. Gaussian/Cauchy, integration and rational arithmetic APIs
could support parts, but no coverage of this full conditional numerical
specialization or its fixed-v1 inputs has been established. This is
reproduction of a saved specialization using cited tools, not a
claim of new general mathematics or a verified RH input beyond scope.
