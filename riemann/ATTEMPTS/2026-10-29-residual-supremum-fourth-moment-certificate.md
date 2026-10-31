# Full second moment, insufficient fourth-moment certificate — 29 October 2026

The unchanged approved target was the full-scale L1 lower bound for
L477's complete residual via second/fourth moment interpolation.
[L480](../lemmas/L480-complete-residual-second-moment-and-fourth-moment-gap.md)
contains the full proof and the exact remaining fourth-moment threshold.
It uses audited L479 to move beyond the older failed termwise budget;
the complete second moment is now comparable to T(log T)^8.

WHY IT FAILS: the complete upper estimate I_4<=C M^2 I_2,
obtained from the coefficient-sum supremum bound, gives at best the
displayed lower certificate c sqrt(T)(log T)^8. Its ratio to the
required T(log T)^3 tends to zero. The actual quotient is not bounded
above by this certificate, and the supremum envelope need not be sharp.
L480 shows that success of this interpolation test is equivalent to
I_4<=C T(log T)^18 along an unbounded sequence; the certified upper
envelope exceeds that scale by T/(log T)^10. Its matching necessary
lower scale does not decide whether such an upper bound holds.

Stop repeating this supremum certificate absent new concentration
control. Neither the true interpolation method nor either L1 defect
threshold is refuted. Preserve L478's coefficientwise failure and
L319's stationary-involution stop. L480 needs its first independent
critical audit before the new moment threshold is relied upon; no
new source search is required for that audit within the unchanged
[ready assessment](../drafts/literature/2026-10-29-l477-residual-moment-interpolation-coverage.md).

The first independent audit is now complete in L480 Section 6 and
accepts its bounds without correction. This updates the audit status
only; the certificate stop and every qualification above remain intact.
