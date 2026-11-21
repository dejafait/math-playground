# Finite heat–Laplace bridge audit — nomination1110

TARGET: Audit C030a's fixed-degree heat-to-mixed-form implication, including squared-node multiplicities, factorial normalization, both improper determinant compositions and strictness, without asserting its heat-block premise.
CHECKED: 2026-11-16
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse assessment1108 and nomination1107/comparison1108 for exact transform coverage, L033/L038/L041 duplicates and scalar/connected-partition/fan stops; no fresh discovery search is claimed for this newly written audit target.
SOURCE_EVIDENCE: Prior inspected tools: Sra Hexagon2610.00584v1 https://hexagonmath.org/pdf/2610.00584v1 LemmaC.1/PropositionC.2 pp18-19; Ruzza4May2022 https://webpages.ciencias.ulisboa.pt/~gruzza/introRMT.pdf Lemma3.1.1 (3.1.1) pp27-28; Polson https://arxiv.org/pdf/1708.02653v24 Definition5.1 (4) and Section6.4; DLMF https://dlmf.nist.gov/5.12.E1 and https://dlmf.nist.gov/5.9.E1. Step1110 checked these exact applicability passages, without a new sign-theorem review.
COMPARISON: C030a supplies the missing conditional specialization using known strict kernel transfer and Andreief; its full improper-integral and multiplicity argument is newly written and needs separate critical review. No mathematical novelty beyond the checked sources is claimed.
GAP: Verify that the complete determinant-product majorant controls both limits, the ordered chamber factorials cancel correctly, and a compact positive contribution proves strictness for every fixed finite size under the exact premise.
REASON: Separate literature review1111 completes the audit gate using the unchanged finite conditional scope and inspected primary theorem cases; the mathematical audit remains unperformed. Existing assessment1108 covers the tools, not certification of C030a.

The main unresolved claim is L030-L032/C032a actual-Xi Q(q)>=0 for
every real polynomial. This audit can establish whether the proposed
conditional bridge is safe to use in a later finite-source application
or independently signed mechanism. It cannot certify the premise.

Essential local inputs are C030a and L018/L024-L026/L030.
Inspect the canonical proof in
`lemmas/C030a-finite-heat-laplace-mixed-form-transfer.md`.
The bounded audit must check:

- The one-node-per-plus/minus-pair convention and conjugate off-line
  squares, with multiplicities; a_j>63/4 and a_j>=(63/65)|lambda_j|.
- The L024-based derivative domination and complete quadrant bound
  A_rs=sum a_j^(-r-s-2), before beta/gamma normalization to S_(r+s+2).
- Exact use of Sra's all-positive-time strict B_(d+1) premise;
  no semidefinite or single-time replacement.
- Ruzza's pairwise L1 hypotheses at each composition, orientations,
  the full (n!)^3 A_*^n bound, and removal of both compact cutoffs.
- Cancellation of the two 1/n! factors by ordered chambers; retention
  of a compact positive box; symmetry, Sylvester and finite-rank cases.
- The degree-one coefficient 2c0c1 S3, the maximum S_(2d+2), and the
  distinction between q(X)=sum c_r X^r and p(x)=sum c_r x^r/r!.

Continue if those checks validate the exact finite implication. If a
failure occurs, preserve the unconditional identity when justified,
repair only what is supported, and record the lost conclusion.
No source-stated numerical block range, common-graph realization,
semidefinite extension, all-order limit or new positivity construction
is included. Mathlib coverage remains unchecked. There is no
cross-notebook input.

This is a conceptual audit of analytic limits and strictness, not
creative work. No independently signed new central mechanism has
emerged from the specialization; that is the present blocker to
nominating a justified creative attempt.

## Completed audit coverage review1111 — 16 November 2026

LITERATURE_REASON: The newly written C030a audit had REVIEW_REQUIRED status; this separate turn compares its exact obligations with ready assessment1108 rather than reopening sign discovery.
SCOPE: Audit only C030a under its stated fixed finite d and all-positive-time strict premise (P), using L018/L024-L026/L030. No new source-sign application, semidefinite extension, all-order inference or new mechanism is authorized.

Reused assessment1108 and completed comparison1108 in nomination1107
for the transform search, L033/L038/L041 duplicates, and recorded
scalar, connected-partition and direct-fan failures. These are unchanged
comparisons, not a fresh novelty search. Read C030a solely to delimit
the audit's obligations; no step of its proof is certified in this turn.

Reopened [Sra, Hexagon2610.00584v1](https://hexagonmath.org/pdf/2610.00584v1),
Lemma C.1 and Proposition C.2, printed pp18-19 (PDF indices17-18),
including both complete proofs. C.1 assumes real C^(k-1) functions
with positive initial Wronskians. Its induction normalizes by a
positive first function, differentiates the quotients, subtracts rows
and integrates on adjacent intervals. C.2 assumes smooth real f and
strict positive definiteness of the signed differential block for
every t>0; it applies C.1 twice to give positive ordered minors of
f(x+y) through order k. No improper composition, semidefinite
variant or one-time substitute is supplied by this theorem. This is
the exact version cited by C030a, not the unrelated arXiv identifier.

Reopened [Ruzza, 4 May 2022 notes](https://webpages.ciencias.ulisboa.pt/~gruzza/introRMT.pdf),
Lemma3.1.1 equation(3.1.1) and full proof(3.1.2)-(3.1.9),
printed pp27-28 (PDF indices26-27). The measure-space statement
allows measurable complex functions with every cross product in L1.
The bilinear determinant identity has n! multiplying the entry
determinant, without conjugation. The proof expands permutations,
renames variables and factorizes integrals. These hypotheses must
be checked for each use; they do not certify the local triple
product majorant or preservation of strictness at infinite endpoints.
Reproving this identity is unnecessary.

Reopened [DLMF5.12.1](https://dlmf.nist.gov/5.12.E1) and
[DLMF5.9.1](https://dlmf.nist.gov/5.9.E1); reuse assessment1108's
parameter conditions and principal-power qualification. Their formulas
cover the proposed beta/gamma tools, not an already verified entry
identity. Polson v24 Definition5.1/Section6.4 remain reused source
conventions, not a newly imported sign theorem. The audit should
resolve the p14 versus p15 Section6.4 locator discrepancy between
comparison1108 and C030a if that passage is retained as a citation;
the direct beta/gamma proof does not depend on importing it.

**Decision:** SPECIALIZE authorizes a conceptual audit of the written
applicability argument. The precise remaining work is the bounded
checklist above: node multiplicities and reality, domination and
normalization, both determinant compositions, chamber factorials,
strict compact contribution, rank, and the exact mixed observable.
These local obligations are not discharged by quoting known tools.
No missing essential source blocks that audit. Mathlib remains
unchecked; no assertion of absent coverage is made.

Continue only if the exact finite implication survives these checks.
On failure identify the first unsupported claim and preserve any
independently justified identity; do not weaken (P) silently. The
main all-degree Xi sign gap and common-graph realization remain open.
This is source-gate completion, with no new mathematical result and
no proof review outcome. The lack of an independently signed central
mechanism still blocks a justified creative nomination; completing
the essential analytic audit takes priority over inventing one.
