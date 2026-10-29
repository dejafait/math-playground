# Step 488 — approved derived-height specialization

Completed attempt: the prior SPECIALIZE assessment is
[the approved target review](literature/2026-10-25-derived-height-defect-accounting.md).
The target is exactly its TARGET line. Existing unrelated working changes
are preserved. No mathematical script is needed for this finite-length proof.

The main gap is rational rank versus arbitrary complex analytic order at
least two. The bounded target is an exact, finite expression for L002's
delta using Howard's full compact Selmer filtration. Future arithmetic
bounds on these layers could bound delta; Sha corank and the analytic
comparison remain independent gaps. Continue if tower/module matching
and finite termination hold; stop any replacement by rational points or
any unproved nondegeneracy assertion.

L002, L003 and L019 were checked for overlap; the latter preserves the
failure of promoting a full-Selmer height radical to the Sha quotient.
The exact quantitative formula is not already stated in those files.
Howard arXiv:1202.6343v1, Section 3 setup/Propositions 3.4--3.5,
Section 4 equation (9), Lemma 4.1, Theorem 4.2 and Corollary 4.3 were
retrieved at their load-bearing statements and proof ranges. This is
source retrieval for the already covered research target, not a fresh
literature search or an expanded mathematical target.

Proof plan: let V_j be Howard's j-th filtered compact Selmer space.
Its dimension is rank_Zp(T^(j-1)X/T^j X). Localize this quotient at
(T) to obtain T^(j-1)M/T^j M. L002's finite block decomposition then
counts blocks of length at least j, so the finite sum for j >= 2 should
count sum_i(e_i-1) = delta. Check the zero module, the absence of a
free part, and localization of all error terms explicitly.

Completed: [L118](../lemmas/L118-derived-height-augmentation-defect-accounting.md)
proves the finite accounting, including tower hypotheses, compact/discrete
matching, finite/pseudo-null errors, the missing free contribution and
the zero module. Its conclusion is a known-theorem specialization,
classified REPRODUCTION. No arithmetic vanishing or rank comparison
was obtained. The [step-488 decision](../history/488-2026-10-25-derived-height-defect-accounting.md)
records the continuation; this draft is not a second canonical proof.
