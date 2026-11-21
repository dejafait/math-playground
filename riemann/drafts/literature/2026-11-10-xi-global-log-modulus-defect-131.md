# Proposed coverage: a global logarithmic-modulus discriminator

TARGET: Assess whether Littlewood's lemma for the actual quotient G_u/G_1 on an L958 rectangle yields an independently estimable signed defect controlling K, retaining common divisors and all boundary terms.
CHECKED: 2026-11-10
DECISION: EXPLORE
SEARCH_EVIDENCE: Step132 searched Littlewood meromorphic rectangle identities, the actual completed-derivative quotient and its logarithmic/mollified estimates; compared L957 Section4, L958 endpoint conventions, L959 and the step127/128 direct-import failures. Primary passages actually read and access qualifications are below; no adequate independent quotient estimate was found in this bounded search.
SOURCE_EVIDENCE: Littlewood1924 Section4 Theorem1 and full proof pp299–300, primary article text in an OCR mirror; Simonic1910.08274v2 Section4.2 pp29–30; Sekatskii–Beltraminelli–Merlini2015 Theorem1, complete slit-contour proof and following branch-jump qualification in Section2; Sekatskii2403.09657 Theorem1 pp2–3 corroborates the generalized meromorphic hypotheses.
COMPARISON: Original Littlewood permits meromorphic functions and half-weight horizontal-boundary orders, unlike the modern holomorphic boundary-free statement. It still requires a regular nonzero right edge and supplies an integrated net divisor count, not a K estimate. Generalized weights retain boundary exclusion and give no actual-quotient estimate; L957's positive-product moment is a different observable.
GAP: No independently bounded signed quotient modulus/argument datum controlling K was supplied. Critical-line and intermediate-parameter boundary terms, original common orders, stationary-endpoint corrections and the passage from weighted net orders to K remain unpaid; neither K=O(T) nor K=0 follows.
REASON: Park this direct logarithmic-modulus import after its boundary and observable comparison; do not derive an uncovered quotient identity or claim that every possible modulus method is impossible. Choose independently testable theta-specific work rather than repeat terminal splitting or the same bare count identity.
LITERATURE_REASON: The saved target changed from local terminal branches to a meromorphic global logarithmic observable. Its essential primary boundary conventions and available estimates were previously unread; ready Rouche and mollified-product coverage did not cover it.
SCOPE: Completed literature-only review of the exact TARGET; EXPLORE records a bounded search without an adequate quantitative match and does not authorize an unrestricted quotient calculation. No lemma, mathematical script, PROOF or DAG change.

## Original nomination and decision test (preserved)

Use the actual H and G_u from L959, L018's completion, and the fixed
positive L958 interval and its full multiplicity conventions. L957
enters through L958's endpoint existence, and its recorded Littlewood
application is the first specific overlap lead to inspect. No
cross-notebook input is proposed. Preserve all common orders and
allow the stationary endpoints admitted by L958. Do not assume
boundary exclusion for intermediate parameters, simplicity, RH,
uniform perturbation scales or a global finite nonreal-zero census.

The next turn is literature-only: search the exact quotient statement,
standard terminology, stronger results and obstructions; retrieve a
primary theorem's complete relevant hypotheses and boundary cases;
compare the recorded L957 application and completion-index failures.
Record what is actually read, separating unread leads. No new lemma,
mathematical script, quotient identity or inequality is approved here.

Continue only toward a separately specified bounded mathematical
test if the reviewed sources identify an actual modulus estimate or
signed defect with a plausible route to a nontrivial K bound, without
assuming the missing critical signs. Abandon this proposed mechanism
if the available comparison merely re-expresses K, needs its sign as
input, or encounters the same persistent unhandled boundary cases.
An unanswered source search is not an obstruction theorem.

This is a prospective source-gate record, written after the focused
L959 audit. It is not an assessment claiming adequate coverage. A
creative proof target cannot yet be justified: the independently
estimable signed quantity is still missing. Full matching Mathlib
coverage is unknown. Sources, an effective estimate and higher/global
transfer remain unresolved.

