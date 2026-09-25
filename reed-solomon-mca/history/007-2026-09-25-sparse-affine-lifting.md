# 007 — 2026-09-25 — Sharp errors from sparse affine lifting

Completed one continuation of the two-coordinate quotient-geometry test.
The [assessment](../drafts/2026-09-25-two-coordinate-affine-lifting.md)
records the named gap, target, prior failures, saved reasoning, and decision
test. The [official statement](https://proximityprize.org/) was reread;
the existing source qualifications are unchanged and all prior work remains.

[L006](../lemmas/L006-sparse-affine-lifting-sharp-error.md) proves the
proposed exact error 3/q and, by the same argument, (r+1)/q whenever
3r<=n-k and r/n<=delta<(r+1)/n. Thus q>=(r+1)2^128 is necessary and
sufficient for safety on each proved cell. It supplies a uniform upper
bound and attainment, not merely a new criterion equivalent to the gap.
At length 16 the two-omission count improves L004's 8,6,7,9 to three;
the new range does not extend L004's wider sufficient length-256 interval.

Outcome: ADVANCE; STATUS remains IN_PROGRESS and exploration turns used
are zero. Wider cells and the source correspondence remain missing. The
reason for the next direction is the specific possible failure of affine
lifting at minimum distance, first reached for three omissions at length
16 and dimension 8. The only current action is in PROGRESS.md. No complete
challenge proof or disproof candidate is claimed.

Validation: `python3 scripts/sparse-affine-lifting/check.py` passed 5,897
original-event pair checks over F_7, F_8, and F_11, including explicit
attainment, degeneracies, and sparse families. Of these, 4,909 exhaust the
constant-code sparse endpoint shapes up to coordinate permutations; other
cases are sampled or explicit, not a global exhaustive search. The script
also checks the excluded four-challenge example and exact budget comparisons.
The general theorem and the excluded example have full algebraic proofs.

The new lemma uses no prior lemma as a mathematical input; L004 and L005
are comparisons. All prior DAG rows are retained. Review covered the
strict distance and radius inequalities, support-dependent codewords,
same-support failure for sparse lines, and attainment in every characteristic.
Mathlib coverage remains not checked.

`python3 ../scripts/docs/check_structure.py --problem reed-solomon-mca`
passed with 7 nodes and 2 edges; `git diff --check -- .` also passed.
These checks validate documentation structure, not the mathematical theorem
or the paper-to-model correspondence.
