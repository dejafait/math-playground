# L107 — A finite cubic limit for the co-closed-base reverse trace

## Hypotheses

Keep exactly L105–L106's R_R and R_(i,N;epsilon,eta): SU(2), both
actual L010 probes i=3,6, straight lower-rooted direction-1 forest,
relative all-face fixed-link box D=(-4,4)^4, admitted even N,
a=8/N, tau=1/16, and the bare small-coupling coefficient at fixed
mesh before refinement. Coordinates and norms are ordinary stored
ones. Every interior axial level, transverse end row and exterior
heat mode is retained. This is distinct from L104's gradient-base G_R.
There is no outside factor 3 in R_R.

Use L105's T, Delta_0, Delta_T, P,Q, W_t, Omega_k, S_st and
c_(i;kl,a). Let c_(i;kl) and v_k be the actual continuum exterior
coefficients and forest mode functions specified in L080 and L104(1).
For theta in [-pi,pi]^3 import the raw tail-indexed symbols
from L104(3)–(5): tau_mu=1-exp(i theta_mu),
lambda=sum_mu |tau_mu|^2, circulation matrix c(theta), path rows
b,q, and z_k=z_(v_k). The lowercase matrix c(theta) is distinct
from the scalar exterior coefficients c_(i;kl). Explicitly, mu<nu,

    c_(mu nu)=(1-exp(i theta_nu)) e_mu^T
                              +(exp(i theta_mu)-1) e_nu^T,
    b_(mu nu)=e_mu^T+exp(i theta_mu)e_nu^T,
    q_(mu nu)=-exp(i theta_nu)e_mu^T+exp(i theta_mu)e_nu^T,
    (z_k)_(mu nu)=(v_(k,mu)+v_(k,nu))q_(mu nu)
                                  -(v_(k,nu)-v_(k,mu))b_(mu nu),
    w_mu=-u_1(x)[(1+exp(i theta_mu))/2] i sin(theta_mu).

Define, for lambda>0,

    p=tau tau*/lambda, q0=I-p,
    omega_k=z_k* c-c* z_k,
    alpha_k=p omega_k q0, beta_k=q0 omega_k q0.          (1)

Stars denote complex adjoints. All quantities are evaluated at the
same (x,theta); tau,c depend only on theta. Set subsequent integrands
to zero at lambda=0, a measure-zero point.

## Conclusion

For both probes there is a finite real, absolutely convergent functional

    K_(i,R)=(1/2) sum_(k,l)c_(i;kl) integral_D
       integral_([-pi,pi]^3) lambda^-2
          tr[q0 alpha_k* tau w* beta_l]
                                     dtheta/(2pi)^3 dx,             (2)

and

    a^3 R_R -> K_(i,R).                                  (3)

In particular each fixed-epsilon trace a^3
R_(i,N;epsilon,epsilon^2) has a limit. Both displayed coefficient
levels and the triangular diagonal half-weight survive the controlled
approximation; the factor 1/2 in (2) is that half-weight plus the
symmetric off-diagonal axial sum, not a new color or cumulant factor.

The value and sign of K_(i,R) are unevaluated. Transverse R_H,tr still
lacks cubic control. The E, H axial, H curvature, gradient-base and
reverse functionals remain unevaluated; their joint value must be
-4 gamma D_i before the outside factor 3 to compensate L084. Finer
powers/logarithm, other response jets, matching, interacting reflected
error <=c_box/2, continuum axioms, reflection positivity, infrared
control and finite positive mass remain independent gaps. No candidate
Yang–Mills solution or complete other/other limit follows.

## Proof

### 1. Normalize only after importing the actual reverse order

