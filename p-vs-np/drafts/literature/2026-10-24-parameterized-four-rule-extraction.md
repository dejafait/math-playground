# Parameterized supplied-proof extraction — bounded scope approved

TARGET: Implement a bounded parameterized L108 extractor and strict receiver for supplied literal-four-rule proofs, retaining arbitrary ordered original alphabets, all source lines and complete dictionaries.
CHECKED: 2026-10-24
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 456 reused steps 425/427/448 primary coverage; inspected L108 §§1–5, L035/L036 contracts, the complete emit_nonzero/receive_nonzero/check_nonzero modules, literal checker and used correction routines; scoped duplicate search found only fixture-bound extractors. Attempts 037/038 remain parked. Static comparison identifies the legal original name 1 as incompatible with raw fixture label transport, and duplicate-key checking must precede generic source reception.
SOURCE_EVIDENCE: Reused Shoenfield (1967) §2.6 p.21 and §3.1 pp.27–30; LTW 40-page author manuscript Definition 1.3 p.6, Theorem 3.1/Lemma 3.3 pp.13–14; audited local L035/L036 and L108 §§1–5, with finite evidence in §§6–9. No fresh external passage or executable test is claimed in step 456.
COMPARISON: L108 already supplies the all-size proof/alphabet theorem and dense dictionary references; the inspected external formula theorem does not certify reused-DAG code. Generic execution is covered only with caller-bound source/goal/dictionary, typed symbol namespaces, whole-source retention, strict parsing and declared finite verification caps. Raw fixture name substitution is insufficient.
GAP: Ready for the bounded parameterized implementation below; implementation, independent generic reception and all-size executable resource guarantees remain unverified. Exact-word verification is allowed to stop at its declared caps.
REASON: The changed serialization and authorization scope can reproduce audited L108 without a new algebraic premise; no essential unread mathematical source remains. This approval does not authorize library synthesis, source-proof construction or a new theorem.
SCOPE: Arbitrary finite ordered checker-legal original alphabets (including empty/unused entries and legal names such as 1, x1 and or), nonempty exact literal-four-rule-v1 proofs ending at the caller-authorized goal, complete caller-supplied Boolean/pair-once dictionaries with unchanged positions, typed dense symbol reception, all source roots and bounded exact-word diagnostics.
COVERED_TARGET: Implement a bounded parameterized L108 extractor and strict receiver for supplied literal-four-rule proofs, retaining arbitrary ordered original alphabets, all source lines and complete dictionaries.

LITERATURE_REASON: Step 455 proposed parameterization outside the fixed-fixture
scope. This separate review resolves its serialization, name and authorization
boundary using unchanged primary coverage, without another broad search.

Essential inputs: L035, L036 and L108 §§1–9; the complete inspected
`scripts/four-rule-extraction/{emit_nonzero.py,receive_nonzero.py,check_nonzero.py}`
interfaces and the narrowly used literal checker/correction routines.
Outputs 449/451/453/455 provide fixed regression evidence to preserve.

The main gap remains unrestricted SAT decision/separation. A parameterized
supplied-proof interface could permit later conditional source compositions
to use the existing abstract extractor without rewriting a fixture-specific
program. It would not supply source proofs, prepare a library or establish
all-size polynomial complexity of free-word verification. Caps must remain
explicit and failures visible; complete dictionaries include unused names
and every required Boolean/commutator position. Any admitted name or
constant convention must match L108 and the actual checker exactly.

The review's discriminating test passes at the contract level: the changes
below implement existing dense references, syntax checks and graph contracts;
they require no new rule, normalization or algebraic identity. The executable
test remains pending. Library synthesis stays parked under Attempts 037/038.
No short-proof availability, M-only bound, universal W₂, arbitrary ER data
or SAT transfer is assumed.

## Reused primary results and qualifications

