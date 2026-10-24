# Coverage: lower-band moving-saddle critical audit

TARGET: Critically audit L457's uniform moving-saddle margin on 7/8≤m/r≤31/32, including L456's fixed-disk input, positive normalization, full deformed contour and both residues.
CHECKED: 2026-10-23
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the exact-target search and duplicate/failure screen in drafts/literature/2026-10-23-lower-band-moving-saddle-coverage.md, plus its lower-band/logarithm/inversion assessments. Compared L457 Sections 1–6 and Mathlib, L456 through its full disk and inversion proof, L452 interpolation/Cauchy passages, and the two scoped lower-band outcome histories; no fresh external search.
SOURCE_EVIDENCE: Reused inspected DLMF 2.4.10–2.4.16 and Temme, arXiv:1308.1547v1, Sections 2.2–2.3, equations (2.9)–(2.13), and Section 4.1, (4.1)–(4.5); Titchmarsh–Heath-Brown (1986), Theorem 14.2 proof pp. 336–337 and Section 14.3 pp. 338–339; DLMF 1.14.20, 25.2(i)/25.2.4 and 5.11.3/5.11(ii). Exact citations, previously inspected cases and external trust limits are retained below and in the linked assessments.
COMPARISON: L457 uses the already assessed local Gaussian, analytic-logarithm, inversion, meromorphy and positive-real Stirling mechanisms. The sources do not give uniformity for this varying exponent or its arithmetic margin. No essential new source is required to audit those application estimates and the inherited full L456 disk; source coverage does not certify their correctness.
GAP: Independently check the complete closed-band disk construction and inclusion, real saddle and Taylor constants, m+1 exponent, factorial and orientation, shrinking annulus, all middle/far tails, fixed-parameter connector limits and both original residues, relative to the same positive M*. No changed-band theta theorem or external-manuscript audit is authorized.
REASON: Separate literature-only comparison now approves precisely the written argument's audit scope by existing primary-source coverage. The new result remains unaudited; approval of its methods neither rejects the completed attempt nor accepts its mathematical conclusion.
SCOPE: L457's exact real-r/even-m domain and direct L452/L456 analytic inputs under the unchanged pinned external premise; no external-manuscript audit, theta-sector extension, every-height transfer or RH claim.

The initial proposal required a separate scope review. That review is
completed below; its SPECIALIZE decision authorizes the exact audit
target on the next mathematical turn. No essential new primary source
has been identified. Do not repeat browsing for this unchanged scope.

The exact current proof is
[L457](../../lemmas/L457-lower-band-uniform-moving-saddle-margin.md).
Its direct local analytic inputs are L456 and L452. Check L456's full
logarithm disk, rather than substituting its narrower statement strip;
the fixed-circle obstruction itself need not be reproved for this audit.
L303/L330/L331/L454 are prior method/obstruction comparisons, not
extra unproved arithmetic hypotheses for L457.

Retain September 30, 2026 Theorem 1.1 at commit
`1581d4cbdd69a0faf34b2089614fe2a814316a6a`, strict Re(s)>7/8,
the allowed pole, and unaudited manuscript/import closure. Verify
the exact m+1 exponent and positive factorial scale before comparing
errors. In particular, the shrinking annulus must use its quadratic
real-part estimate, whereas the global subexponential product bound
is used only beyond a fixed window. Check complete shifted-height-zero
neighborhoods and the order of the fixed-parameter contour limit.

The target is a partial arithmetic margin; the main RH gap, changed-band
theta reduction, every-height passage, smaller indices, bounded heights
and selected-law/regulator questions remain separate. Full Mathlib
coverage is unchecked; no absence or originality is asserted.

## Completed audit-scope comparison — 2026-10-23

This is a LITERATURE / NOVELTY_UNCHECKED / EXPLORATION step. It
approves a bounded independent critical audit, not L457's conclusion.
The subsequent mathematical task is REPRODUCTION unless a new target
requires a new assessment. No theorem has been imported or reproved in
this step, and no lemma, mathematical script, DAG or main argument changes.

### Primary evidence reused and precise limits

