# L125 — Joint scalar/energy placement retains a nonzero first-moment tensor

## Hypotheses

Use exactly L121 and L122's canonical coefficients K_(i,sc) and
K_(i,en): SU(2), both actual L010 probes i=3,6, straight lower-rooted
direction-1 forest, all-face relative fixed-link box D_box=(-4,4)^4,
a=8/N through admitted even meshes, tau=1/16, and the fixed-mesh bare
small-coupling coefficient before refinement. Retain all original
stencils, signs, relative rows, exterior heat modes and prefix fields.
The coefficient limits are imported, not rederived or replaced by
finite equal-level identities. All torus integrals below use normalized
measure dtheta/(2pi)^3 on [-pi,pi]^3, indexed by directions 2,3,4.

Use L121(1)--(2)'s real kernels g_(r,j), p and H, its finite path
stencils S_alpha with coefficients s_alpha(h), and its tensors A,B.
Use L111(1)'s ordered generator list r and displacement component
rho(r). Put ell=x_1+4 and use the continuum phi and c_(i;kl) appearing
in L121(3) and L122(2). They include the physical lower-rooted prefix
and its constant component-1 axial mode.

Define the full-grid plaquette operator and its kernel by

    Q_(alpha,beta)=S_alpha^* P_inf S_beta,
    Q_(alpha,beta)(x,y)=q_(alpha,beta)(x-y).

Here * is the ordinary transpose on real arrays and the complex
adjoint on Fourier symbols. Lower-vertex symbols use the convention
hat k(theta)=sum_d k(d) exp(-i d dot theta); a shift v(x+h) has
symbol exp(i h dot theta). These are L110--L121's conventions.

## Conclusion

The real, absolutely convergent tensor

    M_(r,m;alpha,beta)
      =sum_(j in Z) sum_(d in Z^3)
          d_m tr[g_(r,j)(d) q_(alpha,beta)(-d)], m=2,3,4,       (1)

reduces the two placement coefficients to

    K_(i,sc)+K_(i,en)
      =sum_(k,l)c_(i;kl) sum_(r,m,alpha,beta) M_(r,m;alpha,beta)
         integral_(D_box) ell u_(rho(r))
                  phi_(l,alpha) partial_m phi_(k,beta) dx.    (2)

Every sum and spatial integral in (2) is absolutely convergent.
There is no additional color, symmetry or outside factor 3.

There is a finite torus formula for (1). Write

    d_mu=2 sin(theta_mu/2), eta_mu=cos(theta_mu/2),
    lambda=sum_mu d_mu^2, P_c=d d^T/lambda,
    (D_c)_(mu nu)=i(-d_nu e_mu^T+d_mu e_nu^T),
    S_c=D_c D_c^*/lambda,
    Q_(alpha,beta),c=(S_alpha)_c^* P_c (S_beta)_c,
    G_(r,c)=D_c (T_r C_r)_c S_c.

The centered stencils and ordered signs are exactly L118(7),(9).
At lambda=0 all displayed integrands may be assigned value zero.
Then

    M_(r,m;alpha,beta)
      =i integral tr[(partial_(theta_m) G_(r,c))
                                      Q_(alpha,beta),c].      (3)

The phase-derivative contribution is removed only after integration,
by the parity argument below. It must not be silently omitted in an
arbitrary differentiated matrix product.

This tensor is not identically zero. Take r to be displacement rho=2,
output edge nu=3 and ordered plane pi=(23), with its positive sign.
Let a_b=(pi,b) and a_q=(pi,q). The particular combination

    M_* =sum_(alpha,beta in {a_b,a_q}) M_(r,2;alpha,beta)

satisfies the exact, strictly positive formula

    M_* = integral
      8 eta_3^4 d_2^2 eta_2^2 (d_2^2+d_3^2)(d_3^2+d_4^2)
                                      /lambda^3 > 0.          (4)

This is a universal stencil-tensor test, not the value or sign of
(2) for either actual probe. It rules out discarding the entire joint
placement tensor by L118's undifferentiated odd-parity argument.
Other tensor components and the actual full heat-weighted contractions
may cancel this component. No actual-probe nonvanishing is asserted.

