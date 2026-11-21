# Corollary C034l: parameterized cap-two interval Laplace error lower bound

## Hypotheses

Use exactly C033l's original laws on X=[0,infinity), with width interval
W=[1,2]. Each nu_sigma is a Borel probability with transform
k_sigma(s)=exp(-B_sigma(s)). For a finite real signed Borel measure
eta on W, nu_eta is its setwise mixture, with the bounded-Borel
integration identity and ||nu_eta||_TV<=|eta|(W). The class is

    A_2={eta: eta(W)=1, |eta|(W)<=2}.

It includes all atoms, singular continuous parts and infinite support.
The original residual mu is the probability obtained by removing
ell_1(t)dt on [1,3/2] from the Levy measure ell_1(t)dt; it has zero
drift and killing. Thus, for s>0,

    muhat(s)=exp(-integral_((0,infinity)\[1,3/2])
                                  (1-exp(-s*t))*ell_1(t)dt).

Retain all C033r qualifications from C033i/j/l/p/q: the actual
positive-ordinate nontrivial divisor, z_rho=gamma_rho-i*(beta_rho-1/2),
conjugation and multiplicity, exclusion of ordinate zero, strict strip
|beta_rho-1/2|<1/2, gamma_rho>14, N(T)=O(T log(T+2)), verified real
zeros through height100, a retained real zero in (14,15), reciprocal-
square tail, heat positivity, and separate fixed-j heat errors through
j=2. Sigma is Gaussian half-variance. Both fixed-v1 external preprints
and finite-zero data remain qualified inputs, not independently
certified here. No full cancellation, RH, signed-height payment or
unsmoothed actual-Xi realization is assumed.

Fix once and for all C033r's finite constants B,L,V,D,J, its
modulus omega, and admissible delta,tau,n chosen in
that order by C033r(1)-(5). More precisely, B,L,V,D are finite
nonnegative allowances, J=exp(m)*ell_1(1)>0, 0<delta<1/8,
rho=delta/2, 0<tau<=rho, and

    omega(delta)+4*L*delta<=J/4,
    omega(tau)<=J/8, n>=1, T_n<=J/8.

Here T_n is exactly the paid error in C033r(5), not a new or
uncontrolled remainder. All these choices precede eta. Define

    x_-=1-delta, x_+=1+delta, a_x=log(2)/x,
    A=log(2)/(1-delta), c_n=(2*n)!/[n!*(n-1)!],
    s_(x,k)=a_x*(n+k),                      0<=k<=n,
    v_(x,k)=epsilon_x*a_x*c_n*(-1)^k*binom(n,k),
    epsilon_(x_-)=1, epsilon_(x_+)=-1,
    d(s)=exp(-B_1(s))>0, alpha_(x,k)=v_(x,k)/d(s_(x,k)),
    e_n=J-omega(delta)-4*L*delta-omega(tau)-T_n>=J/2,
    C_n=2*A*n*8^n*exp(B_1(2*n*A)).                       (1)

C033r supplies these exact original-law nodes, coefficients and gap.
No numerical evaluation or effective choice of B,L,V,D,J,omega is
assumed. There is no new cap-V extension or inverse theorem.

## Conclusion

Let S be the set of distinct nodes s_(x,k), retaining a node even if
its combined coefficient is zero. For s in S set

    a_s=sum_((x,k):s_(x,k)=s) alpha_(x,k),
    K_n=sum_(s in S) |a_s|,
    m_*=min({3/2} union S), r_*=min{1/8,m_*/8},
    N=max_(s in S) ceil(|s-3/2|/r_*), p=2^(N+1).         (2)

Then S is finite nonempty and positive, N is a finite nonnegative
integer, and

    0<K_n<=C_n<infinity, 0<e_n<=2*K_n.

For every eta in the entire class A_2, put

    epsilon_eta=sup_(1<=s<=2) |muhat(s)-nuhat_eta(s)|.

