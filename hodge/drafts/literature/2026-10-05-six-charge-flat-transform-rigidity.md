# Six-charge flat-transform rigidity — completed source comparison

TARGET: Determine whether G=O_S^2 at b=-17 in L057 forces the L056 kernel's mixed action tau_D to vanish without assuming a Fourier–Mukai equivalence.
CHECKED: 2026-10-05
DECISION: EXPLORE
SEARCH_EVIDENCE: Scoped comparison found no duplicate rigidity proof; searches for flat hyperkahler/Nahm transforms, inverse-kernel criteria and index curvature located the primary sources below, including a normalized trivial-image example with nonzero mixed polarization action.
SOURCE_EVIDENCE: Bartocci--Bruzzo--Hernandez Ruiperez (1998), Theorems 3--4, pp. 246--247; their alg-geom/9405006v2, Sections 2.2, 3.1, 4.1 and 4.3, Proposition 6 and Theorem 2; Bartocci--Jardim math/0312045v1, pp. 4--7; Bridgeland math/9809114v2, Theorems 1.1, 5.1 and 5.4; Jardim math/0309305v3, Section 2 equations (4)--(8); Stacks 01F2.
COMPARISON: Published inverse results require universal/reflexive or strongly simple kernels; trivial direct image alone is compatible with nonzero mixed action in a different published setting. No inspected theorem settles the exact determinant-zero rank-two-transform case. Arbitrary-kernel preservation and Leray cover an independent opposite-projection necessary test.
GAP: Test whether the opposite direct image's full GRR character and polystable cohomology can coexist with G=O_S^2 and the prescribed tau_D; neither a contradiction nor the rigidity implication has been established.
REASON: Park automatic inversion and flat-image reconstruction. A bounded opposite-projection/Leray test uses inspected tools without those hypotheses and can decide whether this elementary necessary-condition mechanism merits continuation.
SCOPE: Exact S,h,tau_D of L044, locally free rank-two product-polystable F with a=-10,b=-17, L048's forced full character and L056--L057's actual G=R^1 p_2*F=O_S^2. Only the opposite-projection preservation, GRR, Leray and polystable surface-cohomology test is approved; no equivalence, inverse, faithfulness, curvature positivity or global F is assumed.

## Gap, downstream use and discriminating test

The main local gap is compatible global locally free product-polystable
realization of the cubic mixed action. Even such a realization would leave
transverse transport and universal primitive rational Hodge algebraicity
unresolved. The unchanged intermediate target could exclude the flat
b=-17 exception, if a rigorous necessary incompatibility is found.

Continue with one bounded mathematical attempt: first establish all-fibre
concentration for p_1 using L052, then obtain its actual polystable direct
image using the same arbitrary-kernel theorem as L056. Evaluate its full
character, and compare its cohomology through Leray with the given p_2
transform. Retain trivial summands and all remaining stable/split cases;
do not assume the opposite transform is rank two. A contradiction or an
additional discriminating constraint supports continuation. If the full
necessary data coexist, stop this two-projection/cohomology mechanism and
record that rigidity remains unresolved; compatibility is not existence.

No rank, charge, splitting or cohomology value for the opposite transform
has been calculated in this literature turn. The gate permits a separate
attempt, not a claimed implication. The changed ready assessment receives
the supervisor's separate approval before research.

## Inspected primary statements and essential cases

