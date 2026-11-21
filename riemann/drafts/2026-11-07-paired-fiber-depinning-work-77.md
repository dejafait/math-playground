# Finite depinning boundary test — working record

Status: completed; the initial pre-estimate checkpoint below is retained.

Step: 2026-11-07-paired-fiber-depinning-attempt-77.
Invocation-start coverage is the unchanged EXPLORE assessment
`literature/2026-11-07-paired-fiber-finite-replacement-test.md`.

The main gap is L030-L032/C032a actual-Xi all-degree mixed positivity.
The approved intermediate target is one finite two-fiber replacement
or an applicable boundary obstruction, retaining all collars and the
endpoint Jacobian. A strict decrease could exclude this conditional
configuration from a mass minimizer; existence and the other signs
remain independent gaps.

Read L847's actual form/pullback, L879's hypotheses and phase/variation
proof, L888 in full, and L887's hypotheses and crossing calculation.
The parent source comparison is reused. No additional browsing or
source import is needed for this application of the already assessed
boundary method. Existing changes are preserved.

## Attempt saved before completing the estimates

Test finite depinning with both components allowed in the interior.
At a contact fiber write z1=zeta, eta=z2, p=partial_1 u1,
k=partial_2 u2, a=v1, b=v2. The proposed exact trace primitive is

K(r,w)=C*G(zeta*exp(r))*G(w)*(zeta*exp(r)-w)^2
       /((zeta*exp(r))^2*w^2),
A(a,w)=integral_0^a K(r,w) dr.

L888(15) should reduce, with both side boundaries included, to
T=integral A(a,eta*exp(b))*(k+i+b') dy2.
The reduction must cancel, not discard, its mixed b*a' term.
Since K(0,w)=0, A/a^2 has a smooth extension using
integral_0^1 (1-t)*partial_r K(t*a,w) dt.

The signed quadratic coefficient predicted by the full Jacobian is
|partial_1 s|*(1-p^2)/(1+p^2)^2. Check this sign independently before
using it. On the explicit additional subclass |p|<=p_*<1 on both
fiber segments, compact derivative bounds may give a finite positive
trace cone in (a,b,b'), with no a' or interior derivative bound.
This would stop all admissible fillings of those traces, not merely
L887's fixed infinitesimal bump. The slope restriction is not known
for actual conditional data and must never be silently imposed.

Use the concrete field V=(chi,(y1-alpha)*(y1-beta)*chi), where chi
is a smooth bump spanning both fibers. Its first trace is nonzero;
its second trace is zero. Choose a positive finite amplitude from
both the trace bound and sup norm of H^{-1}DV to check endpoint J!=0.
Require a strict full-mass bound or retain the failed term explicitly.
All zeros and the entire cutoff region remain in L888's E>=0.

This is a finite boundary-calibration specialization, not a claim of
novel general mathematics. Nothing here establishes a stationary
configuration, a minimizer, sharp L868 equality, higher signs or RH.
The exact primitive, finite bound and endpoint remain to be checked
and written canonically; these working formulas alone are not evidence.

## Completed attempt

The full proof and all qualifications are now canonical in
`../lemmas/L889-finite-depinned-trace-boundary-mass-obstruction.md`.
The exact endpoint reduction cancels the mixed trace derivative by
the complete parameter-boundary identity. The predicted coefficient
has the stated sign. Compact derivative bounds give a finite positive
trace box when |partial_1 u1|<=p_*<1 on the two fibers. Its bound is
uniform over arbitrary admissible interior fillings, including collars.
The explicit coupled depinning field has a checked nonzero endpoint
Jacobian and strictly increases mass. Outcome NEGATIVE, classification
REPRODUCTION; this is not an independent audit or a novelty claim.

The extra slope and trace bounds are essential to the conclusion.
They do not follow from the conditional configuration. Preserve the
unrestricted finite target: a different second-component trace shear
outside that box still needs its complete phase-cost payment and
endpoint construction. No such shear has been calculated in this step.