Import L106(1) and its uniform O(N^2) exterior-circulation removal.
We can therefore replace both Omega by Omega^0=Zeta^T D_T-D_T^T
Zeta at cubic scale. Put O_(k,a)=Omega_k^0/a and
A_(k,a)=P O_(k,a) Q, H_(l,a)=Q O_(l,a) Q. With
R_ts^epsilon=[(L_D tensor I+I tensor Delta_T+epsilon I)^-1]_ts
and G_eta=(Delta_0+eta I)^-1 the exact normalized trace is

    a^3 R^0_(i,N;epsilon,eta)
      =a^4 sum_(k,l)c_(i;kl,a) sum_(s,t) S_st
          Tr[R_ts^epsilon Q A_(k,a)(s)^T
                                  T G_eta W_t^T H_(l,a)(t)].       (4)

The two Omega factors contributed a^2; the original prefactor was
a^-1. Thus a^3 gives precisely a^4 in (4). No ordered-pair convention
or outside factor is changed. L105(10)–(12) and L106 section 4 give

    ||O_(k,a)||<=C p(k), ||W_t||<=C,
    ||T G_eta W_t^T||<=C,
    sum_(s,t)||R_ts^epsilon||<=n/epsilon, n=N-1.         (5)

The last estimate follows from L106(9)'s scalar domination by the
entry R_ts(epsilon), followed by its row-sum bound. It also applies
to the full transverse inverse before Q is inserted: the scalar
transverse eigenvalues are nonnegative. All heat coefficients have
L080(6), L104(15)'s summable majorant, with any fixed enlarged mode
polynomial p, and converge pairwise to c_(i;kl). These facts already
bound (4) uniformly at fixed epsilon,eta, using transverse dimension
at most C N^3 and a^4 n N^3<=C.

### 2. Approximate projections in Hilbert–Schmidt norm

For 0<delta<=1 put P_delta=T(Delta_0+delta I)^-1 T^T,
Q_delta=I-P_delta. Substitute P_delta,Q_delta for every displayed
P,Q in (4), including Q after R_ts^epsilon. Do not simplify using
idempotence: P_delta,Q_delta are positive contractions, not projections.
By L085's intertwining Delta_T T=T Delta_0 they commute with each
R_ts^epsilon, although they are never commuted through coefficients.

On one layer the nonzero singular values of E_delta=P-P_delta
are delta/(lambda_v+delta), one per pinned transverse vertex mode.
L103(16)'s full vertex shell estimate therefore gives, for
N sqrt(delta)>=1,

    ||E_delta||_HS<=C N^(3/2) delta^(3/4).              (6)

There is no vertex zero mode. The same difference controls Q.
Telescope all finitely many substituted factors. For each (s,t),
use |Tr(X E_delta Y)|<=sqrt(dim_T)||X||||Y||||E_delta||_HS,
and ||R_ts^epsilon||<=R_ts(epsilon). Bounds (5) control all
remaining factors; each exterior occurrence contributes p(k) or p(l).
After summing the scalar majorant, (6) and the heat series, the
normalized projection error is at most

    C_(i,epsilon,eta) a^4 n N^3 delta^(3/4)
                         <=C'_(i,epsilon,eta) delta^(3/4).          (7)

If E_delta occurs after the covariance, the identical estimate follows
by cyclic trace duality. Thus (7) handles every occurrence without an
operator-norm-smallness claim. For each fixed delta the condition in
(6) holds eventually; (7) supplies the required uniform limsup error.

### 3. A block-norm polynomial approximation also localizes axially

An ordinary full-matrix operator error alone is insufficient here:
(4) sums n^2 layer pairs. We instead control the sum of block norms.
The exact finite spectra satisfy 0<=Delta_T<=12I and 0<=L_D<=4I.
Let J=2I-L_D, the nonnegative axial adjacency matrix, whose row sums
are at most 2, and C_T=14I-Delta_T, a positive transverse matrix
with ||C_T||<=14. Define

    B=(J tensor I+I tensor C_T)/(16+epsilon),
    r_(epsilon,m)(L)=(1/(16+epsilon)) sum_(j=0)^m B^j,
    L=L_D tensor I+I tensor Delta_T.

