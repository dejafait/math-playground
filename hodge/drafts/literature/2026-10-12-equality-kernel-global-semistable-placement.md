# Equality kernel — proposed global semistable-moduli placement

TARGET: Assess whether one integral ample polarization places every S_1 fibre of the hypothetical (14,21) kernel in a projective Gieseker moduli space, preserving stability off L096's finite reducible locus.
CHECKED: 2026-10-12
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the two 2026-10-06 uniform-placement assessments and L063; searched primary fixed-Chern real slope chambers and equal-reduced-polynomial direct sums, and checked L071/L096, ATTEMPTS/061 and history/240--248 for overlap and stops.
SOURCE_EVIDENCE: Greb--Toma (2017), Theorem 6.6 and proof, p. 74, Section 6.3.3, p. 75; Huybrechts--Lehn (1997), Definitions 1.2.3--1.2.4, Lemma 1.2.13, Corollary 1.3.8, Remark 1.5.12, Proposition 2.3.1 and proof, Section 4.1, Theorem 4.3.4, Section 8.1 before Definition 8.1.4, and the surface RR formula in Proposition 5.2.2's proof with the K3 facts on p. 133.
COMPARISON: Published uniform slope (semi)stability and projective semistable-family corepresentation cover the changed scope; equal-polynomial direct sums supply the missing split-fibre mechanism. L063 alone remains insufficient, and general slope semistability does not imply Gieseker semistability.
GAP: Write the conditional applicability proof at charge fourteen: rational same-stratum choice also satisfying H.k=0, integral scaling, actual split-line polynomial comparison, fixed numerical class, all geometric fibres and family corepresentation. No such placement result is proved in this literature turn.
REASON: Essential source coverage is now ready for a known-tool specialization; no new wall theorem, new general moduli theorem or kernel-existence claim is needed.
SCOPE: Same hypothetical locally free Omega-polystable rank-two F with integral c_1=0 and ch_2=-14e_1-21e_2-tau_D at identical marked K3 metrics; no F existence, absence of reducibles, generic polarization, universal sheaf, embedding or transport is assumed.
COVERED_TARGET: Prove conditional uniform integral-polarization and projective Gieseker-moduli placement for L096's entire charge-fourteen S_1-fibre family, preserving stability off its finite reducible locus.
LITERATURE_REASON: Changed charge and possible split fibres require an essential reduced-Hilbert-polynomial comparison absent from the reusable all-stable L063 assessment.

Main gap: universal primitive rational Hodge realization. Nearer gap:
equality/positive-Euler kernel existence with the prescribed mixed action.
The proposed intermediate target is one global projective moduli placement
of this conditional family, retaining the possible exceptional fibres.
It could make later image-geometry tests meaningful across the finite
set; no such test or extension theorem is asserted here.

Essential established inputs are L071's actual exact-h polystability
and stable/split classification and separately audited L096's finite
reducible locus. L094 and L095 supply L096's local slice and derivative;
their derivative conclusions do not establish the proposed algebraic
placement. The previous L063 placement and its assessments are narrowly
relevant comparison material within this notebook, not an automatic
import under the changed hypotheses. No cross-notebook input is proposed.

## Primary theorem comparison

