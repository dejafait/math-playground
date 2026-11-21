# C467h — Reverse actual-h spatial majorant and initial L1 trace

## Hypotheses

Use the actual normalized logarithm and raw reversed flow of C467e:

\[
 n=3,\quad R=1/4,\quad a=1/16,\quad T_0=1/1920,
 \quad I=(-a,a)^3,\quad I^*=\{u\in I:\Delta(u)\ne0\},
\]
\[
 x=B'(1),\quad \beta(z)=B(1+z)-B(1)-xz,\quad g=\beta',
 \quad H_0=3(B(1)-x)\in\mathbb R,
\]
\[
 H(z)=H_0+\sum_j\beta(z_j),\quad
 F(z)=\Delta(z)^2e^{-H(z)},\quad
 \Delta(z)=\prod_{j<k}(z_k-z_j),
\]
\[
 Y_j'=2\sum_{k\ne j}\frac{Y_j-Y_k}{|Y_j-Y_k|^2}
                  -\overline{g(Y_j)},\qquad Y(0,u)=iu.
                                                               \tag{1}
\]

Here exp B(w)=xi(1/2+sqrt(w))/xi(1/2), with B(1) real,
and |beta''|<40 on |z|<R. These are C467e's established inputs
from C466z/audit988 and C466/audit993. Use the audited survival and
radial conclusion of C467e, ordering and reconstruction of C467f,
and full-horizon coefficient variation bounds of C467g/audit1017.
All parameter derivatives are at fixed original physical time, with
the original flat metric. In particular no time reparameterization,
metric change, divided weight or modified flow is allowed.

Retain C466a's external critical-strip, symmetry, paired-product,
counting and verified-low-zero qualifications if interpreting this
analytic chart as a reciprocal-density chart. No density construction,
forward-current theorem, RH or all-degree positivity is assumed here.

## Conclusion

For u in I* and 0<=t<=T_0 define the original spatial coefficient

\[
 \mathcal A(t,u)=F(Y(t,u))\det_{\mathbb C}(D_uY(t,u)/i).
                                                               \tag{2}
\]

Give it value zero on I\I*. It is jointly measurable on [0,T_0] x I,
and the single integrable majorant

\[
 G(u)=e^{-H_0}|\Delta(u)|,\qquad
 |\mathcal A(t,u)|\le G(u),\qquad
 \int_I G\,du\le 2^{-18}e^{-H_0}                              \tag{3}
\]

works at every time, uniformly over arbitrarily small unequal initial
gaps. With completed Lebesgue measure on I,

\[
 \lim_{t\downarrow0}\|\mathcal A(t,\cdot)-F(i\,\cdot)\|_{L^1(I)}=0.
                                                               \tag{4}
\]

This is one local spatial trace input, validated by the independent
conceptual audit1021 below. It establishes no smooth diagonal extension, bound on the
normalized K_-, spacetime minors/current, interface or payment identity,
global signed assembly, all-degree result or actual-Xi transfer.

## Proof

### Assessed tools and exact scope

The invocation-start SPECIALIZE assessment is
`drafts/literature/2026-11-15-reverse-pullback-l1-trace-nomination-1017.md`,
completed in review1018. It covers exactly (3)-(4). Its primary-source,
duplicate and failure comparisons are reused: forward damping does
not apply to (1); stop948 does not make smooth collision-divided
extension necessary; stop1009 concerns a different prescribed forward
flow/cap/family. None proves or refutes this reverse spatial target.

