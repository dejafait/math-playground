# Source coverage: one further prescribed-response correlation

TARGET: Assess whether the actual response-weighted second moment E[W(t)^3 f(t)^2] separates L423's fixed k=13,14 mixture.
CHECKED: 2026-10-17
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 200 searched mixed-vertical-line zeta moments, the 5/2 weighted second moment, sixth-power right-line weights and twisted Dirichlet-polynomial mean squares; read Young's primary (2.1)--(2.3), Lemmas 4--5 and both off-diagonal orderings, and Bettin--Chandee--Radziwill's primary (1.1)/Theorem 1. Scoped L419/L421/L422/L423, their October-16 assessments/audits and October-16/17 failure/history searches contain no completed W^3 comparison; this does not establish novelty.
SOURCE_EVIDENCE: Young, A short proof of Levinson's theorem, Arch. Math. 95 (2010), 539--548, DOI 10.1007/s00013-010-0199-9, (2.1)--(2.3), Lemmas 4--5/(4.1)--(4.5), pp. 540, 542--543, https://www.math.ntnu.no/emner/MA3001/2020v/2022v_MA3004/Young.pdf ; Bettin--Chandee--Radziwill, arXiv:1411.7764v1 (28 November 2014), (1.1), Theorem 1, pp. 1--2, https://arxiv.org/pdf/1411.7764v1 ; reused audited L381 (7),(9) and sharp-tail argument, L389 (3), L419 (3), L421 (4)--(9), L422 and L423.
COMPARISON: Known fixed-twist second moments cover each finite head of zeta(5/2+it)^3 with the same order-zero critical factor; existing sharp bracketing and scalar-norm tail machinery cover the required type of full-response passage. Neither source evaluates the specified law difference. L423 fixes its mixture by W^2 only; the W^3 coefficient comparison and its complete-law error remain mathematical obligations.
GAP: Write the changed full-response specialization, retain all three law components and the full covariance correction, and certify either a strict leading-log coefficient mismatch for L423's unchanged fixed mixture or an honest inconclusive/matching result. No mismatch, new coefficient formula or numerical value has been established here.
REASON: Essential theorem and tail scope is covered for one bounded calculation using known inputs; no new general theorem or reproof is needed. This literature-only turn approves the unchanged exact target for RESEARCH / REPRODUCTION, without deriving its coefficients or changing lemmas or mathematical scripts.
SCOPE: Sharp dt/H average on [H,2H], real H tending to infinity, actual ordinary order-zero f, W=|zeta(5/2+it)|^2, and exactly L423's H-independent k=13,14 mixture and all its components. No growing head in H, conditional independence, new covariance tuning or global critical-function realization is covered.
COVERED_TARGET: Assess whether the actual response-weighted second moment E[W(t)^3 f(t)^2] separates L423's fixed k=13,14 mixture.
LITERATURE_REASON: The changed observable W^3 f^2 lies outside the saved core/tail assessment and the prior W^2 calibration target; essential exact coverage must be checked before a new calculation.

Here W(t)=|zeta(5/2+it)|^2, f is L405's actual ordinary normalized
critical function, and E=H^(-1) integral_[H,2H]. Compare the coefficient
of log H for the actual function with the complete L423 law, keeping
its single fixed mixture, actual response, uniform height marginal,
high/intermediate components and all full-response tails. Do not assume
a conditional moment law, RH or an exact finite-H asymptotic.

Essential local inputs for the proposed review are L419, L421, L422,
L423, the audited source/tail arguments they actually use, and the
saved assessments for the W^2 correlation and fixed mixture. The old
single-power failure is retained; it is not a proof about this mixture
or the changed observable. The Gaussian core/tail stops are independent
of this arithmetic correlation test. A mismatch, if eventually proved,
would reject only this specified selected-information law after adding
one necessary correlation; it would not establish clipping, actual
critical-function realization, L413's full-error margin or RH.

## Completed review — step 200

The main gap is global mixed positivity. The intermediate target is one
additional necessary response/critical covariance test, not a renewed
evaluation of L426's integral. A mismatch could constrain the specific
selected-information counterlaw and guide a later covariance design;
it would not undo L421/L423 on their original lists. The strict target
is a nonzero difference between leading coefficients, certified by
disjoint rigorous intervals with some explicit rational gap delta>0.
Both actual and law remainders must be o(log H). Neither coefficient
nor such a gap is calculated in this review.

### Primary input inspected and applicability

Young's published primary PDF was retrieved on 2026-10-17. Its weights
are smooth, between zero and one, supported in [T/4,2T], with j-th
derivative O_j((T/log T)^(-j)). Lemma 5 requires positive twists h,k
with hk<=T^(2 vartheta), vartheta<1/2, and shifts O(1/log T).
It retains both functional-equation diagonals hm=kn. Read Lemma 4's
auxiliary kernel and gamma ratios, and Lemma 5's complete proof on
pp. 542--543: repeated integration by parts treats both hm>kn and
kn>hm using logarithmic separation. The auxiliary expression is singular
at zero total shift; use the combined holomorphic evaluation already
audited in L381, rather than substitute zero into separate terms.

At scale T=2H, fixed-head twists eventually meet the length bound.
L381's fixed-shape smoothing weights fit this support and derivative
scale. The changed observable needs no critical derivative, gamma
carrier in the weight, or shift of size two. Reuse the order-zero
specialization L381 (7); there is no reason to reprove Young's theorem.

