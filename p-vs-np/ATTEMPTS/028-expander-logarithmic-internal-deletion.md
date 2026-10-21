# Attempt 028 — Logarithmic internal deletion on L031's expander family

The proposed application was to obtain L037 data for L031's unchanged
used expander proofs through L073's logarithmic positive-internal deletion
promise. This tests a sufficient structural mechanism, not all data or
certificate representations.

**WHY IT FAILS.** [L074](../lemmas/L074-expander-internal-deletion-threshold.md)
identifies the once-subdivided expander on the shared originals and edge
gates inside the full signed value graph, for both sigma choices.
The imported graph theorems and explicit expansion count force at least
epsilon*n/4-3 deleted edge gates for residual treewidth at most two.
L031's actual full proof length is O_Delta(n log(n+2)), so this exceeds
floor(log_2(T+2)) eventually for fixed epsilon and Delta. L074 gives
finite-size sufficient failure tests; its separate step-286 informal
critical audit found no substantive defect in the restricted conclusion.
Stop this supplied-family application; small instances not meeting those
tests remain undecided. Other structural families, alternative reduced
data/certificates and different proofs remain open. This is not an
affine-ABP, ER or SAT lower bound. Preserve Attempts 019–021 and all
unfinished receiver work.
