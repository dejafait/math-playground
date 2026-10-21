# Proposed L093 critical-audit source scope

TARGET: Critically audit L093's unused-D_6 residual, including denominator clearing, reduction modulo Q, the seed condition Delta=0 and every zero-slope branch.
CHECKED: 2026-10-16
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 245 read full L093, targeted L089/L090/L092 statements and conventions, the step-230 derivation and history, ATTEMPTS/033–034 and the supporting diagnostic's scope; reused ready kernel/involution/quadratic assessments and searched exact cyclic D_6 and RS linear-residual terminology plus primary localization coverage.
SOURCE_EVIDENCE: Milne, Fields and Galois Theory v5.10 (September 2022), polynomial evaluation universal property and Sections 1.6–1.7, printed p. 10; Stacks Project Proposition 10.9.3, tag 00CP, statement and complete proof, retrieved October 16, 2026; reused Nguyen Section 2/Proposition 1 and Bobenko Lemma 2.21 through ready L090/L092 comparisons.
COMPARISON: Standard division and specialization cover the general machinery; no inspected source supplies L093's cyclic determinant expansion, exact remainder coefficients, Delta branches or particular nonidentity witness. Those remain local audit obligations, not grounds to reprove the general theorems.
GAP: Source scope is ready for a separate saved-proof audit; L093 remains unaudited and uniform cyclic rank, rank-27 existence and subgroup nonvanishing remain undecided.
REASON: The exact statement and essential source/artifact obligations have now been compared; no essential unread source remains. Approve only the bounded audit, without deriving a residual, checking its correctness this turn or restarting elimination.
SCOPE: Saved L093 only, in its exact fixed-field and fixed-H hypotheses, using audited L089/L090/L092; no new residual, enlarged symbolic computation, label sweep or rank sampling.
LITERATURE_REASON: The saved audit was REVIEW_REQUIRED; its quartic remainder, zero-slope branches and rational-function nonidentity scope needed comparison beyond the ready L092 quadratic assessment.

## Original proposal — step 244, historical

The main gap remains uniform rank R>=3/rank M=28 versus rank-27
existence. A trustworthy necessary residual would be a usable input to
later independently assessed rank work; its nonidentity on a larger
seed domain alone cannot settle the H-label problem.

The next invocation must first read full L093 to establish its exact
hypotheses and proof/certificate obligations. Reuse the saved source
comparisons of L089/L090/L092 where they apply. Inspect primary
polynomial division/resultant or elimination statements only to the
extent essential to the actual L093 argument; the name Delta alone
does not identify its theorem. Check duplicates and the short stopped
routes ATTEMPTS/033–034 before approving the bounded audit. The new
scope, especially the remainder and zero-slope cases, needs a distinct
comparison; no inference of novelty is licensed by the search here.

Essential proposed inputs: L093, audited L089/L090/L092, with the latter
inputs retaining L010/L087/L088 and L091's gate conventions as used.
Confirm direct uses against L093 and the canonical DAG. Assume neither
L094/L095, a nonzero residual slope for all seeds, an admissible H
specialization, sufficient gates, nor existence of a nonzero kernel.

The eventual audit should accept only if all cleared denominators are
justified, polynomial reduction is exact, the seed condition follows in
every branch, and any nonidentity witness has its stated limited scope.
If a claim fails, narrow that claim rather than extend the computation.
This is verification of saved mathematics, not reopening the stopped
joint-elimination mechanism. Full matching Mathlib coverage is not
checked. This proposal remains REVIEW_REQUIRED until a separate source
comparison records adequate coverage.

## Completed source comparison — step 245

This is one literature-only review of exactly TARGET. Full L093 was read
to identify hypotheses, cases and evidence obligations, not to verify its
algebra. No lemma, DAG, argument overview or mathematical script is changed;
no diagnostic was executed and no mathematical result is derived here.

### Relevance and precise scope

The main local gap is uniform rank R>=3/rank M=28 versus rank-27
existence for L087's cyclic family. The intermediate target is a
trustworthy necessary unused-D_6 residual. Downstream it could restrict
the admitted seed set for a separately assessed rank argument. It cannot
alone settle the subgroup feasibility question, arbitrary families,
triangle twelve or the challenge-definition qualifications. The
11/q–16/q interval remains unchanged.

L093 uses exactly F_(97^20), the order-sixteen H in F_97^*, arbitrary
bijective labeling, unshifted moment columns and L092's original seeds
{0,1,2,3,5,7,9}. Its symbols after normalization lie in T(H), not H.
Direct inputs remain L089/L090/L092, as in the canonical DAG; retain
L010/L087/L088 and L091 conventions through those audited inputs. The
relevant statements, normalization and completion rows were inspected.
L093's historical audit warnings about L090/L092 predate their completed
audits; they do not introduce a missing source. L093 itself is still
unaudited. No L094/L095 conclusion, actual errors, original chart,
weights, universal residual slope, sufficient gates or surviving kernel
is an assumption licensed here.

### Reuse, searches and newly inspected primary statements

Reuse `2026-10-14-cyclic-family-alternating-kernel.md`,
`2026-10-15-cyclic-six-label-critical-audit.md` and
`2026-10-15-cyclic-quadratic-reconstruction-critical-audit.md` in this
directory. Their exact fixed-H limitations and primary-source
qualifications remain. Nguyen's *Projective Line Revisited* (2021),
Section 2, pp. 188–189, and Proposition 1, p. 191, cover the involution
machinery in characteristic different from two; Bobenko's *Projective
Geometry* (December 12, 2019), Lemma 2.21, pp. 21–22, covers projective
invariance over any field. Their already inspected affine/infinity and
proof cases need no repeat retrieval. They do not verify the cyclic
coordinate formulas of L093.

