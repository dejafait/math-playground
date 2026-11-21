# C467s — An actual upper-pair adjoint and a failed conjugate triangle match

## Hypotheses

Retain C467k/audit1033, C467l/audit1037, C467p/audit1049,
C467q/audit1053 and C467r/audit1056, with their actual coefficient
flow, raw time and original forms. In particular,

\[
n=3,\quad R=1/4,\quad a=1/16,\quad T_0=1/1920,
\quad X=1/256,\quad b_*=1/4096,\quad H_*=1/128,
\]
\[
\beta(z)=B(1+z)-B(1)-B'(1)z,\quad g=\beta',\qquad
H=H_0+\sum_j\beta(z_j),\quad H_0\in\mathbb R,
\]
\[
F=\Delta^2 e^{-H},\qquad
\Omega=F\bigwedge_{j=1}^3(dz_j/i).
\tag{1}
\]

The actual logarithm has conjugation normalization,
beta(conj z)=conj beta(z), beta(0)=beta'(0)=0, and |beta''|<40
on |z|<R. No identity beta(-z)=beta(z) is assumed. Retain all
input qualifications, including L018/C466a's unreplayed external
first-zero existence input when using C467q's nontriviality of
G(y)=Re g(iy). No density realization, global sign or RH is assumed.

Let f be the fixed smooth real bump with 0<=f<=1, f=1 on
[-b_*,b_*], and support in (-2b_*,2b_*). For any bump g_b with
these properties, write phi_p^{g_b} and psi_r^{g_b} for precisely
C467p(33)–(35)'s selected pair and C467r(18),(20)'s selected triangle
functions. The symbol g_b here is a bump argument, distinct from
g=beta'. Their constructions allow every such fixed bump. Write
f^sharp(u)=f(-u).

The adjacent triangle is exactly C467k's j=1 map

\[
Z_1=(1-r)\bar v\,\mathbf1+
r[(1-\lambda)(v_2,v_1,v_3)+\lambda(v_3,v_1,v_2)].
\tag{2}
\]

Its upper pair is the actual trace from (x,x,x+h), h<0, with
paired ranks (2,3), singleton rank1, slot order sigma=(1,3,2)
and orientation sign -1 from C467k's table. Apply the same common
minus normalization to every whole form.

## Conclusion

On one common positive interval the functions

\[
\phi_-(t,x,s,h)=\phi_p^{f^\sharp}(t,-x,-s,-h),\qquad
\psi_1^{\rm nat}(t,x,r,\lambda)
 =\psi_r^{f^\sharp}(t,-x,r,1-\lambda)
\tag{3}
\]

satisfy the nominated range, continuity, positive-time interior
smoothness and fixed-endpoint extensions on their respective boxes.
They have initial data f(x)^2 f(x+h) and f(x)^3, solve their original
undivided real adjoints, have all four separate complex derivative
products in L1 on each piece, and satisfy the complete independent-cutoff
complex identities, with zero inner radial flux for the triangle.
They have the exact whole outer-edge equality

\[
\psi_1^{\rm nat}(t,x,1,\lambda)
 =\phi_-(t,x,1-2\lambda,0).
\tag{4}
\]

They do **not** satisfy the prescribed shared radial equality
psi_1(t,x,r,0)=psi_r^f(t,x,r,1) on any positive common interval.
Already at r=0 their difference is nonzero somewhere for every
sufficiently small positive time. The precise leading difference is
(17) below.

This is attempt1058's partial construction and rejection of its natural
conjugate matching ansatz, not an exclusion of the full nominated
class. Arbitrary upper-pair and adjacent-triangle adjoints might have
different free side data. Neither uniqueness in that class nor the
direction of its shared-side characteristics has been proved here.
The result is unaudited. Other triangles, chamber matches, exterior
payment, realization, all degrees and actual-Xi positivity remain open.
This is not a complete RH candidate or a certified novelty claim.

## Proof

### Gate, imports and actual conjugation

The prior EXPLORE assessment is
`drafts/literature/2026-11-16-adjacent-triangle-matching-nomination-1056.md`,
completed by separate source review1057. This calculation is within its
unchanged matching target. That assessment explicitly makes a failed
reflection or chosen construction inconclusive for the whole class.
The present proof supplies the actual conjugation identities rather
than assuming invariance under z->-z. No additional source review is
claimed.

