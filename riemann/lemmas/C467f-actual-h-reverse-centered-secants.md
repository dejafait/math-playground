# C467f — Full-horizon reverse secants in centered coordinates

## Hypotheses

Use the actual normalized B, x, beta, g, H, H_0, F, Y and K_- of
C467e, with n=3, R=1/4, a=1/16 and T_0=1/1920. In particular
beta(z)=B(1+z)-B(1)-xz, g=beta', g(0)=0, and the audited analytic
estimate of C466 is |g'|<40 on |z|<1/4. The initial triple u is
real, distinct, and belongs to (-a,a)^3. Time and parameter derivatives
are at fixed physical time for the stipulated raw reversed field.

Use C467e's survival, radial and Gram conclusions: tau_-(u)>T_0,
sum_j |Y_j|^2<3/160, physical noncollision, and reality of J*J for
J=D_uY, with det_C J nonzero through T_0. C467e's conceptual audit1017
validates these inputs. No forward barrier or current is used.
Keep C466a's external density qualifications if interpreting this
chart as a reciprocal-density chart; the estimates below need only
the stated analytic and reverse-flow inputs.

## Conclusion

Write Y_j=p_j+iq_j. All q_j remain distinct, with their initial
ordering, on 0<=t<=T_0. Set

\[
 c=\tfrac13\sum_jq_j,\quad r_j=q_j-c,\quad
 b=\sum_{j<k}r_jr_k=-\tfrac12\sum_jr_j^2,\quad d=r_1r_2r_3.
                                                               \tag{1}
\]

There are unique real m,U,V such that

\[
 p_j=m-U r_j+V(r_j^2+2b/3),\qquad m=\tfrac13\sum_jp_j.          \tag{2}
\]

Uniformly in every distinct initial triple and, for the strict
time-linear inequalities, every 0<t<=T_0,

\[
 |m|<1/600,\quad |r_j|<9/80,\quad |b|<3/320,
 \qquad |U|<75t\le5/128,\quad |V|<238t\le119/960.               \tag{3}
\]

For each pair j,k and remaining index l,

\[
 \frac{p_j-p_k}{q_j-q_k}=-U-Vr_l,
 \qquad
 \left|\frac{p_j-p_k}{q_j-q_k}\right|
 <\frac{4071}{76800}<\frac1{16}.                               \tag{4}
\]

At t=0 both momenta and all pair slopes vanish. These are complete
fixed-horizon trajectory/secant bounds, not a determinant phase cone.
They do not establish invertibility of u -> q(t,u).

Here is a quantitative sufficient condition for the remaining cone.
Put L=1/8 and introduce scaled canonical coordinates and momenta

\[
 E=(c/L,b/L^2,d/L^3),\qquad P=(3m/L,U,LV).
                                                               \tag{5}
\]

For each distinct initial triple, let A_t=D_{E^0}E_t and
N_t=D_{E^0}P_t denote derivatives of the centered coefficient flow,
with P_0=0. These are local derivatives in the initial coefficient
chart. If, throughout 0<=t<=T_0 for every such triple,

\[
 \det A_t\ne0,\qquad
 \|N_tA_t^{-1}\|_{\mathrm{op}}\le1/5,                          \tag{6}
\]

then the stipulated full K_- has a representative phase with

\[
 |\arg K_-|<95951/64000<3/2<\pi/2.                             \tag{7}
\]

Condition (6) is **not proved in this lemma**, whose phase assertion
is conditional. No current, trace, payment, interface identity,
all-degree positivity or Xi transfer follows. The independent
conceptual audit1017 below validates this partial result.

## Proof

### Source scope and purpose of the calculation

