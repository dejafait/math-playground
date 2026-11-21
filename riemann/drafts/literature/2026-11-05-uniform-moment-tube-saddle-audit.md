# Uniform moment tube and saddle inputs — audit coverage

TARGET: Audit the kernel-tube and full-saddle continuation claims in Michalowski v1 Lemmas3.1–3.3 for k>=10^9 and |z-k|<=k/20, including the real-saddle existence and bounds assumed by L788 and L787.
CHECKED: 2026-11-05
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step469 reused step465–467 comparisons, inspected L787/L788 interfaces and selected working/history records, searched named local failures, and made exact-title/identifier/kernel-tube/saddle/erratum queries; no inspected exact replacement or completed audit was identified in this bounded scope.
SOURCE_EVIDENCE: Read Michalowski arXiv:2607.16795v1 Section3 (5), opening real-saddle data, complete Lemmas3.1–3.3 statements/proofs, opening Lemma3.5 proof and Table1; inspected Rutgers Math503 fall2004 Rouche/Cauchy statements and Waldron Complex Manifolds (spring2020), Theorem2.5.6, p.36, with proof. Ancillary evidence was neither inspected nor replayed.
COMPARISON: Exact tube/saddle conclusions are printed source claims; geometric summation, Cauchy estimates, Rouche and holomorphic implicit-function theorems support the method but give no kernel-specific constants. Approve a reproduction audit on the restricted strip, with admissibility and no circular derivative input.
GAP: Verify the small-strip tube majorant and numerical specialization, real-saddle existence/bounds, both principal-saddle comparisons and full-kernel analytic continuation with drift<=3/200; none is proved by this review.
REASON: Essential primary proof cases and standard hypotheses are accessible, so a separate mathematical audit can test these known antecedents; uninspected ancillary enclosures require proof or replay if essential.
LITERATURE_REASON: Changed hypothesis scope from step467: Lemmas3.1–3.3 and real-saddle data were then assumed and are now under audit; complete the supplied REVIEW_REQUIRED gate using existing overlap assessments.
SCOPE: Ready for exactly the saved audit at k>=10^9, |z-k|<=k/20, with the tube formula restricted to 0<=nu<pi/8 and q<1, including nu=1/10 at x0=3/10,7/20,2/5; no k>=16 extension, saddle action, Taylor estimate, other wedge gate or global sign theorem.

