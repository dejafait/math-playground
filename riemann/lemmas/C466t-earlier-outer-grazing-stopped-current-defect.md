# C466t — Earlier outer grazing produces a stopped-current defect

## Hypotheses

Use C466s's unit flat raw flow and first maximal lifetime in
U=B minus {q=0}, with B={|q|<R,|z|<L}. Set

\[
 R=5,\quad a=4,\quad L=3\sqrt5,\quad b=13/2,\quad T_0=2,
 \qquad H(q,z)=z^2/2-(7+8i)z.                              \tag{1}
\]

Here I=(-a,a) times (-b,b), Q=(0,2) times I and
X(0,r,s)=(ir,s). These are admissible C466s data: H_0=0,
M_1=L+sqrt113 and M_2=1 suffice. The gradient is (0,z-7-8i),
and the complex Hessian is diag(0,1). In particular 0<b<L
because (13/2)^2=169/4<45.

Let D_H consist of r!=0 and t<tau(r,s) in Q, and let Psi=X on
D_H only. For a smooth compactly supported ambient scalar chi on B put

\[
 F=q^2e^{-H},\quad \Omega=F\,dq\wedge dz,\quad
 \beta_\chi=\Psi^*(\chi\Omega),\quad
 \gamma_\chi=\Psi^*(d\chi\wedge\Omega).                   \tag{2}
\]

Bars mean coefficientwise zero extension from D_H to Q,
including at r=0. Parameter-space orientation is dt wedge dr wedge ds.
There is no continuation of the raw stopped map through an exit.

## Conclusion

There exists real chi in C_c^infinity(B), equal to1 on a compact
neighborhood of the comparison images specified below, for which
both complete zero-extended forms have bounded measurable coefficients
on Q, but

\[
 d\bar\beta_\chi\ne\bar\gamma_\chi
 \quad\hbox{as distributions on }Q.                       \tag{3}
\]

More precisely, on the open box

\[
 O=(\log(49/10),\log(51/10))
       \times(29/10,31/10)\times(6-10^{-4},6+10^{-4}),       \tag{4}
\]

one has bar(gamma_chi)=0 and

\[
 d\bar\beta_\chi
 =\delta_{s=6} A(t,r)\,dt\wedge dr\wedge ds,\qquad
 A(t,r)=F(\widetilde\Psi(t,r,6))q_r(t,r)z_t(t,6)\ne0.       \tag{5}
\]

The tilde denotes only an explicit smooth comparison solution used
to compute one-sided values, not a new definition of the killed flow.
The defect comes from the shadow of an earlier outer-boundary grazing.
The example refutes the exact all-stopped-events localized identity
in assessment960. It does not refute an identity with additional
no-prior-escape hypotheses, a collision-only identity, C466s's
absolute-density bound, or RH. This result is an explicit obstruction
under the assessed EXPLORE scope; originality is unestablished.
Independent conceptual audit963 below validates this exact scope.

## Proof

### Explicit raw solutions and the earlier stop

Because H is independent of q, while the trajectory survives one has

\[
 q(t,r)=i\,\operatorname{sgn}(r)\sqrt{r^2-4t},\qquad
 z(t,s)=7+(s-7)e^t+8i(1-e^{-t}).                            \tag{6}
\]

Indeed dot q=-2/bar q and dot z=bar z-7+8i; the displayed
initial conditions and derivatives verify these equations. The q
formula applies for t<r^2/4. It decreases |q| from |r|<a<R,
so there is no q outer exit. Formula (6) agrees with the unique
smooth raw solution up to its first q collision or z outer hit.
It also defines a comparison map tilde(Psi) wherever its square
root is positive, even when an earlier z exit has killed the raw
trajectory. H happens to be entire in this example; using the
explicit formula for comparison does not extend the stopped map.

Write E=e^t and

\[
 N(E,s)=|z(t,s)|^2=[7+(s-7)E]^2+64(1-E^{-1})^2.
\]

At s=6 direct multiplication gives the exact identity

\[
 N(E,6)-45=
 \frac{(E-4)^2(E^2-6E+4)}{E^2}.                            \tag{7}
\]

For 1<=E<=51/10, E^2-6E+4=(E-3)^2-5<0, since
max{(1-3)^2,(51/10-3)^2}=441/100<5.
Consequently N(E,6)<45 except at E=4, where it equals45.
This trajectory starts at |z|=6<L, first touches |z|=L at
t_*=log4 and would be strictly inside again for 4<E<=51/10.
The raw trajectory nevertheless stops at that first touch.

For |s-6|<=10^{-4} throughout 1<=E<=51/10,

\[
 \partial_sN(E,s)=2E[7-E+E(s-6)]>0,                         \tag{8}
\]

