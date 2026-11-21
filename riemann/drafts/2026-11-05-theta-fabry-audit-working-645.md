# Actual-theta Fabry application audit — working record, step645

Approved target: independently audit paper20 v2 Section3's application
of L828, with the unchanged SPECIALIZE coverage supplied at invocation.
This is one conceptual proof audit and a known-source reproduction.
Main gap: actual-Xi all-degree mixed positivity. The intermediate use
is a reliable exclusion of complete Bernstein root-zero representations;
ordinary membership and any sufficient sign bridge remain independent.
Continue only if every density, endpoint and weighted-tail hypothesis
of L828 is paid. Otherwise preserve the exact failed implication.

Read L828's hypotheses and conclusion (its abstract proof is an accepted
input, not the present audit), L016/L018/L019, the existing class comparison,
step643's decision and the earlier sufficient-class stop. Reused step644's
primary coverage. Retrieved paper20 v2 Section3, (17)–(25), including both
tail cases; reviewer comments supply no proof evidence. Existing notebook
changes are extensive and are being preserved. No cross-notebook input.

Partial reasoning saved before full proof assembly: P=K/2 on x>=0;
normal convergence on compact subsets of |Im x|<pi/4 and the theta
inversion give an even positive analytic density. For the cusp, derivatives
of a^(-1/2) exp(-beta/a) have a polynomial loss in a^(-1); the summable
beta=pi(m+1/2)^2 tail should preserve exp(-pi/(4a)). This pays the flatness
used by the identity theorem, not just the undifferentiated transform.
The moment lower interval begins at L-log log s, L=(log s)/2. Its error
is o(s). The low weighted tail has exponent 2s-2 and is bounded only for
s>=1; that suffices for the real-s limit. The high-tail denominator is
eventually positive because s^(1+epsilon) dominates s/log s. Both weighted
tails must be compared with M(s)/L^2 before squeezing the central interval.

Remaining audit work: write complete convergence and tail estimates,
check agreement of the square-root germ at +R, and derive the three
asymptotic hypotheses of L828. No mathematical scripts are needed.

Completion: all listed checks pass; the full proof is now canonical in
C828a. The provisional reasoning above is retained as the pre-assembly
record. The application reproduces paper20 Theorem1 and leaves ordinary
Bernstein membership and Xi signs unresolved. The new finite-index
continuation is only a separate REVIEW_REQUIRED source nomination.
