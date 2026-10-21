# Four-block small-residual diagnostic — source-ready proposal

TARGET: Test Kim–Toan Theorem 12 on every admissible orbit of L022's unchanged extension whose four complemented block weights sum to at most 10, using the fixed Proposition 22/25 recursive upper bound.
CHECKED: 2026-10-06
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched Kim Toan constant weight strengthened inequalities Theorem 1212.3467; scoped local searches found only an unread enhanced-constraint lead, with no prior Theorem 12 test or four-block coefficient certificate.
SOURCE_EVIDENCE: Direct primary source https://arxiv.org/pdf/1212.3467v1 (14 December 2012); inspected Kim–Toan arXiv:1212.3467v1 III.C.1 Theorem 12 (36) and its complete proof (37)–(39), printed pp. 9–10; appendix definition of multiply constant-weight T, Proposition 22(ii),(iii),(v),(vi), and Proposition 25 (99), printed pp. 18–19.
COMPARISON: Theorem 12 adds four-region packing coefficients to the ordinary scalar bound; it applies to the existing binary support model without changing the pair or triple assignment, but the exact four-block maxima are not supplied by the paper at these parameters.
GAP: Evaluate a fixed weaker source-supported inequality with an explicit recursive integer upper coefficient, verify all selected rows exactly, and determine pass or violation; neither the coefficients nor feasibility have been computed.
REASON: A bounded specialization tests a distinct necessary constraint after ordinary scalar nonexclusion; recursion is capped by the selected residual weight, with no unknown tables, variable tuning or individual PSD diagnostics.
SCOPE: Only the exact TARGET, n=1024,w=68,v=956,d=10, unchanged L022/L023 assignment, and the recursion specified below; no full-SDP optimization or unselected orbit conclusion.

The main gap is arbitrary-center safety at 68 agreements; the current
bracket remains 955<=t_star(m)<=957. Inputs are L022, L023's full scalar
supplement, L024 and foundations/04; retain L001/C001a/L021 and the
C012a/L019 threshold context. This is source coverage for a proposed
mathematical test; the separate literature approval was completed on
2026-10-06 in step rsld-2026-10-06-051-four-block-citation-recovery.

Use actual ordered orbits (i,j,t,s), the original t-s, and
h=i+j-t-s. Preserve the forbidden-first, repeated-second, product-third
assignment branches. Form block lengths (i,68-i,i,956-i) and weights
(t,j-t,s,j-s). Complement each block independently to weight
u_a=min(b_a,n_a-b_a); retain exactly those with sum u_a<=10.
Keep original orbit indices even when recursive coefficients coincide.
Theorem 12's denominator is
D=binom(i,t)binom(68-i,j-t)binom(i,s)binom(956-i,j-s)>0.

The prescribed coefficient routine is fixed before computation:
normalize weights by complementation, delete zero-weight blocks, and
use 1 at total weight below 5. At total weight 5, use the minimum of
floor(n_a/u_a) over the remaining blocks. Above 5, take the minimum,
over all positive-weight blocks a, of
floor((n_a/u_a) R(child_a)); child_a replaces (u_a,n_a) by
(u_a-1,n_a-1), then normalizes again. Inductively justify this routine
by the cited propositions before relying on it. The total weight strictly
decreases; the selected scope needs at most five deletion levels.
No exactness of this upper bound on K is claimed. The source omits
proofs of the appendix properties; a short applicability/induction
justification is essential to an implementation, rather than a new bound.

Check exact rational slacks R p_i-D y on every selected ordered orbit,
without dividing by p_i. Include forbidden and repeated words and all
zero-length regions. Independently reconstruct source coefficients and
assignment values; reconcile overlaps with the old certificates. Save
full selected-orbit values, recursion evidence and rational slacks to
disk, and print counts, exact minimum, violations and paths. No count or
slack is asserted here.

Continue only on a certified negative slack: it excludes this prescribed
extension for the weakened Theorem 12 family and identifies a constraint
for a later stronger support-bound attempt. It does not by itself bound
the optimized relaxation by T. If every selected row passes, park this
specific diagnostic; do not widen the residual cap or tune the assignment
within the same attempt. A pass says nothing about omitted Theorem 12
rows, the exact K coefficients, other PSD blocks or full-SDP feasibility.
Actual packing/list realization, scalar/tuple equality, exponent m,
sharpness, 67-agreement safety and ABF equivalence remain unresolved.
No novelty or theorem absence is inferred. Full matching Mathlib coverage
is not checked; this is a known-method specialization (REPRODUCTION).

## Separate approval and citation recovery (2026-10-06)

LITERATURE_REASON: The supervisor identified a missing direct source URL
in this ready assessment; this turn verifies the cited primary version
and repairs that essential evidence field without changing TARGET.

Reopened the [primary v1 PDF](https://arxiv.org/pdf/1212.3467v1) at
Theorem 12 and its complete proof, and at Propositions 22 and 25. The
previous source comparison remains adequate for the exact saved target.
The appendix explicitly omits proofs; applicability and recursive
induction remain implementation obligations. This approval establishes
no coefficient, slack, feasibility result or new mathematical input.
The prior ordinary-scalar stop in ATTEMPTS/015 remains in force.
No lemma, mathematical script or mathematical overview was changed.
