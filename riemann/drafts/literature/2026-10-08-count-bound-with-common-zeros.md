# Completed source review: count loss in the presence of common zeros

TARGET: Assess whether D≤0 and L(G)>0 imply N_G([H,X])−N_F^mult([H,X])≤N_common([H,X])+C_H for nonzero real-analytic pairs, where N_common counts distinct common zeros.
CHECKED: 2026-10-08
DECISION: EXPLORE
SEARCH_EVIDENCE: Nine targeted common-zero/Laguerre-pencil/Wronskian-count searches on 2026-10-08; scoped local theorem and failure comparison; no matching bound or counterexample established in inspected sources.
SOURCE_EVIDENCE: Reused the completed multiplicity and disjoint-count assessments; reopened MIT 18.034 Spring 2009 Lecture 9 Theorem 9.1 with complete proof pp. 1–2, Borcea–Brändén–Shapiro Master4 §3.1 Theorems 9–10 p. 9, and Borcea–Shapiro arXiv:math/0404215v1 Proposition 3 with complete proof and Corollary 5 pp. 12–13; precise URLs and scope below.
COMPARISON: L374 covers a disjoint ray, and L373 refutes constant deficit without a common-zero loss. The inspected primary sources require a common regular ODE, globally hyperbolic/stable polynomial pencils, or a derivative-related global pair; none supplies this analytic-ray inequality by citation.
GAP: Prove or refute the exact distinct-common-zero loss with an X-independent C_H; a finite-interval localization of L374 and complete multiplicity/endpoint accounting remain to be justified, not presumed.
REASON: The changed quantitative target now has a bounded primary-source comparison and a concrete local proof test; one later mathematical attempt is justified without a theorem import or originality claim.
SCOPE: Nonzero real-analytic F,G on a connected open neighborhood of [H,infinity), ordinary derivatives, D=B(F,G)^2−4L(F)L(G), B(F,G)=2F'G'−FG''−F''G, L(U)=U'^2−UU'', with both inequalities throughout the ray and every X≥H; no assumed simplicity of F, common ODE, RH or actual-family disjointness.

LITERATURE_REASON: Allowing common zeros with an explicit distinct-count loss changes L374's load-bearing disjointness hypothesis and conclusion; prior ready coverage does not assess that extension.

This assessment approves source coverage for the unchanged TARGET, not
the inequality. No proof, counterexample calculation or new local lemma
was derived in this literature-only turn. Newly completed readiness
receives the supervisor's separate next-turn approval before mathematics.

The proposed inequality counts F zeros with full analytic multiplicity,
G zeros distinctly, and common zeros distinctly, all in closed [H,X].
C_H may depend on the fixed pair and H but must be finite and independent
of X. Strict L(G)>0 and analyticity are part of the target, not claims
imported for arbitrary pairs. The completed comparison below found no
inspected theorem supplying this exact bound or a replacement loss term.

Essential local inputs are L374, L373 and L377; L371 is multiplicity
contrast only. For source-scope comparison, L374's hypotheses and complete
main proof, L373's statement, full main proof and common-zero audit passage,
and L377's exact conclusion were read. The reused assessments are
`2026-10-07-disjoint-zero-multiplicity-count.md`,
`2026-10-07-disjoint-zero-count-audit.md` and
`2026-10-06-multiplicity-count-implication.md` in this directory.
Scoped checks of the relevant discriminant assessments, ATTEMPTS and
2026-10-07/08 histories found no canonical theorem for this loss term.
L371's recorded distinct-count failure and L373's multiplicity failure
remain intact. L375/L376 remain geometric obstruction context from the
supplied overview; their detailed proofs were not reopened.

Plausible downstream use: a valid quantitative bound could turn L377's
negative count excursions into a necessary lower bound on common-zero
counts under the additional, still-unproved eventual D≤0 premise.
An actual-family upper bound on those common-zero counts would remain
an independent unresolved arithmetic problem. Merely recovering the
already established implication that common zeros must occur arbitrarily
far out would not justify a new mathematical attempt.

## Primary sources and comparison

