# Balanced slot proof-string compiler — completed source comparison

TARGET: Construct and independently check ordinary-basis Frege proof strings for L055 §5's balanced adjacent exchange and cancellation procedures, including logarithmic-depth and full-bit bounds.
CHECKED: 2026-10-11
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched Metamath's classical axiom basis, Hilbert proof checkers and XOR proof labels; compared scoped notebook scripts, histories 162–166 and Attempt 018. No existing local slot proof-string implementation found in the searched paths; no exhaustive-absence or novelty claim.
SOURCE_EVIDENCE: Inspected Metamath ax-1/ax-2/ax-3/ax-mp, propositional completeness discussion, complete displayed xorass/xorcom/xorbi12i/xorbi12d/bitr/excxor/xor2/biid proofs and connective definitions; inspected mmverify.py substitution, assertion application, normal proof processing and final-stack checks.
COMPARISON: The known complete classical basis, fixed XOR laws and substitution checking cover the logical operations; neither these sources nor LTW verifies L055's slot compiler, expanded proof strings or all-size ledger.
GAP: Emit and independently validate fixed-schema proofs, definition elimination and paid ordinary-connective expansion; test root-cut exchange/restoration and duplicate cancellation, with explicit intermediate depths and complete bytes.
REASON: Essential logical and verifier coverage is accessible; the unmatched work is one bounded implementation/reproduction test, not an essential unread theorem or a new mathematical mechanism.
SCOPE: Exactly TARGET for balanced power-of-two padded XOR slots, literal shallow formula terms and specified adjacent pairs; retain L054/L055, L053 §9 operations and L048 unconditional conventions. No entire receiver, certificate existence, ER representation or SAT transfer.
LITERATURE_REASON: The saved REVIEW_REQUIRED target changed from informal audit to emitted strings and an independent checker; newly inspected primitive-basis, definition-elimination and verifier evidence fills that source-scope gap.

## Gap, use and decision test

The main gap remains unrestricted SAT decision/separation. The intermediate target is checked proof output for just L055 §5's exchange and identical-pair cancellation. This could validate an implementation component of the supplied-certificate receiver. Whole-receiver verification, certificate existence, arbitrary ER representation and SAT transfer remain independent unresolved obligations.

Continue if fixed schema proofs expand to the selected primitive rules and bounded slot cases pass independently, with actual/required depth, nodes and byte bounds reported. Preserve a failed rule instance, altered endpoint, unbalanced restoration or excessive depth. Narrow or abandon that implementation if it cannot meet the claimed threshold. Finite success does not prove an all-size polynomial bound; failure is not a Frege lower bound or a P-versus-NP resolution.

Reuse the unchanged semantic coverage and LTW/Kiefer/Nisan qualifications in `drafts/literature/2026-10-11-formula-origin-receiver-critical-audit.md`. No theorem there supplies the mixed-degree polynomial compiler. This review read L055 §5 and its input/scope paragraphs, L053 §9's syntactic audit, histories 162–166 and Attempt 018. The scoped script search found ER and semantic graph/witness checks, not this compiler. Attempt 018 warns against repetitive approval without new evidence; the primitive basis and verifier are the new evidence here. Representation stops remain unchanged.

## Precise primary inputs and qualifications

Sources below are live public-domain Metamath Proof Explorer pages inspected 2026-10-11, identified by stable labels and URLs. Cached pages show differing numerical ordinals; no pinned set.mm revision or local verification is claimed. Implementation must save chosen source versions and hashes with its artifacts.

