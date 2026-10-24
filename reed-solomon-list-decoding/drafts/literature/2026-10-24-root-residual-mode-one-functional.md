# Exact-root mode-one functional — source comparison completed

TARGET: Assess a residual-based certificate for lambda_1(K(x*))+R>=0 at L112's enclosed root, with R=c_5/u_5^2 from L120 and all data unchanged.
CHECKED: 2026-10-24
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 456 searched nonlinear-root functional error bounds, residual correction, adjoints, verified numerics and stronger dual-weighted-residual formulations; checked recent local assessments, foundations/14, ATTEMPTS/098–099 and L112/L120. No duplicate ready functional test was found; absence from this bounded search establishes no novelty.
SOURCE_EVIDENCE: Freshly read Rump, Acta Numerica 19 (2010), DOI 10.1017/S096249291000005X, corrected author PDF, Theorem 13.1 and its complete mean-value justification (13.1)–(13.4), author pp.87–88, integral argument (13.6) p.88, and centered-form discussion §11.6 (11.10) p.84; also read Rannacher arXiv:math/0305006v1 §2 Proposition 1 with its full proof and §3 Proposition 2/application, printed pp.718–719. Precise imported mean-value input and supporting Mathlib coverage are in foundations/14.
COMPARISON: Rump's generic enclosure applies to a residual-corrected scalar polynomial on the existing convex box; it needs neither an exact adjoint solve nor improved root coordinates. Rannacher's stronger dual-weighted-residual identity has Galerkin stationarity and a cubic remainder; the saved numerical point has no such stationarity certificate, and dropping the remainder supplies no rigorous sign. Neither source evaluates this Johnson functional.
GAP: Essential generic theorem coverage is ready for exactly one later fixed residual-corrected centered-form test. That turn must justify the scalar specialization, verify all rational coefficients, residual and derivative enclosures, and compare its full outward interval with zero; no corrected identity, interval endpoint or sign is proved here.
REASON: The previously missing source case is now covered by an inspected primary mean-value theorem. The local residual-correction application remains a known-method specialization, without a novelty claim or a reopened whole-box spectral test.
SCOPE: Preserve L021,L098,L112,L113,L114,L120, N,H,rho, pairs, all 64 equations/point integers/scales/endpoints and the same root. One mode, one fixed weight vector formed from the saved preconditioner, one whole-original-box derivative enclosure; no solve, scan, new root, point update, coordinate-box refinement, weight retuning or midpoint verdict.
COVERED_TARGET: Test one residual-corrected centered-form enclosure of lambda_1(K(x*))+R using L112's original box and saved preconditioner, with all data unchanged.
LITERATURE_REASON: The new target uses the contraction residual to enclose a scalar functional; old Johnson-spectrum and Krawczyk assessments did not cover this use. This turn fills that source gap; no additional literature is needed for the covered test under unchanged hypotheses.

## Main gap, use and decision threshold

Arbitrary-center safety at 67/68 agreements remains the main gap. Full
source PSD is a nearer unresolved condition for this fixed assignment.
The intermediate target is the sign of lambda_1(K(x*))+R at the already
enclosed root, using L120's fixed positive reference R=c_5/u_5^2.
A nonnegative lower certificate would settle just this one sufficient
mode comparison, a possible input to a future all-mode comparison.
It would not establish full PSD. L120's retained correction bounds
supply the existing connection to its sufficient comparison; no new
minimum-of-corrections claim is needed here.

For the single covered test, continue only if the full rigorous interval
has lower endpoint at least zero. An upper endpoint strictly below zero
rejects only this proposed mode inequality, not PSD of the principal
lower block or RS safety. A strict straddle is inconclusive and parks
this fixed residual-centered estimate. If input or derivative verification
fails, report the failure before asserting a sign. There is no automatic
second weight choice, higher-order estimate or refinement in this scope.

## Discovery, duplicates and failures

Queries actually submitted on 2026-10-24 included:

- `nonlinear equations verified functional error bounds adjoint residual interval arithmetic root`
- `Rump Verification methods 2010 nonlinear equations functional error bounds adjoint`
- `Becker Rannacher optimal control approach a posteriori error estimation theorem 2.1 remainder pdf`
- `Rump ActaNumerica2010 pdf mean value form slope functions`
- `"residual" "functional" "interval" "adjoint" nonlinear error bound`
- `"Becker" "Rannacher" "2001" "pdf" "Proposition 2.3"`
- `"residual correction" "interval" nonlinear functional bounds`
- `Rannacher 2002 ICM Adaptive finite element methods arxiv`
- `"goal-oriented" "nonlinear" "error bounds" "certified" adjoint finite dimensional`

The search led to Rump's corrected author PDF and Rannacher's primary
arXiv lecture; the needed passages were actually read. Becker–Rannacher,
Acta Numerica 10 (2001), DOI 10.1017/S0962492901000010, was identified
through publisher metadata and search excerpts, but its full theorem
text was not inspected and is not imported. Probabilistic nonlinear
functional bounds, PDE-specific adjoint estimates, and Alefeld's survey
were additional unread leads, not essential missing inputs. Searches
and excerpts alone are not treated as theorem coverage.

