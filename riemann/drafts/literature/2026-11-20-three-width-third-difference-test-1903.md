# Fixed three-width output: one third-difference test1903

TARGET: Attempt to certify a negative third Hausdorff difference D_3=1-3*m(1)+3*m(2)-sum_i a_i*exp(-B_(sigma_i)(3)) for C034k's fixed widths (1,3/2,2) by analytic bounds, stopping this diagnostic if negativity is not certified.
CHECKED: 2026-11-20
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Review1903 completed signed-mixture positivity, complete-monotonicity and Hausdorff finite-difference comparison for the fixed output; queries, inspected cases and scoped duplicate/failure checks are in drafts/literature/2026-11-20-three-width-interpolant-output-sign-review-1902.md. No theorem deciding this exact sign was located; no novelty claim.
SOURCE_EVIDENCE: Diaconis--Freedman, The Markov Moment Problem and de Finetti's Theorem: Part I, author version15June2003, equation(1) pp1-2, Theorem1 and Lemma1(a)/complete proof p2, https://www.stat.berkeley.edu/~census/631.pdf ; reuse Mimica2015 Proposition1.4(i),(iv)/1.8 and notes1552/1562/1894/1898. Review1903 directly inspected the needed finite-difference case and revisited the Laplace statements/proofs; no density or moment theorem is needed.
COMPARISON: The cited Hausdorff necessity supplies a bounded nonnegative test after x=exp(-u). C034k already fixes the exact weights, mass and observations1,2; C032q supplies signed integration, C032j/C033l the all-s transform and C032m common analytic bounds. None supplies D_3's sign. C034k's determinant/cofactor bounds may support an analytic combined estimate; their j=1,2 observation bounds do not cover3 without proof.
GAP: Justify the finite signed test identity and obtain a strict negative enclosure for this exact D_3, retaining cancellations and the whole divisor. No sign, scalar values, extension of quantitative j=1,2 bounds to3, affordable evaluator, positive factor or full-class conclusion is assumed.
REASON: One density-free necessary-condition specialization probes the fixed output beyond its fitted observations. The source coverage is ready, but this new nomination requires a separate approval turn before execution. No further browsing of unchanged general criteria is needed after approval.
SCOPE: Exactly C034k's existing coefficients, widths1,3/2,2 and residual; one test f(u)=(1-exp(-u))^3, equivalent to the n=3,j=0 case of the cited formula. Analytic estimates only; no scalar-quadrature implementation, changed support, additional observations/tests, coefficient refitting or claim of full positivity.

## Exact input and imported case

Use the unique exact solution of C034k/audit1879, including its
quantitative determinant/cofactor formulas and paid finite count.
Use C032q's signed-output convention Q=sum_i a_i*nu_(sigma_i).
The nominated test is f(u)=(1-exp(-u))^3, 0<=f<=1 on [0,infinity).
The source's forward-difference convention is Delta t_j=t_(j+1)-t_j;
its n=3,j=0 quantity is t_0-3*t_1+3*t_2-t_3. Import Lemma1(a),
not the all-orders converse or the density-constrained Markov theorem.
The research step must explain its bounded signed integration and
substitute only the already established mass and matching observations.
This specification evaluates neither that integral nor its sign.

No endpoint moment, density, absence of a zero atom or positive quotient
is required. This test vanishes at zero, so a negative zero atom alone
need not be detected. C033j's full signed factors are available context,
not an assumption that positivity reflects through nu_1. C034p's
positive-quotient stop is a contrast, not a premise for this diagnostic.

## One bounded analytic attempt

Start with the exact cofactor/common-denominator form of the fixed
solution, preserving its determinant sign and normalization. Seek a
rigorous signed bound on the combined expression; do not replace tiny
differences by rounded weights or independent unqualified asymptotics.
Only existing C034k allowances and the all-s identities/analytic
majorants in C032j/m/q and C033l are licensed inputs. Any quantitative
bound needed at3 is unpaid application work, not a source import.
Do not redo the cap proof, rebuild the interpolation system, run the
stopped C033x/attempt1798 scalar evaluator, or retry optional sources.

Success threshold: a rigorously negative upper bound D_3<=-epsilon
with a specified epsilon>0, which rejects only this fixed output.
A rigorous nonnegative value or a bound containing zero is inconclusive
for positivity. If one analytic attempt cannot certify negativity,
save the exact missing comparison and park this diagnostic. Do not
increase n, scan s or h, or manufacture a favorable-condition lemma.

This is development using a classical necessary condition, not a
creative central mechanism. Its possible downstream use is to reject
one candidate building block for sign-constrained width approximation.
Even a rejection supplies neither an uncapped-cone separator nor RH.
Uniform accuracy, full cancellation, moments, signed height and actual-Xi
realization remain independent. A creative route still lacks an
operation preserving the width span with a decisive sign/error test.

Retain C034k's actual divisor/conjugation and all multiplicities, no
ordinate zero, strict strip and gamma>14, counting, displacements zero
through100 and retained real zero, reciprocal-square tail, heat
positivity/separate fixed-j errors through2, zero drift/killing,
Gaussian half-variance and both fixed-v1 qualifications. No external
source-wide or finite-zero validity is independently certified here.
Full matching Mathlib coverage remains unchecked/unknown. No new
mathematical result or script is produced by this nomination.
