# L289 — Quadratic asymptotic of the complete cubic mixed-covariance action group

## Hypotheses

Use L287–L288's SU(2) relative cube D=[-4,4]^4, even N>=2,
a=8/N, boundary-contained pinned links, boundary-fixed gauges and every
variable normal link at both endpoints. Matrices use Euclidean counting
measure and pinned slots are zero. Keep all three colors, both source
orders, and L282's exact nonnegative product bump h_+=f_* and
h_-=theta f_*, with supports [-1/4,1/4]^3 times [1,2] and [-2,-1].
Source derivatives are at zero in
(|s|+|t|)||f_*||_infinity<eta<1. All ambient all-link Wilson jets
remain on L280's own relative-Coulomb slice.

Use L287(1), (3)–(5)'s exact cubic vertex, internal-curl operator
E_N^int, and complete group

\[
 M_{3,N}=\tfrac14\mathcal B(T,T;G_{-+},G,G).
\]

Use L288's positive polynomial covariance approximation, its complete
operator error and exact bulk agreement. The separate audits of L286–L288
accept those inputs under their stated hypotheses; this extension did
not itself establish their validity. Let S_f>0 and the strong source fields have precisely
L282(3)–(4), (20)–(21)'s meanings. With normalized Brillouin measure set

\[
 \lambda(q)=4\sum_{\mu=1}^4\sin^2(q_\mu/2),\qquad
 I_1=\int_{[-\pi,\pi]^4}\frac{\sin^2q_1}{\lambda(q)^2}
                  \frac{dq}{(2\pi)^4}.
                                                               \tag{1}
\]

This is the same finite positive integral used in L285; retain its
Z_0 and J_f for the comparison below. Values at q=0 are irrelevant.

## Conclusion

The ENTIRE mixed-covariance action/action group, including all internal
vertex pairs, all relative boundary rows, colors and both source orders,
has the limit

\[
 \boxed{\displaystyle
 \lim_{N\to\infty,\ N\ {\rm even}}N^{-2}M_{3,N}
              =\frac9{16}I_1\mathcal S_f>0.}                 \tag{2}
\]

The error is o(N^2) for this complete group. More precisely, the
one-color block of E_N^int converges on smooth sampled fields, and in
pairings of L282's strongly convergent discrete fields, to multiplication
by e_*=24 I_1. Therefore the subtotal with L285(4) is

\[
 \boxed{\displaystyle
 \lim N^{-2}\{M_{3,N}+\mathcal K_4^H+
                          \operatorname{Tr}(DG_{-+})\}
 =\frac{Z_0}{64}\mathcal J_f.}                              \tag{3}
\]

The S_f coefficient cancels exactly in this subtotal. The cubic
insertion/insertion group is
O(1) by L286(1) and hence has zero
normalized limit. The two mixed insertion/action groups and the
G_-/G_+ distinct-line cubic group remain unresolved. In particular (3)
is not the complete cubic or interacting coefficient. No complete cubic
compensation, subleading bound, mesh-uniform higher remainder, continuum axioms or
positivity, nonzero physical sector, or finite positive mass is proved.
This is partial local progress under the prior EXPLORE assessment,
not certified originality or a complete-solution candidate. The separate
audit in section 5 accepts this limit under the stated hypotheses.

## Proof

### 1. Constant external fields in the exact Wilson cubic jet

L287(1) gives V(x)=sum_p (Cx)_p dot zeta_p(x), with
zeta_p=1/2 sum_{j<k}[X_{p,j},X_{p,k}] in matrix notation. All formulas
below are on the full infinite lattice, or on a sufficiently large
periodic lattice used only to compute its finite-range row sums.
They do not change the boundary conditions of the actual relative box.

For a positively oriented mu,nu plaquette based at n, write its four
signed slots as

\[
 A=x_\mu(n),\quad B=x_\nu(n+\hat\mu),\quad
 C=-x_\mu(n+\hat\nu),\quad D=-x_\nu(n),\quad y=A+B+C+D.
\]

For an external constant matrix U in direction mu, its signed slots
are (U,0,-U,0). Direct differentiation of the six brackets gives

