# Corollary C033l: finite Laplace separation for capped signed widths

## Hypotheses

Retain C032j's actual-zero normalization and external-input
qualifications. Thus Z+ is the multiset of positive-ordinate nontrivial
zeta zeros, counting multiplicity, z_rho=gamma_rho-i*(beta_rho-1/2),
and, for sigma in W=[1,2] and t,s>0, use precisely

    H(u)=sum_(rho in Z+) exp(-u*z_rho^2),
    ell_sigma(t)=H(t/(1+4*sigma*t))/(t*sqrt(1+4*sigma*t)),
    B_sigma(s)=integral_0^infinity (1-exp(-s*t))*ell_sigma(t) dt,
    integral_X exp(-s*u) dnu_sigma(u)=exp(-B_sigma(s)),
    X=[0,infinity).

Here nu_sigma are C032j's Borel probability laws with zero drift and
killing. Keep the divisor/conjugation and multiplicity conventions,
exclusion of ordinate zero, strip |beta-1/2|<1/2, first-zero bound
gamma>14, counting N(T)=O(T log(T+2)), verified zeros through height
100, retained real zero in (14,15), heat positivity, and both fixed-v1
preprint qualifications. Sigma is Gaussian half-variance. The
preprints and finite-zero data are not independently verified here.
All qualifications of C033j's audited exclusion remain in force,
including its inherited separate j=0,1 heat-error inputs from C032s.

Use C032m's jointly continuous entire lifts b_sigma and C032q's
identification b_sigma(sqrt(s))=B_sigma(s) for real s>0. For every
finite real signed Borel measure eta on W, use C032q's signed law

    nu_eta(A)=integral_W nu_sigma(A) deta(sigma), A Borel in X.

It has mass eta(W), total variation at most |eta|(W), and the bounded
Borel integration identity of C032q. Atoms, infinite support and
singular continuous parts of eta are allowed.

Fix exactly C033i's residual: L(dt)=ell_1(t)dt on (0,infinity),
I=[1,3/2], and R=L restricted to (0,infinity)\I. Let mu be its Borel
probability law with zero drift and killing, so

    muhat(s)=integral_X exp(-s*u) dmu(u)
            =exp(-integral_(0,infinity) (1-exp(-s*t)) dR(t)).

This is the same mu excluded from the entire finite real signed
width range by C033j, not an approximation to it. Define

    A_2={eta : eta real finite signed Borel on W,
               eta(W)=1, |eta|(W)<=2}.

No positivity of eta, p_sigma or nu_eta, absence of zero atoms,
moment condition, full odd cancellation J_eta=0, RH or unsmoothed
actual-Xi realization is imposed.

## Conclusion

There exist an integer n>=1, positive real numbers s_1,...,s_n,
a nonzero vector (a_1,...,a_n) in R^n, and a real epsilon>0 such that

    sum_(j=1)^n a_j*muhat(s_j)
      >= epsilon + sup_(eta in A_2)
           integral_W sum_(j=1)^n a_j*exp(-B_sigma(s_j)) deta(sigma).
                                                               (1)

Equivalently, the bounded continuous real test

    h(u)=sum_(j=1)^n a_j*exp(-s_j*u), u in X,

satisfies integral h dmu >= epsilon + sup_(eta in A_2) integral h dnu_eta.
The supremum is finite and attained. Both statements concern the full
continuum signed class A_2, not a finite width grid or positive subclass.

This is qualitative existence only. No number of tests, locations,
coefficients, numerical margin, effective error bound or evaluation
algorithm is supplied. Coefficients may have either sign. It gives
no uniform separator for unrestricted total variation, no closed-image
claim for that uncapped class, and no positive inverse, moment payment,
full odd cancellation, actual-Xi positivity or RH conclusion. The
result is a specialization of known compactness and separation tools,
not a claim of mathematical novelty. Application audit1751 below passes
under these unchanged qualifications.

## Proof

### Cited tools and exact scope

