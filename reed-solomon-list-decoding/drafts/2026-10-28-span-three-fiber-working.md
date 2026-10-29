# Span-three fiber test — working record

Approved target: Test whether every auxiliary-line image in the pinned L030 full-sheet model with coefficient-difference span exactly three has affine dimension at most one over K.

Prior assessment: `literature/2026-10-28-span-three-line-fiber-rigidity.md`
(EXPLORE, saved before invocation). This is one mathematical attempt,
not another source review. The full supplied overview and DAG were used;
L030, the relevant saved full-sheet reduction and L135's planar proof
were read. ATTEMPTS/031–032 and 109 remain stop evidence. No theorem
from a different notebook or uninspected classification is an input.

## Scope, relevance and stopping test

Keep q=137, T={16,64,70,102,112,118,121}, E=F_65537,
F=F_(65537^28), H=<19139> of order 1024, k=64, every 61-core C,
and every bijection sigma from (T times F_137) disjoint union four
dummies to H minus C. Write x_(t,y)=sigma(t,y). Let K=E or F and
g_P in K[X] have degree at most two, allowing repetitions. On
A_(t,y)={P=(u,v):u+tv=y}, the value g_P(x_(t,y)) is constant.
Assume the global coefficient-difference span has dimension exactly three.

The main gap remains arbitrary-center 67/68 safety. The intermediate
target is rank at most one on every A_(t,y). A proof could support a
later line-image model for span three; global collapse, partial retention,
compatible laws and RS transfer are independent unresolved steps.
The decisive test is an all-label proof, or an exact permitted assignment
with global difference span three and a rank-two fiber. A reformulation,
generic-label calculation or relaxed counterexample is insufficient.

## Initial local mechanism (unfinished)

Fix a base fiber A_(a,b), with actual label x_0, and a point O on it.
After subtracting g_O, its images lie in ker(ev_(x_0)), whose elements
are (X-x_0)(A+B X). Under a putative rank-two fiber these images
affinely span that plane. Each other evaluation plane cuts this plane
in a line with normal [1:x_(t,y)] after division by x_(t,y)-x_0.
All those actual labels are distinct. Unlike L135, intersections of
two evaluation planes in the full coefficient space need not be points.
The attempt will test compatibility of the six transverse classes
without presuming a planar net or importing a same-field affine map.

This initial checkpoint was saved before the longer attempt. The
completed reasoning below remains an unfinished attempt, with no new
canonical lemma. The previous 74528-by-408 residual-rank route was not
rerun.

## Boundary reconstruction and the unresolved implication

Translate auxiliary coordinates so that O=(0,0) and the base line is
u+a v=0; reindex x_(t,y) by the corresponding intercept translation.
Subtract g_O from every polynomial. These operations preserve the
actual label set, all incidences, all affine dimensions and the global
difference span. In particular they do not identify the two fields.
Write

\[
 P(h,w)=(h-aw,w),\qquad x_0=x_{a,0},\qquad
 g_{P(0,w)}(X)=(X-x_0)(A(w)+B(w)X).
 \tag{1}
\]

Here A(0)=B(0)=0. For r in T minus {a}, set, in the auxiliary field,

\[
 \delta_r=r-a,\qquad s_r(h,w)=w+h/\delta_r,\qquad
 \xi_r(s)=x_{r,\delta_r s}.
 \tag{2}
\]

The r-line through P(h,w) meets the base line at P(0,s_r(h,w)),
and its actual label is xi_r(s_r(h,w)). No operation in (2) is
transported through sigma. All these actual labels differ from x_0;
the six labels for a fixed (h,w) are pairwise distinct. For h!=0
the six indices s_r(h,w) are pairwise distinct as well.

Every quadratic has a unique expression

\[
 g_{P(h,w)}(X)=(X-x_0)(\alpha_{h,w}+\beta_{h,w}X)+c_{h,w},
 \qquad c_{h,w}=g_{P(h,w)}(x_0).
 \tag{3}
\]

The six evaluation equalities with the base fiber are exactly

\[
 \alpha_{h,w}+\beta_{h,w}\xi_r+
       \frac{c_{h,w}}{\xi_r-x_0}
       =A(s_r)+B(s_r)\xi_r ,
 \quad r\in T\setminus\{a\},
 \tag{4}
\]

where xi_r=xi_r(s_r(h,w)). For three distinct actual labels z_1,z_2,z_3,
the determinant of the rows (1,z_i,1/(z_i-x_0)) is

\[
 \frac{\prod_{i<j}(z_j-z_i)}
      {\prod_i(z_i-x_0)}\ne0.
 \tag{5}
\]

To check the sign and the nonvanishing without a numerical calculation,
multiply row i by z_i-x_0. The three columns then evaluate the
polynomials X-x_0, X(X-x_0), 1. Their coefficient matrix in the
ordered basis 1,X,X^2 has determinant 1, leaving the displayed
Vandermonde determinant. Thus any fixed three transverse directions
reconstruct (alpha,beta,c) from the base data. The other three equations
in (4) are compatibility conditions, not automatic consequences.
Equivalently, append each of the other three rows to the three fixed
rows of

