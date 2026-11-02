# Mobius common-observer test: signed boundary remains unresolved

The exact 2-by-2 observer extraction, removable collisions of its
prefix/tail split, and raw boundary calculation are canonical in
[L624, Section 5](../lemmas/L624-exact-divisor-congruence-and-persistent-shift.md).
The fixed normalized coefficients are mu(n)/(sqrt(n) m_N), with
N=floor(T^(1/100)); the exact six terms and Hardy phase are retained.

WHY IT FAILS: The attempted comparison cannot bound the complete signed
boundary. At N=p and T=p^100, the r=2p coordinate has zero zero-shift
value but a mixed arithmetic jet whose positive lower bound exceeds
L622's entire transfer-error scale. Thus that raw boundary cannot be
discarded jet by jet at the required precision. This is a restricted
obstruction, not a lower bound for the signed tail matrix: derivatives
of the Euler factor and pole factors, all six collision cancellations,
the phase and the observer extraction remain in the exact expression.
Neither a negative eigenvalue nor a uniform positive observer margin
was proved. Stop this coefficient specialization by the exact shifted
boundary route as inconclusive; do not infer a global family stop or
an RH counterexample from it.

A physical weighted integration-by-parts comparison is a different
proposed mechanism, subject to a separate literature gate. It would
have to retain all derivatives of both the amplifier and smooth
weight; low frequency alone is not an established sign theorem.
