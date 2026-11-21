# Lemma 883: contact-cell periods reduce to a label-primitive phase test

## Hypotheses

Assume exactly L882's boundary odd-contact hypotheses. In particular,
use L847's actual entire function and its real coefficients,

\[
 G(z)=\tfrac18\xi(\tfrac12+\tfrac{\sqrt z}{2})
     =\sum_{n\geq0}a_nz^n,\qquad a_n>0,\qquad
 C=R^2/G(R)^2>0,
\]
\[
 \omega=C\frac{G(z_1)G(z_2)(z_1-z_2)^2}{z_1^3z_2^3}
                      dz_1\wedge dz_2,
 \qquad z_j(y)=R e^{u_j(y)+iy_j}.
                                                        \tag{1}
\]

Here u is smooth, real and periodic, J=det(I-iDu) is nowhere zero,
and L879's off-zero real radial stationarity gives
Phi_u^*omega=Q dy1 wedge dy2 with Q=lambda*s, |lambda|=1 and s real.
L882 supplies simple actual G-zero labels zeta,theta,eta and fibers

\[
 z_1(a,t)=\zeta,\quad z_1(c,t)=\theta,\qquad
 z_2(t,a)=\zeta,\quad z_2(t,b)=\eta.                       \tag{2}
\]

Choose a real lift a of arg(zeta), and the unique lifts
c,b in (a,a+2pi) of arg(theta),arg(eta). Thus theta!=zeta,
eta!=zeta, and b=c exactly when theta=eta. Both L882 label branches
and all their other zeros and multiplicities remain in scope.
No product-graph, sign-per-cell, symmetry, analytic-u, collar, finite
pullback-contact census or existence hypothesis is added.

Put E1=[a,c], E2=[c,a+2pi], K1=[a,b], K2=[b,a+2pi], with every
interval increasing. The four cells Ep x Kq carry the original
dy1 wedge dy2 orientation. Their unnormalized integrals are I_pq.

## Conclusion

For j=0,1,2 define the single-valued function on C*

\[
 H_j(z)=\sum_{\substack{n\geq0\\n\ne j}}
                  \frac{a_n z^{n-j}}{n-j},\qquad
 r=(a_0,a_1,a_2),\quad T=2\pi i r,\quad
 S(x,y)=x_0y_2-2x_1y_1+x_2y_0.                            \tag{3}
\]

There are finitely many negative powers in H_j. Its remaining series
is entire. Set H=(H_0,H_1,H_2) and

\[
 \begin{split}
 A&=H(\theta)-H(\zeta)
       +r\left(\log\frac{|\theta|}{|\zeta|}+i(c-a)\right),\\
 B&=H(\eta)-H(\zeta)
       +r\left(\log\frac{|\eta|}{|\zeta|}+i(b-a)\right).
 \end{split}                                             \tag{4}
\]

Then the actual four integrals, including all side-boundary effects,
are exactly

\[
 (I_{pq})=C
 \begin{pmatrix}
 S(A,B)&S(A,T-B)\\
 S(T-A,B)&S(T-A,T-B)
 \end{pmatrix}.                                         \tag{5}
\]

No choice of the unknown graph remains in (5) after its actual labels
and their angular lifts are fixed. Complementary arcs have increments
T-A and T-B; the full-turn residue terms must not be dropped.

The four entries must lie on lambda*R. Equivalently,

\[
 S(A,B),\quad S(A,T),\quad S(T,B),\quad S(T,T)
                         \ \in\lambda\mathbb R.          \tag{6}
\]

Write d=a1^2-a0*a2. The sum is the existing total-period identity

\[
 \sum_{p,q}I_{pq}=8\pi^2 C d=(2\pi)^2 M.                 \tag{7}
\]

If d!=0, the line in (6) is R. Define the single-valued real function

\[
 V(z)=\operatorname{Re}\{a_2H_0(z)-2a_1H_1(z)+a_0H_2(z)\}
                              -2d\log|z|.               \tag{8}
\]

In this case the four-cell common-line test is precisely

\[
 V(\theta)=V(\zeta)=V(\eta),\qquad
                        \operatorname{Im}S(A,B)=0.       \tag{9}
\]

The V values in (9) do not depend on logarithm branches. The
mixed condition retains the prescribed lifted arc increments. No
nonzero-period assertion is needed for (5)-(7); when d=0 use (6)
with the actual lambda, without replacing its line by R.

