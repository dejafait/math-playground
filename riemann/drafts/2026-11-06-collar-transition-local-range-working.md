# Transition-zero local range — bounded attempt

The unchanged invocation-start EXPLORE assessment is
`literature/2026-11-06-collar-preserving-linear-phase-correction.md`.
Its exact existential full-torus linear target remains the only target.
Main gap: L030–L032/C032a actual-Xi all-degree mixed positivity.
Intermediate discriminator: smooth local solvability, or a scoped local
range obstruction, at the forced transition form zeros before global
assembly. A local lift would supply one input for assembling the linear
correction; nonlinear convergence, global sign and other orders remain open.

Read L847's complete form/pullback calculation, L849's exact branch and
cutoff definitions, L850's operator derivation, L851's exterior lift and
support reduction, and all of L852. The endpoint argument in L852 retains
all multiplicities and does not divide by F or J. Its pointwise condition
does not establish neighborhood solvability. The accepted L848 sector
input and L850 negative-axis input retain their recorded analytic/software
qualifications; no new numerical claim is being made. Existing inverse
stops and transition working notes were checked. No additional literature
is needed for the bounded operator/source test covered by the assessment.

Let F=P+iQ, A=Du, J=1-det A-i tr A, sigma=Im(FJ), and
M=P I+Q adj A. The target is div(Mv)=sigma, with real smooth v.
At F=0 it reduces to gamma dot v=0, and the residual value is compatible.
The question now is local smooth compatibility beyond that value. No
simple-zero assumption, transversality, nonzero J or effective cutoff
width is available without proof. A conditional local statement must
not be reported as a solution at all actual forced zeros.

Continuation test: obtain an actual local smooth solution with its exact
verified hypotheses, or a violated necessary source condition. Formal
jets alone do not imply a smooth solution; a local solution alone does
not imply collar-preserving global assembly. Preserve any unresolved
degenerate cases and the existential cutoff quantifier.

## Reasoning checkpoint before canonical write-up

Choose the exact L849(18) cutoff with a=epsilon/2,b_0=epsilon.
On t=pi let B=h(pi-delta)+delta beta(pi-delta,delta). Uniformly
B tends to H=log(1000/R)>0. Every negative-axis G-zero reached by
this path belongs to a fixed finite set of radii strictly between R
and 1000. Thus at each crossing chi stays away from 0 and 1. The
explicit cutoff derivative is
-chi'=2 delta chi(1-chi)[(epsilon^2-delta^2)^(-2)
+(delta^2-epsilon^2/4)^(-2)], at least c epsilon^(-3).
The bounded derivatives of B then give A_12=(u_1,m-u_1,delta)/2>0.
The other G factor is nonzero for sufficiently small epsilon: z_2 tends
to the same isolated real root as z_1, but has a distinct nonreal angle.
No multiplicity is removed; locally F=w^n K with K nonzero and
w=u_1-u_1(p)+i(t-p_1) a real analytic coordinate.

For a variation (0,f), put kappa=z_2 partial_2 F/F; its removable
extension is regular because only G(z_1) vanishes. Direct differentiation
gives Dq[(0,f)]=F[J kappa f+A_12 f_t-(A_11+i) f_s].
At p choose f=0, f_s=Im J and
f_t=(A_11 Im J-Re J)/A_12. Then the bracket plus J vanishes at p,
so Dq+q vanishes to order at least n+1. Disjoint smooth bumps and
exchange partners realize all these finite jets globally with collar
support. This is an actual finite-jet compatibility statement, not a
smooth solution on any neighborhood. J=0 remains allowed.

Proposed outcome: EXPLORATION against the full smooth-range threshold.
Second exploration since L851; do not reset the budget for transversality
or jet cancellation. Park further point/finite-jet tests and reassess
using a global flux barrier for the same ready target, retaining the
scope distinction between one cutoff and all permitted choices.

Completed as L853, with the full proof, imports and qualifications in
the canonical lemma file. The outcome is EXPLORATION. The next bounded
test is the global flux condition recorded in PROGRESS.md; no further
finite-jet calculation or source approval is part of this completed step.
