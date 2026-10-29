# L282 — Negative quadratic asymptotic of the complete relative density response

## Hypotheses

Use precisely L280's finite SU(2) box: even N>=2, a=8/N,
all boundary-contained links pinned, gauge transformations fixed on
boundary vertices, and every remaining link, including normal end
links, variable. Sources and their derivatives have L280's real domain
(|s|+|t|)||f_*||_infinity<eta<1. All derivatives below are at zero.
D_N is the complete one-color matrix L280(16), including the Haar
term and both determinant terms. In Tr(D G_-+) it is tensored with
the three-color identity, and G_-+ includes both orders in L280(18).
No nonlinear jet is transferred between slices.

Use the EXACT bump f_* of L002, not merely an arbitrary nonnegative
function with the same support. Its additional property needed for
strict nonvanishing here is the space/time product

\[
 f_*(x,t)=\rho(x)\tau_0(t),\quad
 \rho(x)=\prod_{j=1}^3\frac4I b(4x_j),\quad
 \tau_0(t)=\frac2I b(2t-3),\quad
 I=\int_{-1}^1b(u)du,
 \qquad
 b(u)=\begin{cases}e^{-1/(1-u^2)},&|u|<1,\\0,&|u|\ge1.
 \end{cases}                                                   \tag{1}
\]

This is a narrow use of L002's explicit test, not its infinite-volume
covariance result. Retain L003's relative modes and L281's exact
separated-mode expansion and uniform tail estimate. Their conclusions
are used as recorded; the separate audit in section 6 below also checks
L281's bound and external tail as essential inputs.

## Conclusion

On [-pi,pi]^4 with normalized measure dq/(2pi)^4 define

\[
 \lambda(q)=4\sum_{\mu=1}^4\sin^2(q_\mu/2),\qquad
 d_*=-\frac18-\int\frac{\sin^2q_1}{\lambda(q)^2}\frac{dq}{(2\pi)^4}<0.
                                                               \tag{2}
\]

The integral is finite; the value at q=0 is immaterial. Let the
continuum relative one-form Laplacian \(\mathscr L\) on [-4,4]^4
be defined by L003's tensor sine/cosine modes with frequencies
pi k_mu/8: component mu uses cosine modes (including zero) in mu,
and positive sine modes in every other coordinate. Its inverse is
bounded. Let d* be the adjoint exterior derivative, applied below to
smooth compactly supported 12-forms.

For spatial k in L003's infinite mode set, put

\[
 \begin{split}
 \alpha_k&=(\pi/8)^2(k_1^2+k_2^2),\quad
 \Omega_k=(\pi/8)|k|,\quad
 b_k=\frac{\alpha_k}{\Omega_k\sinh(8\Omega_k)},\\
 \psi_k(x,t)&=\phi_k(x)\sinh(\Omega_k(4-t)),\\
 \sigma_{+,k}&=f_*\psi_k\,dx_1\wedge dx_2,\quad
 \sigma_{-,k}=\theta\sigma_{+,k},\quad
 X_{\pm,k}=\mathscr L^{-1}d^*\sigma_{\pm,k}.
 \end{split}                                                   \tag{3}
\]

The reflection of this spatial two-form has positive orientation.
The following series converges and is strictly positive:

\[
 \mathcal S_f=\sum_k b_k\langle X_{+,k},X_{-,k}\rangle_{L^2}>0.
                                                               \tag{4}
\]

For the ENTIRE density response, with all colors and source orders,

\[
 \boxed{\displaystyle
 \lim_{\substack{N\to\infty\\N\ {
m even}}}
 N^{-2}\operatorname{Tr}(D G_{-+})
       =\frac{3d_*}{32}\mathcal S_f<0.}                         \tag{5}
\]

Thus this density contribution has a nonzero negative N^2 leading
term. This is a statement on the specified relative-Coulomb slice;
it is not a slice-independent assertion about individual summands.
It supplies no cancellation with the cubic/quartic action and insertion
families, no uniform higher remainder, and no continuum interacting
theory or mass gap. The proof below is new local work within the saved
EXPLORE target; originality beyond checked sources is not claimed. The separate audit
in section 6 accepts this density-only result under these hypotheses.

