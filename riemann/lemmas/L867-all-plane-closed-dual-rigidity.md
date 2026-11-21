# Lemma 867: all-plane closed dual forms have no strict period gain

## Hypotheses

Use exactly L847's actual entire function and constants

\[
 G(z)=\tfrac18\xi(\tfrac12+\tfrac12\sqrt z),\qquad
 R>0,\quad RG'(R)/G(R)=1,\quad C=R^2/G(R)^2>0.
\]

Evenness defines the entire G; its positive coefficients imply
G(R),G(2R)>0. On X=(C*)^2 put

\[
 F=-C\frac{G(z_1)G(z_2)(z_1-z_2)^2}{z_1^2z_2^2},\qquad
 \omega=F\frac{dz_1}{iz_1}\wedge\frac{dz_2}{iz_2}.
 \tag{1}
\]

Let alpha be a real C1 differential two-form on **all** X, closed
there. For every z in X and every real matrix A, require

\[
 |\alpha_z(E_1,E_2)|\leq|\omega_z(E_1,E_2)|,\qquad
 (E_j)_k=z_k(A_{kj}+i\delta_{kj}).                         \tag{2}
\]

These are real tangent vectors, and they are real-linearly independent:
their angular components are the two coordinate basis vectors. In (2)
every F=0 point and every J=det(I-iA)=0 matrix is retained. There is no
restriction on A, no bound on its entries, and no restriction to jets
realized by exchange-symmetric nonnegative global graphs.

Let T be the radius-R coordinate torus, oriented by
dtheta_1 wedge dtheta_2, as in L847. No RH, zero simplicity,
zero-location information or graph-existence assumption is used.

## Conclusion

There is a **constant** c in C, |c|<=1, such that on all X

\[
                  \alpha=\operatorname{Re}(c\omega).     \tag{3}
\]

Conversely, every constant c with |c|<=1 gives an admissible alpha.
Consequently

\[
 \left|\int_T\alpha\right|\leq\left|\int_T\omega\right|,
 \qquad
 \sup_{\alpha\text{ satisfying (2), }d\alpha=0}
       \left|\int_T\alpha\right|
       =\left|\int_T\omega\right|.                       \tag{4}
\]

Thus this real C1, globally closed, all-plane-dominated certificate
class cannot give the strict period gain sought in the approved test.
The result constructs no nonnegative graph, supplies no strong duality,
and excludes neither less regular certificates nor forms dominated only
on a smaller class of tangent planes. In particular it proves no
actual-Xi all-degree positivity or RH. The independent conceptual audit
of 6 November 2026 below accepts this exact statement and scope.

## Proof

### Assessed inputs and purpose of the calculation

The invocation-start EXPLORE assessment is
`drafts/literature/2026-11-06-actual-g-closed-dual-domination-test.md`.
It covers precisely the six-coefficient classification, closedness,
bounded scalar extension and period test below. Its bounded search found
no matching classification; that is not a claim of originality. L847
supplies the form, graph differential, actual-function properties and
compact homotopy/Stokes interface. No other notebook result is used.

Import these previously inspected analytic results:

