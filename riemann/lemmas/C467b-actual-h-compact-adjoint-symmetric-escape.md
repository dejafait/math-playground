# C467b — Actual-h compact adjoint test: symmetric escape obstruction

## Hypotheses

Use C467a's actual chart, its unit-flat raw flow and precisely its first
maximal lifetime, without restart. Explicitly,
\[
 h(w)=\xi(1/2+\sqrt w)/\xi(1/2),\quad e^{B(w)}=h(w),
 \quad B(1)=\log h(1)\in\mathbb R,\quad x=B'(1),
\]
\[
 H(z)=\sum_{j=1}^3\{B(1+z_j)-x(1+z_j)\},
 \quad H_0=3(B(1)-x)\in\mathbb R,
 \quad g(z)=B'(1+z)-x.
\]
The logarithm is the normalized branch on \(|w-1|<1/4\) from C466z.
Retain that result's external density qualifications when interpreting
this chart as part of the imported reciprocal density. No RH assumption
or density realization is used in the obstruction below.

Put
\[
 R=\tfrac14,\quad a=\tfrac1{16},\quad T_0=\tfrac1{1920},
 \quad I=(-a,a)^3,\quad \mathcal B=\{z:|z_j|<R\},
\]
\[
 \Delta(z)=\prod_{i<j}(z_j-z_i),\qquad F(z)=\Delta(z)^2e^{-H(z)}.
\]
For distinct real initial parameters \(u\), the flow is
\[
 \dot X_j=-2\sum_{k\ne j}\frac{X_j-X_k}{|X_j-X_k|^2}
                +\overline{g(X_j)},\qquad X(0,u)=iu.
                                                        \tag{1}
\]
Its first lifetime in \(U=\mathcal B\setminus\{\Delta=0\}\) is
\(\tau(u)\). Write
\(D=\{(t,u):0<t<T_0,\ u\in I,\ \Delta(u)\ne0,\ t<\tau(u)\}\).
Fix the ambient smooth compact cutoff \(\chi\) to be exactly one on a
neighborhood of the closed Euclidean ball of radius
\(r_*=(\sqrt3+1)/16\). This is a compact subset of \(\mathcal B\).

Use every coefficient in C467a(1). On survivors, with
\(J_j=\partial_{u_j}X\), \(J=[J_1,J_2,J_3]\), and \(V=\dot X\),
\[
 A=\chi(X)F(X)\det J,\qquad
 B_{ij}=\chi(X)F(X)\det[V,J_i,J_j],
\]
\[
 \begin{split}
 G=F(X)\{&d\chi(V)\det[J_1,J_2,J_3]
       -d\chi(J_1)\det[V,J_2,J_3]\\
       &+d\chi(J_2)\det[V,J_1,J_3]
       -d\chi(J_3)\det[V,J_1,J_2]\}.
 \end{split}                                             \tag{2}
\]
The differential of \(\chi\) is real. All coefficients are extended by
zero off \(D\), including stopped parameters and initial diagonals.
No derivative of a stopped map is defined.

The prescribed initial test is
\[
 \eta_0(u)=\prod_{j=1}^3 b(32u_j),\qquad
 b(s)=\begin{cases}\exp[-1/(1-s^2)],&|s|<1,\\0,&|s|\ge1.\end{cases}
                                                        \tag{3}
\]
An admissible time-dependent test is real, nonnegative, smooth in the
spatial variables and \(C^1\) in time on \([0,T_0]\times I\), with
continuous bounded first derivatives, a single compact spatial support
\(K\Subset I\) for all times, and \(\eta(0,\cdot)=\eta_0\).
These are nomination997's regularity and support requirements.

## Conclusion

There is **no** such test satisfying, on the whole survivor domain,
\[
 \operatorname{Re}\left[-i\{\eta_t A-\eta_1B_{23}
                         +\eta_2B_{13}-\eta_3B_{12}\}\right]\ge0.
                                                        \tag{4}
\]
The obstruction concerns these actual coefficients and this time horizon.
It is not a failed choice of ansatz and does not refute RH or all possible
signed comparisons. The incompatibility uses common compact support and
the pointwise payment condition; it does not exclude an integrated
payment condition with different boundary data.

