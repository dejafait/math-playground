# Proposed critical audit of the frozen finite model

TARGET: Critically audit C919i's frozen five-node all-shift H2 proof and exact r=158 cubic witness, including conjugate multiplicities, the uniform head/error extension and Fraction arithmetic certificate.
CHECKED: 2026-11-21
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step2205 reused the unchanged step2203 bounded theorem/duplicate assessment, searched the exact local C919i/C919e and 2202/2204 stop records, and retrieved primary Python rational/integer documentation for the newly explicit certificate-audit contract. No new global discovery search or novelty claim.
SOURCE_EVIDENCE: Reuse inspected Gautschi1975 Section3(3.1)-(3.4), p339, and Boyd-Vandenberghe2004/2009 A.1.1/A.1.5/A.5.2/A.5.4 and Section2.2.5 from step2203; reopened Nathanson1911.01745v2 Lemmas1-2/Theorem1 and conjugate-pair proof pp2-3; newly read Python3.15.2 fractions Fraction constructor/operations/numerator/denominator and Built-in Types Numeric Types. C919e is the sole local theorem input.
COMPARISON: Published finite-matrix methods cover the ingredients, and Hermite-Sylvester gives unrestricted detection, but neither provides this frozen all-shift sign and prescribed r=158 witness. A bounded independent audit is a known-method specialization, not an import of the two signs or a theorem reproof; a finite shift sample and an unrestricted interpolation witness cannot replace the stated obligations.
GAP: Source coverage is adequate for the exact saved audit. Independent review of the uniform inequality and complete rational-complex certificate remains undone; correct CPython integer/Fraction execution remains an explicit assumption. Actual-Xi realization, shift removal and all-degree positivity remain open; full matching Mathlib coverage is unchecked.
REASON: Complete the separate literature-only approval required by step2204, retaining the exact target and reusing ready matrix coverage. Permit one later conceptual audit classified REPRODUCTION; no sign assertion is accepted in this source review.
SCOPE: Exactly TARGET for one independent conceptual audit, including all five occurrences once, both conjugates, algebraic squares, index shift two, every integer r>=4, the prescribed cubic and r=158 certificate. No tuning, witness search restart, Xi-source import or CPython implementation verification.
LITERATURE_REASON: The saved audit was REVIEW_REQUIRED; ready2203 covered the calculation rather than an independent complete-certificate audit. This step supplies that approval and newly inspects the essential exact-arithmetic documentation without repeating matrix discovery.

Read the canonical C919i proof, C919e only where needed, and
`scripts/h2-head/five_node_2204.py` plus the load-bearing certificate
fields. Check all five opposite classes, both conjugates, index shift2,
real congruence, norm direction, every-integer extension, prescribed
monic cubic, r=158 and exact negative value under correct CPython/Fraction
arithmetic. Full matching Mathlib coverage remains unchecked. Do not
import C919h's actual-Xi sources or arithmetic contracts. No source
blocker or cross-notebook input is asserted. Do not tune the model or
restart its witness search as a new research mechanism.

At nomination2204 this scope was REVIEW_REQUIRED and did not approve its
own calculation. The separate source review2205 below now makes this
same target ready; the mathematical audit remains future work.

## Separate source review2205, 21 November 2026

The main gap is L030-L032/C032a actual-Xi all-degree algebraic mixed
positivity. The intermediate target is independent verification of
C919i's frozen finite countermodel. If accepted, its downstream use is
to reject a generic implication from the restricted all-shift H2 family
to all-degree positivity. It supplies no actual-Xi realization or
independent higher-degree estimate. Continue to one bounded audit if
finite-method and arithmetic coverage is adequate; otherwise retain
the gate for the precise missing source. During the later audit, accept
only after all uniform-bound and prescribed-witness obligations pass;
correct a defect or withdraw its affected conclusion, without tuning.

### Reuse and theorem comparison

The ready assessment
`drafts/literature/2026-11-21-head-annihilator-five-node-gate-2202.md`
records the inspected sources, queries and duplicate comparisons from
step2203. Its node set, moment convention and finite-matrix methods
are unchanged. Gautschi, *Norm Estimates for Inverses of Vandermonde
Matrices*, Numerische Mathematik23 (1975), 337-347, Section3(3.1)-(3.4),
p339, supplies the distinct-node inverse formula:
https://www.cs.purdue.edu/homes/wxg/selected_works/section_01/051.pdf .
Boyd and Vandenberghe, *Convex Optimization*, CUP2004, corrected seventh
printing2009, A.1.1 pp633-634, A.1.5 p636, A.5.2 pp646-647,
A.5.4 pp648-649 and Section2.2.5 pp34-35 supply finite real norm,
order and congruence facts:
https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf .
These passages were inspected in the prior assessment and are reused,
not claimed newly retrieved here. C919e's canonical proof and its
accepted2164 audit were read for scope: its three closed real boxes
and weighted real Gram inequality are conditional inputs. They do not
give the complex error estimate, all-shift extension or witness sign.
Reproving that accepted inverse calculation is unnecessary.

