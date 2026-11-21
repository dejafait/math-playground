# Fixed-dictionary continuum test1571 — enclosure-limited attempt

Approved target: assessment1570, unchanged. Main gap: L030-L032/C032a
actual-Xi all-degree positivity. Seek a q from its fixed dictionary with
uniform residual strictly below 1/2 on [1,2]. This could exclude only
mass-one positive-output annihilators of variation at most 2. Full odd
cancellation, unrestricted variation and unsmoothed Xi realization remain
unresolved. Stop after the two prescribed grids and bounded validation;
do not add frequencies, widths, cancellation orders or variation budgets.

The retained inputs contain no certified individual zero coordinates.
This attempt therefore uses the coarse verified-through-100, first-zero,
counting and tail inputs from calculation1564, with C032m's actual
Gaussian/primitive definitions. No guessed zero coordinate is inserted.
The intended exact rational box calculation distinguishes an error barrier
of these enclosures from a lower bound for the actual dictionary.

Checkpoint before calculation: C032q's pairing gives integral q deta>=0
for a feasible eta. Thus integral(1+q)deta>=1, while its absolute value is
at most 2||1+q||. The required strict residual would contradict feasibility.
No such residual has yet been computed. All fixed-v1, divisor,
multiplicity, strip, zero-ordinate, finite-zero and heat qualifications
remain in force; no density, moments or profile positivity is assumed.

## Outcome and meaning

The completed exact rational calculation is
`scripts/smoothed-law/bounded_variation_dual_1571.py`; its full output is
`scripts/smoothed-law/bounded_variation_dual_1571.json`. The uniform
residual upper bound is rho=1-g, with

    g approximately 1.40971634415*10^(-43),
    999/1000 < rho < 1.

The exact fractions, rather than this decimal, control every comparison.
This fails to certify the requested strict bound below 1/2. The two
allowed grids have been solved in the conservative interval model below;
no numerical point values of the actual kernels were available. The
enclosures apply to the whole closed width interval, validated as 128
closed cells. This is an inconclusive attempt, not a lower bound for the
true dictionary or an informative negative result about actual feasibility.
The lower bound rho belongs only to the independently varying interval
boxes. Neither actual errors nor actual kernel coordinates can be chosen
independently in this fashion. A later audit is needed before using even
the weak residual estimate as a mathematical input; no lemma is added
for that inadequate estimate and no main argument changes.

## Qualified inputs and effective common envelopes

Use C032m's complete Gaussian series, removable quotient, primitives
and their audited uniform estimates. Its analytic import is Haslinger,
*Complex Analysis*, Section 2.7, Theorem 2.39, pp.67-68,
https://www.mat.univie.ac.at/~has/scriptneu.pdf . The fixed-v1 input is
Sra, *Some positivity properties of Riemann Xi under smoothing*,
2611.00345v1, Lemma A.4, p.13, and Section 3.1, p.5,
https://hexagonmath.org/pdf/2611.00345v1 . Reuse the existing assessments;
no general integration theorem or source-wide positivity proof is reproved.
C032q supplies the cone pairing and bounded nonnegative Laplace tests.

The effective divisor information is exactly calculation1564's input:
N(100)<40, zeros through 100 real in the z coordinate, gamma>14,
at least one gamma in (14,15), and sum_(gamma>100)gamma^(-2)<3/25.
The last bound is C032s (8), from the retained fixed-v1 heat preprint
2610.00584v1, Section 2.1, p.3, (2.1)-(2.3), and Appendix B.1, p.17,
https://hexagonmath.org/pdf/2610.00584v1 . Its explanation cites
Bellotti-Wong (2025), Theorem 1.1. No independent check of finite zero
data or the preprints is asserted. The fixed-v1 source qualifications
are unchanged. In particular verification through 100 is not a table of
individual zero coordinates.

Put beta=3/8, epsilon=10^(-100). For 0<=M<=13/4, gamma>100 gives
gamma-M>=gamma/2, and therefore

    sum_(gamma>100) exp(-(gamma-M)^2/8)
      <=sum_(gamma>100) exp(-gamma^2/32)
      <=(3/25)*100^2*exp(-10000/32)
      <1200*beta^312<epsilon.                         (1)