Joseph R. Shoenfield, *Mathematical Logic*, Addison-Wesley (1967), §2.6
p.21 supplies the literal axiom and four rules; §3.1, Tautology Theorem
(Post), p.27, proof pp.28–30 is background completeness
([primary scan](https://w2.cs.uni-saarland.de/op/fullpaper/logics/SHOENFIELD_Mathematical_logic.pdf)).
The local true and ¬false axioms are explicit additions. Supplied-proof
extraction uses neither completeness nor any bound on finding source proofs.
Reuse the actual source inspection recorded in the step-425 assessment
`2026-10-23-complete-or-rule-extraction.md` and step-427 audit coverage.

Li–Tzameret–Wang, *Characterizing Propositional Proofs as Non-Commutative
Formulas*, SIAM J. Comput. 47(4), 1424–1462 (2018),
[DOI](https://doi.org/10.1137/16M1107632), is received through the
[40-page author manuscript](https://www.doc.ic.ac.uk/~itzamere/Ideal_non-commutative.pdf),
revision date unestablished. Definition 1.3 p.6 and Theorem 3.1/Lemma 3.3
pp.13–14 allow a prime field, hence F₂, but treat three schemes/MP after
tree-like conversion. They do not establish this four-rule DAG implementation.
Their full formula theorem is not reproved or used to certify the code.

L035/L036's audited constructive inputs allow constants, zero, arbitrary
acyclic affine graphs and complete dictionaries, with full bounds O(E⁴)
and O(E⁶). Their source comparison includes LTW
[arXiv:1412.8746v4](https://arxiv.org/pdf/1412.8746v4), 11 September 2015,
Lemma 3.7 p.18 (formula-input commutators), and Raz–Shpilka's
[16-page author manuscript](https://www.cs.tau.ac.il/~shpilka/publications/RazShpilka_PIT.pdf),
Lemma 2 Step 1 p.5 (serial/parallel graphs). The arbitrary-ABP correction
extension is justified by the canonical local proofs, not attributed to
those narrower external statements. L108 §§2–5 already supplies the exact
rule seeds, right transitions, all-root induction and C Q¹⁴ ledger in the
full supplied input. The next implementation reproduces these results;
no reproof or stronger bound is needed. Mathlib full matching coverage
remains unchecked; no absence claim is made.

## Exact admitted implementation interface

1. **Trusted request versus certificate.** The caller supplies source bytes
   (or their externally selected path and expected SHA), exact goal tree,
   ordered alphabet and complete dictionary. A request may be a separate
   manifest; it must not be recovered solely from the candidate certificate.
   Compare actual raw source bytes, SHA, header and last endpoint against
   that request. Preserve all source bytes and records. A certificate's
   self-reported digest or goal is not independent authorization.
2. **Source syntax.** Keep literal-four-rule-v1's exact header/record fields,
   ordered prefix trees, constants true/false, seven primitive tags and
   strictly backward integer references. Accept arbitrary finite ordered
   distinct names admitted by checker.tree, excluding true/false as originals;
   other name syntax is outside this serialization, not outside L108.
   Reject duplicate JSON keys before calling the existing checker; it uses
   ordinary json.loads and is not alone a strict generic parser. Enforce
   exact types, arities, nonempty source and exact final goal. No automatic
   rebracketing, rule substitution, renaming or deletion is authorized.
3. **Symbols and dictionaries.** Keep input alphabet order and every supplied
   dictionary position, including unused entries. Validate exactly one Boolean
   axiom per original and one commutator per index pair i<j, with independent
   placeholder names and the declared ordered words. Do not regenerate an
   input dictionary with different names/order. Internal x1,…, b:i and t:i:j
   are dense implementation tokens only. Relocate them through an explicitly
   checked map to typed original/placeholder indices. Scalar 1 is a separate
   tag. A dense-token graph with a typed name table is acceptable; original
   display strings must not be used to distinguish these namespaces.
4. **Concrete incompatibility found.** checker.tree accepts the nonempty
   alphanumeric string `1` as an original name. receive_nonzero.Arithmetic
   instead interprets any edge symbol `1` as the unit before checking original
   membership; emit_nonzero.translation also only indexes A/B. Thus replacing
   ['A','B'] with an arbitrary list while transporting raw strings is not
   sufficient. Dense indexed references already used in L036/L108 avoid
   this encoding collision. Test this case, internal-looking originals x1,
   or/not as atomic strings, reordered alphabets and unused names explicitly.
5. **Graph and endpoints.** Parameterize N proof vertices and all N indexed
   roots, final sink N, and every seed/transition occurrence reconstructed
   independently from the received source. Preserve both cut occurrences
   even if premise indices coincide. Strictly receive integer endpoints
   (excluding bool/float), acyclicity, affine-label entries, fresh block
   interiors, complete partitions and exact connectors/arguments. Preserve
   parallel edges, zero labels and cancellations. Only original graphs may
   enter correction constructors; cut's left prefix stays within its seed.
6. **Independent reception.** The receiver must not import the emitter or
   correction evaluator. Receive typed dictionaries/source first, then check
   all blocks and both exact formal identities at every root, including unused
   lines, against translations of actual trees. Evaluate free/zero/axiom modes
   with typed original indices as word letters. Typed evidence comparisons
   must retain the earlier bool/int/float repair. A neutral duplicate-label
   cancellation may validly pass; do not demand byte equality with one emitter
   output when the full contract still holds. Constructor counters are bounded
   claims until independently checked, not evidence of actual construction cost.

## Finite bounds, test and stop decision

Keep the existing six finite diagnostic caps unless separately justified:
2,000,000 vertices plus edges; 200,000,000 certificate bytes; 1,000,000
polynomial words; word length 256; 100,000,000 multiplication pairs;
20,000,000 stored table words. Add declared input byte/tree-depth/label-entry
limits and preflight checks before large allocations or copies; a depth cap
is a bounded implementation limit, not a depth premise of L108. Check the
source/request before parsing unbounded content and preflight dictionary
cardinality before quadratic construction. Caps cannot be raised by a
certificate. These counters do not bound all process memory or parsing work.

The inspected m.witness performs copies internally, while b.copy_into wraps
other products/Boolean assembly. Retain the existing exact-copy preflight
before m.witness and guards around remaining copies/connectors; parameterizing
only the final graph check would miss intermediate allocations. Account for
dictionary and serialized output separately. On failure write stage, actual
quantity, required bound and artifact path; do not report a partial check as
acceptance. No exact-word expansion, source search or path enumeration belongs
to L108's polynomial construction theorem. A bounded diagnostic may reject a
legal large proof without contradicting that theorem.

Continue implementation only if complete accepted examples and discriminating
malformed inputs meet this interface. Preserve outputs 449/451/453/455 without
rewriting them; exercise empty/singleton/larger alphabets, unused records and
names, colliding display names, exact endpoint mismatch, source/dictionary
substitution, duplicate keys, numeric aliases and cap stops. The two old
fixtures remain regressions, not a general proof. Save complete certificates
and relevant word evidence, with actual/required bounds and explicit failures.
Stop the bounded attempt on a literal mismatch, lost record/name/position,
uncovered correction input or exhausted cap; preserve unfinished work.

No new mathematical result or script was written or run in this literature
step. The negative finding changes the proposed encoding, not the L108
argument. A later critical audit is still needed after implementation.
