# L037 — Nonanchored triple-incidence exclusion in the fixed affine family

## Hypotheses

Use L035's unchanged construction. In particular, let C be any
60-subset of C001a's actual subgroup H, let A be any eight-subset of
H minus C, and put X=H minus (C union A), of size 956. Order A by
its integer residues and its 56 three-subsets T lexicographically.
Give T the slope s_T in {0,...,55} in the auxiliary field F_191.
Put Omega=({0,...,4} times F_191) disjoint union {*}, and let
sigma:Omega -> X be any bijection. For every b in F_191, write

\[
R_{T,b}=\{(x,s_Tx+b):x=0,\ldots,4\},\qquad
B_{T,b}=T\cup\sigma(R_{T,b}).
\]

The three blocks considered below are distinct members of L035's
family I_sigma. The distinguished block A is not one of them.

## Conclusion

There are no three distinct members B_1,B_2,B_3 of I_sigma such that

\[
B_1\cap B_2\cap B_3=\varnothing,
\qquad |B_i\cap B_j|=3\quad(1\le i<j\le3).
\]

This holds for every C,A,sigma, all intercepts, and the exact prescribed
56 slopes. Thus the incidence hypotheses of L033, equivalently clause
(2) of L034, never occur among three neighbors in this family. That
clause is vacuous there, without any actual-label cubic rank calculation.
No full L034 admissibility, adjoined-block quadruple exclusion, full-family
cap, cross-core consistency, common-center RS realization or boundary
improvement is asserted. The 955–957 bracket remains unchanged.

## Proof

**Coverage, purpose and reused input.** The preexisting EXPLORE assessment
`drafts/literature/2026-10-08-affine-nonanchored-triple-incidence.md`
covers this exact target. Its inspected source comparison found no
matching theorem deciding this prescribed incidence; it does not establish
novelty. The argument is a local reproduction of L035's affine
intersection method and elementary finite-set counting. No new external
theorem is imported or reproved. L035 supplies the field construction
and its exact pair-intersection bounds. L033 and L034 explain the use
of the conclusion, rather than supplying mathematical premises of the
exclusion. Their actual-label criteria are not replaced by a generic
rank claim. L036 concerns a different, four-neighbor incidence and is
not used here.

For i=1,2,3 write B_i=T_i union Q_i, with
Q_i=sigma(R_(T_i,b_i)). The head T_i lies in A, and Q_i lies in X,
which is disjoint from A. Consequently, for every pair,

\[
|B_i\cap B_j|=|T_i\cap T_j|+|Q_i\cap Q_j|,
\]

and the full triple intersection is the disjoint union of the head
triple intersection and the tail triple intersection. In particular,
an empty full triple intersection implies T_1 intersect T_2 intersect
T_3 is empty.

L035 proves that different head triples have different slopes and
their tail sets intersect in at most one point, for every intercept
pair. Indeed a common point must have equal x-coordinates and satisfy
(s_(T_i)-s_(T_j))x=b_j-b_i in F_191. The nonzero slope difference
admits at most one x. The bijection sigma preserves this intersection
count. With equal heads, distinct blocks have distinct intercepts,
and their tails are disjoint; their shared head remains the whole
three-set. These bounds retain equal intercepts between different
slopes and do not require translating intercepts or enumerating cases.

Suppose the stated incidence exists. The following three cases exhaust
all equality patterns among the three heads.

1. **All heads equal.** Their common three-set lies in the full triple
   intersection. This contradicts its emptiness.
2. **Exactly two heads equal.** Relabel so that T_1=T_2=T and T_3 is
   different. Empty full triple intersection forces T intersect T_3
   to be empty, since T intersect T_3 is precisely the head triple
   intersection. The pair B_1,B_3 therefore has no shared head point,
   and its different-slope tails meet at most once. Its full pair
   intersection has size at most one, contradicting size three.
   The distinctness of B_1,B_2 entails b_1!=b_2, so no duplicate
   block is hidden in this case.
3. **All heads distinct.** Each pair of three-sets T_i,T_j shares at
   most two points, while its tails share at most one. Full pair
   intersection size three therefore forces
   |T_i intersect T_j|=2 and |Q_i intersect Q_j|=1 for every pair.
   The two sets T_1 intersect T_2 and T_1 intersect T_3 have
   intersection T_1 intersect T_2 intersect T_3, which is empty.
   They would be two disjoint two-subsets of the three-set T_1.
   Their union would have size four and be contained in T_1,
   a contradiction.

