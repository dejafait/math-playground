# Whole-contour propagation after finite pole cancellation: source comparison

TARGET: Review whole-contour propagation for C744t using a finite product that cancels every pole in the continuation domain and retains the unweighted cluster integral.
CHECKED: 2026-11-11
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step525 searched finite-pole cancellation, meromorphic propagation of smallness and three-circle continuation; read the primary statements and essential cases below. Local exact-claim search found C744s, C645d and L651's finite rational grid cancellation as relevant comparisons, not a matching full-contour length theorem. Reused steps518/520/524; no novelty inference.
SOURCE_EVIDENCE: Newly inspected Beck et al. Section7.4 Theorem7.4.8 and proof https://complexanalysis.org/web/sec_singularities.html ; reread Boas Math618 23 April2004 p.1 SectionI(1)-(2), proof discussions1-2 https://haroldpboas.gitlab.io/courses/618-2004a/apr23.pdf ; Beck Section8.1 Theorems8.1.5/8.1.7(1) and proofs https://complexanalysis.org/web/sec_residue-thm.html ; Pope Section5.4 pp.130-132 (5.180)-(5.181) https://people.tamu.edu/~c-pope/methods_pages2011.pdf ; Kalmykov-Nagy author PDF Theorem1(14) pp.12-13 https://www.math.u-szeged.hu/pot/Kalmykov_Nagy_1.pdf . Suzuki and complete-count coverage are reused unchanged from step520.
COMPARISON: Standard pole factorization covers local holomorphic cancellation and Hadamard covers propagation once domain bounds exist. Neither gives the proposed complete-domain bounds or division cost for C744t. The stronger Gonchar-Grigorjan-type component estimate requires the whole boundary norm already; its constant depends on domain and pole region. No cited theorem directly supplies the requested length.
GAP: The mathematical specialization must choose a count-bounded padded domain, cancel every pole on a neighborhood, pay the infinite exterior series and an H-independent holomorphic upper bound, cover all Gamma, and pay a positive product lower bound there before using C744t's ORIGINAL unweighted integral. No such bound or length is established by this review.
REASON: Changed-scope source coverage is complete for one bounded established-method test; general pole cancellation and three circles must be cited, not reproved. Readiness concerns inputs only. All domain, product, horizon and strict-budget estimates remain research obligations, with no internal separation or weighted-residue sign as an input.
LITERATURE_REASON: The invocation-start target was REVIEW_REQUIRED and added cancellation on a larger domain plus division on Gamma, beyond C744s's isolated-pole scope. This review supplies that missing comparison while reusing unchanged pairing, count and phase coverage.
SCOPE: Literature comparison only in step525. The separate continuation assessment is drafts/literature/2026-11-11-cluster-pole-product-test-525.md; its exact TARGET and qualifications define the proposed later mathematical work. No new mathematical result was derived in this review.

The nomination below preserves the pre-review proposal and its original
pending status. The completed comparison after it supersedes that status.

The main gap is still actual-Xi positivity. The proposed intermediate
target concerns the unpaid analytic interface of the now audited C744t,
not an independent sign theorem. Its plausible use is a conditional
finite-window detector length under the existing complete-count,
profile and strict-slack data. Even success would leave the universal
finite-window signs, C744q margin, non-neutral coverage and assembly open.

## One bounded later test, not performed in step524

Compare the following proposed construction with primary results on
holomorphic continuation and finite pole cancellation. In a bounded
domain joining a starting disk in Re(s)>1/2 to the whole C744t circle,
seek a finite product canceling every actual pole, including all cluster
poles. The count must cover the full domain; the remaining infinite
series must be holomorphic on a neighborhood with a paid uniform bound.
Propagation would apply to the resulting holomorphic function, and
division on Gamma would have to recover a bound on the ORIGINAL
G-J_H. Both the product's upper cost on the propagation domain and
its positive lower cost on Gamma must be paid from stated data.

The discriminating threshold is a finite horizon at which
sup_Gamma|G-J_H|<alpha/r under the fixed-window nonnegativity hypothesis.
Continue only if the exact source comparison supports a concrete
test with every geometric and product cost specified. Stop or narrow
the proposed mechanism if it requires a new uncertified internal gap,
a favorable sign of the removed complement, or an unproved lower
bound for a weighted residue sum. No such inequality is derived here.

C645d is an essential contrast: even positive unit residues can cancel
after inverse-Blaschke weighting. The proposal must retain C744t's
unweighted integral, and must not assume that multiplying by a pole
product preserves its projected residue lower bound. The outer-kernel
phase, Gram-dual and removed-remainder stops also remain intact.
The assessment must check for duplicates beyond these already read
comparisons; a different name alone does not justify repeating a route.

