# Monic root-product endpoint attainment: completed scope assessment

TARGET: Determine whether the monic root-product construction attains L001's A=k common-support bound on the pinned smooth domains for every m>=1, and compare the resulting necessary field-size condition with epsilon* q.
CHECKED: 2026-10-03
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Completed the endpoint search using monic-polynomial lower bounds, deep holes, distance distribution, arbitrary evaluation sets and interleaved covering-radius terminology; exact queries and exclusions are recorded below. Reused the recovery's higher-order MDS and additive-subspace comparisons.
SOURCE_EVIDENCE: Read Ben-Sasson-Kopparty-Radhakrishnan's author-hosted manuscript, Sections 1.2-1.3 (pp. 2-3), Proposition 3.4 and its proof (p. 6); Li-Wan, arXiv:1806.00152v3 (2019-07-30), Theorem 1.2, Section 1.2, Corollary 1.6 (pp. 2-4), and the initial interpolation/counting passage in the proof of Theorem 2.1, Section 2. Read the local pinned model and L001; rechecked the prize statement on 2026-10-03.
COMPARISON: Known scalar full-field results give the root-subtraction mechanism and an exact degree-k-center distance distribution. The full TARGET needs the prescribed evaluation-subset and simultaneous-tuple specialization, with strict message degree and the given base-field threshold retained; no direct matching interleaved theorem was inspected.
GAP: The local endpoint attainment and necessity comparison have not been proved. The remaining work is an explicit applicability argument for the known construction on the fixed smooth subset and every m>=1, followed by comparison with L001 and epsilon* q; other grid levels and the ABF26 definition comparison remain unresolved.
REASON: The readable primary construction and named distance-distribution formula supply adequate coverage without relying on unread original references. Approve a later mathematical reproduction of only the domain/metric specialization; no new result, sharp field condition or complete candidate is derived in this literature turn.
SCOPE: Fixed finite field and pinned power-of-two multiplicative-coset domain, n>=16 and one of the four prize rates, m>=1, strict row degree less than k, closed column-Hamming ball at A=k. This assessment covers the saved endpoint action only, not improved bounds at A>k, differential covers or recovery of ABF26.

## Gap, use and bounded test

The [pinned model](../../foundations/02-pinned-list-model.md) provides a
standalone setting: a multiplicative coset of power-of-two size, each
message row of degree less than k, and at least k columns agreeing in every
row. The target concerns an actual received-word list in that setting.
It is independent of the Riccati equation and its blocked ABF26 comparison;
matching this model to the full challenge still remains a source gap.

L001 bounds the endpoint list by binomial(n,k), but treats its associated
field condition only as sufficient. The intended downstream use is to
decide its sharpness for the fixed field and clarify where a search for a
smaller safe grid radius is needed. No complete challenge resolution would
follow: the other agreement levels remain unresolved.

The test sought is a single received array with distinct candidate tuples,
the correct degree restriction and simultaneous agreement, whose count
meets L001's endpoint upper bound. A successful test must state the exact
comparison with epsilon* q and use the specified field. A failed test must
identify the domain, degree, distinctness or common-center obstruction;
failure of an upper-bound certificate alone is not an unsafe-list witness.
No center, multiplicity formula, new inequality or computation is supplied.

## Primary results actually read

