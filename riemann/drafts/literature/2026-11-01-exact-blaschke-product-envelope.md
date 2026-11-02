# Exact finite Blaschke product — source assessment

TARGET: Determine whether the exact finite Blaschke product in L645, without replacing its factors by q_delta, changes C645b's convexity-envelope obstruction at N=floor(log gamma).
CHECKED: 2026-11-01
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Rechecked L645 (6), C645a's conclusion, C645b's exact-product step and audited qualification, C644a's conclusion, the completion-stripped attempt stop and its audit history. Targeted local and external logarithmic-product, Riemann-sum and Euler–Maclaurin searches are recorded below; no inspected theorem settles this exact rate comparison and no novelty is inferred.
SOURCE_EVIDENCE: Newly inspected NIST DLMF 1.2.8 (2026-09-15), Section 2.10(i), hypotheses and full equation 2.10.1 including its finite integral remainder. Reuse Zakeri Section 8.3 after Example 8.33 and Gonek/digamma/Pick coverage from drafts/literature/2026-11-01-completion-stripped-pick-residual.md; those unchanged inputs need no refreshed proof review.
COMPARISON: Standard finite-Blaschke division already supplies the exact product, and Euler–Maclaurin covers controlled finite-grid summation for a sufficiently smooth logarithm. Neither source compares this disk/grid's contraction with delta/4. C645b's q_delta replacement, C645a's completed norm and C644a's fixed reserve do not settle that comparison.
GAP: A later calculation must specialize the summation estimate to the existing factors, retain endpoint and finite-N errors and both floor inequalities, and determine the rate's relation to delta/4 for every fixed delta in (0,1/2), resolving any equality cases. Actual residual control and derivative lower bounds remain independent gaps.
REASON: The changed target's missing finite-grid source coverage is now available. Only elementary quantitative specialization and comparison remain; reproof of finite-Blaschke division, convexity or Euler–Maclaurin is unnecessary. This is source readiness for a bounded refinement, not a new signed mechanism or a calculated result; the changed assessment awaits separate supervisor approval before research.
SCOPE: Fixed delta in (0,1/2), stipulated simple rho, L645's unchanged disk and nodes, N=floor(log gamma), and C645b's existing envelope U. Permitted work is the exact-product rate/finite-grid comparison only. No small-delta uniformity, effective onset, zero existence, actual PSD or residual saving is assumed.
LITERATURE_REASON: The invocation-start REVIEW_REQUIRED nomination changed q_delta^N to the exact finite product and lacked summation-error/theorem comparison. This turn supplies that essential changed-target coverage without reopening the already covered analytic estimates.

The nomination below is preserved; the completed source review at the
end supersedes its pending-review status. No rate was calculated here.

## Why this is a different test

The prior target was audited, not reopened with the same estimate.
L645 already retains an exact product of n explicit factors before
bounding it by q_delta^n. C645b's audit identifies that inequality as
another possible loss, separate from the absolute residual envelope.
The proposed change uses the known factor distribution of the same grid;
it does not ask for the missing derivative lower bound or rename the norm.
No improved rate or favorable comparison is claimed in this nomination.

The literature review should first reuse the assessed finite-Blaschke
statement and its exact L645 specialization. Search the specific
logarithmic-product/Riemann-sum comparison and standard interpolation
error terminology, check local overlap, and inspect only primary inputs
actually needed for a later controlled comparison. Do not repeat the
unchanged gamma, convexity or singular-Pick source review. A citation or
elementary specialization may suffice; no novelty is presumed.

## Bounded later mathematical test, not performed here

Use the exact factors already defined in L645 (6) and C645b's audit.
Compare the normalized negative logarithm of their product with delta/4,
the existing difference between the circle and derivative upper
exponents. Retain the finite-N error and both directions of rounding at
N=floor(log gamma). An equality at the leading rate requires controlling
the remaining logarithmic and finite-grid factors; a leading-rate
preview would not settle it.

Continue only if the comparison supplies a rigorous strict rate gap or
a resolved equality case that changes whether the present upper-envelope
failure is forced. If the exact product still forces that failure, park
this refined certificate with the new evidence. If it does not, record
only removal of that particular obstruction: an upper-envelope test
cannot certify non-PSD from an upper bound on the derivative alone.
Do not infer an actual residual saving, a derivative lower bound or any
matrix sign. If the test merely repeats q_delta^N, abandon it as duplicate.

Essential local inputs for the continuation: L018, L645, C645a and audited
C645b. C644a and L258 are comparisons only. Unresolved assumptions are
exactly the actual signed inequality, useful residual/derivative control,
multiple-zero extension and all-degree positivity. No cross-notebook
input is proposed. Matching Mathlib coverage for the full exact-product
comparison is unchecked; the existing supporting coverage is unchanged.

At nomination this file was not approval or a mathematical result, and
the next invocation was literature-only. No justified creative sign
mechanism emerged from that audit; this refinement must not be labeled
creative to meet a scheduling target.

## Completed source review — 1 November 2026

This literature-only step closes the source-scope gate for the unchanged
TARGET, subject to separate approval of this changed assessment. It
does not evaluate a logarithmic integral, establish a rate inequality,
or strengthen C645b. The main gap remains actual-Xi signs at unbounded
heights and all-degree mixed positivity. This target can determine
whether a specific inequality loss accounts for the failed envelope
certificate; even a favorable answer would supply no actual sign.

