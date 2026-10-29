# Source coverage for a covariant L128 repair

TARGET: Assess source coverage for a covariant Betti--Tate replacement of L128 Step 1 that preserves the original labeled ordinary tower and coefficient localization.
CHECKED: 2026-10-28
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 535 checked L128 Step 1/audit, L127 and ATTEMPTS/061/062; searched covariant Betti--Tate and Jacobian correspondence/transfer terminology; followed the period-paper lead to exact primary statements and reused unchanged steps 527/532. Queries and inspected passages: drafts/source-notes/2026-10-28-l128-covariant-transfer-coverage.md.
SOURCE_EVIDENCE: Milne AV v2.0 (2008), I Theorem 2.9 p.14 and Remark 10.7 p.45 https://www.jmilne.org/math/CourseNotes/AV.pdf; Milne Jacobian Varieties (2021), Theorem 2.5 pp.7--8 and Proposition 6.1/Corollary 6.3 pp.19--20 https://www.jmilne.org/math/xnotes/JVs.pdf; Sertoz--Ouaknine--Worrell arXiv:2505.20397v1, (4.5.54)--(4.5.55), (7.3.29)--(7.3.36), (7.4.37)--(7.4.43) https://arxiv.org/html/2505.20397v1; Fornea v2 Sections 2.1.2/2.2/2.4 and Lemma 2.22/Corollary 2.23 https://arxiv.org/html/2603.28327v2, including the PDF control diagram.
COMPARISON: Covariant Tate/homology lattice comparison and correspondence pushforward/transfer are covered, as are the source's separate pushdown control and pullback coefficient transition laws; none quotes an enlarged algebra action on N_0 or identifies the two limits. Apply these sources with original physical labels, rather than dualizing and suppressing inverses.
GAP: Prove the original-label relation transfer through the ordinary finite levels, faithful endomorphism detection, pullback direct limit and completion, checking product order and all U labels. The original R_0/I comparison and L128 Steps 2--5 remain withheld for later work.
REASON: New essential comparison coverage justifies one bounded known-method specialization attempt, stopping at the first failed map. It does not prove or self-approve a repaired transfer or L128 (2)/(3).
LITERATURE_REASON: The changed dual-to-covariant mechanism lacked essential compatibility coverage at turn start; step 535 supplies that coverage and reuses unchanged flatness/local-sign sources. The repair itself remains unproved.
SCOPE: Unchanged L123/L126/L127 hypotheses, n, W, CM list, full tame units, split exponents one/two, N, P, M, original R_0 and I, complete invariant domains and maps; no rationality, finite-local-condition, nonvanishing or BSD premise.
COVERED_TARGET: Test a covariant replacement of L128 Step 1 on the original labeled ordinary tower, establishing relation transfer to N_0 or stopping at the first failed map.

The [source record](../source-notes/2026-10-28-l128-covariant-transfer-coverage.md)
gives versions, exact hypotheses, essential proof explanations,
specialization scope, duplicate/failure comparisons and access limits.
Milne supplies covariant comparison for abelian homomorphisms; the
period paper supplies correspondence push-pull compatibility, with
empty marking/puncture sets for ordinary Jacobians. Fornea supplies
the two original tower laws separately. The next proof must verify
these applications to every labeled operator and the ordinary summand.
It must retain the source's right-module convention and specify product
order; no opposite-action identification is imported.

The COVERED_TARGET is the exact proposed next mathematical action;
newly written coverage remains subject to separate next-turn approval
by the supervisor. Success means a full relation-transfer argument
on N_0 with original labels; failure means a first precise obstruction,
not a disproof of L128's scalar identity. L128 stays on HOLD, and
its completed-branch comparison and signs are not certified by this
review. Rationality, nonvanishing and local finiteness remain separate.
No reproof of the standard source theorems is needed, and no
originality or Mathlib absence claim is made. Mathlib is not checked.
