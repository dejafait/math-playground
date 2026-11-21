# Shifted Gaussian primitive evaluation — source comparison1572

TARGET: Assess whether the Gaussian explicit formula supplies effective enclosures for C032m's E_sigma and O_sigma for the unchanged dictionary1570 without individual zero coordinates.
CHECKED: 2026-11-18
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Review1572 searched shifted Gaussian explicit formula, Guinand-Weil Gaussian errors, Gaussian primitives and interval arithmetic; inspected primary statements rather than snippets. Queries, inspected ranges, unread leads and duplicate/stop comparison are in drafts/literature/2026-11-18-shifted-gaussian-primitive-evaluation-source-notes-1572.md. No matching effective dictionary evaluation was found; no novelty follows.
SOURCE_EVIDENCE: Chirre-Goncalves, Math.Z.300(2022), Proposition5, p1044, https://link.springer.com/content/pdf/10.1007/s00209-021-02820-9.pdf permits complex even analytic tests with strip decay and sums over complex nontrivial zeros; Carneiro-Chirre-Milinovich arXiv:1710.10362v1 Lemma8 pp9-10 additionally requires real values on R. Connes arXiv:2402.13082v1 Section2(4)-(9), p4, supplies the unconditional Mellin identity and subtracted archimedean integral. Reuse C032m's inspected Haslinger2.39 and removable-quotient proof; no source states the requested effective primitive bounds.
COMPARISON: The general identity supplies a zero-coordinate-free route, not a certified evaluator. Fixed-test hypotheses are covered; uniform parameter bounds, transformed primitives and errors remain a specialization. C032t's small-u weighted sign and the sources' unshifted asymptotics do not cover them. Calculation1571's box optimum above999/1000 does not bound the actual dictionary.
GAP: Prove applicability and explicit uniform truncation bounds for shifted tests and E/O primitives, including the noncompact spatial integral and w=+/-ix; pay prime, archimedean, primitive-tail and numerical errors before a residual claim. No effective formula, constant, actual dictionary value or residual below1/2 is established here.
REASON: Essential general theorem coverage is now available. A bounded established-route specialization is justified; reproof of Guinand-Weil or repetition of the old grids is not. A newly nominated research target is saved separately for next-turn approval.
SCOPE: Same sigma in[1,2], same eight w and four Laplace parameters as assessment1570; no frequency/order/variation-budget increase, no source-wide validation or unsmoothed realization. All actual-divisor, multiplicity, strip/counting, zero-ordinate exclusion, finite-zero, heat and fixed-v1 qualifications remain visible.

The completed comparison is in source-notes1572. Proposition5 does not
impose RH or real-valuedness. Lemma8's additional reality hypothesis must
not be dropped when citing that version. Its entire proof is a citation
to Goldston-Gonek Lemma1 and Iwaniec-Kowalski Theorem5.12, not an
effective shifted-primitive argument. Those upstream proofs were not
newly inspected or reproved. Use Connes(5), not its RH-dependent
spectral rewriting(11). Existing C032m removable values and dominated
integration do not justify new integrands without checking their actual
hypotheses. No essential source remains blocked for attempting this.

Continue with assessment1572's one analytic attempt if it yields explicit
uniform errors decreasing with stated cutoffs, including the removable
cases; otherwise preserve the precise failing interchange or estimate
and stop. No optimizer retry or dictionary growth is approved here.

The proposed use is sharper enclosures for the still unresolved fixed
variation2 test, not a claim that such enclosures will succeed. An actual
certificate would still need independent audit and would leave arbitrary
variation, full cancellation/feasibility and actual-Xi positivity open.
Full matching Mathlib coverage remains unchecked and unknown.
