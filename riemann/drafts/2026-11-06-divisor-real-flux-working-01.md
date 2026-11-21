# Fixed-crossing real flux lift: working record

STEP_ID: 2026-11-06-divisor-real-flux-attempt-01.
Invocation-start coverage: the unchanged EXPLORE assessment
`literature/2026-11-06-divisor-weighted-real-flux-test.md`.

The main gap is L030-L032/C032a actual-Xi all-degree mixed positivity.
The approved intermediate target is a smooth real solution of
div(Mv)=sigma on a full disk about one fixed qualified L853 crossing.
It could support later singular patch assembly, but gives no density
sign, global supported solution, nonlinear convergence or all-degree result.

Inputs read: L847 full form and graph identity; L850 signed general
variation; L853 full crossing/factorization and finite-jet proof with
its separate audit. Retain the actual-G analytic/software qualifications,
finite n>=1, K(p)!=0 and A12(p)>0. Do not assume J(p)!=0 or a simple root.
Reuse the completed source comparison and its named duplicate/failure
checks. No external theorem beyond the covered imports is presumed.

Test: retain the divisor factor in a primitive of the entire source;
allow an exact real one-form correction and require a real smooth radial
lift on the full disk. A neighborhood identity or an obstruction to
this construction is decisive. Punctured inversion, finite jets or
an uncontrolled flat remainder is not decisive and parks this mechanism.

Initial coordinate bookkeeping (not a proved result): put
w=x+iy=u1-u1(p)+i(t-p1), b=A12>0. Locally s=s(x,y),
s_x=1/b, s_y=-A11/b. In logarithmic ambient coordinates w and
zeta=log(z2/z2(p)), omega=-F dw wedge d zeta, with
F=w^n times a holomorphic unit in the ambient coordinates.
Radial variations have delta w=v1 real and delta zeta=v2 real.
The unresolved task is to use primitive freedom without replacing
these real variations by unrestricted complex vector fields.

This initial checkpoint was saved before the all-orders attempt. The
completed bounded attempt below remains unfinished mathematically: no
neighborhood lift or obstruction has been established. It is not a new
canonical lemma or an assertion of formal/analytic solvability.

## Whole-source primitive and the remaining lift

Work on a disk in the accepted real analytic w-coordinate, shrinking
it so A12>0 and the other factors remain nonzero. Put

\[
 Z(w,\bar w)=u_2-u_2(p)+i(s-p_2),\qquad
 a=\partial_w Z,\quad b=\partial_{\bar w}Z.
\]

Here Z is the local logarithm of z2/z2(p), not a holomorphic function
of w. Partial derivatives are Wirtinger derivatives in x,y. In the
ambient logarithmic coordinates w,Z, the full form is
omega=-F dw wedge dZ, and F=w^n k(w,Z), where k is a holomorphic
unit. This follows directly from L853's finite Taylor factorization
of G(z1) and its nonzero remaining factors, without a new zero claim.
Write K=k(w,Z(w,bar w)). K is a nonzero real analytic function; it is
not assumed holomorphic in w.

Coordinate differentiation gives, at every point of this disk,

\[
 \begin{split}
 S_x&=1/A_{12},& S_y&=-A_{11}/A_{12},\\
 U_x&=A_{22}/A_{12},&
 U_y&=A_{21}-A_{22}A_{11}/A_{12},\qquad Z=U+iS,\\
 a&=\frac{A_{22}-A_{11}+i(1+\det A)}{2A_{12}},&
 b&=\frac{\operatorname{tr}A+i(1-\det A)}{2A_{12}},\\
 J&=-2iA_{12}b,& dt\wedge ds&=-A_{12}^{-1}dx\wedge dy.
 \end{split}                                                    \tag{W1}
\]

The signs can also be checked without changing orientation:
dw wedge dbar w=-2i dx wedge dy, so

\[
 \Phi_u^*\omega=2i w^nK b\,dx\wedge dy,
 \qquad \sigma\,dt\wedge ds
       =2\operatorname{Re}(w^nK b)\,dx\wedge dy.                 \tag{W2}
\]

For the center-preserving contraction w -> tau w, the standard
homotopy primitive of the *whole* real source (W2) is

\[
 H(w,\bar w)=\int_0^1\tau^{n+1}K(\tau w,\tau\bar w)
                                b(\tau w,\tau\bar w)\,d\tau,
 \qquad
 \alpha_c=2\operatorname{Re}(w^nH)(x\,dy-y\,dx).                \tag{W3}
\]

