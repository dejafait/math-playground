# Frozen double-zero audit — working950

Approved exact target: review948, separately approved in recovery949.
The main gap is actual-Xi all-degree positivity; this audit addresses
only the collision-weight objection. Stops927/932/941/947/948 retain
their scope. C466a/k/l motivate conventions and are not theorem inputs.

Preliminary calculation to check before canonicalization: writing
q=iy gives y'=-2/y, hence y=sgn(r)sqrt(r^2-4T), hit T=r^2/4.
At fixed T, J=i|r|/sqrt(r^2-4T). Thus the proposed signed density is
W=|r|sqrt(r^2-4T) before the hit, zero afterward, with envelope r^2.
The envelope should give uniform integrability on every measurable
set, not only near r=0. The total mass should be
2(a^2-4T)_+^(3/2)/3; outer endpoint motion prevents invariance.

Checks still to finish when this note was saved: real ODE uniqueness,
maximality, both orientation branches in change of variables,
zero one-sided weighted traces despite divergent J, fixed-time versus
composite variable-time differentiation, and precise source/Mathlib
qualifications. No actual-H perturbation is approved or derived.

Continuation test: explicit envelope or informative failure; abandon
this model as a singularity obstruction if the envelope is valid.
Any next regular-background target requires separate source assessment.

Completed950: the checks above are resolved in the canonical result
C466q, including both oriented changes of variables, explicit mass,
the arbitrary-measurable-set bound and the fixed/scaled-time distinction.
The working calculation is preserved as saved; its tentative status
is superseded by that full proof. No actual-H calculation was made.