For the middle inequality, y^2*exp(-y^2/32) decreases for y>=100;
multiply its supremum by the reciprocal-square tail. This accounts
for the full off-line divisor, with multiplicity. It is a uniform
bound, not a claim that individual high-zero summands are positive.
The last rational inequality is checked in the certificate.

Write A_M,c_M,Q,S_G,S_2 as in C032m. Elementary 3<pi<4,
8/3<e<3 and exp(1/16)<16/15 give the following rational upper bounds:

    S2=40/196+3/25,                  S_2<S2,
    SG=40*beta^6+epsilon,            S_G<SG,
    A=3*(40*beta^18+epsilon),        A_2<A,
    Ac=27*(40*beta^14+epsilon),      A_sqrt(10)<Ac,
    c_0<16/45,                      sqrt(8*pi)<6.      (2)

Indeed c_2=exp(25/16)/sqrt(4*pi)<3 and the low-zero exponent
(14-2)^2/8 is 18. For the other disk, sqrt(10)<13/4;
c_(13/4)=exp(225/64)/sqrt(4*pi)<27, and
(14-13/4)^2/8=1849/128>14. Both c_M and the positive sum in A_M
increase with M, so these also bound A_sqrt(10). For S_G use
14^2/32=49/8>6. Equation (1) handles every high-zero sum in (2).

Use the same removable-quotient proof as C032m, but split at x=3
for |w|<=2. On 0<=x<=3 its h' estimate (4)-(6), with U=9,
bounds the quotient by A_sqrt(10)<Ac. For x>=3,
|x^2+w^2|>=x^2-4>=5*x^2/9. C032m (3) with X=3 then gives

    |R_sigma(w)| < B
      :=3*Ac+(9/5)*[(16/45)*(SG/3+12*S2)+A/3],
    |E_sigma(w)| < 8*B < K=21,
    |O_sigma(w)| <=2*pi*|w|*A <8*|w|*A.              (3)

The full expression for B is rational and recorded in the certificate;
K=21 is an upper bound on 8*B, not an effective constant imported from
an existential O estimate. All integrability, series convergence and
primitive identities come from C032m. The only changed detail is this
explicit cutoff and its denominator factor 9/5. This bound includes
w=+/-ix and the origin using the removable portion. It covers every
sigma in [1,2], including endpoints.

## Real interval boxes for the prescribed dictionary

Conjugate symmetry of the actual divisor makes p_sigma real on R.
Its even Taylor coefficients are real. Thus E is even with real
coefficients, O is odd with real coefficients, and kappa_a is real
for real a, whereas kappa_(i*y) is purely imaginary for real y.
No profile positivity is inferred globally.

For x in [0,2], retain just the real zero gamma_* in (14,15).
The positive-centre Gaussian term alone is greater than

    (1/2)*(1/6)*exp(-225/4) > (1/12)*3^(-57).

Here |x-gamma_*|<=15, sigma>=1 and sqrt(4*pi*sigma)<6.
All other zeros through 100 contribute nonnegative real profiles.
The absolute high-zero part is less than 3*epsilon by (1)-(2).
Consequently, on this compact real spatial interval only,

    p_sigma(x)>P:=(1/12)*3^(-57)-3*epsilon>0.          (4)

For y in {1/4,1/2,1,2}, write O_sigma(i*y)=i*theta_sigma(y).
Straight-segment integration in C032m, and evenness of p, give

    theta_sigma(y)=2*pi*integral_0^y p_sigma(x) dx,
    6*y*P<theta_sigma(y)<8*y*A<=16*A<1.

For 0<=theta<=1 the elementary alternating-series inequality
sin(theta)>=theta-theta^3/6>=theta/2 applies. E_sigma(i*y) is real.
Combining (3)-(4) gives the rational boxes

    y*l < Im(kappa_(i*y)(sigma)) < y*u,
    l=3*P*3^(-K),        u=8*A*3^K.                  (5)

For real a in {1/4,1/2,1,2}, |O_sigma(a)|<8*a*A<1 and
|sinh(t)|<=2*|t| for |t|<=1, hence

    -16*a*A*3^K < Re(kappa_a(sigma)) <16*a*A*3^K.    (6)

