# C467y — Cyclic pair/triangle selection by midpoint reflection

## Hypotheses

Retain the actual background, coefficient flow, maps and input
qualifications of C467k/audit1033, C467o/p/audit1049,
C467v/audit1066, C467w/audit1070 and C467x/audit1074. In particular,

\[
n=3,\quad R=1/4,\quad a=1/16,\quad T_0=1/1920,\qquad
X=1/256,\quad b_*=1/4096,\quad H_*=1/128,
\]
\[
\beta(z)=B(1+z)-B(1)-B'(1)z,\quad
H=H_0+\sum_{k=1}^3\beta(z_k),\quad
F=\Delta^2e^{-H},\quad
\Omega=F\bigwedge_{k=1}^3(dz_k/i).
\tag{1}
\]

B is the actual conjugation-normalized logarithm of
xi(1/2+sqrt(w))/xi(1/2); H0 is real and |beta''|<40 on |z|<R.
The qualifications through C467e/m/q/t/u, including
L018/L021/L024/C466a's unreplayed finite-zero/product inputs,
remain in force. No evenness of beta, RH, realization or all-degree
positivity is assumed. C467s is not an input.

Fix any smooth real f with 0<=f<=1, f=1 on [-b_*,b_*], and support
in (-2b_*,2b_*). No evenness or monotonicity of f is required.
Keep C467p's lower pair test phi_p exactly fixed. Let
phi_-, psi_0^x, psi_1^x be the particular tests constructed in
C467x, using its boundary correction (13), endpoint correction
(15), and backward outer-hit definition, not arbitrary tests
satisfying only C467x's conclusion.

Use all six actual triangle maps Z_j and incident pair maps P_j
in C467k's cyclic order and its six-row orientation table.
The pair variable is s=1-2lambda, with h>0 for even j and h<0
for odd j. Time is raw physical time; the divisor and common minus
normalization of every current are unchanged.

## Conclusion

After reducing to one common existential 0<tau<=T0, there are six
pair tests phi_j and six triangle tests psi_j, real and in [0,1],
continuous on the original closed boxes

\[
[0,\tau]\times[-X,X]\times[-1,1]\times I_j,
\quad I_j=[0,H_*]\ (j\text{ even}),\ I_j=[-H_*,0]\ (j\text{ odd}),
\]
\[
[0,\tau]\times[-X,X]\times[0,1]^2,
\]

smooth for t>0,h!=0 on each pair and t>0,0<r<1 on each triangle,
including angular midpoints and the inherited fixed-endpoint
neighborhood extensions. They satisfy

\[
\phi_j(0,x,s,h)=f(x)^2f(x+h),\qquad
\psi_j(0,x,r,\lambda)=f(x)^3,\qquad \phi_0=\phi_p,
\tag{2}
\]
\[
d\phi_j\wedge\operatorname{Re}(-P_j^*\Omega)=0,\qquad
d\psi_j\wedge\operatorname{Re}(-Z_j^*\Omega)=0,
\tag{3}
\]
\[
\psi_j(t,x,1,\lambda)=\phi_j(t,x,1-2\lambda,0),\qquad
\psi_j(t,x,r,1)=\psi_{j+1}(t,x,r,0)\quad(j\bmod6).
\tag{4}
\]

All four original complex derivative products on each piece are
separately L1, giving 48 individual products. Every complete tested
identity retains all its endpoints and has the limit with independent
cutoffs, also independent between pieces. Each inner radial flux is
zero. The six outer and six radial matching faces cancel with their
original induced orientations after those limits.

This is attempt1076's local construction, validated under its inherited
qualifications by independent conceptual audit1078 below. It is not a complete RH candidate or a certified
novelty claim. Chamber/pair endpoint matching, other interfaces,
exterior payment, realization, higher degrees and actual-Xi positivity
remain unproved. Neither a time-zero derivative nor one value shared
by all angular representatives of the physical vertex is asserted.

## Proof

### Source scope and the precise new step

The invocation-start EXPLORE assessment is
`drafts/literature/2026-11-16-cyclic-six-pair-triangle-selection-nomination-1074.md`,
separately completed by review1075. It covers exactly this simultaneous
selection. The comparison supplies no matching cyclic theorem; the
new local argument is a midpoint reflection of the accepted one-seam
selection, justified by an exact central collar where that selection
has not been modified. It does not assert that unmodified cyclic
copies of C467x already match.

