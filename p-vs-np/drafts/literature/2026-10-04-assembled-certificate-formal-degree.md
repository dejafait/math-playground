# Actual degree of the assembled certificate: completed assessment

TARGET: Test the formal degree of L021's output certificate on L019's used-extension family as an obstruction to polynomial-size trees computing that same certificate.
CHECKED: 2026-10-04
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Targeted searches compared IPS output degree, noncommutative formula degree/size and the used-extension family; no inspected result determines this exact output polynomial. Exact queries and reading scope are recorded below. Prior reverse and circuit assessments are reused for supporting proof translations.
SOURCE_EVIDENCE: Read Li–Tzameret–Wang https://arxiv.org/pdf/1412.8746v4, Definition 4.5 and the opening of the proof of Theorem 4.7, printed pp. 23 and 25; rechecked Forbes–Shpilka–Tzameret–Wigderson https://toc.cs.uchicago.edu/articles/v017a010/v017a010.pdf, Theorems 1.2/1.4 and Remark 1.3, printed pp. 5–6; read Shpilka–Yehudayoff https://www.cs.tau.ac.il/~shpilka/publications/SY10.pdf, Definition 1.1 and the formal-polynomial discussion, manuscript pp. 2–3 (physical PDF pp. 7–8). These cover the comparison, not the family-specific degree.
COMPARISON: The standard noncommutative formula degree bound makes superpolynomial formal output degree a sufficient obstruction to small trees computing the same polynomial. Known commutative EF-to-IPS circuits may compute exponential-degree polynomials; this allows the proposed phenomenon but does not establish it for L021. Literal unfolding, intermediate-gate degree and syntactic degree do not settle the final formal degree after F₂ cancellation.
GAP: Determine the formal degree, or a rigorously surviving superpolynomial-degree component, of the fixed L021 output before substituting original axioms for placeholders. No inspected theorem settles that degree on L019's family.
REASON: Adequate supporting coverage now permits a bounded specialization to the specified output, without redoing proof-system simulations or claiming novelty. The exact same-polynomial test is preserved; optimal-certificate hardness and decision transfer remain separate gaps.
LITERATURE_REASON: The prior ready assembly assessment did not cover formal output degree as a same-polynomial tree-conversion obstruction. This turn completes the pending changed-target comparison and does no dependent calculation.
SCOPE: Only the deterministic Assembly implementation in scripts/shared-extension/check_assembly.py applied to L019's fixed-CNF used-extension family, over F₂ in the free noncommutative ring on original variables and axiom placeholders. Trees are division-free fan-in-two arithmetic formulas with variable/field-constant leaves; powering gates and succinct monomial leaves are excluded. Degree refers to the final formal polynomial before original-axiom substitution, not the maximum intermediate-gate degree.
COVERED_TARGET: Test the formal degree of L021's output certificate on L019's used-extension family as an obstruction to polynomial-size trees computing that same certificate.

## Gap, relevance and threshold

The main gap remains a deterministic polynomial-time SAT algorithm or an unconditional exclusion of all such algorithms. Locally, L021 supplies original-axiom circuit certificates whereas the forward L018 simulation accepts trees. Understanding the cost of computing the identical output polynomial could rule out a direct conversion of this construction. It would leave different reverse translations, lower bounds against every certificate, circuit identity checking and unrestricted decision transfer unresolved.

Keep the previously proved input length T_m=Theta(m log(m+2)) and L019's original fixed CNF. The discriminating positive threshold is formal degree growing faster than every fixed polynomial in T_m, together with the imported formula degree/size comparison. Merely obtaining a degree tending to infinity, or the existing exponential occurrence-tree count, would not meet that threshold. L021's polynomial circuit bound does not supply a tree bound.

Continue this degree obstruction only if a nonzero high-degree contribution survives in the final polynomial, with all cancellations accounted for. A polynomial formal-degree bound abandons this particular obstruction test but proves no small-tree upper bound. An unresolved degree after a bounded test is exploration, not a lower bound. No output-degree calculation, recurrence, leading-word claim or new family result is derived in this review.

## Search and reading record

Queries actually issued on 2026-10-04:

- `arithmetic formula size degree number leaves circuit exponential degree IPS Extended Frege Remark 1.3`
- `noncommutative IPS certificate circuit formula degree lower bound extension variables`
- `arithmetic formula degree at most size leaves Shpilka Yehudayoff survey pdf`
- `"IPS" "certificate" "Fibonacci" degree`
- `"noncommutative" "certificate" "formal degree" resolution`
- `"extended Frege" "IPS" "degree" "formula"`

Search results served as discovery aids. The following primary passages, rather than snippets, determine the comparison:

