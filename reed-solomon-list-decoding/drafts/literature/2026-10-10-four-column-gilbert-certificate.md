# Four-column finite Gilbert certificate — approved specialization

TARGET: Evaluate exact Gilbert closed-neighborhood lower certificates for all nine-sets on at most four F_107 columns and each single-profile subuniverse against total packing size 19800269675.
CHECKED: 2026-10-10
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the completed compatible-four-column search and checked L043, ATTEMPTS/027–028 and history/130; reinspected Wang et al. v1 Section IV p. 8 for the finite inequality and its scope.
SOURCE_EVIDENCE: Wang–Wei–Shangguan–Ge arXiv:1512.08220v1 Section IV p. 8, ball display and first inequality in Theorem 4.4 proof; reuse Xu–Chen arXiv:1505.06524v4 Proposition 2.2 as imported in L043.
COMPARISON: Import the standard finite Gilbert greedy method; the equal-weight source volume is not a formula for this mixed-profile universe. Approve only its finite maximum-neighborhood specialization and exact counting test.
GAP: The mixed-profile closed-neighborhood formula, maximum, integer rounding and resulting lower certificate remain to be proved and checked; no threshold crossing is known.
REASON: This separate source comparison approves the saved target without deriving it; exact mutual-conflict counting is distinct from the exhausted resource exclusion and quoted Derksen lower bound.

SCOPE: Finite Gilbert maximum-closed-neighborhood certificates on the stated full union or one decreasing-profile subuniverse; no union of separately selected packings, optimization over different mechanisms, or RS realization.

Approved scope: Omega={0,...,8} times F_107; all distinct nine-subsets
meeting at most four columns, and separately the subuniverses with
one fixed decreasing positive column profile of nine. Include every
column assignment and every point subset. Conflicts are intersection
at least five; include the chosen block in its closed neighborhood.
Do not add results from different subuniverses without compatibility.
Use maximum closed-neighborhood size for each selected universe,
with the appropriate integer rounding justified from the finite greedy
method. Count exactly, without exhaustive block enumeration or a
resource relaxation. A full certificate must contain every profile
count, neighborhood contribution, actual lower bound and benchmark
comparison, and independent small-parameter checks.

Essential input is L043's scope and imported 107^5 graph baseline.
L041/L042 give downstream relevance only; L044 and ATTEMPTS/027–028
remain preserved contrasts. The test could guarantee a compatible
augmentation, but a shortfall rejects only this certificate, not larger
packings. Continue to a separate application only if the guaranteed
total is strictly greater than 19800269675; otherwise park this
prescription. Two extra embedding points remain unused. Actual-label
transfer, cross-core consistency, common-center realization, 67/68
safety and ABF comparison remain unresolved. Mathlib not checked.
No new finite formula or bound is asserted here. Source coverage is now
ready for the exact saved target; changes outside this scope require review.


## Separate source comparison, 2026-10-10

Read the primary [Wang–Wei–Shangguan–Ge v1](https://arxiv.org/pdf/1512.08220v1),
Section II.A p. 2 and Section IV p. 8, including the full Theorem 4.4
proof. The finite input concerns binary words on fixed equal-size
parts with equal weight; its forbidden ball includes the selected word.
The finite inequality precedes the entropy estimates. The theorem's
omega/delta restrictions concern the asymptotic conclusion, which is
not the input approved here. No entropy estimate is authorized for
the finite certificate.

The standard named Gilbert greedy bound supplies the method, not the
new universe's neighborhood size. Future proof must explicitly justify
its application to a finite conflict graph, including nonconstant
neighborhood sizes and integer rounding. This short applicability
argument is necessary because the product formula's hypotheses fail
for varying profiles and occupied columns; it is not a reproof of the
source's asymptotic theorem. The source does not state a mixed-profile
threshold-crossing construction.

Reuse the completed broader search and its product/asymptotic
comparisons rather than repeat discovery. L043's hypotheses and
compatibility paragraph were inspected: its cited Xu–Chen Proposition
2.2 applies with (q,w,r)=(107,9,5). Retain that baseline and the
963-point universe. L043's resource optimum and ATTEMPTS/027 are
contrasts only; ATTEMPTS/028's small quoted lower bound gives no upper
bound or ban on this test. History/130 records this as a pending test,
not a completed calculation. No duplicate completed certificate was
identified within the relevant scope.

The full union and each single-profile universe are alternative tests.
A single-profile universe still includes all placements of its parts
on the nine labeled columns, not merely one fixed placement. The
certificate must account for neighborhoods into its entire chosen
universe, and for every profile of a possible selected block. Do not
substitute resource capacities, average neighborhood sizes or a sum
of independent lower bounds for the approved maximum-neighborhood
certificate. Independent small-parameter checks validate counting
implementation but cannot replace its combinatorial proof.

The exact continuation/abandonment test and downstream limitations
above are unchanged. This approval is local literature progress only,
with no claim of originality. Mathlib coverage remains not checked;
no matching theorem there is asserted. No lemma or mathematical
script was written in this review.
