# Parallel witnessing and complete output covers

## Hypotheses

This note compares cited witnessing results with the proposed two-round solver-or-antichecker transfer. It constructs no cover and proves no transfer. Retain a supplied two-round strategy, its polynomial EF proofs, and an externally correct SAT comparison circuit within the permitted size bound as conditional inputs. General KPT does not promise two rounds. The [assessment](../drafts/literature/2026-09-27-kpt-polynomial-output-cover.md) specifies the proposed cover and its proof requirement.

## Conclusion

**Parallel witnessing is still adaptive.** Cook–Thapen Theorem 7 below, for an increasing PV term α with the stated PV-provable bound α(x)<|x|, starts from PV+BB(α,PV) proving ∀x∃y∀z φ(x,y,z), with φ an ∃ᵇPV formula. It supplies a constant r, a term s(x,z₁,…,zᵣ) and PV functions f₁,…,fᵣ, with a PV proof of the universal closure of the disjunction of

∃i<α(s)ʳ φ(x,[fⱼ(x,z₁,…,zⱼ₋₁)]ᵢ,[zⱼ]ᵢ), for j=1,…,r.

Their first-order PV is the theory called PV1 here. The displayed lists retain earlier counterexample sequences as arguments. The corresponding author-manuscript statement is Theorem 4.3.

**The polynomial-list generalization.** Ježil–Tsintsilidas Definition 1.2 specifies candidate lists per interaction history. Their Theorem 4.11, for j≥1, a PV function b provably bounded by the identity, and a PVⱼ term t, witnesses ∀x∃y∀z≤t φ with open matrix φ proved in PVⱼ+BB(Σᵇⱼ,b) by a student in ST^(Σᵖⱼ₋₁)[O(1),poly(b)]. At j=1 and b(n)=n this gives constant rounds and polynomially many candidates per round. Definition 4.7 and the proof retain access to earlier teacher replies. No claim about the union of the lists over different histories is in this conclusion. Their Theorem 1.4 requires a nonuniform hierarchy separation and an unbounded round function; it does not rule out this particular two-round proposal under SAT∈P.

**Closest EF transfer.** Pich–Santhanam's feasible-antichecker theorem requires an S¹₂-provably correct polynomial-time generator. Its following discussion leaves the existential version's earlier-assignment dependence unresolved. Both inspected versions retain that distinction: arXiv v1 Theorem 7 and ECCC Theorem 10. Neither gives the proposed complete-output coverage proof.

The comparison is about the actual conclusions of these statements. An adaptive list, a list covering every relevant output of a fixed map, and an EF proof of that coverage are different specifications. No impossibility, unprovability, or novelty conclusion for the proposed cover follows. The existing [substitution and representation inputs](06-reflection-specialization.md) remain sufficient for the syntactic operations in a later test; they do not supply its missing coverage premise.

## Proof

Imports by precise citations, without reproof or a new specialization:

- Stephen Cook and Neil Thapen, [*The strength of replacement in weak arithmetic*, arXiv:cs/0409015v1](https://arxiv.org/pdf/cs/0409015v1), submitted 8 September 2004: §4, definition of BB(α,PV), pp. 13–14; Theorem 7 and proof, pp. 15–16. The retrieved rendering has a cover date of 14 November 2018; this is not treated as a new arXiv submission. The [16-page author manuscript](https://www.math.cas.cz/~thapen/cook.pdf), linked by Thapen under the 2006 ACM TOCL article, has the corresponding Theorem 4.3 and proof on manuscript pp. 12–13. Its text extraction loses some symbols, so the arXiv statement was used to resolve the notation. The journal citation is ACM TOCL 7(4), 749–764 (2006); journal pagination is not substituted for manuscript pagination.
- Ondřej Ježil and Dimitrios Tsintsilidas, [*Parallelism and Adaptivity in Student-Teacher Witnessing*, arXiv:2602.19934v1](https://arxiv.org/pdf/2602.19934v1), 23 February 2026: Definition 1.2, pp. 6–7; Theorem 1.4, p. 7; Theorems 1.6–1.8, p. 8; Definition 4.7, p. 23; Theorem 4.11 and proof, p. 24. Section 4.1, pp. 21–22, was also read for the oracle and case-definition hypotheses. The separation theorem's statement was inspected for applicability; its proof is not imported.
- Ján Pich and Rahul Santhanam, [*Towards P≠NP from Extended Frege lower bounds*, arXiv:2312.08163v1](https://arxiv.org/pdf/2312.08163v1), 13 December 2023: §3, Theorem 7, proof and subsequent discussion, pp. 19–20. Also inspected the [ECCC TR23-199 download](https://eccc.weizmann.ac.il/report/2023/199/download/), 35 pages, cover dated 9 December 2023, retrieved 27 September 2026: §4, Theorem 10, proof and discussion, pp. 25–26. These are distinct layouts and theorem numbers; the relevant generator premise and dependence obstacle agree. No revision chronology is inferred from crawl dates.

## Mathlib

Coverage: **not checked** for parallel witnessing, complete output covers, or the proposed EF transfer. These named sources support witnessing and proof operations; none has been identified as a full match for the cover-transfer statement.
