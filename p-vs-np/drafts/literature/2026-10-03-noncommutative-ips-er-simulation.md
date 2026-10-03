# Algebraic certificate simulations: completed source assessment

TARGET: Review the hypotheses and total binary proof-size overhead of noncommutative formula-IPS simulations into EF/ER for CNF contradictions with Boolean and commutator axioms.
CHECKED: 2026-10-03
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Targeted searches on 2026-10-03 for noncommutative IPS, EF/ER simulation, commutator axioms and degree restrictions located Li–Tzameret–Wang and a September 2026 partially commutative extension; exact queries and the theorem-level comparisons are recorded below.
SOURCE_EVIDENCE: Li–Tzameret–Wang, https://arxiv.org/pdf/1412.8746v4, Definition 1.2, Theorem 1.7 and its note, Theorem 4.1, Lemmas 4.4/4.8 and Theorem 4.11; Grochow–Pitassi, https://arxiv.org/pdf/1404.3820v1, Definition 1.7 and Theorem 4.1 with the soundness-specialization proof; Chatterjee et al., https://eccc.weizmann.ac.il/report/2026/166/download, Theorems 1.2/3.3 and selected Appendix B passages; exact versions, pages and reading limits are in drafts/2026-10-03-noncommutative-ips-source-notes.md. Reuse the existing EF/ER representation assessment.
COMPARISON: The inspected noncommutative theorem gives a quasipolynomial Frege bound over F₂, with a stated polynomial logarithmic-degree case. The new partially commutative theorem still states quasipolynomial overhead. General circuit-IPS/EF equivalence retains PIT-proof premises. None is imported as an unrestricted polynomial EF/ER simulation in total binary length.
GAP: Specialize the published logarithmic-degree F₂ case to the notebook's full binary encoding and original-CNF ER convention; charge every axiom, substitution copy, identifier and proof conversion. General-degree polynomial simulation, certificate existence and unrestricted EF/ER lower bounds remain unestablished here.
REASON: Import the known Frege machinery instead of reproving its identity witnesses. A concrete encoding specialization can identify algebraic certificates that already yield short ER proofs; park the unsupported unrestricted polynomial claim without declaring it impossible or reviving the KPT premises.
SCOPE: Division-free fan-in-two tree certificates over F₂ for 3CNFs with Boolean and all base-variable commutator axioms; dense variable labels, supplied balanced depth at most a·log(s+2) and syntactic degree at most b·log(n+2), for fixed a,b; s counts formula gates and n distinct base variables; the mathematical application must charge full binary input and output lengths. No general circuit, division, rational-coefficient, semantic-degree-only or arbitrary-degree polynomial simulation is approved.
COVERED_TARGET: Apply Li–Tzameret–Wang's logarithmic-degree F₂ simulation to supplied balanced noncommutative formula-IPS certificates for 3CNFs, accounting for total binary length through EF/ER conversion.

## Gap, intermediate target and continuation test

The main gap remains an unrestricted decision lower bound or polynomial-time SAT algorithm. At the proof-system branch, no superpolynomial EF/ER lower bound or unconditional decision-to-ER transfer is available. The intermediate target is to determine which algebraic formula certificates have a justified, genuinely polynomial proof translation. This could screen prospective hard CNF families: supplied short certificates in the covered fragment may already give short ER refutations. It provides no lower bound itself and does not turn formula-IPS lower bounds into EF lower bounds without a separately justified reverse simulation.

Preserve the initial screening requirements: distinguish formulas from circuits, fields, formal identities from Boolean evaluation, Boolean/commutator axioms, depth, syntactic degree, coefficient bit cost and proof construction. The required threshold is one polynomial in total CNF, axiom and supplied-certificate binary length. Gate counts and quasipolynomial bounds are not that threshold. A later mathematical test must establish that bound for the approved logarithmic-degree fragment without adding unprovided PIT or universal-soundness proofs. Continue on success; abandon or narrow the claimed specialization if substitutions or encoding exceed the threshold or require another unsupplied premise. No test or new bound is executed in this literature turn.

## Searches and material actually read

Queries included:

- `noncommutative IPS extended Frege polynomial simulation commutator axioms Li Tzameret Wang`
- `"noncommutative" "IPS" "syntactic degree" Frege`
- `"noncommutative IPS" "Extended Frege" polynomial simulation`
- `"non-commutative IPS" "EF" "polynomial"`
- `"noncommutative" "IPS" "extended Frege" "simulates"`
- `"non-commutative" "IPS" "polynomially" "extended Frege"`
- `"noncommutative IPS" "polynomial simulation" "EF"`
- `"non-commutative IPS" "extended resolution"`
- `Grochow Pitassi circuit complexity proof complexity PIT axioms Theorem 3.1 arxiv 2018 IPS`

Search snippets, secondary mirrors and event abstracts were discovery aids only. The [primary-source note](../2026-10-03-noncommutative-ips-source-notes.md) retains precise named citations in Hypotheses / Conclusion / Proof / Mathlib format. Its reading scope distinguishes inspected statements and proof passages from unread versions or unused full arguments. No essential source for the approved specialization is blocked. The search does not establish absence of a stronger EF theorem or originality of the local encoding exercise.

## Comparison with the required bound and previous failures

The closest statement is Li–Tzameret–Wang's Theorem 1.7 and its degree/depth note. Its detailed proof, Theorem 4.1, works with 3CNFs, so the approved application retains that restriction. The field is F₂; availability of deterministic verification over other fields is not used to extend the propositional simulation. Theorem 4.11 supplies polynomial proofs for homogeneous zero-identity formulas, but this is not a theorem that an arbitrary homogeneous certificate remains homogeneous after clause/Boolean-axiom substitution. The approved low syntactic-degree condition avoids silently making that assertion.

The September 2026 two-bucket result changes commutation hypotheses while retaining quasipolynomial Frege overhead. It is an inspected scope comparison, not a new essential dependency or a critically reviewed proof imported into this notebook. Grochow–Pitassi's general IPS comparison explicitly retains formal PIT-axiom proofs; external polynomial-time verification alone does not discharge them. The source versions and theorem numbering remain distinct.

L012 already supplies ER proofs for linear Tseitin parity, whereas this screen concerns formula identity certificates. [ATTEMPTS/010](../../ATTEMPTS/010-automatic-decider-to-er-simulation.md) rejects automatic simulation from checkability; no such inference is used here. [ATTEMPTS/014](../../ATTEMPTS/014-dropping-complete-output-cover-premises.md) and the canonical-recovery stop remain intact. The [existing reflection assessment](2026-09-26-current-target.md) adequately covers the syntactic EF/ER operations and is reused, not mechanically rediscovered. The exact uniform P-versus-NP target remains the one audited in [the model note](../../foundations/01-model-and-target.md).

**Decision and classification.** SPECIALIZE approves only the exact COVERED_TARGET above. The Frege theorem and supporting conversion results are known imports; the remaining work is an encoding/applicability specialization intended as REPRODUCTION, with no claim of progress beyond the checked literature. This completed literature review is EXPLORATION / NOVELTY_UNCHECKED: it supplies a new source comparison and an actionable test, not a mathematical advance or a new impossibility result. Mathematical exploration turns used remains 1; no calculation turn or counter reset occurs.

## Mathlib

Coverage: **not checked** for formula-IPS, its identity certificates or EF/ER simulations. Direct primary theorem links and their qualifications are retained in the source note. Known supporting results match their stated scope; no full Mathlib match or absence is asserted.
