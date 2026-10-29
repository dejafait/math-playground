# Marked dyadic point image — source comparison

TARGET: Compute the complete Q_2 Kummer image of B-points lifting to L138's marked cover v^2=z, and test strictness inside L145's eight-class image.
CHECKED: 2026-10-27
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Compared L110/L111/L113 proper models, L122's statement and complete feasible-disk/realization proof, L138's model charts and L145's Kummer conventions; checked ATTEMPTS/050 and ATTEMPTS/053-fixed-dyadic. Web queries included Bruin Stoll two cover descent hyperelliptic curves local image rational functions marked cover Kummer image; "67760" "hyperelliptic"; "marked" "Kummer" "local image" hyperelliptic cover; and "3025" "31460" "76230" curve Kummer. No inspected exact-instance answer to this composed image was identified; unsuccessful searches do not establish novelty.
SOURCE_EVIDENCE: Reused drafts/literature/2026-10-23-marked-octic-five-adic-point-image.md and 2026-10-27-pair-two-adic-kummer-filter.md; directly inspected Bruin–Stoll arXiv:0803.2052v2 (21 October 2008), Section 2/Remark 2.1 p.3, Section 4 hypotheses p.6, full Lemma 4.4 proof p.8 and terminal/reciprocal explanations pp.9–11; Stoll Acta Arith. 98 (2001), Section 4 and Lemmas 4.1/4.3 pp.249–251; Stacks 0BY1 statement/full proof, 03PK Lemma 59.28.1/full proof, 0BQL statement/full proof and 03AG Lemmas 21.4.2–3 (proof of 21.4.2 omitted by source). Links and applicability below.
COMPARISON: Known proper-curve extension, normalized Kummer lifting, odd-model point evaluation and dyadic disk methods cover the required tools. L122 supplies complete source-coordinate disks and a different five-class even-degree scalar quotient; it supplies no certified map from that quotient to L145's full odd-model coordinates. L145 supplies the eight-class Jacobian ambient image, not this marked degree-one subset. The remaining task is an instance specialization, not a new general algorithm.
GAP: Source coverage is sufficient for a separate bounded attempt. The composed evaluations, constancy or refinement of every feasible disk, all exceptional target evaluations and complete realizations in L145's coordinates remain uncomputed. Neither strictness, equality nor independence after other local filters is asserted.
REASON: This review resolves the missing source and duplicate interfaces for the saved target; it prepares a later reproduction of known methods without computing a new image or changing a lemma or mathematical script.
LITERATURE_REASON: Startup REVIEW_REQUIRED concerned degree-one marked lifting, proper-boundary coverage and overlap with L122, outside the preceding Jacobian-image audit; this review fills those specific gaps and reuses unchanged dyadic arithmetic coverage.
SCOPE: Exactly TARGET on L138's unchanged B, twist, z and rational infinity, using the proper marked curve of L111/L113 and L145's exact nine square-class coordinates. Includes composed point evaluation, reuse/refinement of L122's complete source disks, all proper-curve exceptional points and exact realization/containment certificates. No new global witness pool, unit/class basis, other place, rank gain or rational/integer point classification.

## Relevance and discriminating test

The main gap remains residual primitive Beal solutions. Even the audited
bound seven is six above the sufficient rank bound one. This proposal
changes the immediate object from a linear Jacobian image to the image
of degree-one points admitting the required marked lift. A strict subset
could supply a necessary point/lift condition for later descent; it
would not itself classify global points or recover integers. The review
classifies this as a standard local-descent specialization, not a
creative or novel method.

Essential input IDs are L110, L111, L113, L122, L138 and L145. L109's
normalized-lifting passage was read to qualify boundary use; its cover
identification is already incorporated in L111. L140/L141 remain accepted
filters only for a later global compatibility claim. There is no
cross-notebook input. No L122-to-L145 quotient transfer is assumed.

