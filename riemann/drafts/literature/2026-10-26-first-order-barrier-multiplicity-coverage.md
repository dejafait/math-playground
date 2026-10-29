# First-order height barrier — local multiplicity test nomination

TARGET: Test whether U'(a)+C(a)U(a)>=0 can hold on a two-sided neighborhood of every real Xi zero for U(a)=w(a)D_1(Xi;a), with w positive C^1 and C continuous, without restricting the zero multiplicity.
CHECKED: 2026-10-26
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the completed height-differential review's Laguerre/ODE/comparison searches and additional Gronwall/multiple-zero and first-order-expression queries; targeted drafts/literature and ATTEMPTS searches found no matching recorded scalar-barrier test. No novelty is inferred.
SOURCE_EVIDENCE: D'Agostino–Eberl, SIAM Review 67(2) (2025), Section 2.3 Theorem 1 and complete proof, pp. 381–382, https://epubs.siam.org/doi/epdf/10.1137/23M1616406; L018 actual real entire Xi and L466's canonical source/multiplicity passages, including its citation of Sra v1 Theorem 1.3 proof p. 11; Csordas–Escassut (2005) Theorem 2.1 p. 333 is an equality-case comparison, not an assumption that Xi is Laguerre-Polya.
COMPARISON: The scalar theorem covers specified differentiable sub/supersolutions, a locally Lipschitz right side and initial order on a finite interval. Analytic local factorization at a zero is standard and explicitly used in L466. Neither source states this weighted local compatibility classification; only that application is proposed, without proving a global Xi inequality.
GAP: Determine the exact local behavior of U and the proposed differential defect for every integer multiplicity m>=1. No compatibility verdict, simplicity result, actual multiple zero or actual-Xi source bound is established in this nomination.
REASON: Prepare one independently testable implementation check before sign propagation. This is routine specialization of known comparison and analytic-factorization tools, not a new central-sign mechanism; the newly written assessment requires separate supervisor approval next turn.
SCOPE: A hypothetical real Xi zero a_0 of arbitrary finite multiplicity m>=1; Xi(a)=(a-a_0)^m g(a) locally with g real analytic and g(a_0)!=0; w>0 of class C^1 and real continuous C on an open neighborhood containing both sides of a_0. No simplicity, nonzero-center division, global Laguerre sign, real-zero location premise or external half-plane theorem.
LITERATURE_REASON: This exact local test was nominated during the completed source-only height-mechanism review. Separate approval is needed for this new mathematical action; no repeated external discovery is requested.

## Relevance and bounded test

The main gap is initial actual-Xi signs at unbounded heights and global
mixed positivity. This test examines the simplest scalar comparison
implementation. Its plausible downstream use is to decide whether the
barrier can preserve all central multiplicities allowed by the notebook
before seeking an actual-Xi defect bound. It cannot establish the first
sign or any higher sign.

The inequality is a proposed test condition, not a theorem imported or
proved here. The later calculation should insert local factorization,
justify leading terms and remainders at the stated regularity of w,
and check both sides of a_0 for every m. Do not choose C by division
through U at its zeros. Compare the exact defect with zero rather than
use plots or samples.

Continue this implementation only if the test admits all m without
singular C or vanishing/singular w. If an allowed m is incompatible,
stop claiming multiplicity-uniform coverage for this first-order class.
A conditional obstruction would not establish an actual multiple Xi
zero or rule out other differential approaches. If all m pass, a proved
actual-Xi defect bound and usable boundary data would still be needed.

## Source applicability and remaining assumptions

Use Section 2.3 Theorem 1 of the scalar comparison source with its full
domain, differentiability, initial ordering and defect-ordering
hypotheses. Its proof uses a local Lipschitz bound and an integrating
factor. A continuous linear coefficient is a narrower prospective
setting, not permission to drop hypotheses. No infinite-dimensional
comparison or boundary theorem at infinity is imported.

Reuse [the completed primary comparison](2026-10-26-first-sign-height-differential-coverage.md)
for citations and inspection details. L018 supplies the actual function;
L466 records local zero factorization and a sign theorem that does not
require simplicity. This local test does not infer exterior signs from
L466's finite-height interval. L468 and its external premise are
motivation only. L251 and L354 remain failure comparisons.

No lemma or mathematical script has been written for this target.
Record a conditional local obstruction as such; do not infer RH, an
off-line zero or a simplicity theorem. No reproof of scalar comparison
is needed. Mathlib matching/supporting coverage is unchecked; no
absence claim is made.
