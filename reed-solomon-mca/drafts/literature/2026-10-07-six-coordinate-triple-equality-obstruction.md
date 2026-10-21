# Six-coordinate triple equality obstruction — source comparison

TARGET: Review known results and local overlap for an analytic at-most-fifteen bound on L010 pencils over F_(97^20) represented on six coordinates and realizing L032's union-six triple.
CHECKED: 2026-10-07
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Compared the analytic L010/L015 passages, L032's hypotheses and local lift, L014's equality gates, previous Hall/Jurrius and MCA assessments, and ATTEMPTS/017, /019, /020; bounded exact-target, syndrome-geometry and shortened-GRS searches are recorded below.
SOURCE_EVIDENCE: Read Marquez-Corbella–Pellikaan (2016), accepted manuscript dated February 29, 2016, section 5, Definitions 5.1–5.2, Lemma 5.3 and the following explicit GRS shortening formula, printed pp. 7–8; reused inspected Hall Theorem 5.1.1 and proof, Jurrius Proposition 4.2 and BCHKS Theorems 1.3/4.6 with their previously inspected proofs; rechecked the BCHKS theorem statements and full bound in the author-hosted PDF.
COMPARISON: Shortening supplies an exact coding transformation, not a fifteen-count theorem; L015's point reduction is restricted to five coordinates and does not extend by citation. The inspected general MCA theorem has an error coefficient exceeding sixteen here. No matching six-coordinate exclusion or progress beyond parked unread stronger claims is established.
GAP: A case-complete shortened-code incidence reduction and a subsequent analytic bound on its parameter incidences are still needed; only the standard transformation and local inputs are ready.
REASON: Inspected standard ingredients support a bounded specialization of the already written L015 mechanism to the six-coordinate class, without importing an inaccessible theorem or claiming a new obstruction during this review.
SCOPE: The reviewed class and the separate continuation assessment only; no arbitrary-family reduction, numerical configuration bound or projective descent is approved by this comparison.
LITERATURE_REASON: The changed six-coordinate target lies outside the five-coordinate reduction and the approved L032 audit; its essential coding and quantitative source comparison had not been completed.

## Gap, intermediate target and decision test

The main gap remains arbitrary-family sixteen-count equality, with
11/q–16/q against allowable fifteen. The reviewed restricted class has
F=F_(97^20), H the order-sixteen subgroup of F_97^*, k=8, the pinned
cell 1/4<=delta<5/16, all eight shifted moments, nonzero polynomial D
and every coordinate locator, both syndromes represented on a six-set U,
and three distinct finite parameters with actual full-weight four-errors
forming L032's union-six pattern and affine weights. Equality arguments
must assume every L010 sixteen-count premise explicitly.

The selected intermediate target is a case-complete analytic description
of additional four-error supports through shortened GRS evaluation
spaces and their intersection with the fixed affine lift. Its plausible
use is an eventual bound of at most twelve additional bad parameters
beyond the selected three, hence at most fifteen in this class. That
threshold is the goal of the subsequent incidence estimate, not a
conclusion of the source review or of shortening alone.

Continue if one later bounded proof attempt gives exact necessary and
sufficient compatibility conditions for all remaining supports over F,
with no missing overlap, cancellation or exceptional-intersection cases.
A useful reduction may leave the incidence bound unresolved. Reassess
if this only restates eight moment equations without reducing the
counting problem. Abandon a proposed exclusion on a verified sixteen-count
pencil meeting every L010 gate; a compatible local triple or abstract
family is insufficient. Park a dependent route if it needs an essential
inaccessible theorem. No new restriction or incidence formula is derived
in this literature turn.

## Primary shortening input

