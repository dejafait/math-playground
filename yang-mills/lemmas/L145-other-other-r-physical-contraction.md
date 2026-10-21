# L145 — R has the same universal scalar as G and a different physical form

## Hypotheses

Import L107(1)--(3)'s established co-closed-base reverse functional
K_(i,R), including its factor 1/2. Keep SU(2), both actual L010 probes
i=3,6, the straight lower-rooted direction-1 forest, relative all-face
fixed-link box D=(-4,4)^4, tau=1/16 and the bare small-coupling
coefficient taken at each fixed mesh before refinement. This lemma
contracts an established continuum functional; it takes no new mesh
limit. No outside factor 3 or color factor is inserted.

Use L080's complete real relative modes f_k, eigenvalues lambda_k,
A_k=f_k/sqrt(lambda_k), and real symmetric coefficients

    c_(i;kl)=exp[-(lambda_k+lambda_l)/16] q_i(A_k,A_l).

The transverse forest field is exactly

    V_(k,a)=A_(k,a)-partial_a integral_(-4)^(x_1) A_(k,1)(r,x_T) dr,
    a in {2,3,4}.

Retain its constant axial mode and full physical prefix, all exterior
labels, both displacement sectors in q_i, the transition region,
and L107's raw path and ordered endpoint filters. Import L132's
full-probe norm, mode-amplitude and heat-tail estimates, and L140's
scalar g_G with L141's exact enclosure. Neither L140's different
physical G form nor L144's G values are substituted for this form.

## Conclusion

Define the absolutely convergent real physical heat form

    B_(i,R)=sum_(k,l)c_(i;kl) integral_D u_1(x)
                                          V_k(x) dot V_l(x) dx.    (1)

Then, with normalized three-dimensional torus measure,

    K_(i,R)=g_G B_(i,R),
    g_G=-(1/4) integral XY(X-Y)^2/(X+Y+Z)^2,
    -61/1000<g_G<-43/1000,                                 (2)

where X=4 sin^2(theta_2/2), Y=4 sin^2(theta_3/2),
Z=4 sin^2(theta_4/2), and the origin integrand is zero.
The scalar identity is exact; the scalar interval is imported from
L141. Both actual physical forms, and hence both R signs, remain
unevaluated. In particular B_(i,R) is not B_(i,G).

For a rectangular mode cutoff K>=1 retaining every allowed index <=K,
put C_R=160380, N_3=6050, N_6=1640736 and

    H(K)=2(4*12^4)(16*12^3)*512/(9K)*exp(-9K^2/1024).

The complete omitted-spectrum bounds are

    |B_(i,R)-B_(i,R)^[K]|<=C_R N_i H(K),
    |K_(i,R)-g_G B_(i,R)^[K]|<(C_R/4) N_i H(K).            (3)

At K=96 these are below 5.329*10^-15 and 1.333*10^-15,
respectively, for both probes. They bound omission only. Section 4
specifies the exact finite physical tensor with both inverse weights;
retained spatial/time and arithmetic inclusion remain to be supplied.

This is local REPRODUCTION under the unchanged complete-other/other
EXPLORE assessment, not an originality claim. L124 adds R with a plus
sign before its single outside factor 3. The actual R values, triplet
transverse-H sign and complete compensation comparison remain open.
Finer powers/logarithm, other response jets, finite matching, interacting
error <=c_box/2, continuum axioms, reflection positivity, infrared
control and finite positive mass remain independent gaps. No candidate
Yang--Mills solution is asserted.

## Proof

### 1. Simplify the projected alternating matrix with all phases intact

Write e_a=exp(i theta_a), tau_a=1-e_a, L=sum_a |tau_a|^2,
and q=I-tau tau*/L for L>0. In this proof q denotes the co-closed
projection, not an individual path row. Import c,z_v,w from L107,
with w_a=-u_1(1+e_a)i sin(theta_a)/2. Directly from those raw rows,

    c tau=0, c* c=Lq,
    z_v tau=c D_v,  (D_v)_a=(1+e_a)v_a.                    (4)

