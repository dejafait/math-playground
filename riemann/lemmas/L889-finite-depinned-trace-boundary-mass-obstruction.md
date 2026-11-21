# Lemma 889: a finite boundary obstruction for depinning traces when the contact slopes have modulus below one

## Hypotheses

Use the actual entire function and positive constants of L847:

\[
G(z)=\tfrac18\xi(\tfrac12+\tfrac{\sqrt z}{2}),\qquad
R>0,\quad RG'(R)/G(R)=1,\quad C=R^2/G(R)^2,
\]
\[
F(z_1,z_2)=-C\frac{G(z_1)G(z_2)(z_1-z_2)^2}{z_1^2z_2^2},\qquad
\omega=C\frac{G(z_1)G(z_2)(z_1-z_2)^2}{z_1^3z_2^3}
                 dz_1\wedge dz_2.                              \tag{1}
\]

Assume exactly L879's smooth real periodic graph hypotheses:
u:T2 -> R2, J=det(I-iDu) nowhere zero, and stationarity of the full
mass for real radial variations compactly supported in its nonzero
density set. Put

\[
z_j=R e^{u_j+iy_j},\quad H=I-iDu,\quad Q=F(z_1,z_2)J,
\quad \mathcal B(u)=(2\pi)^{-2}\int_{T^2}|Q|.
\]

L879 supplies Q=lambda*s with |lambda|=1 and smooth real s.
Assume conditionally L888's clean strip

\[
S=(l,r)\times(c,d),\quad l=\alpha-\epsilon,
\quad r=\beta+\epsilon,\quad\alpha<\beta,\quad\epsilon>0,       \tag{2}
\]

whose compact closure lies in a lifted angular chart. The only
density zeros on that closure are the complete simple G(z1)-zero
fibers at alpha and beta. The factors G(z2), z1-z2 and J do not
vanish there. Thus z1(gamma,y)=zeta_gamma is one fixed simple zero
on each fiber, gamma in {alpha,beta}, and partial_2 u1=0 there.

Let D0=[l,alpha]x[c,d], D1=[alpha,beta]x[c,d], and
D2=[beta,r]x[c,d], all with orientation dy1 wedge dy2. The signs
of s on their interiors are sigma,-sigma,sigma, respectively,
for sigma in {1,-1}. On a fiber, with y denoting y2, define

\[
\eta_\gamma(y)=z_2(\gamma,y),\quad
p_\gamma(y)=\partial_1u_1(\gamma,y),\quad
k_\gamma(y)=\partial_2u_2(\gamma,y),\quad
h_\gamma(y)=\partial_1s(\gamma,y).                         \tag{3}
\]

Here h_gamma is real and nowhere zero. Simplicity and the sign
pattern give h_alpha=-sigma*|h_alpha| and
h_beta=sigma*|h_beta|. These facts are checked below when using
L888's boundary identity.

Let v be smooth, real and compactly supported in S, extended by
zero to the torus. Set u_tilde=u+v and require the finite endpoint
J_tilde=det(I-iD u_tilde) to be nowhere zero. No invertibility
condition is imposed on the intermediate linear homotopy. Write
the real endpoint traces as

\[
a_\gamma(y)=v_1(\gamma,y),\qquad
b_\gamma(y)=v_2(\gamma,y),                               \tag{4}
\]

and use a prime for a y derivative. Both traces vanish near c,d.
All original and new numerator zeros remain in the mass integral.

## Conclusion

There is an exact finite endpoint formula for the interface flux.
For real q and w in C*, set

\[
K_\gamma(q,w)=C\frac{G(\zeta_\gamma e^q)G(w)
                         (\zeta_\gamma e^q-w)^2}
                        {(\zeta_\gamma e^q)^2w^2},
\qquad
D_\gamma(A,w)=\int_0^1(1-t)\partial_qK_\gamma(tA,w)\,dt.   \tag{5}
\]

The letter D_gamma in (5) denotes a coefficient, not one of the
three rectangles D0,D1,D2. It is smooth also at A=0; no division by
A or a G factor is used. Define eps_alpha=2*sigma,
eps_beta=-2*sigma and the real function

