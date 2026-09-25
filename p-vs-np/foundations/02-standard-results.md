# Standard scope results

## Hypotheses

Use the language, explicit-encoding, machine, and circuit conventions in [the model note](01-model-and-target.md). Polynomial reductions below are deterministic many-one reductions. Relativization gives both classes access to the same oracle with the usual charged query-writing time.

## Conclusion

P ⊆ NP; SAT is NP-complete; P = NP iff SAT ∈ P; and P ⊆ P/poly. Consequently SAT ∉ P/poly implies P ≠ NP. There are oracles A and B with P^A = NP^A and P^B ≠ NP^B.

## Proof

**Containment.** For a language in P, a verifier can ignore its certificate and run its decider. This proves P ⊆ NP.

**Completeness input.** Use the standard **Cook–Levin theorem**: SAT, including its 3-CNF restriction, is NP-complete under polynomial-time many-one reductions. A precise source is Stephen Cook, [*The P versus NP Problem*, §2, Definition 4 and Proposition 1 on pp. 4–5, followed by the SAT and 3-SAT completeness discussion on p. 5](https://www.claymath.org/wp-content/uploads/2022/06/pvsnp.pdf). This is a named standard input, not a new proof of completeness. Direct assignment checking also shows SAT ∈ NP.

If SAT has a polynomial-time decider, compose it with the Cook–Levin reduction for any fixed language L ∈ NP. The reduction's output length is polynomial in its input length, so the composition has one fixed polynomial bound for that L. Thus NP ⊆ P. Conversely, P = NP and SAT ∈ NP give SAT ∈ P.

**Computation-to-circuit simulation.** Fix a deterministic polynomial-time machine. It suffices to use a one-tape simulation with polynomial time T(n) ≥ n+1. Encode each tape cell by a constant number of bits, including a marker carrying the state when the head is present. In one step, the new contents of a cell depend only on that cell and its two neighbors: the finite transition rule decides symbol changes and arrival or departure of the head. Each local update therefore has a constant-size Boolean circuit. Only O(T(n)) cells can be visited in T(n) steps. Unroll T(n) rows of local updates, taking input bits and fixed initial markers as the first row, with sufficient blank boundary cells. Make halting states stationary. The final accepting-state markers can be combined with an OR circuit of size O(T(n)). The total size is O(T(n)^2), polynomial in n. This supplies the circuit family and proves P ⊆ P/poly. It makes no converse claim about arbitrary nonuniform families. If SAT ∉ P/poly then SAT ∉ P, so the preceding completeness argument gives P ≠ NP.

**Relativization input.** Use the standard **Baker–Gill–Solovay relativization theorem**, Theodore Baker, John Gill and Robert Solovay, [*Relativizations of the P =? NP Question*, SIAM Journal on Computing 4(4), 431–442 (1975), DOI 10.1137/0204037](https://doi.org/10.1137/0204037). The publisher's abstract, checked on 2026-09-24, explicitly states the two oracle constructions. Hence an argument proving the same answer relative to every oracle cannot settle the unrelativized question. This is a scope test for a proposed proof, not a ban on every use of diagonalization. Only the abstract was inspected; no stronger technical assertion from the paper is used.

## Mathlib

Coverage: **not checked** for Cook–Levin, computation-to-circuit simulation, or Baker–Gill–Solovay. No theorem names from Mathlib have been verified. The named external results above match the stated standard inputs; they do not resolve P versus NP.
