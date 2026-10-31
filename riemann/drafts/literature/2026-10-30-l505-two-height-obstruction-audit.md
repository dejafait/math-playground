# L505 common-witness obstruction: critical-audit coverage

TARGET: Audit L505's common-witness obstruction for all nonnegative two-height multipliers, including kernel applicability, endpoint signs, smooth Fourier support and the uniform onset.
CHECKED: 2026-10-30
DECISION: EXPLORE
SEARCH_EVIDENCE: Reuse the separately approved 2026-10-30-l504-two-height-positive-multiplier-test.md and its parent positive-class review; the audit retains exactly their family, hypotheses and elementary techniques. No fresh discovery search or novelty claim.
SOURCE_EVIDENCE: L504's audited full proof was read this turn. Reuse the approved primary comparisons: Brevig et al. https://arxiv.org/pdf/2210.13922v2 Theorem 3.10, pp. 14--15; Goberna--Volle https://arxiv.org/pdf/2106.14573v1 Propositions 3.1/3.2 and Remark 3.1, pp. 7--9; ABR https://axler.net/HFT.pdf#page=124 Theorem 6.13(a)/Corollary 6.15, pp. 119--120. The separate approval below rechecked the primary statements and relevant proof cases; no source theorem is imported as implying L505.
COMPARISON: The primary sources do not supply this uniform obstruction or a constrained duality equivalence. L505 adds a common smooth witness to the exact previously assessed family; its proof uses only L504 and elementary monotone sine integration. Replaying that proof needs no new theorem import or changed source hypothesis.
GAP: Independently check the new proof's continuum and endpoint treatment, the odd-half-period sign, and the simultaneous margins that cover arbitrarily growing coefficients at every large real T.
REASON: The common-witness argument still needs independent critical review; the separate literature-only approval below confirms adequate coverage for exactly that audit, with no essential unread premise.
SCOPE: Critical audit or repair of L505 only. No strengthening, general measure optimization, positive-class counterexample, L503 conclusion, detector cost or actual-Xi transfer.

## Retained hypotheses and evidence to inspect

Read L505 in full and the load-bearing parts of L504. Fix R>0 and
retain L=log T, a=log L/pi, b=a/4, B=L/(4pi), lambda=pi/(2a), V_R,
K(0)=0, M, Q_a, E_a and normalization 1 on H_a. Heights are exactly
b and 2b; alpha,beta are any nonnegative finite real numbers and may
vary with a. There is no Fourier-derivative bound or sign in the gap.

Verify the rescaled Fourier normalization and integrable b-endpoint
singularity; 2b<B and continuity at b; the monotonicity formula;
the clipped sine integral and count 4n+3 of half-periods; positivity
of the a-independent constants m_1,m_2; the envelope's Fourier support;
all three simultaneous sign margins and the common onset. The claimed
threshold is c_R L^(R/4)/a^2, versus required O_R(a), for every large
real T. Check that no step assumes bounded coefficients, infimum
attainment, M comparable to N, or membership of the witnesses in H_a.

An audit pass certifies only the stated two-scalar full-space
obstruction. A failure requires an explicit repair or narrowing;
do not infer positive-class failure from a sign-indefinite witness.
The sources' qualifications and prior L504 failure remain unchanged.
Matching Mathlib coverage is unchecked. The original nomination prepared a separate approval; the completed source
approval below is not the mathematical audit.


## Separate literature approval, 2026-10-30

LITERATURE_REASON: The supervisor requires separate approval of this newly saved audit assessment; confirm its unchanged source scope without repeating discovery or performing the mathematical audit.

Read L505 in full for scope, L504 through its kernel identities and
integrability argument, the L504 independent-audit record, both parent
assessments, and the two-height failure/history records. No duplicate
mathematical attempt is authorized. Reuse the recorded exact-class searches;
no fresh search or novelty claim is necessary for replaying this proof.

Reopened the direct primary PDFs listed in SOURCE_EVIDENCE:

- Brevig et al., arXiv:2210.13922v2 (1 November 2022), printed pp. 14--15:
  angular Fourier convention, Corollary 3.9, the endpoint warning and
  Theorem 3.10 with its full short proof. The latter assumes 1<=p<infinity
  and a PW^p function normalized at zero. Its p=1 residual can be an
  unbounded functional. Reproduction, Holder and density concern origin
  evaluation; this does not give a weighted two-height certificate.
- Goberna--Volle, arXiv:2106.14573v1 (28 June 2021), printed pp. 7--9:
  Propositions 3.1/3.2, their proofs, the revisited example and Remark 3.1.
  Proposition 3.1 has the stated extended-value qualification; Proposition
  3.2 requires one objective-domain point with a uniform strictly negative
  constraint margin. The attained scalar sup-dual differs from conic
  finite-support multipliers. The finite-index minimax case cannot supply
  an unverified continuum representation or quantitative estimate here.
- Axler--Bourdon--Ramey, second edition, PDF dated 17 July 2020,
  printed pp. 119--120: Theorem 6.13(a) and its bounded-measure weak-star
  proof, and Corollary 6.15 including its proof. Positive representation
  assumes positivity throughout the ball, using constant spherical L1
  mass. It cannot cross the present signed gap without another argument.

These confirm the existing limitations, with no changed theorem input.
L505 proposes only elementary scaling, integration, a monotone sine test
and smooth Fourier localization on top of L504. No strong duality,
optimizer, constrained counterexample, or L503 conclusion is needed for
its audit. Its claim and proof have been read to identify the scope,
not independently replayed or certified this turn. All displayed algebra,
endpoint interchanges, signs and common-onset inequalities remain audit
obligations. Mathlib coverage remains unchecked.

DECISION EXPLORE is approved for the exact TARGET and SCOPE. The next
turn may audit or repair L505 within that scope. This approval adds no
mathematical evidence: STEP_OUTCOME is STALLED, not ADVANCE or NEGATIVE.
The earlier negative result remains pending independent audit, and both
H_a estimates and actual-Xi transfer remain unresolved. No lemma,
mathematical script, PROOF or DAG was changed. A central creative target
still lacks a positivity-sensitive foothold; this essential audit is not
reclassified as creative to meet a scheduling preference.
