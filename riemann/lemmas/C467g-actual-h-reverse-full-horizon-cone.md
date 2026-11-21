# C467g — Reverse actual-h full-horizon tangent and phase cone

## Hypotheses

Use the actual normalized B, x=B'(1), beta, g, H, H_0, F, raw
reversed flow Y and complete coefficient K_- of C467e. In particular,
n=3, R=1/4, a=1/16, T_0=1/1920, beta(z)=B(1+z)-B(1)-xz,
g=beta', beta'(0)=0, and C466/audit993 gives |beta''|<40 on
|z|<1/4. The initial u is any distinct real triple in (-a,a)^3.
Derivatives in u are at fixed physical time, with the original flat
metric and no change of the flow or weight.

Use C467e's full-horizon survival, radial bound and Gram reality, and
C467f's full-horizon imaginary ordering, centered momentum bounds,
canonical identity and conditional phase implication. The independent
conceptual audit1017 in these three canonical files validates C467e,
C467f and this result, with their stated local scope unchanged.
Preserve C466a's external density qualifications if interpreting the
analytic chart as a reciprocal-density chart. No density construction,
RH, forward barrier, forward current or forward lifetime is assumed.

## Conclusion

In C467f's scaled centered coordinates, let

\[
 L=1/8,\quad E=(C,B,D)=(c/L,b/L^2,d/L^3),\quad
 P=(M,U,W)=(3m/L,U,LV),
\]
\[
 A_t=D_{E^0}E_t,\qquad N_t=D_{E^0}P_t,\qquad P_0=0.
\]

The capital B in E is a real centered coefficient, not the analytic
logarithm B(w). Throughout 0<=t<=T_0, uniformly in every distinct u,

\[
 \det A_t>0,\qquad
 \|N_t A_t^{-1}\|_{\rm op}
 \le {9334\over25}t\le {4667\over24000}<{1\over5}.            \tag{1}
\]

Consequently the complete, stipulated K_- is nonzero and has a
representative phase satisfying

\[
 |\arg K_-(t,u)|<{95951\over64000}<{3\over2}<{\pi\over2}.
                                                                    \tag{2}
\]

Thus alpha=3/2 is one uniform cone angle on the gate's entire
survivor domain (indeed through its closed time endpoint). This is an
audited local cone result, not a complete RH argument.
No uniform modulus floor, diagonal extension, reverse current, initial
trace, mass payment, interface identity, all-degree positivity or Xi
transfer is asserted.

## Proof

### Source scope and the purpose of specialization

