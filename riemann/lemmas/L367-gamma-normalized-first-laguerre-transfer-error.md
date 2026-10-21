# Lemma 367: gamma-normalized first-Laguerre comparison with the first regulator response

**Hypotheses.** Use the actual real Fourier family F_ε and F_0 of
L357, the positive envelope A of L358 and the audited response G of
L366. Thus

\[
 A(\xi)=(\xi^2+\tfrac14)
       |\Gamma(\tfrac14+\tfrac{i\xi}{2})|\pi^{-1/4}>0,
 \qquad T=1+|\xi|,\quad L=\log(2+|\xi|).
\]

Work on |ξ|≥40 and 0<ε≤1/(1+ξ²). All primes and frequency
derivatives below hold ε fixed, even when evaluating on a curve
ε=ε(ξ). Let C_j,D_j, j=0,1,2, be the absolute constants in L366
(2); their numerical values are not evaluated. Put

\[
 \delta=\varepsilon T^2\le2,\qquad
 H=F_0+\varepsilon G,\qquad R=F_\varepsilon-H,
\]
\[
 P_j=\frac{F_0^{(j)}}{A L^j},\qquad
 V_j=\frac{G^{(j)}}{A T^2 L^j},\qquad
 X_j=\frac{H^{(j)}}{A L^j}=P_j+\delta V_j.
 \tag{1}
\]

