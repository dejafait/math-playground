# 024 — 2026-10-04 — Three-support constrained actual-pencil test

Completed one mathematical attempt on the saved actual-pencil COVERED_TARGET,
reusing the prior SPECIALIZE assessment. Shared and local instructions,
the whole overview, DAG, ready coverage and existing changes were read and
preserved. No browsing or shared-infrastructure edits were needed.

The [calculation](../drafts/2026-10-04-three-support-constrained-test.md)
solves six four-dimensional triple-weight systems, then tests all 10902
fourth-support matrices. Its [script](../scripts/coefficient-feasibility/three_support.py)
checks determinant coefficients independently by elimination, solves
one-dimensional F_97 root kernels with all prescribed weights nonzero,
and deduplicates 3570 actual projective moment lines. Every retained pencil
passes the nonpersistent checks and receives the complete power/equality
audit and exact F_(97^20) four-error splitting test.

[The results](../scripts/coefficient-feasibility/three-support-result.json)
contain no fourth-power equality. Of 3530 pencils whose total count is
determined, 3483 have four bad parameters, 29 have five and 18 have seven.
Forty retain unresolved lower-weight roots. The best exact seven-count
pencil is independently checked by actual minor recomputation, affine
recurrences and original-event interpolation on all 2517 supports. Its
seven parameters are already in F_97. This is weaker than C013a's eleven.

The test leaves 5083 identically zero determinants, one larger rational
kernel and 1232 nonprime target-field determinant-root occurrences unsearched.
A shared-coordinate polynomial zero-syndrome kernel explains all 1817
zero determinants of the first triple, while failing the full-weight gate.
The [generator stop](../ATTEMPTS/008-one-dimensional-three-support-generator.md)
preserves that evidence without claiming a class exclusion.

Outcome: EXPLORATION; STEP_KIND: RESEARCH; STEP_CLASSIFICATION: REPRODUCTION.
The result implements covered local moment/MDS and standard algebra tools;
no progress beyond the checked literature or originality is asserted.
No new lemma or genuine dependency was introduced, so DAG.md and the
unchanged mathematical overview remain intact. STATUS stays IN_PROGRESS;
the main gap is still 11/q–16/q against fifteen, with July correspondence
parked and no complete candidate.

The next direction keeps the exact preapproved target and takes the saved
common-coordinate triple: remove its compulsory zero-syndrome kernel and
test smaller-minor/full-weight fourth-support conditions before the equality
gates. It addresses an identified blind branch instead of repeating the
one-dimensional prime-field enumeration. No next calculation is made here.
Consecutive uninformative mathematical turns used: one; total resultant
mathematical attempts: four. Existing orbit, two-block, five-coordinate and
July/four-block stops, source exhaustion and old STALLED reviews are retained.

Validation: `python3 scripts/coefficient-feasibility/three_support.py` passes
the finite candidate and independent best-pencil checks. The separate
`shared_coordinate_control()` invocation passes the polynomial triple-kernel
and zero-syndrome identities added to the reproducible script and saved result.
The required documentation checker with `--problem reed-solomon-mca` passes
with seventeen nodes and eleven edges. Current metadata exactly matches the
preexisting ready COVERED_TARGET and retains one EXPLORATION outcome and one
Next action; `git diff --check -- .` passes. No scheduler, launcher, retry
state or other notebook was edited.
