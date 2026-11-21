# C466w — Mixed quadratic small-background sign at every survivor

## Hypotheses

Let 0<a<R<infinity, 0<b<L<infinity, T_0>0, H_0 real and
lambda in C. On B={|q|<R, |z|<L}, set
\[
 H(q,z)=H_0+\lambda qz.
\]
Choose finite nonnegative M_1,M_2 satisfying
\[
 M_1\ge |\lambda|\sqrt{R^2+L^2},\qquad M_2\ge|\lambda|,
 \quad M_1T_0<\min\{R-a,L-b\},                         \tag{1}
\]
\[
 u:=M_1\sqrt{a^2+b^2},\quad v:=M_2T_0,\qquad
 u+v\le\frac1{100}.                                  \tag{2}
\]
These bound the holomorphic gradient and Hessian in the standard
Hermitian norms on the entire bidisk: the gradient is
(lambda z,lambda q), and the Hessian is
[[0,lambda],[lambda,0]], of operator norm |lambda|.
No reality condition is imposed on lambda.

Use C466s's unit flat physical-time flow on U=B minus {q=0}:
\[
 \dot q=-2/\bar q+\bar\lambda\bar z,\quad
 \dot z=\bar\lambda\bar q,\quad X(0,r,s)=(ir,s),        \tag{3}
\]
where r,s are real, r!=0, |r|<a and |s|<b. Let [0,tau(r,s))
be the first maximal lifetime in U. At fixed physical time define
\[
 J_t=[\partial_r X,\partial_s X],\quad F=q^2e^{-H},
 \qquad W_t=-F(X(t))\det_{\mathbb C}J_t/i.             \tag{4}
\]
All four entries of J are retained. No derivative at fixed radius,
separation from the divisor or continuation after tau is assumed.

## Conclusion

For every 0<=t<=T_0 with t<tau(r,s), the weight is nonzero and
\[
 \Re W_t\ge\cos(1/25)|W_t|
          \ge\frac{1249}{1250}|W_t|>0.                \tag{5}
\]
In particular, this mixed family cannot produce the negative witness
sought in assessment969, including when s!=0 and arbitrarily near
first collision. The zero extension to stopped points has nonnegative
real part by definition; no boundary Jacobian is asserted.

This is a local obstruction to one genuinely coupled quadratic ansatz,
not an RH result or an assertion about every quadratic or holomorphic
background. The general sign conjecture, actual-H applicability, patch
phase alignment, signed global integration, all-order signs and Xi
transfer remain open. The proof is a local deduction under the ready
EXPLORE assessment969, with originality unestablished. The separate
independent conceptual audit974 below validates the stated result without
enlarging its scope or asserting originality.

## Proof

### Imported flow facts and scope of the specialization