Reuse ready1012 and its completed review1012 for this unchanged flow,
metric, domain and full coefficient. The sources compared there do
not supply this quantitative cone. Standard smooth-flow, variational
and continuation tools are imported from Gerald Teschl, *Ordinary
Differential Equations and Dynamical Systems*, author-hosted April2012
preliminary version, [Lemma2.14/Corollary2.15, pp52–53; Theorem3.9,
p81; Theorem6.1 and proof, pp189–190](https://www.mat.univie.ac.at/~gerald/ftp/book-ode/ode.pdf).
They are applied on nonsingular local coefficient charts and to
finite-dimensional matrix ODEs with continuous coefficients. No
uniform initial gap is a hypothesis of the estimates below.

The other tools are Cauchy's derivative estimate, the residue theorem,
the real divided-difference mean-value theorem from Rolle's theorem,
and finite-dimensional matrix norm inequalities. Repeated-node
divided differences below follow by taking limits of distinct real
nodes; this is a specialization of the same mean-value bound. The
work needed beyond citation is the actual Hamiltonian's gap-free
Hessian estimate and its quantitative time comparison. No general
invariant-cone theorem is reproved. Originality is unverified.

### Scaled Hamiltonian and the interpolation interval

Write s_j=r_j/L. They are the three distinct real roots of

\[
 Q(s)=s^3+Bs-D,\qquad S_2=\sum_js_j^2=-2B.
\]

C467f's canonical identity becomes sum p_j dq_j=L^2 sum P_k dE_k.
The Hamiltonian for the unchanged physical time is therefore
mathcal H=tilde h/L^2, not tilde h. Explicitly, up to a locally
constant term,

\[
 \mathcal H(E,P)=-128\sum_j\arctan(U+Ws_j)
                  +\sum_j\operatorname{Im}\phi(z(s_j)),       \tag{3}
\]
\[
 \phi(z)={\beta(Lz)\over L^2},\quad
 z(s)=M/3-Us+W(s^2+2B/3)+i(C+s),\quad E'=\mathcal H_P,
 \quad P'=-\mathcal H_E.                                    \tag{4}
\]

Here |phi''(z)|<40 on |z|<2 and phi'(0)=0. All partial derivatives
of (3) use the real coordinates E,P. The root ordering gives a
smooth local chart at every point of the entire trajectory; for
each fixed u its coefficients and Hessians are continuous on the
compact time interval. Uniform estimates do not require a common
open coefficient box or a uniform lower bound on the gaps.

C467e/f give

\[
 S_2<6/5,\quad |s_j|<9/10,\quad |B|<3/5,\quad |D|<9/50,
 \quad |W|<119/7680<1/64.                                    \tag{5}
\]

For the product bound, maximizing |s_1s_2s_3| at fixed S_2 and
sum s_j=0 gives either product zero or two equal coordinates.
Indeed at a nonzero stationary product the equations for log|product|
give 1/s_j=lambda+mu s_j, so at most two distinct values occur.
The two-equal case gives D^2<=S_2^3/54<4/125<(9/50)^2.
The maximum exists on the compact circle, so this covers every case.

Let s run through the closed interval between the extreme roots and
put q_2(s)=s^2+2B/3=s^2-S_2/3. Since a centered three-vector obeys
s_j^2<=2S_2/3, the same inequality holds for s in this interval.
Thus

\[
 |q_2(s)|<2/5,\qquad \sum_j|s_j|<19/10,\qquad
 \sum_j|q_2(s_j)|<4/5.                                      \tag{6}
\]

The middle bound follows from Cauchy–Schwarz and 3S_2<18/5.
For the last bound, the three q_2(s_j) sum to zero and each has
modulus <=S_2/3. For three real numbers of sum zero, their sum of
absolute values is twice their largest absolute value.

The interpolation bounds in C467f(12) apply on this whole interval.
In physical coordinates they give |Re(Lz)|<1/80 and
|Im(Lz)|^2<3/160. Hence |Lz|^2<121/6400, so

\[
 |z(s)|<11/10,\qquad |z'(s)|<a_1:=101/100,\qquad
 |z''(s)|<a_2:=1/32,\qquad z^{(k)}=0\ (k\ge3).              \tag{7}
\]

For z' one may use C467f's bound directly; alternatively (5) and
|U|<5/128 give |Re z'|<5/128+9/320<19/160.
The second derivative is 2W. Cauchy on disks of radii tending to
9/10 inside |z|<2 now gives the following uniform bounds d_k for
|phi^(k)(z(s))|:

\[
 d_2=40,\quad d_3=400/9,\quad d_4=8000/81,\quad
 d_5=80000/243,\quad d_6=3200000/2187.                        \tag{8}
\]

These bounds use the complex-disk estimate on phi'', not a real-axis
estimate. They are valid also when taking real or imaginary parts.

### Root derivatives without inverse-gap majorants

For a smooth real k on the root interval write T k=sum_j k(s_j),
and [k]=sum_j k(s_j)/Q'(s_j), the second divided difference.
When k has no explicit coefficient dependence, root differentiation
gives

\[
 R_B k:=\partial_B T k=-[s k'],\qquad
 R_D k:=\partial_D T k=[k'].                                \tag{9}
\]

For the analytic functions used here, differentiation of the finite
residue integral gives

\[
 R_{BB}k=[s^2k']_6,\quad R_{BD}k=-[s k']_6,\quad
 R_{DD}k=[k']_6,                                             \tag{10}
\]

where [l]_6 is the divided difference at the six real nodes
s_1,s_1,s_2,s_2,s_3,s_3. For example R_B k is
-integral s k'(s)/Q(s) divided by 2pi i; its B derivative is
integral s^2 k'(s)/Q(s)^2 divided by 2pi i. The other signs
follow from Q_D=-1. These contour identities can be taken on any
small contour enclosing the three real roots in a holomorphic
neighborhood of their interval; they assert no common large contour.

For real or imaginary parts in these formulas, use their holomorphic
extensions in s: replace Re phi(z(s)) and Im phi(z(s)) by the half
sum and the difference divided by 2i of phi(z_+(s)), phi(z_-(s)),
where z_+ is (4) and z_- changes i(C+s) to -i(C+s). The same
construction applies to phi'. Conjugation symmetry of beta makes
these extensions agree with the real functions on the root interval;
(7) supplies their local holomorphic neighborhoods.

The mean-value bounds are |[l]|<=sup|l''|/2 and
|[l]_6|<=sup|l^(5)|/120. The latter follows by separating the
repeated real nodes slightly, applying the ordinary bound, and
taking the limit in a slightly enlarged interval. All derivatives
are continuous there. In particular, with r=9/10,

\[
 |R_B k|\le\|k''\|+{r\over2}\|k'''\|,\quad
 |R_D k|\le\tfrac12\|k'''\|,                               \tag{11}
\]
\[
 |R_{BB}k|\le {r^2\|k^{(6)}\|+10r\|k^{(5)}\|+20\|k^{(4)}\|\over120},
\]
\[
 |R_{BD}k|\le {r\|k^{(6)}\|+5\|k^{(5)}\|\over120},\quad
 |R_{DD}k|\le {\|k^{(6)}\|\over120}.                         \tag{12}
\]

Norms here are suprema on that real interval. Explicit dependence of
k on B or other coordinates must be differentiated in addition to
(9)–(12), as is done next.

### Background Hessian, including the cancellation

Let f=Im phi(z(s)), psi=Im phi'(z(s)), and chi=Re phi'(z(s)).
Both psi and chi have first three derivative bounds

\[
 v_1=d_2a_1,\quad v_2=d_3a_1^2+d_2a_2,\quad
 v_3=d_4a_1^3+3d_3a_1a_2.                                  \tag{13}
\]

The chain rule, using z'''=0, gives bounds for f^(4),f^(5),f^(6):

\[
 f_4=d_4a_1^4+6d_3a_1^2a_2+3d_2a_2^2,
\]
\[
 f_5=d_5a_1^5+10d_4a_1^3a_2+15d_3a_1a_2^2,
\]
\[
 f_6=d_6a_1^6+15d_5a_1^4a_2+45d_4a_1^2a_2^2+15d_3a_2^3.
                                                                    \tag{14}
\]

Set eta_0=1/96 and v_B=v_2+r v_3/2. The actual explicit derivative
z_B=eta=2W/3 has |eta|<eta_0. Equations (9)–(14) bound the absolute
entries of the background EE Hessian by the symmetric matrix

\[
 \begin{pmatrix}
 3d_2&3\eta_0d_2+v_B&v_3/2\\
 3\eta_0d_2+v_B&3\eta_0^2d_2+2\eta_0v_B+
 (r^2f_6+10rf_5+20f_4)/120&\eta_0v_3/2+(rf_6+5f_5)/120\\
 v_3/2&\eta_0v_3/2+(rf_6+5f_5)/120&f_6/120
 \end{pmatrix}.                                             \tag{15}
\]

For clarity the six corresponding expressions before majorization
are T(-Im phi''), T(eta Re phi'')+R_B chi, R_D chi,
T(eta^2 Im phi'')+2eta R_B psi+R_BB f,
eta R_D psi+R_BD f, and R_DD f. This accounts for both explicit
B derivatives in the BB entry.

For EP, the momentum derivatives of f are psi/3, -s psi and
q_2 psi. The B,W entry needs a cancellation. Its exact expression is

\[
 \eta T(q_2\operatorname{Im}\phi'')+{2\over3}T\psi
                         -[s(q_2\psi)'].
\]

Since T psi=[Q' psi], Q'=3s^2+B, and s q_2(s)=D-(B/3)s
at each root, its last two terms are exactly

\[
 {2B\over3}[\psi]-D[\psi']+{B\over3}[s\psi'].                \tag{16}
\]

No root-spacing estimate is used. By (5),(11), their total absolute
value is at most (2/5)v_2+(9/50)v_3. Combining all entries yields
the following absolute-entry bound, rows (C,B,D), columns (M,U,W):

\[
 \begin{pmatrix}
 d_2&(19/10)d_2&(4/5)d_2\\
 \eta_0d_2+v_B/3&\eta_0(19/10)d_2+2v_1+(5r/2)v_2+(r^2/2)v_3&
 \eta_0(4/5)d_2+(2/5)v_2+(9/50)v_3\\
 v_3/6&(3/2)v_2+(r/2)v_3&3v_1+3rv_2+v_3/5
 \end{pmatrix}.                                             \tag{17}
\]

Here the first row uses (6) directly. For B,U the root term is
[s psi+s^2 psi']; its second derivative divided by two is
2psi'+(5s/2)psi''+(s^2/2)psi'''. For D,U the analogous expression
is -(3psi''+s psi''')/2. For D,W it is
3psi'+3s psi''+(q_2/2)psi'''. The B,M and D,M entries follow
from (11), and the explicit B,U and B,W terms use (6).
These calculations justify every entry of (17).

The squared Frobenius norms of (15) and (17) are respectively
strictly less than 210^2 and 387^2; exact fractions are certified
below. Since the operator norm is at most the Frobenius norm,

\[
 \|\mathcal H^{\rm bg}_{EE}\|<210,\qquad
 \|\mathcal H^{\rm bg}_{EP}\|<387.                            \tag{18}
\]

Finally, for v_j=(1/3,-s_j,q_2(s_j)) the background PP Hessian
is sum_j Im phi''(z(s_j)) v_j v_j^T. Centering gives
sum s_j^4=S_2^2/2 and hence sum q_2(s_j)^2=S_2^2/6. Therefore

\[
 \|\mathcal H^{\rm bg}_{PP}\|
 \le40\sum_j\|v_j\|^2
 =40(1/3+S_2+S_2^2/6)<40(133/75).                            \tag{19}
\]

### Singular Hamiltonian Hessian

For real w and k>=1, differentiation of
atan w=(log(1+iw)-log(1-iw))/(2i) gives
|atan^(k)(w)|<=(k-1)!, since |1+-iw|>=1. Thus for
k(s)=-128 atan(U+Ws),

\[
 \|k^{(j)}\|\le128(j-1)!\,(1/64)^j\quad(j\ge1).             \tag{20}
\]

There is no explicit B dependence in k. Apply (12) to its fourth,
fifth and sixth derivatives. Only the B,D rows and columns of EE
are nonzero. Its Frobenius norm is <1.

Put l(s)=-128 atan'(U+Ws). Its first three derivative bounds are
t_1=128/64, t_2=256/64^2, t_3=768/64^3. The only nonzero entries
of the singular EP block have absolute bounds

\[
 |(B,U)|\le t_2+rt_3/2,\quad |(D,U)|\le t_3/2,
\]
\[
 |(B,W)|\le2t_1+(5r/2)t_2+(r^2/2)t_3,\quad
 |(D,W)|\le3t_2/2+rt_3/2.                                  \tag{21}
\]

Indeed its U derivative is l, its W derivative s l, and the
same product differentiations used for (17) apply. These four
entries have squared sum <25, giving operator norm <5.

For PP the exact Hessian is

\[
 256\sum_j{w_j\over(1+w_j^2)^2}
 (0,1,s_j)^T(0,1,s_j),\qquad w_j=U+Ws_j.
\]

C467f's secant estimate gives |w_j|<1/16. Its norm is consequently
<256(1/16)(3+6/5)=336/5. Together with (18),(19),(20),(21) this
establishes, along every whole-horizon actual trajectory,

\[
 \|\mathcal H_{EE}\|<211,\qquad
 \|\mathcal H_{EP}\|=\|\mathcal H_{PE}\|<392,\qquad
 \|\mathcal H_{PP}\|<2072/15<139.                            \tag{22}
\]

### Riccati continuation proves the projection, without assuming it

Fix one distinct initial u. Along its already established trajectory,
solve the real matrix ODE

\[
 R'=-\mathcal H_{EE}-\mathcal H_{EP}R-R\mathcal H_{PE}
                         -R\mathcal H_{PP}R,\qquad R(0)=0.   \tag{23}
\]

The coefficients are continuous on [0,T_0]; the right side is
locally Lipschitz in R. Local existence and uniqueness apply.
Symmetry is preserved by (23) and uniqueness. While ||R||<=1/5,
submultiplicativity and (22) give

\[
 \|R'\|\le211+2(392)/5+139/25=9334/25<384.                   \tag{24}
\]

Integration from R(0)=0 bounds ||R(t)|| by (9334/25)t.
This is at most 4667/24000<1/5 for t<=T_0, so a first contact
with the boundary ||R||=1/5 is impossible. Nor can the matrix
solution cease beforehand: it remains bounded and the continuous
coefficient functions are defined on the compact interval, so the
usual continuation theorem extends it. Thus (23) exists throughout
the horizon and satisfies (1)'s norm bound.

Now solve

\[
 V'=(\mathcal H_{PE}+\mathcal H_{PP}R)V,\qquad V(0)=I.
\]

The fundamental-matrix theorem gives V invertible, with positive
determinant by continuity from I. Set W_1=RV. Substitution of
(23) shows

\[
 V'=\mathcal H_{PE}V+\mathcal H_{PP}W_1,\qquad
 W_1'=-\mathcal H_{EE}V-\mathcal H_{EP}W_1,\quad
 (V(0),W_1(0))=(I,0).
\]

These are exactly the variational equations and initial data for
(A_t,N_t). Uniqueness of that linear system proves A_t=V,
N_t=W_1. In particular det A_t>0 and N_t A_t^-1=R. Projection
invertibility has been proved, rather than used to define (23).

### Complete coefficient and the remaining scope

Apply C467f(6)–(7) with (1). Its exact reconstruction includes the
positive determinant of the physical imaginary projection, the real
symmetric physical graph Hessian, and the full complex determinant.
It uses C467e's exact weight law, whose time-dependent multiplier is
positive and whose initial background phase has modulus <15/64.
Thus (2) follows for the stipulated three-variable orientation and
the original K_-. No action-only phase or modulus square replaces
the complex spatial determinant. This proves the local cone; audit1017
below checks the analytic specializations and the reconstruction.

The exact arithmetic reproduction command is
`python3 scripts/adjoint-flux/reverse-tangent-1015.py`.
Its certificate is `scripts/adjoint-flux/reverse-tangent-1015.json`.
All 11 comparisons pass, including the full entrywise Hessian
majorants and the strict 384 versus 9334/25 time budget. The script
verifies rational arithmetic only; the analytic derivative identities,
source applicability and continuation proof are supplied above, not
certified by numerical trajectories or a finite parameter sample.

Attempt1015 supplied the local uniform-cone target of ready1012;
audit1017 validates it below. It is a local conclusion beyond those
compared in that assessment, not certified originality. Reverse-current
construction and integrability, initial trace, payment and interfaces,
all-degree extension and actual-Xi transfer remain separate unproved
steps. Neither a full RH candidate nor an RH resolution is present.

### Independent conceptual audit — 15 November 2026, step1017

The invocation-start assessment nomination1015/completion1016 is
SPECIALIZE for this exact combined audit. C467e and C467f were checked
first in their canonical audit1017 sections. The original n=3, flat
metric, actual normalized B, arbitrary distinct initial triples and
fixed physical horizon are retained. This audit reproduces the local
argument and its constants; it neither asserts originality nor
imports a general phase-cone theorem.

**Physical scale and interpolation domain.** In (3), the factor
-128 is -2/L^2; the background is beta(Lz)/L^2. This follows from
the canonical one-form identity, so (4) evolves in physical time.
In particular phi''(z)=beta''(Lz) is bounded by 40 on |z|<2.
C467f's bounds imply (5). The stationary-product argument includes
the zero-product case and the entire compact centered circle, yielding
D^2<=S_2^3/54. On the whole real root interval q_2 ranges inside
[-S_2/3,S_2/3]. Its three nodal values sum to zero; their absolute
sum is twice the greatest modulus, giving (6). The interpolated
physical z lies in |Lz|^2<121/6400, so the scaled modulus is <11/10.
The derivative bounds in (7) are in the variable s: |z'|<101/100
and |z''|=2|W|<1/32. Cauchy applied to phi'' on complex disks
of radii tending to 9/10 gives exactly (8), with factorials (k-2)!.

**Confluent formulas and a valid local contour.** Use Carl de Boor,
*Divided Differences*, Surveys in Approximation Theory 1 (2005),
46–69, author version dated 21 December 2004,
[Section8, (41), Proposition43 and (44), pp60–61;
Section9, (49)–(52), in particular (51), p63 and (52), pp63–64](https://pages.cs.wisc.edu/~deboor/sat/papers/2/2.pdf).
For real C^5 functions, (44) bounds the order-five divided difference
at the six repeated real nodes by sup|l^(5)|/120. The functions here
are real analytic on a neighborhood of the interval; the order-two
and confluent bounds therefore apply to the required derivatives.
For example l=s^2 k' has five derivatives if k has six, exactly
as provided by (14). Real and imaginary components are taken as
real functions; no real mean-value point for a complex function is
asserted. Separating the repeated nodes is legitimate in this
neighborhood, and continuity returns the interval bound in the limit.

The disk condition in de Boor(51) is not silently enlarged. At each
fixed real coefficient point, compactness of the real interval and
the strict |z_+(s)|,|z_-(s)|<2 bounds provide a small complex
neighborhood where both composites are holomorphic. The arctangent
arguments likewise avoid their poles there. Choose a simple closed
contour in that neighborhood surrounding the interval. Q is nonzero
on it. On a sufficiently small complex parameter neighborhood it
remains nonzero there and its three roots stay inside, so the named
residue theorem and differentiation of this finite contour integral
apply. This is a local construction, not a common circle or a
uniform coefficient neighborhood. Conjugation symmetry gives the
holomorphic extensions of the real components specified after (10).

Holding k fixed while differentiating, Q_B=s and Q_D=-1 give
R_B k=-integral(s k'/Q) and R_D k=integral(k'/Q), with the common
factor 1/(2pi i). One further derivative gives precisely (10).
The denominator Q^2 has the six-node confluent multiset. Leibniz
differentiation gives (s^2 k')^(5)=s^2 k^(6)+10s k^(5)+20k^(4)
and (s k')^(5)=s k^(6)+5k^(5), confirming every term in (12).

**Every background block and the cancellation.** With E=(C,B,D),
the explicit z derivatives are z_C=i, z_B=eta=2W/3, z_D=0.
At fixed P, eta is constant. Consequently the six EE entries are
the six expressions listed after (15): the BB entry includes both
eta R_B psi terms, and CB includes T(eta Re phi''). Applying
(11)–(14) to them gives (15) exactly. The chain-rule coefficients
in f_4,f_5,f_6 and v_1,v_2,v_3 include all contributions of the
nonzero quadratic derivative z''; no third z derivative is present.

For EP, the explicit momentum derivatives z_M=1/3, z_U=-s and
z_W=q_2 give the displayed first row by nodal summation. The B,M
entry has eta T(Im phi'')/3 and R_B psi/3; D,M is R_D psi/3.
The B,U root term is [s psi+s^2 psi'], whose second derivative
divided by two is 2psi'+(5s/2)psi''+(s^2/2)psi'''. The D,U
term is -(3psi''+s psi''')/2. The D,W term is
3psi'+3s psi''+(q_2/2)psi'''. These give the corresponding
entries of (17), including explicit B dependence.

In the B,W entry, differentiating q_2 explicitly contributes
(2/3)T psi; it must not be omitted. Since T psi=[Q' psi] and
s q_2=D-(B/3)s at the nodes, subtracting [s(q_2 psi)'] gives
exactly (16). Its bound is
|B|v_2/3+|D|v_3/2+(|B|/3)(v_2+rv_3/2)
<= (2/5)v_2+(9/50)v_3. The remaining explicit term is
eta T(q_2 Im phi''), bounded using sum|q_2|<4/5.
This verifies the cancellation before using the majorant. Finally
the PP block is the stated sum of real rank-one matrices. Centering
gives sum q_2(s_j)^2=S_2^2/6, proving (19).

**Singular blocks and arithmetic.** The two logarithms defining
arctan give |atan^(k)(w)|<=(k-1)! for real w. Equations (12) and
(20) then bound its EE block. Its momentum derivatives are l and
s l, giving exactly the four EP entries in (21). Directly
differentiating twice in U,W gives the PP expression with positive
coefficient 256w/(1+w^2)^2, whose norm bound uses |w|<1/16.
The centered and tangent scripts were replayed: all 21 and 11 exact
comparisons passed. The full values for the tangent Hessian norm
checks are in `scripts/adjoint-flux/reverse-tangent-1015.json`,
reproduced by `python3 scripts/adjoint-flux/reverse-tangent-1015.py`.
They establish the strict norm majorants 211,392,139 and
9334/25<384 after the analytic entries have been justified above.
These are rational estimates, not a sampled trajectory certificate.

**Independent Riccati solve and original coefficient.** For each
fixed distinct u, C467e/f give a compact trajectory of distinct real
q and a smooth local coefficient chart along it. Smooth dependence
defines (A_t,N_t) in a neighborhood of this initial point; it does
not require a common neighborhood for all u. The Hessian coefficient
functions in (23) are continuous on the closed time interval. Solve
that ODE independently of A_t. Its norm-integral estimate up to a
first contact with 1/5 is (9334/25)t<=4667/24000<1/5. Thus contact
and finite-time blow-up are both excluded. This argument uses no
differentiation of a nonsmooth matrix norm or eigenvalue branch.
Symmetry follows by transposition and uniqueness.

For V'=(H_PE+H_PP R)V, fundamental-matrix invertibility gives
det V>0. Substituting W_1=RV cancels the R H_PE and R H_PP R
terms and yields exactly the Hamiltonian variational system with
initial data (I,0). Uniqueness identifies V=A_t and W_1=N_t.
This proves the projection and (1) without presupposing an inverse.

Now C467f's conditional reconstruction applies: det(D_uq)>0,
Z is real symmetric and det(J/i)=det(D_uq) det(I-iZ).
C467e's original weight law contributes a positive time multiplier
and e^(H_0-H(iu)); Delta(iu)^2=-Delta(u)^2 fixes the stipulated
minus sign in K_-. Hence the phase representative is the initial
background phase minus sum atan(lambda_j(Z)), bounded by
15/64+3(857/12800+133/375)=95951/64000<3/2<pi/2.
This validates the complete full-horizon cone uniformly over all
distinct initial triples, including arbitrarily small unequal spacings.
No claim is made at the diagonal itself. The audit passes all local
conclusions of C467e–g. It supplies no reverse-current integrability,
initial trace, payment, interfaces, all-degree theorem or actual-Xi
transfer, and there is no complete RH candidate.

## Mathlib

Full matching coverage for this actual-h Hamiltonian Hessian and
full-horizon reverse cone has not been checked. Supporting mathematics
is Cauchy's estimate, residue and divided-difference formulas, smooth
finite-dimensional ODE and variational theory, and matrix norm and
fundamental-matrix facts. No matching formalization, absence from
Mathlib, or formal verification of the cone is asserted.