Queries on October 16, 2026 were `"cyclic" "unused" "D_6" "Reed"`,
`"Reed-Solomon" "quadratic" "linear residual"`, and
`site.stacks.math.columbia.edu localization universal property ring
homomorphism S inverse units lemma`. The exact cyclic searches supplied
no inspected matching theorem. Unrelated search results were screening
only, not evidence of novelty. The local targeted search identified the
original step-230 derivation and certificate, not a completed separate
audit. Broader fixed-evaluation theorem comparisons are reused rather
than repeated.

J. S. Milne, [*Fields and Galois Theory*](https://www.jmilne.org/math/CourseNotes/FT.pdf),
v5.10, September 2022, printed p. 10: read the polynomial evaluation
universal property, Section 1.6's full division-algorithm statement
(nonzero divisor polynomial, unique quotient and remainder of smaller
degree), and Section 1.7's factor/root argument. These apply over any
field, including F_97, its extension and the rational seed function
field. They cover the general remainder operation without a separability
hypothesis. They do not establish L093's quartic degree, coefficients
or zero-slope conclusions. Section 1.6 states the standard theorem;
it does not give a full proof of division, and no such proof is needed
as an additional input to this specialization audit.

The [Stacks Project, Proposition 10.9.3, tag 00CP](https://stacks.math.columbia.edu/tag/00CP),
current online statement and complete existence/uniqueness proof read
October 16, 2026, gives the universal property of ring localization:
a ring map extends when the elements inverted map to units. Section
10.9's preceding definition and injectivity discussion were also read.
This covers evaluation of rational seed expressions on a domain where
their denominators are nonzero. The audit must identify that domain
and check the saved witness lies in it; the citation does not certify
the witness, or imply nonvanishing on transformed H seeds. Evaluation
is on the appropriate localization, not on the whole rational function
field at an arbitrary point. Later module-localization results are
unused.

No general resultant theorem is essential: L093 explicitly treats a
linear remainder and substitutes its root into Q, with the zero-slope
cases separate. The symbol Delta alone is not a citation to a stronger
elimination or sufficiency theorem. Direct local checking is justified
by the exact cyclic indices, denominator conventions and displayed
coefficients. Full matching Mathlib coverage remains not checked;
unknown coverage is not absence.

### Artifact obligations, duplicates and stopping evidence

Read `drafts/2026-10-15-cyclic-unused-d6-attempt.md` and history/230.
The canonical proof displays its complete short nonidentity certificate:
the seed assignment, all coefficient polynomials, quotient, remainder
and Delta value. The diagnostic source
`scripts/cyclic-shared-gates/d6_residual.py` was read only to identify
its obligations and limitations, without execution or modification.
It writes `scripts/cyclic-shared-gates/d6-residual-certificate.json`
and claims one-specialization long division and 97 scalar determinant
checks, with no H-assignments or rank tests. Those are claims for the
later audit, not verified evidence of correctness this turn. The
displayed coefficient identity can be checked independently; the
certificate is supporting rather than the sole load-bearing proof.
If the later audit relies on its recorded all-97 claim, it must inspect
all relevant rows or replay the complete bounded diagnostic, not a
preview. No large certificate needs to be loaded for this source review.

Audited L092 bounds continuations by two but does not check unused D_6.
L094 combines another residual, and L095 changes seeds; neither supplies
an independent proof of this saved original-seed statement or an input
to its audit. Their supplied overview is sufficient for this distinction;
their detailed proofs are unnecessary here. No cross-notebook input is
used. ATTEMPTS/033–034 were read in full: they preserve incomplete
expanded elimination and an unsuccessful direct joint-gate test. Neither
refutes L093 nor licenses restarting those routes. Preserve them and
ATTEMPTS/020; this independently testable audit performs no expansion,
new residual, label sweep or positive rank sampling.

### Bounded continuation and acceptance test

Continue with exactly TARGET in a separate REPRODUCTION proof audit.
Check D_1/D_10 and D_8/D_3/D_2 against the audited gate conventions;
justify ell and every seed denominator before clearing D_6. Retain the
affine D_3 case, N/O and Z/W homogeneous pairs, their simultaneous-zero
exclusions, O=0 and W=0 poles and all T(H)/collision gates. Verify the
cleared determinant and degree bound exactly, then the complete remainder
formulas modulo the genuine Q, including u=0, repeated roots and degree
drops of E. Check Delta necessity in every slope branch and use only
L092's uniqueness for the nonzero-slope bound; do not infer sufficiency.
Check the entire displayed nonidentity identity and all denominators at
its one specialization, keeping its scope on rational seed space rather
than the admitted finite seed set.

Accept only the saved necessary restriction if every case holds; a
failed identity, denominator or branch claim narrows or rejects that
claim and ends this bounded audit. Passing does not provide a global
rank answer or reopen elimination. This SPECIALIZE assessment approves
the next audit's source scope, not its correctness. Outcome EXPLORATION
records new comparison and a concrete ready test, with zero mathematical
exploration turns spent and no claimed progress beyond checked sources.