The Church P2 / Lukasiewicz system described in [§§1.2–1.2.2](https://us.metamath.org/mpeuni/mmtheorems1.html) uses NOT and implication. Its named propositional completeness metatheorem identifies truth-table validity with provability. For arbitrary formulas A,B,C its exact schemas and rule are:

- [ax-1](https://us.metamath.org/mpeuni/ax-1.html): A → (B → A).
- [ax-2](https://us.metamath.org/mpeuni/ax-2.html): (A → (B → C)) → ((A → B) → (A → C)).
- [ax-3](https://us.metamath.org/mpeuni/ax-3.html): (¬A → ¬B) → (B → A).
- [ax-mp](https://us.metamath.org/mpeuni/ax-mp.html): from A and A → B infer B.

Import these named standard inputs, not a new lemma or a reproof. Completeness supplies finite proofs of fixed tautological schemas; it gives no polynomial proof-size bound for growing arbitrary tautologies. Any truth-table synthesis is restricted to a fixed schema library before substituting growing terms.

Read all displayed proof lines and logical/definition footprints for [xorass](https://us.metamath.org/mpeuni/xorass.html), [xorcom](https://us.metamath.org/mpeuni/xorcom.html), [xorbi12i](https://us.metamath.org/mpeuni/xorbi12i.html), [xorbi12d](https://us.metamath.org/mpeuni/xorbi12d.html), [bitr](https://us.metamath.org/mpeuni/bitr.html), [biid](https://us.metamath.org/mpeuni/biid.html), [excxor](https://us.metamath.org/mpeuni/excxor.html) and [xor2](https://us.metamath.org/mpeuni/xor2.html). Associativity and commutativity have no logical premises and apply to arbitrary formulas. xorbi12i requires both argument equivalences; xorbi12d retains a common antecedent in both hypotheses. bitr is closed transitivity with both equivalences in its antecedent. biid proves self-equivalence; excxor/xor2 identify XOR with ordinary-connective expressions. Their displayed steps invoke earlier theorems, not merely the primitive axioms: recursively expand those fixed proofs before use. Their applicability does not establish the balanced exposure/restoration algorithm or its costs.

Read [df-bi](https://us.metamath.org/mpeuni/df-bi.html), [df-an](https://us.metamath.org/mpeuni/df-an.html), [df-or](https://us.metamath.org/mpeuni/df-or.html), [df-xor](https://us.metamath.org/mpeuni/df-xor.html) and the justification [bijust](https://us.metamath.org/mpeuni/bijust.html). The primitive expansions are biconditional = ¬((A→B)→¬(B→A)), AND = ¬(A→¬B), OR = ¬A→B, and XOR = negated biconditional. df-bi explains eliminating definition instances by primitive proofs. Metamath formally treats definitions as axioms; these labels cannot remain unpaid primitive Frege rules.

Read [imor](https://us.metamath.org/mpeuni/imor.html), including its four displayed proof steps: implication is equivalent to ¬A OR B. This is a paid connective translation, not literal equality to the database's OR expansion, which introduces double negation. [dftru2](https://us.metamath.org/mpeuni/dftru2.html) supports using q→q as a truth formula. Choose explicit truth/falsehood formulas q→q and ¬(q→q), with a fixed q as L055 permits, rather than importing the database's quantified truth definition.

No matching cancellation-to-fixed-falsehood or zero-to-two-zero-slots source proof was read. These fixed tautological templates fall within the named completeness theorem. Their actual finite primitive proofs must be generated and checked in the implementation turn. No cancellation derivation or estimate is supplied here; essential logical coverage is present, while proof-string construction is precisely the target.

## Concrete format and independent checker

Use the three-schema MP-only primitive system as the complete Frege anchor. Serialize every fully parenthesized native line, axiom tag/substitution and earlier MP references. XOR, equivalence, constants and source theorem names are compiler notation; the checker accepts only primitive axiom instances and MP. Expand source proofs or synthesize fixed schema proofs once, avoiding an unnecessary mathematical reproof of standard logical laws.

Also emit every line with implication expanded to NOT/OR, after eliminating other abbreviations, to test L055's AND/OR/NOT costs. Independently match expanded axioms against the fixed translated schemas and expanded MP against the exact antecedent/consequent. Retain the native proof for the complete-system anchor. Do not claim the translated image alone is a separately proved complete system for all arbitrary NOT/OR formulas. If ordinary input terms need syntax normalization, supply paid fixed connective-law bridges and preserve one chosen expansion at both equality endpoints. This review approves testing that specialization, not assuming it succeeds.

The checker must reparse serialized trees, consistently match repeated schema variables, require earlier in-range references and exact MP syntax, and compare the last line with the requested endpoint. It must not import the emitter's rewrite planner or accept Boolean equivalence as an inference. Recompute depths, nodes and bytes from disk. Corrupt an axiom occurrence, MP antecedent, reference and final endpoint and require rejection.

Primary verifier comparison: [Raph Levien, David A. Wheeler and contributors, mmverify.py](https://raw.githubusercontent.com/david-a-wheeler/mmverify.py/master/mmverify.py), live master inspected 2026-10-11, not installed or executed. Read apply_subst (263–274), complete treat_step (441–492), treat_normal_proof (493–512) and verify's final-stack equality checks (577–606). It checks typed substitutions and essential hypotheses before forming conclusions. A native .mm artifact could use this existing independent verifier after source pinning and an axiom allowlist. The proposed separate line-format checker is unimplemented; no independence or soundness test has passed. Other GitHub checker results were unread leads. Failed guessed xorid/xorbi1d and old downloads/mmverify.py URLs were bypassed by accessible primary material; no essential source blocker persists.

## Continuation and completion

Test M=2 and larger power-of-two slot capacities, including a root-cut pair, literally repeated suffix terms, fixed zero/truth formulas and shallow composite terms. Restore the original slot shape. Save native and expanded proofs, the fixed schema library and full checking/measurement certificates under the notebook scripts subfolder; report concise actual/required bounds, failures and artifact paths. Pay every copied term, raw name, framing byte, rule tag and reference. No hash-only formula substitutes for written text.

Essential inputs are L054 §5, L055 §5/§8, L053 §9 and L048 unconditional conventions. Fixed a and formal IPS identities remain eventual-receiver assumptions, not slot-proof axioms. No cross-notebook input. Full matching Mathlib coverage remains not checked; Metamath is not Mathlib coverage.

Step 167 is EXPLORATION / LITERATURE / NOVELTY_UNCHECKED / literature_comparison. New source comparison approves the unchanged TARGET with SPECIALIZE. No new mathematics, emitted proof, verified bound or originality claim. Mathematical exploration usage remains one after step 164. The next turn defaults to one RESEARCH implementation test, normally REPRODUCTION, under this saved assessment.
