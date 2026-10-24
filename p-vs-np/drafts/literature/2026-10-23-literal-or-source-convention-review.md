# Literal OR source-presentation convention: completed source comparison

TARGET: Review the literal-OR completeness and MP conventions in L097/L098's source presentation against the primary Schoenfield/LTW basis and the saved parity reception diagnostic.
CHECKED: 2026-10-23
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 420 compared the exact checker, L097 §§3–4, L098 hypotheses, L106's template/step-419 passages, Attempt 036 and earlier scope assessments; searched Shoenfield/Schoenfield three-axiom, primitive-disjunction and LTW correction terminology; directly read LTW's definitions/extraction cases and Shoenfield's rules/tautology proof. No matching exact-checker completeness or correction theorem was located; this is not a novelty claim.
SOURCE_EVIDENCE: LTW 40-page author manuscript, printed p.2, Definition 1.3 p.6, Definitions 2.1–2.4 p.11 and Lemma 3.3 pp.13–14; Shoenfield, Mathematical Logic (Addison-Wesley, 1967), §2.6 pp.21–23 and §3.1 Tautology Theorem (Post), p.27, proof pp.28–30, including its connective cases and supporting rules.
COMPARISON: LTW explicitly expands implication as ¬A∨B and prints exactly three schemes plus MP; its displayed extraction supplies no extra OR bridge. Shoenfield's inspected completeness proof instead uses ¬A∨A and expansion, contraction, association and cut. These are different serialized rule sets. The local checker matches LTW's display plus local ground axioms, but the inspected completeness proof cannot be imported for that checker without a proved rule translation.
GAP: Literal-OR completeness/nonderivability for the current checker is unsettled; no bridge or changed extraction is established. The saved diagnostic needs a separate test for soundness under every accepted rule, not only endpoint falsity. Shoenfield supplies a complete alternative literal-OR basis, whose algebraic reception would be a different target.
REASON: This changed-hypothesis source review supplies new negative coverage evidence and stops the unsupported completeness import. It scopes, but does not approve or perform, a new general obstruction test or repaired compiler; the continuation is REVIEW_REQUIRED.

Essential local inputs: L097's source/constant presentation, L098's exact
π interface, L106 §§2–4 and its step-419 section, and
`scripts/parity-source/output/report.json` field
`/fixtures/three-row/endpoint_diagnostic`, plus
`scripts/parity-source/output/failed-row-template.json`.
The literal endpoint has x∨¬y, y∨¬z and x∨z as positive-left OR
nodes; their implication-only opaque-token diagnostic must not be
silently identified with classical OR evaluation.

Retrieve the precise primary definition around LTW's basis/translation
convention first; follow a primary Schoenfield or standard Frege
completeness reference only as necessary to settle this exact scope.
Do not repeat general parity literature. Assess whether the supplied
source presentation covers the exact target, is restricted to a
definitional implication language, or needs an additional OR bridge or
rule. A primary source's use of a standard complete Frege system does
not by itself license adding a primitive to the local serialized checker.
Conversely a failed component synthesis is not proof of nonderivability.

Continue on a precisely cited convention and independently testable
receiver change. If the recorded source basis lacks coverage for literal
OR, record the needed change and its affected L097/L098 extraction cases
for a later separately assessed mathematical step. Do not derive or
approve a new general obstruction, changed-basis extraction or repair in
this source review. The main SAT decision/separation gap, full original-Q
pair/provenance integration and all-size implementation ledger remain
unresolved. Mathlib coverage has not been checked.

## Completed comparison — step 420, 2026-10-23

LITERATURE_REASON: Step 419 exposed an essential changed hypothesis:
completeness for exact primitive-OR strings under only the serialized
three-scheme/MP rules. Earlier parity/extraction assessments did not
compare this boundary. Reuse their general parity coverage; another
parity survey would not resolve it.

### Primary statements and proof cases

