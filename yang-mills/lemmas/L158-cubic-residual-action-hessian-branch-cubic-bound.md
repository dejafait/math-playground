# L158 — Action-Hessian covariance collapse and a cubic bound

## Hypotheses

Keep all hypotheses of L156 and L157: SU(2), the relative box
(-4,4)^4, admitted even meshes a=8/N, straight direction-1 lower-rooted
forest, the complete compact displacement and both actual L010 probes
at tau=1/16. Take the bare expansion at fixed mesh first. Full-link
Taylor tensors precede covariance splitting. All action plaquettes,
both residual insertion subtractions, three colors, the upper pinned
jump, constant axial prefix and exterior heat modes remain.

Use L156's ordinary-coordinate A,L,Sigma,R,Phi,K,C_g,E and heat
coefficients c_(i;kl), with h_k=R v_k. Use L157's B_h and hats for
three-color diagonal extensions. Split its retained J_i into exactly
its two action terms:

    T_i=-sum_(k,l,c) c_(i;kl)
          Tr[Ahat B_(h_k t_c) Khat B_(h_l t_c)^T Lhat Ehat],
    V_i=+sum_(k,l,c) c_(i;kl)
          Tr[Ahat B_(h_k t_c) Khat B_(L h_l t_c)^T Ehat].    (1)

Thus J_i=T_i+V_i. This is an algebraic decomposition of a signed
contraction; E is not asserted positive or independent of the prefix.

## Conclusion

The exact action-Hessian cancellation and remaining covariance order are

    L E A=A,                    E A=R Sigma A,
    T_i=-sum_(k,l,c) c_(i;kl)
             Tr[Ahat B_(h_k t_c) Khat B_(h_l t_c)^T],
    V_i=+sum_(k,l,c) c_(i;kl)
             Tr[Sigmahat Ahat B_(h_k t_c) Khat
                         B_(L h_l t_c)^T Rhat].           (2)

For each actual probe there is a mesh-independent constant with

    |T_i|<=C_i N^3.                                      (3)

Consequently the complete target is reduced only to

    H_i=T_i+V_i+H_i^EE+O_i(N),                            (4)

where H_i^EE is L156's complete two-remainder sector. This bounds one
complete branch and removes a coarse covariance-norm loss in it. It
does NOT establish a limit or vanishing for a^3 T_i, a bound for V_i
or H_i^EE, or cubic boundedness of H_i. The requested zero limit needs
o(N^3), whereas (3) supplies only O(N^3). First-order coefficient and
exterior differences and the local covariance slope may still contribute.
No full compensation, finer powers/logarithm, interacting reflected
error <=c_box/2, continuum construction or mass gap follows.
This is local progress by finite matrix, scalar Green and stencil methods;
no originality beyond the unchanged assessed sources is claimed.

## Proof

### 1. Cancel the Hessian before estimating the signed remainder

L157 proves E L=R Pi with Pi=Sigma L the symmetric co-closed
projection. Since A is symmetric and A D_0=0, R^T A=A. Also
Pi A=A: Delta A=L A because D_0^T A=0, so multiplying by
Sigma gives Sigma L A=A.
Transposing the first identity yields

    L E A=Pi R^T A=A.

L157's exact expansion E=Sigma-D_0 Phi Sigma-Sigma Phi^T D_0^T
instead gives E A=(I-D_0 Phi)Sigma A=R Sigma A. Cycle the finite
traces in (1) to put L E A or E A together. This proves (2), with
no multiplication of E as if it were a covariance of independent noise.
The full-link gauge annihilation is essential; no forest-row tensor
is discarded before these identities.

### 2. The local prefix kernel: stationary growth plus a scalar constant

Fix a compact enlargement of the support of A. Its stencil radius is
fixed, so every endpoint there has distance at least delta N from all
faces for sufficiently large N. In L156(6), let Delta_0 be the
unscaled three-dimensional scalar Dirichlet Laplacian, G=Delta_0^-1,
and R_st(lambda)=[(L_D+lambda)^-1]_st. For interior vertices with
axial coordinates s,t and transverse coordinates y,z, exactly

    K((s,y),(t,z))=min(s,t)G(y,z)-F_N((s,y),(t,z)),
    F_N((s,y),(t,z))=(R_st(Delta_0)G)_(y,z).               (5)

