# 008 — 2026-09-25 — Five challenges at the distance boundary

Completed one minimum-distance-boundary test. The
[assessment](../drafts/2026-09-25-distance-boundary.md) records the gap,
decision test, saved unfinished reasoning, and result. The
[official statement](https://proximityprize.org/) was reread; the source
qualifications remain unchanged, and all prior work is preserved.

[L007](../lemmas/L007-minimum-distance-boundary-sharp-error.md) proves an
affine-lift/disjoint-support dichotomy at n-k+1=3r. Its bound is
max{r+1,floor(n/r)} bad parameters. Five split cubic fibers attain five
on the smooth length-16, dimension-8 code on F_17^*, over every F_(17^s).
The exact error is 5/q on [3/16,1/4); this refutes the
[unconditional r+1 extension](../ATTEMPTS/003-unconditional-distance-boundary-extension.md).
The same argument adds the exact 44/q cell at n=256,k=128,r=43.

Outcome: ADVANCE; STATUS remains IN_PROGRESS; exploration turns used are
zero. The main general radius and ABF26 correspondence remain unresolved.
The exact new budget is q>=5*2^128; q=17^32 meets it, whereas L004's
count 23 does not certify this cell. The length-256 addition still falls
short of L004's wider sufficient interval. No complete challenge candidate
is claimed.

The reason for the next direction is that four omissions permit overlapping
errors beyond the distance boundary. At q=17^32, seven bad parameters
would exceed the actual budget, so that is a discriminating target for
the next cell. The only current next action is recorded in PROGRESS.md.

The proof checks same-support failure and all extension fields algebraically.
The new DAG row has no lemma inputs: its counting and polynomial arguments
are self-contained; prior lemma references are comparisons. Mathlib coverage
is not checked. The auxiliary command
`python3 scripts/distance-boundary/check.py` checks the explicit pair over
all 17 parameters and 697 admissible supports, polynomial identities,
degree bounds, and exact integer thresholds. This is not an exhaustive
search over input words or a substitute for the general upper-bound proof.

Validation passed: the auxiliary check found exactly {0,3,6,10,14};
`python3 ../scripts/docs/check_structure.py --problem reed-solomon-mca`
reported 8 nodes and 2 edges with valid structure and links;
`git diff --check -- .` also passed. Structural checks do not verify
the mathematics or identify the frozen event with ABF26.