\[
 D\zeta_p(x)[U_\mu]
   =[U,B+(A+C)/2]=[U,y/2+(B-D)/2].                         \tag{4}
\]

For an external constant matrix W in direction nu, the slots are
(0,W,0,-W), and the corresponding expression is
[W,C+(B+D)/2]=[W,y/2+(C-A)/2]. The invariant color inner product
satisfies y dot [U,y]=0. Consequently the contribution of this
plaquette to mathsf B(u;x) is exactly

\[
 y_{\mu\nu}\mathbin{\cdot}
 \left([u_\mu,\operatorname{av}_\mu x_\nu]
       -[u_\nu,\operatorname{av}_\nu x_\mu]\right),          \tag{5}
\]

where av_mu x_nu=(x_nu(n+mu)+x_nu(n))/2; av_nu is analogous.
The equality follows from the actual signed slots, not a continuum
approximation. For nu<mu, reversing the orientation label changes both
the curl sign and the external-mu bracket sign, giving the same
fixed-mu contribution for every nu!=mu. Also Cu=0 for constant fields,
so mathsf A(u;x)=0
and this is the complete directional derivative of the cubic action.

### 2. Bulk row sum of the positive polynomial approximant

Write h=h_m from L288(2). In midpoint Fourier coordinates, with each
component indexed by its actual edge center and each curl by its
plaquette center, put

\[
 d_\mu=2\sin(q_\mu/2),\quad c_\mu=\cos(q_\mu/2),\quad
 P=I-dd^{\mathsf T}/\lambda,\quad
 \gamma_m=\lambda h(\lambda)^2.
\]

The covariance widehat G_m=C*C h(L)^2 has one-color multiplier
Gamma_m=gamma_m P for q!=0, and zero at q=0. This follows directly
from C(q)x having components i(d_mu x_nu-d_nu x_mu), so C*C has
multiplier lambda I-dd^T and L has multiplier lambda I.
The averaging in (5) has multiplier c_mu with these precise midpoints.
Thus all original raw-edge phases have been retained.

Take u_mu=u_mu^0 t^A for one fixed unit color A and arbitrary real
numbers u_mu^0. With t^a=i sigma^a/2, define
(J_A)_{ac}=epsilon_{Aac}; then [t^A,x]^a=(J_A)_{ac}x^c.
Here J_A is real antisymmetric and Tr(J_A^2)=-2. For a fixed direction
mu the unsymmetrized spatial kernel from (5) is

\[
 -ic_\mu\left(d_\mu(I-e_\mu e_\mu^{\mathsf T})
                -e_\mu(d-d_\mu e_\mu)^{\mathsf T}\right).
\]

Indeed the first term comes from d_mu x_nu(-q)x_nu(q), summed over
nu!=mu, and the second from -d_nu x_mu(-q)x_nu(q).
Interchanging the two real field factors sends q to -q and transposes
both the spatial kernel and J_A. Since d is odd, c is even and J_A
is antisymmetric, the effective spatial matrix is its symmetric part.
Consequently the real quadratic form mathsf B(u;x) has Fourier matrix

\[
 K_u(q)=-iH_u(q)\otimes J_A,\qquad
 H_u=\sum_\mu u_\mu^0 c_\mu A_\mu,\qquad
 A_\mu=d_\mu I-\tfrac12(e_\mu d^{\mathsf T}+d e_\mu^{\mathsf T}).
                                                               \tag{6}
\]

This matrix is Hermitian and K_u(-q)=K_u(q)^T, as required for a
real symmetric quadratic form. In particular, no factor 1/2 has been
introduced into the definition of mathsf B. Because Pd=0,

\[
 PA_\mu P=d_\mu P,\qquad
 PH_uP=\left(\sum_\mu u_\mu^0\sin q_\mu\right)P,
 \quad \operatorname{Tr}P=3 \quad(q\ne0).                   \tag{7}
\]

These are identities for the full transverse matrix, not a replacement
by scalar covariances.

