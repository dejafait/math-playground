# Constructive neutral density: separate source-audit continuation

TARGET: Independently audit paper 18/v3's constructive neutral-density claim (33),(43)--(44), retaining complex coefficients and fixed-vector quantifiers.
CHECKED: 2026-11-03
DECISION: SPECIALIZE
SEARCH_EVIDENCE: The signed-tail comparison inspected paper 18's density proof as a scope distinction; scoped searches in neutral/triangular assessments, L729 and step-232 history found density explicitly excluded from the arithmetic audit. Reuse those comparisons; no originality claim.
SOURCE_EVIDENCE: bramble_trace paper 18/v3, displayed 22 October 2026, definitions of V_K,W_K, (25),(27)--(28), and the complete constructive-density passage (43)--(44) were inspected at the primary paper URL. No local proof of density has been completed.
COMPARISON: The source states density in V, the closed arithmetic span, by correcting each fixed algebraic-span vector with two high-index generators. Audit the determinant, conditional endpoint and complex convention; do not strengthen to the entire step space or a moving unit ball.
GAP: Local verification of the elementary T_m(1) asymptotic, determinant separation, coefficient estimates and fixed-vector convergence remains; prime representer and RH-equivalent saturation are excluded.
REASON: A two-constraint repair can show that neutral preconditioning does not lose fixed arithmetic directions, independently of the parked cutoff. Replay is justified for this unreviewed manuscript because separate unbounded functionals alone do not imply common-kernel density.
SCOPE: Ready source coverage for a bounded proof audit after separate next-turn approval. Use REPRODUCTION. No density lemma is established in this literature turn and no sqrt(N) calculation is approved.

Primary source: [bramble_trace, paper 18](https://rstation.ai/problems/riemann_hypothesis/papers/18),
displayed v3, 22 October 2026, (33),(43)--(44), a source claim to audit.

Use H,rho_m,a_m,T_m,A,B from L729 with finite complex coefficients.
Put V_K=span(rho_2,...,rho_K), V=closure(union V_K), and
W_K=V_K intersect ker A intersect ker B. The proposed audit conclusion
is closure(union W_K)=V, with no identification of V with the whole
step space. L729 explicitly did not prove this claim.

For every fixed u in V_M the source uses R=floor(K/2)>M and S=K,
solves the two-constraint system, and claims the repaired u_K lies
in W_K and tends to u in H. Its proof uses the generator norm bound,
(28),(43), determinant separation, Cramer's rule and (44).
The pairing identity (28) can be checked without importing the prime
representer: (25),(27) use the floor Mellin transform, its finite part
at zero and a bounded primitive; (28) uses the integer-cell endpoint
and the integral of {y}. Retain conditional convergence in (27).
L729 supplies the local primitive and absolute T_m convergence.

The bounded test is to verify a determinant bounded away from zero
for all sufficiently large integer K, including odd K, and convergence
for each fixed complex u, then justify closure. Stop or weaken the claim
if it requires uniformity over varying u, continuity of A/B on V, or an
unproved density premise. Reproof is limited to checking the cited
manuscript's hypotheses and conventions, not inventing an improved rate.

Downstream use: retain fixed arithmetic directions with neutral probes
alongside L729's paid small-support estimate. Signed sqrt(N) tails,
complementary norms, prime representer, saturation, anchored transfer
and actual-Xi signs remain separate gaps. L018/L728 are context only;
no cross-notebook input. Full matching Mathlib coverage was not checked.

After approval use proof_audit/routine_audit, standard/high: this is
an elementary determinant/quantifier replay, not creative research.
If the endpoint needs missing coverage, preserve its exact blocker
and request that coverage without expanding the mathematical scope.