### Primary input newly inspected

NIST DLMF **1.2.8** (15 September 2026),
[Section 2.10(i), equation 2.10.1](https://dlmf.nist.gov/2.10#E1),
accessed 1 November 2026: read the hypotheses and full remainder.
For integers A<B and m>0 with f^(2m) absolutely integrable on [A,B],
the source states

\[
\begin{aligned}
\sum_{j=A}^{B}f(j)={}&\int_A^B f(x)\,dx+\frac{f(A)+f(B)}2\\
&+\sum_{s=1}^{m-1}\frac{B_{2s}}{(2s)!}
 [f^{(2s-1)}(B)-f^{(2s-1)}(A)]\\
&+\int_A^B\frac{B_{2m}-\widetilde B_{2m}(x)}{(2m)!}
 f^{(2m)}(x)\,dx .
\end{aligned}
\]

The tilde denotes the periodic Bernoulli polynomial. C^(2m)
regularity suffices here. Subsequent examples' first-omitted-term
estimates are not generic remainder signs.

The later proof must check regularity of the logarithm of L645 (6),
rescale the grid and account for the omitted endpoint j=N, allowing
fixed-delta constants. No delta/4 comparison is supplied by this source.
No Abel–Plana or gamma-product asymptotic is needed. The HTML statement
was available in full; the optional TeX endpoint was unsupported.

### Reused inputs and duplicate/failure checks

The ready [completion-stripped assessment](2026-11-01-completion-stripped-pick-residual.md)
already inspected Zakeri's author Notes and Comments, Section 8.3,
paragraph after Example 8.33, including the full finite-division proof.
It permits any selected finite set of zeros of a bounded disk-holomorphic
function and requires no boundary continuity. L645 (6) and C645b's
exact-product proof step are its established specialization. Reuse that
proof and the already assessed uniform envelope; do not reprove them.
Gonek (1984), Section 2 (20), p.127 and its Cauchy paragraph, and the
DLMF gamma/digamma inputs retain their previously checked hypotheses.
No changed zeta growth hypothesis is proposed.

Read the relevant canonical statements and proof ranges: L645's
hypotheses and finite-Blaschke step, C645b's hypotheses/conclusion and
exact-product/exponent-comparison steps, and C645a/C644a's conclusions.
The [completion-stripped stop](../../ATTEMPTS/2026-11-01-completion-stripped-convexity-envelope-limit.md)
and [independent audit](../../history/2026-11-01-c645b-independent-conceptual-audit-01.md)
explicitly leave the smaller product open. C645a's lower bound concerns
the completed norm; it cannot be assigned to this residual. C644a
excludes a fixed reserve in a different matrix-norm test; it is not a
rate comparison. Targeted searches in the vertical-Pick and
completion-stripped assessments and named audit/stop records found no
earlier settlement of this exact test. Earlier distinct-pole annulus
product bounds concern a different quantity and supply no such import.
L258's comparison scope is reused from the prior assessment; it was
not reread or assumed to settle the new test. No cross-notebook input.

### Bounded search record and unread leads

External queries actually submitted:

- `"finite Blaschke product" "Riemann sum"`
- `"Blaschke product" "Euler Maclaurin"`
- `site.dl mf.nist.gov 2.10 Euler Maclaurin remainder` (mistyped
  domain spacing; followed by direct primary-page access)
- `"Blaschke" "zeta" "logarithmic" interpolation product`
- `"finite Blaschke" "equispaced" asymptotic`
- `"Blaschke products" "contraction" "Riemann sums"`
- `"R^2(d^2+t^2)" Blaschke`
- `"Blaschke" "logarithmic grid" "zeta"`
- `"Blaschke" "equispaced nodes" product`

Searches surfaced Bishop–Lazebnik's author-hosted Runge_Jan4.pdf, Kunik's
*Logarithmic Fourier integrals for the Riemann Zeta Function*,
arXiv:0804.4829, and unrelated infinite-product/interpolation work.
These are **unread leads**, not theorem evidence or claims of
nonapplicability. No conclusion here relies on their snippets. The
finite-Blaschke source already covers the exact product and DLMF
covers the needed generic summation mechanism; no essential missing
result from those leads was identified. This bounded search neither
establishes novelty nor rules out an existing exact evaluation.

### Remaining proof obligations and decision test

Approve only routine specialization, classified REPRODUCTION, for the
unchanged TARGET. Keep L018, L645, C645a and audited C645b as essential
local inputs. Importing the generic summation theorem does not replace
the exact parameter comparison, which justifies a calculation rather
than citing an uninspected matching theorem. No reproof is needed.

The calculation must preserve the exact factors and show how finite
errors and floor rounding affect the envelope test. Resolve the full
fixed-delta interval, stating any parameter subranges honestly. A
strict rate gap decides this exponent test; an equality requires its
endpoint, logarithmic and finite-grid factors. Do not infer success
from a leading-rate preview. If divergence still follows, preserve
the refined stop and park this certificate; if it does not, report
only that C645b's stopping reason has not extended to the exact product.
An unresolved derivative lower bound can still prevent certification.
Abandon duplication of q_delta^N or a mere unspecified norm.

Matching Mathlib coverage for the full grid/threshold statement remains
**not checked**, not absent. Existing supporting coverage for Pick and
Borel–Caratheodory is unchanged. No lemma, mathematical script, rate
claim, PROOF.md or DAG.md change belongs to this literature step.
