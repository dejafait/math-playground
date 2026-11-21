# Proposed analytic-enclosure test of the unresolved full Hall cut

TARGET: Determine the sign of L905's full four-demand cut at x=16,y=0 using degree-two Taylor models on its existing M=128 partition, with a certified analytic remainder and complete theta/spatial errors, without mesh refinement.
CHECKED: 2026-11-09
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step165 reused the ready four-demand Hall assessment and step139 audit; inspected L905's cut/errors, L312's older seam-split Taylor method, L036/L037, L898 domination, L908 normalization, L910's holomorphic series and L911's derivative bounds. Primary-source searches for validated multivariate Taylor integration, Makino-Berz functional inclusion, Johansson quadrature and theta/Hall Taylor cuts found known enclosure methods, not an inspected theorem signing this cut; queries and limits are below.
SOURCE_EVIDENCE: Makino-Berz, Taylor Models and Other Validated Functional Inclusion Methods, publisher Volume4 PDF: Definitions1-3 pp383-385, exponential (2.2)-(2.4) p385, integration (2.7) p389, Theorem1 statement pp389-390, Theorem2 statement/induction proof pp390-391, Section6 pp415-416; Johansson1802.07942v1 Section2/2.1 pp2-4 and Section3.2 p6; NIST DLMF1.9(iii), (1.9.30)-(1.9.31), with contour hypotheses. Reuse the previously assessed weighted-Hall input without repeating its discovery.
COMPARISON: Validated Taylor models, interval derivative evaluation and analytic quadrature are known. L312 already uses one-variable Taylor panels with explicit seam splitting; L905 already integrates cosine weights exactly. The remaining specialization is a total-degree-two amplitude model on L905's unchanged two-variable grid, using the full kernel's established even analytic extension at the seam and certified full-series coefficient/remainder errors. No general new method or novelty is claimed.
GAP: No cut sign, effective degree-two remainder budget, second-derivative theta-tail bound, weighted polynomial moment certificate or new script has been produced. These are covered application obligations for the research step, not missing essential source coverage; L911's symbolic derivative constants alone do not certify numerical accuracy.
REASON: The missing method coverage is now supplied by precise primary inputs, with a local Taylor precedent and a valid full-kernel seam interface. One fixed test can reject nearest-neighbor allocation or pass this finite cut; independent infinite-residual and all-degree mixed-sign gaps remain.
LITERATURE_REASON: Step165 completed the changed analytic-enclosure method's essential source comparison, which the prior whole-box-only assessment did not cover. This reason does not authorize repeated literature on the now-ready target.
SCOPE: Exactly the saved TARGET, with unchanged four demands, five resources, x=16,y=0, M=128 grid, T=pi/2 and degree two. Full-kernel Taylor models may use L908/L910/L911 and certified coefficient tails; a reflected finite head is not assumed smooth. One complete enclosure only; no mesh/degree escalation, other block, frequency sweep, metric reopening or global feasibility claim. Prepared here for separate supervisor approval; no research invocation in step165.
COVERED_TARGET: Determine the sign of L905's full four-demand cut at x=16,y=0 using degree-two Taylor models on its existing M=128 partition, with a certified analytic remainder and complete theta/spatial errors, without mesh refinement.

## Relevance and existing stop

The main gap is L030-L032/C032a actual-Xi all-degree mixed positivity.
L905 tests one necessary condition of a proposed positive/negative-lobe
allocation in the full actual-theta marginal of L898. Its fourteen
proper cuts already pass under the stated arithmetic contracts. Its
only remaining cut contains zero. Determining that sign could reject
the nearest-neighbor allocation rule or remove this one finite
obstruction; it would establish neither infinite allocation nor any
unresolved mixed sign.

Preserve the stop in
[the budget record](../../ATTEMPTS/2026-11-08-variable-hall-four-demand-budget-inconclusive.md).
Both M=64 and M=128 certificates and the step139 audit remain unchanged.
The old campaign exhausted its declared range-box budget. Its full-cut
interval has unnormalized width greater than 0.000404, whereas its
complete theta and transverse spatial errors are far smaller. This
is recorded evidence for considering a different enclosure method,
not evidence for either sign of the cut.