Hence the incidence is absent. This argument covers every block triple
and every bijection directly; it is a complete exclusion, not a bounded
search miss. No numerical script, translation quotient, actual-label
symmetry or auxiliary-field embedding into E is used. Pair intersections
are complete points, rather than coordinate indices. If the incidence
had occurred, its three pair sets would be mutually disjoint, and each
eight-set would have 8-3-3=2 private points. Thus omitting a separate
private-part condition does not strengthen the intended incidence test
incorrectly: the excluded condition already implies it.

The plausible downstream use is to discharge L034's triple clause
among the fixed neighbors while considering stronger neighborhood
restrictions. It supplies no quantitative transfer to L034's benchmark
184665717. The already audited four-neighbor result L036 is independent;
quadruples involving the distinguished block, whole-family assembly,
cross-core consistency, RS realization, 67/68-agreement safety and
ABF equivalence remain outside this step. The separate critical audit
below retains this proof.

**Separate critical audit, 2026-10-08.** The preexisting EXPLORE assessment
`drafts/literature/2026-10-08-affine-triple-exclusion-critical-audit.md`
authorizes this unchanged-family audit. The complete L035 construction
and pair proof, the proof above, and the exact hypotheses of L033 and
clauses of L034 were checked. No theorem correction or additional
mathematical input was needed. This is verification of the existing
local reproduction, not a new result beyond the sources assessed there.

First, the objects have the required sizes and distinctness. The five
elements of R_(T,b) have different first coordinates, so every tail has
size five. Its image lies outside A, making every block an eight-set.
Intersecting a block with A recovers its three-set T. For a fixed T,
different b give disjoint nonempty graphs; thus distinct parameter pairs
give distinct blocks, and distinct blocks with equal heads have different
intercepts. There are no duplicate-block exceptions to the head cases.
The spare point belongs to no graph and does not affect intersections.
These facts apply to every allowed C,A and sigma.

Second, the pair bound is uniform in the intercepts: equality of complete
ordered tail points forces the same x and the single equation
(s_T-s_U)x=c-b. For T!=U the coefficient is nonzero in F_191, since
the 56 assigned slopes are distinct. There is at most one solution in
the entire field and hence at most one in {0,...,4}. This includes
b=c and all possible intercept values. For T=U and b!=c there is no
solution. Injectivity of sigma preserves all intersections, including
triple intersections, and its image is disjoint from the heads. The
argument never identifies points just because they have the same x.

Third, an empty full triple intersection forces an empty head triple
intersection, without any converse being assumed. All equal heads
contradict this immediately. With exactly two equal heads T, the third
head U must satisfy T intersect U empty. Any pair with heads T,U then
has full intersection at most one, contradicting the required three.
With three distinct heads, full pair size three and the audited tail
bound force every head pair to intersect in exactly two points. In
particular, inclusion-exclusion inside T_1 gives

\[
 |T_1\cap T_2\cap T_3|
 \ge |T_1\cap T_2|+|T_1\cap T_3|-|T_1|
 =2+2-3=1,
\]

contradicting its emptiness. This independent cardinality check confirms
the disjoint-two-subsets argument. The three partitions of head equality
exhaust all possibilities; no slope ordering, translation representative,
or finite enumeration is required. No assumption on tail triple
intersections is needed beyond the original full-intersection hypothesis.

Finally, the downstream implication uses full sets, not just heads.
If the excluded incidence held, put U_ij=B_i intersect B_j. Any two
of the three U_ij meet only in the empty triple intersection, so they
are mutually disjoint three-sets. Define
W_i=B_i minus (B_j union B_k). Within B_i the removed part is the
disjoint union U_ij union U_ik, of size six, so |W_i|=2. Each W_i
belongs to neither other block. Hence the three W_i are mutually
disjoint and disjoint from every U_jk. All these sets lie outside C.
Thus S_i=C union B_i would meet exactly L033's common-core, overlap
and private-part hypotheses, and L034 clause (2) has exactly this
antecedent. Excluding the antecedent makes that clause vacuous among
the neighbors; it says nothing about cubic ranks for other families.

The audit retains the conclusion and direct dependency L035. L033 and
L034 serve only to identify its intended use; no result from L036 or
any external rank theorem enters the exclusion. No numerical evidence
or mathematical script is needed for this exhaustive symbolic proof.
The unproved admissibility, cap-conversion and realization claims listed
above remain unproved here. No error was found and no new bound was
established; the 955–957 bracket is unchanged.

## Mathlib

Full matching exclusion for this fixed affine family: **not checked**.
Supporting finite-set intersection/cardinality and finite-field linear
equation theorem names: **not checked**. No formal verification or
absence from Mathlib is asserted. The proof above is complete informal
evidence, with the separate informal critical review recorded above.