Fu Li, Iddo Tzameret and Zhengyu Wang, *Characterizing Propositional
Proofs as Non-Commutative Formulas*, SIAM J. Comput. 47(4), 1424–1462
(2018), [DOI](https://doi.org/10.1137/16M1107632), inspected via the
[40-page author manuscript](https://www.doc.ic.ac.uk/~itzamere/Ideal_non-commutative.pdf).
Revision date is unestablished; numbers here are printed manuscript pages.
On p.2 implication explicitly abbreviates ¬A∨B; arguments may be arbitrary
propositional formulas. Its three schemes are followed by exact MP,
not MP modulo equivalence or double-negation simplification. Definition
2.1 (p.11) permits ordered OR/AND/NOT trees and constant leaves.
Definitions 2.2–2.4 define rule instances syntactically and require
implicational completeness for a Frege system. The general equivalence
of Frege systems therefore does not remove that hypothesis for a specific
serialization. These passages supply no extra connective axiom.

Definition 1.3 (p.6) gives ordered falsity translation and constants.
The full axiom/MP cases of Lemma 3.3 (pp.13–14) use the displayed
schemes and exact implication shape; no positive-left-OR or connective
replacement case is given. L097's corrected L035/L036 seeds and DAG
realization remain distinct local work, not rechecked here. Do not
import the suspect Boolean-only product case or a DAG bound from the
paper's tree-size calculation.

Joseph R. Shoenfield, *Mathematical Logic*, Addison-Wesley (1967),
[primary scan](https://w2.cs.uni-saarland.de/op/fullpaper/logics/SHOENFIELD_Mathematical_logic.pdf),
§2.6 p.21, specifies the propositional axiom ¬A∨A and four propositional
rules: from A infer B∨A; from A∨A infer A; from A∨(B∨C) infer (A∨B)∨C;
from A∨B and ¬A∨C infer B∨C. Its first-order apparatus is not needed
for the propositional comparison. The Validity Theorem, p.23, uses
induction on axioms and rules.

The **Tautology Theorem (Post)**, §3.1 p.27, makes every tautological
consequence of finitely many theorems a theorem; its corollary covers
all tautologies. Read its proof pp.28–30: detachment uses expansion,
cut and contraction; the main induction treats disjunction, double
negation and negated disjunction. The supporting rearrangement and
negation steps explicitly use the four propositional rules. No
quantifier/equality inference occurs in that proof, so it supplies
propositional-fragment coverage. It is not a proof in the local
three-scheme/MP checker. The local true/¬false convention is not
silently attributed to this book.

This is a precise citation mismatch, not a nonderivability theorem for
LTW's printed display or a claim about the authors' unstated intentions.
The strongest relevant inspected conclusion is literal-OR completeness
for Shoenfield's stated rule set. A translation of those rules into
the current checker has not been supplied. An alternative basis using
those rules would require L097/L098 extraction cases for each newly
admitted rule. An implication-language encoding would instead need a
proved bridge restoring the exact OR trees. Neither repair is approved
or derived here. In particular L097 §3's completeness call, L098's
generated congruence/template proofs and L106 §2's row templates retain
their qualification. This does not refute conditional extraction from
an actually supplied proof valid in the existing checker.

### Local evidence, duplicates and decision

Inspected `checker.py`'s parser, matcher, ground-axiom and MP branches
and `attempt.py`'s `implication_decode`/evaluation/reception functions
under `scripts/parity-source/`. The complete selected JSON values were
read using the shared inspector: `report.json` pointer
`/fixtures/three-row/endpoint_diagnostic` and all of
`failed-row-template.json`. The first uses x=y=z=0 with all three opaque
values 1; the row failure has its own different saved valuation.
The diagnostic assigns opaque names to entire OR subtrees whose left
child is not syntactic negation. It does not evaluate them as classical
OR. Falsity of a decoded endpoint alone does not establish all-instance
soundness for schemes, arbitrary substitutions, constants and MP.
Any future argument also needs globally consistent, collision-free names
for identical opaque subtrees. This review proves no such invariant.

Earlier assessments 383/418 relied on the displayed basis and general
completeness without this exact comparison. Attempt 036 records component
refusal, not universal rule soundness. Attempt 018's repeated-approval
stop and Attempt 032's independent copying failure are preserved. No
existing theorem or duplicate locally settles the changed source issue.
The checked finite archives and all unfinished work are retained; no
script was rerun and no lemma/script/DAG/PROOF edit is needed.

Queries included `"Shoenfield" "three" "axiom" propositional implication
negation`, `"Schoenfield" "system" "disjunction"`, primitive-disjunction /
implication Frege completeness, and LTW-title errata/correction queries.
These led to the primary scan; unrelated/secondary results are not inputs.
No inspected result supplies the exact-checker bridge or an opaque-subtree
nonderivability theorem. Failed discovery does not establish novelty.
Screenshot extraction was unavailable and local curl DNS failed; primary
web text covered the needed statements and proof cases, so this is not
SOURCE_BLOCKED. Publisher text and unspecified revisions are not claimed
read. Mathlib matching coverage remains not checked.

The main gap is unrestricted SAT. This intermediate source-coverage
target could support a reliable parity/occurrence compiler. Its continuation
test was matching syntax/rules in a precise completeness source; the
identified rule-set difference instead stops the unchanged completeness
import. Next scope a separately reviewed universal rule-soundness test of
the saved opaque interpretation. If soundness and exact endpoint falsity
both hold, that would obstruct this specific interface; if any rule case
fails, abandon the obstruction. No repaired receiver, new general
obstruction or new mathematical result is approved by this review.

Outcome **NEGATIVE / LITERATURE / REPRODUCTION**: new source-scope evidence
changes the route. This is local coverage progress, not progress beyond
the cited mathematics or toward an unrestricted complexity separation.