Here I-B=(L+epsilon I)/(16+epsilon). Its spectral radius is at
most rho=16/(16+epsilon)<1, so the full inverse is the infinite
geometric series. Since the two tensor summands commute,

    (B^j)_ts=(16+epsilon)^-j
       sum_(h=0)^j binom(j,h)(J^h)_ts C_T^(j-h).

Every scalar (J^h)_ts is nonnegative, and
sum_(s,t)(J^h)_ts<=n 2^h. Taking transverse operator norms and
summing proves

    sum_(s,t)||(B^j)_ts||<=n rho^j,
    sum_(s,t)||R_ts^epsilon-[r_(epsilon,m)(L)]_ts||
                              <=n rho^(m+1)/epsilon.               (8)

This uses no sign of a coefficient or trace, no transverse entrywise
positivity, and retains both pinned axial ends. Applied to (4) with
regularized projections, (8), trace dimension and the bounded factors
give error at most C_(i,epsilon,eta) rho^(m+1), uniformly in N,delta.
The degree-m covariance has axial range m. Thus axial localization
has been justified before any freezing or prefix replacement.

For fixed epsilon,eta,delta approximate G_eta and
(Delta_0+delta I)^-1 in P_delta uniformly on [0,12] by

    p_(h,b)(x)=(1/(12+h)) sum_(j=0)^b
                         [1-(x+h)/(12+h)]^j,
    sup |p_(h,b)(x)-(x+h)^-1|
                            <=(12/(12+h))^(b+1)/h.                 (9)

The geometric identity proves (9), and finite spectral calculus gives
the operator estimate. These are bounded finite-range transverse
stencils, including their boundary rows. Product telescoping, (5),(8)
and a^4 n N^3<=C show that their errors vanish uniformly in N at
fixed masses. Constants may depend on those masses. These operations
remain valid after the covariance polynomial substitution, because
its summed block norms are at most n/epsilon by the same series bound.

### 4. Compute the fixed-range limit with the triangular weight intact

First fix all masses, degrees and one exterior pair k,l. The resulting
trace is a finite sum of closed transverse walks and axial offsets
d=s-t of bounded size. W_t restricts nonzero walks to a fixed compact
physical interior for sufficiently fine N. Independently, a collar
wider than the fixed stencil range has O(N^3) rows in four dimensions,
and only finitely many offsets per row. Its normalized contribution
is O(a^4 N^3)=O(N^-1), by the bounded coefficients. This accounts for
all pinned end cases; no boundary value is silently substituted.

For interior walks L080(5),(8)–(10) proves convergence of the actual
forest exterior link divided by a to v_k, with its full lower prefix
and constant axial mode. At s,t separated by a bounded offset this
convergence is to the same smooth physical sample. Raw link samples,
rather than only their opposite-edge averages, have the same limit:
the exact incidence difference of the smooth prefix converges to its
transverse derivative, and the direct staggered sample converges to
A_k. L028(3)–(4) controls these differences and the actual u_a.
Consequently Zeta_k/a converges to z_k in the stated raw path
convention, and O_(k,a) converges to omega_k. Uniform bounds are
(5); coefficient changes over fixed walks tend uniformly to zero on
that compact region. Both original axial coefficient levels are kept
until this controlled step.

Freeze coefficients at their common cell point only now. The finite
closed-walk trace is the zero transverse Fourier coefficient of its
symbol product, since integration of exp(i b.theta) selects exactly
b=0. The transverse Hodge symbol is lambda I: expanding
TT^T+D_T^T D_T with the displayed incidence and circulation symbols
cancels its off-diagonal entries and leaves sum_mu |tau_mu|^2 on
each diagonal. Thus the frozen covariance polynomial has axial Fourier
symbol

    r_(epsilon,m)(2-2 cos(phi)+lambda) I.

Write its finitely many axial coefficients as r_d(lambda), so
r_d=r_(-d), because that symbol is real and even in phi. In (4)
S_st=1_(d>0)+delta_(d,0)/2, hence exactly

    sum_d S_(t+d,t) r_d(lambda)
       =(1/2)sum_d r_d(lambda)
       =(1/2)r_(epsilon,m)(lambda).                   (10)

