# The two-coefficient averaging certificate at rate 1/16

Tested on 2026-10-04 as part of the saved A=k+2 target. On the order-1024
subgroup of F_65537 inside F_{65537^28}, use the Q^2-class collision
certificate at k=64 to seek an unsafe list at 66 agreements.

## WHY IT FAILS

The [canonical comparison](../lemmas/L013-two-leading-coefficient-fibers.md)
shows that ceil(binomial(1024,66)/65537^2) is below 2^317, whereas the
ambient threshold exceeds 2^320. Bare averaging therefore cannot certify
unsafety at this rate. This is a failure of this lower certificate, not an
upper bound for actual fibers, safety of the full code, or a rejection of
the coefficient construction at the other three rates. Preserve the
successful unsafe certificates and the unresolved largest fiber. A
quantitative upper comparison for all joint fibers is a materially different
test that could decide whether to stop this center family at rate 1/16;
its source scope must be assessed before calculation.
