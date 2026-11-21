# Collar transition range: one bounded attempt

The invocation-start EXPLORE assessment is the unchanged
`literature/2026-11-06-collar-preserving-linear-phase-correction.md`.
The target remains its exact existential full-torus linear equation.
The main gap is L030–L032/C032a mixed positivity. A solution would be
one feasibility input for nonlinear phase correction; convergence,
global nonnegativity and all other orders/shifts remain independent.

Use L847's full form, L848's prescribed data, accepted L849's branch
and cutoff, L850's operator, and L851's exterior construction. Checked
the contraction sign and the exterior coordinate/integration argument.
Inspected the complete exact-certificate implementation and replayed it
to `scripts/actual-g-radial-graph/exterior-phase-transition-replay.json`:
eight checks pass, phase margin 0.000273346304964 > 1/4000. This retains
L778(2)–(5)/step433 analytic and software qualifications, and is a
prerequisite check, not a separate complete audit of all cited results.

Targeted duplicate/failure searches in the existing relative-phase
working notes, histories and pointwise-inverse stop found no transition
solution. The ready assessment already compares relative divergence and
Moser results; no further essential source coverage is missing for this
attempt, and no new general PDE theorem will be assumed.

In midpoint coordinates let H=(u1+u2)/2 and V=(u1-u2)/2. For the
cutoff, H=chi h and V=chi delta beta. The constant linear coordinate
change conjugates the matrix to P I+Q adj D(H,V), so its rows are
(P+Q V_delta, -Q H_delta) and (-Q V_m, P+Q H_m).
This displays the actual transition coefficients, including the large
H_delta=chi' h term; the exterior approximation alone does not control
them. A smooth correction supported in the two transition annuli would
suffice, but is not a necessary restriction on the original target.

Discriminating test: find a smooth lift through these coefficients or
a source compatibility obstruction with its exact cutoff/support scope.
Matrix singularity, zero total integral, a pointwise inverse failure,
or a floating diagnostic alone will not count as a full-range result.
Unresolved at this checkpoint: possible actual-G zeros in the transition,
characteristic barriers, and the range of the coupled divergence operator.

## Completed bounded test

The transition really does contain full-form zeros for every allowed
cutoff, by the negative-real slice and endpoint-sign argument now
canonical in L852. No zero count, simplicity assumption or effective
width is needed. The exact negative-axis input was checked and replayed
to `scripts/actual-g-radial-graph/transition-negative-axis-replay.json`;
all seven checks pass, retaining the upstream qualifications.

At a full-form zero, differentiating the full density gives a real
linear functional gamma on the value of the variation. The residual's
required value is automatically in that functional's range, including
gamma=0; L852 contains the exact signs and the supported symmetric
pointwise assignment. This does not solve any neighborhood equation.

The attempted shortcut of an exterior lift followed by transition
inversion is stopped. The original global range test is unresolved,
so this turn is EXPLORATION, not a full-range NEGATIVE or a completed
linear correction. The refined remaining test is smooth local range
and higher source compatibility through the forced form zeros, then
assembly with the exterior lift. No generic PDE theorem, formal-jet
solvability or sufficient zero-integral condition has been imported.