## Proof

### 1. Uniform polynomial approximation on the exact relative domain

Suppress color. B,M,Delta=B*B have L280(1)'s meaning, including zero
extension of vertex fields at every boundary vertex. Write

\[
 P=B\Delta^{-1}B^*,\quad J=M\Delta^{-1}B^*,\quad
 D_N=-\tfrac1{12}I-\tfrac16\operatorname{diag}(P_{ee})
                         +\tfrac14(J_{ef}J_{fe})_{ef}.          \tag{6}
\]

For an integer m>=0 use the polynomial

\[
 h_m(\lambda)=\frac1{16}\sum_{j=0}^m(1-\lambda/16)^j,
 \quad e_m(\lambda)=\lambda^{-1}-h_m(\lambda)
          =\lambda^{-1}(1-\lambda/16)^{m+1}.                   \tag{7}
\]

Replace Delta^-1 in P,J by h_m(Delta) to get P_m,J_m and D_{N,m}
by the full formula (6). In particular the Haar term is unchanged,
and neither determinant term is omitted.

The orthonormal counting-measure vertex sine modes u_k, with all
1<=k_mu<N, have eigenvalues
lambda_k=4 sum_mu sin^2(pi k_mu/(2N)) in (0,16). Directly from the
normalized product modes of L003,

\[
 |u_k(v)|^2\le16/N^4,\quad
 |(Mu_k)_e|^2\le64/N^4,\quad
 |(Bu_k)_e|^2\le16\lambda_k/N^4.                               \tag{8}
\]

For the last inequality the difference in the edge direction is
2 sin(pi k_mu/(2N)) times its normalized midpoint cosine; the other
three factors are normalized vertex sines. This identity also holds
on the first and last normal edges. For M the sum of at most two
vertex values proves the bound, also when one endpoint is zero.
Thus (8) does not delete either endpoint case.

Here are explicit uniform spectral controls. Put

\[
 \begin{split}
 S_0&=15/8,\\
 s_m&=\sup_{N\ge2}\frac1{N^4}\sum_k
       \frac{(1-\lambda_k/16)^{2m+2}}{\lambda_k},\\
 t_m&=\sup_{N\ge2}\frac1{N^4}\sum_k
                      (1-\lambda_k/16)^{m+1}.
 \end{split}                                                   \tag{9}
\]

The bounds are valid for all integer N, hence for even N. There are
at most 15 r^3 indices with max k_mu=r, and lambda_k>=4|k|^2/N^2.
Consequently N^-4 sum lambda_k^-1<=15/8. If lambda_k<=delta, then
max k_mu<=N sqrt(delta)/2; summing r up to this bound gives
N^-4 sum_{lambda<=delta} lambda^-1<=15 delta/16. When the upper
bound is below one the sum is empty; otherwise sum_{r=1}^M r<=M^2.
The number of such indices divided by N^4 is at most delta^2/16.
For any 0<delta<16 it follows that

\[
 \begin{split}
 s_m&\le15\delta/16+S_0(1-\delta/16)^{2m+2},\\
 t_m&\le\delta^2/16+(1-\delta/16)^{m+1}.
 \end{split}                                                   \tag{10}
\]

First choosing small delta, then large m, proves s_m,t_m->0.
No mesh limit or inverse-square full-space theorem is used here.

Set E_m=e_m(Delta) and Z=M E_m B*=J-J_m. Since ||M||<=4, (8) gives

\[
 (ZZ^*)_{ee}\le64s_m,\qquad (Z^*Z)_{ee}\le256s_m.              \tag{11}
\]

Indeed ZZ*=M E_m Delta E_m M*, whereas
Z*Z<=16 B E_m^2 B*. The same computations for J and J_m give
row squared norms <=64 S_0 and column squared norms <=256 S_0;
use 0<=h_m(lambda)<=lambda^-1 for J_m. Also
0<=P_m<=P<=I and

\[
 \sup_e|(P-P_m)_{ee}|\le16t_m.                               \tag{12}
\]

