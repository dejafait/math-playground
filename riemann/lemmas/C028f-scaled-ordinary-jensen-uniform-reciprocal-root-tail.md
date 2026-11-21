# Corollary C028f: scaled ordinary Jensen uniform reciprocal-root tail

## Hypotheses

Use precisely C028b's actual positive entire function and ordinary Jensen
polynomials, with its normalization:

    b_j=gamma_j/gamma_0>0,  b_0=1,  gamma_0=M_0>0,
    F(u)=sum_(j>=0) b_j u^j/j!,
    J_d(x)=sum_(j=0)^d binom(d,j)gamma_j x^j,
    U_d(u)=J_d(u/d)/gamma_0,  d>=3 an integer.

C028b identifies gamma_0 F with Theta(u)=xi(1/2+sqrt(u)), an entire
function of order 1/2. The square-root notation denotes the even entire
series, not a choice of branch. Count every polynomial zero with its
algebraic multiplicity. No RH, real-rootedness, root simplicity, finite
type at order 1/2, or upper bound on compact nonreal-zero mass is assumed.
U_d is not C028d/C028e's centered real-variable polynomial Q_d.

## Conclusion

There is a fixed finite K>=1, depending only on F, such that

    log F(r)<=K r^(3/4)                         (r>=1).

For any such K set

    B=K*3^(3/4)/log 2,    C=4B,    R_0=1.

For every integer d>=3 and real t>=1 the closed-disk count satisfies

    n_d(t):=#{u:U_d(u)=0, |u|<=t} <= B t^(3/4).

For every integer d>=3 and real R>=R_0,

    sum_(U_d(u)=0, |u|>R) |Im(1/u)|
      <=sum_(U_d(u)=0, |u|>R) 1/|u| <= C R^(-1/4).

The complete multiplicity-counted strict tail is controlled with constants
independent of d and R. This meets the approved tail threshold and is
a classical-method specialization, not a new general zero-counting theorem.
It does not bound the remaining compact mass or prove C028b's H_d=o(d).

## Proof

### Imported results and why a specialization is needed

