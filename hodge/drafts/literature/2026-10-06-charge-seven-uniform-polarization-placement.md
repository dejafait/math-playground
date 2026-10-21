# Charge-seven family — uniform polarization and global placement reviewed

TARGET: Assess uniform integral-polarization replacement for L060's entire charge-seven family and its global algebraic classifying map.
CHECKED: 2026-10-06
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched fixed-Chern real-ample slope walls, uniform family polarization replacement and the stable-sheaf moduli functor; inspected Greb--Toma's published Section 6.2--6.3 and Huybrechts--Lehn's family/corepresentation statements; compared L052/L060/L062, L053's prior wall review and ATTEMPTS/044--045.
SOURCE_EVIDENCE: Greb--Toma, Algebraic Geometry 4 (2017), 40--78, Definition 2.3, Lemmas 6.1--6.4, Proposition 6.3 and Theorem 6.6 with proof, pp. 44, 69--74; Huybrechts--Lehn (1997), Lemma 1.2.13, Proposition 2.3.1, Section 4.1, Theorem 4.3.4 and Section 8.1 before Definition 8.1.4, pp. 14, 45, 80, 91, 180.
COMPARISON: Greb--Toma supplies real-class, fixed-invariant uniform slope chambers including lower-dimensional strata; Huybrechts--Lehn supplies the stable-family algebraic coarse moduli map. This is stronger coverage than pointwise perturbation or O'Grady's integral open-chamber theorem; it does not construct F.
GAP: Apply the real chamber theorem on this surface, justify a rational ample point in the same stratum and integral scaling, then verify purity, flatness, fixed numerical class and geometric stability for the moduli functor. This application is reserved for research; no H or map is proved here.
REASON: Essential coverage is ready for a known-tool specialization; preserve the global target while replacing the proposed endpoint-reproof mechanism by the published real-class chamber theorem.
SCOPE: Conditional F of L060, marked surface and real h of L044, every charge-seven fibre, and L052's exact zero-slope lattice. No F existence, global injectivity, embedding, universal sheaf, inverse transform, metric comparison or transverse transport.
COVERED_TARGET: Prove uniform integral-polarization replacement for L060's entire charge-seven family and construct its global algebraic classifying map.

## Target, relevance and continuation test

The main gap remains primitive rational Hodge algebraicity, with global
F existence and transverse transport also unresolved in this route.
The independent audit now verifies the local differential constraint
in L062. A possible next intermediate target is one integral ample
polarization H making all E_x slope-stable, so that a global algebraic
classifying map can be considered in a fixed sheaf moduli space.
Such placement could make later geometric constraints testable.

Essential inputs are L044 (S,h and marking), L052 (actual restrictions
and exact zero-slope lattice), L060 (conditional F and stable charge-seven
fibres) and L062 (verified differential). The vector (2,0,-5) is already
recorded in the previous family assessment. Retain conditional existence;
do not replace F by numerically compatible fibres or assume a global
universal bundle on a moduli space. Any use of Gieseker moduli must
justify the slope-to-Gieseker passage at the same chosen H.

The threshold is one integral ample H preserving strict slope stability
of every E_x, followed by one algebraic morphism to the stable locus
of M_H(2,0,-5). Continue if the uniform theorem and surface-stratum
specialization meet that threshold. Abandon automatic placement if the
real-class stratum application or flat stable-family hypothesis fails.
Separate choices for different fibres, or stability only on a dense
open parameter subset, do not suffice. No H or morphism is derived here.

## Primary coverage and qualifications

