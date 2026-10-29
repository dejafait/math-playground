# L126 factorization and complete norm-moment equality — audit coverage

TARGET: Critically audit L126's local normalizer factorization and complete norm-moment replacement, including rational p-cell actions, CM multiplicities, projection domains and descent.
CHECKED: 2026-10-27
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused step-523 exact-target searches and its classical square-free comparison; checked L126 against L123/L124, their step-515/520 audits and ATTEMPTS/060. Step 525 retrieved the two versioned primary sources and compared the raw-cell, integration, quotient and projected-invariance scopes; no broad rediscovery search or novelty inference.
SOURCE_EVIDENCE: Voight, Quaternion Algebras (2021), Chapter 30 pp.541-567, Proposition 30.5.3(a),(b) with proof, (30.6.2), Lemmas 30.6.3/30.6.9 with proofs, https://doi.org/10.1007/978-3-030-56694-4_30; Fornea arXiv:2603.28327v2 (13 April 2026), (2), Section 2.0.1/(7), level definitions/Section 2.2, (22)-(23), Proposition 3.8 with proof/Corollary 3.9, (34)-(35), Corollary 4.15/(63), Proposition 4.18 and Theorem 4.22 with full proofs, (67)-(68)/Corollary 4.24 with proof, https://arxiv.org/html/2603.28327v2; prior L123/L124 domain/descent audits reused.
COMPARISON: The local sources cover maximal and prime-power Eichler orders, including residue characteristic two in the cited cases. Fornea supplies raw cells and complete integration, but Proposition 4.18 and Theorem 4.22 conclude after specialization; neither is an import of L126's raw norm-moment equality. That stronger equality, representative comparison and restricted adelic assembly remain local claims to audit.
GAP: Verify every local embedding case and adelic choice, L126 (5)-(8) before specialization, the original quotient multiplicities and discarded inert coordinates, then transfer the projection domain and unique descent using L123/L124. No missing essential source prevents this bounded audit.
REASON: Separate source-scope approval is complete. SPECIALIZE authorizes auditing the stated assembly and stronger raw comparison without reproving the imported construction; it does not certify L126, supply a scalar action or approve a different target.
SCOPE: Exactly the TARGET above under all written L123/L124/L126 hypotheses; no new scalar calculation, evaluated residual, rational Kummer membership, finite local condition, auxiliary-prime existence or BSD claim.
LITERATURE_REASON: The new audit target requires coverage of L126's stronger equality before Hecke specialization, beyond simply citing the ready projected construction; the supplied REVIEW_REQUIRED gate requires this separate approval turn.

Essential local inputs are L123 with its step-515 audit and L124 with
its step-520 audit. L125 and ATTEMPTS/060 are contrasts only. Preserve
all conductor, residual, incoherence, integral-embedding, trivial-character
and original-CM-list hypotheses. In particular the unit level must be
the entire tame Eichler unit group, Delta must consist of inert
unramified conductor primes, and p must remain inert unramified.

The already assessed primary sources are
[Voight, Chapter 30](https://link.springer.com/chapter/10.1007/978-3-030-56694-4_30)
and [Fornea v2](https://arxiv.org/html/2603.28327v2). The step-523
search/source record is reused. The separate step-525 comparison is in
[the audit source note](../source-notes/2026-10-27-l126-audit-coverage.md).
The audit must account for L126's use of the raw norm integral rather
than merely invoking Fornea's projected invariant function. Its claimed
exact point equality precedes the original j_m varphi_m maps and has
not been verified in this literature turn.

Acceptance means the fixed w really factors as stated and every
representative change gives the asserted integrated equality, with
the original index multiplicities and both projection domains. If a
step fails, identify the first unsupported equality and preserve the
preceding partial result. No scalar eigenvalue, evaluated R, rational
Kummer class, finite local membership or BSD conclusion is in scope.
Mathlib coverage remains not checked. This assessment was proposed with
REVIEW_REQUIRED in step 524 and separately approved for the unchanged
audit target in step 525. The next turn defaults to that mathematical
audit. No new lemma or mathematical script was written in the approval
turn, and the construction's pending audit status is unchanged.
