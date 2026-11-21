# Corollary 466c: finite contact minors do not force real kernel roots

## Hypotheses

This is a finite algebraic diagnostic, not a density/contact theorem.
For real numbers a_0,...,a_4 define

    A_j=[a_(r+s)]_(0<=r,s<j),
    D_j=(-1)^(j(j-1)/2) det A_j,       1<=j<=3,
    A=A_3.

Consider the class of jets with D_1,D_2>0, D_3=0 and rank A=2.
The leading 2-by-2 block is invertible, so the one-dimensional
kernel has a unique vector v with v_2=1. Set

    P(z)=v_0+v_1 z+z^2.

These are the pointwise finite signs and normalization appearing
in C466b (14), considered without the actual-density, Volterra,
first-contact-neighborhood or zero-kernel hypotheses of that result.
C466a supplies no premise of this finite counterexample.

## Conclusion

The stated finite conditions do not imply that P has real roots.
An exact witness is

    (a_0,a_1,a_2,a_3,a_4)=(1,0,-1,0,1).

It has D_1=D_2=1, D_3=0, rank A=2 and normalized kernel vector
v=(1,0,1). Its polynomial is P(z)=1+z^2, with discriminant -4
and roots i and -i.

This refutes only the implication from the stated finite conditions.
It neither realizes an actual p-jet nor asserts that C466b's actual
contact polynomial has nonreal roots. The full scalar law, the
first-contact interpretation and actual-H structure are untested here.
In particular no actual contact, failure of a sign-variation bound,
failure of global PF, or counterexample to RH follows.

## Proof

For the specified entries the complete matrices are

    A_1=[1],      A_2=[ 1  0 ],      A=[ 1  0 -1 ].
                      [ 0 -1 ]         [ 0 -1  0 ]
                                       [-1  0  1 ]

Thus det A_1=1 and det A_2=-1. The respective sign factors are
1 and -1, giving D_1=D_2=1>0. The last row of A is the negative
of its first row, so det A=0 and D_3=(-1)^3 det A=0. Its leading
2-by-2 minor is nonzero, hence its rank is at least two; the row
dependence makes its rank at most two. Therefore rank A=2.

For a vector (v_0,v_1,v_2), the first two equations Av=0 are
v_0-v_2=0 and -v_1=0. The third is their redundant equation
-v_0+v_2=0. With v_2=1 these give exactly v=(1,0,1), and direct
multiplication gives Av=(0,0,0). Consequently P(z)=1+z^2.
Its real quadratic coefficients have discriminant

    v_1^2-4v_0=0^2-4=-4<0,

where the required counterexample threshold is strictly negative.
Equivalently P(i)=P(-i)=0 and neither root is real. All entries,
minor values, rank and kernel equalities are exact; no numerical
search or approximate root isolation is used. This proves the
claimed failure of the finite implication. ∎

The prior source assessment is
[assessment889](../drafts/literature/2026-11-14-contact-kernel-polynomial-root-test-889.md).
Its inspected positive-raw-minor root theorem (Bakan--Berg,
arXiv:1605.01196v2, Section 5.3, equations (5.6)--(5.10)) requires
positive raw leading determinants. Here det A_2=-1, so that theorem
does not apply. The proof above is an elementary exact diagnostic
of the remaining signed case, not a reproof of that theorem.
The source search did not identify this exact witness as a cited
result; no originality claim is made for the elementary example.

The diagnostic is complete and stops at m=3. A real-factor argument
for C466b must use an additional justified premise; the generic
leading signs alone cannot supply it. Actual-density realization,
weighted masses, strict forcing, simultaneous contacts, local barrier,
compact propagation and L030-L032/C032a transfer remain unresolved.

## Mathlib

Full matching coverage has not been checked. Determinant evaluation,
finite rank, matrix kernels and quadratic discriminants are supporting
elementary algebra, but no specific Mathlib declaration or formal
verification is asserted. Unknown coverage is not evidence of absence.
