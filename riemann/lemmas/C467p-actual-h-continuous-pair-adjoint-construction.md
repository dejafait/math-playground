# C467p — A continuous actual pair adjoint from backward physical characteristics

## Hypotheses

Retain C467e/audit1017, C467l/audit1037, C467m/audit1041 and
C467o's actual positive-h pair and coefficient reconstruction. The
last input is validated by its independent audit1049. In particular,

\[
n=3,\quad R=1/4,\quad a=1/16,\quad T_0=1/1920,\qquad
X=1/256,\quad H_*=1/128,\quad b_*=1/4096,
\]
\[
\beta(z)=B(1+z)-B(1)-B'(1)z,\quad g=\beta',\quad
H=H_0+\sum_j\beta(z_j),\quad H_0=3[B(1)-B'(1)]\in\mathbb R,
\]
\[
F=\Delta^2e^{-H},\qquad \Omega=F\bigwedge_{j=1}^3(dz_j/i).
\tag{1}
\]

Here exp B(w)=xi(1/2+sqrt(w))/xi(1/2), with the inherited
conjugation normalization, beta(0)=beta'(0)=0 and |beta''|<40
on |z|<R. All qualifications of C466z/audit988, C466/audit993
and C466a are retained. No density realization or RH is assumed.

Let f be any fixed smooth real function with 0<=f<=1, f=1 on
[-b_*,b_*] and support in (-2b_*,2b_*). Use the original ordered
positive-h trace from (x,x,x+h), its connector

\[
Y_j=P(q_j)+iq_j,\quad q_1<q_2<q_3,\quad
Z=(m-sd,m+sd,w),\quad
m=(Y_1+Y_2)/2,\ d=(Y_2-Y_1)/2,\ w=Y_3,
\tag{2}
\]

and the raw time t. Write its original pullback as

\[
\Psi=A\,dx\wedge ds\wedge dh+B_c\,dt\wedge dx\wedge dh
       +U\,dt\wedge ds\wedge dh+V\,dt\wedge dx\wedge ds.
\tag{3}
\]

The orientation is dt dx ds dh; the common minus normalization
applies to the whole form. No face matching or exterior condition
is imposed in this pair-only statement.

## Conclusion

For one common existential tau>0 there is a real phi, 0<=phi<=1,
continuous on

\[
K=[0,\tau]\times[-X,X]\times[-1,1]\times[0,H_*],
\]

smooth locally in the physical variables for t,h>0, with neighborhood
extensions at the fixed x,s endpoints, such that

\[
\phi(0,x,s,h)=f(x)^2f(x+h),\qquad
d\phi\wedge\operatorname{Re}(-\Psi)=0\quad(t,h>0),
\tag{4}
\]
\[
\int_K\bigl(|A\phi_t|+|U\phi_x|+|B_c\phi_s|+|V\phi_h|\bigr)
       <\infty.
\tag{5}
\]

The absolute values in (5) are of the complex products separately.
At s=0 the original coefficients remain zero. The complete
positive-h C467m(18) identity has its limit for arbitrary relative
rates of the two cutoffs: all exterior and s faces are retained,
the inner face is the actual one-sided trace, the lower-time term
is zero, and there is no extra corner term. This last assertion
uses the conditional cutoff result C467o.

This construction is the result of attempt1048 and is validated by the
independent conceptual audit1049 below. It resolves nomination1045's local test,
not a complete RH candidate or a claim of originality. No joint smooth
time-zero jet is asserted; C467n's smooth-class obstruction remains.
Triangle matching, exterior flux payment, global assembly, realization,
other degrees and actual-Xi positivity remain unproved.

## Proof

### Coverage, imported tools and the auxiliary extension

Reuse the unchanged EXPLORE assessment
`drafts/literature/2026-11-16-reverse-continuous-pair-adjoint-nomination-1045.md`,
separately reviewed at1046. No matching theorem was identified there.
The new work below is the actual-coordinate cancellation, common
backward domain and derivative estimate, not a reproof of a general
transport theorem. The classical smooth ODE existence, smooth
dependence, variational and compact-continuation tools are the imports
already used in C467e: Gerald Teschl, *Ordinary Differential Equations
and Dynamical Systems*, author-hosted April2012 preliminary version,
[Lemma2.14/Corollary2.15, pp52–53; Theorem3.9, p81; Theorem6.1 and
proof, pp189–190](https://www.mat.univie.ac.at/~gerald/ftp/book-ode/ode.pdf).
Apply these only on smooth open sets with h>0. Passage to h=0 is
proved by the estimates below, not by an ODE theorem at the divisor.
The elementary Gronwall bound used for the variational equation is
the usual scalar integral inequality. The cutoff passage imports the
precise Stokes and dominated-convergence theorems cited in C467o;
their hypotheses are verified by (4)–(5) and continuity below.

The coordinate domain used to construct a function is slightly larger
than the original pair. This is necessary because its s faces have
no prescribed data. The algebraic graph formula is extended to that
domain and then restricted back. The original flow, Z, weight, raw
time and every coefficient in (3) are unchanged on K.

All constants C below are finite and depend only on this fixed compact
analytic setup (and, when indicated, on f). They can increase between
inequalities. All reductions of tau are finite positive reductions.
We use lambda=h+sqrt(t); estimates containing it are stated for t+h>0.

### An enlarged regular coefficient domain and its gap estimates

Put c=x+h/3 and take auxiliary initial parameters

\[
|c|<c_m=1/64,\qquad 0\le h<h_m=1/64,
\]
\[
e^0(c,h)=(3c,\ 3c^2-h^2/3,\ c^3-c h^2/3+2h^3/27).
\tag{6}
\]

The initial roots are (c-h/3,c-h/3,c+2h/3), strictly inside
(-a,a), with a fixed margin even on the closure of this auxiliary
box. Thus C467e's compact coefficient ODE and its smooth derivatives
apply on a neighborhood of it. Let E(t,e^0),Pi(t,e^0) be that
solution, I=E_1, and

\[
\mathcal Q_t(z)=z^3-E_1z^2+E_2z-E_3,\qquad
P_t(z)=\Pi_1+(E_1-z)\Pi_2+(z^2-E_1z+E_2)\Pi_3.
\tag{7}
\]

On a smaller common time interval all relevant derivatives of E,Pi
are bounded, D_(e^0)E=Id+O(t), and Pi and every initial-coefficient
derivative of Pi are O(t). These follow from smoothness and Pi(0)=0
identically in e^0. They do not require simple initial roots.

C467l's ordered-root argument applies on this enlarged compact set:
its differential inequalities use only the initial (-a,a) domain,
the secant bound 5/1024 and |g'|<40, all supplied by C467e here.
Likewise C467m(7)–(9)'s upper-gap inequalities have exactly those
hypotheses. Applying these inequalities before the repeated-root
limit, as in those proofs, gives for the lower gap alpha and upper
gap beta_g

\[
\sqrt t\le\alpha\le5\sqrt t,\quad
\sqrt t\le\beta_g\le\sqrt{2h^2+24t},\quad
\alpha+\beta_g\le6\beta_g.
\tag{8}
\]

For the upper bound on beta_g use C467m(8) with initial upper gap
tending to h, and exp(82t)<2. All roots are real and simple for
t>0, with the ordered actual trace interpretation. These are
applications of the existing inequalities on their common compact
initial domain, not assumptions of a new continuation theorem.

Write q=q_3 and

\[
\ell=q-(I-q)/2=(3q-I)/2=(\alpha+2\beta_g)/2.
\]

In addition to (8), the actual extreme-root equation gives
q_t>=-C at fixed initial data: its two repulsive terms are positive
and Im g(Y_3) is bounded. Hence q>=c+2h/3-Ct, while I=3c+O(t).
Together with ell>=3sqrt(t)/2 and the upper bounds in (8), this
proves, after reducing time,

\[
C^{-1}\lambda\le\ell\le C\lambda,\qquad
C^{-1}\lambda\le q-c+h/3\le C\lambda,
\]
\[
C^{-1}\lambda\le\beta_g,\ \alpha+\beta_g\le C\lambda,
\qquad C^{-1}\lambda^2\le\mathcal Q_t'(q)\le C\lambda^2.
\tag{9}
\]

Explicitly, ell>=h-Ct and ell>=3sqrt(t)/2 imply its lower bound; its upper
bound follows from (8). Also q-c+h/3=2ell/3+h/3+O(t).
Finally beta_g>=2ell/7 follows from the last inequality of (8),
and Q'(q)=beta_g(alpha+beta_g). This proves every comparison in (9).
At t=0,h>0 the same comparisons hold for the simple singleton.

The same extreme-root equation, with its actual secants, now yields

\[
|q_t|\le C/\lambda,\qquad q_t\ge c_1/\lambda-C
\tag{10}
\]

for a fixed c_1>0, at fixed c,h. No frozen-background equation is
used. The additive bounded term in (10) is the actual Im g(Y_3).

### Cancellation in the inverse physical coordinates

Use physical coordinates (I,q,v), related linearly to Q=Im Z by

\[
Q=((I-q)/2-v,\ (I-q)/2+v,\ q).
\tag{11}
\]

For the original connector v=s alpha/2. Temporarily q is an
independent real variable in the coefficient formulas. Put

\[
e_c=(3,6c,3c^2-h^2/3),\qquad
W=e_h/h=(0,-2/3,-2c/3+2h/9),\quad L(q)=(q^2,-q,1),
\]
\[
D=D_{e^0}E,\quad a_1=I_c,\quad b_1=I_W,\quad
a_2=L(q)D e_c,\quad b_2=L(q)D W,\quad N=a_1b_2-b_1a_2.
\tag{12}
\]

Here I_W means the initial-coefficient directional derivative,
not a division of a derivative at h=0. On the actual singleton,
the simple-root formula gives q_c=a_2/Q'(q), q_h/h=b_2/Q'(q).
Since at time zero I_c=3, I_W=0 and D=Id, smoothness gives

\[
a_1=3+O(t),\quad b_1=O(t),\quad
a_2=3(q-c)^2-h^2/3+O(t)=O(\lambda^2),
\]
\[
b_2=\tfrac23(q-c+h/3)+O(t),\qquad
N=2(q-c+h/3)+O(t).
\tag{13}
\]

The O(t) remainders here are smooth on a compact (t,c,h,q) box,
with bounded derivatives there. Since t/lambda<=sqrt(t), (9)
allows one common time for which

\[
a_1\ge2,\quad c_2\lambda\le N\le C\lambda,\qquad
|q_c|\le C,\quad c_2/\lambda\le q_h/h\le C/\lambda.
\tag{14}
\]

In particular the (c,h)->(I,q) Jacobian is hN/Q'(q)>0 for h>0.
At fixed I its q derivative is hN/(a_1 Q'(q))>0. Also I_c>=2.
For |I|<I_m=1/32 and all h in [0,h_m], the equation
I(t,c,h)=I has a unique solution with |c|<c_m, for small common
time, because I=3c+O(t) with a strict endpoint margin. Therefore
(I,q) gives one global chart between the two singleton graphs at
h=0 and h=h_m; it is not merely a collection of possibly conflicting
local inverses. At t>0 the lower graph is smooth in I and t.
Its I derivative is q_c/I_c, uniformly bounded by (14).

Write k_r=h h_r solely as an abbreviation for derivatives of the
inverse chart at h>0. Differentiating its two equations gives

\[
\begin{pmatrix}a_1&b_1\\a_2&b_2\end{pmatrix}
\binom{c_I}{k_I}=\binom10,\qquad
\begin{pmatrix}a_1&b_1\\a_2&b_2\end{pmatrix}
\binom{c_q}{k_q}=\binom0{\mathcal Q_t'(q)},
\tag{15}
\]
\[
\begin{pmatrix}a_1&b_1\\a_2&b_2\end{pmatrix}
\binom{c_t}{k_t}=\binom{-I_t}{-L(q)E_t}.
\tag{16}
\]

The derivatives on the right of (16) hold initial data fixed;
those on the left hold physical I,q fixed. In particular
L(q)E_t=Q'(q)q_t=O(lambda) by (9)–(10). Equations (13)–(16)
give

\[
|c_I|\le C,\ |c_q|\le Ct\lambda,\quad
|k_I|+|k_q|\le C\lambda,\quad |c_t|+|k_t|\le C.
\tag{17}
\]

Thus |D_(I,q)e^0|+|e^0_t|<=C: use e^0_r=e_c c_r+W k_r.
The apparent inverse h factor has canceled in this statement.
It is not an estimate obtained by treating fixed-initial and
fixed-physical time derivatives as interchangeable.

For clarity the differentiated bound needed later is

\[
|D_{(I,q)}^2 e^0|+|D_{(I,q)}e^0_t|
             \le C(1/\lambda+1/h).
\tag{18}
\]

Here is a direct verification, including the possible h singularity.
The first physical derivatives of c,h satisfy
|D c|<=C and |D h|<=C lambda/h by (17). Every smooth compact-box
function of (t,c,h,q) therefore has physical derivative bounded
by C(1+lambda/h). This applies to the entries of (15)–(16),
their numerators and N. Each solution coefficient in those equations
is a quotient R/N which is already bounded by (17). Consequently

|D(R/N)| <= |D R|/N+|R/N| |D N|/N
          <= C(1/lambda+1/h).

This also applies to L(q)E_t, viewed as the smooth coefficient
expression rather than as Q'(q)q_t. Differentiate
e_c c_r+W k_r; e_c,W and their physical derivatives have the
bounds just stated. Since lambda is bounded above, these terms
are all absorbed by C(1/lambda+1/h). This proves (18).

### The extended real graph and the exact auxiliary velocity

Set J=3Pi_1+2E_1Pi_2+E_2Pi_3, eta=-Pi_2-q Pi_3, and
P=P_t. On the inverse chart define

\[
M_0=(J-P(q))/2,\qquad
p=(M_0-\eta v,\ M_0+\eta v,\ P(q)).
\tag{19}
\]

For v=s alpha/2 this is exactly Re Z by the reconstruction
secant identity. Extend (19) only to the auxiliary open cone

\[
|v|<\theta\ell,\qquad \theta=4/5,
\quad |I|<I_m,\quad 0<h<h_m.
\tag{20}
\]

The original connector has |v|/ell<=5/7 by (8), a strict margin
inside (20). Equation (19) has the form p=t R(t,e^0,q,v),
where R is smooth with bounded derivatives on the relevant compact
box: all coefficients of P,J,eta have a smooth factor t. Using
(17)–(18), at fixed physical Q from (11), yields

\[
|p_t|\le C,\quad |D_Qp|\le Ct,\qquad
|D_Qp_t|\le C[1+t/\lambda+t/h],
\]
\[
|D_Q^2p|\le Ct[1+1/\lambda+1/h].
\tag{21}
\]

All norms in these estimates can be changed by fixed constants
between (I,q,v) and Q. For example differentiating
p_t=R+tR_t+tR_(e^0)e^0_t proves the first bound and its derivative
bound in (21); differentiating p=tR proves the others.

Choose time so ||D_Qp||<1/2 and put

\[
M=Id-iD_Qp,\quad u=-iM^{-1}p_t,\quad
\widehat\kappa=(F(p+iQ)/v^2)\det M.
\tag{22}
\]

The quotient in (22) denotes the following explicit smooth factor,
including its value at v=0; it never divides the original current:

\[
F/v^2=-4(1-i\eta)^2 G_1^2G_2^2e^{-H(p+iQ)},\quad
G_1=Z_3-Z_1,\ G_2=Z_3-Z_2.
\tag{23}
\]

In (20), Im G_1=ell+v and Im G_2=ell-v are at least ell/5.
Moreover |Re G_j|<=Ct ell. Indeed P_v=O(t), and
3P(q)-J=sum_j(P(q)-P(q_j)); the sum of the two nonzero imaginary
gaps is 2ell. This bounds P(q)-M_0 by Ct ell, and |eta v| has
the same bound. Thus |G_j| is comparable to lambda and their
phases differ from pi/2 by O(t).

At time zero on the closure of the auxiliary box and cone,
|Q_j|<=1/30 for the pair and |q|<=5/192. Uniform root continuity
and p=O(t) allow a common time with |p_j+iQ_j|<1/16 throughout.
Thus |sum beta(p_j+iQ_j)|<=15/64; H_0 is real. Equations
(21)–(23) show that a phase of -widehat kappa has modulus less
than 1/2 after reducing time: the six gap-factor phase errors and
the determinant phase are O(t), and 15/64<1/2. In particular

\[
\operatorname{Re}(-\widehat\kappa)
       \ge\tfrac12|\widehat\kappa|>0.
\tag{24}
\]

Define the real velocity on (20) by

\[
b=-\operatorname{Re}(\widehat\kappa u)/
                              \operatorname{Re}\widehat\kappa.
\tag{25}
\]

It is smooth wherever t>=0,h>0, including v=0 and at time zero
with positive h. The singleton is simple there even at t=0;
no lower-pair root derivative occurs in (19). All time-zero
statements here mean one-sided smoothness, or its local smooth
extension with h fixed positive.

The key estimates are

\[
|b|\le C,\qquad |D_Qb|\le C[1+1/\lambda+t/h].
\tag{26}
\]

To verify the derivative estimate rather than assume it, (21)
and ||M^(-1)||<=2 give
|u|<=C and |D_Q u|<=C[1+t/lambda+t/h]. In (23), the logarithmic
derivative of each G_j has modulus <=C/lambda, because
|G_j|>=c lambda and D_Q Z is bounded. The eta and H derivatives
are bounded. The determinant logarithmic derivative is bounded
by C|D_Q^2p|, since M^(-1) is bounded. Hence

|D_Q widehat kappa|/|widehat kappa|
       <=C[1+1/lambda+t/h].

Differentiate (25) and use (24) to obtain (26). The factor v^2
has been removed before this estimate, so no fictitious 1/|v|
term occurs. The real parts in (25) retain the actual phase.

On the original connector this is exactly C467o(19). Its
pullback calculation proves that a solution
chi_t+b dot D_Q chi=0 gives (4) off s=0. At s=0 equation (4)
holds because every coefficient of the original form vanishes.

### Backward characteristics stay in one common domain

We now check the characteristic hypotheses, instead of extending a
boundedness estimate into an unproved flow assertion. Transform
the velocity b by (11); write its components as b_I,b_q,b_v.
All are bounded. Along a forward physical characteristic,
the initial-parameter coordinates c(t),h(t) satisfy

\[
I_c\dot c+h I_W\dot h=b_I-I_t,\qquad
q_c\dot c+h q_W\dot h=b_q-q_t,
\tag{27}
\]

where q_W=b_2/Q'(q), and the quantities on the right with subscript
t again hold initial c,h fixed. Eliminating dot c gives

\[
h\dot h=
\frac{I_c(b_q-q_t)-q_c(b_I-I_t)}
     {I_c q_W-I_W q_c}.
\tag{28}
\]

The denominator N/Q'(q) is positive and comparable to 1/lambda.
Equations (10),(14),(26) show globally on the auxiliary domain

\[
|h\dot h|+|\dot c|\le C.
\tag{29}
\]

They also give an actual outward-in-backward-time condition in
a fixed small collar. Choose delta>0 with delta<h_m/2 so small
that the negative c/lambda term from -I_c q_t in (28) dominates
its bounded terms whenever h<=delta and sqrt(t)<=delta. Then
reduce time further, if necessary, so

\[
\frac{d}{dt}h^2\le-d_*<0
       \quad(0<h\le\delta,\ 0\le t\le\tau)
\tag{30}
\]

for a fixed d_*>0. To be precise about this choice, (10) supplies
a numerator bound -c/lambda+C and an upper denominator bound
C'/lambda; first ensure lambda<=2delta makes the numerator
at most -c/(2lambda). Division gives (30). Constants are uniform
in v throughout the cone. We do not assert (30) for every h.

For a uniform neighborhood margin, start at any auxiliary physical
point at time t_0 in (0,tau] satisfying

\[
0<h_0\le h_s=3/256<h_m,\quad |I_0|\le I_s=3/128<I_m,
\qquad |v_0|\le(3/4)\ell_0.
\tag{30a}
\]

All original physical points satisfy these inequalities with strict
margins after reducing time: h_0<=H_*, |I_0|<=5/256+Ctau,
and |v_0|<=5ell_0/7. Thus (30a) includes neighborhoods of the
original positive-t,h images, not merely those images themselves.
Local smooth ODE theory gives a unique backward trajectory while
it stays in (20). On any such trajectory, (29) bounds the change
of h^2 by C t_0. Since h_0<=h_s<h_m, choose tau so it cannot
reach h_m. Its I coordinate moves by at most C t_0, and
|I_0|<=I_s has a strict margin from I_m.
Hence it cannot exit the I sides either. The defining inverse
chart then keeps |c|<c_m.

For the cone sides, let ell_0 be ell at the terminal point. Both
ell and v change by at most C t_0 by (26) and (11), whereas
ell_0>=3sqrt(t_0)/2 and |v_0|<=3ell_0/4. Choose tau with

C t_0 <= c_3 (4/5-3/4) ell_0

for a sufficiently small fixed c_3, say after absorbing the two
velocity constants take c_3=1/4. This is possible uniformly since
t_0/ell_0<=2sqrt(t_0)/3. It prevents exit from |v|<4ell/5
and keeps ell comparable to ell_0 along the trajectory.

Finally (30) prevents backward exit at h=0. While the backward
path is in h<=delta, integration gives

\[
h(r)^2\ge h_0^2+d_*(t_0-r)
\tag{31}
\]

if its terminal point is in that collar. Once it leaves through
h=delta backwards it cannot reenter: the backward vector at that
boundary points toward larger h. If its terminal point already
has h>=delta, it stays at least delta backwards. These claims also
follow directly from the strict differential inequality at h=delta.
Thus every such trajectory stays away from h=0 on every compact
portion of its backward existence interval, and indeed all the way
to r=0 for each h_0>0.

The preceding estimates have strict margins and hold up to any
prospective first exit. Smooth compact-continuation therefore extends
each trajectory to r=0. At that endpoint h>0, so the vector field
is smooth there as already checked. This constructs one common
backward domain for all original points, without an assumption of
an invariant flow on the singular boundary. The same argument holds
on open neighborhoods of the original positive-t,h points, including
the x,s endpoint images, by their strict margins.

### Uniform transported derivatives and continuous boundary values

Along each path just constructed, (26), lambda=h+sqrt(r) and
(31) give a uniform integrable variational bound. In detail,

\[
\int_0^{t_0}\frac{dr}{\lambda(r)}\le2\sqrt{t_0},
\]
\[
\int_0^{t_0}\frac{r\,dr}{h(r)}
 \le t_0\left(2\sqrt{t_0/d_*}+t_0/\delta\right).
\tag{32}
\]

For the second bound use (31) on the portion in the collar and
h>=delta on the rest. The integral of
1/sqrt(h_0^2+d_*(t_0-r)) over any terminal interval is at most
2sqrt(t_0/d_*). The same displayed upper bound covers paths
which never enter the collar. Thus integral ||D_Q b|| is bounded
by one finite constant, independent of t_0,h_0 and the terminal
point. The estimate concerns derivatives at fixed physical Q.

Let R_0(t,Q) be the time-zero endpoint of this backward trajectory,
and define

\[
G(Q)=f(Q_1)f(Q_2)f(Q_3),\qquad
\chi(t,Q)=G(R_0(t,Q)).
\tag{33}
\]

At positive t,h this is smooth on the neighborhoods just obtained.
The variational equation and Gronwall applied with (32) give
|D_Q R_0|<=C. Characteristic constancy gives the exact equation
chi_t+b dot D_Q chi=0. Consequently

\[
0\le\chi\le1,\qquad |D_Q\chi|+|\chi_t|\le C_f,
\qquad |R_0(t,Q)-Q|\le Ct.
\tag{34}
\]

The last bound is the integral of |b|, not a variational assertion
at a singular point. Standard smooth ODE dependence is used only
on individual paths with h>0; the uniform estimate is furnished
by (32).

We spell out the boundary continuity needed for (33). Fix t>0.
In the (I,q) chart the lower h=0 boundary is the smooth graph
q=q_0(t,I), with bounded I derivative by (14). Near an original
point on that boundary, the cone has a strict v margin and the
upper h boundary is separated. Points on the interior side can
be joined locally by paths of length at most a fixed multiple of
their Euclidean distance: lift their q coordinates above the graph
by its Lipschitz constant times the I distance, join, and return.
The bounded spatial gradient in (34) therefore gives a unique
continuous extension of chi to that boundary. On every compact
positive-time interval the graph is smooth in t too, so the same
argument in spacetime, using both bounds in (34), proves joint
continuity. No boundary derivative at t=h=0 is inferred.

Now restrict to the original connector and put

\[
\phi(t,x,s,h)=\chi(t,\operatorname{Im}Z(t,x,s,h))\quad(t,h>0),
\tag{35}
\]

extending to h=0 as above. The original map has a continuous
positive-time one-sided h=0 trace by C467m. As t tends to zero,
its imaginary coordinates converge uniformly on the compact
original parameter box to (x,x,x+h): this follows from uniform
coefficient convergence E_t->e^0, continuity of ordered real roots
of monic cubics on the compact set, and the connector formula.
In particular it holds with h and s varying arbitrarily.
From (34) and the bounded gradient of G,

\[
|\chi(t,Q)-G(Q)|\le C_f t.
\tag{36}
\]

This estimate also holds on the positive-time h=0 trace by continuity.
Equations (35)–(36) therefore extend phi continuously to t=0 with
exactly f(x)^2 f(x+h), uniformly in the other parameters. They prove
continuity at the joint corner as well as on the separate faces.
Range preservation follows from (33). Smoothness and the fixed
x,s endpoint neighborhood extensions follow from the open margins
in the characteristic construction. Taking the final tau strictly
inside the constructed time interval supplies the upper-time face
as well; the outer h face already has the margin H_*<h_m.

### Original equation, complex derivative products and all faces

Equations (25),(33),(35) and C467o's exact pullback calculation give
the original real adjoint off s=0, and its undivided equation at
s=0 follows from the original zero coefficients. The common minus
normalization changes neither assertion.

For completeness, the sufficient estimate C467o(21)–(23) uses the
actual root lower gaps, smooth coefficient derivatives and original
C467m coefficient bounds to give

\[
|Q_t|+|Q_x|+|Q_h|\le C/t,\quad |Q_s|\le C\sqrt t,
\]
\[
|A|+|U|+|V|\le Cs^2t^{3/2},\quad |B_c|\le C|s|^3\sqrt t.
\]

Combining these with (34) by the chain rule proves, on the full
positive-t,h parameter box,

\[
|A\phi_t|+|U\phi_x|+|V\phi_h|\le C_f s^2\sqrt t,
\qquad |B_c\phi_s|\le C_f|s|^3t.
\tag{37}
\]

Both bounds are integrable. They estimate each complex product
before taking real parts, so (5) is the required condition, not a
weaker cancellation of bulk terms. Continuity and (5) satisfy every
hypothesis of C467o's full-cutoff conclusion. Its proof retains the
upper-time, x-side, s-endpoint and outer-h faces, uses the entire
one-sided inner trace and controls the lower-time face uniformly
in the other cutoff. Thus it supplies the stated complete limit
for arbitrary relative rates, with no extra corner term.

All nominated conditions are provided by (33)–(37); audit1049 below
checks the construction and the separate audit in C467o checks that
input. The extended graph is only a device for selecting
unconstrained side data. No assertion about matching those data to
chambers or triangles is part of this result.

### Independent conceptual audit — 16 November 2026, step1049

This is a REPRODUCTION conceptual audit of the unchanged
nomination1045/review1046 EXPLORE target. It reuses the recorded
source comparison and the precise standard ODE, Stokes and DCT
imports above. It does not reprove those general theorems. The full
C467o argument has been independently checked in its audit1049,
without using this construction. C467e/audit1017, C467l/audit1037
and C467m/audit1041 retain their actual-data qualifications. The
following checks concern every condition of the original pair-only
test, not a larger matched family or a smooth time-zero jet.

**Enlargement and gap estimates.** On the closure of (6), both
c-h/3 and c+2h/3 lie strictly in (-a,a): their largest possible
absolute values are 1/48 and 5/192, respectively. Thus C467e's
regular coefficient field supplies a common smooth neighborhood,
including the initial discriminant. Smoothness of the flow and
Pi(0,e^0)=0 for every e^0 imply all the asserted O(t) initial-data
derivatives, on a smaller compact neighborhood if needed.

The lower-gap differential inequality in C467l uses only the
actual ordered distinct flow, its secants and the background bound;
these hold on this enlarged initial set. Apply it and C467m's upper
inequalities before taking ordered repeated-root limits. For the
lower gap the initial value tends to zero, and for the upper it
tends to h. This gives precisely (8), including alpha<=5 beta_g.
At positive time all three roots are simple. The extreme-root
equation is

    q_t=2 c_31/(alpha+beta_g)+2 c_32/beta_g+Im g(Y_3),
    (1+(5/1024)^2)^(-1)<=c_3j<=1.

Its bounded background gives q>=c+2h/3-Ct. Combined with
I=3c+O(t) and the lower gaps, this yields ell>=h-Ct and
ell>=3sqrt(t)/2. For small time these jointly imply ell>=c lambda:
use the latter when h<=2sqrt(t), and the former otherwise.
The upper gaps imply ell<=C lambda. Then
beta_g>=2ell/7, alpha+beta_g>=beta_g and
q-c+h/3=2ell/3+h/3+O(t) prove all of (9).
The displayed extreme-root equation now proves both sides of (10),
with positive c_1. It is not a frozen-background approximation.

**Global chart and differentiated inverse.** Direct differentiation
of (6) gives exactly e_c and hW in (12). At t=0 their contractions
with L(q) are 3(q-c)^2-h^2/3 and 2(q-c+h/3)/3.
Thus (13) has smooth O(t) errors with bounded derivatives when q is
independent. Since t/lambda<=sqrt(t), the positive leading term of
N dominates on one common time. This proves (14), including the
sign of q_h/h. At fixed I, the derivative of q with respect to h
is hN/(a_1 Q'(q))>0. At c=+-1/64 the values of I tend uniformly
to +-3/64, leaving a strict margin around |I|<=1/32. Monotonicity
in c therefore gives a unique c for each such I,h, and monotonicity
in h gives a single inverse chart between its two boundary graphs.
There is no unproved global-injectivity inference from a local Jacobian.

At fixed physical I,q, differentiating Q_t(q)=0 and I=I(t,c,h)
gives (15)–(16), including the minus sign on L(q)E_t. Cramer's
rule, N comparable to lambda and L(q)E_t=Q'(q)q_t=O(lambda)
give (17). In particular c_t and k_t are bounded; neither is
the derivative at fixed initial c,h. Since e^0_r=e_c c_r+W k_r,
the factor h cancels in every first physical derivative of e^0,
including its time derivative.

For the second derivatives, D c=O(1) and D h=O(lambda/h).
Each entry and numerator of these two linear systems is a smooth
function on the compact independent (t,c,h,q) box. Its physical
derivative is at most C(1+lambda/h). Every solution coefficient
is already bounded and is R/N, so differentiating the quotient
gives C(1/lambda+1/h). Differentiating e_c and W contributes at
most C(1+lambda/h), absorbed in that bound on this bounded box.
This verifies (18), in particular D e^0_t, without dropping the
possible 1/h term or differentiating an O(lambda) estimate as though
it were a smooth remainder.

**Graph, phase and original equation.** The polynomial identities
sum P(q_j)=J and (P(q_2)-P(q_1))/(q_2-q_1)=eta verify (19)
on the original connector. Its |v|/ell<=5/7 lies strictly inside
the enlarged 4/5 cone. Each coefficient of the reconstructed graph
has a smooth factor t. Applying the just-checked first and second
physical derivative bounds to p=tR yields every estimate (21).
In particular M is invertible with bounded inverse for a common time.

In the cone, Im G_j>=ell/5. The original secants are O(t), and
P(q)-M_0=(3P(q)-J)/2 is a sum of two such gap differences divided
by two. Hence the real gap parts are O(t ell). The t=0 box has
|Q_1|,|Q_2|<=1/30 and |q|<=5/192; uniform ordered-root continuity
therefore leaves the strict |Z_j|<1/16 margin at small time.
Taylor's bound |beta(z)|<=20|z|^2 gives 15/64 for the sum of
the three background magnitudes. H_0 is real. Factoring (23)
and adding its O(t) gap and determinant phases proves (24).
Here widehat kappa is nonzero, even at v=0; the original F still
has its double zero there.

The derivative of u follows from (21) and differentiation of M^{-1}.
Each G_j has bounded physical derivative and magnitude at least
c lambda; its logarithmic derivative is therefore O(1/lambda).
The eta and H terms are bounded, and the determinant derivative
uses D_Q^2 p. This proves the logarithmic estimate below (26) and
then (26) by differentiating the real quotient (25). Canceling v^2
before this auxiliary estimate avoids a spurious 1/v singularity.
C467o's checked wedge calculation verifies the velocity's minus sign
and the restriction to the exact original undivided equation. No
altered time, flow, connector or modulus-square weight is used.

**Common backward domain.** Equation (28) is obtained by eliminating
dot c from (27); its denominator is N/Q'(q)>0, comparable to
1/lambda. Its numerator is bounded in absolute value by C/lambda,
so |h dot h| is bounded, and the first equation in (27) bounds
dot c. More strongly, the numerator is <=-c/lambda+C by (10),
uniformly in v. Choose the fixed collar delta small after these
constants, then choose tau<=delta^2. Dividing this negative bound
by the positive upper bound C'/lambda proves (30) with a fixed
d_*>0. The direction is outward in backward time.

All terminal original images lie strictly inside (30a):
|I|<=3X+H_*+O(t)=5/256+O(t)<3/128 and H_*<3/256,
while their cone ratio is at most 5/7<3/4. Bounded drift prevents
exit at the I sides; bounded change of h^2 prevents reaching h_m.
Since ell and v change by O(t_0), and ell_0>=3sqrt(t_0)/2,
the margin 4/5-3/4 prevents exit from the cone uniformly as t_0
tends to zero. The inverse chart then retains its c margin.

If a backward path starts in the collar, integrate (30) on its
terminal collar interval to get (31). After exit through delta
it cannot cross back: its backward derivative of h^2 is positive
at that boundary. A path starting outside cannot enter either.
In particular h remains at least min(h_0,delta)>0 along each
individual path. These estimates hold until any supposed first exit,
with the other boundary margins strict. The smooth ODE continuation
theorem applies on a compact subset for that individual path and
extends it to r=0. At r=0 its h is positive, where the simple
singleton and auxiliary field are smooth. Uniform compact separation
from h=0 for all terminal points is neither asserted nor needed.

**Variations and continuity.** Along every constructed path,
1/lambda(r)<=1/sqrt(r) almost everywhere. On its terminal collar
interval, 1/h(r)<=1/sqrt(h_0^2+d_*(t_0-r)); off that interval
it is at most 1/delta. Integration gives exactly (32), with no
dependence on h_0. The finite integral of ||D_Q b|| therefore
controls the backward variational equation by Gronwall uniformly.
The common neighborhood margins justify varying the terminal point.
They give |D_Q R_0|<=C, hence bounded D_Q chi for the fixed bump.
The characteristic identity gives chi_t=-b dot D_Q chi, also
bounded. Bounded drift directly gives |R_0-Q|<=Ct. This proves
(34) using smooth ODE theory only on nonsingular individual paths.

For fixed positive time the lower physical boundary is the graph
q=q_0(t,I), with derivative q_c/I_c bounded by (14). A local
Lipschitz epigraph permits paths whose lengths are bounded by a
constant times the distance of their endpoints, by lifting above
the graph, joining and returning. The strict v and upper-h margins
allow these paths in the common backward domain near every original
boundary point. Bounded D_Q chi makes its limit unique there.
On each compact positive-time interval the graph is also smooth in
t; the identical spacetime argument with bounded chi_t proves joint
continuity, including the fixed parameter endpoints.

At time zero, bounded drift and the bounded gradient of G give
|chi-G|<=C_f t. Coefficients converge uniformly to e^0 on the
compact original box. Ordered real roots depend continuously on
the coefficients there, also at repeated roots, so Q converges
uniformly to (x,x,x+h), with s and h arbitrary. Composition yields
the exact initial value f(x)^2 f(x+h), and joint corner continuity.
Range preservation follows from the initial product in (33).
Smoothness is asserted only at t,h>0, with the x,s neighborhood
extensions already supplied by the strict auxiliary margins. None
of this asserts the joint smooth jet excluded by C467n.

**Four complex products and verdict.** C467o/audit1049 verifies the
C/t root derivative bound, the O(sqrt(t)) s derivative and their
chain-rule use with the original C467m coefficients. Inserting (34)
gives (37): the three separate t,x,h weighted products are bounded
by C_f s^2 sqrt(t), and the s product by C_f |s|^3 t. These are
integrable on the entire box, before any real-part cancellation.
The test is continuous, so C467o's independently verified full-face
limit applies for arbitrary relative cutoff rates.

Every condition of nomination1045 passes on one common existential
positive time. Its finitely many time reductions use fixed compact
constants and strict margins; none depends on the terminal t,h,s,x.
No numerical calculation or mathematical script is needed for this
audit. The DAG inputs remain C467e, C467l, C467m and C467o; the
smooth-stop discussion is a contrast, not a premise. This establishes
the existing proposed local input after review, not a theorem beyond
the sources checked or a complete RH candidate. Triangle and chamber
matching, exterior flux, realization, other degrees and Xi positivity
remain independent unresolved obligations.

## Mathlib

Full matching coverage for this actual continuous-adjoint construction
and its moving-domain estimates has not been checked. The supporting
dominated-convergence locator reused from C467m/o is
[`MeasureTheory.tendsto_integral_of_dominated_convergence`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/MeasureTheory/Integral/DominatedConvergence.html).
It does not provide the physical drift, inverse-coordinate estimates,
common characteristic domain or boundary continuity. No formalization,
new Mathlib search or claim of absence is made.