The last equality is L140(5), obtained using both paths. For the
projection calculation set s_a=sin(theta_a/2), eta_a=cos(theta_a/2),
S=sum_a s_a^2, h_a=eta_a v_a. Change edge basis by
U=diag(exp(i theta_a/2)) and plane basis by
J=diag(exp(i(theta_a+theta_b)/2)), a<b. These are unitary at every
angle. Tildes mean U* on edge outputs, U on edge inputs and J* on
plane outputs. Thus

    tilde tau=-2i s, tilde q=I-ss^T/S,
    tilde c_(ab)=2i(-s_b e_a^T+s_a e_b^T),
    tilde z_(v,ab)=2(-h_b e_a^T+h_a e_b^T)+v_a tilde c_(ab). (5)

For example the raw z row has entries
v_a(1-e_b)-v_b(1+e_b) and 2v_a e_a. Multiplication by the
displayed unitary phases gives (5) exactly. This checks the asymmetric
raw traversal rather than replacing it by a centered path.

For a real vector t define the real matrix C(t) with rows
-t_b e_a^T+t_a e_b^T. Then

    C(h)^T C(s)=(h dot s)I-s h^T.

The real plane multiplier v_a in the last term of (5) cancels from
tilde omega_v=tilde z_v* tilde c-tilde c* tilde z_v. Consequently

    tilde omega_v=4i[2(h dot s)I-s h^T-h s^T],
    tilde q tilde omega_v tilde q=8i(h dot s)tilde q.

Since 2 eta_a s_a=sin(theta_a), returning to the raw basis gives

    beta_v=q omega_v q=4i(sum_a v_a sin(theta_a))q.          (6)

No filter is commuted through a variable finite-lattice projection:
(6) is an exact contraction of the already justified same-point
functional. It supplies no reverse-block operator-norm gain.

### 2. Retain the half-weight and integrate the full signed tensor

L107 has alpha_k=p omega_k q, p=tau tau*/L, and omega_k*=-omega_k.
Equations (4) and c tau=0 imply

    q alpha_k* tau=-q omega_k tau=c* z_(V_k) tau=Lq D_(V_k).

The rank-one trace in L107(2), including its half-weight, is therefore

    (1/(2L)) w* beta_(V_l) q D_(V_k).                      (7)

To evaluate it put t_a=sin(theta_a), X_a=|tau_a|^2 and
T=sum_a t_a^2. The exact scalar products are

    w* D_v=2i u_1 sum_b eta_b^2 t_b v_b,
    w* tau=u_1 T,       tau* D_v=2i sum_b t_b v_b.

Substitute these and (6) into (7). The complete bilinear coefficient
of u_1 V_(l,a)V_(k,b) is

    -4 t_a t_b [eta_b^2-T/L]/L.                            (8)

All factors except t_a t_b are even in every angle. Reflecting
theta_a deletes the integral of every a!=b entry. For a=b,
t_a^2=X_a eta_a^2 and T=L-(sum_j X_j^2)/4 reduce (8) to

    n_a/L^2,
    n_a=X_a(1-X_a/4)[X_a L-sum_j X_j^2].                  (9)

The integral of each of the three diagonals is equal by coordinate
permutation. Their sum satisfies the polynomial identity

    sum_a n_a=-(1/4)sum_(a<b) X_a X_b(X_a-X_b)^2.           (10)

Indeed the left side is [(sum X_a^2)^2-L sum X_a^3]/4;
expanding each unordered pair gives the right side. The three pair
integrals on the right are also equal. Dividing the integrated sum
by three thus identifies each diagonal integral with precisely g_G
in (2), not three times that scalar. This proves the torus identity
for each real exterior pair, including L107's original 1/2.

These manipulations concern integrable functions. For example
|t_a|<=sqrt(X_a), 0<=T<=L and |eta_b|<=1 bound the absolute
value of (8) by 8 sqrt(X_a X_b)/L<=8. The diagonal (9) is also
bounded at the singular corner, as is the symmetrized scalar.
Assigning any value at the one origin point changes no integral.
Thus neither reflection nor permutation invokes a conditionally
convergent angular integral. L140's strict scalar bound -1/4<g_G<0
and L141's stronger exact interval apply to this identical integral.

### 3. Full heat sum and complete spectral omission

