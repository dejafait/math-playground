# C645i one-sided circle counterfamily — approved source scope

TARGET: Critically audit C645i's one-sided regular-polygon counterfamily, including admissibility, the residue-quadrature error, the uniform Hankel upper bound and the strict exponent gap.
CHECKED: 2026-11-01
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the completed one-sided and full-pole comparisons, their recorded queries and failures; inspected the linked primary theorem statements and BCQ v2 operator definitions on 2026-11-01. No expanded novelty search or changed mathematical scope; the exact audit is inside the prior counterfamily alternative.
SOURCE_EVIDENCE: Howell--Mathews, Complex Analysis, online front matter updated 2025-08-22, Sections 8.1 Theorems 8.1.5/8.1.7 and 6.2 Theorems 6.2.18/6.2.19 inspected directly; BCQ arXiv:1501.01161v2 (2015-03-24), Section 2 pp.2--3 and (17) p.7 inspected directly; retain journal citation J. Approx. Theory 206 (2016), 17--47 from the saved comparison. C645i remains an audit object, not source evidence for its own correctness.
COMPARISON: The unchanged prior source assessment permits a fixed-parameter admissible asymptotic counterfamily; C645i proposes one with a full boundary/operator upper bound, rather than C645d's scalar cancellation. The next task is independent scrutiny of this local proof, not new operator theory or a novelty claim.
GAP: Correctness of the exact admissibility, analytic quadrature, factor estimates, uniform norm comparison and exponent margin awaits separate conceptual audit; actual-Xi realization and all-degree signs remain open.
REASON: This separate literature-only turn approves the exact nominated audit using adequate reused coverage, with corrected textbook attribution and a readable primary BCQ fallback. Approval concerns source scope only; C645i is not verified.
SCOPE: Only the explicit fixed delta=2/5, eta=1/100, C=10 family and upper bound in C645i; no actual-Xi transfer, enlarged geometry or new asymptotic family.
COVERED_TARGET: Critically audit C645i's one-sided regular-polygon counterfamily, including admissibility, the residue-quadrature error, the uniform Hankel upper bound and the strict exponent gap.

LITERATURE_REASON: The supervisor requires separate approval of the newly nominated continuation assessment; only its exact source hypotheses and citation identity were checked, without reopening the ready general literature comparison.

## Reused sources and applicability

The prior ready assessment is
[the one-sided pole comparison](2026-11-01-one-sided-pole-hankel-census.md).
It covers arbitrary close distinct poles, integer simple-pole residues,
the exact complex grid weights, a rightmost anchor and M<=C*n for any
fixed C. The proposed counterfamily is inside that scope. Reuse the
full source comparisons there; its one-sided SPF/phase-variation
theorems were comparisons, not inputs asserted to prove this estimate.

