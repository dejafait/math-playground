# Bounded coalescence attempt, step 039

Completed as NEGATIVE route evidence, with the full statement and proof
in [L025](../lemmas/L025-bounded-residue47-coalescence-obstruction.md).
The prior ready assessment was
`drafts/literature/2026-10-05-residue47-bounded-coalescence.md`.

The initial plan tested the old ancestor CRT family against complete
inverse trees rather than assuming its one-path obstruction extended.
The decisive addition was transferring only the first s-t companion
parities to anchor 47, followed by a bound on the remaining formal
branches. The canonical proof retains the threshold, all offsets and
both clocks. Its source comparison distinguishes this argument from the
inspected ancestor and unrefined Mersenne statements.

The saved unfinished analytical checkpoint has now been incorporated
into that proof. Finite checks at horizons 1,4,8,12,20 have no failures;
full trees and exact roots are in
`scripts/bounded-coalescence/certificate.json`, reproduced by
`python3 scripts/bounded-coalescence/check.py`. They do not establish the
all-horizon conclusion. Attempt 014 records the resulting route stop.

Universal descent remains the main gap. A finite base or another fixed
clock cannot rescue this cover. A proposed clock depending on the initial
odd-run length requires a separate literature review before research;
no coverage or companion existence is inferred here. Existing notebook
changes from earlier steps were preserved.