because the bracket is at least 19/10-51/100000>0. Hence if
s<6 the entire z path through any time in O stays strictly inside
|z|<L, by (7)-(8). If s>6, its initial value satisfies
|s|<b<L but

\[
 N(4,s)=(3+4(s-6))^2+36>45.
\]

It therefore reaches the outer boundary strictly before log4.
For s=6 its first hit is exactly log4. No regularity of the
lifetime function or of a general hitting surface is inferred.

The closure of O lies in Q. In particular log(51/10)<2, as
e^2>1+2+2+8/6>51/10, and r^2-4t>41/100 on that closure.
Thus q has not collided at any of these times, for any r in O,
and had no earlier q outer exit. Combining this with the preceding
z comparison proves the exact local survivor description

\[
 D_H\cap O=O\cap\{s<6\}.                                 \tag{9}
\]

### Current localization does not remove the earlier stop

All comparison images of the closure of O are strictly inside B.
For completeness this strict statement also holds on the killed
side. For 49/10<=E<=51/10, (7) gives

\[
 N(E,6)-45\le-\frac{4779}{260100}<-1/100.
\]

Here (E-4)^2>=81/100, E^2-6E+4<=-59/100 and
E^2<=2601/100. Perturbing s within10^{-4} changes N by at most

\[
 2(51/10)(21/10)10^{-4}+(51/10)^2 10^{-8}<3/1000.
\]

Therefore N(E,s)<45-7/1000 on the whole closed box. Also
|q|<=31/10<5 there. The image K=tilde(Psi)(closure O) is
compact in B. The standard smooth bump-function theorem for a
compact subset of an open Euclidean set supplies a real chi in
C_c^infinity(B) equal to1 on an open neighborhood of K.

On O let b_0=tilde(Psi)^*Omega, a smooth complex two-form.
Holomorphy gives dOmega=0: dF is a linear combination of dq,dz,
so dF wedge dq wedge dz=0. Smooth pullback commutes with d, hence
db_0=0. By (9) and chi=1 near K the actual zero extensions satisfy

\[
 \bar\beta_\chi=\mathbf1_{s<6}b_0,\qquad
 \bar\gamma_\chi=0\quad\hbox{on }O.                        \tag{10}
\]

This is the point at which current-position localization fails to
remove the past boundary event. There is no gamma contribution
here that could cancel that event.

### Complete coefficients and integrability

The following bounds also show that (3) is a well-defined
distributional failure rather than a nonintegrability claim.
On every survivor in Q put v=sqrt(r^2-4t), so 0<v<=|r|<a.
The derivatives of (6), for either sign of r, satisfy

\[
 q_r=i|r|/v,\quad q_t=-2i\operatorname{sgn}(r)/v,\quad
 q_s=z_r=0,\quad z_s=e^t,\quad
 |z_t|\le Z:=(b+7)e^2+8.                                   \tag{11}
\]

The elementary bound |H(z)|<=L^2/2+sqrt113 L on |z|<L yields
|F|<=C v^2, with C=exp(L^2/2+sqrt113 L). Let C_0=sup|chi|
and C_1=sup||dchi||, finite by compact support. Expanding all three
coefficients of beta in the order dt wedge dr, dt wedge ds,
dr wedge ds gives

\[
 (\beta_\chi)_{tr}=-\chi Fq_rz_t,\quad
 (\beta_\chi)_{ts}=\chi Fq_tz_s,\quad
 (\beta_\chi)_{rs}=\chi Fq_rz_s.                            \tag{12}
\]

Their absolute values are respectively at most

\[
 C_0CZr^2,\qquad 2C_0Ce^2|r|,\qquad C_0Ce^2r^2.             \tag{13}
\]

For any real tangent vectors u,v the complex determinant bound
|dq wedge dz(u,v)|<=||u||||v|| follows from the Hermitian
Gram identity (also used in C466s). Expanding dchi wedge Omega
in three terms therefore bounds its value on three real vectors
by 3C_1|F| times their norm product. Applying this to
tilde(Psi)_t, tilde(Psi)_r, tilde(Psi)_s and using (11) gives

\[
 |(\gamma_\chi)_{trs}|
 \le3C_1Ce^2|r|(2+Zv)
 \le3C_1Ce^2a(2+Za).                                      \tag{14}
\]

These are uniform finite bounds on every survivor; the stipulated
zero values preserve them elsewhere. The survivor domain is open
and its flow smooth as in C466s, so each zero-extended coefficient
is Borel measurable. Thus all complete coefficients are in
L^infinity(Q), in particular L1_loc(Q). No derivative is taken
of a classically continued killed map.

### A nonzero compact distributional test

One-dimensional integration by parts in s gives
partial_s1_{s<6}=-delta_{s=6}. Applying this identity coefficientwise
to the smooth b_0 in (10), with db_0=0, yields