To compare the product matrices, write
J_ef J_fe-(J_m)_ef(J_m)_fe=Z_ef J_fe+(J_m)_ef Z_fe.
Cauchy–Schwarz on each row, using (11) and the corresponding column
bounds, gives an absolute row sum at most 256 sqrt(S_0 s_m).
The difference is symmetric, so its operator norm is bounded by this
row sum. We obtain the uniform complete-density error

\[
 \sup_N\|D_N-D_{N,m}\|\le
 \varepsilon_m:=\tfrac83t_m+64\sqrt{S_0s_m}\longrightarrow0.    \tag{13}
\]

The same row bounds imply, for every N,m,

\[
 \sup_e\sum_f|(D_{N,m})_{ef}|\le\tfrac14+32S_0=241/4.         \tag{14}
\]

These are bounds on all internal anchors, including diagonal and
near-diagonal pairs, face intersections and every normal link. In
particular they justify approximating the original finite-domain
matrix; a translation-invariant replacement has not been assumed.

### 2. Finite-range bulk calculation and its boundary error

For fixed m, h_m(Delta) is a polynomial in a nearest-neighbor matrix.
Thus P_m,J_m,D_{N,m} have finite range, bounded by a constant R_m
independent of N (R_m=2m+4 suffices in lattice coordinate distance).
Rows whose R_m-neighborhood stays inside the box are exactly the
corresponding infinite-lattice rows. This is an exact polynomial
path identity, not an asymptotic Green-function assertion.

Compute their row sums by finite Fourier orthogonality, indexing each
oriented edge by its tail and direction. B has symbol
b_mu(q)=1-e^{iq_mu}, and M has symbol m_mu(q)=1+e^{iq_mu}.
The symbol of J_m in directions mu,nu is
m_mu(q) conjugate(b_nu(q)) h_m(lambda(q)). Therefore

\[
 \begin{split}
 (P_m)_{ee}^{\rm bulk}
   &=\int4\sin^2(q_\mu/2)h_m(\lambda(q))\frac{dq}{(2\pi)^4},\\
 \sum_{f\parallel\nu}(J_m)_{ef}(J_m)_{fe}
   &=-4\int\sin q_\mu\sin q_\nu\,h_m(\lambda(q))^2
                                      \frac{dq}{(2\pi)^4}.
 \end{split}                                                   \tag{15}
\]

The second identity follows by multiplying the finite Fourier
polynomials and selecting zero displacement: the two edge kernels
have reversed displacements. Their product symbol contains
(1+e^{iq_mu})(1-e^{-iq_mu})(1+e^{iq_nu})(1-e^{-iq_nu})
=-4 sin q_mu sin q_nu. There is no unaccounted midpoint phase.
Oddness makes the second integral zero for mu!=nu. Permutation
symmetry makes each diagonal P integral one quarter of integral
lambda h_m. Thus the bulk row-sum matrix on constant vector fields
is d_m times the four-dimensional identity, where

\[
 d_m=-\frac1{12}-\frac1{24}\int\lambda h_m(\lambda)
                  \frac{dq}{(2\pi)^4}
              -\int\sin^2q_1\,h_m(\lambda)^2\frac{dq}{(2\pi)^4}.
                                                               \tag{16}
\]

On this cube lambda(q)>=(4/pi^2)|q|^2, and sin^2 q_1<=|q|^2.
Hence sin^2 q_1/lambda(q)^2 is bounded by a constant times |q|^-2,
which is integrable in dimension four. Since 0<=lambda h_m<=1,
dominated convergence in (16) proves d_m->d_* of (2). The last
integral in (2) is positive, although d_*<0 already follows from
its -1/8 term.

Let S_a v denote values of a smooth vector field on the four relative
edge grids, and put ||v_a||_a^2=a^4 sum_e |v_a(e)|^2. For fixed m,
interior rows and (14) imply
D_{N,m}S_a v-d_m S_a v=O_v(a R_m) pointwise there, by replacing
values at neighboring edges by the corresponding component at the
row edge's center. The boundary layer has O_m(N^3) edges; on it
both terms are uniformly bounded by (14) and boundedness of v.
Its squared physical norm is O_{m,v}(a^4 N^3)->0. This includes all
faces and their intersections, with normal edge values retained.
Therefore

