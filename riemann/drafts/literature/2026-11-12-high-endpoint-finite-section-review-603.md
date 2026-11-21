# Source review: quantitative unbounded-endpoint reduction

TARGET: Assess source coverage for a quantitative finite-section reduction of C744z(4) on exact neutral cosine subspaces, with an explicit operator-norm remainder tending to zero and with actual U and induced middle coupling retained.
CHECKED: 2026-11-12
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step604 searched compact-operator orthogonal finite sections, quantitative Galerkin norm approximation, compact-resolvent forms and logarithmic-Laplacian FEM, including exact Weil/neutral terminology; screened local12November assessments and stop537, and read C744z Sections1-3, C744v Sections3-4, C744w Section2 and C999k Sections1-2. Queries, primary reads, nonmatches and unused leads are recorded in drafts/2026-11-12-high-endpoint-source-review-604.md; no originality inference.
SOURCE_EVIDENCE: Teschl GSM99, version12February2009, Theorem1.3(iii), Theorem1.7, Lemma5.5, Theorem6.7 and Lemma6.8/proof pp137-138; DNR1978 Section1/Section2 pp113-119; Hernandez-Santamaria et al arXiv2311.13079v3 Theorem1.2, Lemmas4.1-4.2/proofs and Proposition7.2 statement/proof case. Exact citations and qualifications are in the source-review note; previous form/inverse assessments are reused.
COMPARISON: Teschl covers qualitative compact-operator norm approximation with strongly convergent projections, not a computable cutoff rate. DNR requires approximation hypotheses and generic constants; logarithmic-Laplacian FEM requires regular forcing and different spaces. Known projection/Parseval/form inputs cover part of the desired specialization, but none supplies C744z(4)'s explicit neutral cutoff remainder or its sign. Fixed-input tails and C999l/q margins do not transfer to normalized endpoint coordinates.
GAP: A later bounded specialization must quantify exact neutral cosine approximation of A0^-1/2 using the actual logarithmic form, then pay both sides of every normalized block and product in C744z(4). Neither epsilon_N, compactness of the local normalized residual, finite normalized entries nor any positive margin is established in this literature turn.
REASON: Enough primary coverage is available for a separately approved attempt at the explicit projection/product specialization. Direct theorem import does not solve the quantitative target. Preserve all finite stops; do not spend another literature turn on unchanged compactness coverage.
LITERATURE_REASON: Changed target requires compact-resolvent and quantitative finite-section source coverage outside601's fixed1024-support trial-selection and verification scope.
SCOPE: Only the complete neutral three-cell endpoint operator C744z(4), ell=log(3)/2, original D/S/T/T*/U and qualified A0 on H0; all independent complex endpoints, actual separation14 and induced coupling, no new coercivity floor, no assumed finite-head sign, no RH/H2 premise, no cross-notebook input.

## Completed literature comparison604

The source-review note contains the inspected hypotheses and proof cases.
SPECIALIZE licenses a bounded attempt to supply the missing quantitative
estimates; it does not certify that those estimates hold. The proposed
mathematical continuation is saved separately in
`drafts/literature/2026-11-12-neutral-cutoff-bound-604.md` for the supervisor's
separate next-turn approval. No derivation or new lemma was made here.

In particular, an exact compression involving A0^-1/2 is not automatically
the matrix obtained by taking the inverse square root of a finite Galerkin
matrix. Effective enclosure of that finite compression remains separate.
Finite signs in the unnormalized profile/free-coordinate metric are not
sign margins for this new compression. Full Mathlib coverage is not checked.

## Pre-review nomination retained

The text below records the original603 nomination, before external review.
Its statements about unread coverage describe that historical nomination.

This file nominates a future source review, not a ready mathematical
attempt. It does not derive compactness, a remainder, a projection identity
or positivity. No external search is represented as completed.

Main gap: L030-L032/C032a actual-Xi positivity. The intermediate target
would reduce one unbounded-endpoint comparison to signed finite data
plus an explicit error. It would leave finite-head positivity, margins,
C744q, H2, neutral-core/c_* verification, non-neutral coverage and global
actual-Xi assembly unresolved. Even qualitative finite negative index is
not a positivity certificate.

Use C744z(4)'s normalized endpoint operator, with R_7 its separation7
contraction and V14 its actual normalized remote block. These are not
C999k's reference metric. Ask whether primary compact-resolvent and
Galerkin results apply to exact L2 projections onto neutral raw0:N-1
cosine spans on H0, at each endpoint. A proposed norm remainder must
pay both mixed blocks and the full complement of this operator relative
to its identity part. Sources must justify these particular projections;
strong convergence or a qualitative compactness assertion alone is not
a computable uniform bound. No claim that the projections commute with
A0 or its square root is allowed.

Essential local inputs to read narrowly: C744z Sections1-3 and its exact
formula(4), C744v's logarithmic form/bounded-response proof, C744w's
complete tail estimates, C999k's qualified reference order. Keep C999l/q
only as finite contrasts. Preserve stop537 and C744z's diagonal-only and
scalar remote stops; no old numerical tail totals or mixed constants
transfer to this target. Source selection should cover named standard
terminology, stronger results, and quantitative limitations. Full matching
Mathlib coverage is not checked.

Continuation test: approve only a precise applicable theorem or assessed
specialization giving explicit epsilon_N tending to zero, including
neutral projection/domain and all mixed blocks, and specify the later
signed finite margin it would require. If sources supply only qualitative
compactness, uncontrolled projection constants or assume the missing sign,
record that limitation and do not promote a finite sample to the full
operator. New mathematical work, if warranted, requires a separately
approved exact target. This nomination makes no source-access claim and
has not consumed a mathematical exploration turn.
