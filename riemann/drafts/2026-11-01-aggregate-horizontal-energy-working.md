# Aggregate horizontal energy: bounded attempt in progress

Approved target: attempt M(Z)<=E(Z) for the two packets in
`literature/2026-11-01-aggregate-horizontal-energy-test.md`.
The supplied EXPLORE assessment is reused unchanged. Main gap:
actual-Xi all-degree signs; a horizontal count interface would only
be an intermediate input. No zeta realization is assumed.

Source/duplicate check: the finite-frequency assessment's complete
comparison has been read. Lamzouri v1 Proposition 2.1 controls the
simple-real deficit, not this count. L612/L613 and their recorded
stops concern count saturation and a contrast between two families,
respectively; they are contrasts, not mathematical inputs here.

For a>0, packet multiplicities m,n and depths u,v, write
H(b)=(sinh(pi*b)/(pi*b))^2 (continuous value H(0)=1),
F(a,b)=Re K(a+i*b)^2. Direct ordered-pair enumeration gives

    M=4m^2+4n^2,
    E-M=2m^2(H(2u)-1)+2n^2(H(2v)-1)
        +4mn(F(a,u-v)+F(a,u+v)).

Every coincident label is retained when a depth vanishes. This
reduction is provisional until the complete argument is checked.
Equal depths and equal multiplicities suggest useful nonnegative
integral rearrangements; neither observation proves the unequal case.
The remaining bounded task is m/n=2 or 1/2 with unequal depths.

Continue if a rigorous proof on the full specified family can be
obtained, or stop universal domination if a strict counterexample is
certified. A numerical search is diagnostic only. No general-family
extension, all-height count conclusion or Xi sign is asserted.

## Completed bounded attempt

The partial proofs and exact remaining inequality are now canonical in
[L614](../lemmas/L614-two-packet-horizontal-energy-reduction.md).
They cover aligned depth/multiplicity and a<=1/2; the inverse-order
1:2 branch for a>1/2 is not settled. For u<=arcosh(2)/(2pi),
monotonicity in the shallower depth reduces that branch to v=0.

The diagnostic in `scripts/aggregate-energy/two-packet-probe.json`
found no negative sample at its tolerance. This does not validate the
universal inequality or any missing sign. No rigorous negative witness
was found. The outcome is EXPLORATION, with an exact reduced target,
rather than completion of the bounded test.

Continuation reuses the unchanged EXPLORE assessment and its exact
target. Use L614 (3), keeping the negative term (A-2B)^2-1 and
both positive terms; or first settle the v=0 slice in L614 (4).
The proposed refinement is an analytic comparison of the residual,
not another unchanged floating-point grid. Failure of a sufficient
termwise estimate would not refute the energy inequality. All actual-
Xi, general-multiset, weight-removal and charge-conversion gaps remain.
