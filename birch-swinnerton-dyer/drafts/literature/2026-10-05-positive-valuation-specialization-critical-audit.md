# Source approval for the critical audit of the fixed-depth specialization

TARGET: Critically audit L023's fixed-depth two-prime valuation-h witness under L021's hypotheses for every m > h, checking coefficient identification, eligible prime selection, both dual localizations, strict/transverse equality and actual Sakamoto scalar normalization.
CHECKED: 2026-10-05
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused drafts/literature/2026-10-05-positive-valuation-restricted-index.md, L021/L023 and ATTEMPTS/021; retrieved the primary finite-coefficient selection, strict/transverse comparison, first-degree proof and actual basis scalar cases on 2026-10-05; no expanded discovery search.
SOURCE_EVIDENCE: The prior assessment covers Angurel arXiv:2504.20759v2 Corollary 2.30/Lemma 2.31/Theorem 3.27 first-degree proof, Mazur--Rubin Proposition 3.6.1 and Lemma 4.1.7(ii), Kim Section 5.3.1, and Sakamoto Definitions 2.3/2.4, Corollaries 2.14/2.15, Section 2.3, Theorem 2.20(2), Proposition 3.19 and Lemma 4.2; exact versions, theorem/page numbers and direct URLs are retained in the original assessment and L023.
COMPARISON: The proposed audit concerns exactly the same first-degree specialization and hypotheses as the approved attempt; it imports no new higher-ideal equality or normalized-family comparison.
GAP: Independently check the written applicability argument in L023; its restricted witness has been written but has not received this later critical audit, and rational membership and complex comparison remain unresolved.
REASON: Separate literature approval is complete for this unchanged audit target; essential source coverage is ready, and the next turn is mathematics. This report does not perform or certify the critical proof audit.
SCOPE: Same L021 hypotheses; F = S/S_div, h = length_Z_p F and every m > h. Audit only the fixed-depth witness in L023, not a rational certificate or the BSD main gap.
COVERED_TARGET: Critically audit L023's fixed-depth two-prime valuation-h witness under L021's hypotheses for every m > h, checking coefficient identification, eligible prime selection, both dual localizations, strict/transverse equality and actual Sakamoto scalar normalization.

## Coverage reused and audit test

The source versions and primary proof cases are those in
[the approved assessment](2026-10-05-positive-valuation-restricted-index.md).
This separate literature-only approval reuses that coverage; it is not an
independent correctness review of L023. The derivation just completed had ready coverage
before invocation. No new mathematical mechanism is authorized by this
continuation: its target is to check that derivation critically.

Primary cases already inspected, retained for the audit:

- [Angurel v2, 2026-06-08, Section 3.5](https://arxiv.org/html/2504.20759v2#S3.SS5): Theorem 3.27's first-degree proof and its Corollary 2.30/Lemma 2.31 inputs; no all-degree or non-self-dual claim.
- [Mazur--Rubin, Proposition 3.6.1, printed pp. 30--31](https://webusers.imj-prg.fr/~christophe.cornut/ES/Ref/KolySys.pdf#page=36), and [Lemma 4.1.7(ii), printed p. 37](https://webusers.imj-prg.fr/~christophe.cornut/ES/Ref/KolySys.pdf#page=43): finite coefficients and the p>4 proof case.
- [Sakamoto 2022, Theorem 2.20(2), p. 1904](https://ems.press/content/serial-article-files/29299?nt=1#page=14), and [Proposition 3.19 and proof, pp. 1915--1916](https://ems.press/content/serial-article-files/29299?nt=1#page=25): the scalar identity for the constructed basis, not a comparison to another family.
- [Kim, author text 2025-05-12, Section 5.3.1, printed p. 27](https://preprint.press.jhu.edu/ajm/sites/default/files/AJM-kim.pdf#page=28): natural classical coefficient identification. Its finite-Sha rational-rank clauses are not imported.

Essential input: L021. L022 remains only a normalization comparison.
Read L023 and only the primary cases needed to verify its application.
Check that the finite coefficient group is R_m^2 direct sum F, that
order-p^m classes remain detected in the rank-one finite local groups,
and that the selected primes meet the cyclic torsion condition of
P_(m,0). Check self-duality after transverse modification before invoking
the strict/transverse comparison at each of the two selections. Finally
check the module kernel, length h, the tensor G_N trivialization, and
the scalar identity for the actual primitive Sakamoto family.

Continue only if all these checks hold for every integer m > h, including
h=0 and m=h+1. Record any failed hypothesis or implication and preserve
the written work; an audit failure must not be hidden by granting a
stronger depth or an unknown scalar factor. No same pair of primes at
all depths is asserted. The possible finite-index construction after
inverting p is downstream motivation, not a conclusion or part of this
audit. Finite Sha, rational membership, complex equality and higher
analytic ranks remain unproved. Mathlib coverage remains not checked.

## Separate approval record — 2026-10-05

LITERATURE_REASON: The supervisor requires separate approval of the newly saved audit continuation; the scope is unchanged and existing coverage is reused.

Retrieved the linked primary texts, rather than relying on snippets. In
Mazur--Rubin, inspected Proposition 3.6.1 and its p>4 proof case, printed
pp. 30--31, Lemma 3.5.3 and its induced-local-condition proof, pp. 28--29,
Lemma 3.5.6, pp. 29--30, and Lemma 4.1.7(ii) and its proof, p. 37.
The first proposition requires principal artinian coefficients and
(H.0)--(H.5). Its p>4 branch does not use residual non-self-duality;
Proposition 3.6.2(ii), which requires (H.4a), is not the input proposed
for this audit. Lemma 4.1.7(ii) concludes equality on the dual side;
self-duality must be checked in the application, not inferred from
notation. The linked scan places printed pp. 30--31 at PDF pages
36--37 (one-based), and printed p. 37 at PDF page 43.

Read Angurel v2 Corollary 2.30, Lemma 2.31 and Theorem 3.27's
first-degree proof case, through the two displayed simultaneous
localizations and strict/transverse equality. This is the same scope
as the prior comparison. Reuse its recorded H1--H8 checks and caution
about Definition 2.18; no general higher-degree equality is imported.

Read Sakamoto Theorem 2.20(2), p. 1904, Proposition 3.19 and its
proof, pp. 1915--1916, and Lemma 4.2 and its proof, p. 1917. The
proposition explicitly equates basis status at some coefficient level,
basis status at every level, and nonzero residual system scalar. The
Fitting identity concerns a basis of his own system. Lemma 4.2 gives
residual nonvanishing equivalence, not a comparison of positive
valuations between unrelated families. Reuse the earlier inspected
Definitions 2.3/2.4, Corollaries 2.14/2.15 and Section 2.3 for the
local structures and prime set.

Read Kim Section 5.3.1, printed p. 27, including its explicit classical
coefficient identification and citation to Mazur--Rubin Lemma 3.5.3.
Its placement in a corank-zero argument does not license importing
that argument's rank or finiteness conclusions into L023. The audit
must still check the induced local conditions used for the identification.

Decision: SPECIALIZE is ready for the exact TARGET above. No essential
source is blocked; no new lemma, script, derivation or proof audit was
performed. L023 remains unaudited. The finite-module kernel, the two
applications after local-condition modification, depth-m cyclic
eligibility and tensor scalar trivialization are application checks
for the next research turn. Stop or qualify L023 if any check fails;
do not substitute stronger hypotheses silently. ATTEMPTS/021 and
L021's finite-defect obstruction remain in force. Matching Mathlib
coverage remains not checked.