C466s supplies smooth dependence at fixed physical time on the open
survivor domain and the identities
\[
 \dot J=\overline{(D^2S)J},\quad J_0=\operatorname{diag}(i,1),
 \qquad \dot F=-\|\nabla S\|_2^2F,
 \quad S=-2\log q+H.                                 \tag{6}
\]
The first formula is the flat-metric real-variation law in Tanizaki,
Nishimura and Verbaarschot, *Gradient flows without blow-up for
Lefschetz thimbles*, JHEP10(2017)100,
[arXiv:1706.03822v2](https://arxiv.org/pdf/1706.03822v2),
27 September 2017, Appendix B, (B.1)–(B.5), printed p22.
Both the Hessian and the tangent are conjugated. It applies to the
two prescribed real-parameter columns on each compact surviving
interval; it asserts no sign. The second identity is the chain-rule
identity proved in C466s. Neither requires a global logarithm.

Fix arbitrary T<=T_0 with T<tau. All arguments take place on [0,T],
where the trajectory is a compact subset of U and all coefficients
are continuous and bounded. Constants below are independent of the
distance to collision. The singular tangent estimate is proved here
because the assessed primary passages do not provide this sign
conclusion. No affine sign theorem, current identity or Lagrangian
tangent-plane assertion is used.

### Radius, angular variation and earlier survival

Write rho=|q|, rho_0=|r|, sigma=sgn(r), and lift the argument on
[0,T] so that
\[
 q=i\sigma\rho e^{i\delta},\qquad \delta(0)=0.
\]
With g=lambda z, equation (3) gives
\[
 \dot\rho=-2/\rho+\Re(qg)/\rho,\qquad
 \dot\delta=-\Im(qg)/\rho^2,
 \qquad |g|\le M_1.                                 \tag{7}
\]
Put h=M_1 rho_0<=u<=1/100. At rho=rho_0 the radial derivative
is at most -(2-h)/rho_0<0. The radius initially decreases, and an
upward first return to rho_0 would contradict this strict derivative
bound. Thus rho<=rho_0 on the entire surviving interval, and
\[
 \dot\rho\le-\frac{2-h}{\rho}<0,\qquad
 \int_0^t\frac{d\xi}{\rho(\xi)}
 \le\frac{\rho_0-\rho(t)}{2-h}.                       \tag{8}
\]
The latter follows by integrating (2-h)/rho<=-dot rho on [0,t];
no improper collision integral is invoked. Therefore, with
omega=dot delta,
\[
 \int_0^t|\omega(\xi)|\,d\xi
 \le\frac{M_1(\rho_0-\rho(t))}{2-h}
 \le\frac{u}{2-u}=:d\le\frac1{199},
 \qquad |\delta(t)|\le d.                            \tag{9}
\]
The same estimates apply for both signs of r. They also give
|q|<=|r|<a<R. Since |dot z|<=M_1 throughout the bidisk,
\[
 |z(t)|\le |s|+M_1t<b+M_1T_0<L.                     \tag{10}
\]
These are estimates for every earlier surviving time. By C466s's
endpoint classification, any finite first lifetime <=T_0 can only
end at q=0; an earlier outer exit cannot be hidden. Nothing here
asserts that a specified time beyond collision is a survivor.

### Exact two-column system in a rotating frame

Set E=diag(1,0), k=2/rho^2, D=kE and
\[
 K=\operatorname{diag}(i e^{i\delta},1),\qquad
 Z=K^{-1}J=A+iB,
\]
where A,B are real 2-by-2 matrices. Initially A=Id and B=0.
This is a time-dependent change of frame of the already defined
fixed-time Jacobian; it is not differentiation of K^{-1}X with
respect to r,s. From (6), direct matrix multiplication gives
\[
 \dot Z=D\bar Z+C\bar Z-i\omega E Z,\qquad
 C=\begin{pmatrix}0&c\\c&0\end{pmatrix},\quad
 c=-i e^{-i\delta}\bar\lambda.                        \tag{11}
\]
Indeed bar(q)^2=-rho^2 exp(-2i delta) for either sigma, and
the normal diagonal coefficient is
-2 exp(-2i delta)/bar(q)^2=2/rho^2. Both off-diagonal coefficients
are c. The frame derivative is K^{-1}dot K=i omega E. In particular,
no mixed tangent entry has been omitted.

Write C_R=Re C and C_I=Im C entrywise. Both are real symmetric,
and each has real operator norm at most |lambda|. Separating (11)
into real and imaginary parts yields
\[
 \dot A=(D+C_R)A+(C_I+\omega E)B,\qquad
 \dot B=(C_I-\omega E)A-(D+C_R)B.                     \tag{12}
\]
For as long as A is invertible, put P=BA^{-1}, a real matrix
not assumed symmetric. Its exact equation is
\[
 \dot P=-DP-PD+N(t,P),                                \tag{13}
\]
\[
 N=C_I-\omega E-C_RP-PC_R-P(C_I+\omega E)P.
\]
For p=||P||_op and e(t)=|lambda|+|omega(t)|, submultiplicativity
and the preceding bounds give
\[
 \|N(t,P)\|\le e+2|\lambda|p+ep^2\le e(1+p)^2.        \tag{14}
\]

### Uniform graph bound and invertibility

The homogeneous propagator for dot P=-DP-PD is
P maps to Q(t,xi)P Q(t,xi), where
\[
 Q(t,\xi)=\operatorname{diag}
       \left(\exp\!\left[-\int_\xi^t k(w)\,dw\right],1\right).
\]
Its norm is at most one for xi<=t, since k>=0. Variation of constants,
P(0)=0 and (14) therefore give, while A is invertible,
\[
 p(t)\le\int_0^t e(\xi)(1+p(\xi))^2\,d\xi=:b(t).     \tag{15}
\]
This uses two-sided contraction and needs no symmetry of P. Since
p<=b, b(0)=0 and b'<=e(1+b)^2. Integration of
(b/(1+b))'<=e gives
\[
 p(t)\le b(t)\le\frac{\eta(t)}{1-\eta(t)},\qquad
 \eta(t):=\int_0^t e(\xi)\,d\xi.                     \tag{16}
\]
The denominator is positive, because (9) and (2) imply
\[
 \eta(t)\le |\lambda|T_0+d
           \le v+\frac{u}{2-u}\le v+u\le\frac1{100}.
 \quad\hbox{Consequently }p(t)\le\frac1{99}.           \tag{17}
\]
Here u/(2-u)<=u holds for 0<=u<=1/100, including u=0.

To justify that the graph exists on all of [0,T], suppose t_*<=T
were the first zero of det A. On [0,t_*) equation (12) becomes
\[
 \dot A=G A,\qquad G=D+C_R+(C_I+\omega E)P.
\]
The coefficients D,C_R,C_I,omega are bounded on [0,T], and (17)
bounds P uniformly on [0,t_*). Hence |tr G| is bounded there.
Jacobi's determinant identity gives
\[
 \det A(t)=\exp\!\int_0^t\operatorname{tr}G(\xi)\,d\xi>0.
                                                               \tag{18}
\]
Its right side has a uniform positive lower bound as t approaches
t_*, contradicting continuity and det A(t_*)=0. Thus A is invertible,
det A>0 and (17) holds on all of [0,T]. No bound on k uniform in T
was required: boundedness on each compact survivor suffices for this
continuation argument, whereas (17) itself is uniform up to collision.

### Full determinant, weight and sign

Because Z=(Id+iP)A and det K=i exp(i delta),
\[
 \det J/i=e^{i\delta}\det(Id+iP)\det A.               \tag{19}
\]
For a real 2-by-2 matrix P the exact identity
\[
 \det(Id+iP)=1-\det P+i\operatorname{tr}P
\]
retains the complete determinant, including the mixed product.
The real operator norm gives |det P|<=p^2 and |tr P|<=2p. Thus
Re det(Id+iP)>=1-p^2>0. Its principal argument beta satisfies
\[
 |\beta|\le\arctan\frac{2p}{1-p^2}
          =2\arctan p\le2p\le\frac2{99}.              \tag{20}
\]
The equality uses 0<=p<1, so 0<=2 arctan p<pi/2; no branch jump
or assumption of real eigenvalues is involved. In particular det J
never vanishes on the surviving interval.

Let
\[
 E_t=\exp\!\left(-\int_0^t\|\nabla S(X(\xi))\|_2^2\,d\xi\right)>0.
\]
By (6), F(X(t))=F(X(0))E_t, and
F(X(0))=-r^2 exp(-H_0-i lambda r s). The initial correction
B_0:=i lambda r s=H(ir,s)-H_0 obeys
\[
 |B_0|\le M_1\sqrt{r^2+s^2}\le u.                    \tag{21}
\]
For completeness, integrate the holomorphic differential of H on
the segment (q,z)=(i theta r,theta s), 0<=theta<=1, contained
in B, and apply the Hermitian Cauchy–Schwarz inequality. This proves
(21) from the whole-bidisk gradient bound, with no reality symmetry.

Combining (4), (18)–(21) now gives the exact positive-amplitude
factorization
\[
 W_t=r^2e^{-H_0-\Re B_0}E_t\det A\,|\det(Id+iP)|
          \exp(i\phi),\qquad
 \phi=\delta+\beta-\Im B_0.                           \tag{22}
\]
Every factor before exp(i phi) is strictly positive, and
\[
 |\phi|\le\frac1{199}+\frac2{99}+\frac1{100}
          =\frac{69401}{1970100}<\frac1{25}<\frac\pi2. \tag{23}
\]
The strict rational comparison is 69401<78804. Therefore
Re W>=cos(1/25)|W|, and cos x>=1-x^2/2 gives (5).
The signs for negative r were accounted for in (11), and the initial
Jacobian remains diag(i,1) for both signs. There is no orientation
replacement of the real parameters.

Since T was an arbitrary compact surviving time, the conclusion
holds for every survivor in the stated time window. No limit through
the singular endpoint, derivative of a stopped map, numerical
evidence or assumed positivity has entered the proof. C466s is the
direct local input. The buffer named in C466u is imposed in (1),
and C466v is a contrasting affine obstruction, not a premise.

### Independent conceptual audit974 — 14 November 2026

This audit uses unchanged assessment972 and its separate approval973.
It checks the complete argument (1)–(23), with C466s's already audited
smooth real flow, fixed-time variation, endpoint classification and
scalar F identity as inputs. No load-bearing defect was found. This
is verification and reproduction of the existing local obstruction,
not a stronger bound, a new general-H theorem or progress beyond the
literature checked. No additional external theorem is imported.

**Hypotheses and the radial estimate.** The actual gradient norm is
|lambda| sqrt(|q|^2+|z|^2), and the Hessian has both singular values
|lambda|. Thus (1) supplies C466s's bounds everywhere required, not
only on the trajectory. The flow vector is the conjugate of
(-2/q+lambda z,lambda q), as in (3). Using
dot(q)/q=dot(rho)/rho+i dot(delta) gives exactly (7).
For either sign of r the initial
radius is |r|, with h=M_1|r|<=u<=1/100. At any attempted upward
crossing of that radius the derivative is strictly negative. After
excluding that crossing, the stronger differential inequality (8)
holds at every earlier surviving time. Its integrated form has the
correct direction: (2-h) integral(1/rho)<=rho_0-rho(t).
Consequently total absolute angle variation, not just net angle,
is bounded by d=u/(2-u). This is what the graph estimate needs.

The bound |z(t)|<=|s|+M_1 t holds before the first exit. If a finite
first lifetime lies in [0,T_0], its limiting moduli satisfy
|q_*|<=|r|<R and |z_*|<=|s|+M_1T_0<L. C466s's endpoint
classification then forces q_*=0. This is not an assumption that a
flow stopped earlier remains a survivor. The proof uses no value at
that endpoint, and includes t=T_0 whenever T_0<tau.

**Frame and the complete graph equation.** Directly differentiating
J=KZ in time, at a fixed parameter pair, gives

\[
 \dot Z=K^{-1}\overline{D^2S}\,\overline K\,\overline Z
          -K^{-1}\dot K Z.
\]

The normal entry is (-i e^{-i delta})(2/bar(q)^2)
(-i e^{-i delta})=2/rho^2, since sigma^2=1. The two mixed
entries are both -i e^{-i delta} bar(lambda), and the lower
diagonal entry is zero. Also K^{-1}dot K=i omega E.
These checks recover (11), including both conjugations. K(0) is
diag(i,1) for negative as well as positive r, so Z(0)=Id.
Taking the real and imaginary parts gives (12) with +omega E B
in dot A and -omega E A in dot B. No spatial derivative of K is
being taken; J already denotes the fixed-time parameter derivative.

On an interval with det A!=0, differentiating BA^{-1} gives (13)
and its complete N, including -P(C_I+omega E)P. Real symmetry of
C_R,C_I gives their stated norm bounds, but no symmetry of P is
needed or asserted. For the homogeneous equation -DP-PD, direct
differentiation of Q(t,xi)P Q(t,xi) verifies its propagator. Both
factors have norm <=1. Applying that contraction to the full N and
using submultiplicativity proves (15) for every real P.

**Comparison and exclusion of the first singular projection.** On
each initially invertible interval, b is nonnegative, continuously
differentiable, and p<=b. Thus
(b/(1+b))'=b'/(1+b)^2<=e. Integrating from zero and using
eta<=v+u/(2-u)<=v+u<=1/100 gives b<=eta/(1-eta) and p<=1/99.
This comparison is obtained before assuming global invertibility.

If a first zero t_* of det A existed on a fixed compact surviving
interval [0,T], all coefficients D,C_R,C_I,omega would be bounded
on that interval by smoothness and min_[0,T]|q|>0. Together with
p<=1/99 before t_*, this supplies a finite bound K_T on |tr G|,
independent of t<t_*. Jacobi's formula gives
det A(t)>=exp(-K_T T)>0 there. Continuity of A at t_* contradicts
det A(t_*)=0. A limit of P at t_* is not required, and K_T is not
claimed independent of the distance to collision. Only the graph
bound (17) is collision-uniform. This distinction resolves the
potential circularity in continuing the graph.

**Determinant, phase and edge cases.** Since B=PA, the factorization
Z=(Id+iP)A has the correct multiplication order. The exact identity
det(Id+iP)=1-det P+i tr P uses every mixed entry. Singular-value
bounds give |det P|<=p^2; the two diagonal inner products give
|tr P|<=2p even for nonsymmetric P. Its strictly positive real
part justifies the single principal argument beta and (20), since
2 arctan p lies in [0,pi/2) for 0<=p<1. Therefore det J!=0.

The imported scalar identity multiplies F(X(0)) by a positive real
number on every compact survivor. It does not assert constant
Jacobian phase. At the initial point,
F=-r^2 exp(-H_0-B_0), B_0=i lambda r s. Integrating dH along
(i theta r,theta s) has speed sqrt(r^2+s^2), and the whole-bidisk
gradient bound proves |B_0|<=u. Combining the scalar and determinant
factors gives the phase delta+beta-Im B_0 with no additional
orientation sign. Its rational bound is
69401/1970100<78804/1970100=1/25. Finally
cos(1/25)>=1-(1/25)^2/2=1249/1250>0. The amplitude in (22)
is strictly positive because r!=0 and all its integrals are finite
on [0,T]. This proves precisely (5).

The proof permits arbitrary s with |s|<b; its initial phase was
retained above. At t=0, A=Id, P=0, delta=0, so the same argument
includes the initial weight. For lambda=0, direct checking gives
rho=sqrt(r^2-4t), J=diag(i|r|/rho,1) and
W_t=|r|rho exp(-H_0)>0 for 0<=t<r^2/4; it agrees with the
general formulas for either sign of r. No division by lambda, u,
v or p occurs. T=0 is covered directly; arbitrary positive compact
T<tau gives all remaining survivors. The zero extension is only a
definition and no derivative or trace at collision is asserted.

The sole direct lemma input remains C466s. C466u's buffer is an
explicit hypothesis, not an invoked current theorem; C466v is not
used. The DAG row therefore needs no change. General H, actual-Xi
background bounds, common patch phases, signed global integration,
intersecting collision divisors and all-order transfer remain open.

## Mathlib

No full matching Mathlib theorem for this coupled logarithmic flow,
its survivor sign or the tangent-graph bound was checked. Availability
is unknown, not absent. Supporting smooth real ODE dependence,
variation of constants, determinant differentiation, operator-norm
inequalities and elementary trigonometric results were not inspected
in Mathlib in this step. Audit974 verifies the informal argument only;
matching and supporting Mathlib coverage remain unchecked. No formal
verification is claimed.
