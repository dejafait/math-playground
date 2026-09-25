# Independent-link plaquette continuum

Tested 2026-09-24. At Wilson coefficient beta = 0 on the infinite SU(2) lattice, rescale one fixed-orientation plaquette trace to keep a nonzero smeared variance, and test whether it generates a nonvacuum continuum field.

## WHY IT FAILS

The limiting smeared field is Gaussian white noise, as proved in [L001](../lemmas/L001-independent-plaquette-noise-has-trivial-reflection-space.md). Positive and negative open time half-spaces are independent, so the reflection form factors through expectation and every centered polynomial lies in its null space. Nonzero probabilistic fluctuations therefore produce only the vacuum in the reflection quotient, with no finite excited mass. The failure concerns this field and scaling at this endpoint; it does not exclude other observable sectors or a coupling that changes with the cutoff.

No earlier local attempt or lemma existed when this test was chosen. The negative result rules out interpreting an ordinary nonzero covariance alone as physical nontriviality in this construction.
