# C047a — Uniform shifted embedded-quadratic equality

## Hypotheses

Use C001a/C012a's E=F_65537, F=F_(65537^28), with E identified
with the prime subfield of F, H=<g> of order 1024, g=19139, k=64,
and any integer m>=1. Let B_0,...,B_4 be precisely L047's outside
seven-sets, with actual E-labels in its auxiliary-column order:

```text
0: 3414,431,33622,1065,34155,59991,30525
1: 47705,45093,29441,4938,34155,59991,57044
2: 3414,22499,2130,4938,34155,32106,21079
3: 10048,32839,32984,1065,34155,32106,4893
4: 10048,22499,55315,30087,15161,32106,57044
```

Choose one common s in H and any 61-subset C' of H disjoint from
the union of sB_i. Put S_i'=C' union sB_i. Suppose P_i, 0<=i<=4,
are polynomial m-tuples over F, each row of strict degree less than 64,
and Y:H->F^m is one center such that P_i(x)=Y(x) for every x in S_i'.
Distinctness is not assumed. Zero differences and extra agreements are
permitted. No descent of the row coefficients to E is assumed.

## Conclusion

All five polynomial tuples are equal: P_0=P_1=P_2=P_3=P_4. Thus the
five selected 68-supports S_i' cannot belong to five pairwise distinct
messages at one center, for every allowed s,C',m and Y.

For each allowed s,C', the outside sets sB_i can nevertheless be included
in an embedded L030 quadratic family of size 137^3 independent in both
of its old local edge systems. This is incidence-only context: the
uniform equality prohibition supplies a further common-center restriction.

This is a REPRODUCTION specialization of assessed methods and L047's
audited finite input. The separate critical audit below retains this
extension. It gives no useful cardinality cap, compatible-subfamily bound,
other-embedding theorem, cross-core consistency or 67/68 safety. The
fixed-instance bracket remains 955<=t_star(m)<=957.

## Proof

