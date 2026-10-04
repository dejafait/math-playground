# ER-to-formula-IPS translation: completed source assessment

TARGET: Determine whether polynomial binary ER refutations of 3CNFs yield balanced F₂ noncommutative tree formula-IPS certificates of polynomial total binary length.
CHECKED: 2026-10-04
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searches on 2026-10-04 screened the reverse ER/EF translation, tree versus circuit IPS, extension elimination and stronger noncommutative simulations. They located the clause-form Frege theorem and explicit EF degree qualification in Forbes–Shpilka–Tzameret–Wigderson, and a revised Grochow–Pitassi author manuscript. Queries and actual reading scope appear below; no matching general ER-to-tree theorem was found in this bounded search.
SOURCE_EVIDENCE: Read Li–Tzameret–Wang, https://arxiv.org/pdf/1412.8746v4, Definitions 1.2/1.6, Theorems 1.4/3.4, Lemmas 3.5–3.7 and 4.2; Forbes–Shpilka–Tzameret–Wigderson, https://toc.cs.uchicago.edu/articles/v017a010/v017a010.pdf, Theorems 1.2/1.4 and Remark 1.3; Grochow–Pitassi, https://arxiv.org/pdf/1404.3820v1, Proposition 2.2 / §1.3 and §2.2–2.3, and https://www.cs.toronto.edu/~toni/Papers/jacm-gp.pdf, Definition 1.1 / footnote 1, Theorem 3.5 / Lemma 3.6 and §8.1. Reuse the ready CF/EF/ER conversion coverage.
COMPARISON: The known reverse tree-certificate theorem starts from Frege; the unconditional EF comparison produces shared commutative circuit certificates, without a polynomial-degree guarantee. Balancing is covered after a tree certificate exists. None of the inspected statements bounds the extension-elimination tree cost by the original ER binary length.
GAP: Establish or refute the polynomial cost of the direct extension-substitution route while retaining formal noncommutative identities over only the original variables and axiom placeholders. A bound polynomial in an uncontrolled unfolded-size parameter would be conditional progress, not the requested unrestricted reverse simulation.
REASON: The supplied object and simulation direction changed beyond the forward assessment. Known results now cover the Frege and balancing stages; the identified remaining applicability and binary-accounting difference warrants one bounded mathematical audit. This review establishes neither the general reverse translation nor its impossibility or novelty.
SCOPE: Standard ER refutations of well-formed width-at-most-three CNFs, with fresh acyclic AND definitions and complete binary encoding. Desired certificates remain division-free fan-in-two F₂ noncommutative trees with formal identities C(x,0)=0 and C(x,A(x))=1 for the explicit original clause, Boolean and base-variable commutator axioms. The approved specialization concerns extension elimination and its cost; arbitrary circuit certificates, extension placeholders in the final axiom list and a presumed Frege simulation of EF are outside its conclusion.
COVERED_TARGET: Audit the direct ER-to-formula-IPS translation through extension substitution, bounding its binary cost in the total unfolded tree size and testing whether ER proof length controls that parameter.