**Real, uniform slope chambers.** Import Daniel Greb and Matei Toma,
*Compact moduli spaces for slope-semistable sheaves*, Algebraic Geometry
**4** (2017), no. 1, 40--78, doi:10.14231/AG-2017-003,
[Definition 2.3, p. 44](https://content.algebraicgeometry.nl/2017-1/2017-1-003.pdf#page=5)
and [Theorem 6.6 and proof, p. 73, with Section 6.3.3, p. 74](https://content.algebraicgeometry.nl/2017-1/2017-1-003.pdf#page=34).
For a smooth complex projective n-fold X, put P(X)={A^(n-1):
A in Amp(X)_R} in the real numerical curve space. For fixed
topological invariants (r,c_1,...,c_n) and compact K contained in
P(X), finitely many rational linear walls give a chamber structure.
Two classes in K in the same chamber give identical slope stability
and semistability for every torsion-free sheaf with those invariants.
Section 6.3.3 treats chambers as connected strata, including dimensions
less than rho(X). The quantifier is uniform over sheaves. Definition
2.3 uses c_1(A).alpha/rank(A) and strict inequality for every subsheaf
of intermediate rank for stability.

Read the [real-class proof cases in Lemmas 6.1--6.4 and Proposition
6.3, pp. 70--72](https://content.algebraicgeometry.nl/2017-1/2017-1-003.pdf#page=31):
compactness for line subsheaves, a properly semistable first crossing,
and fixed-Chern boundedness over a compact Kahler set. Lemma 6.4
retains a saturated torsion-free quotient, equal slopes, the primitive
first-Chern difference, Hodge index, discriminant identity and
Bogomolov. Iteration ends at rank-one terms. Theorem 6.6 uses those
finite differences for walls; there is no integral-class assumption
at the real crossing. Import the theorem rather than reprove it.

The discriminant in (6.7) is normalized differently from O'Grady's;
no numerical cutoff is transferred between them here. Some extracted
inequality glyphs are ambiguous. The parallel preprint
[arXiv:1303.2480v3, equation (6.9), printed p. 44](https://arxiv.org/pdf/1303.2480v3#page=44)
confirms the nonnegative Bogomolov sign. Published Theorem 6.6 is
preprint Theorem 6.7; use the published numbering consistently.

**Surface applicability still to write.** L044 supplies the projective
surface and algebraic real h; L060 fixes every fibre's invariants and
strict stability. Verify their numerical-space interpretation, choose
a compact ample neighborhood, and justify a rational point in h's
same relative stratum from its finite rational equations and strict
inequalities. Then justify integral scaling. Theorem 6.6 supplies
uniformity. L052's Zk zero-slope lattice remains context; do not assume
h avoids all numerical walls or impose v-genericity on H. Proposition
6.7's separately stated dimension hypothesis is not used to import
an integral representative at dimension two: write the elementary
surface stratum justification. This is an applicability argument,
not a new general wall theorem. No charge-seven wall computation is
performed in this review.

**Algebraic classifying map.** Import Huybrechts and Lehn,
*The Geometry of Moduli Spaces of Sheaves*, Aspects of Mathematics
E31 (1997),
[Lemma 1.2.13, p. 14](https://ncatlab.org/nlab/files/HuybrechtsLehn.pdf#page=26),
[Proposition 2.3.1, p. 45](https://ncatlab.org/nlab/files/HuybrechtsLehn.pdf#page=57),
[Section 4.1, p. 80](https://ncatlab.org/nlab/files/HuybrechtsLehn.pdf#page=92),
[Theorem 4.3.4, p. 91](https://ncatlab.org/nlab/files/HuybrechtsLehn.pdf#page=103),
and [Section 8.1 before Definition 8.1.4, p. 180](https://ncatlab.org/nlab/files/HuybrechtsLehn.pdf#page=192).
For a polarized projective scheme over an algebraically closed field
and fixed Hilbert polynomial, Theorem 4.3.4 gives a projective coarse
scheme for flat semistable families modulo base line twists, and a
stable open for geometrically stable families. For pure sheaves of
full dimension, slope stability implies Gieseker stability. Geometric
stability is open in flat families. Section 8.1 supplies open-and-closed
fixed numerical K-class parts, via locally constant Euler pairings.

L060 already invokes GAGA for F on S x S. In the application, verify
flatness over the parameter, constant Hilbert polynomial/numerical
class and all geometric fibres at H before using the moduli natural
transformation. A universal sheaf on the whole moduli space is not
required for the classifying morphism. Do not identify the fixed
Hilbert polynomial with a fixed Mukai vector without the numerical
class passage. No projectivity of the stable open, absence of strictly
semistable objects, global injectivity or embedding is asserted here.
L062's differential can be identified with that of the resulting map
only after placement is written. Fine moduli are outside this target.

## Comparison, searches and access

O'Grady, *Modular sheaves on hyperkahler varieties*, Algebraic Geometry
**9** (2022), 1--38,
[Definitions 1.1 and 3.1--3.3, Propositions 3.4, 3.8, 3.10 and
proofs, pp. 2, 8--10](https://content.algebraicgeometry.nl/2022-1/2022-1-001.pdf#page=8),
was checked against L053's earlier assessment. Its numerical walls
live in the real cone, but its stability propositions use ample
divisor classes and open chambers. That alone leaves this endpoint
unaddressed. Greb--Toma is the stronger import; an O'Grady endpoint
reproof is unnecessary for the approved application.

Queries included `O Grady moduli vector bundles Proposition 3.4 a walls`,
`Huybrechts Lehn Theorem 4.3.4 corepresents families`, `stable vector
bundles real ample class uniform family perturbation polarization`,
and `Greb Toma compact moduli Theorem 6.6 real ample chamber faces`.
Only the primary passages above are relied on. Greb--Toma's 2018
Kahler Gieseker paper and Greb--Ross--Toma survey/quiver results were
search leads, not inspected theorem imports. An exploratory wrong
arXiv identifier (alg-geom/9609011) was not used; a nonexistent
1303.2480v4 request failed and the correct v3 was read. A shell
download failed DNS, but the published sources remained readable
through the web reader. No essential source blocker remains.

L053 establishes selected charge-five/six factors, not this entire
charge-seven family. L062 supplies a local form, not global placement.
The index/projection and lifting stops in ATTEMPTS/044--045 remain
intact and do not answer this target; the flat-source blocker remains
parked. This is source coverage for a known-tool application, with no
novelty claim, new cycle or progress beyond the imported theorems.

## Mathlib

Full uniform real-polarization and algebraic moduli-family coverage:
**not checked**. No matching declaration or absence is asserted.
