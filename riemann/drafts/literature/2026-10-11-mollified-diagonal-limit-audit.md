# Proposed critical audit of the fixed-head zero limit

TARGET: Critically audit L397's zero-limit bound for L396's fixed-N mollified arithmetic diagonal, including every exceptional-prime factor, both cutoffs, full Mellin tails and normalized shift derivatives.
CHECKED: 2026-10-11
DECISION: EXPLORE
SEARCH_EVIDENCE: Step 69 reused the exact-limit assessment and its local duplicate/failure comparison; queried Titchmarsh "3.11.8" zeta log t pdf and Titchmarsh theory Riemann zeta function 1986 pdf theorem 3.11; retrieved the explicit reciprocal-bound proof case in Baluyot–Gonek (2019), p. 53.
SOURCE_EVIDENCE: Reinspected Young, Arch. Math. 95 (2010), Lemma 7 and proof, pp. 545–547; newly read Baluyot–Gonek, Pacific J. Math. 303 (2019), Section 2, p. 53, explicit bound citing Titchmarsh (3.11.8). Direct book retrieval remains unavailable; no book-page inspection is claimed.
COMPARISON: The claimed zero limit uses its own same-height squarefree factors and a full integral bound; Young's opposite-height coefficient and BCY's different cross-mollifier evaluation remain inapplicable as coefficient substitutions.
GAP: Independently approve coverage and then audit the collision normalization, exceptional-prime factors, reciprocal-zeta hypotheses, Perron interchange, full tails and Cauchy losses without assuming L397 correct.
REASON: Separate step 69 resolves exact-domain source uncertainty and approves the unchanged critical-audit scope; source coverage is ready, but mathematical correctness of L397 is not preapproved.

Essential inputs are L396 (1)–(2) and the new L397 proof. Preserve fixed N,
Y=H^(1/100), P(u)=u^2, both q_H weights and all ordered collisions.
L395 is needed only through L396's already audited physical reduction;
it supplies no arithmetic limit. The audit must compare the actual
unexceptional local factor 1+X-U-V and exceptional factor (7) against
all allowed squarefree exponent pairs. No division by a potentially
zero local factor is permitted.

Check that the two reciprocal-zeta arguments involve the same Mellin
variable s, that the shift bidisk stays in Re>1, and that the standard
unconditional bound has exactly the needed uniformity. Direct extraction
of the underlying Titchmarsh pages was unsuccessful in step 68; the
already covered input is explicitly used in the inspected Young proof.
Resolve any genuine hypothesis uncertainty before approving an audit.
Check the product upper bound, the coupled numerator at all heights,
both degree-two Perron cutoffs including equality, full Fubini majorant,
infinite tails, and every normalized derivative term.

Pass only if the unchanged hypotheses give O_N(log log H/log H)=o(1).
If an estimate fails, identify and repair only the relevant gap or retain
the result as unverified. No growing-N, balanced-coefficient, full signed
mean, global positivity or RH assertion is part of this audit. Matching
Mathlib coverage remains not checked. The original step 68 proposal did not approve itself or claim novelty;
step 69 supplies the separate source gate review below.


## Separate gate comparison — step 69

LITERATURE_REASON: The proposed audit specifically required resolving the
essential unread reciprocal-bound domain and uniformity, beyond the prior
coefficient comparison. This is not repeated carrier-source approval.

Reused `2026-10-11-mollified-carrier-diagonal-limit.md`, L396 (1)–(2),
and L397 as the claim to audit. Read the step 67–68 histories, attempt 68,
and the repeated-carrier-approval stop. The latter parks repeated approval
of the unevaluated carrier reduction, not this new zero-limit audit.
Young and BCY remain technique inputs, not matching coefficient theorems;
no new duplicate search or originality claim is needed for unchanged scope.

The inspected [Young published proof](https://www.math.ntnu.no/emner/MA3001/2020v/2022v_MA3004/Young.pdf#page=8)
explicitly invokes Titchmarsh Theorem 3.8 and (3.11.8) in Lemma 7.
Its opposite-height coefficient is still not imported. Its small-complex-
shift Cauchy argument on p. 541 is reusable technique, not verification
of L397's derivative losses.

The new inspected source is S. Baluyot and S. M. Gonek,
*Explicit formulae and discrepancy estimates for a-points of the Riemann
zeta-function*, Pacific J. Math. 303 (2019), 47–72,
[Section 2, p. 53, before (2-3)](https://msp.org/pjm/2019/303-1/pjm-v303-n1-p02-p.pdf#page=9),
DOI 10.2140/pjm.2019.303.47. It states, citing Titchmarsh (3.11.8),
|zeta(sigma+it)| >= c/log t for sufficiently large positive t and
sigma >= 1-A/log t, with fixed positive constants. In particular it
explicitly includes sigma >= 1. This is a statement about ordinary zeta,
not zeta-a, despite the paper's surrounding a-point application. Complex
conjugation covers negative heights. Restricting this known bound to
1<=sigma<=2 gives L397 (3), with uniform constants. No reproof or stronger
zero-free region is required. The small-height Laurent/compact arguments
in L397 remain proof obligations for the mathematical audit.

The Rutgers book PDF timed out through web retrieval; shell retrieval
failed DNS. The inspected paper explicitly supplies the needed statement
and precise book trace, so book access is not an essential blocker for this
right-half-plane application. Do not claim the original book pages or its
proof were read. Search snippets and unrelated results are not premises.

SCOPE: Only the exact TARGET above with fixed N, L396 (1)–(2), exponent
1/100, degree-two p_H, both q_H weights and all ordered collisions.
The prior EXPLORE comparison covers the unchanged arithmetic difference;
this assessment adds the exact known-bound coverage for its audit.
No new mathematics was derived and no lemma or mathematical script changed.
Full matching Mathlib coverage remains not checked.

Approval permits a later critical audit, not acceptance of L397. Independently
check every squarefree exponent case, the exceptional-prime upper product
without reciprocating local zeros, both same-s reciprocal arguments, the
entire shift bidisk, Perron equality boundary and full Fubini majorant,
coupled numerator at opposite heights, both infinite tails and all nine
normalized derivative terms. Continue only if the claimed unchanged bound
O_N(log log H/log H)=o(1) survives. Identify a failed estimate and retain
unverified status if it does not. The balanced coefficient, complete signed
mean, growing-N passage and all global sign/count gaps remain open.
