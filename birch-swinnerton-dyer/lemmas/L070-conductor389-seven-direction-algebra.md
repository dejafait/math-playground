# L070 — Scalar-fixed direction algebra at conductor 389

## Hypotheses

Use audited L067 and L068 for the exact curve
E: y²+y=x³+x²−2x over Q. Write A for the entire algebra on
Z=E[7]−{O}, C=Q[X]/f for its degree-24 x-coordinate subalgebra,
and A=C[Y]/(Y²−c(X)), c(X)=X³−3024X+46224. The complete ordered
bases, both coordinate models and all six geometric forward scalar
pullbacks σ_a are those of L067/L068. No residual-image, L026, Selmer,
analytic-order or rational-rank hypothesis is imposed.

The exact instance evidence is
`scripts/seven-torsion/compressed-249/direction.json`; the independent
replay is `direction-replay.json` in that directory. The producer imports
only the old producer's rational-polynomial helpers. The verifier imports
only the old independent verifier's helpers, never producer arithmetic.
The original source files and all rational entries are retained.

## Conclusion

Put z=X+[2]⁎X+[3]⁎X in C, using forward geometric pullbacks. The entire
scalar-fixed subalgebra A₊=A^{F₇×} has presentation Q[Z]/h, Z↦z, where

\[
\begin{split}
h(Z)={}&Z^8-254016Z^6+69890688Z^5-17283248640Z^4\\
&+1268096643072Z^3-63037439668224Z^2\\
&+2465179874131968Z-47414394214612992.
\end{split}
\]

This is the algebra of all eight projective directions in E[7], with
degree-six scalar covering A/A₊. It is a field in this fixed instance.
The certificate gives the complete 24-by-24 matrix and inverse of
the mixed basis z^j X^k (j fastest, 0≤j<8, 0≤k<3) of C, and a monic
cubic q(U,Z) in U, with coefficients of Z-degree below eight, giving
C≅Q[Z,U]/(h(Z),q(U,Z)). Every cubic coefficient is in the certificate.

In each of L067's two full 48-dimensional coordinate bases it supplies
an inclusion E, coordinate retraction K and Reynolds projection R with
EK=R and KE=I₈. Thus the inverse coordinates are valid on the **entire
fixed image**. K is only asserted to be linear on ambient A; no ambient
algebra-homomorphism claim is made. All 64 direction-basis products and
both coordinate transports pass complete independent replay.

This is a fixed known-construction specialization. It supplies no verified
point-direction complement, affine-line equalizer, incidence norm,
global power classes, Selmer enclosure or successful localization.
The ordered-pair/incidence target is not completed. No BSD conclusion
or progress beyond the imported general construction is claimed.

## Proof

