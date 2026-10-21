# 96a1 global Selmer certificate scope — completed source review

TARGET: Identify the exact unconditional certificate obligations needed to replace FNS's GRH-dependent 96a1 Selmer input.
CHECKED: 2026-10-10
DECISION: IMPORT
SEARCH_EVIDENCE: Reused the classification assessment and ATTEMPTS/013,017; searched exact 96a1/Selmer/GRH/certification terms and official class/unit/Selmer documentation; located FNS's primary section7.magma and a 2025 primary account of Magma certification. No unconditional 96a1 certificate was inspected.
SOURCE_EVIDENCE: FNS final manuscript dated June 10, 2019, Section 7.2, printed pp.25-29, Table 5 and Lemmas 7.6-7.7; primary section7.magma zero-based lines 4-15 and 255-416; Magma V2.29 handbook ClassGroup, UnitGroup, SelmerGroup, TwoSelmerGroup and LocalTwoSelmerMap; Elsenhans-Voight October 2, 2025 manuscript Sections 1,4,6-8; Milne ANT v3.08 Remark 2.25 and Theorem 4.3.
COMPARISON: The source supplies the exact descent algebra, five conditional generators and a local exclusion routine for the retained -512+2048 Z2 disk; a certified global upper image and a complete local comparison suffice at Lemma 7.7, before the later halving argument. Stored generators and dimension five do not certify completeness.
GAP: No unconditional arithmetic completeness data, localized upper-image certificate or center-fiber disjointness certificate has been computed here; a corrected arithmetic backend and its field-specific workload remain unestablished.
REASON: The certificate obligations and accessible source inputs are now identified by citation, narrowing the global branch test; full certification stays parked pending a bounded workload test, without another local witness search.
LITERATURE_REASON: Changed global two-descent target and essential unread certification/data interfaces, outside the ready local-realization audit scope.
SCOPE: Completed citation-based specification for 96a1 only; no class computation, new lemma, executable source copy, source rerun or unconditional branch exclusion. Subsequent arithmetic needs separate target approval.

## Original proposal and bounded test (preserved)

The main gap remains unconditional global emptiness of the surviving
ordered (3,4,11) twists, alongside other residual Beal signatures. The
proposed intermediate source target isolates one global upper-bound input
rather than repeating local witness searches. Its downstream use would
be to define a checkable unconditional certification attempt, if the
necessary data and theorem hypotheses can be supplied.

Essential local input IDs: L032 for the necessary 96a1 disk and L050 for
K96 and the limitation of local nonexistence; L034 only defines the
complete modular map. No new conclusion uses L045 or L033's 54a1 field.
No cross-notebook input is proposed.

Reuse `drafts/literature/2026-10-07-three-four-eleven-classification-coverage.md`
for its recorded conditional/unconditional distinction. In FNS Section 7.2,
read only the precise Selmer-computation interface, Lemma 7.7's 96a1 case
and the associated primary data/code references before broader passages.
The source identifies a cubic extension of K96 for class/unit input;
its exact defining model, the needed completeness guarantees and the
certifiable computation remain obligations, not established data here.
A numerical rank or conditional class-group table is insufficient.

Continue only if the review can specify an exact certificate package
with accessible primary inputs and a discriminating verification task.
If critical data are inaccessible or no feasible unconditional test is
justified, record that specific blocker and park this dependent route;
do not repeat source-access attempts or enlarge witness boxes. A complete
package would still need verification and the remaining global-to-local
Selmer argument, and could at most address this branch.

ATTEMPTS/013's finite 54a1 polynomial search stays stopped; this is not
an enlargement of those boxes. ATTEMPTS/017's local stop stays confirmed.
No GRH, class-group correctness, unit saturation, rank, Sha vanishing,
Selmer/point equality or integer witness is assumed. Availability of
computational tooling has not been checked. Mathlib coverage is not
checked. This proposal establishes and approves no new mathematics.

## Completed review: precise primary inputs

