# Bounded adjoint attempt1000 — preserved working checkpoints

The sole target is ready998's exact nomination997 test, with its original
eta_0, time interval, actual coefficients and first-lifetime convention.
The main gap is actual-Xi all-degree positivity. Paying this test would
give only one local initial-cycle comparison; global assembly and Xi
transfer remain independent.

Inputs inspected: C467a through audit997; C466y hypotheses, strict-buffer
proof and its cited complete-current conclusion; C466z hypotheses and
conclusion; C466 through its full cone proof. Reuse ready998/review998;
no new source theorem or source search is needed for the present test.
Stops961/968/979 are preserved.

Proposed discriminating argument, NOT YET ESTABLISHED: restrict to the
reflection-symmetric initial line u=(-r,0,r), 0<r<a. The actual real
Taylor coefficients give X=(p-iq,m,p+iq). The complete spatial
coefficient should be purely imaginary with positive -i multiple;
the real adjoint velocity should preserve that line. C466's survivor
matrix factorization J=(Z+iI)Q, ||Z||<=tan(40t), could control the
image q along an adjoint characteristic without defining any velocity
across a stop. Starting at r=31/1000 lies inside eta_0's positive set.

On a symmetric raw orbit, d=p-m and |d|<=tan(40t)q. Its exact imaginary
equation is q_t=-1/q-2q/(q^2+d^2)-Im b(p+iq), where
b(z)=B'(1+z)-x. Since b is real on the real axis and |b'|<40,
|Im b(p+iq)|<=40q. A comparison of this contraction with the much
smaller change of q along the real adjoint characteristic may force
r to approach a before T_0. Common compact support would then
contradict positivity propagated from eta_0.

Still to verify: exact reflection actions and all mixed signs;
nonzero coefficient and legitimate local velocity only on survivors;
quantitative normal-motion bound using all Jacobian components;
continuation of the selected characteristic, including no hidden
stopping event; the time-dependent tested identity with complete gamma
and a.e. raw-slice qualification; strictly positive initial signed mass.
A failed estimate will not prove incompatibility. No new lemma, final
obstruction or RH claim is asserted in this working note.

## Subsequent derivation checkpoint, before canonical write-up

The prospective contradiction now has explicit rational margins. On the
symmetric survivor line, reflection makes A purely imaginary and
rho=-iA>0. With c=J^{-1}V, all three mixed terms give
rho(eta_t-Re(c).grad eta); Re(c) is tangent to u=(-r,0,r).
For its characteristic u'=-Re(c), write J=(Z+iI)Q as in C466's
survivor proof. The image imaginary derivative is
Z(I+Z^2)^{-1}(Z Im(V)-Re(V)). This uses no quotient off survivors.

With k=tan(40t)<1/47, q between 1/40 and a, the full normal-motion
bound is |dq/dt|<=k^2((3+2sqrt(3))/q+40q)+40ak
<380/2209<1/5. Separately the raw symmetric equation gives
partial_t(q^2)<=-91/16+4/2209<-1137/200; raw norm and q both
decrease from their initial values. Thus, on a compactly supported
positive characteristic starting at r0=31/1000,
q>=r0-t/5 and q^2<=a^2-(1137/200)t. At T0 their required bounds
are incompatible: (1483/48000)^2-121/128000
=21289/2304000000>0.

The q lower bound exceeds 1/40 throughout, hence excludes collision
on every earlier raw segment (raw q decreases). Positivity of eta
would confine r to a compact subset of (0,a). The smooth local ODE
continuation theorem then extends this characteristic to every t<T0;
no regular lifetime or stopped-set velocity is used. This argument
and the complete time-dependent scalar weak balance still require
the canonical write-up and exact checks before the final checkpoint.

## Completion pointer

The full argument, hypotheses, qualifications and citations now reside
in [C467b](../lemmas/C467b-actual-h-compact-adjoint-symmetric-escape.md).
Seven exact rational checks passed in the arithmetic-only certificate
`scripts/adjoint-flux/symmetric-escape-1000.json`. The earlier unfinished
notes are preserved as checkpoints, not additional canonical results.
The completed step records an informative negative for the specified
test; independent conceptual audit of the new analytic argument is
pending. It is not an RH candidate or a source-approval step.
