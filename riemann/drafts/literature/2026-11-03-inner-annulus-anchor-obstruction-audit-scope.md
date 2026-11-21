# Proposed source scope for the inner-annulus comparison audit

TARGET: Critically audit L705's fixed-profile failure of uniform anchor comparison at radii 1/4 and 1/2, including both endpoint sums and the complete spatial logarithmic means.
CHECKED: 2026-11-03
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 152 reuses steps 147/149's exact-target, stronger-result and failure comparisons; two bounded supplementary queries on boundary-zero Poisson--Jensen and spatial anchor Rouche found no inspected matching endpoint theorem. Read L705's claimed applications and the relevant L657/L666/L703/L701 statements and local stop records; no novelty inference is made.
SOURCE_EVIDENCE: Reinspected Ash--Novinger, Complex Variables, Theorem 4.8.3/Lemma 4.8.4 and boundary-factor argument pp.33-36, Corollary 4.7.4 p.27; Mathews--Howell Section 8.7 Theorem 8.7.11/Corollary 8.7.12 and Remark 8.7.13; Brunault--Zudilin Propositions 1.4-1.5 pp.6-7; Issa--Lalin arXiv:1203.5379v1 Remark 3.8/Theorem 4.1 and proof p.7. Reuse the complete earlier primary proof readings with their recorded qualifications.
COMPARISON: These theorems cover the fixed-radius polynomial logarithms and boundary-zero Poisson interface for nonzero spatial polynomials, with no fixed-degree restriction. They do not establish the endpoint limits, n-uniform estimates or two-point noncancellation. Mathews--Howell's symmetric Rouche theorem is broader than the anchor-dominance condition tested by L705; failure of that condition must not be reported as failure of every Rouche comparison.
GAP: The separate audit must verify uniform O(log n) product errors near the angular pole, both exact shifted endpoints without reflection, signed phase cancellation, the two-point spatial Poisson bound, complete factors and the restricted contour conclusion. No charge deficit follows from a negative-real angular point.
REASON: Essential source scope is adequate for the exact saved conceptual audit; approval concerns applicability, not the correctness of L705. The source comparison adds no endpoint theorem or mathematical bound. No lemma or mathematical script is changed.
LITERATURE_REASON: The saved REVIEW_REQUIRED audit has changed negative-radius and growing-spatial-polynomial applications; this separate comparison reuses adequate primary readings and resolves only their applicability scope.
SCOPE: Only TARGET for one actual L703 profile fixed before n=12q+3, retaining L657 complete K,Q and L666 unit masses, anchor, inverse angle, j=0, both endpoints and every M=n/3 moment; audit or repair this claimed obstruction, without stronger compensation or a new profile selection.

## Exact proposed audit and limits

Keep one actual L703 profile fixed before n=12q+3. Essential inputs
are L657's complete K,Q, center exceptions and logarithmic accounting;
L666's exact family, unit masses, anchor, inverse angle, j=0, endpoints
-2q and 2q-1 and all M=n/3 moments; and L703's fixed summable cap.
L704 is a preserved partial result and source-interface reference,
not a premise for a stronger charge. No root simplicity, effective
onset, finite support, reflection or gap on a comparison path is assumed.

The conclusion to review is only a failure of uniform comparison to
K_0=Q*T_M(x*zeta/R)/R on the two circles. For either radius r,
L705 claims a full spatial nonanchor log mean n*Phi_r(9/20)+O(log n),
where Phi_r(9/20)>3/40, versus anchor mean -log R. It does not claim
a lower angular mean or refute Z_n^(1/2)>=P_n^(1/2)-o(n).
The auditor must preserve this distinction and the positive-measure,
possibly n-dependent spatial failure set.

Check the complex logarithmic derivative and the geometric endpoint
factor exp(-A*lambda)/(1-exp(-A*lambda)), including the actual
outermost ordinate Y-A/n and the cap-adjusted Y-A*(k+7/8)/n.
Check both signs in the negative-node reindexing. The finite-product
estimate near y=O(1/n) uses bounded variation and rational distance
from the angular pole; no uniform smooth Riemann estimate there is
available for free. The spatial proof must keep both resolvents,
permit cancellation at either evaluation point, use compactness only
for a nonzero two-point vector, and handle boundary zeros in Poisson.

No numerical profile, scalar subsequence or script certificate is an
input. The rational bounds are written in the canonical proof. Full
matching Mathlib coverage is unchecked; the Mahler support recorded
in L657 is not a formalization of this asymptotic. Source approval
must not be confused with the later mathematical audit. No new theorem
coverage or proof approval is supplied by this nomination.

## Completed source comparison — 3 November 2026, step 152

The preceding nomination is historical. The fields above now approve
the same exact audit; L705 itself remains unaudited. This is a new
scope comparison, recorded as EXPLORATION, not a new mathematical
input or a repetition presented as an advance. No calculation-budget
turn is spent by this literature-only step.

### Source interfaces and changed applications

Reuse the [step-147 comparison](2026-11-03-gevrey-inner-disk-complete-charge-scope.md)
and [step-149 boundary-case assessment](2026-11-03-inner-disk-charge-partial-audit-scope.md).
Primary statements and relevant boundary proof cases were reopened
before supplementing the comparison. No general theorem is reproved.

