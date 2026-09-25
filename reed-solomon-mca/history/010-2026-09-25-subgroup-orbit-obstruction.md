# 010 — 2026-09-25 — Full subgroup orbits cannot supply sixteen

Completed one structured test of sixteen bad challenges at support
cutoff twelve on the order-16 subgroup of F_97^*. The
[assessment](../drafts/2026-09-25-sixteen-challenge-budget-test.md) records
the target, alternative mechanisms, saved reasoning, and decision test.
The [official statement](https://proximityprize.org/) was reread; its
preliminary formulation and unresolved source qualifications are unchanged.
No pre-existing local changes were present; other notebooks were untouched.

The new [L009](../lemmas/L009-two-character-orbit-obstruction.md) classifies
four-sparse errors whose full multiplicative orbit spans a projective syndrome line.
Only weighted order-four cosets occur, so arbitrary nonzero normalizations
give at most four distinct points on an affine line. The proof works over
every finite field containing an order-16 subgroup. The
[failed approach](../ATTEMPTS/004-full-subgroup-orbit-sixteen-challenges.md)
preserves the exact scope: general lines, partial orbits, and errors outside
the chosen orbit are not ruled out.

Outcome: NEGATIVE, with zero consecutive exploration turns after this
informative obstruction. Four is below the required sixteen and the
existing lower count ten. The main four-omission bounds remain 10/q and
69/q, while q=97^20 permits fifteen challenges. STATUS stays IN_PROGRESS;
there is no complete challenge candidate and no new safe-radius claim.

The reason for changing direction is that the locator determinant also
applies to general affine moment pencils without subgroup equivariance.
Its degree suggests a bound near sixteen, but singular and persistent-root
cases and any equality analysis remain unresolved. The compact checkpoint
contains the sole current next action. No further search was undertaken
after the full-orbit obstruction settled this step's structured test.

The lemma uses no earlier lemma as a mathematical input; L008 is only
a comparison with an existing lower bound, so the new DAG row has no
inputs. Mathlib coverage is not checked; the supporting ArkLib definition
names and immutable links are retained. The auxiliary check verified all
ten determinant identities over the integers and 50,960 moment-pair/support
systems over F_97, as well as the exact budget. The algebraic proof is
independent of the finite enumeration.

Validation commands: `python3 scripts/subgroup-orbit/check.py`,
`PYTHONDONTWRITEBYTECODE=1 python3 ../scripts/docs/check_structure.py --problem reed-solomon-mca`,
and `git diff --check -- .`. Bytecode writes are disabled for the shared
checker to keep all generated artifacts inside the active notebook.