The unchanged SPECIALIZE assessment1747 and source-notes1748 cover
this precise target. Import the following results from Theo Buhler
and Dietmar A. Salamon, *Functional Analysis*, version 11 May 2016,
[author text](https://math.jhu.edu/~js/Math637/eth.functionalanalysis.pdf):

- Example 1.3.7, printed p.28: the isometric identification of the real
  dual of C(M) with finite signed regular Borel measures, with total
  variation norm, for second-countable compact Hausdorff M.
- Theorem 3.2.4 and proof, p.100: Banach--Alaoglu weak-star compactness
  of the dual unit ball; scaling gives any fixed finite-radius ball.
- Remark 3.2.13(i), p.104: the closed-set finite-intersection
  characterization of compactness.
- Corollary 2.3.19 and proof, p.68: strict uniform separation of two
  disjoint nonempty convex sets in a real normed space when one is
  closed and the other compact. We use only its Euclidean case.

For Laplace uniqueness import Ante Mimica, *Laplace transform*,
Dresden course, 27 April-1 May 2015,
[Proposition 1.8 and proof, printed pp.9-10](https://web.math.pmf.unizg.hr/~amimica/lt.pdf).
Finite positive Borel measures on [0,infinity) are determined by
their positive-real Laplace transforms. We use the uniqueness theorem,
not the source's inversion display at zero. Its signed application and
the zero-atom issue are checked below. These known general theorems
are not reproved. The remaining proof verifies their exact hypotheses
and the connection to the qualified residual and width family.

### The entire capped signed class is compact and convex

Let E=C(W;R) with supremum norm. The compact metric interval W is
second-countable and Hausdorff. Every finite positive Borel measure
on W is regular, and applying this to the Jordan parts gives the
signed case; this is the compact-metric regularity input already used
in C032q. Thus the cited signed Riesz identification applies to all
the signed Borel measures in A_2, including their singular parts.
The functional associated to eta is f -> integral_W f deta, and its
dual norm is exactly |eta|(W), not merely bounded above by it.

Use the weak-star topology sigma(E*,E). Banach--Alaoglu makes the
closed dual ball of radius 2 compact in this topology. Evaluation at
the constant function 1_W is weak-star continuous, so the condition
eta(W)=1 is weak-star closed. Consequently A_2 is a closed subset of
that compact ball and hence compact. It is nonempty because delta_1
has mass and total variation one. It is convex: for 0<=theta<=1,
mass is preserved by theta*eta+(1-theta)*eta', and its total variation
is at most theta*|eta|(W)+(1-theta)*|eta'|(W)<=2. No reduction to
positive measures or finitely supported measures has occurred.

### Continuous Laplace coordinates and all-Borel uniqueness

For each real s>0 set

    k_s(sigma)=exp(-B_sigma(s))=exp(-b_sigma(sqrt(s))).

C032m's joint continuity, together with C032q's identification at
the positive square root, proves k_s in E, including both width
endpoints. It is real and 0<k_s<=1 because it is the Laplace
transform of the probability nu_sigma and B_sigma(s) is finite.
C032q applies to f_s(u)=exp(-s*u), which is bounded and continuous
on all of X, to give

    integral_X f_s dnu_eta=integral_W k_s deta.            (2)

Thus eta -> integral_W k_s deta is weak-star continuous and is
exactly the required signed output coordinate. No unbounded moment
or limit under an infinite signed mixture is being used.

For clarity, equality of all these output coordinates really does
identify signed measures on X. Suppose finite real signed measures
rho and tau have the same Laplace transform for every s>0. Let
zeta=rho-tau, and take its Jordan parts zeta^+, zeta^-. Both are
finite positive Borel measures, and bounded integration gives

    integral_X exp(-s*u) dzeta^+(u)
      = integral_X exp(-s*u) dzeta^-(u), s>0.

Apply Mimica's positive uniqueness theorem to these two measures;
it yields zeta^+=zeta^- on every Borel subset of X, hence rho=tau.
There is no loss at zero: independently, dominated convergence
against each finite Jordan part as s tends to infinity gives
lim integral exp(-s*u) dzeta^±(u)=zeta^±({0}), so equality of the
positive-real transforms also fixes their zero atoms. The domination
is by 1, and no inversion formula at zero is needed.

For s>0 define the closed subset of A_2

    F_s={eta in A_2 : integral_W k_s deta=muhat(s)}.

If an eta belonged to the intersection of all F_s, (2) and the
signed uniqueness just checked would give nu_eta=mu on every Borel
set, including zero. This contradicts C033j's audited exclusion of
this exact mu from all finite real signed width measures on W.
Therefore the intersection of F_s over all positive real s is empty.

### Finite reduction and strict separation

The family (F_s) consists of closed subsets of the compact space
A_2. By the cited finite-intersection characterization, its empty
total intersection implies that some finite subfamily has empty
intersection. Since A_2 is nonempty, this subfamily has n>=1
members, with indices s_1,...,s_n>0. No countability or metrization
of the weak-star topology is needed for this implication.

Define the linear coordinate map and residual vector

    T(eta)=(integral_W k_(s_1) deta,...,integral_W k_(s_n) deta),
    y=(muhat(s_1),...,muhat(s_n)),
    K=T(A_2) subset R^n.

Each coordinate of T is weak-star continuous, so K is compact.
It is nonempty and convex because A_2 is nonempty and convex and
T is linear. In the Euclidean space R^n a compact set is closed.
The chosen empty finite intersection says precisely y not in K.
Hence K and the singleton {y} satisfy all hypotheses of the cited
strict-separation corollary: they are nonempty, disjoint and convex,
with K closed and {y} compact.

Choose the orientation of its nonzero real functional so that,
writing that functional as x -> a dot x,

    M:=sup_(x in K) a dot x < a dot y.

The supremum is finite and attained, since K is compact and the
functional continuous. Set epsilon=a dot y-M>0. The defining
equalities for T and y give exactly (1), including its orientation
and its uniformity over every eta in A_2. Finite linearity in (2)
gives the equivalent bounded-test statement; |h(u)|<=sum |a_j|
makes all its signed integrals finite. Attainment in K also gives
attainment by at least one eta in A_2 by the definition of K. This
completes the qualitative specialization. No estimate of epsilon
or constructive choice of s_j or a_j was used. ∎

The common variation bound is essential to this argument's
compactness step. C033j's stronger exact exclusion for arbitrary
finite variation does not let this proof take a union of the caps
and keep a common finite separating test or positive margin. The
earlier fixed-dictionary enclosure limit1571 is a comparison only:
it neither constructs nor refutes the separator proved here.

### Application audit1751 — 19 November 2026

Verdict: the qualitative specialization passes the exact audit in
SPECIALIZE assessment1749, separately approved1750. No hypothesis,
conclusion, numerical bound or proof step needs correction. This is
verification of an application of known theorems, not a new theorem
beyond the sources checked. Primary theorem coverage in that assessment
and source-notes1748 is reused; no external preprint or zero-data audit
is inferred. The complete proof above was checked against the following
interfaces.

1. **Full signed input class.** W is a compact metric interval, so every
   finite Borel Jordan part is regular. Example1.3.7 therefore identifies
   every allowed signed eta with a real functional on C(W), with exact
   norm |eta|(W). Conversely every functional in the radius-2 ball is
   represented by such a signed measure. There is no missing nonregular
   or singular-input case. Evaluation at 1_W is weak-star continuous;
   intersecting its closed mass-one level set with the compact ball is
   legitimate. The nonemptiness witness delta_1 and the stated convexity
   estimate both obey the mass and variation constraints. Sequential
   compactness or an atomic approximation is not substituted for the
   compactness needed below.

2. **Continuous coordinates with the exact normalization.** C032m supplies
   joint continuity of b_sigma on the closed width interval, and C032q's
   positive-square-root identity identifies its exponential with the
   Laplace transform exp(-B_sigma(s)). Thus each k_s is a real member of
   C(W), including sigma=1,2. C032q's bounded Borel integration identity
   applies to exp(-s*u) on the whole half-line and gives precisely (2)
   for all finite signed eta. No unbounded moments or positivity of
   eta, p_sigma or nu_eta enter this passage.

3. **Exact exclusion and zero.** The difference nu_eta-mu is a finite
   real signed Borel measure. Equality of all positive-real transforms
   gives equal transforms for its finite positive Jordan parts; Mimica's
   uniqueness theorem applies to those parts. The separate dominated
   limit as s tends to infinity retains their atoms at zero, using the
   bound 1 for each part. The argument neither uses the source's inversion
   display at zero nor discards zero before deconvolution. C033i and
   C033j refer to exactly the residual Levy restriction outside [1,3/2],
   with zero killing and drift. Hence their audited all-Borel exclusion
   applies to this mu, not to a nearby or moment-matching output.

4. **Finite reduction.** Every F_s is relatively closed in A_2 by the
   preceding coordinate continuity. An eta in their total intersection
   would violate C033j by item3, so that intersection is empty. The
   closed-set finite-intersection property on compact A_2 supplies a
   finite empty subintersection. It has at least one member because
   A_2 itself is nonempty. This handles the uncountable index set s>0
   without a hidden countability assumption.

5. **Uniform strict inequality.** T has finitely many continuous real
   coordinates. Its image K is nonempty, compact and convex in R^n,
   therefore closed; the selected finite constraints give y outside K.
   Strict separation applies to K and {y} with exactly the cited
   hypotheses. Reversing the functional if necessary gives
   M=sup_K a dot x<a dot y; strictness forces a nonzero. Compactness
   gives finite attained M, so epsilon=a dot y-M is strictly positive
   and (1) follows with the displayed orientation. A maximizer in K has
   a preimage in A_2 by definition of K. Finite linearity and
   |h|<=sum |a_j| justify the equivalent signed bounded-test statement.

All direct mathematical inputs already appear in the DAG; C032s is
retained through C033j's qualified exclusion, not independently reapplied
in this audit. No dependency change is needed. The achieved threshold
is a positive existential gap for this single fixed cap. Neither its
value nor its tests are constructed. The result supplies no common
separator as the cap tends to infinity, no closed unrestricted image,
no odd cancellation, moment payment, actual-Xi realization or RH sign.
The fixed-dictionary/independent-box failure1571 is unchanged and has
not been retried. Full matching Mathlib coverage remains unchecked.

## Mathlib

Full matching coverage of this qualified actual-width/residual
specialization has not been checked and remains unknown. Supporting
signed Riesz, Banach--Alaoglu, compactness, finite-dimensional
separation and Laplace-uniqueness APIs have not been assessed in this
step. No formal verification of this proof, the fixed-v1 preprints
or the finite-zero inputs is claimed.