\[
 \|D_{N,m}S_a v-d_m S_a v\|_a\longrightarrow0\quad(m\ {
m fixed}).
                                                               \tag{17}
\]

Combining (13), (17), d_m->d_* and the Riemann-sum norms of v gives

\[
 \|D_NS_a v-d_*S_a v\|_a\longrightarrow0.                    \tag{18}
\]

The order is: first fix m and take N->infinity, then m->infinity.
A shrinking boundary layer for the original nonlocal inverse was
never postulated. It follows from its uniform approximation (13).

We will also use (18) for strongly convergent discrete fields. Here
this means approximation in physical norm by samples of finite sums
of the continuum relative modes: if Y_a tends to Y, such a finite
sum v can approximate Y in L2 and Y_a in limsup physical norm to
arbitrary accuracy. The uniform norm bound ||D_N||<=241/4 from
L280(25) and (18), followed by this finite-mode approximation, give

\[
 \langle Y_a,D_N Z_a\rangle_a
       \longrightarrow d_*\langle Y,Z\rangle_{L^2}             \tag{19}
\]

whenever both sequences converge in this sense. Inner products of
the approximating finite sums converge by ordinary Riemann sums;
the two approximation errors are bounded by the uniform operator
norm and Cauchy–Schwarz. Thus (19) requires no pointwise assertion
about the continuum fields at the boundary.

### 3. Strong convergence of each actual source-generated edge field

For fixed spatial k use L003's exact discrete psi_{k,a} and set
sigma_{+,k,a}=f_* psi_{k,a} on 12-plaquettes, zero on other components;
reflect to obtain sigma_{-,k,a}. These are defined for all sufficiently
large N. With unscaled C and extended transverse G, put

\[
 X_{\pm,k,a}=aGC^*\sigma_{\pm,k,a}
     =(L/a^2)^{-1}(C^*/a)\sigma_{\pm,k,a},\quad
 L=C^*C+BB^*.                                                \tag{20}
\]

The equality uses C* sigma in ker B* and L^-1=G+B Delta^-2 B*,
L280(23). It is only a quadratic identity. The relative Laplacian
is retained; it is not replaced by scalar Dirichlet inverses for
all edge components.

For fixed k, gamma_{k,a}->Omega_k and the spatial modes are samples
of the same smooth functions as in L003. On the compact source support
psi_{k,a} and every fixed derivative converge to psi_k. Difference
quotients therefore show that (C*/a)sigma_{pm,k,a} converges to
samples of d* sigma_{pm,k}, with vanishing physical norm error.
These source norms are uniformly bounded. The supports stay a fixed
positive distance from every boundary, so no boundary difference
quotient has been extended incorrectly.

For clarity, strong convergence after applying the inverse in (20)
can be checked without an elliptic convergence theorem. The physical
normalized relative tensor modes are restrictions of the continuum
modes. Each fixed coefficient of the source converges by a product
Riemann sum, and its eigenvalue lambda_k/a^2 tends to
sum_mu(pi k_mu/8)^2. L280(21) gives
lambda_k/a^2>=|k|^2/16, including a zero index in an edge direction.
Thus the physical norm of the inverse applied to the source's
|k|>R modes is at most 16 R^-2 times its bounded source norm.
The continuum inverse has the same bound, since its eigenvalues are
(pi/8)^2|k|^2. Fixed finite coefficients converge and these tails
vanish. Consequently

\[
 X_{\pm,k,a}\longrightarrow X_{\pm,k}
       \quad\hbox{strongly in the sense used in (19)}.         \tag{21}
\]

This argument retains the midpoint cosine zero modes and both normal
endpoints. All one-form modes have three positive indices, so no
zero eigenvalue or unstated inverse on constants occurs.

### 4. Exact normalization and removal of the external cutoff

