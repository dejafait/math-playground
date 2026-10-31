# Full raw coefficient specialization — critical audit coverage

TARGET: Critically audit L548's new full raw coefficient specialization (B1)–(B2) and its complete ramified/unit case table against DR v3.
CHECKED: 2026-10-31
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the exact full-domain comparison and duplicate/failure record in drafts/literature/2026-10-31-family003-full-cusp-coefficient-bound-review.md and the prior application assessment; unchanged theorem domain and no new discovery claim. The new proof to review is L548's full raw coefficient specialization dated 2026-10-31.
SOURCE_EVIDENCE: DR arXiv:2109.07463v3 https://arxiv.org/html/2109.07463v3 Section 1.3 Gauss normalization, (2.1)–(2.2), (5.7)–(5.16), Appendix A rows 1,19,10; pinned TeX https://raw.githubusercontent.com/openai/math/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex lines 1806–1854. Complete case and source-proof qualifications: drafts/audits/2026-10-31-family003-full-cusp-coefficient-source-notes.md.
COMPARISON: The exact envelope is source-claimed and the local application is now written in L548. Independent review should check its applicability and constants; reproducing this specialization is justified by removal of an explicitly retained premise. It is not a new cubic-theta bound or an audit of Patterson/Hasse proofs.
GAP: No independent critical verdict on the newly written full-domain specialization is claimed. Check zero-ring conventions, all-primary norm applicability, unit shifts on nonunits, h-to-k arithmetic, support and conjugate unit classes; unrelated finite inputs, source proofs, uniform closure and actual-Xi signs remain separate.
REASON: Separate literature approval completed on 2026-10-31 for the newly written application. Primary coverage and hypotheses are unchanged; the exact target is ready for a research audit. This is coverage approval only, with no mathematical verdict.
SCOPE: Only L548 (3), its new (B1)–(B2) proof and exhaustive source-case table, with L547 (9) as the reviewed cusp input; all primary squarefree nonzero n and primary nonzero b, all units, k>=-4, no S-mask, shared n,b primes and otherwise-zero cases. Exclude upstream theta/norm proof audits and new Gauss or analytic estimates.

The original [application assessment](2026-10-31-family003-full-cusp-coefficient-application-audit.md)
was saved before the completed research step. Its sources were inspected
again for the application, including every relevant case. The new audit
should check the canonical proof, rather than accept the working-record
summary as evidence. Continue only if every retained coefficient satisfies
27*3^(k/6)*|b| without a stronger assumption. Preserve any missed case,
phase/domain error or failed threshold; correct an error only with the
necessary complete argument. Do not repeat the upstream Hasse/Patterson
proofs or apply a composite finite-field theorem.

Mathlib coverage is the reused supporting finite-ring unit-shift theorem
[gaussSum_mulShift_eq](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/NumberTheory/GaussSum.lean#L54).
Full matching cubic-theta coverage is not checked. No cross-notebook
input is involved. This is approved source coverage for the exact audit target, not approval
of the mathematics or a critical-review verdict.


## Separate coverage approval, 2026-10-31

LITERATURE_REASON: The supervisor requires a separate literature approval
of the newly written L548 specialization; reuse the prior discovery and
comparison rather than repeating searches or performing the audit here.

Read the canonical new section (B1)–(B2) and its table to establish the
review scope. Reused the full-domain source notes, prior application
assessment and application history for duplicates and recorded failures.
The earlier good-prime sextic restriction is a scope boundary, not a
counterexample to the ordinary cubic target. No broader claim is approved.

Reopened [DR v3](https://arxiv.org/html/2109.07463v3): Section 2
(2.1)–(2.2), HTML lines 334–351; all branches and otherwise-zero clauses
of (5.7)–(5.8), lines 679–687; (5.13)–(5.16), lines 711–733;
Appendix A rows 1,10,19, lines 3408,3417,3426. These are the required
primary statements, with primary-modulus and squarefree hypotheses.
The coefficient formulas are cited there to Patterson (1977), Theorem
8.1, (8.8)–(8.9), Table III p.151; the norm identity is cited to Hasse
(1950), pp.443–445. Those upstream proofs remain imported and unaudited.
DR's conditional prime-sum results are outside this scope.

Reuse the previously inspected pinned-TeX passage and Mathlib supporting
unit-shift theorem from the source notes; neither is a full matching
formalization. No source blocker or essential unread statement was
identified for this finite application audit. SPECIALIZE remains the
appropriate decision: the next turn checks the written specialization,
including modulus one, rather than proving another theta theorem.

No new mathematical result or independent verdict is established by this
approval. Outcome STALLED records that source readiness is unchanged.
Proceed directly to the exact research target; do not schedule another
approval of this unchanged coverage. The continuation test remains the
complete coefficient envelope check specified above.
