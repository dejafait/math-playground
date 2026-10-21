# Ready residue-degree specialization — separate next-turn approval

TARGET: Factor L016's four trace polynomials modulo 7 and prove the resulting necessary condition on each L024 coefficient-prime residue degree, retaining both embeddings and the exceptional-algebra hypothesis.
CHECKED: 2026-10-06
DECISION: SPECIALIZE
SEARCH_EVIDENCE: The exact statement and stronger finite-field root-degree criteria were screened in 2026-10-05-mixed-seventh-residue-degree-test.md; that assessment records the searches, local overlap and failed-route comparison.
SOURCE_EVIDENCE: Conrad, Finite Fields, https://kconrad.math.uconn.edu/blurbs/galoistheory/finitefields.pdf, Theorems 2.8 and 3.3 with the relevant proofs (pp. 5–6), and Theorem 5.5 (p. 10); Milne, Algebraic Number Theory v3.08, https://www.jmilne.org/math/CourseNotes/ANT.pdf, residue-degree definition and Theorem 3.34 (printed pp. 59–60); reuse L020/L024's trace interface and PVT arXiv:2512.17845v1, https://arxiv.org/html/2512.17845v1#S7.SS2, Theorem 7.8 through the ready direct-import assessment.
COMPARISON: Known results cover the general field-degree mechanism; exact four-polynomial arithmetic and its coefficient-prime application remain unperformed. Any useful result is a specialization of those sources, not a claim of originality.
GAP: Determine all four factorizations and the precise necessary condition; no coefficient-prime splitting list, ambient spectrum, or exhaustion is available.
REASON: This is independently testable with the canonical trace data and ready literature, without accessing blocked matrices or archives. Separate approval precedes the calculation.
SCOPE: Use REPRODUCTION; import the general finite-field result by citation and prove only the finite arithmetic and applicability. Do not compute ambient spectra, remove the algebra hypothesis or assert a signature exclusion.

Primary citations and inspection details are in [the completed review](2026-10-05-mixed-seventh-residue-degree-test.md). No additional browsing is needed while the target and hypotheses stay within this scope.

Essential input IDs: L016, L020 and L024; L018 supplies the parameter restriction through L020. Preserve signed nonzero primitive X^5+Y^3=Z^7, the exact Q-algebra isomorphism in L020/L024, q=(29,sqrt(5)-11), both geometric coefficient embeddings and each separately obtained form, prime lambda above 7, and embedding j. Let d_lambda=[O_(K_f)/lambda:F_7]; do not replace it by [K_f:Q], a base-field degree, or a presumed equality of residue fields. Retain the existing unramified Hecke-trace normalization away from the level and 7. Check every possible polynomial, not just one parameter.

Continue if the result gives a justified prefilter on possible irreducible inputs, distinguishing a necessary condition from actual elimination of known forms. Explicitly compare its scope with L017/L020's reducible exclusion. If no discriminating condition exists, record that negative result. Even success leaves coefficient-prime splitting data, forms satisfying the condition, global algebra applicability and all other residual signatures unresolved. A full factorization and proof may be written by hand; no mathematical script is required for four quadratics.

Mathlib: full condition and supporting declarations not checked. This prepared assessment is not a proof and contains no computed factorization or new residue-degree conclusion.

## 2026-10-06 — Direct-source URL recovery

The single-line SOURCE_EVIDENCE now includes the direct primary URLs rather than relying on the linked completed review. Both PDFs were accessible today; the indexed text confirms Conrad's Theorem 3.3 and Milne's Theorem 3.34. Reuse the full theorem/proof inspection, searches, applicability comparison and duplicate/failure checks recorded in the completed review; no broader search or new theorem comparison was needed. Milne's printed pp. 59–60 are PDF pages 61–62 (one-based), so the page conventions differ. PVT's applicability is reused, not newly audited here.

This repairs a process defect only: SPECIALIZE, the exact target, hypotheses, input IDs, comparison, and continuation/abandonment test are unchanged. No polynomial was factored, no new result was derived, and no source beyond the earlier assessment was claimed to supply packet exhaustion. The next mathematical attempt must cite the imported general field theorem and establish only the finite arithmetic and the already assessed applicability difference; it need not reprove the general theorem. Mathlib coverage remains not checked. Separate next-turn approval precedes that attempt.
