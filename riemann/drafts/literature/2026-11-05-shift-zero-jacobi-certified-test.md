# Fixed central Jacobi feasibility — calculation nomination

TARGET: Test Holland's fixed n=0,d=5,D=B_J/2 matching construction with rigorous gamma(0..4) enclosures, certifying one admissible exact parameter solution and five simple positive model roots or recording a qualified obstruction.
CHECKED: 2026-11-05
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse step474's exact-system, stronger-root-regime and validated-input comparison; no changed degree, family, fixed D or coefficient convention.
SOURCE_EVIDENCE: https://arxiv.org/html/2608.08682v1 (37)–(38),(49)–(52),(66)–(69), Lemma6.2/proof; https://arxiv.org/pdf/2309.10970v3 Proposition4.15(ii), Proposition2.17/proof; https://arblib.org/acb_poly.html Gamma/Zeta-series contracts. Reaccessed 2026-11-05; full prior comparison in 2026-11-05-shift-zero-jacobi-matching-feasibility.md; no numerical input accepted.
COMPARISON: Known matching identities, ball Taylor evaluation, Jacobi/convolution theorems and Banach/IVT certificates cover this conventional finite calculation; no central existence theorem or prescribed multiplier bound is imported.
GAP: All five actual coefficient enclosures, first-stage admissibility, exact solution, degree-dependent roots and implementation verification remain unpaid. Failure of a sufficient condition is not general nonfeasibility.
REASON: Decide an independent finite representation prerequisite before considering residual or growing-degree control; reproduce/specialize known methods, with no novelty claim.
SCOPE: Exactly the bounded test specified in step474; three coefficient precisions, one candidate parameter box with two refinements, and no change of D, degree or family. Step475 supplies the separate literature approval and direct-source repair; research is deferred to the next invocation.

Read the completed [source assessment](2026-11-05-shift-zero-jacobi-matching-feasibility.md),
particularly "Bounded continuation and decisive evidence". Essential inputs:
L019/L021 actual moment normalization, L776 ordinary coefficient definition
only; Holland (37)–(38),(51)–(52),(66),(69), and the cited finite-free/Jacobi
hypotheses. L018 supplies the completion identity if direct Taylor jets are
used. gamma(j)=8*4^j*j!*a_j; source degree n=5 must not be confused with
Holland shift n=0. No Fredholm norm result, RH premise or actual-root sign
is needed. L564 is not an accepted coefficient certificate.

Retain the broader Proposition4.15(ii) comparison and repeated-root caveat.
Prefer either the classical strict Jacobi hypotheses plus mesh theorem,
or five disjoint positive sign brackets for the exact model. A validated
solution needs an exact existence certificate, not approximate residuals.
Actual coefficients through index5, residual multiplier bounds and all
growing-degree central signs remain unresolved and outside this action.
Success or an obligatory parameter obstruction informs this fixed model
only. Nonconvergence, insufficient precision or failure of sufficient root
conditions is inconclusive and must be reported as such. Store full evidence
and actual/required bounds; print a compact result and artifact path.
Mathlib matching coverage is unchecked. No new general theorem is requested.

## Separate source approval and URL repair — step475

The supervisor reported a missing direct source URL in this assessment.
The prior assessment already linked the sources; this repair makes the
ready target independently traceable. No target, hypothesis or bounded
calculation contract changes. This is process repair, not mathematical
progress or a new literature discovery.

Reaccessed [Holland v1](https://arxiv.org/html/2608.08682v1), dated
9 August 2026: (37)–(38) define the first-stage parameters; (49)–(52)
specify the quotient system and fixed D; (66)–(69) define the model.
Read Lemma6.2's complete quotient-induction proof. Its matching claim
requires an exact solution; Lemma6.1's existence statement applies only
eventually in the shift and supplies no shift-zero certificate. Reuse
step474's comparison and normalization; no manuscript-wide validation.

Reaccessed [Martinez-Finkelshtein–Morales–Perales v3](https://arxiv.org/pdf/2309.10970v3),
2 May 2024, printed p.33, Proposition4.15(ii): positive denominator
parameters and each paired numerator exceeding its denominator by
degree minus two imply positive roots. Retain the prior degree-five
specialization and its simplicity caveat. Proposition2.17 and its full
mesh proof, printed p.15, require positive-rooted factors; strict mesh
must be established separately. These are sufficient regimes, not a
complete classification or a central parameter existence theorem.

Reaccessed [Arb2.23.0 Gamma-series contracts](https://arblib.org/acb_poly.html#gamma-function)
and [Zeta-series contracts](https://arblib.org/acb_poly.html#zeta-function),
including Euler–Maclaurin error-bound routines and the Hurwitz parameter
convention. This is archived documentation; an implementation must record
its actual library version. Availability, successful coefficient enclosure
and exact-solution validation remain untested. Reuse the earlier assessment
for the completion expansion and fallback; no new numerical claims.

The saved target is approved as SPECIALIZE for one conventional finite
calculation. All-degree mixed positivity remains the main gap. A successful
model is only a possible starting representation for later residual work.
Continue on a certified exact solution and five simple positive roots;
stop the specified construction only on an obligatory strict obstruction.
Sufficient-condition failure, an excluded box or nonconvergence is
inconclusive. No lemma or mathematical script was written in this review.
