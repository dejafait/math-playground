# Ready continuation: coefficient-1 discrete Beurling diagnostic

TARGET: Specialize Broucke–Vindas Theorem 1.2 at b=3/4 to construct one discrete Beurling system with psi_P(x)=x-x^(3/4)+o(x^(3/4)) and R_P(x)log x+sum_(|g|<=x)Lambda_P(g)R_P(x/|g|)=O(x), where R_P=psi_P-x.
CHECKED: 2026-11-04
DECISION: SPECIALIZE
SEARCH_EVIDENCE: The completed self-consistent-generalized-prime source comparison inspected two primary construction chains and checked scoped duplicates and the fixed-kernel failure; exact queries and read limits are recorded there. No exact-target prior theorem or novelty claim was established.
SOURCE_EVIDENCE: Broucke–Vindas arXiv:2102.08478v2 Theorem 1.2 p. 2 and continuous construction proof pp. 4–6; Section 3 pp. 9–10 for same-system prime powers; Revesz arXiv:2202.01837v3 Section 1 (1)–(7), Section 7 (48)–(51), theta/psi conversion and Theorem 8 pp. 21–22 for comparison only. Full primary citations below and in the completed assessment.
COMPARISON: The known theorem provides discrete primes approximating an admissible continuous prime-counting template within 1. Our remaining difference is verifying a particular template, its coefficient-1 psi asymptotic, and the coarse convolution bound for its own Lambda_P. Revesz's reciprocal-zero coefficient cannot be substituted. Reproving discretization is unnecessary.
GAP: Admissibility, local finiteness, weighted counting error, finite prime-power cutoff/tail and same-system O(x) discrepancy control remain unproved here. No assertion about ordinary primes, integer density, meromorphic continuation through b, the L733 increment envelope, prefix energy or Xi signs is covered.
REASON: Essential source coverage is ready; a bounded reproduction specialization tests the missing self-consistency condition using the imported theorem and the partial-summation mechanism exemplified by L734, rather than reopening the exhausted fixed-kernel diagnostic.
SCOPE: One b=3/4 diagnostic only, allowing an unspecified asymptotic onset and constant; include every real x beyond onset and all atoms at equality. This newly written ready continuation requires separate approval next turn before mathematical execution.

## Imported theorem and proposed template

F. Broucke and J. Vindas, *A new generalized prime random approximation
procedure and some of its applications*, Math. Z. 307 (2024), Article 62;
[arXiv:2102.08478v2](https://arxiv.org/pdf/2102.08478v2), Theorem 1.2, p. 2.
It assumes F is nondecreasing, right-continuous, unbounded, F(1)=0 and
F(x)<<x/log x. For continuous F it provides strictly increasing real
primes p_j>1 tending to infinity and |pi_P(x)-F(x)|<=1 for every x>=1.
It also supplies the simultaneous Fourier estimate (1.3), which need
not be used for this diagnostic. Its continuous construction case,
Section 2 pp. 4–6, was inspected. This theorem, rather than a new
probabilistic proof, is the source input.

The candidate template to test is

    F_*(x)=0                                      (1<=x<=2),
    F_*(x)=integral_2^x (1-(3/4)u^(-1/4))/log u du (x>2).

This is a proposed choice, not an already proved admissible construction.
The flat initial segment avoids a singular template at 1. The next
proof must verify each theorem hypothesis before application and then
handle weighted prime counts and prime powers for the resulting system.
No further template search is needed unless this concrete test fails.

## Exact arithmetic and bounded proof obligations

Use the free commutative semigroup on the prime indices, with the norm
map induced by p_j, retaining multiplicity when real norms coincide.
Define Lambda_P(g)=log p_j on the formal prime powers of generator j,
zero elsewhere, including the unit. This is the convention in
Sz. Gy. Revesz, [arXiv:2202.01837v3](https://arxiv.org/pdf/2202.01837v3),
Section 1 (1)–(7), pp. 1–3. Its Section 7 and Theorem 8 are comparisons,
not substitutes for the coefficient-1 target. Prove local finiteness of
the constructed semigroup rather than identify equal norms as one integer.

The mathematical attempt must justify conversion of bounded pi error
to the weighted theta error; account for the first prime p_1>1 and the
finite cutoff floor(log x/log p_1); prove that the accumulated higher
prime powers are o(x^(3/4)); and obtain one eventual bound for the
displayed discrepancy expression using this system's own psi and Lambda.
These are enumerated obligations, not new results established by this
literature assessment. L734 is a model for a partial-summation estimate,
not a generalized-prime theorem. Its exponent 9/10, ordinary kernel and
positive profile cannot simply be renamed. Any adaptation must be
written and justified, including signs and compact initial ranges.

Success would show only that this self-generated arithmetic category
still admits the tested power diagnostic. Stop if a necessary theorem
hypothesis, finite prime-power control or same-system bound fails;
preserve the precise failure. Do not add N_P(x)=ax+O(x^theta), a zeta
functional equation, continuation through b, full increment envelopes or
growing prefix estimates to the assumptions or conclusion.

The source comparison is
`drafts/literature/2026-11-04-self-consistent-generalized-prime-diagnostic.md`.
The earlier L733/L734 stop is diagnostic context, not an assumption
about this system. Actual-family norms, anchors, covariance, tails and
unconditional Xi mixed signs remain independent gaps. A later canonical
lemma must contain the full specialization and exact citations. Mathlib
coverage is unchecked, with availability unknown.

Recommended work after approval: proof_attempt/development. This is a
known-theorem specialization, not a new central creative mechanism.
