# Actual contact head via a finite-interval Laplace remainder: review910

TARGET: Assess whether a finite-interval Laplace remainder representation of C466b's frozen contact weight proves F_U>=0 at U=100 for the actual reciprocal-Xi density, retaining all endpoint terms and without assuming global PF or real-rooted P.
CHECKED: 2026-11-14
DECISION: EXPLORE
SEARCH_EVIDENCE: Review910 searched exact reciprocal-Xi/contact-head statements, finite Laplace derivative endpoints, Stieltjes/Pade error formulas and Peano kernel signs; inspected the primary statements and essential cases below. Reused assessment889 and the variation/scalar/cumulative stops; no exact actual-head theorem was located, without any novelty inference.
SOURCE_EVIDENCE: Allen--Chui--Madych--Narcowich--Smith (1974), pp264,266-268, Theorem2 (10)-(11), Corollary3 and its orthogonality/positive-weight argument; Hunter, The Riemann Integral, Theorem1.53 and proof p32; DLMF1.14(iii), (1.14.27)-(1.14.29), including the jump case; Komisarski--Wasowicz arXiv:1612.08086v1, Section2 Peano Kernel Theorem and complete Proposition3 proof pp4-5. Reused C466a/b's already assessed density/kernel imports.
COMPARISON: Finite integration by parts applies to the smooth actual density but supplies no sign; the contact-endpoint jet must remain. The inspected Pade theorem needs a positive measure and orthogonality for that same measure, not the signed derivative contact data. The inspected Peano theorem needs polynomial annihilation and a separately signed kernel; these are not established by C466b(4).
GAP: No source proves F_100>=0. Isolate the full contact-endpoint contribution in the finite transform of C466b(14), and test its comparison with the remaining integral using all contact null-row relations; no endpoint-corrected formula or inequality is derived in this review.
REASON: Essential source comparison is adequate for one bounded actual-density endpoint/remainder attempt. Citation alone does not settle that specialization; automatic positive-measure and Peano imports are parked. This is coverage preparation, not new mathematics or approval of a sign.
SCOPE: Exactly C466b's actual-density and hypothetical first-contact hypotheses, arbitrary finite m>=2 and U=100; retain multiplicities and remove only the stated first-zero occurrence. Cover finite integration by parts and a test of its complete signed remainder, without a model substitution, global PF, real-rooted P, new zero-free estimate or numerical source certificate.
COVERED_TARGET: Test whether the endpoint-corrected finite Laplace representation of C466b(14), with all contact null-row relations retained, proves F_100>=0 for the actual reciprocal-Xi density; stop at the exact unresolved signed remainder if its sign cannot be established.
LITERATURE_REASON: Invocation-start REVIEW_REQUIRED concerned a changed signed finite-head observable outside assessment906 and the prior scalar/contact comparisons; this turn supplies its missing primary remainder coverage, without reopening the blocked Mobius route.

## Completed primary comparison, 14 November 2026, step910

This is a literature-only EXPLORATION. No actual head inequality,
finite-transform identity, counterexample or new lemma is established.
The source search now supports the single COVERED_TARGET above. That
new continuation is to receive the supervisor's separate approval
before mathematical invocation; no correctness claim is made by this
coverage decision.

### Inspected statements and essential cases

1. G. D. Allen, C. K. Chui, W. R. Madych, F. J. Narcowich and
   P. W. Smith, *Pade approximation and orthogonal polynomials*,
   Bulletin of the Australian Mathematical Society **10** (1974),
   263-270, [publisher primary PDF, DOI 10.1017/S0004972700040879](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/A56674619ABE0C4A0641B6815FB44B29/S0004972700040879a.pdf/pade_approximation_and_orthogonal_polynomials.pdf).
   Page264 (2)-(3) assumes a positive measure on [0,infinity),
   infinite support and its moments. Theorem2, p267 (10)-(11),
   represents the [N,N-1] approximant and error using its orthogonal
   polynomial. Read the p266-267 argument identifying the polynomial
   through its integral orthogonality, and Corollary3, p268 (14),
   where Gaussian weights are positive. Neither an arbitrary
   differential-operator square nor contact jets supply those
   hypotheses. C466b's P is not established to be orthogonal for a
   positive measure representing the proposed remainder. Choosing
   positive p(y)dy as a measure would still require that identification;
   choosing V(t)dt would lose positivity. No Pade bound is imported.

