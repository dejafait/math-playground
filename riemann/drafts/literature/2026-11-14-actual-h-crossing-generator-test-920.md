# Actual-H two-particle generator test: scoped specialization coverage920

TARGET: Specialize the sourced Levy generator to C466b's actual H and test the two-particle chamber positive minimum principle with one smooth test supported away from collision.
CHECKED: 2026-11-14
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the completed, unchanged-target source comparison in 2026-11-14-ordered-chamber-semigroup-review-919.md, completion920; its exact queries, duplicates and access qualifications cover this single bounded specialization. No independent novelty claim.
SOURCE_EVIDENCE: Schilling, arXiv:1603.00251v2, Lemma6.3 pp37-38, Theorem6.8 p39 eq(6.8), Remark5.10 p34, https://arxiv.org/pdf/1603.00251v2 ; Schilling--Song--Vondracek, Bernstein Functions (2010 first edition), Theorems3.2/5.2 pp15/35 and Definition5.4 p35, https://dokumen.pub/bernstein-functions-theory-and-applications-9783110215311-9783110215304.html ; Karlin--McGregor (1959), Section5 Theorem1 pp1148-1150, https://msp.org/pjm/1959/9-4/pjm-v9-n4-p13-p.pdf ; inspected hypotheses/cases and retained C466a/b qualifications are recorded in comparison919 completion920 and the URL repair921 below.
COMPARISON: The known statements cover the scalar construction and full-space generator, while their application to the antisymmetric chamber cone requires the explicit test below. This is ordinary specialization/obstruction work, not a creative claim.
GAP: Match the actual measure and compensation conventions, then determine the restricted generator's sign at a zero of a nonnegative interior chamber test; no such sign was derived or approved as a result in step920.
REASON: A failed necessary minimum principle would rule out unrestricted chamber-cone propagation before higher-order work. A successful test alone supplies no positivity theorem. The exact local specialization is absent from the inspected sources, and verification is needed to avoid silently replacing antisymmetry by killing.
SCOPE: Only the two-particle backward generator and one smooth interior-supported test; no new all-degree positivity, tau=1 PF failure, density theorem, or Xi implication. Coverage received a separate literature-only URL repair/review in step921; its mathematical scope is unchanged.

## Inputs, retained assumptions and bounded proof obligation

Use C466a's normalized p=theta_1, h and B, and C466b's actual H
and drift-free scalar representation, with their inherited L018
normalization and qualified external zero/counting inputs. The exact
theorem statements and read limits are in the primary theorem records
of [comparison920](2026-11-14-ordered-chamber-semigroup-review-919.md#source-comparison-completed-14-november-2026-step920).
Import those results by citation; do not reprove their general theorems.

Verify the proposed Bernstein measure H(t)dt/t at zero and infinity,
its drift/killing parameters, and the compensated Levy convention.
Use the backward shift T_tau f(x)=E f(x+S_tau); the two copies must
be independent, so their joint process is the relevant two-dimensional
Levy process. Check the domain on compactly supported smooth
full-space extensions rather than assuming a chamber generator core.
Smooth densities for all tau are not needed or assumed.

Set W={x_1<x_2}. Seek one f in C_c^infinity(W), f>=0, and an
interior z with f(z)=0 such that applying the full-space generator to
the antisymmetric extension Ef, then restricting to z, is strictly
negative. This is a target, not an asserted formula or established
counterexample. Keep every coordinate-jump contribution, including
jumps past the other particle; verify absolute convergence, local
drift and compensation terms. Compare against zero extension only
to identify the distinction, never to import its positivity.

Continue this unrestricted maximum-principle route only if a source-
justified actual-H cancellation prevents the proposed negative test
and leaves a concrete additional sign mechanism. A certified negative
value stops that route. Failure to construct the test within one
coherent attempt is inconclusive and must be preserved; it is not
evidence of positivity. After a stop, choose a materially different
mechanism rather than upgrading this test to more particles.

The downstream purpose is route discrimination for the actual-Xi
all-degree gap L030-L032/C032a. Even a negative result says nothing
against a density minor at tau=1. Higher-order signs, the correct
initial/boundary problem, global propagation and Xi transfer remain
unresolved. C466i and stop917/audit919 are comparison constraints,
not hypotheses of the generator calculation. No contact or nonzero
kappa is assumed. Mathlib matching coverage remains unchecked.

## Direct-source repair and review921 — 14 November 2026

This separate literature-only review repairs the missing direct URL in
SOURCE_EVIDENCE. It does not change TARGET, SCOPE, or the proposed test.
The preceding comparison920 remains the reusable theorem comparison;
no new discovery search or theorem specialization was performed.

Reopened the three source URLs above. Rechecked Schilling's Lemma6.3,
Theorem6.8 statement and proof steps1-2, and Remark5.10's semigroup
hypotheses. These concern the full-space generator on smooth compactly
supported tests, its compensated jump convention, and the full-space
positive cone. They do not establish a chamber sign. Printed pagination
is one less than the zero-based PDF page index at these locations.

Rechecked the first-edition book's Theorem3.2 representation, uniqueness
and integrability requirement, with derivative-measure proof passage.
Theorem5.2 and Definition5.4 are reused from completion920's inspected
semigroup/killing record; their proof was not reread in this repair.
The mirror renders mathematical symbols imperfectly; use the retained
edition-specific theorem record rather than treating OCR inequalities
as new hypotheses. Opened the publisher Karlin--McGregor PDF and
rechecked its introductory explanation of why order changes require
coincidence under the special path assumptions; Section5's complete
signed identity and proof remain reused from completion920.

No local actual-H parameter identification, integrability estimate,
antisymmetric extension, or generator sign was derived. C466a/b and
inherited L018/external-input qualifications still require the exact
applicability checks listed above. Existing comparisons with stop508,
working914 and C466i/stop917/audit919 are unchanged; no duplicate search
or expansion of the mathematical target was needed. Mathlib coverage
remains unchecked. SPECIALIZE is retained for the single bounded test.

This is a process repair, honestly STALLED as mathematical progress.
The next research invocation may reuse this separately reviewed scope;
no additional literature is proposed absent a changed hypothesis or
specific essential source gap. No lemma or mathematical script changed.
