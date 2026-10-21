# Attempt 012 — Transfer a repeated postspell minimum to mixed chains

Tested on 2026-10-05 within the approved growing-chain initial-size
calculation. Candidate: every K-word chain with J>=2,H>=3 and tail E^2
starts at least as high as the minimum for K repetitions of W(2,3).

## WHY IT FAILS

[L022](../lemmas/L022-growing-postspell-minima-and-repeated-word-obstruction.md)
gives a smaller mixed two-word root and a four-word counterexample with
every final even tail exact, using imported finite parity coding and
complete guarded replays. It also tests the all-parameter affine
positive-endpoint lower estimate, whose right side is negative. The
[full finite certificate](../scripts/growing-postspell/result.json)
is retained. Stop these specific estimates rather than enlarge the
finite minima table. Neither counterexample refutes another divergent
uniform bound, a bound imposing additional least-root filters, or the
Collatz conjecture. Inverse arithmetic rigidity is a distinct possible
test, requiring separate source coverage and still leaving fixed-start
escape unresolved even if rigidity holds.
