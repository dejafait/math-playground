# Attempt: positive Laplace kernel forces zero-freeness

Date: 2026-09-09

Outcome: failed; the valid η representation and an exact obstruction are retained as Lemmas 12–15 in the lemma files.

The mathematical counterexample or obstruction is proved in [Lemma 15](../lemmas/L015-a-nonnegative-indicator-kernel-can-have-zeros-inside-the-strip.md).

**WHY IT FAILS.** A positive kernel controls the integral for real arguments but does not prevent cancellation of complex phases e^{-itu}. The explicit indicator counterexample has a holomorphic transform and genuine nonreal zeros inside the critical strip. It does not have the specific arithmetic interval pattern of η, so it is not a counterexample to a stronger theorem exploiting that pattern; no such stronger theorem was proved. Positivity alone cannot supply the missing zero-free assertion.

## 2026-09-21 arithmetic-pattern reopening screen

The target is I(s)=η(s)/s≠0 for every 1/2<Re(s)<1 and every imaginary part. On this open strip |2^(1-s)|=2^(1-Re(s))>1, so the multiplier in L012 never vanishes; s also never vanishes. Thus this target excludes exactly the right-half-strip zeta zeros. Together with the localization and reflection in L009, it would prove RH. Neither a bounded-height result nor nonvanishing only on the real axis meets this threshold.

L014 retains substantially more than generic positivity: the occupied intervals in the x variable are exactly [2n-1,2n), and in the Laplace variable they are [log(2n-1),log(2n)). Their endpoints encode the original paired Dirichlet series. L015 has different support and supplies no obstruction to a theorem using these exact endpoints. Its stated zero is in 0<Re(s)<(log 2)/2, so that specific example also must not be described as a demonstrated zero in the target right half-strip. Its role here is solely the already established failure of generic positive-kernel zero-freeness.

The quantitative information available from L014 is an absolute upper bound on the remainder. Write I_N(s) for the integral over its first N occupied intervals. The proof of L014 gives |I(s)-I_N(s)|≤(2N+1)^(-σ)/σ, where σ=Re(s)>0. Consequently a sufficient pointwise certificate is |I_N(s)|>(2N+1)^(-σ)/σ. To finish this route one would need an argument producing such a strict inequality (or another nonvanishing mechanism) for every point of the target strip, with N allowed to depend on s. Merely sending N to infinity does not produce it: at a zero, |I_N(s)| is bounded by precisely the same remainder. No positive constant uniform in height is being demanded here.

The exact cell identity in L014 recovers ((2n-1)^(-s)-(2n)^(-s))/s. Summing it recovers L012, rather than a new sign estimate. The sign argument of L013 works for real σ; with nonzero imaginary part the factors carry rotating phases. Positivity of w bounds absolute mass and the tail but supplies no lower bound on their complex sum. The recorded arithmetic identity η=(1-2^(1-s))ζ transfers the target back to the unresolved zero-exclusion assertion. No independent phase inequality, lower bound on the finite head, or arithmetic recursion preserving nonvanishing was found in these inputs.

**WHY IT FAILS (reopening).** Exact arithmetic support was retained, but the available consequences establish convergence and real-axis positivity, not noncancellation at all heights. The achieved tail bound tends to zero; the required head-minus-tail margin has no established positive sign on the full target domain. This audit does not disprove that margin or rule out all arguments using the interval pattern. It parks technical extension of this route until a specific additional arithmetic mechanism is supplied. No new lemma or strengthened mathematical statement is asserted.
