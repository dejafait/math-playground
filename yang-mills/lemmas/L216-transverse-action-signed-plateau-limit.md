# L216 — A finite signed cubic limit for the transverse action plateau block

## Hypotheses

Keep L025, L213–L215's pinned relative SU(2) cube D=(-4,4)^4,
admitted even meshes a=8/N, straight lower-rooted direction-1 forest,
and both actual L010 probes i=3,6 at tau=1/16. The bare expansion
precedes refinement. Coordinates and transposes are ordinary stored
dimensionless ones. All colors, transverse planes, physical end rows,
constant modes, both residual subtractions and full heat sums remain.

Use L215's H=Delta_3, G=H^(-1), b_j and scalar A_11. Write
B_j=b_j^T tensor I and A_<j=B_j A_11 B_j^T, exactly the cumulative
scalar insertion of L101(1),(13). For a transverse plaquette p at
axial vertex j, let q_(p,l), l=1,...,4, be its signed traversal-edge
endpoint dipoles on pinned transverse vertices. Thus the plateau
part of its one-color residual covariance is

\[
 (V^{\rm pl}_p)_{lm}=q_{p,l}^T G A_{<j}Gq_{p,m}.
 \tag{1}
\]

Add color indices by taking three identical diagonal blocks. Define
the plateau contribution, with L025's original tensor and sign, by

\[
 T_i^{\rm pl}(a)=-24\sum_{p\in P_T}K:U_{i,p}:V^{\rm pl}_p.
 \tag{2}
\]

This is precisely the two-prefix part of L215's replaced transverse
class. The other three row terms in L215(15) are not included in (2).

## Conclusion

For i=3,6 there is a finite real signed functional P_i with

\[
 a^3 T_i^{\rm pl}(a)\longrightarrow P_i.
 \tag{3}
\]

Here is its explicit unevaluated formula. At a plane mu<nu in
{2,3,4}, label traversal directions (mu,nu,mu,nu) by n_l and signs
sigma=(1,1,-1,-1). On Z^3 put

\[
 \eta_1=\delta_{e_\mu}-\delta_0,\quad
 \eta_2=\delta_{e_\mu+e_\nu}-\delta_{e_\mu},\quad
 \eta_3=\delta_{e_\nu}-\delta_{e_\mu+e_\nu},\quad
 \eta_4=\delta_0-\delta_{e_\nu}.
 \tag{4}
\]

For theta in [-pi,pi]^3 use normalized torus measure, Fourier
transform hat eta(theta)=sum_r eta(r) exp(-i r dot theta), and
L101(4)'s real symbol

\[
\begin{split}
 d_\mu&=2\sin(\theta_\mu/2),\quad t_\mu=\sin\theta_\mu,
 \quad\lambda=\sum_\mu d_\mu^2,\\
 W_\mu(x)&=\int_{-4}^{x_1}\partial_\mu u_\mu(t,x_T)\,dt,\\
 m_E(x,\theta)&=\sum_\mu W_\mu(x)(t_\mu^2-d_\mu^2)
 -{\lambda\over2}\sum_\mu W_\mu(x)\cos\theta_\mu
 +u_1(x)\left({1\over2}\sum_\mu t_\mu^2-\lambda\right).
\end{split}\tag{5}
\]

Define the four-edge/color matrix

\[
 \mathcal V^{\mu\nu}_{(l,c),(m,d)}(x)
 =\delta_{cd}\int
 {\overline{\widehat\eta_l(\theta)}m_E(x,\theta)
                  \widehat\eta_m(\theta)\over\lambda(\theta)^2}
                  {d\theta\over(2\pi)^3}.
 \tag{6}
\]

Its integrand may be set to zero at the single point lambda=0.
Let f_k, lambda_k and B_i be the real relative continuum modes,
physical eigenvalues and bounded one-color whitened probe operator
of L008(8). Set beta_(i;kl)=<f_k,B_i f_l>, b_k=f_k/sqrt(lambda_k),
and, for transverse mu, define the smooth lower-rooted lift

