# L131 — Equality kernel has positive normalized Kähler alpha-charge

## Hypotheses

Retain L044/L071's identical marked projective K3 factors S_1,S_2,
common ordered hyperkähler structures and exact common metric g. Let
omega_i denote the pulled-back actual I-Kähler forms, with class h_i,
and put s=q(h,h)>0. Normalize eta by integral_S eta=1, and write
e_1=eta tensor 1, e_2=1 tensor eta. Retain the full integral mixed
class tau_D, with q-self-adjoint operator D and Dh=2lambda h, where
lambda is the positive root of z^3+z^2-2z-1 and 1<lambda<5/4.

Suppose F is a locally free rank-two holomorphic bundle on S_1 x S_2,
slope-polystable at h_1+h_2, with integral c_1(F)=0 and

\[
\operatorname{ch}_2(F)=-14e_1-21e_2-\tau_D.
\]

No existence is assumed. Use only the normalized product Kähler
calibration theta=(omega_1+omega_2)^2/2. No Spin(7) calibration or
independent factor rotations are asserted.

## Conclusion

For base Y=S_1 and fibre S_2 the decomposition is

\[
\theta=\operatorname{vol}_1\wedge\beta+\alpha_1,
\qquad\beta=1,\qquad
\alpha_1=\omega_1\wedge\omega_2+\operatorname{vol}_2.
\]

Both normalized spectral minima are -1. The exact charges are

\[
\kappa_{\alpha_1}(F)=(7+2\lambda)s>0,\qquad
\kappa_{\alpha_2}(F)=(21/2+2\lambda)s>0,
\]

where alpha_2 is the consistently exchanged decomposition. Thus
Galt–Ma's negative-charge, null-charge and strict-gap criteria do not
exclude F or force zero mixed curvature here. This particular Kähler
charge filter is parked. Positive charge proves neither existence nor
the absence of other obstructions. Universal primitive rational Hodge
realization, F existence, separation, reconstruction and transport remain
unresolved. This is a NEGATIVE / REPRODUCTION specialization of the
assessed known framework. The separate critical audit below preserves
the calculation and its non-exclusion verdict.

## Proof

**Actual connection and normalization.** L071's stable-product passage
applies with a=-18,b=-25 and supplies F's compatible hyperholomorphic
HYM connection. Its determinant is holomorphically trivial: Picard
injection on the K3 product follows from H^1(O)=0 and the exponential
sequence, and integral c_1 is zero. The determinant HYM connection is
flat (its curvature is the harmonic representative of zero); the
simply connected product trivializes this flat determinant. Fixing a
unit determinant frame gives the required SU(2) connection.