Reopened Melvyn B. Nathanson, *The Hermite-Sylvester criterion for
real-rooted polynomials*, arXiv:1911.01745v2, 24 November2019,
Lemmas1-2/Theorem1 and complete relevant proof, printed pp2-3:
https://arxiv.org/pdf/1911.01745v2 . Its theorem concerns a nonconstant
real degree-n polynomial and its full n-by-n unweighted power-sum
form. The proof uses conjugation-closed distinct roots for interpolation,
then restores root multiplicities; the selected conjugate roots have
equal multiplicity and contribute algebraic squares. This confirms the
comparison convention. It neither gives the weighted fixed-size shifted
claim nor prescribes the cubic-times-monomial witness. Do not import
its full-form conclusion as acceptance of either C919i assertion.
The earlier Berg-Szwarc all-degree and Arellano-Pena finite-prefix
comparisons are retained as recorded scope comparisons, not new inputs
or freshly read sources. No new essential source was identified there.

### Exact arithmetic contract: new primary evidence

The local `python3 --version` reports Python3.15.2. Read the matching
versioned primary manual, *fractions — Rational numbers*, sections
Fraction constructor, Rational operations, numerator and denominator:
https://docs.python.org/3.15/library/fractions.html . It specifies
rational arithmetic, exact integer numerator/denominator construction,
Rational operations and reduced numerator with positive denominator.
Its float-construction warning matters to an audit: decimal-looking
float input must not silently replace rational operands. The script
was read to identify its declared pair-of-Fraction representation,
integer-power helpers, serialization and finite certificate scope;
their correctness has not been independently audited in this step.

Also read Python3.15.2 *Built-in Types*, Numeric Types section:
https://docs.python.org/3.15/builtins/stdtypes.html#numeric-types-int-float-complex .
It specifies unlimited-precision integers and floating components for
built-in complex values. Thus the declared rational-pair approach has
an appropriate documented arithmetic interface; the manual does not
verify this execution, helper implementation or saved certificate.
The initially retrieved Python3.14 pages are superseded for this review
by the matching3.15 pages; no version mismatch is used as evidence.
No CPython implementation correctness theorem is asserted. The explicit
correct-execution assumption remains, and formal Lean verification is
not supplied. Full matching Mathlib coverage is unchecked.

### Duplicates, stops and exact audit obligations

The narrow local comparison used C919i, C919e, the2203 assessment,
`ATTEMPTS/2026-11-21-generic-all-shift-h2-completion-stop-2204.md`,
`ATTEMPTS/2026-11-21-shifted-h2-review-loop-closed-2202.md`, and the
2203/2204 history entries. C919i is the result to audit, not a second
result to reproduce as a discovery. The2204 stop is pending this audit;
the2202 stop closes repetitive review of the actual-Xi restricted-family
assembly. Neither prevents a first independent audit of this distinct
frozen countermodel. No cross-notebook result is read or imported.
The initial scoped git status produced excessive existing-change output;
it was not used to inspect unrelated proofs, and all work is preserved.

The later audit must check the five opposite-class and multiplicity
conventions, both complex occurrences, real coefficients, algebraic
squares and index shift two. It must check C919e's exact applicability,
real invertible congruence and norm direction, all onset/error operands,
strict margin and geometric extension to every integer r>=4. The
written argument, rather than a finite sample, must supply uniformity.
It must independently reconstruct the prescribed cubic, its real-node
zeros, all five weighted witness terms at r=158, the full exact Q and
positive normalization, and the strict rational sign comparison.
Inspect the complete load-bearing certificate fields via the scoped
JSON inspector, not previews or PASS flags. Correct Fraction use,
nonzero denominators, helper semantics and all failures must be checked.
The normalization field and the inequality in the proof must be compared
by their actual multiply/divide definitions, rather than their labels.
Do not rerun parameter or witness searches as a new mechanism.

This source-only approval establishes no new inequality, calculates no
certificate value and accepts neither model sign. No lemma, mathematical
script, DAG or PROOF change is warranted. Outcome EXPLORATION reflects
new arithmetic source coverage and completed scope comparison, not a
mathematical advance or informative negative. The next action stays
exactly TARGET with SPECIALIZE coverage. After that audit, a new central
mechanism would need a noncircular actual-theta estimate surviving head
cancellation; none is justified merely by this finite-model review.