\[
 (\mathfrak r b)_\mu(x)=b_\mu(x)
       -\int_{-4}^{x_1}\partial_\mu b_1(t,x_T)\,dt.
 \tag{7}
\]

Use its one-sided upper trace; it is not the fixed upper transverse
link value. Put

\[
\begin{split}
 \mathcal P_{i,\mu\nu}(x)
 &=\sum_{k,l}e^{-\tau(\lambda_k+\lambda_l)}\beta_{i;kl}
                (\mathfrak r b_k)_\mu(x)(\mathfrak r b_l)_\nu(x),\\
 \mathcal U^{\mu\nu}_{i,(l,c),(m,d)}(x)
 &=\delta_{cd}\sigma_l\sigma_m
                         \mathcal P_{i,n_l n_m}(x).
\end{split}\tag{8}
\]

The repeated use of l in the first and second lines has its usual
local meaning: k,l in the series are mode labels; l,m in the local
matrix are traversal positions. Then

\[
 P_i=-24\sum_{2\le\mu<\nu\le4}\int_D
           K:\mathcal U_i^{\mu\nu}(x):\mathcal V^{\mu\nu}(x)\,dx.
 \tag{9}
\]

Every series and integral in (6),(8),(9) converges absolutely.
Neither P_i nor the direct/direct and mixed-row limits are evaluated.
In particular (3) does not establish a limit for the complete L025
response. Full compensation, finer asymptotics, finite matching,
reflected error <=c_box/2, continuum axioms and infrared finite mass
remain unresolved. This is a local specialization of existing
cumulative-stencil and Green-energy arguments, without a novelty claim.

## Proof

### 1. Reuse the exact cumulative insertion

Every edge of p lies at the same axial vertex level j. Therefore
the two plateau columns in L215 are b_j tensor Gq_(p,l) and
b_j tensor Gq_(p,m), and their pairing with A_11 gives (1) exactly.
The minus prefix in each forest row has produced a plus sign in
V^pl; the minus in the response is still the original -24 in (2).
No Gaussian-tilt factor 2 is present.

Import L101 proof sections 3–4: its identity (13) computes this
same A_<j, and its normalized stencil limit has symbol (5),
uniformly in all 1<=j<N and transverse positions. More explicitly,
after translating a transverse vertex v to the origin, every fixed
stencil coefficient of a A_<j tends to the corresponding coefficient
of the translation-invariant operator M_x with symbol m_E(x,theta),
where x=(-4+aj,-4+a v), uniformly when x_T stays in a compact
transverse interior. The coefficient convergence is uniform also in
j. This is convergence on rough fixed-stencil test fields, not an
application of smooth-input residual consistency to a Green column.

The input is an exact match, rather than a scalar-to-mixed transfer:
both use the pure component-1 prefix, L065's generator outputs,
the average-of-squares triplet, the clover shear and both subtractions.
In particular L101(13)'s cut term is
(2a)^(-1) sum_mu T_mu^T M_(u_1(j)) T_mu. It accounts for the
u_1 sum t_mu^2/2 part of (5) and cannot be discarded. L101's
quarter-weight layer tends to zero after normalization; all other
axial coefficient levels remain in W_mu. The cumulative weights are
not replaced by the local coefficient times j.

L065's bilinear energy bound, applied to B_j^T f and B_j^T h,
also gives

\[
 |f^T(a A_{<j})h|\le C a j\|f\|_E\|h\|_E
                    \le8C\|f\|_E\|h\|_E,
 \quad \|f\|_E^2=f^T H f.
 \tag{10}
\]

For the frozen operator, (5) gives |m_E|<=C' lambda,
uniformly in x: the smooth W_mu,u_1 are bounded and
t_mu^2<=d_mu^2<=lambda. Thus M_x has the same type of energy
bilinear bound on Z^3. Positivity is not required for either form.

### 2. Prove the complete local dipole limit before summing

