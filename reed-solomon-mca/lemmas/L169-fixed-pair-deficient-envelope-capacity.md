# L169 — Deficient-envelope capacity for the fixed L167 pair

## Hypotheses

Let E be any extension field of F_97. Fix

    S=(1,8,12,18,22,27,33),
    J=(47,50,64,70,75,79,85,89,96), H=S union J.

The universe consists of all 756 supports A=I union K with
I in binom(S,2), K in binom(J,2). Use increasing lexicographic pairs,
I outermost, giving zero-based labels 0,...,755. Use L109's entire
six-by-21 block N_A, with z=min(S minus I), increasing covector pairs,
and increasing S-coordinate-pair columns. Explicitly, set

    g_A(X)=product_{y in J minus K}(X-y),
    c_Ax=g_A(z)e_x^* - g_A(x)e_z^*  (x in S minus (I union {z})),
    (N_A)_{(x,y),(a,b)}=c_Ax,a c_Ay,b-c_Ax,b c_Ay,a.

Let F be a family of distinct universe supports with

1. A_237={8,12,70,75} and A_570={18,22,79,85} in F;
2. |A intersection B|<=1 for distinct A,B in F;
3. each h in H has ordinary integer degree d_h(F)<=4.

The mandatory supports are precisely rows 2 and 3 of L167's canonical
table. No other row of that table is mandatory. Let N_F stack the
original whole blocks for F. These are finite matrix/incidence
hypotheses; no coding, decomposability, projection-rank or weight
condition is imposed on F.

## Conclusion

If rank_E N_F<21, then **|F|<=11**. Equivalently, every such family
with at least twelve members has rank 21 over every extension of F_97.
In particular, every deficient complete-block closure containing the
mandatory blocks has selected-support capacity at most eleven, when
the selection must include the mandatory pair and satisfy hypotheses
2–3. Closure members are optional; the full closure need not itself
be linear or degree feasible. Attainment of eleven is not asserted.

The full bounded cover, same-step independent reconstruction and separate
critical audit on 2026-10-28 pass. This is a fixed numerical
pair exclusion, not an all-pair assertion, a coding realization or a
challenge solution. Classification: **POTENTIALLY_NEW**, only in the
sense that the prior source comparison supplied no matching instance
bound; mathematical originality is not certified.

## Proof

### Known inputs and the instance-specific difference

L109 supplies the block formula, rank-six property and the necessary
coding rank obstruction; L167 supplies the numerical table identifying
the pair. The blocks are rebuilt here, without importing L168's rank
certificate or any other pair's later-row behavior. L153's census is
not a premise.

