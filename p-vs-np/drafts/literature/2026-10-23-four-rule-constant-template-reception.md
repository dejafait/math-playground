# Constant-bearing templates in the four-rule system — completed comparison

TARGET: Assess constant-bearing tautology-template reception in L108's exact four-rule system with only true and ¬false as ground axioms.
CHECKED: 2026-10-23
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 429 reused steps 420/425/427, checked L108's exact declaration, L107's stopped interface and Attempt 036, and searched Shoenfield with truth constants, tautology theorem, atoms and the four rules; no inspected theorem directly gives the local constant-bearing full-bit template interface. Failed discovery is not evidence of novelty.
SOURCE_EVIDENCE: Shoenfield, Mathematical Logic, Addison-Wesley (1967), §2.4 pp.14–15, notation pp.17–18, §2.6 pp.21–22 and §3.1 pp.26–30; primary scan reread for the language, exact rule list, Tautology Theorem (Post) p.27, detachment and all propositional completeness cases. Earlier LTW coverage is reused only for comparison.
COMPARISON: The cited consequence theorem and its propositional-only proof cover the constant-free logical ingredient, including proved premises. Primitive Boolean constants, literal replay with just true/¬false ground axioms, and full-bit instantiation costs require the bounded local specialization below; the book's individual constants are terms, not truth constants.
GAP: Establish the precise constant reception and literal line-by-line instantiation argument for a fixed finite tautology-template library, with no extra rules or auxiliary final names, and charge every copied tree/reference. No such lemma or compiler is established in this review.
REASON: Primary hypotheses and essential proof cases are accessible and sufficient to assess a separate bounded specialization; no essential source blocker remains. Do not reprove general completeness or treat this scope approval as a proof verdict.
SCOPE: Fixed finite libraries of OR/NOT templates with formula slots and Boolean constants true/false, tautological under their prescribed Boolean values; exact L108 rules and ground axioms only. Template-library-dependent constants are allowed, but a polynomial proof bound for arbitrary input tautologies is outside scope.
COVERED_TARGET: Prove reception and full-bit instantiation bounds for fixed constant-bearing tautology templates in L108's exact four-rule system.

## Preserved proposal — step 428

The following proposal predates the completed comparison below. Its
pending process status is superseded; its mathematical cautions remain.

This is a continuation proposal, not an approved theorem, source review
or mathematical attempt. The completed step-428 audit is canonical in
L108 §5 and does not depend on settling this proposal.

Main gap: unrestricted SAT. Intermediate target: assess reception of
fixed constant-bearing tautology templates in exactly L108's system.
Plausible downstream use: justify template availability before attempting
an occurrence-transfer or parity-compiler composition. The threshold is
a precise applicable completeness input or an assessed specialization
that preserves literal conclusions and only the permitted rules. A
theorem about another basis, or Boolean equivalence alone, is insufficient.