R. B. Ash and W. P. Novinger, *Complex Variables*, hyperlinked web
text, [Theorem 4.8.3 and Lemma 4.8.4, printed pp.33-36](https://people.math.sc.edu/girardi/m7034/book/AshComplexVariablesWithHyperlinks.pdf#page=94),
cover an analytic function on a neighborhood of the closed disk,
not identically zero, evaluated at an interior nonzero value.
Interior zeros enter with multiplicity; boundary zeros are allowed
and their logarithms are integrable. The proof removes finitely many
boundary factors and passes from exterior-root harmonic logarithms;
the earlier full proof reading is retained. [Corollary 4.7.4,
p.27](https://people.math.sc.edu/girardi/m7034/book/AshComplexVariablesWithHyperlinks.pdf#page=88)
gives Poisson-kernel mass one. The recorded even-kernel shortcut must
not be used for a general complex evaluation point.

For L705 the disk variable in this application is spatial z, not
angular u; the evaluations are 0 or the real point 1/2. Each normalized
V_n(-r,z) or G_n(-r,z) is a polynomial in z if its displayed finite
family is used. Growing degree creates no additional hypothesis in
this theorem. Nonzero evaluation, a uniform boundary upper bound,
the two-point alternative and the direction of the signed comparison
remain local audit obligations. The theorem supplies no uniform
logarithmic lower bound from convergence alone. In particular, do not
assume both evaluation values stay nonzero for every phase, and do
not integrate an unbounded negative logarithm by uniform convergence.

F. Brunault and W. Zudilin, *Many Variations of Mahler Measures*,
ISBN 9781108794459, [Propositions 1.4-1.5, pp.6-7](https://assets.cambridge.org/97811087/94459/excerpt/9781108794459_excerpt.pdf),
give the root integral with roots inside, outside and on the circle.
Reuse the complex-analytic boundary-arc proof, not an unqualified
equally spaced Riemann sum through a boundary root. Actual degrees
and leading coefficients must be retained. Angular rescaling keeps
K(r*v,z) polynomial; it does not establish a uniform asymptotic.

Z. Issa and M. Lalin, *A generalization of a theorem of Boyd and
Lawton*, [arXiv:1203.5379v1, 24 March 2012, Remark 3.8 and
Theorem 4.1/proof, p.7](https://arxiv.org/pdf/1203.5379v1),
cover nonzero complex polynomials and the required absolute logarithmic
integrability (s=1). This permits finite-n polynomial accounting with
circle roots; no n-uniform small-value constant is imported. Complete
Q factors and exceptional center slices still require local handling.

J. H. Mathews and R. W. Howell, *Complex Analysis*, online
[Section 8.7, Theorem 8.7.11, Corollary 8.7.12 and Remark 8.7.13](https://complexanalysis.org/web/sec_argument-rouche.html),
state the symmetric strict condition |f+g|<|f|+|g|, for functions on
the stated domain with no boundary zeros or poles; the analytic case
equates zero counts. The remark includes the usual stronger condition.
L705 tests only |K-K_0|<|K_0| on each full circle. Neither the broader
condition nor equality of zero counts is disproved by its failure.
Multiplicity and boundary qualifications remain essential to any later
application. Here the theorem explains the proposed sufficient test;
it is not used to infer a count from a failed hypothesis.

### Duplicates, local obligations and bounded decision

L701 assumes reflection and studies a scalar microscopic coordinate
on a subsequence. Its endpoint technique does not cover L705's fixed
radii, independent endpoint shifts or complete spatial polynomial.
L704 proves a partial charge using a positive angular evaluation; it
does not give this negative-point obstruction. L703 supplies a single
actual profile with a cap and decay. Its Fourier gap need not be
invoked in L705, whose statement uses only those profile properties.

Read the short [anchor-comparison stop](../../ATTEMPTS/2026-11-03-inner-annulus-anchor-comparison-stop.md),
[global-endpoint stop](../../ATTEMPTS/2026-11-03-centered-gap-global-endpoint-extension-stop.md)
and [paired-tail stop](../../ATTEMPTS/2026-11-03-gevrey-paired-tail-absolute-variation-stop.md).
The latter two concern the discarded interior at u=-1 and an unpaid
absolute-variation majorant. They neither verify nor refute the two
fixed-radius endpoint applications. No stopped mechanism is reopened.

Supplementary queries were `"Poisson Jensen" polynomial "boundary zeros"
logarithm` and `"Rouche" "anchor" "spatial" polynomial endpoint`.
They returned no additional primary theorem inspected for this exact
asymptotic. Secondary pages and unrelated RH claims were not used.
The comparison to stronger general tools otherwise reuses step 147;
an unsuccessful query is not evidence of novelty or nonexistence.
The essential primary sources above were accessible.

The audit is justified as a check of already written applications,
not a reproof of Jensen, integrability or Rouche. Inspect L705 Sections
2-4 in full: the near-pole logarithmic Riemann error down to y=O(1/n),
the complex logarithmic derivative and geometric endpoint factor,
both signed reindexings and cap-adjusted endpoint distances, the
uniform sum retaining all M moments, and the two-point argument with
boundary zeros. Check complete-factor transfer to K and the scope of
the possibly n-dependent spatial failure set. No script certificate
is an input; no numerical or effective onset has been approved.

Continue only if all those applications support the stated full
spatial means and limited anchor obstruction; otherwise isolate a
specific repair or qualify only the unsupported conclusion. Do not
promote a pointwise angular obstruction to a charge deficit. The
o(n) inner-charge deficit, annular compensation, H/support, realization
and actual-Xi positivity remain unresolved. Full matching Mathlib
coverage remains unchecked; L657's recorded Mahler tools are supporting
coverage only. SPECIALIZE approves this audit and no stronger target.
