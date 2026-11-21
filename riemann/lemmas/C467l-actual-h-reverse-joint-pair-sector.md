# C467l — A uniform actual straight-pair sector at the joint corner

## Hypotheses

Use C467e/audit1017's actual analytic background and regular coefficient
flow, with the qualifications inherited from C466z/audit988 and
C466/audit993. In particular,

\[
n=3,\quad R=1/4,\quad a=1/16,\quad T_0=1/1920,\quad
\beta(z)=B(1+z)-B(1)-B'(1)z,
\]
\[
g=\beta',\quad H_0=3[B(1)-B'(1)]\in\mathbb R,\quad
H(z)=H_0+\sum_j\beta(z_j),\quad
F(z)=\Delta(z)^2e^{-H(z)},\quad
\Delta(z)=\prod_{j<k}(z_k-z_j).
\tag{1}
\]

Here exp B(w)=xi(1/2+sqrt(w))/xi(1/2), with its stated conjugation
normalization, beta(0)=beta'(0)=0, and |beta''|<40 on |z|<R.
Consequently |beta(z)|<=20|z|^2. For distinct real initial u in
(-a,a)^3 the actual reversed flow, in physical time, is

\[
Y_j'=2\sum_{k\ne j}\frac{Y_j-Y_k}{|Y_j-Y_k|^2}
                 -\overline{g(Y_j)},\qquad Y(0,u)=iu.
\tag{2}
\]

Take the exact parameter domain

\[
|x|\le1/256,\quad 0<|h|\le1/128,\quad y=x+h,\quad |s|\le1.
\tag{3}
\]

The trace Y^+(t,x,y) is to be the limit from initial data
(x-delta/2,x+delta/2,y), delta>0. Its existence on a common time
domain is a conclusion, not a hypothesis. Paired slots 1,2 have
increasing imaginary coordinates; slot 3 is the singleton, above
the pair for h>0 and below it for h<0. Put

\[
m=(Y^+_1+Y^+_2)/2,\quad d=(Y^+_2-Y^+_1)/2,\quad w=Y^+_3,
\quad \mathcal Z=(m-sd,m+sd,w).
\tag{4}
\]

Use C467j/audit1029 and C467k/audit1033's chamber-induced orientation
dt wedge dx wedge ds wedge dy, including both signs of h, and the
common minus normalization

\[
\mathcal C=-F(\mathcal Z)
 \det_{\mathbb C}(\mathcal Z_x/i,\mathcal Z_s/i,\mathcal Z_y/i).
\tag{5}
\]

Other placements of the paired slots carry both the target permutation
and its induced parameter orientation. No divided weight, modulus
square, modified flow or reparameterized time is used. C466a's external
qualifications remain if a reciprocal-density interpretation is sought.
No density realization, global cycle, all-degree positivity or Xi
transfer is assumed.

## Conclusion

There is one 0<tau<=T_0 for which every trace in (3) exists and is
smooth in (t,x,y) on its positive-time parameter domain, with the
specified ordering. The entire connector lies in |z_j|<R and satisfies

\[
\operatorname{Re}\mathcal C\ge\tfrac12|\mathcal C|
\quad (0<t\le\tau)
\tag{6}
\]

uniformly over (3). Its only zeros on that domain are s=0. A
representative phase of each nonzero coefficient has modulus <1/2.
There is no restriction on |h|/sqrt(t), and tau is existential.

This additional local input is validated by independent conceptual
audit1037 below. It extends the sector and actual-domain conclusions of the
separated pair construction; it does not extend its spacetime estimates
or prove a joint integrable boundary identity. Lateral/outer payment,
global assembly, other degrees and Xi transfer remain open. It neither
removes C467i's uncorrected collision defect nor contradicts stops1009
or1023.

## Proof

### Source coverage and the necessary new estimate

