# Direct positive-real preflight1800: working record

19 November2026. RESEARCH under the pre-existing SPECIALIZE assessment1799.
Target is exactly its eight-scalar, radius2^-8, total10^6-term preflight.
No transform evaluated. C033v and other existing work are preserved.

Main gap: L030-L032/C032a actual-Xi positivity. Possible downstream use
is C033w's fixed-three-width interpolation; conditioning, TV, the full
observation interval, signed height, cancellation and realization remain
open. Test: pay both Levy-time tails, direct compact quadrature, profiles,
every prime power, constants, rounding/exponentials and aggregate cost;
stop before evaluation if any allowance is unproved or over budget.

Read C033w's exact integrands; C033m's hypotheses/rescaling; C032s's
counting input and large-time argument; C033u's enlarged-width formula
and analytic Gauss/prime-tail proof; C033x and stops1781/1782. Reuse
source-notes1799; no essential source gap found. No new source import.
Retain every actual-divisor/heat/counting/fixed-v1 qualification1799.

Unfinished calculation: take a=2^-30,b=1/4, y=log t and
f(s,sigma,y)=sqrt(pi)*exp(-y/2)*(1-exp(-s*exp(y)))*F(sigma+exp(-y)/4).
The undifferenced f needs its own bound. Small-time counting integration
suggests a radius allowance below2^-11; large-time suppression follows
from gamma>14, through100 and the reciprocal-square tail. These bounds
are not yet certified in this working note.

Candidate compact evaluator: remove the archimedean removable singularity
with R(z)=exp(z/2)/(2*sinh(z))-1/(2*z), R(0)=1/4. Then the old combined
archimedean integral I(w) can be written I(1)-log(w)/4+J(w)-J(1),
J(w)=integral exp(-w*t^2)*R(t)dt. For positive real w, scale x=sqrt(w)t.
This is an algebraic specialization of C033u(5), not an RH-spectrum
replacement. Exact domination, branch, error and finite arithmetic work
remain to be completed. A finite quadrature-node count alone will not
be reported as a passed aggregate preflight.

Initial notebook-local git status was excessively large and truncated;
it supplies no mathematical evidence. Subsequent inspection is confined
to named relevant files. No sibling proofs or checkpoints read.

## Saved completion and remaining work

The tentative analytic calculation above is completed in canonical
[C033y](../lemmas/C033y-direct-positive-real-analytic-preflight.md).
Its regularization, cutoffs, exact residual domain, complex majorants,
adaptive prime tails and discrete weighted errors are proved there.
The rational certificate is
`scripts/smoothed-law/direct_positive_real_preflight_1800.json`.
The actual combined rational analytic upper bound is below2^-9;
the convenient allowance25/16384 leaves two proposed2^-10 arithmetic
allowances within the final2^-8 radius. The latter are UNPAID.

No finite-arithmetic evaluator or aggregate10^6-term certificate was
completed. The53320 named sampling/summation positions do not count
all elementary operations. In particular a stable, certified evaluation
of R at small positive arguments, Gauss nodes/weights, constants,
elementary-function errors and their full costs remain necessary.
No callback or scalar was evaluated. This is an analytic advance and
an unfinished full preflight, not a cost impossibility result.

Continuation uses unchanged assessment1799 and its exact target, now
with C033y's analytic input (audit pending). Develop the missing finite
arithmetic/cost contract; do not redo endpoint bounds or count a callback
as one term. Retain C032s, C033u/w and C033m/x qualifications and all
recorded earlier stops. Stop before evaluation unless that contract passes.
The central creative blocker in comparison1796 remains: no independently
supported signed-height upper estimate or representation was identified.
