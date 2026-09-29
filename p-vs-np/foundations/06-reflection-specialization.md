# Reflection specialization: cited standard inputs

## Hypotheses

Use the notebook's [ER conventions](05-refutation-systems-and-simulation.md). The sources below use circuit Frege (CF), extended Frege (EF), or their own ER encoding; their representation hypotheses must be checked when applying them to a particular CNF. A supplied proof is distinct from an algorithm constructing such proofs. No formal proof of an arbitrary SAT decider's soundness is assumed available.

## Conclusion

The following are established inputs, with the indicated scope; they are not a completed specialization for L011.

1. **Circuit substitution.** For a system extending CF, substitution of circuits into a supplied proof can be performed in time polynomial in the proof length plus the total substitution-circuit length: Pudlák, Lemma 2.1.
2. **Global-to-local reflection.** Pudlák's Fact 1 requires both truth-constant substitution and polynomial-time constructible proofs identifying a formula with the satisfaction circuit applied to its code. Under these hypotheses, proofs of global reflection yield proofs of local reflection with polynomial overhead.
3. **Circuit/formula representation.** Jeřábek, Lemmas 2.4 and 2.5, gives polynomial-time simulations from EF to CF and from CF proofs with a formula conclusion to EF. The restriction on the latter conclusion is part of the statement.
4. **Formal soundness.** Cook's Definition 5.4 requires a PV proof of the encoded soundness identity. His ER Simulation Theorem 6.8 gives polynomial-length ER proofs of the bounded propositional translations of a fixed PV-provable equation, subject to the stated bounding-value condition. This premise is stronger than semantic truth of the equation.

## Proof

These are imports by precise citation, not reproofs:

- Pavel Pudlák, [*Reflection principles, propositional proof systems, and theories*, arXiv:2007.14835v1, submitted 29 July 2020](https://arxiv.org/pdf/2007.14835v1), §2.1–2.2, pp. 4–5, Lemma 2.1; §3.1, pp. 8–9, reflection definitions and Fact 1. Section 2.1 also records the polynomial equivalence of CF, EF, and ER. Fact 1 is the relevant conditional specialization principle, rather than an unconditional assertion about a decider's soundness proofs.
- Emil Jeřábek, [*Dual weak pigeonhole principle, Boolean complexity, and derandomization*, author manuscript dated 25 November 2003](https://users.math.cas.cz/~jerabek/papers/wphp.pdf), §2, pp. 12–14, Lemmas 2.4 and 2.5 and their proofs. This supports the circuit/formula conversion, not an assertion that arbitrary equivalent circuits have short equivalence proofs.
- Stephen A. Cook, [*Feasibly Constructive Proofs and the Propositional Calculus*, STOC 1975 preliminary version, pp. 83–97](https://www.karlin.mff.cuni.cz/~krajicek/cookpv.pdf), §5, Definition 5.4, p. 93; §6, ER Simulation Theorem 6.8 and the subsequent simulation sketch, p. 95. The definition explicitly depends on the algorithm chosen to evaluate formulas. The sketch treats the concrete evaluation computation and definitional clauses. The theorem's proof is omitted in this preliminary version; the following simulation argument is a sketch, not a complete proof reproduced here.

As a supporting example with a different target, Jan Krajíček's [*Consistency of circuit evaluation, extended resolution and total NP search problems*, author-hosted 13-page manuscript](https://www2.karlin.mff.cuni.cz/~krajicek/defc.pdf), §2, pp. 5–8, states and proves Theorem 2.1: a width-w CNF in n variables with an ER refutation π reduces by a clause substitution of width at most max(w,3) to Γ(0,s,k), for k=O(n k(π)) and s≤k/3, where k(π) counts proof clauses. Its Γ formulas encode a different reflection principle from L011's H_(A,N). This is supporting evidence for the method, not a full statement match or a bound in the notebook's binary encoding. The manuscript has no version/date on its title page; accessed 2026-09-26.

## Mathlib

Coverage: **not checked** for reflection specialization, circuit substitution, CF/EF/ER simulations, or the exact L011 encoding. No library identifier or absence claim is asserted. The cited results cover standard components; no cited theorem here establishes the entire local target with its specific evaluator and binary proof accounting.
