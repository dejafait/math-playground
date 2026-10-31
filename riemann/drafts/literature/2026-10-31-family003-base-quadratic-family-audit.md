# Base quadratic primary-family applicability audit

TARGET: Audit the Goldmakher–Louvel specialization giving L543 (1) for fixed S containing primes above 6, verifying primary-generator conductors, global finite-group reciprocity, same-class primitive products and transpose orientation, with the cited quadratic reciprocity formula retained as an input.
CHECKED: 2026-10-31
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the completed base-family source comparison and its scoped duplicate/failure searches; no matching completed independent audit was found and no originality is claimed.
SOURCE_EVIDENCE: https://raw.githubusercontent.com/openai/math/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex lines 519–588, 772–859, 860–927 and 2480–2517; https://arxiv.org/pdf/1112.1642v2 Definition 1/Theorem 1.1/Corollary 1.2 (PDF pp. 1–2), Section 2 (pp. 3–5) and Lemma 4.5/proof (pp. 8–9), inspected 2026-10-31.
COMPARISON: The pinned manuscript claims the full application; Goldmakher–Louvel proves the abstract bound but requires an actual Hecke family. Reproduce only the applicability argument; do not reprove the general large sieve or import its application without checking hypotheses.
GAP: The character-family identification and operator specialization remain unaudited. Essential source coverage is complete; the cited quadratic reciprocity formula and standard finite-field/CRT facts are retained inputs. Independent verification of its Gaussian proof remains outside scope.
REASON: A successful audit could replace L543's retained base-sieve assumption by the cited theorem under explicit arithmetic inputs, reducing L542/L541 contracts locally without supplying Xi signs.
SCOPE: Fixed source S and ray/presentation datum; squarefree good ideals, U,V>=1, arbitrary complex coefficients and zero conventions. Exclude wider/varying S, unrestricted nonsquarefree base indices, cubic primitive, reflection/global contracts, Xi positivity and cross-notebook inputs.

## Source gate and bounded audit

Use [the completed comparison](2026-10-31-family003-base-quadratic-family-scope.md)
for the exact citations and qualification of inspected proof cases. This
assessment is newly written and requires separate next-turn approval.

Input interface is L543 (1) and its source conventions. L543, L542 and
L541 are downstream uses, not proofs of the base sieve. Start with
Goldmakher–Louvel v2 Definition 1 and Theorem 1.1. Corollary 1.2 does not
establish that the raw sextic symbols are a sixth-order Hecke family.

Verify the primary adjustment on units and its lambda correction,
primitive conductor including the e(a)=0 and unit-ideal cases, trivial
infinite type, a global finite group and homomorphism, and primitive
products at coprime same-class indices. Do not treat an isolated fixed
class as the full family required in Definition 1. The cited quadratic
reciprocity formula is available through the pinned
`lem:quadratic-four-term`/`eq:reciprocity-four-class` and the quadratic
CRT identity in `lem:fixed-gauss-phase`; its source Gaussian proof was
inspected but is not independently audited by this continuation.

Match Q_a(b)=chi_a(b)^3 to primitive inducing-character values also when
a,b collide. Give the finite matrix transpose/adjoint argument, with
conjugation and arbitrary coefficient norms explicit; compare Lemma 4.5
without importing any dyadic cutoff not in the desired theorem.
Keep constants dependent on fixed S/modulus only, and make row/support
restrictions only after establishing the family bound.

Continue only on the exact (UV)^epsilon(U+V) bound with these inputs.
Narrow or stop on an unmatched conductor, missing global homomorphism,
uncancelled fixed-prime product factor, zero-value mismatch or additional
length loss. An honest obstruction is useful even if independent cubic,
reflection and all-degree positivity gaps remain. No numerical script is
needed. Mathlib coverage has not been checked.
