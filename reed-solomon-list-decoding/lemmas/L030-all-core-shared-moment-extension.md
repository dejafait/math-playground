# L030 — An all-core shared moment extension of the prescribed lift

## Hypotheses

Use L027's actual core C, its 963-point complement X=H minus C,
vertices V_C consisting of all seven-subsets of X, pair graph G_C
and determinant hypergraph J_C. Thus pair edges have intersection
at least three; every J_C edge has empty triple intersection and all
three pair intersections of size two. Retain the actual field labels
and all determinant-zero nonedges. Fix precisely L028's f,F:

\[
 L=137^3=2571353,\quad v=\binom{963}{7},\quad \rho=L/v,
 \quad N_i=\binom7i\binom{956}{7-i},
 \quad(d_0,d_1,d_2)=(2442832,125664,2856).
\]

Here f_A=F_AA=rho, and for distinct A,B, F_AB=rho*d_i/N_i
when |A intersect B|=i<=2 and F_AB=0 otherwise. The auxiliary
field F_137 used below has no asserted relation to the actual field.

## Conclusion

For every actual C there is one finite rational probability distribution
on families independent in both G_C and J_C whose first and second
indicator moments are exactly f,F. Consequently the saved degree-four
diagnostic has an extension: y_empty=1, y_A=f_A, y_AB=F_AB, every
edge-containing y_S is zero for |S|<=4, and the single matrix

\[
 M_{I,J}=y_{I\cup J}\quad (|I|,|J|\le2)
\]

is PSD. No nonnegativity or additional conditioned matrices are assumed.
The construction in fact supplies moments of all orders.

Every family in this distribution has size 2571353. Thus this diagnostic
cannot exclude L028's witness. Even the exact maximum cardinality of
families independent in these two local edge systems is at least that
large on every core, above L027's sufficient uniform cap 1532495.
This stops strengthening based solely on these same local independent
sets as a way to certify that cap. Additional RS restrictions, compatibility
across different cores, and common-center realization are not addressed.
There is no unsafe-list conclusion and no change to 955<=t_star(m)<=957.

## Proof

