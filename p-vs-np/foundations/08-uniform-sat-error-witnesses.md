# Uniform SAT error witnesses and their quantifiers

## Hypotheses

This note imports source statements for the comparison with Pich–Santhanam, arXiv:2312.08163v1, Corollary 2. It constructs no witnessing function and proves no new transfer. The advice allowance is u(n)=0. The clock exponent k, universal machine, and encoding are fixed as in that source.

Bogdanov–Talwar–Wan use canonical SAT-search algorithms: a nonzero output is checked as a satisfying assignment, so failure on a satisfiable formula is recorded by output 0. Their string encoding permits zero padding. These conventions are not silently identified with the notebook's fixed CNF encoding and evaluator. Canonicalization and universal simulation would also require clock accounting in an application.

## Conclusion

The deterministic **Bogdanov–Talwar–Wan Theorem 1** assumes P≠NP. For each polynomial-time search algorithm A, it supplies a polynomial-time procedure on A, 1^n and its running-time bound that outputs a satisfying formula/assignment pair rejected by A for infinitely many n. The formula has length **exactly n** on those successful inputs. Its Lemma 1 instead gives lengths N in n^(1/r)<N≤n under an additional eventual-failure premise; r denotes the source's growth exponent, renamed here to avoid confusion with the transfer's clock exponent k.

For **Pich–Santhanam Corollary 2**, one fixed polynomial-time f must meet w_n^(k,0)(f) for every sufficiently large n. The formulas quantify over all descriptions A of length at most log n, simulated for n^k steps. Their requirement is conditional on an error at that very length: if the clocked search algorithm fails on some satisfiable n-bit formula, f, given its represented circuit, returns an n-bit formula and a satisfying assignment exposing an error. No error needs to be produced when the algorithm is correct on that length.

Item 1 uses the additional witnessing axioms in EF+w^(k,0)(f). Item 2 requires S^1_2 ⊢ W_(n0)^(k,0)(f) for some n0 and uses ordinary EF. Both conclusions are the stated fixed-exponent exclusion SAT∉Time[n^Ω(k)] at zero advice, conditional on the respective proof system not being polynomially bounded. A single fixed k is not a separation from all polynomial-time algorithms.

**Applicability comparison.** Theorem 1's exact-length output clause does not supply the required all-large-length, pointwise conditional guarantee over the growing set of descriptions. Its P≠NP hypothesis cannot be assumed to obtain an unconditional P-versus-NP resolution. No S^1_2 proof of the required W statement is supplied by the inspected finder theorem or argument. This rules out a direct import of those guarantees; it proves neither that an upgraded finder is impossible nor that its formalization is unprovable.

## Proof

Precise citations and comparison of their explicit hypotheses; no new mathematical proof is asserted.

- Bogdanov, Talwar, Wan, [*Hard instances for satisfiability and quasi-one-way functions*, author manuscript dated 10 November 2009](https://andrejb.net/pubs/quasicrypto-ics.pdf), associated with ICS 2010: Theorem 1 and search convention, printed p. 3; §3.1, pp. 7–8; Lemma 1 and its proof, pp. 8–9; final procedure D and proof of Theorem 1, p. 9. The final procedure filters for length n after calls with parameters between n and n^r; its proof concludes infinitely-often success. The exponent used for the intermediate formula size depends on the represented algorithm. This is a known algorithmic result, not an arithmetic-provability theorem.
- The [11-page Columbia author submission](https://www.cs.columbia.edu/~atw12/papers/quasicrypto-ics-submit.pdf), undated in the inspected text, agrees on Theorem 1, printed p. 2, and on the final length filter and infinitely-often conclusion, pp. 6–7. Only these corresponding portions were cross-checked. Randomized statements and abstract variants are not substituted for the deterministic theorem.
- Pich, Santhanam, [*Towards P≠NP from Extended Frege lower bounds*, arXiv:2312.08163v1](https://arxiv.org/pdf/2312.08163v1), submitted 13 December 2023, manuscript dated September 2023: definition of w_n^k(f), p. 3; restricted-nonuniformity construction, p. 4; W definition, Corollary 2 and following qualification, p. 5. Those definitions and both items were read. Their pointwise disjunction, rather than an assumption that every algorithm is wrong, is essential.
- The [9 December 2023 ECCC TR23-199 version](https://eccc.weizmann.ac.il/report/2023/199/download), p. 7, warns about the lengths produced by the earlier finder. In light of the original Theorem 1, this comparison must be stated as a missing guarantee at a prescribed erroneous length, not as a claim that the final finder never promises length n. This is our reconciliation of the source statements; their theorem numbering is not mixed.

The differences already prevent this direct application at the level of the cited statements. No reproof, padding repair, separation, or counterexample to a stronger witnessing theorem is claimed. The [assessment](../drafts/literature/2026-09-27-uniform-sat-error-witness.md) records discovery scope and the resulting research decision.

## Mathlib

Coverage: **not checked** for the full comparison or supporting witnessing and transfer results. The named source theorems above are supporting inputs; no full matching theorem for the missing strengthened witness is claimed.
