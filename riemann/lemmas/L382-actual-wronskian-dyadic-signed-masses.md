# Lemma 382: both dyadic signed masses of the actual Wronskian

## Hypotheses

Use the fixed actual pair F_0,G and positive envelope A of L366, with
ordinary real derivatives and no positive regulator. For t>0 set
T=1+t, L=log(2+t), and use L380's convention

\[
 A(t)=(t^2+\tfrac14)|\Gamma(\tfrac14+it/2)|\pi^{-1/4},
 \qquad
 \mathcal W(t)=\frac{F_0'(t)G(t)-F_0(t)G'(t)}{A(t)^2T^2L}.
\]

Write W_+(t)=max(\mathcal W(t),0), W_-(t)=max(-\mathcal W(t),0),
and \(\langle f\rangle_H=H^{-1}\int_H^{2H}f(t)\,dt\).
H tends to infinity. There is no RH, simplicity, noncoincidence,
discriminant sign, fourth-moment or common-zero-count assumption.
All constants and the eventual onset refer to this fixed actual pair
and are uniform in H; no numerical onset is asserted.

## Conclusion

There are constants B>=1, c_*>0 and H_*>0 such that for every H>=H_*,

\[
 \sup_{H\le t\le2H}|\mathcal W(t)|\le B H^{3/8},
 \qquad
 \langle W_+\rangle_H\ge c_*H^{-3/8}\log H,
 \qquad
 \langle W_-\rangle_H\ge c_*H^{-3/8}\log H.                 \tag{1}
\]

One may take \(c_*=c/(8B)\), with the positive second-moment coefficient
\(c=\zeta(5)\zeta(3)^2/(96\pi^2\zeta(6))\) from L381, after increasing
H_*. In particular both signs occur in the interior of every such
interval, so a Wronskian sign change occurs there. This does not locate
a zero away from common F_0,G zeros or bound their number. It supplies
neither global actual-theta mixed positivity, the total L367 margin,
nor a new Laguerre sign or zero-exclusion range, nor an RH conclusion.
The separate critical audit below validates the bound without strengthening
its localization conclusion.

## Proof

This is a **REPRODUCTION** under the prior SPECIALIZE assessment
`drafts/literature/2026-10-08-wronskian-signed-mass-application.md`.
The known endpoint Holder inequality is imported; the family-specific
jet envelope and signed-part applicability are supplied here. No new
moment theorem or general interpolation theorem is reproved, and no
originality beyond the sources checked is claimed.

### Fixed completion disks and the real gamma normalization

Fix R=3/4 and rho=1/8 before H varies. If an anchor parameter is needed
to instantiate L320's hypotheses, fix eta=5/8; only its proved strip
bound (4), independent of the anchor, is used. Write xi_c for the entire
completion, to distinguish it from a frequency variable. L320 (4) gives

\[
 |\xi_c(\sigma+i\tau)|
 \le C_R(2+|\tau|)^{17/8}e^{-\pi|\tau|/4},
 \qquad -\tfrac14\le\sigma\le\tfrac54.                 \tag{2}
\]

For t>=40 and \(|v-(1/2+it)|\le\rho\), the real part of v lies in
[3/8,5/8], within this strip, and its imaginary part tau lies in
[t-rho,t+rho], which is positive. In particular

\[
 2+|\tau|\le 2+t+\rho\le(2+\rho)T,
 \qquad e^{-\pi|\tau|/4}\le e^{\pi\rho/4}e^{-\pi t/4}.
\]

Thus the full disk, including its boundary, obeys

\[
 \sup_{|v-(1/2+it)|\le\rho}|\xi_c(v)|
       \le C_0 T^{17/8}e^{-\pi t/4}.                     \tag{3}
\]