For precision, perform this calculation on odd periodic tori with side
length ell and then let ell tend to infinity at fixed m. There is no
Nyquist representative issue; q=0 has zero covariance. A real Gaussian
quadratic form x^T K x has variance 2 Tr(K Gamma K Gamma), by its two
crossing Gaussian pairings. Here it is centered since Tr J_A=0. Its
application to (6), followed by L288(1)'s extra factor two in E^int,
gives the quadratic form per lattice volume

\[
 \begin{split}
 \frac{2\operatorname{Var}(\mathsf B(u;x))}{\ell^4}
 &=\frac{24}{\ell^4}\sum_q\gamma_m(q)^2
                    \left(\sum_\mu u_\mu^0\sin q_\mu\right)^2.
 \end{split}                                                   \tag{8}
\]

Explicitly, (-i)^2 Tr(J_A^2)=2, while
Tr(H_u P H_u P)=3(sum_mu u_mu^0 sin q_mu)^2. The two Gaussian
pairings and E=2 covariance multiply this by four, giving 24.
As an independent real-mode normalization check, a nonzero q,-q pair
in one transverse polarization and the two colors perpendicular to A
has independent cosine/sine coefficients of variance gamma_m. Its
quadratic form is, up to an overall sign,
2s(B_1 A_2-A_1 B_2), s=sum_mu u_mu^0 sin q_mu. Its variance is
8s^2 gamma_m^2. Multiplication by two and by three polarizations
agrees with the two q terms in (8).

For fixed m, all covariance and vertex paths have finite range by
L288. Once ell exceeds twice their complete path range, the periodic
kernel entries in the row sum are precisely the infinite-lattice
entries, with all finite displacements counted. Translation invariance
then identifies the left side of (8) with u^T R_m u, where R_m is
the bulk row-sum matrix on constants. Global color rotations make it
scalar in color, as in L287 section 3. Letting ell tend to infinity
turns the finite Fourier sum into its integral. Off-diagonal direction
terms vanish by oddness in q_mu; permutation symmetry makes the four
diagonals equal. Thus

\[
 R_m=e_m I,\qquad
 e_m=24\int\sin^2q_1\,\lambda(q)^2h_m(\lambda(q))^4
                              \frac{dq}{(2\pi)^4}.          \tag{9}
\]

This extraction does not assume hypercubic invariance of the isolated
internal-curl operator on nonconstant fields. It computes its entire
constant-field matrix instead.

Since 0<=lambda h_m<=1 and lambda h_m tends to one at every q!=0,
the integrand in (9) is bounded by 24 sin^2q_1/lambda^2<=24/lambda.
On [-pi,pi]^4, lambda>=(4/pi^2)|q|^2; the latter bound is integrable
in four dimensions. Dominated convergence proves

\[
 e_m\longrightarrow e_*=24I_1>0.                            \tag{10}
\]

### 3. Relative boundary control and strongly convergent source fields

Suppress the scalar color block. L288 gives
||E_N^int-E_{N,m}^int||<=K/(m+1) and both operator norms <=K,
uniformly on the whole relative box. At fixed m the row range and
number of entries in a row are bounded by constants depending only
on m. Hence its absolute row sum is uniformly bounded, for example
by K times the square root of that number. Rows whose complete paths
avoid the boundary have exactly the bulk kernel used in (9).

Let S_a v be samples of a smooth vector field on all variable edge
centers, with physical norm ||w||_a^2=a^4 sum_e |w(e)|^2. On such an
interior row, replacing every neighboring component value by its
value at the row's center incurs error O_{m,v}(a), using finite range
and the bounded absolute row sum. The row sum is e_m I, so
E_{N,m}^int S_a v-e_m S_a v has that error there. All exceptional
rows lie within a fixed-m lattice distance of a face. There are
O_m(N^3) such edges, including normal end links, face intersections
and corners. On those rows both terms are uniformly bounded by the
row bound and ||v||_infinity. Their squared physical norm is at most
O_{m,v}(a^4 N^3), which tends to zero. Therefore

\[
 \|E_{N,m}^{\rm int}S_a v-e_m S_a v\|_a\longrightarrow0
                                          \quad(m\text{ fixed}).
                                                               \tag{11}
\]

Choose m first and use the whole-box operator bound; then take N to
infinity in (11); finally let m tend to infinity using (10). Riemann
sum bounds for ||S_a v||_a show

