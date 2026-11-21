# Lemma 878: supported radial descent improves the best coordinate-torus period bound

## Hypotheses

Use exactly L847's actual entire function, ordinary coefficients,
normalization and full two-form:

\[
 G(z)=\tfrac18\xi\left(\tfrac12+\tfrac{\sqrt z}{2}\right)
     =\sum_{n\geq0}a_nz^n,\qquad a_n>0,
 \quad R>0,\quad RG'(R)/G(R)=1,\quad C=R^2/G(R)^2>0,
\]
\[
 F(z_1,z_2)=-C\frac{G(z_1)G(z_2)(z_1-z_2)^2}{z_1^2z_2^2},
 \qquad
 \omega=F\frac{dz_1}{iz_1}\wedge\frac{dz_2}{iz_2},
 \qquad X=(\mathbb C^*)^2.                                \tag{1}
\]

Evenness defines G without choosing a square-root branch. In
particular a_0 and a_4 are strictly positive. For real smooth periodic
u:T^2 -> R^2, put

\[
 \Phi_u(y)_j=R e^{u_j(y)+iy_j},\qquad
 J_u=\det(I-iDu)=1-\det Du-i\operatorname{tr}Du,
 \quad Q_u=F(\Phi_u)J_u,
\]
\[
 \mathcal B(u)=\langle|Q_u|\rangle,
 \qquad b(x)=\mathcal B(u\equiv x),\qquad
 B_{\rm tor}=\inf_{x\in\mathbb R^2}b(x).                  \tag{2}
\]

Angle brackets mean (2pi)^(-2) times the angular integral, always
with orientation dy_1 wedge dy_2. Let M=\langle F(\Phi_0)\rangle.
This notation separates the graph density Q_u from the certificate
coefficient q below.

Retain every triple in L868's unchanged admissible class: real global
C1 functions q,r,h on R^2 times T^2, periodic in both angles, with

\[
 h\geq0,\qquad q^2+r^2\leq|F|^2,\qquad
 r_{x_j}=q_{y_j},\qquad(q+h)_{x_j}=-r_{y_j}\quad(j=1,2).
                                                               \tag{3}
\]

L868 gives the constant K=\langle q+h\rangle. There is no growth
condition, bandwidth, zero simplicity, C2 assumption on q,r,h,
global logarithm, uniform zero-free collar, or RH premise. No zero
divisor or graph-Jacobian zero is removed from (3).

## Conclusion

The infimum B_tor is attained at some finite x_* in R^2. There
exist a smooth real periodic v, a compact angular support contained
in an open patch where F(Phi_x*) is nonzero, and a finite t_*>0
such that the embedded radial graph u=x_*+t_*v has mass B satisfying

\[
             |M|<B<B_{\rm tor},\qquad K\geq-B
             \quad\hbox{for every triple in (3)}.        \tag{4}
\]

The graph and its full density are unchanged outside that support;
all original zeros there remain. The graph is homologous to the
original coordinate torus in X. It depends only on F, not on the
admissible triple. Thus (4) strictly improves L868(11) for the whole
class, but it does not reach the required sharp bound K>=-|M|.

This is an existence bound, with no numerical value or effective
size of B_tor-B asserted. It constructs no constant-phase or
nonnegative graph, excludes no full-class strict-gain certificate,
and proves no higher mixed sign or RH. The independent conceptual
audit of 6 November 2026 below accepts this local specialization of
a known variational mechanism. No discovery beyond the inspected
sources or certified originality is claimed.

## Proof

### Approved scope, overlap and standard inputs

The assessment saved before this invocation is
`drafts/literature/2026-11-06-finite-graph-mass-descent-period-test.md`,
with decision SPECIALIZE and the exact target (4). It covers
attainment, phase variation, radial accessibility, finite supported
descent and the universal period consequence. Its parent comparison
checked the existing local obstructions. A targeted search of
L847–L877 and the named graph-failure records found no prior
best-coordinate-torus descent result. This is not a novelty claim.
C868c's relaxed jets and L872/L873's moving-trace/filtering failures
are contrasts only; none supplies an input to this proof.

