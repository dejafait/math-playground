# L074 — Full seven-incidence algebra from the quotient fibers

## Hypotheses

Use L067's audited entire nonzero seven-torsion algebra A for
E/Q: y²+y=x³+x²−2x. In its rational short coordinates,

\[
\mathcal E:Y^2=c(X)=X^3-3024X+46224,
\qquad X=36x+12,\quad Y=216y+108.
\]

Use L070's entire direction field D=Q[Z]/h, of degree eight, and
L071's full relative kernel cubic q(X) over D and actual quotient

\[
\Phi:\mathcal E_D\longrightarrow\mathcal E',\qquad
\Phi(X,Y)=\left(N(X)/q(X)^2,\,YM(X)/q(X)^3\right),
\qquad M=N'q-2Nq'.
\]

Use L072's specified affine-line identification and conventions, and
L073's explicit actual dual with both compositions [7]. Write

\[
B=D[T,V]/(k(T),V^2-c'(T)),\qquad c'(T)=T^3+AT+B_0,
\]

for L073's entire nonidentity dual-kernel algebra, rank six over D
and 48 over Q. The letter B₀ here denotes the target curve's constant
coefficient, not its coordinate algebra. No chosen direction embedding,
selected factor, rational kernel generator or seventh root of unity
is assumed. No residual-image, L026, rank, analytic-order or Selmer
hypothesis is used. L069 and all stopped incidence columns are excluded.

All coefficients and map columns for this fixed construction are in
`scripts/seven-torsion/incidence-269/`. The producer is the fresh copy
of the unexecuted step-268 producer with only its extra closing brace
removed. That failed original and ATTEMPTS/035--039 remain unchanged.
Construction, complete independent replay and the separate fixed
critical audit below pass.

## Conclusion

Put F(X)=N(X)−Tq(X)² in B[X]. There is an explicit finite etale algebra

\[
I=B[X]/(F(X))
\]

with global B-basis (1,X,…,X⁶). Its ordered full rational basis is
ZʲTⁱVᵉXʳ, j fastest, 0≤j<8, 0≤i<3, 0≤e<2, 0≤r<7.
Thus it has rank seven over all of B and dimension 336 over Q.
There is a Galois-equivariant identification of its geometric points
with the entire incidence set

\[
\{(P,H):P\in\mathcal E[7]\setminus\{O\},\quad
 H\text{ an affine line missing zero},\quad P\in H\}.
\]

Both projection pullbacks are explicit and injective. The line-algebra
map B→I is inclusion of the constant-X part. The point-algebra map
A→I sends the short coordinates to

\[
X\longmapsto X,\qquad Y\longmapsto V\,y_f,
\qquad y_f=q^3M^{-1}\in (D[T]/k)[X]/F.
\]

The original coordinates map to (X−12)/36 and Vy_f/216−1/2.
The complete 336-coordinate columns of both maps, both L067 point
bases, and the forward/inverse rational basis transports are retained
and independently verified. Full-domain q, M and F' inverse witnesses
are supplied. No fieldness of B or I is asserted.

This is a fixed specialization of known quotient/fiber and descent
constructions, not progress beyond those sources. It supplies a possible
input for a later rank-seven fiber norm. No norm, descent functions,
complete units/classes, local identifications or upper bounds, Selmer
containment, other L026 premises, successful localization, rational
Kummer membership, divisible-Sha removal or arbitrary-curve complex-order/
rank comparison is supplied. It is not a BSD candidate.

## Proof

**Imported constructions and applicability.** Reuse the ready SPECIALIZE
assessment `drafts/literature/2026-10-17-quotient-fiber-incidence-construction.md`.
Schaefer–Stoll, *How to do a p-descent on an elliptic curve*, author long
version dated 13 June 2001,
[definition of B following Lemma 7.5, printed p.16, and Proposition 7.10 with the preceding incidence paragraph and following matrix paragraph, p.19](https://mathe2.uni-bayreuth.de/stoll/papers/p-descent-long.pdf),
defines the full line/incidence sets and both projection pullbacks.
The base field Q and odd prime seven meet its construction hypotheses;
no maximal Galois-image assumption is needed for these algebras/maps.
No cohomological characterization or norm calculation is imported as
already verified for this instance.

Sutherland, MIT 18.783 Fall 2025,
[Lecture 5, Theorem 5.11 and its quotient/coset proof sketch, pp.5–6](https://math.mit.edu/classes/18.783/2025/LectureNotes5.pdf),
and [Lecture 6, Theorem 6.7 prime-degree Case 1, pp.3–4](https://math.mit.edu/classes/18.783/2025/LectureNotes6.pdf),
supply quotient fibers and the prime-to-characteristic dual compositions.
L071 and L073 are the audited actual degree-seven isogenies in
characteristic zero, and L072 already gives the specified line bijection.
We use these inputs, rather than reprove quotient existence or duality.
The generic choices in Lecture 5 Theorem 5.8, pp.3–4, do not establish
all specialized fibers here; complete unit and inverse-image checks do.

[Stacks 26.17, Definition 26.17.1, Lemmas 26.17.2–3 and Definition 26.17.7, tag 01JO](https://stacks.math.columbia.edu/tag/01JO),
supplies the scheme-theoretic inverse image and affine tensor-product
construction. [Stacks Definition 10.144.1 and Lemma 10.144.2, tags 00UB/00UC](https://stacks.math.columbia.edu/tag/00UC)
supply the monic/invertible-derivative etale criterion; base change and
composition preserve etaleness by
[Proposition 59.26.2, tag 03PA](https://stacks.math.columbia.edu/tag/03PA).
Finally [Lemma 58.2.2, tag 03QR](https://stacks.math.columbia.edu/tag/03QR)
gives finite-etale descent from the complete Galois set. These cited
results apply to the explicit full algebras; a dimension comparison is
not used to establish the incidence identification.

**Whole presentation and inverses.** Let L=D[T]/k and let E₀=L[X]/F.
Both q and N are monic of degrees three and seven, respectively, by
L071. Thus F is monic of degree seven, even at every specialized T.
No condition T≠0 enters. Successive monic division by h, k, F and
V²−c' gives unique normal forms; reordering V and X gives exactly
the displayed 336-element basis and seven-element B-basis. The concrete
flattening map places a coefficient of ZʲTⁱVᵉXʳ at r·48+e·24+i·8+j.
Its inverse groups those entries and performs the monic normal forms.
The independent replay checks both directions on all 336 basis vectors.

Here are the actual witness constructions, with every resulting rational
coefficient saved, not implicit numerical approximations. In D[U]/q,
L071 supplies I_q=(q')⁻¹ and J_q=c⁻¹. Put
H=J_q I_q²/4, reduced to U-degree below three. The audited kernel
identity N=4c(q')² modulo q gives NH=1 modulo q. The new replay checks
the entire free-polynomial exact division

\[
NH-1=qW \quad\text{in }D[X],
\]

including every coefficient of W, not just its residue. In E₀, N=Tq²,
so the retained element

\[
q_i=TqH-W
\]

satisfies qq_i=1. That full product is independently checked.
By L073 the reduced c'(T) has inverse c'_i in L; its complete product
is checked again. L071's curve identity specialized using N=Tq² is
cM²=c'q⁶. The saved witness

\[
M_i=cM c'_i q_i^6
\]

therefore satisfies MM_i=1. The independent replay checks this product,
not merely the derivation. Since F'q=M modulo F, the witness
F'_i=qM_i has F'F'_i=1. The replay differentiates the whole specialized
F and checks that product. The elements y_f=q³M_i satisfy, in all E₀,

\[
c'y_f^2=c,\qquad y_fM=q^3,\qquad N=Tq^2.
\]

All these full residuals are zero in the independent evidence.
Consequently Y=Vy_f satisfies the source curve and both actual quotient
coordinate equations over the entire B. Neither a T-coordinate inverse
nor an inverse for a selected factor is used. B is finite etale by
L073; F is monic and its derivative a unit, so I is finite etale over
B and hence over Q. The explicit B-basis proves the global free rank,
rather than only local freeness.

**Exact inverse image, all projective exceptions and incidence.** Work
after any embedding D→Qbar, labeling its direction C as in L070/L072.
Every geometric point (T,V) of B is a nonidentity point of the actual
dual kernel. L073's cubic-unit witness also ensures V≠0; both signs
are retained. The certified source equation and q inverse show that a
point of I maps to (T,V) under L071's actual quotient. Conversely any
point P of the smooth source with Φ_C(P)=(T,V) is affine and has
q(X(P))≠0: L071's complete projective proof sends precisely O and all
six finite kernel points to O. The target point here is not O.
The x-equation then gives F(X(P))=0. At its resulting point of E₀,
M is a unit by the checked global identity, and the y-equation uniquely
forces Y(P)=Vy_f. These constructions are inverse on every geometric
point. Thus clearing denominators has added no component, and no
projective point was removed from the desired inverse image.

For such a P, the actual dual composition of L073 gives
[7]P=hat(Φ)_C(Φ_C(P))=hat(Φ)_C(T,V)=O. Moreover P≠O since its image
is nonidentity. L072's specified inverse sends (C,T,V) to the line
H=P₀+C for any torsion lift P₀. Because Φ_C has kernel exactly C,
its full fiber is precisely that same coset; our P lies on H.
Conversely an incident pair (P,H) determines its unique direction C
and the nonidentity value Φ_C(P) in that dual kernel, and hence the
unique point of I just constructed. These are inverse maps, using
quotient/coset and duality inputs, not counts alone. They retain all
seven members of every one of the 48 lines.

All polynomial coefficients and witnesses are over D. Under conjugation
of any of its eight embeddings the maps transport coefficientwise to
the quotient with conjugate direction, as in L072. Thus both inverses
are Galois-equivariant. They identify the finite etale scheme over Q
by composition through Spec(D), not Weil restriction. The ordinary
level-one functional labeling remains λ_(aH)=a⁻¹λ_H, and the Cartier
Hom(C,μ₇) convention stays unchanged; no point/ordinary-dual module
identification or trivialization of μ₇ is used.

**Both complete algebra maps.** The replay checks f(X)=0 for L067's
entire degree-24 source polynomial, together with (Vy_f)²=c(X).
These are exactly the generator relations of its two-coordinate
presentation, so substitution gives a unital algebra homomorphism
A→I and multiplication compatibility on every source element.
The displayed inverse rational coordinate change gives the original
model. It is checked coefficientwise in all 336 coordinates, including
the constant −1/2 and Y scale 1/216.

The source standard columns are the images of Xⁱ and XⁱY for 0≤i<24.
The independent verifier computes each image from the quotient and
checks all 48 full columns. It transports every column with L067's
entire 48-by-48 power matrix and back with its audited inverse.
Additionally it computes all powers 1,Y,…,Y⁴⁷ directly by multiplication
in E₀⊕VE₀, using V²=c', and checks equality with all transported
columns. This verifies the full separating-coordinate basis, not a
sampled collection. L067 proves A is a field; I is nonzero by its
monic basis. The unital map therefore has zero kernel and rank 48.
This inference requires no fieldness of B or I. The B-inclusion is
unital and multiplicative by construction; its 48 columns are the
48 distinct constant-X rational basis vectors, all independently
checked. Hence it too has rank 48. The geometric identification above
shows these two homomorphisms are exactly the two projection pullbacks.

**Complete finite replay and qualifications.** The single commands were

```bash
python3 -B scripts/seven-torsion/incidence-269/run_stage.py build_incidence
python3 -B scripts/seven-torsion/incidence-269/run_stage.py verify_incidence
```

The producer uses only the old producer's rational-polynomial helpers.
The independently written verifier imports no producer or notebook
arithmetic. Its exact-rational tower implementation uses sparse
convolution and monic reduction with empty-tuple zeros. It reconstructs
the whole F, H, W, q inverse, M inverse, derivative inverse and y factor
from the audited input coefficients, checking every saved coefficient.
It reconstructs every source and line column, all 336 basis transports
and both complete point transports, with the additional direct Y-power
multiplication check described above. `complete-replay-evidence.json`
retains the reconstructed coefficients, every map column and all six
full residual arrays. Their inspected values are empty arrays, the
verifier's exact zero representation. `replay-report.json` has no
failures. This is complete arithmetic replay, not inspection of saved
success flags, sampled roots or a preview.

Construction internal time is 6.493354749982245 seconds; replay internal
time is 19.939626540988684 seconds, each against 180. The corresponding
external times are 6.563020500005223 and 20.01959408307448 seconds,
each against 181, with neither watchdog firing. The replay watchdog
counts 6309661 bytes before its own report against the combined
134217728-byte limit. No stage was retried, divided or extended.

Three altered-evidence condition tests reject as intended. A corrupt
q inverse fails `full_q_inverse_product`; a changed original-model y
map fails `both_original_point_coordinate_maps`; removing the entire
odd-V line-column block fails
`all_48_line_columns_including_both_sign_components`. The last fixture
removes basis data needed to retain the full quadratic algebra; it
is not a selector for a geometric sign. These use full relevant mutated
files but test the named conditions only, not complete fresh malformed
replays. `rejections.json` records these exact scopes and false
`full_malformed_replay` values. `preservation.json` confirms all 358
inventoried upstream/original non-cache files retain their hashes,
including the failed step-268 script and all stopped earlier evidence.

The full construction threshold is met as a fixed known-method
reproduction, with its projective/all-fiber argument given above.
The separate critical audit below now validates this fixed assembly. A rank-seven presentation
makes a future norm test meaningful; it is not a norm computation or
an arithmetic descent certificate. Every independent limitation in
the conclusion remains.

**Separate critical audit (2026-10-17, step 271).** The invocation-start
SPECIALIZE assessment
`drafts/literature/2026-10-17-quotient-fiber-incidence-critical-audit.md`
covers precisely this audit. The entire proof, producer, independent
verifier and construction wrapper were read before execution. The named
upstream audited inputs are accepted; no upstream audit is repeated and
no claim is made about L069 or any stopped column presentation.

All fresh arithmetic ran once, under one combined 180-second limit:

```bash
python3 -B scripts/seven-torsion/incidence-audit-271/run_stage.py
```

The fresh directory contains byte-identical copies of the independent
verifier and four construction input certificates. Its complete replay
passes in 19.714811749989167 seconds. Recursive comparison of the entire
fresh and original `complete-replay-evidence.json` files agrees, including
every coefficient, both 48-column point bases, all 48 line columns, both
original-model coordinates and the six complete zero residuals. This is
full evidence comparison following arithmetic replay, not acceptance of
stored success flags. All 336 basis-vector round trips and 48 direct
Y-power products in that verifier pass.

`dense_check.py` is independently written and imports no notebook
arithmetic. It uses fixed-length rational vectors of dimensions eight,
three and seven, then an even/odd V pair. Multiplication in each monic
quotient uses Horner shifts: the last coordinate is eliminated by the
monic modulus and the next coefficient multiple is added. Induction on
the polynomial coefficients shows that this computes the full product
normal form. This differs from the replay's sparse convolution and
empty-tuple normalization. It compares whole dense normal forms over D,
not values at any chosen embedding or sample.

The distinct check independently reconstructs F from the audited N and q,
and checks the complete free-polynomial identity NH−1=qW, the c′ inverse,
the saved q/M/F′ inverse products, c′y_f²=c, N=Tq² and y_fM=q³.
It also checks F′q=M, the whole L067 source division polynomial, and both
even and odd components of the original equation y²+y=x³+x²−2x after the
coordinate substitution. Every one of these residuals is retained in
`dense-evidence.json` in full fixed-length form; all were inspected and
are zero. In particular, the ten-coefficient free W residual is not
reduced modulo q, and neither T nor a selected factor is inverted.

The same distinct check computes all 48 standard point columns and all
48 Y-power columns directly; it checks both complete 48-by-48 source
transports, all 48 line-inclusion columns, both original coordinate maps,
and all 336 normal-form basis round trips. Every map column retains all
336 rational coordinates, including the entire odd-V part. The audit
compares every rational entry against the fresh replay as well as the
original certificates. `complete-evidence-inspection.json` records the
complete comparisons and all actual replay checks. The distinct program
passes 792 conditions (including coordinate-length and basis checks);
this count is bookkeeping, not an independent proof claim.

The proof review retains the following essential cases. Successive monic
quotients give the displayed global basis even if B has multiple factors;
the derivative inverse then establishes etaleness. The q and M unit
identities hold everywhere in the entire quotient. For every direction
and both V signs, the recovered source point satisfies both quotient
coordinates. Conversely L071 sends O and each of the six finite kernel
points to O, and is affine elsewhere, so the nonidentity target fiber
has no missing projective point. Its x-coordinate satisfies F, and the
M inverse forces the unique recovered y-coordinate. Thus the two maps
are inverse on all geometric fibers, not only the generic fiber.

L073's actual dual forces every recovered source point to be seven-torsion;
its nonidentity image excludes O. L072 identifies the fiber with the
specified coset and supplies its converse and unique direction. All maps
commute with coefficientwise conjugation, so finite-etale descent applies
to the whole geometric set. Inverse ordinary-functional indexing and
Cartier Hom(C,μ₇) with its cyclotomic action are retained. This uses
composition through Spec(D), not Weil restriction. The source relations
first establish a unital homomorphism into the nonzero monic quotient;
only then does L067's fieldness imply rank 48. The line map has rank 48
from its distinct constant-X basis columns. No fieldness of B or I, or
count-only incidence argument, is used. These checks validate the existing
argument without changing its direct mathematical inputs.

The fresh replay repeats the three explicitly limited construction
condition tests. The distinct checker adds a full q-inverse product test
with the constant changed by one, a full original-y coordinate comparison
with an odd-V coefficient changed, and a full line-column comparison
with the odd-V block omitted. All reject at their named conditions.
`dense-mutants.json` preserves the altered data and `dense-evidence.json`
records the conditions. These are condition-only checks, not complete
malformed-certificate replays. Removing the odd-V block is loss of basis
data, not selection of a geometric sign.

The aggregate internal time is 38.340356417000294 seconds against 180;
external time is 38.4331816250924 seconds against 181, with no watchdog
firing. The watchdog records 7946001 bytes before its own report against
134217728. There was no retry or cap increase. The original 358-file
inventory was included and matched before execution; the new inventory
also includes the whole construction and failed startup evidence.
`audit-preservation.json` verifies that all 379 inventoried original files
retain their bytes, with no missing or changed path. ATTEMPTS/035--039
and incidence-268/269 remain preserved.

The fixed critical audit passes as known-method REPRODUCTION. It makes
this complete incidence algebra and its projection pullbacks a checked
local input for a possible later norm certificate. It produces no norm,
descent arithmetic, Selmer bound, rational direction or arbitrary-curve
rank comparison, and no progress beyond the imported construction is
claimed. Full matching Mathlib coverage remains not checked.

## Mathlib

Full matching Mathlib coverage for this explicit whole incidence algebra,
its two pullbacks, full rational transports and fixed arithmetic replay
has not been checked. This is not an absence claim. The precise cited
primary results provide the imported geometric and etale constructions.