[Bartocci--Bruzzo--Hernandez Ruiperez, *A hyperkahler Fourier transform*,
Differential Geometry and its Applications 8 (1998), 239--249](https://mat.usal.es/ruiperez/Site/Papers_files/Hyperkahler-Fourier-Mukai.pdf#page=8):
Theorem 3, p. 246, is the preservation input already assessed for L056.
Theorem 4, p. 247, concerns a reflexive K3 with H^2=2, ell.H=0,
ell^2=-12, and every nodal curve of H-degree greater than two. Its kernel
is the normalized universal bundle for the specified instanton moduli
K3; the reversed kernel is its dual. These hypotheses are not supplied
for F. Section 3.3's twistor/direct-image proof proves preservation,
not reconstruction from one transform value.

[Bartocci--Bruzzo--Hernandez Ruiperez, *A Fourier-Mukai transform for
stable bundles on K3 surfaces*, J. reine angew. Math. 486 (1997), 1--16;
inspected preprint alg-geom/9405006v2, 5 August 1996](https://arxiv.org/pdf/alg-geom/9405006v2#page=8):
Sections 3.1 and 4.1 use that reflexive setting, with v=(2,ell,-3).
Section 4.1 normalizes Q to R^1 p_2*Q=O. Its mixed character gamma_(2,2)
has -p_2*(gamma_(2,2)H)=Hhat, a polarization by Proposition 6.
Thus this cited setting has trivial direct image and nonzero mixed
polarization action. It has nonzero fibre determinant ell and transform
rank one: it does not answer L057's exact question. In Section 4.3,
Proposition 10 and Theorem 2 obtain inversion from diagonal-supported
kernel convolution, not flatness. The proof uses the universal-family
Ext calculation and the reversed moduli identification.

[Bridgeland, *Equivalences of triangulated categories and Fourier-Mukai
transforms*, Bull. London Math. Soc. 31 (1999), 25--34;
inspected math/9809114v2, 12 March 2019](https://arxiv.org/pdf/math/9809114v2):
Theorem 1.1 concerns smooth projective varieties of equal dimension
and a vector-bundle kernel. Full faithfulness requires strong simplicity:
simple fibres and every cross-fibre Ext group zero at distinct points.
Equivalence also requires invariance of fibres under tensoring by omega_X.
Corollary 1.2 assumes a fine compact two-dimensional stable-bundle moduli
space. Read the essential Theorems 5.1 and 5.4 proof passages: point-object
Ext and adjunction control the composition. Fibre stability alone and
one trivial transform do not provide the missing cross-fibre hypothesis.
The v2 correction requires flatness in Lemma 4.3; that lemma is not used
as a rigidity input here.

[Bartocci--Jardim, *Hyperkahler Nahm transforms*, math/0312045v1,
2 December 2003, pp. 4--7](https://arxiv.org/pdf/math/0312045v1#page=5):
the remark after Theorem-Definition 3 explicitly allows noninvertibility
and reducible transforms. Its later invertibility discussion uses mutual
instanton-moduli interpretations; Theorem 5 uses the reflexive K3 setting.
Neither is a theorem for the arbitrary F in L056.

[Jardim, *A survey on Nahm transform*, inspected math/0309305v3,
16 January 2004, Section 2, pp. 3--9](https://arxiv.org/pdf/math/0309305v3#page=4):
equations (4)--(8) construct the projected index connection and express
its curvature through Dirac variation and a Green operator. This is a
family of irreducible ASD connections on a fixed bundle with the indicated
Hilbert-bundle trivialization. Proposition 2 adds a commutation hypothesis.
No inspected passage gives a coercive flatness-to-kernel-rigidity theorem
for an arbitrary product kernel. Do not silently apply this expression
as a positive norm or assume its extra connection hypotheses for F.
The PDF's generated title-page date differs from its arXiv version stamp;
the version stamp and numbered equations identify what was inspected.

## Reused tools and remaining applicability

Reuse the [six-charge preservation assessment](2026-10-05-six-charge-direct-image-polystability.md)
for the published arbitrary hermitian quaternionic-instanton kernel
theorem, Stacks 0A1H and 0BDH, and real-metric Hermite--Einstein inputs.
Reuse the [character assessment](2026-10-05-six-charge-surface-character-filter.md)
for relative GRR and surface RR; no coefficient-specific inference is
imported for the opposite projection. The factor interchange changes no
compactness or hermitian hypothesis of the primary preservation theorem,
but IT and actual local freeness must be proved anew. L052's relevant
proof ranges establish connection restriction and the exact line lattice.
Its rank-two stable bound cannot simply be assigned to a higher-rank image.

[Stacks Lemma 20.13.4, Tag 01F2](https://stacks.math.columbia.edu/tag/01F2),
read with its proof, gives E_2^(p,q)=H^p(Y,R^q f_*F) converging to
H^(p+q)(X,F) for a morphism of ringed spaces and a bounded-below complex.
The proof applies the Grothendieck spectral sequence to Gamma_Y composed
with f_*. Both projections and F[0] satisfy the categorical hypotheses;
concentration, degeneration and the resulting values are for the next
attempt. K3 RR, dual stability and Serre duality retain their arbitrary
rank statements from the previously inspected Huybrechts passages.

Essential local inputs are L044, L048, L052, L056 and L057. No global F,
opposite-image stability, universal-moduli property, faithful transform
or transverse transport is a continuation premise. The known example
rejects the unrestricted inference; it neither disproves this fixed
implication nor constructs a compatible product bundle.

## Search, duplication and access record

Queries included `hyperkahler Fourier transform flat transform inverse
Bartocci Bruzzo Hernandez Ruiperez`, `Nahm transform flat index bundle
rigidity curvature kernel K3 arbitrary quaternionic instanton`,
`Nahm transform curvature formula projection kernel flat transform
arbitrary kernel rigidity`, `Bridgeland Equivalences triangulated
categories Fourier Mukai transforms 1999 arxiv theorem 1.1`, and
`site.stacks.math.columbia.edu Leray spectral sequence cohomology Rf
sheaves`. Searches for hyperholomorphic cohomology supplied no inspected
full rigidity theorem; their leads are not inputs. No novelty follows.

Scoped searches of local literature, attempts and history found the
uncovered proposal and preservation coverage, but no completed rigidity
argument. L055's five-charge stop and L057's completed directional filter
are preserved. The opposite projection plus global-cohomology comparison
is not a repetition of either character filter.

Itoh's *Yang-Mills connections and the index bundles* was located via the
Tsukuba repository, whose page fetch failed. It is an unread lead, not
essential to the selected cohomology test. PDF screenshots of the 1996
preprint failed; the complete relevant extracted theorem/proof passages
were accessible. Orlov's derived-equivalence paper was opened only at its
header and is not an assessed input. There is no essential source blocker
for the bounded test. No further browsing is required just to fill a quota.

Mathlib coverage of the full rigidity implication and selected
specialization: **not checked**. This source turn imports and compares known
results only; it derives no new lemma. EXPLORE records an unmatched exact
implication and a ready bounded test, not certified originality. A research
application of the imported tools may be classified REPRODUCTION; any
unmatched stronger implication would require honest scope and review.
