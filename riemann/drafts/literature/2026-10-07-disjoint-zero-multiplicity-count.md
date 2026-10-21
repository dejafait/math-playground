# Proposed coverage review for a disjoint-zero count comparison

TARGET: Determine whether nonzero real analytic F,G with no common real zeros, D≤0 and L(G)>0 on an eventual ray must satisfy N_F^mult([H,X])≥N_G([H,X])−C uniformly in X≥H with full closed-endpoint counts.
CHECKED: 2026-10-07
DECISION: EXPLORE
SEARCH_EVIDENCE: Six targeted searches on 2026-10-07 plus scoped duplicate/failure checks; reused the parent assessment and inspected the previously unread Borcea–Shapiro polynomial-pencil lead; no matching result found in this bounded review.
SOURCE_EVIDENCE: Reused drafts/literature/2026-10-06-multiplicity-count-implication.md; reopened MIT 18.034 Lecture 9 Theorem 9.1 and full proof pp. 1–2; read Borcea–Shapiro arXiv:math/0404215v1 (11 April 2004), §1 pp. 2–3 and §4 pp. 12–13, Proposition 3 with proof and Corollary 5.
COMPARISON: L371 and L373 do not meet disjointness; inspected sources still require a common ODE, global polynomial/entire pencil structure or a derivative relationship. Common-zero exclusion alone does not discharge those source hypotheses by citation.
GAP: Decide the exact disjoint-zero analytic-ray count implication, including possible Wronskian degeneracy and full F endpoint multiplicities; actual-family disjointness and D≤0 remain independently unproved.
REASON: The changed hypothesis has now received a bounded primary-source comparison; one later direct attempt is justified without claiming novelty or importing a stronger separation theorem.
SCOPE: Ordinary physical derivatives L(u)=u′²−uu″, B=2F′G′−FG″−F″G, D=B²−4L(F)L(G); real analytic functions on an open neighborhood of [H,infinity), neither identically zero, no t≥H with F(t)=G(t)=0; F zeros counted with full analytic multiplicity and G zeros counted distinctly, including both endpoints; C may depend on F,G,H but not X.

LITERATURE_REASON: The changed no-common-real-zero hypothesis lies outside the parent assessment; this turn reviews that exact change and a previously unread relevant lead.

## Completed source review

The main gap remains actual-theta mixed positivity and the total signed
L367 margin. A bounded-deficit theorem could supply a count consequence
for a future actual-family discriminant argument. It would still require
actual eventual disjointness, D≤0, and signed arithmetic count information.
L368 and audited L372 are downstream context only; neither establishes
these missing premises. No detailed actual-family proofs were needed.

The essential local records are L373 (physical definitions and audited
simple-common-zero obstruction), L371 (distinct-count failure), and
`drafts/literature/2026-10-06-multiplicity-count-implication.md`.
The L373 statement, physical jet calculation and Wronskian discussion
were read. The parent source comparison and query record were read in
full relevant ranges. Scoped searches of the two discriminant assessments
and weak-discriminant ATTEMPTS found no saved disjoint-zero theorem.
L371's supplied overview and the parent comparison suffice for this
review; its detailed audit was not repeated. Existing stops are preserved.

1. [MIT 18.034, Spring 2009, Lecture 9](https://ocw.mit.edu/courses/18-034-honors-differential-equations-spring-2009/0cdeb657491010f0f8c60aa49f2d5248_MIT18_034s09_lec09.pdf),
   Theorem 9.1, printed pp. 1–2, statement and entire proof reopened.
   Independent solutions of the same homogeneous second-order equation
   with continuous coefficients have alternating zeros. The proof uses
   a nowhere-zero Wronskian and opposite derivative signs at consecutive
   solution zeros. TARGET supplies neither the equation nor that
   nonvanishing premise. Removing common zeros from TARGET does not
   by citation establish either. No specialization is imported.

2. J. Borcea and B. Shapiro,
   [Classifying real polynomial pencils](https://arxiv.org/pdf/math/0404215v1),
   arXiv:math/0404215v1, 11 April 2004. Read §1, printed pp. 2–3,
   and §4, pp. 12–13: Proposition 3 and its complete proof,
   canonical-reduction definition, Corollary 5. Their introductory
   constant-pencil-count discussion uses a Wronskian without real zeros.
   Proposition 3 identifies real zeros of P+µQ (nonreal µ) with common
   real zeros of P,Q. Corollary 5 assumes degrees n,n−1, no common
   real zeros and positive leading coefficient of Q; it relates the
   half-plane zero imbalance of P+µQ to the canonical reduction of the
   two real-zero arrangements. It supplies no D inequality or analytic-ray
   bounded deficit. This is a polynomial/global winding comparison, not
   an import. No critical-point condition is inferred from disjointness.
   The source labels its Hawaii statement a conjecture; it is not used
   as an established theorem. Its classification proofs were not audited.

The parent assessment's inspected Borcea–Brändén–Shapiro Theorems 9–10,
Csordas–Escassut Theorems 4.3/4.5, Tyaglov Theorem 8 and
Gnatyuk–Tyaglov Theorem 4.5 comparisons are reused rather than re-browsed.
Their precise versions, pages, URLs and inspected proof cases remain in
that assessment. Excluding common real zeros does not supply global
pencil real-rootedness/HB membership, a one-function derivative relation,
or the finite-nonreal-zero/product hypotheses they require. None is a
citation for this arbitrary-pair implication. The previously unread
polynomial-pencil lead is now inspected only in the ranges stated above.
The parent's arXiv:2406.00686 lead remains unread and is not used.

## Search record and decision

Queries submitted on 2026-10-07:

- `"Laguerre inequality" "two" "interlacing" functions`
- `"Wronskian" "discriminant" "zero separation"`
- `"Sturm" "separation" "no common zeros" analytic functions inequality`
- `"Laguerre inequality" "pencil" disjoint zeros`
- `"Wronskian" "W" "separation" differential inequality zeros functions`
- `"Classifying real polynomial pencils" Borcea Shapiro`

Search hits about orthogonal-polynomial families and time-scale equations
were not treated as coverage. Search snippets were discovery aids only.
ArXiv PDF screenshots for p. 12 returned an internal error; readable
primary PDF text covered the complete selected statements and elementary
Proposition 3 proof, so no essential source blocker remains. No exact
matching source theorem or source counterexample was found. This bounded
assessment is EXPLORE, not an exhaustive survey or evidence of novelty.
Full matching Mathlib coverage is not checked; no mathematical result is
being added, reproduced or imported in this literature-only turn.

A later attempt should test a finite C depending on F,G,H but independent
of X, or an exact disjoint-zero analytic pair with unbounded deficit.
Continue if the exact hypotheses yield a count proof with every local
zero/degeneracy case and the interval assembly justified. Abandon this
restricted implication if a rigorously verified counterexample exists.
Do not assume a common ODE, Wronskian nonvanishing, global real-rooted
pencils or simple F zeros. No such implication or counterexample was
derived here. The ready assessment remains tied to the unchanged TARGET;
its new readiness is subject to the supervisor's separate next-turn
approval before mathematics. No cross-notebook input is proposed.
