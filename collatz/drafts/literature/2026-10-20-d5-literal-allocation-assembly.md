# Literal d=5 allocation assembly — source comparison

TARGET: Assemble audited L086, L087 and L088 to exclude the literal d=5 endpoint/domain/J/H subsystem over the full nonnegative integer tail-allocation simplex.
CHECKED: 2026-10-20
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the ready first-recipient, last-pair and fixed-root discovery assessments; searched histories 350–357, the d5 assessments and C0* canonical corollaries for an existing assembly; compared C082a and read Attempt 032. No inspected matching d5 full-simplex assembly was found; no novelty inference.
SOURCE_EVIDENCE: Read L086 hypotheses, conclusion, cap/first-recipient proof cases and complete critical audit; L087 in full; L088 hypotheses, endpoint/cap/margin proof cases and relevant complete audit cases; L055 pair table; C082a hypotheses and reduction/guard-transport proof. Reused precise primary coverage recorded below without new external retrieval.
COMPARISON: The three audited statements have the identical literal d5 table, budget, shifted endpoints and own-input conventions. L086 covers the full simplex's early-support obligation, L087 covers the closed last-pair interval 2<=t<=B, and L088 covers each fixed endpoint root at t=0,1 without guard or domain assumptions. C082a concerns d=1 and additionally uses all-order reduction; it is a precedent, not the requested d5 result.
GAP: No essential source gap remains for one local assembly applicability proof. The later research turn must write the complete integer-budget case split and match the retained strict row18 H guard to L088; this review establishes no assembly theorem.
REASON: SPECIALIZE permits RESEARCH/REPRODUCTION using the existing audited implications, with only their full-simplex applicability left to write; no new certificate, tuning, affine or analytic reproof is justified.
SCOPE: Only r=25,B=9250245,H_0=35,H_24=32670626 with all other L055 pairs unchanged, literal order, integer b_i>=0 summing to B, a_i=2+18b_i, every cyclic endpoint, s_i>=540/11, non-strict own-input J guards and strict own-input H guards.
LITERATURE_REASON: The saved assembly was REVIEW_REQUIRED and extends beyond the two fixed roots in the prior assessment; a separate comparison of the three canonical hypothesis sets is required before mathematics. Existing primary discovery coverage remains adequate.

## Gap, relevance and bounded target

Universal eventual descent remains the main gap. The exact TARGET is
one intermediate literal-order exclusion. It could supply an input to
a separately assessed cyclic-order reduction or actual-word application.
Those steps and the universal gap remain independent and unresolved.
This literature-only step neither proves the assembly nor develops a
complete Collatz candidate. Essential proposed inputs: L055,L086,L087,L088.
No cross-notebook input is used.

## Primary coverage reused

Reuse the ready assessments
`2026-10-19-d5-remaining-early-recipients.md`,
`2026-10-19-d5-literal-last-pair-cutoff.md`,
`2026-10-20-d5-literal-survivor-h-test.md` and their critical-audit
assessments. Their discovery searches include prescribed finite-word
composition, exponent redistribution, first-recipient comparisons and
own-input height bounds. This conjunction adds no new analytic mechanism,
so repeating those searches or reopening unchanged external sources
would not resolve a missing hypothesis.

