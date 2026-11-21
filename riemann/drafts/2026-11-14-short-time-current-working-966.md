# Short-time current attempt966 — saved reasoning

Approved target: assessment964, separately approved by repair965. Inputs
read: C466s (including audit959), C466t's exact counterexample and audit
evidence, working961 and source statements retained in reviews960/964.
No new source coverage or changed hypotheses are needed. Main gap remains
actual-Xi all-degree algebraic-square positivity; this attempt concerns
only one local boundary identity. Preserve all earlier stops.

Promising argument, not yet claimed as a theorem:

- On survivors rho'=(-2+Re(q H_q))/rho <= M_1, while |z'|<=M_1.
  Thus the strict buffer should exclude both outer boundaries up to T_0.
- The autonomous velocity V and both parameter tangents solve the same
  real variational system. For exterior degrees two and three the singular
  real Hessian has top-eigenvalue sum 2/rho^2. Combining with F'=-|f|^2 F
  should give |F| times each complete area/volume bounded by its initial
  value times exp((k M_2+M_1^2)t). Initial mixed areas and triple volume,
  after multiplication by |F_0|, are at most C(2|r|+M_1 r^2).
- Use a cutoff theta(rho/epsilon) with transition epsilon<rho<2epsilon.
  If 2epsilon M_1<=1, (rho^2)'<=-2 in this small region. A trajectory
  traverses the shell at most once, for time <=3epsilon^2/2. A three-volume
  cutoff bound O((2|r|+M_1 r^2)/epsilon) then has total flux O(epsilon).
- A separate cutoff at |r|=delta has flux using only beta_ts; its O(|r|)
  envelope gives O(delta). It may be unnecessary: small initial r collide
  in O(r^2) time, so positive compact time support has no survivors near
  r=0. Either assertion needs a full argument.
- Critical remaining topological issue: prove cutoff supports stay locally
  inside the survivor domain. A survivor with current rho>epsilon cannot
  previously have entered rho<=epsilon, by the inward barrier. Together
  with uniform outer margins this should rule out an earlier-collision
  shadow. Compact ODE continuation, not a regular lifetime surface or
  post-exit flow, is the intended justification.

Next in this same bounded attempt: justify that support claim, write every
complete coefficient and cutoff estimate with orientations, and pass to
the inhomogeneous distributional identity. Failure of an estimate alone
would not refute the target. No lemma or audit has yet been completed.

Resolution of the remaining support issue: if surviving p_n approach a
point p outside D_H while rho(p_n)>epsilon, the inward barrier forces
their whole earlier paths to have rho>epsilon. The outer buffer confines
those paths to one compact subset of U. Also |r_n|>epsilon, so r at p
is nonzero. Continuous dependence on each compact surviving segment of
the limiting initial path puts that path in the same compact set up to
min(t,tau). If tau<=t, compact continuation contradicts maximality.
Thus p is a survivor, a contradiction. The cutoff's nonzero set is
therefore locally separated from the nonsurvivor set, including r=0.
Its zero extension and the cutoff forms are smooth without a lifetime
surface or post-exit map. A separate initial-axis cutoff is unnecessary.

Completion being written in C466u: all beta coefficients and gamma have
global finite envelopes, and the full cutoff error is at most
(9/2)||phi||_infinity ||chi||_infinity ||theta'||_infinity E epsilon
times integral_I(2|r|+M_1 r^2). The shell-length bound is 3epsilon^2/2.
Dominated convergence then gives d bar(beta)=bar(gamma). This is one
local mathematical advance, not a signed-integral or positivity result.
Independent conceptual audit remains pending; no new source theorem
or homogeneous removability assertion has been used.
