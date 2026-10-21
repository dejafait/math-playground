# Conditional six-support fixed-block obstruction: source comparison

TARGET: Review known results and local duplicates for excluding L010 equality when six of its full-weight error supports have union of size at most eight.
CHECKED: 2026-10-06
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Compared L010, L024, L025, relevant L015/L016 proof ranges and ATTEMPTS/017, /019, /020; reused the Hall extraction and small-union assessment; searched affine-syndrome, MDS sparse-line and six-support terminology, with queries and access limits below.
SOURCE_EVIDENCE: Reused J. I. Hall, Notes on Coding Theory, GRS chapter, Theorem 5.1.1 and complete proof, printed pp. 63–64, interpolation p. 65, inspected 2026-10-05; read the primary ePrint 2025/1712 abstract and metadata only, not its inaccessible theorem text.
COMPARISON: Hall supplies RS distance, L010 supplies moment injectivity, and L024 supplies the exact-family affine-lift mechanism; none of these inspected statements gives the arbitrary-six-support conclusion. L015/L016 cover different support sizes or fixed triples. Full overlap with ePrint 2025/1712 is unresolved, so no originality or progress beyond that source can be claimed.
GAP: For six arbitrary distinct four-supports inside one block of size at most eight, justify a single affine error lift and test its full-weight zero pattern; the implication and any combinatorial contradiction remain unproved here.
REASON: Adequate inspected standard inputs support a bounded reproduction/specialization attempt without importing an unread claim; the optional stronger-source comparison is parked, not a premise or a novelty certification.
SCOPE: The TARGET and COVERED_TARGET only, under L010 equality over every permitted finite field with H of order sixteen, six distinct finite parameters, six distinct full-weight four-element error supports whose union has size at most eight; no universal cluster-existence claim.
COVERED_TARGET: Prove or refute that six distinct full-weight four-error supports with union of size at most eight cannot occur in L010 equality, using a fixed-block affine moment lift.

## Main gap and bounded target

The frozen four-omission interval is still 11/q–16/q against allowable
fifteen. Excluding this conditional cluster could enlarge L024's
applicability beyond its exact doubled family. It cannot cover families
without such a cluster, and L025 expressly prevents assuming the cluster
exists in every matching-two family. Arbitrary triples, larger matching
number, the global fifteen bound and ABF26 identification remain open.

Continue only if the fixed-block lift is justified at every one of the
six actual parameters and the resulting affine coordinate functions have
an incompatible zero pattern under the exact full-weight assumptions.
Abandon this proposed exclusion if a compatible realization is found or
a required step needs a hypothesis unavailable from L010 equality.
Retain singular values, identically zero coordinates and extension-field
weights explicitly. This source review does not carry out either test.

## Reused primary input and specialization obligation

Hall's [author-hosted GRS chapter](https://users.math.msu.edu/users/halljo/classes/codenotes/GRS.pdf),
undated online copy retrieved 2026-10-05, Theorem 5.1.1, printed pp. 63–64,
allows any field, distinct evaluation points, nonzero column multipliers,
and 0<k<=n, and gives dimension k and minimum distance n-k+1. Its inspected
proof uses polynomial root counting and an explicit product attaining the
bound; interpolation uniqueness is discussed on p. 65. The complete
extraction is preserved in `2026-10-05-two-block-moment-obstruction.md`.
No unchanged source retrieval is repeated.

For this target H has sixteen distinct nonzero elements; multipliers
one, n=16 and k=8 satisfy the theorem and give distance nine. L010's
already written Vandermonde argument gives injectivity on coordinate
sets of size at most eight and identifies the kernel with C. These facts
are ready inputs, not new theorems or decoding results to reprove.
L024's complete proof was read: it lifts a pencil on an eight-coordinate
block and compares that lift with actual errors only at assigned
parameters. Its incidence argument uses its precise eight-support family.
The new target must handle a block smaller than eight and six arbitrary
supports without borrowing L024's degree counts. That remaining passage
requires a later proof; SPECIALIZE does not certify it now.

## Duplicates, failures and mechanism comparison

L010 equality supplies distinct supports, full weights, distinct finite
parameters and degree-four incidence. L024 is an exact-family result,
not the conditional statement. L015's five-coordinate reduction and
L016's saved nine-coordinate triple do not state this six-support result.
The narrow lemma search found these overlaps, not a matching canonical
lemma; absence from that search is not novelty evidence.

Three mechanisms were compared. Positive-only universal-rank sampling
has exhausted its three exploration turns (ATTEMPTS/020); it supplies
no all-labeling theorem. Incidence extraction is refuted by L025 and
ATTEMPTS/017; the seven-block containment route also stops at ATTEMPTS/019.
The selected mechanism instead tests actual affine moment compatibility
inside an explicitly hypothesized fixed block. It neither repeats the
sampling nor reopens universal incidence extraction. Original stops and
certificates remain intact. No mathematical exploration counter is reset.

## New search evidence and unread lead

Queries on 2026-10-06 included `"Reed Solomon" "affine" "syndrome"
"support"`, `"MDS" "affine line" "sparse"`, `"Reed Solomon" "six"
"supports" "eight"`, `"affine line" "fixed support" coding syndrome`,
`"Reed Solomon" "small union" supports`, `"Russell Okamoto" "small union"`,
and `"The Syndrome-Space Lens" pdf theorem`. Unrelated search results
were not treated as mathematical evidence. The prior small-union review's
Frankl–Luczak–Mieczkowska and Shangguan comparisons are reused for the
incidence question only; they do not cover moment compatibility.

Russell Okamoto, [The Syndrome-Space Lens: A Complete Resolution of Proximity Gaps for Reed-Solomon Codes](https://eprint.iacr.org/2025/1712),
primary landing page inspected 2026-10-06, records receipt 2025-09-20
and approval 2025-09-21. Its abstract mentions small-union witnesses.
The PDF link was blocked by robots policy; a single shell retrieval failed
DNS resolution, and a title/author search found no accessible primary
replacement. No repeated download or larger secondary extract was used.
The exact theorem hypotheses, proof cases and any overlap with this
conditional target remain unread. This is a parked stronger-result lead,
not an imported input or evidence that the requested result is absent.
A future claim of progress beyond this source requires theorem-level
comparison first. The bounded continuation is classified REPRODUCTION
and uses Hall/L010/L024 alone; their adequate input coverage does not
depend on this lead or any of its abstract's claimed resolutions.

## Continuation qualifications

Essential local inputs are L010 and L024; L025 is a contrast preventing
an unjustified existence assumption. Hypothetical equality, six actual
full-weight errors, one affine syndrome pencil, distinct parameters and
the small union must be retained. No disjoint-pair reduction or global
classification is supplied. Mathlib coverage of the exact conditional
statement and affine lifting is not checked; no absence claim is made.
The newly written ready COVERED_TARGET receives separate supervisor
approval before research. No lemma, mathematical script, DAG or proof
argument is changed in this literature turn.
