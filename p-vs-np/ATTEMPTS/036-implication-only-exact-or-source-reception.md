# Attempt 036 — implication-only reception of exact literal-OR sources

The bounded target was L106's three-row exact-¬F source compiler, with
the independent strict Schoenfield/MP/constant checker and L056's
qualified implication/negation synthesis component. Ground-zero cases
and the finite ax-3 replacement succeed; the full parity export does not.

**WHY IT FAILS.** The component recognizes literal ¬A∨B as implication
but leaves positive-left OR nodes opaque. Its decoded three-row endpoint
fails the tautology reception test, and the first displayed L106 row
template has a separate saved failure. The canonical implementation
evidence and limitations are in
[L106, step 419](../lemmas/L106-source-parity-system-exact-occurrence-witness.md),
with full inputs, exact formulas, countervaluations, successful complete
streams and corruptions in `scripts/parity-source/output/`. Stop this
implementation path before any silent endpoint normalization or extra
checker rule. This failure does not establish source nonderivability,
invalidate every source-proof construction, or prove witness/SAT hardness.
A separate primary-source syntax/completeness review is required to
identify an independently justified reception convention or a changed
interface needing its own assessment. Preserve the checked zero-case
streams, all prior proofs and audits with their new qualification;
original-Q integration and uniform compiler bounds remain unverified.
