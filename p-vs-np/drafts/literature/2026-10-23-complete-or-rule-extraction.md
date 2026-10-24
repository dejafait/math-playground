# Complete literal-OR replacement — completed source comparison

TARGET: Assess Shoenfield's complete literal-OR rule system as a replacement for L097's source presentation, including affine-ABP extraction for expansion, contraction, association and cut.
CHECKED: 2026-10-23
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 425 searched Shoenfield/expansion/contraction/cut with noncommutative IPS and branching-program conclusion extraction; reused step 420 and checked L097 §4, L098 §§2–3, L106 §2, L107 §§4–5, Attempt 036 and the earlier resolution/Frege assessments. No inspected source gives the four-rule exact affine-ABP receiver; failed searches do not establish novelty.
SOURCE_EVIDENCE: Shoenfield, Mathematical Logic (1967), §2.6 p.21 and §3.1 Tautology Theorem (Post) p.27, with proof pp.28–30 reused from step 420; LTW 40-page author manuscript, Definition 1.3 p.6, Theorem 3.1/Lemma 3.3 pp.13–14 and Definitions 2.2–2.4 p.11. Primary rule list, theorem hypotheses and complete assumption/axiom/MP extraction cases were read; exact versions and reuse are recorded below.
COMPARISON: Shoenfield covers literal-OR completeness; LTW states a stronger general Frege-to-formula simulation but its inspected extraction implements three schemes/MP on a tree-like proof. Neither supplies the proposed four-rule graph recurrence or full binary ledger. Existing original-only L035/L036 corrections and L097's right-transition graph provide assessed ingredients for a separate specialization attempt.
GAP: Prove exact algebraic reception of the propositional axiom and all four rules, including compatible witness-multiplier placement and polynomial DAG reuse; retain the local ground constants and both formal identities. Constant-template completeness and the later exact-fg compiler composition remain separate obligations.
REASON: Essential sources and correction interfaces are accessible; a bounded mathematical attempt is justified without another broad survey. SPECIALIZE approves the stated scope for later work, not a replacement theorem, a repaired compiler or any new mathematical result in this literature turn.
SCOPE: Assumption-free explicit acyclic proofs on occurrence variables y with primitive ordered OR/NOT trees, Shoenfield's propositional axiom and four propositional rules, augmented only by true and ¬false; unchanged complete original Boolean/commutator dictionary B. No extension, substitution-inference, rewriting-modulo-equivalence or renaming rule. Measure full proof, alphabet and dictionary bits before extraction.
COVERED_TARGET: Test a right-multiplier affine-ABP conclusion extraction for Shoenfield's four literal-OR rules plus true and ¬false, preserving exact K(y,0)=0 and K(y,B(y))=tr(T) with polynomial full size/time in the written proof and unchanged dictionary.

## Preserved pending proposal — step 424

The following proposal predates this comparison. Its pending process
status is superseded by the completed review below; its mathematical
requirements and the unchanged-interface stop are retained.

This is a pending continuation, not an approval or mathematical attempt.
The completed audit is preserved in L107 §5. Do not rerun the unchanged
compiler, repeat the opaque invariant audit, or treat the old stop as a
ban on a different complete presentation.

