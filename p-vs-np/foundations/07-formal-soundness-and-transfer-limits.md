# Formal soundness and the remaining ER transfer

## Hypotheses

Keep the SAT encoding and evaluator of L011–L013. The reviewed claim asks whether SAT∈P supplies **some** externally correct polynomial-time decider B and a finite PV proof that a rejected well-formed formula has no satisfying assignment. External completeness of B is part of the target; rejection soundness alone does not assert it. No such B or proof is supplied here.

Cook uses equational PV. Modern sources also use its first-order conservative extension PV1 and Buss's S^1_2. These theory names and the scope of their conservation results must be retained when applying a citation. A theorem about propositional proof existence does not by itself provide a single arithmetic proof.

## Conclusion

The following are cited inputs and limitations, not a new decider-existence theorem.

1. **Cook's formal-soundness characterization.** A tautology proof system is PV-verifiable exactly when ER p-verifiably simulates it. ER itself is PV-verifiable. Bounded propositional translations of a fixed PV-provable equation have polynomial-length ER proofs under the theorem's bounding-value condition.
2. **Scope of the proof-complexity program.** Krajíček explicitly distinguishes ER lower bounds from a complexity-class separation. The discussion allows that a polynomial-time SAT algorithm's soundness might need reasoning stronger than the weak theory. It supplies neither a counterexample to the reviewed implication nor an existence theorem for B.
3. **Conditional alternatives.** Pich–Santhanam's witnessing theorems retain an additional witness/provability premise. Their barrier for an unconditional transfer to NP⊈P/poly is explicitly distinguished from a transfer to P≠NP. Neither direction settles this notebook's exact one-sided PV-existence question.

## Proof

Imports by precise citation; no new proofs are given.

- Stephen A. Cook, [*Feasibly Constructive Proofs and the Propositional Calculus*, STOC 1975 preliminary version](https://www.karlin.mff.cuni.cz/~krajicek/cookpv.pdf), Definition 5.4, Main Theorem 5.5, Lemma 5.8, p. 93, and ER Simulation Theorem 6.8, p. 95. Read the statements, the ER soundness argument on p. 92, and the simulation sketch on p. 95. The definition depends on the evaluator; some proof details are omitted in this preliminary version.
- Jan Krajíček, [*Proof complexity generators*, 167-page author manuscript](https://www.karlin.mff.cuni.cz/~krajicek/k4.pdf), Chapter 7 introduction, pp. 83–84; accessed 2026-09-27, no manuscript date identified. Read the discussion of ER bounds, consistency with S^1_2(PV), and the stronger-induction scenario. This is a scope warning, not a theorem disproving the existence of B.
- Ján Pich and Rahul Santhanam, [*Towards P≠NP from Extended Frege lower bounds*, arXiv:2312.08163v1](https://arxiv.org/pdf/2312.08163v1), submitted 13 December 2023, manuscript dated September 2023, §1.1.1, pp. 2–5: Theorem 1 and Corollary 2 with their preceding arguments. Corollary 2 distinguishes adding true witnessing axioms from proving their arithmetic version in S^1_2; only the latter uses ordinary EF in its second item. Section 2.2, pp. 11–12, supplies the theory conventions.
- The same authors' [ECCC TR23-199 version, dated 9 December 2023](https://eccc.weizmann.ac.il/report/2023/199/download), Proposition 1 and proof, p. 3, and its qualification, p. 4: a fixed-system transfer to NP⊈P/poly would imply NEXP⊈P/poly. The qualification explicitly leaves the weaker P≠NP conclusion outside this argument. Read also §1.2, pp. 4–6, and Theorem 2, p. 8. This 35-page version has different numbering from the 29-page arXiv version.

**Applicability limit.** Cook's theorem explains what a supplied formal soundness proof buys. It does not infer that proof from semantic correctness. The witnessed alternatives concern bounded propositional correctness under additional hypotheses. No equivalence between the exact decider-existence claim, PV-provable full SAT search, and ER polynomial boundedness is asserted here. Such a comparison would have to check both directions and the evaluator, not just cite similar terminology.

## Mathlib

Coverage: **not checked** for the full existence claim or the supporting PV, ER, and witnessing results. The named theorems above support conditional components; no full-statement match is claimed.
