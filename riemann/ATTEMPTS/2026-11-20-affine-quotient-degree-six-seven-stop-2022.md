# Prescribed affine quotient: PSD increment fails at N=6,7

The exact result is [C029q](../lemmas/C029q-affine-quotient-degree-six-seven-residual-obstruction.md).
Its certificate retains every coefficient, denominator, identity and
all 49 fixed directions. The degree-seven test and denominator checks
succeed. The vector e_2 in descending Phi_7 coordinates has a strictly
negative residual quadratic form. No degree/precision escalation was
performed and all earlier boundary-metric, runtime and enclosure
failure evidence is preserved.

WHY IT FAILS: Ordinary Euclidean division fixes q from the two leading
coefficients, and multiplication by that q fixes E before sign inspection.
For this actual full Jensen-weighted family, the resulting residual
B_7-E B_6 E^t is not PSD. Therefore this specific increment cannot
propagate an index bound from N=6 to N=7 by PSD addition. The obstruction
is local: an eventual-only increment, another coefficient embedding or
a different index argument is not refuted. Repeating this fixed pair
or increasing degree/precision does not repair the rejected claim;
further propagation work requires a materially new mechanism or a
separately justified eventual starting rule. Independent audit was
pending at step2022. Step2024 now validates the complete fixed-input
certificate with a separate implementation (152 checks, no failures),
as recorded in C029q. This closes the audit and retains the stop;
it is not additional propagation evidence. Park this embedding/pair,
without a degree or precision campaign. The nominated next source
question concerns a single polynomial's signed Euclidean/subresultant
structure, not another inter-degree PSD increment; it is unapproved.