Reuse ready1012 and nomination1011/completion1012's source comparison
for this exact flow and complete coefficient. C467e supplies the
reversed Hamiltonian convention and its actual-B normalization. The
smooth local-flow, variation and compact-continuation tools are Gerald
Teschl, *Ordinary Differential Equations and Dynamical Systems*,
author-hosted April2012 preliminary version,
[Lemma2.14/Corollary2.15, pp52–53; Theorem3.9, p81; Theorem6.1 and
proof, pp189–190](https://www.mat.univie.ac.at/~gerald/ftp/book-ode/ode.pdf).
They apply only on a local smooth chart until its continuation is
justified below. Cauchy's derivative estimate and the divided-difference
mean-value theorem (a consequence of Rolle's theorem) are the standard
elementary analytic tools used here. No general reverse invariant-cone
theorem is being imported or reproved.

The inspected sources do not give these uniform centered estimates.
This is a development of the existing regularization for the same
assessed target, not a claim that the standard tools are new. In
particular (4) must not be substituted for the full tangent condition
(6). Originality of this local result is unverified.

### Centered canonical equations

Initially q=u is distinct. On any interval of distinct q, interpolation
by a quadratic gives (2), uniquely. Since sum r=0 and sum r^2=-2b,
averaging (2) gives the asserted formula for m. Also

\[
 \sum_jp_j\,dq_j=3m\,dc+U\,db+V\,dd.                          \tag{8}
\]

Indeed db=-sum r_j dr_j, while
d=(sum r_j^3)/3 implies dd=sum r_j^2 dr_j; terms proportional to
sum dr_j vanish. The map from q to (c,b,d) has Jacobian determinant
-Delta(q)/3. Thus it is a legitimate local coordinate change exactly
while the imaginary coordinates are distinct. It is not a projection
invertibility assertion for the time-t flow.

Let z(v)=m-Uv+V(v^2+2b/3)+i(c+v). Up to a chamber-dependent additive
constant, C467e's real Hamiltonian h=Im S in this chart is

\[
 \widetilde h(c,b,d;3m,U,V)
 =\sum_{j=1}^3\left\{-2\arctan(U+r_jV)
                          +\operatorname{Im}\beta(z(r_j))\right\}.
                                                               \tag{9}
\]

For the singular part, subtracting (2) gives the first identity (4);
the argument of a gap is pi/2+arctan(U+r_lV), modulo a constant
fixed by its ordering. The three pairs correspond to the three
remaining indices. The background in (9) is the actual beta, not
a polynomial replacement. The identity of one-forms (8) and
C467e's q'=h_p, p'=-h_q convention give, in particular,

\[
 U'=-\partial_b\widetilde h,\qquad
 V'=-\partial_d\widetilde h.                                  \tag{10}
\]

All partial derivatives in (10) hold c,m,U,V fixed. We estimate them
directly at real roots, without assuming a complex rectangular
coefficient box remains invariant.

### Uniform interpolation estimates

The singular forces cancel in the centroid. Hence

\[
 (m+ic)'=-\tfrac13\sum_j\overline{g(Y_j)},\qquad
 |(m+ic)'|\le40\sqrt{\tfrac13\sum_j|Y_j|^2}<40/\sqrt{160}.
\]

Since m(0)=0, |m(t)|<1/(48 sqrt(160))<1/600 through T_0.
For a centered real triple, r_j^2<=2 sum r_k^2/3; also
sum r_k^2<=sum q_k^2<3/160. It follows that
|r_j|<sqrt(1/80)<9/80 and |b|<3/320.

Temporarily impose the bootstrap bounds

\[
 |U|\le1/16,\qquad |V|\le1/4.                                 \tag{11}
\]

Let v range over the closed real interval between the extreme r_j.
Then c+v lies between the extreme q_j, and
|v^2+2b/3|<1/80. Thus, on the entire interpolation interval,

\[
 |\operatorname{Re}z(v)|
 <1/600+9/1280+1/320=227/19200<1/80,
\]
\[
 |z(v)|^2<1/6400+3/160=121/6400<(3/20)^2,
\]
\[
 |z'(v)|^2=1+(-U+2Vv)^2
 \le1+(19/160)^2<(101/100)^2,\qquad |z''(v)|\le1/2.             \tag{12}
\]

The analytic estimates therefore give |g(z(v))|<6 and |g'|<40.
Cauchy's estimate applied to g' on disks about z(v), of radii tending
to 1/10 inside |z|<1/4, gives |g''(z(v))|<=400. This uses the whole
complex-disk bound, not a real-axis estimate.

Put f(v)=Im beta(z(v)). Differentiating along this real interval,

\[
 |f''|\le |g'||z'|^2+|g||z''|
 <40(101/100)^2+3<44,
\]
\[
 |f'''|\le |g''||z'|^3+3|g'||z'||z''|
 \le400(101/100)^3+60(101/100)<475.                             \tag{13}
\]

For w(v)=U+vV, (11) gives |w|<29/320<1/10. With
alpha(v)=-2 arctan w(v), ordinary differentiation gives

\[
 |\alpha''|=\left|\frac{4V^2w}{(1+w^2)^2}\right|\le1/40,
\quad
 |\alpha'''|=\left|\frac{4V^3(1-3w^2)}{(1+w^2)^3}\right|
 \le1/16.                                                     \tag{14}
\]

### Divided differences remove the inverse gaps

The r_j are the three distinct real roots of Q(v)=v^3+bv-d.
Implicit differentiation gives
partial_b r_j=-r_j/Q'(r_j), partial_d r_j=1/Q'(r_j).
For any C^3 real function k on their interval,

\[
 \partial_b\sum_j k(r_j)=-[v k'(v)]_{r_1,r_2,r_3},\qquad
 \partial_d\sum_j k(r_j)=[k'(v)]_{r_1,r_2,r_3},                 \tag{15}
\]

when k has no explicit b,d dependence. The brackets denote the
second divided difference: [l] is sum_j l(r_j)/Q'(r_j).
The divided-difference mean-value theorem gives
|[l]|<=sup |l''|/2, regardless of how unequal or small the gaps are.
Consequently the two right sides in (15) have moduli bounded by

\[
 \sup|k''|+(9/160)\sup|k'''|,
 \qquad \tfrac12\sup|k'''|,                                  \tag{16}
\]

respectively. This applies to alpha and to f for the root-motion
parts of their derivatives. The sole additional explicit b dependence
of f is through z_b=2V/3; it contributes
(2V/3) sum_j Im g(z(r_j)), of modulus <3. There is no explicit
d dependence. Combining (13)–(16) with (10) yields

\[
 |U'|<44+(9/160)475+3+1/32=295/4<75,
\quad |V'|<475/2+1/32=7601/32<238.                            \tag{17}
\]

Here the singular b contribution was bounded by
1/40+9/2560=73/2560<1/32. No inverse gap occurs in (17).

### Closing the bootstrap and imaginary ordering

Fix any distinct initial u. At t=0 the momenta in (2) vanish. Work
until the first possible loss of distinct imaginary coordinates or
of (11), at or before T_0. Integration of (17) gives
|U|<75t<=5/128<1/16 and |V|<238t<=119/960<1/4, so neither momentum
can reach its bootstrap boundary. The same derivative bounds give
finite limits of U,V at a putative first imaginary collision.

If q_j-q_k tends to zero there, (2) and its bounded coefficients
force p_j-p_k=-(U+Vr_l)(q_j-q_k) to tend to zero too. This would
be a physical collision, excluded on the entire closed interval by
C467e. The original smooth physical solution extends past every
time under consideration. Thus neither type of first failure is
possible. This proves distinctness, preserved ordering and (3)
through T_0. Finally

\[
 |U+Vr_l|<5/128+(9/80)(119/960)
 =4071/76800<1/16,
\]

which proves (4). These bounds are independent of the initial gaps;
no uniform positive gap lower bound was assumed.

### What the full tangent estimate would still require

The remaining statement is conditional on (6). For fixed distinct
initial data the smooth coefficient flow and its derivatives exist
locally in the initial chart along this whole trajectory. No common
coefficient neighborhood or uniform derivative estimate is asserted.
If A_t is nonsingular at all the stated times, det A_t>0 by continuity
from A_0=I, and the inverse function theorem makes the evolved momentum
locally a graph P_hat(E). Its derivative is K=N_t A_t^{-1}.

Set q_hat=q/L, r_hat=r/L and let J_E=D_{q_hat}E. The canonical
identity gives p/L=J_E^T P_hat(E). Let C=I-11^T/3 be the orthogonal
projection onto centered triples. With Z=D_qp for this local graph,
differentiation gives

\[
 Z=-U C+2V C\operatorname{diag}(r)C+J_E^T K J_E.                \tag{18}
\]

Indeed the gradients of the three components of E are respectively
1/3, -r_hat_j, r_hat_j^2+2b/(3L^2); the corresponding Hessians are
0, -C and 2C diag(r_hat)C. For a centered three-vector,
sum r_hat_j^4=(sum r_hat_j^2)^2/2. This follows by squaring
sum r_hat_j r_hat_k=-sum r_hat_j^2/2 and using sum r_hat_j=0.
Writing S_2=sum r_hat_j^2<6/5, it follows exactly that

\[
 \|J_E\|_F^2=1/3+S_2+S_2^2/6<133/75.
\]

Hence (3),(18) imply

\[
 \|Z\|<857/12800+(133/75)\|K\|.                               \tag{19}
\]

The chain rule for the centered coefficient map gives
det(D_uq)=det A_t Delta(u)/Delta(q)>0; constant scaling factors
cancel, and the imaginary ordering was proved above. C467e's
Gram identity then makes Z real symmetric and gives the full factorization
det(J/i)=det(D_uq) det(I-iZ). In its exact weight law the other
time-dependent factor is positive and the initial background phase
has modulus <15/64. Thus, if ||K||<=1/5,

\[
 |\arg K_-|\le |H(iu)-H_0|+3\arctan\|Z\|
 <15/64+3\left(857/12800+133/375\right)
 =95951/64000<3/2<\pi/2.
\]

This proves the conditional implication only. Neither a small secant
bound nor an immersed Lagrangian plane ensures A_t is nonsingular or
bounds K. Those two tasks are the remaining quantitative bottleneck.

### Verification and qualification

The exact rational comparisons used above are replayed by
`python3 scripts/adjoint-flux/reverse-centered-1014.py`; its full
arithmetic certificate is
`scripts/adjoint-flux/reverse-centered-1014.json`.
It checks constants, not analytic hypotheses, continuation, or the
unproved condition (6). No numerical trajectory is used. Local progress
is the full-horizon secant estimate and the explicit tangent threshold.
Attempt1014 left the complete cone open; this lemma retains its
conditional role. The main RH gap remains open.

### Independent conceptual audit — 15 November 2026, step1017

This audit uses nomination1015/completion1016's prior SPECIALIZE
coverage and C467e/audit1017. It does not assume C467g's tangent bound
to prove ordering or to validate the conditional implication here.

For the real interpolation input use Carl de Boor, *Divided Differences*,
Surveys in Approximation Theory 1 (2005), 46–69, author version dated
21 December 2004, [Section8, Proposition43 and (44), pp60–61;
(41), p60](https://pages.cs.wisc.edu/~deboor/sat/papers/2/2.pdf).
The order-two mean-value bound applies to the real function l in (15)
on the closed interval of its three real nodes, with two continuous
derivatives. Here l=k' or v k', so the displayed C^3 bounds on k
suffice. The actual composite functions are real analytic on a
neighborhood of that interval. No complex-valued mean-value assertion
is used, and no lower spacing enters this theorem.

**Canonical coordinates and domain.** Quadratic interpolation at
distinct q gives (2) uniquely. Differentiating b and d under sum r=0
verifies (8) and the Jacobian -Delta(q)/3, so the equations (10) have
the correct canonical signs. The average singular force cancels
exactly. C467e's radial estimate therefore gives the centroid bound,
sum r_j^2<3/160 and r_j^2<1/80. For every v between the extreme
centered roots, 0<=v^2<=2 sum r_j^2/3. Hence
|v^2+2b/3|<=sum r_j^2/3<1/80 on the entire interval, while c+v
lies between extreme q_j. This proves all of (12) under (11),
including its complex-domain bound. Disks of radius approaching 1/10
about z(v) lie in |z|<1/4, so Cauchy's estimate genuinely gives
|g''|<=400. The chain rules for f'' and f''' then give (13).

**Explicit coefficient dependence and closure.** Holding c,m,U,V
fixed gives z_b=2V/3 and z_d=0. Thus the additional b derivative
of the background sum is exactly (2V/3) sum Im g(Y_j), of modulus
<3 under (11); omitting it would invalidate the bound. Root motion
contributes -[v k'] or [k'] because Q_b=v and Q_d=-1.
The de Boor bound yields (16) for the real functions alpha and f.
Direct differentiation of arctan gives (14); with |w|<1/10 its
third-derivative factor |1-3w^2|/(1+w^2)^3 is <=1. The resulting
upper bounds in (17) are 295/4<75 and 7601/32<238.

For each fixed distinct initial triple the momenta start at zero.
Those derivative bounds keep both strictly inside their bootstrap
rectangle until T_0 and give limits at a possible first imaginary
collision. Bounded coefficients in (2) would force a physical
collision there, contrary to C467e. Thus ordering is proved before
the tangent reconstruction is attempted. Arbitrarily small and unequal
initial gaps are covered; constants are independent of u.

**Conditional tangent reconstruction.** Scaling the canonical one-form
gives sum p_j dq_j=L^2 sum P_k dE_k exactly. The gradients and
Hessians of E with respect to q/L are those stated before (19).
The cubic centered identity gives sum r_hat_j^4=S_2^2/2, and hence
||J_E||_F^2=1/3+S_2+S_2^2/6<133/75. Differentiation of p/L=J_E^T
P_hat yields (18) in physical variables: the explicit quadratic
term is 2V C diag(r) C, with no missing L factor. Thus (19) has
offset 5/128+2(9/80)(119/960)=857/12800. Under (6), continuity
gives det A_t>0 from A_0=I; the coefficient Jacobian ratio then
gives positive det(D_uq). Gram reality makes Z symmetric after this
invertibility has been established. The original full determinant
is det(D_uq) det(I-iZ), including its orientation. Combining the
initial phase <15/64 with 3 arctan||Z|| proves exactly (7).

All 21 rational comparisons in `scripts/adjoint-flux/reverse-centered-1014.py` were replayed
and their complete check values inspected in
`scripts/adjoint-flux/reverse-centered-1014.json`. This verifies constants;
the analytic and continuation justifications are the audit above.
The ordering, secant estimates and conditional implication pass.
Projection invertibility remains a separate premise within this lemma;
it is not inferred from small secants or immersion.

## Mathlib

Full matching coverage for this centered actual-h reverse-flow estimate
has not been checked. Supporting results are Cauchy's derivative
estimate, the real divided-difference mean-value theorem, finite-dimensional
smooth ODE theory, the inverse function theorem and real symmetric
spectral theory. No absence claim or formal verification is asserted.