For theta=eta, B=A and I12=I21. There is a precise survival case:
if theta=eta=conjugate(zeta)!=zeta, then A=B is purely imaginary,
so all four expressions in (5) are real automatically. Thus these
cell values admit the real common line. If d=0, compatibility with a
prescribed graph phase lambda still requires (6); reality alone does
not check that phase. This is conditional on the indicated actual
labels; no such graph or off-real zero is constructed or asserted.

This is a local exact evaluation and necessary label test, not a
boundary-branch exclusion. The equalities of primitive values are
analytic conditions not computed by the divisor census or by (7).
Whether they eliminate any nonconjugate label tuple permitted by
L882 is unresolved. No sign of a cell is asserted, and satisfying
(6) or (9) does not produce a stationary graph. The main all-degree
Xi-positivity gap, exterior alternatives, graph existence, compactness
and the sharp L868 threshold remain open. The independent conceptual
audit of 7 November 2026 below accepts (5)-(9) with these qualifications.
POTENTIALLY_NEW refers only to the prior bounded source comparison,
not certified originality; the audit is a REPRODUCTION.

## Proof

### Reused coverage and precise standard inputs

The unchanged invocation-start assessment
`drafts/literature/2026-11-07-contact-cell-relative-period-test.md`
has DECISION EXPLORE for exactly this four-cell test. The supplied
current gate requests its mathematical attempt; no new target or
source assessment is approved here. L847 supplies (1) and its
pullback convention, L879 the phase line, and audited L882 the fixed
fibers and their two label branches. Their proofs are not reproved.