The proposed change retains amplitude variation in a Taylor polynomial
instead of replacing the whole amplitude on a box by one interval.
Polynomial terms would be integrated against the existing t^2 and
cos(16q) weights, with a separate certified remainder. Whether that
gives a sufficiently small bound is unproved. Exact cosine integration
alone cannot be claimed as an improvement: L905 already uses it.

## Primary inputs inspected in step165

Makino and Berz, *Taylor Models and Other Validated Functional Inclusion
Methods*, 2003, [publisher PDF](https://www.ijpam.eu/contents/2003-4-4/2/2.pdf).
This exact 74-page file says Volume4, 379-452; catalogue citations often
give 379-456. Inspected ranges are itemized in SOURCE_EVIDENCE.
Definition1 requires C^(n+1) regularity near the domain and a pointwise
remainder enclosure. Multiplication retains discarded terms; the
exponential cases bound the complete Lagrange term with theta in [0,1].
Theorem2 requires a finite expression defined on the represented range;
its proof inducts over valid operations. Section6 permits interval-AD
remainder bounds but requires separate coefficient-roundoff inclusion
and warns of dependency overestimation. Scaling does not certify this
cut's accuracy; (2.7) does not directly treat the cosine weight.

Johansson, *Numerical integration in arbitrary-precision ball arithmetic*,
[arXiv:1802.07942v1](https://arxiv.org/pdf/1802.07942v1), Section2,
pp2-3, requires analyticity and a bound on an enclosing complex ellipse
for its Gaussian error estimate. Its analytic callback must reject invalid
domains. Section2.1, pp3-4, distinguishes requested tolerances from the
actual output radius. Section3.2, p6, requires separate bounds for truncated
improper tails. These inspected cases offer a stronger adaptive integration
alternative, but do not guarantee fixed-degree, fixed-grid accuracy and
do not repair an absolute-value seam automatically. Adaptive Petras/Arb
quadrature would change this test's method and budget; it is not the
proposed calculation or a newly assumed installed dependency.

NIST DLMF [1.9(iii), (1.9.30)-(1.9.31)](https://dlmf.nist.gov/1.9#E31):
read the continuity-on-and-inside-contour and interior-analyticity
hypotheses, and the derivative formula for every integer order n>=1.
This supplies the named Cauchy derivative input for an explicit analytic
remainder. No local derivative constant is calculated in this review.

Searches included `validated integration Taylor models multivariate
integration Taylor remainder Berz Makino rigorous quadrature`,
`Johansson numerical integration arbitrary precision ball arithmetic
Taylor series 2018 1802.07942`, the exact Makino-Berz title, the
Berz-Hoffstaetter interval-remainder title, `theta kernel Hall Taylor
integration`, and `validated oscillatory integrals Taylor models`.
Accessed the publisher PDFs rather than relying on search excerpts.
An attempted author-hosted Makino-Berz PDF failed to fetch; the publisher
copy above resolves access. The 1998 author-hosted Berz-Hoffstaetter PDF
had unreadable extracted text and is not a load-bearing citation.
Julia TaylorModels documentation and other search leads were not used
as theorem evidence. Theta-concavity/paired-tail papers surfaced in the
last search but were not inspected; no scope or sign conclusion is drawn
from their snippets. A failed exact search establishes no originality.

## Local comparison and applicability

The step164 nomination's phrase “no recorded Taylor-model test” referred
to this Hall cut, not the notebook's methods generally. A narrow read of
the already essential L312 reveals its order-eight one-variable Taylor
panels, normalized derivative recurrences and explicit seam split. L036
proves that panel formula, and L037 fixes the arithmetic contracts.
Neither is a ready degree-two, two-variable certificate for L905.
This is a known-method specialization, not a new quadrature invention.
The ready assessment `2026-11-08-variable-lobe-four-demand-cut-test.md`
and step139 history supply Hall/locality coverage; no new flow theorem
or reproof is needed.

The full-kernel interface is available with exact normalization. L908's
proof identifies W(x)=K(x)/4 for x>=0 and even W. L910, proof (2)-(5),
establishes its even holomorphic continuation on |Im z|<pi/4 and its
closed-strip envelope on |Im z|<=1/4. L911, proof (4)-(5), already gives
W derivatives through order four on |Im z|<=1/8, using circles of radius
1/16. These parts hold independently of any complex-zero premise or
metric-symmetry claim. The full kernel is therefore the available smooth
object at t=q/2. No claim that K_4(|s|) is C^3 across s=0 is allowed.

The approved specialization is to retain a total-degree-two amplitude
polynomial on each existing rectangle and bound its remainder for the
full even kernel. L910/L911 supply analytic regularity and derivative
envelopes; their symbolic suprema must still receive certified effective
bounds if used. Finite-series coefficient evaluation must include all
omitted derivative tails through the orders actually used. L312's
value/first-derivative errors do not certify a second derivative. If
reflection is used at coefficient centers, use the full kernel's exact
derivative parity and justify the head-plus-tail enclosures, including
centers at zero. Do not differentiate an unqualified absolute value or
drop a finite-head derivative jump. Deriving these application bounds
is research covered by the named Taylor/Cauchy methods, not work done here.

Integrating the polynomial requires signed, outward-enclosed moments
against the unchanged t^2 and cos(16q) weights. L905 already supplies
fixed-sign cosine cells; linearity and elementary polynomial integration
give the applicability task, not a new general quadrature theorem.
Coefficient errors, discarded terms, analytic remainder, endpoint/pi
errors and all theta indices must be included. An old value-tail bound
cannot substitute for coefficient-tail errors. The original complete
spatial tail may be reused because the integration domain is unchanged;
avoid silently changing T or counting a finite-head approximation error
as full-kernel derivative control. No implementation, derivative bound
or weighted-moment formula is derived in this literature-only step.

## Single bounded application and decision test

Keep exactly L905's M=128 partition: h=pi/(64M), 32M t cells,
9M q cells, t in [0,pi/2] and q in [0,9pi/32]. No refinement or
degree escalation follows this review. The full-cut identity and its
positive normalizer are already in L905; the calculation must enclose
the complete cut, not a midpoint or selected lobe. L898 supplies absolute
domination. The arithmetic contract remains L037's trusted Decimal/exp
implementation, not a newly claimed formal verification.

The research step must declare and complete one remainder/error budget,
write the full certificate to disk, and inspect every load-bearing value.
A strictly negative upper endpoint rejects universal nearest-neighbor
allocation. A nonnegative lower endpoint passes only this finite cut.
A zero-containing enclosure ends this fixed test, preserving the old
mesh stop and the new inconclusive evidence. No claimed success follows
from an expected cubic error order or from the old fourteen proper cuts.

Essential continuation inputs are L036/L037 (arithmetic and jets),
L312 (finite heads and existing tails), L898 (marginal/domination),
L905 (exact full cut, grid, locality, spatial tails and A_0>0),
L908's normalization proof, L910's analytic-even envelope and L911's
derivative estimates. All are local; no cross-notebook input is used.
The new coefficient/remainder constants, implementation and final sign
remain unresolved. Other cuts/lobes, infinite allocation/residual,
nonzero heights and all-degree mixed positivity remain independent gaps.

Step165 closes essential method-source coverage only. SPECIALIZE is
prepared for a separate supervisor approval before mathematical invocation;
the exact target is unchanged. No lemma, mathematical script or numerical
certificate was written. PROOF/DAG need no change because the argument
has not changed. The next mathematical work is ordinary calculation and
reproduction/specialization. A justified new central creative mechanism
is still unavailable; this test is not relabeled creative to meet routing
preferences. Full matching Mathlib coverage is unchecked, not absent.