The existence, derivative estimates and full cutoff limits in (3)
are imported from C467p and C467r with the applicability argument below;
their proofs are not repeated. Their standard tools are Gerald Teschl,
*Ordinary Differential Equations and Dynamical Systems*, April2012
preliminary version, [Lemma2.14/Corollary2.15, pp52–53; Theorem3.9,
p81; Theorem6.1, pp189–190](https://www.mat.univie.ac.at/~gerald/ftp/book-ode/ode.pdf),
Brian Conrad, *Math396. Stokes' theorem with corners*,
[Theorem1.1, pp1–3](https://math.stanford.edu/~conrad/diffgeomPage/handouts/stokescorners.pdf),
and John K. Hunter, *Measure Theory*, [Chapter4, Theorem4.24,
pp49–50](https://www.math.ucdavis.edu/~hunter/measure_theory/measure_notes_ch4.pdf#page=11).
The already assessed source versions are reused. Only smooth positive-time
charts and the existing controlled limiting flows are used below.

Let C denote componentwise complex conjugation and P_23 the exchange
of target slots 2 and 3. The actual distinct-root equation is

\[
Y_j'=2\sum_{k\ne j}\frac{Y_j-Y_k}{|Y_j-Y_k|^2}
                    -\overline{g(Y_j)},\qquad Y(0,u)=iu.
\tag{5}
\]

Conjugating (5), and using g(conj z)=conj g(z), gives exactly the
same equation with initial data -iu. Smooth ODE uniqueness away from
the initial divisor gives Y(t,-u)=conj Y(t,u). Passing to C467k/l's
actual ordered boundary limits preserves this equality. In particular
q_j(t,-x)=-q_(4-j)(t,x), and v_j(t,-x)=conj v_(4-j)(t,x) for
the triple. Its mean y=E1/3 is odd in x and its real mean m is even.

For the lower connector Z_+(t,x,s,h), h>0, conjugation reverses the
order inside the paired slots. Thus the actual target upper connector
and (2) obey exactly

\[
Z_-(t,x,s,h)=P_{23}C Z_+(t,-x,-s,-h),
\]
\[
Z_1(t,x,r,\lambda)=P_{23}C Z_0(t,-x,r,1-\lambda).
\tag{6}
\]

For the second identity, the transformed old vertices V0 and V1
are respectively V2 and V1; reversing lambda gives V1 then V2.
For the first, conjugation interchanges low and high paired ranks;
s->-s restores their required order, and P23 puts the singleton in
slot2. These are the actual maps, not new reflected backgrounds.

Since H0 is real and F is symmetric in the slots,

\[
C^*\Omega=-\overline\Omega,\qquad
P_{23}^*\Omega=-\Omega,
\qquad (P_{23}C)^*\Omega=\overline\Omega.
\tag{7}
\]

The first minus sign is the product of the three minus signs from
conjugating dz/i; the second is the odd slot permutation. Consequently
each upper pulled-back form in (6) is the parameter-reflection pullback
of the complex conjugate lower form. This also holds after the common
minus normalization. Exterior differentiation, real part and wedge
product commute with these pullbacks, so (3) solves exactly the original
real adjoints, including their unchanged divisor zeros.

The bump f^sharp has every required property. Its initial lower-pair
value after reflection is f(x)^2 f(x+h), and its triangle value is
f(x)^3. The parameter changes have constant diagonal derivatives of
magnitude one (with lambda translated before sign reversal). Therefore
the four original coefficient/coordinate-derivative products correspond
one by one up to signs and complex conjugation. Their absolute
integrals are exactly the corresponding finite C467p/r integrals.
No sum cancellation or derivative estimate for an unspecified upper
test has been substituted.

The pair reflection maps h=-eta to h'=eta, time epsilon to epsilon,
and every other face to its reflected counterpart. It reverses the
dt dx ds dh orientation, consistently with the target odd slot order.
The triangle reflection reverses x and lambda and preserves its
dt dx dr dlambda orientation. Change of variables in each entire
Stokes identity, including boundary orientation, therefore transfers
all faces and all four bulk terms. Cutoff independence is preserved
because their positive magnitudes are unchanged. The triangle's
O(eta^8 T^4) inner flux bound transfers unchanged. This proves the
claimed full complex limits and absence of an additional corner term.
The whole outer equality is C467r(3) with s'=-s. Taking the minimum
of the finitely many available positive times gives one common interval.

### Both actual vertex graphs in a common mean coordinate

It remains to test the radial equality rather than infer it from (6).
All following triples are evaluated at x=x(t,y), the common inverse
of y=E1(t,x)/3. Define

\[
d_+=q_3-y,\quad d_-=q_1-y,\quad
S=\tfrac13\sum_j(q_j-y)^2,\quad c=\Pi_3,
\quad a_0=-\Pi_2-y\Pi_3,\quad m=\tfrac13\sum_jP(q_j).
\tag{8}
\]

The notation a0 in (8) is a slope, not the fixed analytic radius a.
The functions m,c,a0 are smooth in physical (t,y). For either
singleton d=d_+ or d_-, the quadratic reconstruction gives exactly

\[
k_p=a_0-cd,\qquad k_s=a_0+c(d-S/d).
\tag{9}
\]

Here kp is the secant of the other two roots, and ks is the singleton's
mean-subtracted quotient. This follows by writing P(z)=A0+A1 z+c z^2,
A1=-Pi2-3y c, using the paired sum 2y-d and the mean square y^2+S.
Thus (9) is valid also for the negative singleton; it invokes no
symmetry of beta under negation.

For the plus triangle use e+=(-1/2,-1/2,1), v+=(-1,1,0);
for the minus triangle use e-=(-1/2,1,-1/2), v-=(-1,0,1).
In either case the physical graph is

\[
Q=y\mathbf1+\ell\mathbf e_\pm+w\ell\mathbf v_\pm,
\qquad p=m\mathbf1+k_s\ell\mathbf e_\pm+k_p w\ell\mathbf v_\pm.
\tag{10}
\]

For the plus triangle ell=r d+; at its shared side lambda=1,
w_+(t,y)=-(q2-q1)/(2d+). For the minus triangle ell=r d-<0;
at its shared side lambda=0, w_-(t,y)=(q3-q2)/(2d-).
Both endpoint values tend to -1/2. Formula (10) for the minus
triangle is also the exact coordinate transform of (6).

The determinant and phase calculation C467q(11)–(16), applied in
these two displayed bases, gives the same formulas for the mean
component and the angular component of the vertex field:

\[
u_0={-i m_t\over1-i m_y},\qquad
u_j={-i k_{j,t}+i k_{j,y}u_0\over1-i k_j}\quad(j=p,s),
\]
\[
K=4(k_p+i)^2[\tfrac94(k_s+i)^2-(k_p+i)^2w^2]^2
e^{-H_0-3\beta(m+iy)}(1-i m_y)(1-i k_s)(1-i k_p),
\]
\[
Y=-{m_t\over1+m_y^2}\left(m_y+{\operatorname{Im}K\over\operatorname{Re}K}\right),
\quad \dot w=w(B_p-B_s),\qquad
B_j=-{\operatorname{Re}(K u_j)\over\operatorname{Re}K}.
\tag{11}
\]

These are formulas at ell=0 for the regular auxiliary fields.
The ell equation is multiplicative, so ell=0 is invariant. A basis
orientation sign cancels from every quotient in (11). Near w=-1/2
the same nonzero real-part floor as C467r(8) holds, on both graphs.
The original forms are still zero at the vertex. Equations (11)
describe the limiting flows of the two constructed tests; they do not
assert a vertex transport equation for every continuous admissible test.

### The first difference in the two transported vertex values

Put G(y)=Re g(iy) and theta(y)=-3 Im beta(iy). C467q(25) gives
m_t(0,y)=-G(y), c_t(0,y)=-G''(y)/2. C467k's smooth root
rescaling, with C467q(8), gives uniformly on a compact mean interval

\[
d_\pm=\pm\sqrt6\sqrt t+O(t),\quad S=4t+O(t^{3/2}),
\quad c=-\tfrac12G''(y)t+O(t^2).
\]
\[
k_p^\pm=a_0\pm{3\over\sqrt6}G''(y)t^{3/2}+O(t^2),\qquad
k_s^\pm=a_0\mp{1\over\sqrt6}G''(y)t^{3/2}+O(t^2).
\tag{12}
\]

All remainders used here come from smooth functions of (sqrt(t),y).
In particular k_p-k_s=t^(3/2) times a smooth such function, so
its physical time derivative is O(sqrt(t)). Formula (11) therefore
gives |B_p-B_s|<=C sqrt(t), uniformly near w=-1/2. The same
factorizations bound the needed y derivatives. No derivative of an
unqualified O-term is taken.

Define the isotropic comparison Y_iso by replacing both slopes in
(11) by the common smooth a0. Its phase is independent of w because

\[
K_{\rm iso}=-4(9/4-w^2)^2e^{-H_0-3\beta(m+iy)}
                   (1-i m_y)(1-i a_0)^8.
\tag{13}
\]

Thus Y_iso(t,y) is smooth in physical (t,y), with bounded y derivative.
At time zero its phase modulo pi is theta(y). A real-part floor
holds since |3beta(iy)|<1/16 in the selected mean domain.

At kp=ks=0, the imaginary logarithmic derivatives of K with respect
to kp and ks at w=-1/2 are respectively -5/2 and -11/2. Explicitly,
with A=9/4-w^2, those derivatives are

\[
-3+4w^2/A,\qquad -1-9/A.
\tag{14}
\]

They include the determinant factors, not just the Vandermonde.
Substitute (12) into (14): the plus phase increment is
[-(5/2)(3/sqrt6)+(11/2)(1/sqrt6)]G'' t^(3/2)
=-(2/sqrt6)G'' t^(3/2); the minus increment is its negative.
Differentiating Y in (11) with respect to this phase multiplies it
by -m_t sec^2(theta)/(1+m_y^2), whose time-zero value is
G sec^2(theta). Smooth Taylor expansion on the nonzero-phase box gives

\[
Y_\pm(s,z,0,w)=Y_{\rm iso}(s,z)\mp A_*(z)s^{3/2}
 +O(s^2+s^{3/2}|w+1/2|),
\]
\[
A_*(z)={2\over\sqrt6}G(z)G''(z)\sec^2\theta(z).
\tag{15}
\]

Here s is the running physical time, and z a mean coordinate.
The error is uniform for z in a fixed compact interval and w near
-1/2. This expansion uses a smooth phase branch modulo pi; the
quotient Im K/Re K makes the choice immaterial.

Fix terminal (t,y) and terminal angular coordinates w_+(t,y) and
w_-(t,y) from (10). Follow the two regular vertex fields backward to
zero, writing their means y_+(s), y_-(s). These are exactly the
vertex flows defining the two functions in (3): C467r(20) gives the
plus one, and (6) transforms it for the minus one. The endpoint
margins of C467r and its reflected construction justify the paths
on one common interval, even if they cross an original angular side.

Both satisfy y_pm(t)=y and |y_pm(s)-y|<=Ct. Their angular variables
satisfy |w_pm(s)+1/2|<=C sqrt(t): the terminal error is O(sqrt(t))
and the integral of the angular velocity bound above is O(t^(3/2)).
Using (15) and the bounded derivative of Y_iso, the integral equation
and Gronwall first give sup_s |y_+(s)-y_-(s)|<=C t^(5/2).
Subtract their backward integral equations. The integral of the
Y_iso difference is O(t^(7/2)); replacing A_*(y_pm(s)) by A_*(y)
also costs O(t^(7/2)). The two error terms in (15) integrate to
O(t^3) and O(sqrt(t) t^(5/2))=O(t^3). Consequently

\[
y_+(0)-y_-(0)
=2A_*(y)\int_0^t s^{3/2}\,ds+O(t^3)
={8\over5\sqrt6}G(y)G''(y)\sec^2\theta(y)t^{5/2}+O(t^3).
\tag{16}
\]

The plus sign in (16) is the backward-time sign applied to
Y_plus-Y_minus=-2A_* s^(3/2). C467r's vertex formula is f of
the corresponding time-zero mean, cubed; for the reflected test
f^sharp at the reflected mean is exactly f at the unreflected mean.
Thus, with x=x(t,y), the actual shared-side difference is

\[
\begin{split}
&\psi_r^f(t,x,0,1)-\psi_1^{\rm nat}(t,x,0,0)\\
&\quad={8\over5\sqrt6}(f^3)'(y)G(y)G''(y)
                 \sec^2\theta(y)t^{5/2}+O(t^3).
\end{split}
\tag{17}
\]

Taylor's formula for f^3 justifies the final step: both means differ
from y by O(t), and their mutual difference is O(t^(5/2)).

On some open interval in (b_*,2b_*) one has 0<f<1 and f'!=0.
C467q(4)–(5), with its stated first-zero qualification, proves that
the analytic functions G and G'' are nonzero and their product cannot
vanish on such an interval. Choose y0 there with G(y0)G''(y0)!=0.
The coefficient in (17) is nonzero. Since t^3=o(t^(5/2)), the
difference is nonzero for every sufficiently small positive t at
x(t,y0), which lies strictly inside (-X,X). This refutes the exact
radial equality for the constructed pair (3), on every positive time
interval. By continuity it also cannot hold for every r>0 and then
extend to r=0.

### Scope of the failed match

The original inner radial flux is zero for both constructed tests;
that does not equate their parameter-vertex values. No single physical
vertex value has been imposed. The discrepancy in (17) is between two
selected functions with allowed angular vertex values, so it is not a
reuse of C467q's stronger excluded hypothesis.

Conversely, an arbitrary adjacent solution may be fed by its angular
boundary and need not be the minus limiting flow chosen above.
Neither initial data nor the present L1 hypotheses alone have been
shown to make (3) unique. To turn this residual into a class obstruction
one would need a justified one-sided characteristic argument in the
actual adjacent domain, including the direction at the shared side,
and show that continuity forces its outgoing vertex trace to equal
the natural one on a bump-transition interval. If that boundary is
incoming, the prescribed trace could instead be admissible inflow.
That test is left unresolved; (17) alone does not decide it.

## Mathlib

Full Mathlib coverage of this actual conjugation specialization, the
two constructed adjoints and the t^(5/2) trace discrepancy was not
checked. C467k/p/q/r retain their supporting coverage notes. Ordinary
smooth ODE theory, Taylor expansion, pullback of forms, Stokes and
dominated convergence are used only in the stated roles; no matching
Mathlib theorem is claimed present or absent. No numerical evidence
or mathematical script is used as a proof.
