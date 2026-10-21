# Signed linear response mean — critical-audit coverage

TARGET: Critically audit L369's negative dyadic-mean theorem for the signed linear response.
CHECKED: 2026-10-05
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the exact-statement, mixed-zeta-moment and truncated-series searches in drafts/literature/2026-10-05-gaussian-linear-response-sign.md; compared the complete L369 audit obligations with that assessment, relevant local inputs and recorded failures; no fresh discovery queries.
SOURCE_EVIDENCE: Reinspected Arias de Reyna arXiv:2406.16667v1 (2024-06-24), Theorem 6 and complete proof, pp. 5–6, and Lemmas 2/4/5 in primary HTML; reused inspected NIST DLMF v1.2.8 (2026-09-15), 25.2.1/11, 25.4.1–5, 5.11.1–2 and section 5.11(ii), 5.15.8–9, and named foundation Cauchy estimates.
COMPARISON: Primary scalar coverage includes the fixed-cutoff critical-line complex neighborhoods and right-line absolute jets; it does not state L369's polarized coefficient mean or its negative constant. The exact audit lies within the assessed scope, with family-specific algebra, weighted means and uniformity still requiring independent verification.
GAP: Verify L369 (7)–(22), especially the projection factor, differentiated reflection, fixed-cutoff Cauchy and pole estimates, full mixed off-diagonal budget, moving weights and negative-limit constant; coverage approval does not validate those claims.
REASON: No essential unread source or source blocker remains for this same-hypothesis audit; known scalar inputs suffice for a bounded reproduction/specialization, with no claim of originality.
LITERATURE_REASON: The saved continuation required separate approval of the newly written proof's audit scope; this turn performs that comparison and reuses ready discovery evidence rather than repeating searches for scheduling.
SCOPE: Only actual F_0/G and positive A of L366/L358, L367's coefficient B, and L369's ordinary real-frequency jets through order two and normalized dyadic mean; no division by F_0/G, RH premise, positive regulator or shrinking-window return.

## Primary source and precise applicability

The saved sign assessment contains the discovery queries, strongest inspected
comparison and unused leads. This turn read it and the complete L369, plus
selected statements of L018/L358/L366/L367/L368, foundation gamma/Cauchy
coverage, prior response audits and the common-threshold failure. No sibling
notebook was consulted. No matching signed-mean theorem was established in
those searches; this is a coverage finding, not evidence of novelty.

J. Arias de Reyna, *On the approximation of the zeta function by Dirichlet
polynomials*, [arXiv:2406.16667v1, Theorem 6 and proof, pp. 5–6](https://arxiv.org/pdf/2406.16667v1#page=5),
provides, for fixed x>0, sigma>=0 and 0<t<=x, the zeta truncation with
pole correction x^(1-s)/(s-1) and absolute error at most (29/14)x^(-sigma).
The proof uses weighted tail summation with a single zero dual mode,
passes its upper cutoff to infinity for sigma>0, and handles sigma=0
by continuity. Lemmas 2/4/5 and their relevant proof cases were read;
no RH assumption or hidden height-dependent real-part restriction appears.
This confirms the previously inspected statement rather than extending it.

L369 sets x=3H and uses disks of radius min(1/4,1/log x) about
1/2+it for H<=t<=2H. At large H these disks have positive real part
and imaginary part strictly between zero and x, within Theorem 6's domain;
they avoid the pole at 1. Cauchy's derivative estimate is an already named
foundation tool. The source does not itself supply derivative bounds:
the later audit must verify the analytic difference, disk supremum and
radius losses, and retain every differentiated pole-correction term.
Neither an O term on the real line nor a cutoff varying with t may be
differentiated. Import the scalar theorem; no reproof is needed.

Reuse [DLMF 25.2.1/11](https://dlmf.nist.gov/25.2#E1) on Re s>1
for the fixed 5/2 line, with local uniform convergence checked in the
audit. Reuse [DLMF 25.4.1–5](https://dlmf.nist.gov/25.4) and L018
for completion/reflection and critical-line reality, without a zero premise.
The exact reflected response is L366 (1); L368 (3) supplies b and its
carrier. Prior audits of L366 and L368 are recorded in their 2026-10-05
histories; repeating their contour proofs or quadratic-margin calculation
would be duplicate work. The new mixed polarization is not imported from them.

Reuse [DLMF 5.11.1–2 and remainder qualifications](https://dlmf.nist.gov/5.11#ii)
and [5.15.8–9](https://dlmf.nist.gov/5.15#E8). The argument 1/4+it/2
lies in a closed sector away from the negative real axis. These support
controlled separate gamma jets or analytic-remainder Cauchy estimates,
not differentiation of an uncontrolled asymptotic error. L369 uses the
phase of Q rather than Qb, so the later audit must check that distinction
and the full p-factor envelope curvature.

Pliego's mixed-moment statements and Csordas–Vishnyakova's all-level
criterion remain mismatches as recorded in the sign assessment. Their
proofs need no additional read. Titchmarsh 4.11 and other discovery leads
remain uninspected alternatives, not essential inputs; Theorem 6 supplies
the scalar truncation. Supporting DLMF books remain unread. No access
blocker persists, and no additional source is invoked for a new conclusion.

## Bounded audit, downstream use and stopping test

The main gap remains global actual-theta mixed positivity. The one
intermediate target is independent verification of L369's claimed negative
dyadic mean. If it survives, eventual nonnegative signing of L367's linear
coefficient is a checked obstruction; total compensation still requires
a separate actual-theta margin and remainder comparison.

The mathematical audit must independently check the projection factor and
all terms in (7)–(11); Cauchy/pole bounds in (12)–(14); and every range of
the infinite mixed-series estimate (15)–(18), including n=m=1, all other
collisions, near-diagonal logarithmic gaps and the infinite m tail. Check
complex weight variation (19)–(20), the residual bound (21), and the
constant and error in (22), without assuming them from L369. Check zero-safe
normalization, evenness and one common finite unevaluated onset.

Continue if the stated limit -zeta(3)/(4pi) with vanishing error survives,
or a precisely justified correction retains a fixed negative margin.
A wrong constant, uncovered term or nonvanishing error requires recording
its exact failure and narrowing or abandoning this certificate. It does
not refute RH or sign the total theta expression. L365's common global
regulator stop remains preserved in ATTEMPTS/2026-10-04-gaussian-common-first-sign-threshold.md;
this audit neither reopens it nor calls qualitative density quantitative.
Independent unresolved gaps include the total L367 margin and relative
remainder, higher levels, low indices, heights above forty and endpoint
arithmetic margin.

## Mathlib and completed outcome

Full matching signed-mean, differentiated truncation and mixed-mean coverage
in Mathlib: **not checked**. Cauchy estimates, holomorphic-series operations
and integration by parts are supporting named tools; no full matching
theorem or absence is asserted. No proof or source reproof was performed.

Outcome: EXPLORATION / LITERATURE / NOVELTY_UNCHECKED. The new evidence is
that the exact proposed audit needs no essential source beyond ready coverage.
SPECIALIZE approves the prospective mathematical audit only, subject to
separate next-turn supervisor approval. L369 remains unaudited. No lemma,
mathematical script, DAG or PROOF was changed.
