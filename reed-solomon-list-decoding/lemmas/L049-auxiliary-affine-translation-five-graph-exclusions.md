# L049 — Fixed-label five-graph exclusions under auxiliary affine translations

## Hypotheses

Use C012a's prime subfield E=F_65537 of F=F_(65537^28),
H=<g> of order 1024 with g=19139, k=64, and any integer m>=1.
Fix the original core C={g^e:0<=e<=60}. In the auxiliary field
F_137 use T=(16,64,70,102,112,118,121), in that order, and
exactly L047's five coefficient triples in constant/linear/quadratic order:

```text
q0=(33,27,3), q1=(106,120,2), q2=(0,0,0),
q3=(64,44,1), q4=(34,47,2).
```

For a,b in F_137 let q_i^(a,b)(Z)=q_i(Z)+aZ+b. For j=0,...,6
put y_ij=rep(q_i^(a,b)(t_j)), with rep in {0,...,136}, and define

\[
 B_i^{a,b}=\{g^{61+137j+y_{ij}}:0\le j\le6\},\qquad
 S_i^{a,b}=C\cup B_i^{a,b}.
\]

The reduction modulo 137 is performed before exponentiation in E.
This is the fixed set labeling; it is not a field embedding.
Suppose one received array Y:H->F^m and five tuples
P_i in (F[X]_<64)^m satisfy P_i(x)=Y(x) on S_i^(a,b).
Selected supports may have extra agreements. Distinctness is not assumed.

## Conclusion

For every one of the 137^2=18,769 ordered parameters (a,b), the complete
signed-star matrix defined below has rank 12 over E. Every realization
in the hypotheses has P_0=P_1=P_2=P_3=P_4 in every tuple row. Thus each
translated configuration is prohibited for five pairwise distinct
messages at one center, uniformly in m.

The translated outside sets still belong to L030's single fixed embedded
quadratic family, independent in its two old local edge systems.
This is a finite REPRODUCTION specialization of assessed source methods.
The initial exhaustive certificate and the separate independent critical
audit below both pass. No statement about a changed core, another labeling, common actual
multiplicative shifts, quantitative cap strength, cross-core consistency,
compatible subfamilies, or 67/68 safety is proved. The bracket remains
955<=t_star(m)<=957; this is no complete candidate resolution.

## Proof

