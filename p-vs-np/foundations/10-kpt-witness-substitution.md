# KPT witnessing and the scope of canonical substitution

## Hypotheses

This is a source comparison for the two-round repair proposed after Pich–Santhanam's existential-antichecker discussion. It supplies no new substitution argument or transfer theorem. Retain their PV1-provable existential solver-or-antichecker statement as an **unproved additional premise**. SAT∈P is a hypothetical external assumption, not an arithmetic axiom supplied with a proof.

The original KPT result yields a proof-dependent constant number of rounds. Restricting the proposed test to two rounds is an additional restriction on the supplied strategy, not a consequence of KPT. The one-sorted PV1 convention in Pich–Santhanam and the two-sorted VPV1 convention in Carmosino–Kabanets–Kolokolova–Oliveira are kept distinct.

## Conclusion

**Imported witnessing statement.** In the quantifier-free PV-language case of Krajíček–Pudlák–Takeuti Theorem A, a PV1 proof of ∀a∃u∀z R(a,u,z) yields finitely many polynomial-time terms t₁,…,t_c and a PV1 proof of

\[
 \forall a,z_1,\ldots,z_c\quad
 \bigvee_{i=1}^{c} R(a,t_i(a,z_1,\ldots,z_{i-1}),z_i).
\]

The number c is constant for a fixed proof; the later terms retain their displayed arguments. This is an imported theorem, not a claim that every strategy can be compressed to c=2 or to one noninteractive witness.

**Imported substitution statement.** Pudlák's Lemma 2.1, already assessed in the [reflection note](06-reflection-specialization.md), permits circuit substitution into a supplied CF proof with polynomial overhead in its length and the substitution circuits. Jeřábek's Lemmas 2.4–2.5 support the stated EF/CF conversions. These statements supply the syntactic operation; they do not certify a substituted circuit's intended SAT-search behavior.

**Exact comparison with the proposed repair.** Pich–Santhanam §3 gives the solver-or-antichecker instance and explains why the dependence of later outputs on earlier satisfying assignments prevents their direct EF argument. Their Theorem 7 separately assumes an S^1_2 proof of a uniform generator's guarantee. For a proposed canonical search function W_A, the source's solver-correctness condition would read

\[
 \forall x,y\in\{0,1\}^{n},\quad
 \operatorname{SAT}_n(x,y)\ \longrightarrow\
 \operatorname{SAT}_n(x,W_A(x)).
\]

This display identifies a **possible missing proof obligation**, not an established theorem or a necessary condition for every possible repair. Mere availability of W_A as a polynomial-time term is not the formal premise of Theorem 7. Whether the two-round application can avoid proving this full condition, for example by needing only certified concrete earlier witnesses, remains untested here. No equivalence with rejection soundness or with EF polynomial boundedness is asserted.

**Closest inspected round-elimination comparison.** Carmosino–Kabanets–Kolokolova–Oliveira Theorem 5.1 states that VPV1 cannot prove both their infinitely-often polynomial circuit upper bound for NP and their uniform NP⊈P assertion. Its proof uses formal counterexample existence and witnessing to eliminate equivalence queries. It is not a theorem obtaining ordinary EF proofs from an externally correct SAT decider. The input lengths in that argument may change within polynomial bounds.

## Proof

Imports by precise citations and comparison of their stated scopes; no new mathematical proof is supplied.

- Krajíček, Pudlák, Takeuti, [*Bounded arithmetic and the polynomial hierarchy*, Annals of Pure and Applied Logic 52 (1991), 143–153](https://www.karlin.mff.cuni.cz/~krajicek/kpt.pdf), §1, pp. 144–146: universal-theory setup, Theorem A and its first, Herbrand-based proof, p. 145. The theorem has a more general ∃Πᵇᵢ matrix; only its polynomial-time, quantifier-free PV1 case is used above. The [second author-hosted copy](https://users.math.cas.cz/~pudlak/KPT.pdf) was also inspected. The later clean statements below corroborate the scanned notation.
- Pich, Santhanam, [*Towards P≠NP from Extended Frege lower bounds*, arXiv:2312.08163v1](https://arxiv.org/pdf/2312.08163v1), submitted 13 December 2023: §2.2, pp. 11–12, for PV1's polynomial-time function symbols; §3, Theorem 7, its proof and existential-witnessing discussion, pp. 19–20. The [earlier generator note](09-antichecker-existence-and-generation.md) records the full assignment/pairing interface. No theorem here proves the canonical repair impossible.
- Carmosino, Kabanets, Kolokolova, Oliveira, [*LEARN-Uniform Circuit Lower Bounds and Provability in Bounded Arithmetic*, author manuscript dated 7 July 2021](https://www.dcs.warwick.ac.uk/~igorcarb/documents/papers/CKKO21.pdf), 65 PDF pages: Theorems 2.15–2.16, printed pp. 18–19; §5.1, equations (3)–(4), Theorem 5.1 and proof, printed pp. 46–48 (PDF pages 48–50). The theorem's formal-provability assumptions, rather than external complexity assumptions alone, are essential to the cited statement.
- Ježil, Tsintsilidas, [*Parallelism and Adaptivity in Student-Teacher Witnessing*, arXiv:2602.19934v1, 23 February 2026](https://arxiv.org/pdf/2602.19934v1), Definition 1.2 and Theorems 1.4, 1.6–1.7, pp. 6–8. The clean general KPT statement supports the displayed dependence. Theorem 1.4 requires a nonuniform hierarchy-separation hypothesis and unbounded round functions, so it is not a two-round obstruction under SAT∈P. Its separation proof is not imported.

The exact source-read/search record and remaining test are in the [assessment](../drafts/literature/2026-09-27-canonical-kpt-witness-substitution.md). No source in that bounded comparison supplies a full match, and failure to locate one is not evidence of novelty or unprovability.

## Mathlib

Coverage: **not checked** for KPT witnessing, the canonical substitution target, or the supporting CF/EF and round-elimination results. The named sources support individual components; none is identified as a full library match for the proposed repair.
