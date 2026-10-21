# L038 — Adjoined affine family satisfies all sixty-core clauses

## Hypotheses

Use L034's actual subgroup H of order 1024 in E=F_65537 and its
definition of an admissible family of eight-subsets outside a 60-core C.
Fix any C in binomial(H,60), any A in binomial(H minus C,8), and put
X=H minus (C union A), of size 956. Use exactly L035's construction:
order A by its integer E-residues, order its 56 three-subsets T
lexicographically, and assign their distinct slopes s_T=0,...,55 in
the auxiliary field F_191. Set

\[
\Omega=(\{0,1,2,3,4\}\times\mathbb F_{191})\sqcup\{*\},
\quad \sigma:\Omega\longrightarrow X
\]

to be any bijection. For all 56 heads T and all b in F_191, put

\[
R_{T,b}=\{(x,s_Tx+b):x=0,1,2,3,4\},\quad
B_{T,b}=T\cup\sigma(R_{T,b}),\quad
\mathcal J_\sigma=\{A\}\cup\mathcal I_\sigma,
\quad \mathcal I_\sigma=\{B_{T,b}\}_{T,b}.
\]

Retain the separately audited L036 and L037 exclusions for precisely
this construction. No other slope assignment or coordinate set is used.

## Conclusion

For every allowed C,A,sigma, J_sigma is L034-admissible and has
cardinality 10697. Every distinct pair has intersection at most three.
No triple in J_sigma has empty triple intersection and all three pair
intersections of size three. No quadruple in J_sigma has all six pair
intersections of size two and empty triple intersections. Consequently
both labeled rank requirements of L034 are vacuous on J_sigma.

This is a construction of an admissible family, not an upper cap for
all admissible families. It supplies no cap meeting L034's benchmark
184665717, no common-center RS realization, and no improvement to
955<=t_star(m)<=957. Cross-core consistency, arbitrary-center safety at
67/68 agreements and ABF equivalence remain unresolved. The separate
critical review below retains this assembly without correction; it is
not a complete candidate resolution of the challenge.

## Proof

