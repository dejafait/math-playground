# Parity source-proof compiler: implementation coverage

TARGET: Implement and independently check L106's exact-¬F ordinary-Frege source-proof compiler on the three-row parity contradiction and inconsistent zero-row cases.
CHECKED: 2026-10-23
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 418 compared L106 §§1–4 and its existing audit, L097's exact source basis/constants, L056's hypotheses/library, and scripts/balanced-slot/compiler.py and checker.py; targeted script-path and source-assessment searches found the slot component, not a matching parity-source compiler. Reused parity and primitive-library discovery assessments; inspected Attempts 018/030/032 for repeated approval, representation and copying failures. No novelty inference is made.
SOURCE_EVIDENCE: Reopened LTW's 40-page author manuscript, printed p.2, confirming all three Schoenfield schemes and MP; reused Cook–Reckhow Definitions 2.1–2.2, Theorem 2.3, Corollary 2.4, Lemma 2.5 pp.39–40 and the named Reckhow basis-invariance input already inspected in the parity assessment; reused L056's inspected Metamath ax-1/2/3/ax-mp and fixed-library completeness coverage.
COMPARISON: Known fixed-rule replacement and propositional completeness cover finite template proofs; audited L106 covers the all-size source construction. L056 supplies useful native synthesis/checking machinery but its translated ax-3 is not Schoenfield's second scheme, its falsehood is a formula with q, and its checker has no ground-constant rules. Its literal images alone do not meet L097's exact source interface.
GAP: Implement the already justified construction, including concrete fixed proofs in the required source basis, constant reception, guarded records, reference relocation and an independent exact-basis checker; no emitted source stream or measured source-compiler bound is yet verified.
REASON: Essential theorem coverage is ready; executable primitive reception remains a necessary specialization rather than a theorem import or a new mathematical mechanism. This review approves one separate bounded implementation attempt, not its success.
SCOPE: L106's exact source π interface on the stated fixtures with its original-Q ledger; no downstream H construction, general SAT procedure, new proof-system theorem or unrestricted proof search.

## Exact interface comparison