The stronger optional comparison is S. Bettin, V. Chandee and
M. Radziwill, *The mean square of the product of the Riemann zeta-function
with Dirichlet polynomials*, arXiv:1411.7764v1, (1.1), Theorem 1,
pp. 1--2; published J. reine angew. Math. 729 (2017), 51--79,
DOI 10.1515/crelle-2014-0133. The inspected theorem assumes smooth
phi supported in [1,2], coefficients a_n=O_epsilon(n^epsilon), and
length N=T^vartheta with vartheta<17/33. Its main sum has factor
a_d conjugate(a_e)/lcm(d,e), multiplying the integral of
log(t gcd(d,e)^2/(2pi de))+2gamma; its error is
O(T^(3/20+epsilon) N^(33/20)+T^(1/3+epsilon)). It covers fixed heads
by zero padding at a small fixed exponent. Its stronger length range
is unnecessary. It supplies no comparison with the artificial law.
Use the already audited Young route for sharp endpoint brackets.

### Changed tail and law scope: obligations for the calculation

L389 (3) identifies f squared with the critical zeta modulus squared,
including at zeros. L419 already establishes absolutely convergent
Dirichlet multiplication for every fixed integer power on Re s>1.
Thus the order-three right-line series is within the assessed class;
this is a theorem-domain check, not an evaluation of its weighted mean.
Apply L381 (7) only after fixing a finite head. Preserve every rational
twist and gcd collision when expanding its complete modulus square.

The mathematical attempt must write the order-three analogue of L422's
tail estimate: use the complete positive divisor-series tail on Re s=5/2,
its uniform sup norm, and the N-independent scalar bound L381 (9).
It must establish convergence of the resulting coefficient, rather than
infer it from finite-head moments alone. Bracket the full nonnegative
integrand at both sharp endpoints. The order is H to infinity at fixed
head and smoothing width, then removal of smoothing, then head removal
with uniform normalized error. This scope requires no growing-head
theorem, stronger zeta moment, prime-phase independence or new derivative
tail result. These obligations follow the audited L422 method; their
changed specialization has not been proved during this source review.

For the law, import the exact alpha and g0 of L423 (5); do not refit alpha
using the new observable. L423's already proved fixed response bounds,
L421 (4),(6) for unnormalized high/intermediate second integrals, and
L423 (9)--(10) for the bulk normalization and full matrix correction
are the relevant inputs. The order-three response weight is bounded.
The later proof must retain the bulk mean and the entire O(sqrt(log H))
correction, and show all omitted component contributions are lower order.
Use L419 (3) at the necessary fixed powers for the remaining bulk
average. No new Schur--Horn application or reconstruction of the law
is needed: this step tests an existing audited law.

### Duplicate/failure comparison and bounded test

Read L422's coefficient/tail proof and audit, L423's exact mixture and
complete-law comparison, L419's fixed-power moments, and L421's
component/correction passages with their audit qualifications. Reused
the step-164/166 fixed-twist coverage and step-169/171 mixture coverage.
The scoped search of their proofs, assessments, audit drafts, October-16/17
histories and failure records found only step 199's new W^3 proposal.
The single-power stop is recorded in
`ATTEMPTS/2026-10-16-fixed-g0-added-response-correlation.md`.
Its all-k conclusion concerns W^2 and cannot reject the fixed mixture
for W^3. The C426b/C426c core/tail stops remain parked and unchanged;
they neither imply nor preclude this coefficient mismatch.

Search queries were `zeta mixed moment "5/2" "second moment" Dirichlet
polynomial`, `"mean square" "zeta" "Dirichlet polynomials" Bettin
Chandee Radziwill theorem 1`, and `"zeta" "different vertical lines"
moments sixth power`. The two primary statements above are the adequate
general results found. Long-polynomial moment/conjecture hits were not
inspected as theorem inputs and are not essential leads. No failed
search certifies novelty or licenses a conditional higher moment.

For one bounded next calculation, first justify the changed actual and
full-law coefficients symbolically from these inputs. Use the existing
Euler moment/tail method for all constants needed by the unchanged
mixture, extending coverage through fixed power 17 where required.
Propagate alpha's dependence on the W^2 constants rigorously; a decimal
fit or independent arbitrary alpha is insufficient. A finite-prime/local
series calculation may start at cutoff 200 and order 40 and refine once
to cutoff at most 1000 and order at most 80. Write a full rational
certificate with actual and required bounds, all tail bounds and failures.
Do not silently reuse L422's order-two local factor for the new actual
coefficient; its order-three factor and omitted-prime bound need proof.

Continue this diagnostic as a separator only if the complete analytic
specialization and a strict rational gap both pass. If exact agreement
is established, stop it as a separator. If intervals still overlap at
the stated cap or an analytic obligation fails, record inconclusive or
the precise obstruction and stop this bounded test; do not claim equality,
nonseparation, failure of the actual moment or an RH consequence.
No alternative mixture or higher observable is approved by this scope.

No new lemma, coefficient formula, mathematical script or certificate
verification was produced. Full matching Mathlib coverage is not checked;
unknown availability is not evidence of absence. Completed outcome is
EXPLORATION / LITERATURE / NOVELTY_UNCHECKED, actual task type
literature_comparison. This is fresh coverage for a changed observable,
not progress beyond the checked moment sources. Mathematical exploration
usage stays 0 of 3. The unchanged TARGET is now ready for one separate
RESEARCH / REPRODUCTION calculation; no essential source blocker remains.