All axial and transverse modes, including the constant axial edge
mode used to obtain (5), are retained.

We first establish the scalar Green comparison needed here, rather
than inferring it from a gradient-projection comparison. On Z^3 set
lambda(theta)=4 sum_(j=2)^4 sin^2(theta_j/2) and

    g(n)=(2 pi)^-3 integral_[-pi,pi]^3
                         exp(i n dot theta)/lambda(theta) dtheta.

The integral is finite since lambda is comparable to |theta|^2 near
zero. The heat representation of 1/lambda gives g>=0 and
Delta_inf g=delta_0. Also

    |g(n)|<=C/(1+|n|).                                   (6)

Here is a direct estimate for (6). For r=|n|>=2 choose a smooth cutoff
on |theta|<=2/r, equal to one on |theta|<=1/r. The integral of its
1/lambda part is O(1/r). For the complementary part integrate twice
by parts in a coordinate with |n_j|>=r/sqrt(3). On the punctured
torus the first and second derivatives of 1/lambda are bounded by
C|theta|^-3 and C|theta|^-4 near zero, and bounded elsewhere. The
L1 norm of the complementary second derivative is O(r): cutoff
second-derivative and cross terms have that same bound on the annulus,
and integral_(1/r<|theta|<1)|theta|^-4 dtheta=O(r).
Periodicity cancels the outer integration-by-parts terms. Multiplying
by n_j^-2 proves O(1/r); boundedness of g handles the remaining n.
This argument uses no bounded infinite inverse on arbitrary l2 inputs.

For fixed z inside the transverse cube, g(y-z)-G(y,z) is harmonic
in its interior and equals g(y-z) on its boundary. The finite maximum
principle (at a maximum a harmonic value is the average of its six
neighbors, propagated to the boundary) and (6) therefore give

    0<=g(y-z)-G(y,z)<=C_delta/N                           (7)

when z is at distance delta N from the boundary. In particular every
local G entry is bounded uniformly. This proves the needed comparison
on all local rows without claiming a global norm approximation.

The second term in (5) has the following uniform estimates:

    |F_N(v,w)|<=C(1+log N),
    |F_N(v+one step,w)-F_N(v,w)|<=C,                     (8)

and likewise for a step in the second argument. To prove these,
use L026's complete normalized transverse sine modes psi_q. Their
entries are bounded by C N^-3/2 and a one-step transverse difference
by C N^-3/2 sqrt(lambda_q). With r=max q_j, the eigenvalue is at
least 4 r^2/N^2 and the shell has at most C r^2 labels.
The one-dimensional killed resolvent is bounded by the full-line
resolvent diagonal:

    0<=R_st(lambda)<=1/sqrt(lambda(lambda+4))<=C/sqrt(lambda).

This follows either from its positive heat kernel or the positive
solution of the tridiagonal recurrence; killing deletes walk paths.
Thus the absolute mode sum for F_N is bounded by
C N^-3 sum_q lambda_q^-3/2<=C sum_(r=1)^(N-1)1/r.
A transverse difference instead has bound
C N^-3 sum_q lambda_q^-1<=C, proving that part of (8).

An axial first difference of R_st(lambda) is bounded by one. For
fixed t its positive solution is proportional to sinh(kappa s) for
s<=t and sinh(kappa(N-s)) for s>=t, with
2 cosh(kappa)=2+lambda. Hence its left slopes are nonnegative and
increase toward t, while right slopes are nonpositive and their
magnitudes are largest next to t. The recurrence at t says the
left slope minus the right slope is 1-lambda R_tt<=1. Each of
those two nonnegative magnitudes is therefore <=1, as are all
other adjacent slopes. An axial difference in the spectral sum
is consequently bounded by C N^-3 sum_q lambda_q^-1<=C.
Symmetry gives the second-argument estimates. The full shell sums
prove (8) uniformly, including low modes and every finite boundary row.

