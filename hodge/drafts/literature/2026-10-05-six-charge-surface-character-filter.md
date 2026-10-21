# Six-charge surface character filter — source assessment

TARGET: Test which integer b in the a=-10 L052 survivor slice pass relative GRR and L052's fixed-metric rank-two polystability tests for the L056 direct image.
CHECKED: 2026-10-05
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Scoped comparison of L048, L052, L055, L056, the prior GRR/factor assessments and histories 101–106 found no completed six-charge character filter; bounded external searches checked rank-two K3 Fourier/Nahm character and stability terminology and the nearby Maciocia classification, detailed below.
SOURCE_EVIDENCE: Reused inspected Fulton Intersection Theory second edition (1998), Theorem 15.2, pp. 286–287, Example 15.2.8, pp. 291–292, and Huybrechts Lectures on K3 Surfaces author-hosted draft, Chapter 1 equations (2.5)–(2.6), Proposition 2.4, pp. 11–13, Chapter 9 Section 3.1, pp. 175–176, Theorem 4.9, p. 182; rechecked Stacks 02UO and 02UM and Maciocia accepted manuscript introduction/Theorem 0.1, Proposition 1.1 and proof, printed pp. 1–4.
COMPARISON: GRR applies to this projection without a coefficient bound; L056 supplies actual locally free higher direct images and polystability at h, and L052's surface stable/split tests apply to any locally free rank-two bundle with zero first Chern class at h. Equivalence-kernel classifications impose additional hypotheses absent here.
GAP: Evaluate the full relative character from L048 for a=-10, verify the resulting first Chern class before invoking L052, and intersect its stable and split necessary tests with the entire integer survivor slice; no evaluated coefficient filter is supplied by the sources or this review.
REASON: The changed character/stability target required separate scope comparison, now complete. Import general GRR and surface theorems and reuse the canonical lattice calculation; only the unevaluated parameter specialization remains, so the next step is REPRODUCTION without a general reproof or originality claim.
SCOPE: Exactly L044's S,h,tau_D, L048's forced rank-two character, integer a=-10 and b satisfying L052, hypothetical locally free product-polystable F, and the actual G=R^1 p_2*F of L056; necessary character and L052 surface tests only, retaining stable and reducible G. No construction, equivalence, optimal existence classification, changed metric or transport.

The global mixed-tensor realization gap remains unresolved. The proposed
intermediate target asks for a necessary coefficient filter, with no
claim that any passing coefficient yields a bundle or transport.
Essential local inputs are L044's exact S,h,tau_D, L048's forced
rank-two higher characters, L052's fixed-metric stable/split tests,
and L056's actual rank-two locally free polystable direct image.
L055 preserves the exhausted five-charge stop, rather than supplying
a new six-charge calculation. The other factor's stability, stability
of the transform, global existence and transverse transport are not
assumptions. No new character, inequality or residue filter is derived
in this proposal.

## Primary theorem hypotheses and reusable coverage

