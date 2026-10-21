# Charge-seven connection/metric rigidity — source comparison

TARGET: Test whether the hyperholomorphic connection on L060's F forces L063's classifying map to be totally geodesic for the natural L2 metric.
CHECKED: 2026-10-07
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Scoped L052/L060/L062/L063 and ATTEMPTS/046; reused preservation, moduli-naturality and prior trianalytic-exclusion assessments; bounded exact-statement and stronger-result searches located Verbitsky's local L2 moduli construction and hyperkahler-embedding geodesy theorem, whose hypotheses and relevant proofs were read below.
SOURCE_EVIDENCE: Verbitsky alg-geom/9307008v1 (29 July 1993), Definition 2.1, Theorems 2.2--2.4, Definition 6.3/Theorems 6.1 and 6.3--6.4, Section 7 opening, Section 9 including Proposition 9.1, and Corollary 10.1, PDF pp. 5--8, 22--25, 34--37; Verbitsky alg-geom/9610010v1 (9 October 1996), Proposition 4.1/Definition 4.2, Propositions 5.1--5.2, Definition 5.3/Corollary 5.4 and Appendix 5.3 proof, PDF pp. 21--22, 29--31.
COMPARISON: Known results cover the local natural L2 hyperkahler moduli and total geodesy after hyperkahler-embedding hypotheses are verified; they do not directly state the fixed-metric charge-seven family specialization. Symplectic immersion and generic degree one alone do not verify those hypotheses.
GAP: Identify the same actual classifying germ under simultaneous induced-complex-structure rotation, verify its quaternionic differential and pullback metric, and distinguish geodesy of a local image from geodesy of the parametrized map at the fixed source metric.
REASON: Essential connection/metric source coverage is now available for a separate applicability attempt; import the general theorems without reproof and test only the stated family-to-moduli and metric differences.
SCOPE: Conditional L044/L052/L060 actual hermitian hyperholomorphic rank-two kernel at the unchanged common hyperkahler metric; locally free stable charge-seven fibre locus, L062 injective differential and L063/L064 actual coarse map. Covers rotation/naturality, local L2 metric, induced-metric versus fixed-metric geodesy and the published hyperkahler-embedding criterion. No global separation, target completeness, reconstruction, F existence or transverse transport is covered.
LITERATURE_REASON: The saved target was REVIEW_REQUIRED and changed from relative-Hom linearization to connection/metric geometry; the essential local moduli-metric and geodesy sources had not been inspected for it.

Retain L060's conditional F on B x Y with the specified common metric,
c_1=0 and ch_2=-6e_1-7e_2+tau_D, carrying L044. L062 supplies the
nonzero form, L063 the common-H map, L064 its differential and L065
only the normalization. L066 leaves off-diagonal jumps open. Neither
F existence, metric compatibility, triholomorphicity of the map, total
geodesy, target metric completeness nor global injectivity is assumed.

This intermediate target is independently testable through the actual
classifying map's connection geometry. A positive result might support
a later rigidity or branch-identification test; that downstream use
is unproved. Total geodesy alone is not being called separation or
reconstruction. F existence, reconstruction, transverse transport and
universal primitive Hodge algebraicity remain open.

The continuation threshold is a rigorous applicability argument for
the actual family, yielding zero second fundamental form and, if claiming
geodesy of the parametrized map at the fixed source metric, the necessary
metric/connection comparison. Stop or narrow that inference if rotation
does not identify the same germs, irreducibility is unavailable, or the
metric comparison fails. Do not add those as hypotheses silently.
No such specialization, metric calculation or new lemma is proved in
this literature-only turn. The assessment approves the attempt's scope,
not its outcome.

## Primary coverage inspected

