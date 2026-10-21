# Lemma 384: positive-proportion empty cells on the actual response grid

## Hypotheses

Let G be the actual regulator response of L366, with the carrier of
L368 and the full increasing phase of L372. Enumerate its consecutive
zeros on the eventual positive ray as g_j, so that, on continuous branches,

\[
 \phi(g_j)=\pi/2+j\pi,\qquad
 \phi(t)=\vartheta(t)+\beta(t)+\eta(t).
\]

Here vartheta is the Hardy gamma phase, eta is the imaginary part of
the absolutely convergent Euler logarithm at 5/2+it, and beta is the
argument of L368's b(t). Count all nontrivial zeta zeros in the full
strip, with their analytic multiplicities. No RH, critical-line
simplicity, noncoincidence, discriminant inequality or common-zero
count hypothesis is assumed.

## Conclusion

There exist fixed c>0 and T_0<infinity such that every real T>=T_0 has
at least c T log T complete response cells

\[
 (g_j,g_{j+1}],\qquad T\le g_j<g_{j+1}\le2T,
                                                        \tag{1}
\]

containing no full-strip zeta-zero ordinate. Both constants are
existential and unevaluated. The number of all complete cells is
(T/(2pi))log T+O(T), so this is a fixed positive proportion.

The excluded left endpoint is unresolved: a zero at g_j is compatible
with (1). Thus no strict product F_0(g_j)F_0(g_{j+1})>0, common-free
Wronskian witness, actual-theta Laguerre sign or RH consequence follows
from this statement alone. The separate critical audit below validates
this specialization; the notebook's main argument remains incomplete.

## Proof