Reuse the [five-charge assessment](2026-10-05-five-charge-relative-direct-image-slice.md)
and [fixed-pair assessment](2026-10-05-minimum-pair-relative-cohomology.md)
for Fulton, *Intersection Theory*, second edition (1998),
[Theorem 15.2, pp. 286–287, Example 15.2.8, pp. 291–292](https://djvu.online/file/87GFN2nbfbdF7).
Retain their scan-host/version qualification. The theorem concerns a
proper morphism of nonsingular varieties; the smooth projective
projection p_2:S x S -> S is in its quasi-projective case. GAGA makes
the hypothetical holomorphic locally free F algebraic. The real h
enters stability and does not need to be an algebraic polarization
for GRR. Neither a=-9 nor a bound on b is a theorem hypothesis.
Import the general theorem without reproof, pass to rational cohomology,
and use ch(p_2![F])=p_2*(ch(F) td(T_(X/S))).

Rechecked [Stacks Section 42.66, Tag 02UO](https://stacks.math.columbia.edu/tag/02UO)
on CHECKED: its stated case assumes proper smooth f, finite locally
free input, and finite locally free higher direct images; its formula
uses their alternating sum and the relative Todd class. The general
proof is deferred there, so Fulton remains the theorem citation.
L056 discharges these direct-image hypotheses in the present slice:
G is actual rank two and all other higher images vanish. In particular
the character to compare is the negative of the alternating character,
not the alternating virtual class treated as a positive bundle.
Base change and IT have already been proved in L056 and do not require
another preservation derivation here.

Rechecked [Stacks Section 42.45, Tag 02UM](https://stacks.math.columbia.edu/tag/02UM)
for the Chern-root definition and expansion through the second character.
The future calculation must determine rank, first and second characters,
retain L048's full mixed-square contribution and use the relative Todd
class from the projected factor. L048 covers the present coefficients
under its weaker sum hypothesis; initial higher characters are not free
parameters after rank-two truncation. No new pushforward is evaluated
in this source review.

Reuse the [variable factor assessment](2026-10-04-nonsymmetric-factor-polystability-region.md)
for Huybrechts, *Lectures on K3 Surfaces*, author-hosted prepublication
draft, [Chapter 1, pp. 11–13](https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf#page=11)
(equations (2.5)–(2.6), Proposition 2.4) and
[Chapter 9, pp. 175–176 and 182](https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf#page=175)
(Section 3.1 and Theorem 4.9). Surface RR, Serre duality, dual stability
and Hermite–Einstein/polystability allow a real Kahler class. Their
surface hypotheses concern the bundle itself, not whether it arose as
a fibre restriction. Thus L052's canonical surface argument applies to
G once its zero first Chern class is checked, with its stable necessary
bound c_2>=4 including equality, and its reducible alternative
L direct sum L^{-1}, c_1(L)=r(-4,-2,1,2), c_2=14r^2, r an integer.
These are recorded L052 results, not new deductions in this review.
The determinant passage uses the same K3's torsion-free Picard group
and Pic^0=0; no different surface or lattice is substituted.

No theorem in this framework says G is stable. L056's quaternionic
connection gives slope-zero polystability at the exact h and permits
reducibility. The hyperholomorphic criterion need not be reapplied to
G, and the other factor's stability is unnecessary for this filter.
Passing either numerical alternative is only non-exclusion by the
specified tests, not holomorphic G or global F existence.

## Stronger results, duplicates and failures

Rechecked Maciocia, *Rank Two Fourier–Mukai Transforms for K3 Surfaces*,
J. Geom. Phys. 118 (2017), 192–201,
[peer-reviewed accepted manuscript](https://www.pure.ed.ac.uk/ws/portalfiles/portal/30370169/Rank_Two_Fourier_Mukai_Transforms_for_K3_Surfaces.pdf),
introduction and Theorem 0.1, printed pp. 1–2, Proposition 1.1 and its
proof, pp. 3–4. Fourier–Mukai transform there means a derived equivalence.
The classification also imposes a special line-subsheaf and determinant
condition. Its character formula is for a specified product-line
extension of the diagonal ideal; the proof uses that extension.
Neither that presentation nor an equivalence follows from L056.
Theorem 2.5's extension criterion is reused from the earlier assessment,
not newly reread. These stronger classification results do not replace
general GRR for this arbitrary hypothetical kernel.

L055 and [its preserved stop](../../ATTEMPTS/040-five-charge-product-realization-slice.md)
exclude a=-9 using an actual line direct image. They do not exclude
a=-10: L056 establishes an actual rank-two transform instead. This is
a different, independently testable finite-rank alternative, not a
reopening of the exhausted line-identity mechanism. L052 treats factor
restrictions, not the relative character of G; L056 evaluates no such
character. Scoped histories 101–106 and the six-charge working record
only propose the target. L048–L050 index/topological tests and L053
individual existence do not provide global compatibility. Prior fixed
K-class, symmetric and boundary stops remain unchanged.

Exact external queries on CHECKED:

- K3 rank two hyperkahler Fourier transform Chern character stability reducible Grothendieck Riemann Roch
- K3 stable vector bundle rank 2 c1 zero c2 Mukai vector square nonempty moduli
- "Rank Two Fourier-Mukai Transforms for K3 Surfaces" Maciocia
- "hyperkahler Fourier" "rank" "stable" Bartocci

Searches found Maciocia and the previously assessed Bartocci–Bruzzo–
Hernandez Ruiperez preservation paper, plus moduli/existence leads.
No matching fixed-metric, fixed-tensor coefficient filter was identified
in the inspected theorems; this does not assert novelty. Nakashima's
c_1=0 existence paper remains an unread lead, as in the factor assessment.
Other Mukai-vector existence results were search leads, not imported
theorems. They are not essential to a necessary filter expressly limited
to L052's tests; optimal existence or a broader classification would
require separate coverage. No essential source blocker remains here.

## Approved bounded test and outcome

In one separate mathematical turn, use L044, L048, L052 and L056 to
compute the relative character for the entire saved integer slice,
check its first Chern class, and apply both surface alternatives.
Compare the exact resulting conditions with the required thresholds;
retain all compatible integers, including equality and reducible
exceptions. Continue if the character or surface tests discriminate
coefficients or leave an explicit compatible region for a different
test. If they add no discrimination, stop this filter. If the zero-first-
character or local-freeness premise fails on audit, park this application
without assuming stability or changing h. A surviving coefficient
does not justify continuing the same filter by relabeling non-exclusion
as existence. Global realization, other representatives, transverse
transport and universal primitive-Hodge algebraicity remain independent
gaps. No new character, inequality or coefficient set is derived here.

Completed LITERATURE / EXPLORATION / NOVELTY_UNCHECKED, actual task
type literature_comparison. The new scope comparison changes the
unchanged TARGET from REVIEW_REQUIRED to SPECIALIZE and recommends a
separate REPRODUCTION calculation; it is not a mathematical advance.
The supervisor may separately approve this newly ready continuation.
No lemmas, mathematical scripts, DAG or PROOF are changed.
Mathlib coverage of the full filter and supporting relative GRR/surface
stability inputs: not checked; no matching declaration or absence is
asserted. Mathematical exploration usage remains zero.
