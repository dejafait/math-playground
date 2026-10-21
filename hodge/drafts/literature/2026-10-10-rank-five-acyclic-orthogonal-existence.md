# Exact-metric rank-five orthogonal block — completed existence comparison

TARGET: Determine whether L079's acyclic stable orthogonal rank-five block J_5 exists at the exact metric h.
CHECKED: 2026-10-10
DECISION: EXPLORE
SEARCH_EVIDENCE: Scoped L079/L052 and ATTEMPTS/043,/045,/053 comparison; exact rank-five/charge-ten, K3 orthogonal and symplectic existence, principal-bundle nonemptiness and orthogonal-deformation searches. Primary statements and inspected cases below; no full matching existence or all-obstruction-class exclusion was identified.
SOURCE_EVIDENCE: Balaji JDG 76 (2007), Theorems 1.3/7.10 and proof pp. 355,394--396, with JDG 83 (2009) addendum pp. 461--463; Bandiera--Manetti--Meazzini 1907.10690v2, Theorems 2.3,3.8,5.1, Example 3.2 and complete Theorem 5.1 proof, pp. 5--8,15; reuse assessed Yoshioka locally-free/slope inputs and Greb--Toma Theorem 6.6 real-stratum coverage.
COMPARISON: General principal-bundle existence is asymptotic and does not reach exact charge ten; ordinary K3 sheaf nonemptiness does not impose a quadratic form. Reductive-automorphism formality and its split-subalgebra transfer offer a different bounded deformation mechanism, without asserting a stable orthogonal deformation or acyclicity.
GAP: Construct an exact-h locally free seed and test its form-preserving deformations; retain genuine realization, underlying-vector slope stability and acyclicity as separate obligations. No inspected theorem decides the full rank-five target.
REASON: The bounded discovery comparison is adequate for one separate existence attempt under the scope below; cite general results and prove their applicability. This is EXPLORE, not a novelty claim or an existence theorem; the audited necessary-test stop is preserved.
LITERATURE_REASON: Changed holomorphic rank-five existence hypotheses required new primary principal-bundle comparison and previously unread formality-transfer/reductive-automorphism statements; the old fourfold formality comparison did not cover this surface target.
SCOPE: L079's marked K3 S, exact h, rank-five symmetric O-valued locally free J, integral c_1=0,c_2=10 eta, h-slope stability and acyclicity, with all obstruction classes allowed. One bounded construction attempt may first test E with rank 2,c_1=k,ch_2=-5 eta and the proposed seed O_S plus E plus E^vee, then its orthogonal deformation equations using the cited split-subalgebra/formality tools. Seed existence, deformation realization and stability are unproved; no generic-polarization, spin, image, common-kernel or inverse assumption is approved.

The main gap is universal primitive Hodge-class algebraicity, with
compatible kernel construction unresolved. The intermediate target
tests whether one necessary building block of L079's t=1 branch is
geometrically available. Its downstream use is deciding whether that
branch merits any later compatibility or kernel-construction work.
Even existence of J supplies neither G nor F nor a Hodge cycle; a
negative answer removes only the t=1 branch, leaving t=2 separately.

Continuation test: continue the proposed construction only if its seed
is locally free and stable at exact h and its deformation model actually
preserves the perfect O-valued quadratic form. A seed lemma or a justified
deformation-model lemma is useful even if independent realization or
stability gaps remain. A formal Maurer--Cartan point or a simple principal
bundle alone is not the required stable vector bundle. Abandon this
specific recipe if the seed cannot be obtained under the cited hypotheses
or the form-preserving model has no admissible deformation. Such a failure
is not nonexistence of all J. Do not restart the exhausted index tests.

Inputs to retain are L079 for the candidate block and necessary-test
stop, L071 for the conditional product setting, L052 for the exact
zero-slope lattice, and L059 only for real-reduction conventions.
ATTEMPTS/043 and /045 concern different ranks/data and preserve the
failure of repeated characteristic/lifting-index tests. ATTEMPTS/053
stops the present summand/index exclusion route. This proposed target
asks about holomorphic block existence, not another run of those tests.
The flat (-10,-17) source blocker remains parked. No cross-notebook
input is used. The exact TARGET is unchanged; this turn completes its
separate literature gate, without attempting the proposed construction.

## Primary comparison and reuse

