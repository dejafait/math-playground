# Corollary C032r: continuum positive-output moment equivalence

## Hypotheses

Use C032m and C032q on W=[1,2] and X=[0,infinity), with their usual
relative Euclidean topologies and Borel sigma algebras. Retain all
their actual-zeta-divisor, multiplicity, counting, finite-zero and
fixed-v1 preprint qualifications. In particular the Gaussian width
sigma is half the variance, the individual laws nu_sigma are the
smoothed probability laws of C032j, and their heat-positivity input
is retained. These are neither the unsmoothed reciprocal Xi laws nor
an assumption that the profiles p_sigma are nonnegative. This result
does not independently verify the underlying preprints or zero data.

Let eta be a real finite signed Borel measure on W such that

    eta(W)=1,    V=|eta|(W)<infinity.

There is no common bound imposed on V. Atoms, infinite support and
singular continuous parts are allowed. C032q defines the finite
signed law

    nu_eta(A)=integral_W nu_sigma(A) deta(sigma), A Borel in X.

Assume explicitly that nu_eta is nonnegative on all Borel sets.
It is therefore a probability measure, since C032q gives its mass
as eta(W)=1. No density, exclusion of an atom at zero, or moment
condition is assumed. Positivity of eta itself is not required.

With the entire functions b_sigma=E_sigma+O_sigma of C032m, set

    F_eta(w)=integral_W exp(-b_sigma(w)) deta(sigma),
    J_eta(w)=integral_W exp(-E_sigma(w))*sinh(O_sigma(w)) deta(sigma).

Here w ranges over all of C. The entire/parity and bounded-Laplace
interfaces established in C032m and C032q are

    F_eta(0)=1,
    F_eta(w)-F_eta(-w)=-2*J_eta(w),
    L_eta(s):=integral_X exp(-s*u) dnu_eta(u)=F_eta(sqrt(s)), s>0, (1)

where sqrt(s) is the positive real square root in the last formula.

## Conclusion

Under precisely these hypotheses the following are equivalent:

1. J_eta is identically zero on C.
2. F_eta is even on C.
3. integral_X exp(c*u) dnu_eta(u)<infinity for some c>0.
4. integral_X exp(c*u) dnu_eta(u)<infinity for every c>0.

When they hold, there is a unique entire function f_eta such that
F_eta(w)=f_eta(w^2) for all complex w. For real s>0 it equals L_eta(s),
and for every integer n>=0 and every real c>0,

    m_n:=integral_X u^n dnu_eta(u)=(-1)^n f_eta^(n)(0)<infinity,
    integral_X exp(c*u) dnu_eta(u)=f_eta(-c)<infinity.          (2)

For n=0 use u^0=1, including at u=0. Thus m_0=1.

This is a conditional specialization of known positive-measure tools
and C032k's finite-law argument. It constructs no eta, decides
neither side of C032q's closed-cone alternative, and proves no
unsmoothed Xi realization or all-degree sign. In particular neither
the entire lift alone nor finitely many odd-coefficient cancellations
is asserted to imply a moment. No finite-width stop is reopened.

## Proof

### Imported tools and the scope of the specialization

C032m supplies the entire functions and exact parity identity in (1).
C032q supplies the signed measure, its mass and the bounded
positive-real Laplace identity. We use these interfaces as proved;
we do not reconstruct the kernel or its width integration. C032k
Section2 provides the finite-law proof pattern, but its finite-sum
statement is not being applied directly to an arbitrary eta.

