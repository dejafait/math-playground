# Adjacent-lobe cancellation for the actual determinant — completed source screen

TARGET: Assess adjacent-cosine-lobe pairing for the exact L814 determinant on 0<x<=40 under Xi R<0 and Xi R'-R Xi'=0, retaining the initial half-lobe and complete tail, and identify whether one independently checkable signed comparison test is justified.
CHECKED: 2026-11-05
DECISION: EXPLORE
SEARCH_EVIDENCE: Step576 searched Fourier positivity, adjacent-lobe/half-period pairing, mixed Wronskians and variation-diminishing terminology; inspected Tuck2006, Cho–Park2110.01885v1 and Dimitrov–Xu1606.05011v1 theorem/proof ranges; compared L814, L738 and named local Polya assessments/stops. No adequate actual mixed-determinant comparison found; no novelty inference.
SOURCE_EVIDENCE: Tuck2006 Bull.Aust.Math.Soc.74,133–138, (3)–(4) pp134–135 https://doi.org/10.1017/S0004972700047511 ; Cho–Park arXiv:2110.01885v1 Theorem2.1/proof/Remark2.1 pp3–5, Lemma4.1/Corollary4.1 pp10–11 https://arxiv.org/pdf/2110.01885v1 ; Dimitrov–Xu arXiv:1606.05011v1 Theorems2.5–2.7/proof pp5–6 and warning p8 https://arxiv.org/pdf/1606.05011v1 . Exact Q and fold coverage reused from step574.
COMPARISON: Known single-amplitude sine pairing needs monotonicity; cosine positivity needs convexity; finite-support reflected-transform criteria assume another positive transform. One-measure Fourier Wronskian positive definiteness is not pointwise positivity or L814's mixed W' sign. None pays its relative remainder, initial half-lobe and full tail.
GAP: No independently controlled signed amplitude, boundary contribution or relative curvature margin has been supplied for the exact mixed determinant under F G<0 and W=0. This is an applicability gap, not an inaccessible-source claim or proof that pairing is impossible.
REASON: Complete the changed-mechanism review and park its unsupported automatic import. The bounded search supplies no concrete signed comparison test to approve. Secure the saved diagnostic by an independent L814 audit instead of repeating unsigned bounds or the parked Polya1927 access loop.
SCOPE: Completed literature-only step576. EXPLORE records a bounded search without an adequate match, not approval of another pairing calculation. No lemma/script edits, new identity, actual sign/event or quantitative margin. Any new signed mechanism needs separate review.

## Original nomination (preserved; superseded below)

Main gap: actual-Xi all-degree mixed positivity. The proposed intermediate
input remains a local signed determinant bound; a valid one could support
zero-deformation control, with degenerate events, infinity and global
mixed transfer still independent. L814 is a saved unaudited diagnostic,
not an audited sign input. Essential local inputs for any subsequent
attempt are L019, L020, L021 and L814. No cross-notebook theorem is proposed.

The new idea to assess is cancellation between successive intervals on
which cos(xu) has alternating sign, applied to the complete two-kernel
determinant rather than to absolute norms of each factor. The shortened
first interval at u=0 and the infinite tail must be retained. The two
event equations must remain available; an inequality simply assumed at
the event is not a paid mechanism. This paragraph nominates a technique,
not a new mathematical identity or sign assertion.

Before approving work, search the exact statement and standard Fourier
oscillation/variation-diminishing terminology, read relevant primary
hypotheses and proof cases, and compare the actual-kernel sign stops.
In particular inspect the scope of L738's recorded generic positive-kernel
obstruction rather than assuming smoothness or log concavity supplies
signed cancellation. Reuse the previous corrected-reference and finite-
fold literature; the uninspected all-real theorem for S is not needed.

Continue only if source comparison yields a concrete finite or tail
inequality whose hypotheses can be tested from the exact kernels without
assuming W' has the desired sign. Otherwise park the pairing proposal and
record which requirement fails; do not rename the absolute-bound attempt.
Any eventual mathematical test requires a ready assessment saved in a
separate turn. No independently supported signed pairing mechanism yet
justifies creative routing, and no new mathematics is approved here.
Full matching Mathlib coverage is unchecked.

## Completed comparison — step576, 5 November 2026

LITERATURE_REASON: Adjacent-lobe cancellation is outside step574's ready
affine-elimination scope; its essential theorem hypotheses and proof cases
had not been read. This completes the saved REVIEW_REQUIRED target.

The main gap is actual-Xi all-degree mixed positivity. The reviewed
intermediate target is an independently paid sign of L814's
W'=F G''-G F'' at F G<0, W=F G'-G F'=0, 0<x<=40. A paid sign could
inform local deformation control; common/degenerate events, endpoints,
infinity and global mixed transfer remain independent. Continue only
with an actual signed comparison retaining the origin interval and full
tail, not a condition assumed equivalent to W'<=0. No such supported
test emerged, so park this proposal.

### Primary hypotheses and relevant proof cases actually read

