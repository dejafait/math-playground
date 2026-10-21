# Nonflat rank-three projective lift — completed source comparison

TARGET: Assess a projective rank-two lift obstruction for the prospective stable orthogonal rank-three opposite transform at (-10,-11), retaining nonzero w_2 and Brauer classes.
CHECKED: 2026-10-06
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Scoped L059/L060, saved orthogonal assessment, ATTEMPTS/043--044 and histories 112--113; primary searches for K3 PGL2/SO3 lifting, Brauer-twisted rank-two sheaves, primitive isotropic twisted moduli and charge-eight Azumaya algebras; queries and inspected ranges below.
SOURCE_EVIDENCE: Venkata Balaji math/0407079v1, Theorems 1.1 and 1.5(b), pp. 1--4, proof p. 12; Yoshioka math/0411538v2, Section 1.1, Lemmas 1.2--1.4, 3.1, Proposition 3.6 and Theorem 3.16 with initial split/nonsplit proof cases, PDF pp. 2,6,8,10; Ingalls--Khalid 1104.4333v3, Theorems 4.3 and 4.7 with relevant proofs, pp. 10,15; reused Stacks/Perego duality and connection coverage in the saved orthogonal assessment.
COMPARISON: Low-rank Clifford/projective lifting and distinct SL2/GL2 obstruction classes are covered; published degree-two Azumaya examples have c_2=8, so a charge-only exclusion cannot be imported. No inspected theorem identifies the prospective image on the exact S,h or supplies its kernel.
GAP: Apply the ready coefficient-duality framework to L060 before assigning orthogonal structure; identify its SO3/PGL2 torsor, keep both lifting classes, and test only necessary spin/ordinary/twisted lift constraints. Exact-metric existence, a universal obstruction on nonsplit lifts and reconstruction remain unresolved.
REASON: The changed target needs local applicability and characteristic calculations, not a reproof of general lifting theorems; the comparison supports one separate bounded attempt while preventing false determinant-zero or charge-only exclusions.
SCOPE: Conditional L044 S,h,tau_D, L052 connections and divisor lattice, L060 rank-three image and cohomology, and L059 coefficient-duality framework only. Covers pairing/parallelness/orientation, regular ternary Clifford and PGL2 description, SL2 versus GL2 versus Brauer-twisted alternatives and necessary characteristic/index tests. Does not approve exact-h twisted existence, an inverse, faithfulness, kernel construction or transport.

## Gap, relevance and bounded test

The main local gap remains a compatible global F with prescribed mixed
action; transverse transport and universal primitive Hodge algebraicity
remain independent. The intermediate object is L060's conditional stable
rank-three H, c_1=0, c_2=8 and cohomology (0,2,0). A lift-sensitive
obstruction could exclude this branch before global construction. A
compatible image would supply neither F nor transverse transport.

Continue with one separate necessary-constraint attempt under SCOPE.
First justify the actual symmetric pairing, then retain three cases:
vanishing SL2 obstruction; nonzero SL2 obstruction with vanishing Brauer
obstruction; nonzero Brauer obstruction. Excluding one case is useful
but is not exclusion of H. If the nonzero classes leave compatible
alternatives after these tests, stop this bounded lifting/index mechanism
and record exactly what passes. Further existence or reconstruction
requires its own assessment. No new lemma or characteristic calculation
is performed in this literature turn.

## Primary statements and essential cases inspected

