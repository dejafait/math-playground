# Three-support fixed-block classification: source comparison

TARGET: Review known results and local duplicates for classifying three L010 equality error supports whose union has size at most eight via their fixed-block affine lift.
CHECKED: 2026-10-07
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Narrow comparison of L010, L015, L031, L006/L007's affine and root-count passages, L016's hypotheses and ATTEMPTS/017, /019, /020; new exact-support, sparse-affine-line and projective-system searches and primary readings are recorded below.
SOURCE_EVIDENCE: Reused Hall Theorem 5.1.1 and complete proof, printed pp. 63–64, interpolation p. 65; read Jurrius (2012), sections 4.1–4.2, Proposition 4.2 and its coordinate-vanishing justification, printed pp. 33–35; inspected a newly found campaign report's Theorem 5.1 and Table 2, without its unavailable proof artifacts.
COMPARISON: Hall and L010 cover the fixed moment block; L006/L007 already contain sparse-affine root accounting, and Jurrius supplies its indexed-hyperplane interpretation. L015 treats five-coordinate pencils, L016 fixes a nine-coordinate triple and L031 excludes six supports; none states this three-support classification. No progress beyond unread stronger sources is claimed.
GAP: Specialize the ready affine-coordinate mechanism to classify possible coordinate-occurrence patterns and nonzero weight relations at three actual four-errors inside one block; do not reprove the generic mechanism or assume that a permitted triple extends to sixteen-count equality.
REASON: Standard input coverage is sufficient for a bounded reproduction; the remaining triple specialization is precisely identified and has not been derived during this literature turn.
SCOPE: Finite F containing H of order sixteen, dimension eight, pinned radius cell, L010 nonzero D and nonzero coordinate-locator polynomials, sixteen-count equality, three distinct finite parameters with actual full-weight four-errors and union of size at most eight; all labelings and extension-field weights retained. L015's additional F_97 and F_(97^20) hypotheses must be stated whenever its conclusion is used.
COVERED_TARGET: Classify the support incidences and nonzero weight relations of three L010 equality errors at distinct finite parameters with union of size at most eight, using their fixed-block affine lift and separating L015's five-coordinate case.

## Gap, use and decision test

The main gap remains arbitrary-family sixteen-count equality, with error
interval 11/q–16/q against allowable fifteen. The intermediate target is
the COVERED_TARGET: a necessary classification for three selected actual
errors, retaining their parameter-dependent nonzero weights. It could
constrain small support unions and distinguish overlap with L015 before
attempting another compatibility obstruction. Neither a universal
small-union triple nor a global fifteen bound follows from this review.

Continue if one bounded mathematical attempt gives an exhaustive,
field-uniform description of the allowed coordinate-occurrence patterns
and their affine-weight relations, with every sufficiency claim explicitly
limited to the three selected errors. Abandon a proposed exclusion upon
a compatible triple, and park the classification if it only restates
L015 or needs an unproved global extraction or unavailable essential
source. No particular union bound, intersection size or exclusion is
asserted here. Triple compatibility is weaker than all L010 equality
gates; it is not a sixteen-count witness.

## Ready primary inputs and applicability obligations