The scoped duplicate search covered recent 2026-10-22/23/24 literature
assessments and foundations/14 for residual, adjoint, goal-oriented and
centered-form terms, together with ATTEMPTS/098–099. L112's saved
polynomial-system and preconditioner definitions, L120's complete
reduction/spectral-evaluation passages and its working record were
inspected to establish applicability, without rerunning any certificate.

ATTEMPTS/098 retains the distance-68 whole-box shell straddle.
ATTEMPTS/099 and audited L120 retain the global signed-sum straddle,
with distinct lower and upper spectral minimizers. These give no
exact-root sign and are not repaired here. The proposed new mechanism
uses the exact equations through a fixed scalar residual correction;
it does not replace their old interval endpoints or replay either test.

## Primary theorem comparison

The canonical import is in
[foundations/14](../../foundations/14-validated-nonlinear-enclosure-source.md).
The inspected primary source is
[Rump, corrected author PDF](https://www.tuhh.de/ti3/rump/intlab/ActaNumerica2010.pdf),
Theorem 13.1, author pp.87–88 (zero-based PDF pages 86–87).
The full row-wise justification matters: a vector mean-value formula
cannot assume one common intermediate Jacobian point. The scalar
application can be placed in the first component of a 64-output map,
with the other components zero. Polynomial differentiability and the
convexity of L112's original box meet the qualitative hypotheses.
The theorem imposes no exact-adjoint condition. All actual enclosures
and the residual correction still need to be checked in research.
The §11.6 centered-form discussion explicitly warns that enclosures may
be too wide; no success guarantee is imported. PDF text was inspected;
screenshot requests returned no usable image, so no visual check is claimed.

For stronger standard terminology compare
[Rannacher, arXiv:math/0305006v1](https://arxiv.org/pdf/math/0305006v1),
§2 Proposition 1, full trapezoidal-rule proof, printed p.718, and §3,
Proposition 2, p.719. The first requires stationary points on the full
space and a Galerkin subspace and enough third differentiability for
its explicit cubic integral remainder. The second specializes to primal
and dual residuals. Its subsequent practical estimator neglects that
remainder. No exact Galerkin/adjoint stationarity for L112's rational
point is available, and an unbounded discarded remainder cannot prove
a sign. This is a comparison, not a theorem imported into the RS
argument. It motivates retaining every correction error in the simpler
mean-value specialization instead of adding a dual solve.

Supporting Mathlib theorem declarations were read in
[Mathlib.Analysis.Calculus.MeanValue](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Calculus/MeanValue.html#Convex.norm_image_sub_le_of_norm_fderiv_le).
The ordinary and primed `Convex.norm_image_sub_le_of_norm_fderiv_le`
statements provide norm bounds on a convex set under differentiability
and a uniform derivative bound. They are supporting results, not a
verified implementation of this residual interval certificate. Full
matching coverage is not checked; unknown availability is not absence.

## One covered later test; no derivation in this turn

Use distinct notation to avoid L112's preconditioner and L120's scalar
reference both being called R. Call the saved rational preconditioner C,
the scalar reference R0, and the normalized coordinates v_i=x_i/s_i,
with the same original s_i=10^(scale_powers[i-5]), point a and box B.
F(v) denotes precisely L112's complete normalized cubic system, not a
new contraction system. All 81,355 aggregate coefficients and all
repeated-factor derivative occurrences remain relevant.

The proposed linear functional is G(v)=1+w^T v, where the future check
must reconstruct w_i=P_1(i)*s_i/R0 from L120's exact integer Johnson
coefficients. Fix the sole proposed adjoint weight z=C^T w using the
saved C, without solving or fitting anything. The proposed corrected
polynomial is h(v)=G(v)-z^T F(v).

The next research turn must establish its equality to G at the retained
root and its full derivative formula, then apply the imported mean-value
enclosure to h from a over the unchanged B. These are future
specialization obligations, not a new result or an evaluated estimate
in this literature step. No assertion that z solves an adjoint equation
is permitted; its entire derivative defect must be enclosed. Exact
signed coefficient collection before interval evaluation is covered,
including across contraction rows. All residual terms and rounding
errors must be retained. A point value alone is never the verdict.

The test must save the complete weight vector, corrected polynomial/
derivative data, original-input bindings and final rational enclosure
in a local certificate, with an independent reconstruction of the
load-bearing rational operations. Print only endpoints relative to the
zero threshold, failures and artifact paths. Existing Krawczyk existence
and uniqueness *in the original box* are reused; do not form or iterate
a smaller coordinate enclosure, update a, or change C or B.

Essential inputs remain L021,L098,L112,L113,L114,L120 and
foundations/09,12,13,14, including the positive-factor-enclosure and
full-product-global-comparison certificates and their retained audits.
Even success would leave modes j!=1, the full included/excluded source
PSD, stronger distributions, global positive-root uniqueness, measures,
packing, RS realization and the 955–957 boundary unresolved. This
source review changes none of those mathematical conclusions or the DAG.