Reuse `drafts/literature/2026-10-23-complete-or-rule-extraction.md` and
`drafts/literature/2026-10-23-four-rule-extraction-critical-audit.md`.
The identified primary lead is Joseph R. Shoenfield, *Mathematical Logic*,
Addison-Wesley (1967), §2.6 p.21 and §3.1 pp.27–30
([primary scan](https://w2.cs.uni-saarland.de/op/fullpaper/logics/SHOENFIELD_Mathematical_logic.pdf)).
Retrieve only the needed language hypotheses and relevant completeness
proof cases if earlier inspected coverage is insufficient. The two
ground axioms are local additions and must not be attributed to the book.
No new external source has been read for this proposal.

Essential local input: L108's exact rule/language declaration and
supplied-proof scope; L035/L036 enter only through its audited receiver,
not as a source of propositional completeness. Compare L107 and Attempt
036 solely to preserve the stopped old-interface evidence. Do not rerun
that compiler or assume its failure applies to this different system.
Check for an existing applicable local assessment before new browsing.

Continue only if the separate review identifies exact ready coverage or
a bounded, independently testable specialization; otherwise record the
essential missing hypothesis/source and an appropriate route decision.
Do not derive or approve new mathematics during that review. Template
instantiation costs, L097/L098/L106 composition, original-occurrence/Q
integration, source-proof availability, M-only bounds, universal W₂,
arbitrary ER data and unrestricted SAT remain unresolved. Mathlib
matching coverage is unchecked.

## Completed source comparison — step 429, 2026-10-23

LITERATURE_REASON: The new target changes the language hypothesis from
supplied-proof extraction to existence of proofs for constant-bearing
templates. Steps 425/427 explicitly excluded that input. Reuse their
extraction coverage and inspect only the missing completeness boundary.

### Primary coverage actually inspected

Joseph R. Shoenfield, *Mathematical Logic*, Addison-Wesley (1967),
[primary scan](https://w2.cs.uni-saarland.de/op/fullpaper/logics/SHOENFIELD_Mathematical_logic.pdf),
is the source; page numbers below are printed pages. The copyright page
identifies 1967. §2.4 pp.14–15 defines atomic formulas and the language;
its constants denote individuals. The notation on pp.17–18 fixes literal
abbreviation expansion and right association. §2.6 pp.21–22 gives the
four propositional rules and permits additional nonlogical axioms.

§3.1 pp.26–27 defines independent truth valuations on elementary formulas.
The **Tautology Theorem (Post), p.27**, covers a tautological consequence
of finitely many proved premises; its corollary covers tautologies.
Its proof on pp.28–30 establishes commutation and detachment, then
handles a complementary-literal base case, disjunction, double negation
and negated disjunction, with explicit supporting rearrangements. These
cases use propositional axioms and the four rules, without first-order
axioms or quantifier inference. The semantic substitution remark on p.30
does not itself provide a serialized proof-substitution rule or bit bound.

This supplies the stronger consequence form needed for comparison,
rather than only completeness without premises. It does not state the
local truth-constant language or its encoding bound. These are the
identified specialization obligations, not missing primary proof cases.

### Exact applicability boundary and assessed mathematical continuation

L108's hypotheses admit primitive ordered OR/NOT trees, true and false,
and only true and ¬false as extra ground axioms. Its independent audit
establishes extraction from supplied proofs, not their existence. L035
and L036 enter only through that audited receiver; they are not inputs
to propositional completeness. No detailed algebraic proof needs to be
reopened for this review.

The separate continuation should justify use of the inspected consequence
theorem by comparing the two truth constants with two designated
propositional atoms and their respective positive/negative premises.
It must specify a syntactic realization of the finite slot alphabet,
retain only the propositional proof fragment, and verify replay into
the actual L108 language. The intended premise images must be exactly
the permitted ground axioms, with no residual assumptions or auxiliary
names. This describes a proof obligation, not a derivation performed here.
One may instead specialize the cited proof's base case if that gives a
cleaner exact argument; no reproof of its connective cases is warranted.

For a fixed finite template library, the next attempt must distinguish
finite proof existence from a uniform instantiation bound. After selecting
fixed template proofs, it must verify every axiom and every rule under
literal replacement of slots by arbitrary formula trees, including
constants and empty original alphabets, while preserving ordered children,
bracketing and backward references. This is a metalevel construction
of legal records, not a new substitution inference. All formula copies,
actual name bits, proof framing and relocated references must be charged.
Any constants in a bound may depend on the fixed library. No polynomial
bound in the size of an arbitrary tautology, efficient tautology solver,
or polynomial source-proof availability is assessed or inferred.

The primary theorem supplies general completeness and consequence closure;
the necessary local work concerns this changed language and complete
encoding. A precise citation plus that applicability argument is the
appropriate result, without claiming a new completeness theorem. It is
not enough to replace a requested endpoint by a Boolean-equivalent tree.

### Search, duplicates, stopped routes and decision test

Queries actually issued were `"Shoenfield" "truth constants" tautology
theorem`, `"Shoenfield" "Tautology Theorem" "atoms"`, `"Shoenfield"
"expansion" "contraction" "truth constants"`, and `"Shoenfield"
propositional completeness constants "false" "true" cut`.
Search results also suggested a Boyer–Moore mechanization report and
the Nqthm reference guide. Their full hypotheses/proofs were not inspected;
they are unread leads, not theorem inputs or essential blockers. No
search snippet or secondary source is used to justify reception.

Reused the completed comparisons in
`2026-10-23-complete-or-rule-extraction.md` and
`2026-10-23-four-rule-extraction-critical-audit.md`, and the primary-syntax
comparison `2026-10-23-literal-or-source-convention-review.md` (all in this
directory). Their exact declarations leave the present input unresolved;
none is a duplicate constant-template theorem. LTW's 2018 SIAM paper,
as inspected there, supplies the translation/extraction comparison, not
the missing literal four-rule constant reception. No LTW source refresh
is needed. L107's exact old three-scheme/MP obstruction and Attempt 036
remain preserved; neither is a ban on the distinct L108 system. The old
parity compiler was not rerun. Mathlib matching coverage is **not checked**;
no absence or complete formalization claim is made.

Main gap: unrestricted SAT decision/separation. Intermediate target: the
single COVERED_TARGET above. Plausible downstream use: justify the fixed
logical-template input before a separately assessed occurrence transfer
or parity-source composition. Continue if a precise citation and explicit
replay argument yield exact assumption-free template records using only
the permitted rules, with one full-bit instantiation bound per fixed
library. Abandon this specialization if it requires an additional rule,
unremoved assumptions, auxiliary output names or endpoint normalization;
record a concrete failed obligation rather than retrying the old compiler.

L097/L098/L106 composition, actual occurrence/original-Q integration,
the general compiler ledger, short source proofs, M-only bounds,
universal W₂, arbitrary ER data and unrestricted SAT remain independent
gaps. No implementation is verified. This newly scoped ready continuation
is for the supervisor's separate approval next turn; this review neither
derives nor approves a new mathematical result.

Outcome: **EXPLORATION / LITERATURE / NOVELTY_UNCHECKED**. New source-scope
comparison makes a bounded specialization assessable, without a theorem,
mathematical advance or novelty claim. No lemma, mathematical script,
DAG or PROOF content changed.
