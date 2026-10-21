# Four-column augmentation — bounded resource test

TARGET: Test whether exact five-subset resource counting rules out augmenting the F_107 quartic graph packing by nine-sets on at most four evaluation columns past 19800269675 blocks.
CHECKED: 2026-10-10
DECISION: EXPLORE
SEARCH_EVIDENCE: Exact packing/constant-weight parameter searches and targeted four-column/support/RS-augmentation queries are recorded in 2026-10-10-finite-nine-set-packing-lower-bound.md; no matching finite resource optimization was retrieved and no novelty is claimed.
SOURCE_EVIDENCE: Direct primary PDFs https://arxiv.org/pdf/1505.06524v4 (Xu–Chen Proposition 2.2 and Theorems 2.1–2.2, printed pp. 3–4) and https://arxiv.org/pdf/1107.4120v2 (Bailey–Burgess Definitions 1.1.1/1.1.3 and Proposition 1.1.4, printed p. 2) were retrieved and inspected; local L041/L042 coverage is reused from the finite lower-bound assessment.
COMPARISON: Known graph constructions provide the finite baseline and a small augmentation; ordinary five-subset uniqueness supplies the resource-counting method, but the specified column-profile optimization is not an inspected source theorem.
GAP: Determine the finite resource allowance for this restricted augmentation and whether it excludes threshold crossing; an allowance above the requirement will not prove an actual packing.
REASON: A bounded finite obstruction test can reject an overly restricted construction before attempting a large packing; the searched sources do not answer this exact profile question.
SCOPE: Omega={0,...,8} times F_107, all degree-at-most-four graph blocks on these nine distinct evaluation points, augmentation by distinct nine-subsets of Omega meeting at most four columns, and ordinary five-subset uniqueness. The two extra points in a 965-point embedding are unused. No arbitrary-column extension or actual-label rank symmetry is included.

The separate literature approval step 124 retains DECISION: EXPLORE
for the unchanged target and supplies the missing direct primary URLs.
No calculation or new lemma was performed during that approval.
The finite lower-bound review at
`drafts/literature/2026-10-10-finite-nine-set-packing-lower-bound.md`
contains precise source hypotheses, versions, proof cases and unread leads.
Import the graph baseline by citation when used; do not reprove its
root-counting construction or silently import an uninspected large design.

The main gap is 67/68-agreement safety. The intermediate target tests
the resource capacity of one concrete augmentation mechanism.
A packing above 19800269675, if subsequently constructed, could use
L042's 1024-deletion guarantee to obstruct L041's sufficient uniform
cap. Neither this review nor a feasible resource relaxation gives
that packing, a common RS center or cross-core consistency.

After approval, first justify the relevant baseline/augmentation
intersection requirements. Then examine the finite linear resource
relaxation indexed by column multiplicity profiles: added nine-sets
have at most four nonempty columns; resources are five-subsets
classified by their column multiplicities. Derive and verify all
incidence coefficients and actual capacities rather than assume
an arbitrary-label symmetry. Column permutations are used only for
ordinary resource counting, not for L041's labeled exclusions.
Retain the q^5 graph baseline; do not assume the source's added
blocks can also be retained without checking conflicts.

The bounded discriminating test is an exact rational optimum or a
sufficient exact dual upper certificate. If the total resource upper
allowance is at most 19800269675, abandon threshold crossing for this
restricted augmentation. If larger, record only nonexclusion and
the remaining construction gap; a primal relaxation witness is not
a packing. Do not expand to more columns within this attempt.
Any script must save its full profile data and rational certificate,
with all row/objective checks and the actual/required bounds.

Essential local inputs for downstream use are L041's exact condition
(A) and benchmark and audited L042. ATTEMPTS/019,021,024,026 concern
different stopped models and remain unchanged. Full matching Mathlib
coverage is not checked; finite set counting and field/polynomial
support would not themselves certify this resource optimum.

## Separate approval and source repair — 2026-10-10

The direct [Xu–Chen v4 PDF](https://arxiv.org/pdf/1505.06524v4)
was checked against its [HTML](https://arxiv.org/html/1505.06524v4).
Proposition 2.2 assumes a prime power q and q>=w>r-1 and gives
A(wq,2w+2-2r,w)>=q^r using all polynomials of degree <=r-1
on any w-element evaluation set. For the saved q=107,w=9,r=5
parameters, 107>=9>4 meets these hypotheses. Import that baseline;
no root-counting reproof is needed. The full proofs of Propositions
2.1–2.2 and Theorems 2.1–2.2 were read. Theorem 2.2 additionally
requires r>=3; its augmentation proof uses at most two columns
and explicitly checks both new/new and new/graph intersections.
This is relevant precedent, not a theorem for our four-column LP.
The source's optional added blocks are not part of the saved baseline.

The direct [Bailey–Burgess v2 PDF](https://arxiv.org/pdf/1107.4120v2),
printed p. 2, defines t-(v,k,lambda) packings for positive integers
v>=k>=t, with each t-subset in at most lambda blocks. Definition
1.1.3 gives the maximum and Proposition 1.1.4 the nested-floor
upper bound. These supply ordinary packing terminology and uniqueness,
not an evaluated column-profile resource optimum or construction.
No proof of that upper bound is needed for the proposed diagnostic.

Reuse the queries, finite-source comparison and unread-lead distinctions
in `2026-10-10-finite-nine-set-packing-lower-bound.md`; no new search
is required by an unchanged scope. Targeted local searches find the
four-column resource proposal in that assessment and this one, with
no completed duplicate certificate. ATTEMPTS/019,021,024,026 were
read: they stop other local relaxations, an anchored neighborhood
cap, and repeated transfer coverage, rather than this augmentation
test. Their evidence remains intact. No source-dependent obstruction
requires parking this now accessible target.

Approval covers exactly the saved SCOPE and discriminating test.
All profile coefficients, capacities, compatibility arguments and
exact rational validation are future mathematical work. L041 and
L042 are downstream inputs, not prerequisites for resource counting;
their canonical statements must be read before any downstream
specialization. No new result, Mathlib coverage claim, global
packing nonexistence or threshold improvement is established.