For completeness, the proposed time-dependent balance itself is valid:
for any real test with the stated regularity and common compact support,
the raw integral \(a_\eta(t)=\int_I\eta(t,u)A(t,u)\,du\) has a unique
Lipschitz representative \(\widetilde a_\eta\) on \([0,T_0]\) with
\[
 \begin{split}
 \widetilde a_\eta(t)-\widetilde a_\eta(s)
  =\int_s^t\!\int_I
   \{\eta_t A+\eta G-\eta_1B_{23}
                    +\eta_2B_{13}-\eta_3B_{12}\}\,du\,dr,\\
 \widetilde a_\eta(0)=i\int_I\eta(0,u)\Delta(u)^2e^{-H(iu)}\,du.
 \end{split}                                             \tag{5}
\]
Here the full \(G\) in (2) vanishes for the specified cutoff. For each
test the representative equals the raw slice only almost everywhere in
positive time; at \(T_0\) only the representative is asserted. There is
no common exceptional set asserted for all tests.

The prescribed initial real signed mass is strictly positive:
\[
 \begin{split}
 M_0&=\operatorname{Re}[-i\widetilde a_{\eta_0}(0)]\\
 &\ge e^{-H_0-15/64}\cos(15/64)
                  \int_I\eta_0(u)\Delta(u)^2\,du>0.       \tag{6}
 \end{split}
\]
Thus failure of (4) is not caused by a missing initial mass or by
discarding gamma. The decisive exact contradiction is
\[
 \left(\frac{1483}{48000}\right)^2-\frac{121}{128000}
       =\frac{21289}{2304000000}>0.                       \tag{7}
\]

This is attempt1000 under the prior EXPLORE assessment ready998, after
its separate approval/recovery999. Independent conceptual audit1002 below
validates the obstruction and balance with unchanged hypotheses and constants.
The assessment did not identify an
existing theorem for this particular test; this is local progress beyond
the statements compared there, not certified originality or an RH
candidate. Global assembly, interfaces, tails, all degrees and Xi
transfer remain independent gaps.

## Proof

### Established local inputs and imported analysis

C467a/audit997 supplies the bounded Borel coefficient extensions, their
complete weak-current identity and the actual fixed-test initial limit.
In its notation, for finite constants \(E,C_0,C_1\),
\[
 |A|\le C_0E p(u),\quad |B_{ij}|\le C_0E m(u),
 \quad |G|\le4C_1E m(u),\quad
 -\int d\phi\wedge\bar\beta=\int\phi\bar\gamma,           \tag{8}
\]
where \(p,m\) are bounded and integrable on \(I\). These estimates cover
the whole box, including all diagonal intersections and zero extensions.

Use C466z/audit988's conjugation property of \(B\). Use C466/audit993's
survivor cone and its proved survivor-local estimates (7),(12),(17)-(21):
\[
 g(0)=0,\quad g(\bar z)=\overline{g(z)},\quad |g'(z)|<M:=40,
                                                        \tag{9}
\]
\[
 J=P+iQ=(Z+iI_3)Q,\qquad Q\text{ real and invertible},
 \quad Z=PQ^{-1}\text{ real symmetric},
 \quad\|Z\|\le k(t):=\tan(40t).                         \tag{10}
\]
Every ordered pair secant has real-to-imaginary slope of modulus at most
\(k(t)\). Also \(J\) is complex invertible and, since \(\chi=1\) on the
image, the cone gives
\[
 \operatorname{Re}(-iA)>0\quad\hbox{on }D,\qquad
 -iA=e^{-H_0}\Delta(u)^2K(t,u).                          \tag{11}
\]
These are used only on actual survivors; no boundary extension, global
velocity or positive uniform modulus floor is imported. The sharper
background bound and full matrix factorization are load-bearing parts
of that already proved survivor cone, not new assumptions about stops.