The prior classification assessment is reused for the GRH boundary and
the remaining signatures. New reading is confined to the certificate
interface and its implementation. FNS is Freitas, Naskręcki and Stoll,
*The generalized Fermat equation with exponents 2, 3, n*, Compositio
Mathematica **156** (2020), 77-113,
[DOI](https://doi.org/10.1112/S0010437X19007693),
[final author manuscript](https://www.mathe2.uni-bayreuth.de/stoll/papers/genfermat-final.pdf),
dated June 10, 2019. Printed pages here follow that PDF; the older
assessment's pp.24-28 locators should be replaced by pp.25-29 for this
interface. This is a locator clarification, not a mathematical correction.

Table 5, printed p.27, gives exactly L050's polynomial m96 and the
conditional Selmer dimension five. Section 7.2, p.25, specifies
L96=K96(theta), of absolute degree 36, where theta is a two-torsion
x-coordinate on E0: y^2+y=x^3-x^2-10x-20. On p.28 its polynomial is
4X^3-4X^2-40X-79. No generator of K96 is identified with this coordinate.

The [author's primary code index](https://www.mathe2.uni-bayreuth.de/stoll/magma/index.html#GenFermat)
links [section7.magma](https://www.mathe2.uni-bayreuth.de/stoll/magma/GenFermat/section7.magma).
Zero-based source lines 315-416 are the first 96a1 test. They construct
K96 (called L in the code), take its maximal order, and either compute
TwoSelmerGroup or read five explicit representatives. The latter live
in K96[T]/(T^3-4T^2-160T-1264); lines 265-267 transport T to 4 theta.
These representatives are accessible primary data, not completeness
certificates. Their coefficients were located, not independently verified.

The default computeSelmer=false uses these stored elements. The true
branch sets SetClassGroupBounds("GRH") at lines 11-15. Consequently
neither default execution nor toggling computeSelmer removes GRH.
No source code was copied into scripts or run in this review.

## Required certificate package

This specifies the source's existing computation; it does not prove a
new descent theorem or assert that any required computation has succeeded.

1. **Arithmetic identity and maximal orders.** Supply exact field/algebra
   models and coordinate maps for K96, L96 and the cubic descent algebra,
   with degree/irreducibility checks, maximal-order bases and discriminants.
   Ideal and prime data must use the maximal order. A polynomial order
   may bound a later workload but cannot replace it in class computation.
2. **Class completeness.** For every absolute field used by the descent,
   give the class generators, principal relation witnesses and their
   matrices, an unconditional proof that the factor base generates, and
   proof that the relation lattice has no missing relations. Include all
   classes needed to construct the finite square-class ambient group,
   not just principal S-units. A partial factor base or a printed class
   number does not establish an upper bound containing all global classes.
3. **Unit completeness.** Retain roots of unity and unit representatives,
   independence and saturation evidence. Certify the required units
   modulo squares; a full unit-group proof is a sufficient implementation
   choice. If regulator/index bounds use numerical arithmetic, give
   rigorous enclosures/error control. The unit proof and the class proof
   are separate obligations.
4. **Descent upper image.** Record the actual finite support set used,
   the supporting unramified-outside-set justification, norm-square
   conditions, and every local condition imposed, including real places
   when relevant. Save the square-class basis, maps and linear algebra
   proving completeness of the resulting global upper image. For a
   full replay use the certified TwoSelmerGroup output and its injection
   into L96^*/L96^{*2}; merely checking that the five published elements
   belong to Selmer gives a lower subspace, which cannot exclude points.
   A larger upper subspace is usable only if it is rigorously shown to
   contain the global point image and passes the exclusion test.
5. **Entire local comparison at two.** Save all primes of K96 above two,
   all factors of L96 tensor Q2, square-class bases, coordinate transport,
   and the localization matrix for the certified global upper image.
   Compute every relevant point of the center fiber j=-512 in each
   completion, with exact root exhaustion and sufficient precision for
   square classes. Retain every combination of component classes and
   demonstrate its disjointness from the global upper image. FNS
   Lemma 7.6, printed pp.28-29, supplies constancy across the entire disk;
   its no-local-two-torsion hypothesis and analytic branch coverage must
   be verified in the actual factors. A selected embedding cannot suffice.

The handbook's
[SelmerGroup/TwoSelmerGroup entries](https://magma.maths.usyd.edu.au/magma/handbook/text/1570),
under "Selmer Groups", identify the norm-square cohomology representation,
the returned algebra map, integral-model requirement and the inheritance
of cached class/unit assumptions. Its
[LocalTwoSelmerMap entry](https://magma.maths.usyd.edu.au/magma/handbook/text/1568)
specifies the product over all local factors. These were read, including
the explicit cache warning. No Sha vanishing or Selmer/point equality
is needed for the necessary inclusion used in Lemma 7.7.

The [ClassGroup handbook](https://magma.maths.usyd.edu.au/magma/handbook/text/416),
V2.29, dated August 3, 2026, describes MinkowskiBound, FactorBasisVerify,
Relations and RelationMatrix. Crucially, Proof="Full" still inherits a
global GRH setting: a clean unconditional setting and cache provenance
must be recorded. The
[UnitGroup handbook](https://magma.maths.usyd.edu.au/magma/handbook/text/417)
separates its default saturation proof from class-group certification.

Andreas-Stephan Elsenhans and John Voight,
[*Computing class groups and unit groups in Magma*](https://jvoight.github.io/articles/clgpunitgp-magma-02Oct25.pdf),
October 2, 2025 manuscript, Sections 1 and 8, distinguishes the proof
regimes and reports certification bugs fixed in V2.29. Section 4,
equations (4.1)-(4.4), separates factor-base generation from relations;
Sections 6-7 explain unit and class saturation. This is an additional
version/proof obligation, not evidence that FNS's particular answers
are wrong. Old software logs or a matching dimension are insufficient
standalone evidence for a new unconditional certificate.

## Narrow downstream use and limits

FNS Lemma 7.7, printed p.29, excludes the 96a1 disk -512+2048 Z2;
its two surviving disks are 960+2048 Z2 and -64+2048 Z2. L032 retains
only the excluded disk. Thus a certified replay of this particular
global/local test would address that branch without requiring Lemmas
7.8-7.12's halving computations. This is the applicability comparison
to the cited conditional result, not an unconditional exclusion here.
The routine check_exclude, lines 255-313, enumerates all combinations
of component images at a center and tests membership. Its injectivity
check is useful replay evidence; the later global halving argument
needs injectivity, whereas this disk exclusion uses only containment
and disjointness. Precision 20 times ramification index in the code is
an implementation setting, not an independently checked error bound.

The accessible files contain models, conditional representatives and
local test code; the inspected package does not export a factor-base
generation proof, relation saturation proof or unconditional upper-image
certificate for L96. The local witness L050 supplies none of those.
No external access blocker persists. Read-only command -v checks found
no magma, gp or sage executable on PATH; other libraries and possible
backends were not checked. No purchase, API, installation or long
arithmetic run is proposed.

Exact searches included `Freitas Naskrecki Stoll genfermat code 96a1
Selmer class group`, `"96a1" "class" "GRH"`, `"96a1" "Selmer"
unconditional certification discriminant`, and official handbook
ClassGroup/Proof/UnitGroup/TwoSelmerGroup/LocalTwoSelmerMap queries.
They did not supply an inspected unconditional field certificate;
this does not imply novelty or nonexistence. The smaller Jacobian-factor
lead in FNS Remark 7.13 remains outside this target. ATTEMPTS/013's
54a1 boxes and ATTEMPTS/017's local stop remain closed and unchanged.

For a bounded feasibility continuation the standard unconditional
generation bound was inspected in J.S. Milne,
[*Algebraic Number Theory*, v3.08](https://www.jmilne.org/math/CourseNotes/ANT.pdf),
July 19, 2020, Theorem 4.3, printed p.70, and discriminant index
Remark 2.25 with its proof, p.34. No field-specific bound was calculated.
A separate workload target is recorded in
[the continuation assessment](2026-10-10-ninety-six-class-generation-workload.md)
for next-turn approval. A large order-discriminant bound would retire
only naive enumeration at that bound, not prove full certification
impossible. Mathematical exploration usage stays 2/3.

Mathlib: the full certificate/replay result and supporting class/unit,
Selmer and discriminant coverage are **not checked**. This turn imports
source specifications, establishes no lemma and changes no main argument.