The original TARGET is preserved from the pending assessment created after the forward audit. This turn completes its source comparison only. The [forward assessment](2026-10-03-shared-homogeneous-ips-ef.md), L017–L018 and all existing scripts remain unchanged. The [Clay problem page](https://www.claymath.org/millennium/p-vs-np/) was rechecked on 2026-10-04; the ordinary P=NP target remains unresolved.

## Gap, relevance and required threshold

The main gap remains a polynomial SAT algorithm or an unconditional separation. This reverse translation would be useful if hardness of every admissible formula-IPS certificate could then exclude short ER refutations. The forward screen does not supply that passage. Even a successful reverse translation would leave certificate lower bounds and the unrestricted decision-to-proof transfer missing.

The required bound is one fixed polynomial in T=2+|F|+|π|, with full binary descriptions of the original 3CNF and supplied ER refutation. It must include the original axiom list, the final tree certificate, balancing and identifiers. A polynomial bound in a larger explicit object is insufficient unless that object's size is itself controlled by T. No such control is asserted here.

The covered audit will keep U(π), the total tree size obtained by fully substituting extension definitions at their written occurrences in the proof, explicit. It will check original-CNF preservation, disappearance of all extension inputs, the applicable Frege theorem, formal rather than Boolean-only identities, and complete binary costs. Import the certificate and balancing constructions rather than reprove them. Test a valid ER family with repeated extension use, charging only occurrences actually used in its refutation; padding the proof with irrelevant definitions is not discriminating evidence.

Continue the direct route only if its size premise has been justified. A polynomial conditional bound with uncontrolled U is a restricted result. A superpolynomial unfolding cost would stop this literal-substitution mechanism, while leaving other certificates and reverse constructions open. No recurrence, example family or parameterized bound is derived in this literature turn.

## Search evidence

Targeted queries actually issued included:

- `"noncommutative" "IPS" "extended Frege" formula`
- `"non-commutative" "Frege" "Theorem 1.4"`
- `"extended Frege" "formula IPS" simulation`
- `"ER" "noncommutative" "certificate" formula`
- `"noncommutative" "IPS" "Extended Frege" "simulation" formula circuit`
- `"non-commutative IPS" "extension" variables`
- `"noncommutative" "Frege" "quasipolynomial" "Extended"`
- `"ER" "Frege" "extension variables" "exponential"`
- `"Algebraic Proof Complexity" "Tzameret" "Theorem 3.3" pdf`
- `"Characterizing Propositional Proofs" "2018" "noncommutative" Extended`
- `"Circuit complexity, proof complexity" "Theorem 3.5"`

Search snippets, bibliographic records, a proof-complexity zoo and talk announcements served only as discovery aids. Failed searches do not establish absence or originality.

## Inspected statements and applicability

1. **Li–Tzameret–Wang**, [*Characterizing Propositional Proofs as Non-Commutative Formulas*, arXiv:1412.8746v4, 11 September 2015](https://arxiv.org/pdf/1412.8746v4), 44 pages. Read the definitions and introduction, printed pp. 6–9; §2.2.1 and §3, pp. 13–18; and Lemma 4.2 with its proof, pp. 19–20. Theorem 1.4 gives polynomial formula certificates from Frege over Q or a prime field, including F₂. Theorem 3.4 goes through tree-like F-PC; Lemma 3.5 gives a fourth-power size bound in that proof's total formula size. Lemmas 3.6–3.7 handle commutation using base-variable commutators. Lemma 4.2 balances an existing division-free noncommutative tree with polynomial size. These cover known stages, not ER extension elimination. Retain this version's numbering.

2. **Forbes–Shpilka–Tzameret–Wigderson**, [*Proof Complexity Lower Bounds from Algebraic Circuit Complexity*, Theory of Computing 17(10), 2021](https://toc.cs.uchicago.edu/articles/v017a010/v017a010.pdf), 88 pages; read printed pp. 5–6, Theorems 1.2/1.4 and Remark 1.3. Theorem 1.2 explicitly pairs Frege with formula-IPS and EF with circuit-IPS. Remark 1.3 allows exponential degree in the EF output. Theorem 1.4 states the noncommutative Frege simulation for the clause polynomial system with Boolean and commutator axioms. This resolves the clause-versus-single-translation source question. It does not extend the input proof system to ER or EF. The further restricted-certificate results are not needed here.

3. **Grochow–Pitassi**, [arXiv:1404.3820v1, 15 April 2014](https://arxiv.org/pdf/1404.3820v1): read the EF comparison following Proposition 2.2 in §1.3, pp. 10–11, and §2.2–2.3, pp. 21–25. Also read [the 59-page author-hosted jacm-gp.pdf](https://www.cs.toronto.edu/~toni/Papers/jacm-gp.pdf), Definition 1.1 / footnote 1, printed 1:4; Theorem 3.5 / Lemma 3.6 and their construction passages, 1:19–22; §8.1, 1:42. The latter explicitly removes the earlier polynomial-degree restriction and retains shared gate references. It uses a placeholder January 2016 journal masthead; its final publication version was not established and is not silently substituted for v1. Its commutative circuit statements support the EF comparison, not the required noncommutative tree conclusion. Existing proofs-of-PIT-axioms qualifications for the opposite simulation remain unchanged.

4. **Chatterjee–Chatterjee–Ghosal–Mukhopadhyay**, [ECCC TR26-166, 4 September 2026 manuscript](https://eccc.weizmann.ac.il/report/2026/166/download), 70 pages. Rechecked Theorems 1.2 and 3.3, printed pp. 7 and 20, against the previously read scope. Their F₂ partially commutative formula simulation still concerns Frege with quasipolynomial overhead. This changed identity model is not a reverse ER-to-tree theorem. Its full proof is not an input to this audit. An author-hosted February 2026 manuscript returned by search was not read or used in place of the inspected ECCC version.

Reuse [the reflection foundation](../../foundations/06-reflection-specialization.md) for the previously screened CF/EF/ER representations and substitution results, and [the ER conventions](../../foundations/05-refutation-systems-and-simulation.md) for freshness and binary proof length. Circuit substitution preserves sharing; it cannot be cited as the missing tree-size estimate. No essential source for the approved audit remains unread. The optional Buss chapter PDF returned an access error and is not used; its search excerpt supplies no theorem input.

## Redundancy, decision and classification

L016–L018 concern the forward direction and do not duplicate this reverse cost question. The stops in [ATTEMPTS/010](../../ATTEMPTS/010-automatic-decider-to-er-simulation.md), [ATTEMPTS/013](../../ATTEMPTS/013-canonical-kpt-universal-recovery.md) and [ATTEMPTS/014](../../ATTEMPTS/014-dropping-complete-output-cover-premises.md) remain applicable to their own missing proof premises. This audit will not infer a short proof from external correctness or reopen those premises.

SPECIALIZE approves the exact covered audit: import the Frege certificate and balancing theorems, then investigate only extension elimination, formal applicability and full binary cost. It does not approve treating the general TARGET as a known theorem. A failed unfolding test would refute a construction, not the existence of some other small certificate and not P=NP.

The completed step is EXPLORATION / LITERATURE / NOVELTY_UNCHECKED. It supplies new source scope and an actionable bounded test, with no mathematical derivation or claimed progress beyond the checked literature. Mathematical exploration turns used remains 0. The reverse hypothesis justified this review; the covered audit is ready for the next mathematical turn without further browsing.

## Mathlib

Coverage: **not checked** for the reverse translation, extension elimination or IPS/propositional simulations. The named direct sources above match supporting results with the stated proof-system and representation restrictions. No full source match, Mathlib theorem identifier or library-absence claim is asserted.
