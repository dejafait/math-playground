# Attempt 002 — Descent after one complete odd-even block

Tested on 2026-09-25. The proposal was to wait through the entire maximal odd
shortcut run and the consecutive even run, then prove the odd endpoint was
smaller than the start for every sufficiently large odd integer. Since even
starts already descend, this plus convergence of the finite exceptions would
give a strong-induction proof. Block lengths are unbounded, so the
fixed-shortcut-window obstruction did not settle this proposal in advance.

## WHY IT FAILS

[L002](../lemmas/L002-maximal-odd-even-block-descent.md) proves the exact
endpoint inequality and shows that every prescribed positive pair of run
lengths (a,b) occurs for infinitely many starts. A long odd run therefore
need not be followed by enough even divisions to compensate. In particular,
arbitrarily large n=16t+11 have block endpoint 18t+13>n, and no earlier state
in the same block is smaller than n. This refutes first-block descent even
with any finite exception set. It does not exclude compensation across
several blocks, provide an infinite expanding trajectory, or refute Collatz.