Eli Ben-Sasson, Swastik Kopparty and Jaikumar Radhakrishnan,
[Subspace Polynomials and List Decoding of Reed-Solomon Codes](https://www.math.utoronto.ca/swastik/rsld.pdf),
author-hosted eight-page manuscript, accessed 2026-10-03. No date, revision
identifier or file hash was recovered; the 2010 journal version was not read.
Section 1.2, p. 2, uses degree at most K and then fixes the full N-element
field. Section 1.3, p. 3, obtains a list of size at least
binomial(N,T) N^{-(T-K-1)} through monic root polynomials sharing high
coefficients. Proposition 3.4 and its proof, p. 6, explicitly relate a
root-rich polynomial family with a common pivot to one scalar received-word
list. These supply the mechanism directly. Its additive-subspace Theorem 2.1
has different domain assumptions, as already assessed in the
[recovery comparison](2026-09-26-current-target.md#2026-10-03-supervisor-recovery-a-different-gap).
Neither passage states the prescribed-domain, simultaneous-interleaving
TARGET. Text extraction was readable; a PDF screenshot returned only a
reference without a readable image.

Jiyou Li and Daqing Wan,
[Distance Distribution in Reed-Solomon Codes, arXiv:1806.00152v3](https://arxiv.org/pdf/1806.00152v3),
dated 2019-07-30, PDF and matching HTML read. Theorem 1.2, p. 2, treats an
arbitrary evaluation subset but gives distance, not the requested list count.
The counting results then fix the full field. Corollary 1.6, p. 4, gives
the exact scalar formula

\[
N(X^k,r)=\binom qr q^{k-r}
 \sum_{j=0}^{k-r}(-1)^j\binom{q-r}{j}q^{-j}.
\]

For 1<=k<=q-1 and 0<=r<=k, N counts polynomials g of degree at most k-1
for which X^k+g has exactly r roots in the full field. This includes the
scalar endpoint. Section 2's proof of Theorem 2.1 explicitly counts interpolation
conditions on distinct subsets. The paper's m is degree excess, independent
of this notebook's interleaving width. Its prime-field asymptotics are
unneeded here. The formula is attributed to A. Knopfmacher and
J. Knopfmacher, reference [15]; that original paper was not read.

The [current prize statement](https://proximityprize.org/) still requests a
list threshold epsilon* times the base-field size, constant interleaving,
the four designated rates and a smooth domain, with the field-existence
proviso. The separate live companion challenge is not substituted for this
target. The unread July ABF26 comparison remains parked; it is unnecessary
for work explicitly confined to the already pinned model.

## Search record and unread leads

Reused the recovery queries and exclusions; the new queries were:

- `Justesen Hoholdt bounds list decoding Reed Solomon codes monic polynomials arbitrary evaluation points binomial n k`
- `Reed Solomon covering radius deep holes list size binomial n k polynomial degree k evaluation set`
- `"Justesen" "Høholdt" "Bounds on list decoding" 2001 pdf`
- `"Reed-Solomon" "binom" "deg(u) = k" distance distribution`
- `"distance distribution" "Reed-Solomon" "binomial" "degree" Wan`
- `"list size" "binom{n}{k}" "Reed-Solomon" deep`
- `"Bounds on list decoding of MDS codes" site:orbit.dtu.dk`
- `"Reed-Solomon" "deep holes" "binomial" evaluation set list`
- `"interleaved" "Reed-Solomon" "covering radius" list size monic`
- `"Reed-Solomon" "monic" "arbitrary" "list size" root polynomials`

Search metadata identified Justesen and Høholdt, *Bounds on list decoding of
MDS codes*, IEEE Transactions on Information Theory 47(4), 1604-1609 (2001),
[DOI](https://doi.org/10.1109/18.923744). No primary text was recovered;
it is an attribution lead, not an inspected theorem. The readable manuscript's
complete mechanism argument removes the need to make that source essential.
Likewise the unread Knopfmacher reference is not an extra prerequisite for
citing Li-Wan's stated formula and inspected supporting proof passage.

The NSF copy of Li-Wan and the author-site PDFs `deep.pdf` and `dist.pdf`
returned reader errors. The versioned arXiv PDF and HTML supplied the needed
Li-Wan text. No ABF26 retrieval path was retried. Search hits concerning
projective, twisted or other non-RS codes, Dickson-polynomial deep holes,
decoding complexity and informal guides were excluded; none supplied an
inspected match. Failed searches establish no absence or novelty.

## Applicability assessment and continuation test

The saved target, common-center test and pinned model remain unchanged from
the pending assessment. There is no established local endpoint-attainment
lemma. L001's upper count, L008's linear lower witness and the toy maxima
do not answer attainment; the latter motivate a test only. The earlier
failed q-polynomial transfer and unfiltered Riccati count address different
gaps. Repeating those routes or the parked source retrieval is unnecessary.

Only the following differences justify a local mathematical reproduction:

| Source scope | Required local check |
| --- | --- |
| Full-field scalar list | Use the fixed prescribed evaluation subset; roots elsewhere cannot count as agreements. |
| Degree at most K in the manuscript | Match K to the strict degree-less-than-k message convention and check cancellation and distinctness. |
| Scalar agreement | Check a common received array and common agreement columns for every m>=1; independent row lists do not suffice. |
| Exact distribution at one scalar center | Combine only after local attainment is proved with L001's worst-case upper bound and the specified epsilon* q. |

This is an applicability plan, not a derivation. The inspected mechanism
uses field polynomials and distinct roots; its statement does not impose a
prime-field or large-characteristic restriction. The smooth subclass needs
no random-domain guarantee for this test. Keep the given field fixed and
retain inclusive threshold equality. Continue if the construction survives
all four checks and attains the target count; abandon its claimed
specialization if degree, common-center, distinctness or simultaneous
agreement fails. A non-sharp lower count alone does not make the binomial
field condition necessary.

No center for the pinned domain, tuple construction, new bound or necessary
field condition is supplied in this turn. In particular L001's present
qualification is not edited. Even a successful later endpoint application
would leave the boundary below that grid point and the full-source comparison
open. The scalar mathematics is known by citation; the later local work
should be classified REPRODUCTION under SPECIALIZE, with no claim of
progress beyond the checked literature. Full-target novelty is not certified.

Completed-step outcome: EXPLORATION, STEP_KIND LITERATURE, classification
NOVELTY_UNCHECKED. This first complete scope comparison adds a versioned exact
formula and the inspected pivot proposition, makes the saved action ready,
and derives no result. Retain the entry exploration count 2/3; this
literature turn spends no mathematical exploration budget.

## Mathlib

Full endpoint-attainment statement: **not checked**. Supporting polynomial
factorization, interpolation and list-size theorems: **not checked** in this
assessment. ArkLib's pinned definitions support the model, not the claimed
attainment. Formal versions of the named distance-distribution and pivot
results: **not checked**. No matching library theorem is asserted.
