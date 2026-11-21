# The natural two-field simplex divergence certificate fails

The bounded step65 attempt tested X=c X_Pbar+d X_Q, Q=sum t_i^2,
inside the approved degree-at-most-13 equivariant face-preserving
class on 1/4<=E<=4. The complete proof and exact full-kernel
certificate are canonical in
[L942](../lemmas/L942-actual-simplex-two-field-divergence-obstruction.md).
Its separate proof audit remains pending.

WHY IT FAILS: The Dirichlet-weighted divergence of X_Pbar is
proportional to Pbar. At two exact interior zeros of Pbar, its
actual-theta responses have opposite signs. The quadratic correction
has positive response at both zeros and negative response at a
vertex. A positive combination of those two evaluations and the
vertex limit annihilates both field columns, every scalar multiple
of Pbar and the radial integrand. Uniform strict residual positivity
would make that zero combination strictly positive. This excludes
the entire two-field span without a coefficient bound, but it does
not annihilate the columns of the full degree-13 field space.

Reopening the same span is unsupported. The informative obstruction
justifies testing independent field columns with nonproportional
divergence, while retaining the exact energy interval, degree cap,
affine scalar multiplier and these three mandatory constraints.
No conclusion about integrated-density crossings or RH follows.
