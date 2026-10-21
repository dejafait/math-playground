# Attempt 017 — Force a late carry using the first complete boundary

Two bounded symbolic attempts used the approved full-height assessment.
The intermediate target was n0>=2^K for K actual postspell words with
every E^2 tail exact, as a possible restricted-alphabet escape bound.

## WHY IT FAILS

[L029](../lemmas/L029-finite-postspell-carry-height-diagnostic.md),
including its boundary-test section, retains the unresolved small-root,
final-parity and residue conjunction. After the last carry the canonical
representatives equal the existing actual orbit. At the first complete
word boundary the incoming B predecessor exists, but is outside residue
20; at internal B endpoints there is no incoming W supplied by the chain.
Thus L023's two incompatible incoming histories at a common endpoint
are not obtained. The earliest root has no assumed preceding word.
No late-carry margin, counterexample to the height bound, or escape
theorem was established. Stop this forcing mechanism after two
EXPLORATION attempts, without resetting the mathematical exploration
counter or declaring the height target false. Reopening requires a
different root-controlled constraint, not another carry-digit reduction.
