# Corollary 869a: the fixed Green countermodel has no zero-fiber closure lift

## Hypotheses

Fix ell in R, H>0, and any phase phi in R/(2pi Z). Let h be
exactly the real C1 function of L869(7)-(9), with the same ell,H.
Thus, writing X=x1-ell and Y=x2-ell,

\[
\begin{gathered}
p(t)=\begin{cases}
1,&|t|\leq2,\\
1-3w^2+2w^3,\quad w=|t|-2,&2<|t|<3,\\
0,&|t|\geq3,
\end{cases}\\
p_1=p(X-12),\quad p_2=p(Y),\quad
p_3=p(X+Y-12),\quad p_4=p(X-Y-12),\\
m=H\left(1+2\sum_{1\leq i<j\leq4}p_i p_j\right),\\
h=m+H\{p_1\cos y_1+p_2\cos y_2
                -p_3\cos(y_1+y_2)-p_4\cos(y_1-y_2)\}.
\end{gathered}
\tag{1}
\]

The proposed lift consists of real, globally C1 functions q,r on
R^2 times T^2, periodic in both angles, satisfying every equation

\[
r_{x_j}=q_{y_j},\qquad (q+h)_{x_j}=-r_{y_j}\quad(j=1,2),
\tag{2}
\]

and the complete fixed fiber trace

\[
q((\ell,s),(\phi,v))=r((\ell,s),(\phi,v))=0
                  \quad(s,v\in\mathbb R).
\tag{3}
\]

No growth, angular bandwidth, Fourier summability, choice of Green
solution, or restriction of homogeneous or zero modes is imposed.
Actual-F domination and the other zero or diagonal traces are not
hypotheses of this test.

## Conclusion

There is no lift (2)-(3). More precisely, (2)-(3) would require

\[
h_{x_2}((\ell,s),(\phi,v))=0\quad(s,v\in\mathbb R),
\tag{4}
\]

whereas the prescribed h has the exact residual

\[
h_{x_2}((\ell,\ell+5/2),(\phi,0))=-3H/2\ne0.
\tag{5}
\]

This holds for every phase, hence for the already chosen actual-zero
parameters ell,phi of C868b. It rules out this fixed h in the
stronger class; it does not invalidate L869's abstract countermodel.
It does not establish joint Green positivity in the remaining class,
the period bound K>=-|M|, graph realization, actual-Xi signs or RH.
The separate exact audit of 6 November 2026 below accepts this local
obstruction at its stated scope.

## Proof

### Scope and reused source assessment

The prior EXPLORE assessment is
`drafts/literature/2026-11-06-green-countermodel-zero-fiber-lift.md`.
Its covered target is exactly (1)-(3), allowing all homogeneous and
zero modes; it explicitly permits a local obstruction valid for every
lift. L869 supplies the prescribed C1 h. The present specialization
needs only its explicit cutoff and first derivatives, rather than
its Green integral or negative-matrix estimate. C868a's profile
interface and C868b's mean identities explain the test but are not
needed to derive (4)-(5). No source theorem about global PDE
solvability or holomorphic extension is imported or reproved.
The ready assessment did not locate this exact fixed-h conclusion;
this elementary calculation makes no claim of originality.

### Differentiate the full trace only in tangent directions

For any fixed real s,v, (3) gives

\[
\begin{split}
q_{x_2}((\ell,s),(\phi,v))
 &=\lim_{t\to0}
 \frac{q((\ell,s+t),(\phi,v))-q((\ell,s),(\phi,v))}{t}=0,\\
r_{y_2}((\ell,s),(\phi,v))
 &=\lim_{t\to0}
 \frac{r((\ell,s),(\phi,v+t))-r((\ell,s),(\phi,v))}{t}=0.
\end{split}
\tag{6}
\]

These derivatives exist by C1 regularity. The angular difference
quotient can be taken in any local lift of the angle, with periodicity
making its value independent of that choice. Both directions remain
on the fiber; no derivative in its fixed x1 or y1 direction is set
to zero. The j=2 second equation of (2) now gives (4). Thus even
this one equation, together with the full trace, is necessary.

### Evaluate the prescribed cutoff at an interior point

Put s=ell+u with 2<u<3. On the fiber x1=ell,

\[
p_1=p(-12)=0,\quad p_2=p(u),\quad
p_3=p(u-12)=0,\quad p_4=p(-u-12)=0.
\tag{7}
\]

Indeed u-12 lies in (-10,-9), and -u-12 lies in (-15,-14),
outside the support [-3,3]. Every pair product in m vanishes
throughout this open interval of s. Consequently (1) gives the
exact restriction, for every phi,v,

