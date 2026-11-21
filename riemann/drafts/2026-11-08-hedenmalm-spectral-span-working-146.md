# Finite spectral-span kernel test, step146 — working checkpoint

Approved target: assess whether ker L intersects H_finite trivially for
Hedenmalm's full complex-zero eigenfunction span, without RH or simplicity.
Reuse the unchanged SPECIALIZE assessment
`literature/2026-11-08-hedenmalm-spectral-span-kernel-review.md`.
This is a mathematical source specialization, not new literature work.

Main gap: L030–L032/C032a actual-Xi all-degree mixed positivity.
The test addresses representative independence only. A positive metric,
pair symmetry, closure/completeness and any mixed-form transfer remain
independent unresolved obligations. L906's enlarged-domain stop survives.

Partial reasoning to preserve before completing the analytical checks:
write u_alpha(t)=t^(-i alpha) integral_0^t y^(i alpha)w(y)dy/y.
For fixed complex alpha, L906's small-t superexponential bound should
justify the integral; the product rule should give
Du_alpha=-alpha u_alpha+w/i. If a nonzero kernel representative is a
finite sum of these functions, Lf=wD(f/w) makes it a nonzero multiple
of w. Thus w lies in that same finite span F, and the displayed identity
makes D an endomorphism of F. No independence of generators is needed.
Cayley–Hamilton would then supply a nonzero monic p with p(D)w=0.

Remaining checks: prove W(x)=w(exp(x)) is Schwartz for every derivative
using the complete L906 bounds at both ends; verify the Fourier symbol
of (1/i)d/dx under exp(-2pi i x xi) is 2pi xi, and use continuity at
the finite real roots of p plus Schwartz inversion. A contradiction to
W(0)=w(1)>0 would prove the intersection is trivial. If an analytical
or invariance hypothesis fails, record it without changing the domain.
No Mellin normalization, generalized eigenfunctions, RH, simplicity or
formal inverse is assumed. No conclusion is certified by this draft.

Completion note: the stated obligations were discharged in canonical
L907, `../lemmas/L907-finite-spectral-span-kernel-intersection.md`.
This preliminary reasoning is preserved as written. The canonical
result awaits independent critical audit; no complete RH claim follows.
