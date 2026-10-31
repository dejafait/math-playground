# Full raw cusp coefficient envelope — prepared application audit

TARGET: Audit L548's raw cubic-theta coefficient bound (3) on all three cusp supports, including shared n,b primes, primes in S and every ramified exponent.
CHECKED: 2026-10-31
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the completed full-cusp source comparison and targeted duplicate/failure searches in drafts/literature/2026-10-31-family003-full-cusp-coefficient-bound-review.md; no new theorem search is needed for this exact application domain.
SOURCE_EVIDENCE: DR arXiv:2109.07463v3 https://arxiv.org/html/2109.07463v3 (5.7)–(5.16), Appendix A rows 1,19,10 and Section 2 (2.1)–(2.3); pinned OpenAI TeX https://raw.githubusercontent.com/openai/math/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex lines 1806–1854; reused finite-ring gaussSum_mulShift_eq coverage at https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/NumberTheory/GaussSum.lean#L54. Complete inspected-case map and qualifications: drafts/audits/2026-10-31-family003-full-cusp-coefficient-source-notes.md.
COMPARISON: Known source formulas and all-primary cubic norms supply the inputs and the manuscript already claims the exact envelope. The local task is verification of the specialization to L547 (9)/L548 (3), preserving the raw support and fixed numerical constant; it is reproduction rather than new mathematics. Directly importing the final claim would bypass the retained-premise audit.
GAP: The application remains unperformed: check conjugate unit/sign cases, h-to-k conversions, all ramified/zero cases, modulus 1, cubic shifts at S-primes and shared n,b factors against 27*3^(k/6)*|b|. Other finite inputs, source-proof audits, uniform closure and actual-Xi positivity remain independent.
REASON: The preceding literature-only turn completed the wider-domain comparison; this recovery turn supplies directly accessible primary URLs required by the supervisor gate, without changing the target or coverage decision. The later proof should import theta/norm theorems precisely and justify only their specialization, without redoing Patterson or Hasse.
SCOPE: Exactly L548 (3), the three coefficient functions identified in audited L547 (9), primary nonzero n,b with n ideal-squarefree, k>=-4, no S-mask and all otherwise-zero cases. Use ordinary cubic symbols for the raw domain, including primes above 2; do not extend good sextic definitions. No new analytic, arithmetic-uniform, global-energy or Xi-sign claim.

The [source comparison](2026-10-31-family003-full-cusp-coefficient-bound-review.md)
and [detailed source notes](../audits/2026-10-31-family003-full-cusp-coefficient-source-notes.md)
record exact citations, the full relevant domain, prior-scope boundaries
and Mathlib qualifications. No cross-notebook result is required.

Continue only if every retained coefficient case meets the exact
envelope. A larger necessary constant, nonunit shift or missing case
prevents discharge and must be preserved as evidence. Treat source
formulas as imports and put any completed application in canonical
L548; avoid a duplicate of L547's already recorded coefficient identities.
No application verdict is supplied by this prepared assessment.

## Direct-source recovery, 2026-10-31

Verified access through the web tool to the
[DR v3 primary text](https://arxiv.org/html/2109.07463v3),
[commit-pinned manuscript TeX](https://raw.githubusercontent.com/openai/math/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex),
and [Mathlib supporting theorem](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/NumberTheory/GaussSum.lean#L54).
The retrieved DR (5.7)–(5.8) locator and the finite-ring unit-shift
theorem agree with the prior source record; no wider theorem search,
new case derivation or coefficient-bound verdict is claimed. Reuse the
complete earlier case map and its source-proof qualifications. The only
change is repair of missing direct URLs in this ready assessment.
The unchanged application target remains SPECIALIZE; proceed to its
mathematical audit after the supervisor validates this repair.