The finite end exceptions were bounded by the collar estimate.
Equation (10), rather than omission of the diagonal or replacement of
a macroscopic prefix, is the axial half-factor in the limit. All other
stencils in this trace are level diagonal. No axial derivative has
been assigned to a frozen coefficient.

The remaining a^4 cell sum tends to the integral over D. Removing
polynomial errors through (8)–(9) gives the fixed-mass, fixed-delta
limit

    K_(i;epsilon,eta,delta)=(1/2)sum_(k,l)c_(i;kl) integral_D
       integral tr[(lambda+epsilon)^-1 q_delta
          (p_delta omega_k q_delta)*
          tau (lambda+eta)^-1 w* (q_delta omega_l q_delta)]
                                              dtheta/(2pi)^3 dx,   (11)

where p_delta=tau tau*/(lambda+delta), q_delta=I-p_delta.
For each fixed exterior pair this follows from the walk argument.
The global bound (5), its polynomial counterparts and L104(15)'s
summable heat majorant justify first uniform exterior-tail removal
and then fixed-pair convergence. Thus every heat mode, both actual
probe forms and every displacement transition are included in (11).
No finite-mesh extrapolation is used.

### 5. Remove projection and inverse regularization in that order

At fixed epsilon,eta the integrands in (11) are dominated by a
summable mode majorant times a finite mass-dependent constant;
p_delta,q_delta are contractions. Dominated convergence as delta
falls to zero gives K_(i;epsilon,eta,0), with p,q0 in their places.
Using (7) and the fixed-delta trace limit establishes the actual
fixed-epsilon,eta limit of (4). L106's O(N^2) comparison restores
both full Omega occurrences at zero scaled cost.

The final symbol is uniformly integrable even as epsilon,eta decrease.
The raw formulas and smooth bounded coefficients give

    ||omega_k||<=C p(k) sqrt(lambda),
    ||tau||=sqrt(lambda), ||w||<=C sqrt(lambda).

The first estimate follows from ||c||<=C sqrt(lambda) and bounded
z_k; the last from the exact endpoint filters and
sin^2(theta_mu)<=|tau_mu|^2. Therefore the absolute trace integrand
with p,q0 is at most

    C p(k)p(l) lambda^2/[(lambda+epsilon)(lambda+eta)]
                                                   <=C p(k)p(l).  (12)

The physical volume is finite and the heat majorant is summable.
Dominated convergence with eta=epsilon^2 identifies its limit as (2)
and proves absolute convergence. Conjugation under theta -> -theta
leaves all real-stencil symbols conjugated, so the integral and series
are real; equivalently they are limits of the real finite traces.

Finally L106(3) gives, for every fixed epsilon and sufficiently large N,

    |a^3 R_R-a^3 R_(i,N;epsilon,epsilon^2)|
                                      <=C_i sqrt(epsilon).         (13)

Combine the fixed-mass trace limit, (12) and (13), first taking N to
infinity and then epsilon down to zero. This proves (3). There is no
mesh-dependent mass choice, unproved local prefix replacement or
termwise projection commutation. In particular the operator obstruction
L094 and the transverse-H mass-removal obstruction L099 remain intact.

This is a standard finite-matrix approximation argument applied in the
previously unresolved reverse order under the unchanged complete-group
EXPLORE assessment. L048 is not rederived, and no finiteness theorem for
a complete flowed Ward response is assigned to this isolated group.
The outcome is local progress, classified REPRODUCTION, with no claim
beyond sources checked. No numerical script or IEEE assumption is used;
L082's qualifications remain attached to future comparison with D_i.

## Mathlib

Full matching reverse-trace limit and its specialization: **not checked**.
Supporting finite spectral calculus, geometric inverse series,
Hilbert–Schmidt trace duality, Fourier coefficient and dominated
convergence coverage: **not checked**. Unknown availability is not
absence. The local inputs are explicitly identified above; no external
Yang–Mills construction theorem is invoked or reproved.
