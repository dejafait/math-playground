# Twisted middle sheaf — proposed global character comparison

TARGET: Determine the global Chern character of R^1p_{2*}(F tensor p_1^*L^{-1}), justifying local freeness and retaining every split-point correction and the integral first Chern class.
CHECKED: 2026-10-22
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched K3 twisted higher-direct-image/Chern-character and cohomology-jumping terminology, general coherent GRR, and endpoint support; compared L071/L094/L096/L145/L146, October 12 IT/effectivity reviews, ATTEMPTS/060 and October 5/17 GRR assessments. No exact whole-base formula was identified; general GRR covers its framework.
SOURCE_EVIDENCE: Inspected live Stacks 0A1H and 0BDK statements and applicable proof cases, and the restricted statement 02UO; inspected Grothendieck SGA 6 Expose 0 Section 1 (1.1)-(1.3) in its online text edition; reused inspected Fulton (1998) Theorem 15.2 pp. 286-287 and Example 15.2.8 pp. 291-292. Inspected Huybrechts K3 draft Chapter 1 Section 3.2 (3.1), printed p. 15, and reused Chapters 1/9 stability-duality coverage.
COMPARISON: General coherent GRR permits non-locally-free higher images; Stacks 02UO alone does not. Perfect concentration covers the stable open, while audited L145/L146 cover selected actual split stalks. Their whole-base assembly, alternating point corrections and integral first-class recovery remain the exact specialization to perform.
GAP: No essential source coverage is missing for the scoped bookkeeping attempt; endpoint support, vanishing of the ordinary degree-zero sheaf, global freeness and the full cohomological evaluation remain unproved mathematical obligations. No image positivity, kernel existence or Hodge realization is covered.
REASON: Separate whole-base theorem comparison is now complete and corrects the proposed reliance on a restricted GRR statement; import general theorems without reproof and attempt only the specified specialization next turn.
SCOPE: Same hypothetical locally free rank-two Omega-polystable F on identical marked K3 factors/common metric, integral c_1(F)=0, ch_2(F)=-14e_1-21e_2-tau_D, and fixed c_1(L)=k=(-4,-2,1,2); allow the split locus to be empty and assume no polystability or scalar self-duality of the twisted middle image.

The main gap remains universal primitive Hodge realization. F existence
is independent. The intermediate target is the actual ordinary middle
sheaf's global character, not the sign of a virtual class presented as
effectivity. Such bookkeeping could make a later geometric inequality
test precise, but no positivity theorem for this image is supplied.

Essential proposed inputs: L071's full kernel character and factor
classification, L096's finite possibly empty split locus, L094's fixed
line cohomology, L145's whole top stalk and L146's audited whole middle
stalk/canonical hull map. The global support and concentration bridges
remain mathematical obligations, not consequences asserted by this review. Retain
the full mixed tensor, actual rank-two higher characters, relative Todd
class, alternating pushforward sign and every point contribution.
Integral first-class recovery needs its own stated justification.

The proposal above was REVIEW_REQUIRED at invocation start. The source
comparison below now supplies SPECIALIZE coverage for exactly TARGET.
It approves an attempt, without certifying any global character or novelty.

The continuation test is whether the actual sheaf, endpoint support
and integral character can be justified with the audited local inputs.
If an essential bridge fails, state that missing bridge. Passing this
test supplies bookkeeping only, without a contradictory inequality.
The October 12 IT and automatic-effectivity stops, ATTEMPTS/060's
strict untwisted Euler stop and the necessary-jet stop remain in force.
The selected point in L146 is conditional; neither F nor any split
point is asserted to exist. Global positivity, reconstruction,
transport and the universal target remain open. Full matching Mathlib
coverage is not checked. No cross-notebook input is proposed.

## Completed source comparison (2026-10-22, step 468)

**Exact scope and downstream test.** Determine the entire rational
cohomological character on B, together with its integral first Chern
class, of the ordinary middle image. This is not a Chow-character
computation from cohomological data. A subsequent inequality would
need an independently covered geometric hypothesis. Continue if the
whole-base support/freeness assembly works with the retained local
inputs; stop that assembly at any unsupported endpoint or stalk bridge.
Passing this test gives bookkeeping only. No numerical evaluation,
new lemma, or mathematical script is supplied in this literature turn.