Essential local inputs are C744r, C744s and C744t. Retain C744t(1)-(4):
the complete two-sided count for U>=1, hypothetical z0, positive kappa,
bump/seminorm data and strictly slack f0,M0. The count and strip alone
must not be called a numerical zero-location certificate. Any future
claim of a bound using only T,delta must separately discharge the
remaining data. The C744s three-circle source is reusable if its
hypotheses match; it supplies no new pole-product costs by itself.
Full matching Mathlib coverage is unchecked. No cross-notebook input
is proposed.

This is standard continuation-method development if approved, not a
new central sign-producing mechanism. The present audit supplies no
justified creative sign target. The next invocation is source comparison
for this exact nomination, with no new lemma or mathematical script.

## Completed source comparison — 11 November 2026, step525

This was one literature-only step. The main gap remains actual-Xi
positivity, L030-L032/C032a. The intermediate target is quantitative
whole-contour propagation for C744t. Its downstream use would be a
conditional finite-window detector under the supplied count, profile,
kappa and strict-slack data; it would not establish independent signs,
non-neutral coverage, C744q's margin or all-window assembly.

### Primary inputs and their exact limits

Beck, Marchesi, Pixton and Sabalka, *A First Course in Complex Analysis*,
[Section7.4, Theorem7.4.8](https://complexanalysis.org/web/sec_singularities.html),
unversioned author text, inspected 11 November2026: a function analytic
on a punctured disk has a pole of order k exactly when it is h(z)
divided by (z-a)^k, with h analytic at a and h(a) nonzero. Read both
Laurent-series directions of the proof. This is the local cancellation
input to import. For C744r the poles of G are at most simple, even for
multiple Xi zeros: multiplicity belongs in a_z. Vanishing coefficients
give removable points. No higher-order G pole should be inferred from
a multiple Xi zero. The theorem supplies no global norm bound.

Pope, *Methods of Theoretical Physics: I*, author-hosted
[2011-named PDF, Section5.4, pp.130-132](https://people.tamu.edu/~c-pope/methods_pages2011.pdf),
especially (5.180)-(5.181), explicitly uses the finite product of pole
factors. Read its surrounding definition: the rationality conclusion
assumes meromorphy also at infinity. That conclusion does NOT apply to
G. The bounded-domain proposal requires only local cancellation from
Beck's theorem, not rationality, an infinite product or a polynomial
growth assertion about the full G. The file's internal revision date
was not established. This source is comparison evidence, not an extra
input needed beyond local pole factorization.

Boas, [*Math618: Three-circles theorem*, 23 April2004](https://haroldpboas.gitlab.io/courses/618-2004a/apr23.pdf),
p.1 SectionI(1)-(2): a holomorphic function on an open annulus,
continuous on its closure, has log-radius convex circle suprema.
Read proof discussions1-2: the modulus argument avoids a global
noninteger power, and truncation handles zeros of the function.
Thus zeros introduced by pole cancellation do not invalidate this
theorem. A neighborhood of a closed disk is sufficient; the maximum
principle permits disk maxima. Translation and chosen concentric
radii need no reproof. A common upper bound on every enlarged disk
and a finite covering of ALL Gamma are still required. Boas supplies
neither the product bound nor the division bound. This is reused
C744s coverage, now compared with the changed domain obligation.

Beck et al., [Section8.1, Theorems8.1.5 and8.1.7(1)](https://complexanalysis.org/web/sec_residue-thm.html):
read the finite-singularity contour theorem and disjoint-circle proof,
and the simple-pole Laurent proof. The hypotheses require an analytic
boundary and analyticity inside except at every listed singularity;
the circle is simple, positively oriented and lies in a simply connected
domain. C744t already checks these for G-J_H. The new task must recover
a bound for that original function on Gamma before using (9), rather
than substitute an integral of the holomorphic canceled product. No
new residue identity is established in this source review.

For a stronger norm comparison, Kalmykov and Nagy, *On estimate of the
norm of the holomorphic component of a meromorphic function in finitely
connected domains*, [author-hosted PDF](https://www.math.u-szeged.hu/pot/Kalmykov_Nagy_1.pdf),
2015 header, no version tag, Theorem1(14), printed pp.12-13: for a
finitely connected domain with finitely many C2 Jordan boundary curves
and poles confined to a fixed closed interior set, the rational and
holomorphic components are bounded by C(D,Z) log(n) times the WHOLE
boundary norm (in particular for n>=3). The sum of principal parts is
normalized to vanish at infinity. Read the proof's Green-level contour,
meromorphic Bernstein-Walsh bound, Cauchy integral and small-n reduction;
Proposition1 supplies the logarithmic Cauchy-kernel estimate. A fixed
compact interior pole region is within this scope. This theorem is
comparison only: its right side already needs the unknown whole-boundary
norm, and C(D,Z) is not a paid numerical constant here. It cannot replace
propagation from a small right-half-plane disk. No use of its delicate
boundary regularity estimates is proposed in the continuation.

Suzuki2206.03682v4 Section2.2, pp.7 and3.1-3.5, pp.9-11,
(3.3),(3.5), Proposition3.1 and its distributional interpretation,
and Bellotti-Wong2412.15470v2 Theorem1.1/Section5 retain the exact
scope in the step520 assessment. They were not fetched again. In
particular the supplied complete count (1), not merely the named count
theorem or a finite zero list, remains a hypothesis. No new zero-count
or pairing theorem is needed for this bounded specialization.

### Duplicate and failure comparison

Read C744s Sections1-4 and C744t hypotheses/conclusion and Sections1-4;
read C744r's complete-series passage (13)-(14) to fix the actual poles
and convergence scope. C744s already solves the isolated selected-pole
problem with an all-other-pole clearance certificate. Repeating its
formula is unnecessary. The proposed difference is cancellation of
all poles in a count-bounded neighborhood, followed by recovery of the
unweighted cluster integral; no new quantitative claim is yet made.

A targeted active-notebook search for all-pole cancellation and finite
pole products also located L651's finite rational grid-cancellation
passage, lines336-344. Read that passage only. Its finite polynomial,
grid partial fractions and reciprocal-Blaschke factors do not provide
the full infinite-complement bound for this G-J_H. It is evidence that
finite cancellation itself is standard, not a new mechanism. The
exact-product assessment of1 November and the complete-angular-response
assessment of3 November likewise concern different finite-grid/rational
families and their paid norm/logarithmic losses.

C645d's audited hypotheses/conclusion and its ATTEMPTS record retain
the exact inverse-Blaschke cancellation stop. It does not refute the
actual C744t phase bound, but forbids an unproved weighted-residue
lower bound. The signed-neutral Gram-dual and screw signed-remainder
ATTEMPTS records retain norm and removed-complement stops. The interior
Cartan certificate stop concerns its fixed geometry's log-height cost;
this proposal uses a fixed compact propagation geometry and asks only
for a finite qualified horizon, with every cost retained. It does not
reopen that optimized log-height certificate. No historical stop is
treated as a global ban.

### Bounded continuation and abandonment test

Proceed to one mathematical test only after separate supervisor scope
approval of the new continuation assessment. Choose a bounded compact
propagation region in Re(s)>0 joining a starting disk in Re(s)>1/2 to
all Gamma. The proposed finite product must include every potential
pole on a padded neighborhood; its degree must be bounded using (1)
on the full required height range. A concrete choice of neighborhood,
covering disks and positive real-part margin is a proof obligation.

The unpaid estimates are: the canceled function's common upper bound
independent of H under the finite-window contradiction assumption;
the entire exterior series on every disk, with a paid geometric margin;
the starting-disk decay including product cost; and a positive lower
bound for the same product on all Gamma using its degree and C744t's
existing all-pole boundary clearance. Holomorphy alone pays none of
these norm costs. Numerical location of every factor or of r is not
being asserted from a count; distinguish an existential qualified bound
from a computable certificate.

The decisive threshold remains sup_Gamma|G-J_H|<alpha/r at an explicitly
specified finite H=(K-1)ell, under the all-admitted-two-cell nonnegativity
hypothesis. Success may be a rigorously qualified formula retaining
T,delta,kappa,A,profile,f0,M0; it need not remove independent sign gaps.
Stop or narrow at the first essential unpaid domain clearance, H-dependent
upper bound that defeats the desired decay, product lower bound, internal
zero gap or weighted-residue sign. Record the exact failed estimate;
do not substitute a selected arc or delete the exterior residues. No
one of these inequalities was derived or verified in step525.

### Search record and decision

Queries submitted on11 November2026:

- `meromorphic function finite poles polynomial multiplication Hadamard three circles quantitative continuation pole cancellation`
- `holomorphic propagation smallness meromorphic function cancel poles finite product boundary lower bound`
- `"finite poles" "three circles" meromorphic`
- `"meromorphic" "polynomial" "cancel" "poles" propagation smallness`

The inspected sources above support SPECIALIZE for the standard tools
and expose the remaining quantitative difference. The search did not
establish a matching theorem or originality. Search leads on numerical
analytic continuation and visible-pole determinants, including
arXiv2607.12256/2607.04568, were not read at theorem level and are not
inputs or blockers; neither is needed for the proposed elementary
finite-product test. NIST1.10's meromorphic definition was retrieved
but supplies no quantitative input. The initial erroneous Beck URL
sec_zeros-poles.html was inaccessible; sec_singularities.html supplies
the needed actual theorem, so no essential source remains blocked.

No general theorem needs a reproof. Full matching Mathlib coverage is
unchecked; unknown coverage is not absence. No cross-notebook result
is used. This review supplies source readiness, not a lemma, a validated
pole-product estimate, a length, a sign gain or progress beyond the
inspected literature. No new central sign-producing creative target
is justified by these standard continuation sources; the outstanding
sign input is the blocker, not a reason to relabel the present method.