**Ternary Clifford description.** T. E. Venkata Balaji,
*A Limiting Version of a Theorem in Cohomology*,
[math/0407079v1, 6 July 2004](https://arxiv.org/pdf/math/0407079v1),
Theorem 1.1 and regular-form restriction, pp. 1--2; Theorem 1.5,
pp. 3--4, and proof, p. 12. The general statement relates line-valued
ternary forms modulo twisted discriminant bundles to specializations
of rank-four Azumaya algebras. The regular case gives Azumaya algebras.
Theorem 1.5 identifies SO with the specified determinant-preserving
even-Clifford automorphisms; part (b), for integral X and a semiregular
fibre, removes that restriction. The proof checks local similarity
multipliers and determinants and descends the group statement. Only
the everywhere nondegenerate complex case is needed here. This does
not assert that the Clifford algebra is split. After orientation is
justified, the standard split identification Aut(M_2)=PGL_2 supplies
the projective description. The future application must identify its
adjoint bundle rather than importing line-valued degenerations.

**Obstruction classes and twisted indices.** Kota Yoshioka,
*Moduli spaces of twisted sheaves on a projective variety*,
[math/0411538v2, 8 May 2006](https://arxiv.org/pdf/math/0411538v2),
Section 1.1, Lemmas 1.2--1.4, PDF p. 2; Lemma 3.1, p. 6;
Proposition 3.6, p. 8; Theorem 3.16, p. 10. The SL_r boundary w
maps to the GL_r Brauer boundary. An ordinary projectivization has
w=c_1 mod r; Lemma 1.4 characterizes ordinary lifts by w lying in NS
modulo r. Lemma 3.1 gives the End discriminant congruence modulo 2r.
Proposition 3.6 gives simple twisted-sheaf deformation dimension v_G^2+2
and bound v_G^2>=-2. Primitive positive-rank nonemptiness requires a
general ample polarization. Read the reduction and separate Brauer-trivial
and nontrivial proof cases; the latter uses deformation, not deletion
of the twist. These support necessary tests, not locally free
slope-stable existence at the saved irrational h. Integrality uses a
lift of w and a twisted Mukai lattice, not an ordinary c_1 for a
twisted sheaf. The cited Theorem 3.14 and asymptotic Proposition 3.15
are not used to assert charge-eight existence.

**Existing charge-eight examples.** Colin Ingalls and Madeeha Khalid,
*An explicit derived equivalence of Azumaya algebras on K3 surfaces via
Koszul duality*, [1104.4333v3, 7 January 2014](https://arxiv.org/pdf/1104.4333v3),
Theorems 4.3 and 4.7, pp. 10 and 15. Hypotheses: a double-plane K3
branched over a smooth sextic, an ineffective even theta characteristic,
and its net of quadrics with base-locus K3 X. Projection from x in X
produces a degree-two Azumaya B_x with chi=0 and c_2=8. Read the local
matrix-algebra check across the branch divisor, pushforward exterior
power description, and H^0/GRR conclusions in Theorem 4.3's proof.
Theorem 4.7's proof records h^1(B_x/O)=2, h^2(B_x/O)=0 and retains
the underlying mu_2-gerbe. This overlaps the prospective adjoint
character; it does not give existence on L044's S,h. No identification
with this RM K3, metric, stability condition or F is supplied. The
older search result numbers the moduli theorem 4.6; the inspected v3
numbers it 4.7. Use v3 numbering.

## Reused coverage and future applicability obligations

The [saved orthogonal assessment](2026-10-05-flat-transform-orthogonal-residual.md)
already inspected Stacks 48.19(2),(9), 0A9Q, 0BRT and 0GWN, and Perego
(2021), Propositions 3.9--3.12 and 3.15, pp. 36--38. Reuse it for
proper smooth coefficient duality, Koszul signs and parallel holomorphic
morphisms between zero-Einstein bundles. L059's proof through the
parallel real reduction was read; its hypotheses concern the flat pair
and cannot be silently applied to L060. Verify det(F)=O, relative
canonical trivialization, all-fibre H^1 concentration and both signs.
L060 supplies concentration and the induced zero-Einstein connection.
There is no flat residual to split off. Orientation must be justified
before SO3 is invoked.

The SL2 obstruction is the class of its central double cover; identify
it with w_2 of the compact real reduction in the future application.
Its image in H^2(O^*) is a different obstruction. Distinguish
topological integral lifts from holomorphic ordinary lifts. Base spin
and integral c_1(H)=0 do not supply a spin lift of this bundle.

An ordinary rank-two lift may have arbitrary determinant in Pic(S).
Its adjoint is unchanged by line twisting; rational half-determinant
normalization is not necessarily an integral twist. L052's Zk lattice
describes actual slope-zero lines, not every lift determinant. Do not
restrict that determinant to Zk without a separate argument. For a
nonsplit lift use the twisted conventions and descending End bundle;
do not apply untwisted Euler formulas to an imaginary ordinary bundle.
Verify simplicity, required for Proposition 3.6, from the actual
adjoint rather than from the word “twisted”.

Surface RR, Picard injectivity, Serre duality and real-metric stability
coverage in L052/L060 is unchanged. No broad existence theorem is
needed for this bounded necessary test. Rational-polarization existence
cannot substitute for exact-h coverage. General lifting theorems need
no reproof; local sign, determinant, characteristic and index
specializations are necessary because the sources do not describe
this conditional direct image.

## Search, duplicates and limitations

Queries included “K3 stable PGL2 bundles Brauer twisted sheaves rank two
discriminant 8 orthogonal rank 3”, “Yoshioka moduli twisted sheaves K3
primitive isotropic rank 2 vector theorem”, “SO(3) bundle K3 instanton
w2 Brauer obstruction lift holomorphic”, “Azumaya 8 K3 c2 rank four”,
and “rank 3 Azumaya equivalence quadratic bundles”. Primary statements
and proof cases above, not snippets, support this assessment. A
Citeseer copy failed to open; arXiv v3 supplied the needed passages,
so access does not block the approved test. Juan--Ledet's field-level
PGL2 representation, Section 2, was inspected as a lead, not used as
a holomorphic lifting theorem. No originality is inferred.

L059 and ATTEMPTS/043 concern the flat rank-seven parity/index stop;
L060 and ATTEMPTS/044 concern the nonflat rank-three cohomology stop.
Neither these exhausted mechanisms nor the flat analytic source blocker
decides the changed lifting question. Preserve their evidence. The
exact S,h lifting test remains unperformed; the source overlap prevents
only a generic charge-only argument.

Mathlib: full low-rank holomorphic lifting, Brauer-twisted and exact-metric
specialization coverage **not checked**; no absence is claimed. No
proof assembly or dependency was added. No H, F, cycle or transverse
surface is constructed, and no complete Hodge candidate is proposed.