- Jiri Lebl, *Tasty Bits of Several Complex Variables*, v4.4,
  31 May 2026, [Definition 1.1.2 and the C1 Cauchy--Riemann
  characterization, pp14--15; Theorem 1.6.1, pp40--41](https://www.jirka.org/scv/scv.pdf#page=40).
  The latter extends a holomorphic function from U minus the zero set
  of a nonidentically-zero holomorphic function on a domain U, provided
  it is locally bounded in U. Its proof covers singular divisor points;
  zero simplicity is not a hypothesis.
- Lebl, *Guide to Cultivating Complex Analysis*, v1.10,
  5 November 2026, [Theorem 3.3.10, p80](https://www.jirka.org/ca/ca.pdf#page=80),
  Liouville's theorem for bounded entire one-variable functions.

The scalar reduction and the checks of these hypotheses are the
mathematical work here. These standard analytic theorems are not
reproved. The available isolated-puncture theorem is unnecessary:
exponential slices give entire functions directly after divisor removal.

### Six coefficients and every complex-Jacobian-zero plane

Use the global smooth real coframe

\[
 dx_j=\operatorname{Re}(dz_j/z_j),\qquad
 dy_j=\operatorname{Im}(dz_j/z_j),\qquad
 \eta=(dx_1+i\,dy_1)\wedge(dx_2+i\,dy_2).
\]

Here dx_j=d log|z_j|; dy_j is a global one-form, although a global
single-valued angular coordinate is not asserted. Both are closed.
Equation (1) gives omega=-F eta, including its minus sign.
Write uniquely, with six real C1 coefficient functions,

\[
 \alpha=p\,dx_1\wedge dy_1+q\,dx_1\wedge dx_2
       +r\,dx_1\wedge dy_2+s\,dy_1\wedge dx_2
       +t\,dy_1\wedge dy_2+v\,dx_2\wedge dy_2.           \tag{5}
\]

Fix z, and write A=[[a,b],[c,d]] in this paragraph only; this matrix
entry c is unrelated to the constant in (3). Evaluation on E_1,E_2
gives, term by term,

\[
 \begin{split}
 \alpha(E_1,E_2)&=-pb+q(ad-bc)+ra+sd+t+vc,\\
 \eta(E_1,E_2)&=(a+i)(d+i)-bc
                  =\det A-1+i\operatorname{tr}A=-J.
 \end{split}                                               \tag{6}
\]

For any real a and any nonzero real b, take
d=-a and c=-(1+a^2)/b. Then tr A=0, det A=1, so J=0.
Hypothesis (2) forces alpha(E_1,E_2)=0, whether or not F(z)=0.
Multiplying this exact equality by b yields

\[
 -pb^2+[q+t+(r-s)a]b-v(1+a^2)=0
       \quad\text{for every }a\in\mathbb R,\ b\ne0.       \tag{7}
\]

For each fixed a this polynomial in b vanishes on all nonzero real
b. Its coefficients vanish. Taking a=0 gives p=v=0 and t=-q;
taking a=1 then gives s=r. Therefore (5), at every point of X,
has the form

\[
 \alpha=q(dx_1\wedge dx_2-dy_1\wedge dy_2)
             +r(dx_1\wedge dy_2+dy_1\wedge dx_2)
        =\operatorname{Re}(\gamma\eta),\quad \gamma=q-ir.
 \tag{8}
\]

No division by F or J has occurred. The coefficients gamma are C1
globally, including at all their zeros.

### The sharp scalar bound

Every pair (U,V) in R2 can occur as (det A-1,tr A): use

\[
             A=\begin{pmatrix}0&-(U+1)\\1&V\end{pmatrix}.
\]

Equations (2), (6) and (8) thus imply

\[
 |qU+rV|\leq |F|\sqrt{U^2+V^2}\qquad(U,V\in\mathbb R).
\]

Taking (U,V)=(q,r) proves

\[
                         |\gamma|\leq |F|               \tag{9}
\]

when (q,r)!=0; when (q,r)=0 it is immediate. In particular alpha
vanishes at every F=0 point. This is a consequence of domination,
not a premise discarding those points.

### Closedness forces holomorphic coefficients

Complexify the differential forms. Since d eta=0 and eta has type
(2,0), its wedge with the (1,0) part of d gamma vanishes in complex
dimension two. Equation (8) and real closedness give

\[
 0=2d\alpha=\bar\partial\gamma\wedge\eta
                  +\partial\bar\gamma\wedge\bar\eta.    \tag{10}
\]

The two summands have distinct types (2,1) and (1,2), which are
linearly independent subspaces of the complexified three-forms.
Hence each summand vanishes. Moreover
eta=(z_1 z_2)^(-1) dz_1 wedge dz_2 has nonzero coefficient everywhere
on X. The forms dbar z_1 wedge dz_1 wedge dz_2 and
dbar z_2 wedge dz_1 wedge dz_2 are independent basis elements.
Thus bar partial gamma wedge eta=0 forces both antiholomorphic
partial derivatives of gamma to vanish. The imported C1
Cauchy--Riemann characterization applies in the ordinary open
coordinates of X, proving that gamma is holomorphic on all X.
This type argument uses complex dimension two; it makes no
one-dimensional closedness assertion.

### The whole divisor and the noncompact domain

F is holomorphic on the connected open domain X and is not identically
zero: at (R,2R) all factors in (1) are nonzero. On X minus {F=0}, set

\[
                              h=-\gamma/F.
\]

It is holomorphic there, and (9) gives the **global** bound |h|<=1.
In particular it is locally bounded near every point of X. Lebl's
Theorem 1.6.1 therefore extends h holomorphically across the entire
zero divisor, including intersections, multiple G zeros and the
double diagonal. The extension still satisfies |h|<=1 by continuity.
The required density is also explicit here: G is nonzero entire, its
zeros are isolated (the identity/isolated-zero theorem already used in
L847), and one can perturb both coordinates to avoid these zeros and
each other. No boundedness is inferred from a compact-torus period.

For fixed z_2 in C*, the function w -> h(exp(w),z_2) is entire on C
and bounded by 1. Liouville's theorem makes it constant. Since exp maps
C onto C*, h is independent of its first coordinate. Applying the
same theorem to w -> h(z_1,exp(w)), for any fixed z_1, makes it
independent of the second coordinate as well. Thus h=c globally for
one constant |c|<=1. This handles the full noncompact X without an
unproved bound at an end of X or a choice of global logarithm.

Off the divisor gamma=-cF. Continuity gives that identity on the
divisor too; also (9) already gives gamma=0 there. From (8) and
omega=-F eta we obtain alpha=Re(c omega) on all X, proving (3).

### Period, sharpness and the obstruction scope

The form omega is holomorphic and closed on X by L847. Thus any
constant |c|<=1 gives a smooth real closed form Re(c omega), and
|Re(c omega(E_1,E_2))|<=|omega(E_1,E_2)| proves its admissibility.
Let I=integral_T omega, a finite complex number since T is compact.
Equation (3) gives integral_T alpha=Re(cI), proving (4)'s inequality.
If I!=0, choose c=bar I/|I| to attain |I|; if I=0 all the periods
are zero and c=0 attains the supremum. No sign or nonvanishing of I
has been presumed.

For the downstream interpretation import Scott Lawrence and Yukari
Yamauchi, *Convex optimization and contour deformations*,
[arXiv:2311.13002v2, Section III, (18)--(20)](https://arxiv.org/html/2311.13002v2#S3):
closed dominated forms give lower bounds for absolute contour
integrals in a fixed homology class. Here it suffices to apply that
inequality to L847's graph contours. Their tangent vectors are exactly
those in (2). Their C2 homotopy to T lies in a compact product of
annuli in X; alpha is C1 and closed on that whole swept chain.
Consequently the same compact-cylinder Stokes interface of L847
applies to alpha, including every divisor contact and J zero.
These checks justify this restricted application of the cited bound;
no domination on additional planes is assumed or needed.

A graph with real nonnegative full pullback has absolute integral
|I|. To obstruct it by this lower bound one would need
|integral_T alpha|>|I|. Equation (4) precludes that strict gain for
the entire stated class. Equality provides no contour existence or
duality-attainment implication. Coupled graph realization, all other
orders/shifts, and the main all-degree Xi sign problem remain open.

### Independent conceptual audit, 6 November 2026

This audit reuses the unchanged invocation-start EXPLORE assessment
named above. It checks the submitted proof rather than extending its
hypotheses or treating a source's sufficient bound as a classification.
L847's actual form, graph differential and compact-cylinder argument
were checked directly; the definitions and radius properties agree with
L775. The value of the saddle radius is not used by the rigidity
argument: its uses are the definition of T and a positive point at
which F is nonzero. No zeta estimate or minor sign is imported.

The six wedge evaluations in (6) were independently replayed in the
ordered real coframe. In particular dx_1 wedge dy_1 evaluates to -b,
dy_1 wedge dx_2 to d, and dx_2 wedge dy_2 to c; these check the signs
that enter (7). For each fixed a, both signs and all magnitudes of
b!=0 are permitted by the stated quantifier. The zero-polynomial
argument therefore really gives p=v=0 and q+t+(r-s)a=0 for every a,
then t=-q and s=r. No claim that these jets belong to a positive or
exchange-symmetric global graph is needed. The displayed companion
matrix in the scalar-bound paragraph has determinant U+1 and trace V,
so it realizes every required pair, including (U,V)=(q,r). The bound
and vanishing at F=0 follow without an exceptional set.

In (10) the complexified cotangent space has independent dz_1,dz_2,
dbar z_1,dbar z_2. Its (2,1) and (1,2) three-form subspaces have zero
intersection, even though their coefficients in d alpha are conjugate.
Thus real closedness cannot permit cancellation between the two
displayed types. Wedge multiplication by eta is injective on (0,1)
one-forms, since z_1 z_2!=0. The coefficient gamma is C1 in genuine
open complex coordinates on X, so the cited CR characterization applies
without strengthening alpha's regularity. This checks both the type
argument and its regularity threshold.

All hypotheses of the cited removal theorem are met on the connected
open domain X: F is holomorphic and nonzero at (R,2R); h is holomorphic
on its divisor complement; and the bound is 1 everywhere on that
complement, hence locally uniform near every divisor point. The theorem
does not require a smooth or reduced divisor. The stated density
argument then preserves the bound at the double diagonal, at any G
zero, and at their intersections. The exponential-slice functions are
entire and bounded on the whole w-plane, not just on a horizontal strip.
Surjectivity of the exponential and the two successive fixed-coordinate
applications of Liouville prove a single constant on all X. There is
no inferred growth bound at zero or infinity and no global logarithm.

Finally, integration of the real part commutes with the finite compact
torus integral. The choices c=bar I/|I| for I!=0 and c=0 for I=0
verify sharpness, including the zero-period case. For a C2 periodic
graph, pulling the C1 closed alpha back by L847's compact homotopy gives
a C1 closed two-form on the parameter cylinder. Stokes has exactly the
two endpoint orientations recorded there; contacts with F=0 or J=0 do
not create boundaries. This verifies the stated downstream application
of the imported sufficient bound without assuming duality or existence.

No mathematical defect was found. The scoped no-gain theorem is
accepted; the absolute, every-plane domination hypothesis is essential
to the proof as written. This is an independent verification of the
existing local obstruction, not a new theorem beyond the sources
checked, a graph construction, or progress to an RH resolution. No
numerical script or additional local mathematical input was needed.

## Mathlib

Full matching theorem and supporting formal coverage were not checked.
No absence claim is made. The cited analytic inputs are informal
theorem imports; the coefficient calculation, type decomposition,
divisor specialization and period conclusion above have been
independently audited as recorded here, but not formalized. No
numerical evidence is used.
