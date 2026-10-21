# L042 — At most 1024 deletions enforce the prescribed five-support exclusions

## Hypotheses

Use L041's subgroup H of order 1024 and generator h=19139. Fix any
C subset H of size 59. Let P be an ordinary (965,9,5,1) packing on
H minus C: its members are distinct nine-element subsets, and each
five-subset belongs to at most one member. Equivalently, distinct
members intersect in at most four points. Admissibility means exactly
L041's two conditions, including its full ordered common-shift condition
(A) and every permitted private choice. Independent edge shifts and
additional forbidden patterns are not included.

Let pi_C and alpha_C be the respective maximum sizes of ordinary
packings and L041-admissible families on H minus C. Both maxima
exist since the ground set is finite and both classes contain the
empty family.

## Conclusion

There is R subset P with |R|<=1024 such that P minus R is
L041-admissible. Consequently, at every 59-core,

\[
 \pi_C-1024\le\alpha_C\le\pi_C.
\]

This supplies no value or useful upper bound for either maximum,
no finite packing lower bound and no RS realization. L041's ordinary
nested upper bound is not a lower bound. The main bracket remains
955<=t_star(m)<=957 for every m>=1.

## Proof

**Assessed tools and specialization.** The prior SPECIALIZE assessment
`drafts/literature/2026-10-10-five-support-deletion-stability.md`
approves this exact test. L041 supplies the actual-label definition.
Import the ordinary packing definition from R.A. Bailey and A.C.
Burgess, *Generalized packing designs*,
[arXiv:1107.4120v2](https://arxiv.org/pdf/1107.4120v2),
15 November 2011, printed p. 2, Definitions 1.1.1/1.1.3. With
(v,k,t,lambda)=(965,9,5,1), the uniqueness property is precisely the
one in the hypotheses, and 965>=9>=5. No nested-floor bound or
design-existence theorem is used.

A transversal meets every hyperedge, as in Artem Chernikov,
*Topics in Combinatorics*, updated 28 February 2017,
[Definition 4.1, printed p. 21](https://www.math.ucla.edu/~chernikov/teaching/Combinatorics285N/CombinatoricsNotes.pdf).
Here packing blocks are vertices and violating five-block collections
are hyperedges. We construct a transversal directly; Remark 4.5's
general maximal-matching bound is not needed or reproved. Neither
definition supplies the numerical deletion conclusion. The application
below checks its label and completion quantifiers. This is REPRODUCTION
of assessed finite tools and their specialization, with no claim of
progress beyond those sources.

**One possible anchor at each active shift.** Put

\[
 E_s=\{s h^d:0\le d\le19\},\qquad
 V_s=\{s h^d:0\le d\le7\}\quad(s\in H).
\]

Because h has order 1024, these sets have twenty and eight distinct
points, respectively. Call s active if E_s is disjoint from C.
An inactive shift cannot witness (A), which requires all twenty
overlap points to avoid C. For an active shift, V_s lies in H minus C.
The first four edges in L041's order are 12,13,14,15, so V_s is
exactly the union of the four prescribed overlaps incident to vertex 1.

At most one block B in P contains V_s: otherwise two blocks would
both contain any five-subset of V_s, contradicting packing uniqueness.
This is an application of the imported uniqueness, not a reproof of
a general packing theorem. Denote the unique block B_s when it exists.
Its ninth point need not be a permitted private point. Selecting an
anchor that cannot participate in a violation causes no difficulty.

**A transversal with at most 1024 blocks.** Define

\[
 R=\{B_s:s\in H,\ E_s\cap C=\varnothing,
                   \ B_s\text{ exists}\}.
\]

R is a set rather than a multiset: at most one block is selected per
active shift and a block selected repeatedly is deleted once. Thus
|R| is at most the number of active shifts, hence at most |H|=1024.
Missing anchors contribute nothing. Empty P and no active shifts
are included.

Let P'=P minus R. Removing members preserves the intersection bound
of four. If P' had an ordered violation A_1,...,A_5 of (A), with any
common shift s and permitted private singletons W_1,...,W_5, that
shift would be active and its first block would satisfy

\[
 A_1=W_1\cup U_{12}\cup U_{13}\cup U_{14}\cup U_{15}
     =W_1\cup V_s.
\]

Since A_1 belongs to the original P and contains V_s, uniqueness
forces A_1=B_s. Therefore A_1 belongs to R, contradicting A_1 in P'.
This treats every ordering: whichever block occupies position 1
must contain that shift's V_s. It treats every private completion
without assuming uniqueness or bounding the number of completions
of the other four blocks. Any violation among surviving members was
already a violation among the original members and has the same
deleted first block. Thus no additional violation can survive or be
created by deletion, and P' is fully L041-admissible.

**Comparison of maxima and limits.** Every admissible family is an
ordinary packing by L041's first condition, so alpha_C<=pi_C.
Apply the deletion statement to an ordinary packing attaining pi_C.
The admissible remainder has size at least pi_C-1024, proving the
other inequality. For pi_C<1024 the inequality remains valid; no
nonempty remainder is asserted.

The continuation test succeeds for every core, with no transport
of packings by label permutations. A future ordinary packing lower
bound could now give an admissible-family lower bound. The result
does not turn an ordinary upper bound into a matching lower bound,
and an admissible family need not be realizable at one RS center
or consistent across cores. The deletion loss is not claimed optimal.
Safety at 67/68 agreements and the ABF comparison remain unresolved.
The separate critical audit below retains this conclusion; no complete
candidate is claimed.

**Separate critical audit (2026-10-10).** The turn-start SPECIALIZE
assessment `drafts/literature/2026-10-10-five-support-deletion-critical-audit.md`
covers this audit. We compare the proof with L041's stated condition
(A), rather than assuming that a five-block incidence pattern alone
is forbidden. These checks retain the hypotheses, constant and direct
input L041.

1. **Ground set and labels.** L041 fixes H of order 1024 and the
   generator h=19139. Its inherited order input is the audited L040
   identity h^1024=1, h^512=-1 in characteristic 65537, also used in
   C040a. Thus exponents 0,...,19 are distinct modulo the order;
   multiplication by s in H is injective. Every 59-core leaves exactly
   965 points. This uses the existing order input, not a new matrix
   or arithmetic certificate. On nine-sets the packing formulations
   agree: intersection size at least five gives a five-subset in two
   blocks, and a shared five-subset gives intersection size at least
   five. Distinctness of blocks is essential and explicit in P.
2. **Exact first position.** L041's edges 12,13,14,15 have indices
   0,1,2,3. Their pairs are {s,s h}, {s h^2,s h^3}, {s h^4,s h^5},
   {s h^6,s h^7}; their union is precisely V_s. The other six edges
   account for exponents 8,...,19. Any witness to (A) requires all
   twenty points outside C, so an inactive shift cannot give a
   witness even if V_s alone avoids C. No permutation of the edge
   assignment or separate shift for an edge is licensed by (A) or
   used in this proof.
3. **Unique anchors and all private choices.** For active s consider
   the original blocks containing V_s. If two distinct ones existed,
   the five distinct points {s h^d:0<=d<=4} would lie in both,
   contrary to packing uniqueness. Thus this collection is empty or
   the singleton {B_s}. In the empty case no ordered witness at s
   exists. Otherwise its ninth point is determined by B_s, but need
   not satisfy the private-point conditions. Deleting that block is
   still permitted and can only overdelete. For an actual witness
   those conditions hold and A_1=W_1 union V_s forces A_1=B_s.
   Neither existence nor uniqueness of completions at positions
   2,...,5 is required. Reordering the members cannot evade this:
   each witnessing ordering has a first member with this prescribed
   eight-set at its s.
4. **Entire transversal and surviving witnesses.** Map the subset of
   active shifts with a containing block to that unique original
   block. R is the image, so |R|<=1024 even if different shifts select
   the same block. A surviving ordered violation would still be a
   violation in P: its definition involves only its five members,
   labels, core and private points, not the presence of other blocks.
   Its first member is in R by the preceding check, a contradiction.
   Deletion also preserves the pair-intersection condition. With
   empty P the image is empty. With no active shifts condition (A)
   has no witness and the image is again empty. These cases require
   no choice of a nonexistent anchor or private completion.
5. **Attained maxima and inequality direction.** Both classes are
   nonempty subsets of the finite power set of the nine-subsets of
   H minus C. Their cardinality maxima are therefore attained. Every
   admissible family is an ordinary packing, giving alpha_C<=pi_C.
   For a maximizing ordinary P, the audited construction gives an
   admissible P' with |P'|=pi_C-|R|>=pi_C-1024. Maximizing over
   admissible families gives the other inequality. If pi_C<1024,
   the lower bound is merely nonpositive; it asserts neither a
   negative cardinality nor a nonempty remainder. No equality of
   admissible maxima at different cores is used.

All permitted violations are hit. No escaped ordering, private
completion, missing-anchor case or reversed maximum inequality was
found. This is independent local verification of the existing
specialization, classified REPRODUCTION, not a new deletion bound or
progress beyond the assessed tools. It establishes neither an ordinary
packing lower bound nor an obstruction to L041's sufficient cap.
Cross-core compatibility, common-center realization and 67/68-agreement
safety remain unresolved. The cited packing/transversal definitions
remain the only external tools; their general theorems are not reproved.

## Mathlib

Full matching coverage, finite-transversal declarations and supporting
finite-set theorem names were **not checked** in Mathlib. No absence
is asserted. This is an informal specialization, without a numerical
experiment, mathematical script or formal verification.
