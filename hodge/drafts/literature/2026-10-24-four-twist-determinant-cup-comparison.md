# Four line twists — proposed determinant-cup comparison

TARGET: Assess whether polarized determinant-cup identities for the four coefficients F tensor p_1^*L^epsilon tensor p_2^*L_B^delta, epsilon,delta in {-1,1}, constrain L157's two extremal formal branches.
CHECKED: 2026-10-24
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 516 compared L090's coefficient identity and complete actual counit/trace proof, L157's comparison and extremal branches, the step-219/511 assessments and ATTEMPTS/057,/060,/069,/087,/089; exact determinant/cup/Plucker/polarization and K3 line-transform queries found general machinery but no inspected theorem deciding these four-coefficient branches.
SOURCE_EVIDENCE: Fresh Stacks reads: 20.31.3 (0FP3) statement/adjunction proof, 20.31.8 (0H99) full statement (proof omitted), 15.59 (0GWN) interchange/differential check, 36.23.1 (0FLN) hypotheses and both proof cases, 48.12.4 (0AAB) and 48.7.1 (0B6J) statements/proofs; reuse step-219 Demailly alg-geom/9410022v3 Sections 1.A/4.A and 20.31.7, plus step-511 Pareschi–Popa Lemmas 2.1–2.2, projection/Leray, preservation and duality coverage.
COMPARISON: General results allow arbitrary locally free coefficient pairs, product-line coefficients and compatible relative traces; L157 supplies both opposite powers and line multiplicities. They cover construction/comparison, not a signed polarized rank-two identity or branch verdict. Only these finite data-specific checks require derivation; no general theorem needs reproof.
GAP: Separately check graded determinant identities, actual degree-one identifications and line-valued targets at z=0; decide whether controlled components force incompatibility in either saved branch, retaining other cup components as unevaluated unless independently determined.
REASON: Essential general coverage is ready for one separate bounded REPRODUCTION attempt on the unchanged target; park it if targets force vacuity or an unknown actual global cup value is essential. No identity or compatibility verdict is established in this review.
LITERATURE_REASON: The changed hypothesis is four distinct line-valued coefficient groups and cross-cup maps outside the prior additive or untwisted scope; this turn supplies their source comparison without executing the specialization.
SCOPE: Exactly the four signed coefficients in TARGET, L157's (12,2) and (6,8) formal branches at z=0, the fixed hypothetical equality kernel and preferred line connections; graded determinant products, actual counit/trace comparisons and one finite necessary compatibility test. No general multiplicity optimization, inverse transform, nonempty split locus or new existence mechanism is covered.

## Startup proposal (preserved; source review completed below)

The main gap is universal primitive rational Hodge realization. The
proposed intermediate target is a source-supported, evaluable compatibility
test for the two formal branches (m_-1,m_1)=(12,2) and (6,8) at z=0
in L157. Its plausible use is distinguishing individually compatible image
indices from images of one rank-two kernel. No cup identity, dimension,
nondegeneracy or obstruction for these twists is proved in this proposal.

Retain the identical marked projective K3 factors S_1 and B, common g,h,
fixed chamber and preferred HE lines L,L_B of class k=(-4,-2,1,2),
k.h=0, k^2=-14 eta, integral eta=1. F remains hypothetical, locally
free, rank two, Omega-polystable, integral c_1=0, with full character
2-14e_1-21e_2-tau_D+62P. Z is finite and may be empty. M and H_r are
not assumed simple or self-dual. Independent lower control, nonempty Z,
F existence, transport and universal Hodge realization remain unresolved.

Essential existing inputs to compare are L071 (actual compatible kernel),
L090 (untwisted determinant cup with its actual comparison), L093
(untwisted equality acyclicity), L147 (ordinary M and W), L153 (same-h
polystability), L156 (endpoint/Euler control) and audited L157 (actual
opposite powers, cross-power duality and the two formal branches).
The first read of L090 should target its coefficient-level identity and
actual counit/restriction-to-Serre proof, not unrelated earlier recipes.
Then inspect the necessary primary theorem statements/proof cases, reuse
ready coverage where it truly matches, and search the exact generalized
statement and standard terminology. No cross-notebook input is proposed.
Full matching Mathlib coverage remains unchecked.

The proposed coefficient sheaves are
Q_(epsilon,delta)=F tensor p_1^*L^epsilon tensor p_2^*L_B^delta,
for epsilon,delta in {-1,1}. A later mathematical attempt would have
to identify actual cohomology and cup maps for these sheaves; L157's
one-sign degree-one comparison alone is not declared sufficient.
Keep the line coefficients in every determinant cup and every scalar
Künneth group. Polarizing an untwisted identity is a proposed tool,
not permission to replace these groups by H^2(O_X), invent a perfect
pairing, erase W, or impose self-duality on an individual transform.

