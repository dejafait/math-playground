# 027 — 2026-10-04 — First disjoint singular fourth-support family

Completed one mathematical attempt on the exact saved actual-pencil
COVERED_TARGET, reusing its prior SPECIALIZE assessment. Existing changes,
the complete overview, canonical DAG and source stops were preserved.
No additional browsing or essential-source access was needed.

[L018](../lemmas/L018-first-disjoint-singular-family-exclusion.md) excludes
sixteen bad parameters for the full-weight K={1,12,22,64} family of the
saved disjoint triple. Its [calculation](../drafts/2026-10-04-disjoint-singular-family-test.md)
and [exact certificate](../scripts/coefficient-feasibility/singular-family-result.json)
retain the generic kernel, exceptional rank, all actual weights and
coordinate-resultant elimination. Equality forces fourth parameter sixteen;
that pencil fails the singular-root criterion and has exactly four bad
parameters even over the algebraic closure. The
[branch stop](../ATTEMPTS/011-first-disjoint-singular-sixteen-count.md)
records why it cannot produce the desired witness.

Outcome: NEGATIVE; STEP_KIND: RESEARCH; STEP_CLASSIFICATION: POTENTIALLY_NEW.
The standard algebra is imported from the ready coverage; the new local
family obstruction is not established by the inspected source statements.
No certified originality, complete candidate or global improvement is
claimed. STATUS remains IN_PROGRESS and the interval is still 11/q–16/q
against fifteen. Consecutive uninformative mathematical turns used: zero.

The reason for the next direction is the three remaining singular systems,
which were outside both the isolated-root certificate and this calculation.
The second support {8,27,50,75} is selected within the same preapproved
actual-pencil scope; no calculation on it is performed here. Arbitrary
triples, all-prime configurations on other supports and July correspondence
remain unresolved. The only direct mathematical input to L018 is L010.

Validation: `python3 scripts/coefficient-feasibility/singular_family.py`
checks every symbolic kernel and weight identity, 125 independent minor
values, 495 independent Sylvester determinant values, all 455 triple gcds,
all fourth-root residuals, separate equality/field gates, the 560 lower-weight
supports and the original event on 2517 supports. The required checker
`python3 ../scripts/docs/check_structure.py --problem reed-solomon-mca`
passes with twenty nodes and fourteen edges; `git diff --check -- .` passes.
The next action exactly matches the prior ready COVERED_TARGET. Only the
active notebook is edited; no commit, reset or runner-state change is made.
