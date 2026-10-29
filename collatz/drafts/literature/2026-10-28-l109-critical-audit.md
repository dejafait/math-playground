# L109 finite-word negative — critical-audit nomination

TARGET: Critically audit L109's finite-word carry formula and guarded counterexample, including source specialization, least-representative conventions and the incomplete-search qualification.
CHECKED: 2026-10-28
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse step534's saved finite-word comparison and step535's EXPLORE assessment; targeted October28 assessment/history and Attempt036 searches found the completed L109 negative but no separate critical audit. No fresh novelty search or change of mathematical target.
SOURCE_EVIDENCE: L109 read in full; Rozier2019 Lemma1 and affine proof pp.2–3 rechecked; Rozier–Terracol arXiv:2502.00948v2 Definition2.2/Lemma2.1 and complete two-step/common-suffix proof rechecked. The existing certificate is named but has not been inspected or rerun in this literature turn.
COMPARISON: Finite coding and additive-remainder order are known imports; L109 combines them with an exact modular carry and explicit arithmetic. Audit that local combination and its reported evidence; do not reprove the general imported facts or claim literature novelty.
GAP: Independent checking of the carry representative interval, source rescaling, both first-drop guards, exact witness and partial-search report remains for this audit. Success validates a negative certificate only; no escape, CST or universal-descent conclusion follows.
REASON: The discovery step selected no justified pointwise test. Preserve the parked route's evidence by checking the newly recorded negative before using it as a settled routing constraint. This newly written assessment requires separate approval and no audit is performed in step536.
SCOPE: Only L109's existing formula, witness and reported bounded evidence; no variant, expanded search, new escape mechanism or broader theorem.

## Inputs and precise comparison

The sole local mathematical object to audit is
`lemmas/L109-first-drop-swap-margin-counterexample.md` and its existing
`scripts/first-drop-swap-margin/certificate.json`. No other local lemma
is a mathematical premise. L001/L003 and Attempt020 are scope contrasts;
Attempt036 records the stopped route. No cross-notebook input is needed.

The primary finite imports are [Rozier, INTEGERS19(2019), A8,
Lemma1 and affine proof, pp.2–3](https://math.colgate.edu/~integers/t8/t8.pdf#page=2)
and [Rozier–Terracol, arXiv:2502.00948v2, February13,2025,
Definition2.2/Lemma2.1](https://arxiv.org/html/2502.00948v2#S2).
Their finite hypotheses cover the words under audit. The local work
requiring verification is L109's carry calculation and explicit witness,
including the treatment of the class containing1. This is source
specialization and local reproduction, not creative mathematics.

## One bounded audit and decision threshold

After separate approval, check the written proof and the complete
selected certificate values `/counterexample` and `/lengths`, using the
shared JSON inspector. Check the exact integer representative interval,
the prefix-sum convention, both first-drop predicates, modular carry,
two direct trajectories and margin difference against the canonical
statement. Inspect the existing script only for the evidence claims
being relied upon; rerun its bounded certificate only if needed.

Accept only if every displayed formula and witness hypothesis agrees
and the search qualification remains exact: lengths1–4 completed, first
violating edge at length5, no exhaustive length5 or length24 claim.
A discrepancy requires a concrete correction or an unresolved audit
finding; do not tune the failed inequality or search for a replacement
in this turn. All-depth escape, coefficient-to-actual descent, sorting
alternatives and universal convergence remain unresolved and are not
assumptions. The audit's downstream use is reliable rejection of one
certificate; it creates no new pointwise mechanism.

Full matching Mathlib coverage is not checked. Supporting source
identities are mathematical citations, not a claim that Lean has checked
L109. No source theorem needs reproof for this audit.
