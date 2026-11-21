# Reciprocal-power Appell production-TP construction: restricted stop

13 November 2026, step775. The approved single-entry test for
R_(n,k)=binom(n,k)S_(n-k+2)/S_2 gives a negative P_(2,0) interval.
The full proof, assumptions, precise source imports and qualifications are
in [C040a](../lemmas/C040a-reciprocal-power-appell-production-entry-stop.md);
full evidence is `scripts/central-jacobi/appell-production-entry-775.json`.
The independent step777 finite audit passed under the same inherited
contracts; its full evidence is `scripts/central-jacobi/appell-entry-audit-777.json`.
This is an informative known-method
specialization, not an advance beyond the checked general sources.

WHY IT FAILS: This particular sufficient construction requires all
production minors to be nonnegative. Its actual single-entry minor is
strictly negative, under the inherited L778 evaluator/error/software
contracts. Therefore the production-TP hypothesis needed for the cited
Sokal propagation theorem is false for this array. The failure does not
refute actual Hankel positivity or RH, and a historical stop here does
not forbid different arrays or mechanisms. No adjacent-entry or degree
sweep is justified by this diagnostic.
