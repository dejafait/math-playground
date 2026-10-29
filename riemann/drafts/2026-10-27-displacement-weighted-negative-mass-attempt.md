# Displacement-weighted negative mass: working attempt, 27 October 2026

The invocation reuses the saved EXPLORE assessment
`drafts/literature/2026-10-27-displacement-weighted-negative-mass-test.md`.
The exact target is its zero-safe conjugate-pair majorant for N(T),
tested against o(T(log T)^3). The main gap remains all-height initial
signs and global mixed positivity. A mean saving would only control
exceptional mass; it would not exclude individual negative heights.

Startup inspection found substantial existing notebook work; all of it
is retained. L018, the complete L024 product proof, L251, L465 Sections
1, 2 and 5, the preceding source comparison, and the count/gap failure
were read narrowly. No external half-plane premise is used.

## Partial reasoning saved before the summation test

For a distinct conjugate Xi pair gamma +/- i d with multiplicity m,
0<d<1/2, put q(z)=(z-gamma)^2+d^2 and F_pair(z)=Xi(z)/q(z),
removing just one copy of each zero. The Csordas (2.3) pair kernel
is 2m((t-gamma)^2-d^2)/q(t)^2. Off real zeros it gives the tentative
bound

    max(0,-D_1(Xi;t))/A(t)^2
      <= 2 sum_pair m (d^2-(t-gamma)^2)_+
                         (F_pair(t)/A(t))^2.

Only pairs whose windows meet [T,2T] contribute, a finite set. At a
real zero the left side is zero since D_1=Xi'^2, and each summand on
the right is zero. The product's inverse-square summability should
justify logarithmic differentiation off real zeros. Integrating with
t=gamma+d v gives a d^3 weight; this cancels denominators before any
estimate. These application details still need the full written proof.

The unresolved arithmetic quantity is the resulting sum of squared
entire pair-divided factors. Merely retaining d^3 does not bound it:
F_pair/A=-Z/q on the real line, so a separate estimate is essential.
The next part of this same bounded attempt checks ordinary moments
and whether their loss can be quantified without importing an
uncovered zero-indexed theorem. No summation saving is claimed.

## Completed bounded attempt

The tentative argument is now written with its application checks in
[L471](../lemmas/L471-displacement-weighted-negative-mass-majorant.md).
That canonical file contains the full proof, exact sufficient weighted
estimate, gamma transfer and failed ordinary-moment substitution. The
notes above preserve the reasoning saved before that work and are not
a second canonical proof. The summation saving was not obtained.

The implementation stop and reopening condition are recorded in
[the attempt decision](../ATTEMPTS/2026-10-27-displacement-weighted-negative-mass-test.md).
