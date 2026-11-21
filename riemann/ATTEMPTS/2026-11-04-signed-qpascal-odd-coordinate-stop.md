# Strict q-Pascal accretivity fails at the exceptional edge

Step415 tested only e_1 for the original actual-coefficient normalization
at k=d=r-1. [L774](../lemmas/L774-actual-qpascal-odd-coordinate-accretivity-obstruction.md)
proves an eventually negative coordinate after a positive normalization.
The separate step417 critical audit passed; the full proof, explicit
finite-value error budget and determinant-transfer qualifications are
canonical there. This verifies the local specialization without changing
its conclusion or supplying an actual minor sign. No large-degree matrix scan or effective onset is used.

## WHY IT FAILS

The two adjacent log defects both tend to the same nonzero positive
constant. Their exponentials therefore force the exact signed coordinate
below zero, with a rigorously vanishing combined error. This violates
a necessary condition for positive definiteness of the symmetric part.
It stops the proposed sufficient accretive-determinant interface, not
the actual determinant sign, alternative normalizations or RH. Preserve
the separate L765 norm stop and L766/L773 evidence. Reopening a positivity
route needs a materially different signed mechanism, not a larger scan
or a claim that the old norm bound was unnecessary.
