# Changing the output by coefficient reduction: completed assessment

TARGET: Test whether local Boolean/commutator reduction of L021's clause-placeholder coefficients yields original-axiom noncommutative circuit-IPS certificates with size and formal degree polynomial in the supplied ER binary length.
CHECKED: 2026-10-04
DECISION: EXPLORE
SEARCH_EVIDENCE: Target-specific queries screened IPS multilinearization, polynomial-degree EF simulations and noncommutative degree reduction; they located restricted correction theorems and Hrubeš's characteristic-two hardness result, but no inspected full match. Exact queries and reading scope appear below; supporting prior coverage is reused.
SOURCE_EVIDENCE: Read Forbes–Shpilka–Tzameret–Wigderson https://toc.cs.uchicago.edu/articles/v017a010/v017a010.pdf, §4.2, Propositions 4.4–4.6, Lemma 4.9 and Corollaries 4.10–4.11; Hrubeš https://users.math.cas.cz/~hrubes/PDFs/Mult.pdf, §2.1 Theorem 1, Corollary 2, Proposition 3 and §4 Theorem 7(ii)–(iii); rechecked Grochow–Pitassi https://www.cs.toronto.edu/~toni/Papers/jacm-gp.pdf, Definition 1.1/footnote 1 and degree definitions, and Li–Tzameret–Wang https://arxiv.org/pdf/1412.8746v4, Lemmas 3.6–3.7. Versions, pages and applicability are recorded below.
COMPARISON: Restricted commutative correction results require representations not supplied by L021. Generic multilinearization has a conditional hardness obstruction even over F₂. Neither comparison rules out an ER-specific different-output construction, but neither imports simultaneous polynomial size and degree for its complete formal noncommutative certificate.
GAP: Establish or refute a local multiplication update that retains both formal IPS identities using only original axioms, including the size and degree of Boolean/commutator correction terms. Reduced clause coefficients alone are insufficient; propagation through arbitrary supplied ER proofs remains unresolved.
REASON: The bounded comparison is complete and no essential source remains unread for a local formal audit. Approve a discriminating mathematical test rather than assume generic multilinearization preserves small circuits or repeat the same-output obstruction. No full theorem match or novelty claim is established.
LITERATURE_REASON: The changed hypothesis permits replacing the output polynomial using Boolean and commutator corrections; the prior ready assessment required computing the identical polynomial and supplies no coverage for this degree-reduction mechanism.
SCOPE: Original width-at-most-three CNFs and supplied fresh acyclic AND-extension ER refutations, T=2+|F|+|pi|, over the free noncommutative polynomial ring F₂<x,t>. The output may change and may be nonlinear in Boolean/commutator placeholders, but must use only the original axiom list, satisfy both formal IPS identities and have complete circuit size and final formal degree T^{O(1)}. Approval is for a bounded test, not a presumed positive construction or arbitrary-circuit identity algorithm.
COVERED_TARGET: Test whether local Boolean/commutator reduction of L021's clause-placeholder coefficients yields original-axiom noncommutative circuit-IPS certificates with size and formal degree polynomial in the supplied ER binary length.
COVERED_TARGET: Audit one multiplication update for Boolean/commutator reduction of L021's clause-placeholder coefficients, accounting for both formal IPS identities and polynomial shared size and formal degree of the complete original-axiom correction.

## Gap, relevance and required bound

The main gap remains a polynomial-time SAT algorithm or an unconditional exclusion of every such algorithm. The intermediate target seeks a different reverse certificate representation after L022 stopped small trees computing L021's identical output. Its plausible downstream use is to separate the cost of high formal degree from the cost of sharing. Polynomial degree would still leave tree conversion, general identity verification, all-certificate hardness and unrestricted decision transfer open.

The required global threshold remains one fixed polynomial in T for both full binary circuit size and final formal degree in independent x,t. L021 achieves O(T⁵) binary size without a degree bound; L022 proves a superpolynomial degree for its specific output. These do not settle the cost of changing that output. Solving only L019's fixed original CNF would duplicate its constant alternative certificate.

Both C(x,0)=0 and C(x,A(x))=1 must remain formal identities. Degree after the axiom substitution is irrelevant because that output is 1. A Boolean-equivalent reduced coefficient, a commutative quotient identity, or polynomial clause-sector degree without bounds on the remaining placeholder sectors does not meet the target.

## Search and actual reading

Queries issued on 2026-10-04:

- `"IPS" "multilinearization" circuit degree Boolean axioms`
- `"noncommutative" "IPS" "degree" extended Frege`
- `"Ideal Proof System" "low degree" "Extended Frege"`
- `"multilinearization" "circuits" "VNP" Boolean`
- `"noncommutative IPS" "degree reduction"`
- `"IPS" "polynomial degree" "Extended Frege" multilinearization`

Search results were discovery aids. The following primary passages determine the comparison; theorem labels refer to the specified versions.