Use L281's v_{k,a}, U_pm, reflection permutation S, and rectangular
matrix T. On the plus source set v_{k,a}=sqrt(f_*) psi_{k,a}, so
U_+v_{k,a}=GC* sigma_{+,k,a}=a^-1 X_{+,k,a}, and the analogous
minus identity uses U_- S v_{k,a}. L281's exact identity
Tr(D G_-+)=6 Tr(U_+* D U_- T) includes two equal source orders and
three identical color blocks. Inserting its mode sum gives

\[
 N^{-2}\operatorname{Tr}(D G_{-+})
    =\frac6{64}\sum_{k\in\mathcal K_N}
           b_{k,a}\langle X_{+,k,a},D_NX_{-,k,a}\rangle_a.     \tag{22}
\]

Indeed T has the coefficient a^4 b_{k,a}; each source-generated
field contributes a^-1; and a^2 N^2=64. There is no extra a^4 in
L279's original observable.

For a fixed external cutoff |k|<=R, (19), (21) and b_{k,a}->b_k
show that (22)'s truncated sum tends to
(6d_*/64) sum_{|k|<=R} b_k <X_{+,k},X_{-,k}>. L281(16) bounds
the difference between the full expression and its truncation by

\[
 E(R)=\frac{241}{8}\,8^4\|f_*\|_\infty^2
                  C_{\rm sep}(>R)\longrightarrow0,           \tag{23}
\]

uniformly in even N. The same argument bounds absolute mode tails:
by L281(9)–(10),

\[
 \|X_{\pm,k,a}\|_a^2
 \le\frac{64\|f_*\|_\infty}{12}
                   a^4\|v_{k,a}\|^2.
\]

Reflection makes the two right sides identical. Multiplying by
b_{k,a}>0 and ||D_N||<=241/4, and summing the diagonal mode tail
as in L281(15), gives (23) also for the sum of absolute contributions
in (22). Passing to fixed finite partial tails, then their supremum,
proves absolute convergence of the limiting series. Taking R large
after the finite-mode limits proves (5) with the series (4), subject
only to the sign check next. Every internal density anchor remained
untruncated throughout this use of the external tail bound.

### 5. Strict sign for the specified bump

Use (1). For a fixed spatial k write

\[
 w_k(x)=\rho(x)\phi_k(x),\qquad
 \tau_k(t)=\tau_0(t)\sinh(\Omega_k(4-t)).
\]

Then sigma_{+,k}=w_k tau_k dx_1 wedge dx_2, and tau_k is
nonnegative, nonzero, and supported in [1,2]. Its adjoint derivative
has only components 1 and 2, equal to (partial_2 w_k)tau_k and
-(partial_1 w_k)tau_k, respectively. For each component expand the
spatial factor in its orthonormal relative spatial modes E_{mu,l}:
cosines in direction mu, sines in the other two, with coefficients
c_{mu,l}. Their spatial eigenvalues beta_{mu,l}^2 are strictly positive.
The time coordinate is a Dirichlet vertex coordinate for both.
Therefore

\[
 \begin{split}
 X_{+,k,\mu}(x,t)&=\sum_l c_{\mu,l}E_{\mu,l}(x)
                                      u_{\mu,l}(t),\\
 u_{\mu,l}&=(-\partial_t^2+\beta_{\mu,l}^2)_{D}^{-1}\tau_k,\\
 X_{-,k,\mu}(x,t)&=\sum_l c_{\mu,l}E_{\mu,l}(x)
                                      u_{\mu,l}(-t).
 \end{split}                                                   \tag{24}
\]

For -4<t,s<4 the continuum Dirichlet kernel is
sinh(beta(min(t,s)+4)) sinh(beta(4-max(t,s))) /
[beta sinh(8 beta)], strictly positive. This is precisely the
continuum interval kernel obtained in L003, with parameter beta.
Hence every u_{mu,l}(t)>0 in (-4,4). Spatial orthogonality gives

\[
 \langle X_{+,k},X_{-,k}\rangle
   =\sum_{\mu=1}^2\sum_l c_{\mu,l}^2
           \int_{-4}^4u_{\mu,l}(t)u_{\mu,l}(-t)dt>0.          \tag{25}
\]

