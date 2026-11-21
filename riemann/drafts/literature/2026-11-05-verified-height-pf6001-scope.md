# Verified height and fixed-order coefficient positivity — completed comparison

TARGET: Assess whether the published verified zero height and finite-order zero-sector theorems certify PF_6001 for the actual coefficient sequence (a_j).
CHECKED: 2026-11-05
DECISION: IMPORT
SEARCH_EVIDENCE: Reused step385/569 assessments; exact PF6001, verified-height, Schoenberg-sector and height-number searches in local lemmas and the named continuation/failure records found L813 and L466 but no matching canonical PF6001 import. External exact-title, sector, 2607.16795 and Riemann/PF6001 queries; primary passages inspected below, with no novelty inference.
SOURCE_EVIDENCE: Michałowski arXiv:2607.16795v1 Section1.1 (1)–(3), full Section1.2 sector/height argument and Remark8.3; Katkova math/0505174v1 Definition2, Theorem B and full Theorem1 product-limit proof, printed pp.4–6; Platt–Trudgian 2004.09765v1 Theorem1 and Section2, printed pp.2–3. Schoenberg's original publisher landing page was accessible but its full text was not; use the precise reproduced theorem as specified below.
COMPARISON: The inspected sector/height argument already covers a much larger fixed finite-order region and therefore the nominated PF6001 scope. PF means every ordered Toeplitz minor of size at most the order, not merely consecutive minors. L813 imports only one order-five cell; L466 concerns different Laguerre coefficients. Neither is a duplicate of this full coefficient-PF scope.
GAP: Only canonical citation/applicability for the fixed order remains: exact ordinary coefficients, sector inequality, real grouped products, coefficient limits and positive rescaling. Strictness, determinant margins, hybrid paths and all orders are outside coverage; no mathematical result is derived in this literature turn.
REASON: Import the known finite-order input instead of treating its nonnegative signs as unknown or reopening the stopped hybrid ratio. This is useful local source coverage, not progress beyond the inspected sources or a solution of RH.
LITERATURE_REASON: Order6001 with published verified height lies outside the ready order-five assessment; essential theorem applicability is missing, while an existing broader verified-height discussion may already cover it.
SCOPE: Completed literature-only comparison. A separate fixed-order KNOWN_IMPORTED applicability continuation is nominated below and requires next-turn approval; no lemma or mathematical script was written.

## Starting nomination retained

The following nomination records the question as supplied to step660;
its pending-source statements are superseded by the completed comparison.

Use a_j=lambda_j/(8*4^j) as in L018/L021/L776, extended by zero to
negative indices. PF_6001 means every ordered finite Toeplitz minor
of size at most6001 is nonnegative. That is the target, not a property
established here. D_(6001,6000) is only one such minor; actual PF
does not by definition supply a hybrid reference sign or error margin.

Start with relevant passages of
`2026-11-04-actual-jensen-mechanism-discovery.md` (step385) and
`2026-11-05-actual-theta-order-five-cell-coverage.md` (step569).
The latter explicitly reports a stronger verified-height region in
Wojciech Michalowski, arXiv:2607.16795v1, Section1.2. Read its exact
hypotheses and conclusion before proposing any reproof. Retain the
Katkova printed PF44 versus sector-index mismatch; do not import an
unchecked maximal-order endpoint. L813 is the canonical order-five
import, not evidence for order6001.

Retrieve Platt–Trudgian's exact theorem and verification scope, and
any essential product-limit theorem. Check scales, sector boundaries,
multiplicities and local duplicate claims. An unread original is a
lead, not evidence. No cross-notebook input is proposed; Mathlib
coverage is unchecked.

Downstream use: establish a bounded actual mixed-sign region and
remove redundant finite-order searches. All-degree positivity and
hybrid regularity remain separate. Continue only to a precise import
or separately approved applicability calculation; cite duplicates
instead of reproving them. Park an essentially source-blocked variant.

No justified central creative mechanism is prepared. The blocker is
an independent quantitative all-order sign mechanism. The established
finite-order source question must not be labeled creative.

## Completed primary comparison — step660

The main gap is actual-Xi all-degree mixed positivity. This review's
intermediate target is source coverage for PF_6001 of the actual ordinary
coefficient sequence. Its downstream use is a bounded known sign input
and the removal of redundant negative-minor searches. The discriminating
test is an inspected sufficient theorem covering all ordered minors,
with the exact generating function and an admissible sector; otherwise
record the missing hypothesis and do not calculate determinants.

### Inspected statements and essential cases