In L124's nine-term comparison only the sum K_(i,sc)+K_(i,en) is
replaced by (2). All seven other canonical terms remain, with exactly
L124's signs; K_(i,oo)+4 gamma D_i is still unevaluated. No compensation,
finer remainder, logarithmic coefficient, interacting reflected-error
bound <=c_box/2, continuum axioms, reflection positivity, infrared
control or finite positive mass follows.

## Proof

### 1. Combine the canonical coefficients using their common joint tails

L121(2) and L122(1) use the same H and the same B, in the same
lower-vertex convention. L121, proof section 4, (12)--(13), proves

    sum_(j,h,n,d) (|d|+M_0) |H_(r,j;alpha,beta,h,n)(d)| < infinity,

where M_0 bounds the finite path shifts. This is a joint bound; no
separate first absolute moment of the projection kernel is needed.
Expanding the kernels of S_alpha^* P_inf S_beta gives exactly

    q_(alpha,beta)(-d)
      =sum_(h,n) s_alpha(h)^T p(-d-h+n) s_beta(n).

Thus summing H over h,n gives tr[g_(r,j)(d) q_(alpha,beta)(-d)].
Absolute convergence permits adding L121's A and B before any other
operation. Their two weights add as n_m+(d_m-n_m)=d_m. Consequently

    sum_j (A_(r,j,m;alpha,beta)+B_(r,j,m;alpha,beta))
                                        =M_(r,m;alpha,beta).   (5)

At each fixed set of labels, the product rule in L122(2) cancels
L121(3)'s term -B (partial_m phi_l) phi_k exactly. The remaining
term is (A+B) phi_l partial_m phi_k. Equations (5) and the two
canonical formulas prove (2). Their polynomial mode bounds on the
compact displacement support and their full Gaussian heat majorant
justify this operation through the entire heat sum and spatial
integral. No integration by parts in x, boundary replacement, or new
mesh limit was made.

### 2. Sum the axial kernel before computing the first joint moment

L121(12) and L110(2), with the unweighted estimate from L111, give

    sum_j [||g_(r,j)||_2+|| |d| g_(r,j)(d)||_2] < infinity.    (6)

The fixed stencils S_alpha and bounded projection imply
||q_(alpha,beta)||_2<infinity. Fourier Plancherel, first for spatial
truncations and then using (6), gives the bilinear identity

    sum_d d_m tr[g_(r,j)(d) q_(alpha,beta)(-d)]
       =i integral tr[(partial_m hat g_(r,j)) hat Q_(alpha,beta)].
                                                               (7)

Indeed differentiating exp(-i d dot theta) gives -i d_m; the
integral of the product selects the opposite coefficient -d.
Both sides extend by L2 pairing, without any assumption that the
kernels individually have absolutely summable first moments.
Equation (6) permits summing (7) over j in the periodic W^(1,2)
space of matrix entries and in its pairing with the L2 symbol Q.

For lambda>0 the explicit axial multiplier in L110 is

    r_lambda(j)=exp(-kappa |j|)/(2 sinh kappa),
    kappa=2 asinh(sqrt(lambda)/2).

The geometric series and lambda=4 sinh^2(kappa/2) give

    sum_j r_lambda(j)
       =coth(kappa/2)/(2 sinh kappa)=1/lambda.

Since hat g_(r,j)=D T_r C_r E_j, we obtain in the original raw phases

    sum_j hat g_(r,j)=G_r=D T_r C_r S,
    S=D D^*/lambda.                                      (8)

Equality holds also in W^(1,2) by (6); it is not a merely pointwise
interchange of a derivative and a singular series. Combining
(7)--(8) yields i integral tr[(partial_m G_r) Q_(alpha,beta)].

### 3. Track the component phases in the derivative

Use L118's unitary plaquette phases

    U_2=diag_(pi=(mu,nu)) exp(i(theta_mu+theta_nu)/2).

Then G_r=U_2 G_(r,c) U_2^* and Q=U_2 Q_c U_2^*. Put
R_m=diag_pi[(1_(m=mu)+1_(m=nu))/2]. Differentiating gives, away
from zero and hence as the corresponding integrable weak derivative,

    i tr[(partial_m G_r)Q]
       =i tr[(partial_m G_(r,c))Q_c]
                                      -tr[[R_m,G_(r,c)]Q_c].  (9)

