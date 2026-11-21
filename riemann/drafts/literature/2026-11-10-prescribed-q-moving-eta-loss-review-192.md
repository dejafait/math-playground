# Moving-eta loss — bounded specialization assessment

TARGET: Test whether Q_{eta_(n+1)}(n)-Q_{eta_n}(n)>=-A/8 for every n>=1, with eta_j=1/(64*9^j), L964's a_n, one fixed A>=sum_j|beta_j|, and the full resolvent charges retained.
CHECKED: 2026-11-10
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step192's direct-index review searched regularized Li recurrences, resolvent monotonicity and exact Q_eta terminology; no inspected theorem covers this two-parameter comparison. Existing single-eta estimates were compared explicitly; bounded search does not establish novelty.
SOURCE_EVIDENCE: NIST DLMF https://dlmf.nist.gov/1.9.E30 and https://dlmf.nist.gov/1.9.E31 (Cauchy hypotheses/formulas), https://dlmf.nist.gov/1.10.E1 (analytic-disk Taylor theorem), version1.2.8; H. Xiao https://arxiv.org/pdf/2006.13103v1 Theorem3.2 and Corollary3.3/proof pp4-5; local L964(7),(9)-(13), L966 and L968 coverage reused from step192.
COMPARISON: L964 bounds Q_eta(n)-lambda_n one-sidedly at one eta; subtraction of two such bounds is invalid. Standard analytic tools and L026 node geometry are ready, but the entire two-eta loss and its uniform threshold remain to be proved. RH-conditional recurrence estimates are inapplicable.
GAP: Establish or rigorously refute the proposed uniform lower bound on the complete moving-eta difference; retain the constant part of a_n^2, the remaining analytic part, absolute convergence and realness. No sign or bound for this difference has been derived in step192.
REASON: This isolates one necessary signed error in a later n-recurrence with an independently testable threshold. New specialization is justified by the changing denominator; it is not a reproof of Li's criterion or of the existing single-eta bound. Step193 separately checked the direct primary URLs and approved the unchanged specialization scope for a later mathematical turn; no bound is imported.
SCOPE: Actual Xi and paired beta_j=alpha_j^(-2) with all multiplicities; L024 summability and L026 geometry; real finite A>0 with sum_j|beta_j|<=A; integer n>=1; algebraic a_n^2 with L964/L966 normalization; only this parameter-loss test. No full index recurrence, all-Q signs, new finite-Q certificate, theta-profile rescue or assumed positive Stieltjes representation.

## Exact test and downstream use

For a positive real eta define the already existing regularized observable

    Q_eta(n)=sum_j beta_j^2 a_n(beta_j)^2/(beta_j+eta).

The index inside a_n is n on both sides of the TARGET. Changing it to
n+1 in the first term would be another problem. The evaluation
Q_{eta_(n+1)}(n) is an off-diagonal parameter value, not a relabeling
of the prescribed Q_(n+1). Seek exactly the lower bound in TARGET.
The constant A is independent of n; an existential finite mass bound
suffices. No numerical value or zero data is required.

This is one component of an induction-or-obstruction test for the
L966 sign problem. If it succeeds, the rapid eta change can be charged
at a uniform scale in a later recurrence. The fixed-eta signed forcing,
recurrence closure, initialization, and a margin paying accumulated
losses remain independent gaps. No implication from this bound alone
to Q_n>=0 or RH is asserted. L968 is the existing conditional downstream
link, not an assumed sign input; L970's audited n=2 base is not needed.

## Ready tools and remaining specialization

Reuse L964's pre-margin Cauchy estimates for a_n^2 on the fixed disk;
they do not assume a negative Li coefficient. Use the full L026
alpha geometry, not just Re(beta)>0 if a sharper sector is needed.
The elementary subtraction of the two scalar rational weights may be
used, with no operator spectral theorem or RH-positive measure import.
Its signed summation is the new obligation. A future proof must check
every denominator and absolute majorant before separating sums; actual
conjugation symmetry must justify realness. No two-sided version of
L968's one-sided error is available.

