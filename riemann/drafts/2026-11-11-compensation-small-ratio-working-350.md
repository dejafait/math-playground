# Small-ratio compensation — working record, step350

Started 11 November 2026 under unchanged EXPLORE review345, exact approved
packet target. One RESEARCH proof attempt, theta=1, lambda=A/128,
fixed A>=A_0>=16. Reuse C997m's original-TV and target-retention result.

Main gap: L030-L032/C032a positivity, L966/L968 signed forcing and
L984(H). Intermediate test: charge the exact finite-exponential
correction in the complete data response at 2; a rigorously conflicting
rate would stop this subfamily, not the general point bridge or RH.

Duplicate/failure check: review344's inspected contracts and comparisons;
C997i's degree<=n condition fails since q_n=n; C997m's leakage condition
theta>=Theta_0,lambda>=A fails. Failures340/341 leave spectral tails
unpaid and supply no response estimate here. No source refresh or
cross-notebook input is needed for the finite integral calculation.

Partial reasoning, not yet a result: put v=64*x^2, k=r_n+1>lambda*n.
The gamma integral for 1-Q_r may give an exponential bound for u/k<=1/4.
Split at v=1/8. In the outer piece (1-v)^n<=exp(-n/8);
in the inner piece u=2*lambda*n*v<=lambda*n/4. Seek a correction
bound <=C*exp(13*n/64) for each unnormalized integral, using
lambda>=1/8 and the factor exp(n*c/8)<=exp(17*n/64).
This is smaller than the anticipated pure-endpoint saddle rate, but
does NOT prove that saddle asymptotic or noncancellation.

Remaining issue: at theta=1 the proposed saddle is fixed away from 0.
C997e gives an existential amplitude neighborhood only; increasing A
does not move this pure-endpoint saddle. Do not silently assume its
containment in that neighborhood. Continue only with a justified domain
and complete error comparison, or record the paid correction and the
unresolved pure-endpoint integral honestly.

Completed: the proposed real correction bound is proved, with an
explicit original-TV estimate and uniform complete-response charge in
[C997n](../lemmas/C997n-small-ratio-compensation-original-tv-reduction.md).
The decisive calculation splits v=64*x^2 at1/8 and uses the exact
nonnegative exponential tail with tilt4. It works for every fixed
A>=A_0>=16, including lambda<A. No mathematical script was needed.

Result is a partial ADVANCE / REPRODUCTION, not a scoped stop: the
data error has upper rate13/64>0. No complete data lower or upper
suppression rate was established. The next source-scope nomination
is REVIEW_REQUIRED in literature/2026-11-11-endpoint-saddle-domain-review-350.md;
it does not approve the proposed fixed contour. Full proof and exact
qualifications are canonical in C997n; independent audit remains open.
