# Corollary C034d: adjoint cutoffs and a negative rational bulk kernel

## Hypotheses

Use C034c's exact functions and all its qualifications, with Gaussian
half-variance sigma in [1,2] and the parameter neighborhood (1/2,3).
Suppress sigma and write spatial derivatives with primes. Explicitly,

    G_sigma(z)=exp(-z^2/(4*sigma))/sqrt(4*pi*sigma),
    p(x)=(1/2)sum_rho[G_sigma(x-z_rho)+G_sigma(x+z_rho)],
    z_rho=gamma_rho-i*delta_rho,
    Q_j(x)=4*j*(3*x^2+j)/(x^2*(x^2+j)^2), j=1,2,
    A=p-p(0), B=p''-p''(0),
    d_j=int_0^infinity A Q_j, e_j=int_0^infinity B Q_j,
    D=Q_2-Q_1, h=d_2-d_1, C=d_1*e_2-d_2*e_1,
    S4=sum_rho gamma_rho^(-4).

The actual positive-ordinate divisor includes every multiplicity and
conjugate, has gamma>14 and |delta|<1/2, and satisfies
N(T)=O(T log(T+2)). Retain the excluded ordinate zero, verified zeros
through100, retained real zero in (14,15), reciprocal-square tail,
heat positivity and separate fixed-j errors, both fixed-v1 preprint
qualifications, zero drift/killing and C033w's probability interpretation
through C034b. Their source-wide/finite-zero validity is not independently
verified here. The calculation uses C032n's heat identity, evenness,
uniform Gaussian majorants and boundary growth; it does not require
nonnegative p, RH, or global Sobolev membership for p.

## Conclusion

Put V(x)=p(x)-p(0)-p''(0)*x^2/2. The integrals in (27)-(28) are
ordinary absolutely convergent integrals, uniformly in width, and
permit absolute summation over every independent divisor pair:

    int_0^infinity D=0,
    h=int_0^infinity p D,
    partial_sigma h=int_0^infinity p D''=int_0^infinity V D'',
    e_j=int_0^infinity V Q_j'',                         (27)
    C=int_0^infinity int_0^infinity
           A(x)V(y)[Q_1(x)D''(y)-D(x)Q_1''(y)] dx dy.  (28)

The quadratic subtraction in V is essential to this convergent
transfer of the singular Q_j. No individual divergent term in V Q_j''
is assigned a finite part.

For x,y>=1 the explicit symmetric rational kernel

    K(x,y)=(Q_1(x)Q_2''(y)+Q_1(y)Q_2''(x)
                 -Q_2(x)Q_1''(y)-Q_2(y)Q_1''(x))/2    (29)

is strictly negative. To state the resulting bound without omitting
the origin, define finite real quantities

    U_j=int_1^infinity p Q_j, W_j=int_1^infinity p Q_j'',
    alpha_j=int_0^1 A Q_j-p(0)*int_1^infinity Q_j,
    beta_j=int_0^1 B Q_j-p''(0)*int_1^infinity Q_j
                         -p'(1)Q_j(1)+p(1)Q_j'(1),
    R=U_1*beta_2-U_2*beta_1+alpha_1*W_2-alpha_2*W_1
                                  +alpha_1*beta_2-alpha_2*beta_1.

Writing p_+=max(p,0), p_-=max(-p,0), one has the signed bound

    C=int_1^infinity int_1^infinity p(x)p(y)K(x,y) dx dy+R
      <=R+2*int_1^infinity int_1^infinity
                         p_+(x)p_-(y)*(-K(x,y)) dx dy. (30)

The achieved bound (30) isolates contributions with opposite profile
signs and the exact origin/cutoff correction. To obtain C034c(20), its
right side would need to be <=S4^3/5 for every width. That comparison
is NOT established. Thus the bounded attempt1847 supplies a local
signed kernel reduction, passing conceptual audit1849 below, and
parks this transfer as a closure mechanism without a new estimate of
those remaining terms. It proves neither T<0 nor an actual zero of T,
ECT, conditioning, exact weights, TV<=2, full observations, signed-height
cancellation or actual-Xi realization.