Uniformly in eta,

    epsilon_eta >= 3*(e_n/(3*K_n))^p
                >= Delta_n:=3*(e_n/(3*C_n))^p
                >= 3*(J/(6*C_n))^p >0.                 (3)

In particular the original-law interval infimum d_2=inf_(eta in A_2)
epsilon_eta is strictly positive under these inherited qualifications.
The bound is explicit in C033r's fixed finite parameters and C033v's
node count; those parameters remain generally nonnumerical. It is not
a computed margin, optimal exponent, feasible algorithm or unrestricted-
variation estimate. Every division by d(s) remains charged in C_n.

This is a local reproduction/specialization of the already assessed
separator and analytic-continuation tools. It supplies no claim of
progress beyond the checked general sources or certified originality.
It constrains approximation of this particular residual law; it does
not realize actual Xi, settle full cancellation or prove RH. The
composite argument passes the separate application audit1885 below
under these unchanged qualifications.

## Proof

### Source scope

Use the unchanged SPECIALIZE assessment1880, with comparison1881 and
source-address repair1882, available before this attempt. C033l supplies
the original-law probability and signed-mixture TV statements. C033r(7)
and (8), already audited1777, supply the fixed finite separator and its
full coefficient allowance. C033v(1)-(2), already audited1880, supply
the finite-node propagation estimate for signed measures with unbounded
support. We apply these statements; none is reproved here.

