# Triangle isolated recovery versus the both-zero net

Ready target: the unchanged twelve-additional-recovery question in
`drafts/literature/2026-10-10-triangle-twelve-recovery-bound.md`.
Main gap: exclude thirteen additional parameters uniformly in labels.
Intermediate target: use one isolated disjoint-P recovery to restrict
simultaneous both-zero recoveries beyond L065's five/six bound.
Downstream use: strengthen L059's necessary seven-scalar fiber profile.
Continue on a uniform simultaneous restriction or concrete obstruction;
abandon if the calculation merely restates restored equations or capacities.

Unfinished reasoning checkpoint: put Y,Z,W for L065's pair quadratics.
For a net polynomial f=A ZW+B YW+C YZ, the restored coefficients appear
to satisfy beta_x^Y/c_x=A Z(x)W(x)/f(x), and the analogous Z formula.
Cross-multiplying all three restored equations gives a 3-by-3 matrix
linear in mu, hence a determinant of degree at most three. Essential
remaining check: show its kernel is exactly the net recurrence kernel
even when f vanishes at a P label or has degree below four. If one
isolated recovery has full weight, uniqueness of a degree-at-most-four
annihilator should force the determinant nonzero at its scalar. Then
at most three both-zero scalars could coexist. Lower-weight anchors
must not be silently treated as full. L010 equality supplies fullness
only in the hypothetical thirteen-additional case.

Reused coverage and duplicate check: the supplied ready EXPLORE
assessment covers this bounded triangle attempt. Inspected L057's
exact recovery and recurrence, L059's table statement, L065's full
classification and audit, the preceding interpolation/pair attempts,
and ATTEMPTS/025. No saved result supplies the proposed cubic bound.
The stopped formal pair-resultant/sampling route is preserved: this
test instead uses the exact net and a full-moment annihilator at an
actual isolated anchor. L060–L064 are not assumed. No source refresh,
cross-notebook input or mathematical script is needed for this proof.

Completed result: [L066](../lemmas/L066-triangle-isolated-anchor-net-bound.md)
proves the proposed cubic restriction under a full-weight isolated
disjoint-P anchor. A five-node Lagrange identity verifies all four
recurrence rows without dividing by f(P), so degree loss and shared-label
zeros cause no gap. At the anchor, L010's full-weight moment factorization
forces every degree-at-most-four annihilator to be its support quartic;
that quartic is outside the net by L065. Thus the determinant is nonzero
at the anchor. Both-zero recoveries give roots, hence at most three
distinct additional finite parameters. This proof needs no descent.

At thirteen additional recoveries, L010 first supplies full weights and
coordinate balance. At least seven supports then miss P, and L065's
audited maximum six supplies a full isolated anchor. Therefore this
hypothetical case has at most three both-zero parameters, at least ten
isolated parameters in total, and at least four isolated disjoint-P
parameters. The test succeeds with a uniform simultaneous restriction;
there is still no estimate on those four or more isolated rows. A
lower-weight isolated anchor alone is explicitly insufficient for the
annihilator-uniqueness argument. No need to classify the identically
zero determinant case without an anchor was inferred or pursued.

Mathematical verification in this step: checked signs of the recurrence
identity independently against L057's restored beta formula; verified
the five-node interpolation degree threshold 0 through 3, nonzero
scalings and all matrix dimensions; inspected L010's exact equality
statement and full-weight factorization; checked each direct DAG input
as L010/L057/L065. These are checks within the proof attempt, not its
required separate critical audit. No numerical certificate or script
is used as evidence for the uniform restriction.

Outcome: ADVANCE / RESEARCH / POTENTIALLY_NEW in the assessment's
limited sense. This is local progress beyond the inputs used, not a
certified originality claim or progress beyond unread sources. The
global interval remains 11/q–16/q. Preserve ATTEMPTS/025, the pending
L060–L064 audits and all unfinished work. The next route is separate
coverage approval and then critical audit of L066; its new assessment
is REVIEW_REQUIRED, so no audit is declared approved or completed here.