Reuse [the full-pole operator comparison](2026-11-01-full-pole-hankel-boundary-mechanism.md)
for normalized Hardy spaces, bounded rational symbols and contractive
orthogonal projection. The exact BCQ source is
[the author-hosted journal paper](https://www.must.edu.mo/images/SCSE/qiantao/QianTao_P147.pdf),
J. Approx. Theory 206 (2016), 17--47, Section 2 and (17)--(19).
The proposed upper bound uses only ||H_q||<=||q||_infinity; it does
not require a Nehari equality or estimates of small singular values.

The residue and contour statements are
[Howell--Mathews, Section 8.1](https://complexanalysis.org/web/sec_residue-thm.html),
Theorems 8.1.5 and 8.1.7, and
[Section 6.2](https://complexanalysis.org/web/sec_contour-integrals.html),
Theorems 6.2.18--6.2.19, online source with front matter dated 22 August 2025, directly
inspected in this approval turn. Verify their application to C645i's explicit kernel and
the pole-free neighborhood, not the general theorems afresh.
No essential unread primary source has been identified. Full matching
Mathlib coverage remains unchecked.

## The independent audit and its decision test

Read the full C645i proof and exact arithmetic certificate, with the
complete load-bearing values rather than a preview. Essential inputs
are C645g's normalized symbol/rescaling; C645i's explicit polygon
and residue kernel; the named residue theorem and projection bound.
C645h gives the downstream boundary interpretation, and C645d/C645b
are recorded comparisons, not premises.

Check every n>=5, all poles including the anchor, disk clearance,
grid avoidance, positive integer residues and exact M=10n. Verify
holomorphy for the auxiliary circle, the residues at its origin and
roots of unity, the 1/R scaling, uniformity for all outer-boundary z,
and the finite-grid derivative/rectangle estimates. Replay the exact
rational table if needed, without treating the arithmetic script as
an analytic proof. Confirm that the bound controls the largest
operator norm and that 513/10000>delta/8=1/20 yields the asserted
asymptotic violation at fixed parameters.

Accept the local stop only if all these implications hold; otherwise
identify a concrete failed hypothesis or estimate, repair it within
the assessed scope if possible, and report its effect on the exponent.
Do not infer actual-Xi realization or an RH disproof. No new mathematical
derivation was performed to assess this future audit, and no independent
audit is claimed completed in the proof-attempt turn.


## Completed approval — 1 November 2026

The exact TARGET and SCOPE above are approved for one later conceptual
audit. No new lemma, estimate, counterfamily or mathematical verification
was performed here. Read only C645i's hypotheses/conclusion, source scope,
(8)--(15), (23) and verification/Mathlib notes to identify the imports;
the full proof and certificate remain required reading for that audit.
C645g's symbol (2) was checked for scope, without replaying its proof.
The saved one-sided comparison and its recorded failures suffice for
duplicate/known-result screening at this unchanged target. No claim of
novelty or exhaustive absence follows.

### Correct citation and theorem hypotheses

The [source front matter](https://complexanalysis.org/web/root-1-2-2.html)
names Russell W. Howell and John H. Mathews, *Complex Analysis*, last
updated 22 August 2025. The attribution to Beck et al., *A First Course
in Complex Analysis*, in C645i and the prior nomination is incorrect.
The linked theorem numbers are valid in Howell--Mathews. Correct C645i's
attribution during the authorized mathematical audit; its lemma file was
left untouched in this literature-only turn. C645g has the same recorded
attribution error; no mathematical failure of either proof follows from
this bibliographical finding alone.

[Theorem 8.1.5](https://complexanalysis.org/web/sec_residue-thm.html)
requires a positively oriented simple closed contour in a simply
connected domain and analyticity on and inside it except finitely many
interior isolated singularities. Theorem 8.1.7(1) supplies the simple-pole
limit rule. For C645i (14), these are the imports to apply to its explicit
kernel; confirming holomorphy, the enclosed singularities and their
residues belongs to the next audit, not this approval.

[Theorems 6.2.18--6.2.19](https://complexanalysis.org/web/sec_contour-integrals.html)
require continuity on the real integration interval or contour; the
latter bounds the integral by contour length times a modulus bound.
The short proof of 6.2.19 using parametrization and 6.2.18 was inspected.
Its use in (15) requires the proposed bound on the entire auxiliary
circle uniformly in the external boundary point; sampled values do not
satisfy that obligation.

### Operator source and bounded access fallback

The journal PDF opened initially but subsequent targeted requests timed
out. This is not an essential source blocker: the already recorded
[author preprint v2](https://arxiv.org/pdf/1501.01161v2), dated 24 March
2015, was accessible. Section 2, printed pp.2--3, specifies normalized
circle measure, the orthogonal Hardy decomposition, strictly negative
modes in the exterior space, and contractive Riesz projections. Equation
(17), printed p.7, defines the bounded-symbol Hankel operator on H2.
These are exactly the conventions needed for C645i (23). Its neighboring
AAK identities (18)--(19) are unnecessary for the proposed upper bound;
no singular-value or Nehari equality needs auditing or rederiving.

### Decision and limits

DECISION remains SPECIALIZE: standard residue/projection inputs are
available, while their explicit application and quantitative estimates
in C645i are local work still requiring scrutiny. This is approval of
adequate coverage, not a new mathematical advance. Full matching Mathlib
coverage is not checked; no declaration or Lean verification is claimed.
No essential unread primary theorem was identified for this fixed scope.

The continuation must read all of C645i (1)--(23) and the complete
load-bearing arithmetic table, check every stated n>=5, and either
validate the proposed uniform norm bound and strict exponent gap or
identify a precise failure and its effect. Keep C645d's scalar stop and
C645b's envelope stop as comparisons, not premises; C645h supplies only
downstream context. Actual-Xi selection, census, clearance, realization,
boundary upper bounds and all-degree signs remain unresolved. A changed
family or extra hypothesis lies outside this approval and needs its own
assessment.
