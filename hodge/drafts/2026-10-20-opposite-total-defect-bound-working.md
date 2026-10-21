# Opposite total normalization length — calculation checkpoint

Approved target: derive a fixed-parameter upper bound for the total
normalization length of L120's opposite image using L121, L137 and
Hoa's Hilbert-coefficient bounds. The pre-invocation SPECIALIZE gate is
`drafts/literature/2026-10-20-opposite-total-defect-bound-specialization.md`.

Main gap: universal primitive rational Hodge realization. This step
only tests conditional global control of the normalization quotient;
an independent geometric lower bound, F existence and transport remain
unresolved. Continue if every bound parameter is fixed independently
of F and the quotient. Stop if an extra singularity/cohomology assumption
or unassessed source is essential. A finite upper bound is no exclusion.

Inputs read: L118 hypotheses/conclusions; L120 through the finite
unramified reduced-image factor; L121's complete proof and audit;
L137's full proof and audit. Reused the bridge and projective-degree
source assessments. Compared ATTEMPTS/070,073,078; none supplies or
invalidates the proposed coarse Hilbert-coefficient control. Existing
unfinished work is preserved.

Calculation in progress: let Q=nu_*O_B/O_Z. The finite image C of the
off-diagonal coincidence scheme contains all multiple-fibre values.
At a closed singleton fibre Stacks 04DG makes nu a closed immersion
over a neighborhood; the normalization injection makes it an
isomorphism there. Coherence and the Jacobson property then confine
Supp(Q) to C. Thus lambda=length(Q)=2-chi(O_Z), including Q=0.
Write Hoa's polynomial as
P_S(t)=delta binom(t+2,2)-e_1(t+1)+e_2.
Eventual graded/sheaf comparison and Serre vanishing identify it with
the Euler polynomial, hence lambda=2-delta+e_1-e_2.

Pending final coefficient check: with c=N-2 and
b=delta(delta+1)/2, reg(I)<=b^2, |e_1|<=delta^c reg(I),
|e_2|<=(3/2)delta^c reg(I)^2 should give
lambda<=2-delta+delta^c(b^2+(3/2)b^4).
Keep the original ambient N even if Z is linearly degenerate. Check
the nonzero-ideal edge case before importing the regularity formulas.
No mathematical script is needed. This checkpoint is unfinished;
the full proof and precise citations will be canonical in L138 if
the hypothesis check passes.

Completion: the hypothesis/substitution test passed. The canonical
proof is `lemmas/L138-opposite-total-normalization-length-bound.md`;
it also uses L137's established K3 Hilbert polynomial to fix the
linear coefficient and improve the displayed initial estimate.
This early checkpoint is preserved as working history, not a second
proof or current continuation. A separate critical audit remains
the sole next action in PROGRESS.md.
