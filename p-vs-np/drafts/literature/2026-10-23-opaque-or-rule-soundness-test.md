# Opaque OR: universal rule-soundness test — coverage assessment

TARGET: Test whether a globally consistent opaque-OR interpretation validates every rule of L097/L098's exact serialized basis while falsifying the retained three-row parity endpoint.
CHECKED: 2026-10-23
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 421 reused step 420, inspected Attempt 036, exact checker branches and diagnostic code, and searched propositional independence / axiom schemes / primitive disjunction / modus ponens soundness. No inspected theorem settles this exact syntax-sensitive interpretation; failed discovery is not novelty evidence.
SOURCE_EVIDENCE: Shoenfield, Mathematical Logic (1967), Validity Theorem p.23 (proof induction), Problems 5(a)–(i) pp.24–25 (alternative formula evaluations); LTW, 40-page author manuscript, p.2 displayed schemes/MP and Definitions 2.2–2.4 p.11 (syntactic instances, proof sequences, completeness hypothesis). Relevant primary passages reread in step 421; precise links and scope below.
COMPARISON: Known proof induction and independence methods cover the proposed mechanism. They do not verify this nonstandard, syntax-sensitive interpretation for arbitrary instances of the exact local three schemes and ground axioms. Specialize only by checking that explicit difference and the retained endpoint; no completeness import, basis repair or general Frege obstruction is approved.
GAP: Ready coverage for one bounded attempt: define a globally consistent collision-free interpretation, establish or refute every accepted rule case for arbitrary formulas, and check the exact saved three-row endpoint. All these mathematical obligations remain unproved.
REASON: The essential primary method and exact source syntax are accessible. The separate comparison is complete; further general browsing is unnecessary for the unchanged target. Approval concerns research scope, not the truth of the proposed obstruction.

Essential local inputs: L097 §§3–4 (basis/constants), L098's exact proof
interface and L106's step-419 qualification; these are the objects of the
test, not assumed completeness results. Inspect the actual parser,
matcher, ground-axiom and exact-MP branches in
`scripts/parity-source/checker.py` and the diagnostic definition in
`attempt.py`. Read the complete selected value in
`scripts/parity-source/output/report.json` at
`/fixtures/three-row/endpoint_diagnostic` using the shared JSON inspector.

The proposed test must define an interpretation on all source strings,
independently of one proof. Identical opaque subtrees must get identical
values, with names disjoint from arbitrary legal source names. Check
negation and implication recognition under arbitrary schematic formula
arguments; all three schemes; ground true/¬false; and exact earlier-line
MP. Endpoint falsity alone and finite tests of substitutions do not
establish the required invariant. No semantic rewrite, extra axiom,
substitution inference, or normalized endpoint is permitted in this test.

Continue only if all-instance soundness and the exact retained endpoint's
falsification both work. A failed axiom, constant or MP case abandons this
obstruction and must be saved explicitly. A successful test would address
only this exact source interface, motivating a separately assessed basis
or bridge change; it would not obstruct ordinary Frege, revised extraction,
alternative proofs/witnesses or SAT algorithms. No repair belongs in that
same attempt.

Actual L087 pair/provenance and original-Q integration, uniform source
compiler bounds, short-proof availability, M-only witness bounds,
universal W₂, arbitrary ER data and unrestricted SAT remain unresolved.
Mathlib coverage is not checked. The original scope proposal above is retained;
step 421 below supersedes its pending-approval status without establishing
the proposed mathematical conclusion.

## Completed source review — step 421, 2026-10-23

LITERATURE_REASON: The saved target is REVIEW_REQUIRED and asks for universal
rule soundness, beyond step 420's source-convention comparison. This turn
checks that difference; it does not repeat the parity survey or attempt the
mathematics.

### Primary coverage and limitations