**Imported method and scope.** Reuse the pre-invocation SPECIALIZE
[translation-family assessment](../drafts/literature/2026-10-11-embedded-quadratic-affine-translate-rank.md).
Alrabiah, Guruswami and Li, *Randomly punctured Reed–Solomon codes achieve
list-decoding capacity over linear-sized fields*,
[arXiv:2304.09445v3](https://arxiv.org/pdf/2304.09445v3), 26 July 2023,
Definition 2.5 and Lemma 2.7 with its complete proof, printed pp. 7–8,
provide signed evaluation stars and subtraction of the last message's
coefficient vector. Shangguan and Tamo, *Combinatorial list-decoding of
Reed–Solomon codes beyond the Johnson radius*,
[arXiv:1911.01502v1](https://arxiv.org/pdf/1911.01502v1), 4 November 2019,
Lemma 4.3's common-root proof case, printed pp. 11–12, supplies common-root
removal. Neither a generic/random-domain conclusion nor a characteristic-two
unsigned matrix is imported. The sources do not certify these translated
labels. The specialization therefore requires the finite identities and
the zero-difference, higher-overlap and tuple arguments below.

L047 supplies the fixed polynomial data and audited unshifted matrix.
C047a is a comparison of proof methods only: its common-multiplier
coefficient identity is not used for these auxiliary translations.

**Complete incidence reconstruction.** C012a's exact order calculation
g^1024=1, g^512=-1 makes the powers g^0,...,g^1023 distinct.
For each j the label exponents lie in [61+137j,197+137j]. These seven
intervals are disjoint and contained in [61,1019]. Hence the label map
on T times F_137 is injective and disjoint from C. Each support has 68
points. Adding the same a*t_j+b to all five graph values preserves
every equality and inequality at column j; the labeling preserves
exactly these incidences. The five translated graphs are distinct,
because their polynomial differences are the original nonzero quadratics.

For every nonempty subset I of {0,...,4}, the full support intersection is

\[
 \bigcap_{i\in I}S_i^{a,b}
 =C\cup\{g^{61+137j+y_{i_0j}}:
              y_{ij}=y_{i_0j}\ \hbox{for every }i\in I\},
 \qquad i_0\in I.
\]

The certificate reconstructs all 31 such intersections independently by
actual set intersections and auxiliary-coordinate equality, and checks
their agreement. It retains empty outside intersections as well as the
four-way overlap 0123 and triple overlap 234. The full common intersection
of all five is exactly C, since its outside part is empty.

Every translated polynomial has degree at most two on L030's unchanged T.
Extend the fixed injection by mapping L030's four dummy points to
g^1020,...,g^1023. This is a bijection onto H minus C, so L030's
incidence-only independence applies to the entire quadratic family and
its five translated members. This uses no actual-label rank symmetry.

**Definition and exhaustive exact rank certificate.** At each actual
outside label x in the union of the five B_i^(a,b), form the complete
incident set I_x. Choose min(I_x) as anchor and make one signed equality
row with each other index in increasing order. Sort points by their
integer representatives in E. For anchor i and other index l the row is

\[
 M_{a,b}[(x,i,l),(u,d)]
   =(\mathbf1_{u=i}-\mathbf1_{u=l})x^d,
       \quad u=0,1,2,3,\ d=0,1,2.
\]

The index-4 coefficient block is omitted. The complete incident sets,
including the higher intersections, give exactly twelve rows for each
parameter. Thus M_(a,b) is a 12-by-12 matrix over E. Twelve is also the
required rank, not an estimated threshold.

Run `python3 scripts/finite-support/embedded_quadratic_affine_translations.py`
from this notebook. The summary is
`scripts/finite-support/embedded-quadratic-affine-translations/summary.json`.
The 137 complete certificate files are `a-000.json` through `a-136.json`
in that directory. File a contains the 137 cases b=0,...,136 in order,
with each parameter, translated coefficients, all auxiliary values,
exponents, actual labels, full supports, all subset intersections,
complete incident stars, matrix, RREF, transformation, pivots, determinant
residue, complete row operations and verification flags. Full intersections
are stored without repeated core arrays: the file's shared `core` union
the case's `subset_intersections.outside` is each full intersection.
The summary records every file's hash and the original L047 certificate hash.

The calculation enumerates a=0,...,136 and b=0,...,136 with no skips and
no early success stop. Exact modular Gauss–Jordan elimination uses the
first nonzero available row in each coefficient column, records any swap,
scales by the nonzero pivot's inverse, and subtracts its appropriate
multiple from every other row. The transformation starts at I_12 and
receives the same operations. Every recorded operation is then replayed
on a fresh copy of M_(a,b) and I_12. The replay checks the complete
transformation U_(a,b), reduced matrix R_(a,b), and identity
U_(a,b)M_(a,b)=R_(a,b). All pivots, leading entries and any zero rows are
checked against the RREF definition. The full-rank branch additionally
checks every entry of both inverse identities:

\[
 U_{a,b}M_{a,b}=M_{a,b}U_{a,b}=I_{12}.
\]

For all 18,769 parameters these identities pass and R_(a,b)=I_12.
In total all 2,119,867 recorded invertible operations are replayed.
The full rank distribution is {12:18769}; the singular-parameter list
and failures list are both empty. Had any singular case occurred, the
script would save it separately with a nonzero free-variable kernel
vector and check every original row equation; no singular case is omitted.

The (0,0) case agrees entry by entry with L047's audited canonical
matrix, stars and inverse. Independent integer Bareiss elimination of
that matrix gives
det=-49740849785522550165823979466653588692992014892312,
with residue 26669, agreeing with the modular operation factors. The
complete integer trace is retained in the summary. As another explicitly
inspected certificate, (136,136) has determinant residue 22612 and all
twelve pivots. These inspected cases are illustrations: the rank conclusion
uses all complete identities, not samples or JSON previews.

The checker imports only the existing exact `rref`, matrix-product and
integer-determinant helper functions from the old script. Its search is
never invoked. This producer therefore is not an independent
critical audit of those helpers. The separate review below independently
reconstructs its saved evidence and checks the logical specialization.

**Tuple equality from the fixed-core equations.** Fix any tuple row r.
Put G_C(X)=product_(c in C)(X-c), of degree 61. For i=0,...,3 the
difference P_i,r-P_4,r vanishes on C. Inductively divide by its distinct
linear factors: at the next root c, the previously removed product is
nonzero at c, so the remaining quotient vanishes there and the factor
theorem permits another division. Thus

\[
 P_{i,r}-P_{4,r}=G_C h_{i,r},\qquad \deg h_{i,r}\le2,
       \quad h_{4,r}=0.
\]

If the difference is zero take h_i,r=0. Otherwise its degree is at most
63 and degree additivity gives the stated quotient bound. All reasoning
is in F[X]; there is no descent assumption on message coefficients.

For x outside C, every factor in G_C(x) is nonzero in F. Agreement at
the one center gives P_i,r(x)=P_l,r(x) for any two incident indices,
hence h_i,r(x)=h_l,r(x). The complete signed stars give all these
necessary equations, including higher overlaps. Additional agreement
positions do not remove any equation. Let v_r in F^12 contain the
coefficients of h_0,r,...,h_3,r in the prescribed order. Then
M_(a,b)v_r=0. The prime-subfield embedding E->F preserves
U_(a,b)M_(a,b)=I, so v_r=0. Every tuple row therefore has
P_i,r=P_4,r for all i, proving the equality conclusion for every m.
There is no assumption that one scalar row distinguishes all five tuples.

**Separate independent critical audit (2026-10-11, step 154).** The
pre-existing SPECIALIZE
[audit assessment](../drafts/literature/2026-10-11-auxiliary-affine-translation-critical-audit.md)
covers precisely these parameters, fixed core and tuple conclusion.
It reuses the primary statements cited above; no additional generic-rank
or scalar-distinctness theorem is assumed. Run
`python3 scripts/finite-support/audit_auxiliary_affine_translations.py`.
The full audit report is
`scripts/finite-support/auxiliary-affine-translation-audit-results.json`.
It records the producer-summary and verifier hashes, every shard hash,
every parameter's independent elimination pivots and determinant,
operation counts, check counts and failures. The complete original
arrays and operation lists remain in the 137 unchanged input shards.

The verifier imports no producer or original elimination helper. It
constructs subgroup powers by successive multiplication, checks the two
primes and generator order, and checks the whole graph/dummy-point
bijection. It evaluates the five translated polynomials in Horner form
modulo 137 before label lookup. It reconstructs all supports and all
31 full intersections per parameter directly, separately comparing
column equality. It constructs incident stars from the auxiliary column
partitions, sorts by actual label, builds all five signed coefficient
blocks, then removes the last block. Thus both the higher intersections
and the signs/omitted block are checked independently of saved matrix
entries. All coefficients, values, exponents, labels, supports,
intersections, stars and matrices match the saved arrays.

For each case it replays every saved invertible operation on the augmented
matrix [M | I]. It checks the complete saved RREF, transformation, pivot
order, normalized pivot columns and zero-row placement; then checks all
entries of UM=R, UM=I and MU=I. Every scale is nonzero, and all swap and
subtraction indices are valid and distinct. These identities alone
certify rank 12 without relying on the rank algorithm. Independently,
the verifier transposes M, reverses both coordinate orders, chooses the
last available nonzero pivot, and eliminates only below each pivot.
Transpose preserves determinant, and the two reversals have cancelling
signs. Each row subtraction preserves determinant; swap signs and the
nonzero diagonal pivots therefore give the original determinant. The
pivot count supplies an independent rank. This forward column method
agrees with every saved rank and every operation-derived determinant;
it does not reuse the producer's first-pivot Gauss–Jordan method.

All 137 shards and their ordered parameter coordinates are checked against
the full lexicographic product, including filename coverage and SHA-256
hashes. All 18,769 cases have actual rank 12, equal to required rank 12.
All 581,839 full intersections and 2,119,867 operations pass, with
9,606,618 checks and zero failures. The rank distribution is exactly
{12:18769}, with no singular parameters. No saved Boolean substitutes
for a computation. The (0,0) matrix, stars and inverse agree with L047's
original certificate of SHA-256
`40157ba7440ef639ec238405c7c25f5b03ec1b07b6d5d69b10abb2974a985b49`.
Every one of the eleven saved integer Bareiss states and all 506 exact
divisions are checked. A separate rational forward elimination of the
transposed, reversed base matrix, again choosing last available pivots,
gives exactly the displayed integer determinant and residue 26669.
The final parameter independently has determinant residue 22612.
The two displayed cases illustrate the evidence; the conclusion uses
complete verification of every parameter, not sampling or previews.

The critical logical review also retains the full necessity argument.
The supports lie in H, each contains exactly the same 61 distinct core
points, and every outside label avoids that core. The difference in
each tuple row is divisible by its 61 distinct linear factors. The zero
difference gives the zero quotient; a nonzero difference has degree at
most 63 and quotient degree at most two. Outside the core its removed
factor is nonzero, so agreement with the one common center imposes all
incident equalities. Stars span these equalities even at triple and
four-way overlaps, and selected supports with extra agreements retain
every necessary row. Subtracting row-polynomial P_4 makes precisely its
coefficient block zero. The verified left inverse over E remains valid
over F, forcing the other twelve coefficients to vanish in each tuple
row separately. No coefficient descent or common distinguishing scalar
row is required. L030's already audited general incidence theorem is
imported through the completed set bijection, not reaudited here; no
field operations or ranks are transported by that bijection.

The audit retains the existing REPRODUCTION input, without a new theorem,
novelty claim, or improvement of the safety bracket. Its direct mathematical
inputs remain C012a, L030 and L047. Changed cores and actual common shifts
remain outside this result; singularity sufficiency, cap strength,
compatible RS subfamilies and cross-core consistency remain unresolved.

**Qualifications and retained stops.** The intermediate exclusions could
be inputs to a later stronger labeled support model. No cardinality
bound for that model was tested, and no all-core or simultaneous-translation
transport is proved here. L048 and ATTEMPTS/021,031 still stop their
precise earlier restrictions. An equality exclusion within a large local
independent family is not an unsafe list or a proof of safety. The result
is local progress by reproducing assessed methods, without any claim of
progress beyond the sources' general framework or of mathematical novelty.

## Mathlib

Full matching translation-family rank or tuple obstruction: **not checked**.
The retained inspected support is `Polynomial.dvd_iff_isRoot` in
[Div.lean, commit 9e6b3aac99b624d10c84653ab9c5357283b9b3b8](https://github.com/leanprover-community/mathlib4/blob/9e6b3aac99b624d10c84653ab9c5357283b9b3b8/Mathlib/Algebra/Polynomial/Div.lean).
Its commutative-ring factor theorem applies in F; induction here also uses
the field property and distinct roots. C047a's inspected polynomial
composition/scaling declarations do not certify these auxiliary
translations and are not used. Matrix and finite-field support coverage
for the exhaustive family has not been separately checked. Unknown full
coverage is not evidence of absence.
