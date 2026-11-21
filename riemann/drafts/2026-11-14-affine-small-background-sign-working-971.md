# Affine small-background sign attempt971

Approved target: assessment969's degree-at-most-two negative-weight test.
Chosen mechanism: H(q,z)=H_0+Aq+Bz, H_0 real and A,B arbitrary
complex. This tests collision amplification from constant complex drift;
it does not impose a reality symmetry. No quadratic mechanism is being
attempted in this step. Essential local input: C466s's raw flow,
fixed-time variational convention and dot F=-||f||^2 F. C466u supplies
the imposed buffer only, not a sign input.

The main gap is actual-Xi all-degree algebraic-square positivity.
A negative witness would disprove the proposed local sufficient sign
condition; an affine obstruction would stop this specific search while
leaving quadratic/coupled backgrounds and Xi/global assembly open.
Continue only for a rigorous witness, relevant estimate or informative
ansatz obstruction. No sampled phase is a sign certificate.

Saved partial reasoning before proof completion:

- q'=-2/conj(q)+conj(A); z=s+conj(B)t. The fixed-time Jacobian
  is diag(u,1), with u=q_r and u'=2 conj(u)/conj(q)^2, u(0)=i.
- With rho=|q|, rho'=-2/rho+Re(A exp(i theta)). Put
  epsilon=M_1 sqrt(a^2+b^2)<=1/100. Since |A||r|<=epsilon,
  rho ought to decrease throughout survival. Then
  integral_0^t rho^(-1)dv <= (|r|-rho(t))/(2-epsilon).
- A continuous trajectory angle theta has drift delta from its initial
  value +/-pi/2 bounded by epsilon/(2-epsilon)<=1/199.
- Write u/i=|u| exp(i alpha), alpha(0)=0. The real variational
  equation should give alpha'=-(2/rho^2)sin(2(alpha-delta)).
  A scalar invariant interval would confine alpha to [-1/199,1/199].
- F retains its initial phase. Consequently W has phase alpha minus
  Im(iAr+Bs), whose absolute value would be <=1/199+1/100<pi/2.

Unresolved at this checkpoint: verify the decreasing-radius barrier,
nonvanishing u, angle lifts for negative r, invariant interval at its
endpoints, first-lifetime/buffer scope, and every inequality above.
If valid, this rules out all affine witnesses, not all degree-two
witnesses and not the general holomorphic conjecture. No numerical
script or claim of originality is intended.

Completion971: all the listed proof checks were resolved in the
canonical C466v proof, including negative r and equality at the angle
barriers. The affine ansatz cannot yield a negative witness under the
approved bounds. This saved reasoning remains a chronological work
note; the full statement, proof and qualifications are in
[C466v](../lemmas/C466v-affine-small-background-survivor-sign.md).
No quadratic calculation was performed. PROGRESS.md holds the sole
current continuation; independent audit of the new proof is pending.
