# Renewal-density cutoff test — working record

2026-10-30. One proof attempt under the unchanged EXPLORE target in
`drafts/literature/2026-10-30-weil-nullspace-renewal-adjoint-coverage.md`.
The startup snapshot and that assessment were supplied and read.

Main gap: actual-Xi all-degree positivity; this test addresses only
vanishing of both traces of an assumed real normalized simple nullvector
at a finite first-zero radius. Endpoint success would be necessary for
the proposed relative-flux route under additional trace-continuity
assumptions; it would not establish the near-zero O(lambda) rate.

Inputs inspected: L512 normalization; L513's full signed trace (T),
including its exterior tail and renewal facts; L514's domain split;
L515's bounded-data application; L516's exact model (2). The L517
Abel/form-energy stop concerns non-eigenvectors and remains in place.
No cross-notebook input or new source import is used. The approved
assessment already excludes the inapplicable weak-dual shortcut.

At the working stage no trace cancellation is proved. Let I=(0,ell),
f=v 1_I and phi_epsilon be smooth interior cutoffs of f. For positive
epsilon the weak null equation permits phi_epsilon. The proposed test
is to identify the complete interior distributional limit of A phi_epsilon
and the remaining endpoint contribution in its pairing with the actual
nullvector. Every prime power in the common finite mu_A, nu_rho, scalar
term, pole and exterior forcing must be kept, including cutoff equalities.

Candidate diagnostic, not yet established here: apply L513 to compact
smooth functions with zero trace to identify G_I f distributionally;
then determine whether translated v singularities at interior prime
displacements survive in A f. A residual nonzero as a distribution is
an obstruction to coefficientwise adjoint cancellation, not a proof
that its pairing with a particular eigenvector is nonzero. Check this
distinction and the cutoff limit before drawing a route decision.

Continue only on a justified identity forcing both traces to vanish.
A surviving residual or a demonstrated domain failure ends this raw
renewal-weight implementation. No singular test, H1 regularity, spectral
gap, eigenvector sign, endpoint branch convergence or rate is assumed.

## Completed bounded test

The full proof and qualifications are canonical in
[L518](../lemmas/L518-raw-renewal-adjoint-cutoff-residual.md).
The reference interior distribution is the retained exterior tail;
the full residual has unavoidable scalar and interior prime-power
singularities. No nonzero raw left/right combination cancels it.
The legitimate cutoff pairing keeps the trace term and does not force
the residual's pairing with an actual nullvector to vanish.

Outcome: NEGATIVE for this raw-adjoint implementation. No assumed
nullvector was constructed, and no zero or nonzero trace was proved.
The old source limitations and Abel/form-energy stop are unchanged.
This is a local calculation under reused coverage, not an imported
resolution or a claim of progress beyond the literature checked.
The new result awaits a separate conceptual audit; its prepared scope
is a new continuation, not an audit performed in this turn.
