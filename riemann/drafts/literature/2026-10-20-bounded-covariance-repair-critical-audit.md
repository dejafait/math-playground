# Source coverage: critical audit of the bounded covariance repair

TARGET: Critically audit L441's bounded prime-2 covariance repair and all preserved L438 constraints under the original cutoff.
CHECKED: 2026-10-20
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused step 260's exact occupation/covariance/Schur--Horn searches and recorded failures; compared the complete new L441 proof with L419's exact forms and six-state implementation, L438 (12)--(20) and all tolerance/cap interfaces, and L440's raw-second identity and audited residual. No changed source hypothesis or uncovered theorem was identified; no fresh external search was needed.
SOURCE_EVIDENCE: Reused the inspected Carlen--Lieb arXiv:0904.0734v2 (13 May 2009), pp. 1--2, Horn theorem after (1.1) and proof through (1.2); Lasserre--Henrion--Prieur--Trelat arXiv:math/0703377v1, Sections 2.1--2.3, (2.7), (2.10)--(2.12), pp. 3--5; Aistleitner--Berkes--Seip, JEMS 17 (2015), Section 3, p. 1527, identity before Lemma 1 and (23), through the construction assessment and canonical local interfaces.
COMPARISON: These sources cover real pointwise matrix realization, the necessary finite-interval occupation identity and finite Poisson coefficients. L419 adds Borel branches and L440 adds the unchanged-cutoff complete residual. They do not certify L441's simultaneous preservation claims; checking those local specializations is the exact later audit.
GAP: Independently verify every L441 preservation and residual claim against the canonical inputs, including exact weighted recentering, all six raw seconds, translated support, both first means, conditional x-second equality, signed cubic and absolute moment/cap estimates, with one eventual real-H family.
REASON: The complete written repair stays inside the prior bounded-covariance source scope. Essential coverage is adequate for one separate mathematical audit; this comparison neither performs that audit nor establishes the repair or any originality.
LITERATURE_REASON: The new critical-audit TARGET was REVIEW_REQUIRED. This turn compares the newly written proof's source scope with ready construction coverage, rather than repeating discovery or browsing to meet a quota.
SCOPE: Audit only L441 as written, using L419, L438 and audited L440, with L429's original cutoff and the unchanged L421/L437 rare interfaces through L438. Elementary finite-matrix, polynomial-moment and finite-interval estimates are covered; no stronger occupation theorem, actual sine limit, basis continuity, growing-character uniformity or trajectory sufficiency is covered.

## Main gap, intermediate target and decision test

Global mixed positivity remains the main RH gap. The intermediate target
is an independent critical audit of the bounded repair of one asymptotic
occupation residual. Its plausible downstream use is to decide whether
this added necessary identity distinguishes only the unchanged law or
also survives this specific supported correction. Success gives no
trajectory or RH completion mechanism.

Continue with the repair as an audited local input only if every exact
calibration, support condition, original tolerance and complete residual
claim survives on one eventual real-H ray under the unchanged cutoff.
A failed coefficient, support margin, measurability claim or tolerance
must be identified and repaired or left explicitly unresolved. An
unchecked estimate is not an impossibility result. No new law or new
occupation target is approved by this assessment.

## Precise source imports and applicability boundaries

The ready source record is
`drafts/literature/2026-10-20-prime-two-occupation-covariance-repair.md`.
Its actual searches and primary theorem inspection are reused, not
represented as newly performed external research.

