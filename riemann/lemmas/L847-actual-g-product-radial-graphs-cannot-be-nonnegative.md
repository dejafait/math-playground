# Lemma 847: the actual-G form has no nonnegative product radial graph

## Hypotheses

Use the actual entire G of L018/L775, with its ordinary coefficients
and positive radius

\[
 G(z)=\frac18\xi\left(\frac12+\frac{\sqrt z}{2}\right)
     =\sum_{n\geq0}a_nz^n,\qquad a_n>0,\qquad
 R=R_1>0,\qquad RG'(R)/G(R)=1.
\]

Evenness defines G without a square-root branch. In particular
G(R)>0, a_0>0 and a_3>0. Retain exactly the full r=2,k=1 form
of L846(3), on X=(C minus zero)^2:

\[
 \begin{split}
 C&=\frac{R^2}{G(R)^2}>0,\\
 F(z_1,z_2)&=-C\frac{G(z_1)G(z_2)(z_1-z_2)^2}{z_1^2z_2^2},\\
 \omega&=F\frac{dz_1}{iz_1}\wedge\frac{dz_2}{iz_2}
 =C\frac{G(z_1)G(z_2)(z_1-z_2)^2}{z_1^3z_2^3}
       dz_1\wedge dz_2.                                      \tag{1}
 \end{split}
\]

Let u=(u_1,u_2):T^2 -> R^2 be C^2 and 2pi-periodic in each
coordinate, where T^2=(R/2pi Z)^2. Such a u is bounded; no specified
bound, smallness, symmetry, total reality or Jacobian nonvanishing
is assumed. Orient T^2 by dtheta_1 wedge dtheta_2 and put

\[
 \Phi_u(\theta)_j=R\exp(u_j(\theta)+i\theta_j),\qquad A=Du,
 \quad A_{j\ell}=\partial_{\theta_\ell}u_j.                   \tag{2}
\]

For the obstruction in the conclusion only, the product subclass
means u_1(theta)=v_1(theta_1), u_2(theta)=v_2(theta_2), for real
C^2 periodic v_1,v_2. This is a restriction of the allowed graphs,
not a hypothesis imposed on the general graph question. All zeros
of G, of z_1-z_2 and of the full pullback are retained. No RH or
simplicity of zeros is used.

## Conclusion

Every graph (2) is an oriented embedded torus homologous in X to
the coordinate torus of radius R, and its exact full pullback is

\[
 \Phi_u^*\omega=q_u\,d\theta_1\wedge d\theta_2,\qquad
 q_u=F(\Phi_u)\bigl(1-\det A-i\operatorname{tr}A\bigr).       \tag{3}
\]

Writing F(Phi_u)=P+iQ, B=1-det A and S=tr A, the requested
pointwise condition is exactly

\[
 QB-PS=0,\qquad PB+QS\geq0.                                 \tag{4}
\]

There is **no graph in the product subclass** for which q_u is
real and nonnegative everywhere. Consequently any solution of the
general graph problem must have at least one of
partial_2 u_1, partial_1 u_2 not identically zero.

The general coupled system (4) is unresolved. This result excludes
independent one-variable radial contour choices, including arbitrary
large deformations, but not coupled graphs, other contours, or RH.
The full-form calculation and elementary source applications are
not new general theorems. The invocation-start EXPLORE comparison
did not locate this exact product obstruction; this is not a claim
of certified originality. The independent conceptual audit of
6 November 2026 below accepts this scoped conclusion without strengthening it.

## Proof

### Scope of the reused inputs

Use the assessment saved before invocation,
`drafts/literature/2026-11-06-actual-g-radial-graph-full-phase.md`,
and its reused joint-contour comparison. The former explicitly
permits the complete pullback calculation and a rigorously scoped
obstruction in this fixed graph problem. The product restriction is
the bounded test made here; it does not settle the unrestricted
target. No contour-existence or calibration theorem is imported.