Daniel Greb and Matei Toma, *Compact moduli spaces for slope-semistable
sheaves*, Algebraic Geometry **4** (2017), 40--78,
doi:10.14231/AG-2017-003,
[Theorem 6.6 and proof, p. 74](https://content.algebraicgeometry.nl/2017-1/2017-1-003.pdf#page=35):
for fixed topological invariants of torsion-free sheaves on a smooth
complex projective n-fold and compact K in P(X)={A^(n-1): A real ample},
finitely many rational linear walls give identical slope stability and
semistability for all such sheaves at two classes in the same chamber.
The proof invokes the finite first-Chern-difference walls from Lemma
6.4. [Section 6.3.3, p. 75](https://content.algebraicgeometry.nl/2017-1/2017-1-003.pdf#page=36)
explicitly includes chambers of smaller dimension. This reread confirms
semistability and wall-stratum coverage; it is not an open-chamber-only
result. Reuse the earlier assessments' inspected Lemmas 6.1--6.4 and
Proposition 6.3 rather than repeat their proof. On surfaces P(X) is the
real ample cone itself. No changed discriminant bound is imported.

Daniel Huybrechts and Manfred Lehn, *The Geometry of Moduli Spaces of
Sheaves*, Aspects of Mathematics E31 (1997), inspected in the
[primary book PDF](https://ncatlab.org/nlab/files/HuybrechtsLehn.pdf):

- [Definitions 1.2.3--1.2.4, pp. 10--11; Lemma 1.2.13, p. 14](https://ncatlab.org/nlab/files/HuybrechtsLehn.pdf#page=22):
  stability uses reduced Hilbert polynomials; pure full-dimensional
  slope-stable sheaves are Gieseker-stable, with no reverse semistable
  implication supplied.
- [Remark 1.5.12, p. 24](https://ncatlab.org/nlab/files/HuybrechtsLehn.pdf#page=36):
  semistable sheaves with one reduced polynomial form an abelian
  category; stable and polystable objects are its simple and semisimple
  objects. This is the direct-sum input, conditional on equal polynomials.
- [Corollary 1.3.8, p. 18](https://ncatlab.org/nlab/files/HuybrechtsLehn.pdf#page=30):
  semistability survives field extension. [Proposition 2.3.1, p. 45](https://ncatlab.org/nlab/files/HuybrechtsLehn.pdf#page=57)
  gives openness; its proof uses geometric quotients, bounded
  destabilizing polynomials and projective Quot images.
- [Section 4.1, p. 80; Theorem 4.3.4, p. 91](https://ncatlab.org/nlab/files/HuybrechtsLehn.pdf#page=103):
  the flat semistable-family functor modulo base-line twists has a
  projective corepresenting scheme, with closed points recording
  S-equivalence. Stable objects give an open subscheme.
- [Section 8.1, p. 180](https://ncatlab.org/nlab/files/HuybrechtsLehn.pdf#page=192):
  fixed numerical-class parts are open and closed.

For the line comparison, reuse L071's inspected Huybrechts K3 source,
Chapter 1 (2.5)--(2.6). Independently read the surface HRR formula in
[Huybrechts--Lehn, proof of Proposition 5.2.2, p. 129](https://ncatlab.org/nlab/files/HuybrechtsLehn.pdf#page=141)
and the K3 canonical/Euler facts on
[p. 133](https://ncatlab.org/nlab/files/HuybrechtsLehn.pdf#page=145).
These supply the formula for a line of divisor class D:
chi(O(D))=chi(O_S)+D.(D-K_S)/2, with K_S=0 and chi(O_S)=2 here.
The author-hosted K3 PDF returned browser internal errors on two
targeted requests; the reused coverage and accessible primary book
passages remove any essential source-access gap. No claim is based on
the unsuccessful requests.

## Specialization reserved for the next research step

Retain L071 and audited L096, not the old charge-seven hypotheses.
The family parameter is S_2 and the fibre is S_1. The proof must apply
Theorem 6.6 to rank two, c_1=0 and charge fourteen, choose a rational
ample class in h's connected relative stratum, and also retain k.H=0.
The latter rational equality must be explicit even if the theorem's
wall list does not include it. L063 provides the reusable rational-density
and very-ample-power mechanism; its unchanged all-stable conclusion is
not being imported for this new family.

Off L096's finite set, use preserved slope stability and Lemma 1.2.13.
At its possible split points, verify both actual lines L and L^{-1}
are stable and have the same reduced polynomial at that H, using the
source RR formula and retained orthogonality. Only then use Remark
1.5.12; do not infer Gieseker semistability from slope semistability.
The numerical substitution and simultaneous-polarization proof are
unperformed here. This is the identified difference requiring a local
specialization, not a reproof of the cited general theorems.

Then algebraize the actual F, verify base flatness, its fixed Hilbert
polynomial and numerical class, and all geometric semistable fibres.
Corollary 1.3.8 and Proposition 2.3.1 cover the field-extension/openness
passage; checking only generic or closed stable fibres is insufficient.
Apply corepresentation to this actual family over the whole parameter
surface. The goal is a map into the projective semistable space, whose
stable open contains the complement of the finite set. No extension
from a punctured map, universal sheaf or smoothness of the semistable
space is needed or approved.

## Search, overlap and decision test

Queries: `Greb Toma Compact moduli spaces slope semistable Theorem 6.6
chambers semistability`; `Huybrechts Lehn reduced Hilbert polynomial
direct sum semistable Theorem 4.3.4 moduli projective`. Searches also
returned Greb--Toma's 2020 Kahler-Gieseker paper and quiver-variation
work: these are unread leads, not necessary inputs or coverage claims.
L063 already supplies the uniform stable-family method. ATTEMPTS/061
stops quadratic exclusion, not algebraic placement; the line-twist,
index-curvature and strict-Euler failures are preserved. No local
duplicate for this changed split-family placement was identified in
the named recent histories. Failed searches are no novelty evidence.

Coverage decision: SPECIALIZE. Continue only if the explicit rational
orthogonality, split polynomial, numerical-class and actual-family tests
all pass. If one fails, record the obstruction and narrow placement;
do not declare reducibles absent or kernel existence. The plausible
downstream use is a global image-geometry test across the finite set;
that further test is not covered by this assessment. F existence,
integrated germs, global separation and transport remain independent.
This review establishes source readiness, not the conditional placement
or progress beyond the sources. The newly covered continuation remains
subject to the supervisor's separate next-turn approval.

## Mathlib

Full matching real-chamber, Gieseker-polystable and family-moduli
coverage: **not checked**. No absence or matching declaration is claimed.