The energy-projection argument in L042 proof section 2 applies to
each translated signed dipole eta_l in (4). Here are the needed
details for the present bilinear specialization. With H_infinity
the Z^3 vertex Laplacian, define g_l by hat g_l=hat eta_l/lambda.
Since |hat eta_l|^2=d_(n_l)^2<=lambda, g_l is in l2 in three
dimensions: its squared Fourier integrand is bounded by 1/lambda,
whose singularity is O(|theta|^-2) and integrable. It has finite
energy integral |hat eta_l|^2/lambda<=1. Truncating g_l in l2
gives finitely supported energy approximants, since H_infinity is
a bounded operator on l2.

Translate the finite cube by v and extend Gq_(p,l) by zero to Z^3.
On any finitely supported field h inside that translated cube,

\[
 \langle Gq_{p,l},h\rangle_E
   =\langle\eta_l,h\rangle=\langle g_l,h\rangle_E.
 \tag{11}
\]

The energy includes every edge to a pinned zero endpoint. Thus
Gq_(p,l) is the energy-orthogonal projection of g_l onto the
finite supported vertex space. Its norm is no larger than that of
g_l and its distance from g_l is bounded by the error of any
finitely supported approximant inside that cube. For x_T in a fixed
compact interior, every fixed approximant fits for all sufficiently
small a, uniformly in v. Hence the convergence in energy is uniform
there and independent of the axial cut j.

Fix epsilon>0 and choose finite h_l with
||h_l-g_l||_E<epsilon for all four dipoles. Equation (11) makes
||Gq_(p,l)-h_l||_E<=2 epsilon eventually. Applying (10) in the
finite cube bounds the error in replacing both Green columns in
q_(p,l)^T G(a A_<j)Gq_(p,m) by h_l,h_m by C epsilon.
For these fixed finite fields the stencil convergence from section 1
gives convergence of their pairing to <h_l,M_x h_m>, uniformly
in j and compact x_T. The frozen energy bound then allows h_l,h_m
to be replaced by g_l,g_m with another C epsilon error. Let epsilon
tend to zero. Fourier transformation of the frozen pairing yields

\[
 a(V^{\rm pl}_p)_{lm}
   =\int {\overline{\widehat\eta_l}m_E(x,\theta)
                         \widehat\eta_m\over\lambda^2}
                         {d\theta\over(2\pi)^3}+o(1),
 \tag{12}
\]

uniformly on every compact transverse interior and all cuts. The
integrand is uniformly bounded: its numerator has magnitude at most
C lambda^2. In particular it is absolutely integrable. Conjugation
and theta->-theta prove that the integral is real and symmetric.
This also proves continuity in x by dominated convergence.

No unweighted finite-box Green approximation, coefficient commutation
or unproved pointwise Green asymptotic was used. The two energy
approximations precede coefficient freezing and control all distant
coefficient rows, rather than only a fixed local preview.

### 3. Retain the full exterior heat kernel

L213(6),(11) express U_i as the complete double heat expansion in
the exterior columns v_(k,a)=a R_F(lambda_(k,a)^(-1/2) f_(k,a)).
For each fixed mode, its smooth relative sine/cosine sampling and
L028(9)'s exact prefix formula give

\[
 a^{-1}(v_{k,a})_\mu(j,v)
       \longrightarrow(\mathfrak r b_k)_\mu(x).
 \tag{13}
\]

Indeed each prefix difference divided by a converges to
partial_mu b_(k,1), and a times the sum of those divided differences
is its lower-anchored integral. Riemann-sum convergence is uniform
over all cuts, including j=N-1. It never compares that last row with
the fixed transverse upper link. On compact transverse interiors,
all four edge samples of p approach the same physical x, leaving
precisely their traversal signs in (8).

L008 supplies convergence of every fixed probe matrix entry to
beta_(i;kl) and a uniform operator bound. L213(11) supplies
|v_(k,a)|/a<=p(k) on every transverse row, including normal end
rows, for a fixed polynomial. The physical spectral gap and lower
eigenvalue estimate give a summable two-mode majorant
C_i p(k)p(l) exp[-c tau(|k|^2+|l|^2)]. Therefore fixed-mode
convergence (13) passes through the complete double sum, proving