The precise analytic imports behind C033v are Lloyd N. Trefethen,
*Quantifying the ill-conditioning of analytic continuation*, BIT60
(2020),901-915, DOI10.1007/s10543-020-00802-7,
[Lemma2.1/proof p904 and Theorem3.1/proof pp904-905](https://people.maths.ox.ac.uk/trefethen/trefethen_ac.pdf).
The base Gaver formula behind C033r is A. Kuznetsov,
*On the convergence of the Gaver-Stehfest algorithm*, SIAM J. Numer.
Anal.51(6)(2013),2984-2998,
[arXiv:1305.0715v2, pp2-3, (2)-(3)](https://arxiv.org/pdf/1305.0715v2),
with J. Abate and W. Whitt, *A Unified Framework for Numerically
Inverting Laplace Transforms*, INFORMS J. Computing18(4)(2006),408-421,
[p414,(28)](https://www.columbia.edu/~ww2040/AbateUnified2006.pdf),
and D. P. Gaver, Jr., *Observing Stochastic Processes, and Approximate
Transform Inversion*, Operations Research14(3)(1966),444-459,
[pp448-451,(13)-(29), especially(17)-(20)](https://doi.org/10.1287/opre.14.3.444).
The inspected hypotheses and essential proof cases are reused from
notes1774/1790/1881. No fresh inspection or source-wide verification is
claimed. The additional work here is only the original-law uniform TV
allowance and scalar combination, including coefficients and endpoints.
The missing global regularity and whole-axis-data hypotheses recorded
in stop1790 are not assumed or needed.

### Original-law allowance and fixed coefficient costs

For each eta in A_2 set theta_eta=mu-nu_eta. These are finite real
signed Borel measures on the whole half-line. C033l and the TV triangle
inequality give

    ||theta_eta||_TV<=||mu||_TV+||nu_eta||_TV
                   <=1+|eta|(W)<=3.                    (4)

The atom at zero, any singular part, and every tail are included in
(4). We have not used ||R_sigma||_TV in place of this original-law
bound. Its Laplace transform is precisely

    F_eta(z)=integral_X exp(-z*t) dtheta_eta(t), Re z>0,
    F_eta(s)=muhat(s)-nuhat_eta(s),             s>0.      (5)

C033v ensures holomorphy and |F_eta(z)|<=3. In particular epsilon_eta
is a finite supremum, at most3. No inverse-convolution or interval
division is applied to (5).

All the indexed nodes in (1) are positive, since a_x>0 and n+k>=1.
There are at most2(n+1) of them. Thus S and every number in (2) are
fixed independently of eta; m_*,r_*>0 and N is finite. Finite grouping
of C033r's exact separator preserves its value, so

    sum_(s in S) a_s*F_eta(s)>=e_n>0,       eta in A_2.  (6)

By the triangle inequality for each group and C033r(8),

    K_n<=sum_(x,k)|alpha_(x,k)|<=C_n<infinity.           (7)

This is an upper bound after merging, never an assertion that the
absolute sums are unchanged. The coefficients are the original-law
v_(x,k)/d(s_(x,k)); the factor exp(B_1(2*n*A)) in C_n retains their
division costs. A deconvolved coefficient sum is not substituted.

The class is nonempty: eta=delta_1 has mass1 and TV1. Its original
mixture is nu_1, so ||mu-nu_1||_TV<=2. Consequently |F_delta_1(s)|<=2,
and (6) for this particular member gives

    0<e_n<=sum_s a_s*F_delta_1(s)
          <=sum_s |a_s|*|F_delta_1(s)|<=2*K_n.          (8)

Thus K_n>0, and

    0<e_n/(3*C_n)<=e_n/(3*K_n)<=2/3<1.                 (9)

No favorable cancellation in the generic signed law is needed for (8);
it only checks the scale of the fixed separator using one positive law.

### Propagation, inversion of the scalar inequality, and endpoints

Apply C033v to theta_eta, prescribed allowance M=3, and exactly the
node set S of (2). Its exponent is alpha(S)=2^(-(N+1))=1/p.
If 0<epsilon_eta<3, (4)-(5) meet all its hypotheses and give

    max_(s in S)|F_eta(s)|<=3*(epsilon_eta/3)^(1/p).

Together with (6)-(7), this yields

    e_n<=K_n*max_(s in S)|F_eta(s)|
        <=3*K_n*(epsilon_eta/3)^(1/p).

Divide by3*K_n>0 and raise the two nonnegative sides to the finite
positive integer p. The power function is increasing, hence

    epsilon_eta>=3*(e_n/(3*K_n))^p.                    (10)

If epsilon_eta=0, C033v's zero-error identity case gives F_eta=0 on
the positive half-plane. This contradicts (6), so zero error is
impossible. If epsilon_eta>=3, the right side of (10) is strictly
less than3 by (9); hence (10) holds directly. The actual supremum
here is at most3, but this also handles any larger prescribed error.
In particular theta_eta=0 is ruled out by the same separator, with
no normalization by its possibly zero norm.

Now K_n<=C_n and e_n>=J/2>0 give the remaining inequalities in (3)
by monotonicity of the same power. Every finite base is strictly
positive and p is finite, so Delta_n>0 even if very small. All
constants are fixed before eta; taking the infimum over the entire
class preserves this lower bound. No minimizing law, compactness
argument, positivity of nu_eta or additional smoothness is required.

This closes only the stated parameterized interval application. It
does not evaluate any input parameter or strengthen the inherited
external inputs. Stops1790/1792 and numerical stops1571/1576/1781/1782
retain their stated scopes.

### Application audit1885 — 20 November 2026

Verdict: (1)-(10), including the full signed class and all error cases,
pass the independent bounded application audit under the unchanged
SPECIALIZE assessment1883, approved1884. No hypothesis, constant,
inequality or mathematical input is changed. This is informal
verification of the local reproduction, not independent certification
of the upstream preprints, heat inputs or finite-zero data.

1. **The correct measure and uniform allowance.** C033l supplies the
   original probability mu and the setwise signed mixture nu_eta,
   with its bounded-Borel integration identity and TV<=|eta|(W).
   Therefore theta_eta=mu-nu_eta is a finite real signed Borel measure
   on all of X, with TV<=3 uniformly over A_2. This includes zero atoms,
   singular measures and unbounded tails. Its transform is exactly (5),
   not the transform of lambda-R_eta. C033v's signed-integral proof
   permits a prescribed nonsharp M=3, so neither an unknown positive
   norm nor an undamped moment is required. Realness of the measures,
   exponents and coefficients makes (6) an ordered real inequality.

2. **Parameters and finite nodes.** C033r first fixes delta, then tau,
   and finally an admissible finite integer n. Its allowances leave
   e_n>=J-J/4-J/8-J/8=J/2>0. Every x is positive and n+k>=1;
   thus all 2(n+1) indexed nodes are finite and strictly positive.
   Forming their distinct set, including nodes with zero combined
   coefficient, gives a nonempty finite S fixed before eta. Its
   m_*,r_*,N are exactly C033v's choices, so alpha(S)=1/p, with p
   a finite positive integer (at least2). No eta-dependent propagation
   constant or optimization is introduced.

3. **Grouping and all division costs.** Finite grouping preserves
   the value of C033r(7) exactly. For each group the triangle
   inequality gives |sum alpha_i|<=sum |alpha_i|, proving (7)
   without assuming that merging preserves absolute sums. All
   coefficients are v_i/d(s_i). C033r's original-law return and
   audit1777 case6 pay d(s_i)>0 and B_1(s_i)<=B_1(2*n*A), so the
   bound C_n includes the full factor exp(B_1(2*n*A)); it is positive
   and finite. No interval estimate has been divided by d(s).

4. **Nonzero vector and scale.** The member eta=delta_1 belongs to
   the same A_2 and gives the probability nu_1. Its difference from
   mu has TV<=2. Applying the very same separator to this member
   proves e_n<=2*K_n. In particular complete cancellation of merged
   coefficients is impossible. Hence both normalized bases in (9)
   are positive and e_n/(3*K_n)<=2/3<1. This scale check uses one
   probability member; it never asserts positivity of general nu_eta.

5. **Scalar directions and exceptional errors.** For 0<epsilon_eta<3,
   C033v applies to (5), M=3 and S. The absolute value of the finite
   sum in (6) is at most K_n*max_S|F_eta|. Consequently division by
   3*K_n>0 and raising to p>0 give (10) in the displayed direction.
   Zero interval error invokes C033v's identity case and contradicts
   (6). For epsilon_eta>=3 the proposed lower bound is strictly below3
   by case4, so it holds directly, including equality epsilon_eta=3.
   The actual error is at most3; there is no missing endpoint or
   division by epsilon_eta or by ||theta_eta||. Finally K_n<=C_n
   decreases the denominator's reciprocal, and e_n>=J/2 decreases
   the numerator when replaced by J/2. Monotonicity of a positive
   power gives both remaining inequalities in (3). Fixed positive
   bases and finite p give a strictly positive uniform bound on the
   infimum; attainment of that infimum is unnecessary.

All divisor/conjugation/multiplicity, excluded ordinate-zero,
strict-strip/gamma>14, counting, through100/retained-real-zero,
reciprocal-square-tail, heat positivity and separate fixed-j errors
through2, Gaussian half-variance and both fixed-v1 qualifications
remain in force. The direct mathematical inputs remain exactly
C033l, C033r and C033v; no DAG change is needed. Source imports are
the precise Gaver and Trefethen citations above, reused through the
audited interfaces rather than reproved. No new mathematical script
or numerical check is needed for these finite-sum and scalar checks.

The achieved threshold is only the parameterized positive Delta_n
for cap2 on the full observation interval. C034k's exact match at the
two observations {1,2} is compatible with this result: those two
observations do not control the whole interval. No numerical margin,
unrestricted-variation obstruction, source-wide verification, signed
height, full cancellation or Xi realization follows. The audit removes
the composite proof's pending status; it supplies no result beyond
the scope of the inspected general tools.

## Mathlib

Full matching coverage for this qualified original-law application and
its explicit finite-node exponent has not been checked and is unknown.
Finite signed integration, the TV triangle inequality and finite sums
are supporting tools; no matching Mathlib declaration or formalization
is asserted. Audit1885 does not change this unknown coverage status.
C033r/v's cited Gaver and analytic-continuation mechanisms
remain mathematical inputs, not claims of Mathlib coverage. Neither
fixed-v1 preprint nor finite-zero data is certified here.