## Completed source review — step132

Main gap: L030–L032/C032a actual-Xi all-degree mixed positivity.
The proposed intermediate observable was a global logarithmic defect
for the actual G_u/G_1 on one fixed L958 interval. A quantitative
signed bound could discriminate nonreal-pair loss before attempting
higher-derivative/global transfer. Continue only if a source supplies
an independently estimable term; stop the proposed direct import if
only a count identity or unhandled boundary assumptions are available.
No quotient identity or new mathematical implication is derived here.

### Original meromorphic theorem, including its boundary convention

J. E. Littlewood, *On the zeros of the Riemann zeta-function*,
Proc. Cambridge Philos. Soc. **22** (1924), 295–318,
[DOI10.1017/S0305004100014225](https://doi.org/10.1017/S0305004100014225),
Section4, Theorem1 and its full proof, pp299–300; read the
[primary-article OCR mirror](https://studylib.net/doc/7952840/on-the-zeros-of-the-riemann-zeta-function).
The publisher PDF request redirected to its abstract; the mirror,
not a successfully inspected publisher scan, is the textual evidence.

For a meromorphic phi on and inside a rectangle [alpha,beta]+i[0,T],
the right side must be regular and nonzero. Start its logarithm there
and continue horizontally, averaging the upper/lower limiting values
when the path crosses a zero or pole. Theorem1 states

    integral_boundary F(s) ds = -2 pi i integral_alpha^beta nu(sigma,T) dsigma.

Here nu is the excess of zeros over poles strictly to the right of
sigma; orders on the horizontal boundaries count one half. The proof
first avoids horizontal-boundary divisors, interchanges integrations,
applies residues and cancels the logarithmic endpoint terms; it then
invokes the halving convention. This is broader boundary coverage
than the modern statement, but it retains a nonsingular right edge.
It does not supply a closed-count convention identical to L958's.
No unrecorded primary proof of arbitrary corner or parameter contacts
is being inferred from the short final boundary observation.

### Modern statement and weighted extension

Aleksander Simonic, *Explicit zero density estimate for the Riemann
zeta-function near the critical line*,
[arXiv:1910.08274v2](https://arxiv.org/pdf/1910.08274v2),
29 November2019, Section4.2 pp29–30: holomorphic on a neighborhood
of the rectangle, no boundary zero, with 1/2<=sigma<1<a. The
integrated zero count equals the difference of the two vertical
log-modulus integrals plus the top-minus-bottom horizontal argument
integrals. The subsequent application uses Phi_X=zeta S_X and
its own right-edge normalization. Those arguments and normalizations
are not estimates for G_u/G_1. This verifies the exact scope of
L957's named-tool citation; L957's different moment is not reproved.

S. K. Sekatskii, S. Beltraminelli and D. Merlini, *On Equalities
Involving Integrals of the Logarithm of the Riemann zeta-Function with
Exponential Weight Which Are Equivalent to the Riemann Hypothesis*,
International Journal of Analysis **2015**, article980728,
[DOI10.1155/2015/980728](https://doi.org/10.1155/2015/980728),
Section2 Theorem1 and entire slit-contour proof. Its f is meromorphic
inside, analytic and nonzero on the contour; g is meromorphic inside
and analytic on it, with the divisors of f and g disjoint and the displayed
integrals existing. The conclusion retains residues of g and the
separate full-order zero/pole integrals. The proof treats an interior
simple factor, shrinks its logarithmic slit circle, then adds orders.
The following paragraph warns that the horizontal-branch logarithm
jumps on the left edge; its modulus is continuous there only away
from edge divisors. This supplies neither general boundary-contact
coverage nor a bound for our quotient. No RH-equivalent equality
in that paper is imported as an estimate.

S. K. Sekatskii,
[arXiv:2403.09657](https://arxiv.org/pdf/2403.09657),
*Inverse applications of the generalized Littlewood theorem concerning
integrals of the logarithm of analytic functions*, Theorem1 pp2–3,
was also read: it preserves the boundary exclusion, multiplicities,
disjointness and existence assumptions. Its proof is referred back,
so the complete proof was read in the 2015 paper instead. The 2023
Axioms article returned429; it is an unnecessary unread lead, not
a persistent essential source blocker. No new constants are imported.

### Exact applicability and estimate comparison

Use L018's actual completion and L959's H,h,G_u definitions, with
the fixed positive interval and full-order conventions of L958.
The left-half s-rectangle has critical line as its right edge.
L958 does not assert a regular nonzero G_u/G_1 there. It expressly
allows stationary endpoints; L959 discusses critical-line denominator
zeros and persistent common orders. No source removes these cases.
Moving an edge or rotating the rectangle would introduce new terms
and applicability work; it is not an established repair here.

A quotient theorem records net divisor orders after cancellation.
Original common multiplicities must therefore still be kept separately
as L959 does; cancellation is not evidence that they were absent.
Littlewood's horizontal half convention cannot silently replace
L958's closed endpoint correction E. Nor does integrability of a
logarithmic singularity provide its signed boundary argument or a
uniform parameter limit. No all-u boundary exclusion, fixed common
perturbation scale, simplicity, RH or finite global census is assumed.

Even on a permissible contour, the source conclusion is an integrated
horizontal-displacement statistic. L958's K is an unweighted critical
multiplicity sum, equivalently J-J'. A conversion with useful sign
or constants and an estimate for every modulus/argument term would
still be needed. This is a scope comparison, not a newly proved
identity, impossibility theorem or assertion that the proposed defect
has been shown to equal K. No upper bound or nontrivial saving for K
was obtained.

L957 Sections1/4 concern a positive mollified zeta product, not a
reciprocal completed derivative. The stored step127 assessment already
compared Levinson1974 and Wu1206.3737v2: their auxiliary completed
combinations give fixed-proportion line-zero lower bounds, not the
signed loss needed here. Reuse that ready comparison; do not rebrowse
it or subtract unrelated lower bounds. The step128 argument-principle
boundary stops remain valid in their stated scope, while the original
Littlewood horizontal-half case is a genuine additional qualification
and prevents an overbroad claim that all inspected versions exclude
all boundary roots.

### Search evidence, decision and continuation

Queries included `"Littlewood" "lemma" "meromorphic" zeros poles boundary`,
`"zeta" "zeta'" "quotient" "Littlewood"`, `"xi-function" derivative
"mollifier" logarithm`, `Littlewood "On the zeros of the Riemann
zeta-function" 1924 pdf`, `"generalized Littlewood" "contour" "zeros"
boundary theorem`, `"zeta" "zeta'" "H'/H" Littlewood`, and `"xi"
"derivative" "ratio" "Littlewood lemma"`. Exact-symbol searches were
mostly noisy; no novelty or exhaustive absence follows. Only the
primary passages named above and the specified local records are
source evidence. No search snippet supplies an estimate.

Outcome NEGATIVE is the failed direct-import test with a newly
inspected meromorphic/horizontal-boundary comparison, not a discovery
beyond these sources. Park the bare quotient route. Reopening needs
an actual independent signed estimate and a separate source assessment,
not another formal contour or local branch count. Main mixed signs,
higher/global transfer and critical-count bounds remain open.
Mathlib full matching coverage was not checked and remains unknown.

For the next direction, the narrowly checked L617 audit records already
contain both an independent audit and a repeated audit; its stale
PROOF overview label is not a reason to run it again. Its source
coverage is ready for the old audit, not for a new coercivity mechanism.
Nominate bounded source discovery of at most three theta-specific
collision-coercivity candidates, with explicit comparison to the
semiconcavity/event-atom stops. This different mechanism requires its
own review; no mathematics or creative approval is implied. No
justified creative target is yet available: the independent signed
theta estimate and a discriminating intermediate threshold are missing.
No cross-notebook input or supervisor-state change was used.
