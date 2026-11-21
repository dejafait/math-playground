# L762 — effective periodic boundary trace of the exact CCM trial

## Hypotheses

Fix lambda=sqrt(13), L=log(13), c=26pi, and the exact modes and signs
of L761. Thus psi_0,psi_4 are real unit L2(-1,1) angular modes,
phi_n(t)=lambda^(-1/2)psi_n(t/lambda) on [-lambda,lambda], extended
by zero, I_n=int phi_n(t)dt, and

    h(t)=I_4 phi_0(t)-I_0 phi_4(t),
    k(u)=sqrt(u) sum_(r>=1) h(ru),  lambda^-1<=u<=lambda.

At support boundaries, h and its derivatives in the formulas below mean
the inward values of this analytic combination, not derivatives of its
zero extension. Use L761's certified chi_0<82, chi_4<726,
J_0>1.187, J_4>0.720 and
|I_n-J_n|<=sqrt(2lambda)epsilon_n, with epsilon_0<2.645*10^-97,
epsilon_4<4.034*10^-93. Their audited numerical arithmetic trust
assumptions are inherited. No new numerical certificate is required here.

Step378 separately audited the full analytic specialization and its
elementary constants; section5 records the checks and their scope.
The inherited L761 spectral/interval computation was not rerun.

For any integer N>=1 extend exactly the translated basis and boundary
row of L761 and L760:

    V_j(u)=L^(-1/2) exp(2pi i j log(lambda*u)/L), |j|<=N,
    a_j=<V_j,k>,  P_N k=sum_(|j|<=N) a_j V_j,
    b_N(a)=L^(-1/2) sum_(|j|<=N) a_j.

Inner products are conjugate linear in the first argument. Below
b(P_N k) means b_N(a). It is an evaluation of a finite polynomial,
not an assumed bounded trace on L2. No variable-N ground matrix,
ground eigenvector, inversion parity or denominator nonvanishing is assumed.