Irene Marquez-Corbella and Ruud Pellikaan, *A characterization of MDS
codes that have an error correcting pair*, Finite Fields and Their
Applications 40 (2016), 224–245, DOI
[10.1016/j.ffa.2016.04.004](https://doi.org/10.1016/j.ffa.2016.04.004).
Read the [institutional accepted manuscript](https://pure.tue.nl/ws/files/93073933/16_02_29_ECP_MDS.pdf),
with submission date February 29, 2016 and repository publication date
July 1, 2016, section 5, printed pp. 7–8 (PDF pages 8–9).

Definition 5.2 retains codewords zero on the shortened set before deleting
those coordinates. Lemma 5.3 states MDS parameters after puncturing and
shortening for an [n,k] MDS code and m shortened positions with n-m>=k.
The following unnumbered paragraph gives single-coordinate GRS shortening:
GRS_k(a,b) shortened at its final position becomes
GRS_(k-1)(a',b' * v'), where v'_j=a_j-a_n. This formula, rather than a
puncturing dual-multiplier formula, is the selected input. The paragraph
has no separate detailed proof; Hall's inspected polynomial-root proof
and the GRS evaluation definition explain its factor convention. Reuse
the formula by citation, with coordinate permutations and repeated
applications justified if needed; do not reprove general shortening.

For this notebook the labels are finite, distinct elements of H and the
original multipliers are one. The same theorem may be used over F;
nonzero differences of distinct labels retain nonzero multipliers.
For any proposed use, state the actual shortened set, check the parameter
conditions at every stage, and distinguish evaluation on retained labels
from the original sixteen-coordinate moment vector. This is applicability
coverage, not an assertion about which shortened sets an additional
error forces. Those cases belong to the later proof attempt.

The source supplies no affine-line incidence count. Its main
error-correcting-pair characterization and gluing theorem are not used.
There is no generic-domain assumption, extension-weight descent or smoothness
requirement for this selected elementary shortening input.

## Reused coverage and quantitative comparison

Reuse the complete Hall extraction in
`2026-10-05-two-block-moment-obstruction.md`: J. I. Hall, *Notes on Coding
Theory*, GRS chapter, Theorem 5.1.1 and proof, printed pp. 63–64,
interpolation p. 65, undated author-hosted copy inspected 2026-10-05
([primary PDF](https://users.math.msu.edu/users/halljo/classes/codenotes/GRS.pdf)).
Any field, distinct labels, nonzero multipliers and 0<k<=n are allowed.
Here n=16,k=8 gives distance nine. L010 supplies the shifted-moment
kernel and eight-column injectivity. L032 supplies the actual rank-two
six-coordinate affine lift and its three prescribed values. Jurrius
(2012), Proposition 4.2, printed pp. 33–35, as inspected in the prior
classification assessment, interprets zeros using indexed column
hyperplanes; it counts zeros of the lift, not all sparse coset
representatives. Neither generic reproof is needed.

Reuse `2026-10-03-persistent-root-puncturing.md` for inspected proofs and
hypothesis comparison of BCHKS, WHIR, Habock and BCGM. Theorem-level
coverage of the pinned support event is distinct from July ABF26
identification, which remains unresolved. Rechecked Ben-Sasson, Carmon,
Habock, Kopparty and Saraf, *Improved Proximity Gaps for Reed–Solomon
Codes*, the [author-hosted PDF](https://www.math.toronto.edu/swastik/rs-proximity-gaps-2025.pdf),
Theorems 1.3 and 4.6, printed pp. 8 and 28–29; the prior assessment
records its November 11, 2025 version and inspected proofs. No changed
version identity is asserted from a new download.

This paper uses degree bound seven for dimension eight, so its reduced
rate is rho=7/16. Theorem 1.3 requires gamma<=Delta/2-1/n, with
Delta=1-7/16; its upper endpoint is 7/32, below the present cell.
Theorem 4.6 applies for gamma<1-sqrt(rho) and gives a same-support
exceptional-set bound. Its coefficient is
M * ((2*(m+1/2)^5+3*(m+1/2)*gamma*rho)/(3*rho^(3/2))*n
+ (m+1/2)/sqrt(rho)), with
m=max(ceil(sqrt(rho)/(1-sqrt(rho)-gamma)),3).
For M=1,n=16,rho=7/16 its displayed first term alone exceeds sixteen,
since m>=3 and rho<1. Thus this theorem supplies no count-fifteen import.
This is source applicability arithmetic, not a new MCA estimate or a
claim that the actual error exceeds the budget. Its useful-factor proof
mechanism was previously inspected; no further unchanged proof browsing
is needed for this strict quantitative mismatch.

## Duplicates and recorded failures

L015's full analytic proof was checked through its projective reduction:
a five-coordinate lift gives rational points attached to minimum-weight
codewords, then descends a line containing two distinct rational points.
It neither gives a six-coordinate configuration nor licenses descent for
a line meeting rational subspaces. Its finite maximum is excluded.
L032's converse concerns three local moment representatives only.
L031 excludes six actual supports with small union, not this triple.
L014's necessary fourth-power and exact affine-compatibility gates are
an alternative fallback; merely restating its equations does not bound
this six-coordinate class. No claimed new result is duplicated as an
import, and no broader result is inferred from these overlaps.

Three candidate mechanisms were compared within the reviewed target:
shortened-code incidence reduction reusing L015; actual-locator residual
analysis using L010/L014; and a universal incidence extraction or finite
rank sampling. The first has adequate standard coverage and a
case-completeness test. The second still needs a discriminating symbolic
obstruction and is not selected. The third repeats failed or exhausted
routes: ATTEMPTS/017 refutes the universal cluster criterion, /019 stops
seven-block containment, and /020 stops positive-only rank sampling.
Preserve those stops and all unfinished artifacts. Conditional shortening
does not assume any universal triple extraction.

## Bounded search and access record

Queries on 2026-10-07:
- `"Reed Solomon" "syndrome" "secant" line sparse`
- `"Reed-Solomon" "six" "four errors"`
- `"rational normal curve" "secant" "line" identifiability binary forms`
- `MDS code affine line sparse representatives minimum weight support syndrome`
- `shortening generalized Reed Solomon code polynomial product roots theorem`
- `"Reed-Solomon" "affine line" "syndrome" six`
- `"mutual correlated agreement" "Johnson" bound Reed Solomon`
- `"six" "syndrome" "pencil" Reed Solomon`
- `"shortening" "GRS" "product" "Theorem"`
- `"Reed-Solomon" "pencil" "six" syndrome`
- `"Reed-Solomon" "syndrome" "projective lines"`

The searches led to the inspected primary shortening passage and the
already assessed general MCA theorem. Binary-form identifiability,
Gaussian-mixture secants, cryptanalytic Schur-square claims and secondary
code summaries were discovery hits only; their full hypotheses and
proofs were not read and they are not inputs. The bounded search found
no inspected theorem with this exact six-coordinate fifteen-count
conclusion; that is not evidence of novelty or absence from the literature.

A guessed Hall `ModifyingCodes.pdf` URL returned Internal Error. This
is one failed URL, not an essential source blocker: ready Hall distance
coverage is reused and the institutional shortening manuscript was read.
Optional ePrint 2025/1712 and the campaign's missing proof artifacts
remain parked; no specific new primary-access lead appeared, so their
exhausted retrieval was not repeated. No progress beyond either unread
stronger claim is asserted.

## Continuation scope

Essential local inputs for the selected reduction are L010 and L032;
L015's analytic proof supplies a mechanism to adapt, not its five-set
bound or numerical maximum. Retain arbitrary F weights and finite
parameters, full-weight equality errors, every overlap with U, vanished
coordinates, common-subspace or coincident-intersection cases, and any
nonpersistent-locator or singular-value exclusion used. A projective
change of parameter must not silently drop the original finite point at
infinity. General incidence estimates, base-field descent, universal
extraction, global fifteen and ABF26 identification remain unresolved.

Mathlib coverage of the exact six-coordinate reduction and shortening
formula is not checked; no absence, matching formal theorem or Lean
verification is claimed. A separate newly written continuation assessment
records the exact next target and receives supervisor approval next turn.
This completed source review writes no lemma or mathematical script and
changes no mathematical argument or DAG edge.
