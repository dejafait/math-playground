# Coverage proposal for a critical audit of L374

TARGET: Critically audit L374's disjoint-zero count theorem, including pencil positivity, finite-order degeneracies, analytic dependence and full closed-endpoint counting.
CHECKED: 2026-10-07
DECISION: EXPLORE
SEARCH_EVIDENCE: Reused the six-query exact-hypothesis search and parent comparisons in drafts/literature/2026-10-07-disjoint-zero-multiplicity-count.md; scoped L374, its attempt/history and the recorded L373 failure; no new discovery search required for the unchanged theorem audit.
SOURCE_EVIDENCE: Reopened MIT 18.034 Spring 2009 Lecture 9 Theorem 9.1 and complete proof, printed pp. 1–2; reopened Borcea–Shapiro arXiv:math/0404215v1 (11 April 2004), Proposition 3 with complete proof and Corollary 5 with canonical-reduction definition, printed pp. 12–13; read canonical L374 in full for source-scope comparison only.
COMPARISON: L374 derives pencil positivity and Wronskian nonvanishing from the physical inequalities plus disjointness; the reviewed common-ODE/global-pencil results cannot replace that derivation by citation.
GAP: A separate mathematical audit must validate the finite-order contradiction, analytic identity case and C=1 bound; coverage permits that audit but does not establish correctness.
REASON: The unchanged analytic-ray hypotheses fit the ready parent EXPLORE comparison; this separate coverage turn maps the new audit cases without deriving or approving mathematics.
SCOPE: The exact hypotheses and proof of L374, ordinary physical derivatives on an open neighborhood of [H,infinity), no common real zeros, D≤0, L(G)>0, and full closed-endpoint multiplicities.

Essential input is canonical L374. L373 supplies obstruction context only;
its common-zero example must remain excluded for the stated reason.
The parent source assessment
`drafts/literature/2026-10-06-multiplicity-count-implication.md` remains
available for precise source comparisons; no actual-family lemma or
cross-notebook input is needed for the audit.

The critical points for a later mathematical audit are whether (2)
really yields (3) for every fixed pencil pair including a zero diagonal,
whether every proposed Wronskian zero produces a finite-order zero or
global dependence, whether the leading orders in (4) contradict (3)
also at H, and whether k closed-interval G zeros always yield k−1
distinct interior F zeros. Retain or repair the theorem only after all
these cases pass. Full matching Mathlib coverage is not checked.

Actual-family D≤0 and eventual disjointness, the signed arithmetic count
comparison, total L367 margin and the main RH gap remain unresolved.
This proposal records no additional mathematical derivation or audit
result. Coverage approval is now complete; the next invocation may perform the separate mathematical audit.

## Completed source-scope review

LITERATURE_REASON: The essential unread item was L374's new proof relative to the ready parent comparison; its proposed audit required separate coverage approval. This review closes that process gap without repeating discovery searches.

The main gap remains global actual-theta mixed positivity and the total
L367 signed margin. The intermediate target is the L374 critical audit.
A retained conditional count theorem could later be combined with response
count information; actual-family D≤0, eventual disjointness and a signed
arithmetic comparison remain independent missing premises.

Primary ranges actually reopened:

- [MIT Lecture 9](https://ocw.mit.edu/courses/18-034-honors-differential-equations-spring-2009/0cdeb657491010f0f8c60aa49f2d5248_MIT18_034s09_lec09.pdf), Theorem 9.1 and full proof, printed pp. 1–2 (PDF pages 2–3). It assumes independent solutions of a common homogeneous second-order equation with continuous coefficients. Its interval sign argument uses nonvanishing Wronskian. L374 does not assume that equation, so this is a comparison rather than an import.
- J. Borcea and B. Shapiro, [Classifying real polynomial pencils](https://arxiv.org/pdf/math/0404215v1), version 1, printed pp. 12–13. Proposition 3 and its full proof concern real zeros of P+µQ for nonreal µ and common real polynomial zeros. Corollary 5 assumes degrees n,n−1, no common real zeros and positive leading coefficient of Q; it describes half-plane imbalance through canonical reduction. Neither supplies the physical discriminant implication or analytic-ray endpoint count.

The parent's inspected global Obreschkoff/Hermite–Biehler and
one-function logarithmic-derivative comparisons are reused within their
recorded scopes. Its arXiv:2406.00686 lead remains unread and is not an
essential input. No essential source blocker remains. The bounded search
did not establish a stronger matching theorem; no originality is claimed.
No theorem is imported here. Full matching Mathlib coverage is not checked.

Scoped duplicate/failure checks identify L374 as the canonical count
result awaiting audit, with L373's retained common-zero failure as context.
The earlier six-query review already covered disjointness. L374 was read
to identify source scope and required audit cases, not to validate its
calculations or conclusion. No detailed actual-family proof is needed.

The future audit must check (2) to (3), including zero diagonals;
differentiated finite-order expansions (4), m=2 and approach from the
right at H; the identity theorem on the connected component; dependence
with a nonzero proportionality constant; both Wronskian-zero cases;
compact zero-set finiteness; and k=0,1 and k≥2 closed-endpoint counts,
including X=H. These are audit questions, not new deductions. No common
ODE, global real-rooted pencil or nonvanishing Wronskian may be assumed
by analogy with the sources.

Continuation test: retain L374 only if every hypothesis, local case and
C=1 endpoint count passes critical review. A failed load-bearing inference
requires a documented repair or withdrawal of that claim while preserving
prior work and common-zero stops. Approval covers exactly TARGET, not a
broader actual-family attempt. No lemma, mathematical script, DAG or
PROOF change is made in this literature-only step.
