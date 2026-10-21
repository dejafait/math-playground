# Signed linear response mean — working checkpoint, 2026-10-05

Approved target: determine whether L367’s signed linear coefficient is
negative at arbitrarily large real frequencies. Reuse the unchanged
SPECIALIZE assessment in drafts/literature/2026-10-05-gaussian-linear-response-sign.md.
Main gap: global actual-theta mixed positivity. A negative dyadic mean
would stop eventual nonnegative signing of the linear response, without
signing the total expression or deciding RH. Continue if a negative
constant exceeds all errors; abandon this mean certificate otherwise.
Existing notebook changes and L365’s separate fixed-regulator stop are preserved.

Unfinished calculation: write U=ζ(1/2+it), Z=ζ(5/2+it), Q=A exp(iφ),
W=bZ with b=(t²/4−3/16−it/2)/π. L366 gives F_0=−A exp(iφ)U
and L368 gives G=A Re(exp(iφ)W). Critical-line reality implies
exp(2iφ)U=conj(U), including differentiated identities. It appears to
reduce the polarization to conjugate mixed products, whose diagonal is
−4 Re(b) Σ n^(−3)(ω−log n)² after retaining the envelope curvature.
The proposed normalized mean limit is −ζ(3)/(4π), not yet established.
Still to verify: the exact algebra, fixed-cutoff Cauchy remainder through
two jets, all equal-frequency collisions, absolute off-diagonal bounds,
moving weights, pole-correction derivatives and the error terms from b′,
b″ and (log A)″. The full proof, if completed, belongs in a canonical lemma.

## Completion

The negative-mean threshold was met. The full projection algebra, fixed-cutoff
Cauchy jets, infinite right-line tail, equal-frequency diagonal, all
off-diagonal sums and moving-weight estimates are canonical in
lemmas/L369-signed-linear-response-negative-dyadic-mean.md. The proof yields
mean −ζ(3)/(4π)+O(1/log H+H^(−1/2)(log H)²), and a fixed negative margin
in every sufficiently high dyadic interval. This is a local specialization
of assessed scalar inputs, not a novelty claim. The initial unfinished
checkpoint above is retained as work history, not as a second proof.
A separate critical audit is proposed and has not been approved or performed.
