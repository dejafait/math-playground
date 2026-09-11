# Absolute centered-primitive bound — 2026-09-13

WHY IT FAILS: Centering removes the boundary term but leaves a primitive
of size T(log T)^4. The available O(1) normalized bound on |Q'| therefore
gives only O(T(log T)^4/M), with no decay for fixed M. The direct bound
is better but still supplies no decay. [Lemma 167](../lemmas/L167-centered-primitive-cutoff-covariance.md)
proves the identity and scale. This rejects the absolute estimate as a
justification, not the actual signed covariance replacement.