Reuse the assessed ordinary smooth-flow existence, uniqueness and
dependence results in Gerald Teschl, *Ordinary Differential Equations
and Dynamical Systems*, author-hosted April2012 version,
[Theorems2.5/2.10 pp40-47, Lemma2.14/Corollary2.15 pp52-53,
Theorems3.9/3.12 pp81-84 and Theorem6.1 pp189-190](https://www.mat.univie.ac.at/~gerald/ftp/book-ode/ode.pdf).
They are applied only on the regular graph charts already estimated
in C467p/v/x, at positive separation or positive time. Singular
continuity, confinement and cutoff bounds are inherited from those
proved constructions, not inferred from these general theorems.

For the complete identities use Brian Conrad, *Stokes' theorem with
corners*, [Theorem1.1/proof pp1-3](https://math.stanford.edu/~conrad/diffgeomPage/handouts/stokescorners.pdf),
on positive-cutoff boxes, and John K. Hunter, *Measure Theory*,
[Chapter4, Theorem4.24 pp49-50](https://www.math.ucdavis.edu/~hunter/measure_theory/measure_notes_ch4.pdf#page=11),
componentwise on the complex products with the majorants below.
These standard results are imported rather than reproved.

The relevant recorded failures have different hypotheses. C467u
fixes C467r's entire radial trace, whereas the present triangles
are reselected. C467w fixes C467v's incompatible upper datum,
whereas C467x and the present reflection preserve the forced upper
midpoint. The joint-smooth obstruction does not concern continuity
at time zero. No stopped selection is silently reinstated.

### Exact paired-slot symmetries

F is invariant under every permutation of its three arguments:
Delta changes by the permutation sign and is squared, and H is a
sum with the same beta in each slot. Thus, for a slot permutation S,

\[
S^*\Omega=\operatorname{sgn}(S)\Omega.
\tag{5}
\]

This uses no conjugation and does not replace f by f(-x).
Let S_+=S12 exchange slots1,2, and S_-=S13 exchange slots1,3.
For the base lower and upper pair maps, respectively,

\[
P_0(t,x,-s,h)=S_+P_0(t,x,s,h),\quad
P_1(t,x,-s,h)=S_-P_1(t,x,s,h).
\tag{6}
\]

The corresponding triangle identities are

\[
Z_0(t,x,r,1-\lambda)=S_+Z_0(t,x,r,\lambda),\quad
Z_1(t,x,r,1-\lambda)=S_-Z_1(t,x,r,\lambda).
\tag{7}
\]

They follow exactly by exchanging the two endpoints of the affine
pair segment; the singleton and center remain fixed. If iota denotes
either parameter reflection, (5)-(7) give
iota^*(P_j^*Omega)=-P_j^*Omega or
iota^*(Z_j^*Omega)=-Z_j^*Omega. Consequently reflection carries an
adjoint solution to an adjoint solution, with the common minus sign
unchanged. The equality is for the original complex form, including
its divisor, not just its real part.

The selected lower pair is itself symmetric:

\[
\phi_p(t,x,-s,h)=\phi_p(t,x,s,h).
\tag{8}
\]

Here is the required check for that particular selection. In C467p's
physical graph, Q=((I-q)/2-v,(I-q)/2+v,q) and
p=(M0-eta v,M0+eta v,P(q)). The auxiliary cone is invariant under
v -> -v, and p(t,S_+Q)=S_+p(t,Q). Thus
M=Id-iD_Qp transforms to S_+MS_+, its determinant is invariant,
u=-iM^{-1}p_t is equivariant, and
widehat kappa=(F/v^2)det M is invariant, including v=0 by its
explicit smooth factorization. The velocity
b=-Re(widehat kappa u)/Re(widehat kappa) is equivariant. Uniqueness
on the regular backward paths, confined to that invariant cone by
C467p, gives R0(t,S_+Q)=S_+R0(t,Q). Since
G(Q)=prod_k f(Q_k) is permutation-invariant, G(R0) is invariant.
This proves (8) in the interior and then on the closed box by
C467p's continuity.

Exactly the same argument applies to C467x's upper *reference*
chi^0=G(R0), with S_- and singleton slot2. Its physical graph is
the reflected C467p graph, as specified in C467x(4)-(8). This is
also C467w's midpoint-equivariance argument, now used for the
entire invariant cone. Hence the upper reference edge datum g_-
of C467x satisfies

\[
g_-(t,y,1-\lambda)=g_-(t,y,\lambda),
\tag{9}
\]

and the lower edge
g_+(t,y,lambda)=phi_p(t,x(t,y),1-2lambda,0) has the same symmetry.
The actual mean y=E1(t,x)/3 is fixed by both permutations. These statements
hold for an arbitrary allowed asymmetric f.

### The upper pair is unmodified locally at its midpoint

C467x constructs phi_- from (G+D)(R0). In its auxiliary initial
coordinates the correction support, including its closure away
from the diagonal, satisfies C467x(18):

\[
v_0=(Q_{0,3}-Q_{0,1})/2\ge c\ell_0>0,\qquad
\ell_0=\tfrac32\left(\tfrac13\sum Q_{0,k}-Q_{0,2}\right).
\tag{10}
\]

For a fixed original point t>0,h<0,s=0, upper midpoint invariance
gives v0=0 at its backward endpoint, and that endpoint has ell0>0
by C467x's backward confinement. Smooth endpoint dependence and
(10) therefore give an open neighborhood of this point where
D(R0)=0. The same is true after reflecting s. In that neighborhood
phi_- equals the symmetric reference. Thus

\[
\widehat\phi_-(t,x,s,h):=\phi_-(t,x,|s|,h)
\tag{11}
\]

is smooth across s=0 for positive t and negative h: locally it is
just the smooth reference, not a function with an absolute-value
singularity. Away from s=0 it is an original solution or its
reflection. On the closed box (11) is a composition of continuous
maps and has the same initial data, range and endpoint extensions.
At h=0 its midpoint value is unchanged, so C467w's necessary
midpoint trace remains satisfied. No smoothness at t=h=0 is used.

### Both triangle tests have an exactly symmetric central collar

Use C467v/x's coordinates (t,y,u,lambda_j), where u=r sqrt(t).
On either single chart its normalized field is
(Y_j,u C_j,N_j), with

\[
|N_j|\le C\sqrt t,\quad
N_j=-\frac{1-2\lambda_j}{2}
\left[B_p-B_s-
 \frac{W_{\pm,t}+Y_jW_{\pm,y}}{W_\pm}\right].
\tag{12}
\]

The paired-slot symmetry makes Y_j and C_j even in
lambda_j-1/2 and N_j odd. This can be checked in C467v(4)-(8):
w=(1-2lambda_j)W_pm changes sign; the graph values p+iQ are
permuted, so H and its exponential are unchanged; the other
factors in K depend on w^2. Consequently Y,B_p,B_s are even,
and (12) has the asserted parity. The quantities D_pm,W_pm and
the change x(t,y) do not depend on lambda. These are exact
identities of the actual field, not leading-order expansions.

Work first on each of C467x's two transition mean bands, with
its nested larger bands. Reduce the common time so that

\[
\frac{2C}{3}\tau^{3/2}<\frac1{16},\qquad
\delta\tau^{3/2}<\frac18,
\tag{13}
\]

where delta is the fixed collar width in C467x(13). A backward
path from 3/8<lambda_j<5/8 changes its angle by at most
integral_0^t C sqrt(s) ds<1/16 before its outer hit. It therefore
remains in 1/4<lambda_j<3/4; a first-exit argument justifies
using the one-chart bound throughout. It never reaches a radial
seam. The mean and radial confinement are the existing
C467v(15)-(19) estimates, not additional boundary assumptions.

The original C467x solution on this collar is thus the one-chart
transport of its own outer datum. For j=0 that datum is g_+.
For j=1 the outer hit has angle in (1/4,3/4) and time sigma<=t;
by (13) it is outside the support of C467x's correction near
lambda_1=0. Its datum is exactly g_-, not an approximation to it.
The two data are symmetric by (8)-(9).

Reflect a one-chart characteristic by lambda -> 1-lambda.
Equation (12)'s exact equivariance and regular uniqueness identify
it with the characteristic of the reflected terminal point. Its
y,u coordinates are identical. Thus its unique hit on u=sqrt(sigma)
has the same time and mean and the reflected angle. Symmetry of
the datum proves, on this whole central collar for positive t,r,

\[
\psi_j^x(t,x,r,1-\lambda)=\psi_j^x(t,x,r,\lambda)
\quad(j=0,1).
\tag{14}
\]

C467x glues the two mean-band constructions to exact constants 1
and 0 on open overlaps. Those constants obey (14), so the argument
covers every original x, with the same endpoint neighborhoods.
Continuity gives the endpoint versions at r=0,1 and t=0. There is
no requirement that different angles have the same value at r=0.

### Folding the two tests and repeating the two types

Define

\[
\widehat\psi_+(t,x,r,\lambda)
 =\psi_0^x(t,x,r,\max\{\lambda,1-\lambda\}),
\]
\[
\widehat\psi_-(t,x,r,\lambda)
 =\psi_1^x(t,x,r,\min\{\lambda,1-\lambda\}).
\tag{15}
\]

By (14), on an open neighborhood of lambda=1/2 these definitions
are exactly the original smooth tests. On each remaining open
half they are either the original test or its reflection, so (7)
proves their original undivided adjoint equations. They retain
range, initial values, all continuity and endpoint extensions.
No cutoff has been multiplied into an interior transport solution.
Both new tests are symmetric in lambda.

C467x's established seam is retained in the form

\[
\widehat\psi_+(t,x,r,1)=\psi_0^x(t,x,r,1)
 =\psi_1^x(t,x,r,0)=\widehat\psi_-(t,x,r,0).
\tag{16}
\]

Since each hatted test has equal values at its two angular
endpoints, (16) also supplies the opposite seam. At the outer
edge, put s=1-2lambda. C467x(3), (8) and (11) give exactly

\[
\widehat\psi_+(t,x,1,\lambda)
 =\phi_p(t,x,-|s|,0)=\phi_p(t,x,s,0),
\]
\[
\widehat\psi_-(t,x,1,\lambda)
 =\phi_-(t,x,|s|,0)=\widehat\phi_-(t,x,s,0).
\tag{17}
\]

For all j set phi_j=phi_p and psi_j=widehat psi_+ when j is
even; set phi_j=widehat phi_- and psi_j=widehat psi_- when j
is odd. These are scalar tests in the original parameter charts,
not replacements of their physical maps. To check every map and
orientation, let P(z1,z2,z3)=(z3,z1,z2). Then P is even and the
exact C467k maps obey

\[
Z_{2k}=P^k Z_0,\quad Z_{2k+1}=P^k Z_1,\qquad
P_{2k}=P^k P_0,\quad P_{2k+1}=P^k P_1\quad(k=0,1,2).
\tag{18}
\]

For clarity the full pair slot check, in the ordered template
(low paired value, high paired value, singleton), is

| j | slot order | permutation sign | separation |
|---|---|---|---|
| 0 | (1,2,3) | +1 | h>0 |
| 1 | (1,3,2) | -1 | h<0 |
| 2 | (3,1,2) | +1 | h>0 |
| 3 | (2,1,3) | -1 | h<0 |
| 4 | (2,3,1) | +1 | h>0 |
| 5 | (3,2,1) | -1 | h<0 |

P fixes Omega by (5), so the forms and equations for each parity
are exactly the base forms and equations. C467k's triangle
orientations are all dt dx dr dlambda, and its pair orientations
are the signs in this table times dt dx ds dh. Equations (16)-(17)
therefore give all of (4), including j=5 to j=0, with no change of
orientation or same-time spatial return-map assumption.

### All 48 complex derivative products

Write each pair pullback in the original coefficient order

\[
P_j^*\Omega=A\,dx\,ds\,dh+B_c\,dt\,dx\,dh
                 +U\,dt\,ds\,dh+V\,dt\,dx\,ds,
\]

and each triangle pullback as

\[
Z_j^*\Omega=A\,dx\,dr\,d\lambda+B\,dt\,dx\,d\lambda
                 +U\,dt\,dr\,d\lambda+V\,dt\,dx\,dr,
\tag{19}
\]

where juxtaposition of differentials denotes wedge product.
For a pair, (6) implies A,U,V are even in s and B_c is odd.
For a triangle, (7) implies A,U,B are even about lambda=1/2
and V is odd. For example reflection changes the sign of the
three triangle basis forms containing dlambda and preserves
dt dx dr; comparing with iota^*Psi=-Psi gives precisely that
parity. The pair calculation is identical with ds in place of
dlambda and B_c as the coefficient whose form omits it.

Consequently each absolute complex derivative product of a
reflected test equals the corresponding product at the reflected
point: the sign from the angular derivative cancels the odd
coefficient. The parameter reflections have absolute Jacobian 1.
Folding gives an integral at most twice the original integral,
separately for each product. Smoothness at the fold has already
been proved, so no distributional derivative is omitted there.
Even slot permutations preserve all these coefficients exactly.

More explicitly, C467p(37) applies to each even pair:

\[
|A\phi_t|,|U\phi_x|,|V\phi_h|\le C_f s^2\sqrt t,
\qquad |B_c\phi_s|\le C_f|s|^3t.
\tag{20}
\]

C467x(22) and reflection give, for each odd pair,

\[
|A\phi_t|,|U\phi_x|,|V\phi_h|
 \le C_f s^2(\sqrt t+t^{-1}{\bf1}_{|h|\le C\sqrt t}),
\]
\[
|B_c\phi_s|
 \le C_f|s|^3(t+t^{-1/2}{\bf1}_{|h|\le C\sqrt t}).
\tag{21}
\]

The t^(-1) collar integrates in h to O(t^(-1/2)), integrable
at zero; the other terms are integrable as well. For each of the
six triangles put s_j=1-2lambda. C467x(25) gives

\[
|A\psi_t|\le C_f r^5t^{5/2}s_j^2,\quad
|U\psi_x|\le C_f r^5t^3s_j^2,
\]
\[
|B\psi_r|\le C_f r^6t^{5/2}s_j^2,\quad
|V\psi_\lambda|\le C_f r^5t^2s_j^2.
\tag{22}
\]

All four are integrable independently. Equations (20)-(22) are
on the original complex products, before any real part or sum.

### Complete independent-cutoff identities and matching faces

For a pair use [epsilon,T] in time and h in [eta,H_*] for
even j or [-H_*,-eta] for odd j, with the full x,s intervals.
The exact complex Stokes identity, in coordinate orientation
dt dx ds dh, is

\[
\int(A\phi_t-U\phi_x+B_c\phi_s-V\phi_h)
 =\int[\phi A]_{t=\epsilon}^{T}
  +\int[\phi B_c]_{s=-1}^{1}
  -\int[\phi U]_{x=-X}^{X}
  -\int[\phi V]_{h=h_{\rm left}}^{h_{\rm right}}.
\tag{23}
\]

Every face integral retains all the other coordinates of its
cutoff box. Multiply the entire equality by the negative of the
pair orientation sign in (18)'s table for the stipulated common
minus normalization. In particular the upper pair's h=0 face is
the upper h endpoint; it is not assigned the lower pair's sign.

Continuity, range and (20)-(21) meet C467o's entire-face criterion,
with its exact negative-h counterpart already checked in C467x.
Specifically the lower-time face is O(epsilon^(3/2)) uniformly in
eta; x and outer-h faces have a Ct^(3/2) majorant, and s faces
have C sqrt(t). The moving h face coefficient has the original
full tangential L1 limit and majorant Cs^2t^(3/2). Uniform
continuity of the new test on its closed box gives the limit of
its product with that coefficient: the difference is bounded by
the uniform difference of the tests times the coefficient's L1
norm plus the L1 difference of coefficients times the test bound.
Omitting [0,epsilon] from this face costs O(epsilon^(5/2))
uniformly in eta. The fixed upper-time face converges as well.
The bulk products have the fixed integrable majorants (20)-(21).
Thus every term of (23) has its limit for unrelated cutoff rates.

For a triangle use [epsilon,T] and eta<=r<=1-zeta, with full
x,lambda intervals. Its complete complex identity is

\[
\int(A\psi_t-U\psi_x+B\psi_r-V\psi_\lambda)
 =\int[\psi A]_{t=\epsilon}^{T}
  +\int[\psi B]_{r=\eta}^{1-\zeta}
  -\int[\psi U]_{x=-X}^{X}
  -\int[\psi V]_{\lambda=0}^{1}.
\tag{24}
\]

The common minus sign multiplies this whole identity by -1.
Equation (22) justifies all four bulk limits. C467k(19)'s actual
coefficient bounds and |psi|<=1 give lower-time face O(epsilon^4)
and inner radial face O(eta^8 T^4), uniformly in the other
cutoffs. The latter tends to zero. The outer radial face has
majorant Ct^3, x faces Cr^7t^4, angular faces Cr^7t^3, and their
continuous test traces give the full limits. The upper-time face
also converges. No midpoint boundary has been introduced: the
folds are smooth interior tests, and all original coefficients
vanish on the midpoint divisor anyway.

These arguments apply to each piece with its own cutoff parameters.
For any joint sequence all twelve identities converge individually;
there are only finitely many pieces, so their sum has the sum of
these limits. On each outer match C467k's map identification,
ds=-2dlambda, and its opposite induced orientations apply to the
equal scalar tests in (17). On each radial match its maps and
t,x,r derivatives agree, and the angular faces have opposite
induced orientations. Equation (16) and endpoint symmetry give
equal scalar tests on all those faces. Thus all six outer and
six cyclic radial terms cancel after their independent limits.
Every remaining time, x, pair-s endpoint and outer-h term remains
in (23)-(24). This proves only the claimed local component.

### Independent conceptual audit — 16 November 2026, step1078

This RESEARCH / REPRODUCTION conceptual audit uses the unchanged
invocation-start SPECIALIZE assessment
`drafts/literature/2026-11-16-cyclic-midpoint-reflection-audit-nomination-1076.md`,
separately approved by review1077. It checks the particular tests in
the hypotheses, rather than arbitrary tests with the same three traces.
The general ODE, Stokes and dominated-convergence inputs are precisely
the citations above; their source assessments are reused. No new
construction, external theorem or numerical premise is introduced.
The qualified C467k/o/p/v/w/x results are used as local inputs;
the inherited external finite-zero/product inputs are not reaudited.

**Exact reference symmetry and the upper-pair fold.** In (5) the
Vandermonde square and exponential are invariant, whereas the ordered
top differential has the permutation sign. Thus the full complex
form, including its zeros, is anti-invariant under each paired-slot
transposition. The affine formulas for both original connectors and
triangles give (6)–(7) with the indicated transpositions. No parity
of beta or of f is involved.

For the lower reference, exchanging Q1,Q2 fixes I,q and the inverse
initial parameters c,h. Therefore it fixes P,J,eta,M0 in C467p(19)
and changes only v to -v. Its domain |v|<(4/5)ell, |I|<I_m,
0<h<h_m is invariant. Differentiating p(SQ)=Sp(Q) gives
D_Qp(SQ)=S D_Qp(Q) S and p_t(SQ)=Sp_t(Q). Consequently det M
is unchanged and u is equivariant. F/v^2 is unchanged off v=0;
C467p(23)'s explicit smooth factorization extends that equality
through v=0. Its real-part floor makes b an equivariant smooth
field on this same domain. This verifies the actual field and
domain hypotheses for ordinary uniqueness, rather than inferring
symmetry from the initial test alone.

C467p(30a)–(31) confines the original and reflected backward paths
in that domain until time zero. Their separated endpoints lie in a
regular chart, so uniqueness gives R0(t,SQ)=S R0(t,Q). The product
G is invariant under S even when f is asymmetric. This proves (8)
where t,h>0; continuity proves it on the stated closed box. The
upper reference is obtained from this graph by the exact C467x(4)
conjugation/slot change and fsharp(u)=f(-u). In upper Q coordinates
its initial function is again G. The corresponding invariant domain
and argument exchange Q1,Q3, leaving singleton Q2 fixed. They give
the full upper-reference symmetry and (9). In both cases the change
from x to y=E1/3 fixes the reflection parameter and introduces no
additional hypothesis on the mean.

At a positive-time upper midpoint with h<0, equivariance preserves
v=0 on its entire backward path. Its endpoint has ell0>0: C467x(6)
and the reflected C467p confinement exclude backward exit at k=|h|=0
and keep the singleton separated at time zero. In a neighborhood of
this endpoint, ell0 remains bounded below by half its value there.
The closed off-diagonal correction support in C467x(18) satisfies
v0>=c ell0. It is therefore disjoint from a smaller neighborhood
of the midpoint endpoint. Smooth endpoint dependence pulls this
neighborhood back to a neighborhood of the original midpoint.
Both it and its reflection can be used by intersecting the two
neighborhoods. There phi_- equals its symmetric smooth reference
on both sides. Formula (11) thus equals that smooth reference locally.
This proves all orders of smoothness at the fold, not merely equality
of values or first derivatives. The neighborhoods may shrink with
t,h; the conclusion needs local smoothness, not a uniform radius at
the singular corner. Closed-box continuity and the original initial
data follow by composition with |s|. At h=0 the continuous folded
trace is retained; no derivative at t=h=0 is claimed.

**Exact triangle field parity and a common open collar.** In C467v(5),
the paired-slot transposition fixes y,ell and changes w to -w. It
permutes p+iQ exactly. The H term in C467v(7) is therefore invariant;
the remaining w dependence of K is through w^2. The quantities
m,k_p,k_s and v0,v_p,v_s have no w dependence. Hence K,Y,B_p,B_s
are even in w, with the nonzero real-part denominator already
provided by C467v. Since D and W depend only on t,y, C is also
even in lambda-1/2 and N in (12) is odd. This argument applies to
the upper chart although W_- is negative. Its sign does not alter
the exact reflection. It checks the actual fields, not their
small-time leading terms.

Take the maximum of the constants in C467v(11) on the two nested
mean-band constructions. Their finite margins and existing radial
confinement give one horizon. Reduce it further to satisfy (13).
Until a possible first exit from 1/4<lambda<3/4, a path starting
at 3/8<lambda<5/8 moves by at most

    integral_0^t C sqrt(s) ds = (2C/3)t^(3/2) < 1/16.

This is less than the distance 1/8 to either boundary of the larger
collar; thus no such first exit occurs. In particular no radial
seam is reached. For r>0 the outer-hit construction in
C467v(15)–(19) applies, with a unique positive hit time sigma<=t.
The upper hit has lambda>1/4, while C467x(13)'s correction is
supported in |lambda|<delta sigma^(3/2)<1/8. Its value is exactly
g_-, throughout this collar; the lower value is exactly g_+.

Reflecting a path preserves t,y,u and changes lambda to 1-lambda.
The parity just checked and ordinary uniqueness on this single chart
identify the reflected path, without invoking a piecewise-flow
uniqueness theorem at a seam. Both paths have the same outer hit
time and mean, with reflected hit angle. Symmetry of the two
reference data proves (14) on the whole collar, for every positive
t,r. C467x's construction is exactly constant on its central and
outer mean overlaps, so those portions supply the same identity and
smooth joins outside the transition bands. This covers all original
x on the same horizon. Continuity supplies r=0,1 and t=0 values.
No angle-independent physical-vertex value is inferred.

**The folds and all twelve interface matches.** On this open collar
each composition in (15) equals the original smooth triangle test.
On either remaining open half it is the original test or its reflected
solution. Pulling back the original adjoint under (7) multiplies
its form by -1 and therefore preserves its zero equation. Smoothness
on the collar removes any interface distribution at the fold.
The same argument applies to (11). Reflection transports the original
fixed-angular-endpoint extensions; the other fixed endpoints and
range/initial conditions are inherited. In particular phi0 is still
the unmodified phi_p.

Let R denote the even permutation called P in (18), to distinguish
it from the pair maps. Directly from C467k(5), R sends
(V0,V1,V2,V3,V4,V5) to (V2,V3,V4,V5,V0,V1). It fixes the center,
and hence sends each complete triangle map to the one two positions
later. The ordered pair template sends low/high/singleton slots
(1,2,3) to (3,1,2) to (2,3,1), and
(1,3,2) to (2,1,3) to (3,2,1), verifying every row of (18), also
away from h=0. All even rows have sign +1 and h>0; all odd rows
have sign -1 and h<0. R preserves Omega, so copying the scalar
tests preserves each equation without changing the maps.

For even triangles the folded outer datum is phi_p at -|s|,
which equals phi_p at s by (8). For odd triangles it is phi_-
at |s|, precisely (11). At both ends of an even triangle the
folded value is psi0^x at lambda=1; at both ends of an odd one
it is psi1^x at lambda=0. These values are equal by C467x's
accepted seam identity. This verifies all six radial matches,
including the odd j=5 to even j=0 match, as equalities for every
t,x,r, and all six outer matches. It is not a same-time return-map
argument or an added condition on all representatives of r=0.

**Forty-eight separate absolute products.** Comparing the reflected
basis forms in (19) gives pair parities (A,U,V) even, B_c odd,
and triangle parities (A,U,B) even, V odd. For a reflected test,
each non-angular derivative is evaluated at the reflected point;
the angular derivative gains a minus sign, exactly paired with
the odd coefficient. Thus each of the four complex products has
the same absolute value as its original counterpart at that point.
The reflection Jacobian has absolute value one. The folded integral
is at most twice its corresponding original integral, individually.
The fold itself is smooth and has measure zero, so this argument
omits neither a derivative measure nor a nonintegrable jump. Even
slot permutations leave the coefficients unchanged.

For each of the three even pairs, (20) follows from C467p(37).
For each of the three odd pairs, (21) follows from C467x(22):
its potentially largest term integrates in h as

    integral_0^{H_*} t^(-1) 1_{k<=C sqrt(t)} dk <= C t^(-1/2),

where k=|h|, and then in t on [0,tau]. The angular collar term
integrates in k as at most C; the reference terms sqrt(t),t
and all powers of |s| are integrable. For each triangle, multiplication
of the four C467k(19) coefficients by C467x(24)'s derivatives gives,
respectively, r^5t^(5/2)s_j^2, r^5t^3s_j^2,
r^6t^(5/2)s_j^2, r^5t^2s_j^2, exactly (22).
All exponents are integrable separately. There are twelve even-pair,
twelve odd-pair and twenty-four triangle products. No real-part
cancellation is used to count or bound these 48 products.

**Every cutoff face and the signed sum.** Omega is closed on the
whole original polydisc, including the divisor. The audited fold
smoothness and inherited endpoint extensions meet Stokes' hypotheses
on each positive-cutoff box. For ordered coordinates t,x,s,h the
positive face contractions have signs +,-,+,-; their pairings with
(19) give exactly (23). The same calculation in t,x,r,lambda gives
(24). The stipulated domain orientation and common minus sign
multiply the entire pair equality by -epsilon_j and each triangle
equality by -1. In particular the negative-h inner boundary is the
upper endpoint of its h interval; it is not assigned the lower-pair
endpoint sign.

On each pair the lower-time face is O(epsilon^(3/2)) uniformly in
eta. Fixed x and outer-h faces use Ct^(3/2), and s faces use
C sqrt(t). The fixed upper-time face is bounded and converges as
eta decreases. For the moving h face, C467o's full tangential L1
coefficient limit, or its exact C467x negative-h counterpart, gives
V_eta -> V0 on [0,T] times the two fixed intervals. The new tests
are uniformly continuous on their own closed boxes. Consequently

    ||phi_eta V_eta-phi0 V0||_1
      <= ||phi_eta-phi0||_infinity ||V_eta||_1
         + ||phi0||_infinity ||V_eta-V0||_1 -> 0.

The uniform Cs^2t^(3/2) majorant makes the removal of [0,epsilon]
cost O(epsilon^(5/2)), independently of eta. This verifies the
moving face itself, not only the bulk or a fixed positive-time trace.
The four fixed bulk majorants already checked give every bulk limit
by componentwise DCT along arbitrary joint cutoff sequences.

For each triangle, the lower-time face is O(epsilon^4), uniformly
in both radial cutoffs; the inner radial face has absolute integral
O(eta^8 T^4), uniformly in epsilon and the outer cutoff. The outer
radial face has continuous limiting test and coefficient at r=1,
with Ct^3 majorant; its omitted time mass is O(epsilon^4), uniformly
in the outer cutoff. The x faces have Cr^7t^4 and the angular faces
Cr^7t^3 majorants. Both radial cutoff indicators converge almost
everywhere on those faces; continuity and DCT give their complete
limits. The fixed upper-time face is bounded on its compact spatial
box and converges as both radial cutoffs vanish. Thus every term of
(24), not just the zero inner face, has the asserted independent limit.

Only now sum the twelve identities. Finitely many individual limits
permit unrelated cutoffs on all pieces. C467k's actual matching maps
and their tangential columns identify the limiting outer forms after
ds=-2 dlambda. For even pairs the h=0 face has orientation
+dt dx ds, and for odd pairs -epsilon_j dt dx ds is also
+dt dx ds; both become negative in t,x,lambda. Each triangle's
r=1 orientation is positive. For radial faces, lambda=1 has
-dt dx dr and the neighboring lambda=0 has +dt dx dr on the
same map. The common minus normalization preserves these opposite
signs. The already checked scalar equalities therefore cancel exactly
the six outer and six radial pairs of terms, including j=5,0.
All time, x, pair-s and outer-h terms are retained. Their signs,
vanishing or payment beyond the stated limits are not asserted.

Verdict: the original C467y construction passes this conceptual audit
on one existential common positive horizon. Its local result is now
an audited input, not a new theorem imported from the literature or
a claim of originality beyond the checked sources. Stops1043/1058/
1060/1068 retain their original scopes. Chamber endpoint matching,
exterior payment, realization, higher degrees and actual-Xi positivity
remain unpaid. No complete RH candidate follows.

## Mathlib

Full matching Mathlib coverage for this actual singular cyclic
selection has not been checked. The precise ODE, Stokes and dominated-
convergence citations above are supporting mathematical inputs;
they do not formalize the midpoint folds, the qualified actual
background or the twelve-piece construction. No absence or machine-
checked claim is made. Audit1078 validates the local construction
under its retained input qualifications; it does not provide a
formalization or replay the external finite-zero/product inputs.