Wojciech Michałowski, *An explicit uniform cubic wedge for consecutive
Toeplitz minors of the Riemann xi-coefficients*,
[arXiv:2607.16795v1, 18 July 2026, Section1.2](https://arxiv.org/html/2607.16795v1#S1.SS2),
explicitly gives nonnegative consecutive minors at every k for
r<=floor(pi H)-1, H=3,000,175,332,800. The preceding sufficient theorem
is coefficient PF_m, and the displayed argument uses
w=4(rho-1/2)^2 and pi-|arg w|<1/H for the unverified zeros.
Its admissibility condition is m+1<=pi H. Order6001 is safely inside
this condition; no maximal-order endpoint is needed. Section1.1 defines
exactly the G of L776, including negative-index zeros. Remark8.3
repeats the independent finite-order sector region. Theorem1.1's strict
cubic tail and its certificates are unnecessary for this import and
were not audited here. Broad claims of an open complementary region
in Remark1.2/8.2 cannot erase the stated bounded-order coverage.

Olga M. Katkova, *Multiple positivity and the Riemann zeta-function*,
Comput. Methods Funct. Theory7 (2007),13–31,
[DOI10.1007/BF03321628](https://doi.org/10.1007/BF03321628).
Inspected numbering is [math/0505174v1](https://arxiv.org/pdf/math/0505174v1),
Definition2/(8), printed p.4; Theorem B and Theorem1 with its entire
short proof, pp.5–6. Definition2 specifies **all** ordered minors of
size at most m of the upper one-sided Toeplitz matrix, nonnegative.
Theorem B's sufficient hypothesis is a polynomial with positive
constant term and no zeros in |arg z|<pi m/(m+1). Its conclusion is
PF_m, not strict positivity. Theorem1's proof supplies the relevant
entire extension using an order-one-half genus-zero product with
positive constant, summable reciprocal zero moduli and compactly
convergent finite products. It then passes to the coefficients/minors.
The later import should state the real conjugate-grouped polynomial
case explicitly, as already qualified in L813, and retain repeated
zero factors. No simplicity assumption or uniformity over infinite
matrix sizes is part of that passage. These are the cited proof cases,
not a new product argument proved during this review.

Katkova attributes Theorem B to reference[29]: I.J. Schoenberg,
*A note on multiply positive sequences and the Descartes rule of signs*,
Rend. Circ. Mat. Palermo(2)4 (1955),123–131,
[DOI10.1007/BF02846031](https://doi.org/10.1007/BF02846031).
This is the sufficient sector theorem, distinguished from the
necessary sector theorem attributed there to reference[28].
The original publisher page and PDF endpoint returned a subscription
preview, not the theorem text. The original proof remains unread;
no original theorem number is invented. Coverage uses the precisely
reproduced Theorem B together with Katkova's inspected application
proof and Michałowski's explicit height argument. Thus this access
failure is not an essential blocker. No reciprocal-generating-function
closure theorem is used. The printed PF44 versus 43*pi/44 mismatch
remains excluded; neither that inference nor a corrected maximal
Katkova order is imported.

Dave Platt and Tim Trudgian, *The Riemann hypothesis is true up to
3 times 10^12*, Bull. London Math. Soc.53 (2021),792–797,
[arXiv:2004.09765v1](https://arxiv.org/pdf/2004.09765v1),
Theorem1, printed p.2, states the verified height H=3,000,175,332,800.
Read the theorem and Section2, pp.2–3: sign-change counts, a Turing
count excluding omitted zeros, and Arb arithmetic. Import this as a
published rigorous verification, not a new replay or a list of sampled
zeros. The stated positive-height range is closed at H. L018's
conjugation handles negative heights; the real-height-zero case must
be addressed using L021's imaginary-axis positivity. No simplicity
claim is required. L466 supplies an existing exact local citation,
not its distinct Laguerre-sign conclusion as a PF premise.

### Applicability and overlap decision

L018/L021 and L776's definitions identify the actual entire function
and ordinary coefficients. L813 has already checked the relation to
Katkova's xi_1(w/4)/8 convention. A subsequent canonical applicability
step must retain positive constant/geometric factors for arbitrary
increasing row/column selections, including zero negative indices;
no factorial change, row reversal or exponential-coefficient convention
is allowed. The sector index is m=6001, hence m+1=6002, unrelated to
k=6000 in one selected minor. Only nonnegativity is covered. No bound
for det B, an adjacent cofactor, a singular value or a relative margin
follows from a nonnegative sign statement alone.

The exact local searches found no existing canonical PF6001 claim.
L813 is a weaker cell import. L466 is all Laguerre orders at bounded
real centers, a different matrix family. The step659 hybrid stop is
preserved: its uncertain reference entry and whole interval are not
actual coefficient sequences to which this theorem automatically
applies. Nothing here supplies the missing strict determinant ratio.
All-degree mixed signs, quantitative stability and any uniform
unverified-height bridge remain independent gaps.

Queries included the exact Schoenberg titles with sector/1955/PDF,
2607.16795 with sector/positive, and Riemann/PF/6001. Search hits
were leads only. Reused step385/569 rather than repeating their
unrelated proof audits; read only the relevant L018/L021/L466/L776/L813
passages and step659 working/stop/history. No sibling notebook was
read. Full matching Mathlib coverage remains unchecked. Screenshot
requests failed; the complete relevant PDF text passages above were
retrieved and read, so no screenshot was treated as evidence.

**Decision:** known-result coverage is sufficient for a fixed-order
import, with no theorem reproof or numerical determinant experiment.
The exact follow-on target is saved in
[the import assessment](2026-11-05-verified-height-pf6001-import.md).
It requires separate next-turn approval. Stop that import on an actual
normalization, real-product or sector mismatch rather than manufacturing
an estimate. This review creates no lemma, mathematical script or
change in PROOF/DAG. The main gap remains open. A central creative
nomination remains blocked by the absence of an independent all-order
signed mechanism; routine specialization is not relabeled creative.
