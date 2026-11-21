# Tilted full-theta first-variation nomination1716

TARGET: Derive and test the exact first tilt variation of centered finite-Jacobi spectral skewness for the full theta measure, retaining the outer recurrence coefficient and the actual cubic matching normalization.
CHECKED: 2026-11-19
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the completed bounded review1716 and its exact-family, Toda, varying-recurrence and local failure comparisons in drafts/literature/2026-11-19-tilted-theta-skewness-source-notes-1716.md. No exact theta first-response statement was located; no originality claim.
SOURCE_EVIDENCE: Walter Van Assche, Orthogonal polynomials, Toda lattices and Painleve equations, arXiv:2202.11017v1, https://arxiv.org/pdf/2202.11017v1 Section1.1 equations(1.1)-(1.4), Section2.1 Lemma2.1 and complete proof/compatibility pp4-6 equations(2.1)-(2.4), inspected again1717; DLMF https://dlmf.nist.gov/18.2#iv equations18.2.10-11 and https://dlmf.nist.gov/18.2.E21 for parity, inspected1717. L019 and C028k provide local applicability and actual power sums; source-notes1716 remains supporting evidence.
COMPARISON: The source supplies the deformation equations, not the centered finite-block response. C028p's zero-tilt parity floor and C028j/k's classical-family infeasibility do not determine this response; probability-variance tilt tests address another observable. No global varying-potential asymptotic is needed.
GAP: The exact finite-block response and actual coefficient normalization have not been calculated. Nonvanishing/sign may remain undecided from existing theta recurrence information; no uniform tilt bound, attainable cubic magnitude or full companion-cost payment is asserted.
REASON: One finite identity and its nonvanishing criterion test whether an odd local coordinate survives the even-reference stop before proposing nonlinear matching. Separate literature approval1717 checks the exact unchanged scope and repairs direct source URLs; no mathematical derivation is performed in either literature step.
SCOPE: Full K of L019; positive measure proportional to exp(theta*u)K(|u|)du on R; each fixed integer d>=3, real theta near0; monic recurrence x*p_n=p_(n+1)+A_n(theta)*p_n+B_n(theta)*p_(n-1), B_n>0, B_0=0. J_d has indices0,...,d-1 and off-diagonal sqrt(B_n), n=1,...,d-1; the semi-infinite recurrence still has B_d>0. Use empirical centered spectral moments M_r=tr((J_d-tr(J_d)I/d)^r)/d and g_d=M_3/M_2^(3/2). No truncation of the measure, spectral-weight substitution, fitted roots, RH, simplicity, determinacy, recurrence asymptotic or uniform-in-d remainder is assumed.

## One bounded mathematical attempt after separate approval

Main gap: L030-L032/C032a actual-Xi positivity, or C028b's unpaid
H_d=o(d). This target addresses only the odd-reference obstruction.
It is a conventional finite Toda specialization, not a creative payment
mechanism. Essential inputs are L019, C028a/b/h/o/p and C028k's exact
centered actual power sums. Use C028j only as a comparison.

Import the source equations with t=theta, A_n=b_n and B_n=a_n^2;
do not reprove them. Justify compact-tilt moment differentiation by the
L019 domination recorded in source-notes1716. Normalizing the measure
does not alter the monic recurrence. At zero tilt the existing even
parity input supplies A_n(0)=0.

Compute the exact first derivative of g_d at theta=0, including the
derivative of its spectral mean and its variance normalization. Retain
the exterior recurrence coefficient in the final diagonal derivative;
do not use finite-Toda isospectrality for a principal block. State the
resulting finite recurrence criterion for zero, positive or negative
response. Check the d=3 endpoint algebra explicitly. No formula for
this response is asserted in this nomination.

Compare this observable's normalization with the actual second/third
centered power sums already proved in C028k. Verify the empirical
division by d and the effect of both signs of a real affine scale.
C028a/h supply the coefficients for d>=3; do not silently import the
classical parameter optimization or its d>=5 feasibility range.

Continuation test: an exact nonzero response proved from the full theta
inputs identifies an adjustable local cubic direction, only. If the
response is identically zero, or its nonvanishing remains undecided
without a new recurrence estimate, record the exact criterion and stop.
No higher derivative, tilt sweep or new asymptotic calculation is part
of this attempt. A numerical grid is not a nonvanishing certificate.

Even a successful response test would not refute uniform vanishing as
d grows, reach the actual cubic magnitude, prove three-match feasibility,
pay lower expansion residuals, or prove H_d=o(d). Those remain independent
gaps. Preserve stops1695/1713, parks1534/1708 and global-source park1716.
Do not change PROOF/DAG unless an actual argument/dependency changes.
Full matching Mathlib coverage is unchecked. No cross-notebook input.

Separate approval should reuse source-notes1716 and check only this
scope, without another broad source search. Intended research after
approval: calculation/standard/high, REPRODUCTION. Approval itself is
literature_comparison/standard/high. No new central creative mechanism
is justified by local skewness adjustability alone.

## Separate source approval1717 — 19 November 2026

Approved SPECIALIZE for exactly TARGET above. Recovery repairs the missing
direct URL in SOURCE_EVIDENCE; the prior source assessment is reused.
This is a process repair, not a mathematical advance or a new search result.

The versioned [Van Assche preprint](https://arxiv.org/pdf/2202.11017v1)
was retrieved successfully. Read Section1.1 and Section2.1, including all
of Lemma2.1's proof and the subsequent coefficient comparison, printed
pp4-6. The low-power orthogonality cases and final norm-ratio case are
both covered. Equations(2.1)-(2.2) distinguish finite terminal-zero
boundaries from the semi-infinite case. Import these equations with
A_n=b_n, B_n=a_n^2 and t=theta; no reproof is needed. The source does not
compute the requested centered finite-block response.

[DLMF recurrence relations](https://dlmf.nist.gov/18.2#iv), equations
18.2.10-11, and [parity18.2.21](https://dlmf.nist.gov/18.2.E21) were
inspected directly; the earlier shorthand reference to all of18.2 is
now made precise. These support monic norm ratios and even parity,
not a skewness estimate. No measure-uniqueness theorem is needed.

Checked L019's positive full kernel and integrable exponential majorants,
C028k's centered actual sums and formal-root qualification, and C028p's
even-reference recurrence. The compact-tilt applicability argument is
already recorded in source-notes1716; reuse it without an asymptotic
claim. The empirical spectral convention is essential: quadrature
weights describe a different observable. Retain B_d, centering, both
affine signs and d>=3. C028k's d>=5 classical infeasibility is only a
comparison. No existing stop proves the tilted response zero.

Coverage is sufficient for one finite identity calculation and its
nonvanishing criterion, even if no sign can be established. Stop at that
criterion if theta recurrence information does not decide it; do not
replace the test by a numerical sweep. Nonlinear attainability, uniform
remainders, actual cubic magnitude and full companion cost remain open.
No new mathematics, Mathlib coverage claim, lemma or script is added.
The next turn may perform the saved calculation as REPRODUCTION; no
further literature review is required for this unchanged target.
