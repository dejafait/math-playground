# Centered companion diagonal-scaling review1522, completed1523

TARGET: Review positive diagonal similarity of C028d's centered reciprocal-Jensen companion matrix as a height majorant, checking primary matrix bounds and whether a fixed terminal block can rule out an o(d) optimized cost.
CHECKED: 2026-11-18
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Review1523 completed the bounded matrix/diagonal-scaling search and primary comparison; queries, exact reads, reused assessments1493/1496/1497/1500 and local stops are recorded in drafts/literature/2026-11-18-centered-companion-source-notes-1523.md. No matching evaluation of the exact optimized imaginary-part cost was located; no novelty is inferred.
SOURCE_EVIDENCE: Inspected Schmeisser2002 Lemma1 pp211-212 and relevant proof pp213-214; Higham2021 companion identity(*); Watrous2018 Section1.1(1.165)-(1.175),(1.179)-(1.181) pp32-34; De Teran-Dopico-Perez2014 author manuscript Section7 Lemma7.2/Theorem7.4 pp18-19 and complete theorem proof. Precise citations, URLs and qualifications are in source-notes1523.
COMPARISON: Schmeisser's general matrix lemma covers the proposed total-height majorant; Watrous covers principal compression. The inspected optimal diagonal-balancing theorem concerns an induced whole-matrix infinity norm and does not settle the imaginary-part Schatten cost. C028a/c retain their different reference-family stops.
GAP: The uniform positive degree-linear terminal-block cost floor is unproved. Actual centered coefficient algebra and optimization over unrestricted positive ratios remain for one separate calculation; no general norm theorem evaluated that specialization in the passages checked.
REASON: Essential coverage is now adequate for a finite known-method specialization, with no matrix-theorem reproof. Review1523 is literature-only and derives no terminal estimate; the newly nominated continuation receives separate approval before research.
SCOPE: Actual b_j and centered Q_d(y)=P_d(y-b_1) of C028d, P_d=R_d/gamma_0 of C028b, integer d>=3, all root multiplicities; positive diagonal entries may depend arbitrarily on d. No RH, simple roots, bounded scaling condition number, positive symmetrizer, sublinear cost or new degree asymptotic is assumed.

## Completed source decision1523

[Source notes1523](2026-11-18-centered-companion-source-notes-1523.md)
record the exact primary interfaces and their applicability. The norm
majorant and compression are known inputs; the actual finite-block
optimization remains unpaid. Schmeisser's general matrix lemma, rather
than its orthogonal coefficient theorem, is the relevant interface.
No new lemma, coefficient identity, degree estimate or mathematical
script was produced. Full matching Mathlib coverage is unchecked.

The selected continuation tests only the last three principal coordinates
with arbitrary positive scaling ratios. Its exact target and separate
approval requirement are in
[assessment1523](2026-11-18-centered-companion-terminal-block-test-1523.md).
A positive uniform degree-linear floor stops this majorant only; failure
of that block test supplies no o(d) upper bound. No independently
justified theta-specific sublinear mechanism was identified, so this
finite specialization is not routed as a creative proof attempt.

## Original nomination1522 (historical scope, not current source status)

## Proposed object and bounded decision

Use C028d's already defined real coefficients

    Q_d(y)=y^d+c_(d,1)y^(d-1)+...+c_(d,d).

Let A_d be its monomial Frobenius companion matrix: entries
(A_d)_(j+1,j)=1 for 1<=j<d and
(A_d)_(j,d)=-c_(d,d-j+1) for 1<=j<=d, with other entries zero.
For a positive diagonal D define the proposed cost

    K_d(D)=||(D A_d D^(-1)-(D A_d D^(-1))*)/(2i)||_1,

where * is conjugate transpose and ||.||_1 here means the Schatten
trace norm (sum of singular values), not the entrywise norm. These are
candidate definitions only. Source review must verify the proposed
comparison H_d<=K_d(D), and its precise hypotheses, before any use.
The translation by real b_1 preserves root heights; the actual centered
coefficients and all factorials must be retained. No new coefficient
identity is asserted in this nomination.

The bounded prospective test is whether a terminal principal block of
fixed size at most four gives a positive degree-linear lower bound for
K_d(D), uniformly over all positive D. Review the known scaling and
compression results first. If such a bound is already covered, import
it with the actual specialization; if only a finite algebraic difference
remains, nominate that difference for a separate research turn. A floor
would stop this majorant family, not lower-bound H_d or refute RH. If no
floor is justified, that is not evidence for an o(d) upper bound: record
the exact surviving optimization and its next discriminating test.

Plausible downstream use is an explicit sequence D_d with K_d(D_d)=o(d),
which, if the comparison is valid, would pay C028b's criterion and the
S_F=0 gap identified by C028g. This strong threshold is unresolved;
finite-dimensional numerical optimization or a large majorant is not
evidence that actual nonreal roots exist. Do not assume a positive
symmetrizer or choose a similarity by already knowing the roots are real.

## Reuse, failures and routing limits

Preserve C028a/c's stopped coefficient budgets. The difference to assess
is diagonal scaling of one explicitly fixed companion representation,
not another parameter choice inside either stopped reference family.
The November4 exact-projection-similarity assessment concerns a separate
fixed-pair determinant normalization, so its algebraic similarity scope
does not pay this height norm. The prior derivative/primitive direction
stop1514/1515 also supplies no upper bound for this cost. These are
comparisons, not new mathematical inputs or claims of exhaustive search.

The next step is literature_comparison, standard/high. A creative central
attempt is not yet justified: source coverage and a theta-specific
sublinear-cost mechanism are both absent. A finite scaling obstruction
could instead be a routine known-method specialization; do not label it
creative merely because it addresses the central gap. If source review
identifies a genuinely new mechanism, nominate its precise bounded test
and escalation separately. No mathematics from this new target was
derived or approved during audit1522. Full matching Mathlib coverage is
unchecked, not absent.