Import Galt–Ma, *Dimension Reduction of Generalized ASD Instantons*,
[arXiv:2405.17086v2, section 2.3, after (2.21)](https://arxiv.org/html/2405.17086v2#S2.SS3):
SU(r) HYM uses theta=omega^(m-2)/(m-2)!. Here m=4. Kähler Hodge-star
identities give eigenvalues -1,1,3 on real primitive (1,1), real
(2,0)+(0,2), and R omega respectively, so the minimum is -1. This
is the cited normalization, not the unscaled power in section 6.3.
The degree-four expansion on the product of two surfaces gives

\[
\theta=\frac{\omega_1^2}{2}+\omega_1\wedge\omega_2
             +\frac{\omega_2^2}{2}.
\]

Since vol_i=omega_i^2/2, its top Y-degree term is exactly vol_1,
so beta=1; both remaining terms belong to alpha_1. On the oriented
four-dimensional fibre Q_beta=* has minimum -1 as well. Parallelness
holds for all these forms. Hence the calibration is admissible and
compatible in the source's Definitions 1.1–1.2. The base and fibre
are closed and the fibre has real dimension four, as required.

**Full cohomological pairing.** Since c_1=0,
c_2=-ch_2=14e_1+21e_2+tau_D. Also [vol_i]=(s/2)e_i and
Vol(S_i)=s/2. In a rational q-dual basis v_j,v^j of the full H^2(S,Q),
the tensor convention is tau_D=sum_j v^j tensor Dv_j. Therefore

\[
\int_{S_1\times S_2}\tau_D(h\otimes h)
 =\sum_j q(v^j,h)q(Dv_j,h)
 =q(Dh,h)=2\lambda s.
\]

All classes here have even degree, so no interchange sign occurs.
This retains the whole tensor: its transcendental block pairs to zero
with h by cup-product orthogonality, rather than being deleted from
c_2; no integral NS/T splitting is used. Factor degrees give
e_1(h tensor h)=e_2(h tensor h)=0, tau_D e_i=0 and e_i^2=0,
whereas integral e_1e_2=1. It follows that

\[
\begin{aligned}
\kappa_{\alpha_1}(F)
 &=\int(14e_1+21e_2+\tau_D)
           (h\otimes h+(s/2)e_2)\\
 &=2\lambda s+7s.
\end{aligned}
\]

In particular, discarding the pure vol_2 term would miss 7s.
For the reversed order alpha_2=omega_1 omega_2+vol_1, so the pure
contribution is 21s/2. Tensor exchange transposes D to D*=D and
preserves the even-degree sign. This proves the second charge.
As a consistency check, in either decomposition the total pairing is

\[
\int c_2(F)\theta=(35/2+2\lambda)s;
\]

subtracting the vertical contribution 21s/2 or 14s/2 returns exactly
the corresponding alpha-charge. Thus the pure coefficients, relative
volume and factorial agree in both orders.

**Threshold comparison.** Apply only the hypotheses of
[Galt–Ma v2, Proposition 4.2 and Lemma 4.3](https://arxiv.org/html/2405.17086v2#S4).
Negative charge would exclude the instanton; zero charge at matched
spectra would force the two product curvature components to vanish.
Both charges here are strictly positive. The positive-charge exclusion
requires -1<eta_beta<0 and a charge strictly below
Vol(Y) kappa_beta(-1-1/eta_beta). Here eta_beta=-1, not a strict gap;
even formal substitution makes that threshold zero. Neither positive
charge meets it. This is failure of these sufficient criteria, not a
converse to them and not a splitting or existence theorem. No reproof
of the source's energy theorem is needed.

### Separate critical audit, 2026-10-19

This is a RESEARCH / REPRODUCTION audit under the unchanged saved
SPECIALIZE assessment. It finds no substantive error or stronger
conclusion. Its outcome is EXPLORATION, not a second NEGATIVE result
or a new mathematical advance. The original filter remains parked.

**Connection hypotheses.** The coefficients correspond to L071's
a=-18,b=-25. Its two-line exclusion uses the nonzero action on the
holomorphic two-form, so it applies to these data before invoking
the stable hyperholomorphic connection theorem. In particular no
stability of the charge-fourteen restrictions is needed. The actual
product HYM connection has zero Einstein constant since c_1=0.
For its determinant curvature f=tr(R), the Bianchi identity gives
df=0, and HYM gives type (1,1) and Lambda f=0. The Kähler star
identity is *f=-f wedge Omega^2/2 in complex dimension four, where
Omega here denotes the actual product Kähler form. Hence d*f=0.
This proves the harmonicity used above; since [f/(2pi i)]=c_1=0,
f vanishes. Simple connectedness removes flat determinant holonomy,
so a global parallel unit determinant frame reduces this same
connection to SU(2). This does not impose a new connection on F.

**Metric and factorial.** The product complex orientation has
Omega^4/4!=vol_1 wedge vol_2. For a primitive real two-form a of
type (1,1), *a=-a wedge Omega^2/2; for a real form of type
(2,0)+(0,2), *a=a wedge Omega^2/2. Also *Omega^3=6Omega.
Consequently Q_theta=*(theta wedge -) has eigenvalues -1,+1,3
on these spaces and R Omega. Their real dimensions 15,12,1
exhaust Lambda^2 in real dimension eight. On the fibre beta=1,
Q_beta=* has its usual three-dimensional +1 and -1 spaces.
Thus neither minimum has an omitted rescaling. This specializes
the Kähler identities and the SU(r) statement immediately after
Galt–Ma (2.21), rather than importing section 6.3's unscaled power.

**Independent pairing check.** By the full dual-basis convention,
sum_j q(v^j,h)v_j=h, so contraction of tau_D against h tensor h
is q(Dh,h). The pairing needs only rational duality followed by
real extension to h; no integral orthogonal decomposition occurs.
The following table retains every nonzero contribution:

| Base | Fibre | integral c_2 theta | Vol(base) kappa_beta | Difference |
| --- | --- | --- | --- | --- |
| S_1 | S_2 | (35/2+2lambda)s | 21s/2 | (7+2lambda)s |
| S_2 | S_1 | (35/2+2lambda)s | 14s/2 | (21/2+2lambda)s |

The fibre charges are respectively 21 and 14 by actual restriction;
neither depends on stable versus split fibre type. The exchanged
mixed tensor is the adjoint D*=D, since both factors have degree
two. This checks the alpha calculation independently by the total
charge decomposition, including its pure term and orientation.

**All source branches.** Reopened Galt–Ma v2, section 4.1 setup,
Proposition 4.2(a)–(c), and Lemma 4.3 with (4.10)–(4.16).
Case (a) requires null charge and a strict spectral gap, (b)
requires positive charge below the strict-gap bound, and (c)
requires negative charge. Here both charges are positive and the
gap is zero. Lemma 4.3 separately requires null charge with matched
minima. Its vanished curvature components have real product
bidegrees (2,0) and (1,1); they are not Dolbeault components.
Thus ordinary HYM type (1,1) does not supply that lemma's conclusion
or its missing topological premise. The determinant passage puts us
in the source's SU(r) scope without using its general U(r) energy
formula. No reproof of its exclusion or splitting theorem is needed.

F existence and the universal primitive-Hodge gap are unchanged;
separation, ambient extension, reconstruction and transport are
still unresolved. This audit neither reopens the energy test nor
asserts any Spin(7) instanton equation.

## Mathlib

Full matching coverage for the normalized instanton/alpha-charge
criterion was not checked. Unknown availability is not absence. The
informal specialization uses the precisely cited primary theorem and
the explicit cup-product calculation above; no formal verification is
claimed.