Eric A. Carlen and Elliott H. Lieb, *Short proofs of theorems of Horn
and Mirsky on diagonals and eigenvalues of matrices*,
[arXiv:0904.0734v2](https://arxiv.org/pdf/0904.0734v2), pp. 1--2,
Horn theorem after (1.1), proof through (1.2), supplies real orthogonal
realization of a diagonal majorized by the eigenvalue list. The ready
record inspected the two-dimensional and inductive cases, including
the scalar equality case. L441 uses the real symmetric matrix SJS and
its constant trace-average diagonal. Positive covariance and negative
trace remain local audit obligations. This theorem supplies neither
Borel selection nor continuity; L419's deterministic finite rotation
branches, including equality/tie branches, are the separate local input.
No reproof of the imported theorem is needed.

J. B. Lasserre, D. Henrion, C. Prieur and E. Trelat, *Nonlinear optimal
control via occupation measures and LMI-relaxations*, SIAM J. Control
Optim. 47 (2008), 1643--1666, DOI 10.1137/070685051,
[arXiv:math/0703377v1](https://arxiv.org/pdf/math/0703377v1),
Sections 2.1--2.3, (2.7), (2.10)--(2.12), pp. 3--5, supplies a
necessary C^1 finite-interval identity including endpoints. Each fixed
H uses bounded boxes; L440 supplies the same test and ordinary dynamics.
Changing the conditional covariance does not call for a stronger source
identity. No derivative of the Borel kernel or cutoff, uniform compact
box, sufficiency or no-gap result is imported. The later audit checks
the difference of full residuals, not a trajectory construction.

C. Aistleitner, I. Berkes and K. Seip, *GCD sums from Poisson integrals
and systems of dilated functions*, JEMS 17 (2015), 1517--1546,
DOI 10.4171/JEMS/537, Section 3, p. 1527, identity before Lemma 1
and (23), [primary text](https://ems.press/content/serial-article-files/32047?nt=1),
covers finite Poisson products with radii below one. The moving weighted
limit under the original cutoff is L440's local result, not a consequence
of qualitative Haar convergence alone. L441 claims no changed product,
cutoff or new sine coefficient. Its additional fixed-frequency sine
averages are finite-interval calculus audit obligations, not missing
external coverage.

## Comparison with the written proof and earlier failures

The entire L441 proof was read for source scope. Its new ingredients
are a bounded xy covariance increment with exact w-weighted recentering,
reapplication of L419's supported realization, polynomial moment
comparisons, and a complete raw-second residual difference. None calls
for a new general matrix or occupation theorem. This source comparison
does not validate the displayed formulas or estimates.

The later audit must check both covariance margins and all six translated
support values, without assuming closeness or continuity of reselected
atoms. It must check exact six integrated seconds and first B mean,
the original first D tolerance, conditional x-second equality, the signed
cubic formula, all 23 quartics, both third envelopes, physical bounds and
the cap for every fixed parameter with one family. Retain both slow x^2
terms, the entire old raw-second residual, the new cross term and its
constant recentering. Only o(1) cancellation is asserted.

Duplicate/failure comparison reuses the construction record and steps
259--261: L440 separates the unchanged law; L439's Gaussian o(1) result
does not decide this quadratic test; L428 rejects a uniformly bounded
normalized x-second density, not an off-diagonal increment retaining the
Poisson product. The earlier sign-only and capped-radial failures remain
at their original scopes. No historical stop is erased. No checked source
already proves this complete supported repair, and no novelty follows
from that observation. Unread frame/geometric Schur--Horn leads in the
construction record remain unread and unnecessary to this audit scope.

## Approved continuation and qualifications

SPECIALIZE approves the exact TARGET for a later RESEARCH /
REPRODUCTION / proof_audit turn. It approves source coverage only; no
lemma, mathematical script, DAG edge or PROOF.md argument changes here.
Essential inputs are L441, L419, L438 and L440, retaining L429's original
cutoff and L421/L437 rare kernels through L438. Read complete relevant
canonical evidence during that audit; this scope comparison is not a
replacement for it.

Exact finite-H cancellation, other occupation identities, actual/global
realization, actual clipping, capped nondegeneracy, L413's full-error
regulator margin and global mixed positivity remain unresolved and are
not assumptions. Full matching Mathlib coverage was not checked; no
absence or formal verification claim is made.