Continue only if source comparison identifies a concrete finite
compatibility question with controlled actual input groups and maps.
Abandon this proposed mechanism if all candidate identities are forced
zero by their coefficient targets, or the comparison needs an arbitrary
uncontrolled global cup map. ATTEMPTS/069 warns precisely against
assigning such a map from fibrewise vanishing. ATTEMPTS/060's untwisted
strict-Euler stop remains valid; the changed four-coefficient input,
not a renaming of that argument, must justify any reopening. A failed
search alone would not establish novelty or an obstruction.

This proposal does not reopen L157's completed additive index filter,
prove a stronger spectrum bound, or approve new mathematics during its
audit turn. Source review and any later mathematical test are separate
invocations. The supervisor owns routing and acceptance.

## Completed source comparison — step 516

This is LITERATURE / EXPLORATION / REPRODUCTION. The proposal above
records the questions at entry; the source inspections are now completed
as specified below. No new identity, dimension, nondegeneracy assertion
or branch verdict is established. No lemmas or mathematical scripts change.

**Coefficient products.** Reuse Demailly, *L2 vanishing theorems for
positive line bundles and adjunction theory*,
[alg-geom/9410022v3, 28 February 1995](https://arxiv.org/pdf/alg-geom/9410022v3),
Section 1.A (1.1)–(1.3), printed pp. 4–5, and Section 4.A
(4.3)–(4.4'), printed pp. 27–28, inspected in the
[step-219 assessment](2026-10-11-common-kernel-determinant-cup-square.md).
These cover the coefficient Dolbeault resolution for any holomorphic
vector bundle and the compact-manifold coefficient Serre pairing.
Each proposed coefficient is locally free holomorphic; X and its K3
fibres are smooth projective. The resolution therefore permits these
line coefficients. L090 checks an untwisted rank-two identity, rather
than the proposed four-group statement. Its graded polarization must
be checked separately; ordinary even Plucker signs are insufficient.
No reproof of Dolbeault, GAGA or Serre duality is warranted.

Freshly read [Stacks 20.31.3, 0FP3](https://stacks.math.columbia.edu/tag/0FP3),
including the adjunction proof comparing naive and derived products,
and [15.59, 0GWN](https://stacks.math.columbia.edu/tag/0GWN), including
the signed interchange and differential check. These apply to arbitrary
coefficient complexes, not just structure sheaves. They cover the
passage from coefficient forms to coherent products and the signs,
not a four-coefficient rank-two identity or branch exclusion.

**Actual comparisons.** Reuse
[20.31.7, 0FP6](https://stacks.math.columbia.edu/tag/0FP6), whose
statement and counit-composition proof were inspected in step 219.
A fresh retrieval initially returned the page, but focused retrieval
subsequently timed out; no fresh full proof inspection is claimed.
Freshly read the complete statement of
[20.31.8, 0H99](https://stacks.math.columbia.edu/tag/0H99): relative
cup commutes with the derived base-change transformations in a
commutative square for arbitrary derived coefficients. Its proof is
omitted in the source. Compatibility does not make a base-change map
an isomorphism or evaluate an unknown global cup component.

Reuse Pareschi–Popa, *GV-sheaves, Fourier-Mukai transform, and generic
vanishing*, Amer. J. Math. **133** (2011), 235–271,
[author-hosted version, Lemmas 2.1–2.2 and proofs, pp. 5–6](https://people.math.harvard.edu/~mpopa/papers/GV.pdf#page=5),
and the projection-formula/Leray coverage in the
[step-511 assessment](2026-10-24-double-line-twist-summand-spectrum.md).
Those inputs allow arbitrary bounded coherent inputs on smooth
projective factors and a perfect product kernel. Lines of either sign
and locally free F meet these hypotheses. L157 already checks opposite
concentration and cross-power duality for both r=1 and r=-1 and
records both L and L^{-1} multiplicities. Thus the coverage includes
all four groups via the opposite projection with either target line;
no new preservation theorem or inverse is required. Their
multiplicative identifications remain to be verified mathematically.

At the proposed z=0 branches W is zero by L147, rather than discarded
from a spectral sequence. Extending the test to z>0 would retain W
and is outside this bounded branch test. The positive source-line
coefficient must be treated using actual dual coefficients and
relative duality. Neither M nor H_1 has asserted scalar self-duality;
L157 pairs H_1 with H_{-1}.

**Line targets and traces.** Freshly read
[Stacks 36.23.1, 0FLN](https://stacks.math.columbia.edu/tag/0FLN),
including the projection/base-change proof and affine-complex/gluing
proof. It covers arbitrary quasicoherent derived inputs on
quasi-compact, quasi-separated factors Tor-independent over the base;
its global statement additionally needs an affine base. Here the
base is Spec(C), the factors are smooth projective and all target
lines are locally free. Thus line-valued Kunneth is covered, beyond
L090's untwisted scalar target. Determining which degree-two targets
vanish and which degree-four products survive is future mathematics.

Freshly read [48.12.4, 0AAB](https://stacks.math.columbia.edu/tag/0AAB)
and its affine-reduction proof, and
[48.7.1, 0B6J](https://stacks.math.columbia.edu/tag/0B6J) and its
unit/counit proof. The first covers right-adjoint base change for
proper flat morphisms of finite presentation over quasi-compact,
quasi-separated schemes; the second identifies trace transformations
in Tor-independent squares. Our projections satisfy these hypotheses;
the fibre squares are Tor-independent because the projections are
flat. Use the perfect/coherent setting and the assessed smooth
identification omega_p[2]
([48.15.7, 0BRT](https://stacks.math.columbia.edu/tag/0BRT)). These
support actual restriction-to-trace comparison for dual coefficients.
They do not assert a perfect H^1-by-H^1 pairing on a fourfold, or
perfection on arbitrary spaces of sections. Any needed isotypic
perfection must be checked using the actual cross-power form.

## Discovery, duplicates and remaining mathematical work

Queries on 2026-10-24 included `rank two vector bundle cohomology
cup product Plucker relations determinant H1`, `polarized determinant
cup square identity rank two bundle Dolbeault line bundles`,
`"determinant" "cup product" "Plücker" "cohomology"`,
`"rank two" "cup" "square" "line bundles"`,
`"rank two" "cohomology" "polarization" "Plucker"`, and
`"K3" "line" "cup product" "Fourier" rank two`.
The general product/sign/Kunneth/trace sources above are the inspected
theorem evidence. Results about curve-moduli cohomology, ordinary
Grassmannian Plucker equations and Reider's surface cup invariant
remain uninspected leads; none is imported or treated as a matching
fourfold theorem. No inspected source decides these branches, which
establishes no novelty.

Scoped reads included L090's identity and complete actual counit/trace
proof with audit, L157's hypotheses, double-twist comparison, full line
multiplicities and both branch descriptions, the step-219/511
assessments and step-513/514 source qualifications. Searches in the
named endpoint assessment and L117 checked the global-map failure.
ATTEMPTS/057,/060,/069,/087,/089 preserve the earlier untwisted
strict-Euler, uncontrolled global entry and additive-index stops.
Those results neither approve nor exclude this four-group question.
A different input is simultaneous multiplication for coefficients
of the same rank-two F; repeating the old spectrum calculation would
not test it. No source claims an otherwise unknown global map is
fixed by fibrewise vanishing.

The approved separate attempt keeps TARGET unchanged. First verify
the actual four degree-one identifications from L157's opposite powers
and full line isotypic pieces at z=0. Form determinant cups with their
tensor-product target lines. Use line-valued Kunneth before asserting
zero or scalar targets. Check any polarized rank-two formula and its
signs in the coefficient resolution. No such formula is established
here. Compare only components controlled by the actual counit and
cross-power trace maps.

The finite question is simultaneous compatibility of those necessary
identities and controlled components in each of the two saved branches.
Unknown cup components may remain universally quantified in a finite
necessary-constraint relaxation: a contradiction must hold for every
assignment. A compatible assignment is neither the actual cup map nor
a bundle construction. Park the mechanism if the relaxation is
compatible, if all usable targets vanish, or if a verdict requires
choosing an unevaluated actual global map. This is one bounded test,
not permission to pursue unspecified extra maps after a stop.

A restriction could inform common-kernel existence beyond additive
indices. Essential inputs remain L071, L090's coefficient/counit
method (not its different Chern-data exclusion), L093, L147, L153,
L156 and audited L157. Fixed metrics, full tensor, preferred lines,
rank, local freeness and conditional polystability remain assumptions.
F, a nonempty split set, lower control, transport and universal
primitive Hodge realization remain unresolved. No cross-notebook
input is used. Full matching Mathlib coverage is not checked;
abstract algebra alone would not certify the geometric comparisons.
The supervisor owns separate approval and routing of this ready
continuation. No new mathematics was derived during this review.
