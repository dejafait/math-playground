# Canonical KPT substitution: working proof-obligation test

These working notes were saved during the test authorized by the prior EXPLORE assessment in `drafts/literature/2026-09-27-canonical-kpt-witness-substitution.md`. The completed proof is now [L014](../lemmas/L014-canonical-kpt-recovery-guard.md); the tentative wording below records the reasoning before that proof was finished. This is not a candidate resolution of P versus NP.

## Target and threshold

Keep the supplied two-round KPT strategy and the hypothetical polynomial-time SAT decider fixed. The intermediate target is removal of the first satisfying-assignment argument while preserving a universally valid solver-or-antichecker conclusion with one polynomial EF proof-length bound. The existential PV1 premise and an EF lower bound remain unproved. KPT does not promise two rounds.

Use the existing circuit-substitution theorem. Track the earlier formula, assignment, comparison circuit, and assignment-certification data separately. Stop the direct repair if the missing universal recovery condition has the same proof-length cost as the desired EF boundedness.

## Reasoning saved before completion

Write V(x,y) for assignment verification and let B be the fixed first solver candidate. With the first antichecker disjunct falsified by concrete comparison/assignment data, its solver term is Q_B(x,y) := (V(x,y) -> V(x,B(x))). Replacing the first assignment by W(x) gives Q_B(x,W(x)) in the KPT disjunction.

The exact condition for replacing this first term by Q_B(x,y), independently of the second term, is

G_(B,W)(x,y) := (V(x,y) AND NOT V(x,B(x))) -> V(x,W(x)).

Indeed Q_B(x,W(x)) -> Q_B(x,y) simplifies to G_(B,W). This is weaker semantically than correctness of W alone. It is the search-correctness statement for the fallback circuit that returns B(x) when its answer verifies and returns W(x) otherwise. The Boolean derivations and the proof-length consequences still need to be written in the lemma format and checked.

For fixed first-round output (including its pairing data), a correct comparison circuit and a concrete satisfying assignment falsify the antichecker term: if every encoded label agrees with the comparison circuit, its error disjunction is false; a disagreement can only be a satisfiable input carrying an invalid chosen assignment, which supplies a falsifying certification challenge. Malformed pairing data already falsify the term. All this concerns constants at a given length, and does not require an EF proof of the comparison circuit's global correctness.

The potentially decisive proof-cost test is to specialize G_(B,W) to an arbitrary unsatisfiable F. Both B(F) and W(F) fail verification, irrespective of their intended semantics. After checking those concrete computations, the guard becomes NOT V(F,y). L013's explicit evaluator identification and the imported CF/EF conversions appear sufficient to turn polynomial guard proofs into polynomial EF proofs of arbitrary tautologies. Conversely, under external correctness of W, G is a polynomial-size tautology family, so EF polynomial boundedness would bound its proofs. The encoding, circuit/formula representation and both implications must be checked before recording this as a completed result.

No general impossibility of canonical substitution or EF simulation follows. This tests the direct recovery inference; a method exploiting additional strategy structure could avoid its guard. No new theorem is being claimed from the saved source assessment.

## Completed test

L014 checks both proof-length implications, retaining the exact L013 evaluator and the formula-conclusion restriction in the CF/EF conversion. It also spells out the first-round pairing and label challenges, and the unsatisfiable-input case where the canonical substitution becomes vacuous. The outcome is NEGATIVE for the direct recovery mechanism, classified as REPRODUCTION of standard reflection and Boolean reasoning. The encoding, proof conversions and both directions of the conditional proof-length claim are checked there. The existential arithmetic premise and EF lower bound remain unproved; no separate mathematical claim rests on this draft.
