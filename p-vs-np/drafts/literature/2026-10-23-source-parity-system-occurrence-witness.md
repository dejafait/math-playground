# Source parity systems: proposed ordinary-Frege supplier comparison

TARGET: Assess a polynomial original-Q exact-fg witness for the canonical width-three CNF encoding of an arity-at-most-three F₂ equation system with a supplied row-combination contradiction, via ordinary Frege and L098.
CHECKED: 2026-10-23
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 414 searched linear-equation/parity/Gaussian-elimination Frege proofs, Tseitin ordinary-Frege upper bounds and finite-field equational proof simulations; checked the local parity records, L087/L098 receiving hypotheses, L012's ER-only statement and Attempts 009/018/030/031. Primary passages and access limits are recorded below; search absence establishes no novelty.
SOURCE_EVIDENCE: Inspected Buss–Impagliazzo–Krajicek–Pudlak–Razborov–Sgall author manuscript §2.2 p.9, including ring schemas, congruence rules, the named Reckhow all-bases/Frege correspondence and its symbol-size qualification; Cook–Reckhow (1979) Definitions 2.1–2.2, Theorem 2.3, Corollary 2.4 and Lemma 2.5 with the rule-replacement proof pp.39–40; Impagliazzo–Segerlind arXiv:cs/0308012v1 §6 pp.15–16, including Theorem 4 and its explicit-CNF/linear-certificate comparison. Reuse audited L098 and L097's step-380 repair.
COMPARISON: Known finite-field equational reasoning has an ordinary-Frege simulation; the general explicit-linear-system theorem inspected separately uses counting axioms, which must not be silently identified with ordinary Frege. Exact original-CNF reception, supplied-row use and the complete original-Q composition through L098 remain a specialization, not an imported full-statement match. L012 alone remains insufficient.
GAP: Construct and charge the exact assumption-free proof of ¬F in L098's presentation from the supplied row contradiction, using named proof-system simulations rather than literal expansion of a long XOR chain; then compose its full binary length/time with L098 in the original Q. No such construction or bound is established by this review.
REASON: Essential component coverage is now adequate for one separate mathematical specialization attempt. Import the named Frege simulation; do not reprove general Gaussian-elimination correctness or all-bases invariance. The original-CNF and full-bit interfaces justify SPECIALIZE rather than IMPORT.
SCOPE: Explicit F₂ equation matrix with at most three distinct source variables per row, explicit right sides and binary row coefficients λ whose row sum is 0=1; F is exactly its canonical clause encoding, with original clause positions and every occurrence retained. Q=2+M+|F|+|system|+|λ| is fixed before proofs or witnesses.
COVERED_TARGET: Construct a polynomial-full-bit ordinary-Frege proof of the exact negated canonical source CNF from a supplied arity-at-most-three F₂ row-combination contradiction, and apply L098 to obtain unchanged fg/B witnesses with polynomial full size/time in original Q=2+M+|F|+|system|+|λ|.

## Startup proposal preserved

The following proposal records the uncovered state at step 413. Its
REVIEW_REQUIRED conclusion is superseded by the completed review below;
its mathematical target and unresolved obligations are preserved.

Main gap: unrestricted SAT decision/separation. The intermediate target
is a polynomial ordinary-Frege source proof for this explicit algebraic
input class. Its plausible downstream use is an exact original-fg
witness through L098 without a small-backdoor assumption. This would
still be a restricted supplier, not general witness existence or a
complexity separation. No such proof is derived here.

Use one fixed canonical clause encoding per row: forbid each assignment
to that row's distinct variables that violates its parity equation.
Arity zero, repeated rows and empty/inconsistent equations must be
covered by the comparison; the resulting CNF has width at most three.
The system and λ are explicitly supplied and charged, and must be
checked against the actual original F rather than a newly selected
Boolean-equivalent encoding. The source variables are not new extension
variables. Preserve L087's actual occurrence names, original fg, B and
pre-witness M, including its appended gadget.

Essential prospective local inputs are L087 and audited L098, with
L097's repaired extraction received through L098. L012 is a narrowly
specified comparison for its parity-row proof presentation, not a
premise asserting ordinary-Frege simulation. Its detailed proof has
not been read for this proposal. Search the local parity source notes
and exact theorem scope before reading additional proof ranges. The
next review must distinguish ordinary Frege from EF/ER and from a
semantic polynomial-time parity solver. Reuse any adequate existing
primary assessment it finds; do not rebuild known parity proofs.