Primary lead: W. Michałowski,
[arXiv:2607.16795v1, Section3](https://arxiv.org/html/2607.16795v1#S3),
18 July 2026, *An explicit uniform cubic wedge for consecutive Toeplitz
minors of the Riemann xi-coefficients*, (5) and Lemmas3.1–3.3.
The real-saddle data also appear at the opening of Lemma3.5's proof.
Numbering binds to v1. This step approves the audit, not the claims
under audit. Generic complex-analysis theorems do not certify its constants.

## Completed source comparison — step469

This is a literature-only review: no new lemma or bound. The exact
TARGET is retained; the completed gate permits a later RESEARCH /
REPRODUCTION audit. The original pending gate is recorded in step468's
history. Main gap: actual-Xi all-degree mixed positivity. Intermediate
use: discharge L788/L787's tube/saddle assumptions before actual-I
factorization and separately assessed growing-order Taylor control.

### Primary claims and qualifications to test

Section3 defines B=2pi exp(4u), H=B-9/2-6/(B-3), K=uH and the
positive real solution K(u_k)=k. For k>=10^9 the needed data are
1<u_k<log(k)/4, H_0=k/u_k and (21/25)B_0<=H_0<=B_0.
The opening asserts existence, uniqueness and localization;
Lemma3.2's proof discusses monotonicity for u>=9/20, and Lemma3.5's
proof uses K(1)<10^9. A later audit must justify real initialization,
existence and the relevant interval, rather than accept these opening
assertions as independently audited premises.

Lemma3.1 bounds each summand relative to Phi_1 and sums a geometric
majorant with q=16 exp(-3pi X cos(4nu)), X=exp(4x0).
Its printed hypotheses give cos(4nu)>0 and 2pi X>3 but do not state
q<1. Its proof also uses cos(4y)>=cos(4nu)>0 for all |y|<=nu.
These are admissibility issues to check before using the proof;
the approved specialization is 0<=nu<pi/8 and q<1. No general
claim about other cosine-positive bands is approved. L788 already
makes q<1 explicit; its universal-looking tube premise must not be
discharged outside the qualified strip by this audit. Check normal
convergence and the nonzero denominator before forming analytic
R=Phi/Phi_1-1. Source numerical targets are <10^-15 at x0=2/5
and <1.1*10^-14 at x0=7/20, both with nu=1/10. The x0=3/10
larger tube is essential for L788's horizontal Cauchy circles.

Lemma3.2 uses the complete radius1/20 disk about u_k, K'(u_k)>4k
and sup|K''|<60k. Its printed Rouche comparisons are 0.2k against
0.125k there, and 0.06k against 0.05675k on radius3/200.
These are source thresholds to verify, not calculations made here.
Check every derivative/denominator estimate over the whole disk.
Count zeros with multiplicity before invoking analytic dependence;
the closed z-disk requires boundary continuation, not only a germ
at z=k.

Lemma3.3 uses full radius1/25 Cauchy circles about points of the
control disk in the (7/20,1/10) tube. It claims
K_Phi=K-(u/2)R'/(1+R), |K_Phi-K|<7*10^-15 k, then repeats
both Rouche comparisons. The sharper drift<=3/200 appears in the
proof. Check the u/k bound, analytic ratio, nonzero denominator,
phase logarithm and its real-axis normalization. Uniqueness must
justify patching local implicit branches over the parameter disk.
Do not use L788's conclusions to establish their own antecedent.
The reported 6.53*10^-15 enclosure and certificate function names
remain unread leads, not verified evidence.

### Standard inputs and exact-source limits

Geometric summation requires |q|<1 and supplies no numerical theta
bound without the termwise estimate. The [Rutgers Math503 diary,
fall2004](https://sites.math.rutgers.edu/~greenfie/mill_courses/math503/diary.html),
December8 Rouche statement and assumptions S, requires holomorphic
functions on an open neighborhood, a null-homotopic counting curve,
no boundary zero and strict boundary domination. Zeros are counted
with multiplicity. Its Cauchy-estimate passage requires holomorphy
near the closed disk and bounds derivatives by n! M/r^n, with M the
supremum on the entire circle. The complete statements/hypotheses
were inspected; future work must provide those circles and inequalities.

Alex Waldron, [Complex Manifolds (MTH935), spring2020](https://people.math.wisc.edu/~awaldron3/Notes/Complexnotes20.pdf#page=36),
Theorem2.5.6, printed p.36, (2.29)–(2.30), requires holomorphic
functions and an invertible derivative block and gives a local
holomorphic solution graph. Its proof via Theorem2.5.5 was read.
Here the scalar derivative condition and compatible branches remain
audit obligations; this theorem gives no global disk or drift constant.
PDF find requests failed transiently; direct selected-page extraction
then exposed the complete statement/proof. No essential source blocker
remains. Matching Mathlib coverage is unchecked.

### Reuse, failures and search record

Reused step465's growing-order comparison and step466–467's ready
conditional assessments, with exact L787/L788 interfaces and selected
working/history passages. Their completed work leaves this target
conditional. A scoped ATTEMPTS search for saddle/author/identifier
terms found no matching completed audit in the selected records;
this is not an exhaustive novelty claim. Read the named actual
q-Pascal endpoint norm and real-moment pointwise-sign stop records.
Their obstructions concern different sign mechanisms, not existence
of this far-tail saddle. L765/L774 and their audited stops remain;
stronger tail estimates do not reopen them automatically.

External queries included author with kernel tube, exact title with
saddle, identifier with erratum, and theta moment complex saddle.
Primary proof cases were read before broader returned material.
No inspected correction or stronger exact replacement was located.
Aggregator snippets supplied no mathematical input. Returned teal-sea
methods and two-thirds Jensen-wedge pages remain unread leads; the
gate neither relies on nor claims to cover their results. Standard-
theorem searches served only the stated hypotheses. Initial combined
output was oversized; truncated output was not completeness evidence.
Essential local interfaces and source cases were retrieved separately.
No sibling notebook was read.

### Bounded continuation and stop rule

Continue only in a separate mathematical turn that recovers every
required bound on its full domain from the kernel and standard inputs.
Explicit analytic verification may replace certificate-only roundings
if it meets the same thresholds: justified reproduction of a known
claim, not progress beyond the source. If any real initialization,
domain or constant fails, isolate the first failure, retain conditional
status and distinguish a broken intermediate estimate from a false
conclusion. This review ran no mathematical calculation.

Essential local interfaces: L788's explicit tube and real/full-saddle
assumptions and L787's factorization hypotheses; L786 supplies only the
coefficient normalization for the downstream use. The source scalar
map K is distinct from the notebook theta kernel. In a later approved
audit, continue only if the exact larger/smaller tubes, full saddle drift,
analyticity and real-saddle data are proved without the derivative
conclusions that depend on them. Otherwise isolate the first failed
estimate and keep L788/L787 conditional.

Plausible downstream use is actual-I complex factorization and then
separately assessed coefficient Taylor control. The saddle-action bound,
other wedge gates, bounded k/r and all-degree mixed positivity remain
open. This is established-route development, not a creative central sign
mechanism. Matching Mathlib coverage is unchecked.

The source comparison supplies no independently justified central signed
mechanism; step465's blocker to creative routing remains. Do not invent
a creative target solely to fill the scheduling preference.
