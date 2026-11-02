# Hardy periodic closure: completed source comparison

TARGET: Assess source coverage for C2 periodic closure of fixed-divisor Hardy segments with paired second/fourth moment errors inside L473's tolerances.
CHECKED: 2026-10-31
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Completed bounded searches for quintic endpoint interpolation, uniform-phase periodic stationarity and Hardy/Z-function periodic approximation; compared the exact-law and direct-import stops and narrowly searched active literature/failure records. No matching complete Hardy paired-moment closure theorem was located; no novelty inference.
SOURCE_EVIDENCE: Inspected Finn, MA 323 Day 09 (2004), Section 9.2 pp.9-3--9-4 and 9-7; Phung, ZAA 37 (2018), Theorems 2.1--2.2 pp.253--254; Bui--Hall arXiv:2304.05178v1 Introduction before (1); Colonius--Kliemann (1990), Section 7 p.39, Stat paragraph. Reuse L473 (1)--(2),(6),(9)--(10) and prior arithmetic assessments; exact URLs and qualifications below.
COMPARISON: Prescribed second-order endpoint interpolation, fixed-order Hardy pointwise bounds and uniform-phase periodic occupation cover the inputs for one elementary closure specialization. They do not state its complete lag-one moment error bounds. L581 excludes the exact corrected law, not this changed marginal; Bernard's qualitative compact generalized-curve approximation is unnecessary here.
GAP: The unit-length bridge, all phase regions and normalization errors, tight odd entries and one eventual ray must still be calculated. No quantitative Hardy closure, hard ell^2 support, clipped-mass lower bound, rare/bulk replacement or Xi transfer is established.
REASON: Source coverage is sufficient to nominate one bounded calculation using standard inputs; its exact error comparison remains research. Newly ready continuation requires separate approval before invocation, and this review performs no mathematical specialization.
LITERATURE_REASON: The saved REVIEW_REQUIRED target changes the marginal and needs second-order gluing, endpoint-neighborhood and periodic-occupation coverage beyond the ready exact-law audit; that older coverage is reused where unchanged.
SCOPE: Fixed H, ell=log H and f_H(s)=Z(H+s/ell) on [0,H ell]; investigate a deterministic C2 periodic extension/closure with uniform random phase and ordinary lag-one jets. Compare all 21 second and 126 fourth moments to L473 (1)--(2), including the four tight same-height odd entries and constants on one eventual ray. No prescribed ell^2 support, clipped-mass lower bound, covariance correction, rare weighting or Xi transfer is claimed or approved here.
COVERED_TARGET: Test the appended unit-length quintic Hermite closure of f_H against all L473 second/fourth tolerances, including wrap-around phases.

## Original nomination, retained as the pre-review record

The following pending-source statements describe the previous nomination.
The completed review below supersedes their missing-coverage status only
for the single COVERED_TARGET; it supplies no closure proof.

The completed turn audited L581 only. This file is a nomination, not a
source approval or a mathematical attempt on periodic closure. No
gluing formula, error estimate, feasibility result or stationary moment
matching has been derived. The next turn is literature-only.

The main gap remains actual-Xi positivity and unbounded-height initial
signs. A derivative-consistent path component preserving the assessed
actual moment data could be useful in testing whether stationary
constraints strengthen the finite-moment obstruction. That use remains
conditional: closure alone gives no positive clipped mass and no
derivative-preserving rare/bulk decomposition. Hard support, spectral
covariance correction and actual-Hardy/Xi comparison remain independent.

Essential local inputs are L473 (1)--(2) for the exact target data and
the endpoint/interface hypotheses of L581. Reuse the source assessments
`2026-10-31-stationary-hardy-path-feasibility.md` and
`2026-10-31-l581-critical-audit-scope.md` only within their recorded
scope. The earlier fixed-order pointwise bound must be checked for any
newly needed derivative orders; do not infer a uniform-in-order bound.
Any required endpoint neighborhood and shifted wrap-around cases need
coverage, not just endpoint values. There is no cross-notebook input.

This differs from importing a realization theorem for L473's exact
nu_H and from tuning exhausted wave/packet families. The proposed
marginal would change. The old source stop's hard paired support is
expressly unresolved rather than silently satisfied or refuted. A
successful closure result would therefore be only an intermediate,
not the original bounded full-feasibility target.