If logarithmic resolvents/theta ratios are used, L966 is stated for
the diagonal prescribed family only. Justify any off-diagonal
specialization instead of silently importing it, recompute its
parameter-dependent coefficients, and retain both distant-h charges
at h=1/eta_n and h=1/eta_(n+1). The original beta sum offers a way
to test the comparison without such an extension. No omitted-h
estimate or modulus-square replacement is acceptable.

The prior source comparison and its primary citations, exact searches,
recorded failures and inaccessible unused leads are in
[step192's completed review](2026-11-10-prescribed-q-index-recurrence-review-191.md).
This target does not reopen L967/L969/C969a/L971 payment rules or the
L874 heat-contact nomination. L040/L044/L046 supply warnings, not
premises paying this difference. Reproof of a sourced recurrence is
unnecessary; only the changed-parameter estimate needs specialization.

## Continuation and abandonment

One bounded analytic attempt is approved in scope after the separate
approval. Continue only on a proof of the full all-n threshold or a
rigorous counterexample/obstruction to it under the exact stated
hypotheses. Distinguish a model-geometry obstruction from failure for
actual Xi if a model is used; a model is no RH counterexample.
An exponential-in-n loss, sign-free identity or finite numerical
prefix does not settle this test. If the bound cannot be paid, preserve
the precise failed inequality and stop rather than varying eta or
loosening the threshold repeatedly.

No proof, new inequality, recurrence or mathematical script was created
in writing this assessment. Expected classification for an eventual
successful elementary specialization is REPRODUCTION; no originality
is certified. Full matching Mathlib coverage is not checked and remains
unknown; no Mathlib theorem is imported. No cross-notebook input.

## Separate source approval and URL repair — step193

10 November 2026. This is the separate literature-only approval of the
unchanged TARGET, repairing the missing direct source URLs. The earlier
search/comparison and failure screen are reused; no new search for novelty
or different target is needed. LITERATURE_REASON: supervisor recovery
requires direct source URLs in the ready assessment; verify the essential
Cauchy/Taylor passages rather than repeat recurrence discovery.

Read [DLMF1.9.30](https://dlmf.nist.gov/1.9.E30) and
[1.9.31](https://dlmf.nist.gov/1.9.E31), including the preceding
hypotheses: continuity on and inside a simple closed contour, analyticity
inside, and an interior evaluation point. The formulas give the function
and its positive-order derivatives by contour integration. Read
[1.10.1](https://dlmf.nist.gov/1.10.E1) and its surrounding statement:
analyticity in the open radius-R disk gives the Taylor expansion there
with convergence radius at least R. The displayed version is1.2.8,
released15 September2026. These are tool imports, not a two-eta inequality.
L964(5),(9)-(10) already places its function and Cauchy circle strictly
inside its analytic domain; reuse those established local bounds.
No reproof of the standard formulas is warranted. The new denominator
comparison, real signed sum and all-n constant remain research obligations.

Read [Xiao v1](https://arxiv.org/pdf/2006.13103v1), Theorem3.2,
its derivation on p4, and Corollary3.3 with the complete proof on pp4-5.
The recurrence applies to ordinary Li coefficients for n>=3 and retains
a zero-sum forcing term. The corollary explicitly assumes RH; its proof
uses unit modulus of the zero-dependent power. Conjecture3.4 remains a
conjecture. No statement compares two eta parameters. This confirms the
previous scope comparison; it supplies no new mathematical evidence for
or against the proposed loss threshold.

The source-comparison/failure screen in step192 remains applicable:
L964's single-eta one-sided estimate cannot be subtracted to obtain this
bound; L967/L969/C969a/L971 and the heat-contact stops concern other
payment rules. None is silently reopened. L024/L026, L964/L966 are the
essential local inputs; L968 is downstream only. Full matching Mathlib
coverage remains unchecked/unknown. No new lemma, proof, mathematical
script or mathematical conclusion was produced. The source-access issue
is repaired; SPECIALIZE is ready for the exact saved mathematical test.
Outcome of this repair: STALLED in mathematical evidence, LITERATURE,
NOVELTY_UNCHECKED. No mathematical exploration counter is reset here.