**Perfectness and concentration.** Reinspected [Stacks Lemma 36.30.1,
0A1H](https://stacks.math.columbia.edu/tag/0A1H): finite-presentation f,
perfect E and bounded finitely presented base-flat coefficient complex
with proper support give perfect pushforward and arbitrary derived
base change. Use E=O and the locally free twisted coefficient for the
smooth projective projection. The Noetherian proof case applies;
its further approximation argument is unnecessary. Reinspected
[Lemma 36.31.3, 0BDK](https://stacks.math.columbia.edu/tag/0BDK),
including its proof: remove non-middle derived-fibre cohomology first,
then finite local freeness follows and fixed rank defines open pieces.
This is stable-open coverage, not whole-base IT or ordinary split-point
base change. Reuse the minimal-complex coverage in the L145/L146
assessments for the remaining stalks.

**Endpoint and gluing obligations.** L071 classifies the charge-fourteen
fibres; L096 supplies a finite, possibly empty Z. Use the actual
h-stable fibres on B minus Z and the fixed degree-zero line twist,
with slope stability and Serre duality at that same real metric, to
test both endpoints. Reuse the assessed surface tools in
`2026-10-12-equality-split-fibre-line-twist.md` and
`2026-10-08-sign-reversed-six-charge-character-filter.md`.
This is a slope test, not a Fourier-transform IT theorem at Z.
For the degree-zero ordinary sheaf, the research proof must distinguish
a derived split-fibre section from an actual local section: use a
finite-free representative in nonnegative degrees and its degree-zero
kernel, with the stable-open vanishing, rather than declaring base
change at Z. Nonnegative amplitude comes from the fibre cohomology
and the already assessed minimal-perfect-complex construction.

For the top sheaf, establish its whole support before assembling the
actual L145 length-one stalks; do not substitute central fibre dimension
for length. For the middle sheaf, combine stable-open concentration
with L146 at every actual split parameter and justify that freeness
at all closed points covers the entire coherent sheaf. These are
ordinary algebraic stalks on the same smooth base, so intrinsic
cohomology sheaves and canonical hull maps supply the overlap data;
no chosen local bases need compatible transition choices. The review
licenses these checks, not a conclusion that they have been carried out.

**GRR with point sheaves.** [Stacks Section 42.66,
02UO](https://stacks.math.columbia.edu/tag/02UO) assumes locally free
higher direct images and defers a general proof. It cannot alone
justify a formula retaining nonzero point sheaves. Reuse the general
proper-morphism theorem on nonsingular varieties, Fulton,
*Intersection Theory*, second edition (1998), Theorem 15.2,
pp. 286-287, and Example 15.2.8, pp. 291-292, already inspected in
`2026-10-05-six-charge-surface-character-filter.md` (which retains
its scan-host qualification), and reused in
`2026-10-17-opposite-global-normal-character.md`.

As a primary statement check, read Grothendieck, SGA 6, Expose 0,
Section 1, formulas (1.1)-(1.3), [online text edition](https://grothendiecksga.com/read/sga6/fr/0.html).
For a proper map between smooth quasi-projective schemes over a field,
it states GRR for a coherent coefficient, defines pushforward by the
alternating coherent higher-image classes, and gives the relative
virtual-tangent version. This is a statement check; no claim to a new
inspection of its general proof is made. The retained Fulton proof
coverage supplies that input. Here both schemes are smooth projective
over C. The relative tangent is that of the first K3 factor. Neither
an algebraic choice of the real polarization nor local freeness of
every higher image is required by this general theorem.

The research calculation must expand the fixed line exponential and
L071's full rank-two character through all surviving degrees, retain
the full mixed tensor and its square, and use the relative Todd class.
It must then recover the ordinary middle class from the alternating
coherent pushforward, retaining each actual top point contribution
with its sign. Any hull correction must be justified by L146 rather
than introduced as a new unknown defect. No ordinary twisted scalar
self-duality is available. There is no reason to reprove GRR.

**Integral first class.** Reinspected Huybrechts, *Lectures on K3
Surfaces*, author-hosted prepublication draft, [Chapter 1, Section 3.2,
(3.1), printed p. 15](https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf#page=15):
the exponential sequence gives Picard injection into integral H^2 and
torsion-freeness of H^2. Reuse Proposition 2.4 and the assessed duality
and stability inputs at the locations above. After computing the
rational first character, the research step must identify its proposed
integral representative using this injection and torsion-freeness.
Zero slope alone does not do this. No determinant or first class has
been computed in this review.

**Duplicates, limits and Mathlib.** The exact-phrase queries were
“K3 twisted higher direct image Chern character”, “K3 twisted direct
image split”, and “K3 cohomology jumping Chern character”; broader
queries targeted coherent GRR and pushforward endpoint support.
Returned Brill-Noether surveys, a Teleman torsion paper and rank-two
Fourier-Mukai classification leads were not read as theorem inputs.
No novelty is inferred from search results. Known coherent GRR is
stronger than the required virtual bookkeeping; the actual ordinary
sheaf identification remains a specialization using local notebook
results, not an uncovered general theorem.

The October 12 IT and automatic-effectivity stops and ATTEMPTS/060
remain unchanged. L145/L146 already contain the local conclusions;
do not duplicate or reprove them. This target supplies neither
polystability nor a positive metric on the twisted image. Kernel and
split-locus existence remain hypothetical, as do positivity,
reconstruction and transport. The universal primitive Hodge gap is
unchanged. Full matching Mathlib coverage was not checked; supporting
local algebra is as recorded in the canonical input files. No
cross-notebook input is used.