**Assessed scope and source use.** The prior EXPLORE assessment is
[the shared-moment comparison](../drafts/literature/2026-10-06-shared-degree-four-moment-extension.md).
It explicitly permits an exact all-core construction for this fixed
assignment. The finite-independence-system framework is imported from
Gouveia, Parrilo and Thomas, *Theta Bodies for Polynomial Ideals*,
SIAM J. Optim. 20(4) (2010), 2097–2118, DOI 10.1137/090746525,
[arXiv:0809.3480v3](https://arxiv.org/pdf/0809.3480v3), Remark 3.6,
printed p. 16, with its Boolean qualification in Proposition 2.18,
pp. 10–11. Hypotheses and version details are in
[the source record](../foundations/08-boolean-moment-source.md).
No general hierarchy or representation theorem is reproved or inferred.
The difference supplied here is a concrete representing distribution
for the already prescribed f,F. The elementary average-of-squares
calculation below verifies this certificate, rather than asserting that
arbitrary feasible order-two moments have a representing distribution.

**An exact seven-point certificate.** In F_137 take

\[
 T=\{16,64,70,102,112,118,121\}.
\]

For three disjoint unordered pairs (a_j,b_j) of T, form the columns
(a_j b_j,-a_j-b_j,1)^t, the coefficient vectors of the monic
root quadratics (Z-a_j)(Z-b_j). Their determinant is nonzero.
The following table records all 105 residues modulo 137. For each
omitted point, sort the remaining six increasingly. Generate matchings
recursively: pair the smallest remaining point with each later point
in increasing order, and recurse on the remaining sorted points.
This also orders the three columns. There are 5*3*1=15 matchings
per omission and seven omissions, exhausting all possibilities.

| Omitted point | Determinants in the specified matching order |
| --- | --- |
| 16 | 57,90,10,2,124,31,39,78,114,57,111,129,21,67,49 |
| 64 | 30,134,84,88,118,42,7,45,34,4,12,4,15,88,91 |
| 70 | 95,36,135,44,17,68,10,32,19,61,110,46,74,59,8 |
| 102 | 55,1,87,83,135,62,132,61,48,130,7,133,6,80,82 |
| 112 | 50,43,11,125,81,35,71,129,70,20,122,114,79,31,82 |
| 118 | 94,4,45,112,16,15,63,11,108,14,58,67,54,59,108 |
| 121 | 134,63,136,5,73,118,80,55,74,77,121,6,58,76,79 |

For direct reproduction, if s_j=a_j+b_j and p_j=a_j*b_j, each
entry is the residue of

\[
 p_1(s_3-s_2)+p_2(s_1-s_3)+p_3(s_2-s_1).
\]

The script below checks this cofactor expansion against an independent
six-term permutation expansion for every matching. All residues lie
in {1,...,136}, so all these triples of root quadratics are linearly
independent. Only this finite calculation is needed; no genericity of
T or the actual subgroup labels is assumed.

**The packing avoids the entire hyperedge incidence pattern.** Replace
L028's auxiliary evaluation set {0,...,6} by T. On

\[
 \Omega=(T\times\mathbb F_{137})\sqcup D_0,\qquad |D_0|=4,
\]

take P_T={B_p:deg p<=2}, where B_p={(x,p(x)):x in T}, including
p=0. L028's polynomial root argument gives exactly 137^3 distinct
seven-subsets and intersection at most two for distinct blocks.

Suppose distinct p,q,r yielded three blocks having pair intersections
of size two and empty triple intersection. Let U_pq be the two
evaluation points where p=q, and similarly define U_qr,U_rp.
These are two-element subsets of T. They are pairwise disjoint:
if an evaluation point belonged to any two, all three polynomial
values at that point would coincide, giving an actual point of the
triple intersection. Thus the three U's are one of the 105 matchings
just checked.

Since p-q is nonzero of degree at most two and vanishes at the two
distinct elements of U_pq, it is a nonzero scalar multiple of their
monic root quadratic. The same holds for q-r and r-p. But

\[
 (p-q)+(q-r)+(r-p)=0
\]

is then a linear relation with all three coefficients nonzero among
the three root quadratics. This contradicts their nonsingular
coefficient matrix. Hence this incidence pattern never occurs in P_T.
This argument covers all distinct polynomial triples, without enumerating
them or assuming that pairwise distinctness implies a nonempty or empty
triple intersection. Triples with a nonempty triple intersection are
irrelevant to J_C's edge condition.

For every bijection sigma:Omega -> X, the image family sigma(P_T)
has the same intersections. It is therefore independent in G_C and
avoids every J_C edge before its determinant is evaluated. This
establishes independence for every actual labeling and every core.
It does not assert that sigma preserves field operations or labeled
determinants. In particular, no determinant-zero nonedge has been
silently made an edge.

**The pair moments are exactly the old ones.** For a fixed p, translation
q -> q-p is a bijection on the degree-at-most-two polynomials. At any
two distinct elements of T, exactly 136 nonzero polynomials vanish,
each a nonzero multiple of the corresponding root quadratic, with
no other root in T. Hence d_2=21*136=2856. At any one point there
are 137^2-1 nonzero polynomials vanishing: evaluation is a surjective
linear map from a three-dimensional vector space, with two-dimensional
kernel. Counting incidences with the seven possible roots gives

\[
 d_1=7(137^2-1)-2d_2=125664,\qquad
 d_0=137^3-1-d_1-d_2=2442832.
\]

Thus the block size, number of blocks and all ordered pair counts
are unchanged from L028. This verifies why changing T preserves the
prescribed lower moments; invariance is not inferred from the new
triple-avoidance property.

Choose sigma uniformly among all 963! bijections, and let z_sigma
be the indicator of sigma(P_T). A fixed seven-subset A has probability
L/v=rho of being selected. On ordered distinct pairs with intersection
size i, the full permutation action on the underlying point set is
transitive, with v*N_i pairs. Each image family has L*d_i such ordered
pairs for i<=2 and none for i>=3. Consequently

\[
 \mathbb E z_A=\rho,\qquad
 \mathbb E z_Az_B=\rho d_i/N_i\ (A\ne B,\ i\le2),
 \qquad \mathbb E z_Az_B=0\ (A\ne B,\ i\ge3).
\]

The diagonal is E z_A^2=E z_A=rho. These are exactly L028's f,F.
The permutation average is used to compute the moments; feasibility
holds separately for every image family by the preceding argument,
so no actual-label symmetry is required.

**One shared extension, including zero rows.** For every subset S
of V_C define

\[
 y_S=\frac1{963!}\sum_\sigma\prod_{A\in S}z_\sigma(A).
\]

The empty product is one. This finite formula specifies each required
third and fourth moment exactly and consistently, as well as the
already verified first and second moments. If S contains a G_C edge
or a J_C edge, every summand vanishes; hence y_S=0. This verifies
all required triple and quadruple zeros directly, including supersets
of a forbidden triple. No graph-only zero-propagation theorem is
used for the cubic constraints.

For any real vector (u_I) indexed by subsets of size at most two,
Booleanity of z_sigma gives

\[
 \sum_{I,J}u_Iu_J y_{I\cup J}
 =\frac1{963!}\sum_\sigma
   \left(\sum_Iu_I\prod_{A\in I}z_\sigma(A)\right)^2\ge0.
\]

Thus the single shared matrix is PSD. An index I containing a pair
edge has identically zero product and an explicitly zero matrix row.
No division, invertibility, deletion of singular rows or completion
from separately chosen link matrices is needed. The same expression
with larger index sets proves the claimed higher-order extension.
Nonnegative moments are a consequence of this distribution, not an
extra condition imposed on the diagnostic.

Finally every sigma(P_T) has L vertices. This gives a true independent
family of size L in the local mixed edge system, and its expectation
has sum f_A=L. L027's threshold comparison therefore fails even if
one replaces its relaxed local maxima by the exact independence
numbers: each is at least 2571353>1532495, and its all-core sum is
at least binomial(1024,61)*2571353. L027's strength test excludes this
as a sufficient certificate. This does not say that these independent
families can arise from actual lists, or that the choices across all
cores can be assembled from one support family or received word.

**Verification and limits.** Run
`python3 scripts/finite-support/shared_degree_four.py`.
It saves the full certificate, including every matching with its pairs,
in `scripts/finite-support/shared-degree-four-results.json`.
The bounded search uses seed 137007 and at most 1000 candidates;
the fourth succeeds. The original {0,...,6} has three zero determinants,
so the replacement, rather than an unchecked use of the old packing,
is essential to this proof. All 105 determinant residues were inspected.
All nine arithmetic checks pass, and enumeration of all monic
polynomials of degrees zero, one and two verifies the unchanged
neighbor counts. The symbolic proof supplies all-core feasibility
and PSD; no numerical eigenvalue or finite principal-subsystem pass
is offered as a substitute. No complete challenge solution is claimed.

**Independent critical audit, 2026-10-07.** Run
`python3 scripts/finite-support/audit_shared_degree_four.py`.
Its complete certificate is
`scripts/finite-support/shared-degree-four-audit-results.json`.
The audit does not import the construction script. It selects unordered
triples from all 21 evaluation pairs, retaining exactly those with six
distinct endpoints, and computes their determinants by modular Gaussian
elimination with pivot products and row-swap signs. The resulting 105
distinct matchings exhaust the required set. Every residue agrees with
both the complete original certificate and the canonical table above;
all are nonzero. This checks completeness as well as arithmetic, rather
than trusting the original nonzero flag or its determinant expansions.

Independently enumerating all 137^3 coefficient triples (including zero,
without normalizing by scalar multiples) gives the exact root-count
histogram, indexed by zero through seven evaluation roots,

\[
 (2442832,125664,2856,0,0,0,0,1).
\]

The last entry is precisely the zero polynomial. The other entries
verify every prescribed neighbor count and agree with the saved monic
enumeration after multiplication by 136. The audit recomputes v, rho,
all three N_i and F_i as exact fractions, checks the ordered-pair
identities v N_i F_i=L d_i and the diagonal-inclusive row sum L rho,
and independently recomputes L027's strict adjacent-cap threshold:
N*1532495<D(M+1)<=N*1532496 and N*L>=D(M+1).
All 22 checks pass; complete selected determinant, histogram, moment,
threshold and check fields were inspected, with no failures.

The symbolic critical review separately checks that belonging to any two
evaluation-root pairs forces equality of all three values at that point.
Thus the empty triple intersection gives disjoint pairs, and the cyclic
polynomial-difference identity contradicts the verified nonsingularity.
This forbids the incidence pattern itself, so every relabeling remains
independent irrespective of actual labels or singular determinant
nonedges. Ordered-pair transitivity is used only to calculate moments.
The finite indicator distribution, Boolean union identity and explicit
zero products establish PSD and zero rows without normalization or
separately chosen link measures. No gap was found in these implications.

The audited conclusion is restricted to each core separately. Exact
local independence numbers are at least L on every core, and substituting
those numbers into L027's sum cannot meet its threshold. The audit does
not construct a distribution on global 68-support packings, impose
cross-core moment consistency, realize an RS list, or decide either
remaining agreement threshold. It validates this local obstruction;
it supplies no progress beyond the assessed sources' general moment
framework and makes no originality claim for the finite construction.

## Mathlib

Full matching prescribed-moment construction: **not checked**.
Supporting polynomial root, finite-field, determinant, finite averaging
and PSD coverage: **not checked**. Unknown availability is not evidence
of absence. The finite-independence-system framework is known and
imported by the precise citation above; novelty of this particular
certificate beyond the assessed sources is not established.
