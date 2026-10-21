# Two-postspell local-minimum cutoff — completed scope review

TARGET: Determine the exact local-minimum count of an actual closed two-postspell word and apply Hercher's Theorem 23 to obtain a necessary lower bound on J_1+J_2, retaining repeated periods.
CHECKED: 2026-10-07
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the targeted discovery in 2026-10-06-two-postspell-cycle-exclusion.md; searched its cycle/period passages, history 057/058 and L031 for counting duplicates, then checked the two primary PDFs for the specific nonminimal-period condition. No fresh broad discovery or novelty claim.
SOURCE_EVIDENCE: Hercher, JIS 26 (2023), Article 23.3.5, Definitions 1/4/5/6, printed pp. 2–4, and Theorem 23 with full proof, pp. 15–16; Simons–de Weger v1.44 (2010-08-31), section 1.2, printed p. 2, including the full period/extrema definitions. Prior essential cycle proof coverage is reused.
COMPARISON: Published cycle restrictions cover positive shortcut cycles and local extrema, including nonminimal representations in the predecessor source; the remaining difference is the exact cyclic run count for the specified two-word syntax, not a new general cycle theorem.
GAP: The exact count and resulting J_1+J_2 bound still require a mathematical attempt, checking both cyclic junctions, nontriviality, and repeated versus primitive periods. No all-parameter cycle exclusion is supplied.
REASON: Approve one bounded counting specialization and cited theorem application; no reproof of the general cutoff, computational replication, parameter-table enlargement or claim of novelty is needed.
SCOPE: Actual positive closed W_1 W_2 with W_i=(OOEO)^(J_i) O^(H_i) E^(a_i), J_i>=2, H_i>=3, a_i>=0 congruent to 2 modulo 18, positive odd residue-20 junctions and starting n>1; no distinct-junction, primitive-period, first-return or least-root assumption.
LITERATURE_REASON: Changed target from closure boundary guards to a local-minimum counting specialization; the essential unresolved source condition was nonminimal-period scope.

## Primary source evidence

[Hercher](https://cs.uwaterloo.ca/journals/JIS/VOL26/Hercher/hercher5.pdf),
*There are no Collatz m-Cycles with m <= 91*, JIS 26 (2023),
Article 23.3.5, uses the shortcut map (Definition 1). Definitions 5/6
count cyclic minima through exact consecutive odd/even runs;
the chosen first minimum need not be the global minimum.
Theorem 23 excludes nontrivial cycles with at most 91 minima.
Its full proof uses the verification height 695*2^60, iterated
continued-fraction bounds and the cited upper bound on odd steps.
These published numerical inputs are imported, not independently
certified here. No primitive-period clause appears in these definitions.

[Simons–de Weger](https://deweger.net/papers/%5B35a%5DSidW-3n%2B1-v1.44%5B2010%5D.pdf),
*Theoretical and computational bounds for m-cycles of the 3n+1 problem*,
v1.44, 31 August 2010, section 1.2, printed p. 2, explicitly permits a
nonminimal return period p. Extrema are indexed by their occurrences
within that period. The repeated 1,2 cycle is explicitly trivial.
This supports retaining repetitions rather than silently requiring
first return or distinct junctions. The older cutoff is not substituted
for Hercher's stronger published theorem.

On 2026-10-07 the browser read Hercher's definition and full Theorem 23
proof passages and Simons–de Weger's complete section 1.2. Searches
for “period”, “primitive” and “multiple” in the latter PDF located the
period convention; absent string matches were not evidence of a theorem.
Other essential proof cases and source discovery remain as recorded in
[the prior assessment](2026-10-06-two-postspell-cycle-exclusion.md).
The newer conditional 95-minimum lead remains parked and nonessential.
Full matching and supporting Mathlib coverage: **not checked**.

## Approved mathematical difference and limits

The main gap is universal eventual descent. The intermediate target is
the exact local-minimum count of this actual closed language followed by
one application of the published cutoff. Its plausible use is to remove
a bounded region of the unresolved cycle parameters. Closure divisibility,
unbounded parameters, other cycles, divergent orbits and universal entry
remain independent unresolved questions.

Use L020/L021 only for actual-word and concatenation conventions.
Begin with an actual positive closed word, without assuming L031's
unresolved divisibility has a solution. The mathematical attempt must
establish the exact cyclic transitions, handle terminal E runs and the
initial O across closure, and distinguish occurrence counts from distinct
values. It must verify the nontrivial-cycle hypothesis. If using a
primitive-period reduction for safety, explicitly justify how occurrence
counts compare; do not divide by an assumed repeat factor or assert the
two junctions are different. No exact count, repeat factor or parameter
bound is derived in this literature turn.

Continue if a rigorous count and valid theorem application supply a
necessary restriction; abandon this application if a required parity,
nontriviality or period condition fails, recording that precise failure.
This approval covers only this bounded specialization. It does not
approve a larger finite screen or a new cycle-exclusion mechanism.

## Duplicates and preserved failures

The prior cycle assessment identifies the internal even-to-odd
transitions but supplies no exact two-word count or parameter restriction.
Targeted checks of L031 and histories 057/058 found no completed matching
result. This is local source reuse, not evidence of mathematical novelty.

History 058 and Attempt 019 preserve the failure of adding boundary
guards: L031 shows those guards automatic under positive integer closure.
The present test uses a published external restriction instead. Attempts
016/020 and the completed L033 audit are independent and remain preserved.
No exhausted clock or digit mechanism is being renamed or reopened.

SPECIALIZE is ready for the exact TARGET above. The next turn may derive
only the stated counting difference and necessary restriction, citing
the cutoff precisely and recording a full canonical proof if successful.