The [attempt assessment](2026-10-23-lower-band-moving-saddle-coverage.md)
records actual inspection of [DLMF 2.4(iii)–(iv)](https://dlmf.nist.gov/2.4#iii),
2.4.10–2.4.16: analyticity and endpoint convergence/gap hypotheses,
two half-paths at the simple saddle, and the direction-selected square
root. [Temme (2013), arXiv:1308.1547v1](https://arxiv.org/html/1308.1547v1),
Sections 2.2–2.3 and 4.1, supplies Gaussian reduction, the additional
parameter warning and separate pole handling. These inspected cases
cover the mechanism used in L457 Sections 1, 3–5. Neither text supplies
its changing paired-zeta exponent's uniform estimates. Flajolet–Sedgewick
remains an unread, nonessential lead; the prior retrieval failure does
not block this audit.

The [Littlewood assessment](2026-10-21-fixed-half-plane-endpoint-derivative-review.md)
records the inspected [Titchmarsh–Heath-Brown second edition, pp. 336–339](https://sites.math.rutgers.edu/~zeilberg/EM18/TitchmarshZeta.pdf#page=173).
The printed RH assumption is stronger than the pinned premise; only the
analytic logarithm, Borel–Caratheodory, three-circles and Cauchy proof
mechanisms are reusable. L456's proof changes the disks. Its radius
273/256 full-modulus statement, rather than L452's narrower derivative
conclusion, is the actual inherited input requiring audit. The disk
construction itself is within scope, not an accepted consequence of
this literature comparison.

The [inversion assessment](2026-10-23-subendpoint-relative-mellin-coverage.md)
records the inspected hypotheses of [DLMF 1.14.20](https://dlmf.nist.gov/1.14.E20):
continuity, piecewise continuous derivative, exponential growth and an
inversion line to its right. [DLMF 25.2(i)/25.2.4](https://dlmf.nist.gov/25.2)
records absolute Dirichlet convergence only to the right of 1 and the
simple unit-residue pole. [DLMF 5.11.3 and error bounds](https://dlmf.nist.gov/5.11)
cover positive-real Stirling. These cover the source operations in
L457 Sections 2–3 and L456's inversion, but not uniform contour errors.
The elementary all-height growth formula is in L452's proof; its use
near shifted height zero and its pole clearance must also be audited.

### Bounded audit and decision test

Inspect the full relevant evidence in the canonical proofs. Start with
L456's complete disk construction and L452's growth identity, then test
L457's disk reserves at both closed endpoints. Check all derivatives
and one common real-r onset. Independently recompute the bare factorial
scale at N=m+1 and verify upward orientation and the positive root.
Distinguish the quadratic real-part estimate on the shrinking annulus
from the subexponential product bound beyond a fixed window. Check
finite rectangles and connector limits at fixed parameters before
uniform tail estimates, including both shifted-height-zero neighborhoods
and both original residues. Finally compare the complete error with
M* and its claimed lower scale, retaining the exact coupled a(r,m).

Continue only if every contribution and inherited analytic input is
justified on the full domain with a common onset. A failed estimate,
missing hypothesis or incorrect normalization requires a precise
recorded defect and qualification or repair within the approved audit;
an uncontrolled complement cannot be counted as a positive margin.
This is an audit test, not a calculation or correctness verdict here.

The scoped duplicate/failure comparison reuses the attempt assessment
and the fixed-circle and moving-saddle outcome histories. L456's
fixed-center certificate and L331's shrinking-domain obstruction retain
their stated scopes; auditing the different moving-saddle proof does
not reopen those exhausted certificates. L323/L327 and fixed-r/unit-phase
stops remain preserved. No novelty inference follows from the searches.

The main unresolved claim remains global mixed positivity and the
initial low-index signs. A validated arithmetic margin could support a
separately assessed lower-band theta reduction. That reduction,
every-height passage, smaller indices, bounded heights and all
selected-law/regulator gaps remain independent. Mathlib matching
coverage is unchecked, and no absence is asserted. The exact pinned
external premise and unaudited manuscript/import closure remain as
stated above; this review performs no external verification.