**Imported result.** Schaefer–Stoll, *How to do a p-descent on an
elliptic curve*, Trans. AMS 356 (2004), 1209–1231, DOI
10.1090/S0002-9947-03-03366-X,
[author long version dated 13 June 2001](https://mathe2.uni-bayreuth.de/stoll/papers/p-descent-long.pdf),
Lemma 7.2 and its proof, printed pp. 13–14, followed by the general-p
paragraph, identify the scalar-orbit subalgebra for nonzero E[p].
The stabilizer/scalar-intersection hypothesis holds because a nonzero
point has order seven: aP=P forces a=1 in F₇×. Q has characteristic
zero, seven is odd, and L067/L068 supply the whole geometric set and
the correct scalar action. Actual Galois image GL₂(F₇) is not assumed.
Its scalar orbits are the six nonzero vectors on each of the eight
one-dimensional subspaces. We use this source theorem, not the source's
p=3 coordinate example. The finite-etale/Galois-set correspondence is
[Stacks Lemma 58.2.2, tag 03QR](https://stacks.math.columbia.edu/tag/03QR).
All bases below concern full algebras, without a selected geometric fiber.

**Exact generation and presentation.** In the ordered C-basis
(1,X,…,X²³), the independent verifier reconstructs z from all coefficients
of the three audited forward X-coordinates. It computes z⁰,…,z⁸ by
independent rational convolution and monic reduction modulo f. For every
0≤j<8 and 0≤k<3 it reconstructs the complete reduced vector of z^jX^k.
These are the columns of M. It reads the full saved N and verifies
MN=NM=I₂₄ entry by entry. Thus all 24 mixed elements form a basis;
in particular 1,z,…,z⁷ are independent. It checks h is monic of degree
eight and h(z)=0 in the whole C. Hence the substitution Q[Z]/h→C is
injective and identifies its eight-dimensional image exactly.

Let q(U,Z)=U³−∑_{k=0}²∑_{j=0}⁷ v_{j+8k}Z^jU^k,
where v=N·coord_C(X³). These are the complete saved cubic coefficients.
The verifier checks q(X,z)=0 by evaluating every coefficient modulo f.
Successive division by the monic h(Z) and then monic q(U,Z) shows that
Q[Z,U]/(h,q) is free of dimension 24 on the displayed mixed basis.
Its substitution to C has the invertible matrix M, hence is an algebra
isomorphism with full inverse N. There is no claim that a guessed
separating generator succeeds without these identities. The 64 checks
reduce Z^{i+j} modulo h and compare its value at z with z^i z^j for
all 0≤i,j<8, retaining every coefficient and zero entry.

**Complete invariant image and both transports.** In the full B-basis
of A, define R_B=(1/6)∑_{a=1}⁶σ_a. Audited L068 supplies the complete
group action, so the averaging projector has image exactly the fixed
subalgebra: each averaged vector is fixed by permuting its six summands,
and a fixed vector equals its average. This elementary application uses
division by six in Q. The independent verifier reconstructs all 2304
entries directly from all six audited matrices. It checks σ_a E_B=E_B
on every one of the eight columns, for all six a, and

\[
 E_BK_B=R_B,\qquad K_BE_B=I_8.
\]

E_B consists of the eight reconstructed even power vectors with all 24
odd entries zero. These identities prove rank R_B=8 and equality of its
whole image with the generated subalgebra. They also prove that K_B
really recovers the unique power coordinates of every invariant vector.
This is a kernel/image certificate on all 48 coordinates, not only an
upper dimension estimate or sampled fixed elements. No invariant odd
component has been silently removed: the full six-scalar mean includes
the sign action and its factorization is checked on all coordinates.

Let M₀,N₀ be L067's full mutually inverse transports, with M₀ sending
T-coordinates to B-coordinates. The verifier checks

\[
 M_0E_T=E_B,\quad N_0E_B=E_T,\quad
 K_BM_0=K_T,\quad K_TN_0=K_B,
\]
\[
 E_TK_T=R_T=N_0R_BM_0,\qquad K_TE_T=I_8.
\]

All products are full exact rational matrix products. Consequently the
two inclusion maps, projection maps and inverses on the whole invariant
images agree in both coordinate models. The cited orbit theorem now
identifies this algebra with all eight directions, and gives covering
degree six. Because L067's A is a field and the invariant algebra is an
eight-dimensional subalgebra containing one, it is a field: multiplication
by any nonzero element is injective, hence surjective in finite dimension.
Etaleness also follows from the source correspondence. No new irreducibility
test, residual-surjectivity hypothesis or dual-to-point identification enters.

**Finite replay, bounds and qualifications.** The commands executed from
the notebook were:

```bash
python3 scripts/seven-torsion/compressed-249/run_stage.py build_direction
python3 scripts/seven-torsion/compressed-249/run_stage.py verify_direction
python3 scripts/seven-torsion/compressed-249/run_stage.py check_direction_rejections
```

The existing-output watchdog logs and rejection directory intentionally
prevent accidental overwrite. For fresh replay of the retained certificate,
run `python3 scripts/seven-torsion/compressed-249/verify_direction.py --report
scripts/seven-torsion/compressed-249/fresh-direction-replay.json` with an
unused report filename. The saved producer and independent replay completed
in approximately 0.23 and 1.07 seconds of internal arithmetic, below each
180-second cap, with separate external 181-second watchdogs. The direction
certificate has fewer than 0.4 MiB including its initial code/reports,
below the cumulative 128-MiB cap. Full reports retain exact timings.
Four full-schema altered copies are rejected at the intended mathematical
checks: an altered scalar matrix, missing leading degree, wrong inclusion,
and a retraction altered together with its projection to test KE=I directly.
For the altered scalar fixture only, its own action-input hash is updated;
it still fails the complete Reynolds identity. All original upstream
hashes and direction artifacts checked by the rejection harness agree.
No omitted-component, relation or norm rejection is claimed: those
constructions are outside this completed partial result. The separate
critical audit below validates this fixed assembly.

**Separate critical audit (2026-10-16, step 251).** The unchanged saved
SPECIALIZE assessment covers precisely this proof and finite instance.
The inspected Schaefer--Stoll theorem and Stacks correspondence are reused;
this is REPRODUCTION, with no new general theorem or residual-image premise.
The audited L067/L068 inputs identify the entire geometric algebra and
forward scalar action before any invariant computation is used. L069 and
all unfinished incidence evidence are excluded as mathematical premises.

The mixed inverse establishes both rank inequalities, not just eight
candidate invariant elements. Successive monic division means first
forming (Q[Z]/h)[U] and then quotienting by its monic cubic; it gives a
free rank-three module even without assuming that Q[Z]/h is a field.
The actual cubic has all three lower coefficients of Z-degree at most
seven, and every coefficient is exactly the negative of the appropriate
entry of N coord_C(X³). Thus the claimed presentation and its inverse
are justified before fieldness is deduced. The invariant-image argument
uses all six actions on all 48 coordinates. KE=I gives injectivity and
EK=R gives surjectivity onto the entire Reynolds image. The unit is
included, and this image is closed under multiplication because all six
maps are algebra automorphisms. Consequently the inverse on this image
is an algebra inverse; the ambient linear K need not preserve products.
The field argument uses finite-dimensionality and L067's fieldness only.
The scalar action has free orbits of size six, and the field degrees
48/8 also give the asserted covering degree. No Galois-surjectivity
claim is needed.

Fresh reports are in `scripts/seven-torsion/direction-audit-251/`:
`upstream.json`, `actions.json`, `direction.json`, `crosscheck.json` and
`audit-report.json`. Complete upstream replay passes, followed by all
576 scalar basis images and 165888 composition entries. The fresh
direction report passes all 93 original checks. Both retained direction
reports have the identical complete check list and bounds. Each fresh
stage finished in less than four seconds against the 180-second bound;
the external stage watchdog was 181 seconds and never fired.

The distinct `crosscheck.py` imports no producer or verifier arithmetic.
It reconstructs multiplication in C directly from the monic f, and clears
denominators before full integer matrix products. It verifies the printed
h coefficient by coefficient, all nine powers, all 24 mixed columns,
both full inverse products, every cubic coefficient, all 64 direction
products, every shape and both transports. Independently in each full
basis it averages the six saved action matrices and checks E K=R,
K E=I, R²=R, tr(R)=8 and every fixed-column identity. In characteristic
zero an idempotent's trace is its rank, so this provides an additional
full-image dimension check; it does not replace the image factorization.

Two exact checks supplement substitution into the defining relations.
Writing X_i=[i]⁎X for i=1,2,3, the script verifies every coefficient in C
of

\[
q(U,z)=(U-X_1)(U-X_2)(U-X_3).
\]

This is a check of the existing relative cubic, not a construction of an
incidence algebra. Next let Z_C be the 24-by-24 matrix of multiplication
by z on C. Pivoted fraction-free Bareiss determinants, after clearing
all denominators, verify

\[
\det(tI-Z_C)=h(t)^3 \quad(t=-12,-11,\ldots,12).
\]

Both expressions are polynomials of degree 24. Their difference has
25 distinct rational roots and is therefore identically zero. All 25
complete exact determinants and comparison values are retained in
`crosscheck.json`; no numerical eigenvalues or modular sample are used.
This supplements the already verified rank-eight power basis rather
than replacing it. All 129 distinct-check assertions pass.

`inspect_evidence.py` reads and compares the complete retained evidence,
not previews. It verifies every intended fixture modification and freshly
replays all four original altered certificates. The scalar fixture changes
one action entry and updates its own input hash; it fails at
`all_2304_Reynolds_entries_six_scalars`. The degree fixture fails at
`degree_eight_monic`, the inclusion at `entire_B_inclusion`, and the
inverse fixture at `B_inverse_on_full_image`. For the last fixture the
changed projection is independently checked to equal the changed EK,
so its failure specifically tests KE=I. None is accepted merely on a
schema or hash failure. The original report, fixture bytes, watchdogs
and logs agree with these fresh results. The full old preservation
inventory has 28 entries; all 101 old upstream hashes also agree.
The fresh manifest covers all 130 original non-cache seven-torsion files,
including both stopped presentations and their partial output, with zero
changed or missing files. Preservation is not verification of the stopped
incidence arithmetic.

Reproduction, with unused output paths/directory as required, is:

```bash
python3 scripts/seven-torsion/direction-audit-251/run_replays.py
python3 scripts/seven-torsion/direction-audit-251/inspect_evidence.py
```

The saved audit directory deliberately refuses existing final report/log
paths. Its manifest was saved before any fresh computations. This separate
fixed audit passes; it establishes neither universal implementation
correctness nor any incidence, norm, Selmer, localization or BSD conclusion.

## Mathlib

Full matching coverage for this fixed degree-eight polynomial, mixed
presentation, all invariant-image coordinates and complete rational
certificate was not checked. Unknown availability is not absence.
The named source theorem supplies the general construction; this is an
informal instance verification, not a Lean formalization.
