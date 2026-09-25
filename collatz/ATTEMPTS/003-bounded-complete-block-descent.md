# Attempt 003 — Descent within a fixed number of complete blocks

Tested on 2026-09-25. The proposed repair to first-block descent was to allow
a common finite number K of complete maximal odd-even blocks. Arithmetic
compatibility might have forced compensating divisions within those blocks.
The test also allowed a finite residue correction to log(n) when comparing
block endpoints. Such a certificate, together with finite base verification,
would give termination through finite sublevel sets.

## WHY IT FAILS

[L003](../lemmas/L003-consecutive-growing-blocks.md) proves that every K is
realized by arbitrarily large starts whose first K blocks all have lengths
(2,1), with strict growth at every block endpoint and no descent at any
intermediate shortcut time. Multiplying the construction's parameter by q
keeps all these endpoints in the same residue modulo q, so every correction
h(n mod q) cancels and the logarithmic change is positive. The necessary
negative change is therefore impossible within any fixed block bound,
regardless of the finite exception set. This refutes the bounded-block
certificate; it does not refute unbounded return times, unbounded arithmetic
corrections, or Collatz. Each fixed positive start eventually exits this
particular repeated pattern, and the theorem supplies no estimate forcing
the later orbit below its original start.