\[
 d\bar\beta_\chi
 =-\delta_{s=6}\,ds\wedge b_0
 =\delta_{s=6}Fq_rz_t\,dt\wedge dr\wedge ds.                \tag{15}
\]

The sign is explicit: (b_0)_{tr}=-Fq_rz_t by (12), and
ds wedge dt wedge dr=dt wedge dr wedge ds. Equivalently the
coefficient of d beta is partial_t beta_rs minus partial_r beta_ts
plus partial_s beta_tr, giving the same positive coefficient in
(15). This elementary computation justifies the jump formula;
no homogeneous removability theorem is invoked for this
inhomogeneous question.

At s=6, z_t=-e^t+8ie^{-t} is nonzero. Also q_r!=0, q!=0 and
e^{-H}!=0 on O. Thus A(t,r) in (5) is nonzero everywhere on
the indicated (t,r) box. To exhibit a scalar compact test without
any cancellation assumption, let t_1=log5, r_1=3 and
A_0=A(t_1,r_1)!=0. Continuity gives a smaller product neighborhood
J_t times J_r of (t_1,r_1) within the box on which

\[
 \Re\left(\frac{\bar A_0}{|A_0|}A(t,r)\right)>|A_0|/2.
\]

Choose nonnegative nonzero smooth bumps u,v supported in J_t,J_r,
and a nonnegative smooth bump w supported in (6-10^{-4},6+10^{-4})
with w(6)=1. The real scalar test phi(t,r,s)=u(t)v(r)w(s) is
compactly supported in Q. Pairing (15) with phi gives
integral A(t,r)u(t)v(r) dt dr. After multiplication by
bar(A_0)/|A_0| its real part is strictly positive. It is therefore
nonzero, whereas bar(gamma_chi) pairs to zero by (10). This proves
(3) and (5), including a full distributional witness.

### Scope and source qualification

The local review in assessment960 explicitly allowed a nonzero
defect from any stopped event and warned that an earlier outer
escape cannot be suppressed solely by current-position chi. The
present exact example realizes that alternative; it is more than
failure of an envelope or cutoff construction. The imported
background is the C466s flow convention and smooth survivor domain,
the named standard uniqueness and bump-function theorems, and
smooth pullback/exterior differentiation. The explicit specialization
and integration-by-parts computation above are necessary because
no exact source import for the proposed stopped identity was found
in review960. No broader novelty claim follows from that search.

This defect occurs with q bounded away from zero on the test support.
It does not decide whether a purely collisional stopped-current
identity holds when prior outer exits are excluded. It also does
not show a sign for any actual-Xi determinant or supply global
homology, metric normalization, divisor-intersection control or
endpoint accounting. C466s's absolute result remains intact.

### Independent conceptual audit963 — 14 November 2026

This audit uses the unchanged EXPLORE assessment961, separately
approved in review962. It checks the complete claimed counterexample,
not just the later comparison path or a coefficient preview. The
result passes without changing its hypotheses or mathematical proof.
The only local mathematical input remains C466s's setup and smooth
survivor-domain construction. No general extension theorem is applied.

**Admissibility and raw flow.** The polynomial H is holomorphic on
the whole bidisk, H(0,0)=0, and its only nonzero gradient component
is z-(7+8i). Since |7+8i|=sqrt113, M_1=L+sqrt113 bounds the
Hermitian gradient norm; diag(0,1) has operator norm1. Also
0<4<5 and 0<13/2<sqrt45. These are precisely C466s's data,
with the unit physical-time vector field, not a modified metric.

For either nonzero sign of r, differentiating (6) gives
q_t=-2i sgn(r)/v=-2/bar q and q_r=i|r|/v, where
v=sqrt(r^2-4t)>0. Writing z=x+iy gives x'=x-7 and y'=8-y,
which checks both real components of z'=bar z-7+8i and the
initial value s. Smooth ODE uniqueness therefore identifies this
formula with the raw map exactly until its first boundary event.
The q modulus decreases, so no q outer hit has been overlooked.
A tangential z hit still ends the maximal interval in the open
set U: an interval continuing beyond the hit would contain a time
whose value is outside U. Smoothness of the comparison formula
does not change this definition.

**Complete earlier path and exact survival.** Multiplying
E^2(N(E,6)-45) independently yields

\[
 E^4-14E^3+68E^2-128E+64
   =(E-4)^2(E^2-6E+4).
\]

On the whole interval [1,51/10], (E-3)^2<=441/100<5.
The quadratic factor is consequently strictly negative there,
so the only boundary equality is E=4. Moreover
7-E+E(s-6)>=19/10-51/100000>0 throughout the stated
s interval. Thus monotonicity in s compares the whole earlier
path, including E=4, not just its endpoint. For s<6 it is
strictly interior throughout. For s>6, N(1,s)=s^2<45,
whereas N(4,s)>45; continuity forces an earlier boundary hit.
For s=6 the first hit is exactly log4.

