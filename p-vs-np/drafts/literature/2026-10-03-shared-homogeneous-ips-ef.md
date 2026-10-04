# Shared homogeneous components: completed source assessment

TARGET: Test whether shared homogeneous-component circuits yield a polynomial EF/ER simulation of arbitrary-degree balanced F₂ noncommutative formula-IPS certificates for 3CNFs.
CHECKED: 2026-10-03
DECISION: EXPLORE
SEARCH_EVIDENCE: Targeted searches on 2026-10-03 compared noncommutative formula/ABP IPS, EF sharing, circuit homogenization and stronger simulations; they located Raz–Shpilka's component-ABP construction, Hrubeš–Tzameret's short circuit-decomposition proofs and Filmus et al.'s restricted EF simulation. Exact queries and inspected scope are recorded below and in drafts/2026-10-03-shared-homogeneous-ips-source-notes.md.
SOURCE_EVIDENCE: Read Raz–Shpilka, https://www.cs.tau.ac.il/~shpilka/publications/RazShpilka_PIT.pdf, Lemma 2 / Theorems 4–5; Hrubeš–Tzameret, https://users.math.cas.cz/~hrubes/PDFs/DetSIAM.pdf, GF(2) circuit-Frege interpretation / Lemmas 3.1–3.2; Li–Tzameret–Wang, https://arxiv.org/pdf/1412.8746v4, Lemmas 4.4/4.8/4.15 and Theorems 4.11–4.12; Filmus et al., https://arxiv.org/pdf/2302.06241, Proposition 3.3 / Theorem 3.4 / Lemma 3.7. Precise versions, pages, proofs inspected and limits are in the source note; reuse existing EF/ER coverage.
COMPARISON: Known formula simulation is quasipolynomial in general and polynomial at logarithmic degree. Known component ABPs and circuit-decomposition proofs avoid a representation-only source gap, but do not themselves prove zero identities in EF for the chosen shared encoding. Hitting simulation is a restricted comparison; general IPS/EF retains PIT-proof premises. No inspected theorem matches the full proposed binary-length simulation.
GAP: Prove the imported homogeneous-ABP coefficient-matrix transitions in EF with shared gate definitions and free assignment variables, identify their outputs with both IPS identities, and charge the entire original-CNF ER conversion in one polynomial total binary bound. No such assembly is established in this review.
REASON: The prior logarithmic-degree/tree assessment did not cover this changed hypothesis. The bounded search supplies usable known ingredients and a specific internal-proof test, with no full-statement match or essential source blocker; investigate only the remaining proof/encoding difference and import the covered mathematics.
SCOPE: Supplied balanced division-free fan-in-two F₂ noncommutative tree formula-IPS certificates for 3CNFs, with explicit clause/Boolean/base-variable commutator axioms and formal identities. Syntactic degree may grow with formula size. Sharing is permitted in the proposed component-ABP/circuit and EF proof representations, not as an unassessed replacement of the input tree by an arbitrary arithmetic circuit. No divisions, other fields, Boolean-only identity premise, unprovided PIT axioms or unconditional decision-to-proof transfer.
COVERED_TARGET: Construct EF proofs of the imported coefficient-matrix transitions for a supplied homogeneous F₂ noncommutative zero ABP, preserving shared gates.
COVERED_TARGET: Check a polynomial total binary EF/ER bound for the screened shared-component translation of balanced F₂ noncommutative formula-IPS certificates for 3CNFs.

The initial REVIEW_REQUIRED record was created after L016 because arbitrary degree and internal circuit sharing were outside the [prior assessment](2026-10-03-noncommutative-ips-er-simulation.md). This turn completed only that source review. The exact TARGET is preserved; no proposed simulation has been calculated or proved. The prior assessment and its [source note](../2026-10-03-noncommutative-ips-source-notes.md) remain adequate for L016 and are unchanged.

## Gap, downstream use and discriminating test

The main gap remains SAT decision hardness or a polynomial SAT algorithm. This intermediate upper-bound screen could eliminate a larger algebraic certificate fragment from prospective ER-hard CNFs. It still leaves certificate lower bounds, exclusion of all EF/ER proofs and a decision-to-ER transfer unresolved. It is neither a separation target by itself nor an assumption of a successful simulation.

The required threshold is one fixed polynomial in T=2+|F|+|A|+|C|, including the original binary variable labels and every auxiliary definition and proof reference. The existing general quasipolynomial bound does not meet it. The known component ABP construction and short homogeneous-decomposition proofs meet their own stated bounds; combining them into the required EF/ER bound remains a mathematical obligation. L016's logarithmic-degree result is not extended merely by citing them.

