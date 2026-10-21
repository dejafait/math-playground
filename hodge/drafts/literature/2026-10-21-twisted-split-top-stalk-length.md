# Twisted split-fibre top stalk — completed source comparison

TARGET: Assess whether R^2p_2*(F tensor p_1^*L^{-1}) has length one at an actual split equality fibre, using L134's weight-rank conclusion and retaining cohomology jumps.
CHECKED: 2026-10-21
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched fixed-tensor Dolbeault-module, first-order cup-product/cohomology-jump, split K3 line-bundle and length-one terminology; compared ATTEMPTS/060, the 2026-10-12 IT/effectivity screens, L110 and L134. Primary discovery/comparison identifies Budur–Wang Remark 6.5 as the arbitrary-bundle coefficient coverage; no exact family-specific length theorem was identified.
SOURCE_EVIDENCE: Budur–Wang 1309.2264v2, Definitions 3.2/3.8, boundedness assumption, Proposition 3.10/Lemma 3.11, Theorem 6.4 with proof (9)–(10), Remark 6.5 and Theorem 1.3 hypotheses inspected; Stacks 0A1H, 0BCC, 0BCD, 0117, 00DV, 0B6S and 0G81 statements and relevant proof cases inspected; Huybrechts K3 draft Chapter 1 Section 2.3/(2.5), pp. 11–12 inspected. Reuse the recorded FIM and exact GAGA coverage within scope.
COMPARISON: General results cover the actual defining-module coefficient deformation even at a nonsimple positive-charge fibre, derived base change, minimal presentations, dual-coefficient cup/trace and Nakayama. L134 supplies the actual two weight ranks. Unlike L110's adjoint case, the one-sided action and its correct dual must still be specialized; no source states this stalk's length.
GAP: The mathematical attempt must identify the actual degree-one-to-two connecting map with the last minimal differential, compute its full cotangent rank with the twisted coefficient, and justify control of the entire ordinary cokernel. No map, twisted fibre dimensions, rank or length is computed in this literature turn.
REASON: Essential coefficient coverage is available, especially the explicit arbitrary-bundle extension in BW Remark 6.5. Approve only the unchanged local length test as a known-tool specialization; retain the IT/effectivity stops and leave F, split-locus nonemptiness and global defect comparisons unresolved.
SCOPE: Hypothetical locally free rank-two Omega-polystable F on the identical marked K3 product at the common metric, integral c_1=0 and ch_2=-14e_1-21e_2-tau_D; p_2 has charge-fourteen fibres, c_1(L)=k=(-4,-2,1,2), and a selected actual split fibre L plus L^{-1}. The split locus may be empty globally.

## Relevance and bounded decision test

The main gap remains universal primitive rational Hodge realization,
and F existence remains independent. The proposed intermediate result
is the entire ordinary top cohomology stalk of this particular twisted
pushforward at a selected split parameter. A verified local multiplicity
could supply an input to a later global twisted-complex defect comparison;
it would not by itself make a virtual index effective or exclude F.

Essential input IDs to inspect next are L071 (line and kernel data),
L094/L095 (the actual split coefficient deformation), L096 (finite
possibly empty split locus), and L134 (both actual weight projections).
L110 supplies a comparison for a different coefficient, End_0(F), whose
proof must not simply be assigned to the twisted rank-two coefficient.
The relevant earlier assessments are
[the line-twist screen](2026-10-12-equality-split-fibre-line-twist.md) and
[the jumping-cycle screen](2026-10-12-equality-jumping-cycle-index.md).
No cross-notebook input is proposed.

The next turn is literature-only: retrieve primary hypotheses and the
essential coefficient-base-change, connecting-map and top-cokernel cases,
and compare them with this exact target. Approve a mathematical attempt
only if that coverage permits testing length exactly one for the whole
ordinary stalk. If it instead requires unavailable actual higher
coefficients, record that specific missing input. Neither a one-dimensional
derived fibre nor finite support alone meets the test. Do not assume
ordinary scalar self-duality after twisting, everywhere odd IT, expected
codimension, automatic effectivity, or a nonempty split locus.