\[
h((\ell,\ell+u),(\phi,v))=H\{1+p(u)\cos v\}
                                      \quad(2<u<3).
\tag{8}
\]

Differentiation in s is differentiation in u, with the other
coordinates fixed. On this positive interval w=u-2, so

\[
p'(u)=-6(u-2)+6(u-2)^2,\qquad p'(5/2)=-3/2.
\tag{9}
\]

Using v=0 in (8)-(9) proves (5), contradicting (4) since H>0.
The evaluation is strictly inside the polynomial interval; no
endpoint derivative or limiting value at an infinite radius is used.

The contradiction was derived directly for arbitrary q,r satisfying
the C1 equations and trace. Changing any homogeneous mode, adding
frequencies with zero forcing, or changing compatible zero modes
cannot avoid (6). There is no Fourier reconstruction, truncation or
interchange of limits here. The actual-zero input only selects a
phase and radius already covered by the arbitrary ell,phi argument;
no new zero certificate or RH assumption is involved.

### Independent exact audit, 6 November 2026

The unchanged invocation-start EXPLORE assessment is
`drafts/literature/2026-11-06-fixed-green-zero-fiber-obstruction-audit.md`.
This audit checks (1)-(9) against L869(7)-(9); it does not retest
L869's Green matrix or assume the stronger actual-F hypotheses of
C868a/C868b. It verifies the submitted obstruction rather than
claiming a new theorem beyond the sources checked.

For the elementary derivative operation, reuse Jiří Lebl,
*Basic Analysis II*, author-maintained HTML,
[Section 8.3, Definition 8.3.8](https://jirilebl.github.io/ra/html/sec_svtheder.html)
(inspected in the approved source assessment on 6 November 2026).
This defines partial derivatives by coordinate difference quotients
on an open real-coordinate domain. C1 regularity here supplies
existence; a local angular chart supplies that domain for y2.
No trace theorem, normal derivative rule or second derivative is
being imported.

1. The fiber fixes only x1=ell and y1=phi. Its parameters s and v
   independently range over all real values (with v interpreted
   periodically). Thus both shifted points in each quotient (6)
   satisfy exactly (3); their numerators vanish for every small
   nonzero t. These are q_x2 and r_y2, not q_x1 or r_y1.
   The j=2 second closure equation is q_x2+h_x2=-r_y2,
   so its sign gives h_x2=0. The first closure equation and
   the j=1 equations are not needed: every solution of the full
   system must satisfy this one necessary equation.
2. Formula (1) has exactly L869's four cutoff arguments and six
   pair products. With x1=ell and 2<u=x2-ell<3 they are
   -12, u, u-12, -u-12. The first, third and fourth lie
   strictly outside [-3,3] throughout this open interval.
   Their cutoffs and their x2 derivatives therefore vanish there.
   Each of the six pair products has at least one such factor;
   equivalently the whole mean restricts identically to H on an
   open interval. Hence no derivative of the mean is omitted.
   The only surviving angular term is +H p(u) cos(v), exactly
   as in (8); all terms carrying phi are identically zero there.
3. At u=5/2 the positive transition variable is w=1/2, and
   -6w+6w^2=-3+3/2=-3/2. With v=0 the surviving cosine is
   1, giving h_x2=-3H/2 at the finite point in (5). This is
   nonzero for every H>0, for arbitrary ell and every phi.
   No cutoff endpoint, absolute-value corner, numerical rounding
   or phase selection enters the evaluation. H=0 would remove
   this contradiction and is explicitly outside the hypotheses.
4. The quotients were applied to arbitrary original q,r, not to
   selected coefficients. Consequently arbitrary homogeneous
   solutions, zero-forcing frequencies and compatible zero modes
   cannot change the contradiction while retaining (2)-(3).
   No growth assumption, Fourier convergence or higher regularity
   has been added. C868b's actual zero only chooses parameters
   already covered by the universal statement; neither its
   existence proof nor the remaining actual-F conditions is a
   mathematical input to this obstruction.

No defect was found in the stated C1 full-class conclusion. The
unchanged fixed forcing has no such lift. This is a stop for its
realization, not joint positivity of other admissible Green data.
L869 remains valid in its abstract class. Any different forcing,
even one passing this necessary tangential condition, still needs
its own closure/trace construction or obstruction and source scope.
Actual-F domination, other zero and diagonal conditions, the period
bound, graph realization and actual-Xi signs remain unresolved.

## Mathlib

Full matching coverage has not been checked; no absence claim is
made. The proof uses first derivatives of identically zero C1
restrictions and the derivative of an explicit cubic. No Mathlib
theorem or numerical script is used as verification.
