# Existence of a formally sound efficient SAT decider: literature assessment

TARGET: Review whether SAT∈P alone implies the existence of a polynomial-time SAT decider B with a PV proof of its rejection-soundness identity, and compare this existence claim with the ER polynomial-boundedness gap.
CHECKED: 2026-09-27
DECISION: EXPLORE
SEARCH_EVIDENCE: Searched SAT/P=NP with PV soundness, provable algorithms, ER/EF polynomial boundedness, and Pich–Santhanam transfer results; followed primary references and read the theorem statements listed below. No exact unconditional existence theorem was located.
SOURCE_EVIDENCE: https://www.karlin.mff.cuni.cz/~krajicek/cookpv.pdf, Definition 5.4, Theorem 5.5, Lemma 5.8, p. 93, and Theorem 6.8, p. 95; https://www.karlin.mff.cuni.cz/~krajicek/k4.pdf, Chapter 7, pp. 83–84; https://arxiv.org/pdf/2312.08163v1, Theorem 1 and Corollary 2, pp. 4–5; https://eccc.weizmann.ac.il/report/2023/199/download, Proposition 1, pp. 3–4, and Theorem 2, p. 8. Statements and surrounding arguments were inspected.
COMPARISON: The inspected results give conditional reflection/simulation or conditional witnessing transfers. None supplies the exact existential choice of B from SAT∈P alone; the nonuniform circuit-transfer barrier does not rule out the weaker uniform target.
GAP: The one-sided PV soundness proof for some externally complete B remains missing; no equivalence with full PV-provable SAT search or with ER polynomial boundedness has been imported or proved.
REASON: Retain the exact target as unresolved, stop treating formal soundness as automatic, and assess the explicit uniform witnessing mechanism separately. A failed search is neither a counterexample nor evidence of novelty.

## Gap, target, and test

The main gap is still a polynomial-time SAT algorithm or an unconditional exclusion of every such algorithm. The intermediate target preserves the saved existential quantifier over B, a fixed polynomial clock, and one finite PV proof of its no-false-rejection identity. The evaluator is the fixed one used in L013. This proof could supply the soundness input for the existing ER transfer; a suitable superpolynomial ER lower bound would remain an independent obligation.

The positive review test was an inspected theorem selecting such a B from SAT∈P with no extra formal-correctness premise. That test was not met. A theorem assuming the desired PV proof, or only yielding proofs in EF with extra axioms, fails it. There is also no inspected counterexample to the implication. The review therefore completes the search assessment without declaring the mathematical implication true, false, independent, or novel.

**Required versus available.** The needed bound is one polynomial for the soundness refutations at every input length. L013's bound is polynomial in N+|H|+|π| for a supplied π; this does not bound |π|. The source theorem also retains a fixed formal proof as a hypothesis. No missing polynomial bound was obtained during this literature turn.

## Search and inspected sources

Queries used on 2026-09-27 included:

- `"P=NP" "PV" "soundness"`
- `"polynomially bounded" "extended Frege" "P=NP"`
- `"SAT" "PV" "provably" "algorithm"`
- `"SAT" "PV-provable" soundness`
- `"P=NP" "extended Frege" implication open`
- `Pich Santhanam "NEXP" "proof system" "P" 2023`
- `"Pich" "Santhanam" "Towards" "Extended Frege" pdf`

The [source note](../../foundations/07-formal-soundness-and-transfer-limits.md) records the precise imported statements, versions, page numbers, hypotheses, and limitations in the standard Hypotheses / Conclusion / Proof / Mathlib format. Cook's Main Theorem 5.5 and Lemma 5.8 were additional inspected inputs beyond the prior review's Definition 5.4 and Theorem 6.8. The [prior reflection assessment](2026-09-26-current-target.md) was reused for L013's conversion machinery and left unchanged.

Additional material actually read: Pudlák, [arXiv:2007.14835v1](https://arxiv.org/pdf/2007.14835v1), Theorem 4.1, p. 19, states the strongest-system characterization under provable soundness; its premise does not supply B. Oliveira's [2025 survey](https://www.dcs.warwick.ac.uk/~igorcarb/documents/papers/Oli25-Survey.pdf), §5.1.2, pp. 17–18, was used to locate the standard SAT-search formalization and its Cook reference; it is not used as a primary proof of this notebook's different one-sided claim.

The [Clay page](https://www.claymath.org/millennium/p-vs-np/) and [official Cook description, §1, pp. 1–2](https://www.claymath.org/wp-content/uploads/2022/06/pvsnp.pdf) were reconfirmed: the target remains ordinary uniform P versus NP, and the page labels it unsolved.

**Source access and versions.** The Pich–Santhanam ECCC and arXiv presentations differ in length and numbering; each citation names its version. The journal DOI landing request failed and the journal PDF returned HTTP 403, so the journal text is not claimed read. The accessible primary versions suffice for the qualified statements imported here. A search-result reference to CCC 2024 article 22 led to a different paper and was excluded. No essential source for the completed assessment is left unread; the Bogdanov–Talwar–Wan paper is an unread lead for the separate proposed target, not an input here.

## Comparison and route decision

The exact target requires external correctness of B and a proof of only rejection soundness. Replacing it with a PV proof of full SAT-search correctness would change the question. Conversely, Cook's PV proof for ER soundness concerns the proof verifier, not arbitrary SAT deciders. No existence claim for B follows merely by giving a polynomial-time algorithm a PV function symbol.

The fresh literature evidence identifies a concrete conditional mechanism and its input-length requirement. In the arXiv version, Corollary 2 treats clocked algorithms with bounded advice and separates extra witnessing axioms from provability in S^1_2. Its zero-advice case is relevant to the uniform goal. The ECCC version's discussion on p. 7 flags the length mismatch with the earlier uniform counterexample-finding work. These observations justify a focused source comparison, not a claimed witness construction.

Keep the [automatic-transfer failure](../../ATTEMPTS/010-automatic-decider-to-er-simulation.md) in force. L012's easy ER parity family and L013's completed conditional specialization do not supply the missing premise. L003 and L009 warn that changing or padding input lengths can destroy the desired lower-bound transfer; any witness comparison must retain the prescribed length rather than pay for a different task.

**Decision: EXPLORE.** The unconditional existence implication remains unestablished in the checked literature. No reproof of reflection or new equivalence is warranted by this assessment. The separate [witness assessment](2026-09-27-uniform-sat-error-witness.md) starts at REVIEW_REQUIRED. Continue that comparison only if the primary theorem has a relevant uniform guarantee or exposes a specific repairable difference; abandon a direct import if its length or formal-provability requirements are missing. This is exploration turn 1 since the last advance; the review does not reset the counter.

All mathematical results reported here are known source inputs. The completed step is NOVELTY_UNCHECKED because no full match for the exact implication was established; this does not label any statement as new. No lemmas or mathematical scripts were changed.

## Mathlib

Coverage: **not checked** for the existence implication or the supporting formal-soundness and witnessing results. Direct links and theorem identifiers are preserved above; none is claimed to match the full target.
