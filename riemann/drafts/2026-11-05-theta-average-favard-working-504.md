# Step504: actual theta-prefix Favard test

Approved SPECIALIZE target: the exact degree-three recurrence action in
`drafts/literature/2026-11-05-theta-average-degree-three-recurrence.md`.
Main gap: actual-Xi all-degree mixed positivity. This bounded test may
reject common nondegenerate positive-measure orthogonality, without
settling individual roots or any all-degree signs.

Read L019/L021/L795 and L791's actual-coefficient proof and step478 audit;
reused the completed step503 source assessment. Inspected the complete
gamma(0..3) intervals, audit PASS/no failures and original hashes.
L778's analytic evaluator/software contracts remain inherited, not
independently re-audited. Prior unfinished work remains intact.

Put a=gamma(1)/gamma(0), b=gamma(2)/gamma(0), c=gamma(3)/gamma(0).
Then Q0=1, Q1=x-1/a, Q2=x^2-2a*x/b+1/b,
Q3=x^3-3b*x^2/c+3a*x/c-1/c. All divisions are legitimate by L021.
Coefficient comparison gives alpha0=1/a, alpha1=2a/b-1/a,
beta1=1/b-1/a^2, alpha2=3b/c-2a/b,
beta2=1/b+3a/c-4a^2/b^2, and the forbidden Q0 coefficient
delta=1/c+1/(a*b)-2a/b^2 in xQ2.

Next within this bounded attempt: verify these polynomial identities and
evaluate their exact rational interval enclosures once, preserving full
inputs/provenance and denominator bounds in a disk certificate. Stop
the common-measure mechanism if delta excludes zero or beta is proved
nonpositive; an undecided prefix ends this test without degree extension.
No result had yet been claimed at that checkpoint. No fresh quadrature
or parameter model is permitted by this target.

Completed: L796 contains the full canonical specialization and scope.
`scripts/central-jacobi/favard-prefix-certificate-504.json` records exact
Laurent identity checks and rational enclosures: beta1 and beta2 are
positive, delta lies in [-645.225425,-645.225424]. No rearrangement or
degree extension was needed. Common-measure orthogonality stops;
individual roots and the main gap remain open. This draft preserves
the pre-calculation checkpoint and is not a second proof or next-action
record.
