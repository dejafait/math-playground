# Fixed canonical point: bounded dyadic membership attempt

Started 2026-10-17 under the saved SPECIALIZE assessment
`drafts/literature/2026-10-17-canonical-point-primitive-dyadic-test.md`.
Main gap: global positive primitive integer emptiness. The one target is
membership of L062's fixed point's TWO-descent class in L082's set;
its five-isogeny class is a different object and remains preserved.

Inputs: L033/L034 complete modular map; L046 fixed Q2 times H;
L062 fixed sigma and point at 9261/8; L069 cubic map; L071/L078
same theta and maximal fields; audited L082 comparison set. No
cross-notebook input. ATTEMPTS/014 and 034–037 are checked and not
reopened. The supplied assessment covers the changed scalar, general
Kummer formula, root lifting, localization and square comparison.

Checkpoint before writing full proof: m=3, beta=9261. The shifted
fiber coefficients obey C0 valuation -3, C11 valuation -6, C12=1,
and other coefficients at least -3. Reciprocal Hensel lifting gives
a rational root of x valuation -6; ramified lifting with z=pi^3 W
gives one root generating H, with v_H(z)=3. Reconstruction and
uniqueness of the whole identification must be written out.

Proposed exact comparisons, to be justified in the canonical proof:
kappa=64-theta is square with J-valuation 44. The canonical value
kappa+4z has relative perturbation valuation 66+9-44=31. Its ratio
to xi's representative has difference from one of the SAME valuation
31, because v_H(z)=3 whereas v_H(pi^5+pi^10)=5. Both are nonsquares
by the odd-leading-valuation test, since 31<66. The rational component
should be square by the parameter normalization, with bound 16>6.
No numerical approximation or script is needed for these symbolic
strict inequalities; no membership decision is based on scalar domains.

Continuation/abandonment test: finish both exact Hensel reconstructions,
nonvanishing evaluations and fixed-theta comparisons. Exclusion removes
only this actual global two-descent class;
membership would retire this witness test. Any uncertified root or square
comparison leaves the answer unresolved. Neither result determines a
supported-unit dimension, localized class contribution, rank or integer
lifting. A separate critical audit remains necessary after a full proof.

Completed the approved bounded test in L083: all reconstruction and
nonvanishing obligations above are proved, and both exact nonsquare
comparisons exclude the class. The rational bound is 16>6. The full
proof and citations are canonical in
[the result](../lemmas/L083-canonical-point-primitive-dyadic-exclusion.md).
No independent global direction or rank bound is inferred; the newly
proposed critical audit requires separate source approval next turn.
