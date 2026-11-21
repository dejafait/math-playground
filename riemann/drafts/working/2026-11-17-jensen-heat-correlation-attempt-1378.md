# Shifted heat-product attempt1378 — working checkpoint

Approved target: attempt (C) for C019k at h=3*pi/log(Y_-), retaining
both actual moving floors and all real-product channels. Coverage is the
unchanged assessment1377 (EXPLORE), supplied at invocation start.

Main gap: L030-L032/C032a actual-Xi all-degree positivity; the present
test can at most supply a signed heat-reference correlation. Its possible
use is opposite-sign pairs; quantitative margins, ordered disjoint pairs,
Jensen transfer, growing root deficit and bulk separation remain open.

Inputs read: C019k in full, C019j hypotheses/normalization and gamma input;
assessment1376's exact (C) and recorded source comparison. Stops1345,
1355 and the exact unshifted-bulk history559 were checked; they do not
decide this different product. No cross-notebook input is used.

Provisional mechanism (not yet a proved result): combining the exact
heat factors gives exp(t*(alpha-log n)^2/4). With X=Y_- and
ell=log(Y/(2*pi)), the leading weight is
exp(t*((ell/2-log n)^2-pi^2/16)/4). Its diagonal correlation suggests
2*integral_0^(1/2) exp(pi^2*lambda^2*x^2/8)*cos(3*pi*x) dx,
lambda=Y/X in [1,sqrt(2)]. The increasing exponential favors the
negative part of the cosine. This is a candidate calculation only.

Remaining proof work: justify the elementary phase/gamma reduction with
paid pointwise product error; bound varying amplitudes; separate unequal
indices in the difference channel; bound every sum-phase case including
near-cutoff stationary endpoints; retain actual entry intervals; pass
from the diagonal logarithmic sum to a uniform band limit and prove its
sign. Stop if any remainder cannot be made o(X*log X).

No sign theorem, root count, RH candidate or novelty claim is established
at this checkpoint. Preserve this reasoning if interrupted.

## Proof completion checkpoint

The planned bounds now close on paper, pending the full canonical
write-up. Put c=pi/8, v_n=ell/2-log n, and
f_n=Y*ell/2-Y/2-pi/8-Y*log n+c*t*v_n. Then
f_n'=v_n+c*t*(2*v_n+1/2)/Y,
f_n''=1/(2*Y)+c*(2*v_n+3/2)/(2*d), and
f_n'''=-1/(2*Y^2)+c/(2*d*Y).
These explicit derivatives avoid differentiating a Stirling O-term.

Stirling and the explicit G_0 phase reduce S_d to the negative of this
cosine sum with uniform error O(X^(-3/4)); its product cost is O(sqrt X).
All amplitudes have total variation O(1/sqrt(m*n)). Each pair's actual
floor domain is one entry interval. The sum phase has second derivative
at least a constant/X, giving total O(X), including near-stationary
cutoff endpoints. For unequal indices the difference derivative is
separated by log(n/m); elementary integration by parts and A.3 give
O(sqrt X*log X). The surviving diagonal converts to the displayed
double integral with O(X*log log X) error. Its inner integrand's weight
is increasing, so comparison at x=1/6 gives coefficient at most
-2/(3*pi) after averaging. No numerical evidence is needed.

The canonical proof is to retain all estimates and the exact floors,
state an existential onset and nominate a separate conceptual audit.
No root-distribution or quantitative Jensen transfer is inferred.

## Completion

The argument is now written in full in C019l, including all product
cases, exact entry intervals, the signed coefficient and the error
threshold. The earlier sections above preserve unfinished reasoning
at its two checkpoints; the canonical proof supersedes their provisional
status. Separate scrutiny is nominated without assuming any downstream
sign-distribution or actual-Jensen transfer statement.
