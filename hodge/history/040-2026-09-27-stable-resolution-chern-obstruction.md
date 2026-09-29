# 2026-09-27 — Stable-resolution Chern obstruction

STEP_ID: 2026-09-27-hodge-040-stable-resolution-chern-obstruction.
Outcome: NEGATIVE. Kind: RESEARCH. Classification: REPRODUCTION.

Read the shared/local instructions, checkpoint, whole overview and DAG;
inspected the existing changes and preserved unfinished work. Reused
the prior SPECIALIZE [assessment](../drafts/literature/2026-09-27-compatible-cubic-rm-stable-bundle.md)
for its exact saved bundle target. Reopened the cited Mistretta
Theorem 3.1 and Verbitsky Proposition 1.2/Theorem 2.5 to confirm
presentation length and the invariant-class framework. No changed
assessment was used to admit research in this turn.

The selected intermediate test now has a uniform negative answer:
[L026](../lemmas/L026-stable-resolutions-fail-common-metric-chern-test.md)
excludes invariant first two Chern classes for every terminal
single-polarization resolution bundle and every line-bundle twist.
Its normalized divisor action has rational eigenvalues, while the
common metric would require the irrational cubic eigenvalue. The
proof retains both exceptional components over infinity and the
full mixed tensor, and imposes no unjustified freedom on the actual
resolution choices. The known framework is imported; the scoped
application is REPRODUCTION, with no originality claim.

The terminal resolution has three presentation terms, so L012's
second-syzygy theorem is not applied verbatim to it. L012 remains
relevant evidence for the construction cases it actually covers.
Reviewed the new DAG row against the proof's use of the correspondence
action, finite-cover geometry and divisor basis. References to L012
are comparisons; the proof works for every Kahler class in N_R
without using L025's construction. No previous branch or proof was removed.

This stops the recipe before metric-specific stability work. It
does not settle existence of arbitrary compatible stable bundles.
The 21-dimensional cycle span and three attained RM directions
against four required are unchanged. No transverse surface or
complete informal candidate is obtained; STATUS remains IN_PROGRESS.

Saved the reasoning before finalizing it, then completed the
[calculation record](../drafts/2026-09-27-stable-resolution-chern-test.md)
and [attempt record](../ATTEMPTS/017-single-polarization-stable-resolution.md).
The discriminating test finishes after one source-review turn and
one research turn; this informative negative result resets the
exploration count to zero. Resolutions with different divisor-class
summands change the constraint causing this failure, but have not
been screened. The [pending assessment](../drafts/literature/2026-09-27-multiple-divisor-stable-resolutions.md)
requires a separate literature turn and comparison with the old
recovery obstructions. No calculation for that target was made.

Validation: the exact algebra certificate passed for the universal
twist identity, rank-one characteristic polynomial, alternating
K-class signs and cubic rational-root test. It checks no geometric
or stability assertion. The required command
`PYTHONDONTWRITEBYTECODE=1 python3 ../scripts/docs/check_structure.py --problem hodge`
passed with 27 nodes and 68 edges. Report and assessment fields,
the exact pending-target binding, compact overview and checkpoint,
and `git diff --check -- .` passed. Entry hashes show only the
three intended checkpoint/overview/DAG changes and six new local
artifacts, with no deletion or edit to a prior lemma, script or
assessment. These checks validate the recorded structure and
algebra; correctness of the informal geometric proof is separate.