The primary affine input is Halbeisen–Hungerbuehler, *Optimal bounds
for the length of rational Collatz cycles*, Acta Arithmetica 78 (1997),
227–239, DOI 10.4064/aa-78-3-227-239,
[section 2, equations (2)–(4), Lemma 2, pp. 228–229](https://www.math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf).
The reused inspections cover nonempty finite binary words, the numerator
recursion, length-one and appended-zero cases; appended one is printed
as analogous. Only formal real affine composition and its fixed-point
formula with nonzero denominator are imported upstream. The canonical
inputs already check their integer word parameters and positive Lambda;
no integer/parity-realization conclusion is imported.

Reuse positive-real analytic inputs [DLMF 4.5.1](https://dlmf.nist.gov/4.5.E1)
(real x>-1,x!=0), [4.6.4](https://dlmf.nist.gov/4.6.E4)
(Re(z)>=0,z!=0), and [4.2.19](https://dlmf.nist.gov/4.2.E19),
with the audited outward remainders and amplified errors. The ready
assessment records version 1.2.8; no new release claim is made here.
The assembly needs no fresh numerical bound or series derivation.
The primary Collatz statement and shortcut equivalence remain as
recorded by the ready MathPrize inspection; no prize-adjudication
claim is used. Full matching Mathlib coverage is unchecked, not absent.

The reused stronger-result comparisons distinguish the 1997 paper's
Lemma 4 (equal length/one count plus every-prefix domination) and
Lemma 5/Corollary 1 (minimum over rotations) from designated outgoing
input guards. The previously assessed Christoffel lead is likewise
not an input here. No new theorem-level claim about that preprint or
its unread references is made. The canonical implications, rather
than scalar extremum or integer-cycle thresholds, supply this scope.

## Hypothesis and boundary coverage for a later proof

| Obligation to match | Inspected canonical coverage | Restriction |
|---|---|---|
| Full-simplex early support | L086 hypotheses, conclusion and step-349 audit | Literal order; same endpoints/domain/J guards; arbitrary later tails |
| Remaining budget parameter | Original integer simplex plus L086 conclusion | Later proof must explicitly identify b_23 and b_24 and justify both bounds |
| Large last-pair parameters | L087 statement and step-353 applicability audit | Entire integer interval 2<=t<=B, including closing tail 2 |
| Two fixed endpoint roots | L088 statement and step-357 audit | Separately t=0,1; no domain/J/H premise needed for uniqueness and H failure |
| Contradictory guard | Proposed subsystem's strict own-input row18 H guard and L088 conclusion (2) | Same indexed row18 and same input; later proof must write the contradiction |

These are source comparisons and remaining proof obligations, not a
performed case split. No cyclic relabeling is needed or licensed: the
proposed target already fixes literal order. All 25 outgoing inputs and
closure must be retained unchanged. L088's endpoint uniqueness is part
of the audited input; do not assume survivor feasibility or import a
minimum/seed at row0. The H guard has strict sign, whereas J is non-strict.
Keep these signs when writing the later application.

## Duplicates and failures

C082a covers H_0=39,H_24=32670622 (d=1), all permutations and the
same guard types, using a full C077a reduction before its two root tests.
It is not a theorem for the present pair table. L084 covers d=1,...,4
through its sufficient tests; d=5 fails the actual row0 support-offset
test. Attempt 032 remains an exact stop for that full conjunction.
L086 instead has a separately audited first-recipient argument, L087
uses only independent C data and L088 only independently justified
endpoint and early H proof cases. The assembly must cite these completed
statements, never the unavailable full C077a or L083 theorem at d=5.

The scoped canonical-corollary search found no d5 assembly; histories
350–357 explicitly leave it separate. Both original d=0 rational
witnesses concern another table and remain valid. Recorded modular
cancellation failures and other allocation/order stops are unchanged.
No feasibility inference follows from any failed sufficient datum.

## One bounded continuation

Coverage is ready for exactly TARGET in a later RESEARCH/REPRODUCTION
turn after the supervisor's separate approval. Import L086,L087,L088
by their canonical statements, using L055 only for table identification.
Write a complete applicability proof, including the integer budget
bounds, both last-pair endpoints, closure and the own-input H sign.
No mathematical script or reproof of audited data is needed.

Continue only if every assumption matches on the same tuple throughout
and the full nonnegative integer simplex is exhausted. A missing boundary,
additional unproved premise or coordinate mismatch stops the assembly;
record it without tuning the table or inferring feasibility. No all-order,
actual-word, integrality, minimum, seed, parity, valuation or primitive-count
conclusion is covered. No lemmas, scripts, DAG or PROOF argument are
changed by this review. This is source readiness, not a mathematical
exclusion or progress beyond the inspected literature.