L132's normalized mode estimates give |V_(k,a)|<=1/2 for every
allowed label, including component 1 with axial index zero. Also
|u_1|<=165 on support of volume <=1296. Therefore

    |integral_D u_1 V_k dot V_l|<=1296*165*3/4=C_R.

Together with L132's bound
|c_(i;kl)|<=N_i exp[-(lambda_k+lambda_l)/16], this proves
absolute convergence of (1). The uniform angular bound after (8)
and the same mode bounds also dominate the full pre-integration
series. Hence the finite-cutoff identity passes to the full heat sum.
No cancellation or decay of the physical prefix at x_1=4 is required.

Import L132's complete two-label omitted heat-weight bound H(K).
Multiplication by C_R N_i proves (3)'s first inequality; the strict
|g_G|<1/4 proves its second. At K=96 the exponential is exp(-81)
and the prefactor of H is 2717908992. As in L132, e^3>20 gives

    C_R N_6 H(96)
      <160380*1640736*2717908992/20^27
      <5.329*10^-15.

Dividing by four gives the stated R bound. This retains both inverse
weights through the normalized modes and the entire omitted spectrum;
it says nothing about retained tensor evaluation.

### 4. Exact finite tensor and reproducible algebra check

Let L_F f=f_T-grad_T integral_(-4)^(x_1) f_1. At cutoff K set

    (M_R,K)_kl=integral_D u_1 (L_F f_k) dot (L_F f_l),
    (Q_i,K)_kl=q_i(f_k,f_l),
    (F_K)_kk=exp(-lambda_k/16)/lambda_k.

The matrices M_R,K and Q_i,K are real symmetric. Expansion of their
trace, with the normalization of A in both the probe and physical
form, gives exactly

    B_(i,R)^[K]=Tr(M_R,K F_K Q_i,K F_K).                    (11)

For explicit separable entries use L132's complete lift rows and probe
curvature rows. Write r=rho, f(x)=x rho(x); the physical weight here
is u_1=f tensor r tensor f' tensor r, without an additional x_1+4
factor. Pair every transverse lift component with itself and include
all input components. A component-1 lift row has the negative prefix
factor p_0=(x_1+4)/sqrt(8) or
p_n=sin(n pi(x_1+4)/8)/(2n pi/8), n>=1, with its transverse
derivative. Both copies are retained. The probe matrix keeps both
Psi_13 and Psi_24 with their actual triplet/shear polarizations.
Every entry is thereby a finite signed sum of products of the four
one-dimensional integrals of weight times two mode factors. Finally
use exp(-lambda/16)/lambda=integral_(1/16)^infinity exp(-t lambda)dt
separately for both F_K factors. This supplies the evaluable full-probe
tensor without identifying it with the G tensor or dropping an inverse.

In particular oddness of u_1 in x_1 alone is not permission to delete
(1): its component-1 prefix includes x_1+4, not an odd centered
primitive. No actual-probe sign or reflection cancellation is used.

Reproduction command from the active notebook:

    python3 scripts/combined-ward-response/check_r_physical_reduction.py

It saves `scripts/combined-ward-response/r-physical-reduction-certificate.json`.
All 46 exact rational Laurent checks pass: nine c*z_v*tau entries,
27 complete projected-omega entries, nine full raw parity numerators
including the half-factor denominator, and the diagonal pair-square
identity. The script multiplies the original raw matrices, clears
their known powers of L and checks every Laurent coefficient, not
sample angles. Its exact rational omitted-spectrum comparisons also
pass, with zero failures. Full actual and required polynomials and
residuals are saved. This verifies algebra and tail arithmetic; the
analytic convergence and integration arguments are given above.
No IEEE or numerical quadrature premise is needed for this reduction.

## Mathlib

Full matching R-functional contraction and finite tensor specialization:
**not checked**. Supporting unitary conjugation, finite matrix trace,
Fourier reflection, absolute convergence, Laplace identities and Gaussian
tail coverage: **not checked**. Unknown availability is not absence.
The scalar theorem is imported from L140/L141, and the heat estimates
from L132; only the different R contraction is derived here. No general
Yang--Mills, Ward or flow-finiteness theorem is reproved or assigned to
this isolated group.
