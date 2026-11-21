# Fixed eight exterior delays excluded — step867

The approved one-family attempt gives a finite exact obstruction in
[C750b](../lemmas/C750b-exterior-delay-nine-phase-obstruction.md).
Its full certificate is
`scripts/good-frequency/exterior-delay-certificate-867.json`.
This is a new local NEGATIVE result using standard geometric-sum and
validated-scalar methods (REPRODUCTION). Independent rational audit869
now accepts the same bounds and restricted conclusion; its proof and
full evidence are recorded in C750b and
`scripts/good-frequency/audit-869.json`.

WHY IT FAILS: The positive uniform measure on the nine exact points
2*pi*j/(9*T), -4<=j<=4, T=4log3, annihilates every allowed cosine
correction exactly, while its value on the complete primitive base is
strictly less than -49/50. Thus at least one of these points stays
negative for every unrestricted real coefficient vector. This rejects
only the fixed eight-delay nonnegative-symbol representation. The
measure is not identified with a smooth supported Fourier-square test,
so it supplies no negative neutral Weil form or RH conclusion. C750a's
older coarse-screen stop is preserved as separate evidence. A later
attempt beyond this family needs a materially different correction
mechanism and its own discriminating test; this is not a global ban.
