# Fixed-allocation permutation attempt — 2026-10-11

Approved target: Decide whether modulo 5 excludes every permutation of
L055's 25 fixed word triples.

The main gap is universal eventual descent. This bounded target could
extend L056's integer-allocation exclusion to all orders of one fixed
multiset; it cannot exclude other allocations or establish descent.
Reuse the prior SPECIALIZE assessment
`drafts/literature/2026-10-11-fixed-allocation-permutation-mod-five.md`.
Essential inputs are L055's complete intact triples and L056's unshifted
integer numerator, chronological composition convention and denominator.
The relevant source, duplicates and stops were checked in that assessment;
targeted local checks confirm that L056 covers only literal order and
Attempt 026 concerns exclusion from the unchanged real subsystem.

Bounded attempt: start with literal order, then test at most 300 single
transpositions of its 25 intact triples. A verified numerator-zero order
stops uniform prime-five exclusion. If none is found, this bounded search
alone proves no universal claim; decide whether a complete finite-state
multiset enumeration is justified. Cross-check complete word residues and
the chronological numerator against the explicit integer numerator sum.
No tail may be detached from its J,H pair. Save all witness indices,
prefix/suffix exponents, contributions and composition states on disk.

Unresolved assumptions: a surviving prime-five test does not establish
integrality, complete cancellation, actual parity/valuation/residue or
primitive realization. Real-system guards after permutation also need
separate verification. Other allocations/branches, unrestricted cycles,
entry, divergence and eventual descent remain unresolved.

Completed: [L057](../lemmas/L057-fixed-allocation-permutation-prime-five-stop.md)
proves numerator and denominator both 0 modulo 5 after swapping intact
indices 0 and 6. Six swaps were tested, with 60 exact comparisons and no
failures. Complete parameter and witness arrays were inspected using the
shared JSON inspector. The explicit 25-term sum is 45; sequential
composition independently yields (2,0,2). Uniform prime-five exclusion
is abandoned. No exhaustive search is necessary for this counterexample
to uniform nonvanishing. This does not establish integer or real-system
realization. The next checkpoint selects a separate critical audit, with
coverage approval still required.
