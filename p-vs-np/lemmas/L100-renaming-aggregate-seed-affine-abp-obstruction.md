# L100 — An exact cut-rank obstruction for the aggregate initial seed

## Hypotheses

Fix n≥1 and the free algebra F₂⟨x_1,x'_1,…,x_n,x'_n⟩ on 2n
distinct generators. Let ρ_i exchange x_i and x'_i and fix all other
generators. For U⊆[n], let a_U be the length-n word whose jth letter
is x'_j if j∈U and x_j otherwise. Put a=a_∅ and p=a+a². Define

    S_0=p,
    S_i=ρ_i(S_(i−1))p+S_(i−1)(1+ρ_i p)p,   1≤i≤n.       (1)

This is precisely L099 §3's initial-seed contribution: first set every
later axiom seed Z_i to zero in that recurrence, then substitute B.
Take the output at K_n, before multiplication by the final b. It is
not the B image of the complete K_n with its later seeds retained.
L099's original supplied family has Q_n≤C(n+2)³, for a fixed encoding
constant C, including the source proof and complete occurrence package.

An affine ABP is an explicitly encoded finite acyclic directed graph
with N vertices, arbitrary designated source s and sink t, parallel
edges permitted, and labels c+Σ_z c_z z over these 2n generators with
coefficients in F₂. Its output is the sum of ordered accepting-path
products, including the empty path when s=t. Full binary length B_ABP
charges every vertex, edge, label, name, reference and framing record;
in particular B_ABP≥c_0 N for a fixed c_0>0. Implicit graphs and
circuit-valued labels are excluded. Equality means formal equality in
the free algebra, with all cancellations retained.

## Conclusion

Let d=n(n+1). The homogeneous degree-d component of S_n is its lowest
nonzero homogeneous component. Its coefficient matrix at cut n,

    M_(u,v)=[uv]S_n,   |u|=n, |v|=n²,

has rank exactly 2^(n−1) over F₂. Every affine ABP computing S_n thus
satisfies

    N≥2^(n−1),             B_ABP≥c_0 2^(n−1).             (2)

Consequently no fixed polynomial in L099's original Q_n bounds such
explicit graphs, even with arbitrary sharing, refactoring and cancellation.
This stops exact-output affine-ABP compression of the isolated contribution.

This is a local specialization of the known coefficient-rank method to
the assessed aggregate, not a claim of a new lower-bound method or
certified originality. Its separate step-392 informal critical audit
below finds no substantive defect. It is not a lower bound for the full extracted certificate,
alternative witnesses, Frege/SF/EF proofs, or SAT decision. General
occurrence normalization, exact fg transfer, short-proof availability,
an M-only bound and universal W₂ remain unresolved.

## Proof