The permitted test is to use the original formula's known homogeneous ABPs and Li–Tzameret–Wang's ABP coefficient-matrix witnesses, retaining sharing when expressing the local identities in EF. Establish identification proofs, the transition proofs and their base case with the original assignment free. If these admit one polynomial total bound, check both C(x,0)=0 and C(x,A(x))+1=0 and use the screened original-CNF conversion. Continue only after those proof obligations and binary costs are justified. If the construction needs general-circuit PIT proofs, unfolds shared components at quasipolynomial cost, or cannot justify its identification/transition equations, record the failure and stop or narrow this mechanism. No transition, constant-edge compiler or new combined bound is derived in this literature turn.

## Search and theorem comparison

Queries actually issued included:

- `"noncommutative" "extended Frege" homogeneous simulation`
- `"non-commutative" "IPS" "EF" simulation sharing`
- `"homogeneous" "circuits" "Frege" Li Tzameret Wang simulation`
- `"noncommutative formula" "extended Frege" polynomial`
- `"non-commutative IPS" "Extended Frege" polynomial`
- `"noncommutative" "homogenization" "Extended" "Frege"`
- `"noncommutative" "ABP" "Extended Frege"`
- `"non-commutative" "branching" "extended Frege"`
- `"identity testing" "noncommutative" "EF" proof`
- `"Li" "Tzameret" "Wang" "Extended Frege" "polynomial" simulation`
- `Raz Shpilka deterministic polynomial identity testing noncommutative polynomials Theorem 4 homogeneous formulas pdf`
- `Hrubes Tzameret short proofs determinant identities homogenization Proposition 4.4 circuit pdf`

Read the primary theorem statements and proof passages listed in the [source note](../2026-10-03-shared-homogeneous-ips-source-notes.md). Search snippets, secondary mirrors, surveys returned by search and talk announcements are discovery aids, not proof evidence. The unsuccessful full-statement search does not establish absence or novelty.

The closest formula theorem supplies homogeneous **formula** zero proofs. Its quasipolynomial cost is explicitly charged to the formula homogenization in the inspected proof. Substituting circuit components into its statement changes its input model. The ABP witnesses are a relevant earlier stage of that argument, but their semantic vanishing must be separated from a short EF derivation in a specified Boolean encoding. Hrubeš–Tzameret provides known short decomposition proofs in a commutative circuit proof system; that supports representation, not the missing noncommutative identity-witness assembly.

The hitting theorem shows that extensions for linear-algebra basis data can support an actual polynomial EF simulation. Its structured variable-ordered products are not all formula-IPS certificates; it is supporting technique evidence only. The Grochow–Pitassi general theorem retains its PIT-axiom-proof premise, and the September 2026 partially commutative manuscript still states quasipolynomial Frege overhead. No general PIT proof is silently imported.

Reuse the [reflection assessment](2026-09-26-current-target.md) and [foundation](../../foundations/06-reflection-specialization.md) for supplied-proof substitution and CF/EF/ER conversion, retaining the formula conclusion. No source access gap remains for the selected test. Unreviewed full proofs of the recent partially commutative manuscript and the hitting paper's unrelated sections are not essential inputs.

## Redundancy, stopping evidence and classification

L016 handles logarithmic syntactic degree only; its known theorem application does not settle this target. L012 already handles the Tseitin linear-algebra family; it is not the same general identity screen. [ATTEMPTS/010](../../ATTEMPTS/010-automatic-decider-to-er-simulation.md) stops a checkability-to-ER shortcut, so external ABP PIT verification will not replace the required free-variable proof here. The KPT stops in [ATTEMPTS/013](../../ATTEMPTS/013-canonical-kpt-universal-recovery.md) and [ATTEMPTS/014](../../ATTEMPTS/014-dropping-complete-output-cover-premises.md) are preserved. This is a distinct algebraic test, not a restart of their missing universal guards or cover premises.

EXPLORE approves the unchanged TARGET and the exact covered subtargets for subsequent mathematical attempts. Known homogenization, ABP witness existence, reflection and proof conversions must be imported. Only their circuit-proof realization, applicability and binary accounting are left for investigation. Successful assembly would be local progress; the checked search cannot certify originality and no progress beyond the checked literature is claimed now.

This completed step is EXPLORATION / LITERATURE / NOVELTY_UNCHECKED. It adds specific source coverage and a usable test without establishing a new mathematical input or an informative impossibility result. Mathematical exploration turns used stays 0. The pending degree/representation coverage justified this literature turn; the now-ready assessment calls for mathematics on the following invocation.

## Mathlib

Coverage: **not checked** for the full target, homogeneous ABPs, identity witnesses or EF/ER simulation. The named direct sources match supporting results with the qualifications above; none is asserted to match the full simulation or a Mathlib entry. Existing coverage for L016 is preserved.