For local smooth ODE dependence and compact continuation, reuse Gerald
Teschl, *Ordinary Differential Equations and Dynamical Systems*, author
preliminary version April 2012,
[Lemma 2.14/Corollary 2.15, pp.52–53, and Theorem 6.1 and proof, pp.189–190](https://www.mat.univie.ac.at/~gerald/ftp/book-ode/ode.pdf).
The vector fields to which these are applied below are smooth on their
open domains, and compact continuation is invoked only after exhibiting
a compact subset separated from the original singularities.

For (5), reuse the tools inspected in review994 and review998: complex
Fubini and dominated convergence from J. K. Hunter, *Measure Theory*,
[Theorem 5.18, p.61](https://www.math.ucdavis.edu/~hunter/measure_theory/measure_notes_ch5.pdf#page=8)
and [Theorem 4.24 and Section 4.6, pp.49–50](https://www.math.ucdavis.edu/~hunter/measure_theory/measure_notes_ch4.pdf#page=11);
and the one-dimensional Sobolev representative theorem of T. Muthukumar,
*Sobolev Spaces and Applications*, 17 December 2023,
[Theorem 2.8.2 and proof, printed p.109](https://home.iitk.ac.in/~tmk/courses/mth656/main.pdf#page=117),
with the bounded-derivative fundamental-theorem consequence recorded in
Hunter, *PDE notes* (2009),
[Appendix, Theorems 3.50, 3.57, 3.59, 3.60, pp.75–77](https://www.math.ucdavis.edu/~hunter/m218a_09/ch3A.pdf).
The interval is finite and all integrands below are bounded by integrable
functions, so the precise hypotheses used in C467a remain satisfied.
No general transport comparison theorem is imported. The new work is
the actual symmetric characteristic and its quantitative escape test.

### Time-dependent testing, all terms, and the initial mass

Take \(\phi(t,u)=\theta(t)\eta(t,u)\), with
\(\theta\in C_c^\infty(0,T_0)\). This is a compact \(C^1\) test on the
open spacetime box. Equation (8) applies to it: convolve it with a smooth
approximate identity of sufficiently small support. The convolutions
have supports in one compact subset of the box and converge with their
first derivatives uniformly, by uniform continuity of those derivatives.
The bounded coefficients in (8) therefore permit passage to the limit.
This justifies the use of a \(C^1\)-in-time test without assuming extra
time smoothness.

Expansion in orientation \(dt\wedge du_1\wedge du_2\wedge du_3\) gives
\[
 d\phi\wedge\bar\beta
 =\{\theta'\eta A+
     \theta(\eta_tA-\eta_1B_{23}+\eta_2B_{13}-\eta_3B_{12})\}
          \,dt\wedge du_1\wedge du_2\wedge du_3.          \tag{12}
\]
Fubini is legitimate by (8), the finite box, and bounded first
derivatives of \(\eta\). It identifies the weak derivative of
\(a_\eta\) as the bounded function
\[
 t\longmapsto\int_I
     (\eta_tA+\eta G-\eta_1B_{23}+\eta_2B_{13}-\eta_3B_{12})\,du.
\]
Thus \(a_\eta\in W^{1,\infty}(0,T_0;\mathbb C)\); the cited scalar
representative theorem, applied componentwise, and the fundamental
theorem give (5), except for the initial identification, and its unique
Lipschitz extension to both endpoints.

The difference between \(a_\eta(t)\) and the fixed-test integral with
test \(\eta(0,\cdot)\) is bounded by
\(t\|\eta_t\|_\infty C_0E\int_Ip\), which tends to zero. C467a's
fixed-test initial limit therefore gives the initial expression in (5).
As there, equality along a sequence of times in the full-measure set
identifies the representative at zero; no arbitrary raw positive-time
slice is identified.

The strict buffer puts every surviving image in the closed radius
\(r_*\) ball. Consequently \(\chi(X)=1\) and the real covector
\(d\chi_X=0\). Each of the four terms in (2) vanishes on \(D\), and
the zero extension vanishes elsewhere. This proves \(G=0\), after
retaining it in the full identity. It uses no trace at a stopped event.

C466(8) gives \(|H(iu)-H_0|<15/64\) on \(I\). Since \(H_0\) is real,
\[
 \operatorname{Re}e^{-H(iu)}
       \ge e^{-H_0-15/64}\cos(15/64)>0.
\]
The nonnegative smooth bump (3) is positive on the open cube
\((-1/32,1/32)^3\). The squared Vandermonde is positive off its three
diagonals, hence its product with this bump has strictly positive
integral. This proves (6), including finiteness and strictness.

### The complete real adjoint field on a symmetric survivor line

Only on survivors define \(c=J^{-1}V\). Cramer's rule, with its column
orders retained, gives
\[
 B_{23}=Ac_1,\qquad B_{13}=-Ac_2,\qquad B_{12}=Ac_3.     \tag{13}
\]
Thus (4) involves every mixed term and is precisely
\(\operatorname{Re}[-iA(\eta_t-c\cdot\nabla\eta)]\ge0\).
This division is legitimate on \(D\), by (10)-(11); it has not been
defined at a zero or across the stopped set.

Let \(\mathsf P\) reverse the first and third coordinates and let
\(\mathsf T=-\mathsf P\) on real parameters. Conjugation and permutation
invariance of (1), and uniqueness on the first lifetime, give
\[
 X(t,\mathsf T u)=\mathsf P\overline{X(t,u)},\qquad
 \tau(\mathsf T u)=\tau(u).
\]
The domain and initial data have the same invariance. Differentiating
on survivors yields
\[
 J(t,\mathsf T u)=-\mathsf P\overline{J(t,u)}\mathsf P,
 \quad V(t,\mathsf T u)=\mathsf P\overline{V(t,u)}.
\]
The Vandermonde square and the sum defining \(H\) are invariant under
permutations. With \(\chi=1\) on the image, in complex dimension three
these identities give
\[
 A(t,\mathsf T u)=-\overline{A(t,u)},\qquad
 c(t,\mathsf T u)=\mathsf T\overline{c(t,u)}.             \tag{14}
\]

The fixed real subspace of \(\mathsf T\) is the line
\(u=r e\), \(e=(-1,0,1)\). On this line, \(A\) is purely imaginary
and (11) makes \(\rho=-iA\) real and strictly positive. Also
\(\operatorname{Re}c\) is tangent to the same line. Equation (4) there
is exactly
\[
                \eta_t-\operatorname{Re}c\cdot\nabla\eta\ge0.
                                                        \tag{15}
\]
The associated local characteristic is
\(\dot u=-\operatorname{Re}c(t,u)\), with \(u=r(t)e\).
It is smooth wherever it remains a survivor. The field also extends
smoothly to time zero near any fixed distinct initial point, where
\(J=iI_3\). No global real-field extension is required.

### Actual raw contraction on that line

For initial \(u=re\), \(0<r<a\), the symmetry in (14) writes the raw
orbit as
\[
 X=(p-iq,m,p+iq),\qquad p,m,q\in\mathbb R,\quad q(0,r)=r.
\]
One has \(q>0\) before the first lifetime: a first zero would make
\(X_1=X_3\). Put \(d=p-m\). The adjacent-secant bound from C466 gives
\[
                            |d|\le k(t)q.               \tag{16}
\]
For \(0\le t<T_0\), elementary sine and cosine bounds imply
\[
 k(t)\le\frac{1/48}{1-1/(2\cdot48^2)}
       =\frac{96}{4607}<\frac1{47}.                     \tag{17}
\]
The inequalities \(\sin s\le s\) and \(\cos s\ge1-s^2/2>0\) are
used only for \(0\le s\le1/48\).

From (9), \(|g(z)|\le40|z|\) on the disk. For real \(p\) with
\(p+iq\) in the disk, \(g(p)\) is real, and integration along the
vertical segment gives
\[
                        |\operatorname{Im}g(p+iq)|\le40q. \tag{18}
\]
All these segments are inside the original convex disk.

The three singular pair forces contribute exactly \(-12\) to the
derivative of \(\|X\|^2\), by grouping each unordered pair. Hence
\[
 \frac d{dt}\|X\|^2
   =-12+2\operatorname{Re}\sum_j\overline{X_j}\,
                                      \overline{g(X_j)}
   \le-12+80\|X\|^2.                                   \tag{19}
\]
Initially \(\|X\|^2=2r^2<2a^2\), and
\(80\cdot2a^2=5/8<12\). A first-crossing argument at the level
\(2a^2\), followed by (19), proves that this norm decreases on every
raw surviving interval and
\[
                             \|X\|\le\sqrt2 r\le\sqrt2 a. \tag{20}
\]

The imaginary equation for the third particle in (1) is exactly
\[
 \partial_tq=-\frac1q-\frac{2q}{q^2+d^2}
                         -\operatorname{Im}g(p+iq).     \tag{21}
\]
Using (16)-(18),
\[
 \partial_t(q^2)\le-2-\frac4{1+k^2}+80q^2
                  \le-6+4k^2+80q^2.                   \tag{22}
\]
At \(q=a\) the last bound is negative. The same first-crossing
argument therefore gives \(q\le r<a\), and then throughout the raw
surviving interval
\[
 \partial_t(q^2)\le-\frac{91}{16}+\frac4{2209}
                      <-\frac{1137}{200}=-C.
                                                        \tag{23}
\]
For the last strict inequality,
\(91/16-1137/200=1/400>4/2209\); its exact positive margin is
\(609/883600\). In particular the raw \(q\) decreases, and
\[
                       q(t,r)^2\le r^2-Ct.              \tag{24}
\]
This is asserted only as long as that raw solution survives, not as
a continuation after the right side becomes negative.

### The image moves too little along the adjoint characteristic

Write \(V=V_R+iV_I\). By (10), direct multiplication gives
\[
 \operatorname{Re}(J^{-1}V)
       =Q^{-1}(I_3+Z^2)^{-1}(ZV_R+V_I).                 \tag{25}
\]
Along \(\dot u=-\operatorname{Re}c\), the imaginary part of the image
has total derivative
\[
 \frac d{dt}\operatorname{Im}X(t,u(t))
       =V_I-Q\operatorname{Re}c
       =Z(I_3+Z^2)^{-1}(ZV_I-V_R).                     \tag{26}
\]
This includes the full parameter Jacobian, not just a gap derivative.
Since \(Z\) is real symmetric, \(\|(I_3+Z^2)^{-1}\|\le1\).
On the symmetric line the left side of (26) is \(\dot q e\), whose
Euclidean norm is \(\sqrt2|\dot q|\).

For clarity, all singular real components of \(V\) are
\[
                \left(-\frac{2d}{q^2+d^2},
                       \frac{4d}{q^2+d^2},
                      -\frac{2d}{q^2+d^2}\right).
\]
Their norm is at most \(2\sqrt6 k/q\). Equations (18),(20),(21)
bound the remaining components and give
\[
 \|V_R\|\le\frac{2\sqrt6 k}{q}+40\sqrt2 a,\qquad
 \|V_I\|\le\sqrt2(3/q+40q).                            \tag{27}
\]
Consequently (26) implies
\[
 |\dot q|\le k^2\{(3+2\sqrt3)/q+40q\}+40ak.            \tag{28}
\]
On any part of the characteristic where \(1/40\le q\le a\), use
\(3+2\sqrt3<13/2\), (17), and \(40a=5/2\) to obtain
\[
 |\dot q|<\frac{260+5/2}{2209}+\frac{5}{94}
              =\frac{380}{2209}<\frac15.                \tag{29}
\]
The final strict inequality is the integer comparison \(1900<2209\).
The raw derivative in (21)-(24) and the total characteristic derivative
in (26)-(29) are different derivatives; neither has been substituted
for the other.

### Compact support contradicts continuation and the two bounds

Suppose an admissible \(\eta\) obeying (4) exists. Start the characteristic
at \(u(0)=r_0e\), where \(r_0=31/1000\). This is strictly inside
the bump's positive set, since \(32r_0=124/125<1\). In particular
\(\eta(0,r_0e)>0\).

Take its maximal interval with \(t<T_0\), \(0<r(t)<a\), survival, and
\(q(t,r(t))>1/40\). Local existence gives a nonempty such interval.
By (15) and the chain rule, throughout it
\[
                  \eta(t,u(t))\ge\eta(0,r_0e)>0.        \tag{30}
\]
Thus \(u(t)\) lies in the single compact support \(K\Subset I\).
Choose \(a_K<a\) bounding every coordinate modulus on \(K\).
We have \(r(t)\le a_K\), and \(r(t)\ge q(t,r(t))>1/40\) by
raw contraction. Integration of (29) gives
\[
 q(t,r(t))\ge r_0-t/5
       \ge r_0-T_0/5=\frac{1483}{48000}
                        >\frac1{40}.                   \tag{31}
\]
The strict margin over \(1/40\) is \(283/48000\). Therefore the
characteristic cannot end by reaching that lower barrier or a parameter
diagonal, and (30) keeps it away from the faces of \(I\).

Here is the continuation justification at a potential endpoint
\(s<T_0\), without any regularity assumption on \(\tau\). For each
parameter \(r(t)e\) along this curve, every *earlier raw time*
\(0\le\theta\le t\) has
\(q(\theta,r(t))\ge q(t,r(t))>1/40\), by (23). Its three pair
distances are \(2q\) and two copies of \(\sqrt{q^2+d^2}\); all
exceed \(1/40\). Equation (20) bounds the entire earlier raw path by
\(\sqrt2 a<R\). These paths therefore lie in one compact subset of
the nonsingular ODE domain, with a strict distance from its boundary.

For any sequence of curve points tending to a finite time at most
\(s\), their parameters have a convergent subsequence in
\([1/40,a_K]\). Smooth dependence and compact continuation of (1)
give the limiting raw path through that time, and slightly beyond,
inside the same nonsingular domain. One way to apply the cited theorem
is to extend the smooth vector field from a neighborhood of that compact
set using a smooth compact cutoff; its common local flow agrees with
all the original paths there. The strict gap and spatial margins keep
the limiting path inside that neighborhood. Uniqueness identifies it
with the original first-lifetime solution. Thus the closure of these
curve points for times at most \(s\) is a compact subset of the actual
survivor chart, not of a conjectural stopped continuation.

On this compact subset, \(J\) is smooth and invertible by (10)-(11),
so \(c=J^{-1}V\) and its derivatives are bounded locally. The local
characteristic continuation theorem now extends \(r(t)\) past any
proposed endpoint \(s<T_0\). This proves existence along every
\(t<T_0\) under the hypothetical support and payment assumptions.
No quotient at a stopped point, uniform lower bound on \(A\) over all
survivors, or trace on a lifetime interface has entered the argument.

Apply (24) to the actual initial parameter \(r(t)e\) at each of those
times and combine it with (31):
\[
              (r_0-t/5)^2\le q(t,r(t))^2
                            \le a^2-Ct\qquad(0<t<T_0). \tag{32}
\]
Both outside expressions have ordinary scalar limits as \(t\uparrow T_0\).
They would force
\[
 \left(\frac{1483}{48000}\right)^2
       \le a^2-\frac{1137}{200}T_0=\frac{121}{128000},
\]
contrary to (7). This limiting step claims no raw slice at \(T_0\).
It proves the nonexistence in (4).

The time-dependent balance (5) would make its real signed representative
nondecreasing if (4) held, starting from (6). The contradiction above
instead shows that a regular test with the required common compact
support cannot impose that full pointwise payment through \(T_0\).
Stops961/968/979 are preserved: no unbuffered-current claim, automatic
sign inference from a weak identity, or repeated completed volume audit
is used. This is a local obstruction, not a global impossibility result
for the signed-current approach.

Exact arithmetic can be replayed with
`python3 scripts/adjoint-flux/symmetric-escape-1000.py`.
The full certificate is `scripts/adjoint-flux/symmetric-escape-1000.json`;
all seven strict rational comparisons pass, with no failures. It checks
the arithmetic in the displayed margins, not the analytic hypotheses,
matrix identities or characteristic continuation. Those are checked in
the independent conceptual audit below, not by the certificate.

### Independent conceptual audit — 15 November 2026, step1002

The invocation-start EXPLORE assessment ready1001 covers exactly this
audit. Reuse nomination1000/completion1001's inspected Teschl flow and
compact-continuation cases and its scalar representative sources, with
their versions, theorem numbers and links given above. C467a/audit997,
C466/audit993 and C466z/audit988 are established inputs. In particular,
the cone's estimates concern the actual full fixed-time Jacobian and
every ordered pair secant, on the first raw lifetime. They do not supply
continuation of a changing-parameter characteristic automatically.

**Full balance and endpoints.** C467a gives
\(p=|\Delta(u)|^2\le(2a)^6\) and
\(m\le6\sqrt2(2a)^5+120(2a)^6\), including the defined diagonal
extensions. These are integrable bounds on the whole finite box. For
\(\theta\eta\), common compact spatial support and compact time support
leave a positive distance from the spacetime boundary. Extension by
zero followed by convolution is therefore legitimate; uniform continuity
of its first derivatives on that compact neighborhood gives uniform
\(C^1\) convergence. Bounds (8) pass the complete weak identity to this
test. In the specified orientation the three mixed contributions are
\(-\eta_1B_{23},+\eta_2B_{13},-\eta_3B_{12}\). Moving them from
\(-\int d\phi\wedge\bar\beta=\int\phi\bar\gamma\) gives exactly
the weak derivative in (5), with \(+\eta G\). Finite measure, bounded
first derivatives and these Borel majorants meet complex Fubini's
hypotheses. The componentwise \(W^{1,\infty}\) representative and
fundamental theorem apply, yielding a unique Lipschitz extension to
both endpoints. The estimate preceding (13) identifies its initial
value using the actual fixed-test limit. It identifies no arbitrary
positive-time raw slice and no raw slice at \(T_0\).

The buffer is a neighborhood on which \(\chi\) is constant, so its
real differential annihilates all four vectors in (2), regardless of
their tangential or complex directions. Thus every term of \(G\)
vanishes before zero extension is used. At time zero,
\(\det(iI_3)=-i\) and \(\Delta(iu)^2=-\Delta(u)^2\), giving the
factor \(+i\) in (5). C466(8) and \(H_0\in\mathbb R\) give (6);
the bump times \(\Delta(u)^2\) is positive on an open set and bounded
with compact support. Initial positivity is consequently strict.

**Signs, reflection and matrix order.** Expansion of the replaced
column yields respectively \(c_1,-c_2,c_3\) in (13). The real
reflection \(\mathsf T=-\mathsf P\) preserves the initial domain
and the raw vector field under conjugation and permutation. Uniqueness
on the maximal nonsingular domain preserves first lifetimes, not just
short-time trajectories. Since
\(J(t,\mathsf T u)=-\mathsf P\overline J(t,u)\mathsf P\), its
complex determinant is \(-\overline{\det J}\); the two permutation
determinants cancel and the scalar minus sign has odd dimension.
The normalized real branch gives \(F(\mathsf P\bar X)=\overline{F(X)}\).
This proves (14), including the sign of \(A\). At the fixed line,
\(A=-\bar A\), and the inherited cone makes \(-iA>0\). Thus taking
the real part gives exactly (15); no unproved global velocity is used.

From \(J=(Z+iI)Q\), its inverse is
\(Q^{-1}(Z-iI)(I+Z^2)^{-1}\). The real and imaginary parts of \(V\)
then give (25). Multiplication by \(Q\) cancels only the leftmost
\(Q^{-1}\); subtraction from \(V_I\) gives (26), because \(Z\)
commutes with \((I+Z^2)^{-1}\). No commutation with \(Q\) is assumed.
Real symmetry of \(Z\), rather than its norm alone, gives the stated
inverse norm bound. At time zero the raw field and Jacobian extend
smoothly near every distinct initial parameter, with \(J=iI\), so the
characteristic has the claimed local initial solution.

**Bounds and the two derivatives.** For each unordered pair, its two
terms in \(d\|X\|^2/dt\) sum to \(-4\). With three pairs this is
\(-12\), as in (19). At the level \(2a^2\), the background upper
bound is \(5/8<12\); therefore the raw norm stays below that level
and decreases, giving (20). Reflection gives a real middle coordinate
and a conjugate outer pair. A zero of \(q\) would collide the outer
pair, so \(q>0\) on every raw survivor interval. The adjacent secant
bound gives \(|d|\le kq\). The vertical segment in (18) stays in the
convex disk, and \(g(p)\) is real. The outer-pair force contributes
\(-1/q\) and the adjacent force contributes \(-2q/(q^2+d^2)\) to
the third imaginary velocity; hence (21)-(22) have the indicated signs.
The upper bound at \(q=a\) is strictly negative. Once this barrier is
established, (22) is strictly negative everywhere below it, so \(q\)
decreases from \(r\), and (23)-(24) hold throughout the raw interval.

The real singular force vector in (27) has norm
\(2\sqrt6|d|/(q^2+d^2)\le2\sqrt6 k/q\). Its background norm is at
most \(40\|X\|\le40\sqrt2a\). The imaginary vector has opposite
outer components and zero middle component, giving its stated bound.
Dividing the norm in (26) by \(\sqrt2\) yields (28), including the
coefficient \(3+2\sqrt3\). Thus (29) bounds the **total** derivative
of \(q(t,r(t))\); (23) bounds its raw derivative with \(r\) fixed.
Both are used in their proper roles. The replay checked every rational
comparison, including \(380/2209<1/5\), with no failures.

**Changing parameters and compact continuation.** This is the essential
additional applicability check. Suppose the characteristic's maximal
restricted interval has endpoint \(s<T_0\). Positivity (30) confines
its parameters to \(K\), so \(r(t)\le a_K<a\). Equations (24),(29)
give \(r(t)\ge q(t,r(t))\ge q_*:=1483/48000>1/40\).
For each fixed parameter \(r(t)e\), every earlier raw path has norm
at most \(\sqrt2a\) and pair distances at least \(q_*\). Consequently
all these earlier paths lie in the fixed compact set
\[
 \mathcal C=\{z\in\mathbb C^3:\|z\|\le\sqrt2a,
                    \min_{i<j}|z_i-z_j|\ge1/40\}\Subset U.
                                                        \tag{33}
\]
This compactness includes the whole raw path, not only its final point.

Choose a smooth cutoff equal to one on a neighborhood of \(\mathcal C\)
with compact support in \(U\). The raw real six-dimensional vector field
times this cutoff, extended by zero outside \(U\), is a smooth bounded
field on \(\mathbb R^6\) with bounded derivative. Its flow \(\Phi\)
exists on every finite time interval by the cited continuation theorem
and depends smoothly on its initial point. It agrees with each original
earlier path by uniqueness. Given \(t_n\uparrow s\), pass to a
subsequence with \(r(t_n)\to r_\infty\in[q_*,a_K]\). For every
\(0\le\theta<s\), eventually \(\theta\le t_n\), and hence
\[
 \Phi_\theta(ir_\infty e)
   =\lim_n X(\theta,r(t_n)e)\in\mathcal C.
\]
Continuity in time gives the same inclusion at \(\theta=s\). Since
\(\mathcal C\Subset U\) and the cutoff is one nearby, this limiting
path continues slightly past \(s\) as the original raw ODE. Uniqueness
on its entire preceding interval identifies it with the first-lifetime
solution, proving \(s<\tau(r_\infty e)\). It is not a restart at \(s\).
The same argument applies to every limit point of the characteristic
graph; interior times already lie in the survivor chart, and the initial
point has its usual smooth neighborhood.

Thus its closed graph up to \(s\) is a compact subset of the open raw
flow chart (with the smooth extension at time zero). The cone proves
\(J\) invertible at every point of that compact set; continuity and a
finite neighborhood cover give bounded \(c=J^{-1}V\) and first derivatives
near it. Bounded characteristic velocity makes \(u(t)\) Cauchy as
\(t\uparrow s\), and smooth local existence extends it at its limit.
The margins \(q\ge q_*>1/40\), \(r\ge q_*\) and \(r\le a_K<a\)
remain strict there. Hence no defining restriction can fail at \(s\),
contradicting maximality. This proves continuation for every \(t<T_0\)
without any regularity assumption on \(\tau\) or inverse on the stopped
set. The cutoff is only a proof of local source applicability; no
cutoff-modified characteristic or stopped-map derivative is substituted.

**Terminal comparison and verdict.** Apply the raw inequality separately
to each actual parameter \(r(t)e\). The characteristic lower bound and
\(r(t)<a\) give (32). The lower bound is positive throughout the
interval, so squaring preserves its order. Taking the two scalar limits
would require \(2199289/2304000000\le121/128000\), whereas their
difference is \(21289/2304000000>0\). No endpoint raw slice is used.
All seven full certificate comparisons were inspected after replaying
`python3 scripts/adjoint-flux/symmetric-escape-1000.py`; the certificate
remains arithmetic-only evidence. The analytic checks above validate
(4)-(6) and retain stop1000 with unchanged hypotheses and constants.
The DAG's direct inputs C466, C466z and C467a suffice; C466y is used
through the latter two, and historical stops are contrasts, not premises.

This is independent reproduction of a previously unaudited local
obstruction, not another discovery or an RH resolution. Common compact
support and pointwise payment are essential to (30). Integrated payment
or different boundary data are not ruled out or approved by this audit.
All-degree positivity, global assembly, interfaces and actual-Xi transfer
remain unresolved. Full matching Mathlib coverage remains unchecked.

## Mathlib

Full matching coverage for this stopped-current adjoint obstruction has
not been checked; unknown availability is not evidence of absence.
C467a records supporting results
`MeasureTheory.tendsto_integral_of_dominated_convergence` and
`MeasureTheory.tendsto_integral_filter_of_dominated_convergence` in the
[DominatedConvergence documentation](https://leanprover-community.github.io/mathlib4_docs/Mathlib/MeasureTheory/Integral/DominatedConvergence.html).
They support limiting steps only, with their stated measurability and
integrable-majorant hypotheses; the filter theorem also has its
countably-generated-filter condition. No matching flow, cone,
characteristic-escape or Sobolev-representative formalization was checked.
No Lean verification is claimed. The rational margins in (7),(17),
(23),(29),(31) are exact; the analytic proof, rather than a numerical
trajectory or a bounded preview, is the evidence for nonexistence.
