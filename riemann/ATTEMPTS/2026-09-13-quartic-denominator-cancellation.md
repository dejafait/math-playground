# Universal quartic denominator cancellation — 2026-09-13

Tested substitution of Q′ into L157 followed by complete quartic
monomial collection, before taking absolute values.

**WHY IT FAILS.** The pair-exchange kernel is (x/y+y/x)/2, and a repeated
unconjugated index leaves a collected coefficient growing like N even
in a fixed allowed window. The exact proof and qualifications are in
[L158](../lemmas/L158-quartic-symmetrization-retains-small-denominators.md).
This rules out universal coefficientwise denominator cancellation only.
It does not rule out cancellation in time with the amplitude cutoff;
that estimate remains unproved. The amplitude-derivative contribution
can already be bounded by O(1/(M sqrt(T))).