**Asymptotic existence.** V. Balaji, *Principal bundles on projective
varieties and the Donaldson--Uhlenbeck compactification*, JDG 76
(2007), 351--398,
[Theorems 1.3 and 7.10, pp. 355,395--396](https://www.cmi.ac.in/~balaji/Publications/PrincipalBundlesOnProjectiveVarietiesAndDonaldson-UhlenbeckCompactification.pdf#page=45),
gives nonemptiness for sufficiently large characteristic classes on a
smooth complex projective surface, for semisimple structure group.
Read the principal-SL2 proof and its reference to Proposition 7.6.
The bound is polarization-independent but does not identify this
rank-five vector representation's charge ten as admitted, prescribe its
obstruction class, or assert acyclicity. Principal stability also needs
comparison with the required underlying-vector stability.

Read the complete
[2009 addendum, JDG 83, 461--463](https://www.cmi.ac.in/~balaji/Publications/Addendum-PrincipalBundlesOnProjectiveVarietiesAndDonaldson-UhlenbeckCompactification.pdf).
It repairs the omitted torus-normalizer monodromy case using a
Prym-dimension bound and differential surjectivity of restriction for
large charge. It remains asymptotic. Do not import the uncorrected
countability argument or extrapolate its SL2 threshold to SO5.
Balaji--Parameswaran's 2011 Theorem 3 and Section 10 were inspected as
discovery leads; their positive-characteristic/full-holonomy construction
adds no exact charge-ten conclusion and is not an input here.

**Formality tools, not orthogonal existence.** Bandiera--Manetti--Meazzini,
*Formality conjecture for minimal surfaces of Kodaira dimension 0*,
Compositio Math. 157 (2021), 215--235;
[postprint 1907.10690v2, 2 August 2020](https://arxiv.org/pdf/1907.10690v2).
Read Theorem 5.1 and its entire proof, p. 15: on a complex projective
surface with trivial canonical bundle, a coherent sheaf with linearly
reductive automorphism group has formal derived-endomorphism DG Lie
algebra. The proof uses equivariant resolutions, cyclic trace/Serre
duality and rational finitely supported representations.
Theorem 2.3, pp. 5--6, transfers formality from L to an injective
DG Lie subalgebra M when M splits off as an M-module.
Theorem 3.8, p. 8, requires a quasi-cyclic algebra of degree n<=2
and splitting L=H+d(K)+K: H has no negative degrees, H^0 is a
Lie subalgebra, and H^i,K^i are H^0-submodules for i>0.
Example 3.2, p. 6, identifies the quadratic Maurer--Cartan map with
the symplectic-representation moment map. These are possible inputs;
the seed's reductivity, skew-adjoint splitting and actual deformation
bridge must be justified. No orthogonal formality specialization is
derived here.

The earlier
[fourfold comparison](2026-09-27-two-way-rotation-yoneda-products.md)
already inspected Theorem 1.1; its ambient-dimension mismatch concerned
sheaves on S x S, not bundles on S. This is changed applicability,
not reversal of that evidence. Budur--Zhang, 1803.03974, Theorem 1.2
and its Fourier--Mukai proof cases were inspected as a comparison;
ample-line-bundle polystability cannot silently be replaced by slope
polystability at irrational h. Use the stronger explicit reductive-group
hypothesis above after verifying it, not that shortcut.

**Seed and real polarization.** Reuse
[the existing factor-existence assessment](2026-10-05-minimal-survivor-stable-factor-existence.md):
Yoshioka math/9907001v2, Theorem 0.1, Proposition 0.5, Section 1.1
and Lemma 1.5, with the recorded primitive/local-freeness qualifications;
Ellingsrud--Lehn Theorem 1 is available only if a point-defect bound
is needed. These general results do not assert the proposed E at h.
Check its Mukai hypotheses, admissible polarization and local freeness
rather than reuse L053's different numerical conclusion.
Reuse
[the real-stratum assessment](2026-10-06-charge-seven-uniform-polarization-placement.md):
Greb--Toma, Algebraic Geometry 4 (2017), 40--78, Theorem 6.6,
pp. 73--74, gives uniform slope stability on the same chamber stratum
for fixed invariants over a compact real ample set, including faces.
Check seed and rank-five invariants separately. Neither a nearby open
chamber nor an integral ray of arbitrary choice proves stability at h.
The existing K3 RR, dual-stability and parallel-morphism coverage is
reusable; no reproof of these general theorems is warranted.

Reuse the Bhosle and Abuaf--Boralevi comparisons in
[the orthogonal assessment](2026-10-05-flat-transform-orthogonal-residual.md).
Their even-rank/double-plane/line-valued-form and P^2 hypotheses,
respectively, do not cover this block. Yoshioka's twisted ordinary-sheaf
nonemptiness, already reviewed for L061, supplies no symplectic
structure on a spinor lift; no vanishing Brauer class is assumed.
Cadek--Vanzura remains a topological theorem only.

## Discovery evidence and permitted attempt

Queries included `"K3" "orthogonal bundles" existence`,
`"symplectic bundles" "K3 surfaces"`, `"SO(5)" stable bundle`,
`"orthogonal" "bundle" "K3" "rank 5"`,
`"orthogonal" "K3" "c_2" "10"`, principal-bundle existence on
surfaces, and orthogonal deformation/formality. Theorem statements,
not snippets, support the comparisons above. Rank-five tautological
bundles on spinor Grassmannians and real structures defined by an
antiholomorphic involution appeared in search results; they were not
inspected as matching theorems and are not inputs. A failed search
does not certify novelty or nonexistence.

Local exact-term searches in assessments, canonical lemmas, attempts
and histories found the older formality comparison and the preserved
necessary tests, but no recorded construction of this J. Read L079's
candidate/Schur/topology ranges, L052's setting, and ATTEMPTS/043,
/045,/053. The proposed seed uses the rank-two character already
present in L079's different t=2 formal alternative; that numerical
compatibility is not seed existence. Moving to deformations of an
actual orthogonal seed is a different mechanism from repeating indices.

One separate mathematical turn may test the seed and its orthogonal
deformations under SCOPE. Import the cited tools, justify all
specializations and stop at the first unsupported bridge. In particular,
formality does not by itself produce an analytic/algebraic bundle,
local freeness, vector slope stability or acyclicity. Preserve unfinished
reasoning if the bounded step establishes only an intermediate input.
Any genuinely changed construction requiring essential unread sources
needs a new REVIEW_REQUIRED assessment. No seed, J, image or F was
constructed in this literature-only turn; the universal Hodge gap and
attained cycle span are unchanged.

Full matching and supporting Mathlib coverage: not checked. No full
matching theorem was established in the inspected mathematical sources;
this does not assert Mathlib absence. No lemmas, mathematical scripts,
DAG edges or PROOF.md argument were changed.