The other eight real/imaginary components are identically zero.
For each of the four specified Laplace parameters, C032j/q give
0<L_sigma(s)<=1. Equations (3) and 16*A<1 imply |b|<K+1, so

    3^(-(K+1)) < L_sigma(s) <=1.                    (7)

These are deliberately conservative enclosures. They discard both
correlations among columns and width dependence. The script uses them
as stated; it does not mistake them for independent actual kernel
values. No unbounded output test is used. Every coefficient is rational;
the four nonnegative coefficients will all be zero. Rational interval
arithmetic has rounding allowance zero; (1) pays the complete divisor
tail and (3) pays the noncompact primitive. Coefficient multiplication
of every interval radius is explicit, with no hidden kernel tolerance.

## Exact box minimax calculation

On either allowed grid sigma=1+j/n, n=128 or 256, attach the same
whole-width boxes (5)-(7) to each row. Solve the robust finite problem:
minimize the largest residual over all independent values in these
boxes, with arbitrary real odd-kernel coefficients and nonnegative
Laplace coefficients. This is a conservative certificate-generation
problem, not the actual sampled-kernel minimax problem. It has an exact
solution, so no floating optimizer or convergence theorem is invoked.

Set rho=(u-l)/(u+l). For each imaginary column its midpoint is
m_y=y*(u+l)/2 and its radius is rho*m_y. Write t=sum a_y*m_y and
p=sum c_s*m_L for the odd-imaginary and Laplace contributions;
c_s>=0 and m_L>0, so p>=0. The real-axis boxes have zero midpoint.
The worst-case absolute residual in any one independent-box row is
the absolute residual midpoint plus the sum of coefficient-weighted
radii. It is at least

    |1+t+p| + rho*sum |a_y|*m_y
      >= |1+t+p|+rho*|t|
      >= rho*(|1+t+p|+|t|)
      >= rho*(1+p) >= rho.                          (8)

The first step merely drops the nonnegative real-axis and Laplace
radii. The second uses the triangle inequality. The third uses
0<rho<1 and the fourth is again the triangle inequality. Hence this
is a bound for all coefficients in this box model, not just for the
returned candidate. Identically zero columns make no difference.

Equality is attained by the rational function

    q(sigma)=-2/[ (1/4)*(u+l) ]*Im(kappa_(i/4)(sigma)),

with every other coefficient zero. Its residual midpoint is zero
and its radius is exactly rho. Therefore both finite box problems
have exact optimum rho, and the same candidate has certified uniform
residual at most rho on [1,2]. The script enumerates 128 closed width
cells, with both endpoints included, using (5) on each entire cell;
no interpolation or qualitative modulus is substituted for a bound.
No extra solve, frequency, width, jet or variation budget is added.

The script checks rho>999/1000 and rho<1 exactly, and records the
failed target inequality rho<1/2. The certified bound would contradict
no variation-at-most-2 measure: 2*rho>1. It supplies no actual
dictionary lower bound. In particular the box optimum does not exclude
a successful certificate obtained from sharper correlated enclosures.

## Decision and limitations

Stop this bounded numerical attempt as inconclusive. The dominant
error is the coarse finite-divisor/primitive enclosure width, multiplied
by the chosen coefficient; the high-zero disk tail is already below
10^(-100). Repeated grids with these boxes cannot improve the bound,
as (8) shows. This is a limitation of this implemented enclosure method,
not a theorem that retained hypotheses cannot yield sharper estimates.
An alternate direct evaluation with explicit prime/gamma remainders
would be a materially new input and needs source assessment before a
retry; no such formula has been derived or approved this turn.

This is elementary certificate exploration under ready assessment1570,
classified REPRODUCTION. It is not a novel discovery, a positive-output
witness, full cancellation, unrestricted infeasibility, or progress
beyond the checked sources. No complete candidate exists. The exact
rational checks validate arithmetic conditional on the displayed
analytic reductions and external inputs; they do not validate those
external inputs. Full matching Mathlib coverage is unchecked and unknown.
No general solver theorem, new criterion, moment identity or unaudited
C032n evolution formula is imported. The partial estimate is retained
as failed-attempt evidence, not as a new lemma or part of PROOF.md.
