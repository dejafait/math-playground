# L118 — Every full-grid comparison diagonal vanishes exactly

## Hypotheses

Use L116's R_inf and R_prod, with L111's exact ordered transverse
endpoint/clover stencils T_r,C_r and A_r=D T_r C_r; L113's path
stencils S_alpha; and L110's unregularized energy kernel E_j. All
infinite-grid indices are the original lower-vertex indices. For the
finite comparisons retain SU(2), both actual L010 probes i=3,6,
straight lower-rooted direction-1 forest, relative all-face fixed-link
box (-4,4)^4, sufficiently fine admitted even N, a=8/N and tau=1/16.
Take the bare small-coupling coefficient at fixed mesh before refinement.
Keep both coefficient levels, both generator orientations, all path and
component filters, every pinned row and the complete exterior heat sum.

In particular import L116(4)--(5)'s exact diagonal formula, whose
coefficients are

    kappa_(alpha,beta,r;j)
      = integral tr[(S_alpha^inf)^* P_inf S_beta^inf A_r E_j]
                                                   dtheta/(2pi)^3. (1)

The integral is over [-pi,pi]^3, and j is any integer. The scalar
coefficient product in that formula is at a common lower-vertex index,
as specified in L116(1). No change to the original finite trace's
coefficient placements is assumed to have negligible cubic error.

## Conclusion

For every alpha,beta,r and every integer j,

    kappa_(alpha,beta,r;j)=0.                              (2)

Consequently, for both probes and every sufficiently fine admitted mesh,

    R_inf=0,          a^3 R_prod -> 0.                    (3)

No first-order local path correction survives in this particular
full-grid comparison. This strengthens L117's bound for R_inf, without
changing its valid bound for the actual transverse H trace. L110's
exterior-circulation remainder and L111/L113/L115's placement errors
are still merely O(N^3) and may carry the actual cubic coefficient.
There is no conclusion here about their limits, the actual transverse-H
limit, the full H diagonal's limit, or complete other/other compensation
against -12 gamma D_i. Other jets, finer powers/logarithm, matching,
interacting error <=c_box/2, continuum axioms, reflection positivity,
infrared control and finite positive mass remain unresolved.

## Proof

### 1. Match the component-center phases in the complete closed trace

Write theta=(theta_2,theta_3,theta_4), d_mu=2 sin(theta_mu/2),
eta_mu=cos(theta_mu/2), and lambda=sum_mu d_mu^2. Let U_1 be the
diagonal edge matrix with entry exp(i theta_mu/2), and U_2 the
diagonal plaquette matrix with entry exp(i(theta_mu+theta_nu)/2)
in plane pi=(mu,nu), mu<nu. Vertex phases need no change.
For a lower-vertex symbol O from q-cochains to p-cochains define
its centered symbol by O_c=U_p^* O U_q. These matrices are unitary
at each theta. Adjoints transform consistently, and all intervening
U_q U_q^* cancel in a closed product. Thus the trace in (1) equals
the trace of the corresponding centered product pointwise.
Periodicity of each individual centered entry is unnecessary: the
closed trace equals its original periodic trace.

The gradient has centered symbol i d, so

    (P_inf)_c=P_c=d d^T/lambda.                          (4)

In plane pi=(mu,nu) put z_pi=-d_nu e_mu^T+d_mu e_nu^T.
L110's incidence convention gives (D_c)_pi=i z_pi, since
exp(i theta_mu)-1=exp(i theta_mu/2) i d_mu. Hence

    (E_j)_c=r_lambda(j) D_c D_c^*                       (5)

is real and even under simultaneous theta -> -theta. Here
r_lambda(j)=exp[-2 asinh(sqrt(lambda)/2)|j|]/
[2 sinh(2 asinh(sqrt(lambda)/2))], exactly L110's multiplier.

### 2. Project each path stencil separately

Import L088(11)'s exact centered two-edge paths in plane pi:

    b_pi=eta_nu e_mu^T+eta_mu e_nu^T+i z_pi/2,
    q_pi=-eta_nu e_mu^T+eta_mu e_nu^T+i z_pi/2.         (6)

These identities retain all traversal signs and imaginary phases.
Let epsilon_pi be the coordinate column for that plaquette plane.
L113(1) therefore gives

    (S_(pi,b))_c=q_pi^* epsilon_pi^T,
    (S_(pi,q))_c=-b_pi^* epsilon_pi^T.                  (7)