**Sources and exact finite input.** The pre-invocation SPECIALIZE scope
is [the uniform-proof assessment](../drafts/literature/2026-10-11-embedded-quadratic-uniform-proof.md).
Alrabiah, Guruswami and Li, *Randomly punctured Reed–Solomon codes
achieve list-decoding capacity over linear-sized fields*,
[arXiv:2304.09445v3](https://arxiv.org/pdf/2304.09445v3), 26 July 2023,
Definition 2.5 and the complete proof of Lemma 2.7, printed pp. 7–8,
supply signed evaluation stars and last-message subtraction. Shangguan
and Tamo, *Combinatorial list-decoding of Reed–Solomon codes beyond the
Johnson radius*, [arXiv:1911.01502v1](https://arxiv.org/pdf/1911.01502v1),
4 November 2019, Lemma 4.3's common-root proof case, printed pp. 11–12,
supplies the common-root method. We use neither a random/generic rank
conclusion nor its decoding-radius conclusion. These methods require
the application below because our selected supports allow higher overlaps,
zero differences, arbitrary cores and extension-field tuple rows.

Import L047's complete incidence data, its signed 12-by-12 quadratic
matrix M over E, and its audited inverse U with UM=I_12. These finite
identities were separately checked in L047; they are not reaudited here.
In particular we import the matrix, rather than apply L047's fixed-core
equality conclusion to a different core. C040a is a method comparison for
a different quartic pattern, not an input theorem for these supports.

**Incidences and nonvacuity.** Multiplication by s is a bijection of H,
since H is a multiplicative subgroup and s is nonzero. Consequently,
for every nonempty set I of indices,

\[
 \bigcap_{i\in I}sB_i=s\bigl(\bigcap_{i\in I}B_i\bigr),\qquad
 \bigcap_{i\in I}S_i'=C'\cup s\bigl(\bigcap_{i\in I}B_i\bigr).
\]

The latter equality uses disjointness of C' from every shifted block.
Each S_i' therefore has 68 elements. All of L047's higher overlaps are
retained: its outside four-way intersection 0123 is {34155}, its outside
triple 234 is {32106}, and the corresponding shifted intersections are
{s*34155} and {s*32106}. The other subset intersections are transported
in the same way; no pair-only incidence is imposed. The common outside
intersection of all five remains empty, so the full common intersection
is precisely C'.

For every s the union of the shifted blocks has at most 35 points,
leaving at least 1024-35=989 points from which to choose a 61-core.
Thus the quantified cores exist. For every allowed core, taking all P_i
and Y equal to zero also shows that agreement realizations exist; the
conclusion concerns equality, not nonexistence of all realizations.

**Arbitrary-core division, including zero differences.** Fix a tuple
row a and write

\[
 G(X)=\prod_{c\in C'}(X-c),\qquad \deg G=61.
\]

For i=0,...,3, the difference D_i=P_{i,a}-P_{4,a} vanishes at each
point of C'. The distinct linear factors divide D_i jointly. Explicitly,
after dividing by any initial product of factors, evaluation at the next
root makes that product nonzero, forcing the remaining quotient to vanish
there; the factor theorem permits the next division. Induction gives
G dividing D_i. If D_i=0 take its quotient to be zero. Otherwise
deg D_i<=63, and degree additivity over the field F gives

\[
 D_i=G h_i,\qquad \deg h_i=\deg D_i-61\le2.
\]

Set h_4=0. At each point sx in a shifted outside block, G(sx) is
nonzero because sx is outside C'. If sx is incident with both indices
i,j, the shared center yields P_{i,a}(sx)=P_{j,a}(sx). Therefore

\[
 0=G(sx)(h_i(sx)-h_j(sx)),\qquad h_i(sx)=h_j(sx).
\]

This includes zero differences, any number of incident messages and any
additional agreement positions.

**All twelve transported signed rows.** Retain L047's recorded anchors
and row order. The complete row list below uses unshifted x; the new
evaluation point in each row is sx:

```text
x       anchor  other
1065       0      3
3414       0      2
4938       1      2
10048      3      4
22499      2      4
32106      2      3
32106      2      4
34155      0      1
34155      0      2
34155      0      3
57044      1      4
59991      0      1
```

Incidence transport preserves each incident index set and hence its least
index anchor. At the triple and quadruple overlap points the two or three
star rows are all retained; subtracting star equations gives every pair
equation there. Multiplication by s can reorder numerical representatives
of the labels, but we do not sort them again. The displayed order fixes
the correspondence with the imported M and U.

Write h_i(X)=c_i0+c_i1 X+c_i2 X^2 and let v be the twelve coefficients
of h_0,...,h_3, ordered by index and then degree. As in L047, a row with
anchor i and other j has +V(x) in block i and -V(x) in block j, where
V(x)=(1,x,x^2); the block for h_4=0 is omitted. Define over E

\[
 D_s=\operatorname{diag}(1,s,s^2,\;1,s,s^2,\;1,s,s^2,\;1,s,s^2).
\]

For each signed block V(sx)=V(x) diag(1,s,s^2). This checks every
displayed row, including repeated overlap labels and rows against index 4.
Thus the shifted matrix is exactly

\[
 M_s=M D_s,\qquad M_s v=0.
\]

Equivalently the coefficients of h_i(sX) are c_id s^d, which confirms
the substitution direction: the column scaling uses s, not s^(-1).

**Equality over F in each row.** All diagonal entries of D_s are
nonzero. The E->F embedding preserves the imported identity UM=I, so

\[
 (D_s^{-1}U)M_s=D_s^{-1}(UM)D_s=I_{12}
\]

holds over F. Multiplying M_s v=0 by this left inverse gives v=0.
Hence h_0=...=h_3=0 and P_{i,a}=P_{4,a} as polynomials for every i.
The argument applies independently to every row a=1,...,m, proving
equality of the polynomial tuples. It does not require a scalar projection
distinguishing messages, descent to E or a singularity converse.

**L030's incidence-only context.** Use its auxiliary set
Omega=(T times F_137) disjoint union four dummy points, of size 963,
and its quadratic graph family on T=(16,64,70,102,112,118,121).
On the union A of the five graphs q_i from L047 define the partial map

\[
 (t_j,y)\longmapsto s g^{61+137j+\operatorname{rep}(y)}.
\]

L047's injectivity on all 959 graph points implies injectivity on A;
multiplication by s preserves it. Its image is exactly the union of
sB_i, contained in H minus C'. Both Omega and H minus C' have size 963.
Choose any bijection between their remaining complements; these have
the same size 963-|A|. This extends the partial map to a full bijection
sigma:Omega -> H minus C'. L030 proves that every such image of its
137^3 quadratic graphs is independent in both old local edge systems,
by intersection preservation and absence of the triple-incidence
antecedent. This family contains the five sB_i.

No auxiliary-field operation or actual-label determinant is transported
by sigma. The rest of this embedding is arbitrary, and its independence
does not assert common-center realization. The equality obstruction
therefore adds a restriction beyond those edges without providing any
cardinality bound or altering C001a's boundary bracket.

**Separate critical audit (2026-10-11, step 146).** The unchanged
[SPECIALIZE audit assessment](../drafts/literature/2026-10-11-embedded-quadratic-uniform-critical-audit.md)
was approved before this invocation. The audit imports L047's previously
audited identity UM=I, its labeling of the five auxiliary graphs and
L030's incidence-only independence under every set bijection. It does
not rerun the finite search, elimination, determinant or inverse audit.
The cited AGL signed-star method and Shangguan–Tamo common-root proof
case are reused with the qualifications above; neither is invoked as a
theorem already proving the tuple equality conclusion.

First, C001a/C012a give the required degree cutoff, prime-subfield
embedding and subgroup order. For every s in H the shifted blocks remain
in H and retain all their incidences. Their union has at most 35 elements,
so disjoint 61-cores exist. Each support has size 61+7=68. L047's five
distinct auxiliary graphs give distinct outside blocks, and adding a
disjoint common core does not identify them. Neither the hypotheses nor
the proof assume that their associated messages are distinct.

For a fixed row, successive factor division is valid even if an
intermediate quotient is zero: the next root is distinct from previous
roots, so the value of the previously removed factor is nonzero. Thus
G divides every difference. The nonzero case has quotient degree at
most 63-61=2; the zero case has the zero quotient and a zero coefficient
triple. Since G(sx) is a product of nonzero differences sx-c in F,
cancellation at all shifted outside labels is valid for every allowed
core. Agreement at additional points imposes further conditions and
cannot invalidate any of these necessary equations.

Here is a direct audit of every row against the five displayed block
lists. In this table h_i is evaluated at sx, and h_4=0. All labels with
at least two incident blocks are included; singleton labels impose no
equality of two messages.

| Row | x | Complete incident indices | Required signed expression |
| --- | --- | --- | --- |
| 1 | 1065 | 0,3 | h_0-h_3 |
| 2 | 3414 | 0,2 | h_0-h_2 |
| 3 | 4938 | 1,2 | h_1-h_2 |
| 4 | 10048 | 3,4 | h_3 |
| 5 | 22499 | 2,4 | h_2 |
| 6 | 32106 | 2,3,4 | h_2-h_3 |
| 7 | 32106 | 2,3,4 | h_2 |
| 8 | 34155 | 0,1,2,3 | h_0-h_1 |
| 9 | 34155 | 0,1,2,3 | h_0-h_2 |
| 10 | 34155 | 0,1,2,3 | h_0-h_3 |
| 11 | 57044 | 1,4 | h_1 |
| 12 | 59991 | 0,1 | h_0-h_1 |

This checks the signs and the omitted index-4 blocks, including both
rows at the triple point and all three at the quadruple point. Shifting
changes neither the incident indices nor their least-index anchor.
The original row order is retained even when representatives of sx
are numerically reordered. For each coefficient degree d=0,1,2, each
signed matrix entry is either zero or plus/minus (sx)^d, which equals
its original entry times s^d. This verifies M_s=M D_s entry by entry
for the entire twelve-row matrix, without a rank-symmetry assumption.
Substitution h_i(sX) confirms the same direction of scaling.

The inverse must consequently be D_s^(-1)U on the left. The displayed
identity (D_s^(-1)U)(M D_s)=I follows by associativity and UM=I,
since s is nonzero. Its entries map into F through the fixed embedding.
Thus the kernel over F is zero, even for coefficient vectors outside
E^12. Applying this argument separately to each of the m rows proves
equality of the five polynomial tuples. No row need distinguish all
messages, and no scalar realization converse is used.

Finally, the incidence-context claim prescribes the exponential label
map only on the union A of the five auxiliary graphs. Its exponents
61+137j+rep(y), with 0<=j<=6 and 0<=rep(y)<=136, lie in disjoint
intervals within [61,1019]; exact order 1024 gives injectivity there.
Multiplication by s preserves injectivity. The image of A is exactly
the union of the shifted blocks and is disjoint from the chosen core.
Both full underlying sets have size 7*137+4=1024-61=963. After removing
A and its image their complement cardinalities agree, so a bijection
between the complements extends this partial map. This does not require
the same exponential formula on the other auxiliary points: its image
there might meet the new core. For the completed arbitrary bijection,
L030's proof of incidence-pattern avoidance applies to every graph in
its family. Distinct graphs remain distinct, so the family has exactly
137^3 members and contains the five shifted blocks. Independence refers
only to L030's old pair and determinant edge systems; it makes no claim
that all those members have one common RS center.

All quantified obligations survive; no repair or narrowing is needed.
The direct mathematical inputs remain C001a, C012a, L030 and L047;
C040a remains comparison only. The Mathlib qualifications below remain
accurate: supporting field/polynomial facts are sufficient here, while
full matching coverage is unchecked. This is independent verification
of the existing reproduction, not a new general theorem, cardinality
cap, or improvement of the 955–957 bracket. Useful cap strength,
compatible subfamilies, other embeddings and cross-core consistency
remain unresolved.

## Mathlib

Full matching uniform obstruction: **not checked**. The inspected
supporting declarations, retained in the source assessment, are
`Polynomial.eval_comp` and `comp_assoc` in
[Eval/Defs.lean, commit 6be3d352cec3ceabd28bf85266d28646e02f1975](https://github.com/leanprover-community/mathlib4/blob/6be3d352cec3ceabd28bf85266d28646e02f1975/Mathlib/Algebra/Polynomial/Eval/Defs.lean),
`Polynomial.comp_C_mul_X_coeff` and `comp_C_mul_X_eq_zero_iff` in
[Eval/Degree.lean, commit 9e6b3aac99b624d10c84653ab9c5357283b9b3b8](https://github.com/leanprover-community/mathlib4/blob/9e6b3aac99b624d10c84653ab9c5357283b9b3b8/Mathlib/Algebra/Polynomial/Eval/Degree.lean),
and `Polynomial.dvd_iff_isRoot` in
[Div.lean at that commit](https://github.com/leanprover-community/mathlib4/blob/9e6b3aac99b624d10c84653ab9c5357283b9b3b8/Mathlib/Algebra/Polynomial/Div.lean).
The scaling coefficient identity holds over a semiring; the zero
equivalence requires a non-zero-divisor multiplier, as satisfied by s
in our fields. The factor theorem is over a commutative ring; F meets
that hypothesis, and the division induction explicitly uses its field
property at the other distinct roots. These are supporting tools, not
a matching theorem for this tuple obstruction, local caps or safety.