The primary source is Fu Li, Iddo Tzameret and Zhengyu Wang,
*Characterizing Propositional Proofs as Non-Commutative Formulas*,
SIAM J. Comput. 47(4) (2018), 1424–1462,
[DOI](https://doi.org/10.1137/16M1107632). Reopened the
[40-page author manuscript](https://www.doc.ic.ac.uk/~itzamere/Ideal_non-commutative.pdf)
on 2026-10-23, printed p.2 (PDF page index 1), complete displayed basis
and MP paragraph. Revision date remains unestablished. Its schemes are

    A → (B → A)
    (¬A → ¬B) → ((¬A → B) → A)
    (A → (B → C)) → ((A → B) → (A → C)),

with A→B literally abbreviated ¬A∨B and MP from A and A→B to B.
L097 additionally specifies the ground axioms true and ¬false.
The primary paper's basis paragraph does not itself specify those ground
axioms; their precise local reception is L097's step-380 repair, reused
by audited L098 and L106. AND uses ¬(¬A∨¬B), not a new primitive rule.

By contrast L056's native ax-3 is (¬A→¬B)→(B→A).
The other two native schemes agree up to ordering with the first and
third source schemes. `checker.py`'s `pattern` accepts exactly its own
three schemes. Its image MP checks literal ¬A∨B, but its image ax-3
remains the translation of the different native ax-3. Neither semantic
validity nor an image-mode acceptance establishes a proof in the source
basis. This is a code/interface observation, not a new separation result.

`compiler.py` uses Z=¬(q→q), native X/E expansions, and only ax1/2/3/MP
in serialized streams. The checker treats every unparenthesized token as
a variable; strings named true or false have no constant status. There
is no true/¬false axiom branch. Renaming these tokens would not implement
L097's ground axioms. The emitter's `write` retains only root-reachable
records; that export policy alone does not retain all generated unused
row/template records demanded by L106's chosen archive ledger.
These differences must be addressed explicitly, preserving L056's files
and qualifications. Its complete archives were not rerun or independently
audited in this source-only turn.

## Reused theorem coverage and permissible implementation

Reuse the ready assessment
`drafts/literature/2026-10-23-source-parity-system-occurrence-witness.md`
and L106 §1 for the finite-field/Frege correspondence and named Reckhow
basis-invariance theorem. For fixed-rule replacement the precise input is
Cook–Reckhow, *The Relative Efficiency of Propositional Proof Systems*,
JSL 44(1) (1979), 36–50, Definitions 2.1–2.2, Theorem 2.3, Corollary 2.4,
Lemma 2.5 and proof pp.39–40,
[primary scan](https://www.cs.toronto.edu/~sacook/homepage/cook_reckhow.pdf).
These passages were inspected in the reused assessment; not reopened
here. Theorem 2.3 alone is not the different-basis theorem.

Reuse `drafts/literature/2026-10-11-balanced-slot-frege-proof-string-test.md`
for the named Church P2/Lukasiewicz completeness input and primitive
[ax-1](https://us.metamath.org/mpeuni/ax-1.html),
[ax-2](https://us.metamath.org/mpeuni/ax-2.html),
[ax-3](https://us.metamath.org/mpeuni/ax-3.html),
[ax-mp](https://us.metamath.org/mpeuni/ax-mp.html).
Those live-page statements and proof-library qualifications were inspected
in that assessment; this turn does not claim a pinned set.mm revision.
No further browsing of general parity or Gaussian elimination is needed.

The next implementation may construct a finite library directly in the
required Schoenfield basis, or materialize fixed rule-replacement proofs
for a reused native library. In either case every final axiom must match
the source schemes or one of the two ground axioms, with only MP as an
inference. Any connective normalization must have paid proof records
restoring the exact requested source endpoint. L056's strings are leads
and reusable proof components, not automatic source-basis certificates.
Completeness justifies finite fixed templates; it supplies neither an
unpaid checker rule nor a polynomial proof of an arbitrary growing
truth-table tautology. Any synthesis must be limited to the fixed library.
The next step is implementation/reproduction of these known mechanisms;
no general simulation theorem needs reproof.

## Bounded target, duplicates and stopping test

Main gap: unrestricted SAT decision/separation remains wholly open here.
Intermediate target: complete source π streams for rows x+y=0, y+z=0,
x+z=1 with λ=(1,1,1), and the inconsistent zero row 0=1 with λ=(1).
Use the exact forbidden-assignment clauses in row/assignment order,
explicit actual clause/global trees and genuine constants. Include a
nontrivial global conjunction tree in the parity fixture. The zero-row
case must retain its exact F=false endpoint. Future downstream use is
reception by audited L098 for L087's unchanged fg/B; this step does not
implement H or claim a formula-length-only witness bound.

L106 is the existing all-size construction, not a duplicate theorem to
recreate. The scoped path search `rg --files scripts` filtered for parity,
source-frege, source-proof and balanced-slot top-level Python files found
only the latter component; this is limited discovery, not an exhaustive
claim that no other code exists. Exact basis searches in source-Frege
assessments and ATTEMPTS found no matching source checker. Attempt 018's
approval-only loop is avoided by the concrete basis/constants/export
comparison above and a ready implementation continuation. Attempts 030
and 032 concern different universal suppliers/copying procedures; they
do not prohibit this finite ordinary-source compiler. No renaming rule,
ancestry unfolding or affine-ABP seed export is needed.

Continue only on complete primitive streams independently parsed from
disk, with exact externally reconstructed ¬F endpoints and no assumptions,
semantic rewrite rules, aliases or inference substitution. Check the fixed
library as well as the full fixture streams. Require deliberate altered
axiom occurrences, forward/out-of-range references, wrong MP premises,
constant misuse and endpoint changes to reject. Retain all supplied input
and intended unused row/template records; relocate references globally.
Inspect complete load-bearing evidence, not certificate previews.

Record full uncompressed bytes/bits, substitution occurrences, names,
references, record counts and actual trees, against the explicit compiler
ledger and L106's |π|,time ≤ cQ^12 source requirement. Constants in a
measured bound must be stated and justified, not fitted to successful
fixtures. A finite test cannot verify the all-size polynomial theorem.
Q=2+M+|F|+|system|+|λ| is fixed before output; the fixture must charge its
actual L087 pair/provenance or explicitly leave that original-Q integration
unverified. A source-only size parameter must not be mislabeled as the
full downstream input. Do not generate H to test this interface.

On failure preserve the complete failed stream/certificate and identify
the precise compiler limitation. Stop that implementation path if its
success requires changing the source endpoint, accepting extra primitive
rules or uncharged formula expansion. Failure supplies no optimal-proof,
witness or SAT lower bound. No essential source blocker remains; if
implementation exposes a changed mathematical hypothesis, record it for
a separate review rather than approving it during research.

Essential inputs are L106, L097/L098, and qualified L056; L087 supplies
only the eventual original-pair/provenance interface. General short source
proof availability, M-only bounds, universal W₂, arbitrary ER data and
unrestricted SAT remain unresolved. Mathlib full matching coverage is
not checked; Metamath coverage is not a Mathlib result.

Step 418 is LITERATURE / literature_comparison / NOVELTY_UNCHECKED,
outcome EXPLORATION. The new interface review approves the unchanged
TARGET with SPECIALIZE. No lemma, mathematical script, primitive proof,
new theorem or verified implementation was produced. Mathematical
exploration usage remains zero; this literature turn spends no calculation
exploration budget. The next turn defaults to RESEARCH / implementation /
REPRODUCTION under this saved assessment.