**Coverage and purpose.** The prior SPECIALIZE assessment
`drafts/literature/2026-10-08-adjoined-affine-admissibility.md` covers
exactly this all-clause target. The work assembles existing canonical
inputs with the separately adjoined block; it is RESEARCH/REPRODUCTION,
without a claim of novelty beyond the checked sources. The reused
primary comparison includes Alrabiah–Guruswami–Li,
*Randomly punctured Reed–Solomon codes achieve list-decoding capacity
over linear-sized fields*, [arXiv:2304.09445v3](https://arxiv.org/pdf/2304.09445v3),
Definition 2.5 and Lemma 2.7 with proof, printed pp. 7–8;
Shangguan–Tamo, *Combinatorial list-decoding of Reed–Solomon codes
beyond the Johnson radius*, [arXiv:1911.01502v1](https://arxiv.org/pdf/1911.01502v1),
Definition 4.1 and Lemmas 4.2/4.3, PDF pp. 9–11; and Agrell–Vardy–Zeger,
*Upper Bounds for Constant-Weight Codes*, June 24, 2000
[manuscript](https://publications.lib.chalmers.se/records/fulltext/local_14986.pdf),
definition (5), Theorems 8/32/36, printed pp. 3/6/16/17.
None states this enlarged-family conclusion. Their rank dictionaries
and shortening tools are already incorporated with the requisite
qualifications in the canonical inputs. No external rank or cardinality
theorem is newly imported or reproved here. The additional argument is
the exhaustive finite-set split below; no new enumeration is needed.

**Objects and pairs (clause 1).** Each R_(T,b) has five distinct points
because its first coordinates are distinct. Its image is in X, disjoint
from A and C, so B_(T,b) is an eight-subset outside C. Recovering
B_(T,b) intersect A=T distinguishes different heads. For fixed T,
distinct intercepts give disjoint nonempty graphs by L035's affine
equation, and hence distinct blocks. Thus I_sigma has 56*191=10696
members, as in L035. Every such block has five points outside A, so
none equals A. The adjoined family has 10697 distinct eight-subsets.

For a pair wholly in I_sigma, L035 gives intersection size three for
equal heads, and at most |T intersect T'|+1<=3 for different heads.
These are intersections of complete points, transported by the injective
map sigma. For a pair A,B_(T,b), the intersection is exactly T, of
size three. These two pair types exhaust all distinct pairs in J_sigma
and establish clause (1) of L034.

**Triples (clause 2).** Consider any three distinct blocks in J_sigma.
If all belong to I_sigma, the separately audited L037 excludes precisely
empty triple intersection together with all three pair sizes three.
Otherwise the triple is A,B_(T,b),B_(U,c). Its triple intersection is
T intersect U, since both tails are outside A. If this is nonempty,
L034's clause (2) antecedent fails. If it is empty, T and U are disjoint
and hence distinct. Their slopes are distinct, so L035's bound gives
|sigma(R_(T,b)) intersect sigma(R_(U,c))|<=1. The heads contribute
nothing to B_(T,b) intersect B_(U,c), and head-tail intersections are
empty. Thus its size is at most one, contradicting the required size
three. Equal-head and all intercept cases are included in this split.
There is no triple satisfying the antecedent, so no overlap-cubic rank
test is required. In particular no rank invariance under sigma is used.

**Quadruples (clause 3).** Consider any four distinct blocks in J_sigma.
If all belong to I_sigma, the separately audited L036 excludes all six
pair sizes two with empty triple intersections. L034's antecedent is
a special case: its prohibition of a point in three members implies
every triple intersection is empty, and it additionally requires the
six pair sets to be mutually disjoint. Thus no such four-neighbor
configuration requires a signed-matrix or difference-map test.

Otherwise the quadruple contains A and three neighbors. For each
neighbor B_(T,b), |A intersect B_(T,b)|=3, whereas L034 requires all
six pair intersections to have size two. Already these three pairs
contradict that antecedent, regardless of the remaining overlaps or
triple intersections. This exhausts quadruples because A was adjoined
only once and is distinct from every neighbor. Clause (3) is vacuous
on the whole enlarged family, including every configuration containing A.

All three exact L034 clauses hold. This uses incidence absence before
labels are tested; auxiliary F_191 is not assumed to embed in E or F.
L031 and L033 are therefore not needed as additional rank-test inputs
to this assembly. No singular configuration is incorrectly excluded:
neither labeled antecedent occurs at all. L036's retained full finite
certificate proof and L037's retained symbolic proof supply their stated
neighbor exclusions; aggregate numerical counts are not substituted
for either proof, and their completed audits are not repeated here.

The continuation test was a complete clause split, with an actual-label
violation stopping admissibility if an antecedent survived. The split
leaves none unchecked. This resolves the bounded intermediate claim,
while leaving the independent global gaps in the conclusion open.

**Separate critical audit, 2026-10-08.** The preexisting SPECIALIZE
assessment `drafts/literature/2026-10-08-adjoined-affine-critical-audit.md`
covers this exact audit. The review compared the complete assembly with
L034's definition and the precise constructions and retained exclusions
of L035–L037. It found no correction, new bound or additional mathematical
input. This is REPRODUCTION verification, with no novelty claim.

The quantifier check is as follows. Every allowed C and A leaves exactly
956 outside points, the size of Omega. Sending the ordered elements of A
to 0,...,7 carries its lexicographically ordered three-subsets to exactly
L036's ordered heads, so it carries every assigned slope to the same
slope. Combining this head map with sigma inverse on X is a bijection
of the disjoint ground sets. It transports every full intersection,
including triple intersections; all 191 intercepts remain present.
Thus neither L036 nor L037 is being applied to a different slope
assignment, a restricted intercept set or a different evaluation set.
The unused spare point creates no block or duplicate. Five distinct tail
points and the recovered head distinguish all 56*191 parameter pairs,
and no neighbor equals the separately adjoined A.

The exhaustive audit of L034's clauses is:

| Configuration of distinct members | Exact check |
|---|---|
| Two neighbors, equal heads | Different intercepts give disjoint tails; intersection is the three-point head. |
| Two neighbors, different heads | At most two head points and one complete tail point; intersection at most three. |
| A and one neighbor | Intersection is exactly its three-point head. |
| Three neighbors | L037 excludes exactly empty full triple intersection with three pair sizes three. |
| A and two neighbors | The triple intersection is the head intersection. If empty, heads are distinct and the neighbor pair has at most one point. Otherwise the empty-triple requirement fails. |
| Four neighbors | L034 clause (3) implies all six pair sizes two and every triple intersection empty, precisely the condition excluded by L036. |
| A and three neighbors | Each of the three pairs involving A has size three, contradicting the required size two. |

Distinctness, already checked, ensures this table exhausts every instance
of the three universally quantified clauses. In the four-neighbor row,
only the implication from L034's full antecedent to L036's excluded
condition is needed: the additional disjointness requirement cannot
create an omitted case. Neither the rank-two conclusion for triples nor
the six augmented-rank inequalities for quadruples need verification on
any actual labels, since their antecedents are absent. This does not
replace those requirements by singularity or assume rank invariance
under a bijection. No embedding of F_191 into E or F is used.

The audit accepts L036's separately audited finite exclusion and L037's
separately audited symbolic exclusion as inputs within their exact
scopes; it does not claim to revalidate their certificates from counts
or previews. The direct inputs in the existing DAG row remain unchanged.
The construction size 10697 remains distinct from the sufficient uniform
upper-cap benchmark 184665717. No cap, cross-core compatibility, common
received word or safety improvement is established by this verification.

## Mathlib

Full matching coverage for this enlarged-family admissibility statement:
not checked. Supporting finite-set cardinality, intersection and
finite-field affine-equation theorem names: not checked. No Mathlib
absence or formal verification is asserted.