\[
 a^{-2}U_{i,p}\longrightarrow\mathcal U_i^{\mu\nu}(x)
 \tag{14}
\]

uniformly on compact transverse interiors and all cuts. The same
majorant proves absolute convergence and continuity of (8), with
the actual lower-prefix constant mode included. This argument uses
the original full-link heat flow on the forest slice, not the
restricted forest Hessian or a nonlinear quotient transfer.

### 4. Control every collar and take the physical Riemann sum

There are global bounds |U_(i,p)|<=C_i a^2 from L213 and
|a V^pl_p|<=C from (10). For the latter, each pinned endpoint
dipole q_e satisfies q_e^T Gq_e<=1, including normal end edges,
by L215(10); a signed traversal changes no energy bound.
Both arguments hold for every row of every transverse plaquette;
fixed rows are zero. The limiting matrices in (6),(8) are bounded
by the estimates already proved.

Rewrite the scaled response exactly as

\[
 a^3T_i^{\rm pl}
   =-24 a^4\sum_{p\in P_T}
                  K:(a^{-2}U_{i,p}):(a V^{\rm pl}_p).
 \tag{15}
\]

For fixed delta>0, restrict anchors to transverse points at least
delta from every transverse face. Equations (12),(14) are uniform
there, for all axial cuts. Thus (15) on that set tends to the
corresponding integral in (9), by a four-dimensional Riemann sum.
The original positive orientation of each plane is used exactly once;
there is no extra axial or color normalization.

The omitted transverse collar contains at most
C(delta a^(-4)+a^(-3)) plaquettes over all axial levels. Its
absolute contribution to (15) is at most C_i(delta+a). The limiting
integral over that collar is at most C_i delta. Take a->0 first
and then delta->0 to obtain (3),(9). Axial levels 0,N have fixed
transverse links and contribute zero; adding their one-sided traces
to a Riemann interpolation changes no integral. All normal end rows
and upper-adjacent cuts have consequently been accounted for. No
smooth extension through a fixed upper link has been made.

### 5. Scope, duplicates and remaining test

The unchanged ready EXPLORE assessment
`drafts/literature/2026-10-16-complete-residual-coefficient-cubic-assembly.md`
covers the complete L025 target and its intermediate signed estimates.
L101 already proves the cumulative identity and its coefficient
limit; these are imported with their exact hypotheses rather than
reproved. L042 supplies the energy-projection method, specialized
above to the present four signed dipoles and uniform axial cuts.
Neither earlier statement evaluates (2). The new local work is the
applicability argument and the complete plateau response limit,
classified REPRODUCTION without claiming an advance beyond the
checked sources. No new mathematical script or numerical sign input
is needed. The meaningful checks are the shared axial cut, cut
endpoint term, bilinear energy convergence, complete heat majorant,
traversal/color signs, -24 factor and the collar count in (15).

Let T_i^dm be the contribution of the untouched direct/direct and
both mixed terms in L215(15), with the original K,U_i and signs.
Then L213,L215 and (3) give only

\[
 a^3 G_i^{\rm nr}=P_i+a^3T_i^{\rm dm}+o(1).
 \tag{16}
\]

Thus the still-complete action limit exists exactly when the retained
sum T_i^dm has a finite scaled limit. L214 bounds that sum at cubic
scale; boundedness is not convergence. No separate mixed-row limit,
actual-probe sign or compensation is inferred. A continuation must
retain both mixed orientations and meet a uniform summed o(N^3)
replacement threshold. The recorded bounded-raw-loop and upper-pin
failures remain applicable to any proposed shortcut.

## Mathlib

Full coverage of this specialized signed forest-action plateau limit:
**not checked**. Supporting Fourier/Parseval identities, finite
Dirichlet energy projection, dominated convergence and Riemann sums:
**not checked**. Unknown coverage is not evidence of absence. No
matching Mathlib theorem or certified originality is asserted.
