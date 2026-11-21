# Common-eta obstruction working note — step198

Completed after this checkpoint: the full proof is canonical in
`lemmas/L973-rh-conditional-common-eta-convexity-obstruction.md`.
The pending qualifications below describe the saved intermediate state,
not additional current tasks. Independent conceptual audit remains due.

Checkpoint before completing the approved mathematical attempt. The target
and prior EXPLORE coverage are unchanged from
`literature/2026-11-10-fixed-eta-second-difference-review-196.md`.

From L964's unconditional rational identity, with
x(z)=(1-z/4)/(1+z/4), the proposed complete difference is
2 sum_j beta_j^2 T_n(x(beta_j))/((beta_j+u)(1+beta_j/4)).
All three Q terms must use the same u=eta_n; fixed-n convergence
uses L024/L026 and L964's analytic bound, without a theta formula.

Under the explicit diagnostic RH assumption, beta_j>0 and
theta_j=2 atan(sqrt(beta_j)/2) lies in (0,1/4). Put
c_j=2 beta_j/(1+beta_j/4). Then S(n)=sum c_j cos(n theta_j)
has uniform absolute tails, zero one-sided Cesaro mean, and positive
mean square V=(1/2)sum_theta (sum_{j:theta_j=theta} c_j)^2.
L021 makes Xi nonconstant; L024 then implies a nonempty node set.
This avoids importing any numerical zero data.

The full error is bounded by sum c_j u/(beta_j+u), uniformly in n.
For a finite head of J nodes this is at most 2Ju plus twice the
remaining beta mass, hence tends to zero with u. To prove arbitrarily
large negative margins directly, let M=sum c_j and delta=V/(4M).
If S(n)>=-2delta eventually, (S+2delta)(M-S)>=0 and Cesaro
averaging imply V<=2delta M=V/2, a contradiction. Thus infinitely
many S(n)<-2delta, and the vanishing eta_n error should give
differences <-delta for infinitely many n. Full proof, sums, constants,
scope and citation comparison are still to be written canonically.

No unconditional actual-Xi negative value or RH resolution follows.
The next step after completion should independently audit the conditional
obstruction, especially the nonresonance and complete regularization
error, before choosing a different constructive sign mechanism.