Since d dot z_pi=0, P_c z_pi^T=0. Applying (4) to (7)
annihilates their entire imaginary parts separately. Consequently,
for every alpha, P_c (S_alpha)_c is a real matrix even under
simultaneous frequency reversal. Since P_c^*=P_c^2=P_c,

    (S_alpha)_c^* P_c (S_beta)_c
      =[P_c (S_alpha)_c]^* [P_c (S_beta)_c]              (8)

is also real and even, for arbitrary separate alpha,beta.
No relation between their scalar coefficients, levels or exterior
labels has entered this statement. It is stronger than the frozen
vector combination used in L117: projection removes the imaginary
path part before any such combination is taken.

### 3. Check each ordered endpoint/clover stencil

In L111's list, r selects displacement component rho, output edge
component nu distinct from rho, and plane pi with those two directions.
Let sigma_(rho,nu)=+1 if rho<nu and -1 if rho>nu, so that the
ordered curvature F_(rho,nu)=sigma_(rho,nu) F_pi.
L009(3)'s endpoint average takes the two vertex values at the ends
of the output nu-edge. Its centered symbol is eta_nu. The clover
average at a vertex takes the four pi-plaquette centers displaced
by (+/- e_rho +/- e_nu)/2; its centered symbol is eta_rho eta_nu,
with the ordered sign sigma_(rho,nu). Multiplication of these
two actual averages gives, for this individual r,

    (T_r C_r)_c
      =sigma_(rho,nu) eta_rho eta_nu^2
                                      e_nu epsilon_pi^T. (9)

Thus each individual stencil is real and even. The original
unequal output-component filters eta_nu^2 remain in (9).
There is no interchange of a component filter with P_c or E_j.
Combining (9) with the circulation row i z_pi shows that

    (A_r)_c=D_c (T_r C_r)_c                            (10)

is purely imaginary and odd under simultaneous frequency reversal.
This uses the fixed constant-coefficient stencil after L111's
displacement placement; no variable displacement is moved again.

### 4. Integrate the individual odd trace and return to the comparison

Equations (5),(8),(10), in their original matrix order, imply that

    g_(alpha,beta,r;j)(theta)
      =tr[(S_alpha)_c^* P_c (S_beta)_c (A_r)_c (E_j)_c]

is purely imaginary and satisfies g(-theta)=-g(theta).
The stencils are bounded on the torus and ||P_c||<=1.
Moreover L110's explicit formula gives ||E_j||_F<=C sqrt(lambda):
||D_c D_c^*||_F<=C lambda, exp(-kappa |j|)<=1, and
2 sinh kappa=2 sqrt(lambda) sqrt(1+lambda/4).
The trace integrand is therefore absolutely integrable, including
near lambda=0. One may assign arbitrary projection values at the
single zero-frequency point without changing its integral.
Changing variables theta -> -theta on the symmetric cube proves
that the integral equals its negative, hence is zero. This proves
(2) individually; it does not assert a pointwise-zero integrand.

Use L116's exact finite-rank diagonal formula. Every spatial
coefficient product multiplies one of the zero numbers (2), so
R_inf=0 exactly. No Taylor expansion, equality of s and t, extension
across the upper pinned jump, omission of a heat mode, or estimate
of a path-coefficient difference is required. L116 already justifies
the complete heat and level sums and the diagonal identity.
Finally L116(3) gives

    |R_prod|=|R_prod-R_inf|<=C_i N^3 eta_N,
    eta_N -> 0.

Multiplication by a^3=(8/N)^3 proves the second assertion in (3).
This removes the final retained comparison only. The earlier
O(N^3) errors have different, variable coefficient placements;
(8)--(10) do not give their limits or make them negligible.

This is local REPRODUCTION of finite-stencil Fourier phase conversion,
orthogonal projection and integration of an odd function under the
unchanged EXPLORE assessment
drafts/literature/2026-10-10-other-other-cubic-leading-scale.md.
The finite contraction, exact path and generator stencils, and
compression comparison are imported from the stated canonical inputs.
The necessary additional specialization is the individual projected
path identity (8) and individual ordered-generator parity (9)--(10);
the earlier frozen-vector cancellation did not state these. No
reproof of a source theorem, novelty claim beyond checked sources,
or complete Yang--Mills solution is made. No numerical check is used.

## Mathlib

Full matching exact diagonal vanishing: **not checked**. Supporting
unitary phase conjugation, orthogonal-projection identities and odd
integral vanishing: **not checked**. Unknown availability is not absence.