\[
 \bigl(1,\xi_r,1/(\xi_r-x_0),A(s_r)+B(s_r)\xi_r\bigr)
 \tag{6}
\]

and require each resulting four-by-four determinant to vanish.

The remaining direction a requires, for every fixed h,

\[
 (x_{a,h}-x_0)
       (\alpha_{h,w}+\beta_{h,w}x_{a,h})+c_{h,w}
       \quad\hbox{to be independent of }w.
 \tag{7}
\]

For h=0, reconstruction gives alpha=A(w), beta=B(w), c=0,
and (7) is automatic. Equations (4) for all (h,w), together with
(7), retain the full original equality system: every transverse line
meets the base line once, so all its points acquire that base point's
evaluation at its one actual label. Conversely every original
assignment yields (1)–(7). This is a working equivalence, not a computed
rank bound or an assertion that the nonlinear rank condition follows.
The global span-three hypothesis must still be checked on the
reconstructed assignment.

For this fixed base fiber the desired conclusion is precisely

\[
 A(s)B(t)-A(t)B(s)=0\quad\hbox{for all }s,t\in\mathbb F_{137}.
 \tag{8}
\]

The zero base value in (1) makes affine dimension equal to the rank of
these pairs. Each pair of transverse evaluation planes meets in an
affine line in the full three-dimensional coefficient space, rather
than the unique coefficient point used in L135's planar projection
argument. Consequently that argument supplies neither (8) nor a
well-defined permutation of coefficient points here.

## Exact check of what one off-fiber point can force

The following small patch checks the proposed one-point root-count
argument. It is not a full-sheet assignment or a counterexample to the
approved target. It works for every permitted label bijection.

Take Q=P(1,0), let s_r=1/(r-a), and put z_r=xi_r(s_r)=x_(r,1).
The six s_r are nonzero and pairwise distinct. Prescribe g_Q=1,
g_O=0, and on those six base points prescribe

\[
 R_r(X)=\frac{X-x_0}{z_r-x_0}
           +b_r(X-x_0)(X-z_r).
 \tag{9}
\]

Choose two distinct directions r_1,r_2 outside {a}, set b_(r_1)=0,
b_(r_2)=1, and set the other b_r to zero. Put g=0 at every remaining
base point. Each R_r has degree at most two, R_r(x_0)=0 and
R_r(z_r)=1. Hence the whole prescribed base fiber has constant
evaluation zero at x_0, and every one of the six lines connecting Q
to the base has the required common evaluation one at its actual
label z_r. Every other transverse line contains exactly one prescribed
base point, so it gives no further equality among the prescribed
points. The a-line through Q contains only Q in this patch and may
have common value one at x_(a,1).

After division by X-x_0, R_(r_1) has coefficient pair
(1/(z_(r_1)-x_0),0), whereas R_(r_2) has second coefficient 1.
These pairs are independent. Together with the zero base point the
fiber therefore has affine dimension two. Since g_Q(x_0)=1 while
every base value vanishes at x_0, the prescribed patch has global
affine span three. All original-model constraints whose two endpoints
are prescribed have been checked; polynomials at the other auxiliary
points have not been assigned. In particular this patch does not
verify (4) at the other off-fiber points or (7) on their full fibers.

This exact substitution shows that the six connections from a single
off-fiber point, even with distinct permitted labels and span three,
do not force (8). It does not show that all six complete transverse
classes admit the patch. The unresolved work is their simultaneous
extension, including (7); ignoring that distinction would fabricate
a counterexample.

## Outcome and continuation boundary

EXPLORATION. Required: rank at most one on every fiber under the full
span-three hypotheses, or an exact permitted full-sheet counterassignment.
Achieved: no rank improvement and no such assignment. The determinant
and patch substitutions above were checked algebraically, with every
denominator justified by label injectivity. No rank samples, mathematical
scripts, new canonical lemma or source import were used. Mathlib
coverage was not checked; no absence or novelty claim is made.

The boundary reconstruction exposes the missing implication (4),(7)
plus global span three => (8); it does not close it. Park the one-point
projection/root-count mechanism. Repetition requires genuinely new
coupling information, not another presentation of the same linear system.
ATTEMPTS/031–032,109 and the L135 omission failures remain unchanged.

A separately testable refinement is to retain two complete parallel
auxiliary fibers and all six transverse matchings between them. With
their h coordinates 0 and h_1!=0, the r matching sends base coordinate
w to second-fiber coordinate w-h_1/(r-a). This retains cyclic matching
compatibility absent from the patch. The proposed question is whether
both fibers can have rank two. A positive example for this reduced
model would refute only that proposed two-fiber obstruction; it need
not extend to the full sheet. An impossibility result could limit
rank-two fibers within a parallel class, but would not exclude a lone
exceptional fiber or resolve global collapse, retention or RS transfer.
This changes the hypotheses and needs a separate source assessment
before mathematical work. No such two-fiber result was attempted or
approved here.
