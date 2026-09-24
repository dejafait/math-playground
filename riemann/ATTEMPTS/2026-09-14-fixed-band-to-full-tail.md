# Fixed prime bands do not yet control the full tail — 2026-09-14

The finite-band joint-divisor bound is proved in
[L206](../lemmas/L206-fixed-prime-band-joint-divisor-bound.md).

WHY IT FAILS: the proof takes N to infinity with each prime fixed.
It cannot sum the errors over primes up to 2N. On the actual b
progressions the number of terms becomes bounded at primes of size
sqrt(N), so the slice cancellation argument no longer yields a
vanishing relative error. The residual iterated tail is specified
in L206 and remains unproved. This is a failure of that inference,
not a disproof of the desired arithmetic population bound.
