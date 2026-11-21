# Actual Jensen moving-saddle complement: assessment1362

TARGET: Establish or refute uniform o(|Z_d(q)|) control of the lower-semicircle complement of Ono v1's Gaussian saddle interval for K=Q and d^(-1/2)<=q-q_e(d)<=2*d^(-1/2), using oscillatory integration by parts near the coalescing endpoint and the fixed-angle exterior bound.
CHECKED: 2026-11-17
DECISION: EXPLORE
SEARCH_EVIDENCE: Review1362 searched exact-identifier saddle remainder and unshifted Jensen nonstationary terminology, inspected Ono's exact remainder proof, and compared C019d's fixed-window annulus with assessments1344/1354/1358 and stops1345/1355/559. No inspected theorem supplies the specified complement estimate; this bounded search does not certify novelty.
SOURCE_EVIDENCE: Ken Ono, An Asymptotic Jensen–Pólya Criterion for GRH, arXiv:2610.38870v1, 28 October2026, https://arxiv.org/html/2610.38870v1 : Lemma7/(3.3)-(3.11), Lemma8/(3.12), Lemma9/(3.13)-(3.16), Corollary10/(3.17)-(3.20) and full endpoint/local proof, Lemma11/(3.21)-(3.24), Lemma12/(4.2)-(4.3) including gamma remainder, Lemma13/(4.4)-(4.9) with whole-circle and Euler-product derivative proof cases, Lemma14 with full integration-by-parts proof, Proposition15/(5.2)-(5.5) and full complementary-circle assembly inspected in review1362; (2.9) reused from1358.
COMPARISON: Proposition15 imports the local Gaussian estimate but its absolute complementary bound does not vanish on the proposed band. The source's small n-independent real-part gap is not a cancellation estimate. C019d covers a different fixed x-window and excludes the endpoint-to-saddle gap; its algebra is precedent, not a matching theorem. Known integration by parts is the tool; only this quantitative application requires work.
GAP: Uniform control of the exact complex phase derivative and amplitude on both retained intervals, including the endpoint side of the saddle and every boundary term, is missing. No estimate below |Z_d|, growing barrier count, effective onset or far-end closure is established.
REASON: Source coverage for one bounded complementary-integral test is sufficient: exact phase, contour, saddle neighborhood, nonzero Gaussian scale and standard finite integration-by-parts identity have been inspected. The hypothesis checks and bounds are mathematical work deferred to a separately approved turn. No generic Airy theorem or uninspected external asymptotic is needed for this test.
SCOPE: Fixed K=Q, integer d tending to infinity, exact source r(d,q), q_e(d), Lambda, T, P_d=d!/d^d and principal D_q square root; only the lower-semicircle complement defined below. No change of contour, effective d threshold, root count, extension to all q, global hyperbolicity, source-wide audit or Mathlib artifact verification. Newly ready assessment needs separate supervisor approval.
LITERATURE_REASON: Review1362's permitted comparison identified an omitted moving band and a specific failed absolute-error bound; this assessment prepares its different oscillatory complement test while reusing the existing local and fixed-window coverage.

## Exact proposed observable and discriminating test

Keep the source notation

    theta_q=-2 alpha, ell_q=epsilon_0 min(alpha,cos(alpha)),
    E_q=[-pi,theta_q-ell_q] union [theta_q+ell_q,0],
    P_d=d!/d^d,
    Z_d(q)=P_d a_q(theta_q) exp(d h_q(u_q))/sqrt(2 pi d D_q).

The two intervals have their ordinary increasing angular orientation.
Define the proposed remainder, with no new contour or omitted connector,

    R_d^-(q)=P_d/(2 pi) integral over E_q
                     a_q(theta) exp(d h_q(r^2 exp(i theta))) dtheta.

Test exactly

    sup over d^(-1/2)<=q-q_e(d)<=2*d^(-1/2)
                     |R_d^-(q)|/|Z_d(q)| -> 0.

The hypotheses and formula are imported source definitions; the asserted
limit is an unproved research target. Retain all dependence on Lambda
and q_e(d). A successful bound must display a vanishing majorant uniform
on the whole band, including the q-endpoints. An eventual bound <1/4
would be a useful weaker milestone, recorded honestly if the full target
is not obtained. A lower bound or counterexample refuting the limit
would be an informative negative. Failure of one majorant alone is
only a failed proof mechanism, not refutation of the limit.

An allowed plan is to keep a fixed 0<theta_0<=1/10, pay the distant
part with source Lemma8's concavity and Lemma13's whole-circle amplitude
bound, and test finite complex-phase integration by parts on the two
remaining pieces outside the source saddle neighborhood. Verify the
neighborhood and split lie in the stated ranges at a common onset.
The endpoint-side piece ending at zero must be included. Prove the
phase derivative never vanishes on each divided interval before using
its reciprocal; keep its actual angular second derivative, the actual
amplitude derivative, all boundary terms and exponential real-part
control. Do not transfer C019d's beta>=2 alpha estimates onto beta<alpha.
Use the source identity of Lemma14, not a reproof of general stationary
phase. Proposition15's local proof can be cited only after verifying
n_q>=1 and its unchanged hypotheses on this band.

No missing essential source is being deferred to research: the exact
phase, saddle equations, concavity, analytic amplitude factorization,
Euler-product bounds and finite integration-by-parts identity are
inspected. Their new uniform specialization is the open mathematical
obligation. If the test needs a different external theorem or a changed
band, save partial reasoning and mark the changed target REVIEW_REQUIRED.

## Relevance and limits

Main gap: L030-L032/C032a actual-Xi all-degree positivity; this route
still lacks every-degree Jensen hyperbolicity. Essential local inputs
are L018/L021 for the actual family and C019c/C019d/C019g only for
conventions and earlier fixed-window calibration. Their compact-window
conclusions are not hypotheses at the new band. Use the named source
statements directly for geometry/local integration. C019f's Airy limit
is comparison context and not a mathematical input to this estimate.

Plausible downstream use is to combine a vanishing complement with
the source local Gaussian formula and its exact conjugation, then
separately validate phase barriers from (6.2) on a growing omitted
family outside I_d. A quantitative phase-span estimate, integer hitting
argument and exact nonoverlap must still be proved before adding roots.
The larger Q-end loss remains independent; this target alone cannot
close RH or improve the overall source deficit order automatically.

Continue if explicit uniform bounds control the endpoint side, outer
side and boundaries on |Z_d| scale. Abandon this implementation on a
proved obstruction, or park it if its tested derivative/amplitude bounds
do not give a vanishing error; name the failing term and a materially
new input before repetition. Preserve stops1345/1355/559. This uses
established oscillatory cancellation in a changed moving regime and
is development, not a claimed creative invention. No justified creative
global mechanism is ready; omitted far-end signs remain a blocker.
Full matching Mathlib coverage and source formal artifacts are unchecked.