L118 proves each projected path product Q_c real and even under
simultaneous theta reversal, and D_c(T_r C_r)_c imaginary and odd.
S_c is real and even. Hence the last trace in (9) is imaginary
and odd, and has integral zero on the symmetric cube. It is
integrable: G_(r,c)=O(|theta|) near zero, while Q_c is bounded.
The differentiated first term is also integrable, either from (6)
and the bounded phases, or from partial_m G_(r,c)=O(1) near zero.
This proves (3). The derivative of an odd function is even; L118's
zero undifferentiated integral does not give a zero value in (3).
Individual centered entries need not be periodic, and no boundary
integration by parts with those entries was used in (9).

### 4. Test an actual ordered stencil and its two same-plane paths

For r=(rho=2,nu=3), L118(9) gives

    (T_r C_r)_c=eta_2 eta_3^2 e_3 epsilon_(23)^T.

Here epsilon_(23) is the corresponding plaquette column. For the
same plane, L118(6)--(7) imply

    (S_(pi,b)+S_(pi,q))_c
       =(q_pi^*-b_pi^*) epsilon_pi^T
       =-2 eta_3 e_2 epsilon_pi^T.

The imaginary circulation parts cancel before projection. Therefore
summing Q_(alpha,beta),c over the four indicated pairs gives

    Q_* = [4 eta_3^2 d_2^2/lambda] epsilon_pi epsilon_pi^T.

Also (S_c)_(pi,pi)=(d_2^2+d_3^2)/lambda and
(D_c)_(pi,3)=i d_2, so

    (G_(r,c))_(pi,pi)
      =i F, F=d_2 eta_2 eta_3^2 (d_2^2+d_3^2)/lambda.

Formula (3) now reads

    M_*=-integral (partial_2 F) J,
    J=4 eta_3^2 d_2^2/lambda.

An integration by parts in theta_2 is legitimate. On the two
faces theta_2=+/-pi, F=0 because d_2 eta_2=sin(theta_2).
To handle zero frequency first remove a ball of radius epsilon:
F=O(|theta|), J=O(1), and its surface boundary contribution is
O(epsilon^3). The derivatives are locally integrable, with
partial_2 F=O(1) and partial_2 J=O(1/|theta|). Removing the ball
therefore gives M_*=integral F partial_2 J, with no omitted boundary
term. Direct differentiation, using partial_2 d_2=eta_2, yields

    partial_2 J=8 eta_3^2 d_2 eta_2 (d_3^2+d_4^2)/lambda^2.

Multiplication by F proves (4). Its integrand is nonnegative
everywhere it is defined, bounded near zero, and strictly positive
on an open neighborhood of (pi/2,pi/2,pi/2). That neighborhood has
positive measure, proving strict positivity without numerical evidence.

This proves nonvanishing of a specific component combination of the
universal tensor. It does not isolate that combination in the actual
phi fields: a physical mode determines coefficients in all planes,
and both probe heat forms and all ordered r remain in (2).

### 5. Scope of the comparison

L124 imports all nine limits with signs
K_E+K_ax-K_Q+K_G+K_R+K_f+K_V+K_sc+K_en. Replacing just the last
two by the exact identity (2) retains every coefficient and L124's
single outside factor 3. L084's reference is unchanged. Nothing in
the positivity witness evaluates this full signed expression or
assumes separate forest invariance or complete-response finiteness.

This is a local RESEARCH / REPRODUCTION calculation under the unchanged
EXPLORE assessment drafts/literature/2026-10-10-other-other-cubic-leading-scale.md.
The product-rule and Fourier steps are written out because their signs,
component phases and actual stencil specialization matter here. Existing
kernel-tail and scaled-limit theorems are imported by the equation and
section citations above, not reproved. No novelty beyond the checked
sources or progress on the interacting construction is claimed.

## Mathlib

Full matching theorem: **not checked**. Supporting Fourier/Plancherel,
weak-derivative, product-rule and integration-by-parts coverage:
**not checked**. Unknown availability does not imply absence. The
specialized tensor calculation is proved here; it uses no new external
source theorem, numerical certificate or mathematical script.
