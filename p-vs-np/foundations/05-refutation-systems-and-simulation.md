# Refutation systems and polynomial simulation

## Hypotheses

Use the explicit CNF encoding and uniform complexity classes in [the model note](01-model-and-target.md). UNSAT consists only of well-formed unsatisfiable CNFs. Malformed strings are recognized separately in polynomial time. The class coNP consists of complements of NP languages.

A refutation system Q is a deterministic verifier V_Q(F,π), polynomial-time in |F|+|π|, such that F belongs to UNSAT exactly when some π is accepted. Soundness and completeness are semantic requirements on the fixed verifier, not additional tasks it must decide about its own code. Define

s_Q(F) = min { |F|+|π| : V_Q(F,π)=1 }

for F in UNSAT. The system is **polynomially bounded** when s_Q(F)≤r(|F|) for one polynomial r and every such F. System Q **size-simulates** R when s_Q(F)≤p(s_R(F)) for one polynomial p and every F in UNSAT. System Q **p-simulates** R when one polynomial-time function g(F,π) produces a Q certificate for F whenever V_R(F,π)=1; its running time is bounded on invalid inputs as well. These polynomials and algorithms may depend on the fixed systems.

Extended resolution (ER) here permits resolution, weakening, reuse of earlier clauses, and fresh extension variables. An extension z↔(ℓ₁∧ℓ₂), where the literals use previously available variables, introduces the clauses (¬z∨ℓ₁), (¬z∨ℓ₂), and (z∨¬ℓ₁∨¬ℓ₂). Extension variables never occur in the original CNF, and a refutation ends in the empty clause. Proof length charges all written literals, binary indices, and inference references.

## Conclusion

ER is a sound, complete polynomial-time-checkable refutation system. Every p-simulation is a size simulation. A polynomially bounded refutation system exists if and only if NP=coNP; this existential assertion does not select ER or any other prescribed system.

## Proof

**ER verification and soundness.** Check each initial clause against F, each inference against its explicitly referenced premises, and each extension for freshness and the three defining clauses. These are polynomial-time string operations in the complete input and proof lengths. A satisfying assignment of F extends to each fresh z by the value of ℓ₁∧ℓ₂. It therefore satisfies all extension clauses. Resolution and weakening preserve truth under every such assignment, so a satisfiable F cannot have an ER refutation.

**Completeness.** Ordinary resolution with weakening already suffices. Let the distinct variables of an unsatisfiable F be x₁,…,x_m. For every assignment a, choose a clause of F falsified by a. By weakening, derive the full clause D_a containing exactly the m literals falsified by a, since the chosen clause is a subset of D_a. Resolve the two clauses corresponding to each common (m−1)-bit prefix on x_m. Repeat on the remaining variables to obtain the empty clause. If m=0, unsatisfiability already requires an empty initial clause. This is a finite proof, with no polynomial length assertion.

**Simulation and the class equivalence.** A polynomial-time translator has polynomial output length, giving the size bound by translating a shortest source proof. If Q is polynomially bounded, guess a certificate of its fixed polynomial size bound to recognize UNSAT in NP. Cook–Levin reductions output well-formed CNFs; hence for every L in NP its complement also lies in NP, by reducing L to SAT and applying this UNSAT verifier. This gives NP=coNP. Conversely, if NP=coNP, UNSAT has an NP verifier with a fixed polynomial certificate bound, which is the desired Q. Its complement is SAT together with the polynomial-time-recognizable malformed encodings, so the well-formedness convention causes no difficulty.

The standard named input is the **Cook–Reckhow characterization**. A precise primary source is Cook–Reckhow, [*The Relative Efficiency of Propositional Proof Systems*, JSL 44(1), 36–50 (1979), §1, Definitions 1.3 and 1.5, Propositions 1.1, 1.4 and 1.6, pp. 37–38](https://www.cs.toronto.edu/~sacook/homepage/cook_reckhow.pdf). It uses polynomial-time onto functions for tautologies. Our verifier convention gives such a function for UNSAT by mapping a valid pair (F,π) to F and any invalid pair to a fixed contradictory CNF. Conversely, equality with the output of an onto function is a verifier. Both transformations preserve polynomial bounds and translations: for invalid source pairs, a translator can output a hardwired target proof of the fixed contradiction. The direct UNSAT argument above supplies the class equivalence for this encoding.

Source audit: 2026-09-25. [Cook's author page](https://www.cs.toronto.edu/~sacook/) explicitly corrects the premise in the paper's Corollary 4.7 from P≠NP to coNP≠NP. The erroneous printed premise is not imported. No assertion about ER simulating all proof systems, or about arbitrary polynomial-time algorithms having short ER correctness proofs, is used.

## Mathlib

Coverage: **not checked** for the full proof-system statements, Cook–Reckhow equivalence, ER, or polynomial simulation. No Mathlib identifier or absence claim is asserted. The primary source matches the standard characterization and p-simulation definitions; it is not a matching theorem for an ER simulation of arbitrary SAT deciders. The elementary ER arguments are given above.
