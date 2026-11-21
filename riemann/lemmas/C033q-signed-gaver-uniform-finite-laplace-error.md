# Corollary C033q: uniform signed Gaver evaluation with full variation tails

## Hypotheses

Retain C033j's real signed measures on X=[0,infinity), indexed by
sigma in W=[1,2], and their specified continuous density representatives:

    R_sigma=exp(-M_sigma)*delta_0+r_sigma(t)dt.

For their application here retain C033j/p's qualified actual positive-
ordinate nontrivial zeta divisor, z_rho=gamma_rho-i*(beta_rho-1/2),
conjugation and multiplicity, excluded ordinate zero, |beta_rho-1/2|<1/2,
gamma_rho>14, counting N(T)=O(T log(T+2)), verified real zeros through
height 100, retained real zero in (14,15), reciprocal-square tail,
heat positivity and separately controlled fixed-j heat errors through
j=2. Sigma is Gaussian half-variance. Both fixed-v1 preprints and the
finite-zero data remain external inputs, not independently certified
here. No asymptotic remainder is differentiated.

Put I=[3/4,5/4] and X_0={7/8,9/8}. Choose finite nonnegative bounds

    sup_(sigma in W, t in I) |r_sigma(t)|<=B,
    |r_sigma(t)-r_sigma(u)|<=L*|t-u|  (t,u in I, sigma in W),
    sup_(sigma in W) ||R_sigma||_TV<=V.                 (1)

C033j(7),(14) provide B and V; for example V=exp(2*K_0) with
K_0 exactly as defined there. L may be C033p(1)'s audited constant.
V bounds the full measure, including its zero atom and both spatial
tails. These constants are generally nonnumerical. The proof below
in fact applies to any such family of finite real signed measures
satisfying the displayed decomposition and (1).

Let F_sigma(s)=integral_X exp(-s*t)dR_sigma(t) for s>0. This finite
integral is also exp(-(B_sigma(s)-B_1(s))) by C033j(9). Only exact
values of F_sigma are used. No global boundedness of r_sigma,
positivity of R_sigma, finite moments of R_sigma, inverse stability,
width-measure realization, full odd cancellation or RH is assumed.

## Conclusion

For every integer n>=1 and x in X_0 define

    a_x=log(2)/x,  c_n=(2n)!/[n!*(n-1)!],
    w_(n,k,x)=a_x*c_n*(-1)^k*binom(n,k),
    s_(n,k,x)=a_x*(n+k),              0<=k<=n,
    G_(n,x)[F]=sum_(k=0)^n w_(n,k,x)*F(s_(n,k,x)).    (2)

All n+1 sample arguments are strictly positive. Define explicit
constants and sequences

    q=max{4*2^(-6/7)*(1-2^(-6/7)),
          4*2^(-10/9)*(1-2^(-10/9))},   0<q<1,
    b_n=(9/(8*log(2)))*sqrt(n+2)/n,
    E_n(B,L,V)=L*b_n+64*B*b_n^2+(8*log(2)/7)*V*n*q^n. (3)

Then

    sup_(sigma in W, x in X_0)
        |G_(n,x)[F_sigma]-r_sigma(x)|<=E_n(B,L,V),
    lim_(n->infinity) E_n(B,L,V)=0.                   (4)

The zero atom contributes exactly zero to (2) for each n>=1; it is
retained in the identity, rather than assumed absent. For arbitrary
errors epsilon_k in the sampled transforms, the additional error is
at most sum_k |w_(n,k,x)|*|epsilon_k|, and

    sum_(k=0)^n |w_(n,k,x)|=a_x*c_n*2^n<=a_x*n*8^n. (5)

This proves a parameterized analytic evaluation bound, using the known
unaccelerated Gaver mechanism. It supplies no numerical values of
B,L,V, inverse or data-evaluation error bounds, finite separator data,
margin or runtime. It does not pay uncapped width variation, moments,
cancellation or actual-Xi positivity. The proof passes the separate
conceptual audit1773 below under these unchanged hypotheses. No complete
RH candidate is claimed and no originality beyond the checked literature
is asserted.

## Proof

### Known formula, normalization and specialization scope