This proposal records a changed, unassessed target only. No twisted
cohomology dimension, connecting map, stalk length or global inequality
has been derived in step 459. The later actual weight-rank input is the
specific reason to distinguish this target from the preserved historical
IT and index-effectivity stops. Full matching Mathlib coverage is not
checked.

## Completed review — step 460, 2026-10-21

The preceding proposal records the starting gate; the completed review
supersedes its missing-coverage status. This is one LITERATURE /
REPRODUCTION step. The advance is source coverage for a concrete later
specialization, with no new mathematical result or novelty claim.

### Primary coefficient coverage

Budur–Wang, *Cohomology jump loci of differential graded Lie algebras*,
Compositio Math. 151 (2015), 1499–1528, DOI
10.1112/S0010437X14007970,
[arXiv:1309.2264v2, 2 October 2014, Section 3](https://arxiv.org/html/1309.2264v2#S3):
Definitions 3.2 and 3.8 use the module action in the differential
d_omega=d+omega; the standing assumption is bounded-above module with
finite-dimensional cohomology. Proposition 3.10 and Lemma 3.11 retain
the differentiated gauge term in the chain intertwining identity.
[Theorem 6.4, proof (9)–(10), and Remark 6.5](https://arxiv.org/html/1309.2264v2#S6)
identify the actual fixed-tensor Dolbeault complex with derived
pushforward. Remark 6.5 explicitly extends this comparison to abstract
deformation functors for arbitrary holomorphic bundles on a compact
complex manifold. The compact K3, split bundle, and fixed line twist
therefore meet that scope. It requires neither a simple split fibre
nor a universal coarse family. Its module uses End(E) acting on E,
not the adjoint action on End(E). Theorem 1.3's stable/zero-Chern
resonance identification is inapplicable here. No formality is imported.

Reuse FIM, *Differential graded Lie algebras controlling infinitesimal
deformations of coherent sheaves*, JEMS 14 (2012), 521–540, DOI
10.4171/JEMS/310,
[0904.1301v3, Remark 7.3, Theorem 7.6 and Section 8](https://arxiv.org/pdf/0904.1301v3#page=17),
as assessed in `2026-10-16-split-first-order-defect-length-critical-audit.md`.
Its negative-cohomology requirement holds for a bundle concentrated
in degree zero; simplicity is not required. That source was not
downloaded again. BW's explicit Remark 6.5, inspected now, covers the
changed fixed tensor rather than silently extending the old adjoint
assessment. No general theorem needs reproof.

### Derived presentation and duality coverage

The following live Stacks passages were read on 2026-10-21.
[Lemma 36.30.1, 0A1H](https://stacks.math.columbia.edu/tag/0A1H)
assumes finite presentation, a perfect object and a bounded finitely
presented base-flat complex with proper support. Use the structure
sheaf as the perfect object and the locally free twisted coefficient
as the complex. The product projection is smooth projective, so all
hypotheses hold. The Noetherian proof case invokes proper cohomology;
arbitrary derived base change is explicit. This includes the actual
dual-number pullbacks, without ordinary middle-sheaf base change.

[Lemma 15.77.6, 0BCC](https://stacks.math.columbia.edu/tag/0BCC)
gives a local minimal free representative with ranks given by derived
residue-field cohomology. Its proof lifts a zero-differential residue
complex; the uniqueness argument checks invertibility after reduction.
[Lemma 15.77.7, 0BCD](https://stacks.math.columbia.edu/tag/0BCD)
gives a finite representative near a point for a perfect complex by
localization. These apply to the actual perfect pushforward, retaining
all its cohomological degrees and the jumps. The next attempt must
compute the ranks for this coefficient rather than copy L110's ranks.

[Lemma 12.13.12, 0117](https://stacks.math.columbia.edu/tag/0117)
provides natural connecting maps for short exact cochain-complex
sequences; its snake-lemma proof preserves functoriality and shifts.
Reuse projective GAGA as in L110: after forgetting the finite
dual-number projection the coefficient sequence consists of coherent
sheaves on the projective fibre. Exact GAGA and natural cohomology
comparison apply there. The actual sequence and comparison diagram
are obligations for the next proof, not supplied by equal dimensions.

[Remark 48.12.5, 0B6S](https://stacks.math.columbia.edu/tag/0B6S)
assumes a quasi-compact quasi-separated base and a proper flat finitely
presented map; its trace is compatible with base change.
[Remark 48.12.6, 0G81](https://stacks.math.columbia.edu/tag/0G81)
assumes a perfect coefficient pairing into the relative dualizing
complex and pseudo-coherence of the relevant input; it identifies
derived pushforward duality by the actual cup/trace map. Its argument
uses proper duality and the cup/evaluation diagram. A locally free
coefficient has its evaluation pairing with its dual, and the smooth
K3 fibre has canonical bundle O. The next attempt may use that
dual-coefficient Serre pairing. It must not identify the twisted
coefficient with its dual without proof or import L110's scalar
self-duality. No middle-module pairing or split normal form is approved.

[Huybrechts, *Lectures on K3 Surfaces*, author-hosted prepublication
draft, Chapter 1 Section 2.3/(2.5), pp. 11–12](https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf#page=11)
records K3 structure-sheaf cohomology, line-bundle RR and line Serre
duality. The adjacent ample-degree observation and the exact-h line
data in L071/L094 supply the existing inputs for the central fibre
calculation. No twisted dimension is inferred in this source review.

[Nakayama, Lemma 10.20.1, 00DV](https://stacks.math.columbia.edu/tag/00DV),
especially (2) and (8), applies to finite modules over a local ring.
Its determinant proof and reduction to the radical case were inspected.
The source covers promoting generation modulo the maximal ideal to
generation; it does not supply this family's needed linear generators.
The base stalk is Noetherian regular of dimension two. Determining
whether the actual last row meets that criterion is the bounded
mathematical test; a one-dimensional derived top fibre is insufficient.

### Comparison, limits and approved continuation

Read L134 through its actual weight-rank proof: both projections of
the actual derivative have complex rank two. Read L110 through its
actual adjoint first-variation comparison to locate the coefficient
change. The present target concerns the defining coefficient, so its
connecting map must be established independently, with the fixed line
held constant. L094/L095 supply the actual split KS data, not merely
an abstract model plane. L096 supplies a finite possibly empty split
set but no scheme length. None of these local results states the
twisted length conclusion. The scoped local searches found no duplicate
of that conclusion, without claiming exhaustive absence or novelty.

Queries included “Budur Wang cohomology jump loci differential graded
Lie algebra pairs cohomology vector bundles fixed tensor Dolbeault
module”, “cohomology and base change minimal first order cup product
length”, “K3 cohomology jump loci polystable line bundles”, and
“cohomology jump loci length one bundle”. The exact-stalk queries
gave no usable primary theorem beyond the general framework. Returned
third-party numerical K3/jump discussions and unrelated geometric
papers remain unread leads and support no assertion. The initial
mistyped arXiv 1309.2254 and unrelated Stacks 0G80 are excluded;
the correct coefficient paper and duality antecedent 0B6S were read.

Continue only with the exact TARGET above, after the supervisor's
separate approval of this newly completed assessment. The attempt must
check the actual coefficient connecting sequence, its Serre transpose
against the correct dual, and the full last-row cotangent rank.
The required rank is two, the dimension of the base cotangent space;
its value has not been computed here. If those identifications hold
and the rank suffices, test the whole ordinary cokernel by the imported
local algebra. If they fail, record the precise missing map or rank
defect and stop this first-order length mechanism. Do not claim that
failure disproves the desired length or excludes the kernel.

The plausible downstream use remains a later twisted-complex defect
comparison, which needs its own coverage and global inputs. It is
outside this approval. Ordinary self-duality, global IT, effectivity,
F existence, nonempty split locus, reconstruction, transverse transport
and universal primitive Hodge realization remain unproved. The main
argument, lemmas and DAG are unchanged. Full matching Mathlib coverage
has not been checked; no absence claim is made.