Reuse [Hall's author-hosted GRS chapter](https://users.math.msu.edu/users/halljo/classes/codenotes/GRS.pdf),
undated copy retrieved 2026-10-05, Theorem 5.1.1 and complete proof,
printed pp. 63–64, with interpolation on p. 65, as extracted in
`2026-10-05-two-block-moment-obstruction.md`. Any field, distinct
evaluation points, nonzero multipliers and 0<k<=n are permitted. Here
H has sixteen distinct points, the multipliers are one and k=8, giving
distance nine. L010's written shifted-moment Vandermonde proof supplies
the invertible eight-coordinate block over F itself. No generic-domain
assumption or new distance proof is needed.

Read R. P. M. J. Jurrius, *Codes, arrangements, matroids, and their
polynomial links*, Eindhoven PhD thesis, 2012, version-of-record PDF,
DOI [10.6100/IR734704](https://doi.org/10.6100/IR734704), sections
4.1–4.2, printed pp. 33–35 (PDF pages 47–49), on 2026-10-07
([institutional primary PDF](https://pure.tue.nl/ws/portalfiles/portal/102837385/734704.pdf)).
For a nondegenerate linear code over a finite field with full-row-rank
generator G and no zero columns, Proposition 4.2 identifies the zero
coordinates of xG with the indexed column hyperplanes containing x.
Section 4.1 allows repeated hyperplanes and distinguishes simple
arrangements; multiplicities must be retained. The preceding
coordinate-inner-product argument supplies the justification. The
extension-code discussion embeds the same arrangement over the larger
field. This is weight/zero accounting, not a three-error classification.

For a later application to an affine lift, zero columns must first be
removed and the actual row rank handled. Rank two permits this
description with the two affine coefficients as rows and the selected
finite parameters as message vectors (1,gamma). Rank one needs its own
case or a basis of the actual row span; full rank may not be assumed
merely from three parameters. Repeated column directions and nonzero
constant affine coordinates are allowed. No projective parameter change,
generic generator or descent of arbitrary weights to F_97 is licensed.
These are applicability obligations for later mathematics, not checked
claims about the selected triple. The theorem is a supporting named
input, not an IMPORT of the requested classification.

Also inspected D. R. Kohel, *Coding theory: algebraic geometry of linear
algebra*, undated [author-hosted notes](https://www.i2m.univ-amu.fr/perso/david.kohel/pub/codes.pdf),
section 3, Theorems 0.1–0.2 and the evaluation-map proof, printed pp. 2–3.
This supplies related projective-system terminology with repeated
points. Its weight-enumerator formula is an exercise, not a proved
matching classification; its broad ring formulation is unnecessary
here. Jurrius's finite-field statement is the more precise proposed input.

## Local duplicates and preserved failures

L031's full proof and audit already construct a fixed-block affine
lift after enlarging a smaller union to eight coordinates and compare
it only with actual errors at the selected parameters. Its contradiction
uses six selected supports and L010's four-incidence fact; it cannot
be imported as a triple exclusion. L010's moment-kernel/invertibility
and equality/distinct-support passages were read for the exact inputs.

L006's proof interpolates two errors and uses the code distance to
annihilate a discrepancy supported in a triple union. It then counts
zeros of nonzero scalar affine coordinates, including constants.
L007 reuses that accounting in its common-lift branch. Their respective
global hypotheses 3r<=n-k and d=3r do not hold for n=16,k=8,r=4;
their global counts are not applicable here. Their already written
mechanism must be reused rather than advertised as a new affine-lift
theorem. The proposed work is only the remaining three-point pattern
and weight specialization under an explicitly assumed small union.

L015 was read in full. It assumes a five-set A representing both input
syndromes, specifically over F_(97^20) with H inside F_97. Its conclusion
is |B(a,b)|<=5+M(A), with a stronger dependent-syndrome case; its analytic
reduction does not supply M(A)'s value. The recorded maximum six depends
on a complete finite configuration certificate, not on this source
review. No new verification or extension of that certificate is claimed.
Its pair-with-three-coordinate-intersection consequence must remain
separate from a classification of arbitrary triples over arbitrary F.
L016's hypothesis and initial discrepancy argument were checked: its
saved union has nine coordinates, outside this target, and its fixed
labels and parameters are not a universal normal form.

ATTEMPTS/017 refutes universal six-edge/eight-vertex extraction;
ATTEMPTS/019 stops the already exhausted seven-block containment search;
ATTEMPTS/020 stops positive-only finite rank sampling. These stops remain
intact. The conditional triple question uses actual moment compatibility
and does not reopen any of those universal or sampling assertions.
The previously inspected Lovett FOCS 2018 Theorem 1.2 and
Brakensiek–Gopi–Makam arXiv:2206.05256v4 Definition 1.4, Theorem 1.12 and
Corollary 1.15 comparisons in `2026-10-05-cyclic-0125-affine-compatibility.md`
are reused: selectable/generic evaluation points and common-intersection
statements cannot be silently applied to this fixed H and affine line.

## New discovery search and unread leads

Queries on 2026-10-07 included `"affine line" "constant weight" codes
supports`, `"MDS" "three" "error supports" affine`, `"linear code"
"dimension two" "weight distribution" projective points`, `"Reed
Solomon" "three" "small union"`, `"projective systems" "weight"
"hyperplanes" linear codes notes`, `"three collinear" "constant
weight" code`, `"two-dimensional" "linear codes" "weight distribution"`,
`"three" "error supports" "Reed" "affine"`, `"three collinear"
"codewords" weight`, `"affine line" "Hamming weight" "supports"`,
and `"Reed-Solomon" "small union" triple`. These found the primary
inputs above and the report below, not an inspected matching triple
classification. No novelty follows from this bounded search.

A new lead was *The Million-Dollar Window* campaign webpage,
[section 3.2](https://deltastar-paper.pages.dev/), inspected 2026-10-07,
and its linked June 2026 report, *The delta-star Localization: Reducing
the Proximity Prize to One Inequality, and Machine-Checked Proofs of Why
the Elementary Roads Are Blocked*, Theorem 5.1 and Table 2, printed
pp. 6–7 ([primary PDF](https://deltastar-paper.pages.dev/deltastar.pdf)).
They discuss global distance/band bounds, not this conditional
three-error classification. Their boundary row is relevant to a
four-omission cell, but the webpage includes a band-divides-length
qualification absent from the PDF table; this cell has band five and
length sixteen, which fails that webpage qualification. The displayed
proof-artifact link `UniversalStaircaseCollapse.lean` and its corresponding
raw main-branch URL both returned HTTP 404. No proof cases or formal
hypotheses from that artifact were inspected; no claimed bound,
machine-checking status or challenge identification is imported. Broader
claims and their proofs are outside this review. This optional overlap
is parked without further retrieval attempts; it is not essential to
the Hall/L010/local affine specialization.

The ePrint 2025/1712 theorem text remains unread and parked as recorded
in the six-support assessment. No new access lead for that paper arose,
so its exhausted retrieval was not repeated. This assessment certifies
adequate standard ingredient coverage, not originality or progress
beyond either uninspected stronger-source claim.

## Continuation limits

The direct mathematical inputs for the proposed attempt are L010 and
the existing fixed-block passage in L031; L006/L007 and Jurrius identify
the known mechanism to specialize. L015 is a scope-limited comparison,
not a uniform premise outside its field hypotheses. Retain all eight
shifted moment equations, three distinct finite parameters, actual
full-weight errors, the hypothesized small union, and the full L010
polynomial nonvanishing and equality assumptions. No universal cluster,
triple classification, extension to all sixteen errors, global fifteen
bound, ABF26 identification or Mathlib coverage is established.

DECISION SPECIALIZE approves ingredient coverage for the COVERED_TARGET;
the newly written continuation receives separate supervisor approval
before invocation. The later step should be REPRODUCTION without a
claim of originality, importing the standard inputs by citation and
proving only the explicit specialization. This literature turn derives
no new support restriction or weight identity and changes no lemma,
mathematical script, DAG or proof argument. Mathlib coverage of the
exact classification and the supporting arrangement theorem is not
checked, with no absence claim.
