# Arbitrary-curve denominator specialization — working attempt

2026-10-11. Authorized target and prior coverage: the unchanged
`drafts/literature/2026-10-11-arbitrary-curve-denominator-specialization.md`.
This records unfinished reasoning before the full write-up, not a verified result.

Main gap: rank equality for arbitrary complex order at least two.
Intermediate target: a computable reduced-denominator bound for every
integral relative value, allowing CM and additive reduction and requiring
neither an optimal equation nor a supplied isogeny map.

Proposed assembly: compose the canonical optimal parametrization with an
existential Q-isogeny of degree at most 163. Bound its integer differential
scalar using the unconditional factor-six theorem and von Kanel's
conductor-only degree estimate. Independently enumerate two good primes
splitting completely in Q(zeta_delta), delta squared the largest square
dividing N; the gcd of the target point counts kills both cusp images.
A multiplied image path then closes on E(C). Use the complete real-period
projection lattice, whose positive generator is Omega(E)/2 in both lattice
types, rather than only the purely real period. Check the size bound
separately from any common clearing integer.

Continue if every factor is independently computable and both endpoints
are controlled. Abandon if a map certificate, unknown normalization scalar,
unproved optimality or an absolute-cycle-only input is needed. Exact
integration enclosures and recovery, coefficient nonvanishing, rational
directions, Sha and complex-order comparison remain unresolved. L027 is
the downstream conditional enclosure; L028/L038 fix conventions only.
ATTEMPTS/022--024 are preserved production limitations, not this mechanism.

## Completed attempt

The complete proof is now canonical in
[L048](../lemmas/L048-arbitrary-curve-full-relative-denominator-bound.md).
The bound is B(E)=1956DT, with an independently computable integer degree
majorant D and a gcd T of two exact target point counts at good split
primes. The separate lcm integer clears the entire integral relative
module. The mathematical attempt is known-source reproduction and its
first assembly awaits critical audit. This note preserves the earlier
unfinished reasoning and supplies no alternative proof or dependency list.
