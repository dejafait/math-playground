# PV sound-decider existence: source-reading notes

Saved during the literature-only review on 2026-09-27. No mathematical derivation is recorded here.

The reviewed target is the exact existence question saved in [its assessment](literature/2026-09-26-pv-sound-decider-existence.md). It asks for some externally correct polynomial-time SAT decider with PV-provable rejection soundness. It does not require a PV proof of both directions of correctness, and does not concern every implementation of a decider.

Sources inspected so far:

- Cook, [STOC 1975 preliminary version](https://www.karlin.mff.cuni.cz/~krajicek/cookpv.pdf), Definition 5.4, Main Theorem 5.5, and Lemma 5.8, p. 93; ER Simulation Theorem 6.8, p. 95. Theorem 5.5 characterizes PV-verifiable proof systems by a formally verified ER simulation. Lemma 5.8 supplies formal soundness of ER itself. Neither statement selects the required SAT decider from SAT∈P. The preliminary paper omits some proof details.
- Krajíček, [*Proof complexity generators*, author manuscript](https://www.karlin.mff.cuni.cz/~krajicek/k4.pdf), Chapter 7 introduction, pp. 83–84. The discussion explicitly separates ER lower bounds from complexity-class separation and discusses a SAT algorithm whose soundness requires stronger induction. This is a warning about an unproved implication, not a counterexample satisfying SAT∈P.
- Pich–Santhanam, [arXiv:2312.08163v1](https://arxiv.org/pdf/2312.08163v1), submitted 13 December 2023, manuscript dated September 2023, §1.1.1, pp. 2–5: Theorem 1, Proposition 1, Corollary 2, and their surrounding arguments. Conditional witnessing supplies a concrete alternative transfer mechanism. The distinction between truth of witnessing formulas and their formal provability is retained.
- The [ECCC TR23-199 PDF](https://eccc.weizmann.ac.il/report/2023/199/download), dated 9 December 2023, is a different 35-page presentation. Its Proposition 1, p. 3, concerns a transfer to NP⊈P/poly; the following paragraph explicitly leaves a transfer to P≠NP outside that argument. The arXiv version has 29 pages and different theorem numbering. Do not mix their citations.

The comparison was subsequently completed in the [assessment](literature/2026-09-26-pv-sound-decider-existence.md), with precise imports in the [source note](../foundations/07-formal-soundness-and-transfer-limits.md). These interim notes are retained as a reading record. The journal PDF at https://dl.acm.org/doi/pdf/10.1145/3801091 returned HTTP 403; no theorem from that version has been used. A search-result citation to CCC 2024 article 22 led to a different paper and has been excluded.

The Bogdanov–Talwar–Wan paper is an unread lead for a possible later target. No claim about its theorem has been imported. The current review must not turn a counterexample finder at unspecified lengths into a witness at the given input length.

## Mathlib

Coverage: **not checked** for the exact existence claim or the supporting formal-soundness and witnessing results.
