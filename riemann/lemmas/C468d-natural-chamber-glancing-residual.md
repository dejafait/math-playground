# C468d — The natural chamber transport fails the glancing first-jet test

## Hypotheses

Retain the joint selection problem of C468a–c and nomination1086/review1087,
with C467e's actual coefficient flow, C467p's original lower connector,
C467z's smooth physical chamber field, C467's glancing curve and
C467u's qualified actual-background signs. Thus

\[
n=3,\quad R=1/4,\quad a_0=1/16,\quad T_0=1/1920,\quad
X=1/256,\quad b_*=1/4096,\quad H_*=1/128.
\]

The original initial chamber collar is
u=(x-d,x+d,x+h), |x|<=X, 0<=h<=H_*, 0<=d<=h/4.
The original pair box is |x|<=X, |s|<=1, 0<=h<=H_*.
Use the original lower-slot endpoint permutation, raw time, divisor,
common minus sign and algebraic-square form
F=Delta^2 exp(-H), H=H0+sum beta(z_j), with
beta(z)=B(1+z)-B(1)-B'(1)z, g=beta', real H0 and |beta''|<40
on |z|<R. B is the specified conjugation-normalized logarithm of
xi(1/2+sqrt(w))/xi(1/2). No replacement of this background is made.

Retain L018/L021/L024/C466a's finite-zero/product qualifications through
the above inputs. In particular C467u's signs use the cited finite
verification through positive ordinate100 and first-zero isolation in
(14,15), from Suvrit Sra, *On some positivity properties of the Riemann
Xi function*, [W_pr5z5huy_v1, section2.1, (6)–(8)](https://hub.valency.io/works/W_pr5z5huy_v1).
This external verification is not independently replayed here.
The original calculation did not audit C468a–c; the separate
conceptual audit1094 checks their load-bearing claims and this result.

Let f be any fixed smooth real [0,1]-valued bump, equal to one on
[-b_*,b_*] and supported in (-2b_*,2b_*), with no evenness assumption.
Write G(Q)=product_j f(Q_j). A joint candidate is continuous on the
two original closed domains, smooth on their regular positive-time
interiors, satisfies the original undivided adjoint equations, and has
initial products G(u) and f(x)^2 f(x+h). No boundary or time-zero jet
of an unknown candidate is assumed.

Let R_c(t,Q) be C467z's regular auxiliary backward chamber endpoint
map and set

\[
\chi_c(t,Q)=G(R_c(t,Q)),\qquad
\Theta_c(t,u)=\chi_c(t,\operatorname{Im}Y(t,u)),
\quad a(x)=\operatorname{Re}g(ix),\quad
k(x)=\tan(3\operatorname{Im}\beta(ix)).                 \tag{1}
\]

Here Theta_c is a proposed chamber assignment, not a necessary value
for every chamber candidate. It has the original initial product and
its lower trace is C467z's T_c. All physical coordinates in the proof
lie in C467z's regular box after a common time reduction.

## Conclusion

Fix x in (0,X). Let h=h_g(t,x)>0 be C467's actual glancing curve and
Q_g(t)=Im Y(t,x,x,x+h_g). At these points

\[
\lim_{t\downarrow0}t^{-3/2}
 (b_p-b_c)(t,Q_g(t))\cdot D_Q\chi_c(t,Q_g(t))
=-\frac{\sqrt6}{2}(1+k(x)^2)a(x)a''(x)f(x)^2f'(x).
                                                               \tag{2}
\]

For every allowed f, choose x0 in (b_*,2b_*) with
0<f(x0)<1 and f'(x0)<0. C467u gives a(x0)<0 and a''(x0)<0,
so the right side of (2) is strictly positive. Therefore no pair
selection in the nominated class can match the chamber assignment
Theta_c on any positive common horizon. This remains true if that
assignment is imposed only on the earlier open interior sections used
by C468c at these glancing points.

This stops keeping the natural auxiliary chamber transport while
reselecting the pair. It does not stop jointly changing both scalars:
the glancing past-section datum has not been forced from time zero.
It does not import C468's fixed-h expansion into a shrinking-h limit.
The result and its load-bearing C468a–c inputs pass conceptual audit1094 below.
Repeated hits, alternative compatible past data, outer-face choices,
the common h=0 extension, integrability, cyclic matching, global signed
assembly and Xi transfer remain unresolved. There is no RH candidate
or certified claim of progress beyond the sources checked.

## Proof

### Scope, prior comparisons and standard inputs

Use the unchanged invocation-start EXPLORE assessment
`drafts/literature/2026-11-16-boundary-fed-chamber-pair-nomination-1086.md`,
separately approved at review1087. Its target includes testing jointly
selected characteristic data through glancing. C468c gives the
necessary first-jet condition but has not evaluated it for this datum.
C468/audit1086 stops a different assignment, the fixed pair transport;
its expansion holds with h fixed. Stops1043/1058/1060/1068/1081 keep
their stated hypotheses. The relevant chamber assessments and
boundary-fed working/history1088–1090 contain no evaluation of (2).
This bounded comparison is not a novelty certification.

Reuse the assessed regular ODE results of Gerald Teschl, *Ordinary
Differential Equations and Dynamical Systems*, April2012 preliminary
version, [Theorems2.5/2.10 pp40–47, Lemma2.14/Corollary2.15 pp52–53,
Theorems3.9/3.12 pp81–84 and Theorem6.1/proof pp189–190](https://www.mat.univie.ac.at/~gerald/ftp/book-ode/ode.pdf).
The regular flow and its smooth endpoint map are already supplied by
C467e/z. Taylor's theorem, the ordinary implicit function theorem at
simple roots, and elementary determinant differentiation suffice below.
The new application is the moving glancing limit and the graph-slope
variation. No general singular transmission theorem is reproved.

### The spatial normal in the shrinking glancing layer

Fix x>0. C467 gives h_g(t,x)=d(x)t^2/2+O(t^3), with d(x)>0.
Put epsilon=sqrt(t), c=x+h/3, and let Q1<Q2<Q3 be the actual
seam roots. Write e_c=(3c,3c^2,c^3) for the triple-root vector in
this subsection. The initial coefficient vector at fixed c,h is

\[
e^0(c,h)=(3c,3c^2-h^2/3,c^3-ch^2/3+2h^3/27).
                                                               \tag{3}
\]

C467e's smooth coefficient flow and C467(12) give
E_t(e)=e+t S_0(e)+O(t^2) in C1 on the fixed coefficient box,
where S_0=s+R_j, s(e)=(0,-6,-2e1), j(y)=Im g(iy), and
R_j(e_c)=j(c)e_c'. Here and below all asymptotics are along
h=h_g(t,x), with x fixed; no derivative of h_g is taken.
Because e^0=e_c+O(h^2), the mean mu=E_1/3 is c+t j(c)+O(t^2).
The centered physical cubic has linear coefficient -6t+O(t^2)
and constant coefficient O(t^2). After Q=mu+epsilon z and division
by epsilon^3 its polynomial is
z^3-6z+O(epsilon)(1+|z|) on bounded z sets. Its three simple limiting
roots are r=(-sqrt6,0,sqrt6). The ordinary simple-root implicit
function theorem, or disjoint small root intervals and Taylor's
theorem, therefore gives

\[
Q_j=c+\epsilon r_j+O(\epsilon^2),\qquad
\mathcal Q_t'(Q_j)=t(3r_j^2-6)+O(t^{3/2}).              \tag{4}
\]

All three roots here are the ordered actual roots from C467p, not roots
of a substituted background model. The bounded polynomial remainder
and the nonzero limiting derivatives justify the displayed errors.

We also need two actual seam tangents, not just its root locations.
Let Q_c and Q_W=Q_h/h be derivatives of the seam map holding t
and the other initial variable fixed. For h>0, differentiation of its
polynomial gives, with L(y)=(y^2,-y,1) and D_t=D_{e^0}E_t,

\[
(Q_c)_j=\frac{L(Q_j)D_t e^0_c}{\mathcal Q_t'(Q_j)},\qquad
(Q_W)_j=\frac{L(Q_j)D_t W}{\mathcal Q_t'(Q_j)},\quad
W=(0,-2/3,-2c/3+2h/9).                                \tag{5}
\]

The first numerator is t(3r_j^2-6)+O(t^{3/2}). Indeed
L(Q_j)e_c'=3(Q_j-c)^2, D s(e_c)e_c'=(0,0,-6), and
D R_j(e_c)e_c'=j'(c)e_c'+j(c)e_c''. Multiplication of the last
expression by L(Q_j) is O(epsilon), since
L(Q_j)e_c''=6(c-Q_j). Its contribution after multiplication by t
is thus O(t^{3/2}); the differences e^0-e_c and e^0_c-e_c'
are O(h^2). For the second numerator, D_t=Id+O(t) gives
(2/3)(Q_j-c)+2h/9+O(t)=(2/3)epsilon r_j+O(t).
Equations (4)–(5) prove

\[
Q_c\longrightarrow(1,1,1),\qquad
\epsilon Q_W\longrightarrow
\left(-\frac1{3\sqrt6},0,\frac1{3\sqrt6}\right).        \tag{6}
\]

Use C468a's rho=v^2-w0(t,I,q), I=Q1+Q2+Q3, q=Q3,
v=(Q2-Q1)/2, and put n=D_Q rho at the positive endpoint.
Because rho vanishes on the seam, n.Q_c=n.Q_W=0. At fixed I,q,
the vector Q_v=(-1,1,0) gives n.Q_v=2v. The three limiting vectors
in (6) and Q_v are linearly independent. Solving this nonsingular
three-equation system, using 2v/epsilon -> sqrt6 from (4), gives

\[
\frac n{\sqrt t}\longrightarrow
n_0=\frac{\sqrt6}{3}(-1,2,-1).                         \tag{7}
\]

This also proves n=O(sqrt(t)). No h-uniform bound for the second
derivatives of the inverse chart has been used.

### A uniform value limit for the interpolation factor

The smooth physical chamber graph p_c(t,Q) exists on a box including
all diagonals by C467z. It has a smooth factor t, and
partial_t p_c(0,Q)=(-a(Q1),-a(Q2),-a(Q3)). In coordinates
Q=(m-v,m+v,q), w=v^2, lower-slot symmetry writes it as

\[
p_c=\big(P-vS,\ P+vS,\ W_c\big)(t,m,w,q).             \tag{8}
\]

P,S,W_c each have a smooth factor t. The even/odd factorizations
are valid through v=0 even when q=m: the odd part divided by v
is given by the integral of its v derivative. Taylor's theorem for
the resulting smooth even functions shows that their first w
derivatives extend continuously to w=0. The needed bounds are on a
fixed physical box, so no singleton separation denominator occurs.

C467p's affine connector is exactly (8) with w replaced by w0 in
P,S,W_c, keeping v unchanged. Divided differences in w therefore give

\[
p_p-p_c=t\rho V,
\qquad V(t,Q_g(t))\longrightarrow
V_0=(a''(x)/2,a''(x)/2,0).                             \tag{9}
\]

For completeness, at t=0 the functions P/t and S/t are respectively
minus the mean and minus the divided difference of a(m-v),a(m+v),
whereas W_c/t=-a(q). Thus (P/t)_w -> -a''(x)/2 and
(W_c/t)_w=0, and v(S/t)_w ->0. These give (9) with the sign shown.
The integrals for the divided differences run between w and w0,
both tending to zero. This proves the value limit along h=O(t^2)
directly; it does not extend any fixed-h Taylor remainder.
At each positive t,h, V is smooth in a neighborhood of the seam.

On that seam, differentiation of the exact identity (9) gives

\[
Z_p-Z_c=tVn,\qquad U_p-U_c=tV\rho_t,\qquad
Z_j=D_Qp_j,\quad U_j=\partial_t p_j\big|_Q.             \tag{10}
\]

The terms involving derivatives of V vanish because rho=0. Hence
no estimate on such derivatives as h tends to zero is required.
At glancing C468a gives rho_t+n.b_c=0 exactly. C467z gives

\[
Z_c=O(t),\quad U_c\longrightarrow U_0=-a(x)(1,1,1),
\quad b_c\longrightarrow k(x)U_0.
\]

Since n0 annihilates (1,1,1), equations (7),(9),(10) imply, with
delta=t^(3/2),

\[
\frac{Z_p-Z_c}{\delta}\longrightarrow E_0=V_0 n_0,
\qquad \frac{U_p-U_c}{\delta}\longrightarrow0,
\qquad E_0U_0=0,\quad
\sigma:=\operatorname{tr}E_0=\frac{\sqrt6}{6}a''(x).    \tag{11}
\]

Here V0 n0 is the outer-product matrix. The zero limit for the
fixed-physical time derivative uses actual glancing, not a time-zero
jet of a scalar or an interchange of fixed initial and physical data.

### Exact matrix variation of the real adjoint velocity

At the seam both graphs have the same p+iQ and the same nonzero F.
Set M_j=Id-iZ_j, A_j=F det M_j, u_j=-i M_j^(-1)U_j, so
b_j=-Re(A_j u_j)/Re A_j as in C468a. All denominators are nonzero
at these positive-time distinct physical roots. Equation (11) and
M_c -> Id give

\[
\frac{A_p/A_c-1}{\delta}\longrightarrow-i\sigma,
\qquad \frac{u_p-u_c}{\delta}\longrightarrow E_0U_0=0,
\qquad u_c\longrightarrow-iU_0.                       \tag{12}
\]

The first limit is determinant differentiation, and the second uses
M_p^(-1)-M_c^(-1)=i M_c^(-1)(Z_p-Z_c)M_c^(-1)+o(delta).
F cancels exactly from the first ratio; no derivative of its vanishing
Vandermonde factor or singular logarithmic derivative is taken.

C467z's factorization of the chamber density, including
p_k-p_j=(Q_k-Q_j)O(t), gives

\[
\frac{A_c}{\operatorname{Re}A_c}\longrightarrow1-ik(x).
                                                               \tag{13}
\]

Indeed A_c/Delta(Q)^2 tends to -exp(-H0-3 beta(ix)), whose real
part is nonzero by the inherited small-box phase bound. This checks
the sign and keeps the actual algebraic square.
Writing q_A=A_p/A_c, the exact difference formula is

\[
b_p-b_c=
-\frac{\operatorname{Re}(A_c q_A u_p)-
        \operatorname{Re}(A_c u_c)
        +b_c\{\operatorname{Re}(A_c q_A)-\operatorname{Re}A_c\}}
       {\operatorname{Re}(A_c q_A)}.
\]

Substitute (12)–(13), first dividing numerator and denominator by
Re A_c. The numerator divided by delta tends to
-sigma U0-k sigma b_c(0,x,x,x)=-(1+k^2)sigma U0.
The denominator tends to one. Therefore

\[
\frac{b_p-b_c}{t^{3/2}}
\longrightarrow(1+k^2)\sigma U_0
=-\frac{\sqrt6}{6}(1+k^2)a(x)a''(x)(1,1,1).            \tag{14}
\]

This computation uses the full density ratios; there is no claim of
equal tangential velocities at glancing. In particular (14) evaluates
the difference left open by the normal-flux identity.

### The scalar jet and the assignment-specific contradiction

Smooth dependence of the regular chamber flow gives
R_c(t,Q_g(t)) -> (x,x,x) and D_Q R_c(t,Q_g(t)) -> Id.
Consequently D_Q chi_c(t,Q_g(t)) -> f(x)^2 f'(x)(1,1,1).
Taking its scalar product with (14) proves (2).

The restriction Theta_c is an admissible chamber-only scalar on a
sufficiently small common horizon. Its values stay in [0,1], its
initial product is G, and X_c chi_c=0 by characteristic constancy.
The actual interior physical-coordinate map transfers this to the
undivided chamber equation; uniform root continuity supplies its
continuous boundary values. The small original collar stays inside
the regular physical box, which has a fixed margin. These observations
do not assert that the auxiliary backward paths stay in that collar.

Because f(b_*)=1 and f vanishes near 2b_*, the mean value theorem
gives a point with f'<0 in (b_*,2b_*). At such a point 0<f<1:
a differentiable [0,1]-valued function has zero derivative at a point
where it attains 0 or 1. Fix that x0. It has strict x and upper-h
margins, and the glancing points h_g(t,x0)>0 exist for all sufficiently
small positive times. They lie in the fixed-margin core required by
C468c after a common time reduction. C467u makes the right side of (2) strictly positive,
so the residual is nonzero at all these sufficiently small times.

If a joint candidate used Theta_c, C468c's smooth extension psi_minus
from its earlier interior section would equal chi_c near the glancing
point: both transport exactly the same smooth section data by the same
regular chamber field. C468c(4) requires the residual to be zero,
contradicting (2). The argument also applies when only these past
section values are prescribed to be chi_c. The contradiction occurs
at positive t,h on every positive proposed horizon and needs no
boundary derivative of the unknown pair scalar.

Nothing here forces an arbitrary candidate's past section to equal
chi_c. In the shrinking corner its backward path can meet an outer
collar face or a previous interface; the separated forcing theorem
cannot assign its datum there. A genuinely joint selection must change
the chamber data in this region as well as the old pair selection.
Whether such changed data meet the first-jet condition, the causal
return, the forced center and separated traces together remains open.

### Independent conceptual audit — 16 November 2026, step1094

This REPRODUCTION audit checks (3)–(14), as required by the unchanged
SPECIALIZE nomination1092/review1093, and their stated fixed-assignment
consequence. The actual coefficient graph and qualified background
signs come from C467e/z, C467/audit1083 and C467u/audit1062.
The first-jet prerequisite is checked in C468c's audit1094.

For fixed positive x, h_g=O(t^2) gives e0=e_c+O(t^4).
C467e's smooth flow has E_t=e+t(s+R_j)+O(t^2) in C1, with
s=(0,-6,-2e1) and R_j(e_c)=j(c)e_c'. After centering the cubic,
its linear coefficient is -6t+O(t^2) and its constant is O(t^2).
Scaling by sqrt(t) gives a perturbation of z^3-6z with simple
limiting roots -sqrt(6),0,sqrt(6). Its separated nonzero limiting
derivatives justify both error terms in (4); no near-multiple-root
inverse is taken after scaling.

For the first tangent numerator in (5),
L(Q)e_c'=3(Q-c)^2, L(Q)D s(e_c)e_c'=-6, and
D R_j(e_c)e_c'=j'(c)e_c'+j(c)e_c''. The last contraction is
O(sqrt(t)), since L(Q)e_c''=6(c-Q), so its time-weighted
contribution is O(t^(3/2)). The second numerator is
(2/3)(Q-c)+2h/9+O(t). Dividing by (4)'s nonzero scaled root
derivatives gives exactly (6). The three vectors 1,
(-1/(3sqrt(6)),0,1/(3sqrt(6))) and (-1,1,0) are independent.
The solution of the normal equations is n0=sqrt(6)(-1,2,-1)/3,
with n0.(-1,1,0)=sqrt(6); this verifies (7)'s sign and normalization.

The lower-slot even/odd decomposition of the smooth chamber graph
has bounded fixed-order w derivatives on a compact half-box w>=0,
including w=0. Smooth even functions of v have smooth functions
of v^2 there, with the needed bounded derivatives supplied by their
Taylor formula. Dividing by t is legitimate because the graph
vanishes identically at t=0. Freezing w at w0 is exactly the original
affine connector, including its singleton component. Since
pc_w/t tends to (-a''/2,-a''/2,0), its divided difference with the
frozen value gives the positive V0 in (9). On rho=0, derivatives
of V disappear from (10). In particular U_p-U_c uses rho_t at
fixed physical Q. The exact glancing identity rho_t=-n.b_c and
n0.1=0 imply its zero scaled limit in (11).

The matrix calculation in (12) uses
M_p^{-1}-M_c^{-1}=i M_c^{-1}(Z_p-Z_c)M_c^{-1}+o(t^(3/2)).
Its leading contribution to u_p-u_c is E0 U0=0. The trace is
sigma=sqrt(6)a''/6. The actual normalized chamber density tends
to 1-ik, while b_c tends to kU0. Thus the two nonzero terms in
the real quotient numerator are -sigma U0 and
-k sigma(kU0), giving -(1+k^2)sigma U0. The outer minus sign
produces (14). F cancels before taking ratios; its vanishing
Vandermonde size is never inverted in an error estimate.

Finally the smooth regular chamber endpoint map has D_Q R_c tending
to Id, so its scalar gradient tends to f(x)^2 f'(x)1. Its dot
product with (14) gives the factor 3 and hence (2)'s sqrt(6)/2.
At a point with f'<0 in (b_*,2b_*), the [0,1] range implies
0<f<1; C467u gives a<0 and a''<0. The residual is therefore
strictly positive. The auxiliary chamber assignment is admissible
by regular transport, fixed-box containment and root continuity;
it need not have backward paths in the original collar. If a
candidate prescribes these same local section values, uniqueness of
regular section transport identifies psi_minus with chi_c locally,
so C468c excludes it. This validates the fixed-assignment stop and
the velocity limit used by C468e, without forcing that assignment
on an arbitrary candidate. The finite-zero input remains unreplayed.

## Mathlib

Full matching coverage of this moving-interface glancing residual is
unchecked. Smooth flow dependence, elementary matrix differentiation,
the chain rule and Taylor/implicit-function tools are supporting facts,
not a formalization of the joint selection or this limit. No absence
claim or certified novelty claim is made.
