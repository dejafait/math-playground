# Signed Gaver uniform-error attempt1771

19 November 2026. Preserved working checkpoint for the approved target1769;
the draft below records reasoning before completion. Reuse the separately approved
SPECIALIZE assessment1769 and source notes1764/1769. Essential inputs
are C033j and audited C033p, with every qualified external input retained.
No additional source review, mathematical script or numerical experiment.

Main gap: L030-L032/C032a actual-Xi all-degree positivity, including
C028b's unpaid sublinear height and realization. Intermediate target:
uniform finite-Laplace evaluation of r_sigma at x=7/8 and 9/8. Its
possible downstream use is jump resolution and capped finite separation;
cancellation, moments and actual-Xi signs remain independent.

Let a_x=log(2)/x and c_n=(2n)!/[n!(n-1)!]. The source's unaccelerated
finite formula has coefficients a_x*c_n*(-1)^k*binom(n,k) at positive
nodes a_x*(n+k), 0<=k<=n. For a finite signed measure the proposed
kernel identity is integration against

    K_(n,x)(t)=a_x*c_n*exp(-n*a_x*t)*(1-exp(-a_x*t))^n.

Finite linearity needs only finite variation; the zero atom contributes
exactly zero for n>=1. Normalization is the source's beta integral.
The local Lipschitz term can use the exact Gaver mean/variance sums;
the local normalization loss needs its own kernel-mass bound.

Proposed full-variation bound: c_n=n*binom(2n,n)<=n*4^n. Outside
I=[3/4,5/4], for either selected x, t/x<=6/7 or t/x>=10/9.
The function 4*y*(1-y), y=2^(-t/x), is strictly below one there.
Take q=max{4*2^(-6/7)*(1-2^(-6/7)),
           4*2^(-10/9)*(1-2^(-10/9))}<1.
Then sup_(t outside I) K_(n,x)(t)<=a_x*n*q^n would pay the whole
variation tail by V*a_x*n*q^n. This is a supremum calculation,
not probability concentration against an arbitrary measure.

Continuation/abandonment test: independently justify the exact signed
identity, normalization, moment/local-error bound, normalization leakage,
and supremum-tail decay, obtaining an explicit E_n(B,L,V)->0. A failing
term stops this application. Record coefficient amplification without
claiming evaluation stability, numerical heat constants or a separator.
Preserve unfinished C033k, stops1571/1576, and closure1768.

Completed1771: the full proof and exact bounds are now canonical in
[C033q](../lemmas/C033q-signed-gaver-uniform-finite-laplace-error.md).
All three error terms tend to zero under the specified parameters.
The next source-gated critical audit is separate from this derivation;
this working draft is not an independent proof or current checkpoint.
