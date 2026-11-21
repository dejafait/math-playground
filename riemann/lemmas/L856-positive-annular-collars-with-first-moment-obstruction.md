# Lemma 856: positive annular collars can fail the first boundary-moment test

## Hypotheses

Use the actual data of L855: the entire function
G(z)=xi(1/2+sqrt(z)/2)/8, defined by its entire power series;
R=R_1>0, C=R^2/G(R)^2>0; and a fixed pair (zeta,eta) with
zeta eta!=0, zeta!=eta, G(eta)!=0 and G(zeta)=0 of finite
multiplicity n>=1. The normalization and full-form convention are
those retained in L855 from L775/L847. No zero simplicity or RH is
assumed. The full form is

\[
 \omega=C\frac{G(z_1)G(z_2)(z_1-z_2)^2}{z_1^3z_2^3}
                dz_1\wedge dz_2.                            \tag{1}
\]

Write G(zeta+w)=w^n g(w). Use the jointly holomorphic inverse
chart constructed in L855, on an open neighborhood B of (0,0),

\[
 \begin{split}
 H(w,z)&=C\frac{g(w)G(z)(\zeta+w-z)^2}{(\zeta+w)^3z^3},
 &H_0&=H(0,\eta)\ne0,\\
 (w,v)&\longmapsto (\zeta+w,h(w,v)),
 &\omega&=w^n dw\wedge dv.                                  \tag{2}
 \end{split}
\]

Its image stays where all denominator factors and H are nonzero;
h(w,0)=eta, h_w(0,0)=0 and h_v(0,0)=1/H_0. Fix the L855 germ

\[
 A=-iH_0\eta/\zeta,\qquad
 v_0(w)=Aw+\frac{i}{n+1}\overline w^{\,n+1}.                 \tag{3}
\]

All radii below may depend on this fixed chart, pair and n. Orient
the w plane by dx wedge dy, w=x+iy. Original angle lifts are the
continuous lifts of arg(zeta+w) and arg(h(w,v(w))) near the base
pair, with the same orientation as L855.

## Conclusion

For every sufficiently small r>0 there are prescribed smooth inner
and outer collar graphs in this one chart, about |w|=r/2 and |w|=r,
respectively, with the following properties:

1. The inner graph is exactly (3). Both collars have strictly positive
   real full density, and their original angular-projection determinants
   are strictly positive. They are actual surfaces for (1).
2. Their constant Stokes boundary period M_0 is positive. Their first
   holomorphic boundary period M_1 is real and equals 2r M_0.
3. There is no smooth graph v(w) on the closed annulus
   r/2<=|w|<=r, agreeing with both collars on relative open
   neighborhoods of its boundary circles, staying in B, and having
   real nonnegative full density. This excludes, in particular, an
   interpolating graph also having positive original angular determinant.

Thus positive total flux, even together with positive full density and
positive original angular orientation of the prescribed collars, is
not sufficient for this relative gluing problem. This is a local,
conditional-in-the-pair obstruction, not a construction of global
contour data, a sign of an Xi minor, or a resolution of RH. It does
not concern interpolants that leave this chart or cease to be graphs
over w. Its first independent conceptual audit on 6 November 2026
accepts precisely this statement; no stronger gluing obstruction or
mathematical novelty beyond the checked tools is claimed.

## Proof

### Imported tools and scope of the specialization

Use the invocation-start SPECIALIZE assessment
`drafts/literature/2026-11-06-positive-annular-gluing-boundary-moment.md`.
The primary statements and their relevant proof cases were inspected
there. The inputs used here are:

