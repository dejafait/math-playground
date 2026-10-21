# Balanced fixed-head mathematical attempt — step 72 (unfinished)

Approved target: the exact TARGET in drafts/literature/2026-10-11-mollified-balanced-fixed-head-limit.md (prior SPECIALIZE).

Main gap: global actual-theta mixed positivity. Intermediate target: evaluate B_N at fixed N, with both balanced diagonals, ordinary jets and sharp endpoints. Downstream use: combine later with L397 and L395 to test a complete mollified signed mean; no such assembly is being performed in this step.

Inputs inspected: L390 definitions and physical polynomial, audited L395 weighted jets/physical-tail bounds, L396 ordinary reflected identity, L397 carrier conclusion. Historical L390 absolute-contour failure, L394 quadratic-weight obstruction and repeated-carrier approval stop remain intact. Existing changes have not been discarded.

Working calculation (not established): the finite-prime factor for a nontrivial reduced response ratio may vanish at zero Mellin variables/shifts because of local Mobius cancellation. If justified uniformly in the two-diagonal asymptotic, only r=s would survive at constant scale. The scalar normalized ordinary-Hardy jet coefficient must then be evaluated, including the reflected diagonal and derivative signs.

Continuation/abandonment test: seek complete normalized o(1) arithmetic, combined holomorphic shift and absolute endpoint errors. Stop this implementation if a retained error remains order one; no coefficient is claimed from a formal Euler-factor value alone. All global sign/count gaps and growing N remain unresolved. No RH, common-zero bound, phase independence or sign premise is used.

## Completion — step 72

The attempt establishes the fixed-N sharp limit in canonical L398, with normalized error O_N(1/log H). Every ordered response pair is retained; the modified arithmetic factor is 1 on the diagonal r=s and 0 otherwise at the origin, with a uniform Mellin remainder. The complete ordinary-jet combination is -10282/1125. Both functional-equation diagonals are combined holomorphically before derivatives; both endpoint losses are bounded absolutely by O(1/log H).

The exact degree-four rational algebra certificate is scripts/discriminant/mollified_balanced_coeff_certificate.json, reproduced by scripts/discriminant/mollified_balanced_coeff.py; it does not verify the analytic proof. This is local REPRODUCTION of known-source tools with a justified finite arithmetic specialization, not a novelty claim. No complete physical mean or infinite-response limit is derived in this step. L398 needs a separate critical audit, with new audit coverage marked REVIEW_REQUIRED.