The general necessary local mass-stationarity condition is known:
Scott Lawrence and Yukari Yamauchi, *Convex optimization and contour
deformations*, arXiv:2311.13002v2, PDF dated 14 August 2024,
[Section II B, equations (11)–(16), pp3–4](https://arxiv.org/pdf/2311.13002v2#page=3).
The assessed passage treats phase stationarity where the density
and complex Jacobian are nonzero. We do not import sufficiency,
global perfection, flow convergence, contour attainment or duality.
The calculation below specializes that mechanism to real radial
variations and the full Jacobian, because those constraints and the
zeros elsewhere on the torus must be checked explicitly.

For smooth pullback differentiation reuse Victor Guillemin and
Shlomo Sternberg, *Semi-classical analysis*, manuscript dated
13 January 2010, [Sections 13.13–13.14.1, equations (13.7)–(13.9),
pp449–455](https://math.mit.edu/~vwg/semiclassGuilleminSternberg.pdf#page=449).
The maps and omega below are smooth on a compact parameter domain;
only differentiation, not Moser existence, is used. We evaluate the
derivative directly from L847's exact pullback to verify its signs.

For the holomorphic identity theorem and compact Laurent operations
reuse Jiří Lebl, *Guide to Cultivating Complex Analysis*, v1.10,
5 November 2026, [Theorem 2.4.7, pp49–50, and Theorem 4.4.2,
pp104–107](https://www.jirka.org/ca/ca.pdf#page=104).
Only entire power series, products on fixed compact circles, and
one-variable identity theorems on the connected domain C* occur.
For Stokes reuse Lebl, *Tasty Bits of Several Complex Variables*,
v4.4, 31 May 2026, [Appendix C, Theorem C.6 and its following
regularity remark, p224](https://www.jirka.org/scv/scv.pdf#page=224).
The theorem is stated for smooth forms; the remark permits lower
regularity without explicitly specifying C1. For the needed C1
case use Robert C. Gunning, *An Introduction to Analysis*, Summer
2017, [Theorem 7.15 and the proof of Corollary 7.16,
pp342–343](https://web.math.princeton.edu/~gunning/bk.pdf#page=350):
although the statements use smooth forms, that proof explicitly
handles an arbitrary C1 form on a smooth singular cell. The compact
cylinder below can be represented by the angular parameter box;
opposite angular faces cancel by periodicity. Thus this cell case
suffices. The exact pullback and boundary hypotheses are checked
below. These source qualifications were inspected in the saved audit
assessment before the independent audit; no new analytic input or
certificate regularity is assumed.

### Four coefficients give compact sublevels and attainment

Set rho_j=R exp(x_j). Expanding (1) on a fixed coordinate torus gives

\[
 F=-C G(z_1)G(z_2)
       (z_1^{-2}+z_2^{-2}-2z_1^{-1}z_2^{-1}).             \tag{5}
\]

The power series converge absolutely uniformly on each fixed pair
of circles. Thus their product and angular coefficient integrals
can be computed term by term. All Laurent exponents in each
coordinate are at least -2. With f_x=F(Phi_x), four Fourier
coefficients, using the convention \widehat f_n=\langle f e^{-in.y}\rangle,
are exactly

\[
 \begin{split}
 \widehat f_{(-2,0)}&=-C a_0^2\rho_1^{-2},&
 \widehat f_{(0,-2)}&=-C a_0^2\rho_2^{-2},\\
 \widehat f_{(4,-2)}&=-C a_0a_4\rho_1^4\rho_2^{-2},&
 \widehat f_{(-2,4)}&=-C a_0a_4\rho_1^{-2}\rho_2^4.
 \end{split}                                             \tag{6}
\]

For example, a second-coordinate exponent -2 can only come from
the z_2^-2 summand, and forces the G(z_2) coefficient a_0;
the mixed summand cannot contribute. The same observation checks
the other three coefficients, so no cancellations were omitted.
Every Fourier coefficient has modulus at most \langle|f_x|\rangle.
Writing d_0=C a_0^2>0 and d_4=C a_0a_4>0 gives

\[
 b(x)\geq d_0\max(\rho_1^{-2},\rho_2^{-2}),\qquad
 b(x)\geq d_4\max(\rho_1^4/\rho_2^2,\rho_2^4/\rho_1^2)
          \geq d_4\max(\rho_1^2,\rho_2^2).               \tag{7}
\]

For the last inequality choose the larger radius; its fourth power
divided by the smaller radius squared is at least its own square.
Consequently b(x)<=L, for finite positive L, implies simultaneously

\[
          \sqrt{d_0/L}\leq\rho_j\leq\sqrt{L/d_4}
          \quad(j=1,2).                                 \tag{8}
\]

The dependence of f_x on x is uniform on each compact set of x
times the angular torus. The inequality ||a|-|b||<=|a-b| therefore
makes b continuous, including at every zero of f_x. Thus each
sublevel is closed and, by (8), bounded in logarithmic radii.
Take the nonempty sublevel b<=b(0). It is compact and b attains
its minimum there by the extreme value theorem. Outside this
sublevel b>b(0), so that minimum is the global infimum B_tor.
This proves finite attainment without any growth estimate for G.

### No coordinate torus has locally constant phase

Fix any finite positive rho_1,rho_2. Suppose f_x has constant phase
phi on a nonempty open angular rectangle where it is nonzero.
Then f_x=e^(2i phi) conjugate(f_x) there. The coefficient F has
real Laurent coefficients. Hence the function

\[
 H(z_1,z_2)=F(z_1,z_2)
     -e^{2i\phi}F(\rho_1^2/z_1,\rho_2^2/z_2)             \tag{9}
\]

is holomorphic on X and vanishes on the corresponding product of
circle arcs. For each fixed z_2 on its arc, the one-variable
identity theorem on C* makes H(z_1,z_2)=0 for all z_1 in C*.
Now fix any such z_1 and apply the same theorem in z_2. This gives
H=0 on all X. The accumulation points of the arcs lie inside C*,
so both applications meet the theorem's hypotheses.

On the whole original torus this equality would force the Fourier
relation

\[
 \widehat f_{(4,-2)}
       =e^{2i\phi}\overline{\widehat f_{(-4,2)}}.         \tag{10}
\]

Its left side is nonzero by (6). Its right side is zero because
(5) has no first-coordinate exponent below -2. This contradiction
rules out even a locally constant phase on a nonzero rectangle.
No inference about signs across zeros or their multiplicities was
needed; the holomorphic identity theorem used values on a patch.

In particular f_x is not identically zero, by (6), and any sufficiently
small nonzero patch has a smooth argument phi. Such a patch can be
chosen as an angular coordinate ball on which f_x takes values in
a complex disc avoiding zero, so a single smooth logarithm exists
there. Its gradient cannot vanish identically on that ball: constancy
on the connected ball would contradict (9)–(10). There is therefore
a point with grad(phi)!=0 and a smaller ball where that remains true.

Also b(x)>|M| at each coordinate torus. Indeed L847's compact
homotopy gives \langle f_x\rangle=M. If M=0, (6) gives b(x)>0.
If M!=0 and equality held, the continuous nonnegative function
|f_x|-Re(conjugate(M) f_x/|M|) would have integral zero and so
vanish everywhere. On every nonzero patch this forces the fixed
phase arg(M), contradicting (9)–(10). At the attained minimum,

\[
                         B_{\rm tor}>|M|.               \tag{11}
\]

### A permitted radial direction gives finite supported descent

Apply the preceding patch construction to x_*. Write f=f_x* and
choose a nonnegative smooth bump chi, not identically zero, with
compact support inside a ball where f!=0 and grad(phi)!=0.
Set v=-chi grad(phi) there and extend it by zero to T^2. Because
the support is compactly contained in the ball, this is a smooth
real periodic vector field. Put u_t=x_*+t v and K_0=supp(v).
On K_0, |f| has a positive minimum. By continuity, uniformly on
this compact set, F(Phi_u_t) stays nonzero for all sufficiently
small |t|. Also

\[
       J_{u_t}=1-t^2\det Dv-it\operatorname{div}v        \tag{12}
\]

stays nonzero for such t, since Dv is bounded and J_u_0=1.
Outside K_0, v and Dv vanish, so Phi_u_t=Phi_x* and Q_u_t=f
exactly. In particular every initial zero is outside K_0 and is
unchanged; none is divided out or made a boundary. The selected
graph's nonvanishing Jacobian follows from smallness of this test
deformation, not from a restriction of the admissible class (3).

Holomorphy gives partial_yj f=i z_j F_zj at t=0. Differentiating
the full pullback using (12) therefore yields

\[
 \left.\frac{dQ_{u_t}}{dt}\right|_{0}
    =\sum_j v_j z_jF_{z_j}-if\operatorname{div}v
    =-i\operatorname{div}(f v).                         \tag{13}
\]

Write f=s e^(i phi), s=|f|, on the support patch. Its pointwise
modulus derivative at t=0 is

\[
 \operatorname{Re}\left(e^{-i\phi}
              [-i\operatorname{div}(f v)]\right)
        =s\,v\cdot\nabla\phi.                          \tag{14}
\]

In detail,

\[
 e^{-i\phi}\operatorname{div}(f v)
   =v\cdot\nabla s+s\operatorname{div}v
      +i s\,v\cdot\nabla\phi.
\]

Multiplying by -i makes just its last term contribute to the real
part. Thus no integration by parts,
omitted Jacobian term, or unproved availability of complex-valued
variations is hidden in (14).

The mass difference is supported on K_0. On this compact set the
modulus of the full density is smooth in (t,y) for all sufficiently
small |t|, with bounded derivative. Differentiation of its integral
is valid there. The integral outside K_0 is constant, even at its
zeros. Consequently

\[
 \left.\frac{d\mathcal B(u_t)}{dt}\right|_0
       =-\langle\chi |f|\,|\nabla\phi|^2\rangle=-D<0.    \tag{15}
\]

Here D>0 because chi is positive on an open subset of the chosen
nonzero-gradient patch and |f| is positive there. By the definition
of the derivative, some epsilon>0 gives

\[
       \mathcal B(u_t)\leq B_{\rm tor}-Dt/2<B_{\rm tor}
                   \quad(0<t<\epsilon).                \tag{16}
\]

Shrink epsilon to retain (12) and the support nonvanishing. By
continuity and (11), shrink it again so that
\(\mathcal B(u_t)>(B_{\rm tor}+|M|)/2>|M|\).
Choose the single finite parameter t_*=epsilon/2. Equations
(15)–(16) prove actual finite descent from a global minimizing
coordinate torus. A merely formal negative first variation or
decrease from an arbitrary radius is not the conclusion used here.

### Universal comparison for the original C1 certificate class

Take any triple (3). L868 gives the real C1 closed form

\[
 \alpha=\operatorname{Re}((q-ir)\eta)-h\beta,
 \quad\eta=(dx_1+i\,dy_1)\wedge(dx_2+i\,dy_2),
 \quad\beta=dy_1\wedge dy_2,
\]

satisfying alpha_z(E_1,E_2)<=|omega_z(E_1,E_2)| for every real
matrix A with the ordered tangent pair in L868. On Phi_u use
A=Du, including the determinant factor in Q_u. Integration gives

\[
                   \int_{T^2}\Phi_u^*\alpha
                  \leq(2\pi)^2\mathcal B(u).             \tag{17}
\]

The explicit homotopy Psi(s,y)_j=R exp(s u_j(y)+iy_j), 0<=s<=1,
is smooth on the compact oriented cylinder [0,1] times T^2.
Since u is bounded, its image stays in a compact product of annuli
in X. The pullback of the C1 closed form alpha is C1 and closed.
The cited C1 Stokes theorem applies: the s=1 boundary has positive
angular orientation, the s=0 boundary negative orientation, and
there are no angular side boundaries. It gives

\[
       \int_{T^2}\Phi_u^*\alpha=\int_T\alpha
                         =-(2\pi)^2K.                  \tag{18}
\]

This homotopy is permitted to meet F=0 and J=0; both are regular
points for the globally defined alpha, and no excision is made.
The same compact argument for omega gives its period (2pi)^2 M.
Taking u=u_t* in (17)–(18) proves -K<=B, namely K>=-B.
Only upper domination on the prescribed orientation was used.
Smoothness of the test graph has not strengthened the C1
hypotheses on q,r,h. All assertions in (4) follow.

The remaining sharp bound and a constant-phase/nonnegative graph
are unresolved. This proof provides no uniform descent estimate for
subsequent graphs, no compactness of a minimizing sequence of graphs,
and no limiting argument as B approaches |M|. In particular finite
descent cannot be iterated to that threshold without new input.

### Independent conceptual audit — 6 November 2026

The separate invocation-start SPECIALIZE assessment is
`drafts/literature/2026-11-06-finite-graph-mass-descent-audit.md`.
The audit checks the preceding proof under the unchanged hypotheses
(1)–(3). It accepts (4), with no numerical improvement size and no
sharp-limit conclusion. This is REPRODUCTION and validates an
existing application, not a new general variational theorem.

**Attainment and phase obstruction.** For first exponent -2, only
the z_1^-2 term in (5) can contribute, fixing the first G index at
zero. The second indices zero and four give (-2,0) and (-2,4).
Interchanging coordinates gives the other two coefficients. All
four terms have the displayed minus sign and no factorial factors:
the a_n are ordinary coefficients. If rho_1>=rho_2 then
rho_1^4/rho_2^2>=rho_1^2; the other ordering gives the analogous
bound. Together with both inverse-square bounds this confines every
nonempty finite sublevel to the closed rectangle (8). Uniform
continuity on compact radial neighborhoods proves continuity of b
without differentiating a modulus at a zero. Minimization on
b<=b(0) is therefore global and attained at finite radii.

Real coefficients give conjugate(F(z))=F(conjugate(z)). On each
chosen circle, conjugate(z_j)=rho_j^2/z_j; the inversion is
holomorphic on C*. Thus (9) really is a holomorphic function on X.
Fixing a point of the second arc first gives an identically zero
function of z_1, not just zero on its arc. This permits the second
identity theorem for every z_1. Both domains are the connected
open set C*, and the accumulation points are nonzero. The resulting
global Fourier relation contradicts (6), since every first Laurent
exponent is at least -2. A nonzero angular patch exists by (6), and
a small ball in it admits a smooth logarithm. If its phase gradient
vanished everywhere, connectedness would make its phase constant,
which has just been excluded. This justifies the required smaller
nonzero-gradient patch. Equality in the triangle inequality for
the continuous density would force one common phase on all such
patches; if M=0 it would force f=0 everywhere. Both alternatives
are excluded. Hence the attained strict gap (11) is valid.

**Finite descent with all other zeros untouched.** On
K_0=supp(v) let m=min|f|>0. Uniform continuity makes
|F(Phi_u_t)-f|<m/2 on K_0 for sufficiently small |t|. Since Dv
is bounded, we can also require

\[
 |t|\|\operatorname{div}v\|_\infty
   +t^2\|\det Dv\|_\infty<\tfrac12.
\]

Equation (12) then gives |J_u_t|>1/2. Thus the full density is
bounded away from zero on this fixed support. The support is a
proper compact subset of a coordinate ball; extension by zero is
smooth. Off the support v=Dv=0, and the old density is unchanged,
including every old zero. On the support the modulus has a continuous
parameter derivative, uniformly bounded for t in a closed small
interval. Differentiating its integral is therefore justified even
though the unchanged exterior modulus need not be smooth in y.

The exact linear term of det(I-it Dv) is -it div(v); its determinant
term starts at order t^2. Combining it with the radial derivative
of F gives -i div(fv), with the sign in (13). In the local polar
decomposition the terms v.grad(s)+s div(v) are real and contribute
only to the imaginary part after multiplication by -i. The real
part is s v.grad(phi), giving the strictly negative D in (15).
For some epsilon>0 the difference quotient is <=-D/2 whenever
0<t<epsilon. Independently, continuity and
Delta=B_tor-|M|>0 ensure |B(u_t)-B_tor|<Delta/2 after shrinking
epsilon. Together these prove both strict inequalities for the
single choice t_*=epsilon/2. The projection of Phi_u onto its angles
is the identity, so this finite graph remains an embedding.

**Upper-only comparison and C1 regularity.** At Phi_u the ordered
tangent vectors have components z_k(partial_j u_k+i delta_kj),
exactly L868's family with A=Du. Directly,

\[
 \eta(E_1,E_2)=\det A-1+i\operatorname{tr}A=-J_u,
 \qquad \beta(E_1,E_2)=1,
\]
\[
 \alpha(E_1,E_2)
 =q(\det A-1)+r\operatorname{tr}A-h
 \leq\sqrt{q^2+r^2}\,|J_u|\leq|F|\,|J_u|.
\]

This uses h>=0 in the required direction and never reverses
orientation or puts an absolute value on alpha. The full closure
equations in (3) make the global C1 form alpha closed, as in L868.
For a direct C1 Stokes application, pull it back by Psi to
[0,1] times [0,2pi]^2. This is a C1 form on a neighborhood of the
compact box because Psi is smooth, extends across its faces and
stays away from z_j=0. Its exterior derivative is zero. The cited
C1 cell formula applies; the two faces in each angular direction
cancel with opposite orientations because the pullbacks agree by
periodicity. The remaining two faces have signs + at s=1 and - at
s=0. Thus their integrals agree. At s=0 the coefficient is
-(q+h), giving exactly -(2pi)^2 K. Equations (17)–(18) yield
-K<=B, hence K>=-B. No second derivative of q,r,h, behavior at a
radial end, zero excision or uniform collar enters this argument.
The same smooth compact homotopy applies to omega and preserves M.
The chosen x_*, v and t_* depended only on F, so the same B works
simultaneously for every admissible triple.

All direct mathematical inputs remain L847 and L868. C868c and
L872/L873 are contrasts, not additional premises. No defect in the
mathematical claim was found; the C1 source attribution above was
made precise using the already inspected audit coverage. The sharp
threshold, stationary graphs beyond this local perturbation,
compactness, higher signs and Xi transfer remain unproved.

## Mathlib

Full matching and supporting formal coverage have not been checked;
unknown coverage is not an absence claim. This is an informal
specialization using the cited compact Laurent, identity-theorem,
pullback-differentiation and C1 Stokes inputs. No numerical evidence,
mathematical script or formal verification is used. The independent
conceptual audit above accepts the informal statement only; it does
not establish Mathlib coverage or formal verification.
