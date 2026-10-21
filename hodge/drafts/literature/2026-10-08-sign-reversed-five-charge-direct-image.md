# Sign-reversed five-charge slice — source comparison

TARGET: Test whether the sign-reversed L071 slice a=-9 is excluded by the actual first higher direct image for every admitted integer b.
CHECKED: 2026-10-08
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Read L055 in full, L071's hypotheses/character and every-fibre restriction passages, L048's character proof, ATTEMPTS/039--040 and the saved five-charge/fixed-pair assessments; bounded changed-sign K3-product searches on CHECKED supplied no inspected matching slice theorem. Exact queries and limits are recorded below.
SOURCE_EVIDENCE: Reused Fulton, Intersection Theory, second edition (1998), Theorem 15.2, pp. 286--287 and Example 15.2.8, pp. 291--292; freshly inspected Stacks 0A1H statement and Noetherian proof case, 0BDH Lemma 36.31.3 and its complete proof, and 02UO's smooth-proper relative statement; retained the previously inspected surface and Maciocia coverage.
COMPARISON: L055's stated hypotheses prescribe +tau_D, so its exclusion is not a literal import. Audited L071 already covers -tau_D's invariant connection, every-fibre factor tests and full forced higher characters; base change and relative GRR impose no mixed-sign hypothesis. This reuses the same obstruction method, not a new mechanism.
GAP: Separately apply L071's charge-five factor input to every fibre, obtain the actual first higher direct image by the cited perfect-complex criteria, and evaluate the signed full relative character against the line identity for every admitted integer b. No changed image character or exclusion is established in this review.
REASON: Essential theorem coverage is now ready for the unchanged target; only the changed-data applicability argument and signed substitution remain. Import the general tools without reproof and classify the later attempt as REPRODUCTION.
LITERATURE_REASON: The saved target was REVIEW_REQUIRED because its full mixed character changed from +tau_D to -tau_D; this turn resolves its exact overlap with L055 rather than adding literature to an already ready target.
SCOPE: L071's identical marked product and real common metric, full mixed tensor -tau_D, rank two, local freeness and product slope-polystability, c_1=0, a=-9 and all integers b admitted by L071; unrestricted initial higher characters/K-class.

## Exact review obligations and continuation test

The universal gap remains primitive rational Hodge-class algebraicity.
The audited filter supplies topological bundles and conditional factor
polystability, not compatible holomorphic product bundles. This proposed
target tests global compatibility through an actual relative direct
image, rather than repeating the completed topology/factor audit.

Essential continuation inputs are L071, L044, L048, L052 and L055.
The review read L055's full canonical proof and its saved assessment,
including primary base-change and relative-GRR hypothesis coverage.
L071 now licenses the changed-sign restriction passage; L052's old
sign-specific hypotheses do not apply directly. The later application
must preserve the distinction between the positive direct-image bundle
and the alternating pushforward class, compare the full square and all
linear mixed terms, retain every admitted b, and assume neither stability
of the other factor nor of the direct image.

Attempts 039--040 preserve the earlier positive-tensor failure.
The new idea being tested is whether that existing compatibility
obstruction also controls the independently specified opposite-action
slice; it is not a proposal to construct the already excluded positive
kernel. L055 does not cover the changed statement verbatim, but the
general tools and audited L071 supply the required coverage. Continue
with one separate REPRODUCTION application, without rebuilding the
general theory. Stop this bounded test if every-fibre concentration
cannot be justified, or if a compatible integer subcase survives the
full character comparison. In the latter case retain that subcase
without claiming existence. A justified exclusion would redirect
construction to larger factor charges; it would not prove algebraicity.

The later mathematical threshold would be a justified exclusion or
an explicitly compatible integer subcase, not a numerical scan. No such
result is asserted in this file. Holomorphic product existence, gluing
in other slices and transverse transport remain unresolved regardless
of the outcome. L070's positive-tensor stop, the charge-seven stop and
the parked flat-index blocker remain intact. No L060/L067 or
cross-notebook input is proposed.

## Primary theorem hypotheses and relevant proof cases

Reuse the ready [five-charge assessment](2026-10-05-five-charge-relative-direct-image-slice.md)
and [fixed-pair assessment](2026-10-05-minimum-pair-relative-cohomology.md)
for the unchanged general inputs. On CHECKED, re-inspected these
primary Stacks passages for the changed-sign hypothesis comparison:

- [Lemma 36.30.1, Tag 0A1H](https://stacks.math.columbia.edu/tag/0A1H):
  finite-presentation morphism, perfect E, bounded finitely presented
  base-flat complex with proper support; perfect derived pushforward
  and arbitrary base change. Take E=O_X and the complex F[0]. Smooth
  projectivity of p_2 and local freeness of F discharge these geometric
  conditions after GAGA. The Noetherian proof case applies to S;
  approximation is unnecessary. The theorem does not independently
  assert local freeness of the higher direct images.
- [Lemma 36.31.3 in Tag 0BDH](https://stacks.math.columbia.edu/tag/0BDH):
  a perfect complex has an open locus of concentration in degree i as
  a locally free rank-r module, characterized by derived pullback.
  Read its full proof: other fibre Betti numbers vanish on an open
  locus, the finite-free complex criterion gives concentration, and
  the remaining rank loci are open. The future application must use
  i=1,r=1 and verify every closed fibre; the finite-type complex base
  then makes an empty closed complement check sufficient. Virtual
  rank and generic-fibre concentration alone are insufficient.
- [Section 42.66, Tag 02UO](https://stacks.math.columbia.edu/tag/02UO):
  proper smooth morphism, finite locally free input and finite locally
  free higher direct images; the formula retains the alternating sum
  and relative tangent Todd class. Its general proof is deferred there.
  Retain Fulton, *Intersection Theory*, second edition (1998), Theorem
  15.2, pp. 286--287 and Example 15.2.8, pp. 291--292,
  [previously inspected scan](https://djvu.online/file/87GFN2nbfbdF7),
  as the theorem citation. Proper projection between nonsingular
  projective varieties is in its scope. Preserve the recorded scan-host
  1997 label versus cited-edition 1998 qualification; no fresh Fulton
  passage was necessary.

The relative formula is ch(p_2!F)=p_2*(ch(F) td(T_{X/S})); its
relative tangent is p_1^*T_S. These theorems impose no positivity or
mixed-sign hypothesis. Pass through the rational cycle-class map and
keep the actual positive bundle distinct from the alternating class.
Reuse the [character identity, Stacks 02UM](https://stacks.math.columbia.edu/tag/02UM)
and Fulton Theorem 3.2(a), pp. 50--52 from the prior assessment:
a line has character exp(c_1), while rank truncation concerns an
actual rank-two bundle, not an arbitrary virtual class.

No new stability theorem is needed. L071 already proves, for these
exact negative-mixed data, stable product F, an invariant compatible
connection and polystable locally free restrictions at every factor
fibre. Its inspected proof uses Verbitsky, arXiv:math/0107182v10,
Theorem 3.9 and Proposition 3.7/Lemma 3.8, pp. 13--14, and
Huybrechts, *Lectures on K3 Surfaces*, author-hosted draft, Chapter 9,
Theorem 4.9, p. 182. Its factor discussion and L052's unchanged
zero-slope line lattice retain stable/split alternatives, surface RR
and dual stability. Reuse their approved source coverage; this review
does not derive a new cohomology result or widen restriction stability.

## Exact overlap and remaining specialization

L055's full proof retains every-fibre cohomology, actual base change,
full variable character, relative pushforward and line identity. Its
hypotheses prescribe +tau_D; direct application to the new F is invalid.
L071, rather than L052's positive-tensor hypotheses, now licenses the
connection and factor passage at exactly the same metric.

L071 equations (2) and (6) already give the changed-sign forced
higher characters and full square, retaining the divisor contribution
36 and transcendental contribution 120. These are established local
inputs, not calculations first performed here. L055 explicitly
separates linear mixed terms from the square and records the relevant
pushforward and Todd products. The later attempt must substitute the
whole changed character, inspect the linear terms by factor degree,
retain the alternating sign and test every admitted b. This review
supplies no new image character, exceptional value or slice verdict.

The fixed first-factor charge, real metric, projection and actual rank
are within the assessed tools' scope. Neither stability of opposite
factor restrictions nor of the image is needed for a line-identity
test. L071's forced characters must replace unrestricted initial higher
characters; no old virtual K-class is retained. Topological realization
and individual factor existence still do not supply F.

## Searches, stronger results, duplicates and failures

On CHECKED, bounded external queries were:

- `"K3" "rank two" "sign" "direct image" bundle Chern`
- `"K3" "rank two" "c_2=5" "product"`

They returned broad bundle, index, spectral-cover and transform leads,
but no inspected theorem deciding this exact signed tensor slice.
Search snippets and nonprimary mirrors supplied no theorem evidence;
these are unread leads, not exclusions. Failed searches imply no
novelty. No essential source is blocked for the proposed specialization.

Reuse the earlier theorem-level comparison with Maciocia, *Rank Two
Fourier--Mukai Transforms for K3 Surfaces*, J. Geom. Phys. 118 (2017),
192--201, [accepted manuscript](https://www.pure.ed.ac.uk/ws/portalfiles/portal/30370169/Rank_Two_Fourier_Mukai_Transforms_for_K3_Surfaces.pdf),
Theorem 0.1, Proposition 1.1 and Theorem 2.5, printed pp. 2--5.
Those inspected statements classify equivalence kernels in specified
determinant/line-subsheaf scopes, or a diagonal-ideal extension with
acyclic line-ratio and line-product hypotheses. They do not classify
the arbitrary polystable product bundle here. Sign reversal supplies
neither equivalence, strong simplicity nor the missing presentation.
No further Maciocia passage was needed or reread.

The scoped duplicate/failure check read ATTEMPTS/039--040 and relevant
sign-reversed assessment/history passages. The former retain the
positive-tensor minimum-pair and whole-five-charge stops, with canonical
proofs in L054 and L055. L071 supplies a necessary non-exclusion set
and topological realization, not global holomorphic compatibility.
No completed changed-sign direct-image exclusion was located in those
paths. This is an overlap test of an existing mechanism with no claim
of originality. L070's positive-tensor stop, the charge-seven stop and
the parked flat-index blocker remain intact; none is reopened here.

## Review outcome and Mathlib

Completed one LITERATURE / EXPLORATION / NOVELTY_UNCHECKED step,
actual task type literature_comparison. The exact scope comparison
makes SPECIALIZE ready for this unchanged TARGET and authorizes a
separate REPRODUCTION attempt. It proves no exclusion and constructs
no bundle. No lemma, mathematical script, DAG or PROOF change was made;
mathematical exploration usage is zero. Import the general theorems
by precise citation and write only the identified application.

Mathlib coverage of a matching full signed slice or supporting coherent
base-change/relative-GRR inputs is not checked. No declaration match or
absence is asserted. Canonical local proofs remain in lemmas/; the
sources above supply supporting general tools.