## Proof

### Source scope and reason for the specialization

Reuse the pre-invocation EXPLORE assessment1846 and its primary-source
comparison. The general Gaussian heat identity is imported through
C032n from James Nolen, *Partial Differential Equations and Diffusion
Processes*, Section2.3, (3.17), P0-P1, pp14-17,
[primary notes](https://math.stanford.edu/~ryzhik/STANFORD/STANF227-10/notes227-09.pdf).
C032n already justifies its complex-shift, divisor-sum and width
specializations, including the origin value. Its estimates, rather
than a new general heat theorem, are used below.

Stéphane Nonnenmacher, *Introduction to Spectral Theory*, September2021,
Section3.1.1, Example3.1.12 and complete boundary proof, printed p29,
[primary notes](https://www.imo.universite-paris-saclay.fr/~nonnenma/enseign/Spectral%20Theory%202021%20chap1-4.pdf),
identifies the half-line Neumann Laplacian on H2 functions with zero
derivative trace. Global membership of p in this domain is unproved,
and Q_1 is singular. We therefore do not apply that operator theorem.
Finite-interval integration by parts with the explicit estimates below
is required to justify this particular transfer. This is not a reproof
of the general adjoint result. No DLMF evaluation or uninspected source
is needed. C034c already supplies the product-integral framework and
its absolute summability conditions; the new work is the cutoff
specialization and the rational sign in (29), not a new general
determinant or covariance identity. Originality is not asserted.

### Exact cancellations and finite-cutoff transfer

Partial fractions give, for j=1,2,

    Q_j=4/x^2-4/(x^2+j)+8*j/(x^2+j)^2,
    D=-4*d/dx [x/((x^2+1)(x^2+2))].                   (31)

The rational primitive vanishes at zero and infinity, so int D=0.
The function D is smooth and even, D'(0)=0, and its first two
derivatives decay respectively as O(x^-5) and O(x^-6); D=O(x^-4).
Consequently ordinary integration by parts also gives

    int D''=0, int x^2 D''=2*int D=0.                 (32)

All three integrals in (32) converge absolutely. The boundary terms
are D'(0)=0, x^2 D' and x D at zero and infinity, all zero.
This justifies removing the origin constant from int A D; it does
not justify removing that constant from int A Q_j.

Evenness and compact fourth-derivative bounds give V=O(x^4) and
V'=O(x^3) near zero, uniformly on [1/2,3]. Also V''=B. Twice
integrating by parts on [epsilon,M] gives exactly

    int_epsilon^M B Q_j
       =[V'Q_j-V Q_j']_epsilon^M+int_epsilon^M V Q_j''.

Near zero Q_j=O(x^-2), Q_j'=O(x^-3), Q_j''=O(x^-4), so the
boundary terms are O(epsilon), and V Q_j'' is bounded. At infinity
Q_j=O(x^-4), Q_j'=O(x^-5), Q_j''=O(x^-6).
C032n(13) gives p,p'=O((x+1)log(x+2)); hence both terms at M
vanish even with the quadratic subtraction in V. The integral at
infinity is absolute by C032n(8)-(9): |V| is bounded by a constant
times P(x)+1+x^2, and int_1^infinity P(x)/x^2 is finite.
This proves e_j=int V Q_j''.

The same cutoff argument for D has even smaller origin boundary
terms and gives int B D=int V D''. C034c proves partial_sigma h
=e_2-e_1=int B D, retaining partial_sigma p(0)=p''(0).
Now (32) gives int V D''=int p D''. This proves (27), including
both width endpoints, without presuming an L2 adjoint domain.

For absolute divisor exchanges write

    u_rho(x)=Re([G_sigma(x-z_rho)+G_sigma(x+z_rho)]/2),
    A_rho=u_rho-u_rho(0),
    V_rho=u_rho-u_rho(0)-u_rho''(0)*x^2/2.

Conjugation invariance gives p=sum u_rho with every multiplicity.
C032n(8) makes the sum of suprema of |u_rho''''| on [0,1] finite,
uniformly in width. Taylor's integral remainder gives
|V_rho(x)|<=x^4 sup_[0,1]|u_rho''''|/24 there. On x>=1 the sum
of |V_rho(x)| is bounded by c P(x)+c_0+c_2 x^2, where c_0,c_2
are finite sums of absolute origin values. Therefore

    sum_rho int |V_rho| (|Q_1''|+|Q_2''|)<infinity.    (33)

C034c(21) gives sum_rho int |A_rho| Q_1<infinity, and
|D|<=Q_1. Bound |D''| by |Q_1''|+|Q_2''| in (33).
The sum of absolute double integrals in (28) is thus bounded by
twice the product of these finite sums. Tonelli and then Fubini
justify every independent divisor pair, including diagonal pairs.
All dominators are uniform in width. The boundary growth argument
also applies to sums of absolute member values. No truncation in
ordinate or conditional rearrangement has been made.

Finally C=d_1*(e_2-e_1)-h*e_1. Substitute (27), d_1=int A Q_1
and h=int A D, and factor the absolutely convergent products. This
is (28). The resulting representation is an identity; the sign test
still has to be performed.

### A signed test for the rational kernel

Let t=x^2>0. Direct differentiation of (31) gives

    Q_j''(x)=24*j*(10*t^3+5*j*t^2+4*j^2*t+j^3)
                              /(t^2*(t+j)^4)>0.       (34)

Define r(x)=Q_2/Q_1, ell(x)=Q_1''/Q_1 and s(x)=Q_2''/Q_1''.
As functions of t these are

    r=2*(3*t+2)*(t+1)^2/((3*t+1)*(t+2)^2),
    ell=6*N(t)/F(t),
    s=2*(10*t^3+10*t^2+16*t+8)*(t+1)^4
                                      /(N(t)*(t+2)^4),
    N(t)=10*t^3+5*t^2+4*t+1,
    F(t)=t*(t+1)^2*(3*t+1).

C034c(26) gives r'/r, with t derivative having numerator
15t^2+9t-2>0 for t>=1. Moreover

    (d ell/dt)=-6*(1+10*t+36*t^2+48*t^3+21*t^4
                              +30*t^5+30*t^6)/F(t)^2<0,
    s-r=2*(t+1)^2*P_5(t)/(N(t)*(t+2)^4*(3*t+1)),
    P_5(t)=4*t+12*t^2-43*t^3-114*t^4-55*t^5.

For t=1+u, u>=0, the exact shifted polynomial is

    P_5(1+u)=-196-832*u-1351*u^2-1049*u^3-389*u^4-55*u^5<0.

Thus r increases, ell decreases, and s<r on x>=1. Substitution
in (29) gives the exact decomposition

    2K(x,y)/(Q_1(x)Q_1(y))
      =(ell(y)-ell(x))*(r(y)-r(x))
          +ell(y)*(s(y)-r(y))+ell(x)*(s(x)-r(x)).       (35)

The first term is nonpositive for every pair x,y>=1; each of the
last two is strictly negative by (34). This proves K<0 throughout
the closed quadrant, including its diagonal and edges. For example,
K(1,1)=-784/27. No claim is made about a signed profile's product.

The exact polynomial coefficients are independently reproduced by
`python3 scripts/smoothed-law/laplace_adjoint_algebra_1847.py`.
The full small certificate is
`scripts/smoothed-law/laplace_adjoint_algebra_1847.json`; its complete
load-bearing coefficient arrays were inspected. All four exact checks
pass. This checks the displayed algebra only, not the analytic
argument, inherited sources or the required curvature threshold.

### Origin correction, achieved bound and stopping point

Separate each original d_j integral at1; this gives d_j=U_j+alpha_j.
Integrating the un-subtracted p'' Q_j only on [1,M] and retaining
its lower boundary gives e_j=W_j+beta_j. The terms at M vanish by
the already proved boundary bounds. Both expressions over [0,1]
retain their origin subtractions. All U_j,W_j,alpha_j,beta_j are
absolutely convergent linear divisor sums under the same majorants.
Expanding their products, with no omitted cross or diagonal pairs,
gives C=U_1 W_2-U_2 W_1+R.

The bulk product difference is int int p(x)p(y)K(x,y) by Fubini
and symmetry. Each expanded absolute product is finite because
int_1^infinity |p|Q_j and int_1^infinity |p|Q_j'' are finite.
In particular the same is true with p_+ or p_-. Expanding
p=p_+-p_- and using K<0 drops the two nonpositive same-sign
terms. The two remaining terms are equal by symmetry and give
(30), with the factor2 intact. This is a signed bound preserving
the joint rational kernel, rather than independent hulls for d_j,e_j.
The positive-part decomposition is made after the absolutely convergent
full profile sum; it does not replace p_+ by a sum of positive parts.

To close attempt1847's threshold target, (30) would have to pay the explicit
threshold S4^3/5. C034b's integrated d_j>0 neither proves p_-=0
nor bounds R. Its negative-phase estimates weight Q_j, not the
joint kernel in (30); they do not already supply this comparison.
No upper bound at the required threshold has been established for
the signed R plus the mixed-sign integral. Absolute convergence
alone gives no such smallness, and R cannot be discarded as a
boundary-at-infinity term: it includes the retained normalization
and the finite cutoff at1.

The algebraic negative quadrant is a useful partial signed input;
the actual positive contribution remains unpaid. Park the adjoint
mechanism at this explicit remainder. A further closure attempt
requires materially new, separately covered control of it, not a
repeat of (27) or an assumption that the spatial profile is positive.
This failure to prove the sufficient bound is not a counterexample
to it, a prefix zero, a failure of ECT, or a disproof of RH. Preserve
stops1839/1843 and their earlier route evidence.

### Conceptual audit1849 — 20 November 2026

The partial statements (27)-(35) pass the unchanged EXPLORE
assessment1847, separately approved1848. This is verification of an
existing qualified reduction, with no stronger inequality or repaired
mathematical error. The source coverage above is reused; source-wide
and finite-zero validity and C034c(20) are outside this verdict.

**Uniform analytic interface.** Put I=[1/2,3]. For k=0,2,4,
C032n(8) and the count give

    M_k:=sum_rho sup_(sigma in I, 0<=x<=1)|u_rho^(k)(x)|<infinity.

The same holds for every fixed derivative needed here. Each u_rho is
even, since G is even and the two translates exchange under x -> -x;
conjugation invariance makes their sum the real p without changing
multiplicity. Taylor's integral remainder yields

    sum|A_rho(x)|<=M_2*x^2/2,
    sum|B_rho(x)|<=M_4*x^2/2,
    sum|V_rho(x)|<=M_4*x^4/24,
    sum|V_rho'(x)|<=M_4*x^3/6,                 0<=x<=1.

At infinity the sums of absolute Gaussian derivatives are bounded by
constants times the width-independent P of C032n(9). The subtractions
add only finite constants or c*x^2 (c*x for V'). Hence A*Q_j,
B*Q_j and V*Q_j'' have summable absolute memberwise dominators on
both spatial regions: at zero they are O(1); at infinity use
(P+1)/x^4 and (P+1+x^2)/x^6. These are integrable because
int_1^infinity P/x^2<infinity. This proves uniform dominated limits,
not just boundedness of each separate integral. It also validates
partial_sigma h=e_2-e_1, with partial_sigma p(0)=p''(0) retained.

**Every cutoff and moment.** On [epsilon,M] the exact boundary
pairing for V and Q_j is V'Q_j-VQ_j'. At epsilon its two terms
are O(epsilon). At M, C032n(13) gives respectively
O(log(M)/M^3) and O(1/M^3+log(M)/M^4), uniformly on I;
both vanish. For D, smooth evenness gives D'=O(x) at zero, and
D,D',D'' have orders x^-4,x^-5,x^-6 at infinity. The primitive
in (31) proves int D=0. Independently,

    int_epsilon^M D''=[D']_epsilon^M,
    int_epsilon^M x^2 D''=[x^2 D'-2xD]_epsilon^M
                                      +2 int_epsilon^M D.

Their boundaries vanish, proving both moments in (32) as ordinary
absolute integrals. Thus the constant and quadratic differences
between V and p may both be removed against D'', while neither
is split into divergent integrals against Q_j''. At the origin
pD and pD'' have bounded memberwise sums; at infinity their
dominators are P/x^4 and P/x^6. This covers all representations
in (27), including their absolute divisor exchanges.

**Products and rational sign.** Let a=sum int|A_rho|Q_1 and
v=sum int|V_rho|(|Q_1''|+|Q_2''|). Both are finite by the
preceding bounds. Since |D|<=Q_1 and |D''|<=|Q_1''|+|Q_2''|,
the sum of absolute pair integrals in (28) is at most 2av.
Tonelli and Fubini therefore retain every ordered and diagonal
divisor pair. The boundary estimates also hold before absolute
member summation, using the same P growth and finite origin sums.

Independent replay starts from Q_j as a rational function of t,
using d_x^2=2*d_t+4t*d_t^2. It verifies both partial fractions,
both second derivatives, D's primitive and regular formula, r,ell,s,
and all three derivative/difference formulas by exact polynomial
cross multiplication. The 12 identity differences are identically
zero; the three coefficient sign checks and K(1,1)=-784/27 also
pass. Complete difference numerators, sign arrays and corner values
were inspected in `scripts/smoothed-law/laplace_adjoint_audit_1849.json`.
Reproduce with `python3 scripts/smoothed-law/laplace_adjoint_audit_1849.py`.
The first execution's missing reflected-division method caused a
TypeError before any check; its repair is recorded in that certificate.

Equation (35) also checks by direct expansion: both sides reduce to
ell(y)*s(y)+ell(x)*s(x)-r(x)*ell(y)-r(y)*ell(x).
All rational denominators are positive for real t>=1. The verified
shifted coefficients give r increasing and s-r<0 there, while ell
is positive and decreasing. This proves the sign for every x,y>=1,
including x=y=1, without extrapolation from sampled values.

**Retained correction and signed bound.** At the lower boundary 1,
subtracting the pairing p'(1)Q_j(1)-p(1)Q_j'(1) gives exactly
-p'(1)Q_j(1)+p(1)Q_j'(1) in beta_j. The original constant
subtractions contribute -p(0)int_1^infinity Q_j and
-p''(0)int_1^infinity Q_j, respectively. Thus d_j=U_j+alpha_j
and e_j=W_j+beta_j with all six terms of R present. The origin
integrals, finite traces and tail integrals are absolutely summable
over the divisor; their products have the corresponding product
majorants. Symmetrizing U_1W_2-U_2W_1 gives (29)-(30) with factor 1/2
in K. In addition |K| is bounded by half the sum of its four positive
rational product terms, so all full-profile positive-part integrals
are finite. The same-sign terms are nonpositive; symmetry identifies
the two opposite-sign terms and gives factor 2. This step takes
positive parts only after the real full profile has been summed.

No sign or sufficient smallness of R or that mixed-sign integral is
established by this audit. In particular K<0 is not C<=0 and does
not pay S4^3/5. The closure stop1847 remains in force for transfer
alone; no RH, global Neumann-domain premise, discarded normalization,
finite-zero truncation or numerical sign inference has entered.

## Mathlib

Full matching coverage is unchecked and unknown. No Mathlib theorem
is used or claimed absent. Supporting Gaussian, integration-by-parts,
polynomial and finite-product results may exist; no matching theorem
for this qualified infinite-divisor transfer and signed remainder
bound has been verified. Conceptual audit1849 validates the stated
partial result and retains every external-input qualification; it is
not a formal Mathlib verification.
