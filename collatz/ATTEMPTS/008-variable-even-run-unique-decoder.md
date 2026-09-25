# Attempt 008 — Extend the unique decoder to a second even-run length

Tested on 2026-09-25. The proposal was to preserve the unique extendible
inverse branch from {(1,1),(2,1),(3,1)} after adjoining (1,2), as a way
to constrain a larger set of histories containing growth and contraction.

## WHY IT FAILS

[L010](../lemmas/L010-variable-even-run-inverse-branching.md) recomputes
the endpoint union as all nonzero residues modulo 3. The old branches
whose predecessors are 2 modulo 3 can now extend using (1,2), so the
three even-run-1 extendibility sets become nested. An infinite positive
family has three extendible branches with distinct penultimate states,
and endpoint 661 has five depth-two histories, exceeding the old bound
three. This stops the direct generalization of uniqueness and its old
all-depth count, not the earlier theorem on its smaller alphabet. It
neither proves unbounded multiplicity nor controls forward escape. A
restriction to histories staying above their own starting value would
require a fresh argument; the present unrestricted counterexamples do
not decide it. No Collatz disproof or global research stop follows.
