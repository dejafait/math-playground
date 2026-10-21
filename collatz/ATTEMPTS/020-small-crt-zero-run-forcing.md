# Attempt 020 — Elementary digit lifting for small CRT roots

The approved bounded attempt derives the exact recurrence and guarded
infinite-selection equivalence in
[L032](../lemmas/L032-small-crt-digit-reduction.md).
It leaves the assertion for every real B>=0 unresolved.

## WHY IT FAILS

Nested CRT lifting provides an exact digit and carry recurrence, but
does not force arbitrarily long zero runs in this particular sequence.
L032 shows that such runs are equivalent to the desired infinite
selection, including its strict lower height guard. Thus invoking long
runs without a new arithmetic argument would assume the missing input.
The complete finite certificate in `scripts/small-crt/certificate.json`
finds three B=0 hits and no B=1,2,3 hits through L=256; neither finding
decides the infinite claim. Park this elementary forcing mechanism
under the stated stopping test. Reopen only with a specific mechanism
forcing unbounded run lengths or a rigorous uniform obstruction, not
with more sampling or presumed equidistribution. This is not a
counterexample to the target, nor a stop on other clock coefficients.

A separate proposed continuation examines the open coefficient interval
using L028's existing height envelope and coefficient slack. It needs
its own scope review before any new deduction. No such extension is
proved in this attempt.
