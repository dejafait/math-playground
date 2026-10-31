# Fixed-cutoff square defect: proposed bounded mathematical scope

TARGET: Test whether the fixed-length Riemann--Siegel square surrogate G_T defined in the assessment approximates D_1(Xi;t)/A(t)^2 with integrated absolute error o(T(log T)^3).
CHECKED: 2026-10-29
DECISION: EXPLORE
SEARCH_EVIDENCE: Reuse the completed alternate-source comparison in 2026-10-29-l317-square-surrogate-source-alternative.md and the earlier blocked square assessment; exact-square, analytic-Cauchy, absolute-mean and stronger-result searches found no inspected matching defect theorem. This is not a novelty claim.
SOURCE_EVIDENCE: Reuse L317 (1) and the previously inspected Hardy--Littlewood AFE: Titchmarsh--Heath-Brown (1986), Theorem 4.15/(4.12.4), printed pp. 79, 81--84, https://sites.math.rutgers.edu/~zeilberg/EM18/TitchmarshZeta.pdf ; L316, L471 (7), L465 Section 5. Rechecked Bui--Hall arXiv:2304.05178v1 (1), https://arxiv.org/html/2304.05178v1#S1.E1 and DLMF 5.11.1/5.11(ii), https://dlmf.nist.gov/5.11 . Optional finite Hilbert input: Montgomery--Vaughan (1974), Theorem 2/Corollaries 2--3, pp. 74--75, https://personal.science.psu.edu/rcv4/personal/Publications/s2-8-1-73.pdf ; retain the prior formula-extraction limitation and use no newly certified constant.
COMPARISON: Existing inputs supply local ordinary jets and exact completion curvature, but no theorem decides this phase-sensitive L1 residual or permits a silent dyadic cutoff replacement. Keep the entering finite sums and calculate their cost within the attempt; the new target is not a reproof of the local derivative estimate.
GAP: The absolute residual and the dyadic endpoint/phase-replacement estimates remain unproved; no essential further differentiated-Riemann--Siegel source is required to attempt those finite-sum obligations. An unsuccessful bound need not decide the target.
REASON: Separate literature approval on 2026-10-29 repairs the missing direct-source URLs while retaining the prior adequate comparison and unchanged target. Source scope supports one bounded attempt, not a defect estimate or independent audit of L317. No mathematical work is performed or approved retroactively.
SCOPE: Actual Xi, real T tending to infinity, t in [T,2T], exact L471 A, fixed M_T=floor(sqrt(T/(2pi))), j=0,1,2 local Hardy jets, retained entering terms and all arithmetic phases. No RH, simplicity, zero spacing, external half-plane premise, selected-law realization or unproved differentiated remainder.

## Unchanged candidate and required scale

Use natural logarithms and exactly

    W(t)=D_1(Xi;t)/A(t)^2,
    lambda(t)=(1/2)log(t/(2pi)),
    P_(1,T)(t)=sum_(1<=n<=M_T) (lambda(t)-log n)n^(-1/2-it),
    G_T(t)=4|P_(1,T)(t)|^2,
    E(T)=integral_T^(2T) |W(t)-G_T(t)| dt.

These are definitions, not an approximation or a verified coefficient
normalization. A little-o defect could yield a saving for L471's N(T);
individual-height signs, higher signs and RH would remain open.

## One coherent attempt after this source approval

Use L317's existing local jet conclusion through order two without
reproving its AFE/Cauchy mechanism. Its balanced length changes with t.
Retain the difference between that length and M_T in each jet. Split
finite integrals at cutoff transitions, or expand them with their
actual activation intervals; bound all boundary/diagonal/off-diagonal
costs before discarding any term. Fixed-coefficient mean-value bounds
do not automatically handle moving endpoints. Cite the known finite
Hilbert inequality if used; direct finite integration by parts is an
alternative and needs its complete summation bound. No new exact
constant is imported from the illegible Montgomery--Vaughan PDF formulas.

Retain L471's curvature and L316's phase derivative error. Check the
factor 4 by the actual quadratic expansion. After these transfer costs
are proved, test the phase-sensitive absolute residual against the
full T(log T)^3 scale. No generic moment-law inference, pointwise
diagonal-dominance bound or positivity assumption substitutes for this
comparison. Do not change G_T to a fitted or moving-length square.

Continue if a rigorous little-o bound or a quantitative smaller
residual estimate supports that threshold. Abandon this surrogate if
E(T)>=c T(log T)^3 is proved for fixed c>0 along an unbounded sequence.
If neither occurs in this bounded attempt, save the exact unresolved
term and route decision honestly; a large error envelope is not a
lower bound. A genuine endpoint obstruction also warrants parking the
implementation, without declaring the mean-sign target false.

## Coverage and failure qualifications

L317's stopped fourth-order ordering dominance, the earlier blocked
direct derivative-source route, L471's displacement loss, L472/L473's
abstract moment obstruction and L475's band-cost failure are preserved.
None is asserted to decide this exact first-order arithmetic L1 test.
Reuse the completed comparison rather than retrieve inaccessible papers
again. An essential new analytic input outside this scope requires a
separate literature turn; finite algebra and endpoint estimates within
this scope are the proposed mathematical work, not assumed inputs.
Full matching Mathlib coverage is unchecked. No cross-notebook input.

## Separate source-readiness repair, 29 October 2026

LITERATURE_REASON: The supervisor reported missing direct source URLs in
this ready assessment. This separate literature-only step supplies them;
it does not reopen the earlier source search or spend a calculation turn.

Reused the completed alternate-source assessment and the AFE statement in
foundations/notation-and-inputs.md. Read L317's conclusion and analytic
proof through the low-order specialization to identify the exact reused
input, without undertaking a fresh independent audit. The Rutgers book
link above identifies the original cited source; prior access failures
and earlier inspected coverage remain as recorded in the alternate-source
assessment. No new book retrieval or fresh proof-case inspection is claimed.

Reopened Bui--Hall v1 (11 April 2023), Introduction, definition of Z and
(1): fixed nonnegative integer orders k,l with k+l=2s and |k-l|=2d have
a signed mixed second moment with coefficient (-1)^d/[4^s(2s+1)],
a monic polynomial Q_(2s+1), and error O(T^(3/4)(log T)^(2s+1/2)).
This is source evidence for the previously assessed signed-moment input;
no dyadic subtraction or new specialization is derived here. It states
no L1 distance to the nominated finite square. Reopened DLMF 5.11.1 and
5.11(ii): the expansion uses |arg z|<=pi-delta, and the complex
remainder bound retains its secant factor. This supports the existing
analytic Stirling input, not termwise differentiation of a real error.

The optional Montgomery--Vaughan URL is bibliographic/source provenance,
not a claim of newly readable displayed formulas. The previously recorded
finite inequality may be reused with its qualifications; direct finite
integration by parts remains an alternative inside the approved scope.
No essential theorem is made dependent on a fresh successful extraction.
The earlier bounded searches, duplicate comparison and failure record
are reused unchanged; no novelty inference is made from them.

Decision remains EXPLORE for exactly the saved TARGET. This completes the
separate source approval of the earlier nomination; the next invocation
may attempt it using this assessment. The endpoint transfers, factor 4,
completion curvature cost and phase-sensitive absolute residual are still
unproved. Full matching Mathlib coverage remains unchecked. This is an
honest STALLED metadata/source-readiness repair, with no new mathematics,
no exhausted-route reset, and no change to the continuation test.