Continue only if inspected sources give the needed ordinary-Frege
mechanism with a fixed polynomial in the full supplied data, or isolate
a small explicit specialization with ready coverage. Park/narrow if
only extension-based proofs are covered, if exact CNF reception fails,
or if eliminating parity sharing is charged by an uncontrolled tree
unfolding. No implication about optimal proof hardness follows from a
failed construction. General short proofs, M-only bounds, universal W₂,
arbitrary ER data and unrestricted SAT remain unresolved. Full matching
Mathlib coverage is not checked.

This newly saved continuation needs a separate literature review next
turn. It is not an approval or a mathematical result of step 413.

## Completed source review — step 414, 2026-10-23

LITERATURE_REASON: The source hypothesis changes from a strong 2-CNF
backdoor to an explicit parity-row contradiction; ordinary-Frege source
coverage was missing at invocation. This review does not repeat L105's audit.

The main gap is unrestricted SAT decision/separation. The intermediate
target is the COVERED_TARGET above. Its downstream use is a restricted
source-proof supplier for L098 without assuming small incidence width,
backdoor size or a common order partition. No separation between these
promised classes, universal short-proof bound or new theorem is asserted.

### Primary inputs and qualifications

1. S. Buss, R. Impagliazzo, J. Krajíček, P. Pudlák, A. A. Razborov and
J. Sgall, *Proof Complexity in Algebraic Systems and Bounded Depth Frege
Systems with Modular Counting*, Computational Complexity 6 (1996/97),
256–298, [DOI](https://doi.org/10.1007/BF01294258).
Inspected the [37-page author manuscript](https://mathweb.ucsd.edu/~sbuss/ResearchWeb/nullstellensatz/token.pdf),
§2.2, printed p.9, including its footnote (revision date unestablished).
Equations are explicit ring terms with identity schemas and congruence
rules. The stated fixed-F_p equivalence with unrestricted Frege cites
Reckhow; the footnote specifies symbol-size accounting. Import this
ordinary-Frege bridge, while retaining the obligation to write and charge
the equational derivation. It supplies no circuit or PIT shortcut.

2. S. A. Cook and R. A. Reckhow, *The Relative Efficiency of Propositional
Proof Systems*, JSL 44(1) (1979), 36–50,
[primary scan](https://www.cs.toronto.edu/~sacook/homepage/cook_reckhow.pdf),
Definitions 2.1–2.2, Theorem 2.3, Corollary 2.4, Lemma 2.5 and proof,
pp.39–40. These cover finite sound implicationally complete systems in
one fixed adequate language. The proof replaces each rule by a fixed
derivation and substitutes its actual arguments. The following paragraph
attributes different-basis simulation to the standard named **Reckhow
basis-invariance theorem**, also stated in source 1; Theorem 2.3 alone
does not cover it. The original *On the Lengths of Proofs in the
Propositional Calculus*, Toronto thesis, usually cited 1976 (scan ©1975),
was [too large for retrieval](https://www.cs.toronto.edu/~sacook/homepage/reckhow_thesis.pdf).
Its proof was not read; this review uses the named theorem as stated in
the inspected primary papers, without a reproof or invented theorem number.

3. R. Impagliazzo and N. Segerlind, *Constant-Depth Frege Systems with
Counting Axioms Polynomially Simulate Nullstellensatz Refutations*,
[arXiv:cs/0308012v1, 5 August 2003](https://arxiv.org/pdf/cs/0308012v1),
§6, printed pp.15–16, Theorem 4 and preceding argument. For a fixed
prime q, an inconsistent m-by-n system of row width w has a refutation
of its explicit CNF encoding in constant-depth Frege with counting
axioms modulo q, polynomial in m,n,2^w. The argument identifies row
polynomials and a degree-one, O(mn)-size Nullstellensatz certificate.
This is a stronger bounded-depth comparison with extra axioms, not
itself the ordinary-Frege receiver needed here. The review does not
import an uninspected simulation removing those counting axioms.

The needed F₂ specialization of source 1 has no non-Boolean field
elements. It covers explicit terms and proof records, not arbitrary
semantic consequences of a SAT solver. The future attempt must still
give a paid symbolic derivation from the supplied λ, and the actual
original-CNF-to-row implications, before applying this bridge.

### Discovery, duplicates and access limits

Queries included `"linear equations" "Frege" "polynomial" parity proofs`,
`Tseitin tautologies polynomial size Frege proofs Gaussian elimination
Urquhart`, `"Frege" "Gaussian elimination" proofs polynomial size`,
`"polynomial calculus" "Frege" "simulated by"`, and
`Urquhart "Hard examples for resolution" pdf`. Terminology checked
included Res(⊕), counting axioms versus parity gates, finite-field
equational logic and ordinary versus extended Frege.

Urquhart, *Hard examples for resolution*, JACM 34(1) (1987), 209–219,
[DOI](https://doi.org/10.1145/7531.8928), §6 Lemma 6.1 p.218, appeared
with its indexed proof paragraph: graph clauses are converted to
biconditionals and repeated variables are cancelled using associativity
and commutativity, with an O(n⁴) stated bound. Both the publisher PDF
and the CiteSeer scan were inaccessible. This is a discovery lead and
graph-specific comparison, not a fully inspected general-row theorem
or a load-bearing import. No graph hypothesis or its exponent is
silently extended to arbitrary supplied systems. Search answers and
the Pitassi–Rossman–Servedio–Tan introduction corroborate the familiar
parity upper bound but are not used instead of the primary bridge above.
EF Gaussian-elimination correctness papers, Res(⊕)-to-R(lin) comparisons
and unrelated algebraic simulations are not imported.

Local searches found no ready assessment for this exact supplier.
L012's hypotheses and output explicitly permit fresh ER definitions;
its graph/charge result is not the needed ordinary proof. Read L087's
full input model and L098's source-proof hypotheses and import interface;
reuse its ready construction/audit assessments and step-384 audit.
L097's ground-constant repair remains essential through L098.
Attempt 009 rejects a proof-size-to-unrestricted-time inference; Attempts
030/031 reject universal representation/partition promises, not this
proof-dependent algebraic supplier. Attempt 018 rejects unchanged
approval repetition. These stops and the unfinished local work remain.
The existing official target/model audit is unchanged and reused; no
new interpretation of P versus NP is being selected.

### One subsequent mathematical attempt and its test

The covered attempt must check λ against the supplied system and compare
F against the exact row-forbidden-assignment CNF, preserving every actual
clause position, name, literal and connective tree. Only distinct variables
occur within each row; repeated rows and arbitrary row right sides are
allowed. Charge the entire system, λ and original F, even if some rows
are unused. Count occurring names rather than assuming a huge binary
variable identifier denotes an explicitly paid dense matrix dimension.
Do not request or prove a uniform correctness tautology for a general
Gaussian-elimination algorithm: the contradiction coefficients are supplied.

Receive the standard finite-field proof simulation by citation and give
only the needed applicability argument. Supply the original-CNF-to-row
interface and a fully written polynomial-size equational derivation,
then obtain an assumption-free ordinary-Frege proof whose conclusion
is exactly ¬F in L098's fixed presentation. Bounded-arity row encodings
need only finitely many local truth-functional forms, but their imports,
actual-tree projections, guard copies and assumption discharge must be
paid. A left-associated parity term must not be literally expanded as
if XOR duplicated neither argument; use the imported proof-system
translation or a separately justified balanced presentation. No inference
substitution or extension rule may survive in the received proof.

Handle arity-zero 0=1 by the actual empty clause, arity-zero 0=0 by its
empty conjunction, units, no occurring variables, empty selected lists,
unused rows, repeated rows, and all constant/right-side conventions.
Do not replace the source by a more convenient Boolean-equivalent CNF.
Apply audited L098 only after its exact source-proof hypotheses hold;
compose the proof-input enlargement with its fixed polynomial in the
unchanged original Q. Retain actual fg, B, M, provenance and the gadget.
This paragraph specifies obligations; it derives no new identity or bound.

Continue if the written ordinary proof and L098 composition have one
fixed polynomial full-bit and deterministic-time bound in original Q.
Record a negative or unfinished outcome if exact CNF reception fails,
the derivation needs fresh extension gates, or basis conversion, proof
discharge or reference copying is left uncontrolled. Such failure is
not a lower bound on all proofs or witnesses. General small source
proofs, M-only bounds, universal W₂, arbitrary ER data and unrestricted
SAT remain unresolved. Full matching Mathlib coverage is not checked.

Outcome: EXPLORATION / LITERATURE / NOVELTY_UNCHECKED. This completes
new component coverage and approves a separate specialization attempt;
it does not establish the proposed supplier, audit it, or claim progress
beyond the checked sources. No lemma, mathematical script, PROOF.md or
DAG.md was changed.
