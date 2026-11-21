# C467e — Reverse actual-h survival, nonvanishing and a uniform short-time cone

## Hypotheses

Use C466z's actual normalized logarithm B, with exp B(w) equal to
h(w)=xi(1/2+sqrt(w))/xi(1/2), on |w-1|<1/4. Thus B is real under
conjugation and x=B'(1) is real. Use C466/audit993's unchanged analytic
bound |B''(w)|<M=40 on this disk. Set

\[
 R=1/4,\quad a=1/16,\quad T_0=1/1920,\quad
 g(z)=B'(1+z)-x,\quad \beta(z)=B(1+z)-B(1)-xz,
\]
\[
 H(z)=\sum_{j=1}^3[B(1+z_j)-x(1+z_j)],\quad
 H_0=3(B(1)-x),\quad F(z)=\Delta(z)^2e^{-H(z)},\quad
 \Delta(z)=\prod_{j<k}(z_k-z_j).
\]

For distinct real u in I=(-a,a)^3 take the raw reversed field

\[
 Y_j'=2\sum_{k\ne j}\frac{Y_j-Y_k}{|Y_j-Y_k|^2}
                      -\overline{g(Y_j)},\qquad Y(0,u)=iu.       \tag{1}
\]

Its first maximal lifetime tau_-(u) is in
U={z: |z_j|<R, Delta(z) != 0}. No restart or modified metric is used.
All derivatives J=D_uY below are at fixed physical time. The complete
coefficient, with the stipulated three-variable orientation, is

\[
 K_-(t,u)=-\frac{e^{H_0}}{\Delta(u)^2}
                 F(Y(t,u))\det_{\mathbb C}(J/i).                 \tag{2}
\]

Retain C466a's external density qualifications if interpreting this
as a chart for its reciprocal density. The proof below uses the actual
analytic B and its stated bound, not a density construction or RH.

## Conclusion

Every distinct u in I has tau_-(u)>T_0. On 0<=t<=T_0,

\[
 \sum_j|Y_j(t,u)|^2<r_*^2:=3/160<R^2.                           \tag{3}
\]

For each such u the physical pair distances have a positive lower
bound throughout this interval, allowed to depend on u. The full
complex determinant det_C J and K_- never vanish there.

There also exists one delta in (0,T_0], independent of all spacings
and of u, such that K_- has a representative phase satisfying

\[
 |\arg K_-(t,u)|<27/64<\pi/2
       \quad(0\le t\le\delta,\ u\in I,\ \Delta(u)\ne0).          \tag{4}
\]

This is an existential uniform short-time cone. **No bound delta>=T_0
is proved here.** This compactness argument alone leaves the fixed-horizon
cone from ready1012 unresolved; it gives no counterexample to it.
A regular symmetric-coordinate
Hamiltonian and the precise remaining derivative bound are given below.
No current, initial trace, mass payment, interface identity, all-degree
positivity or Xi transfer is claimed. The independent conceptual
audit1017 below validates this local result of attempt1013.

## Proof

### Imported tools and scope

Reuse the source comparison in ready1012 and nomination1011/completion1012.
C466z/audit988 supplies B and its conjugation normalization; only the
analytic estimates (7)-(8) of C466/audit993 are used. None of their
forward trajectories, barriers, lifetimes or currents is reversed by
assertion.