\[
W_\gamma(A,B,Z;y)=\varepsilon_\gamma
 \operatorname{Re}\left\{\overline\lambda
 (k_\gamma(y)+i+Z)
 D_\gamma(A,\eta_\gamma(y)e^B)\right\}.                   \tag{6}
\]

With Q_tilde=F(Phi_(u+v))*J_tilde, put

\[
E(v)=\sum_{j=0}^2\int_{D_j}
 \bigl(|Q_{\rm tilde}|-\sigma_j
          \operatorname{Re}(\overline\lambda Q_{\rm tilde})\bigr)
 \ge0,\qquad (\sigma_0,\sigma_1,\sigma_2)=(\sigma,-\sigma,\sigma).
\]

Then, for every finite v under the hypotheses above,

\[
(2\pi)^2\bigl[\mathcal B(u+v)-\mathcal B(u)\bigr]
 =E(v)+\sum_{\gamma=\alpha,\beta}\int_c^d
   a_\gamma(y)^2
   W_\gamma(a_\gamma(y),b_\gamma(y),b_\gamma'(y);y)\,dy.    \tag{7}
\]

In particular, there is no first-trace derivative a_gamma' in this
endpoint expression. The mixed term in L888(15) has been integrated
exactly, not omitted. The coefficient at zero trace is

\[
W_\gamma(0,0,0;y)
  =|h_\gamma(y)|\frac{1-p_\gamma(y)^2}
                         {(1+p_\gamma(y)^2)^2}.           \tag{8}
\]

For the obstruction, impose the following **additional condition**:
there exists 0<=p_*<1 such that

\[
             |p_\gamma(y)|\le p_*
 \quad(\gamma=\alpha,\beta,\ c\le y\le d).               \tag{9}
\]

It is not known to follow from stationarity or to hold for any
realized actual-G datum. Define the finite, data-dependent constants

\[
m=\min_{\gamma,y}|h_\gamma(y)|
             \frac{1-p_\gamma(y)^2}{(1+p_\gamma(y)^2)^2}>0,
\]
\[
L=\max_{\substack{\gamma,\ c\le y\le d\\
                         |A|,|B|,|Z|\le1}}
   \bigl(|\partial_A W_\gamma|+|\partial_B W_\gamma|
                              +|\partial_Z W_\gamma|\bigr)<\infty,
\qquad
\delta=\min\left\{\tfrac12,\frac{m}{2(1+L)}\right\}>0.     \tag{10}
\]

Every admissible finite replacement with

\[
\max_{\gamma}\{
 \|a_\gamma\|_\infty,\|b_\gamma\|_\infty,
                         \|b_\gamma'\|_\infty\}\le\delta   \tag{11}
\]

satisfies the full mass bound

\[
\mathcal B(u+v)-\mathcal B(u)
 \ge\frac{m}{2(2\pi)^2}
       \sum_{\gamma=\alpha,\beta}\int_c^d a_\gamma(y)^2\,dy.
                                                               \tag{12}
\]

The right side is strictly positive whenever at least one first
trace is nonzero. There is no bound on a_gamma', on the size of v
inside the cells, or on its interior derivatives, beyond smoothness
and endpoint admissibility. All collars are included. The proof
gives one explicit finite coupled field satisfying (11), with both
first traces nonzero and J_tilde!=0. It therefore fails the requested
threshold B(u_tilde)-B(u)<0 by a strictly positive margin (12).

This stops that finite depinning construction and all admissible
fillings with the same trace restrictions and (9). It does not stop
large traces, contacts violating (9), or all finite replacements.
If |p_gamma|>1, the coefficient (8) is negative; negative interface
flux by itself still does not pay E(v). At |p_gamma|=1 the argument
gives no positive uniform margin. No actual stationary configuration,
minimizer, compactness theorem, sharp L868 bound, higher sign or RH
claim follows. This is a boundary-calibration specialization under
the ready EXPLORE assessment, classified REPRODUCTION; no progress
beyond the inspected general methods or certified novelty is claimed.
The result and the new endpoint reduction remain unaudited.

## Proof

### Scope, known method and the identity used from L888

The invocation-start assessment is
`drafts/literature/2026-11-07-paired-fiber-finite-replacement-test.md`.
It permits a finite construction on the conditional strip or an
applicable actual-form boundary obstruction, explicitly allowing
both components and requiring all collars and endpoint J!=0. The
extra condition (9) states the subclass tested here. It is not an
assumption silently added to the whole approved target.

Reuse Scott Lawrence and Yukari Yamauchi, *Convex optimization and
contour deformations*, arXiv:2311.13002v2, 14 August 2024,
[Section III, equations (18)-(19), p5](https://arxiv.org/pdf/2311.13002v2#page=5),
for the known closed-form boundary lower-bound method. The forms
on the three cells are sigma_j*Re(conjugate(lambda)*omega), each
dominated by |omega| on every real tangent plane. They are not one
globally closed signed certificate; the internal flux is retained.
No optimization duality, attainment or graph-realization theorem
is imported. The application difference is the finite trace sign
estimate (10)-(12), uniform over arbitrary admissible interiors.

For smooth pullback differentiation reuse Guillemin and Sternberg,
*Semi-classical analysis*, 13 January 2010,
[Sections 13.13-13.14.1, (13.7)-(13.9), pp449-455](https://math.mit.edu/~vwg/semiclassGuilleminSternberg.pdf#page=449).
For the integrated boundary comparison reuse Lebl, *Tasty Bits of
Several Complex Variables*, v4.4, 31 May 2026,
[Appendix C, Theorem C.6 and regularity remark, p224](https://www.jirka.org/scv/scv.pdf#page=224).
Their relevant hypotheses were inspected in the reused assessments.
Here the finite homotopies and coefficients are smooth on compact
parameter rectangles, with images in compact annuli in (C*)^2.
Numerator zeros cause no singularity. Only these standard facts and
elementary compact estimates are used; no new source is required.

L847 supplies the actual form. L879 supplies the phase line and
variation formula. Before using the unaudited L888(8),(15), check
the needed identities as follows. Along a contact fiber,

\[
\partial_1Q=F_{z_1}(\zeta_\gamma,\eta_\gamma)
              \zeta_\gamma(p_\gamma+i)J\ne0.              \tag{13}
\]

The nonzero factors follow from the simple first zero, nonzero
second G factor, distinct coordinates and J!=0. The other terms
contain F=0. Consequently s crosses simply, giving the stated
sigma,-sigma,sigma pattern and signs of h_gamma.

For u_t=u+t*v and Q_t=F(Phi_(u_t))*det(I-iDu_t), L879's
division-free formula is

\[
\partial_tQ_t=\operatorname{div}B_t,\qquad
B_t=-i F(\Phi_{u_t})\operatorname{adj}(I-iDu_t)v.          \tag{14}
\]

It follows from the zero divergence of the adjugate columns and
H_t*adj(H_t)=det(H_t)I, with no division by det(H_t). Its first
component on a fiber equals omega(Psi_t,Psi_y), for
Psi(t,y)=(zeta_gamma*exp(t*a_gamma),eta_gamma*exp(t*b_gamma)).
Indeed the first adjugate row is (1-i u_(t),22, i u_(t),12);
evaluation gives exactly

\[
T_\gamma=\int_0^1\int_c^d
 K_\gamma(t a_\gamma,\eta_\gamma e^{t b_\gamma})
 [a_\gamma(k_\gamma+i+t b_\gamma')
                         -t b_\gamma a_\gamma']\,dy\,dt. \tag{15}
\]

In particular its sign agrees with the positive C in omega (1).
All exterior fluxes are zero by compact support. Integrating (14)
on the three oriented cells gives respective period changes
T_alpha, T_beta-T_alpha and -T_beta. Since each original cell
saturates its signed real-part bound, their weighted sum is
2*sigma*Re(conjugate(lambda)*(T_alpha-T_beta)). Adding the
nonnegative E(v) gives L888(8) with the normalization in (7).
This checks precisely the load-bearing identity; it is not a claim
of an independent audit of the entire L888 write-up.

The L887 fixed-field logarithmic expansion is a comparison, not
an input. L888's pinned class has a=0; the construction below has
a nonzero on both fibers. L883's label primitives and L886's
unpaid chord moments are not used. The named local comparison and
attempt65/69 stops remain unchanged. The present primitive is a
finite radial trace primitive, not an assertion about their signs.

### Exact endpoint reduction, including the mixed trace term

Fix gamma and suppress its subscript. Since G(zeta)=0, K(0,w)=0
for every w in C*. Define

\[
\mathcal A(A,w)=\int_0^A K(q,w)\,dq.                      \tag{16}
\]

This is smooth for real A and holomorphic in w. Differentiation
under this finite integral is justified uniformly on every compact
set of A,w used here. Let w_t=eta*exp(t*b),
ell_t=k+i+t*b', and A_t=mathcal A(t*a,w_t). Since
eta'=eta*(k+i), the chain rule gives

\[
\partial_t(A_t\ell_t)-\partial_y(A_t b)
    =K(ta,w_t)\,[a\ell_t-t b a'].                         \tag{17}
\]

For completeness, the terms with mathcal A_w cancel because
partial_t w_t=w_t*b and partial_y w_t=w_t*ell_t. The terms
A_t*b' cancel as well; the remaining partial_A mathcal A=K
terms are exactly those displayed in (17). Thus no bound or
smallness of a' is needed for this identity.

Integrate (17) over [0,1]x[c,d]. At t=0, mathcal A(0,eta)=0.
At y=c,d the side terms vanish, since the traces are zero in
neighborhoods of both endpoints. Formula (15) therefore becomes

\[
T_\gamma=\int_c^d
 \mathcal A_\gamma(a_\gamma,\eta_\gamma e^{b_\gamma})
                 (k_\gamma+i+b_\gamma')\,dy.             \tag{18}
\]

All boundary terms of the parameter rectangle have been included.
The construction does not select a logarithm of the moving w;
w_t'/w_t=ell_t is an identity of the given nonzero trace. Nor does
it need a global holomorphic primitive on (C*)^2.

The fundamental theorem of calculus twice, followed by integration
over the finite triangle 0<=t<=s<=1, gives

\[
\mathcal A(A,w)
 =A\int_0^1K(sA,w)\,ds
 =A^2\int_0^1(1-t)\partial_qK(tA,w)\,dt
 =A^2D(A,w).                                             \tag{19}
\]

This is exact for either sign of real A and also at A=0. The
integrands and all needed derivatives are continuous and uniformly
bounded on the compact domains involved; Fubini and all
differentiations are justified there. Equations (18)-(19) and the
checked three-cell mass identity give (7).

### Contact coefficient and a finite uniform bound

On the fiber partial_2 u1=0, so the full matrix is lower triangular:

\[
J=(1-ip)(1-ik),\qquad
\lambda h=F_{z_1}(\zeta,\eta)\zeta(p+i)(1-ip)(1-ik).
                                                               \tag{20}
\]

Moreover K(q,w)=-F(zeta*exp(q),w), whence
D(0,eta)=-zeta*F_(z1)(zeta,eta)/2. Using
1-ip=-i(p+i) and k+i=i(1-ik) in (20) yields

\[
(k+i)D(0,\eta)=\frac{\lambda h}{2(p+i)^2},\qquad
\operatorname{Re}(p+i)^{-2}=
                         \frac{p^2-1}{(1+p^2)^2}.        \tag{21}
\]

The signs of h_alpha and h_beta then give (8) for both choices
of gamma. The cross derivative partial_1 u2 is allowed in (20);
it drops out of the triangular determinant, not out of the graph.

Under (9), continuity, compactness and h_gamma!=0 imply m>0.
The functions in (5)-(6) are smooth for all real A,B,Z in the
box [-1,1]^3. Indeed zeta*exp(q) and eta(y)*exp(B) stay in compact
annuli bounded away from zero, and G is entire. Other numerator
zeros in this box are harmless; no G denominator was introduced.
Consequently the derivative bound L in (10) is finite.

Integrating the derivative of W along the straight line from
(0,0,0) to (A,B,Z) gives, when the three coordinates have modulus
at most delta,

\[
|W_\gamma(A,B,Z;y)-W_\gamma(0,0,0;y)|
 \le L\max(|A|,|B|,|Z|)\le L\delta<m/2.                 \tag{22}
\]

The last strict inequality follows from delta<=m/[2(1+L)];
it also holds if L=0. Hence W_gamma>=m/2 throughout the specified
finite trace box. Substitute in the exact identity (7) and retain
E(v)>=0 to obtain (12). A nonzero smooth a_gamma has positive
squared integral. No Taylor remainder, limit in the amplitude,
small interior norm or omitted collar is used in this bound.

### One finite depinning construction and its endpoint

Let rho(t)=exp(-1/(1-t^2)) for |t|<1 and zero otherwise. Set

\[
m_1=(\alpha+\beta)/2,\quad h_1=(\beta-\alpha)/2+\epsilon/2,
\quad m_2=(c+d)/2,\quad h_2=(d-c)/4,
\]
\[
\chi(y)=\rho((y_1-m_1)/h_1)\rho((y_2-m_2)/h_2),\qquad
V(y)=\bigl(\chi(y),(y_1-\alpha)(y_1-\beta)\chi(y)\bigr).   \tag{23}
\]

Its support is compactly contained in S. Both components are
nonzero functions with dependence on both variables. Extending
by zero gives a smooth real periodic field on the torus. On each
contact fiber, V1=chi is positive on an interval, whereas V2=0
and its y2 derivative is zero. Thus this field depins both first
components and still allows a nonzero coupled second component
throughout the interior and cutoff regions.

Let

\[
K_J=\sup_{T^2}\|H^{-1}DV\|<\infty,\qquad
B_\chi=\max_\gamma\|\chi(\gamma,\cdot)\|_\infty,
\quad
\tau=\min\left\{\frac1{2(1+K_J)},
                      \frac{\delta}{2(1+B_\chi)}\right\}>0,
\qquad v=\tau V.                                        \tag{24}
\]

The operator norm is the Euclidean complex matrix norm. These
constants are finite for the fixed conditional datum. The endpoint
matrix factors as

\[
I-iD(u+\tau V)=H(I-i\tau H^{-1}DV),\qquad \tau K_J<1/2.  \tag{25}
\]

The second factor has no nonzero null vector, since such a vector
w would imply ||w||<=tau*K_J*||w||<||w||. Hence J_tilde is
nowhere zero. The exterior and a neighborhood of the whole strip
boundary are unchanged. The traces satisfy (11), with b=b'=0 and
||a||_infinity<delta/2. Both first traces are nonzero, and (12)
gives the concrete strict bound

\[
\mathcal B(u+\tau V)-\mathcal B(u)
 \ge\frac{m\tau^2}{2(2\pi)^2}
     \sum_{\gamma=\alpha,\beta}\int_c^d\chi(\gamma,y)^2dy>0.
                                                               \tag{26}
\]

This is one finite endpoint, not an inference from a first or
second variation. More broadly, (12) applies to every admissible
interior extension of traces in (11), however large the extension.
It is the signed interface contribution itself that is positive
here; arbitrary interior phase cost can only add to it.

The next genuinely different finite construction must escape this
trace regime or use contact data outside (9), and must still pay
the entire E(v) in (7). The negative zero-trace coefficient for
|p|>1 indicates only where this obstruction ceases to apply. It
is not a finite descent endpoint, a configuration-existence result
or a prescription for an admissible interior.

## Mathlib

Full matching coverage for this finite trace obstruction and
supporting coverage for its constrained pullback and boundary
integration have not been checked. No Mathlib theorem is imported
and no absence claim is made. The exact identities, compact bounds
and endpoint norm argument above are informal proofs, not Lean
verification, numerical evidence or an independent audit. No
mathematical script or numerical certificate is used.
