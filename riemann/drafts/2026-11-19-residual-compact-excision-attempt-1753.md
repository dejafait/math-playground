# Residual compact-excision attempt1753

19 November 2026. Work under the unchanged SPECIALIZE assessment1752,
explicitly gate-approved in this invocation. Main gap is L030-L032/C032a
actual-Xi all-degree positivity. The intermediate target is an explicit
absolute-error evaluator for C033i's residual transform; its plausible
use is the residual side of a later finite-test range certificate.

## Saved reasoning before completion

C033i gives B_R(s)=B_1(s)-B_P(s) and Laplace(mu)(s)=exp(-B_R(s)).
The proposed change of variables is a(t)=1+1/(4t), so
ell_1(t)=sqrt(pi)*t^(-3/2)*p_a(t)(0). Here p_a(t) means p_{a(t)},
not evaluation at spatial argument t. On I=[1,3/2], the width lies
in [7/6,5/4], inside C032w's closed interval [1,2].

Plan: justify a uniform second derivative bound for the compact
integrand using the Gaussian heat equation and C032w's disk bounds;
import the assessed composite midpoint remainder. Pay profile errors
using C032w(6)-(7), finite node arithmetic separately, and B_1(s)
using C032w(12)-(13) at the positive square root. Combine both exponent
errors and propagate through exp using the known nonnegative residual
exponent. All choices must be ordered and explicit for arbitrary fixed
rational s>0 and absolute tolerance. No numeric evaluation is required.

Continue only if normalization, closed-domain uniformity, finite
arithmetic and ordered convergence all hold. Stop at the first failed
requirement. Existing stops1571/1576 concern independent boxes and
literal implementation cost, respectively, and remain intact. Inputs
are C033i, C032j/m/q/w with all inherited divisor, source and law
qualifications. No separator margin, continuum support-function bound,
signed cancellation, moments or Xi realization is presumed. Existing
unfinished C033k and all pre-existing notebook edits are preserved.

Completion and canonical result will be recorded below; this saved plan
alone is not a proof or verification.

## Completed attempt

The full specialization is now in
[C033m](../lemmas/C033m-effective-compact-excision-residual-laplace-enclosures.md).
The rescaling, summably dominated width differentiation and explicit
midpoint bound close the compact interface. C032w's full-exponent
errors are reused with separate coefficient and square-root arithmetic;
nonnegativity of the residual exponent bounds final exponential error.
The ordered procedure attains arbitrary absolute tolerance in principle.
No numeric implementation or practical runtime is claimed, and the
new application is pending independent audit. This is local progress
using known tools, not progress beyond their general theorems or an
RH resolution. The next audit is nominated separately; no second
mathematical attempt was made.