For the closure language, use Crowley–Simpson–Wang, *Combinatorial
flats and Schubert varieties of subspace arrangements*, Algebraic
Combinatorics 8(5) (2025), 1285–1312, section 2.1 and Example 2.2,
pp. 1289–1290, [published author copy](https://connorgs.net/assets/papers/combinatorial_flats_and_schubert_varieties_of_subspace_arrangements.pdf).
Their rank/intersection-of-kernels description applies over an arbitrary
field. Here the ambient space has dimension 21 and the maps are N_A;
the rank of a label set is dim(sum_A row(N_A)). Thus its usual closure
consists of labels whose entire blocks add no rank. The paper's later
characteristic-zero geometry is not imported.

General finite closure enumeration is already covered by Borchmann,
*A Generalized Next-Closure Algorithm — Enumerating Semilattice
Elements from a Generating Set*, CLA 2012, Theorems 1–2 and Lemmas
1–3, pp. 10–14, [primary PDF](https://ceur-ws.org/Vol-972/paper1.pdf).
No general enumeration theorem is reproved or claimed as new. The
certificate below uses a more redundant ordered-history cover, whose
particular pruning needs the explicit justification given below;
Next-Closure does not justify that pruning.

For capacity certificates, import finite LP weak duality from Boyd–
Vandenberghe, *Convex Optimization* (2004), sections 5.1.3 and
5.2.1–5.2.3, pp. 216,224–227, [author PDF](https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf).
The incidence constraints below have nonnegative residual capacities;
additional pair-group rows have capacity one. This is an ordinary
finite nonnegative packing LP. Only displayed feasible rational dual
weights and weak duality are used, not integrality or strong duality.

The invocation-start EXPLORE assessment is
`drafts/literature/2026-10-28-block-closure-capacity-pilot-review.md`.
The missing source-level ingredient was precisely a complete rank/
capacity coupling for this pair. The present additional ingredient is
the deficient-extension envelope and its fully checked finite cover.

### Descendant-safe envelope and ordered histories

Work first over F_97. For a selected history T beginning with (237,570),
let W(T) be the sum of its whole block row spaces and r(T)=dim W(T).
Let

    C(W)={a:row(N_a) subset W},
    D(W)={a:dim(W+row(N_a))<21}.

If W is contained in a deficient span W', every block lying in W'
belongs to D(W): W+row(N_a) is then contained in W'. This is why a
capacity bound on D(W) controls deficient descendants. No analogous
inference from capacity on C(W) alone is made.

For reproducibility, a history orders only its nonmandatory labels
in increasing order. Its last added label is -1 if there are none.
The candidate list B(T) consists of **every** label a satisfying:

- a is not already selected and exceeds the last added label;
- r(T union {a})<21;
- A_a intersects each selected support in at most one label;
- d_h(T)<4 for every h in A_a.

Suppose a deficient family F satisfying the hypotheses contains T,
and T's added labels form an initial segment of F's sorted nonmandatory
labels. Every remaining label of F lies in B(T). The rank condition
follows from the preceding envelope containment; the other three
conditions follow from ordering, linearity and integer degrees in F.
This statement is the cover invariant, including at low deficient ranks.

At a branch, the tree has one child T followed by a for every a in
B(T). Histories are never merged, even when their spans agree. Only
the whole-block rank/closure data are cached by span. The residual
degrees, candidate restrictions, capacity certificate and children are
computed separately for each history. The tree may stop a history only
with a verified total capacity bound at most eleven.

To see why this suffices, assume a deficient F with at least twelve
members exists and, if necessary, take a twelve-member subfamily
containing the mandatory pair. Starting at the root, follow its least
remaining nonmandatory label whenever the tree branches. The invariant
puts that label in the complete child list. At any terminal node all
remaining members are candidates, so a total bound at most eleven
contradicts the twelve members of F. The exact finite tree below has
no pending branch and all its leaves have that bound. This proves the
required exclusion without enumerating all maximal deficient closures.

### Exact capacity certificates on the envelopes

For a history T let b_h=4-d_h(T). For any possible additional selection
X subset B(T), its incidence vector x satisfies

    sum_{a:h in A_a} x_a <= b_h,
    sum_{a:I_a=I} x_a <= 1,   sum_{a:K_a=K} x_a <= 1.

The group inequalities follow because two distinct supports with the
same I, or the same K, would intersect in at least two labels. They
do not assert that whole blocks form a matroid. Already selected
supports are included in d_h(T); each candidate is separately compatible
with all of them. Dropping further conflicts between candidates only
enlarges this relaxation.

The certificate either uses |X|<=|B(T)| or supplies a coordinate set
U subset H, a denominator q in {1,2}, one grouping side I or K, and
nonnegative integer numerators t_G for that side's pair groups. It
checks, for **every** a in B(T),

    |A_a intersection U| + t_{G(a)} >= q.

Assign weight 1/q to each coordinate in U and t_G/q to group G,
with all other weights zero. This is a feasible dual for the displayed
packing constraints. Weak duality bounds

    |X| <= (sum_{h in U} b_h + sum_G t_G)/q.

All quantities on this line are ordinary rational or integer quantities,
not residues modulo 97. Since |X| is an integer, the recorded total
bound is |T| plus the floor of this rational value. The verifier checks
every column inequality, every numerator, all nonnegativity conditions
and the exact objective; it need not trust the producer's search for
weights or their optimality.

For example, node 1 has history (237,570,0). Its complete 136-label
candidate envelope has the certificate U={18,22}, q=1, grouping side I,
and t_{8,27}=t_{8,33}=1, all other t zero. Both coordinates have
residual capacity three, so the additional bound is 3+3+1+1=8 and
the total bound is 3+8=11. The complete candidate list and its column
checks, not this example alone, occur in the full evidence.

### Full finite cover and independent exact verification

The producer `scripts/block-closure-capacity/pilot.py` constructs all
756 original blocks from the product formula. It stores full blocks,
canonical complete kernel bases, all extension ranks, entire closures,
every history/candidate list/dual/child list, input hashes and the frontier
in `scripts/block-closure-capacity/pilot.json`.

For a canonical basis K of ker N_T, stored as rows, adding block N_a
adds exactly rank(N_a K^t) to r(T). Indeed the new kernel is the
kernel of the restricted map N_a on ker N_T, so rank-nullity gives
this equality. The coefficient kernel of N_a K^t, multiplied by K,
gives the entire child kernel. These computations retain each of the
six equations in each original block. A zero increment is precisely
complete-block closure membership.

The completed producer cover has:

| Quantity | Exact result |
|---|---:|
| Distinct generated deficient spans | 300 |
| Whole-block extension tests | 226800 |
| Histories of lengths 2,3,4 | 1,382,12125 |
| Branch nodes | 91 |
| Capacity leaves | 12417 |
| Largest leaf upper bound | 11 |
| Pending frontier | 0 |

The distinct-span rank distribution is
12:1, 16:4, 17:164, 18:106, 19:4, 20:21. These are the ranks reached
in this exhaustive cover, not a generic-rank assumption or a restriction
on allowed deficient ranks. All 382 third-label histories are retained;
90 branch further and 292 close by capacity. Every fourth-label history
closes by capacity. The limits of 10000 spans and 1000000 block tests
were not reached.

The independent `scripts/block-closure-capacity/verify.py` imports no
producer code. It enumerates four-subsets of H and retains exactly the
two-plus-two supports. It expands each g_A polynomial, evaluates it by
Horner's rule, forms normalized quotient covectors, and rescales their
exterior blocks by g_A(z)^2 to reproduce every original entry, pivot
and ordering. It independently checks all 756 block ranks. For each
span it reconstructs the original generating stack, checks the complete
canonical kernel and all its residuals, and records an explicit nonzero
rank-sized minor with original row and column indices and determinant.
It independently recomputes all 226800 extension ranks and all closures.

The verifier then checks every history, all integer degrees and pair
intersections, all candidate lists, every dual inequality, the full
child lists, their exact parent histories and 10367 distinct kernel
transitions. Strictly earlier parents make the finite tree acyclic;
the unique root is the mandatory pair. No frontier entry or twelve-row
witness is left outside the tree. All 12417 terminal bounds pass.
Complete reconstructed blocks, full kernels/minors/rank vectors and
node verification records are in
`scripts/block-closure-capacity/verification.json`; its failures list
is empty. These are the original same-step independent checks; the
separate critical audit below inspects both complete saved certificates.

Reproduction commands, from the notebook directory:

```text
python3 scripts/block-closure-capacity/pilot.py
python3 scripts/block-closure-capacity/verify.py
```

All field arithmetic is exact modulo 97. Matrix products use signed
64-bit integers only for sums of at most 21 products of residues
0,...,96, bounded by 193536; elimination and polynomial operations use
Python integers. No floating optimization, approximate rank, random
sample, external solver or symmetry transport is used.

Finally every original block has entries in F_97, so the rank of every
support stack is unchanged over any extension E, by its minors. The
integer incidence inequalities are unchanged. The result therefore
holds over every such E, including the algebraic closure; it is not
just a sample over F_97. If a deficient span W contains the mandatory
blocks and a feasible selection of twelve of its closure members, that
selection would be the forbidden F. This also proves the closure-capacity
formulation.

### Separate critical audit, 2026-10-28

Step 535 uses the invocation-start EXPLORE assessment
`drafts/literature/2026-10-28-l169-critical-audit-review.md` and its
already inspected closure/weak-duality sources. It imports no additional
mathematical theorem and makes no claim of a stronger or original result.
Both entire original scripts and both complete certificates were inspected.
No missing essential source or mathematical correction was identified.

The logical cover is valid. For any supposed deficient family with at
least twelve members, a twelve-member subfamily containing the mandatory
pair remains deficient, linear and degree feasible. Order only its ten
other labels. At every prefix T, each remaining whole block lies in the
deficient span of that subfamily. Thus its extension from W(T) is still
deficient, even if the rank increment is zero. Every remaining label
also passes the order, distinctness, pairwise-linearity and residual-degree
tests. It is therefore in the *entire* B(T), not just the current closure.
If the node branches, its least remaining label is a recorded child.
Every terminal node gives a total bound at most eleven. The finite tree
has a unique root and strictly earlier parents, so the path cannot end
elsewhere or cycle. This contradicts the presumed twelve-member family.

Equal kernels identify equal row spaces under the nondegenerate coordinate
pairing. They justify caching extension ranks, but not merging histories.
The audit checks each history's original stack directly, as well as its
own degrees, ordering, candidate list and children. In particular,
mandatory label 570 is not a lower bound on nonmandatory labels: the
root's last-added marker is -1. Optional closure members may occur as
zero-increment children and are never made mandatory. Low deficient ranks
are covered by the same invariant; the displayed reached-rank histogram
is not an additional assumption on families.

Every I-group and every K-group has selection capacity one because any
two distinct members intersect in its two labels. This remains true in
every residual selection; selected supports have already been removed
or enforced by compatibility. Dropping other candidate conflicts enlarges
the relaxation. All residual coordinate capacities are nonnegative
integers, including zero. The exact nonnegative dual satisfies every
candidate column, with genuine pair-group indices. Its rational objective
bounds the integer number of additions; flooring only that objective and
then adding |T| is sound. No optimality, integrality of the LP or field
arithmetic in the degree/dual computations is used.

The new `scripts/block-closure-capacity/audit_l169.py` imports neither
producer nor verifier. It reconstructs every original block by the product
formula; elementary symmetric coefficients independently check all stored
expanded polynomials. Incremental row insertion and backward substitution
replace the earlier Gauss-Jordan routines. The audit checks all 756
rank-six blocks, every full canonical kernel and the original nonzero
rank minor for all 300 spans, and all 226800 whole-block extension ranks
and closure memberships. It compares every reconstructed mathematical
field in both saved certificates, including all normalized matrices,
original minor indices, 12508 node records and the complete summaries.

Crucially, it reconstructs the original stack and *entire* canonical
kernel for each of the 12508 histories, independently of cached parent
transitions. These checks validate all 10367 distinct transitions because
each child history is exactly its checked parent's history with the
chosen label appended, and both stacks have their claimed kernels. The
audit checks every candidate and exact dual column and proves equality
between the recorded and actually reached children at every node.
The 91 branches and 12417 terminal nodes all pass; the largest terminal
bound is 11, against the forbidden size 12. There are 200143 audit checks
and zero failures. This is a complete comparison and replay, not an
inference from the summary or a sample of histories.

Full reconstructed blocks, kernels, extension-rank vectors, original
minors, all history records with complete candidate lists and dual-column
coverage, checks and input hashes are saved in
`scripts/block-closure-capacity/l169-critical-audit.json`. The original
`pilot.json` and `verification.json` are preserved. Reproduce with:

```bash
make -C scripts/block-closure-capacity audit
```

All elimination and dual arithmetic uses Python integers. The only
fixed-width matrix products sum at most 21 products of residues at most
96, giving 193536 before reduction, safely within signed 64-bit range.
For every possible support family, all stack entries are in F_97.
Consequently its rank over any extension E equals its rank over F_97:
nonzero base-field minors remain nonzero and vanishing minors remain zero.
This reduces a purported extension-field counterexample to exactly the
base-field finite cover. It requires neither a rational chosen kernel
vector nor descent of a decomposable plane. Integer incidences do not
change under extension.

Verdict: L169's fixed-pair theorem passes separate critical scrutiny.
The direct mathematical inputs remain L109 and L167; no new DAG edge
is needed. This independently establishes the reliability of the local
partial input without extending it to a different pair, all pairs, a
coding converse or the grand challenge.

### Qualifications and downstream boundary

Nothing identifies an arbitrary disjoint pair with labels (237,570).
C152a extracts an unspecified pair; neither its result nor equal pair
ranks permit this exclusion to be transported. No common-kernel tensor
is presumed decomposable, and no rank-zero restriction, recovered weight,
locator, chart or event is inferred from an exterior constraint.

A coding application still requires the hypotheses establishing this
represented class: L104/L086/L010, F=F_(97^20), k=8, unit multipliers,
the pinned 1/4<=delta<5/16 cell, both syndromes in U_S, sixteen original
finite events, t=0, nonzero D and locators, arbitrary original weights/
chart and all inherited qualifications, as well as identification of
the mandatory numerical supports. The present necessary exclusion
does not establish arbitrary representation, a wider radius, challenge
equivalence or a solution of the grand MCA challenge.

## Mathlib

Full matching coverage for this finite rank/incidence exclusion is
**not checked**. The cited closure and weak-duality results are supporting
inputs, not a matching instance theorem. No Mathlib absence or theorem
name is inferred from this calculation. The explicit full blocks,
kernels, minors, complete history cover and rational duals provide the
informal finite certificate and its reproduction path.
