# Signed Green product test: harmonic-replacement stop

The full application and quantitative comparison are canonical in
[L501](../lemmas/L501-signed-green-reduction-and-harmonic-cancellation.md).
This is the bounded test at delta=log log T/log T authorized by the
saved signed-curvature assessment. It has not received separate critical
audit, and no new zero-density or mixed-moment theorem is claimed.

WHY IT FAILS: combining both curvatures cancels the completion exactly,
but also annihilates every harmonic prime-log main term. The surviving
signed mixed error is independent of that replacement. The mean-amplitude
part has a sufficient power saving; the remaining centered amplitude/count
covariance has only the losing bound in L501 (4). Declaring the log error
small would insert an unproved weighted estimate. Rewriting it as a count
or repeating Cauchy--Schwarz does not supply one. Thus this implementation
does not reach the target, although neither the desired weighted bound
nor RH is refuted and no lower bound on the actual covariance follows.

Park the identity-plus-harmonic-replacement implementation. Reopening
needs an independently justified nonharmonic mixed-error estimate or a
different mechanism. A separate source review of nonnegative analytic
majorants in the weighted one-level statistic is nominated in
`drafts/literature/2026-10-30-positive-analytic-window-majorant-feasibility.md`.
That feasibility question has no approved answer and assumes no weighted
zero estimate. The detector, count-only and Blaschke stops retain their
original scopes; they are not global bans on these subjects.