L775 supplies the entire power series and strict coefficient
positivity, and L846(3) supplies the precise form (1); no relative-cycle
obstruction from L846 is used. The standard named homotopy invariance
of singular homology is imported. For the other standard inputs use
the following sources, already inspected in
`drafts/literature/2026-11-06-actual-g-product-radial-graph-obstruction-audit.md`:

- Jiří Lebl, *Guide to Cultivating Complex Analysis*, version 1.10,
  5 November 2026, [Theorem 2.4.7, pp49–50; Theorem 3.3.8, p79;
  Theorem 4.4.2, pp104–107](https://www.jirka.org/ca/ca.pdf):
  isolated zeros/identity theorem on a connected open domain,
  Cauchy's coefficient estimate on a closed disc in that domain,
  and Laurent existence, uniqueness and compact uniform convergence
  on an open annulus. Here G and the remainder E are entire; the
  annulus used below is |w|>|c|/rho.
- Sabine Boegli, *Complex Analysis II (Michaelmas)*, 2023–2024,
  [Section 4.3, circline proposition and proof](https://maths.dur.ac.uk/users/sabine.boegli/CA2.html#circles-and-lines):
  a nonsingular Möbius map preserves generalized circles. Below the
  map is nonsingular because a!=b and lambda!=0. The displayed
  equation (9) checks its specialization and restores its pole.
- Lebl, *Tasty Bits of Several Complex Variables*, version 4.4,
  31 May 2026, [Appendix C, Theorem C.6 and the following regularity
  remark, p224](https://www.jirka.org/scv/scv.pdf#page=224):
  Stokes on a compact oriented parameter manifold with boundary,
  in its C^1 differential-form version. The C^2 homotopy gives that
  regularity on the parameter cylinder, as checked below.

These standard results are imported, not reproved. The specializations,
finite-zero checks and elementary Laurent/circle algebra are retained
because they supply this obstruction and its qualifications.
There is no new asymptotic estimate, contour-existence assumption,
unread essential source or reproof of a perfect-contour theorem.

### Exact graph, orientation and closed-form invariance

The angular projection X -> T^2, z -> (arg z_1,arg z_2), composed
with Phi_u is the identity. Its differential composed with D Phi_u
is also the identity. Thus Phi_u is an injective immersion and,
by compactness of T^2, an embedding. The explicit homotopy

\[
 \Phi_{t u}(\theta)_j=R\exp(tu_j(\theta)+i\theta_j),
 \qquad 0\leq t\leq1,                                      \tag{5}
\]

stays in X and carries the same parameter orientation. It proves
the claimed homology equality. Its whole image lies in a compact
product of annuli, since u is bounded. The form (1) is holomorphic
on X and closed: differentiating its coefficient introduces only
dz_1 or dz_2, which repeats a factor in the wedge; its antiholomorphic
derivatives vanish. Write Psi(t,theta)=Phi_(tu)(theta). The source
[0,1] x T^2 is a smooth compact manifold with boundary, oriented by
dt wedge dtheta_1 wedge dtheta_2. Since Psi is C^2 and omega is smooth,
Psi^*omega is C^1 and d(Psi^*omega)=Psi^*(d omega)=0. Apply the C^1
Stokes theorem separately to its real and imaginary parts. The t=1
boundary has orientation +dtheta_1 wedge dtheta_2, the t=0 boundary
has the negative orientation, and there are no side boundaries.
Thus integral Phi_u^*omega = integral Phi_0^*omega. Psi itself need
not be an embedding. The zero divisor of
the numerator is not a singularity of omega and need not be avoided.
No sign follows from this integral equality.

For the full differential, with no omitted factors,

\[
 \Phi_u^*\frac{dz_j}{iz_j}
   =d\theta_j-i\sum_\ell A_{j\ell}\,d\theta_\ell.
\]

Their wedge has coefficient det(I-iA)=1-det A-i tr A, proving (3).
Multiplication by P+iQ proves (4). These identities involve no
division by F or by det(I-iA). In particular, they hold at every
density zero and every complex-Jacobian degeneracy. The two minus
signs in (1), from F and 1/i^2, cancel; this also checks the sign in
the product calculation that follows.

### Bounded periodic derivative-moment comparison, 6 November 2026

This specialization uses the invocation-start SPECIALIZE assessment
`drafts/literature/2026-11-06-periodic-jacobian-moment-scope.md`.
It applies to every real C2 periodic u in (2), hence also to the
exchange-symmetric class. It does not assume that any prescribed
contact germs extend to such a graph. The earlier product obstruction
and its audit do not constitute an audit of this added comparison.

Write angle brackets for the normalized cell integral
(2pi)^(-2) integral over [0,2pi]^2, and put d=det Du, S=tr Du.
The periodic lift of u is C2 on R2. Each derivative entry has mean
zero: integrate first in its differentiation coordinate and use the
equal endpoint values of u, then integrate in the other coordinate.
All these integrands are continuous on a compact cell, so Fubini
applies. Import J. M. Ball, J. C. Currie and P. J. Olver,
*Null Lagrangians, Weak Continuity, and Variational Problems of
Arbitrary Order*, J. Functional Analysis **41** (1981), 135–174,
[Theorem 3.4(iii), p143, and Theorem 4.1, p149](https://people.maths.ox.ac.uk/~ball/Papers/Ball%2C%20Currie%20%26%20Olver%201981.pdf).
Their p=q=2, k=1 Jacobian minor is det Du; the continuous periodic
gradient is almost periodic, and its large-domain mean is this
normalized cell mean. The theorem gives mean(det Du)=det(mean Du).
Thus, without reproving the null-Lagrangian theorem,

\[
 \langle S\rangle=0,\qquad \langle d\rangle=0,\qquad
 \langle J\rangle=\langle1-d-iS\rangle=1.                 \tag{M1}
\]

Now retain the actual coefficient P+iQ=F(Phi_u), not its unweighted
mean. Set p=\langle P\rangle, v=\langle Q\rangle, and
K=\langle F(Phi_0)\rangle. This K is real: G has real coefficients,
so conjugation of F(Phi_0(theta)) is F(Phi_0(-theta)); the cell
integral is invariant under theta -> -theta on T2. The full-form
homology equality already proved above gives \langle q_u\rangle=K.
Expanding (3), then using (M1), yields exactly

\[
 \begin{split}
 K&=p-\langle(P-p)d\rangle+\langle(Q-v)S\rangle,\\
 0&=v-\langle(Q-v)d\rangle-\langle(P-p)S\rangle.           \tag{M2}
 \end{split}
\]

Every quantity is continuous and bounded for the fixed graph; no
series, limiting interchange, global potential or boundary flux
cancellation is introduced here. Equations (M2) hold even when
q_u is not pointwise real or nonnegative. Consequently the two
derivative means do not remove the variable-weight terms in the
already known homology equality. In particular replacing
\langle P d\rangle by p\langle d\rangle, or
\langle Q S\rangle by v\langle S\rangle, would require additional
information not present in (M1).

Under the requested q_u>=0, (4) is still the exact pointwise test.
For completeness, its division-free weighted version is

\[
 |F(Phi_u)|^2(1-d)=Pq_u,\qquad
 |F(Phi_u)|^2S=Qq_u.                                    \tag{M3}
\]

Indeed q_u\overline{F(Phi_u)}=|F(Phi_u)|^2J. These are identities,
not an additional sign estimate. At F=0 both sides vanish and give
no restriction on J; at J=0 the full density vanishes as well.
Thus neither the exchange diagonal nor any other F zero, nor any
permitted J zero, has been divided out. No uniform bound on u or
range/phase bound for F is available from this comparison.

The bounded test therefore stops at automatic periodic identities
and the unsolved weighted sign condition. It proves no new actual-G
obstruction, no compatibility sufficiency and no global realization.
In particular it does not rule out or construct L861's conditional
four-cycle; that mention is a comparison, not an input to (M1)–(M3).
No assertion that arbitrary formal moment data are derivatives of a
periodic graph is used. A useful new weighted estimate would be a
changed target requiring its own assessment.

### Product curves and their finite exceptional sets

Suppose now, for contradiction, that u is in the product subclass
and its pullback is real and nonnegative. Write

\[
 \gamma_j(t)=R\exp(v_j(t)+it),\qquad
 A_j(t)=\frac{G(\gamma_j(t))\gamma_j'(t)}{\gamma_j(t)^3}.
\]

Each gamma_j is a simple closed curve meeting each ray from zero
exactly once, with winding number +1. Its derivative
gamma_j(t)(v_j'(t)+i) never vanishes. Thus in this subclass the
complex Jacobian is nonzero as a consequence, not an extra assumption.
Equation (1) gives exactly

\[
 q(t,s)=C A_1(t)A_2(s)(\gamma_1(t)-\gamma_2(s))^2.            \tag{6}
\]

G is entire and not identically zero because a_0>0. Its zeros on
either compact curve are finite by the isolated-zero theorem:
an infinite subset would have a finite accumulation point in C.
Each such zero has a unique curve parameter modulo 2pi. Also a
fixed point of C can be attained at most once by each gamma_j.
These statements use neither simplicity nor real location of zeros.

Choose distinct parameters t_0,t_1 for which A_1 is nonzero, and
put a=gamma_1(t_0), b=gamma_1(t_1); hence a!=b. Except for finitely
many s, both values q(t_0,s),q(t_1,s) in (6) are nonzero. They are
then strictly positive by the assumed nonnegativity. It follows that

\[
 \frac{A_1(t_0)}{A_1(t_1)}
 \left(\frac{a-\gamma_2(s)}{b-\gamma_2(s)}\right)^2
       \in\mathbb R_{>0}.                                   \tag{7}
\]

Fix either nonzero square root lambda of A_1(t_1)/A_1(t_0).
A complex number whose square is strictly positive real is itself
nonzero real. Thus (7) forces

\[
 \frac{a-w}{\lambda(b-w)}\in\mathbb R,
 \qquad w=\gamma_2(s),                                     \tag{8}
\]

at every nonexceptional parameter. No point is permanently deleted:
the exceptional parameters will be restored by continuity below.

### The two curves must be the same circle

Clearing the denominator in the reality condition (8) gives

\[
 \operatorname{Im}\bigl((a-w)\overline{\lambda(b-w)}\bigr)=0. \tag{9}
\]

This is a real quadratic equation with only a real multiple of
|w|^2, real-linear terms and a constant. Its zero locus is a circle
or a line through a and b. For completeness it cannot be the
identically zero polynomial: the nonconstant fractional-linear map
(a-w)/(lambda(b-w)) maps C minus {b} onto C minus one point, and
so cannot take only real values there. If the quadratic coefficient
vanishes the nonzero equation is a line; otherwise completing the
square gives a circle, with positive radius because it contains the
distinct points a,b. Denote this closed locus by K.

Continuity in (9) restores all the finitely many excluded parameters,
including possible G zeros and points a,b. Therefore gamma_2 lies
entirely in K. A line cannot meet every ray from zero in a nonzero
point: if it passes through zero it has only two directions, and
otherwise it misses the rays on one side. Thus K is a circle.
Write it as |z-c|=rho. Since gamma_2 meets every ray, avoids zero
and lies in K, zero is strictly inside the circle: rho>|c|.
Indeed a circle with zero outside or on its boundary misses at
least one ray in a nonzero point. Each ray then meets K in exactly
one positive radial point, so gamma_2 is the entire circle K.

Keep t_1 fixed and repeat the argument for any other parameter t
with A_1(t)!=0 and gamma_1(t)!=b. The resulting circle contains
the entire image gamma_2=K. Two distinct circles cannot have three
distinct common points, as follows by subtracting their quadratic
equations. Hence that circle equals K, and gamma_1(t) belongs to K.
The finitely many remaining parameters are included by continuity.
The same radial argument now gives gamma_1=K as well. This step
does not assume that the original curves were disjoint or equal.

### The forced real boundary value

Parametrize this common circle by z(t)=c+rho e^{it}. The change
from the original radial angle to this angle preserves orientation:

\[
 \frac{d\arg z(t)}{dt}
 =\frac{\rho^2+\rho\operatorname{Re}(\bar c e^{it})}{|z(t)|^2}
 >0,
\]

since rho>|c|. Therefore real nonnegativity of the density is
preserved by the two separate parameter changes. Define

\[
 H(z)=\frac{G(z)(z-c)^2}{z^3}.
\]

Using z'(t)=i(z(t)-c) and
(z(t)-z(s))^2=-4(z(t)-c)(z(s)-c) sin^2((t-s)/2), the full
pullback in these parameters is

\[
 4C H(z(t))H(z(s))\sin^2\frac{t-s}{2}\,dt\wedge ds.          \tag{10}
\]

For any t with H(z(t))!=0, take s tending to t through distinct
parameters with H(z(s))!=0. The latter exclusions are finite.
After division by the strictly positive 4C sin^2((t-s)/2),
nonnegativity implies H(z(t))H(z(s)) is positive real. Passing to
the limit gives H(z(t))^2 nonnegative real; it is nonzero by the
choice of t, hence positive, so H(z(t)) is real.
At every zero the same reality statement holds trivially. Hence

\[
 H(z)\in\mathbb R\quad\hbox{on }|z-c|=\rho.                 \tag{11}
\]

In fact the nonzero values must all have the same sign, but only
(11) is needed. Thus neither the diagonal zeros nor any zeros of G
have been ignored in obtaining the required boundary condition.

### A centered circle is impossible

If c=0, H(z)=G(z)/z, and on |z|=rho its absolutely uniformly
convergent Fourier series is

\[
 H(\rho e^{it})=\frac{a_0}{\rho}e^{-it}+a_1+
             \sum_{n\geq1}a_{n+1}\rho^n e^{int}.
\]

For a real continuous boundary function its Fourier coefficients
satisfy b_{-n}=overline{b_n}, directly by conjugating the defining
integral. Here b_{-2}=0 but b_2=a_3 rho^2>0, contradicting (11).

### An off-center circle is impossible

Suppose c!=0. H is meromorphic on C, with its only finite pole at
zero. Its principal part and entire remainder are

\[
 \begin{split}
 H(z)&=P_0(z)+E(z),\qquad
 P_0(z)=h_3z^{-3}+h_2z^{-2}+h_1z^{-1},\\
 h_3&=c^2a_0\ne0,\qquad h_2=c^2a_1-2ca_0,\qquad
 h_1=c^2a_2-2ca_1+a_0,
 \end{split}                                                \tag{12}
\]

where E is entire; subtraction removes all negative powers at the
only possible singularity. Put w=(z-c)/rho, so the circle is |w|=1.
The entire function E(c+rho w) has Taylor coefficients e_n with

\[
 \limsup_{n\to\infty}|e_n|^{1/n}=0.                          \tag{13}
\]

Precisely, Cauchy's coefficient estimate on any circle |w|=r gives
|e_n|<=max_{|w|=r}|E(c+rho w)|/r^n; r may be arbitrarily large.

Because |c|/rho<1, the geometric-series expansions of
(c+rho w)^{-j}, j=1,2,3, converge absolutely uniformly on |w|=1.
They contain only negative powers of w. For n>=3 the coefficient
b_{-n} of w^{-n} in H(c+rho w) is exactly

\[
 b_{-n}=\frac{(-c)^{n-3}}{\rho^n}
       \left[h_3\binom{n-1}{2}-c h_2(n-1)+c^2h_1\right].     \tag{14}
\]

For example the jth principal-part term contributes
h_j (-c)^{n-j} binom(n-1,j-1)/rho^n; summing these terms gives
(14). In expanded form the bracket is

\[
 P(n)=\frac{h_3}{2}n^2+
       \left(-\frac{3h_3}{2}-c h_2\right)n+
       h_3+c h_2+c^2h_1.
\]

Since P(n)/n^2 tends to h_3/2!=0, for all sufficiently large n
one has |h_3|n^2/4 <= |P(n)| <= K n^2 for some fixed K>0.
Thus P(n) is eventually nonzero and |P(n)|^(1/n) tends to 1;
complex coefficients cannot cancel its leading term indefinitely.
Consequently

\[
 \lim_{n\to\infty}|b_{-n}|^{1/n}=|c|/\rho>0.                 \tag{15}
\]

All positive Fourier coefficients b_n equal e_n, because P_0 has
only negative powers in this annulus. The uniform expansions
justify identifying their Laurent and boundary Fourier
coefficients term by term. Reality (11) would give
b_{-n}=overline{b_n}=overline{e_n}, contradicting (13) and (15).
This argument uses the genuine pole at zero and the entire
remainder, not a reflection across an unexamined zero divisor.

Both cases are impossible. Thus the product graph assumed in (6)
does not exist. The general system (4) remains valid but undecided:
with cross-coordinate dependence, its Jacobian and density factors
do not separate as in (6), so the ratio argument cannot be applied.
No bound on the remaining coupled phase error has been obtained.

### Independent conceptual audit, 6 November 2026

The complete proof (1)–(15) was independently checked under the
invocation-start EXPLORE audit assessment cited above. The audit
accepts the statement as written. The explicit parameter-cylinder
Stokes check and expanded polynomial bound above make its regularity,
boundary signs and full coefficient limit explicit; they do not change
the hypotheses or strengthen the obstruction.

In (7), the square of (8) equals q(t_0,s)/q(t_1,s), since
lambda^2=A_1(t_1)/A_1(t_0). Both numerator and denominator are strictly
positive off precisely the finite sets identified in the proof.
Equation (9), rather than division by b-w, restores every excluded
point. The radial curve fills the entire resulting circle, and fixing
b while varying a yields the same circle, not merely unrelated arcs.
The displayed angular derivative is strictly positive because
rho>|c|, so both parameter changes preserve the original coordinate
orientation. In (10), the negative sign from the two tangent factors
cancels the negative sign from the squared difference. Its limit is
taken only after division away from the diagonal, and reality at
zeros follows by continuity. The centered contradiction is exactly
b_2=a_3 rho^2>0 versus b_-2=0. Off center, the order-three pole survives
because c^2a_0!=0, the entire remainder has coefficient root limsup
zero, and the full negative tail has root limit |c|/rho>0. All relevant
series converge absolutely uniformly on the boundary circle. No
numerical estimate, pole deletion or claim about locations of G zeros
is used.

The source comparison also records a stronger known conditional
boundary theorem: Tuen-Wai Ng and Xiao Yao, *Rationality of meromorphic
functions between real algebraic sets in the plane*,
[arXiv:2204.06753v1, 14 April 2022, Theorem 1.1 and Example 1.2,
p2; rationality proof pp4–5](https://arxiv.org/pdf/2204.06753v1#page=2).
A nonconstant function meromorphic on the whole plane that maps a
nondegenerate unit-circle continuum into a real algebraic curve
defined by an irreducible real polynomial is rational. This is a
comparison, not an extra mathematical input: the proof above retains
the exact existing coefficient calculation instead of invoking that
theorem. Its global meromorphic and boundary-reality requirements
explain the overlap; it does not supply the earlier product geometry.
No new general rationality result or originality claim is made.

This verifies a restricted route obstruction, not a sign of a mixed
minor and not RH. In particular the audit adds no assumption that
det(I-i Du) is nonzero for general coupled graphs. The direct local
inputs remain L018, L775 and L846(3); no new DAG edge is needed.

## Mathlib

Full matching coverage has not been checked; no absence claim is
made. The argument uses elementary differential-form pullback and
Stokes, isolated zeros, circle algebra and Cauchy/Fourier coefficient
identities. No named Mathlib theorem was used or asserted to cover
the product-contour obstruction. The independent informal audit above
is complete; it is not a formal verification or an extension to coupled graphs.
For the later periodic-moment comparison, full matching Mathlib
coverage is likewise not checked; the cited null-Lagrangian theorem
is an informal imported input, and (M1)–(M3) have no formal audit.