Reuse `drafts/literature/2026-10-23-literal-or-source-convention-review.md`
for the inspected primary completeness passages. Joseph R. Shoenfield,
*Mathematical Logic*, Addison-Wesley (1967), §2.6 p.21 and the Tautology
Theorem (Post), §3.1 p.27 with proof pp.28–30,
[primary scan](https://w2.cs.uni-saarland.de/op/fullpaper/logics/SHOENFIELD_Mathematical_logic.pdf),
are the identified source. The propositional axiom is ¬A∨A; the rules
recorded there are expansion A / B∨A, contraction A∨A / A,
association A∨(B∨C) / (A∨B)∨C, and cut
A∨B, ¬A∨C / B∨C. Its first-order rules are not intended inputs.
Do not silently attribute true/¬false axioms to that book.

Compare Fu Li, Iddo Tzameret and Zhengyu Wang, *Characterizing
Propositional Proofs as Non-Commutative Formulas*, SIAM J. Comput.
47(4), 1424–1462 (2018),
[DOI](https://doi.org/10.1137/16M1107632),
[author manuscript](https://www.doc.ic.ac.uk/~itzamere/Ideal_non-commutative.pdf),
Lemma 3.3 pp.13–14. The manuscript revision date remains unestablished.
The earlier comparison inspected its three-scheme/MP cases, not an
all-rule affine-ABP replacement. Retrieve only essential primary rule
and extraction cases before larger passages; distinguish a known
formula/circuit simulation from the needed explicit affine-ABP bound.
No new external source was consulted in step 424.

Essential local inputs for this proposed comparison are L107 §§4–5,
L097 §4's corrected axiom seeds and graph-of-transitions construction,
and the relevant interfaces of L035/L036 if their hypotheses are needed.
L098 §§2–3 and L106 §2 specify the endpoint/template reception to retain.
The intended downstream use is a justified source presentation for the
same literal source trees and ultimately the original occurrence product;
no witness identity, source compiler or proof-length bound is established
for the replacement. In particular preserve both formal witness identities,
arbitrary formula arguments, full source bits and proof-reference reuse.

Discriminating review test: determine whether a primary theorem actually
covers each replacement rule with the required representation, or isolate
the precise unproved algebraic reception cases and assess a bounded
specialization. Missing essential cases keep the target literature-only;
a source mismatch must not be hidden by endpoint rewriting or by citing
basis equivalence as an affine-ABP theorem. Mathlib matching coverage is
unchecked. Actual L087/original-Q integration, short source proofs,
M-only bounds, universal W₂, arbitrary ER data and unrestricted SAT remain
independent unresolved obligations.

## Completed comparison — step 425, 2026-10-23

LITERATURE_REASON: The changed source rules are outside the old ready
extraction assessment. Step 420 supplies reusable completeness evidence;
the essential new comparison is the representation and reuse of each
changed rule, rather than another parity or completeness survey.

### Sources actually inspected and what they cover

Use Joseph R. Shoenfield, *Mathematical Logic*, Addison-Wesley (1967),
§2.6 p.21 and §3.1, **Tautology Theorem (Post)**, p.27, proof pp.28–30,
[primary scan](https://w2.cs.uni-saarland.de/op/fullpaper/logics/SHOENFIELD_Mathematical_logic.pdf).
Step 425 reread the rule list and theorem; the detailed propositional
proof cases remain covered by step 420. Only the propositional fragment
is proposed. The book's first-order axioms and quantifier rule are
excluded. Its completeness statement supplies no ABP resource bound.

Use Fu Li, Iddo Tzameret and Zhengyu Wang, *Characterizing Propositional
Proofs as Non-Commutative Formulas*, SIAM J. Comput. 47(4), 1424–1462
(2018), [DOI](https://doi.org/10.1137/16M1107632), inspected through the
[40-page author manuscript](https://www.doc.ic.ac.uk/~itzamere/Ideal_non-commutative.pdf).
Revision date remains unestablished. Theorem 3.1, printed p.13, states
polynomial formula-size extraction of tr(T) from translated assumptions
over Q or a prime field, so F₂ is included. Lemma 3.3, pp.13–14, supplies
both identities and a fourth-power tree-ancestry bound. Its proof treats
assumptions, three axiom schemes and MP, after tree-like conversion;
it does not give the four proposed rule cases. Definitions 2.2–2.4,
p.11, retain soundness and implicational completeness. Basis invariance
alone does not supply these missing exact graph transitions. Retain
L097's correction of the suspect Boolean-only seed argument.

The strongest inspected general formula simulation is therefore a
comparison, not a direct all-rule affine-ABP import. No reproof of that
general simulation or of completeness is proposed. The separate task
tests a particular graph realization with existing correction inputs.
Do not apply the paper's numerical tree bound unchanged to a reused DAG.

### Rule-by-rule scope of the separate specialization

Here a,b,c, if used in the later proof, must denote original-only
translations of the actual formula arguments, never prior placeholder
witnesses. The following are obligations, not proved recurrences.

| Exact source step | Assessed ingredient | Remaining reception test |
| --- | --- | --- |
| Axiom ¬A∨A | L036 on the translated argument | Write its exact seed and both identities. |
| Expansion A / B∨A | Ordered translation; L035 | The new formula is placed on the left. Test a right-multiplier realization with a local original-only correction, rather than copying the old witness prefix. |
| Contraction A∨A / A | L036 | Check the ordered correction and preservation of zero substitution. |
| Association A∨(B∨C) / (A∨B)∨C | Associativity in the free algebra | Retain the exact source trees and identify their translated polynomials; do not admit propositional rewriting as a rule. |
| Cut A∨B, ¬A∨C / B∨C | L035; the written premise translations | Establish the ordered correction, both premise multipliers and a common orientation compatible with graph reuse. |
| Ground axioms true, ¬false | Existing zero seeds in L097 §4 | Retain their declared local status and full dictionary; do not attribute them to Shoenfield. |

L035 receives two arbitrary explicit original-only affine graphs, including
constant/zero graphs and nonextremal or coincident roots. It supplies a
commutator-only witness with zero-placeholder value zero, full size
O(E³ log(E+2)) and polynomial construction time. L036 receives one such
graph with complete Boolean/commutator framing and supplies its Booleanity
witness in O(E⁵ log(E+2)) bits and polynomial time. The formula arguments
here can use the ordered formula-to-graph component already received in
L097. These promises cover the contemplated correction inputs, not the
unproved arrangement of the rule transitions. No correction call may
receive a previously extracted placeholder-containing witness.

L097 §4 already proves how right-multiplier transitions and independently
copied seeds share earlier proof-line vertices without unfolding ancestry.
It does not prove that the four replacement rules have that form. The
bounded idea to test is whether original-only commutator corrections
suffice to put all witness propagation in that orientation. If this fails,
the old graph proof cannot be cited as a size bound for mixed left/right
contexts. This review supplies no recurrence or construction solving it.

The constants are an explicit local augmentation, with the existing LTW
falsity translation unchanged. Exact extraction from a supplied legal
augmented proof is the covered target. Existence of fixed constant-bearing
templates in that system requires its own applicability argument using
the source completeness theorem and the two ground axioms. It is not
assumed in this extraction target, and no new constant-completeness lemma
is derived here. This distinction permits a useful intermediate result
while leaving the later compiler obligation visible.

### Search, failures and decision test

Queries actually issued included `noncommutative IPS Shoenfield expansion
contraction cut algebraic branching programs Frege`, `"Shoenfield"
"non-commutative" proofs expansion`, `"Shoenfield" "expansion"
"noncommutative"`, `"Frege" "cut" "noncommutative" "contraction"`,
`"noncommutative" "conclusion" "Frege" "branching"`, and
`"Shoenfield" "contraction" "algebraic" proofs`. Search leads to
surveys/ECCC metadata added no inspected four-rule graph theorem; neither
snippets nor secondary summaries are theorem inputs. No unread essential
source remains for this bounded attempt. PDF text supplied the statements
and complete LTW cases; screenshot requests yielded no inspectable images.
Mathlib matching coverage has not been checked.

The local duplicate check used the earlier resolution/Frege assessments,
L097 §4 and L098 §§2–3. Their proof-dependent graph receiver uses the old
rules; their occurrence substitutions and tester correction do not
establish the replacement rule induction. Attempt 036 and audited L107
§§4–5 stop the unchanged interface, not Shoenfield's different system.
No old compiler or opaque-interpretation test was rerun. Arbitrary
renaming/substitution inference and the copying/compression mechanisms
discussed by L099–L103 are outside this target; no such inference is added.

The main gap remains unrestricted SAT. The intermediate target is the
COVERED_TARGET above: for any supplied legal assumption-free proof ending
in the exact formula T, construct K with both displayed formal identities,
only the original alphabet and unchanged B, and one fixed full-bit/time
polynomial in the explicit proof, alphabet and dictionary. Count all
records, repeated formula arguments, unused proof lines, names, references
and independent correction copies before claiming that polynomial.
No witness output or degree data may enlarge the original input parameter.

Continue this mechanism only if every source case admits an exact ordered
identity and the graph can realize them with paid proof reuse. Abandon
the proposed right-multiplier realization if a required correction needs
placeholder-containing operands, changes tr(T), or the claimed bound
requires ancestry unfolding; such a failure would not refute alternative
extractions. This is an all-size proof attempt, not a request to enumerate
unbounded formula arguments or merely check sample Boolean valuations.

Its plausible later use is repairing L097/L098's source reception and
eventually L106's exact parity endpoint. Those compositions are not part
of this step or automatically covered by this target. Fixed-template
constant reception, full original-Q integration, the general compiler
ledger, short source proofs, M-only bounds, universal W₂, arbitrary ER
data and SAT remain unresolved. Newly recorded ready continuation coverage
is available for the supervisor's separate next-turn approval.

Outcome: **EXPLORATION / LITERATURE / NOVELTY_UNCHECKED**. This is a
completed source/interface comparison with a concrete bounded continuation,
not a new algebraic result or progress beyond the cited mathematics.
No lemma, mathematical script, DAG or PROOF content changed.