**Forbes–Shpilka–Tzameret–Wigderson**, [*Proof Complexity Lower Bounds from Algebraic Circuit Complexity*, Theory of Computing 17(10), published 1 November 2021](https://toc.cs.uchicago.edu/articles/v017a010/v017a010.pdf). Read §4.2 and Propositions 4.5–4.6, printed pp. 29–32: commutative roABP multilinearization and correction witnesses retain controlled width; construction costs depend on input individual degree. Read Lemma 4.9 and Corollaries 4.10–4.11, statements and construction passages, pp. 34–37: correction for a low-degree sparse factor requires an already multilinear sparse/formula coefficient. Proposition 4.4, pp. 28–29, linearizes placeholders; it does not bound x-degree. The introduction, p. 4, records linear-degree certificate existence with exponential sparsity. These are supporting results, not a theorem for L021's arbitrary shared noncommutative coefficients. The published labels are **Proposition** 4.5 and **Corollary** 4.11, despite cross-references in the PDF saying “Theorem.” The missing representation and correction-degree bounds prevent direct import.

**Hrubeš**, [*On hardness of multilinearization, and VNP-completeness in characteristics two*, author manuscript dated 21 April 2015](https://users.math.cas.cz/~hrubes/PDFs/Mult.pdf), 13 pages; also located as [ECCC TR15-067](https://eccc.weizmann.ac.il/report/2015/067/). Read §2.1, pp. 3–4: Theorem 1 gives VNP-hard multilinearizations of constructible monotone 2-CNFs over every field; Corollary 2 is conditional on VP≠VNP; Proposition 3 gives VNP membership. Read Theorem 7 and its characteristic-two proofs, pp. 6–7: over F₂, width-three affine products can have VNP-hard multilinearization, whereas width-two products have O(n)-size multilinearizations. These statements are commutative; F₂ hardness is not silently promoted to p-projection completeness. They obstruct an unsupported generic canonical-multilinearization shortcut, not ER-specific certificate replacement or all low-degree Boolean representatives. No assumption VP≠VNP is adopted here. The final journal version was not inspected.

**Grochow–Pitassi**, [*Circuit complexity, proof complexity, and polynomial identity testing: The ideal proof system*, author-hosted 59-page jacm-gp.pdf](https://www.cs.toronto.edu/~toni/Papers/jacm-gp.pdf). Rechecked Definition 1.1 and footnote 1, printed 1:4, and semantic/syntactic degree definitions, 1:10. This manuscript removes the earlier polynomial-degree restriction because the EF simulation appeared to require unbounded degree. An old VP-IPS definition therefore supplies no missing bound. The placeholder January 2016 masthead is retained as a version qualification; no final-edition identity is inferred.

**Li–Tzameret–Wang**, [*Characterizing Propositional Proofs as Non-Commutative Formulas*, arXiv:1412.8746v4, 11 September 2015](https://arxiv.org/pdf/1412.8746v4). Rechecked Lemmas 3.6–3.7 and their proofs, printed pp. 17–18. They give formal base-commutator witnesses for changing product order in formulas, measured in formula size. They support the formal correction obligation, without giving a low-degree shared-circuit reduction theorem.

Reuse the [circuit assessment](2026-10-04-shared-noncommutative-er-circuit-ips.md) for finite-field axiom elimination and the original-axiom witness mechanism, and the [output-degree assessment](2026-10-04-assembled-certificate-formal-degree.md) for final formal degree versus formula size. The previously inspected finite-field elimination analogue is commutative and imposes no polynomial-degree conclusion for arbitrary ER depth. No rereading of its lower-bound proof is needed for this comparison. The established [uniform target](../../foundations/01-model-and-target.md) is unchanged.

**Unread optional leads.** Discovery returned *Symmetric Proofs in the Ideal Proof System* (MFCS 2025), *IPS Lower Bounds for Formulas and Sum of ROABPs* (FSTTCS 2025) and older IPS introductions. Their full theorem passages were not inspected and none is used to claim an exact match or impossibility. The older polynomial-degree wording is resolved by the inspected Grochow–Pitassi footnote. No essential source for the approved local audit is blocked. Search failure establishes neither novelty nor theorem absence.

## Approved bounded test and stopping decision

EXPLORE permits the preserved TARGET and the exact local audit listed in COVERED_TARGET. Perform one multiplication-update audit before attempting a whole ER translation. Specify the proposed reduced operands and the formal correction obligation, retaining ordered multiplication, both IPS identities, and the complete original clause/Boolean/commutator placeholder list. Charge every correction sector and sharing reference. Do not assume that gatewise reduction is a ring homomorphism or that independently small local updates yield a polynomial global recurrence.

Continue only if the update has a valid formal certificate and an explicit size/degree bound with a plausible polynomial propagation invariant in T. A new informative negative result would identify a concrete formal-identity failure, compulsory superpolynomial correction degree, or a size recurrence incompatible with that threshold. Polynomial degree of reduced clause coefficients alone is not a successful test. If the update relies on unrestricted canonical multilinearization, restrict it to a proved structural case or abandon that version; Hrubeš's theorem supplies no unconditional impossibility of the saved target. A test on L019's family may diagnose a specified correction rule, but its easy original CNF prevents an all-certificate conclusion.

The later ER-wide invariant remains explicitly unresolved. This approval does not authorize claiming a tree simulation, invoking deterministic arbitrary-circuit PIT, or importing a commutative theorem into the free ring without its applicability argument. Known restricted results should be cited in their stated scope; reproof is justified only for the identified sharing, noncommutative or full-correction difference.

Completed step: EXPLORATION / LITERATURE / NOVELTY_UNCHECKED, ACTUAL_TASK_TYPE literature_comparison. This assessment supplies new comparison evidence and a ready bounded mathematical test, not an imported full result, a reproduction or progress beyond the checked literature. No reduction identity, new degree estimate, lemma or mathematical script is derived. Mathematical exploration turns used remains 0; the review does not consume that budget.

## Mathlib

Coverage: **not checked** for the complete degree-reduction target or its local update. Named primary supporting results and direct links are preserved above and in the reused assessments. No full matching theorem, Mathlib identifier or library-absence claim is asserted.
