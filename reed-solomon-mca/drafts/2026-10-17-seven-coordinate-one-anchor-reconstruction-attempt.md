# Seven-coordinate t=1 support-seed reconstruction — completed reduction

2026-10-17, step 293. Reuse the unchanged ready EXPLORE assessment
`literature/2026-10-17-seven-coordinate-syndrome-bound-review.md`.
Inputs read: L010, audited L103/L104/L105. No new source review or
cross-notebook input. Preserve all earlier work and restrictions.

Main gap: exclude or realize sixteen original bad parameters; global
interval 11/q–16/q unchanged. Bounded target: a finite support-seed
reconstruction of L104's t=1 profile on
S={1,8,12,18,22,27,33}, using its r>=9 two-overlap rows. Downstream
use: an exact finite simultaneous-compatibility test, not a bound yet.
Continue if equality forces enough seeds to reconstruct every coefficient
with explicit gates; abandon a proposed rank implication on a contrary
gated instance, and reassess if only independent equations remain.

Provisional mechanism, requiring completion in a canonical proof:
the unique equal-lift event has zero triple P and support R=S minus P.
Pair linearity follows from audited L103 exactly as in L105. Thus each
two-overlap I is PP or PR, with no repeated I; r>=9 implies at least
six PR rows. Two PR edges can be chosen disjoint in their P and R
labels (otherwise this bipartite edge family is a star, size <=4).
Those rows determine a rational normalized nonzero vector p on P.
After projective rescaling the lift is p on P and A_z*mu+B_z on R,
with every A_z nonzero because the base event is full on R at infinity.

Normalize the first two rows to mu=0,1. On their two common observed
R coordinates, B and A are rational, with A nonzero. Equality degree
four leaves at most three other-row occurrences at each R label.
Since r>=9, a third row avoids both exceptional R labels. It observes
at least one of the already reconstructed coordinates, so has a unique
rational mu distinct from 0,1. It provides the second value at each
of the two missing R coordinates, reconstructing their affine functions.
All remaining observation/weight gates must be checked explicitly.

Obligations: prove the seed-existence argument including PP rows;
derive the projective normalization without rationalizing the original
chart; specify all rejection gates and all 540 remaining row tests;
prove the construction converse supplies actual nonpersistence and
only selected events, not sixteen; quantify the finite seed bound.
No mathematical script or certificate is planned for this analytic step.

Completed in
[L107](../lemmas/L107-seven-coordinate-one-anchor-three-seed-reconstruction.md),
the canonical statement and full proof. All obligations above are discharged
there. The bound is 14,696,640 support seeds per fixed (S,P), with 540
remaining row tests per surviving seed and the necessary nine-scalar
threshold. These are case-count bounds, not executed computations. No
maximum, nine-row survivor or equality pencil is claimed. The local
converse supplies the base and three seed events only. Separate critical
audit is the next substantive action under the unchanged ready scope.
