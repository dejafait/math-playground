# Equality-only both-zero budget — step 259

Approved target: test whether L065 and L086 force at most two both-zero
scalars at L059's thirteen-scalar threshold, or one for dependent pair
quadratics. The main gap is the uniform triangle twelve bound. This
restriction could reduce the both-zero contribution in a violating fiber;
few/no-both-zero fibers remain independent gaps.

Initial proof checkpoint: realize all thirteen scalars in L059's
nonprime chart before using equality fullness and audited L086. A
both-zero support containing a singleton label contains its entire pair
by L065, contradicting linearity against the corresponding base support.
Thus every actual both-zero support is a four-subset of the seven-label
complement V. L065 gives at most two such supports for independent pair
quadratics. In the dependent case each is a union of two of at most
three disjoint two-label fibers. Any two different such supports share
a fiber, violating linearity, so at most one survives.

Remaining checks before the canonical write-up: identify actual supports
using fullness rather than padded witnesses; use at most one scalar per
both-zero support; retain every restored gate and transfer the bound by
the original-chart deletion rule without rationalizing that chart.
Stop if any of these applications fails; projected configurations alone
are not conditional counterexamples. No new calculation or source search
is needed. ATTEMPTS/036's cross-difference route remains stopped.

## Completed attempt

The checks above close in the
[canonical L098 proof](../lemmas/L098-triangle-equality-both-zero-budget.md).
It proves the conditional thresholds two and one. Fullness identifies
each relaxed witness with its actual four-support before linearity is
used. L065's pivot uniqueness converts support counts to scalar counts;
L059's original-chart deletion then transfers the bound without applying
equality linearity to a chart with only twelve additional events.

This is a relevant local refinement, not a uniform twelve theorem or
progress beyond the checked literature certified as original. No
counterexample, enumeration or mathematical script was needed. The
independent and dependent branches both pass the stated continuation
test; few/no-both-zero fibers and isolated-row counts remain unresolved.
L098 is not yet separately critically audited. The sole continuation is
its critical audit after a separate coverage approval; the newly saved
assessment remains REVIEW_REQUIRED.
