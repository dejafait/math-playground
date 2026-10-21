# Simultaneous shared-label pair sampling stopped

2026-10-17, step 278.

WHY IT FAILS: The first concentrated prefix (step 277) and the distinct
seed-277 distributed sample (step 278) each tested 250,000 actual triangle
assignments with the restored L057 common-weight join, but neither reached
pairs at two tags in any assignment. The
[distributed attempt](../drafts/2026-10-17-three-shared-label-pairs-distributed-attempt.md)
preserves all selections and counters, with complete independent replay
of all 224 reported pair-bearing assignments. Negative sampling supplies
neither a uniform obstruction nor a six-recovery witness; extension weights,
untested labels and arbitrary original charts remain. This stops further
extensions or reseeding of this sampling mechanism after two EXPLORATION
turns, not the mathematical feasibility target. Reopening needs a concrete
new structural restriction and a discriminating test. Preserve L101 and
ATTEMPTS/036–037/039. A distinct exact subgroup-constraint mechanism is
proposed for separate source review; no claim that it succeeds or avoids
the older cyclic elimination failures has been established.
