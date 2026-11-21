# Complete-kernel signed bulk specialization — proposed bounded test

TARGET: Specialize Vanlessen Theorem2.4(b) to C997s's two original windows and obtain a signed leading endpoint formula with a uniform absolute remainder at z_star and the full band, retaining both beta terms and the constant subtraction.
CHECKED: 2026-11-11
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the completed review405 step406 growing-argument Laguerre/Plancherel-Rotach and short-window Fourier source comparison; the target is its identified finite-window specialization, not a new source-discovery question or novelty claim.
SOURCE_EVIDENCE: M. Vanlessen, arXiv:math/0504604v2 (29 August2005), https://arxiv.org/pdf/math/0504604v2 and https://arxiv.org/html/math/0504604v2 ; Theorem2.4(b)/(2.13), Remarks2.5-2.7, Theorem3.32 and Section5.2 Proposition5.1/(5.5)-(5.6), with normalization(5.1); primary statement and relevant proof inspected in review405 step406. DLMF Table18.3.1, https://dlmf.nist.gov/18.3#T1 , supplies Laguerre normalization. Standard named Taylor theorem with integral remainder and the fundamental theorem of calculus suffice for the proposed finite-window calculation; their quantitative hypotheses must be checked locally.
COMPARISON: The source supplies the signed bulk polynomial resource and additive algebraic error; it does not state the notebook's integrated endpoint formula, which must retain two windows, two exponentials and K's exact -1. No reproof of the general asymptotic theorem is justified. No exponential E_n bound, uniform relative error at oscillatory zeros, growing truncation or derivative estimate for the source error is supplied.
GAP: Translate the positive-leading orthonormal polynomial to degree n+1, alpha=2, with the correct sign/norm, integrate only its explicit leading expression, and bound the source error absolutely without differentiation; pay all endpoint, subtraction and coefficient-cap costs before interpreting the result toward E_n.
REASON: An accessible signed bulk primary theorem covers the proposed specialization's essential source needs; finite-window integration is the identified remaining calculation. Newly written in step406, this assessment received separate literature approval in step407 with direct source URLs repaired; no expansion has been derived or audited.
SCOPE: Fixed I=[7/4,9/4], z_star=1+i/8, full closed E=[15/8,17/8], integer n>=64 subject to the source's possibly larger existential onset, original gamma_j and cap exp(sqrt(n)); C997c(1),(4)-(6) and C997s's complete kernel. Fixed-order leading formula and uniform absolute error only, without an effective numerical constant or onset promise.

The completed source evidence, hypotheses, branches and access record are
in [review405, step406](2026-11-11-signed-bulk-kernel-review-405.md).
Reuse those inspected results. Further literature would need a changed
hypothesis or a specific essential unread source; do not browse them again
merely to approve the continuation.

## Separate approval and URL repair — step407, 11 November 2026

The recovery gate reported missing direct source URLs in this assessment.
The URLs above now identify the versioned primary theorem and normalization
table directly. Reopened only the source hypotheses in Section1,
Theorem2.4(b)/(2.13) and its uniformity statement, Theorem3.32/(3.110),
Section5.2/(5.5)-(5.6), and the DLMF Laguerre row to confirm the saved
comparison. Reused review405's remaining inspected evidence, applicability
screen and failure comparisons; no broadened search or new calculation.
The unchanged bounded target is approved as SPECIALIZE. This is a process
repair (STALLED), not new source coverage or mathematical progress.
The source's two-component additive error and existential onset remain
essential qualifications. Full matching Mathlib coverage remains unchecked.

The main gap is L030-L032/C032a actual-Xi positivity, L966/L968 signed
forcing and L984(H). The distinct local point-bridge objective E_n in
C997s remains unresolved. A signed complete-kernel formula could expose
which endpoint oscillations a later primal/dual construction must cancel.
It would supply neither that construction nor its exponentially small
residual. This is a reproduction/specialization, not a creative claim.

Use N=n+1 for the source degree and a distinct variable x for its rescaled
argument; the source MRS scale for Q(t)=t is 4N. Review405's applicability
screen places BOTH physical windows in a fixed compact interior of(0,1).
The frequency z is not the Laguerre argument. Keep the source's upper-side
boundary convention and both source cosines when controlling its additive
error; never divide by an oscillatory leading term. Retain the exact sign
and squared norm from DLMF Table18.3.1 when translating p_N to L_N^(2).

The allowed calculation is one uniform leading endpoint formula and its
absolute remainder, obtained by integrating the explicit smooth amplitude
and phase over intervals of bounded physical length. A Taylor expansion
of that EXPLICIT leading expression may be used with checked derivative
bounds. A pointwise O term must instead be integrated by its absolute
envelope; it may not be differentiated, treated as analytic with unproved
bounds, or assigned cancellation. Keep all four physical endpoints
cn,c(n+2),n,n+2; both beta terms; the exact constant-subtraction integrals;
and the dependence on Im(z). Uniformity must include c's and E's closed
endpoints. No exchange of an infinite series and an integral is licensed.

Success for this intermediate test means a rigorously normalized signed
endpoint formula with a finite, n-independent absolute-error constant
beyond one existential onset, with all dependence on c,z and n displayed.
Report the remainder at the original exp(sqrt(n)) coefficient cap and
compare it honestly with exp(-n/64). No effective onset of 64 is assumed.
A larger algebraic-envelope error can still complete this intermediate
formula but does not pass the E_n threshold. Do not extend it into an
exponential-certificate claim without a separate paid cancellation input.
If no uniform absolute formula follows, record that precise obstruction
and stop this specialization instead of increasing numerical degrees or
replacing the kernel by its absolute spectral envelope.

The fixed-order source supplies no estimate uniform in an increasing
truncation order. A proposed exponentially accurate expansion would leave
this assessment's scope and require REVIEW_REQUIRED before dependent work.
C997x/y/z, C999c, spectral-tail341 and paid-leakage372 remain comparisons
on their recorded scopes, without a global impossibility claim. E_n,
C997a(8), selected/both-sign transfer, reconstruction, complements,
regulators, L993, L984(H), forcing and Xi signs remain unpaid. Full
matching Mathlib coverage is unchecked. No cross-notebook input.