\[
 \|E_N^{\rm int}S_a v-e_*S_a v\|_a\longrightarrow0.          \tag{12}
\]

This does not delete a shrinking layer of the original nonlocal
operator. Its boundary control comes from the uniform operator
approximation before either limit is removed.

Finite sums of continuum relative tensor modes are smooth and dense
in L2. L282's notion of strong discrete convergence is approximation
by samples of those sums in physical norm. Approximating two strongly
convergent sequences by such samples, and bounding both errors by
K and Cauchy–Schwarz, extends (12) to

\[
 \langle Y_a,E_N^{\rm int}Z_a\rangle_a
       \longrightarrow e_*\langle Y,Z\rangle_{L^2}.         \tag{13}
\]

The continuum inner products and sampled inner products of the finite
sums agree in the limit by Riemann sums. No boundary trace or pointwise
boundary value of Y,Z is assumed. In particular L282(20)–(21) supplies
(13) for every fixed external spatial mode's actual fields
X_{pm,k,a}=aGC* sigma_{pm,k,a} and limits X_{pm,k}.

### 4. Complete source sum and comparison

Let M_{3,N}^int=Tr(E_N^int G_-+)/4. Use L287(14), (17)'s exact
source factorization and the mode sum of L282(22). Including all
three external colors and two equal source orders gives

\[
 N^{-2}M_{3,N}^{\rm int}
   =\frac3{128}\sum_{k\in\mathcal K_N}b_{k,a}
       \langle X_{+,k,a},E_N^{\rm int}X_{-,k,a}\rangle_a.    \tag{14}
\]

Here the matrix in the pairing is its one-color block. The factor is
(3 colors)(2 source orders)/4, followed by 1/(a^2N^2)=1/64.
The mode matrix contributes a^4; each U_pm v contributes a^-1 X_pm.
Internal colors are already included in E^int and are not counted again.
There is no extra a^4 in the original Wilson plaquette sums.

For a fixed finite |k|<=R, (13), b_{k,a}->b_k and L282's source-field
convergence give the limit of (14) with E^int replaced by e_*.
L287(6) bounds the complete normalized external tail of M_{3,N}^int
by C_f C_sep(>R), uniformly in N. Its proof also bounds the sum of
absolute discarded mode contributions; every internal vertex pair
remains in the operator. The limiting scalar series is absolutely
convergent by L282(4) and its proof. Taking R to infinity after the
finite-mode limits therefore yields

\[
 \lim N^{-2}M_{3,N}^{\rm int}
       =\frac{3e_*}{128}\mathcal S_f=\frac9{16}I_1\mathcal S_f.
\]

Finally L287(5) bounds M_{3,N}-M_{3,N}^int by
O_f(N sqrt(log(eN))+log(eN))=o(N^2), proving (2).
Adding the established complete quartic-plus-density limit L285(4)
initially gives

\[
 \frac{10Z_0-1-16I_1}{128}\mathcal J_f
  +\frac3{32}\left(\frac14-2Z_0+4I_1\right)\mathcal S_f.
                                                               \tag{15}
\]

The elementary integral simplification needed for this comparison is

\[
 2I_1=\int\frac{\cos q_1}{\lambda(q)}\frac{dq}{(2\pi)^4}
       =Z_0-\frac18.                                       \tag{16}
\]

To justify its integration by parts at the only singular point,
remove a ball of radius epsilon about q=0 and integrate
partial_1(sin q_1/lambda)=cos q_1/lambda-2 sin^2q_1/lambda^2
on the remaining cube. Both terms are O(|q|^-2) and hence integrable.
The outer face flux is zero, since sin q_1 vanishes on its two
corresponding faces and the other faces have zero first normal
component. The small-sphere flux is O(epsilon^2), because
|sin q_1/lambda|=O(epsilon^-1) and the surface area is
O(epsilon^3). Letting epsilon decrease to zero proves the first
equality. For the second, symmetry and
sum_mu(1-cos q_mu)=lambda/2 give
integral (1-cos q_1)/lambda=1/8. This is a direct evaluation of the
comparison's convergent integrals, not a scalar kernel replacement.