2. John K. Hunter, *The Riemann Integral*, Chapter1,
   [UC Davis primary notes](https://www.math.ucdavis.edu/~hunter/m125b/ch1.pdf),
   Theorem1.53 and proof, printed p32. For real f,g continuous on
   [a,b], differentiable inside, with integrable derivatives, it states

       integral_a^b f g' = f(b)g(b)-f(a)g(a)-integral_a^b f' g.

   Read the product-rule/fundamental-theorem proof. Smooth p and
   real exponential factors on [0,x_*] meet these regularity hypotheses
   at every finite derivative order. Repeated use is a standard tool;
   the contact-specific finite sum and any sign remain to be proved.
   Zero-endpoint flatness does not remove data at the other endpoint.

3. [NIST DLMF1.14(iii), Derivatives](https://dlmf.nist.gov/1.14#iii),
   (1.14.27)-(1.14.29), inspected 2026-11-14. The first formula assumes
   continuity on [0,infinity) and piecewise-continuous derivative;
   the higher formula assumes continuity and exponential bounds
   (1.14.18) through order n-1 and piecewise continuity at order n.
   Formula (1.14.28) explicitly retains jumps for piecewise smooth
   functions. These are infinite-interval formulas, not a license to
   truncate derivatives while suppressing the cutoff data. The finite
   interval can instead be handled by Hunter's theorem. No global
   derivative growth assumption on actual p is needed for that tool.

4. Andrzej Komisarski and Szymon Wasowicz, *Inequalities between
   remainders of quadratures*,
   [arXiv:1612.08086v1, Section2](https://arxiv.org/html/1612.08086v1#S2),
   Peano Kernel Theorem, PDF p4, and Proposition3 proof, pp4-5.
   For r>=2 the recalled theorem concerns a continuous linear
   functional E on C[a,b] annihilating all polynomials through degree
   r-1. Its kernel is E[(.-u)_+^(r-1)/(r-1)!], and for f in C^r it
   represents E[f] as the integral of f^(r) against that kernel.
   A one-sign kernel gives a mean-value remainder. Read the complete
   Proposition3 proof: polynomial exactness and the kernel sign are
   checked separately on both pieces of [0,1], then symmetry supplies
   [-1,0]. Thus a representation alone supplies no sign. For the
   proposed contact functional, neither polynomial annihilation nor
   such a kernel sign is established; a C[a,b]-bounded extension of
   an endpoint-derivative functional must also be justified before
   applying this version. No quadrature inequality is imported.

### Scope, overlap and access qualifications

C466b(4) supplies one zero H-weighted integral, not the polynomial
exactness hypothesis in the Peano statement. Its endpoints V(0)=V(x_*)=0
do not state that all intermediate p-derivatives at x_* vanish.
C466c already refutes inferring real roots from the relaxed finite
contact signs. These are applicability comparisons, not a newly derived
remainder identity, actual-density counterexample or impossibility
theorem. C466d/e's scalar-law stops and the cumulative/variation stops
remain contrasts with precisely their existing scope. No model is
substituted for actual p, and no claim about actual head failure follows.

The explicit source searches used: `Pade approximants Stieltjes function
error formula orthogonal polynomial positive measure Markov theorem
remainder integral`; `finite Laplace transform derivatives endpoint
terms integration by parts formula`; `Peano kernel theorem positive
remainder sign kernel linear functional derivatives finite interval`;
`"finite Laplace transform" "f(T)"`; `"finite Laplace" "f(L)"`;
`"generalized Peano kernel theorem" "differential" operator`;
`"finite contact" "reciprocal" Xi "Laplace" remainder`;
`"Pade" "signed measure" "remainder" "positivity"`;
`"finite Laplace" "Hankel" "contact" density`.
Exact/stronger-result searches yielded no matched actual-contact theorem.
Unrelated search hits were not mathematical evidence. The local screen
was confined to the 14 November contact/Volterra assessments and stops,
then the relevant C466a/b/c/e ranges and assessment903's source-block
description. Assessment889's inspected positive-raw-minor comparison
was reused, not re-browsed. No sibling notebook was read.

Buschman's *Finite Laplace Transformation* (1991), the Brass--Petras
book mirror, and Ferguson (1973), DOI10.1137/0710087, were discovery
leads. Publisher retrieval of Buschman failed; the book mirror returned
403; Ferguson supplied only an abstract/access page. PDF screenshots
through this interface yielded no visible images, and shell downloads
failed DNS. They are not inspected theorem inputs. Allen's extracted
orthogonality/measure hypotheses and the HTML Peano statement/proof
were readable. No claim depends on a poorly rendered Allen formula.
Hunter's complete finite-interval theorem and the readable Peano
comparison remove any essential dependency on these blocked leads;
do not retry them merely to fill a literature turn. Mathlib coverage of
the full matching remainder/sign target remains unchecked.

### Bounded continuation and outcome

Use essential input C466b(14) and its contact kernel equations with
C466a's actual p and inherited L018 convention. Keep the externally
cited zero-counting, verified-low-zero and multiplicity qualifications.
The bounded test is the actual F_100>=0 inequality, not positivity of a
raw moment determinant or of an infinite-interval substitute. First
derive the complete finite formula using the cited elementary tool;
then test the resulting signed remainder against the contact relations.
Retain both endpoint evaluations before using flatness, and preserve
all remaining contact-endpoint data. No positivity of raw moment forms,
real-rooted P, endpoint cancellation, tail sign or global PF is a premise.

Continue only if those hypotheses prove the required weak head sign
or isolate a quantitatively precise additional endpoint/remainder
obligation. If contact algebra does not sign it, record that limitation
and stop this bounded attempt; an identity by itself is not ADVANCE.
Do not replace a missing actual bound with a generic numerical density.
Even a proved weak head sign would leave C466b(7)'s first-zero term,
full tail, strict forcing, simultaneous contacts, propagation and L030
transfer unpaid. No complete candidate is suggested.

The automatic Pade/Peano citation route is parked; the actual finite
endpoint comparison is a still-untested specialization. It is not yet
a justified creative mechanism. Source coverage is now prepared, so
the intended subsequent work is one mathematical attempt after the
separate continuation approval, not another broad literature search.
Classification of this completed source review is NOVELTY_UNCHECKED;
EXPLORATION reports completed essential comparison and an isolated
test, not progress beyond the inspected theorems or a new sign result.

## Original nomination specification (preserved, preceding review910)

The pending-review language below records the original nomination only;
the completed fields and comparison above are the current assessment.

The main gap remains L030-L032/C032a actual-Xi algebraic-square
positivity. C466g supplies an audited boundary initialization for the
stated growing range, but no propagation law. The proposed intermediate
target is only the nonnegative head term F_U in C466b(7). Even if
established, it would leave S_+-S_-, the full tail J_U, the strict
inequality in (7), simultaneous contacts and propagation unpaid.
A head sign is potentially useful in that exact signed budget;
it is neither a contact barrier nor a route completion by itself.

Use p, x_*, V, the frozen real monic polynomial P and R_U exactly as
defined in C466b. In particular

    F_U = integral_0^{x_*} (-R_U'(t)) V(t) dt,  U=100.

The proposed observable to compare with primary theorems is

    F_*(z) = integral_0^{x_*} exp(-zt) V(t) dt.

Seek a finite-interval Laplace/Green-function or Pade remainder
representation using C466b(14)'s differential-operator square and
the actual contact equations. This is a source-search specification,
not a formula or sign derived in this turn. All endpoint terms at
x_* must be retained: p's flatness at zero does not make its jet at
x_* vanish. Establish the meaning of any positive measure before
applying a positive remainder theorem. Do not identify signed density
derivative minors with positive raw moment minors or assume P has
real roots. C466c records the exact failure of that finite-jet inference.

Reuse the relevant earlier comparisons rather than repeat them:

- C466b and assessments884/886 give the scalar equation, signed-weight
  obstruction and actual-H qualifications. Assessment888/step889 parks
  automatic bell-shape/variation-diminishing control.
- C466c and assessment889/step890 distinguish positive raw moment
  determinants from signed contact determinants. Bakan--Berg,
  arXiv:1605.01196v2 Section5.3, is an inherited comparison, not an
  already applicable remainder theorem for this functional.
- C466d/e and ATTEMPTS898 show downward crossings for generic scalar
  laws even with the specified integer-pole structure. They neither
  supply the actual F_U nor refute its proposed sign; any purported
  universal inference must confront these models.
- Assessment898/step899 parks cumulative dominance without its
  missing cumulative premise. No such dominance is assumed here.
- Assessment903's Mobius/subordination proposal remains source-blocked;
  C466f stops fixed-head global relative domination. The new target uses
  the already defined finite zero head R_U and does not depend on the
  unread Polson source or reciprocal-series continuation.

Essential input ID is C466b, with C466a's qualified density and
inherited L018 convention. C466g supplies boundary motivation only;
C466c-e are obstruction comparisons, not sign inputs. Retain external
counting and verified-low-zero qualifications; this nomination replays
no zero data and adds no premise on the unverified zeros.

Bounded continuation test: find applicable primary hypotheses and
essential proof cases reaching F_U>=0, or isolate one endpoint or
signed-remainder obligation suitable for a subsequent independently
testable attempt. If the only applicable theorem assumes global PF,
real-rooted P, positive raw moment determinants or drops endpoint
data, record that exact mismatch. A formal identity alone is not
head-sign progress. Do not derive or approve a new remainder formula
during the literature turn. An informative obstruction need not refute
the actual-density inequality.

Creative discovery is prioritized through this concrete signed-head
proposal, but a viable positivity mechanism is not established yet.
Primary coverage and a discriminating remainder test must precede any
proof_attempt/creative nomination. A routine transform identity should
not receive that label. This assessment is deliberately not ready;
matching Mathlib coverage is unchecked. No lemma, mathematical script,
new sign or new source theorem was produced in this nomination.