Reuse the unchanged SPECIALIZE assessment1769, separately approved1770,
and its primary-source coverage in notes1764/1769. The base finite
formula and normalized kernel are A. Kuznetsov, *On the convergence
of the Gaver-Stehfest algorithm*, SIAM J. Numer. Anal. 51(6) (2013),
2984-2998, [arXiv:1305.0715v2](https://arxiv.org/pdf/1305.0715v2),
served manuscript dated 29 October 2018, pp.2-3, equations (2)-(3).
The positive-real sample formula is also J. Abate and W. Whitt,
*A Unified Framework for Numerically Inverting Laplace Transforms*,
INFORMS J. Computing 18(4) (2006), 408-421,
[p.414, equation (28)](https://www.columbia.edu/~ww2040/AbateUnified2006.pdf),
DOI 10.1287/ijoc.1050.0137.

For the exact kernel transform and cumulants use D. P. Gaver, Jr.,
*Observing Stochastic Processes, and Approximate Transform Inversion*,
Operations Research 14(3) (1966), 444-459,
[pp.448-451, equations (13)-(29), particularly (17)-(20)](https://doi.org/10.1287/opre.14.3.444).
Inspection of these proof cases is recorded in source-notes1764;
no new retrieval or inspection is claimed here. The beta integral is
Euler's formula [DLMF (5.12.1)](https://dlmf.nist.gov/5.12.E1).

The cited inversion results concern functions or positive kernels,
and do not by themselves cover this signed, atom-bearing family.
We import the base formulas and cumulants only. The short beta-product
calculation below checks the exact n-to-2n indexing, log(2)/x scaling
and normalization needed for our explicit bounds; it is not a new
inversion theorem. No accelerated theorem or bounded-smooth-function
expansion is used. The additional work is signed finite integration,
local normalization leakage and a supremum tail against full variation.

### Exact finite signed-measure identity and atom

For fixed n,x put

    K_(n,x)(t)=a_x*c_n*exp(-n*a_x*t)*(1-exp(-a_x*t))^n,
                                                       t>=0. (6)

Every exp(-s_(n,k,x)*t) is bounded by one on X, so it is integrable
against |R_sigma|. Finite linearity and the binomial theorem give

    G_(n,x)[F_sigma]=integral_X K_(n,x)(t)dR_sigma(t).  (7)

No infinite sum or limit is interchanged. The kernel is nonnegative
and bounded. At t=0 its factor (1-exp(-a_x*t))^n is zero because
n>=1. Equivalently, the atom's transform is the constant exp(-M_sigma),
whose contribution to (2) is a_x*c_n*exp(-M_sigma)*(1-1)^n=0.
Thus the full atom is included and cancels exactly. This says nothing
about numerical cancellation with inexact samples.

### Normalization and the local second-moment bound

Write p_n(u)=c_n*exp(-n*u)*(1-exp(-u))^n, u>=0. For real z>-n,
the substitution y=exp(-u) and the beta integral give

    J_n(z)=integral_0^infinity exp(-z*u)*p_n(u)du
          =c_n*Beta(n+z,n+1)
          =product_(j=n)^(2n) j/(j+z).                (8)

All beta parameters are positive. At z=0 this is one, proving
integral_0^infinity K_(n,x)(t)dt=1 by u=a_x*t. To check the imported
cumulants directly, derivatives through order two under (8) at zero
are legitimate: for |z|<=n/2 their absolute integrands are bounded
by c_n*(1+u+u^2)*exp(-n*u/2), which is integrable on the half-line.
Logarithmic differentiation of the finite product therefore gives,
for a variable U with density p_n,

    E[U]=S_n=sum_(j=n)^(2n) 1/j,
    Var(U)=T_n=sum_(j=n)^(2n) 1/j^2.                 (9)

Here probability notation applies only to the positive normalized
kernel, never to R_sigma. For the first sum, monotonicity of 1/t gives

    sum_(j=n)^(2n-1) 1/j >= integral_n^(2n) dt/t=log(2),
    sum_(j=n+1)^(2n) 1/j <= integral_n^(2n) dt/t=log(2).

Adding the omitted endpoint in each case proves
0<=S_n-log(2)<=1/n. Also T_n<=(n+1)/n^2 since there are n+1 terms,
each at most 1/n^2. Consequently, after scaling u=a_x*t,

    integral_0^infinity (t-x)^2*K_(n,x)(t)dt
      =(x/log(2))^2*[T_n+(S_n-log(2))^2]
      <=(x/log(2))^2*(n+2)/n^2<=b_n^2.               (10)

The final inequality uses x<=9/8. Cauchy-Schwarz against the unit
kernel mass gives integral |t-x|K_(n,x)(t)dt<=b_n. Also every
t outside I satisfies |t-x|>=1/8 for either selected x, hence

    integral_(X\I) K_(n,x)(t)dt<=64*b_n^2.           (11)

This Lebesgue-mass estimate will pay only the local normalization
loss. It will not be applied to the variation measure |R_sigma|.

### Supremum decay outside I and the full signed tail

For v>=0 let h(v)=4*2^(-v)*(1-2^(-v)). It is increasing up to v=1
and decreasing thereafter: put y=2^(-v), so the derivative of
4*y*(1-y) with respect to v is -4*log(2)*y*(1-2*y).
Moreover h(v)=1-(2*2^(-v)-1)^2, with equality to one exactly at v=1.
Both h(6/7) and h(10/9) belong to (0,1), proving 0<q<1 in (3).

If t<3/4 and x in X_0 then t/x<=6/7; if t>5/4 then t/x>=10/9.
It follows from the two monotonicity intervals that h(t/x)<=q on
X\I. The binomial theorem also gives binom(2n,n)<=2^(2n), so

    c_n=n*binom(2n,n)<=n*4^n,
    0<=K_(n,x)(t)<=a_x*n*h(t/x)^n
                         <=a_x*n*q^n       (t outside I). (12)

Therefore the full signed tail, including the point zero, obeys

    |integral_(X\I) K_(n,x)(t)dR_sigma(t)|
      <=integral_(X\I) K_(n,x)(t)d|R_sigma|(t)
      <=V*a_x*n*q^n<=(8*log(2)/7)*V*n*q^n.           (13)

The zero contribution was evaluated exactly above. The estimate
covers the entire remaining tails, however their signed densities
are distributed. No moment, global density supremum or probability
tail estimate for R_sigma is used.

### Three error terms and coefficient accounting

There is no atom on I and dR_sigma(t)=r_sigma(t)dt there. Using the
unit Lebesgue integral of K_(n,x), subtract r_sigma(x) from (7):

    G_(n,x)[F_sigma]-r_sigma(x)
      =integral_I K_(n,x)(t)*(r_sigma(t)-r_sigma(x))dt
       +r_sigma(x)*(integral_I K_(n,x)(t)dt-1)
       +integral_(X\I) K_(n,x)(t)dR_sigma(t).          (14)

All terms exist by local boundedness, finite variation and the
bounded integrable kernel. By (1),(10), the first term is at most
L*b_n in absolute value. By (1),(11), the second is at most
64*B*b_n^2. The third is bounded by (13). This proves (4), uniformly
in sigma and both x. Since b_n->0 and 0<q<1, all terms in (3)
tend to zero; in particular the ratio of successive n*q^n tends
to q<1, proving its decay without an asymptotic approximation.

Finally finite linearity bounds sample errors by the weighted sum
stated before (5). Summing the absolute binomial coefficients yields
a_x*c_n*2^n exactly, and (12)'s bound on c_n gives (5). The transform
ratio F_sigma=exp(-(B_sigma-B_1)) is supplied by C033j, but no bound
on errors in that ratio is established here. Exact convergence (4)
therefore does not imply stable finite-precision computation or a
separator for C033l. Stops1571/1576 concern different, still-unpaid
data/evaluation budgets and are not contradicted.

### Conceptual audit1773 — 19 November 2026

**Verdict.** Equations (2)-(5) pass under exactly (1) and the stated
decomposition. No hypothesis, constant, formula or direct dependency
requires correction. This is a verification of the existing local
specialization, not a new estimate or an independent certification of
the external heat/zero inputs. The unchanged SPECIALIZE assessment1771,
separately approved1772, covers this audit. Read the full proof above,
C033j's measure, atom, transform and density construction through (14),
and C033p's hypotheses and audited Lipschitz assertion. Primary coverage
is reused from notes1764/1769 and approval1770, with no fresh retrieval
or substitution of source versions. The following checks concern this
proof, not a second audit of the upstream heat estimates.

1. **Input representatives and exact finite integration.** C033j(14)
   supplies a genuine Lebesgue density away from zero, with a specified
   continuous representative; its compact bound supplies B on I.
   C033p(2) supplies L on that same closed interval, for all widths in
   [1,2]. C033j(7) supplies full variation V, not just density mass.
   These constants are independent of n and x. Every sample in (2)
   is positive because a_x>0 and n+k>=1; its exponential is bounded
   by one on X. Thus each integral exists absolutely against variation,
   and a finite binomial expansion proves (7) without a limiting
   interchange. The coefficient of the atom is exactly (1-1)^n=0.
   No atom is discarded, and this identity is asserted only for exact
   samples. At sigma=1, C033j gives R_1=delta_0 and r_1=0, consistent
   with both sides. Finite variation and the specified density also
   exclude any hidden singular mass at the endpoints of I.

2. **The n+1 factors and moment centering.** In (8), y=exp(-u)
   contributes du=-dy/y, leaving y^(n+z-1)(1-y)^n. Hence the beta
   parameters really are n+z and n+1. Multiplying by c_n gives

       J_n(z)=[(2n)!/(n-1)!]*Gamma(n+z)/Gamma(2n+z+1),

   which is the product over every integer j from n through 2n,
   including both endpoints. It has n+1 factors. The parameters are
   positive for real z>-n; J_n(0)=1. The displayed dominator for
   |z|<=n/2 controls derivatives of orders zero, one and two, so
   J_n'(0)=-E[U] and J_n''(0)=E[U^2] legitimately. The first and
   second logarithmic derivatives are -S_n and T_n, giving (9).
   This probability calculation is for p_n alone. No moment of
   R_sigma is requested. Scaling by a_x centers at a_x*x=log(2),
   not at the kernel's mean S_n; the squared bias in (10) is retained.
   The integral comparisons give S_n<=log(2)+1/n and
   S_n>=log(2), and T_n<=(n+1)/n^2. Their sum with squared bias
   is at most (n+2)/n^2, also for n=1. Thus b_n has precisely the
   upper scaling factor 9/(8*log(2)).

3. **Local leakage and the two different tail measures.** Normalization
   and (10) justify Cauchy-Schwarz for the first absolute moment.
   The distances from 7/8 to the two boundaries of I are 1/8 and
   3/8; those from 9/8 are 3/8 and 1/8. Consequently the indicator
   of X\I is at most 64*(t-x)^2 there, proving (11). This is
   integration against K(t)dt. Multiplying it by the single number
   |r_sigma(x)|<=B pays the normalization term in (14). It would
   not bound the signed tail against |R_sigma|, and the proof does
   not use it for that purpose.

4. **The whole outside-interval supremum.** The left-tail supremum
   of t/x is (3/4)/(7/8)=6/7<1. The right-tail infimum is
   (5/4)/(9/8)=10/9>1. The derivative of h has
   positive sign below 1 and negative sign above 1, and its identity
   h(v)=1-(2*2^(-v)-1)^2 proves that both endpoint values defining
   q lie strictly between zero and one. These bounds cover the entire
   half-line complement of I, including arbitrarily large t, without
   truncation. Also c_n=n*binom(2n,n)<=n*4^n, so (6) is bounded by
   a_x*n*h(t/x)^n. Integrating its outside supremum against full
   variation proves (13), with a_x<=8*log(2)/7. The zero atom is
   included in that variation budget, though its actual contribution
   was already proved zero. No global density bound or signed-measure
   concentration statement enters this step.

5. **Error assembly and uniformity.** Restriction to I has density
   r_sigma(t), so add and subtract r_sigma(x)*integral_I K(t)dt
   in (7) to get exactly the three terms of (14). Their bounds are,
   respectively, L*b_n, 64*B*b_n^2 and (8*log(2)/7)*V*n*q^n.
   All integrals are defined by the local bounded density or full
   variation. The same constants hold for both x and every sigma,
   including the width endpoints. As b_n tends to zero and
   ((n+1)*q^(n+1))/(n*q^n) tends to q<1, all three terms vanish.
   This proves the claimed uniform convergence without moving the
   fixed evaluation points or using a limit of signed measures.

6. **Coefficient scope and qualifications.** Taking absolute values
   of the finite coefficients gives a_x*c_n*sum_k binom(n,k), which
   equals a_x*c_n*2^n and is at most a_x*n*8^n. The triangle
   inequality gives exactly the stated sample-error allowance. It
   neither controls the epsilon_k nor guarantees reliable numerical
   cancellation. In particular, F_sigma=exp(-(B_sigma-B_1)) being
   exact does not certify the error of any numerical transform ratio.
   The actual divisor, conjugation/multiplicity, excluded ordinate
   zero, strict strip, gamma>14, counting, finite-zero/retained-zero/
   reciprocal-square-tail, heat positivity, separate fixed-j errors
   through j=2, half-variance and both fixed-v1 qualifications are
   unchanged. B,L,V remain finite but nonnumerical. The two fixed
   spatial points do not establish a shrinking-neighborhood jump
   witness or C033l separator. Such a new target requires its own
   coverage and proof. No inverse stability, uncapped variation,
   moments, cancellation or actual-Xi conclusion follows.

## Mathlib

Full matching coverage of this signed, atom-bearing, width-uniform
finite-Gaver estimate has not been checked and is unknown. Supporting
beta integrals, binomial sums, finite signed integration and moment
inequalities have not been separately assessed here. No Mathlib
theorem is substituted for the qualified C033j/p inputs or for the
variation-tail argument above.