Joseph R. Shoenfield, *Mathematical Logic*, Addison-Wesley (1967),
[primary scan](https://w2.cs.uni-saarland.de/op/fullpaper/logics/SHOENFIELD_Mathematical_logic.pdf),
Validity Theorem, printed p.23 (PDF page index 30): its proof inducts on
theorems, using axiom validity and rule preservation. Problems 5(a)–(i),
pp.24–25 (indices 31–32), give alternative evaluations to separate omitted
axioms or rules. These are exercises with hints, not completed proofs of
our target. The inspected hints include evaluations depending on formula
shape, so an independence test need not be ordinary connective semantics.
The book supplies the method; it supplies neither this interpretation nor
its rule checks. Its own rule set differs, as step 420 records.

Fu Li, Iddo Tzameret and Zhengyu Wang, *Characterizing Propositional
Proofs as Non-Commutative Formulas*, SIAM J. Comput. 47(4), 1424–1462
(2018), [DOI](https://doi.org/10.1137/16M1107632),
[40-page author manuscript](https://www.doc.ic.ac.uk/~itzamere/Ideal_non-commutative.pdf)
(revision date unestablished), printed p.2 and Definitions 2.2–2.4 p.11:
read the three displayed schemes, literal implication abbreviation, MP,
and syntactic rule/proof definitions. Completeness is a separate defining
requirement, not a consequence of that display. This fixes the comparison
object; it proves no nonderivability statement for the local serialization.
Reuse step 420's extraction-case review; no changed extraction is proposed.

The discovery query was `propositional calculus independence interpretation
axiom schemes modus ponens primitive disjunction negation implication
soundness`. Secondary search hits were discovery leads only, not theorem
inputs. No new exact-target theorem was inspected. The standard method is
adequately sourced; the outstanding work is its explicit local application.
No originality is inferred. Mathlib matching coverage was not checked.

### Exact local boundary and discriminating attempt

Read `checker.py` lines 12–163: parser/spelling, `implies`, all three
`pattern` branches, consistent `match`, ground constants, exact MP with
strictly earlier references, and final endpoint comparison. Read
`attempt.py` lines 125–170: recursive implication decoding and valuation.
The parser admits source names such as `opaque_0`; the diagnostic's token
strings therefore cannot be presumed globally fresh. Its dictionary is
also created afresh for each diagnostic. These are scope requirements for
the proposed interpretation, not evidence that any axiom fails.

Read L097's §3 constant/template argument, L098's exact supplied-proof
hypotheses and L106's step-419 limitations. Attempt 036 stops the component
retry, not a separately tested universal invariant. No duplicate theorem
was identified in these targeted inputs. No other old stop is reopened.

Read the complete selected JSON value at
`scripts/parity-source/output/report.json` pointer
`/fixtures/three-row/endpoint_diagnostic` with the shared inspector `--full`.
It contains the exact source endpoint, decoded formula, three subtree/token
pairs and the six-entry countervaluation. The saved assignment is x=y=z=0
and all three opaque tokens 1. It reports `synthesis_invoked=false`.
These are retained diagnostic data, not a verified universal certificate.
The next attempt must evaluate the exact source endpoint under its own
consistent definition and reconcile the saved data explicitly.

Only the following specialization is covered: define the interpretation
on all legal source trees with an opaque namespace disjoint from source
names; check negation/implication recognition under arbitrary schematic
arguments, each of ax1/axS/ax2, true and not-false, and exact MP; then test
the retained endpoint. Identical subtrees must retain identical values
across all lines. Per-instance finite truth tables alone do not establish
an all-instance claim. No substitution inference is admitted by the checker;
no commutation with arbitrary source substitution is assumed. Any needed
compatibility must be proved as part of the axiom-instance argument.
This is a list of unproved obligations, not a derivation or a successful
interpretation.

Continue only if all-instance preservation and exact endpoint falsity
both succeed. Save the first failed rule case and abandon this obstruction
if either fails. Success would concern this exact serialized interface and
motivate a separately reviewed repair. It would not refute ordinary Frege,
alternative witnesses or SAT algorithms. Main gap: unrestricted SAT remains
untouched; immediate gap: reliable literal-OR source reception.

Outcome: EXPLORATION / LITERATURE / NOVELTY_UNCHECKED. The new comparison
makes one bounded mathematical attempt ready under SPECIALIZE; it supplies
no lemma, new mathematical result or result beyond the inspected sources.
No lemmas, scripts, DAG or PROOF were modified.