For exponential-moment holomorphy use Jean-Baptiste Boyer,
*The speed of convergence in the renewal theorem*, author manuscript
dated 19 June 2015,
[Definition2.1 and Lemma2.2 with proof, printed p.6](https://maths.jbboyer.fr/documents/articles/renewal.pdf).
For a Borel probability measure on R with a finite absolute
exponential moment of order c_0>0, the Fourier-Laplace transform
with integrand exp(-z*u) is holomorphic on |Re(z)|<c_0. No drift or
renewal hypothesis occurs in that lemma. We use z=s throughout.

For positive-real derivatives and their right limits at zero use
Ante Mimica, *Laplace transform*, course notes for Dresden,
27 April-1 May 2015,
[Definition1.1 and Remark1.2, p.5; Proposition1.4(i)-(ii), p.6, with proofs p.7](https://web.math.pmf.unizg.hr/~amimica/lt.pdf).
For a positive measure on [0,infinity) with finite Laplace transform
at every positive argument, part (i) identifies its nth derivative
there with the integral of (-u)^n exp(-s*u). Part (ii) identifies
finite moments with finite right derivative limits at zero, using
positivity and monotone convergence. These results include atomic
measures. The inspected proof cases and the convention comparison
are recorded in source notes1547; that coverage is reused.

The remaining tools are the identity theorem, Cauchy's coefficient
estimates and the monotone convergence theorem. Only their
applicability and the continuum output-law specialization are proved
below; no new general analytic theorem is claimed.

### One moment forces the full parity identity

Assume condition 3, and choose c_0>0 for which its integral is finite.
View the probability nu_eta as a Borel probability on R with zero
mass on (-infinity,0). Since |u|=u on its support, it has the absolute
exponential moment required by Boyer's lemma. The lemma gives

    g(z)=integral_X exp(-z*u) dnu_eta(u)

holomorphic on |Re(z)|<c_0, agreeing with L_eta on 0<s<c_0.
Choose r>0 with r^2<c_0. Then g(w^2) is holomorphic on |w|<r,
because |Re(w^2)|<=|w|^2<c_0 there. For real 0<w<r, (1) gives

    F_eta(w)=L_eta(w^2)=g(w^2).

The identity theorem on this disk makes the equality hold for every
|w|<r. Consequently F_eta(w)=F_eta(-w) on the disk. The entire
function F_eta(w)-F_eta(-w) then vanishes everywhere by the identity
theorem on C. This proves 3 implies 2. The second identity in (1)
gives 2 if and only if 1 without any additional assumption.

### Even-entire descent and the positive-output moments

Assume condition 2. Write the Taylor series of F_eta at zero as
sum_(k>=0) a_k*w^k. Evenness implies a_(2n+1)=0 for every n>=0.
Define

    f_eta(s)=sum_(n>=0) a_(2n)*s^n.                         (3)

This defines an entire function, not merely a formal substitution.
Indeed, fix any A>0 and take R>sqrt(A). Let
M_R=max_(|w|=R)|F_eta(w)|<infinity. Cauchy's coefficient estimate
gives |a_(2n)|<=M_R/R^(2n), and hence

    sum_(n>=0) |a_(2n)|*A^n <= M_R/(1-A/R^2)<infinity.

The series converges uniformly absolutely on |s|<=A. Since A was
arbitrary it has infinite radius, and termwise comparison with the
Taylor series of F_eta gives F_eta(w)=f_eta(w^2) on C. Uniqueness
follows because every complex s has a square root. Formula (1) now
gives f_eta(s)=L_eta(s) for every real s>0, and f_eta(0)=1.

We apply Mimica's proposition to nu_eta itself. It is a positive
Borel probability on X, so 0<=L_eta(s)<=1 for every s>0, exactly the
needed finiteness hypothesis. For each integer n>=1, part (i) gives

    (-1)^n f_eta^(n)(s)
        =integral_X u^n exp(-s*u) dnu_eta(u), s>0.          (4)

Here the derivatives of f_eta restricted to the positive real axis
agree with the ordinary derivatives of L_eta because the two
functions agree on that interval. The positive-s differentiation
does not require any undamped moment to be known in advance.

The entire function f_eta has continuous derivatives at zero.
Thus the left side of (4) has the finite limit
(-1)^n f_eta^(n)(0) as s decreases to zero. By part (ii) of the
cited proposition this is m_n. Explicitly, the nonnegative
integrands u^n exp(-u/k) increase to u^n as k increases to infinity,
so the monotone-convergence limit in (4) is precisely the moment
integral, including any atom at zero. The finite analytic limit
makes that integral finite. For n=0 the same identity is simply
m_0=nu_eta(X)=1=f_eta(0). This proves the first formula in (2).

For any fixed c>0, the partial sums

    P_N(u)=sum_(n=0)^N c^n*u^n/n!

are nonnegative and increase pointwise on X to exp(c*u). Positivity
of nu_eta and monotone convergence, followed by the entire Taylor
series (3) evaluated at -c, give

    integral_X exp(c*u) dnu_eta(u)
       =lim_(N->infinity) sum_(n=0)^N c^n*m_n/n!
       =sum_(n>=0) (-c)^n*f_eta^(n)(0)/n!
       =f_eta(-c)<infinity.

The last series converges absolutely since f_eta is entire; each
term in the preceding moment series is nonnegative. Thus the
extended-valued integral from monotone convergence is actually
finite. This proves 2 implies 4 and the second formula in (2).
Finally 4 implies 3 by choosing, for example, c=1. All equivalences
are proved.

All moment integrals and monotone limits above are taken against
the positive output measure nu_eta. There is no integration of
u^n or exp(c*u) through eta, no subtraction of infinite component
moments, and no uniform tail hypothesis on the width family. The
bounded Laplace test in (1) is the only output/width interchange
used. The hypotheses therefore suffice for the proposed continuum
specialization, with the independent existence and Xi gaps unchanged.

### Conceptual audit1550 (18 November 2026)

The complete proof above passes an independent critical check under the
unchanged SPECIALIZE assessment1548, separately approved in turn1549.
No mathematical correction or additional hypothesis is required. The
inspected Boyer/Mimica statements and proof cases in source-notes1547
are reused; this is not verification of the underlying preprints.

1. **The inherited interfaces suffice.** C032m's compact-disk bounds
   are integrable against each Jordan part of every fixed finite eta.
   They supply entire F_eta and J_eta, the mass value F_eta(0)=1,
   and exactly the sign -2 in (1). C032q's signed construction gives
   a finite Borel output with mass one. Its assumed nonnegativity
   therefore makes it a probability, including at the endpoint zero.
   For each s>0 the test exp(-s*u) is bounded and continuous on X,
   so C032q authorizes (1) without any component moment. No common
   bound on V, continuity of set evaluations, or density is needed.

2. **One moment gives global evenness.** Extension of nu_eta by zero
   to the negative half-line preserves its probability mass, and
   exp(c_0*|u|)=exp(c_0*u) on its support. These are exactly Boyer's
   probability and absolute-exponential-moment hypotheses. His
   integrand is exp(-z*u), so z=s is the correct convention. For
   |w|<r and r^2<c_0, |Re(w^2)|<c_0; consequently g(w^2) is
   holomorphic on the entire disk, without selecting a square-root
   branch. Equality on 0<w<r has an accumulation point inside the
   disk, so the identity theorem applies there. It first proves
   local evenness, then applies to the entire difference
   F_eta(w)-F_eta(-w). No continuation of the integral outside
   Boyer's strip is asserted. The parity identity gives full
   complex J_eta=0, not merely a finite coefficient condition.

3. **The descent is entire.** Evenness eliminates precisely the
   odd Taylor coefficients. For each A>0, the finite maximum M_R
   on a circle with R>sqrt(A) bounds the descended series by
   M_R*sum_n(A/R^2)^n. This proves uniform absolute convergence on
   every closed s-disk and hence an entire f_eta. Comparing the
   convergent series gives F_eta(w)=f_eta(w^2) for every w.
   Surjectivity of w -> w^2 proves uniqueness. Formula (1) gives
   f_eta=L_eta on the positive axis and f_eta(0)=1. There is no
   bound on M_R as R grows and none is required for this argument.

4. **The derivative and moment limits use positivity correctly.**
   Mimica's finiteness premise holds since 0<=L_eta(s)<=1 for s>0.
   The derivatives of the entire f_eta restricted to that interval
   are the ordinary derivatives of L_eta. For each fixed positive
   s_0, the damped powers u^n exp(-s*u) are bounded for
   s in [s_0/2,3*s_0/2]; no undamped moment is being assumed in
   applying the cited differentiation theorem. Its sign is exactly
   (-1)^n. On s=1/k, u^n exp(-u/k) increases to u^n for n>=1.
   Monotone convergence against nu_eta identifies that integral
   with the finite limit (-1)^n f_eta^(n)(0). An atom at zero
   contributes zero for n>=1; it is counted in m_0=1 with u^0=1.
   Thus neither a zero atom nor a singular part is lost.

5. **Every exponential order, with the claimed value.** For each
   fixed c>0 the exponential partial sums are nonnegative and
   increase pointwise, including at zero. Their integrals equal
   sum_(n<=N) c^n*m_n/n!. The proved derivative identity turns
   this into the Taylor partial sum of f_eta at -c, since
   c^n*m_n=(-c)^n*f_eta^(n)(0). Entirety makes its limit finite
   for every c>0. Monotone convergence therefore yields precisely
   integral exp(c*u) dnu_eta=f_eta(-c), rather than merely a
   formal analytic continuation. Taking c=1 also verifies the
   trivial implication from every order to some order.

Both monotone limits and all unbounded tests above concern only the
positive output law. Nothing passes u^n or exp(c*u) through the signed
width measure, and no infinite positive and negative component moments
are subtracted. The statement is valid separately for each finite V;
it contains no estimate uniform over all eta. C032m and C032q remain
the direct mathematical inputs; C032k is a compared proof pattern,
not an extra finite-width hypothesis. All fixed-v1, actual-divisor,
multiplicity, counting, finite-zero and heat-positivity qualifications
are retained. No feasibility, actual cone membership, source-wide
verification, unsmoothed Xi transfer or RH conclusion follows from
this audit. This is validation of the local specialization of known
tools, not progress beyond those source theorems.

## Mathlib

Full matching coverage has not been checked and remains unknown.
No Mathlib theorem is imported. General holomorphic-function,
measure, derivative and monotone-convergence APIs are not asserted
to supply the complete qualified continuum statement. The cited
analytic tools and the inherited preprint inputs remain the
mathematical references for this informal proof.
