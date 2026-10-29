# Cubic internal-curl operator: finite-range test

Started 2026-10-26 under the unchanged prior EXPLORE assessment
`literature/2026-10-26-complete-cubic-quadratic-asymptotic.md`.
The registered target is the complete cubic N^2 asymptotic and comparison
with L285(4). This note preserves the current reasoning before completion.

Main gap: interacting continuum existence with a nonzero sector and finite
positive mass. Intermediate target: a uniform finite-range approximation
to L287's internal-curl covariance operator. Its downstream use is a
controlled bulk-limit passage in the G_-+ group. The other three residual
groups, compensation, subleading control and uniform higher remainder
remain unresolved. Continue only with a whole-operator or whole-sandwich
error, including boundaries; abandon an entrywise-only localization.

The supplied ready review supplies literature coverage. Checked the exact
L280(20) expression, L287's full proof and unfinished work, L286's exact
curl vertex, L283's polynomial approximation and L285's comparison and
local approximation. ATTEMPTS/047–049 remain preserved. L283 controls
local entries of a different approximation, not this two-vertex operator.

Proposed test, not yet a result: set M=m+1, use L283's geometric polynomial
h_m, and define G_m=C*C h_m(L)^2. This is a positive transverse covariance
below G, unlike relying on the old entrywise approximation. Couple x=y+z
with independent covariances G_m and R_m=G-G_m. Seek uniform diagonal
bounds R_m(e,e)=O(M^-1), (C R_m C*)(p,p)=O(M^-2), while
||G_m||<=M/16 and ||C G_m C*||<=1. The exact B(u;x) of L287 expands
into B(u;y), B(u;z) and the two mixed y/z terms. Schur-product estimates
using the small residual diagonal should control every term of the
difference of covariance operators by O(M^-1), even though the residual
curl operator itself is not small in operator norm. Orthogonality of the
independent Gaussian chaos components must be verified, together with
normal endpoints, color pairings, path range and source trace factors.

No claim yet of a bulk coefficient, convergence of M_3/N^2 or cancellation.
No new external theorem, source review or mathematical script is needed
for this finite-dimensional specialization of the existing inputs.

## Completed partial result

The proposed whole-operator estimate is proved in
[L288](../lemmas/L288-cubic-internal-curl-finite-range-approximation.md).
The positive residual has edge diagonal at most 960/M and curl diagonal
at most 122880/M^2, uniformly over even N and all relative rows. The
retained covariance has norm at most M/16. Independent Gaussian splitting
and the finite Schur-product inequality give
0<=E_N^int-E_{N,m}^int<=K/M, not merely entrywise convergence.
The source sandwich error is at most C_f N^2/M. The polynomial
construction has finite range and exact agreement with bulk rows whose
paths avoid the boundary. No hard tail of the original kernel is asserted
small without the replacement estimate.

Load-bearing checks in this attempt: the exact relative difference gives
|(Cv_{mu,k})_p|^2<=16 lambda_k/N^4 for each contributing component,
including endpoints; summing both components gives the stated curl
constant. The shell integrals bound sum r exp(-beta r^2) by 2/beta and
sum r^3 exp(-beta r^2) by 8/beta^2 for every beta>0, so no restriction
between m and N is hidden. Conditional expectation over the residual
Gaussian annihilates every remainder term, since the pure residual
quadratic has distinct colors. This proves the covariance difference is
positive and avoids an erroneous square-root error. The source factor
remains 3*2/4=3/2. These are proof checks, not a separate critical audit.

The approved full target is unfinished. L288 controls replacement in one
complete group but does not compute its bulk row-sum tensor, dispose of
the boundary layer in the source limit or evaluate a coefficient. The
two mixed insertion/action groups and distinct-line cubic group remain
open. No sign, compensation or uniform higher remainder follows.

Continue the unchanged approved target using the finite-range sandwiches:
test their bulk action on L282's actual strongly convergent source fields,
including their boundary norm, then control m->infinity with L288(4).
All tensor symmetries and slot phases must be checked rather than assumed
for the internal-curl piece in isolation. This is a possible next test
inside the prior scope, not a newly approved theorem. No route is declared
exhausted and no supervisor counter reset is claimed.
