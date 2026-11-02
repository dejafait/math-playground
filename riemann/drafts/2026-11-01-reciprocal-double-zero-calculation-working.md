# Reciprocal-cutoff double-zero calculation working record

2026-11-01. In progress under the prior SPECIALIZE assessment
`literature/2026-11-01-reciprocal-cutoff-double-zero-variation.md`.
Only its fixed-double-zero calculation is attempted. L019/L020 were read
in full; L016 normalization and L018 conjugation convention checked;
L610 supplies definitions only. Its numerical premise is unused.
Scoped duplicate checks found the heat-flow double-zero result L059,
whose different parameter evolution is not imported.

Working identity to verify: set Q(z)=(Xi(z+2i)+Xi(z-2i))/2.
The weight derivative at epsilon=0 is -cosh(2u), so F=Xi-epsilon Q
with second-order remainder. Scalar Taylor's bound for x>=0 is
0<=exp(-x)-1+x<=x^2/2. Applied to both reciprocal factors it bounds
the weight remainder by epsilon^2 cosh(4u)/2. L019 makes this
integrable after multiplication by u^j exp(Ru), j<=2.

At a hypothetical double zero, write A=Xi''(a) nonzero. Then
F(a)=-epsilon Q(a)+O(epsilon^2), F'(a)=-epsilon Q'(a)+O(epsilon^2),
F''(a)=A-epsilon Q''(a)+O(epsilon^2), suggesting
D_1(F;a)=epsilon A Q(a)+O(epsilon^2).
Check all constants and reality before canonicalizing. No assertion that
such a exists, no control of A Q(a), and no zero-splitting conclusion.
Equality cascades and frequency sweeps remain outside scope.

Completion: canonicalized as L611 after checking the exact product
remainder and an explicit strict-sign threshold. The conjectured leading
term above is proved there; its sign remains uncontrolled. This working
record preserves the calculation's initial state, not an additional proof.