[Verbitsky, *Hyperholomorphic bundles over a hyperkahler manifold*,
arXiv:alg-geom/9307008v1](https://arxiv.org/pdf/alg-geom/9307008v1),
29 July 1993. Definition 2.1 describes a compatible hermitian connection
integrable for every induced complex structure. Theorems 2.2--2.4 give
the irreducible Hermite--Einstein/stable correspondence, zero contraction
for hyperholomorphic curvature and the surface case. Definition 6.3 and
Theorem 6.1 provide local coarse classifying maps and the Ext tangent.
Theorem 6.3 supplies the hyperkahler moduli structure; the surface
smoothness qualification follows Theorem 6.4. Section 9 defines its metric
by integration of pointwise pairings of harmonic representatives, checks
quaternionic compatibility and identifies the holomorphic symplectic form
in Proposition 9.1. Corollary 10.1 compares induced complex structures
through the same connection moduli. Read these statements and the
Section 9 proof, pp. 34--37, plus Section 7's connection-moduli
identification, pp. 24--25. This is local smooth L2 coverage, without
compactness or completeness of the full stable locus.

[Verbitsky, *Deformations of trianalytic subvarieties of hyperkahler
manifolds*, arXiv:alg-geom/9610010v1](https://arxiv.org/pdf/alg-geom/9610010v1),
9 October 1996. Proposition 4.1 and Definition 4.2 relate geodesy to
parallel preservation of the orthogonal tangent/normal splitting.
Definition 5.3 requires both quaternionic and metric compatibility for
a hyperkahler embedding; Corollary 5.4 makes it totally geodesic.
The ambient manifold need not be compact. Read Propositions 5.1--5.2
and Appendix 5.3's proof through its conclusion, pp. 29--31: all relevant
induced connections are hyperholomorphic, and zero curvature contractions
force the second fundamental form to vanish. This is not a theorem for
an arbitrary holomorphic symplectic immersion. The printed Proposition
5.5 omits an ambient Yang--Mills assumption used explicitly in its proof
(zero contraction of the middle curvature). Do not import that broader
wording; Proposition 5.2's stronger all-hyperholomorphic hypotheses supply
the needed zero contractions. The retrieved text contains broken equation
formatting; no reconstructed signed formula is used here. PDF screenshot
calls returned no usable image in this interface. The full relevant text
of the proof and its hypotheses, rather than previews, was read.

## Reused coverage, differences and proposed applicability test

Reuse the [factor-restriction assessment](2026-10-04-corrected-rank-two-factor-restrictions.md)
and [six-charge preservation assessment](2026-10-05-six-charge-direct-image-polystability.md).
L052 supplies the actual product connection and invariant-curvature
restriction mechanism; L060 supplies stable charge-seven restrictions.
The new task must check irreducibility of those restrictions under
rotation using the connection/stability correspondence. Stability for
one holomorphic structure is not simply declared stable for another.
The Nahm preservation theorem supplies no metric identity for this
classifying map and is not used to replace that check.

Reuse the natural family/coarse Ext tangent and exact GAGA/Dolbeault
coverage in the [L064 audit assessment](2026-10-07-charge-seven-finite-unramified-critical-audit.md).
L062's equation (4a) already identifies the mixed curvature representative
with the actual Kodaira--Spencer class; it does not make that representative
harmonic. The attempted quaternionic comparison must occur in the
appropriate deformation quotient/harmonic tangent, retaining gauge terms
and the source's conjugate-(1,0) convention. Alternatively, use local
classifying germs for every induced complex structure and the inspected
connection-moduli identification, explicitly checking that they are the
same underlying map. These are alternative checks of one bridge, not
independent new targets.

The intended specialization must distinguish the fixed metric at h from
the auxiliary integral H of L063. Work in the h-stable, locally free
analytic locus near each image point; identify that germ with the germ of
the algebraic coarse map. No metric associated with H is substituted for
the instanton L2 metric. K3 simplicity/trace-free unobstructedness must be
retained when asserting a smooth target chart. No global universal sheaf
is required: the actual family and local coarse charts suffice.

Use L062/L064's injective differential to work with local embedded
branches only. Before invoking Corollary 5.4, verify the induced metric
and all quaternionic structures on each branch. Before claiming the
parametrized map is totally geodesic for the original metric on B, check
that its pullback metric has the same Levi--Civita connection. The fact
that B has quaternionic dimension one is relevant to that bounded
comparison, but no homothety or scale is derived here. L062's signed
ordered Yoneda form is not a positive Riemannian metric; an arbitrary
normalization of sigma is not a metric normalization. Do not reprove the
general geodesy theorem or interpret its source proof's missing hypothesis
as permission for a stronger splitting claim.

Neither local geodesy nor a metric comparison alone proves global
injectivity. L065 identifies only the normalization; isolated point
identifications and the actual higher Hom differential remain unresolved.
Do not use completion, convexity, simply connectedness of the target,
image normality or a global embedding as premises. A later branch test
would require its own assessed target. F existence and the universal
Hodge gap are separate even if this entire conditional step succeeds.

## Duplicates, obstructions and bounded discovery record

L062--L066 and ATTEMPTS/046 contain no proof of rotation-compatible
classifying maps or L2 geodesy. Their positive differential and
normalization constraints are reused; the Euler/sheaf/linearized-Hom
route remains stopped. The parked flat-index curvature target in
[its assessment](2026-10-06-flat-index-curvature-detection.md) requires
a different unread index formula and sign/detection mechanism. It is not
an essential source for the present local moduli-metric test; no renewed
Itoh access search was made.

Reuse the prior [universal-sheaf assessment](2026-10-03-cubic-rm-universal-sheaf-map.md)
and its source discussion: Verbitsky
alg-geom/9705004v2, Theorem 1.1, PDF p. 4, excludes trianalytic subvarieties
only under its automorphism-free, Mumford--Tate-generic K3 hypotheses.
Those hypotheses were not established for this projective RM surface.
The theorem's source was located again; its prior inspected comparison
is reused, not upgraded to an obstruction on this target. General
position must not be added to evade the actual marked metric.

Queries performed: `hyperholomorphic bundle family classifying map
triholomorphic totally geodesic moduli`; `Verbitsky hyperholomorphic
bundles classifying map trianalytic L2 metric`; `"hyperholomorphic"
"classifying" "map"`; `"quaternionic" "families" "moduli"
"triholomorphic"`; `"hyperholomorphic" "family" "totally geodesic"`;
`"hyperholomorphic" "family" "moduli" "map" trianalytic`;
`"triholomorphic maps" "totally geodesic" hyperkahler`;
`"instanton" "classifying map" hyperkahler`; `"family"
"quaternionic instantons" "map" "moduli"`; `"hyperholomorphic"
"map" "moduli space" "product"`; and `"hypercomplex" "maps"
"Obata" "connection" preserves`.

The last searches found Obata-connection and physics terminology leads;
no Fueter-type notion called triholomorphic is substituted for commuting
with each I,J,K. Those snippets are not theorem evidence and no general
map-affineness theorem is imported. Bartocci--Jardim,
[math/0312045v1](https://arxiv.org/pdf/math/0312045v1), Section 4,
printed pp. 6--8, was checked as a stronger moduli/invertibility lead:
its component hypotheses and reflexive-K3 example do not identify this
two-dimensional image with a full charge-seven moduli component. No
invertibility conclusion is imported. The inspected sources cover the
general machinery, not a published theorem evaluating this exact F.
Absence of an exact match establishes no novelty.

Mathlib coverage of the local instanton L2 metric, rotation bridge and
total-geodesy specialization: **not checked**. This is not evidence of
absence. A subsequent successful specialization should be classified
REPRODUCTION, with full applicability in its canonical lemma and precise
citations to the imported theorems.
