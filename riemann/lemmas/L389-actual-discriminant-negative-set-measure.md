# Lemma 389: quantitative measure of the physical negative-discriminant set

## Hypotheses

Use the fixed actual functions F=F_0,G and positive common envelope A
of L366, with the physical discriminant and normalization of L370/L388.
For t>=40 put T=1+t, L=log(2+t), and use ordinary real derivatives:

\[
 A=(t^2+1/4)|\Gamma(1/4+it/2)|\pi^{-1/4},\qquad
 P_j=\frac{F^{(j)}}{AL^j},\quad
 V_j=\frac{G^{(j)}}{AT^2L^j}\quad(0\le j\le2),
\]
\[
 \mathscr L(u)=u'^2-uu'',\quad B_*=2F'G'-FG''-F''G,
 \quad D=B_*^2-4\mathscr L(F)\mathscr L(G),\quad
 \Delta=\frac{D}{A^4T^4L^4}.
\]

All functions are fixed as the real height H tends to infinity. No RH,
simplicity, noncoincidence, independent phases, eventual discriminant
sign or common-zero count hypothesis is imposed.

## Conclusion

There are fixed finite constants C>0, c>0 and H_0>=40 such that, for
every real H>=H_0,

\[
 \frac1H\int_H^{2H}|\Delta(t)|^2\,dt\le C(\log H)^4,
 \qquad
 \operatorname{meas}\{t\in[H,2H]:D(t)<0\}
       \ge \frac{cH}{(\log H)^2}.                         \tag{1}
\]

Constants and onset are existential, not numerically evaluated. This
quantifies L388's negative-point conclusion. It establishes neither
eventual D<=0 nor control of the positive part, response-grid visits,
common-zero upper counts, a total L367 pencil margin, or RH.

## Proof

This is a **REPRODUCTION** under the prior SPECIALIZE assessment
`drafts/literature/2026-10-10-negative-discriminant-set-measure.md`.
The analytic moment theorem and concentration inequality are imported;
the work here is their application to the complete physical jets. No
new derivative-moment theorem or novelty beyond the checked sources
is claimed.

