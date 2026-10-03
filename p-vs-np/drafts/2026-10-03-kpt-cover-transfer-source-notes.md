# Source scope for the supplied-cover transfer

## Hypotheses

This is a citation and applicability note for the unchanged [conditional transfer assessment](literature/2026-09-27-kpt-output-cover-transfer.md). The proposed two-round strategy, its EF translations, complete-output lists and coverage proofs are supplied hypotheses. Their existence does not follow here from KPT or SAT∈P. The assignment verifier must retain the checked implementation or separately supplied short identification proofs.

The target concerns ordinary EF with a polynomial bound in full binary input length. Nonuniformly supplied proof data and polynomial-time generation are different requirements. No mathematical case split or transfer proof is performed in this literature turn.

## Conclusion

**Closest ordinary-EF statement, imported by citation.** For fixed k≥3, Pich–Santhanam Theorem 7 assumes an S¹₂-provably correct polynomial-time solver-or-antichecker generator. Given that premise, lack of polynomial boundedness of EF yields infinitely-often size-n^k SAT circuit lower bounds. Its subsequent KPT discussion preserves all earlier replies and does not settle the supplied-cover inference.

**Related stronger-system statement, scope only.** Arteche–Khaniki–Pich–Santhanam Theorem 19 links nonboundedness of iEFtt(h,n₀) to #P⊈FP/poly. Definition 17 adds average-case hardness axioms; Corollary 20 obtains a statement about iEF when those axioms have short iEF proofs. These are different premises and systems from the saved ordinary-EF target. Neither statement is imported as its solution.

**Supporting operations reused.** Existing source assessments cover adaptive and parallel witnessing, circuit substitution, and CF/EF conversion. These permit syntactic operations on supplied proofs; none supplies the proposed complete-output coverage proofs. A general reproof of witnessing or a new proof compiler would duplicate that coverage.

## Proof

Imports and scope comparisons by precise citations; no new proof is supplied.

- Ján Pich and Rahul Santhanam, [*Towards P≠NP from Extended Frege lower bounds*, arXiv:2312.08163v1](https://arxiv.org/pdf/2312.08163v1), 13 December 2023, §3, Theorem 7, its proof and the following displayed interactive strategy and discussion, printed pp. 19–20. Read for this exact target. The predicate includes assignment certification and the pairing relation, rather than only the solver circuit. The [author-hosted 29-page manuscript](https://users.ox.ac.uk/~coml0742/papers/eopt.pdf), retrieved 3 October 2026, was also read at the same section and theorem number; its cover says September 2023. No newer-version claim is inferred from retrieval dates.
- Noel Arteche, Erfan Khaniki, Ján Pich and Rahul Santhanam, [*From Proof Complexity to Circuit Complexity via Interactive Protocols*, ICALP 2024, LIPIcs 297, article 12](https://drops.dagstuhl.de/storage/00lipics/lipics-vol297-icalp2024/LIPIcs.ICALP.2024.12/LIPIcs.ICALP.2024.12.pdf), DOI 10.4230/LIPIcs.ICALP.2024.12. Read Definition 17, Lemma 18 and its proof, Theorem 19 and Corollary 20 with their proofs, printed pp. 12:16–12:17, plus the introductory statements and proof outline on pp. 12:4–12:6. The short transfer argument uses the preceding sum-check simulation. No claim of having checked every underlying formalization proof is made; the simulation is not a mathematical input here.
- Reuse Cook–Thapen Theorem 7 (author-copy Theorem 4.3) and Ježil–Tsintsilidas Definition 1.2 / Theorem 4.11 through the sufficient [parallel-witnessing assessment](literature/2026-09-27-kpt-polynomial-output-cover.md) and [named source citations](../foundations/11-kpt-output-covers.md). The distinction between per-history lists and history-independent complete-output coverage is retained.
- Reuse Pudlák [Lemma 2.1 and Fact 1](https://arxiv.org/pdf/2007.14835v1), pp. 5 and 9, and Jeřábek [Lemmas 2.4–2.5](https://users.math.cas.cz/~jerabek/papers/wphp.pdf), pp. 12–14, through the sufficient [reflection assessment](literature/2026-09-26-current-target.md) and [source note](../foundations/06-reflection-specialization.md). The latter conversion requires a formula conclusion. These references support proof operations, not universal selector soundness or the full conditional inference.

The completed search/read record, required threshold and continuation/stop test are in the assessment. No inspected theorem is identified as a full match. Failed searches certify neither novelty nor impossibility.

## Mathlib

Coverage: **not checked** for the conditional transfer, complete-output covers or the supporting witnessing and proof-system statements. Precise theorem names and direct primary links are retained above. The supporting imports and the full-statement gap are distinct; no library absence is claimed.
