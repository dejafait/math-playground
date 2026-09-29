# Two-way rotation Yoneda test: saved reasoning

The prior SPECIALIZE assessment matches the saved target exactly.
The gap is a representative for the cubic RM action that can move in
the fourth RM direction. This test allows both mixed first-order
classes for P=O_C and Q=O_(C^(2)), no self class, and an ambient
coefficient first appearing at order tau^2. The desired threshold is
one pair canceling both full diagonal obstructions for a common
kappa outside V_D; earlier results permit only three of four
directions. Higher orders, algebraization and the universal Hodge
target would remain open after success.

The pair-deformation model in the saved review should identify the
order-two obstruction as the central ambient Atiyah term plus the
square of the mixed degree-one matrix. This uses the actual chosen
first-order sheaf, not just the central direct sum. No formality
assumption is needed at this order.

At a finite intersection write M=R/(z,r), N=R/(z,q). Both directed
Ext^1 groups have one coordinate there. A local reference for mixed
coordinates a,b has generators m,n and relations

    z m = z n = 0,   r m = tau a n,   q n = tau b m.

It is the cokernel of a two-by-two matrix over R/(z), whose central
matrix is diag(r,q). The central matrix is injective, so the
reference should be flat over C[tau]/(tau^3). On the separated M
branch its support has r=tau^2 ab/q, with the analogous expression
on N. Differences from this reference are order-two central Ext^1
classes; their diagonal blocks should add regular normal shifts.

The restricted motion is constant on supports modulo tau^2 away
from intersections. A rank-one pushforward then supplies graph
supports, even when the lifted sheaf is a line bundle rather than
a chosen quotient. Complete elliptic fibres force equality of j.
L014's unmatched critical pairs (1,2) and (1,3) appear to force the
three critical-value variations to coincide for each sign. The
matched pair (2,3) would then force ab=0 on each double curve.

Remaining checks: justify the global block obstruction identity and
the reverse seven-dimensional mixed group; control all corrections
to the local reference; recover and glue an embedded first-order C
lift from the order-two graph displacements; retain arbitrary point
coordinates at infinity via the normal-sheaf Hartogs property. It
would suffice to exclude cancellation geometrically, without
asserting that local products determine the full global Ext^2
classes. A point product need not be zero merely because it is
invisible away from that point.

Continue if a pair survives the full test. Stop this restricted
mechanism if any cancellation necessarily recovers C and thus forces
kappa into V_D. These notes are provisional, not a proved result.

## Completion on 2026-09-27

[L024](../lemmas/L024-two-way-rotation-products-cannot-cancel.md)
completes this test. The pair model gives the full diagonal
obstruction with the same two mixed classes. Its reference matrix
is flat, and all second-order differences add only regular normal
terms on the separated branches. The two unmatched critical pairs
force all three critical-value variations to agree, so every
finite product residue vanishes. Embedded C recovery and Hartogs
then force kappa into V_D, including all punctual mixed parameters.

This decides non-cancellation in the full global Ext^2 groups
without identifying global products with their stalk images or
asserting that the point products vanish. The admissible
coefficient set is exactly V_D, since zero mixed motion suffices
there. It is not a claim that every mixed motion lifts there.

Outcome: NEGATIVE. The standard obstruction theory is imported;
the compatibility and recovery specialization was not matched by
the prior review, so it is POTENTIALLY_NEW without certified
originality. The restricted mechanism stops. The attained span,
the set of surfaces covered and the universal Hodge gap do not
change. No numerical experiment or new mathematical script is
needed for this argument.