The invocation-start EXPLORE assessment is
`drafts/literature/2026-11-16-reverse-pair-joint-sector-nomination-1033.md`,
completed by separate review1034. Its exact target is (3),(6).
The comparison found no matching theorem in the sources checked;
this is not a claim of originality. Root regularity by itself does
not supply the weighted sector. C467j's separated floor and C467k's
compact-positive-time incident charts do not cover the joint corner.
The new work is a uniform actual-root gap estimate and an exact
separation factor in the complete connector Jacobian.

Use the regular flow and reconstruction already proved in C467e.
The standard smooth-dependence/continuation tools are Teschl,
*Ordinary Differential Equations and Dynamical Systems*, April2012
preliminary version,
[Lemma2.14/Corollary2.15, pp52–53; Theorem3.9, p81; Theorem6.1,
pp189–190](https://www.mat.univie.ac.at/~gerald/ftp/book-ode/ode.pdf),
as assessed in reviews1024/1032/1034. They apply on C467e's regular
coefficient domain. The ordinary real simple-root implicit function
theorem is applied only after positive root separation has been proved.
Neither theorem is reproved. No hyperbolicity on an open neighborhood
of the time-zero coefficient discriminant is assumed. No Stokes or
integrable-limit theorem is used in this result.

### Uniform real-root separation and identification of the actual traces

Write e(q)=(sum q_j,sum_(j<k)q_j q_k,q_1q_2q_3). On a fixed
neighborhood of the compact initial coefficient set, C467e supplies
the smooth real solution (E_t(e^0),Pi_t(e^0)), with E_0=e^0, Pi_0=0,
and polynomial reconstruction

\[
Q_t(v)=v^3-E_1v^2+E_2v-E_3,\qquad
P_t(v)=\Pi_1+(E_1-v)\Pi_2+(v^2-E_1v+E_2)\Pi_3.
\tag{7}
\]

There is a common time tau_0>0, at most T_0, on which all these
coefficient trajectories stay in the regular domain with
max |Pi_b|<1/256. For distinct initial u, C467e identifies them
with the actual flow Y=p+iq, preserving imaginary order, with
p_j=P_t(q_j) and

\[
\sum_j|Y_j|^2<r_*^2:=3/160,\qquad
\frac{p_j-p_k}{q_j-q_k}=-\Pi_2-q_l\Pi_3\quad(l\ne j,k).
\tag{8}
\]

In particular |q_l|<r_*<1/4. Every secant in (8) has absolute
value less than kappa=5/1024. For distinct data, put
c_jk=(1+[(p_j-p_k)/(q_j-q_k)]^2)^(-1). Taking imaginary parts
in (2) gives exactly

\[
q_j'=2\sum_{k\ne j}\frac{c_{jk}}{q_j-q_k}+b_j,
\qquad b_j=\operatorname{Im}g(Y_j),\qquad
\frac1{1+\kappa^2}\le c_{jk}\le1.
\tag{9}
\]

The original analytic disk is convex, so its |g'|<40 bound implies
|b_j-b_k|<=40|Y_j-Y_k|<41|q_j-q_k|. The last strict comparison
follows from kappa<1/8 and 40sqrt(1+1/64)=5sqrt(65)<41.

Order the imaginary roots r_1<r_2<r_3, regardless of their labels,
and set A=r_2-r_1, B=r_3-r_2, mu=min(A,B). When A<=B, (9) gives

\[
A'=\frac{4c_{12}}A-\frac{2c_{23}}B
           +\frac{2c_{13}}{A+B}+b_2-b_1
\ge\frac{4/(1+\kappa^2)-2}{A}-41A
\ge\frac1A-41A.
\tag{10}
\]

The same estimate holds for B' when B<=A. Here c_{12}, etc. in
(10) denote the corresponding ordered-root pairs, and
1/(1+kappa^2)>3/4. Both estimates hold at a tie. The positive
function mu is locally Lipschitz for each distinct-data solution;
at almost every point its derivative is the derivative of a minimizing
gap, so (mu^2)'>=2-82mu^2. Multiplication by exp(82t) and integration
give

\[
\mu(t)^2\ge e^{-82t}\mu(0)^2+\frac{1-e^{-82t}}{41}\ge t
\quad(0<t\le\tau_0).
\tag{11}
\]

For the last inequality, 82t<=82/1920<1, and
1-exp(-z)>=z-z^2/2>=z/2 for 0<=z<=1. Thus (11) is uniform
even when the initial minimum gap tends to zero. It has been proved
only on actual distinct-data flows, not by evaluating (2) on a divisor.

Now fix t>0 and any initial repeated triple (x,x,y) in the closure
of (3), also allowing h=0 temporarily. Approximate by distinct data
inside (-a,a)^3. The regular coefficient solutions converge by smooth
dependence. Their ordered real roots are bounded by (8), and their
adjacent gaps are at least sqrt(t) by (11). Any convergent subsequence
therefore gives three distinct real roots of the limiting monic cubic,
in that order. A monic cubic has only this ordered list of three roots,
so every subsequence has the same limit. Reconstruction by (7) gives
the actual complex boundary trace and

\[
r_2-r_1\ge\sqrt t,\qquad r_3-r_2\ge\sqrt t,\qquad
\sum_j|Y_j^+|^2\le r_*^2.
\tag{12}
\]

At each positive-time parameter point the real simple-root theorem
gives smooth root branches in time and initial coefficients. This
also proves convergence of the derivatives in local positive-time
charts. These charts define one consistent ordered family on the
whole domain, since the order uniquely specifies every branch.
For h>0, first take 0<delta<2h: the paired slots approach r_1,r_2
and the singleton r_3. For h<0, take 0<delta<2|h|: the paired
slots approach r_2,r_3 and the singleton r_1. This identifies the
actual delta>0 traces on both sides, with one common time tau_0.
No uniform positive lower bound on delta/|h| is required.

Let q denote the imaginary singleton root. Smoothness of E_t on
the compact initial set gives a finite constant K_1 such that

\[
|E_1(t,e(x,x,y))-(3x+h)|\le K_1t.
\tag{13}
\]

The largest root exceeds the mean E_1/3 by at least sqrt(t),
and the smallest lies below it by at least sqrt(t), by (12).
Decrease tau_0 to tau_1>0 so K_1 sqrt(t)/3<=1/2 throughout.
Consequently

\[
\operatorname{sgn}(q-x)=\operatorname{sgn}h,\qquad
|q-x|\ge |h|/3+\sqrt t/2\quad(0<t\le\tau_1).
\tag{14}
\]

This estimates the actual root, with the actual background included
in the finite center-drift bound. It covers every separation/time ratio.

### The exact separation factor in the spatial Jacobian

All derivatives in this section are at fixed physical time. Define
the smooth symmetric complex sum, as a function of initial coefficients,

\[
S(t,e^0)=3\Pi_1+2E_1\Pi_2+E_2\Pi_3+iE_1.
\tag{15}
\]

Newton's identity sum q_j^2=E_1^2-2E_2 in (7) shows that
S=sum Y_j^+. Hence m=(S-w)/2 and, writing J=m_xw_y-m_yw_x,

\[
J=\tfrac12(S_xw_y-S_yw_x).
\tag{16}
\]

For e^0=e(x,x,y), let A=partial_x e^0 and B=partial_y e^0,
where x,y are independent. Explicitly,

\[
A=(2,2x+2y,2xy),\quad B=(1,2x,x^2),\quad
V=(0,1,x),\quad A-2B=2hV.
\tag{17}
\]

Subscripts B,V below mean directional derivatives in initial
coefficient space, evaluated at e^0, holding those direction vectors
fixed for that derivative. The chain rule in (16) therefore gives
the exact identity J=h(S_V w_B-S_B w_V).

Put L(q)=(q^2,-q,1), D= D_(e^0)E_t, and let P_U(q) denote
the derivative of P_t(v) in the initial direction U while holding
v=q fixed. Implicit differentiation of Q_t(q)=0 at its simple
extreme root gives, for U=B,V,

\[
q_U=\frac{L(q)DU}{Q_t'(q)},\qquad
w_U=P_U(q)+(\partial_vP_t(q)+i)\frac{L(q)DU}{Q_t'(q)}.
\tag{18}
\]

The denominator Q_t'(q) is strictly positive for either extreme
root: it is the product of its two differences from the other roots.
Thus

\[
J=\frac{hN(t,x,h,q)}{Q_t'(q)},
\tag{19}
\]
\[
\begin{split}
N={}&S_V\{Q_t'(q)P_B(q)+(\partial_vP_t(q)+i)L(q)DB\}\\
 &-S_B\{Q_t'(q)P_V(q)+(\partial_vP_t(q)+i)L(q)DV\}.
\end{split}
\tag{20}
\]

Regard q in (20) temporarily as an independent real variable in
[-r_*,r_*]. This expression is smooth on a compact box including
t=0 and h=0; it involves no root derivative or inverse discriminant.
At t=0, Pi=0 identically as a function of e^0, D=I, S=i e_1^0,
P_U=partial_v P=0, S_V=0 and S_B=i. Therefore, for every such q,

\[
N(0,x,h,q)=-i\,iL(q)V=x-q.
\tag{21}
\]

Bound the continuous t derivative of (20) on a slightly smaller
compact time box. Taylor's integral remainder gives a finite constant
K_2, independent of x,h,q, with |N-(x-q)|<=K_2t. Inserting the
actual root and (14) yields

\[
\left|\frac{N}{x-q}-1\right|\le2K_2\sqrt t.
\tag{22}
\]

Choose one tau<=tau_1, positive, so 2K_2 sqrt(t)<=1/16 on
(0,tau]. Equations (14),(19) then give the exact factorization

\[
J=-J_*(1+\varepsilon),\qquad
J_*:=\frac{h(q-x)}{Q_t'(q)}>0,\qquad |\varepsilon|\le1/16.
\tag{23}
\]

The smallness is relative to the extracted nonzero real factor, not
to a separated lower floor. In particular no O(t)/|h| loss occurs.

### Original weight, all zeros and the induced orientation

Use paired labels q_1<q_2 and singleton q_3=q, with actual real
parts p_j=P_t(q_j). These labels need not be increasing as a triple.
Set D_0=(q_2-q_1)/2>0. The exact secants (8) imply

\[
d=iD_0(1-i\eta_0),\qquad |\eta_0|\le\kappa,
\tag{24}
\]

with eta_0 real. Write G_1=w-(m-sd), G_2=w-(m+sd), and let
A_1,A_2 be their imaginary parts. Since each segment point is a
convex combination of Y_1^+,Y_2^+, and q is outside their imaginary
interval, A_1,A_2 have the sign of h and |A_j|>=sqrt(t). Moreover
each G_j is the same nonnegative convex combination of the two
singleton-to-pair gaps. Their imaginary parts have the same sign,
so division by A_j expresses the real-to-imaginary slope as a
convex average of the secants in (8). Consequently

\[
G_j=iA_j(1-i\eta_j),\qquad \eta_j\in\mathbb R,
\quad |\eta_j|\le\kappa\quad(j=1,2).
\tag{25}
\]

The argument applies also at s=+-1 and on h<0; there is no
subtraction of oppositely signed imaginary gaps.

C467j's identities are algebraic identities for the smooth map (4),
so require no separated-patch estimate:

\[
\Delta(\mathcal Z)=2sdG_1G_2,\quad
\det_{\mathbb C}(\mathcal Z_x/i,\mathcal Z_s/i,\mathcal Z_y/i)
=2idJ,\quad
\mathcal C=-8is^2d^3G_1^2G_2^2e^{-H(\mathcal Z)}J.
\tag{26}
\]

Substituting (23)–(25), with every sign retained, gives

\[
\mathcal C=\mathcal A\, e^{-\sum_j\beta(\mathcal Z_j)}
(1-i\eta_0)^3(1-i\eta_1)^2(1-i\eta_2)^2(1+\varepsilon),
\tag{27}
\]
\[
\mathcal A=8s^2D_0^3A_1^2A_2^2J_*e^{-H_0}\ge0.
\tag{28}
\]

Here A is positive exactly when s!=0. In particular the original
coefficient vanishes exactly at s=0, and (27) treats that zero
without assigning it an argument or dividing the current by its weight.

The parallelogram identity and (12) give

\[
\sum_j|\mathcal Z_j|^2
=2|m|^2+2s^2|d|^2+|w|^2
\le\sum_j|Y_j^+|^2\le3/160<R^2.
\tag{29}
\]

Thus the original analytic polydisc contains the entire connector,
and |sum beta(Z_j)|<=20(3/160)=3/8. For s!=0 take the arguments
of the explicitly nonvanishing factors in (27). Since Re(1+epsilon)
>=15/16 and |Im epsilon|<=1/16, its argument has modulus at most
arctan(1/15)<1/15. Also |arg(1-i eta_j)|<=|eta_j|. A representative
theta of the full coefficient's phase therefore satisfies

\[
|\theta|<\frac38+7\frac5{1024}+\frac1{15}
=\frac{7309}{15360}<\frac12.
\tag{30}
\]

In particular cos(theta)>=1-theta^2/2>7/8>1/2, proving (6)
at nonzero coefficients; at s=0 both sides of (6) are zero.

Finally, (17),(26) were computed in the original x,s,y order.
The change y=x+h has positive determinant and introduces no reversal
on either separation side. C467j's chamber-face cancellation forces
the positive dt dx ds dy connector orientation; C467k's six-face
orientation check explicitly retains that orientation for h<0 as
well as h>0. For another pair placement a target permutation multiplies
the top form by its sign, since F is symmetric; the induced parameter
orientation carries the same sign. Their product is unchanged. Thus
(27) concerns the chamber-induced coefficient, not a connector whose
sign has been chosen to make it positive.

All reductions of time above are minima of finitely many positive
times obtained on fixed compact sets. They give one tau for (3),
including arbitrarily small nonzero h and both signs, with the actual
background and physical time. No assertion about the pair family's
physical-time integrability, its joint boundary limit, or global
positivity follows merely from this sector estimate.

### Independent conceptual audit — 16 November 2026, step1037

The invocation-start SPECIALIZE assessment is
`drafts/literature/2026-11-16-reverse-joint-pair-sector-audit-nomination-1035.md`,
separately approved in review1036. This is a REPRODUCTION audit of
(3)–(6), retaining the actual background, raw physical time and every
qualification in the hypotheses. The ready source comparison and its
recorded discovery are reused; no new source search, construction or
claim of originality is made. The separated floor in C467j and the
positive-time charts in C467k do not establish the claim being audited.

**Common regular domain and differentiated coefficients.** C467e(18)–(22)
and audit1017 provide a smooth real vector field on an open neighborhood
of the closed initial coefficient box, including its discriminant.
For (3), |y|<=3/256<a, so e(x,x,y), including h=0, lies strictly
inside this box. A fixed slightly larger compact neighborhood also
contains all sufficiently close distinct approximations. The cited
Teschl smooth-dependence and compact-continuation theorems therefore
give a common time on this neighborhood and uniform bounds for each
of the finitely many coefficient derivatives used below. The field
is analytic there, so the time derivatives of its first initial-data
derivatives exist and are continuous as well. This is stronger than
merely asserting C^1 convergence, and follows from the same smooth
flow theorem with its smooth-field hypothesis checked. It requires
no hyperbolicity off the initial real-root locus.

For distinct data, C467e's continuation argument identifies this
coefficient solution with the physical flow on the entire common
interval, with unchanged imaginary ordering. Its radial bound gives
|q_l|<sqrt(3/160)<1/4. Thus its exact secant identity bounds every
real-to-imaginary gap ratio by (1+1/4)/256=5/1024. The imaginary
part of -conjugate(g(Y_j)) is +Im g(Y_j), which verifies the sign
of b_j in (9). The segment joining two Y_j stays in the analytic
disk, so |b_j-b_k|<=40|Y_j-Y_k|<41|q_j-q_k|. All these estimates
precede the limiting argument at repeated initial data.

**Minimum gap, switches and the repeated-root limit.** For ordered
roots, direct subtraction of (9) gives

\[
 (r_2-r_1)'=4c_{12}/A-2c_{23}/B+2c_{13}/(A+B)+b_2-b_1.
\]

When A<=B, the negative term is at least -2/A, the third term
is positive, and 4/(1+kappa^2)-2>1. This proves (10). When
B<=A, subtraction instead gives

\[
 (r_3-r_2)'=4c_{23}/B-2c_{12}/A+2c_{13}/(A+B)+b_3-b_2,
\]

which proves the identical bound for B. At A=B both inequalities
hold. On each distinct-data trajectory A,B are smooth and positive
up to the common time. Their minimum is Lipschitz on each closed
time interval; at almost every differentiability point its derivative
is an active gap derivative. Hence the asserted differential inequality
for mu^2 holds almost everywhere, and the integrating-factor argument
applies without a missing switching contribution. Since 82t<1,
(1-exp(-82t))/41>=t. The resulting lower bound is independent
of the initial minimum gap.

Fix any positive t and repeated initial coefficients in the closed
parameter family. Distinct approximations have real ordered roots
in a fixed compact interval, with both gaps at least sqrt(t).
Coefficient convergence forces every subsequential limit to be a
triple of distinct real roots of the same limiting cubic. The ordered
triple is unique, so this is full convergence, not an unchosen branch
or a subsequence-dependent construction. Reconstruction by (7) passes
to the limit and proves (12). The simple-root implicit function theorem
now applies at each positive-time point; on its neighborhood the
same polynomial roots and their parameter derivatives converge.
The order identifies these local charts on intersections. This proves
smoothness and the required trace identification on one common time
interval, without any uniform positive lower time cutoff. For h>0
the singleton is r_3; for h<0 it is r_1. Choosing delta<2|h|
before its limit gives exactly the labels asserted in (4).

The extreme roots satisfy
r_3-E_1/3=(A+2B)/3>=sqrt(t) and
E_1/3-r_1=(2A+B)/3>=sqrt(t). At time zero E_1=3x+h.
The uniform coefficient derivative bound gives (13); shrinking time
so K_1 t/3<=sqrt(t)/2 proves, respectively,

\[
 q-x\ge h/3+\sqrt t/2\quad(h>0),\qquad
 q-x\le h/3-\sqrt t/2\quad(h<0).
\]

These inequalities verify both the sign and the lower bound in (14).
They impose no relation between |h| and sqrt(t).

**Exact Jacobian factor and relative error.** Summing (7) gives
sum P_t(q_j)=3Pi_1+2E_1Pi_2+E_2Pi_3, verifying (15).
At fixed time and independent x,y, the coefficient directions are
A=(2,2x+2y,2xy), B=(1,2x,x^2), and A-2B=2h(0,1,x).
Substitution into (16) cancels both terms containing S_B w_B and
gives exactly J=h(S_V w_B-S_B w_V). No derivative of the vectors
B,V is taken in this first chain-rule identity.

Differentiating the cubic equation gives (18), with numerator
(q^2,-q,1)DU and the displayed positive sign. For the largest root
both factors of Q'(q) are positive; for the smallest both are
negative. Their product is positive in either case. Substitution
of (18) proves (19)–(20), with no omitted derivative of P_t: P_U
holds its polynomial argument fixed, and partial_v P supplies the
root-derivative term separately.

For the error estimate, q must remain an independent variable in
[-r_*,r_*] while differentiating (20) in time. On this compact
product Q'(q), P_U, partial_v P, S_U and DU are smooth and bounded
with their needed time derivatives. There is no division by Q' in
N. At zero momentum and zero time P_U=partial_v P=0, D=I,
S_V=0 and S_B=i. Consequently

\[
 N(0,x,h,q)=-i\,i\,(q^2,-q,1)(0,1,x)^T=x-q.
\]

Integration of the bounded partial_t N at fixed x,h,q gives
|N-(x-q)|<=K_2t uniformly, including h=0. Only afterwards is
the actual root inserted. By (14) the relative error is at most
2K_2 sqrt(t), as claimed. Thus a single positive time makes it
at most 1/16, and h(q-x)/Q'(q)>0 for either h sign. This validates
(23) even though J_* may approach zero. No absolute perturbation
of a vanishing separated floor is used.

**Original coefficient, zero set and orientations.** The imaginary
half-gap D_0 is positive. Each singleton-to-segment gap is a convex
combination of its two singleton-to-pair gaps. Their imaginary parts
have the same sign and magnitude at least sqrt(t), including the
endpoints s=+-1. The slope of that combination is a convex average
of the two real secants: after dividing by the imaginary sum its
two weights are nonnegative and add to one, also when both imaginary
parts are negative. This proves (24)–(25) on h<0 as well as h>0.

For an independent determinant check, add and subtract the first two
target rows of the spatial derivative matrix. The undivided determinant
is 2d(m_x w_y-m_y w_x). Dividing all three columns by i multiplies
it by i, so it is 2idJ. Together with the three exact Vandermonde
gaps this gives (26). Substituting d=iD_0(1-i eta_0), both
G_j=iA_j(1-i eta_j), and J=-J_*(1+epsilon), the constant sign
is positive: (-8i)i^3 i^4(-1)=8. Thus (27)–(28) retain the
original algebraic square and common minus sign. D_0, |A_1|,
|A_2| and J_* are nonzero, the exponential never vanishes, and
|epsilon|<=1/16. Therefore the only zeros are exactly s=0;
no argument is assigned to those zero coefficients.

The parallelogram identity verifies (29), including |s|=1. Its
bound is strictly below R^2, and the beta bound gives at most 3/8
for the modulus of its sum. The remaining phase bounds total
7kappa+arctan(1/15), strictly below 35/1024+1/15. Hence the
exact rational bound in (30) is 7309/15360<1/2. The cosine
estimate proves the required sector at nonzeros; at s=0 both
sides vanish. No limiting nonzero argument at s=0 is required.

The initial coordinate change (x,delta,y) to
(x-delta/2,x+delta/2,y) has determinant +1 for either sign
of h. In the chamber orientation dt dx ddelta dy, the lower
delta face has sign minus and the upper face plus. In the connector
orientation dt dx ds dy, the s=1 face has sign plus and s=-1
minus. The equal endpoint maps therefore cancel with exactly the
orientation used in (5). Changing y to x+h has determinant +1
on both components. For any other paired-slot placement, the target
permutation multiplies the pulled-back form by its parity and the
induced domain orientation has the same parity, as checked in
C467k/audit1033. The evaluated coefficient is unchanged. This
verifies the sector with the forced orientations rather than selecting
a favorable sign for an individual piece.

**Verdict and limits.** All local conclusions pass with unchanged
hypotheses and constants. The common time is the minimum of finitely
many positive compact-flow and error-control times; no effective
lower bound for it is established. The audit validates C467l as a
local pair/triple compatibility input by reproducing the saved proof;
it makes no new originality claim. The proof does not bound
all mixed physical-time minors or justify the joint integrable limit
at h=t=0. Lateral/outer payment, signed global assembly, all degrees
and Xi transfer remain open; stops1009/1023 remain intact. No
mathematical script, numerical preview or certificate was needed.

## Mathlib

Full matching coverage of this actual weighted pair-family result is
not checked, and is not asserted absent. The smooth ODE and simple-root
tools used here are supported by the cited standard sources; no
matching Mathlib declaration was identified or required in this step.
The proof is analytic and algebraic, with no numerical certificate or
unverified preview used as evidence. Independent conceptual audit1037
above checks (10)–(14), the factored derivative (19)–(23), and the
full oriented coefficient (27) with unchanged hypotheses. This is an
informal audit, not a Lean verification or a claim of new Mathlib coverage.