- Jiří Lebl, *Tasty Bits of Several Complex Variables*, v4.4,
  31 May 2026, [Theorem B.2, p206, with orientation p205](https://www.jirka.org/scv/scv.pdf#page=205),
  and [Theorem 4.1.1 with the punctured-domain proof, pp130–131](https://www.jirka.org/scv/scv.pdf#page=130):
  planar Green–Stokes for bounded domains with positively oriented
  piecewise-C1 boundary and C1 coefficients. The inner-circle
  contribution is subtracted. A smooth closed annulus and all the
  forms below satisfy these hypotheses; simply connectedness is not
  required. Apply the real theorem to real and imaginary parts.
- Philipp J. di Dio and Konrad Schmüdgen, *The multidimensional
  truncated Moment Problem: The Moment Cone*,
  [arXiv:1809.00584v1, 3 September 2018, positivity (5), pp4–5,
  Definition 5, p5, and Proposition 24(i), p12](https://arxiv.org/pdf/1809.00584v1#page=12):
  integration against a positive measure is nonnegative on every
  nonnegative member of the real span of its integrable test
  functions. Here the space is the compact closed annulus, the
  functions are 1, Re(w), Im(w), and the proposed measure has smooth
  nonnegative density. All three functions are bounded and integrable.

These general tools are imported, not reproved. We calculate their
primitives, boundary periods and actual admissible collars. This is
the authorized finite known-tool specialization (REPRODUCTION), not
a claim of a new general moment theorem or certified originality.
L855 supplies all the chart and tangent facts in (2)–(3); no earlier
fixed-cutoff transition, crossing or global extension is assumed.

### Constant and first-moment identities, with signs

Let a hypothetical interpolant have full pullback

\[
 w^n dw\wedge dv=q(w)\,dx\wedge dy,
 \qquad q(w)=-2i w^n\partial_{\bar w}v(w).                  \tag{4}
\]

This retains the full form, not only a scalar factor of it. For
j=0,1 the smooth complex one-form

\[
 \alpha_j=-w^{n+j}v(w)\,dw
 \quad\hbox{satisfies}\quad
 d\alpha_j=w^{n+j}dw\wedge dv=w^j q(w)\,dx\wedge dy.        \tag{5}
\]

Indeed d(w^{n+j}) wedges to zero with dw and the remaining term is
-w^{n+j}dv wedge dw, with the indicated plus sign. There is no
division by w, the form or a Jacobian in this identity.

For a circle of radius s define its counterclockwise period by

\[
 P_j(s;v)=-\int_{|w|=s}^{\rm CCW} w^{n+j}v(w)\,dw.
\]

The annular positive boundary is the outer circle counterclockwise
and the inner circle clockwise. Green–Stokes therefore gives

\[
 M_j:=P_j(r;v_{\rm out})-P_j(r/2;v_0)
      =\int_{r/2\leq|w|\leq r}w^j q(w)\,dx\,dy.            \tag{6}
\]

Agreement on collars guarantees the stated boundary traces. Smoothness
on the closed annulus gives the regularity and boundedness required
by the imported theorem. If q is real nonnegative, positivity of
the affine function r-Re(w) on this closed annulus implies

\[
                  rM_0-\operatorname{Re}M_1\geq0.           \tag{7}
\]

Only the constant and first moments are used. In particular (7) is
an instance of the imported positive-functional condition, not an
assertion that these moments suffice for a smooth interpolation.

### Explicit prescribed outer collar

Set

\[
 d_n=1-2^{-2n-2}>0,\qquad
 b_r=\frac{2d_n}{n+1}r^{2n+3}>0,
 \qquad
 v_{\rm out}(w)=v_0(w)+i b_r w^{-n-2}.                     \tag{8}
\]

Use (8) on the open collar 3r/4<|w|<5r/4, and use (3) on
the open collar 3r/8<|w|<5r/8. The pole term is single-valued
and holomorphic on the outer collar, with no singularity there.
It is not proposed as a function on the inner disc. Consequently
both prescribed collars satisfy, exactly,

\[
 \partial_{\bar w}v=i\overline w^{\,n},\qquad
             q(w)=2|w|^{2n}>0.                             \tag{9}
\]

We next verify chart confinement and original angular orientation;
formal boundary moments alone would not be admissible data.

Put beta=2d_n/(n+1), a constant for fixed n. On the entire outer
collar the perturbation E_r=i b_r w^{-n-2} obeys

\[
 \begin{split}
 |E_r|&\leq\beta(4/3)^{n+2}r^{n+1},\\
 \|D E_r\|&\leq\beta(n+2)(4/3)^{n+3}r^n.                  \tag{10}
 \end{split}
\]

Here D is the real derivative and its Euclidean operator norm; for
a holomorphic function that norm equals the modulus of its complex
derivative. The antiholomorphic term in v_0 has value at most
(5/4)^(n+1)r^(n+1)/(n+1) and derivative norm at most
(5/4)^n r^n. Hence, uniformly on the outer collar as r decreases,

\[
 w\longrightarrow0,\quad v_{\rm out}\longrightarrow0,\quad
               Dv_{\rm out}\longrightarrow D(w\mapsto Aw). \tag{11}
\]

Since B is an open neighborhood of (0,0), these value bounds put
the whole collar in B for all sufficiently small r. The corresponding
surfaces S_r(w)=(zeta+w,h(w,v_out(w))) therefore lie in the same
inverse chart as the inner germ, where the original coordinates
and all the nonzero factors in (2) remain nonzero. They are smooth
embedded surfaces because their first coordinate is zeta+w.

Joint holomorphicity of h, its derivatives in (2), and (11) give
uniformly on these collars

\[
 S_{r,1}\to\zeta,\quad S_{r,2}\to\eta,\quad
 DS_{r,1}=D w,\quad
 DS_{r,2}\to D(w\mapsto-i\eta w/\zeta).                    \tag{12}
\]

For example, DS_{r,2}=h_w Dw+h_v Dv_out, and the two holomorphic
derivatives approach 0 and 1/H_0, respectively. Near the base pair
use the fixed logarithm branches of L855 to define the original
angle lifts Theta_{r,j}. Their differentials are
Im(dS_{r,j}/S_{r,j}). If 1/zeta=p+it, their real derivative matrices
therefore converge uniformly to

\[
 \begin{pmatrix}t&p\\-p&t\end{pmatrix},\qquad
                         \det=|\zeta|^{-2}>0.               \tag{13}
\]

Continuity of determinant gives det DTheta_r>1/(2|zeta|^2) on
the entire outer collar for all sufficiently small r. All estimates
are uniform on the stated collar; none asserts a radius uniform in n.
Shrink r also so the inner collar lies in L855's audited germ
neighborhood, with the same determinant lower bound there.
Equation (9), divided by this positive determinant under local angular
coordinates, is strictly positive real density in the original
orientation. No zero of the full form or Jacobian has been deleted.
This proves all the prescribed-collar admissibility assertions.

### Exact periods and the obstruction

On |w|=s, conjugate(w)^(n+1)=s^(2n+2)w^(-n-1). The term Aw
in (3) contributes zero to both periods: its powers are
w^(n+j+1), whose integrals vanish. The antiholomorphic term gives

\[
 P_0(s;v_0)=\frac{2\pi}{n+1}s^{2n+2},\qquad
                         P_1(s;v_0)=0.                    \tag{14}
\]

Explicitly the two integrands after weighting have powers w^-1
and w^0, respectively, and -i times integral w^-1 dw is 2pi.
The added term in (8), after weighting, has powers w^(j-2).
Its constant-period contribution is zero and its first-period
contribution is 2pi b_r. These assertions also follow directly
by parametrizing w=s exp(it), t in [0,2pi], so no extension of
the pole term through the inner disc is being used.

Taking the difference of the two boundary circles yields

\[
 \begin{split}
 M_0&=\frac{2\pi d_n}{n+1}r^{2n+2}>0,\\
 M_1&=2\pi b_r=\frac{4\pi d_n}{n+1}r^{2n+3}=2rM_0.        \tag{15}
 \end{split}
\]

Thus the scalar total flux is exactly the positive mass of the
unperturbed germ on this annulus; the Laurent term has not changed
it. But (15) makes the left side of (7) equal to -rM_0<0.
This contradicts a real nonnegative density for any hypothetical
interpolant, regardless of its angular determinant. Adding the
requested positive angular condition cannot remove the contradiction.

This ends the finite first-moment test. The example invalidates a
universal gluing rule based on total flux and collar positivity; it
does not claim that collars from any particular global Xi contour
have these periods. Compatible collars, global matching, exchange
compatibility, other orders and all-degree mixed positivity remain
open. No higher-moment escalation or reopening of the fixed-cutoff
linear route is inferred.

### Independent conceptual audit — 6 November 2026

The audit uses the invocation-start SPECIALIZE assessment
`drafts/literature/2026-11-06-l856-annular-first-moment-audit.md`.
It independently checks (4)–(15), the complete preceding proof and
L855's joint inverse and original-angle tangent. The fixed actual
G, normalization and full form agree with L775/L847. L855 is the
only direct mathematical input; its inherited inputs are not new
assumptions. The inspected Green–Stokes and positive-functional
theorems above suffice without another existence theorem.

Here is an explicit uniform-domain and orientation verification.
Choose a closed polydisc |w|<=delta, |v|<=delta compactly contained
in B. Decrease delta until (zeta+w)/zeta and h(w,v)/eta lie in the
fixed neighborhood of 1 admitting L855's logarithm branch. This is
possible by continuity at (0,0), independently of r. Put

\[
 \begin{split}
 K_0&=\frac{(5/4)^{n+1}}{n+1}
          +\beta(4/3)^{n+2},\\
 K_1&=(5/4)^n+\beta(n+2)(4/3)^{n+3}.
 \end{split}
\]

On the whole outer collar, including its closure, (10) gives

\[
 |w|\leq5r/4,\quad
 |v_{\rm out}|\leq5|A|r/4+K_0r^{n+1},\quad
 \|Dv_{\rm out}-D(Aw)\|\leq K_1r^n.                       \tag{16}
\]

Choose r so both value bounds are less than delta/2. Hence all
evaluations occur in a fixed compact subset of B. Continuity of
h_w,h_v there, evaluated at points tending uniformly to (0,0),
and the last bound in (16) justify the uniform chain-rule limit
in (12). Division by S_1,S_2 in the angle differentials is valid
and uniformly bounded because they tend to the nonzero zeta,eta.
This proves uniform convergence of the actual angle matrix to
T=[[t,p],[-p,t]], rather than only convergence of formal jets.
The requirement n>=1 is used: r^n tends to zero also when n=1.
No estimate uniform in n or the pair is claimed.

For an explicit determinant threshold put lambda=1/|zeta|.
Then T^T T=lambda^2 I. For sufficiently small r the angle matrix
T_r satisfies ||T_r-T||_op<lambda/4 everywhere on the collar.
For every real vector e and 0<=s<=1,
|(T+s(T_r-T))e|>=(3lambda/4)|e|. Thus the entire matrix segment
is nonsingular, its determinant keeps the positive sign of T,
and det T_r>=(3lambda/4)^2>lambda^2/2. The same threshold for
the inner collar follows by placing 5r/8 inside L855's already
chosen germ disc. These choices can all be met by one r_*>0;
they then hold for every 0<r<r_*. They prove confinement and
orientation on open collars, not just on the boundary circles.
The graph embedding uses the first coordinate zeta+w. Only a
local angular inverse is needed for each collar; no global
injectivity of its angle map is asserted or needed.

The full-density and boundary checks do not discard any zero or
factor. In dw wedge dv the holomorphic derivative cancels, and
the antiholomorphic derivative of the Laurent term is exactly
zero on the collar. Thus (9) is exact, with no error to compare
against its vanishing small-radius size. Changing to original
angles divides it by the positive determinant just proved.
For a hypothetical smooth graph on the closed annulus, q in (4)
is smooth and bounded; if real nonnegative it defines a finite
positive measure there. The primitives (5) are smooth there too.

For completeness all circle signs can be checked without a
residue theorem. For an integer ell and s>0, parametrization gives

\[
 I_\ell(s):=\int_{|w|=s}^{\rm CCW}w^\ell\,dw
  =i s^{\ell+1}\int_0^{2\pi}e^{i(\ell+1)t}\,dt
  =\begin{cases}2\pi i,&\ell=-1,\\0,&\ell\ne-1.\end{cases}
                                                                  \tag{17}
\]

The Aw term in P_j is -A I_(n+j+1), hence zero. The remaining
inner-germ term is -i s^(2n+2) I_(j-1)/(n+1). It is positive
2pi s^(2n+2)/(n+1) for j=0 and zero for j=1. The outer
increment is -i b_r I_(j-2), zero for j=0 and positive 2pi b_r
for j=1. Green–Stokes subtracts the inner counterclockwise
period. This independently reproduces (15), including both
orientations and the plus sign of M_1. The coefficient with
a pole is never evaluated at zero or integrated over a disc.

Finally d(-w^(n+j)v dw)=w^(n+j)dw wedge dv has the plus sign
because dv wedge dw=-dw wedge dv. With the finite positive
measure q dx dy, the imported positive-functional condition
applied to the bounded nonnegative function r-Re(w) yields
rM_0-Re(M_1)>=0. The exact periods instead give -rM_0<0.
Thus the achieved first moment exceeds its allowed upper bound
by a factor of two. This accepts the stated obstruction for
graphs over this annulus in this chart. It does not exclude
surfaces with a different projection domain, establish that
actual exterior contour data have these periods, or prove any
Xi sign. No repair of the original mathematical claim was needed.

## Mathlib

Full matching coverage of this prescribed-collar obstruction is not
checked. Supporting coverage of planar Stokes, positive integration,
holomorphic charts and continuity of determinants is also not checked
here; no absence or formal-verification claim is made. The inspected
primary citations above supply the standard tools. The application
uses only the constant and first affine moment and the audited local
chart of L855.