E.O. Tuck, *On positivity of Fourier transforms*, Bull. Austral. Math.
Soc. **74** (2006), 133–138, DOI above;
[publisher PDF](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/D232B9DEB4819E4D2FF17E8162B8B066/S0004972700047511a.pdf/on_positivity_of_fourier_transforms.pdf).
Read pp133–135, especially (3)–(4). Infinite sine pairing uses a
decreasing amplitude and convergence; cosine positivity uses the
negative derivative of a convex function. Integration by parts requires
decay at infinity and the stated origin limit. Each negative full sine
lobe is controlled by its preceding positive lobe. No convex residual or
decreasing compensated sine amplitude for L814 has been established.
The contour discussion on pp135–136 adds analytic continuation,
shifted-line decay and real/imaginary-part shape hypotheses, unverified
here. The parsed display (4) is incomplete, so no formula is transcribed
from it; Cho–Park's intact finite proof supplies the case comparison.

Yong-Kum Cho and Young Woong Park, *The zeros of certain Fourier
transforms: Improvements of Pólya's results*, arXiv:2110.01885v1
(5 October 2021). Read definitions pp1–3 and Theorem2.1, its complete
proof and Remark2.1 pp3–5. A positive decreasing f on (0,1), in their
general case, is asserted to have positive sine transform. The printed
statement removes ordinary integrability/continuity assumptions; this
review uses only convergent integrals and imports no singular-endpoint
extension or convergence assertion. Their exceptional case is
constancy on cells of a finite rational partition; the remark gives only
nonnegativity there. The proof retains the unfinished terminal interval
in all three cases: m=1, odd m>=3 and even m. Corollary2.1 needs a
positive decreasing derivative amplitude and its endpoint condition for
cosine positivity: its first part assumes f(t)=integral_t^1 g(s)ds with
g positive, continuous, decreasing and in the general case. Lemma4.1
and Corollary4.1, pp10–11, require positive
integrable finite support and positivity of a separate reflected
transform. Neither premise is certified for L814's mixed determinant.
A finite truncation also leaves its original infinite tail unpaid.

Dimitar K. Dimitrov and Yuan Xu, *Wronskians of Fourier and Laplace
Transforms*, arXiv:1606.05011v1 (16 June 2016). Read Theorems2.5–2.7
and the determinant/Fubini proof pp5–6, plus the explicit p8 warning
that positive definiteness does not imply positivity everywhere.
Theorem2.5 requires f and t^(2n-2)f integrable and concerns successive
derivatives of ONE transform. The positive-measure Fourier conclusion
of Theorem2.6 is positive definiteness. Theorem2.7's completely monotone
conclusion concerns Laplace transforms on the positive half-line.
Neither is the required pointwise sign for two different cosine
transforms. No mixed specialization, strictness claim or constant is
imported. Kernel/correlation positivity does not supply the missing sign
through these conclusions alone.

These are source-scope comparisons, not newly derived identities or
counterexamples. Full matching Mathlib coverage remains unchecked.

### Local overlap, search limits and decision

Read all of L814 and L019–L021, and L738's hypotheses/conclusion and
audit qualification. Reused the source assessments
`2026-11-05-polya-local-collision-mechanism-test.md` and
`2026-11-05-polya-corrected-reference-collision-scope.md`, and the failure
`ATTEMPTS/2026-11-05-polya-affine-collision-sign-unpaid.md`.
L738 rules out a generic admissibility/log-concavity substitute, not a
special arithmetic cancellation law. L814 remains unaudited; reading
it for scope does not verify it. Its saved normalization/ratio diagnostics
do not verify the source pairing hypotheses or a curvature lower bound.

Queries included `Fourier cosine transform positivity decreasing convex
function Polya theorem lobe pairing`, `Fourier cosine transforms Wronskian
monotone ratio kernels sign variation diminishing`, `The zeros of certain
Fourier transforms improvements Polya results arxiv`, `Xi Polya Wronskian
pairing`, `Fourier cosine adjacent lobes positivity`, and `Fourier Wronskian
two kernels sign`. Local searches were confined to the named Polya,
modulated-kernel and 5 November assessments/stops. No matching earlier
assessment was found there; absence of a search match proves no novelty.
Secondary surveys, snippets and general total-positivity/sign-regular
leads were not theorem evidence. No total-positivity theorem for this
operator was inspected or applied. Primary PDF text supplied the relevant
complete proof cases above; screenshots returned no images and shell
retrieval failed DNS. Those failures do not block the extracted source
statements used here. The parked Polya1927 access loop was not retried.
No sibling notebook or cross-notebook input was read.

Outcome NEGATIVE is a documented source-overlap/applicability decision
that changes the route, not a mathematical impossibility or beyond-source
advance. Reopening needs a specific independently verifiable signed
amplitude or block inequality retaining the short origin cell and full
tail. Another absolute envelope or restated event equation does not qualify.
The independent continuation is a critical audit of L814's saved
diagnostic, scoped separately in `2026-11-05-l814-diagnostic-critical-audit.md`.
No audit is performed here. Creative routing is blocked by the absence
of a supported new signed mechanism, not a historical global ban.
