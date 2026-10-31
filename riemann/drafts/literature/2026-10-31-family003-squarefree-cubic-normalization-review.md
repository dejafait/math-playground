# Squarefree-composite cubic normalization — source comparison

TARGET: Audit L548's squarefree-composite cubic Gauss normalization and unit modulus, retaining all good-prime factors and the zero extension.
CHECKED: 2026-10-31
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Queried cubic Gauss sums twisted multiplicativity squarefree and Gauss sum gamma_2 Quasi-Riemann; searched the relevant L531–L558 finite-Gauss passages, family003 prime/reflection assessments and notes, corresponding histories and recorded failures. L556–L558 explicitly exclude composite propagation; no completed exact composite audit was found in that scope. Detailed retrieval and limits are in drafts/audits/2026-10-31-family003-squarefree-cubic-source-notes.md.
SOURCE_EVIDENCE: Read pinned OpenAI TeX commit 1581d4cbdd69a0faf34b2089614fe2a814316a6a definitions 519–591 and complete finite norm/conversion passage 1826–1871; Dunn–Radziwill arXiv:2109.07463v3 Section 1.2 (1.4)–(1.8) and full Section 2 (2.1)–(2.3), including primary and both residue-degree conventions; official Mathlib GaussSum.lean 54–76 including the complete finite-commutative-ring unit-shift proof and field restriction at 177–181.
COMPARISON: DR directly states the all-primary-modulus norm and a stronger cubic formula, so prime propagation is unnecessary. The pinned manuscript defines gamma_j(n) by a composite sum, gamma_j(1)=1 and chi_1=1; it already claims the exact conversion. Standard unit-shift scaling covers the remaining additive-character specialization. Any factorization must retain DR (2.3)'s conjugate cubic-symbol factor. This is known mathematics, not a novel Gauss identity.
GAP: Essential coverage is complete for a separate application audit: match the cubic symbol to chi_n^2 on all residue classes, check lambda is a unit and the additive characters and q_n normalization agree, preserve all nonunit zeros and primary units, and check n=1 explicitly. No application or L548 discharge is completed here; raw theta coefficients, remaining Gauss inputs, arithmetic uniformity and Xi signs stay open.
REASON: The changed prime-to-composite scope required this literature-only step. All-modulus DR statements and the finite-ring unit-shift theorem now cover the necessary inputs; importing them avoids an unnecessary reproof. The newly changed ready assessment requires separate gate approval before research.
SCOPE: Only L548's tilde-g_3(n)=chi_n(lambda)^(-2) gamma_2(n) and |gamma_2(n)|=1 for squarefree primary n coprime to S, including n=1 and both split and inert good-prime factors. Retain source definitions; exclude coefficient estimates, non-squarefree moduli, analytic/arithmetic uniformity and Xi signs.

The exact local interface remains L548 (4) and its following retained
paragraph, with L546's product symbols/zero extension and L556's prime
normalization as context. No cross-notebook input is proposed. The
complete source record, theorem statements, search qualifications and
Mathlib distinction are in
[the source notes](../audits/2026-10-31-family003-squarefree-cubic-source-notes.md).

Primary inputs are Dunn–Radziwill, *Bias in cubic Gauss sums: Patterson's
conjecture*, Annals of Mathematics 200 (2024), no. 3, 967–1057,
[arXiv:2109.07463v3, Section 2, (2.1)–(2.3)](https://arxiv.org/html/2109.07463v3#S2),
and the definitions/claimed application in the
[pinned OpenAI TeX](https://raw.githubusercontent.com/openai/math/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex).
DR's norm statement is for primary composite moduli, not solely prime
ones; its twisted product includes a phase. Its upstream Hasse 1950,
pp. 443–445, is cited but not independently inspected. No GRH-dependent
prime-average theorem is used. The pinned source explicitly defines
both empty-modulus values and restricts the sextic conversion to good
moduli; its wider cubic coefficient support is outside this target.

The inspected official
[Mathlib unit-shift theorem](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/NumberTheory/GaussSum.lean#L54)
works over a finite commutative ring with a unit shift; its proof is a
finite reindexing. Its finite-field norm theorem must not be applied
directly to the composite quotient. A full matching Eisenstein theorem
was not found in this file; global Mathlib availability is not checked.

Downstream use would remove the retained squarefree cubic normalization
and modulus premise in L548, while raw coefficients, remaining finite
inputs, uniform closure and signed-Xi transfer stay independent. The
test is exact phase/normalization agreement and a unit-modulus theorem
covering every permitted squarefree modulus, including the empty one.
Any missing hypothesis, extra primitivity restriction or unaccounted
CRT/unit factor prevents discharge. Keep this exact target for the
separate gate approval and later reproduction audit. The source
comparison supplies coverage only: no new lemma, composite derivation,
application approval or change to L548 was made in this turn.