The source review should retrieve quantitative smooth/Hermite endpoint
gluing and random-phase periodic occupation results, or document the
specific specialization needed, before any derivation. Read primary
hypotheses and essential proof cases. Bernard's compact-manifold result
is a recorded comparison, not permission to import an unproved jet
approximation; any new lead remains unread until actually inspected.
Search for duplicate Hardy stationarization/periodization results and
known obstructions as well as generic interpolation bounds. Matching
Mathlib coverage has not been checked.

Continue only if coverage supports a concrete bound for the complete
paired second/fourth errors within the exact target tolerances,
including the boundary-crossing lag-one samples. Otherwise identify
the failed tolerance or essential missing source and park this scope.
Do not assert stationarity of the original dyadic samples or assume
the periodization preserves any of their moments exactly. The new
assessment, if made ready, requires separate approval before research.

## Completed primary-source comparison, 31 October 2026

This is one literature-only step. SPECIALIZE licenses the later error
test using the following inputs; it does not assert that test succeeds.
No original closure estimate, lemma or mathematical script was written.

### Inputs, hypotheses and source cases

David L. Finn, *MA 323 Geometric Modelling, Course Notes: Day 09,
Quintic Hermite Interpolation*, 13 December 2004,
[author PDF](https://www.rose-hulman.edu/~finn/CCLI/Notes/day09.pdf),
Section 9.2, printed pp.9-3--9-4 and 9-7. Read the six endpoint
conditions, basis construction, all six displayed basis polynomials
and piecewise C2 joining discussion. Data are position, ordinary first
and second derivatives at each end of the unit interval. No bounds on
those data or moments of the resulting curve are supplied. The printed
coefficient-system row `a0=b2` is inconsistent with its own second-
derivative convention; do not use that row. Use the endpoint conditions
and the general theorem below; any chosen basis must be replayed in
research. This is a source qualification, not a repaired closure proof.

Van Manh Phung, *Continuity and Convergence Properties of Integral Means
of Bojanov--Xu Interpolation*, Z. Anal. Anwend. 37 (2018), 251--268,
[DOI 10.4171/ZAA/1612](https://doi.org/10.4171/ZAA/1612),
[publisher PDF](https://ems.press/content/serial-article-files/35980),
Section 2, Theorems 2.1--2.2, pp.253--254, were reopened from the ready
zero-preserving-interpolation comparison. Distinct real nodes t_i and
positive multiplicities mu_i, total d, with derivatives through mu_i-1,
give a unique polynomial of degree <=d-1; Theorem 2.2 provides its
linear formula. For the proposed bridge the two nodes are specified,
with multiplicity three at each and all six data supplied by the Hardy
segment. This covers ordinary Hermite interpolation, not an unknown-
zero correction. The source cites Bojanov--Hakopian--Sahakian (1993),
Theorem 1.1 for the formula; that upstream proof was not newly audited.
No interpolation remainder or coalescing-node theorem is needed.

H. M. Bui and R. R. Hall, *On the derivatives of Hardy's function Z(t)*,
Bull. Lond. Math. Soc. 55 (2023), 2304--2323,
[DOI 10.1112/blms.12859](https://doi.org/10.1112/blms.12859),
[arXiv:2304.05178v1](https://arxiv.org/html/2304.05178v1),
Introduction, printed p.1 immediately before (1), was reopened. The
stated pointwise bound is Z^(k)(t)<<_k T^(1/6), for fixed k and heights
of order T. Orders 0,1,2 are required here, not only L581's endpoint
orders 0,1. The bound concerns all such heights, permitting fixed
microscopic neighborhoods of H and 2H; the later calculation must
apply it uniformly there, with ell held fixed. No uniform-in-k claim
or derivative of an unspecified remainder is licensed. Its arithmetic
proof remains an import. For complete reference moment/norm bounds
reuse L473 (6),(9)--(10) and the assessed Bettin/Bui--Hall inputs;
Proposition 3's omitted proof retains its qualification.

Fritz Colonius and Wolfgang Kliemann, *Stability radii and Lyapunov
exponents*, in Hinrichsen--Martensson (eds.), *Control of Uncertain
Systems*, Birkhauser (1990), pp.19--55,
[institutional scan](https://opus.bibliothek.uni-augsburg.de/opus4/files/47118/47118.pdf),
Section 7, printed p.39 (PDF page 22), Stat paragraph. Read its
shift-invariant path-measure definition and the subsequent periodic
path/uniform phase example. The surrounding setup takes a compact
connected real-analytic manifold M and right-continuous paths. The
comparison needed here is uniform rotation of the phase circle, with
the scalar path and its ordinary jets as observables; the later proof
must justify the pushforward and full real-shift stationarity. No
stochastic stability, diffusion or Lyapunov theorem is used. The source
asserts no Hardy approximation, derivative bounds or moment matching.
The scan screenshot timed out; its complete relevant extracted text
was accessible. No essential source is blocked by that image failure.

The named fundamental theorem of calculus and ordinary product rule
cover periodic integration by parts; their application to the four
tight entries is still a research obligation. No realization theorem
for the original dyadic law or for nu_H is imported. In particular,
Bernard's already assessed Theorem 31 need not be strengthened or
reproved to attempt the explicit deterministic bridge.

### Complete proposed test, awaiting separate approval

Retain the original target rather than only a scalar moment. Set
L=H ell. The proposed calculation appends a bridge on [L,L+1],
matching f_H's value and first two ordinary derivatives at L to their
values at 0; repeat with proposed period P=L+1 and sample a uniform
phase. This specifies a later test, not a construction verified here.
No growing bridge length, altered divisor or random endpoint selection
is needed for this nomination.

The later proof must establish C2 matching at both joins, translate
all derivative divisors, and bound the bridge's three jet coordinates
from the actual endpoint data. Obtain its required operator bound from
the fixed polynomial interpolation formula, rather than assuming
bounded derivatives merely because a bridge exists. No high-order
Hardy estimate or new arithmetic mean value theorem is indicated.

Compare uniform-period moments to L473's exact reference integrals,
not just their leading coefficients. Account for interior phases,
the final lag-one strip of the Hardy segment, phases on the bridge,
and wrap-around into the initial segment; also retain the original
reference samples just beyond 2H and the change from L to P in the
normalization. Bound every coordinate through order two on each
relevant endpoint neighborhood. Use the complete actual second/fourth
norm input for the normalization term; a pointwise bound alone is not
a substitute for that input. Finitely many indices must share one
onset and uniform constants.

Required thresholds remain exactly L473 (2): O(1) error for ordinary
second entries; same-height first/zeroth and first/second products
O(H^(-2/3)ell^(-1)) and O(H^(-2/3)ell^(-3)), respectively, at both
lags; and O_m(ell^3) error for each fourth monomial. The tight second
requirements are absolute moment bounds, not an O(1) approximation
to their small reference values. Test their periodic total-derivative
cancellation explicitly instead of estimating them by a generic bridge
error. No cancellation, error bound or successful threshold comparison
is proved in this source review.

Continue only if all these comparisons pass on a common eventual ray.
A failed entry or an unbounded normalization/join cost parks this
unit-bridge choice; keep the exact failed estimate. Success would
provide only a stationary changed marginal preserving the specified
moment data at their tolerances. It would not establish the hard
ell^2 paired support or the clipped mean ell/288, nor a derivative-
preserving rare/bulk decomposition, actual-Xi positivity or RH.
This is standard interpolation/occupation specialization, not a
protected creative central-gap attempt. Those independent missing
inputs prevent a justified creative nomination from this review.

### Search, overlap and coverage limits

External queries included `quintic Hermite interpolation endpoint value
first second derivative basis functions bound`, `Hardy Z function
stationary process periodic approximation moments derivatives`,
`"quintic" "Hermite" "Finn" 2004 pdf`, `"periodic function" "uniform"
"strictly stationary" process random shift`, `"Z-function" "periodic
approximation"`, `"Hardy" "Z" "periodic" "stationary" "moments"
closure`, and `"periodic approximation" "shifted" "moments" derivatives
zeta`. Searches for exact/stronger Hardy closures found no inspected
matching theorem. Nonprimary RH portfolios, exercise pages and search
snippets were not theorem evidence. The robot-interpolation article
was a discovery lead; PMC presented a browser challenge, and no result
from that unread article is imported. Finn and Phung are accessible.

Narrow local periodic/bridge searches and the read L473/L581 interfaces
found no completed calculation of this prescribed closure. Reused the
stationary-path, paired-Hardy-moment and L581-audit assessments. The
exact corrected-law obstruction remains canonical in L581; the direct
process-import and wave/packet stops are retained with their original
scope. This changed marginal is not excluded by those recorded stops.
No exhaustive literature search or originality claim is made.

Full matching Mathlib coverage is unchecked. The standard interpolation,
fixed-order analytic bounds and occupation inputs are citations, not
new discoveries. The sources leave a local quantitative specialization
to perform; no closure lemma, DAG row or PROOF.md change is warranted
until that later mathematical attempt. A newly ready COVERED_TARGET
needs separate approval before research under the supervisor gate.