The intended bounded test is the image inside L145's eight actual local
Jacobian classes. A later approved attempt must authenticate all retained
classes by actual marked local points and prove completeness, including
zeros/poles of z and exceptional points of the model maps. A partial
point sample cannot reject any class. A proper subset would establish a
local marked-point refinement; equality would stop this particular
mechanism. Incomplete chart coverage leaves the test unresolved. No
stricter global rank bound follows merely from a non-linear point image,
and no additional pruning after the old filters is presumed.

## Precise imports and applicability

Nils Bruin and Michael Stoll, *Two-cover descent on hyperelliptic
curves*, Math. Comp. **78** (2009), 2347–2370,
[DOI 10.1090/S0025-5718-09-02255-8](https://doi.org/10.1090/S0025-5718-09-02255-8),
[arXiv:0803.2052v2](https://arxiv.org/pdf/0803.2052v2), 21 October 2008:
Section 2/Remark 2.1 p.3 distinguishes the even scalar quotient from
the odd raw square-class target. Section 4 p.6 assumes characteristic
zero, a complete discretely valued field with finite residue field,
integral squarefree polynomial and its full local factorization.
Lemma 4.4 p.8 and SquareClasses/LocalImage pp.9–11 cover strict dyadic
precision, nonbranch and linear-branch termination, both coordinate
charts and separate infinity values. Reuse the fuller extraction in
the two assessments named in SOURCE_EVIDENCE.

Michael Stoll, *Implementing 2-descent for Jacobians of hyperelliptic
curves*, Acta Arith. **98** (2001), 245–277,
[DOI 10.4064/aa98-3-4, publisher PDF](https://www.impan.pl/shop/en/publication/transaction/download/product/83397):
Section 4 and Lemmas 4.1/4.3 pp.249–251 give odd-model Kummer
evaluation, its identification with the connecting map, and branch
values over field extensions of Q. Their proofs refer to Schaefer;
the already ready L145 assessment supplies this import's coverage,
rather than a reproof here.

[Stacks Theorem 53.2.6, 0BY1](https://stacks.math.columbia.edu/tag/0BY1)
extends nonconstant function-field maps to normal proper curves.
[Lemma 59.28.1, 03PK](https://stacks.math.columbia.edu/tag/03PK),
[Lemma 58.11.2, 0BQL](https://stacks.math.columbia.edu/tag/0BQL), and
[Lemmas 21.4.2–3, 03AG](https://stacks.math.columbia.edu/tag/03AG)
supply unit-root Kummer covers, their normalization when connected,
and the torsor/section criterion. L109's existing normalized-unit
interface, already retained by L110/L111, supplies the boundary rule;
this review does not prove a new extension of that rule.

Here the base field is Q_2, hence characteristic zero despite residue
characteristic two. L113 supplies the actual squarefree integral octic
and complete smooth proper charts. L138 supplies the actual monic
squarefree quintic and its rational infinity. L111 identifies the
proper marked cover, not just an affine equation with canceled factors.
These curve maps are over Q and are available after base extension.
For the curve local rings over Q_2, the constant 2 is invertible;
this must not be confused with its being a unit of Z_2. At zeros or
poles the normalized unit, not the value zero or infinity, determines
the marked fiber. Connectedness in 0BQL is checked at the function-field
model, not presumed for a split completed local algebra.

Reuse L145's certified field, valuation conventions, square-class basis
and complete image. Clark's Local Square Theorem, *Algebraic Number
Theory II*, [161-page author notes](https://plclark.github.io/PeteLClark/Expositions/8410FULLL.pdf),
Theorem 2.24/full proof p.73, is already covered in the ready dyadic
assessment (accessed 2026-10-27; revision date unidentified). No fresh
source access or field reconstruction is required for that unchanged
input. It gives sufficient square neighborhoods, not a precision guess
or permission to omit a valuation bit.

## Duplicate comparison and boundary cautions

The object sought is the set of values delta_2([P−infinity_B]) for
P in B(Q_2) admitting a point on the **proper normalized** marked cover.
L111/L113 supply the source curve and projection. L145's eight classes
are the comparison ambient set. Its dimension saturation used a
quadratic trace divisor; it does not assert that eight degree-one
marked point classes exist.

L122 already covers every feasible source coordinate: four even disks
modulo eight, two odd disks modulo sixteen, and the reciprocal even
chart with its entire tail and both infinity points. Its five quotient
labels summarize the source fake map, not the composed map in this
target. Equal fake labels, even within a disk, cannot be assumed to
have equal L145 labels without an exact transport/constancy proof.
Computing five center values alone would therefore be insufficient.
The partition and its point-realization evidence can be reused, with
further refinement if the new evaluations need it; repeating the full
octic fake-image computation has no research purpose.

L113's sentence excluding other **Q-rational** coordinate exceptions
does not exclude them over Q_2. In particular L122 already realizes
t=0 locally, although L113 excludes that fiber over Q. L111's proper
finite/infinity charts and L113's global conic parametrization are the
appropriate interfaces. Later execution must handle target branch
points, odd infinity, sextic infinity, the source infinity points and
all zero/pole fibers of the original marking functions through these
maps. A rational-root test over Q cannot replace a local calculation.
The review evaluates none of these new target classes.

ATTEMPTS/050 stops only its bounded rational rank-lower detector, not
this complete local point calculation. ATTEMPTS/053-fixed-dyadic stops
an independence inference from a witness already failing the real
filter. Consequently a proper marked subset here must not be advertised
as extra global pruning without a separate compatibility test.
ATTEMPTS/045,052,061–063 and unfinished L108 remain parked and unchanged;
no dependent global backend or exhausted witness search is reopened.

## Bounded contract for a separate research turn

1. Bind the exact proper projection in L111/L113 and odd-model maps in
   L138. Compose the established odd Kummer evaluation with this map,
   retaining L145's rational component and exact twist. Prove any
   claimed factorization through L122's scalar quotient; otherwise
   work directly on its source-coordinate disks. No such factorization
   or simplified instance formula is established in this review.
2. Reuse L122's complete feasible disk partition. Certify the new target
   value on every retained disk by coefficientwise strict bounds, or
   subdivide it exhaustively. Bind every table to L145's nine coordinates.
   Retain actual point realizations, including any extra refinements;
   containment or a list of sampled values alone is not equality.
3. Record separate normalized rows for all exceptional target values,
   with all source fibers included. Use branch evaluation or the target
   infinity convention rather than a zero/noninvertible representative.
   If working through the proper C-to-B map, show that it accounts for
   every marked lift, rather than imposing the Q-only open-locus list.
4. Compare the resulting exact set with L145's eight actual classes,
   preserving a set rather than taking its linear span. Supply a full
   certificate and independent replay; an unresolved disk or chart
   prevents rejection of its classes. Strictness supports this necessary
   marked Abel condition; equality stops this mechanism.

Caps: 200000 processed refinement disks, depth 64 in base-field binary
digits, at most 2^20 entries per residue-ring table, and 8192 bits per
exact rational numerator/denominator. Reuse already certified arithmetic;
these are stopping caps, not assumed sufficient precision. Save complete
unresolved coverage and actual/required bounds if a cap is hit. No
mathematical program runs in this literature-only review.

No full matching Mathlib result was checked; supporting formal coverage
is not assumed absent. This review produces source readiness and a
delimited instance contract, not a new theorem or an image answer.
SPECIALIZE permits a later REPRODUCTION. The newly completed assessment
receives separate next-turn approval before execution. The discovery
priority supplies no reason to relabel this standard specialization
creative; a justified new central mechanism remains unprepared, while
this now-covered point-image test is independently testable. Global
units/classes, point control, marked integer recovery and all other
residual signatures remain independent gaps.