These are real derivative values divided by A, not derivatives of
F_0/A or H/A. In particular no envelope derivative is discarded.
Write \(\mathcal L(f)=f'^2-ff''\) and
\(\ell_f=\mathcal L(f)/(A^2L^2)\), using this same divisor for
all f at the comparison point.

**Conclusion.** Define

\[
 \begin{aligned}
 \mathcal B&=2P_1V_1-P_0V_2-P_2V_0,\\
 \mathcal C&=V_1^2-V_0V_2,\\
 \mathcal E_H&=\delta^2
       (2C_1|X_1|+C_2|X_0|+C_0|X_2|)
       +\delta^4(C_1^2+C_0C_2).
 \end{aligned}                                                   \tag{2}
\]

Uniformly on the stated domain, including zeros of F_0 or H,

\[
 \ell_H=\ell_{F_0}+\delta\mathcal B+\delta^2\mathcal C,
 \qquad |\ell_{F_\varepsilon}-\ell_H|\le\mathcal E_H.
 \tag{3}
\]

Equivalently the error divided by A², without the extra L² scaling,
is at most

\[
 \delta^2\left(
    2C_1L\frac{|H'|}{A}
    +C_2L^2\frac{|H|}{A}
    +C_0\frac{|H''|}{A}\right)
    +\delta^4(C_1^2+C_0C_2)L^2.                       \tag{4}
\]

For either sign σ∈{−1,1}, sufficient strict sign margins are

\[
 \begin{aligned}
 \sigma\ell_H>\mathcal E_H
       &\ \Longrightarrow\ \sigma\ell_{F_\varepsilon}>0,\\
 \sigma\ell_{F_\varepsilon}>\mathcal E_H
       &\ \Longrightarrow\ \sigma\ell_H>0,\\
 \sigma(\ell_{F_\varepsilon}-\delta\mathcal B-\delta^2\mathcal C)
       >\mathcal E_H
       &\ \Longrightarrow\ \sigma\ell_{F_0}>0,\\
 \sigma(\ell_{F_0}+\delta\mathcal B+\delta^2\mathcal C)
       >\mathcal E_H
       &\ \Longrightarrow\ \sigma\ell_{F_\varepsilon}>0.
 \end{aligned}                                                   \tag{5}
\]

A sign-insensitive sufficient transfer threshold between F_ε and F_0
is \(\mathcal E_H+|\delta\mathcal B+\delta^2\mathcal C|\).
No assertion that any required margin holds is made.

There are absolute constants K,K′ for this family such that

\[
 \mathcal E_H\le K\delta^2T^{1/2},\qquad
 |\ell_{F_\varepsilon}-\ell_{F_0}|
       \le K'\delta T^{1/2}.                              \tag{6}
\]

Consequently, for any fixed α>1/4, uniformly over
0<ε≤T^(−2−α),

\[
 \frac{|\mathcal L(F_\varepsilon)-\mathcal L(H)|}{A^2}
       =O(T^{1/2-2\alpha}L^2)=o(1)
       \quad (|\xi|\longrightarrow\infty).                \tag{7}
\]

For any fixed α>1/2 on the same type of subdomain,

\[
 \frac{|\mathcal L(F_\varepsilon)-\mathcal L(F_0)|}{A^2}
       =O(T^{1/2-\alpha}L^2)=o(1).                        \tag{8}
\]

These are sufficient regimes from a coarse unconditional growth
estimate, not optimal thresholds. They do not give relative errors
against an unknown sign margin, or vanishing errors at ε≈ξ^(−2).

**Proof.** This is a **REPRODUCTION** of the product subtraction
already used in L357, specialized to L366's uniform remainder and
the positive L358 normalization. The cited inputs are unconditional
analytic estimates; L358's finite arithmetic certificates are not
used. No new contour displacement or real-zero premise is needed.

Set W_j=R^(j)/(A L^j). By L366 (2),

\[
 |W_j|\le C_j\delta^2,\qquad |V_j|\le D_j.           \tag{9}
\]

At the fixed comparison point, the three normalized jets of F_ε
are X_j+W_j. Exact multiplication gives

\[
 \ell_{F_\varepsilon}-\ell_H
   =2X_1W_1+W_1^2-X_0W_2-X_2W_0-W_0W_2.             \tag{10}
\]

Taking absolute values and using (9) proves (2)–(4). In particular
the two products of remainder jets contribute the δ⁴ term; they
cannot be dropped at the upper boundary. Expanding
(P_1+δV_1)²−(P_0+δV_0)(P_2+δV_2) proves the first identity in
(3). In unnormalized form its response is exactly

\[
 \mathcal L(H)=\mathcal L(F_0)
   +\varepsilon(2F_0'G'-F_0G''-GF_0'')
   +\varepsilon^2(G'^2-GG'').                             \tag{11}
\]

Thus neither the signed cross term nor the quadratic response has
been estimated away in (5). Each implication there follows by
subtracting an error of absolute value at most E_H from a strict
margin. The sign-insensitive threshold follows from the triangle
inequality applied to (3). All denominators are positive; this
argument also applies at zeros and uses no derivative lower bound.

For a concrete unconditional shrinking regime, specialize the
already proved strip estimate L320 (4) at its strip parameter R=1.
Distinguish that fixed strip parameter from the remainder R above.
Fix η=3/4 in L320, so its full hypothesis R>η>1/2 holds;
the strip argument itself needs only 1/2+R=3/2>1. Both parameters
are fixed independently of ε and ξ. It gives

\[
 |\xi_c(\sigma+it)|\le B_1(2+|t|)^{9/4}e^{-\pi|t|/4},
             \qquad -1/2\le\sigma\le3/2.                 \tag{12}
\]

L366 identifies F_0(ξ)=2ξ_c(1/2+iξ). Apply Cauchy's derivative
estimate to the entire function z↦2ξ_c(1/2+iz) on the circle
|z−ξ|=1/4. On that circle the completion has real part between
1/4 and 3/4, hence lies inside (12); its imaginary part differs
from ξ by at most 1/4. In particular
e^(−π|Im(1/2+iz)|/4)≤e^(π/16)e^(−π|ξ|/4), and its polynomial
factor is at most a constant times T^(9/4). Cauchy's bound with
factor j!4^j therefore proves, for j=0,1,2,

\[
 |F_0^{(j)}(\xi)|\le E_j^*T^{9/4}e^{-\pi|\xi|/4}.
 \tag{13}
\]

The vertical gamma estimate already used in L320 and L358 gives

\[
 A(\xi)\ge a_*T^{7/4}e^{-\pi|\xi|/4},\qquad |\xi|\ge40,
                                                        \tag{14}
\]

for an absolute a_*>0. Explicitly the scalar Stirling modulus at
1/4+iξ/2 is asymptotic to
sqrt(2π)(|ξ|/2)^(−1/4)e^(−π|ξ|/4). Multiplication by
(ξ²+1/4)π^(−1/4) proves (14) at large |ξ|. On the remaining
compact real-frequency range its ratio to the stated lower scale
is continuous and strictly positive, so reducing a_* extends it
to |ξ|≥40. This uses the scalar complex Stirling estimate with
its vertical sector, as in L320: NIST
[DLMF 5.11.3](https://dlmf.nist.gov/5.11.E3) and
[5.11.9](https://dlmf.nist.gov/5.11.E9). No new gamma theorem or
critical-line lower bound is being asserted.

Dividing (13) by (14) proves

\[
 |P_j|\le E_jT^{1/2}L^{-j}.                           \tag{15}
\]

Since L>1, δ≤2, and |V_j|≤D_j, (1) gives
|X_j|≤E_j T^(1/2)+2D_j. Hence the δ² coefficient in E_H is
bounded by a constant times T^(1/2). Also δ⁴≤4δ² and T^(1/2)≥1.
This proves its first bound in (6). Equations (2), (9) and (15)
give |B|≤K_B T^(1/2) and |C|≤D_1²+D_0D_2. Applying (3) yields

\[
 |\ell_{F_\varepsilon}-\ell_{F_0}|
 \le K_B\delta T^{1/2}
       +(D_1^2+D_0D_2)\delta^2+K\delta^2T^{1/2}
 \le K'\delta T^{1/2},
\]

where δ≤2 absorbs both quadratic terms. This proves (6).
To make the uniformity explicit, put M_j=E_j+2D_j and choose

\[
 \begin{aligned}
 K&=2C_1M_1+C_2M_0+C_0M_2+4(C_1^2+C_0C_2),\\
 K_B&=2E_1D_1+E_0D_2+E_2D_0,\qquad
 K_C=D_1^2+D_0D_2,\\
 K'&=K_B+2K_C+2K.
 \end{aligned}
\]

Here |X_j|≤M_j T^(1/2), δ⁴≤4δ², and δ²≤2δ;
these choices depend only on the fixed input constants. They do
not depend on a choice of regulator curve or on any transform value.
The subdomain ε≤T^(−2−α) lies inside the original domain, since
T²≥1+ξ². There δ≤T^(−α). Multiply (6) by L² to recover
the error divided only by A². The negative polynomial exponents
in (7) and (8) dominate L², proving both o(1) assertions. ∎

The achieved output is a controlled conditional margin, with a
quantitative shrinking-regulator comparison. Neither an actual
positive margin for H nor control of the signed response sufficient
to establish positivity of F_0 is known. The common global-first-sign
certificate stopped by L365 is not reopened: its negative signs are
at fixed regulator with a regulator-dependent onset, whereas this
lemma restricts the frequency-regulator relation. Higher levels,
the remaining low-index signs and heights above forty remain open.
No RH candidate or new sign range follows. No originality beyond
the sources checked is claimed.

**Critical audit, 2026-10-05.** The full statements (3)–(8) survive
with their original domain and sufficient exponents. The fixed η
above discharges L320's statement hypotheses; the entire completion,
circle radius 1/4, height change at most 1/4 and factor exp(π/16)
justify (13). The gamma lower bound (14) is independent of the
critical-line zeta value. The displayed choices of K and K′ verify
global uniformity after dividing by the positive A and L.

For clarity about every signed implication, set
d=ell_(F_ε)−ell_H and q=δB+δ²C. Then |d|≤E_H and
ell_(F_ε)−q=ell_(F_0)+d. For either σ, subtracting σd costs at
most E_H. This proves both directions in (5), without any sign
assumption on q. At F_0=0 the expression ell_(F_0)=P_1² remains
defined, and at H=0 it is ell_H=X_1²; neither case requires
deflation or a logarithmic derivative of a vanishing function.

All jet identities hold with ε fixed. In particular one must not
differentiate δ(ξ), P_j or V_j to construct the next jet, nor
interpret H′ as the derivative of F_0(ξ)+ε(ξ)G(ξ) along a curve.
The curve only selects points at which already computed fixed-ε
jets are evaluated. Multiplication by L², rather than its omission,
is essential in (7)–(8). At α=1/4 or α=1/2, respectively, the
stated estimates give only O(L²), so no endpoint o(1) is certified.
At the original upper regulator boundary they likewise give no
vanishing bound. This audit validates a conditional comparison;
it establishes no signed margin and no stronger positivity claim.

**Mathlib.** Full coupled nonlinear comparison and sign-margin
specialization: **not checked**. The supporting Poisson and smooth
series coverage recorded in L357–L366 addresses the family and
derivative interchanges, not this complete statement. Cauchy,
complex Stirling and normalized algebra coverage were not looked
up here; unknown coverage is not evidence of absence.