**Known input.** H. M. Bui and R. R. Hall, *On the derivatives of
Hardy's function Z(t)*, arXiv:2304.05178v1 (11 April 2023),
[Theorem 3 and its preceding defining asymptotic](https://arxiv.org/html/2304.05178v1),
give unconditional fixed-order fourth product moments. Taking all four
orders equal to j gives the needed upper bound

\[
 \int_0^X |Z^{(j)}(t)|^4\,dt
      \ll_j X(\log X)^{4j+4}\quad(j=0,1,2),              \tag{2}
\]

for sufficiently large X. Here Z(t)=e^{i\theta(t)}\zeta(1/2+it)
is their real Hardy function, with ordinary derivatives; its continuous
phase satisfies

\[
 e^{2i\theta(t)}=
 \pi^{-it}\frac{\Gamma(1/4+it/2)}{\Gamma(1/4-it/2)}.
\]

No growing derivative order is used. The source asymptotic has a finite
leading coefficient and an error of one lower logarithmic degree, so
its upper-bound consequence (2) needs no coefficient evaluation.
Their equations (3)--(4) use Cauchy--Schwarz on a sign set; we import
that inequality below. We do not import their sign proportions for
Hardy products as proportions for D. Reproving their moment theorem
would serve no purpose; the normalization application is necessary.

**Hardy identification and full envelope.** Set s=1/4+it/2,
p=t^2+1/4, Q=p\Gamma(s)\pi^{-s}, and choose a smooth phase \phi
with Q=Ae^{i\phi} on the positive ray. The positive p contributes no
phase. Gamma conjugation gives

\[
 (Q/A)^2=\pi^{-it}\frac{\Gamma(s)}{\Gamma(\bar s)}
         =e^{2i\theta(t)}.
\]

Both phase factors are continuous and nonzero, so their quotient is a
single constant \sigma in {1,-1} on this connected ray. This comparison
does not divide by zeta and remains valid at its zeros. L366 (1) and
the reality of the completion on the critical line give exactly

\[
 f:=F/A=-e^{i\phi}\zeta(1/2+it)=-\sigma Z(t).
                                                               \tag{3}
\]

Consequently all ordinary derivatives f^(j) have the same constant-sign
relation to Z^(j). Introduce a=A'/A and q=(log A)''. Product
differentiation, retaining both envelope derivatives, gives

\[
 P_0=f,\qquad
 P_1=\frac{f'}L+\frac aL f,\qquad
 P_2=\frac{f''}{L^2}+2\frac aL\frac{f'}L
                   +\frac{a^2+q}{L^2}f.                    \tag{4}
\]

These are values of normalized physical derivatives. No derivative of
L or T is suppressed: neither divisor is differentiated in their
definition or in (4).

For completeness the envelope terms have exact formulas, with
\Psi=\Gamma'/\Gamma,

\[
 a=\frac{2t}{p}-\frac12\operatorname{Im}\Psi(s),\qquad
 q=\frac2p-\frac{4t^2}{p^2}
                      -\frac14\operatorname{Re}\Psi'(s).   \tag{5}
\]

In particular this is the full envelope, including its rational factor,
not just the gamma modulus. L366 (12) gives |Q'/Q|<=B_1 L. Since
a=Re(Q'/Q), it implies |a|/L<=B_1 on t>=40. The audited L370 (5)
gives |q|<=K_q/T^2. As L>1, all coefficients in (4) are bounded
uniformly, including |a^2+q|/L^2<=B_1^2+K_q. We need no
differentiation of an asymptotic remainder and no relative curvature
estimate.

On [H,2H], L>=log H. The nonnegative integral in (2) may be
restricted to [H,2H] by bounding it by the integral up to 2H. For
H sufficiently large, log(2H)<=2 log H. From (2)--(3), for r=0,1,2,

\[
 \int_H^{2H}\left|\frac{f^{(r)}(t)}{L(t)^r}\right|^4dt
 \le (\log H)^{-4r}\int_0^{2H}|Z^{(r)}(t)|^4dt
 \ll_r H(\log H)^4.                                     \tag{6}
\]

Thus no signed sharp subtraction or additional weight theorem is
needed. Applying |x_1+...+x_m|^4<=m^3 sum |x_i|^4 to (4), with
the uniformly bounded coefficients just proved, yields fixed C_j with

\[
 \int_H^{2H}|P_j(t)|^4dt\le C_jH(\log H)^4
                    \quad(j=0,1,2).                      \tag{7}
\]

**Complete discriminant budget.** L366 (2) gives the fixed bounds
|V_j|<=D_j for all t>=40 and j=0,1,2. These are bounds for the
complete response, not a finite Dirichlet head. Choose
K=max(1,D_0,D_1,D_2). By the exact zero-safe polynomial L370 (3),

\[
 \Delta=(P_0V_2-P_2V_0)^2
       -4(P_0V_1-P_1V_0)(P_1V_2-P_2V_1).                  \tag{8}
\]

All envelope terms are included through the physical P_j,V_j; there
is no additional omitted q correction in (8). In particular we never
replace G/A by G/(AT^2) inside differentiated minors.
Let U=P_0^2+P_1^2+P_2^2. Each of the three minors in (8) is at
most sqrt(2)K sqrt(U) in absolute value, because
|P_iV_j-P_jV_i|<=K(|P_i|+|P_j|). Therefore

\[
 |\Delta|\le10K^2U,\qquad
 |\Delta|^2\le100K^4U^2
             \le300K^4\sum_{j=0}^2|P_j|^4.               \tag{9}
\]

Combining (7) and (9) proves the first inequality of (1), with for
example C=300K^4(C_0+C_1+C_2)>0. Every term meets the required
log^4 H budget. These pointwise bounds allow arbitrary vanishing jets.

**Measure application.** Set
\alpha=\zeta(5)\zeta(3)^2/(240\pi^2\zeta(6))>0.
The audited all-real-H conclusion of L388 gives, after increasing
H_0 if necessary,

\[
 -\int_H^{2H}\Delta(t)\,dt
       \ge \frac\alpha2 H\log H\quad(H\ge H_0).          \tag{10}
\]

Let E_H={t in [H,2H]:Delta(t)<0}. The functions are smooth and A
is positive, so E_H is measurable and the relevant integrals are finite.
Decompose the signed integral. Its positive part is nonnegative, hence

\[
 \int_{E_H}(-\Delta(t))dt
   \ge-\int_H^{2H}\Delta(t)dt
   \ge\frac\alpha2H\log H.
\]

Cauchy--Schwarz on E_H and the first part of (1) imply

\[
 \left(\frac\alpha2H\log H\right)^2
 \le \left(\int_{E_H}(-\Delta)\right)^2
 \le\operatorname{meas}(E_H)\int_{E_H}|\Delta|^2dt
 \le\operatorname{meas}(E_H)\,CH(\log H)^4.
\]

Dividing by the positive final factor gives
meas(E_H)>=\alpha^2 H/(4C(log H)^2). Since A^4T^4L^4>0,
E_H is exactly the physical D<0 set, proving (1) with
c=\alpha^2/(4C). Closed endpoints have measure zero. All thresholds
come from fixed constants and all-height estimates, so their maximum
works for every sufficiently large real H, not merely a subsequence.

This argument uses the complete negative mean, not a pointwise sign
assumption. It allows positive discriminant values elsewhere. It says
nothing about intersection with a discrete response grid or about
common zeros, which may occur at D=0. It preserves the stopped grid
and sharp-source routes. The result remains a partial local
known-source specialization and requires a separate critical audit. ∎

### Separate critical audit — 2026-10-10

The prior SPECIALIZE assessment
`drafts/literature/2026-10-10-negative-discriminant-measure-audit.md`
approves this REPRODUCTION audit. The original proof's pending-audit
qualification is discharged here for (1), with unchanged hypotheses
and conclusions. Bui–Hall v1, Theorem 3 and its defining asymptotic,
are imported as precisely cited above, using the previously inspected
ordinary fixed-order cases. No moment theorem is reproved or extended.

**Phase and ordinary derivatives.** L366 (1) identifies
F=-Re[Q zeta(1/2+it)], and its real completion identity makes the
quantity inside Re real. The positive factor p in Q has no phase.
The ratio (Q/A)/exp(i theta) is continuous, takes values in {1,-1},
and therefore is constant on the whole connected positive ray.
Neither this ratio nor its constancy uses a nonvanishing zeta value.
Thus f=-sigma Z and f^(r)=-sigma Z^(r) for r=0,1,2, including at
zeros and across any zero multiplicities. The source's moments of
four equal ordinary derivatives are |Z^(r)|^4 because Z is real.

Direct product differentiation gives F'=A(f'+af) and
F''=A[f''+2af'+(a^2+q)f]. Differentiating the exact log A gives
both formulas (5): d log|Gamma(s)|/dt=-Im Psi(s)/2 and
d[-Im Psi(s)/2]/dt=-Re Psi'(s)/4. The rational terms from log p
are retained. L366 (12) implies |a|<=B_1 L since a=Re(Q'/Q).
The audited L370 bound gives |q|<=K_q/T^2 on the entire ray.
These verify every coefficient in (4), including the second-order
coefficient bounded by B_1^2+K_q. P_j and V_j are defined by
division after differentiation; neither (4) nor (8) differentiates
a power of L or T. No derivative of an asymptotic error is taken.

**Uniform moment constants and response.** To make uniformity explicit,
choose finite positive M_r and X_r such that the imported (2) is at
most M_r X(log X)^(4r+4) for X>=X_r, r=0,1,2. For
H>=max(40,X_0/2,X_1/2,X_2/2), (6) is bounded by
J_r H(log H)^4, where J_r=2^(4r+5)M_r. This follows from
the nonnegative restriction to [0,2H], L(t)>=log H and
log(2H)<=2 log H, so is valid for every real H above that threshold.
For example, valid fixed constants in (7) are

\[
\begin{aligned}
C_0&=J_0,\\
C_1&=8(J_1+B_1^4J_0),\\
C_2&=27[J_2+16B_1^4J_1+(B_1^2+K_q)^4J_0].
\end{aligned}
\]

All three full physical response jets are covered by the second
inequality of L366 (2). Its constants D_j are independent of height
and regulator; the response itself is fixed. Consequently K is a
single finite bound for V_0,V_1,V_2, with no Euler-series truncation
or response-phase independence assumption.

**Full polynomial and divisor.** Independently put
(x,y,z)=(P_0,P_1,P_2) and (u,v,w)=(V_0,V_1,V_2). The physical
definition divided by A^4T^4L^4 is
(2yv-xw-zu)^2-4(y^2-xz)(v^2-uw). Its complete expansion is

\[
x^2w^2+z^2u^2-2xzuw-4xyvw+4xzv^2+4y^2uw-4yzuv.
\]

Expanding (xw-zu)^2-4(xv-yu)(yw-zv) gives exactly those same
seven terms, checking (8) including zero jets. Each minor has absolute
value at most sqrt(2)K sqrt(U). The squared first minor costs
2K^2U and four times the product costs 8K^2U. Hence the factors
10,100,300 in (9) are valid, the last using
U^2<=(1+1+1)(x^4+y^4+z^4). Thus
C=300K^4(C_0+C_1+C_2) works for the complete second moment.
There is no separate curvature term to add to the physical polynomial:
q has already been retained in the physical jets.

**Signed set and all-H conclusion.** L388 has precisely the same
fixed Delta, positive divisor and dt/H normalization. Its all-real-H
little-o error is eventually at most (alpha/2)log H in absolute
value, giving (10). If I_- is the integral of -Delta on E_H and
I_+ is the integral of Delta on its complement, then
-integral Delta=I_--I_+<=I_-. All are finite by continuity on
the compact interval, and I_+>=0; this is the direction needed in
the displayed Schwarz chain. The established square integral then
gives meas(E_H)>=alpha^2 H/[4C(log H)^2]. The divisor is strictly
positive for t>=40, so E_H is exactly {D<0}; its endpoints cannot
affect its measure. The maximum of the finite moment thresholds,
the L388 threshold and 40 supplies one fixed H_0. No subsequence,
uniform zero-multiplicity estimate or extra sign hypothesis enters.

The audit finds no defect, changed bound or new dependency. Conclusion
(1) passes unchanged as a partial known-source application. This
verification is not a new moment result or a stronger negative-set
estimate. The lower proportion c/(log H)^2 tends to zero; neither
a positive limiting proportion nor eventual D<=0 follows. Positive
values elsewhere, a discrete grid missing E_H, and common zeros on
D=0 remain compatible with the proof. The main positivity, total
pencil margin and actual common-zero upper-count gaps remain open.

## Mathlib

Full matching Hardy derivative-moment and actual discriminant measure
coverage is **not checked**. Supporting Hölder inequalities were
inspected in the reused assessment: see
[Mathlib's Holder documentation](https://leanprover-community.github.io/mathlib4_docs/Mathlib/MeasureTheory/Function/Holder.html),
including `MeasureTheory.Lp.norm_smul_le` and
`MeasureTheory.eLpNorm_le_enorm_mul_eLpNorm_mul_eLpNorm`.
That supporting coverage does not establish (2) or its complete actual
jet application. No Lean verification or library absence is claimed.