To justify equality, first take finite spatial projections in (24),
then use their L2 convergence and Cauchy–Schwarz; the right-hand
partial sums are nonnegative and converge to that inner product.
Strictness holds because w_k is a nonzero smooth compactly supported
function: phi_k is a nonzero product of trigonometric modes and rho
is positive on an open cube. If both partial_1 w_k and partial_2 w_k
vanished, w_k would be independent of those coordinates, contradicting
its compact support and nonzero value. At least one c_{mu,l} is
therefore nonzero. In particular a single admitted mode, for example
k=(0,2,1), already gives a strictly positive summand in (4).

This sign argument relies on the actual space/time product bump.
It does not assert reflection positivity of the inverse-square
operator on arbitrary signed time profiles, nor does ordinary
negative definiteness of a density matrix decide a mixed reflected
pairing. Equations (23) and (25) prove 0<mathcal S_f<infinity, and
(2) completes the negative, finite, nonzero limit (5).

### Scope and source comparison

The known interval modes, their normalization and continuum kernels
are reused from L003; their primary scalar coverage is recorded in
the saved density-asymptotic assessment (Dowker, 1207.2096v2,
sections 7–8, equations (29)–(37)). No new scalar kernel identity is
being reproved. The finite polynomial approximation here supplies
the previously unproved complete-density boundary control; its
finite Fourier calculation uses only orthogonality of exponentials.
No whole-space inverse-square asymptotic, Toeplitz theorem, or gauge
identity is invoked to infer the boundary result. In particular the
dimension-four exclusion noted for Michta–Slade is not bypassed by
assuming its hypotheses: the relevant finite spectral sums are
estimated explicitly in (8)–(13).

The result closes this density-only scale test, not the full
coefficient problem. Achieving an O(log N) or smaller full correction
would require the action/insertion families to compensate the
nonzero term (5), together with their own remainder estimates.
Nothing here establishes such compensation or exchanges the mesh
and coupling limits. The independent continuum and infrared gaps
in PROOF.md remain open.

### 6. Separate critical audit (2026-10-26)

**Verdict.** Equations (2)–(5) pass this audit, including the complete
operator approximation and L281's bound/tail used in their proof. This
is acceptance of an existing local partial result, not a new asymptotic
or a solution of the interacting problem. The audit uses the unchanged
EXPLORE assessment for this exact target. No replacement theorem,
new analytic premise, numerical evidence or new DAG input is required.
The following checks retain the entire relative domain and explain the
load-bearing estimates independently.

**Uniform approximation, including endpoints.** A counting-normalized
vertex eigenvector is a product of four factors sqrt(2/N) sin(pi k j/N).
Each first difference is -2 sin(pi k_mu/(2N)) times the corresponding
midpoint cosine. The formula holds at j=0 and j=N-1 because the vertex
values there are extended by zero at j=0,N. Thus the three bounds in
(8) hold on every variable edge; the sum row for M has no larger bound
when one endpoint is zero. Each interior vertex has eight incident
edges and |u+v|^2<=2|u|^2+2|v|^2, proving ||M||^2<=16.

For positive four-tuples with max k=r the shell count is
r^4-(r-1)^4<=15r^3. Also sin(pi k/(2N))>=k/N, so
lambda_k>=4|k|^2/N^2. Consequently

\[
 N^{-4}\sum_k\lambda_k^{-1}
 \le\frac{15}{4N^2}\sum_{r=1}^{N-1}r
 \le\frac{15}{8}.
\]

For lambda_k<=delta let M_delta=floor(N sqrt(delta)/2).
If M_delta=0 the sum is empty. Otherwise sum_{r<=M_delta}r<=M_delta^2,
which bounds the low-frequency inverse sum by 15 delta/16; the
normalized number of indices is at most M_delta^4/N^4<=delta^2/16.
On the complementary indices, the residual powers are bounded by the
powers of 1-delta/16 in (10). These estimates first let delta decrease,
then m increase, uniformly over all N. They do not approximate the
singular inverse in unweighted operator norm.