The time upper endpoint obeys log(51/10)<2 because
e^2>1+2+2+8/6>51/10. On the closed box,
r^2-4t>(29/10)^2-8=41/100. Hence none of these paths has
an earlier q collision. This proves (9) with all possible stopping
events checked; it does not require continuity of tau.

**Compact current-position cutoff.** On [49/10,51/10],
(E-4)^2>=81/100, -(E^2-6E+4)>=59/100, and
E^2<=2601/100. Therefore (7) is at most -4779/260100,
strictly less than -1/100. The exact perturbation is
2(7-E)E(s-6)+E^2(s-6)^2. Its absolute value is bounded by
the expression in the proof, which is <3/1000. Thus the
strict margin N(E,s)<45-7/1000 holds on the entire closed
box, including s>=6. Together with |q|<=31/10<5 and the
positive radicand, this makes K a compact subset of B. The
smooth bump-function theorem applies with chi=1 on an open
neighborhood of K, so dchi=0 there. It localizes the comparison
positions but cannot revive a killed raw path.

**All complete coefficients on Q.** The audit checks all three
coefficients in (12), not only the fixed-time dr wedge ds term.
On any survivor, v<=|r|<a, e^t<=e^2 and |z_t|<=Z.
The estimate |H|<=L^2/2+sqrt113 L gives
|F|<=Cv^2. Consequently the three products before the last
simplification in (13) are bounded by
C_0CZ|r|v, 2C_0Ce^2v and C_0Ce^2|r|v, respectively.
These imply exactly (13), for either sign of r and arbitrarily
near collision.

For gamma, the real tangent norms are

\[
 \|\widetilde\Psi_t\|\le2/v+Z,\qquad
 \|\widetilde\Psi_r\|=|r|/v,\qquad
 \|\widetilde\Psi_s\|=e^t.
\]

The three-term alternating expansion of dchi wedge Omega,
with the complex determinant inequality, is bounded by their
product times 3C_1Cv^2. This is
3C_1Ce^2|r|(2+Zv), as in (14), so no additional singular
time minor has been suppressed. Smoothness on the open survivor
domain makes each coefficient continuous there. Its zero extension
to the Borel complement, including r=0, is measurable. The bounds
are finite uniformly on all Q; because Q has finite measure,
the coefficients are also in L1(Q), stronger than the L1_loc
needed to define their distributions. No trace theorem follows
from this integrability statement.

**Distribution orientation and a genuine test.** On a neighborhood
of the closed box the comparison map is smooth. Holomorphy makes
dOmega=0 as an ordinary complex-valued real form. Therefore
db_0=0, while the actual extensions on O are precisely (10).
For the orientation dt wedge dr wedge ds, the derivative coefficient
is partial_t beta_rs-partial_r beta_ts+partial_s beta_tr.
The derivative of the indicator is -delta_{s=6}; multiplying its
jump by beta_tr=-Fq_rz_t gives the positive coefficient A in (15).
The other two coordinate derivatives do not differentiate the
indicator. This verifies the sign without a convention for a
general survivor-boundary normal.

On s=6, z_t=-E+8i/E is nonzero, q_r is nonzero, and F is
nonzero because v>0. In particular A_0 at (log5,3) is nonzero.
Continuity provides the asserted strict positive rotated real part
on a smaller product neighborhood. Nonnegative nonzero bumps u,v
have positive integrals; w(6)=1. Thus the rotated real part of
the scalar pairing is greater than
(|A_0|/2)(integral u)(integral v)>0. The test is supported
strictly inside O, so no contribution elsewhere in Q can cancel it.
The gamma pairing is zero because dchi vanishes on K. This proves
an actual distributional inequality, not merely a nonzero pointwise
coefficient or a failure of one cutoff method.

**Verdict and limits.** Stop961 is retained as an audited obstruction
to the exact universal all-stopped-events identity. No correction,
new lemma, numerical evidence or mathematical script was needed.
This is independent verification of a previously written local
negative, not a discovery beyond the sources assessed. The counterexample
does not involve q=0 on the witness support and does not settle a
collision-only identity with earlier outer events excluded. C466s's
absolute bound, actual-Xi signs, global homology and endpoint payment
are unaffected. No RH candidate is claimed. The proof and its direct
mathematical inputs are unchanged, so the DAG requires no new edge.

## Mathlib

Full matching coverage of this explicit killed-flow counterexample
and stopped-current defect has not been checked. Supporting ordinary
calculus, smooth bump functions and distributional integration by
parts have not been mapped to exact Mathlib names in this step.
Unknown availability is not evidence of absence. The proof above
is informal and exact; no numerical certificate or formalization
is substituted for the complete compact test. Audit963 did not change
the Mathlib coverage status or claim a machine-checked proof.