Cormac O'Sullivan, *Zeros of Jensen polynomials and asymptotics for the
Riemann xi function*, arXiv:2007.13582v2, 9 December 2020,
[Introduction (1.2), Section 3.1, Theorem 3.1 and Corollary 3.2](https://arxiv.org/html/2007.13582v2#S3.SS1),
supplies the actual Theta convention and its order 1/2. C028b has already
verified the identification with gamma_0 F and the factorial convention.
We reuse that identification without assuming the hyperbolicity conclusion
that would require RH.

Import the standard named Jensen formula in Min Ru, *Nevanlinna Theory*,
undated author-hosted notes,
[Theorem A1.1.1 and Corollary A1.1.3, printed pp.1-2](https://www.math.uh.edu/~minru/log.pdf).
For a holomorphic function g on a neighborhood of the closed radius-rho
disk, with g(0)!=0 and no zeros on its boundary, the needed case is

    sum_(g(a)=0, |a|<rho) log(rho/|a|)
      =(1/(2pi)) integral_0^(2pi) log|g(rho exp(i theta))| dtheta
         -log|g(0)|,

with multiplicities. There are no poles in this application. The
growth-to-counting method is also in Sheng-Chi Liu, *Lecture Notes in
Analytic Number Theory*, Lecture 23, 18 March 2019,
[Theorems 23.1.2 and 23.2.1(i), printed pp.57-58](https://bpb-us-w2.wpmucdn.com/faculty.umaine.edu/dist/1/19/files/2022/08/analyticnumbertheory.pdf).
Only the counting method and Jensen formula are used; Liu's part (ii)
is not imported. The essential statements and boundary cases were inspected
in source review1516 under assessment1515.

Applying a fixed-function counting theorem separately to U_d would leave
uncontrolled constants depending on d. We therefore verify a single growth
majorant and retain its constant in the imported formula. The finite-root
integration below is supplied explicitly rather than relying on the
unimported summability formula. The theorem itself is not reproved.

### A single majorant for the entire family

Let M_F(r)=max_(|u|=r)|F(u)|. Positivity and absolute convergence of
the entire series give M_F(r)=F(r)>=1 for every r>=0: the triangle
inequality proves the upper bound and u=r attains it.

Order 1/2 means limsup_(r->infinity) log log M_F(r)/log r=1/2.
Since 3/4>1/2, there is a finite r_1>=1 such that
log M_F(r)<=r^(3/4) for every r>=r_1. Increasing a constant over the
compact interval [1,r_1] gives a finite K>=1 with

    log F(r)=log M_F(r)<=K r^(3/4)       for all r>=1.       (1)

This uses an exponent strictly above the order, and asserts no finite-type
bound at exponent 1/2. The existence of K is enough for this target; no
effective numerical value or onset is claimed.

For 0<=j<=d put a_(d,j)=(d)_j/d^j, where (d)_0=1 and
(d)_j=d(d-1)...(d-j+1). The exact finite coefficient identity is

    U_d(u)=sum_(j=0)^d a_(d,j) b_j u^j/j!.

Each multiplier lies in [0,1], including a_(d,0)=1. Consequently, for
every complex u and every d>=3,

    |U_d(u)|<=sum_(j=0)^d b_j |u|^j/j!<=F(|u|).           (2)

Also U_d(0)=1, its degree is exactly d because b_d>0, and it has no
zero at the origin. Thus all reciprocal weights are defined. Equations
(1)-(2) hold for every degree, including the smallest d=3; compact
convergence and eventual-in-degree estimates are not used.

### Counting all multiplicities, including radius endpoints

Fix d>=3 and t>=1. Since the polynomial has finitely many roots,
choose rho in (2t,3t) that is not the modulus of any root. Jensen's
formula applies to the entire U_d, with log|U_d(0)|=0. Every root
with |u|<=t is strictly inside rho and contributes at least log 2.
All other terms of the Jensen sum are nonnegative. Hence (1)-(2) give

    n_d(t) log 2
      <=sum_(U_d(u)=0, |u|<rho) log(rho/|u|)
      <=log F(rho)<=K rho^(3/4)<=K (3t)^(3/4).            (3)

This proves n_d(t)<=B t^(3/4). Roots on |u|=t are included; no Jensen
formula is applied on that circle. The auxiliary zero-free rho may depend
on d,t, but (3)'s constant does not. Multiple roots contribute with their
full multiplicity throughout, so neither contour avoidance nor counting
loses a repeated root.

### Complete finite-root tail

Fix R>=1 and write a=|u| for a polynomial root. For a>R,

    1/a=integral_a^infinity t^(-2) dt.

Sum this identity over the finite multiset of roots with a>R. Interchanging
a finite sum and the integrals is valid, giving the exact identity

    sum_(U_d(u)=0, |u|>R) 1/|u|
      =integral_R^infinity #{u:U_d(u)=0, R<|u|<=t} t^(-2) dt
      <=integral_R^infinity n_d(t) t^(-2) dt
      <=B integral_R^infinity t^(-5/4) dt
      =4B R^(-1/4).                                     (4)

Changing the count at an integration endpoint changes no integral. In
particular roots with |u|=R are excluded from the exact tail identity;
the upper bound by n_d(t) may include them and is still valid. The
integral evaluation uses t^(-1/4)->0 at infinity. The bound is uniform
over all finite degrees, even though the upper integration endpoint is
infinite. There is no exchange with a degree limit or an infinite root
sum. Finally |Im(1/u)|<=|1/u| proves the asserted height tail.

### Relevance and limitations

C028b's exact inversion identity is
H_d/d=sum_(U_d(u)=0)|Im(1/u)|. Thus (4) controls the terms outside any
fixed disk uniformly in d. It does not make the terms inside that disk
small. If a fixed nonreal zero of F exists, C028b's lower bound still
forces a positive liminf for H_d/d. No actual nonreal zero is supplied.
In particular no zero value for a limiting full sum, interchange of the
full root measures, or RH-equivalent upper payment follows here.

Duplicate check: C028e controls an exterior integral in the centered
reciprocal variable, rather than this root-plane tail. L130 uses a
different heat-deformed entire family and reciprocal-square weights;
L135 counts translated windows under an additional strip hypothesis.
Neither is an input or a substitute for (2). C019i concerns a moving
negative-real-root band rather than the complete escaping multiset.
The Schmeisser coefficient-budget and inverse-degree stops remain intact.
This proof establishes only the approved quantitative specialization.

### Separate proof audit1518 (2026-11-18)

Replayed the whole stated bound under the unchanged SPECIALIZE
assessment1515, using the previously inspected source statements in
review1516. The conclusion passes; no correction, stronger estimate or
new theorem import is needed. The checks are as follows.

* **Actual coefficient normalization.** C028b's
  gamma_j=j!M_(2j)/(2j)! makes b_j/j!=M_(2j)/(gamma_0(2j)!).
  Thus its even Xi series gives precisely gamma_0 F=Theta, without
  an extra j! or a derivative shift. In binom(d,j)gamma_j(u/d)^j/gamma_0
  the remaining multiplier of b_j u^j/j! is exactly (d)_j/d^j.
  All its factors lie in (0,1] for j<=d. The positive b_j therefore
  justify (2) for every complex u and every allowed degree.
* **One growth constant.** Positivity gives M_F(r)=F(r), including
  equality at the positive real radius. The cited order is a property
  of this fixed entire F, not of the individual polynomials. Its
  limsup definition gives log F(r)<=r^(3/4) beyond one fixed radius.
  On the remaining compact interval log F(r)/r^(3/4) is continuous
  and bounded. Hence K in (1) is independent of d. Finite type at
  order 1/2 is neither used nor inferred.
* **All roots in closed disks.** U_d(0)=1 excludes an origin zero,
  and b_d>0 gives exactly d finite roots with multiplicity. For each
  fixed d,t the finite set of root moduli cannot exhaust (2t,3t).
  Jensen's formula at a radius outside that set has no boundary
  zero or pole. Each root of modulus <=t has log(rho/|u|)>log 2;
  the other included terms are positive. The boundary mean is at
  most log F(rho), so (3) proves the closed count with precisely
  B=K*3^(3/4)/log 2, independent of the chosen radius and degree.
* **Strict tail and infinity.** For each of the finitely many roots
  with a=|u|>R, integration of t^(-2) over [a,infinity) is 1/a.
  The exact indicator count under the integral is R<a<=t. It
  excludes a=R even for a multiple root, while the upper count
  n_d(t) can include it. Endpoint values have measure zero. With
  t>=R>=1, (3) bounds the integrand by B t^(-5/4), whose full
  integral is 4B R^(-1/4). This checks the infinite integration
  endpoint without interchanging d->infinity or an infinite zero
  sum. The last step uses only |Im(1/u)|<=1/|u|.

The sole direct mathematical input remains C028b, including its cited
actual order and positive coefficient contracts; its entire earlier
dependency chain is not reproved by this bounded audit. No new DAG
edge is needed. The audit certifies the local specialization only.
It supplies neither a vanishing compact contribution nor a full-root
limiting identity, and does not change the RH-equivalent gap.

## Mathlib

Not checked. Availability of a full matching uniform-family tail theorem
and of formalized supporting Jensen/order results is unknown. No absence
or formal verification is claimed. The informal verification above checks
the factorial multiplier, common growth constant, boundary radii,
multiplicities, strict cutoff and complete finite-root integration.