Indeed, with E=e_m(Delta), exact multiplication gives
ZZ*=M E Delta E M* and Z*Z<=16 B E^2 B*. Applying (8) bounds their
diagonals by 64s_m and 256s_m. The same calculation with E replaced
by Delta^-1 or h_m(Delta) gives row and column squared norms at most
64S_0 and 256S_0. The diagonal error of P is at most 16t_m since
lambda e_m(lambda)=(1-lambda/16)^{m+1}. Each row of the reversed
entrywise-product error has absolute sum at most

\[
 \sqrt{64s_m\,256S_0}+\sqrt{64S_0\,256s_m}
 =256\sqrt{S_0s_m}.
\]

That error matrix is symmetric. Multiplying by 1/4 and adding the
1/6 diagonal error gives exactly (13). The absolute row sum of each
D_{N,m} is at most 1/12+1/6+(1/4)sqrt(64S_0 256S_0)=241/4.
The same bound holds for D_N. No boundary compression or missing
normal link enters this calculation.

**Bulk contraction and boundary passage.** For fixed m the polynomial
path formula gives finite range and exact equality to infinite-lattice
rows whose whole path neighborhood avoids the boundary. This uses the
standard graph-power locality argument inspected in Benzi–Razouk,
*ETNA* 28 (2007), pp. 24–25, proof of Theorem 3.4; its analytic inverse
decay theorem is not invoked. The explicit weighted estimates above
supply the needed uniformity instead. Here is the relevant primary
[source](https://etna.ricam.oeaw.ac.at/vol.28.2007-2008/pp16-39.dir/pp16-39.pdf).

For a bulk row of direction mu and columns of direction nu, writing
the displacement as r gives sum_r j_{mu,nu}(r)j_{nu,mu}(-r), hence
the integral of the two symbols at the SAME Fourier argument. Their
product is

\[
 m_\mu\overline b_\nu m_\nu\overline b_\mu h_m^2
 =(2i\sin q_\mu)(2i\sin q_\nu)h_m^2.
\]

This verifies the negative sign in (15); using an absolute square
would give an incorrect answer. The mixed-direction integrals vanish
by oddness in one coordinate. Permutation symmetry gives the diagonal
P integral as (1/4) integral lambda h_m. Therefore (16), including
its Haar constant, is correct. The majorant for its last integral is
O(|q|^-2), integrable in four dimensions, and lambda h_m<=1. Dominated
convergence gives exactly d_*=-1/8-integral sin^2(q_1)/lambda^2<0.

For fixed m all shifts of a smooth sampled field in an interior row
are O_v(a R_m); its absolute row bound is uniform. At most O_m(N^3)
edges lie within the required boundary strip, including intersections
of faces and normal endpoints. Their bounded values contribute
O_{m,v}(a^4N^3) to the squared physical error. Thus (17) holds with
m fixed. Next (13), convergence of sampled norms, and d_m->d_* give
(18), taking N first and then m. Finite sums of relative continuum
modes are smooth and dense in L2. Approximating both strongly
convergent fields by such sums and using ||D_N||<=241/4 proves (19).
There is no assertion that the inverse itself has finite range or
that its boundary contribution can simply be deleted.

**Actual generated fields.** Since CB=0, C* sigma is transverse;
L280(23) gives L^-1 C* sigma=G C* sigma. Thus
(L/a^2)^-1(C*/a) sigma=a G C* sigma, verifying (20) and its scale.
For fixed external k, the smooth interpolation of psi_{k,a} converges
with its derivatives on the source support. Applying C*/a is precisely
taking centered differences from the 12-plaquette grid to the component
1 and 2 edge grids. The compact support stays away from every boundary,
so these differences converge in physical norm to d* sigma; all other
components are zero. No remote zero extension is differentiated.

The relative one-form modes sampled on their own grids are exactly
orthonormal for a^4 counting measure, including the constant cosine
in their edge coordinate. Each has three strictly positive vertex
indices. Source coefficients for a fixed mode converge by Riemann
sums; inverse eigenvalues converge to the corresponding continuum
ones. Both discrete and continuum inverse eigenvalues on |j|>R are
at most 16/R^2. Parseval therefore bounds the norm of each inverse
source tail by 16/R^2 times the uniformly bounded source norm.
Finite coefficients followed by this tail establish (21), in exactly
the strong sense required in (19). No uniform control in the external
index k is inferred here; that is supplied separately by L281.

**Normalization and full external tail.** L281's separate input audit
verifies its (4)–(16), including the rectangular factorization and both
source orders. In one color, T=a^4 sum_k b_{k,a} S v_{k,a}v_{k,a}*,
V=U_+*D_N U_-, and U_+v=a^-1 X_+, U_-Sv=a^-1 X_-. Thus its trace
identity gives

\[
 \begin{aligned}
 6N^{-2}\operatorname{Tr}(VT)
 &=6N^{-2}a^4\sum_k b_{k,a}a^{-2}
                      X_{+,k,a}^{\mathsf T}D_NX_{-,k,a}\\
 &=\frac6{a^2N^2}\sum_k b_{k,a}
                      \langle X_{+,k,a},D_NX_{-,k,a}\rangle_a.
 \end{aligned}
\]

Since aN=8 this is (22), with coefficient 6/64. The 6 counts two
orders and three colors; no source-volume factor is missing.

The tail proof also controls absolute terms, not merely cancellation
in their sum. From (9)–(10) of L281,
||X_{+,k,a}||_a^2<=a^6 F N^2 ||v_{k,a}||^2/12
=(64F/12)a^4||v_{k,a}||^2, and reflection gives the same bound for
X_-. Cauchy–Schwarz and ||D_N||<=241/4 imply that the sum of absolute
terms of (22) with |k|>R is at most
(241/8)F a^4 sum_{|k|>R} b_{k,a}||v_{k,a}||^2, bounded by E(R)
in (23). This tends to zero uniformly in N. Passing first to any
fixed finite band R<|k|<=M and then increasing M proves absolute
convergence and the same tail bound for the limiting contributions.
Because d_* is finite and nonzero, it also proves absolute convergence
of (4). The finite-mode limits may consequently be summed, giving
(5) once the next sign check is made.

**Strict sign and scope.** L002's exact constant 128/I^4 equals the
product (4/I)^3(2/I) in (1). Hence w_k is a nonzero compactly supported
smooth spatial function and tau_k is nonnegative and nonzero. The
adjoint derivative has precisely components (partial_2 w_k)tau_k and
-(partial_1 w_k)tau_k. On each of the two component spaces the spatial
relative modes are complete; their two positive sine indices ensure
beta_{mu,l}>0. Time is Dirichlet in both components. Reflection acts
on them without a sign and commutes with the scalar time inverse.

The kernel displayed before (25) is strictly positive for both
arguments in (-4,4); the nonzero nonnegative forcing makes each
u_{mu,l} positive there. Finite spatial projections therefore give
sums of c_{mu,l}^2 times strictly positive integrals. Their L2 limits
justify (25). If every coefficient vanished, both partial_1 w_k
and partial_2 w_k would vanish; independence of those coordinates
contradicts compact support and w_k nonzero. Thus at least one square
coefficient is nonzero. The admitted mode (0,2,1) alone gives a
strictly positive contribution, and all b_k are positive. Together
with the absolute tail this proves 0<S_f<infinity and the strictly
negative finite limit (5).

This does not claim inverse-square reflection positivity for arbitrary
time profiles, nor infer a mixed reflected sign from an ordinary norm.
It validates only the specified SU(2), fixed-box, exact-bump density
response. Action/insertion compensation, a uniform higher remainder,
composite renormalization, a continuum nonzero sector, the field axioms
and finite positive physical mass are still independent unresolved
requirements. No conclusion concerns all compact simple gauge groups.

## Mathlib

Coverage of the full asymptotic and its operator approximation is
**not checked**. Supporting spectral decompositions, finite Fourier
orthogonality, operator norms, dominated convergence and Riemann
sums are used with the explicit arguments above; no matching Mathlib
theorem or formal verification is claimed. Unknown coverage is not
absence. Section 6 records the separate informal critical audit; it is
not a formal verification.