Choose a reference interior vertex v_e within a fixed number of
steps of the midpoint c_e of an output edge e, and put
alpha_e=F_N(v_e,v_e). On the complete local A stencil, (8) gives
F_N(v,w)=alpha_e+O(1). Put j_e equal to the axial lattice coordinate
of c_e (half-integers are allowed). Then min(s,t)-j_e=O(1), and
(6)--(7) prove the local entrywise identity

    K(v,w)=j_e g(y-z)-alpha_e+O(1),
    |alpha_e|<=C(1+log N).                               (9)

This estimate is only for bounded offsets within that stencil; it
does not approximate the whole forest covariance. It retains the
logarithmic potential term rather than silently calling it bounded.

### 3. Color contraction and removal of the local constant

Let S be the endpoint-sum incidence from vertices to links,
(S phi)_e=phi(tail e)+phi(head e), and put K^+=S K S^T.
For a one-color link column h let M_h denote its diagonal matrix.
For fixed exterior color c, B_(h t_c)=M_h S tensor b_c, where
b_c phi=[t_c,phi] and Tr(b_c b_c^T)=2 in the stated SU(2) convention.
Summing the three exterior colors in (2) gives exactly

    T_i=-6 sum_(k,l) c_(i;kl)
                sum_(e,f) A_ef (h_k)_f (h_l)_e K^+_fe.  (10)

Only a compact enlargement of the support of A enters the e,f sum.
On each row stencil (9) implies

    K^+_fe=j_e W^infty_fe-4 alpha_e+O(1),                 (11)

where W^infty is the endpoint sum of the scalar g, independent of
both axial levels. Its entries are uniformly bounded. The factor
four is the number of endpoint pairs, not a deleted color or pairing.
Every endpoint in these supported stencils is interior.

The constant term of (11), when summed over f, is exactly

    -4 alpha_e (h_l)_e (A h_k)_e.                        (12)

L156(9) gives ||A h_k||_infinity<=C a^5 p(k); the actual interior
columns satisfy ||h_l||_infinity<=C a p(l) by L150(8)'s mode-column
argument. There are O(N^4) supported edges. Thus the absolute sum
of (12) is at most C p(k)p(l) N^4 a^6(1+log N), which is
O(p(k)p(l) N^-2(1+log N)). No estimate for A B_h on a rough
input is made: (12) arises only after the constant scalar kernel
has been summed exactly. alpha_e may vary with e and is never
commuted through A.

### 4. The growing stationary contraction cancels before estimating

The finite-stencil description in L028 gives |A_ef|<=C/a, and the
smooth interior mode extensions in L150 give

    |(h_k)_f|<=C a p(k),
    |(h_k)_f-h_(k,nu)(c_e)|<=C a^2 p(k)                  (13)

for f in component nu within the row stencil of e. Axial interior
columns are identically zero; their extension is zero. This does not
extend the field smoothly across the upper pinned jump.

Let A_e^0 be the whole translation-invariant principal generator row
obtained by freezing every displacement coefficient in
(L K_a+K_a^T L)/2 at c_e, keeping all its component filters and
stencil offsets. Its entries are O(1/a). Smooth coefficient changes
on bounded offsets are O(a), multiplied by 1/a. The two actual
insertion matrices Q_3,Q_6 have bounded dimensionless entries and
fixed range. Therefore on every supported row

    |A_ef-(A_e^0)_ef|<=C.                                (14)

Both the adjoint coefficient derivatives and the subtractions are
in this remainder; neither is omitted.

Use unitary edge-center Fourier phases. Put d_j=2 sin(theta_j/2),
c_j=cos(theta_j/2), H=sum_j d_j^2. L has the real even symbol
H I-d d^T. The complete frozen generator, including endpoint and
clover averages, is (i/a)M with

    M_(nu,sigma)=c_nu^2 [delta_(nu,sigma) sum_rho u_rho c_rho d_rho
                                  -u_sigma c_sigma d_nu].

