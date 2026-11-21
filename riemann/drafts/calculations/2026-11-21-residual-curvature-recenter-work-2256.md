# Residual-curvature midpoint translation2256

Saved before the sign pass, 21 November2026. Reuse the unchanged
SPECIALIZE2254 target and its complete source comparison. Main gap:
L030-L032/C032a actual-Xi all-degree mixed positivity. The one target
is W_x>0 on [14,29/2] times [0,1]; a positive result could provide a
compact residual shape input, with exterior, removal preservation
and all-degree transfer still unresolved.

2255's complete fixed pass left3072 crossing enclosures and no
nonpositive enclosure. Its worst polynomial lower endpoint was
already negative before the complete remainder inflation. This step
performs exactly the nominated representation change: translate each
saved interval polynomial W to its closed cell midpoint and evaluate
on the symmetric interval [-1/1024,1/1024]. Keep all131072 closed
cells, x mesh, degrees, precision80, input coefficients and complete
nonlinear error bounds unchanged. No quadrature, new derivatives,
mesh refinement, root substitution or automatic retuning is allowed.

For V(d)=sum a_k d^k and h=midpoint(u)-parent_center, use
b_j=sum_(k>=j) binom(k,j)a_k h^(k-j). This is the finite binomial
identity, with interval coefficient uncertainty retained. An in-place
triangular translation implements it with outward-rounded operations.
The saved2255 product-error bound still applies because its I,G,K
magnitude bounds cover the identical closed cell. Translation changes
only V's representation; no actual remainder is dropped or recentered.

Require strictly positive final lower bounds on every closed cell,
or a rigorously nonpositive upper endpoint to reject the stronger box.
Crossing enclosures remain inconclusive. Save every failure. A second
inconclusive attempt ends this fixed-enclosure mechanism; do not repeat
it unchanged. Correct CPython integer/Fraction and directed libmpdec
arithmetic remain assumptions. Full matching Mathlib coverage is
unchecked. No cross-notebook theorem is used and no RH candidate is
claimed. Check the whole resulting cell/error certificate; its preview
does not establish correctness. A later audit would require its own
coverage and separately routed turn.

## Completed fixed pass and complete inspection

Outcome EXPLORATION. Midpoint translation reduced crossing enclosures
from3072 to1024 of131072 cells. The other130048 cells have positive
computed lower endpoints. There is no nonpositive upper endpoint,
positive full-box bound, actual-root countervalue, canonical new lemma
or RH candidate. The worst final lower endpoint is approximately
-3.65395904e-12; the requirement is strictly greater than zero.
No second pass or settings change was performed.

The complete certificate is
`scripts/real-zero-origin/residual_curvature_recenter_2256.json`.
The inspector consumed every old/new cell pair, the entire error
budget for every new cell, all closed-face coverage, all failures and
all regional/global extrema. It passed1441861 exact-rational checks
with no failures. It also checked all33 worst-cell translated
coefficients against the exact finite binomial formula and checked
that cell's symmetric Horner range by exact rational arithmetic.
Full evidence is
`scripts/real-zero-origin/residual_curvature_recenter_inspection_2256.json`.
This is not an independent replay of all translated coefficients,
quadrature, polynomial formation or the arithmetic backend. No audit
acceptance is claimed. The unchanged2251/2253 inputs and2255 files
were preserved.

Region14 fails only subcell31; region15 fails subcells29,30,31,
each for all256 x cells. Thus the failed u cells are [479/512,15/16]
and [509/512,255/256], [255/256,511/512], [511/512,1]. Their closures
and every shared boundary were included. No face was replaced by an
interior grid sample.

The worst record is x in[14,7169/512], u in[479/512,15/16]. Its
midpoint shift from the parent center29/32 is31/1024. The translated
constant interval has lower endpoint about2.99570833e-12 and upper
endpoint about8.97076195e-11. The symmetric nonconstant enclosure is
approximately[-6.64963897e-12,6.64963897e-12], so the polynomial
enclosure already has negative lower endpoint about-3.65393064e-12.
The complete nonlinear inflation is less than2.840e-17. These decimal
summaries are not substitute bounds: complete endpoints, all33
translated coefficient intervals, the old coefficient record binding,
and the exact-rational checks are in the full worst-cell record.
As in2255, changing only the final remainder inflation cannot repair
this saved polynomial enclosure. Neither endpoint is a value of W.

For completeness, the triangular translation can be verified by its
loop invariant. With original degree n, after outer iterations
n-1,...,i, the current coefficient at index j>=i is

    sum_(k=j)^n binom(k-i,j-i) a_k h^(k-j).

Indices j<i are unchanged. In the next increasing-j inner loop,
Pascal's identity combines the old terms at j and j+1; at j=i-1
it gives a_(i-1)+h times the previous entry at i. After i=0 the
coefficients are exactly the ordinary binomial translation. All
interval operations are outward, so uncertain original coefficients
can only widen these ranges. Evaluating the translated polynomial
in y=u-midpoint gives precisely the same finite polynomial. The
original full I/G/K remainder estimates remain valid on this same
closed cell; reusing their old magnitude bounds is conservative.
There is no claim that interval lower bounds commute with translation
or that the coefficients' discarded dependence has been recovered.

Mathematical inputs are exactly L019/L058, C919m's half-line
identities and C919r's complete bounds(5)-(14), with the precise
Conrad/Tao/DLMF/Taylor citations and source qualifications retained
in assessment2254 and work2255. This elementary finite polynomial
representation change needs no new general analytic theorem.
CPython3.15.2/libmpdec4.0.1 at precision80 raised only Inexact/Rounded.
Correct integers/Fraction and directed basic operations remain
contracts, not independently certified facts about the runtime.
No new transcendental evaluation was needed. Full matching Mathlib
coverage remains unchecked; absence is not asserted.

## Route reassessment and continuation scope

Two bounded attempts,2255/2256, remain inconclusive. Close the fixed
coefficient-enclosure route; do not run an unchanged third pass or
infer that compact curvature is false. The unchanged-source numerical
mechanism has not produced a justified threshold. The source records
2254/2239 and scoped stops2241/2246 distinguish quotient positivity
from correlation-kernel positivity; C919q explicitly makes no
logarithmic-concavity assertion. None of those statements alone
settles a log-concavity preservation law. No new external search or
theorem assessment was performed this turn.

The uncovered next nomination is a first-real-zero-conditioned
log-concavity preservation test. If a source supplies it, import its
exact hypotheses; otherwise source review must fix an admissible
counterexample test before a creative attempt. This changes from
repeated compact enclosures to a proposed removal invariant, relevant
to iteration but still insufficient by itself for all-degree mixed
positivity. The first-zero restriction, exact decay class, known
preservers/counterexamples and duplicate scope are essential unread
coverage, recorded REVIEW_REQUIRED in the new assessment. No theorem,
model or ready approval for that target is derived here. Prior ready
2254 coverage does not authorize it. Exterior curvature, actual-Xi
applicability, repeated-removal closure and the all-degree interface
remain unpaid. The next step is literature-only preparation, not an
automatic third calculation or a mislabeled creative specialization.

Reproduction, from the active notebook:

    python3 scripts/real-zero-origin/residual_curvature_recenter_2256.py
    python3 scripts/real-zero-origin/inspect_residual_curvature_recenter_2256.py

PROOF.md and DAG.md remain unchanged: no established mathematical
argument was added. No shared infrastructure or supervisor state was
edited. No cross-notebook premise is used.

Scoped documentation validation passed with --problem riemann.
PROOF/DAG hashes match the supplied snapshot; checkpoint target matching
and size checks passed. No dependency was added or changed.