**Coverage and standard input.** The unchanged pre-invocation EXPLORE
assessment `drafts/literature/2026-10-20-renaming-aggregate-seed-compression.md`
authorizes precisely this coefficient-cut test of (1). It inspected
Noam Nisan, *Lower Bounds for Non-Commutative Computation (Extended
Abstract)*, STOC 1991, pp.410–418,
[Theorem 1, §3, PDF p.5](https://www.csa.iisc.ac.in/~chandan/courses/arithmetic_circuits/notes/noncomm.pdf),
[DOI](https://doi.org/10.1145/103418.103462): the cut-rank characterization
for homogeneous linear-edge ABPs, including its factorization proof.
The original statement uses real coefficients. L033's audited proof
supplies the F₂ finite-constant-path version for two generators. Below
we give only its necessary 2n-generator and unequal-cut specialization,
so the real-field statement is not silently imported over F₂. No circuit
factorization or formula-to-ABP upper-bound theorem is needed.

L099 supplies (1), the isolated-contribution interpretation and the
original-Q bound. Its literal copy count alone is not a rank premise.
Attempts 020/032 remain distinct earlier stops. The inspected source
comparison contains no theorem deciding (1); novelty is not inferred
from that absence of an inspected match.

**1. Isolate the lowest homogeneous component with all parities.**
For each i, we prove that S_i has no terms below degree (i+1)n and
that its degree-(i+1)n component H_i is

    H_i = Σ_(U⊆[i]) W_i(U),
    W_i(U) = ∏_(j=0)^i a_(U∩{j+1,…,i}),                 (3)

where products are ordered by increasing j and the last set is empty.
All a_U still have length n, including when i<n. In particular there
are exactly 2^i distinct words in (3), each with coefficient one.

For i=0, p=a+a² has lowest component a, because n≥1. This is (3).
Suppose the claim holds at i−1. Expand (1) in the given factor order:

    S_i=ρ_i(S_(i−1))p+S_(i−1)p+S_(i−1)(ρ_i p)p.

The first two terms have no words below (i+1)n. The third has no
words below (i+2)n. Renaming preserves length, and p and ρ_i p each
have lowest degree n. Thus no higher-degree choices, including the
a² parts of either p, can contribute in degree (i+1)n. Exactly

    H_i=(ρ_i H_(i−1)+H_(i−1))a.                         (4)

In (3) at stage i−1, no block mask contains i. Therefore ρ_i toggles
the ith letter in every one of its i blocks and replaces every mask
V by V∪{i}. The first term of (4), followed by the new empty-mask
block a, gives exactly W_i(U) with i∈U. The second gives exactly
W_i(U) with i∉U. This accounts for every U⊆[i] once.

The first block of W_i(U) is a_U. Distinct U have distinct first
blocks, since the 2n original generators are distinct. Hence none of
these words coincide: their parity coefficients are one, not merely
nonzero individual contributions before addition. This proves (3),
its nonvanishing and the exact lowest-degree assertion by induction.
Fixed-length blocks have unique segmentation, so no alternative
block parsing can create an overlooked collision.

**2. Compute the cut rank exactly.** For V⊆{2,…,n}, put

    v_V=∏_(j=1)^n a_(V∩{j+1,…,n}).                    (5)

This is a word of length n². Its first block (j=1) is a_V, so these
2^(n−1) suffixes are distinct. By (3), the complete degree-d support
is precisely

    a_U v_(U\{1}),             U⊆[n],                 (6)

with coefficient one. In the rows a_V, V⊆{2,…,n}, and columns v_W
for the same index set, it follows that

    [a_V v_W]S_n = 1 if V=W, and 0 otherwise.           (7)

Indeed, total length d selects H_n; the first block fixes U=V in
(6), and the injective suffix map then forces W=V. Thus (7) is an
identity submatrix, proving rank at least 2^(n−1). Formula (6) also
shows there are only 2^(n−1) nonzero columns in the whole coefficient
matrix: each is indexed by some v_V. All other length-n² columns
are zero. Therefore rank is exactly 2^(n−1). Rows indexed by
a_V and a_(V∪{1}) coincide, which explains why the claimed rank is
not the literal context count 2^n. For n=1 there is one column v_∅=a;
H_1=(a_{1}+a)a and the selected 1-by-1 matrix is [1].

**3. Charge rank to the original affine graph.** This is L033's
audited constant-closure argument with a matrix for each letter z in
the finite alphabet. Topologically number the N vertices. Let C
contain the aggregate constant coefficients of all parallel edges,
and A_z their aggregate z coefficients, with all sums in F₂. These
are strictly upper triangular. Set

    K=I+C+⋯+C^(N−1),        G_z=A_z K.

For a word w=z_1⋯z_r, write G_w=G_(z_1)⋯G_(z_r), with G_∅=I.
Finite constant-path closure gives, for the graph's output f,

    [w]f=e_s K G_w e_t.                                 (8)

To verify applicability, expand each affine edge into its scalar and
single-letter choices. Every expanded path producing w has a unique
constant-only prefix, followed by r variable edges and their constant-only
suffix runs. Conversely these pieces concatenate to an actual path,
since every nonempty piece advances topologically. Summing their
products is exactly (8); path multiplicities and cancellations are
counted modulo two. The constant run after a cut letter belongs to
that letter's right-hand K, and is not counted again at the next
letter. This prevents multiple choices of a cut along one constant run.
The empty-word case also follows from K; arbitrary s,t and dead records
do not affect the argument.

For any chosen row words u of length n and column words v of length
n², equation (8) gives M=R T with

    R_(u,*)=e_s K G_u,          T_(*,v)=G_v e_t.

The factors have inner dimension N, independent of the two word lengths
and of the number of letters. Thus rank_F₂ M≤N on the original graph.
There is no loss from first enlarging it to a homogeneous graph, and
no assumption that f itself is homogeneous. Its length-d coefficients
are exactly those of its degree-d homogeneous component.

All 2n letter names and all their nonzero label coefficients were
already charged in B_ABP. The matrices here are finite proof objects,
not an implicit replacement for the output encoding. If explicitly
formed, there are 2n+1 N-by-N bit matrices, and their assembly and
finite closure are polynomial in the full graph input and n; coefficient
bits do not grow. No fixed-alphabet size bound from L033 is applied
unchanged to growing labels. The rank inequality itself loses no
alphabet factor. Applied to (7), it proves (2).

**4. Required threshold and limitations.** For fixed H>0 and exponent
r≥0, L099's unchanged Q_n bound gives

    B_ABP/(H Q_n^r)
      ≥ c_0 2^(n−1)/(H C^r(n+2)^(3r)) → ∞.

This meets the assessed superpolynomial original-input threshold,
rather than just a polynomial rank test at one cut. It rules out all
exact-output affine ABPs for S_n, not just a whole-seed copying rule.

Crucially, retaining later Z_i changes the object. L099's extraction
identity gives K_i(B)=p at every complete stage. The other seeds can
therefore cancel the difficult lowest component isolated here. A bound
on S_n does not bound that complete B image or the pre-B full witness.
It also does not show that any selected certificate must contain S_n
as a separately represented subgraph. The source CNFs retain their
easy alternative proofs. No full-certificate hardness, source-proof
normalization obstruction, general circuit lower bound or SAT consequence
is concluded. This is not a candidate resolution of P versus NP.

**Finite checks, not a substitute for the proof.** Reproduce with
`python3 scripts/renaming-aggregate/check_lowest_cut.py`.
The script expands the full recurrence over F₂ for n=1,2,3,4 in the
injective fixed-length block encoding, before selecting coefficients.
It checks complete equality of the lowest support with (3), absence
of lower degrees, suffix injectivity, every selected matrix entry and
binary elimination rank. Ranks are 1,2,4,8, equal to their required
2^(n−1) bounds; full supports have 14,100,710,5044 words, respectively.
All checks pass with no failures. Full finite polynomials, selected
matrices and check outcomes are retained in
`scripts/renaming-aggregate/lowest-cut-certificate.json`.
The all-size conclusion relies on §§1–4, not these four cases.

**Separate critical audit — 2026-10-20, step 392.** The pre-invocation
EXPLORE assessment
`drafts/literature/2026-10-20-renaming-aggregate-cut-critical-audit.md`
authorizes exactly this audit. Reuse its Nisan/Raz–Shpilka coverage and
L033's audited constant-closure method. The audit inspects §§1–4 above,
L099 §3 and its step-388 recurrence/input ledger, and the distinctions
recorded in Attempts 020/032/033. It finds no substantive defect; the
argument, hypotheses, bounds and direct mathematical inputs are unchanged.

1. **Receive the correct aggregate.** In L099 the seed Z_i has B image
   (1+p)(1+ρ_i p)p. With all seeds retained, substituting the received
   induction hypothesis K_(i−1)(B)=p gives
   (ρ_i p)p+p(1+ρ_i p)p+(1+p)(1+ρ_i p)p=p.
   Thus the complete K_i(B) is not the object bounded here. Setting the
   later seeds to zero first, and using the compatibility of renaming
   with B proved in L099, gives exactly (1). The final multiplier b is
   absent. The free generators here are the distinct source x_i,x'_i;
   no occurrence identification or Boolean quotient is used in the rank
   calculation. The initial seed's B image is exactly a+a².

2. **Degree and parity.** At stage i−1 all degrees are at least in,
   and the first two expanded terms of (1) start at (i+1)n. The third
   starts at (i+2)n, strictly higher because n≥1. A higher-degree
   component of S_(i−1) or of either p cannot enter the proposed lowest
   component. For U⊆[i−1], adjoining i to every old block mask is exactly
   the action of ρ_i, since no old mask contains i. Appending a therefore
   gives the i∈U terms in (3); the unrenamed terms give the complementary
   family. The first block records all of U, so no two terms within or
   between these families agree. This verifies the coefficient-one
   assertion after addition in F₂, not just the degrees of individual
   summands. It also proves that the proposed lowest component is
   nonzero for every stage, closing the induction without assuming it.

3. **Both exact-rank directions.** At i=n, removing the first block
   erases bit 1 and no other bit: the suffix's first block retains
   U∩{2,…,n}. Hence the suffix map is injective on subsets of {2,…,n},
   and the support is exactly (6). Fixing a row a_V with 1∉V determines
   U=V, so the selected columns give the entire identity matrix (7),
   including its zero off-diagonal entries. Conversely every nonzero
   entry of the full matrix lies in one of these 2^(n−1) columns.
   Higher-degree components cannot add entries, because each indexed
   concatenation has length n+n²=d. This supplies the upper rank bound
   as well as the lower one. In the endpoint case n=1 the two support
   words are x'_1 x_1 and x_1 x_1, with the same suffix x_1; the full
   matrix has rank one, agreeing with the selected [1].

4. **Original graph and constants.** Aggregating parallel edge
   coefficients uses distributivity before path parities are collected.
   A term in K A_(z_1) K ⋯ A_(z_r) K is a path with its selected
   letter edges and constant runs. Topological progress prevents any
   repeated vertex, and conversely the selected letters uniquely
   determine those runs in each expanded path. At a positive cut the
   complete constant run after its last selected letter is in R's last
   K; T starts with A for the next letter. There is exactly one boundary
   vertex for that path under this convention. An extra initial K in T
   would be unjustified and could double-count constant paths; none is
   present in (8) or the stated factorization. Thus the rank is bounded
   by the original N, not by a degree-normalized graph size. The proof
   applies to unequal lengths n and n² and any finite alphabet over F₂.
   It uses neither the real-rank theorem as an F₂ theorem nor a
   fixed-alphabet encoding bound. Dead vertices and arbitrary endpoints
   cause no exception. When s=t an acyclic graph has only its empty
   accepting path and cannot compute the positive-degree S_n; the
   coefficient formula still holds, as it does when there is no path.

5. **Full-input threshold and limits.** L099's audited family explicitly
   charges 4n diamond lines of O(n) symbols, O(log(n+2))-bit references,
   q=4n+6 occurrence names, two width-three testers and the entire
   q+q(q−1)/2-entry Boolean/commutator dictionary. Its original Q is
   O((n+2)² log(n+2)), hence at most C(n+2)³, before any witness or
   degree output is added. The 2n-letter alphabet of S_n is not a hidden
   constant-size premise. Explicit vertex records give B_ABP≥c_0 N.
   For every fixed H>0,r≥0 the logarithm of the displayed lower ratio
   in §4 grows as (n−1)log 2−3r log(n+2)+O(1), tending to infinity.
   Therefore it excludes every fixed polynomial in original Q. It says
   nothing about whether a complete witness must represent this isolated
   component separately; later-seed cancellation is explicitly present.

The existing finite checker was rerun without modification. All five
checks pass for each n=1,2,3,4, with actual/required ranks 1/1, 2/2,
4/4 and 8/8 and no failures. Its complete certificate is retained at
the path above. These executions check the finite recurrence, not the
all-size proof or the affine-graph factorization. No general graph
checker, verified implementation or formal proof is claimed.

This audit establishes a checked local input for route selection, not
a new mathematical bound or certified originality. Attempt 033's stop
is retained for this isolated output only. General normalization,
complete-certificate or alternative-witness hardness, exact fg transfer,
short-proof availability, M-only bounds, universal W₂ and unrestricted
SAT remain unresolved. L033 and L099 remain the only direct local
mathematical inputs, so the DAG row is unchanged.

## Mathlib

Full matching coverage for the aggregate coefficient formula, its
cut-rank value and finite-alphabet affine-DAG specialization is **not
checked**. No absence claim or formal verification is asserted. Nisan's
Theorem 1 is the named standard input; L033 supplies the audited local
constant-closure method. The separate informal audit above checks the
exact aggregate application and its original-Q comparison. Neither the
proof nor the audit is formally verified.