1. [MIT 18.034 Spring 2009, Lecture 9](https://ocw.mit.edu/courses/18-034-honors-differential-equations-spring-2009/0cdeb657491010f0f8c60aa49f2d5248_MIT18_034s09_lec09.pdf),
   Theorem 9.1, printed pp. 1–2 (PDF pages 2–3). Reopened its equation,
   continuous-coefficient hypotheses, statement and full proof. Independent
   solutions of one regular homogeneous second-order equation have
   alternating zeros. The proof uses a nowhere-zero Wronskian and opposite
   derivative signs at successive solution zeros. TARGET lacks the common
   equation; this proof does not treat a Wronskian reset at shared zeros.
   It is a comparison, not an import or a specialization.

2. J. Borcea, P. Brändén and B. Shapiro,
   [Pólya–Schur master theorems for circular domains and their boundaries](https://staff.math.su.se/shapiro/Articles/Master4.pdf),
   author Master4 manuscript, §3.1, printed p. 9. Reopened proper-position
   conventions and Theorems 9–10, including both weak and strict clauses.
   Manuscript revision date remains unverified; this exact author version
   was retrieved on 2026-10-08. Hermite–Biehler assumes polynomial stability;
   Obreschkoff characterizes hyperbolicity of every real polynomial pencil
   member. Common roots are permitted in the weak formulations and excluded
   in the strict ones. Neither formulation replaces its global zero
   hypothesis with TARGET's first differential inequality on a ray.
   No such replacement or inference about common-zero counts is imported.

3. J. Borcea and B. Shapiro,
   [Classifying real polynomial pencils](https://arxiv.org/pdf/math/0404215v1),
   arXiv:math/0404215v1, 11 April 2004, §4, printed pp. 12–13.
   Reopened Proposition 3 and its entire real/imaginary-part proof,
   canonical-reduction definition and Corollary 5. Proposition 3 identifies
   real zeros of P+µQ, µ nonreal, with common real polynomial zeros.
   Corollary 5 assumes degrees n,n−1, no common real zeros and a positive
   leading coefficient for Q; it relates the half-plane zero imbalance to
   canonical reduction. Neither gives the proposed physical-discriminant
   count loss for arbitrary analytic functions. They are comparisons only.

Reuse the parent assessment's inspected Csordas–Escassut (2005)
Definition 4.2/Theorems 4.3 and 4.5, Tyaglov arXiv:0902.0413v2
Definitions 1–2/Theorem 8, and Gnatyuk–Tyaglov arXiv:2506.22330v1
Theorem 4.5 with its complete common-root/pole proof cases. Exact pages,
URLs and qualifications remain in the parent. Their entire HB/product
hypotheses or fixed derivative relationship and rational behavior at
infinity are absent from TARGET. Changing the loss term does not supply
these premises. These source inspections are reused, not reported as new
readings. No cited result is being reproved or imported in this turn.

## Search record and later bounded test

Queries submitted on 2026-10-08:

- `"Laguerre inequality" "pencil" "common zeros"`
- `"Wronskian" "common zeros" "zero count" real functions`
- `"Sturm separation" "common zeros" analytic functions`
- `"Laguerre inequality" "common" "pencil" zeros`
- `"interlacing" "common zeros" "count" analytic functions Wronskian`
- `"Wronskian" "common roots" "Obreschkoff"`
- `"Laguerre" "inequality" "common zeros" analytic functions`
- `"log-concave" "linear combinations" "zeros" functions separation`
- `"zero count" "common zeros" "Wronskian" inequality`

Hits on orthogonal-polynomial recurrences, ODE eigenfunctions and
coefficient-sequence log-concavity were discovery material only. Langley's
*Non-real Zeros of Derivatives* (2024) and the quasi-orthogonal q-Laguerre
common-zero paper are uninspected leads; no theorem from them is used.
The parent's arXiv:2406.00686 lead remains unread and unused. The selected
primary statements and essential separation/common-root proof cases were
available as readable PDF text. Screenshot calls supplied no additional
usable visual evidence. There is no essential source blocker for the
proposed direct test. This bounded search establishes no novelty and no
exhaustive absence claim. Full matching Mathlib coverage is not checked.

The specific later proof test is to reuse L374's finite-order Wronskian
and interval-sign proof portions on pieces separated by common zeros,
then check the exact loss after restoring the shared points. This is a
proposed argument, not a proved localization: L374 as stated needs a
disjoint entire ray and cannot simply be invoked on each bounded piece
when future common zeros remain. A later proof must justify the finite-
interval use, analytic dependence, compact zero-set finiteness, any
multiple F zeros, pieces with zero or one G zero, common zeros at H or X,
and absence of double counting. It must not assume a global Wronskian
sign across shared zeros or differentiate an unjustified deflated pair.

Continue only with a proved uniform finite C_H for the displayed
inequality, or an exact counterexample with an unbounded residual deficit
after subtracting N_common. A proof should reuse the available L374
argument rather than recreate an unrelated separation theorem. Abandon
this form on such a counterexample; a merely qualitative common-zero
conclusion repeats L377's joint-premise obstruction and is insufficient.
Preserve all prior failures. This is EXPLORE coverage for one separate
proof-or-counterexample attempt, with no mathematical conclusion approved.

Global mixed positivity, the total L367 margin, actual D≤0, actual
common-zero frequency, low-index signs, heights above forty and the
endpoint margin remain unresolved. No new zero-exclusion or sign range
is asserted. No lemma, mathematical script, DAG or PROOF change is made.