This is the relative-primitive construction already covered by
Domitrz-Janeczko-Zhitomirskii, *Relative Poincare lemma,
contractibility, quasi-homogeneity and vector fields tangent to a
singular variety*, Illinois J. Math. 48(3) (2004), 803-835,
[Definitions 2.1-2.2, Theorem 2.3 and Lemma 2.4 with proof,
pp807-808](https://pages.mini.pw.edu.pl/~domitrzw/poincare-ijm48%283%29.pdf#page=5).
The disk contracts to its center, the source coefficients vanish
there, and a top-degree form on the disk is closed. The general
relative Poincare theorem is imported, not reproved. The power
tau^(n+1) in its explicit specialization includes tau from the
two-form homotopy and tau^n from the divisor factor. In particular,
with E=x partial_x+y partial_y, differentiating
tau^(n+2)(Kb)(tau w) gives
(n+2)H+EH=Kb. Consequently differentiation of the displayed alpha_c
gives exactly (W2). This checks its normalization and orientation
for the variable source.

The integrals and their derivatives exist on a smaller closed disk:
the analytic coefficients have a convergent power series on a larger
disk, and integration on [0,1] preserves that convergence. In
particular alpha_c is real analytic through the center and vanishes
to order at least n+1. The expression retains w^n and its conjugate
in the real part; it does **not** establish complex divisibility of
an arbitrary real flux component or a smooth inverse for M.

Every smooth real lifted primitive would have the form alpha_c+d psi
on this disk, for a smooth real psi. Indeed its difference from
alpha_c would be a closed one-form, and the same disk homotopy gives
an exact primitive; a lifted form vanishes at the center since M=0
there. The exact remaining condition, with v1,v2 real, is

\[
 \operatorname{Im}\!\left[
  w^nK\{(a v_1-v_2)\,dw+bv_1\,d\bar w\}\right]
       =\alpha_c+d\psi.                                      \tag{W4}
\]

This is -Im beta in L850's sign convention. Differentiating a
solution of (W4) would give div(Mv)=sigma in the original angles.
The availability of psi as an arbitrary exact correction is retained;
failure to lift alpha_c alone would not refute (W4). No such failure
is used as an obstruction here. Pointwise inversion on a punctured
set does not prove that v extends across its determinant-zero loci
or across the center. No uniform matrix lower bound is available
from the hypotheses used in this attempt.

## Attempted sufficient correction and the all-orders stopping point

A concrete sufficient subansatz is to require the stronger complex
identity d beta=-Phi_u^*omega, where the existing contraction is

\[
 \beta=w^nK\{(v_2-av_1)\,dw-bv_1\,d\bar w\}.
\]

It would supply a real correction psi in (W4) by exactness of
-Im beta-alpha_c. This subansatz is not necessary for the original
real phase equation. Its failure cannot be a nonexistence proof.
Writing f=v2, c=K_barw/K and e=K_w/K, differentiation on w!=0
reduces this sufficient identity to

\[
 \partial_{\bar w}f-a\partial_{\bar w}v_1
       +b\partial_wv_1+c f
       +\{(n/w+e)b-ca\}v_1=-b.                              \tag{W5}
\]

To check (W5), d beta has coefficient
-partial_barw(F(f-av1))-partial_w(Fbv1) in dw wedge dbarw;
-Phi_u^*omega has coefficient Fb. Mixed derivatives cancel because
partial_barw a=partial_w b. The derivatives of the *whole* K remain
in c and e. No coefficient or derivative term has been discarded.

The attempted factor-preserving choice v1=|w|^2 g, with g real,
removes the apparent pole in (W5) and gives the whole-disk equation

\[
 \partial_{\bar w}f-a\partial_{\bar w}(|w|^2g)
       +b\partial_w(|w|^2g)+cf
       +(eb-ca)|w|^2g+n b\bar w g=-b.                       \tag{W6}
\]

All coefficients in (W6) are real analytic. A real smooth pair f,g
satisfying it would therefore prove the stronger identity everywhere,
including at w=0, after multiplication by w^nK. Removing the pole
alone is insufficient: the coefficients of both derivatives of g
vanish at the center. Thus the two-real-equation first-order system
has no invertible matrix of transverse derivatives for (f,g) there.
An ordinary noncharacteristic first-order application has not been
justified. This observation concerns that subansatz, not the local
range of the original underdetermined real equation.

At the center (W6) reduces to
partial_barw f(0)+c(0)f(0)=-b(0). Choosing f(0)=0 permits real
linear f to satisfy it, reproducing the already known finite-jet
freedom. Freezing coefficients and iterating homogeneous corrections
was considered, but no convergent right inverse, remainder estimate
or all-orders compatibility argument was obtained. In particular,
Im a(0)=(1+det A(p))/(2A12(p)) is not assumed nonzero; and an inverse
for a frozen operator would still require control of variable
coefficients. This is exactly where the attempt stops. No formal
series is promoted to a smooth or analytic solution.

## The J(p)=0 case is still separate and unresolved

By (W1), J(p)=0 is equivalent to b(0)=0. Then det A(p)=1,
tr A(p)=0 and Im a(0)=1/A12(p)>0. The ambient holomorphic unit
also gives K_barw=k_Z b, so c(0)=0. In this case (W3) vanishes to
order at least n+2 and the central equation in (W6) is
partial_barw f(0)=0. These higher vanishing orders do not solve
(W4) or (W6) on a neighborhood: b need not vanish identically, and
the derivative degeneracy of g persists at the center. The method
has neither treated J(p)=0 by a neighborhood lift nor excluded it.
No division by J is made anywhere.

## Decision and saved boundary of the attempt

Outcome EXPLORATION: a new bounded whole-source homotopy and
factor-preserving correction test was carried out, but the required
full-neighborhood identity or scoped obstruction was not obtained.
The primitive is an application of a known source; the lift remains
unproved. There is no progress claimed beyond the inspected literature,
no new lemma and no mathematical certificate or script.

Park this particular primitive/correction mechanism. The earlier
three-exploration fixed-cutoff sequence and its inverse, finite-jet
and characteristic-loop stops remain unchanged; this reopening does
not reset that budget. Resumption would require a materially new
all-orders estimate or an independently testable range obstruction,
not more finite jets or repetition of (W3).

The next independently testable task is the already approved L861
conceptual audit, as recorded in PROGRESS.md. Its global individual-
divisor incidence constraints do not depend on solving this singular
linear equation. No L861 proof is audited in this turn. Global
support/exchange assembly, nonlinear convergence, density signs and
actual-Xi all-degree positivity remain unresolved. Mathlib coverage
of the full lifting problem and the relative-primitive input is not
checked; unknown coverage is not absence.