This follows directly from L028's endpoint/clover composition:
the curl contributes i(d_rho x_nu-d_nu x_rho), its clover contributes
c_rho c_nu and the output endpoint contributes c_nu. Hence

    A_e^0(theta)=(i/(2a))[(H I-d d^T)M-M^T(H I-d d^T)]    (15)

is imaginary and odd under simultaneous theta->-theta, entrywise.
The stationary scalar potential is constant in the axial coordinate.
Its endpoint-sum kernel in this same closed-trace convention has,
on theta_1=0, the real even symbol

    W^infty_(nu,mu)(theta_T)=4 c_nu c_mu/lambda(theta_T).

Thus for each output component mu and input component nu,

    sum_(f in component nu) (A_e^0)_ef W^infty_fe=0.      (16)

Indeed the finite row sum is the integral over the full transverse
torus of the product of the two indicated symbols. Its integrand is
odd and integrable: near zero (15) is O(|theta_T|^3/a), whereas
lambda is comparable to |theta_T|^2. All path phases are retained
by the center convention; summing the axial offsets gives theta_1=0.
There is no finite-box inversion assumption, no frozen-forest symmetry
and no discarded zero prefix. The identity applies separately to each
component pair, before the actual exterior column values are multiplied.

Now freeze only the local column value (h_k)_f at h_(k,nu)(c_e) in
the stationary part of (11), and replace A by A_e^0. Its sum is
zero by (16). The differences have explicit per-row bounds:

    coefficient difference: C N a^2 p(k)p(l),
    exterior difference:    C N a^-1 a^3 p(k)p(l),
    bounded kernel error:   C a^-1 a^2 p(k)p(l).          (17)

Here j_e<=N, W^infty is bounded, (13)--(14) apply, and each row
has a fixed number of entries. Each expression is O(N^-1 p(k)p(l))
since a=8/N. Summing O(N^4) rows gives C N^3 p(k)p(l). The
constant term was separately bounded in (12), so it introduces no
N^3 log N loss.

Finally L156(8) gives the mesh-uniform complete heat sum
sum_(k,l)|c_(i;kl)|p(k)p(l)<=C_i. Summing (12),(17), with the
factor six in (10), proves (3). Equation (4) is L157(6) and (1).
No bound is transferred to the still differently ordered V_i or E,E.
In particular the O(N^3) errors in (17) must be retained at cubic
scale; their signs and limits have not been evaluated.

### 5. Exact finite check and interpretation

Run `PYTHONDONTWRITEBYTECODE=1 python3 scripts/combined-ward-response/check_cubic_action_hessian_collapse.py`.
Its full rational certificate is
`scripts/combined-ward-response/cubic-action-hessian-collapse-certificate.json`.
It checks (2) on a pinned two-cycle graph with its actual Hodge inverse,
prefix retraction and signed E, using a symmetric A annihilating the
gradient but not commuting with L. Both full colored trace branches
are compared with their collapsed forms, and the factor-six scalar
color reduction is checked. Nine exact rational Fourier cases also
check the complete-filter odd parity and paired endpoint-kernel integrands.
All four matrix identities, six branch/color comparisons and nine
parity cases have maximum exact error zero. The graph has noncommuting
A,L and E with both positive and negative diagonal entries. These
checks establish finite algebra
only, not the actual-probe coefficient or a cutoff limit. The
asymptotic estimate is the analytic argument (5)--(17).

The raw absolute stationary count was O(N^4); (16) removes precisely
that contribution, leaving O(N^3). This is a relevant scale gain,
without meeting the required o(N^3). Both original action terms remain
in (4). Other response jets, full compensation, finer asymptotics and
the main construction gaps stay open. No candidate is claimed.

## Mathlib

Full matching result: **not checked**. Supporting finite trace identities,
scalar lattice Green estimates, maximum principle and stencil parity:
**not checked**. Unknown availability is not evidence of absence.
Reuse the unchanged
[assessment](../drafts/literature/2026-10-12-cubic-residual-action-cubic-scale.md).
No further continuum theorem is imported or reproved. The finite
specialization is necessary because L E A, the locally logarithmic
potential correction and the ordered endpoint filters determine whether
the branch exceeds the cubic threshold.