The source inputs are the periodic piecewise-smooth convergence theorem
of [Lebl, Notes on Diffy Qs, section4.3.2, Theorem4.3.1](https://www.jirka.org/diffyqs/html/moreonfourier_section.html),
the Bernoulli jump model in [Batenkov, Math.Comp.84(2015),2329–2350,
section2, Proposition6/(2.2), pp2330–2331](https://dimabatenkov.info/pdf/batenkov_complete.pdf),
and [DLMF24.8.2–3](https://dlmf.nist.gov/24.8).
For the modes use [Osipov–Rokhlin, arXiv:1301.1707v1,
Theorem1/(27), Theorem3/(38), Remark6](https://arxiv.org/html/1301.1707v1#S3.SS1):
the unit modes satisfy the finite-Fourier identity with nonzero
eigenvalue and extend to entire functions. Only this regularity and the
identity, not the further assertions about roots, are used here.
The source jump method is specialized, not claimed as new. Its generic
O-constant does not supply the explicit bound below; that is why the
normalizations, integrations and constants are given in full.

## Conclusion

Set

    M=(lambda^(-1/2) sum_(r=1)^12 h(r/lambda)
                          +sqrt(lambda)h(lambda))/2.

For every integer N>=1,

    |b(P_N k)-M| <= A/(N+1) + L V/(2pi^2 N) < 34000000/N.       (1)

Here A and V are the following exact nonnegative finite quantities,
with effective upper bounds A<57200 and V<200000000. Put
alpha_r=log(13/r) for r=2,...,12, and define the value jumps

    Delta_0=lambda^(-1/2) sum_(r=1)^12 h(r/lambda)
                                           -sqrt(lambda)h(lambda),
    Delta_r=-sqrt(lambda/r)h(lambda),                       2<=r<=12,

and the first-derivative jumps in logarithmic coordinates

    E_0=lambda^(-1/2) sum_(r=1)^12
                       [h(r/lambda)/2+(r/lambda)h'(r/lambda)]
                     -sqrt(lambda)[h(lambda)/2+lambda h'(lambda)],
    E_r=-sqrt(lambda/r)[h(lambda)/2+lambda h'(lambda)],      2<=r<=12.

For F(x)=k(e^x/lambda), 0<x<L, let F''_pw denote its ordinary
second derivative separately on the open smooth pieces. Then

    A=(1/pi) sum_(r=2)^12 |Delta_r|/sin(pi alpha_r/L),
    V=|E_0|+sum_(r=2)^12 |E_r|+int_0^L |F''_pw(x)|dx.        (2)

In particular b(P_N k) tends to the periodic midpoint M, not in
general to either assigned endpoint value. Section3 gives the exact
finite jump-model sum and retains the mean explicitly. The r=13 term
does not enter M or any coefficient because it lives at one point only.

This is local progress by reproduction of an assessed standard method.
It gives no lower bound for |M|, no ground/trial comparison and no
family or lambda-limit assertion. At N=120 the coarse bound is
283333+1/3, whereas C761a's finite denominator is about4.73*10^-29;
there is no useful denominator control at that scale. C761a's
discrepancy>0.48616>1/10 is unchanged. No Xi sign or RH follows.

## Proof

### 1. Effective bounds for the exact modes and inward derivatives

The imported source identity is, writing nu_n for its finite-Fourier
eigenvalue to distinguish it from lambda and chi_n,

    nu_n psi_n(x)=int_(-1)^1 psi_n(t) exp(i c x t)dt.          (3)

Nonzero nu_n and compact integration give the entire continuation and
justify differentiation by an integrable bound on each compact x-set.
For real x and m=0,1,2, Cauchy–Schwarz therefore gives

    |psi_n^(m)(x)| <= c^m sqrt(2/(2m+1))/|nu_n|.             (4)

We must bound the denominator effectively; nonzero alone is insufficient.
L761 and sqrt(2lambda)<3 give |I_n-J_n|<1/1000 for n=0,4.
Consequently I_0,I_4>7/10 in the specified signs. Since sqrt(lambda)<2,

    int_(-1)^1 psi_n = I_n/sqrt(lambda) > 7/20.              (5)

The differential equation in the source is H_c psi_n=chi_n psi_n.
The entire continuation makes psi_n and psi_n' bounded on [-1,1].
Multiplying by psi_n and integrating by parts, the boundary term
(1-x^2)psi_n psi_n' vanishes at both endpoints, so

    int_(-1)^1 (1-x^2)|psi_n'|^2
              +c^2 int_(-1)^1 x^2|psi_n|^2 = chi_n <726.    (6)

Thus int_(-1/2)^(1/2)|psi_n'|^2 <(4/3)726. On this interval of
length1 there is y with |psi_n(y)|<=1, since the full L2 norm is1.
Cauchy–Schwarz on the segment from y to0 now proves

    |psi_n(0)| <=1+sqrt(1/2)||psi_n'||_L2(-1/2,1/2)<23.

Equation(3) at zero and (5) imply |nu_n|>7/460>1/100.
In particular none of the divisions in (4) rests on an existential
nonvanishing assertion or a trace of an L2 approximation.

Unit norm of phi_n implies |I_n|<=sqrt(2lambda). Scaling (4) and
using both terms in h gives the explicit inward bounds

    |h^(m)(t)| <= 400(c/lambda)^m/sqrt(2m+1)
               <=400(c/lambda)^m,   |t|<=lambda, m=0,1,2.   (7)

For later simple constants use sqrt(lambda)<2, L<3, and c<82
(the last follows from pi<22/7). These deliberately loose bounds
avoid any unverified pointwise use of L761's polynomial error.

### 2. Complete seam and cutoff data

Let u=e^x/lambda and, where ru<=lambda, set

    g_r(x)=sqrt(u)h(ru),  alpha_r=log(13/r), 1<=r<=12.

Almost everywhere in 0<x<L,

    F(x)=sum_(r=1)^12 g_r(x) 1_(0,alpha_r)(x),
    alpha_1=L.

For x>0 the r=13 term has ru>lambda and is zero; at x=0 it is
supported at one assigned point. Higher r have no support. The eleven
numbers alpha_12<...<alpha_2 lie strictly between0 andL. Every smooth
piece extends analytically past its closed endpoints by section1.
At alpha_r exactly the rth term disappears. At the seam the left
periodic limit is the limit at L from below. Consequently

    F(0+)=lambda^(-1/2) sum_(r=1)^12 h(r/lambda),
    F(L-)=sqrt(lambda)h(lambda),

and the right-minus-left value jumps are exactly Delta_0,Delta_r
listed in the conclusion. This includes r=1 through the seam;
r=13 creates no inward jump and must not be added to Delta_0.

Writing t=ru, ordinary differentiation of one piece gives

    g_r'(x)=sqrt(u)[h(t)/2+t h'(t)],
    g_r''(x)=sqrt(u)[h(t)/4+2t h'(t)+t^2 h''(t)].            (8)

The same one-sided subtraction gives exactly E_0,E_r in (2).
These are jumps of the piecewise first derivative, not distributional
derivatives with their value-jump atoms silently removed. Both sorts
of jumps are accounted for separately below.

As 0<u<=lambda and t<=lambda on each contributing interval, (7) gives

    |g_r|<800,
    |g_r'|<800(1/2+82)=66000=:G_1,
    |g_r''|<800(1/4+2*82+82^2)=5510600=:G_2.               (9)

The seam derivative jump has at most13 such terms; the eleven
interior jumps contribute at most11 more. The piecewise integral
satisfies, by the triangle inequality on the finite partition,

    int_0^L |F''_pw| <=sum_(r=1)^12 int_0^(alpha_r)|g_r''|
                      <12L G_2<36G_2.

Therefore

    V <24G_1+36G_2=199965600<200000000.                     (10)

No derivative across a cutoff was used in this integral estimate.

### 3. Normalization, mean and the exact Bernoulli subtraction

Define ordinary period-L Fourier coefficients

    Fhat_j=(1/L)int_0^L F(x)exp(-2pi i jx/L)dx.

The change du/u=dx gives a_j=sqrt(L)Fhat_j. Hence exactly

    b(P_N k)=sum_(|j|<=N) Fhat_j.                          (11)

The realness of F gives conjugate coefficients; it does not justify
discarding their imaginary parts or imposing inversion parity. Its mean is

    Fbar=Fhat_0=(1/L)sum_(r=1)^12 r^(-1/2)
                              int_(r/lambda)^lambda h(t)t^(-1/2)dt. (12)

This weighted, truncated mean need not vanish even though int h=0.

For alpha on the circle define the period-L sawtooth

    B_alpha(x)=1/2-{(x-alpha)/L}  when x!=alpha modulo L,
    B_alpha(alpha)=0  (the midpoint convention).

It is minus the periodic B1 polynomial, has mean0 and a right-minus-left
jump+1. By the cited Bernoulli formula its nonzero Fourier coefficient is
exp(-2pi i j alpha/L)/(2pi i j). DLMF's B1 identity has an open-interval
restriction; the assigned value0 at the jump here is the periodic midpoint
from Lebl's theorem, not an endpoint substitution into that identity.
Set

    Phi(x)=Delta_0 B_0(x)+sum_(r=2)^12 Delta_r B_(alpha_r)(x).

Then R=F-Phi extends continuously and periodically using midpoint
values. In particular

    Phi(0)=sum_(r=2)^12 Delta_r(alpha_r/L-1/2),
    R(0)=M-Phi(0),  Rhat_0=Fbar.                           (13)

For completeness the piecewise integration which makes the constant
effective is recorded. Write omega_j=2pi j/L. For j!=0, integration
by parts on every piece, with periodic endpoint phases equal to1, gives

    Fhat_j=(Delta_0+sum_(r=2)^12 Delta_r exp(-i omega_j alpha_r))
                  /(L i omega_j)
           +(1/(L i omega_j))int_0^L F'_pw(x)exp(-i omega_j x)dx.

The first term is Phihat_j. Integrating the last integral piecewise
once more yields the exact identity

    Rhat_j=[E_0+sum_(r=2)^12 E_r exp(-i omega_j alpha_r)
                 +int_0^L F''_pw(x)exp(-i omega_j x)dx]
                    /(L(i omega_j)^2).                    (14)

Thus |Rhat_j|<=L V/(4pi^2 j^2). The derivative jumps remain even
after the value jumps have been removed. Equivalently, the extra constant
slope in R'=F'_pw+(Delta_0+sum Delta_r)/L has zero nonzero-frequency
coefficient, leaving (14) unchanged.

Combining the positive and negative modes of Phi in (11) gives the
exact finite jump-model formula

    b(P_N k)=Fbar
       -(1/pi)sum_(r=2)^12 Delta_r sum_(j=1)^N sin(2pi j alpha_r/L)/j
       +sum_(1<=|j|<=N) Rhat_j.                            (15)

In particular the seam jump was not discarded: its symmetric partial
sum at its own jump is identically0, and its midpoint is0. Its effects
on R and the mean are already retained by (12)–(14).

### 4. Effective tails and their limits

The finite partition and analytic one-sided pieces meet Lebl4.3.1's
piecewise-smooth hypotheses. At the seam its theorem identifies the
Fourier limit of F as M; R's limit is its continuous value R(0).
The bound from (14) also proves absolute convergence of R's tail and

    |sum_(|j|<=N) Rhat_j-R(0)|
        <=(L V/(2pi^2))sum_(j>N)1/j^2 <=L V/(2pi^2 N).     (16)

For theta not a multiple of2pi the finite geometric-sum identity gives

    |sum_(j=p)^q exp(i j theta)|<=1/|sin(theta/2)|.

Summation by parts with the decreasing weights1/j, followed by the
limit q->infinity, therefore proves the conditional, not absolute, bound

    |sum_(j>N) exp(i j theta)/j|
                  <=1/((N+1)|sin(theta/2)|).               (17)

Indeed the weighted finite-sum bound is at most B/(N+1) when all
partial sums beginning at N+1 have modulus<=B; convergence follows
by applying the same estimate to arbitrarily late starting indices.
Take imaginary parts and theta=2pi alpha_r/L. Each alpha_r is strictly
inside(0,L), so every denominator is positive. At the seam use the
exact symmetric cancellation noted above rather than (17).
The Bernoulli series consequently gives

    |sum_(|j|<=N) Phihat_j-Phi(0)|<=A/(N+1).               (18)

Equations(13), (16) and (18) prove the first inequality in (1).

Here is an entirely elementary effective upper bound for A. For
0<=t<=1, concavity on each half-interval gives
sin(pi t)>=2min(t,1-t). For 2<=r<=12,

    min(alpha_r/L,1-alpha_r/L)
       =min(log(13/r),log r)/L >=log(13/12)/L >1/39.

The last strict inequality uses L<3 and
log(13/12)=int_0^(1/12)(1+s)^(-1)ds>=1/13.
Thus sin(pi alpha_r/L)>2/39. Also |Delta_r|<800 by (9), and pi>3.
There are exactly eleven such jumps, so

    A<11*800*39/(2*3)=57200.

Together with (10), L<3 and pi^2>9 this gives

    |b(P_N k)-M|<57200/(N+1)+100000000/(3N)<34000000/N.

This proves all asserted constants for every integer N>=1. Only
standard geometric sums and elementary arithmetic were needed in addition
to the imported Fourier/prolate facts and L761's certified mode data.
No numerical preview, pointwise approximation certificate, interchange of
an uncontrolled infinite arithmetic sum, or assumption on zeros is used.

### 5. Separate conceptual audit (step378, 2026-11-04)

This audit uses the previously approved SPECIALIZE assessment
`drafts/literature/2026-11-04-ccm-periodic-trace-audit.md`. It is
REPRODUCTION of the stated source-method specialization. All claims in
(1)–(18) survive; no estimate, onset, sign convention or hypothesis is
weakened. The source statements and their essential cases are reused
from that assessment. The check below is of their application, not a
new import of the whole conclusion from a general Fourier theorem.

**Exact functions and the finite-Fourier denominator.** L761 identifies
the continuous-endpoint angular realization, the mode indices and
their independent real signs. Its positive integrals give I_n>7/10
for both modes after the stated integral error, hence (5). The entire
source mode is used in the ODE integration: multiplying the equation
by the real mode gives (6), since the factor 1-x^2 kills both bounded
endpoint products. In particular the derivative energy on [-1/2,1/2]
is <968. Unit norm supplies a point y on this interval with
|psi_n(y)|<=1, and the segment from y to zero has length<=1/2.
Its Cauchy–Schwarz cost is <sqrt(968/2)=22, giving |psi_n(0)|<23.
The integral identity at zero then gives

    |nu_n| |psi_n(0)| = int psi_n >7/20,
    |nu_n| >7/460 >1/100.

The same identity excludes psi_n(0)=0. Differentiation under its compact
integral has an integrable uniform majorant on each complex compact
set. For real x, |exp(i cxt)|=1, so the Cauchy–Schwarz norm is exactly
sqrt(2/(2m+1)). Scaling each derivative by lambda^(-m-1/2), and using
|I_n|<=sqrt(2lambda) in both summands of h, gives the factor400 in (7).
Thus no evaluation of the L2 approximation error, nor an assumed
quantitative version of source nonvanishing, enters the argument.

**Every jump and the mean.** In the open logarithmic interval, exactly
the summands r=1,...,12 occur, on 0<x<alpha_r. The r=13 term is confined
to x=0 and affects no coefficient or one-sided limit. The limit at L
contains only r=1. Each of the eleven interior right-minus-left jumps
removes one g_r; the periodic seam subtracts the limit at L from the
limit at zero. Applying these subtractions also to
g_r'=sqrt(u)(h/2+t h') verifies all Delta and E formulas, including
their signs. A second derivative is sqrt(u)(h/4+2t h'+t^2 h''),
so (9) has no missing middle term. There are13 possible derivative
contributions at the seam and11 at interior jumps. The twelve separate
open support integrals bound the ordinary second derivative; no
distributional jump is counted as part of that integral.

The change of variable dx=du/u gives a_j=sqrt(L) Fhat_j and removes
exactly the boundary row's reciprocal sqrt(L). Changing variables
t=ru separately in the constant coefficient gives (12), with weight
r^(-1/2)t^(-1/2). The zero additive integral of h does not cancel it.
Assigned values at all cutoffs may be replaced by their midpoints
without changing any Fourier coefficient.

**Two integrations and conditional convergence.** On a smooth piece,
integration by parts contributes its left value minus its right value,
divided by i omega_j. Summing over pieces therefore gives right-minus-left
jumps with the positive numerator in (14). Repeating this operation
on the ordinary first derivative retains E_0 and every E_r, as well
as the integral of F''_pw. Subtraction of the value-jump model removes
only the first such boundary term. Its constant slope has zero
nonzero-frequency integral, so it creates no omitted term in (14).

For B_alpha the coefficient is exp(-i omega_j alpha)/(2pi i j).
Pairing j and -j produces -sin(omega_j alpha)/(pi j), confirming
(15)'s sign. At alpha=0 each pair cancels; the same sawtooth has
midpoint0 there. At 0<alpha<L its value at zero is alpha/L-1/2.
Consequently (13) retains the exact midpoint, including the seam.
Lebl's theorem applies to the finite analytic partition; R has matching
one-sided values and hence a continuous periodic representative. Its
j^(-2) bound is summable, and its Fourier value at zero is R(0).

For the remaining sawtooth tail, put m=N+1 and
S_k=sum_(j=m)^k exp(i j theta). Geometric summation bounds each S_k
by B=1/|sin(theta/2)|. The finite summation-by-parts identity is

    sum_(j=m)^q exp(i j theta)/j
       =S_q/q+sum_(j=m)^(q-1) S_j(1/j-1/(j+1)).

Its modulus is <=B/m. Applying this to later starting indices proves
convergence, and then gives (17); absolute convergence is neither
asserted nor needed. Each interior alpha_r lies strictly in (0,L),
whereas the seam is handled by exact symmetric cancellation. Finally
sum_(j>N)j^(-2)<=1/N proves (16). These estimates hold for every
integer N>=1, without a limiting exchange between N and a parameter.

**Constants and scope.** The sine lower bound is valid on both halves
of [0,1]. For all eleven r, both log(13/r) and log r are at least
log(13/12)>1/13; dividing by L<3 gives the strict margin >1/39.
Using c<82 and pi>3 yields exactly

    G_1=66000,  G_2=5510600,
    24G_1+36G_2=199965600<200000000,
    11*800*39/6=57200,
    57200+100000000/3=100171600/3<34000000.

These rational arithmetic checks can be reproduced with

    python3 scripts/spectral-triples/periodic-trace-audit-378.py

The complete arithmetic certificate is
`scripts/spectral-triples/periodic-trace-audit-378.json`. It checks
only these constants, the energy square and the denominator comparison;
the preceding analytic reasoning and inherited L761 hypotheses remain
essential. It neither samples N nor replays the spectral certificate.
The all-N slack is 1828400/3 after replacing 1/(N+1) by 1/N.
There are no failed checks or changed bounds.

The verified midpoint is not certified nonzero. The error at N=120
is still far too large for a relative denominator estimate. C761a's
fixed-cell discrepancy and its preserved failures remain contrasts,
not premises. Ground/trial agreement, family uniformity, both limiting
questions and actual-Xi positivity remain open. This audit validates
an existing local input and claims no result beyond the source methods.

## Mathlib

Full matching coverage and supporting periodic Fourier, Bernoulli and
prolate results were not checked. No Mathlib theorem is an input.
Unknown coverage is not absence. The separate analytic and elementary
arithmetic audit is recorded in section5; it does not change Mathlib
coverage or the inherited software trust assumptions.