Import smooth dependence on the nonsingular domain and the linear
variational theory from Gerald Teschl, *Ordinary Differential Equations
and Dynamical Systems*, author-hosted April2012 preliminary version,
[Lemma2.14/Corollary2.15, pp52-53; Theorem3.9, p81;
Lemma3.11, (3.91), p83; Theorem6.1, pp189-190](https://www.mat.univie.ac.at/~gerald/ftp/book-ode/ode.pdf).
In particular Lemma3.11 is the Abel-Liouville determinant formula for
a linear system with continuous coefficients. Import dominated
convergence from John K. Hunter, *Measure Theory*, undated author-hosted
chapter, [Chapter4, Theorem4.24 and Section4.6, printed pp49-50](https://www.math.ucdavis.edu/~hunter/measure_theory/measure_notes_ch4.pdf#page=11).
Apply it below to nonnegative absolute differences; no new ODE or
integration theorem is reproved.

The root/coefficient identity is already specialized in C467f. The
supporting primary identity compared in review1018 is Athreya, Bufetov,
Eskin and Mirzakhani, *Lattice Point Asymptotics and Volume Growth on
Teichmuller Space*, author version dated 17September2011,
[AppendixA, (A.5), printed p40](https://www.math.uchicago.edu/~eskin/final_final.pdf#page=40).
Its coefficient convention is not substituted for the centered/scaled
one here. We check the scaling through C467f's exact formula below.
The work beyond citation is the original weight times complete
determinant cancellation. This is a specialization of assessed tools
and audited local inputs, without a claim of originality.

### Uniform coefficient determinant

Fix any u in I*. Write Y=p+iq and use C467f's centered coordinates
c,r,b,d,m,U,V and C467g's scale L=1/8:

\[
 E=(c/L,b/L^2,d/L^3),\quad P=(3m/L,U,LV),\quad
 \mathsf M=D_{E^0}E_t,\quad \mathsf N=D_{E^0}P_t,
 \quad \mathsf R=\mathsf N\mathsf M^{-1}.
\]

The letter mathsf M here denotes C467g's A_t, not a bound on beta''.
C467g proves det mathsf M>0, ||mathsf R||<=1/5, and the exact
fixed-physical-time variational equation

\[
 \mathsf M'=(\mathcal H_{PE}+\mathcal H_{PP}\mathsf R)\mathsf M,
 \qquad \mathsf M(0)=I_3,
 \qquad \|\mathcal H_{PE}\|<392,\quad
 \|\mathcal H_{PP}\|<139.                                  \tag{5}
\]

For this fixed u the coefficients are continuous on the whole compact
time interval. Thus the cited determinant formula applies. For a real
3 by 3 matrix T, |tr T|<=3||T||, by evaluating on an orthonormal
basis. Equation (5) gives

\[
 0<\det\mathsf M(t)
 =\exp\!\int_0^t\operatorname{tr}
       (\mathcal H_{PE}+\mathcal H_{PP}\mathsf R)\,ds
 \le \exp(6297t/5)
 \le \exp(2099/3200)<3.                                    \tag{6}
\]

The last inequality follows from 2099/3200<2/3 and
e^v<=1/(1-v) for 0<=v<1, which follows by comparison of the
power series. All constants are independent of u. No common initial
distance from the divisor or common coefficient neighborhood is used.

### Complete determinant and weight compensation

C467f-g give distinct q_j in their initial ordering. The local graph
p=p(q) has real symmetric matrix Z=D_qp, with

\[
 \|Z\|<857/12800+(133/75)\|\mathsf R\|
 \le80951/192000<1/2.                                      \tag{7}
\]

Symmetry here is part of the audited full reconstruction, not a
consequence of small pair slopes. For Q=D_uq the chain rule gives
D_uY=(Z+iI_3)Q. The coefficient map has determinant
det(D_qE)=-Delta(q)/(3L^6). Its initial determinant is the same
expression with u in place of q. Therefore, exactly,

\[
 \det Q=\det\mathsf M\frac{\Delta(u)}{\Delta(q)}>0,
 \qquad
 \det_{\mathbb C}(D_uY/i)=\det Q\det_{\mathbb C}(I_3-iZ).
                                                               \tag{8}
\]

This checks both the scaling cancellation and the original orientation;
it uses only local distinct-root charts, without global injectivity.
For each pair j<k let l be its remaining index and put w_l=U+Vr_l.
C467f gives

\[
 Y_k-Y_j=(q_k-q_j)(i-w_l),\qquad |w_l|<1/16.                \tag{9}
\]

Each remaining index appears once among the three pairs. Substitution
of (8)-(9) into the original complex expression (2) yields the exact
identity

\[
 \mathcal A=e^{-H(Y)}\det\mathsf M\,\Delta(u)\Delta(q)
       \prod_{l=1}^3(i-w_l)^2\det_{\mathbb C}(I_3-iZ).        \tag{10}
\]

Only now take absolute values:

\[
 |\mathcal A|=e^{-\operatorname{Re}H(Y)}\det\mathsf M
       |\Delta(u)\Delta(q)|\prod_l(1+w_l^2)
       |\det_{\mathbb C}(I_3-iZ)|.                           \tag{11}
\]

In particular no full determinant factor is discarded, and no algebraic
square in the integrand has been replaced by a modulus square. The
latter appears only in this absolute bound. The sole inverse
Vandermonde in (8) has canceled one of the original weight's two
Vandermonde factors.

C467e gives sum_j |Y_j|^2<3/160. Its background estimate gives
|H(Y)-H_0|<3/8, so

\[
 e^{-\operatorname{Re}H(Y)}\le e^{-H_0+3/8}
                      \le(8/5)e^{-H_0}.                    \tag{12}
\]

For each real gap,
|q_k-q_j|^2<=2(q_k^2+q_j^2)<=2 sum |Y_j|^2<3/80<1/25.
Consequently |Delta(q)|<1/125. Also
prod_l(1+w_l^2)<(257/256)^3<(5/4)^3<2. Finally the real
symmetric Z has three real eigenvalues of modulus <1/2, hence

\[
 |\det_{\mathbb C}(I_3-iZ)|
 =\prod_{j=1}^3\sqrt{1+\lambda_j(Z)^2}
 <(5/4)^{3/2}<2.                                           \tag{13}
\]

Combining (6),(11)-(13) gives the slightly stronger bound

\[
 |\mathcal A(t,u)|\le {96\over625}e^{-H_0}|\Delta(u)|
                         \le G(u),                         \tag{14}
\]

since (8/5)*3*(1/125)*2*2=96/625<1. These bounds include t=0
and t=T_0 and every distinct initial triple. On I, each initial
gap has modulus <=2a=1/8; therefore |Delta(u)|<=2^-9. The
volume of I is also 2^-9, proving the integrability bound in (3).

### Measurability and the initial trace

The original vector field is smooth on the open punctured polydisc.
For each fixed u in I*, C467e's survival beyond T_0 and smooth ODE
dependence give Y and D_uY locally continuous in (t,u) throughout
[0,T_0] x I*. This uses local neighborhoods along each compact
trajectory, not a neighborhood uniform in u. Thus mathcal A is
continuous there. The complement I\I* is the union of three diagonal
hyperplanes, a closed Lebesgue-null set. The specified zero extension
is jointly Borel measurable and hence measurable for completed
Lebesgue measure. The continuous function G is measurable too.

For every fixed u in I*, the same smooth dependence at the initial
time gives Y(t,u)->iu and D_uY(t,u)->iI_3. Hence
mathcal A(t,u)->F(iu). At t=0 the exact formula (10) also gives
mathcal A(0,u)=-e^{-H(iu)}Delta(u)^2=F(iu), because
Delta(iu)^2=i^6 Delta(u)^2=-Delta(u)^2. On a diagonal F(iu)=0,
matching the extension. In particular |F(iu)|<=G(u) a.e.

For any sequence t_k in [0,T_0] tending to zero, the functions
|mathcal A(t_k,u)-F(iu)| are measurable, tend pointwise to zero,
and are bounded by 2G in L1(I). Hunter's Theorem4.24 therefore
gives convergence of their integrals to zero. Since this holds for
every such sequence, the real-time limit (4) follows: failure would
give an epsilon>0 and a sequence of times tending to zero whose
L1 distances are at least epsilon. This completes the target.

The proof is analytic; no finite sampling, numerical trajectories,
diagonal smoothness, interchange over an uncontrolled domain, or
forward-flow damping is used. Local progress is the original reverse
spatial majorant and trace. The checked sources do not state this
specific bound; this specialization makes no claim of mathematical
novelty. Spacetime minors/current,
interfaces, payment, global assembly, all degrees and Xi transfer
remain independent gaps. The independent audit1021 below validates
the stated local result without changing these limitations.

### Independent conceptual audit — 15 November 2026, step1021

The invocation-start SPECIALIZE assessment
`drafts/literature/2026-11-15-reverse-spatial-trace-audit-nomination-1019.md`,
completed in review1020, covers this exact audit. Reuse its primary
source coverage and C467e-g/audit1017 as established inputs. C467h's
assertions themselves are not premises of the review. All formulas
(5)-(14), and the complete measurability and limit argument, were
checked. No new source import, changed hypothesis or novelty claim
is needed.

**Physical-time determinant.** C467g's Hamiltonian is
mathcal H=tilde h/L^2, and its variational equations are in the original
time t. Its independently solved Riccati system establishes
mathsf R=mathsf N mathsf M^-1 before (5) is used. Since p(0,u)=0,
the unique centered momenta are zero for every initial u. Thus the
initial coefficient variation is exactly (mathsf M,mathsf N)=(I,0);
there is no omitted derivative of initial momentum. For each fixed
distinct u, C467f gives distinct q through the closed interval, so the
real Hessian coefficients and mathsf R are continuous there. Teschl's
cited Abel-Liouville formula applies to this fixed linear system.
For its coefficient T, |tr T|<=3||T|| and

\[
 3(392+139/5)=6297/5,\qquad
 (6297/5)T_0=2099/3200<2/3.
\]

Consequently det mathsf M is positive and less than 3. Neither
continuity nor that estimate requires a common initial gap or a common
coefficient neighborhood. No time rescaling is hidden in the exponent.

**Centered Jacobian and complete complex cancellation.** To check
the coefficient convention explicitly, put e_1=sum q_j,
e_2=sum_{j<k}q_jq_k and e_3=q_1q_2q_3. Then

\[
 c=e_1/3,\quad b=e_2-e_1^2/3,\quad
 d=e_3-e_1e_2/3+2e_1^3/27.
\]

The Jacobian of this triangular change is 1/3. The rows of D_qe
are 1, e_1-q_j and e_2-e_1q_j+q_j^2. Determinant-preserving row
operations reduce them to 1, -q_j and q_j^2, so this determinant
is -Delta(q) in the stated order. Hence
det D_qE=-Delta(q)/(3L^6). Applying the chain rule to
E(q(t,u)) as the coefficient flow with initial E(u) and P_0=0 gives

\[
 D_qE\,Q=\mathsf M D_uE(u),\qquad
 \det Q=\det\mathsf M\,\Delta(u)/\Delta(q)>0.
\]

All six ordering chambers are covered: each q_k-q_j keeps the sign
of u_k-u_j, so the ratio is positive in each chamber. The factors
-1/3 and L^-6 cancel exactly. This uses local root charts only.

The local physical graph exists by that invertibility. Its derivative
Z is real, and Gram reality from C467e implies symmetry: writing
J=(Z+iI)Q, the imaginary part of J*J is Q^T(Z^T-Z)Q, hence vanishes
only when Z^T=Z. C467f's reconstruction and C467g give

\[
 \|Z\|<857/12800+133/375=80951/192000<1/2.
\]

Division of every column of J by i yields (I-iZ)Q. For a pair j<k
with remaining index l, the interpolation formula gives exactly
Y_k-Y_j=(q_k-q_j)(i-U-Vr_l). Each l appears once. Squaring the
three factors and multiplying by the complete determinant proves
(10), before any absolute values are taken. It leaves one Delta(q)
and one Delta(u), with det(I-iZ) intact. At time zero, mathsf M=I,
q=u, Z=0 and U=V=0; the product is i^6=-1. Thus the orientation
agrees with F(iu), not its negative or a modulus square.

**Uniform majorant.** C467e's radial estimate and Taylor remainder
give |H(Y)-H_0|<3/8; H_0 is real. The exponential bound is
e^(3/8)<=8/5. Each real gap has square <3/80<1/25, hence
|Delta(q)|<1/125. The pair-slope factor satisfies
(257/256)^3<(5/4)^3=125/64<2. The symmetric spectral theorem
applies to Z just proved symmetric; it gives the full determinant
modulus bounded by (5/4)^(3/2)<2, since 125/64<4. Therefore

\[
 (8/5)\,3\,(1/125)\,2\,2=96/625<1
\]

is the uniform coefficient in (14). These exact comparisons, not
sampled trajectories, verify (6)-(14). The initial gap bound and box
volume are both 2^-9, giving integral G<=2^-18 e^-H_0. All bounds
hold at both time endpoints and for arbitrary unequal distinct gaps.

**Measurability and the entire limit passage.** The maximal flow
domain of the smooth real vector field is open. For each u in I*,
survival beyond T_0 supplies local smooth dependence, including at
T_0; local existence at the initial point supplies it at t=0 as well.
Thus Y and D_uY are continuous on the relative domain
[0,T_0] x I*. The latter is relatively open, and its complement is
Borel. Extending the coefficient by zero on that complement is
jointly Borel measurable, without asserting continuity at any diagonal.
For each slice the exceptional set is a union of three null planes.

The analytic F is defined on the full polydisc, including collisions,
and F(iu)=0 on those planes. Off them, smooth dependence gives
Y(t,u)->iu and D_uY(t,u)->iI, so the coefficient converges to F(iu).
On them the specified extension already equals that value. The time
zero case of the validated bound gives |F(iu)|<=G(u). Hence, for
every sequence t_k in [0,T_0] tending to zero, the measurable
nonnegative absolute differences converge pointwise to zero and are
bounded by the single integrable function 2G. Hunter's cited DCT
applies to their integrals; it also establishes their L1 finiteness.
If the asserted real-time L1 limit failed, an epsilon-bad sequence
t_k->0 would contradict this conclusion. No uniform pointwise
convergence, interchange of an unbounded derivative, or Sobolev/current
trace theorem is being assumed.

The audit passes the majorant and initial L1 trace with unchanged
constants and hypotheses. It validates a local specialization of
assessed tools, not a new discovery beyond the literature checked.
C466a's density qualifications remain. Mixed spacetime minors,
collision/interface fluxes, payment, global assembly, all degrees and
actual-Xi transfer are not established by this audit. No RH candidate
is asserted.

## Mathlib

The full matching singular reverse-pullback result has not been checked
in Mathlib. Supporting coverage reused from review1018 includes
`MeasureTheory.tendsto_integral_of_dominated_convergence` and
`MeasureTheory.tendsto_integral_filter_of_dominated_convergence`
in [MeasureTheory.Integral.DominatedConvergence](https://leanprover-community.github.io/mathlib4_docs/Mathlib/MeasureTheory/Integral/DominatedConvergence.html).
Their measurability, integrable norm majorant and a.e. convergence
hypotheses are consistent with the sequence application above; the
filter version also has a countable-generation hypothesis. No Lean
formalization or full matching coverage is claimed. Unknown coverage
is not evidence of absence.