The local existence, uniqueness, smooth dependence, variational and
compact-continuation tools are Gerald Teschl, *Ordinary Differential
Equations and Dynamical Systems*, author-hosted April2012 preliminary
version, [Lemma2.14/Corollary2.15, pp52-53; Theorem3.9, p81;
Theorem6.1 and proof, pp189-190](https://www.mat.univie.ac.at/~gerald/ftp/book-ode/ode.pdf).
They apply first on the smooth open set U, and later to an explicitly
regular six-dimensional real ODE. Uniform short-time existence below
uses a compact set inside that regular domain, not the original divisor.

The real-parameter variational convention is Tanizaki, Nishimura and
Verbaarschot, *Gradient flows without blow-up for Lefschetz thimbles*,
JHEP10(2017)100, [arXiv:1706.03822v2, AppendixB (B.1)-(B.5),
printed p22](https://arxiv.org/html/1706.03822v2#A2).
For Gram reality use Fukuma and Matsumoto, *Worldvolume approach to the
tempered Lefschetz thimble method*, [arXiv:2012.08468v1, (1.6)-(1.12)
and (3.16), including footnotes3 and12](https://arxiv.org/html/2012.08468v1).
These local tools require nonsingular surviving trajectories; the latter
identity is not a phase theorem. The reversed sign and imaginary initial
plane are checked explicitly below. No general flow, symplectic or
invariant-cone theorem is reproved. The additional work is the particular
radial estimate, symmetric-coordinate regularization and uniform
reconstruction; the inspected sources do not supply (4).

### Full-horizon survival in the original domain

Locally write S=-2 log Delta+H and f=grad S. Only the single-valued
derivatives of S are needed. Equation (1) is Y'=-conjugate(f(Y)).
Since dF=-F sum_j f_j dz_j, its exact weight law is

\[
 \frac{d}{dt}F(Y)=\|f(Y)\|^2F(Y),\qquad
 F(Y(t))=F(iu)\exp\!\left(\int_0^t\|f(Y(s))\|^2ds\right).       \tag{5}
\]

Every integral here is on a compact surviving interval. In particular
|F| is nondecreasing, and the factor in the exponential is real.

Put V=sum_j |Y_j|^2. Each unordered pair contributes exactly 4 to V'
under (1): its contribution is
4 Re[(conjugate(Y_j)-conjugate(Y_k))(Y_j-Y_k)/|Y_j-Y_k|^2].
As g(0)=0 and |g(z)|<=M|z|, the regular contribution has absolute
value at most 2MV. Thus

\[
 V'\le12+80V,\qquad
 V(t)\le(V(0)+3/20)e^{80t}-3/20.                               \tag{6}
\]

For t<=T_0, 80t<=1/24 and e^{80t}<=24/23, using
e^s<=1/(1-s) for 0<=s<1. Since V(0)<3/256,

\[
 V(t)<(3/256+3/20)(24/23)-3/20=3/160.                          \tag{7}
\]

Taylor's integral formula and |B''|<=M give
|H(z)-H_0|<=MV/2. In particular |H(iu)-H_0|<15/64 and the
bound along (7) is at most 3/8. Equation (5) consequently yields

\[
 |\Delta(Y(t))|^2=|F(Y(t))|e^{\operatorname{Re}H(Y(t))}
       \ge e^{-39/64}\Delta(u)^2.                              \tag{8}
\]

For each particular pair, the other two squared distances are at
most 4r_*^2=3/40. Therefore

\[
 |Y_j(t)-Y_k(t)|^2\ge(1600/9)e^{-39/64}\Delta(u)^2>0.            \tag{9}
\]

All these bounds hold for t<min(tau_-(u),T_0), with no previously
assumed common lifetime. If tau_-(u)<=T_0, (7),(9) keep the trajectory
in a compact subset of U through that endpoint. The cited continuation
theorem contradicts maximality. It also extends past an endpoint equal
to T_0. This proves tau_-(u)>T_0 and (3). The lower bound (9) is not
uniform as u approaches a diagonal, and no such bound is used later.

### Nonvanishing of the complete determinant

Let G=D^2S(Y), complex symmetric. The cited variational rule with
action -S and initial derivative iI gives

\[
 J'=-\overline{GJ},\qquad J(0)=iI.                              \tag{10}
\]

The real six-dimensional flow derivative is invertible on each compact
surviving interval, by the linear variational fundamental-matrix theorem.
Its restriction J to the initial real three-plane has real rank three.
For the reversed/rotated specialization of the cited Gram identity,

\[
 (J^*J)'=-J^TGJ-\overline{J^TGJ}.                               \tag{11}
\]

The right side is real symmetric, and J(0)^*J(0)=I. Hence J^*J is
real symmetric. It is positive definite on real vectors by real rank
three, and therefore is a positive definite real matrix. The exact
identity det(J^*J)=|det_C J|^2 now proves det_C J != 0. This step uses
Gram reality as well as immersion; immersion alone would not suffice.

Finally Delta(iu)^2=-Delta(u)^2, so (2),(5) give

\[
 K_-(t,u)=e^{H_0-H(iu)}
       \exp\!\left(\int_0^t\|f(Y(s,u))\|^2ds\right)\det(J/i).
                                                                    \tag{12}
\]

This proves nonvanishing on the full horizon. It leaves the phase of
the last determinant unpaid. No sign is inferred from (11).

### Removal of inverse gaps in symmetric canonical coordinates

Write Y=p+iq with p,q real. As long as the q_j are distinct let

\[
 e_1=q_1+q_2+q_3,\quad e_2=q_1q_2+q_1q_3+q_2q_3,\quad
 e_3=q_1q_2q_3,\qquad p=(D_qe)^T\pi.                           \tag{13}
\]

The real momenta pi are uniquely defined there because
det(D_qe)=-Delta(q). More explicitly,

\[
 p_j=P_{e,\pi}(q_j),\qquad
 P_{e,\pi}(v)=\pi_1+(e_1-v)\pi_2+(v^2-e_1v+e_2)\pi_3.        \tag{14}
\]

If l is the index other than j,k, subtraction gives exactly

\[
 \frac{p_j-p_k}{q_j-q_k}=-\pi_2-q_l\pi_3.                       \tag{15}
\]

With h=Im S, the Cauchy-Riemann equations turn the reversed field
into q'=h_p, p'=-h_q. Equation (13) gives the identity of one-forms
sum_j p_j dq_j=sum_b pi_b de_b. Differentiating this identity, or
substituting its chain rule into these Hamilton equations, therefore
gives e'=h_tilde_pi, pi'=-h_tilde_e in this coordinate chart.

Indeed each ordered gap has argument pi/2+atan(pi_2+q_l pi_3)
by (15). The local action branch changes only an additive real
constant in h. Its relevant Hamiltonian is thus

\[
 \widetilde h(e,\pi)=-2\sum_{l=1}^3\arctan(\pi_2+q_l\pi_3)
       +\frac1{2i}\sum_{l=1}^3
        [\beta(P_{e,\pi}(q_l)+iq_l)
                    -\beta(P_{e,\pi}(q_l)-iq_l)].                \tag{16}
\]

The conjugation property of beta justifies the second term for real
q,e,pi. This formula keeps the actual background, rather than a jet
replacement. The equations to be studied are exactly

\[
 E'=\partial_\pi\widetilde h(E,\Pi),\qquad
 \Pi'=-\partial_e\widetilde h(E,\Pi),\qquad
 (E(0),\Pi(0))=(e(u),0).                                      \tag{17}
\]

We now construct a regular domain for (16), rather than assuming
smoothness through an imaginary collision. Put r=31/128, so a/r=8/31
and R-r=1/128. On |v|=r, for
|e_1|<=3a, |e_2|<=3a^2, |e_3|<=a^3,

\[
 \frac{|e_1v^2-e_2v+e_3|}{r^3}
       \le3(a/r)+3(a/r)^2+(a/r)^3=29528/29791<1.                \tag{18}
\]

Choose a slightly larger complex coefficient polydisc V retaining
this strict inequality and with |e_1|<1/5, |e_2|<1/64.
For example enlarge each of the three bounds in (18) by 257/256;
the ratio remains 7588696/7626496<1. Rouche's theorem places all
three roots of Q_e(v)=v^3-e_1v^2+e_2v-e_3 strictly inside |v|<r.

If max_b |pi_b|<1/256, (14) gives, for |v|<=r,

\[
 |P_{e,\pi}(v)|<\frac1{256}
       (1+1/5+1/4+1/16+1/20+1/64)<1/128=R-r,
\]
\[
 |\pi_2+v\pi_3|<5/1024<1/2.                                  \tag{19}
\]

Both beta arguments in (16) lie inside its original disk |z|<R,
and arctan is its holomorphic branch at zero. Define

\[
 A(v;e,\pi)=-2\arctan(\pi_2+v\pi_3)
       +[\beta(P_{e,\pi}(v)+iv)-\beta(P_{e,\pi}(v)-iv)]/(2i).
\]

The residue theorem gives the following definition even at repeated
roots, without choosing individual root branches:

\[
 \widetilde h(e,\pi)=\frac1{2\pi i}
       \int_{|v|=r} A(v;e,\pi)\frac{Q_e'(v)}{Q_e(v)}\,dv.       \tag{20}
\]

The residue at a root of multiplicity m is m A evaluated there.
The denominator is uniformly nonzero on the circle locally in V,
and the integrand is holomorphic in all parameters. Differentiation
under this finite contour integral is justified by uniform bounds
on a smaller parameter neighborhood. Thus (20) is holomorphic on
V times the stated momentum polydisc and agrees with (16) at simple
roots. For real parameters it is real, including at nonreal conjugate
root pairs: A has real Taylor coefficients in v for real e,pi, so
conjugate roots contribute conjugate values. Consequently (17) is a
regular real Hamiltonian ODE throughout that domain.

The named Rouche and residue theorems are the standard elementary
complex-analysis inputs. The finite contour formula proves this
particular extension; no general singular quotient theorem is imported.
As a sign check only, suppressing beta in (16) gives, at Pi=0,
E_1'=0, E_2'=-6, E_3'=-2E_1 and Pi'=0. The actual proof retains beta.

### A common short-time graph and its complete phase

The compact set of e(u) for u in [-a,a]^3 lies in a smaller real
coefficient box V_0 whose closure is inside V. Choose V_0 convex.
Apply the cited smooth ODE tools to (17) for every initial point
(e^0,0) with e^0 in the closure of V_0. Compactness gives a common
time delta_1>0, at most T_0, on which the coefficient solutions stay
inside (19)'s domain and depend smoothly on e^0. Write them as
(E_t(e^0),Pi_t(e^0)). Uniformly on that compact initial set,

\[
 E_t\longrightarrow\mathrm{id}\text{ in }C^1,\qquad
 \Pi_t\longrightarrow0\text{ in }C^1\quad(t\longrightarrow0).
                                                                    \tag{21}
\]

Reduce delta_1 if necessary so that
||D_{e^0}E_t-I||<1/2 for all these initial points and times.
The mean-value integral along line segments in V_0 makes E_t
injective there: its increment differs from that of the identity
by at most half the distance. The inverse function theorem supplies
a smooth inverse on E_t(V_0). Also det D_{e^0}E_t>0, by continuity
from t=0 without a zero. Define on this image the momentum graph

\[
 \widehat\Pi_t=\Pi_t\circ E_t^{-1},\qquad
 D_e\widehat\Pi_t=(D_{e^0}\Pi_t)(D_{e^0}E_t)^{-1}.               \tag{22}
\]

We must still check that this coefficient graph describes the actual
raw flow. For a fixed distinct u it does so initially, by (13)-(17)
and local uniqueness. Up to the first possible failure of distinct
imaginary coordinates, its coefficient solution agrees with (17).
It cannot exit the regular coefficient chart there, since the latter
solution remains in a compact interior subset on this smaller time
interval. Nor can two imaginary coordinates first coincide: bounded
Pi and (15) would then force the corresponding p difference to zero,
giving a physical collision, contrary to (9). This continuation
argument proves agreement, distinct q and unchanged ordering on the
whole interval 0<=t<=delta_1. It assumes neither a forward barrier
nor an a priori inverse for the actual spatial projection.

For such an actual trajectory set Q=D_uq, P=D_up. Differentiating
e(q(t,u))=E_t(e(u)) at fixed time gives

\[
 (D_qe)Q=(D_{e^0}E_t)(D_ue),\qquad
 \det Q=\det(D_{e^0}E_t)\frac{\Delta(u)}{\Delta(q)}>0.           \tag{23}
\]

Distinctness and preserved ordering give the last sign. This proves
Q invertible. In a neighborhood of this point the real part of the
deformed plane is the graph

\[
 p(q)=(D_qe)^T\widehat\Pi_t(e(q)),\qquad Z=D_qp,\quad P=ZQ.
                                                                    \tag{24}
\]

Reality of J^*J from (11) says P^TQ=Q^TP. With Q now known invertible,
this implies Z=Z^T. Direct differentiation of (24) also gives the
bound, for |q_j|<=r_* from (3),

\[
 \|Z\|\le 2|\widehat\Pi_{t,2}|+2r_*|\widehat\Pi_{t,3}|
       +(3+12r_*^2+3r_*^4)\|D_e\widehat\Pi_t\|.                 \tag{25}
\]

Here ||D_qe||^2 is at most its squared Frobenius norm
3+12r_*^2+3r_*^4, ||D_q^2e_2||=2,
||D_q^2e_3||<=2r_*, and D_q^2e_1=0. Thus no inverse gap is hidden
in (25). By (21),(22), its right side tends uniformly to zero for
all e^0 in the compact set of initial triples, including repeated
ones. Choose one delta in (0,delta_1] making it <1/16 throughout
0<=t<=delta. This choice is independent of each original spacing.

The actual complex determinant now factors as

\[
 \det(J/i)=\det(Q-iP)=\det Q\det(I-iZ)
                  =\det Q\prod_{j=1}^3(1-i\lambda_j),           \tag{26}
\]

where the lambda_j are the real eigenvalues of Z. Its representative
phase has modulus <=sum_j arctan|lambda_j|<3/16. In (12) the middle
factor is positive, and the initial factor has phase bounded by
|H(iu)-H_0|<15/64. Their sum is <15/64+3/16=27/64, proving (4).
This also checks the orientation and complete determinant; no scalar
or action-only phase is substituted for K_-.

### Exact limit of the attempt

The compact ODE argument selects delta without an effective lower
bound. It therefore cannot establish the gate's specified horizon
T_0. Nonvanishing on that full horizon does not supply an angular
margin. No reverse cone is refuted by the failure of the forward
Riccati barrier.

One concrete sufficient continuation test for the same target is to
control (17) through T_0 in a valid regular chart, keep D_{e^0}E_t
invertible with positive determinant, and bound (25) by 1/4. The same
continuation and factorization would then give a full-horizon phase
bound <15/64+3/4=63/64<pi/2. Those quantitative estimates are unproved.
They concern the unchanged actual field and complete K_-; a failed
coefficient bound would still not be an actual-flow refutation.

The symmetric regularization and resulting common short-time cone
are local mathematical progress beyond the conclusions of the sources
compared in ready1012. The standard ODE, Gram, inverse-function and
complex-analysis tools themselves are imported/specialized, not claimed
as discoveries. Originality of the local result is not certified.

### Independent conceptual audit — 15 November 2026, step1017

The invocation-start SPECIALIZE assessment nomination1015/completion1016
covers this combined C467e–g audit. This section checks C467e independently
of the later centered estimates; neither C467f nor C467g is a premise.
Reuse C466z/audit988's actual logarithm and conjugation normalization and
only C466/audit993(7)–(8)'s whole complex-disk bounds. The earlier forward
trajectory and current results are not imported. The named ODE, Gram,
Rouche and residue inputs above have exactly the local hypotheses needed.

**Survival and determinant.** Direct pairwise summation in the original
reversed equation gives 4 per unordered pair in V', hence 12, not a
spacing-dependent error. Integrating V'<=12+80V gives (6), and
(3/256+3/20)(24/23)-3/20=3/160 exactly. The estimate is applied only
before the first lifetime. Taylor's remainder bounds the initial and
evolved background by 15/64 and 3/8, respectively. The sign in
dF/dt=||f||^2 F is positive for this reversed field and the original F.
It gives (8) with exponent -(15/64+3/8)=-39/64. Bounding the other
two squared distances by 3/40 proves (9). For each fixed distinct u,
these estimates give a compact subset of U; the cited continuation
theorem therefore excludes a lifetime <=T_0, including equality.
No uniform positive separation of initial data was used.

For real parameter derivatives, J'=-overline(GJ) with J(0)=iI is
the correct variational equation. Differentiating J*J gives (11),
not a Hermitian-only identity. The real six-dimensional fundamental
matrix is invertible, so J has real rank three. Since J*J is a real
symmetric matrix, positivity on nonzero real vectors implies its three
real eigenvalues are positive. Thus its determinant is positive and
det_C J is nonzero. This inference uses both facts; neither immersion
alone nor a Gram identity alone is being used as a phase bound.

**Regularization and short-time reconstruction.** With S holomorphic
locally, Cauchy–Riemann gives q'=h_p and p'=-h_q for h=Im S.
The canonical one-form identity (13) gives (17) with the displayed
signs. For a gap, (15) gives a real-to-imaginary ratio
-(pi_2+q_l pi_3); its argument is pi/2+atan(pi_2+q_l pi_3)
up to a chamber constant. This verifies the singular term in (16).
The ratio in (18) is strictly below 1 even after the stated 257/256
enlargement. The momentum bound in (19) puts both beta arguments
strictly inside |z|<1/4 and the arctangent arguments inside their
analytic branch. Residues in (20) count each root with multiplicity.
Nonvanishing of Q on the fixed circle on a smaller parameter
neighborhood justifies parameter differentiation. For real parameters,
A(overline(v))=overline(A(v)); conjugate root pairs therefore yield a
real Hamiltonian even off the real-root locus. The regular real ODE
is consequently defined on an open neighborhood of the compact
initial coefficient box, including its repeated-root points.

The common C^1 convergence in (21) follows from smooth dependence
on this compact box, not from uniform control of the singular physical
field. Convexity and ||DE_t-I||<1/2 imply injectivity by integration
along segments. Until a putative first imaginary collision, uniqueness
identifies the coefficient and physical solutions. Bounded momenta
would turn that event into a physical collision by (15), contradicting
(9). This checks the continuation needed before (23). Its determinant
ratio has positive sign because imaginary ordering is preserved.
Differentiating the actual graph gives (25), with no inverse-gap term.
Its right side tends uniformly to zero; this proves only the asserted
existential common delta. In (26), Gram reality makes Z symmetric,
and the positive det Q leaves the phase equal to the sum of the
principal -atan(lambda_j). Finally Delta(iu)^2=-Delta(u)^2 cancels
the leading minus sign in (2), yielding exactly (12). The background
phase plus this determinant phase is <27/64. All conclusions of this
lemma pass, without supplying an effective delta here, a reverse
current, an integrability estimate or a density construction.

## Mathlib

Full matching coverage for this actual-h reversed flow, its symmetric
Hamiltonian extension and uniform short-time cone has not been checked.
The supporting inputs are standard finite-dimensional ODE and variational
theorems, real symmetric spectral theory, determinant/Gram identities,
the inverse function theorem, Rouche's theorem and the residue theorem.
No matching formalization, absence from Mathlib, or formal verification
of the phase conclusion is asserted.
