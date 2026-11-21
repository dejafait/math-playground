# Shared endpoint Taylor moments — working checkpoint687

Gate: supplied assessment685, completed686, is SPECIALIZE for this
invocation. Reuse source-notes683/686, C998i/audit682, C998h/audit678,
C998a/audit655, C998g Section1/audit674 and C999q's exact Z.
Pre-existing notebook work is preserved. No source refresh or cross-notebook
input is needed. C998j is comparison evidence, not an audited input.

Main gap: actual-Xi positivity L030-L032/C032a and signed S3 coupling.
Intermediate target: one shared endpoint power-moment service on[0,1/8],
joined to interior Gauss, with complete square error<=1e-10 and total
scalar work<=20000000. It could pay the unchanged three-column square;
other residual terms, inverse debt and signed/global assembly stay open.
Stop at an unpaid error/setup term or an excessive prescribed cost.

Fixed prescription before calculation: expand f_n and d_n through
z^256 (128 nonzero terms) on[0,1/8]; share the seven power-moment
banks indexed by even powers2..256. For the bank use outward
integration of the fixed weights, with every tail and error charged;
no bank identity or accuracy is assumed. Join the three panels
[1/2,1],[1/4,1/2],[1/8,1/4], rho=2, with respectively117,81,63
Gauss points. Use512 fractional bits. Construct nodes by the assessed
Legendre recurrence and exact-sign dyadic bisection; exploit symmetry
and the exact zero root. After isolation in width2^-16 brackets, run
496 midpoint/sign updates per positive root to width2^-512. Evaluate
the full recurrence at each midpoint, with precomputed rational
coefficients; no Newton or reuse between different midpoint evaluations.
Initial isolation, bank setup and all remaining costs are not free.

First test the mandatory finite-node work, before bank construction or
quadrature batches. Even a fully successful bank cannot remove these
interior-node evaluations from this prescription. If this alone exceeds
the cap, preserve the local stop without claiming all shared moments
fail. The degree, precision and node scheme will not be retuned here.

Completed: C998k proves the mandatory node prefix costs23254464,
exceeding the complete square cap by3254464 even with root symmetry
and the zero root free. Exact planning checks pass; full rows/checks/work
were inspected. No endpoint bank, Taylor error, complete square error,
actual node or square entry is certified. The work stop precedes those
tasks and applies to every completion retaining this fixed node loop.
The5000000-budget interval-Newton node/weight subtarget is nominated
REVIEW_REQUIRED for separate source approval; no Newton derivation is
performed here. No justified new signed central mechanism was identified.