The constants absorb only fixed height shifts and fixed radii.
The ordinary complex Cauchy derivative estimate, valid because xi_c
is entire, bounds \(|\xi_c'(1/2+it)|\) by the right side of (3)
divided by rho. L366 (1) identifies the real function
\(F_0(t)=2\xi_c(1/2+it)\); therefore its ordinary real derivative is
\(F_0'(t)=2i\xi_c'(1/2+it)\). We obtain

\[
 |F_0(t)|\le2C_0T^{17/8}e^{-\pi t/4},\qquad
 |F_0'(t)|\le(2C_0/\rho)T^{17/8}e^{-\pi t/4}.           \tag{4}
\]

The standard complex Stirling formula used in L320 and L366 gives

\[
 |\Gamma(\tfrac14+it/2)|
       \asymp t^{-1/4}e^{-\pi t/4}\quad(t\longrightarrow\infty).
\]

Here the arguments have fixed positive real part, and eventually
\(|\arg(1/4+it/2)|\le3\pi/4\), a fixed sector away from the negative
real axis. Precisely this is the scalar input
[DLMF 5.11.3](https://dlmf.nist.gov/5.11.E3) with the asymptotic
sector qualification in [5.11(i)](https://dlmf.nist.gov/5.11#i).
Its leading exponential modulus includes a bounded factor tending
to a positive constant; hence the displayed comparison is two-sided.
Multiplying by \((t^2+1/4)\pi^{-1/4}\) yields an a_0>0 and finite t_0
such that

\[
 A(t)\ge a_0T^{7/4}e^{-\pi t/4}\quad(t\ge t_0).         \tag{5}
\]

Since A is positive, (4)-(5) give, uniformly for t>=max(40,t_0),

\[
 |F_0(t)|/A(t)\le K_0T^{3/8},\qquad
 |F_0'(t)|/A(t)\le K_1T^{3/8}.                         \tag{6}
\]

The denominator is the real center envelope A(t), never a zeta value,
a shifted envelope or a central derivative. No derivative of an
uncontrolled asymptotic remainder is used.

### Complete response jets and the Wronskian envelope

L366 (2), for j=0,1, gives

\[
 |G(t)|/A(t)\le D_0T^2,\qquad
 |G'(t)|/A(t)\le D_1T^2L.                              \tag{7}
\]

These bounds retain the complete response, not a finite Dirichlet head.
For explicit applicability, L368 (3)-(5) identifies
\(G=\operatorname{Re}(QbZ)\), where

\[
 Q=(t^2+\tfrac14)\Gamma(s)\pi^{-s},\quad s=\tfrac14+it/2,
 \quad |Q|=A,\quad
 b=(t^2/4-3/16-it/2)/\pi,
 \quad Z=\zeta(5/2+it).
\]

The full absolute sums \(M_j=\sum_{n\ge1}(\log n)^j n^{-5/2}\)
converge for j=0,1 and bound \(|Z|,|Z'|\). The domain is Re v=5/2>1
in [DLMF 25.2.1](https://dlmf.nist.gov/25.2#E1); local uniform
convergence justifies the real differentiation. The exact identity

\[
 Q'/Q=2t/(t^2+1/4)+(i/2)(\Psi(s)-\log\pi)
\]

and L368's controlled digamma expansion (7), sourced to
[DLMF 5.11.2](https://dlmf.nist.gov/5.11#E2) with
[5.11(ii)](https://dlmf.nist.gov/5.11#ii), give \(|Q'/Q|=O(L)\).
Also b=O(T^2), b'=O(T). Thus differentiating the exact carrier gives

\[
 |G'|\le A\bigl(|Q'/Q|\,|b|M_0+|b'|M_0+|b|M_1\bigr),
\]

which explicitly confirms (7) with the full series and all first-jet
carrier terms. Division by Q here is permitted by its explicit nonzero
gamma carrier; it is not division by F_0, G or zeta.

Using (6)-(7) in the defining Wronskian, with no sign assumptions,

\[
 |\mathcal W(t)|
 \le \frac{K_1T^{3/8}D_0T^2+K_0T^{3/8}D_1T^2L}{T^2L}
 \le K_2T^{3/8}.                                      \tag{8}
\]

Here L>=1 eventually. For H>=1 and H<=t<=2H, T<=3H.
Choose B>=max(1,3^{3/8}K_2). This proves the first bound in (1)
for every sufficiently large H, uniformly throughout the interval.

### Absolute mass and the full signed comparison

The measure dt/H on [H,2H] is a probability measure. The real continuous
function \(\mathcal W\) belongs to L^1 and L^infinity there, as required
for the known Holder endpoint inequality. Apply it to
\(|\mathcal W|\in L^1\) and \(|\mathcal W|\in L^\infty\):

\[
 Q_H:=\langle\mathcal W^2\rangle_H
 \le \|\mathcal W\|_{L^\infty(dt/H)}S_H,
 \qquad S_H:=\langle|\mathcal W|\rangle_H.               \tag{9}
\]

The precise primary reference is Terence Tao,
[245B, Notes 3: Lp spaces](https://terrytao.wordpress.com/2009/01/09/245b-notes-3-lp-spaces/),
9 January 2009, Proposition 3, with p=1, q=infinity, r=1.
The statement includes this endpoint; its printed proof leaves the
infinity case as an exercise. The endpoint applicability is immediate
here from the established bound \(|\mathcal W|\le BH^{3/8}\) throughout
the interval and integrability of its absolute value. No general
interpolation reproof or additional moment is needed.

Import audited L381 (1) in its exact normalization:

\[
 Q_H=c\log H+e_2(H),\qquad e_2(H)=o(\log H),\qquad c>0.
\]

For every sufficiently large H, \(|e_2(H)|\le(c/2)\log H\).
Equations (8)-(9) consequently imply

\[
 S_H\ge d H^{-3/8}\log H,\qquad d=c/(2B)>0.             \tag{10}
\]

Retain the entire first mean from L380 (2):

\[
 M_H:=\langle\mathcal W\rangle_H
 =\frac{\zeta(3)\log2}{2\pi H}
       +O((H\log H)^{-1})+O(H^{-1/2}(\log H)^2).         \tag{11}
\]

The implied constants are uniform in H for the same fixed actual
pair. Since the diagonal and both errors are included, (11) gives
\(|M_H|\le K_3H^{-1/2}(\log H)^2\) eventually, for some K_3.
Relative to the lower scale in (10), this bound costs at most

\[
 \frac{K_3}{d}H^{-1/8}\log H\longrightarrow0.            \tag{12}
\]

In particular choose the onset so that
\(|M_H|\le(d/2)H^{-3/8}\log H\) for every larger H.
The exact pointwise identities W_++W_-=|\mathcal W| and
W_+-W_-=\mathcal W now give

\[
 \langle W_\pm\rangle_H=(S_H\pm M_H)/2
 \ge(S_H-|M_H|)/2
 \ge(d/4)H^{-3/8}\log H.                               \tag{13}
\]

Taking c_*=d/4 proves (1). Increase H_* to cover every preceding
onset. All choices were fixed before H varied, so this is an eventual
assertion on every dyadic interval, rather than on a subsequence.

Positive signed integrals and continuity yield an interior point of
each sign (the endpoints alone have measure zero). The intermediate
value theorem gives an interior zero between them. Nothing here
separates that zero from the common-zero set: the common-only reset
obstruction recorded in L373 remains a warning, not a premise used
in the bound. Global positivity, total discriminant margin, common-free
localization, common-zero control, the low-index gap, heights above
forty and the endpoint arithmetic margin remain unresolved. This is a
local application of known inequalities and existing moments, not a
solution or candidate solution of RH.

### Separate critical audit, 2026-10-08

This audit uses the prior SPECIALIZE assessment
`drafts/literature/2026-10-08-wronskian-signed-mass-audit.md`.
The conclusion and constants survive unchanged. No mathematical repair,
new moment input or additional zero hypothesis is required.

**Fixed strip and center normalization.** L320's full proof of (4)
propagates the boundary bound by the damped maximum principle, taking
the rectangle-height limit before removing the damping. It applies at
R=3/4>eta=5/8>1/2 and has exponent 7/4+R/2=17/8.
The radius-1/8 disk centered at 1/2+it lies in [3/8,5/8] in real part,
strictly within [-1/4,5/4]. Its height shift costs at most
exp(pi/32), independent of t. The completion is entire on a neighborhood
of the closed disk, so Cauchy's estimate applies without a pole or zero
restriction. The exact identity in L366 (1) gives the factor 2 for F_0
and 2i for its ordinary real derivative; the derivative bound costs
rho^(-1)=8, a constant rather than a growing power of t.

For clarity, the scalar vertical modulus input can also be cited directly
as [DLMF 5.11.9](https://dlmf.nist.gov/5.11.E9), uniform for bounded real
parts. At real part 1/4 and imaginary part t/2 it gives

\[
 \frac{A(t)}{T^{7/4}e^{-\pi t/4}}
 \longrightarrow \pi^{-1/4}\sqrt{2\pi}\,2^{1/4}>0.
\]

Thus a fixed positive a_0 in (5) exists. This uses the real center
envelope, not a gamma value on the Cauchy circle. Subtracting exponents
17/8-7/4=3/8 verifies both estimates in (6). Neither a central zeta
lower bound nor differentiation of a Stirling remainder enters.

**Every response term.** The exact L368 carrier gives
G'=Re(Q'bZ+Qb'Z+QbZ'). Here
b'=t/(2pi)-i/(2pi), |b|=O(T^2), and |b'|=O(T).
The exact Q'/Q formula in the proof and the sector-controlled digamma
bound give |Q'|<=C A L. The full series on Re v=5/2 bounds |Z| and
|Z'| by M_0 and M_1; its local uniform convergence justifies the jet.
All three terms therefore satisfy (7), with fixed constants. Combining
them with (6) leaves K_1D_0/L+K_0D_1 times T^(3/8) in (8).
For L>=1 and T<=3H a single B>=1 absorbs this on the full interval.
Division is only by positive A and the nonzero explicit carrier Q.

**Complete errors and a common onset.** The L380 and L381 normalizations
are exactly the present ordinary-derivative Wronskian divided by A^2T^2L,
with the same T, L and dt/H. L381's audited sharp-endpoint and full-tail
argument gives an all-H limit: at fixed head N the normalized square-root
moment converges, and its difference from the full one is at most
C rho_0(N), uniformly for large H. Letting N grow squeezes liminf and
limsup together. The derivative-tail terms, cross terms and coefficient
variation cost O(1/log H), O(1) and O(log H/H) in the averaged square,
and the complete same-height projection costs O(1). These, together with
the fixed-head little-o and uniform norm-tail passage, are included in
e_2(H)=o(log H); no rate uniform in a growing head is assumed here.

Consequently choose H_2 so that Q_H>=c log H/2 for all H>=H_2.
Endpoint Holder with the proved supremum gives S_H>=d H^(-3/8)log H,
where d=c/(2B). L380 retains its diagonal and both errors: their absolute
sum is bounded by K_3 H^(-1/2)(log H)^2 for all H beyond a fixed H_1.
Relative to d H^(-3/8)log H this is (K_3/d)H^(-1/8)log H, which
tends to zero. Choose H_3 so it is at most 1/2 for every H>=H_3.
Take H_* above H_1,H_2,H_3, the strip/gamma/jet onsets and e.
Then the exact signed-part identities yield

\[
 \langle W_\pm\rangle_H
 \ge \tfrac12\left(d-\tfrac d2\right)H^{-3/8}\log H
 =\frac{c}{8B}H^{-3/8}\log H\qquad(H\ge H_*).
\]

No diagonal-only or subsequence estimate is substituted for a full error.
Both signed integrals are strictly positive, hence both signs occur at
interior points. Continuity supplies an intervening zero; real analyticity
and nonidentity ensure an actual sign-changing zero, not an interval of
zeros. This last observation uses no simplicity assumption. There is no
restriction here on whether that zero is common to F_0 and G. L373's
common-only reset obstruction remains relevant; the audit supplies no
common-free localization or RH consequence. This is validation of an
existing reproduction, not a new bound or progress beyond checked sources.

## Mathlib

Full matching coverage of the actual gamma-normalized jet and signed-mass
statement is **not checked**. The prior assessment inspected supporting
[Holder documentation](https://leanprover-community.github.io/mathlib4_docs/Mathlib/MeasureTheory/Function/Holder.html#MeasureTheory.Lp.norm_smul_le),
including `MeasureTheory.Lp.norm_smul_le` and
`MeasureTheory.eLpNorm_le_enorm_mul_eLpNorm_mul_eLpNorm`.
These supply general inequality support, not this actual-pair theorem.
Completion, gamma, Cauchy and moment coverage is inherited with the
qualifications of the local inputs; no complete Lean proof or library
absence is asserted. The DLMF and Tao inputs above are classical
citations, not claims of matching Mathlib coverage.
