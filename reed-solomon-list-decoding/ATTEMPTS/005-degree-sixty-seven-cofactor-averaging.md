# Degree-67 cofactor averaging at 66 agreements

Tested on 2026-10-04 while specializing the ready residual-linear-factor
dictionary on the fixed rate-1/16 instance.

## WHY IT FAILS

The [canonical dictionary and comparison](../lemmas/L015-degree-sixty-seven-linear-cofactor-dictionary.md)
show that the corrected averaging certificate is below 2^317, whereas
the ambient threshold exceeds 2^320. Root-subset/cofactor incidences
overcount fully split 67-root differences, so ignoring that correction
cannot be called an attained list. The corrected lower certificate is
about 0.111 times threshold and does not certify unsafety. This stops
bare averaging, not the degree-67 family, arbitrary-center upper bounds
or research on the problem. The screened uniform three-moment/cofactor
upper test uses a different conclusion and remains available.
