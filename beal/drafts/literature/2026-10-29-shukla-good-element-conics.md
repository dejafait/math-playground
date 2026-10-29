# Fixed Selmer pair: Shukla good-element conic test

TARGET: Test Shukla's good-element condition for eta_class and nu by complete branch-pair conic solubility certificates in the actual odd-model root-pair algebras.
CHECKED: 2026-10-29
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse discovery and duplicate/failure comparison in 2026-10-28-quartic-algebra-pairing-mechanism.md; no separate formula or new-theory claim is proposed.
SOURCE_EVIDENCE: Shukla, On computation of the Cassels-Tate pairing, published Bayreuth thesis, DOI 10.15495/EPub_UBT_00008348, Chapter 4 setup pp.85–86, Theorem 4.2.1 pp.88–89, Section 4.4/Assumption 4.4.3/Proposition 4.4.4 pp.107–111 and Algorithm 2/Remark 4.5.1 pp.113–114; defining conic and complete conditional construction inspected. Use the named Hasse–Minkowski theorem over number fields and quaternion splitting criterion only for the conic test.
COMPARISON: The known simpler pairing construction avoids raw torsor equations when its first Selmer argument is good. Neither L147/L149 membership nor the 1+4 action verifies goodness; the instance difference is a finite family of conics over actual root-pair fields and compatible exact solutions.
GAP: Determine whether either fixed class satisfies the whole branch-pair condition; do not replace it by the rational-root row, test only descent-support primes, or infer a pairing value from success/failure.
REASON: This independently testable gate can enable the known cochain construction without ATTEMPTS/065's raw-model box, or supply a new local obstruction to that simpler construction. It is standard specialization and requires separate supervisor approval because this assessment is newly written.
SCOPE: Exactly TARGET for L138's model/algebra and L147/L149 masks 132102 and 3109; exact representative transport, finite factorization and conic tests only. No covering-model box, new Selmer witnesses, full pairing evaluation, class/unit computation or cross-notebook input.

## Bounded mathematical test after approval

Reuse the full source analysis in
`drafts/literature/2026-10-28-quartic-algebra-pairing-mechanism.md`.
The primary source is
[Shukla's published thesis](https://epub.uni-bayreuth.de/id/eprint/8348/1/thesis.pdf).
Use L138's exact root-algebra map and L147/L149's full Q×K
representatives, without quotienting by rational scalars. Authenticate
each representative and its model before testing it.

For each class, enumerate branch-pair orbits by factoring the quintic
over each representative root field, omitting the diagonal. Construct
the Section 4.4 conic in each resulting field in a fixed variable/sign
convention. Preserve exact factor, field, embedding and representative
certificates. Do not assume generic quartic Galois action or discard
the quartic-root rows. Do not copy Algorithm 2's initialization/guard
literally; its printed inconsistency is noted in the source comparison.

For a negative answer for one class, a single nonsplit local conic with
exact embedding, normalized coefficients and certified Hilbert symbol
is sufficient; stop that class and test the other. For a positive
answer, require the complete finite-place set and archimedean tests,
an outside-support argument for the conic itself, exact field solutions,
and compatibility under conjugation. Check each solution in its defining
equation; a finite point-search failure is not insolubility. Use
Hasse–Minkowski to distinguish proved solubility from a bounded search.
If constructing a solution is blocked, preserve the precise positive
local evidence and label the constructive gate unfinished.

Stop after these two classes. If neither is good, abandon this
conditional shortcut on this pair while retaining the general cochain
method as a distinct untested route. If either is good, save its complete
certificate for later cochain construction and local lifting; do not
compute or claim a pairing in this test. No sufficient rank-one bound
is promised. Missing exact factorization, field arithmetic or complete
local evidence leaves an unresolved gate, not a negative theorem.

The main gap remains point control at rank <=2+c<=4, followed by
marked/integer recovery and all other signatures. Essential inputs are
L138/L139/L147/L148/L149. Goodness of eta_class/nu, their rational Kummer
status, mutual pairing, class generation and all later recovery steps
remain unresolved. Full matching Mathlib coverage is not checked.