1. **Li–Tzameret–Wang**, [*Characterizing Propositional Proofs as Non-Commutative Formulas*, arXiv:1412.8746v4, 11 September 2015](https://arxiv.org/pdf/1412.8746v4). Definition 4.5 assigns degrees 0/1 to field constants/variables, maximum at addition and sum at multiplication. The opening of the proof of Theorem 4.7 explicitly states that a size-s noncommutative formula computes a polynomial of degree at most s+1. These are supporting degree/representation inputs, directly applicable with both original variables and placeholders as input variables over F₂. They do not compute the polynomial of a supplied ER translation. Reuse the already inspected formula-certificate and balancing coverage in the prior assessments; no reproof of those simulations is warranted.

2. **Forbes–Shpilka–Tzameret–Wigderson**, [*Proof Complexity Lower Bounds from Algebraic Circuit Complexity*, Theory of Computing 17(10), 2021](https://toc.cs.uchicago.edu/articles/v017a010/v017a010.pdf). Theorem 1.2 pairs Frege with formula-IPS and EF with circuit-IPS in the commutative setting. Remark 1.3 explicitly permits exponential-degree polynomials from the EF translation, while its Frege output has polynomially bounded degree. Theorem 1.4 supplies the noncommutative Frege/formula comparison with commutator axioms. These statements support testing actual output degree and preserve the circuit/formula distinction. They neither analyze L021 nor assert that every certificate of a CNF has large degree. The commutative exponential-degree observation is an analogue, not an imported noncommutative family theorem.

3. **Shpilka–Yehudayoff**, [*Arithmetic Circuits: a survey of recent results and open questions*, author-hosted SY10.pdf, 123-page manuscript](https://www.cs.tau.ac.il/~shpilka/publications/SY10.pdf). Definition 1.1 fixes variable/constant leaves, addition/multiplication gates, formulas as trees and edge-count size. The following discussion distinguishes formal polynomials from their induced functions, including over F₂. Its circuit-degree convention is maximum gate degree; this assessment instead asks for final output polynomial degree. This source supplies representation and terminology only; its commutative depth reduction is not imported into the noncommutative test. Exact edition equivalence to the typeset monograph was not checked.

The [Clay target page](https://www.claymath.org/millennium/p-vs-np/) was also read on 2026-10-04; the ordinary uniform decision target is retained. Reuse [the reverse tree assessment](2026-10-04-er-to-formula-ips.md) and [the circuit assembly assessment](2026-10-04-shared-noncommutative-er-circuit-ips.md) within their stated scope. No essential source for the approved test remains unread.

**Optional leads not used.** Discovery returned Shastri's ITCS 2026 low-syntactic-degree circuit paper; its primary full-text open returned an internal error. The symmetric-IPS and recent restricted-circuit/formula lower-bound papers were not theorem-read. None determines this local translation's output or is required for the elementary degree test. They remain optional leads, not source inputs or persistent blockers. Failed searches establish neither absence of a theorem nor originality.

## Redundancy and approved test

L019 already excludes polynomial control of literal unfolding, so recounting that quantity would duplicate an established negative result. Its original CNF already has a constant-size alternative certificate. L021's larger finite cases serialize and count the output without expanding formal words at exponentially large degree. Thus those data are not an actual formal-degree result for the final polynomial in independent x,t variables. The prior checks after zero/original-axiom substitution do not answer the saved question.

The next mathematical turn may study the fixed construction's final root with placeholders retained independently. Import the formula degree comparison by citation. Any finite expansions are diagnostic; the desired family conclusion requires a proof that accounts for F₂ cancellation in the output. Syntactic-degree bookkeeping may bound degree from above but cannot certify survival. Substituting A(x) for t yields the constant 1 by L021 and therefore asks a different question. Boolean reduction or commuting the original variables would also change the formal target.

SPECIALIZE approves exactly TARGET and COVERED_TARGET: the standard comparison is known; the family-specific application remains unproved. If it succeeds, it obstructs polynomial-size trees for this particular output only. No all-certificate hardness, general reverse-simulation impossibility, P-versus-NP conclusion or certified originality follows. No new lemma or mathematical script is written in this literature-only step.

Completed step: EXPLORATION / LITERATURE / NOVELTY_UNCHECKED. New source scope and the bounded test are saved; no mathematical advance or result beyond the checked literature is claimed. Mathematical exploration turns used remains 0. The next invocation defaults to mathematics on this ready target.

## Mathlib

Coverage: **not checked** for formal noncommutative degree/formula-size bounds, IPS translations or the particular output-degree target. The direct primary citations above supply supporting statements; no full target match, Mathlib identifier or library-absence claim is asserted.