This is a **REPRODUCTION**, covered before invocation by the unchanged
SPECIALIZE assessment
`drafts/literature/2026-10-10-variable-response-cell-occupancy.md`.
The known-source mechanism is T. Trudgian, *On the success and failure
of Gram's Law and the Rosser Rule*, Acta Arith. 148(3) (2011), 225–256,
DOI 10.4064/aa148-3-2, Theorems 5.2–5.3, pp. 242–244
([published version](https://www.impan.pl/shop/publication/transaction/download/product/82370)).
Those theorems concern ordinary Gram cells, not (1). We prove the
bounded variable-phase and complete-endpoint specialization below;
transporting ordinary-grid signs would not suffice.

**Imported inputs.** Use Trudgian Theorem 5.1, p. 242, reproducing
K.-M. Tsang, *Some Omega-theorems for the Riemann zeta-function*,
Acta Arith. 46(4) (1986), 369–395, Theorem 4,
DOI [10.4064/aa-46-4-369-395](https://doi.org/10.4064/aa-46-4-369-395).
For fixed a>1/2, T^a<H<=T, 0<h<1 and positive integer m, it gives,
with ell=log(2+h log T),

\[
 \int_T^{T+H}(S(t+h)-S(t))^{2m}\,dt
 =\frac{(2m)!}{(2\pi^2)^m m!}H\ell^m
  +O\!\left(H(Am)^m\{m^m+\ell^{m-1/2}\}\right).       \tag{2}
\]

We use only a=3/4, H=T and m=1,2. This precise citation relies on
Trudgian's reproduced statement: the original Tsang proof is unread.
No reproof, stronger uniformity or vanishing relative error at fixed
h log T is claimed. Also import Backlund's count formula and S(t)=O(log t)
from Trudgian Theorem 4.1 and (35)–(36), pp. 237–238, citing
E. C. Titchmarsh, *The Theory of the Riemann Zeta-function*, 2nd ed.,
revised D. R. Heath-Brown (1986), pp. 212–213 and Theorem 9.4.
The Hardy phase is Trudgian (7)–(9), p. 227.

**One-sided convention.** Define N_+(t) as the number of full-strip
zeros with 0<Im rho<=t, retaining multiplicity. At a zero ordinate
define S_+(t)=lim_(u down to t, u>t) S(u); elsewhere S_+=S. Apply the
count formula first off the zero ordinates, then take this right limit.
The finitely many zeros in a bounded height interval and continuity of
vartheta give, at every sufficiently large real t,

\[
 N_+(t)=\vartheta(t)/\pi+S_+(t)+1,
 \qquad S_+(t)=O(\log t).                            \tag{3}
\]

This reconciles the source's strict count notation with its right-hand
S limit without losing a moving-endpoint multiplicity. The growth bound
passes to the right limit with the same uniform constant. Changing S
at the discrete zero ordinates changes neither integral in (2): the
exceptional t for t or t+h to be an ordinate form a measure-zero set.
We use S_+ throughout the remaining proof.

**Actual phase and spacing.** Put delta=beta+eta. L368 (3) gives

\[
 b(t)=(t^2/4-3/16-it/2)/\pi.
\]

For t>=2 its real part is positive, so take
beta=-arctan(8t/(4t^2-3)), with |beta|<=pi/2. Since Q/A is exactly
exp(i vartheta), this gives the same carrier phase as L372, up to a
constant 2pi branch change. L372's Euler-log bound is
|eta|<=E=log zeta(5/2). Hence fix

\[
 |\delta(t)|\le D:=\pi/2+E \quad(t\ge2).             \tag{4}
\]

L372's controlled carrier derivative and bounded eta derivative give
phi'(t)=(1/2)log(t/(2pi))+O(1). Consequently, for every sufficiently
large T and every t in [T/2,3T],

\[
 \tfrac14\log T\le\phi'(t)\le\log T.                \tag{5}
\]

The constants here are independent of T and t. Strict increase and a
phase increment pi, by the mean-value theorem, therefore bound each
complete cell in this region by

\[
 \pi/\log T\le g_{j+1}-g_j\le w:=4\pi/\log T.       \tag{6}
\]

The first response zero a_T>=T and last response zero b_T<=2T exist
for large T, and
0<=a_T-T<=w, 0<=2T-b_T<=w. Indeed the phase gains pi within distance w
to the right of T and to the left of 2T by (5); all such short intervals
are in [T/2,3T]. They have a_T<b_T for large T. Let n_T denote the number
of consecutive cells tiling (a_T,b_T]. It is exactly
(phi(b_T)-phi(a_T))/pi. L372 (8)–(9), now used on [T,2T], gives

\[
 n_T=\frac{f(2T)-f(T)}\pi+O(1)
     =\frac{T}{2\pi}\log T+O(T),
 \quad f(t)=\tfrac t2\log(t/(2\pi))-\tfrac t2.       \tag{7}
\]

The O(1) endpoint phase loss follows directly from (5)–(6); the
integrable carrier error and bounded eta are uniform on this dyadic
interval. No fixed-H count error is assumed uniform in moving H.

**Run bound with multiplicities.** For each of these complete cells put
k_j=N_+(g_{j+1})-N_+(g_j), a nonnegative integer. A good cell has k_j=1;
a bad cell has k_j!=1. Take a run of good cells with endpoints u=g_p
and v=g_q. If g_i<=x<g_{i+1} lies in the run, then

\[
 N_+(x)-N_+(u)=(i-p)+e(x),\quad 0\le e(x)\le1,
 \qquad (\phi(x)-\phi(u))/\pi=(i-p)+r(x),\quad0\le r(x)<1.
\]

All k_j=1 in the run count full multiplicity, so the first assertion
holds even if the unique zero occurs at the right endpoint. At x=v
both differences are q-p, and their difference is zero. Therefore

\[
 R(x):=N_+(x)-N_+(u)-(\phi(x)-\phi(u))/\pi
 \quad\hbox{satisfies}\quad |R(x)|\le1\quad(u\le x\le v).
\]

Combining (3) with phi=vartheta+delta shows, for any x,y in this same run,

\[
 S_+(y)-S_+(x)=R(y)-R(x)+(\delta(y)-\delta(x))/\pi,
 \qquad |S_+(y)-S_+(x)|\le B:=2+2D/\pi.              \tag{8}
\]

A strip zero at the excluded run endpoint u is already counted in
N_+(u) and cancels; no hypothesis about that endpoint is needed.

**Exceptional neighborhoods and full moment errors.** Write K_T for
the number of bad complete cells. Choose a fixed C>0 below and take
h=C/log T; for large T, 0<h<1 and T^(3/4)<T, so (2) applies. Let
X_T be the union, intersected with [T,2T], of the two boundary regions
{t<a_T} and {t+h>b_T}, and of [g_j-h,g_{j+1}] for every bad cell.
Endpoints of these sets have zero measure. By (6),

\[
 |X_T|\le2w+h+(w+h)K_T
       =\frac{C+8\pi+(C+4\pi)K_T}{\log T}.           \tag{9}
\]

Outside X_T the window [t,t+h] is contained in one run of good cells,
so (8) bounds |S_+(t+h)-S_+(t)| by B. This remains true if there are
no bad cells; a_T,b_T supply the only exceptional boundaries then.

Let ell=log(2+C), independent of T. From the complete errors in (2)
there are finite positive constants K_1,K_2 independent of T and C
(with a=3/4 and m=1,2 fixed) for which

\[
 I_2:=\int_T^{2T}|S_+(t+h)-S_+(t)|^2dt
 \ge T[\ell/\pi^2-K_1(1+\sqrt\ell)],
\]
\[
 I_4:=\int_T^{2T}|S_+(t+h)-S_+(t)|^4dt
 \le T[3\ell^2/\pi^4+K_2(4+\ell^{3/2})].             \tag{10}
\]

The fixed factors (Am)^m are absorbed into K_1,K_2; neither term
in the original error is dropped. Choose C once, sufficiently large
that ell/pi^2-K_1(1+sqrt ell)>=B^2+1. Such a finite C exists because
the linear term in ell dominates its square root. Define the finite
positive constant U=3ell^2/pi^4+K_2(4+ell^(3/2)). Then (8), (10) and
Cauchy–Schwarz give

\[
 T\le\int_{X_T}|S_+(t+h)-S_+(t)|^2dt
 \le |X_T|^{1/2}I_4^{1/2}\le(|X_T|UT)^{1/2}.
\]

Thus |X_T|>=T/U. With (9),

\[
 K_T\ge\frac{T\log T}{U(C+4\pi)}
          -\frac{C+8\pi}{C+4\pi}
      \ge\kappa T\log T,\qquad
 \kappa:=\frac1{2U(C+4\pi)}>0                       \tag{11}
\]

for all sufficiently large T. This is a fixed-C inequality with a
fixed positive surplus; it is not an asymptotic with relative error o(1).

**Exact complete-cell count balance.** The half-open cells are disjoint
and tile exactly (a_T,b_T]. Consequently

\[
 d_T:=\sum_j k_j-n_T
  =N_+(b_T)-N_+(a_T)-(\phi(b_T)-\phi(a_T))/\pi
  =S_+(b_T)-S_+(a_T)-(\delta(b_T)-\delta(a_T))/\pi
  =O(\log T).                                       \tag{12}
\]

This uses (3)–(4) at the actual moving endpoints; no zeros in incomplete
boundary cells are assigned to the sum, and no endpoint multiplicity is
discarded. Let Z_T count cells with k_j=0, let M_T count those with k_j>=2,
and set P_T=sum_(k_j>=2)(k_j-1). All sums are finite, M_T<=P_T, and

\[
 d_T=P_T-Z_T,\qquad K_T=Z_T+M_T\le2Z_T+d_T.
\]

Equations (11)–(12), enlarging the onset so that
|d_T|<=(kappa/2)T log T, imply

\[
 Z_T\ge(K_T-d_T)/2\ge (\kappa/4)T\log T.
\]

Take c=kappa/4. A zero count of zero excludes every full-strip ordinate
in the half-open cell because all its multiplicities are positive.
This proves (1), with the claimed positive proportion following from
(7). It leaves a zero at the left endpoint possible, so none of the
stronger sign or common-zero conclusions in the qualifications has
been used or established. ∎

### Critical audit, 2026-10-10

The separately approved audit, under
`drafts/literature/2026-10-10-variable-response-cell-occupancy-audit.md`,
validates (1) without a repaired hypothesis, new estimate or stronger
conclusion. This is a REPRODUCTION audit of the existing specialization.
The imported result remains Tsang's theorem as reproduced in Trudgian
Theorem 5.1; the original Tsang proof is not claimed checked.

**Phase and moving endpoints.** L366's reflected identity gives exactly
G=Re(QbZ), with b as displayed above. Since p=t^2+1/4 is positive,
Q/|Q| is exp(i vartheta), with the continuous Hardy gamma argument.
For t>=2, Re b>0 and Im b<0, so the displayed negative arctangent is
the continuous argument of b on this whole ray. Taking the Euler
logarithm itself, rather than a principal argument, gives |eta|<=E.
Thus phi=vartheta+beta+eta is a permissible L372 phase; a different
carrier branch merely relabels its zero levels by a fixed even integer.
In particular (4) bounds the correction on the branch actually used.
The uniform derivative estimate has constants independent of t and T.
On [T/2,3T], log(t/(2pi))=log T+O(1), proving (5) with one onset.
Phase increments of pi give (6) and the two boundary distances. Using
L372's explicit error C_0/a_T+2E for the phase difference, and the
O(1) phase losses from each boundary, proves (7) uniformly in real T.
No O_H(1) constant is substituted with an uncontrolled moving H.

**One-sided residual.** Off zero ordinates the cited exact formula
uses the standard Hardy argument. Its right limit counts all zeros at
that ordinate, since zeros in a compact height interval are finite and
vartheta is continuous. This proves (3), including its growth bound,
despite the source's strict-count notation. At an internal grid point
x=g_i, both count and phase differences from u equal i-p, so R(x)=0.
Inside a good cell, its full-multiplicity count is either 0 or 1, and
the phase fraction lies strictly between 0 and 1. Their difference is
in [-1,1]. At x=u and x=v it is zero. A zero at u cancels in N_+(x)-N_+(u);
a zero at an internal or final right endpoint belongs to the preceding
cell exactly once. This verifies every endpoint case of (8), including
a window ending at a grid zero. It makes no assumption about F_0.

**Exceptional set.** Its left boundary portion has length at most w;
its right portion, including the extension by h, has length at most w+h.
Every bad cell contributes at most its length plus h, hence at most w+h.
Overlap can only reduce the union's measure. Conversely, a window
outside this union lies inside [a_T,b_T], meets no bad cell, and hence
lies in one consecutive run of good cells. Closed neighborhood endpoints
may be overcounted and form a null set. These observations verify (9)
even when a_T=T or b_T=2T, or when there are no bad cells. No moment
integral beyond [T,2T] is required: its integrand already uses t+h.

**Moment surplus and quantifiers.** Reinspection of Trudgian Theorem
5.1 and the complete pp. 242–244 argument confirms the stated ranges
and the complete error in (2). With a=3/4 and H=T these apply for all
sufficiently large T, uniformly over 0<h<1. For m=1 the main coefficient
is 1/pi^2 and the error is bounded by K_1(1+sqrt ell); for m=2 they are
3/pi^4 and K_2(4+ell^(3/2)), respectively. Thus K_1,K_2 are fixed
before choosing C. The function ell/pi^2-K_1(1+sqrt ell) tends to
infinity, so one finite C gives the stated surplus B^2+1. Only after
this choice is T increased to ensure h=C/log T<1 and all phase bounds.
The source's simplified (42), with log(3+h log T), is not used.
Subtracting the integral over the good set loses at most B^2 T;
Cauchy–Schwarz with the full fourth moment then gives |X_T|>=T/U.
Inserting (9) yields (11) with fixed kappa>0. There is no fixed-C
relative o(1) assertion or limit requiring C to grow with T.

**Count balance and final threshold.** Telescoping over (a_T,b_T]
retains every included multiplicity and excludes every multiplicity at
a_T. The phase increment is exactly pi n_T. Subtracting these two
quantities therefore gives exactly (12), not an approximate boundary
count. The right-limit S bound controls it by O(log T) even when
either moving endpoint is a zero ordinate. For each bad cell the
integer alternatives are k_j=0 or k_j>=2, so M_T<=P_T and
K_T<=2Z_T+d_T have the indicated direction. After increasing T once
more, |d_T|<=(kappa/2)T log T, giving Z_T>=(kappa/4)T log T.
Thus the proof really attains the required fixed threshold with
c=1/[8U(C+4pi)]>0 for every sufficiently large real T. Constants and
onset remain unevaluated. No multiplicity bound in either incomplete
boundary cell is needed.

The canonical mathematical inputs remain L366, L368 and L372. The
audit establishes no new theorem beyond this checked specialization.
An empty (g_j,g_(j+1)] still permits F_0(g_j)=0; neither a strict
adjacent product nor a common-free Wronskian witness has been proved.

## Mathlib

Full matching variable-response empty-cell theorem and shifted-S moment
theorem: **not checked**. No matching Mathlib theorem is asserted absent.
Supporting Euler-log coverage is inherited from L372 and L368; general
measure inequalities alone would not supply (2) or this zeta application.