Substituting I_1=Z_0/2-1/16 in (15) makes its S_f coefficient zero
and its J_f numerator 2Z_0, proving (3). No statement about the other
three cubic groups or their compensation was used. This exact partial
cancellation does not imply a smaller scale for their complete sum.

### 5. Separate critical audit (2026-10-26)

This audit accepts (2)–(3), conditional on the preceding audited
finite-box estimates and L282's strong fields, series and strict sign.
It verifies the bulk tensor and the complete limit rather than using
L291's conditional cancellation as evidence for them.

Differentiating the six ordered brackets for constant signed slots
(U,0,-U,0) gives [U,B]+[U,A+C]/2. The other direction gives
[W,C]+[W,B+D]/2. Removing only the terms y dot [U,y] and
y dot [W,y], which are identically zero by the invariant color
inner product, gives (5) with the actual endpoint averages. The
midpoint Fourier derivative and average are i d_mu and c_mu.
Real quadratic symmetrization then gives A_mu in (6); it does not
introduce another factor into B. With the stated generators,
J_A is antisymmetric, Tr J_A^2=-2, and -i H_u tensor J_A is
Hermitian with the required reality condition at -q.

Projection on both sides gives PA_mu P=d_mu P. Thus the spatial
trace is 3(sum u_mu sin q_mu)^2. The color trace contributes
(-i)^2 Tr J_A^2=2; two Gaussian pairings and E=2 covariance
give another factor four. This independently checks 24 in (8)–(9).
The q=0 covariance is zero, and using the entire q,-q pair counts
real modes exactly once as in the displayed real-mode check.
At fixed m, polynomial locality makes the periodic row sum equal
to the infinite-lattice one once no finite path wraps. Oddness
removes off-diagonal directions and permutation symmetry equates
the diagonal integrals. The bound sin^2(q_1)/lambda^2<=1/lambda
is integrable in four dimensions, so e_m tends to 24 I_1.

For fixed m, a row has a bounded number of entries and a uniform
operator bound, hence a bounded absolute row sum. Smooth-field
freezing has O_m(a) error on interior rows. Only O_m(N^3) rows
are exceptional; their bounded entries contribute O_m(a^4 N^3)
to the squared physical error, including all normal end links and
corners. Crucially this is done for E_m, after the uniform K/(m+1)
comparison on the entire original box. It is not a boundary cutoff
of E itself. Approximation by finite relative tensor modes and the
same operator bound extend the conclusion to L282's actual strong
fields, without requiring their pointwise boundary traces.

For the complete source sum, the exact separated matrix contributes
a^4 b_(k,a), each source field contributes a^-1 X_(pm,k,a),
and the counting inner product contributes a^-4. Multiplication
by N^-2 therefore leaves 1/(a^2 N^2)=1/64. Three colors, two
orders and 1/4 give 3/128 in (14). Fixed-mode convergence followed
by L287's uniform absolute tail verifies the full limit, not a
truncated source result. Its external-curl error is o(N^2).

Lastly the punctured-domain integration by parts in (16) is valid:
both integrands are O(|q|^-2), the small-sphere flux is O(epsilon^2),
and the outer flux vanishes. Symmetry gives the remaining 1/8.
Substitution into (15) makes its S_f coefficient zero and leaves
2 Z_0/128 on J_f. No rate for these limiting steps, no other cubic
group and no uniform higher perturbative remainder follows.

## Mathlib

Coverage of the full Wilson-specific finite relative-box asymptotic is
not checked; no absence or matching-theorem claim is made. The exact
cubic jet and finite Gaussian pairing are reused from L287; the uniform
positive-covariance approximation and path locality from L288; strong
source-field convergence, normalization and scalar series from L282;
and the comparison coefficient from L285. Fourier orthogonality is
used on finite periodic tori only to evaluate the bulk polynomial
row sum, with its color and real-mode factors displayed. No external
scalar kernel, renormalization theorem, nonlinear forest transport or
continuum construction is imported or reproved. The uncovered work
is this complete internal-curl bulk tensor and relative-box source
limit within the previously approved scope.