Import Will J. Merry, *Differential Geometry*, ETH Zurich, academic
year 2020-2021, last modified 17 July 2021,
[Definitions 25.1/25.20 and Theorems 26.2/26.17,
PDF pp208,211,213,218-220](https://www2.math.ethz.ch/will-merry/files/Merry%20-%20Differential%20Geometry%20%282021%29.pdf#page=218).
The theorem is Stokes for smooth parameter cubes extending to a
neighborhood of the closed cube, with the signed cubical boundary.
Its pullback reduction does not require embedded or immersed cubes.
Apply it separately to real and imaginary parts. The explicit
comparison below checks smoothness, compactness and every side face;
Stokes alone does not supply that comparison.

For one-variable integration import Jiří Lebl, *Guide to Cultivating
Complex Analysis*, v1.10, 5 November 2026,
[Definition 4.1.1/Proposition 4.1.2, pp94-95](https://www.jirka.org/ca/ca.pdf#page=94),
[Theorem 4.3.3/Corollary 4.3.4, pp100-101](https://www.jirka.org/ca/ca.pdf#page=100),
and [Theorem 4.4.2/Proposition 4.4.3, pp104-108](https://www.jirka.org/ca/ca.pdf#page=104).
These supply tracked logarithm increments, primitives on simply
connected nonvanishing domains, and compactly convergent Laurent
series with the residue term separated from their primitives.
Proposition 4.4.3's proof is left as an exercise in the source; its
stated standard result is imported, not represented as a read proof.
The assessment inspected the essential proofs of the other inputs.
Below explicit logs along the arcs avoid assuming a global log on C*.
Only the residues at zero occur. No log of G or division by G at a
contact is introduced. Fubini applies only to smooth functions on
compact parameter rectangles.

These are known tools. The new work is their explicit application
to the four fixed fibers, followed by the label formulas and the
limited compatibility test. No general Stokes, Laurent or contour
existence theorem is reproved. The finite-real-box and retired
two-period stops retain their different scopes.

### Boundary-preserving comparison on each cube

Define smooth periodic real functions

\[
 v_1(y_1)=u_1(y_1,a),\qquad v_2(y_2)=u_2(a,y_2),
 \quad v(y)=(v_1(y_1),v_2(y_2)).                           \tag{10}
\]

For 0<=t<=1 use the displayed map

\[
 \Psi(t,y)_j=R\exp\{(1-t)u_j(y)+t v_j(y_j)+iy_j\}.        \tag{11}
\]

It extends smoothly across every closed parameter box
[0,1] x Ep x Kq. Affinely rescaling the positive-length intervals
gives the smooth cubes in the cited theorem without changing their
orientations. Periodicity supplies the same extension at lifted
seams. Boundedness of u,v on these compact cubes gives positive
lower and finite upper bounds on both moduli. Thus every image
lies in a compact subset of X=(C*)^2, where omega is smooth and
closed. Closedness follows also directly from (1): its coefficient
is holomorphic, and each holomorphic differential in its derivative
repeats dz1 or dz2 in the wedge.

Every side face is accounted for as follows. On y1=a or a+2pi,
both u1 and v1 equal log(|zeta|/R); their fixed argument gives
Psi1=zeta throughout the face. On y1=c the same argument gives
Psi1=theta. On y2=a or a+2pi, Psi2=zeta throughout the face, and
on y2=b it equals eta. These equalities use both the actual fibers
in (2) and their values in (10), not just the corner endpoints.
Hence on every side face G(Psi1)G(Psi2)=0. The ambient form itself
vanishes there by (1), so its pullback to each such face is zero.
No boundary homotopy in the divisor is being inferred from endpoint
membership; (11) proves it on the entire face.

Orient the parameter cube by dt wedge dy1 wedge dy2. Its t=1 face
has the positive cell orientation and its t=0 face the negative.
The upper/lower y1 faces carry respectively minus/plus dt wedge dy2;
the upper/lower y2 faces carry plus/minus dt wedge dy1. Each of those
four integrals is zero as just shown. Cubical Stokes therefore gives

\[
             \int_{E_p\times K_q}\Phi_u^*\omega
                  =\int_{E_p\times K_q}\Phi_v^*\omega.    \tag{12}
\]

The homotopy is allowed to meet any numerator zeros and the diagonal;
neither is a pole. It need not preserve stationarity or J!=0 at its
intermediate times. No such condition is required by Stokes. The
reference Phi_v is a product for evaluation only; (12) does not
assert that Phi_u is a product or transfer its pointwise phase to
the reference graph. Thus it does not conflict with L847's product
nonnegativity obstruction.

### Product-arc integrals and all logarithm increments

On C* let h_j=G(z) dz/z^(j+1), j=0,1,2. In coordinate order,

\[
 \omega=C\{h_0(z_1)\wedge h_2(z_2)
           -2h_1(z_1)\wedge h_1(z_2)
                    +h_2(z_1)\wedge h_0(z_2)\}.          \tag{13}
\]

This is the expansion of (z1-z2)^2 in (1), with no omitted i factors.
Let gamma(y1)=R exp(v1(y1)+iy1) and delta(y2)=R exp(v2(y2)+iy2).
Their first arcs go respectively from zeta to theta and from zeta
to eta, with increasing lifted angles. Their complementary arcs go
back to zeta at the terminal lift a+2pi. The one-variable Laurent
primitive formula gives

\[
                         h_j=dH_j+a_j\,dz/z.              \tag{14}
\]

Its hypotheses hold on every compact subannulus of C*: G is entire,
the negative terms are finite, and the remaining primitive series
converges locally normally. Thus (3) is single-valued there, whereas
the remaining residue term must be integrated with a lifted log.
Along gamma use log R+v1(y1)+iy1; along delta use
log R+v2(y2)+iy2. Their exponentials are exactly the arcs, and their
derivatives give dz/z. Formula (14) gives precisely A,B in (4).
Along a complete turn the H_j increments cancel by periodicity,
the radial log increment is zero and the angular increment is 2pi i.
Consequently the complementary vectors are T-A and T-B.

Using arbitrary endpoint logarithms instead changes the displayed
increment by 2pi i times its tracked integer. That integer is fixed
by the actual lifted arc; it is not a free adjustment to force a
phase identity. The radial-graph angular coordinates traverse each
of the indicated first arcs by an amount in (0,2pi), and the two
arcs together traverse exactly one full turn. Equations (4)-(5)
retain this full winding information, including arcs across a
chosen logarithm cut. A common change of lift a by 2pi leaves the
differences unchanged.

Fubini applied to (13) on each compact product rectangle, followed
by (12), now proves (5). Other G zeros, including the additional
simple interior or double boundary zero allowed by L882's unmatched
branch, produce no terms in (14): they are zeros of h_j, not poles.
The squared diagonal is already retained in (13). No sign per cell
or deletion of any zero has occurred.

### Phase test, total period and its limitations

The actual Q=lambda*s implies I_pq in lambda*R by integration over
each cell. Conversely the four numbers in (5) lie on that line if
and only if their first entry, first row sum, first column sum and
total sum do. These are respectively C times the four expressions
in (6). This converse is only a statement about four complex
numbers; it does not imply pointwise phase or stationarity.

Since S(r,r)=2a0*a2-2a1^2=-2d, we have
S(T,T)=(2pi i)^2 S(r,r)=8pi^2 d, proving the first equality in (7).
For the second, the constant angular coefficient of
F=-C G(z1)G(z2)(z1^-2-2(z1*z2)^-1+z2^-2)
on the radius-R torus is -C(2a0*a2-2a1^2)=2Cd.
The Taylor series are absolutely uniformly convergent on that
compact torus. This recovers M and agrees with L847's total-period
invariance. It supplies no new sign or nonzero assumption on d.

If d!=0, the nonzero real total forces lambda*R=R. Now
S(A,T)=2pi i S(A,r) and S(T,B)=2pi i S(r,B).
Their reality is equivalent to Re S(A,r)=Re S(r,B)=0.
Inserting (4), and using that r and d are real, gives

\[
 \operatorname{Re}S(A,r)=V(\theta)-V(\zeta),\qquad
 \operatorname{Re}S(r,B)=V(\eta)-V(\zeta).                 \tag{15}
\]

The remaining entry in (6) is real exactly when Im S(A,B)=0,
which proves (9). The equalities (15) show why the row and column
tests lose their logarithm-branch dependence, while the mixed test
still uses (4). If d=0, the argument fixing the line fails and is
not used. Formula (6), equivalently the vanishing imaginary parts
after multiplication by conjugate(lambda), remains the necessary
and sufficient common-line test for the four entries.

The total identity (7) alone cannot perform the row, column or mixed
tests: its algebraic derivation cancels all A and B. The count
identities in L881/L882 contain none of the values H_j at the labels.
This observation is not a proof that an actual permitted label tuple
fails (9), or that the full stationary hypotheses logically permit
one to fail it. Their consequence is exactly that no such stationary
graph can exist for a tuple failing (6). Determining the selectivity
of this analytic test on actual G zeros remains a separate question.

If theta=eta, the selected increasing lifts coincide and (4) gives
B=A, regardless of the shapes of gamma and delta. Symmetry of S
then gives I12=I21. Finally, since all a_n are real, local normal
convergence in (3) implies H_j(conjugate(z))=conjugate(H_j(z)).
If theta=eta=conjugate(zeta), each H difference in (4) is purely
imaginary and the modulus log is zero. The angular term is also
purely imaginary, with its actual full increment retained. Thus
A=B is purely imaginary; T, T-A and T-B are likewise purely
imaginary, and S of any two of them is real. In particular (9)
holds whenever d!=0; when d=0 the cell data still admit the real
common line, though (6) must use the actual graph's lambda.

This is the bounded test's demonstrated limitation: common-line
cell values do not rule out matched conjugate labels. Their signs,
pointwise phase realization and the feasibility of a graph with
those labels have not been established. The exact formulas retain
the unmatched branch and provide a necessary label criterion, but
no branch exclusion or actual off-line zero follows. A repeat aimed
at exclusion requires new actual-label separation or sign information,
not merely the sum (7) or a renamed winding calculation.

### Independent conceptual audit, 7 November 2026

This audit uses the unchanged invocation-start EXPLORE assessment
`drafts/literature/2026-11-07-l883-contact-cell-period-conceptual-audit.md`.
Read the complete proof above and reuse the accepted statements of
L847, L879 and L882. The primary Stokes and primitive coverage is
unchanged; no new theorem, actual-zero estimate or cell-sign premise
is imported. The checks below accept the stated local evaluation.

**Relative comparison and orientation.** L882 ensures a<c<a+2pi and
a<b<a+2pi, so all four affine parameter rectangles have positive
orientation. On the vertical faces a,a+2pi and c, the first components
of u and v are respectively log(|zeta|/R) and log(|theta|/R).
On the horizontal faces a,a+2pi and b, their second components are
respectively log(|zeta|/R) and log(|eta|/R). The angles are unchanged.
Consequently (11) fixes the required coordinate on
each entire side face, including its t direction. Corners satisfy
both applicable fixed-coordinate conditions. Periodic extensions of
u and v make the lifted seam a+2pi smooth, and the formula is also
smooth for t in a neighborhood of [0,1].

On the compact union of the four cubes there is a finite K with
|(1-t)u_j+t v_j|<=K for 0<=t<=1. Both coordinate moduli are therefore
between R exp(-K) and R exp(K). The poles at zero are absent. The
holomorphic top form is closed on this neighborhood, including every
G zero and diagonal point. Its coefficient is zero on each side
face; the side pullbacks vanish without any division by the vanishing
factors. With volume dt wedge dy1 wedge dy2, the t faces have signs
+/-; contraction by the upper/lower y1 normal gives -/+ dt wedge dy2,
and by the upper/lower y2 normal gives +/- dt wedge dy1. Thus Stokes
gives exactly (12), with no cell reorientation. Degeneracy of J along
the comparison is harmless: smooth singular cubes require no immersion.
Nor is stationarity of the product reference used.

**Convergence and monodromy.** On an arbitrary compact annulus
rho<=|z|<=L, rho>0, the positive-power tail of H_j is bounded termwise
by rho^(-j)|a_n|L^n, since n-j>=1. Its derivative tail is bounded by
rho^(-j-1)|a_n|L^n. Both majorants sum because G is entire. Together
with the finitely many negative powers, this verifies the local normal
convergence needed for H_j'=(G-a_j z^j)/z^(j+1). Formula (14) is
therefore valid even at a G zero. This is the specific applicability
check for the cited Laurent primitive, not a reproof of that theorem.

The lifted logs ell_gamma(y)=log R+v1(y)+iy and
ell_delta(y)=log R+v2(y)+iy are smooth on each complete parameter
interval and satisfy ell'=gamma'/gamma or delta'/delta. Their first
increments are exactly the modulus logs and positive angle changes
in (4); their complete increments are 2pi i. Subtracting first
increments gives T-A and T-B, including at arcs crossing any chosen
principal-log cut. At such a cut the local principal logs differ by
2pi i times an integer; the displayed smooth lift accounts for that
integer and never resets it at a cut. A different common lift a+2pi k
does not change the increments. Changing an individual arc winding
would be a different arc, not a permitted branch adjustment.

Expanding the numerator square gives h0(z1) wedge h2(z2),
-2h1(z1) wedge h1(z2), and h2(z1) wedge h0(z2), in that order.
Their pullbacks to the product reference have the original positive
dy1 wedge dy2 orientation. Compactness justifies each product integral
and Fubini. This proves all four entries of (5), with no discarded
factor of i. Extra numerator zeros, their multiplicities and the
diagonal square do not alter the primitive increments.

**Four-number test and normalization.** Put x=S(A,B), y=S(A,T),
z=S(T,B), w=S(T,T). The matrix divided by C is exactly

\[
 \begin{pmatrix}x&y-x\\z-x&w-y-z+x\end{pmatrix}.
\]

Its first entry, first row sum, first column sum and total recover
x,y,z,w. This invertible real-linear change proves (6) for any fixed
lambda, including d=0. It is only a test of four integrals. Directly,
S(r,r)=-2d and S(2pi i r,2pi i r)=8pi^2 d. Independently the three
constant terms of the radius-R expression for F are a2*a0,
-2a1^2 and a0*a2, multiplied by -C; hence M=2Cd and (7) has the
correct normalization. No positivity or nonvanishing of d is inferred.

For d!=0 the nonzero real total lies on lambda*R, forcing that line
to be R. Since Re(2pi i w)= -2pi Im(w) and
Im(2pi i w)=2pi Re(w), reality of S(A,T) is precisely Re S(A,r)=0;
the column condition is the exchanged statement. Substitution of (4)
gives (15): the real logarithm has coefficient S(r,r)=-2d, and the
angular term is purely imaginary. This checks the sign in V and
both equalities in (9). Its mixed condition uses the actual A,B.
When d=0, the zero total cannot select a line; only (6) is used.
In particular no nonzero-period input is hidden in this argument.

**Both branches and conditional survival.** For eta!=theta, the
calculation never identifies B with A or deletes either extra-zero
alternative in L882. For eta=theta, the prescribed lifts coincide,
so A=B despite potentially different arc shapes, and symmetry of S
gives I12=I21. If that common label is conjugate(zeta)!=zeta,
real coefficients and the verified normal convergence give
H_j(conjugate(zeta))=conjugate(H_j(zeta)). The real modulus logarithm
is zero, and the full angular term is imaginary; thus A=B and T
are purely imaginary. Every bilinear entry is real. For d!=0 this
passes (6); for d=0 it supplies a possible real common line, without
proving compatibility with an independently prescribed nonreal lambda.
The conclusion's wording now states that qualification explicitly,
as already required in the original proof. Similarly, the branch-free
claim in (9) refers to V; the mixed term retains its fixed arc lifts.

No error in (5)-(9) was found. The audit establishes a usable local
input, not a new theorem beyond the sources checked, a discriminating
test on actual labels, or a stationary graph. In particular it cannot
infer a sign for any cell, turn compatible numbers into a graph, or
exclude the matched conjugate pattern. The existing count-only,
finite-box and two-period stops are contrasts, not mathematical inputs.
The direct inputs remain L847, L879 and L882, exactly as in the DAG.

## Mathlib

Full matching coverage for this four-cell label-primitive formula,
and formal coverage of its supporting cubical Stokes, Laurent
primitive and lifted-arc specializations, have not been checked.
No absence claim is made. The cited primary statements supply the
informal standard inputs; no formal verification is claimed.
