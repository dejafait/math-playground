# Low moments: origin-normalization closure overlaps the existing stop

Step 87 tested the exact unit-residue first-moment normalization and
simultaneous low moments under the approved inner resolvent target.
The incomplete attempt is saved in
[the working record](../drafts/2026-11-03-joint-low-moment-rigidity-working-87.md).
It produced no new lemma or norm countersequence.

WHY IT FAILS: Moving the noncancelling continued values at u=0 to the
circle by cancelling the common interior poles incurs exactly the
factor already proved in
[C645p](../lemmas/C645p-angular-projection-zero-evaluation-cost.md).
Its exponential rate is 1+log(121/80), far above the proposed 1/1000
block budget. C645p already retains the full continued spatial response;
retaining additional moments alone does not remove that cost. This is
an overlap with the old origin-evaluation stop, not a new obstruction
to the actual simultaneous moment block. No ambient extremizer is
asserted to have unit residues or admissible displacements. Stop this
closure; the next test uses the original unit-residue logarithmic
derivative on L673's explicit full-support node family.
