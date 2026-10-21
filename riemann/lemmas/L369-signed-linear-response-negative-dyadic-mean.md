# Lemma 369: a negative dyadic mean for the signed linear response

**Hypotheses.** Use the actual functions F_0 and G of L366, the positive
A of L358 and the signed coefficient of L367. For real t set

\[
 T=1+|t|,\qquad L=\log(2+|t|),\qquad
 \mathcal B(t)=\frac{2F_0'(t)G'(t)-F_0(t)G''(t)-G(t)F_0''(t)}
                         {A(t)^2T^2L^2}.
 \tag{1}
\]

Primes denote ordinary real frequency derivatives; this is exactly
L367's coefficient, with no positive regulator or differentiation along
a regulator curve. No zero hypothesis is imposed. All asymptotic constants
below refer to this fixed family and are independent of H.

**Conclusion.** As H tends to infinity,

\[
 \frac1H\int_H^{2H}\mathcal B(t)\,dt
    =-\frac{\zeta(3)}{4\pi}
       +O\left(\frac1{\log H}+H^{-1/2}(\log H)^2\right).
 \tag{2}
\]

Consequently there is a finite, unevaluated H_0 such that every H≥H_0
admits t_H in [H,2H] with

\[
 \mathcal B(t_H)\le-\frac{\zeta(3)}{8\pi}<0.
 \tag{3}
\]

The coefficient is even, so the same assertion holds on the reflected
intervals. This rules out eventual nonnegativity of this individual linear
coefficient. It neither signs the total comparison in L367 nor establishes
any actual-theta Laguerre sign, off-line zero, regulator-uniform onset or RH
candidate. The separate critical audit described below validates this
statement with its original constant and error.

**Proof.** This is a **REPRODUCTION** specializing the scalar truncation,
functional equation and gamma inputs covered by the saved linear-response
assessment. No inspected source states this mixed signed conclusion; the
family-specific algebra and mean estimate are proved below. No originality
beyond the sources checked is claimed.

### Exact projections and envelope curvature

For t>0 put

\[
 s=\tfrac14+it/2,\quad p=t^2+\tfrac14,\quad
 Q=p\Gamma(s)\pi^{-s}=A e^{i\phi},\quad
 U=\zeta(1/2+it),\quad Z=\zeta(5/2+it),
\]
\[
 b=-\frac{s(s+1/2)}\pi
    =\frac{t^2/4-3/16-it/2}\pi,\qquad W=bZ,
 \quad\omega=\phi',\quad q=(\log A)''.
 \tag{4}
\]

A smooth phase exists on the positive ray because Q never vanishes.
L366 gives F_0=−Re(QU)=2ξ_c(1/2+it). In fact QU=−2ξ_c(1/2+it)
is real: in L018's completion formula,
(1/2+it)(−1/2+it)=−p, and reflection and conjugation make the completion
real on this line. Thus, without dividing by U,

\[
 r=e^{i\phi}U\in\mathbb R,\qquad
 e^{2i\phi}U=\overline U,\qquad F_0=-Ar.
 \tag{5}
\]

The reflected response and gamma recurrence in L368 (3) give
G=A Re(e^{iφ}W). L358's scalar gamma estimates, or its exact digamma
formulas with separately controlled polygamma remainders, give uniformly
on the positive ray at large t

\[
 \omega=\tfrac12\log(t/(2\pi))+O(t^{-2}),\quad
 \omega'=O(t^{-1}),\quad q=O(t^{-2}).
 \tag{6}
\]

These concern the phase of Q, not Qb. The covered inputs are
[DLMF 5.11.2](https://dlmf.nist.gov/5.11#E2), the remainder qualifications
in [§5.11(ii)](https://dlmf.nist.gov/5.11#ii), and the separate polygamma
expansion [5.15.8](https://dlmf.nist.gov/5.15#E8). The arguments
1/4+it/2 lie in a closed sector away from the negative real axis.
In particular q includes the p factor and the gamma modulus; no
uncontrolled asymptotic error is differentiated.

More explicitly, with Ψ=Γ′/Γ and the separately controlled expansion
Ψ′(s)=1/s+1/(2s²)+O(t⁻³), the exact formulas for this carrier are

\[
 \omega=\tfrac12(\operatorname{Re}\Psi(s)-\log\pi),\qquad
 \omega'=-\tfrac14\operatorname{Im}\Psi'(s),\qquad
 q=\frac2p-\frac{4t^2}{p^2}-\tfrac14\operatorname{Re}\Psi'(s).
\]

Here Re(1/s)=O(t⁻²), so the last estimate in (6) follows with
the full envelope. No phase or curvature of b is inserted into these
formulas; b is differentiated explicitly in (11).

For real f,g the direct product identity is

\[
 \frac{2(Af)'(Ag)'-(Af)(Ag)''-(Ag)(Af)''}{A^2}
       =2f'g'-fg''-gf''-2qfg.
 \tag{7}
\]

It follows by expansion; the terms involving A'/A cancel. Apply it with
f=−r and g=Re(e^{iφ}W), moving real derivatives through the projection.
Differentiating e^{iφ}U and e^{iφ}W, then canceling the ω² and mixed ω
terms inside their polarization, gives for its unscaled numerator

\[
 -\operatorname{Re}\left[e^{2i\phi}
   \{2U'W'-UW''-WU''-2(i\omega'+q)UW\}\right].
 \tag{8}
\]

This expression retains the sum-phase terms; they are not discarded by
oscillatory intuition.

To check the projection factor, put h=e^(iφ)W. Since r, r′ and r″
are real, the right side of (7) with f=−r and g=Re h is exactly
−Re(2r′h′−rh″−hr″−2qrh), with no factor 1/2. The expression
inside this real part is e^(2iφ) times the braces in (8). In particular
the critical-line reality was used before replacing products of real
parts; discarding a sum-phase term would give an incorrect constant.

Differentiating (5) gives

\[
 \begin{aligned}
 e^{2i\phi}U'&=\overline U'-2i\omega\overline U,\\
 e^{2i\phi}U''&=\overline U''-4i\omega\overline U'
                         -(2i\omega'+4\omega^2)\overline U.
 \end{aligned}
 \tag{9}
\]

Here \(\overline U'=(\overline U)'\), and similarly for the second jet.
Substitution into (8) is exact and cancels its remaining ω' terms. After
W=bZ is expanded, equation (1) becomes

\[
 \mathcal B=-\frac{\operatorname{Re}\{bK+R\}}{T^2L^2},
 \tag{10}
\]
\[
 \begin{aligned}
 K={}&2\overline U'Z'-\overline U Z''-\overline U''Z
       +4i\omega(\overline U'Z-\overline U Z')
       +4\omega^2\overline U Z,\\
 R={}&b'(2\overline U'Z-2\overline U Z'-4i\omega\overline U Z)
             -b''\overline U Z-2bq\overline U Z.
 \end{aligned}
 \tag{11}
\]

Thus both projections and the full envelope curvature are accounted for,
including at zeros of F_0 or G. This use of the functional equation is an
exact identity on the critical line, not an assumption that its zeros are
all the zeros of zeta.

### Fixed-cutoff jet input

Import J. Arias de Reyna, *On the approximation of the zeta function by
Dirichlet polynomials*, arXiv:2406.16667v1 (2024-06-24),
[Theorem 6 and proof, pp. 5–6](https://arxiv.org/pdf/2406.16667v1#page=5):
for fixed real x>0, s_1=σ+iτ, σ≥0 and 0<τ≤x,

\[
 \left|E_x(s_1)\right|\le\frac{29}{14}x^{-\sigma},\qquad
 E_x(s_1)=\zeta(s_1)-\sum_{n\le x}n^{-s_1}
                         -\frac{x^{1-s_1}}{s_1-1}.
 \tag{12}
\]

The scalar approximation is imported, not reproved. Set x=3H once for
the entire interval [H,2H], with H sufficiently large, and N=⌊x⌋.
For every center 1/2+it use a complex disk of radius
ρ=min(1/4,1/log x). Every point has real part at least 1/2−ρ>0 and
imaginary part between H−1/4 and 2H+1/4, hence between 0 and x.
The analytic difference E_x has no pole on these disks. Equation (12)
bounds it there by C x^(−1/2), because x^ρ≤e. Cauchy's derivative
estimate therefore yields, for a=0,1,2, a uniform bound
C_a H^(−1/2)(log H)^a for its a-th complex derivative, and hence for
its a-th frequency derivative at the center.

The pole correction is also retained. Its exact complex derivatives are

\[
 \frac{d^a}{ds_1^a}\frac{x^{1-s_1}}{s_1-1}
 =x^{1-s_1}\sum_{k=0}^a\binom ak
          (-\log x)^{a-k}\frac{(-1)^k k!}{(s_1-1)^{k+1}}.
\]

At 1/2+it, |s_1−1|≥H and |x^(1−s_1)|=√x, so these have the
same bounds. Frequency derivatives introduce only factors i^a.
Consequently

\[
 U^{(a)}(t)=\sum_{n\le N}(-i\log n)^a n^{-1/2-it}
             +O\big(H^{-1/2}(\log H)^a\big),\qquad 0\le a\le2,
 \tag{13}
\]

uniformly on [H,2H]. In particular
\(|U^{(a)}|\le C\sqrt H(\log H)^a\). No real-variable O term was
differentiated and no moving cutoff was differentiated.

The series in L368 (5), citing [DLMF 25.2.1](https://dlmf.nist.gov/25.2#E1)
on its domain Re v>1, gives

\[
 Z^{(c)}(t)=\sum_{m\ge1}(-i\log m)^c m^{-5/2-it},\qquad
 |Z^{(c)}|\le\sum_{m\ge1}(\log m)^c m^{-5/2}<\infty,
 \quad 0\le c\le2.
 \tag{14}
\]

Local uniform absolute convergence justifies these derivatives. At n=1
or m=1 the zeroth power is 1 and each positive log power is zero.

### Weighted mixed means and all off-diagonal terms

Write ⟨h⟩_H=H^(−1)∫_H^(2H)h(t)dt. For any complex C¹ weight w on
this interval satisfying

\[
 \sup|w|+\int_H^{2H}|w'(t)|\,dt\le C_w,
 \tag{15}
\]

with a constant independent of H, we show, for a+c≤2,

\[
 \left\langle w\overline U^{(a)}Z^{(c)}\right\rangle_H
       =i^a(-i)^c\mu_{a+c}\langle w\rangle_H
                         +O\big(C_w H^{-1/2}(\log H)^2\big),
 \quad \mu_j=\sum_{n\ge1}\frac{(\log n)^j}{n^3}.
 \tag{16}
\]

Here \(\overline U^{(a)}\) denotes the derivative of \(\overline U\).
The three μ_j are finite and μ_0=ζ(3). Use (13) and (14). The remainder
from (13) contributes at most C C_w H^(−1/2)(log H)^a, since the
right-line jet is uniformly bounded. The remaining finite-by-infinite
product can be integrated term by term: at each H it is absolutely
summable, including its constant log powers.

All zero-frequency collisions are exactly n=m. Their contribution is
i^a(−i)^c∑_(n≤N)n^(−3)(log n)^(a+c)⟨w⟩_H. The omitted diagonal
tail is O(C_w N^(−2)(1+log N)^2), by the integral comparison for
n^(−3)(1+log n)^2. In particular the n=m=1 term is retained.

For n≠m integration by parts at the nonzero frequency log(n/m) gives

\[
 \left|\left\langle w(t)e^{it\log(n/m)}\right\rangle_H\right|
       \le\frac{2\sup|w|+\int|w'|}{H|\log(n/m)|}
       \le\frac{2C_w}{H|\log(n/m)|}.
 \tag{17}
\]

The full absolute coefficient budget is bounded as follows, with
log powers replaced by 1+log where needed:

\[
 \sum_{n\le N}\sum_{m\ne n}
 \frac{n^{-1/2}m^{-5/2}(\log n)^a(\log m)^c}
             {|\log(n/m)|}
       \le C\{1+\sqrt N(1+\log N)^2\}.
 \tag{18}
\]

To verify every range, if m≤n/2, the reciprocal denominator is at most
1/log 2 and the sum of m^(−5/2)(1+log m)^c is finite. Summing over n
costs at most C√N(1+log N)^a. If m≥2n, the same denominator bound and
∑_(m≥2n)m^(−5/2)(1+log m)^c≤C n^(−3/2)(1+log n)^c leave the
convergent sum ∑n^(−2)(1+log n)^(a+c). In the remaining range
n/2<m<2n, m≠n, the mean value theorem for log gives
|log(n/m)|≥|n−m|/(2n). The coefficient is then bounded by
C n^(−2)(1+log n)^(a+c)/|n−m|. Its m sum costs at most
C(1+log n), leaving ∑n^(−2)(1+log n)^3<∞. These arguments include
the small indices and the infinite m tail. Thus (18), (17), the diagonal
tail and the analytic remainder prove (16). There are no unhandled
sum-phase products: (9) removed them exactly before this integration.

### Actual moving weights and the sign margin

In the leading part bK of (10) take the three weights

\[
 w_k(t)=\frac{b(t)\omega(t)^k}{T(t)^2L(t)^2},\qquad k=0,1,2.
 \tag{19}
\]

They satisfy (15) with a common absolute constant. Indeed b=O(t²),
b'=O(t), ω=O(L) and ω'=O(1/t). Differentiating (19) also uses
T'=1, L'=1/(2+t); every resulting term is O(1/H) on [H,2H],
for each k≤2. The supremum is O(1), and integration over length H
bounds the total variation.

For completeness, put D=T²L², so D′/D=2/T+2/((t+2)L).
For k=0,1,2 the exact complex derivative is

\[
 w_k'=\frac{b'\omega^k}{D}
       +\frac{k b\omega^{k-1}\omega'}D
       -w_k\left(\frac2T+\frac2{(t+2)L}\right),
\]

where the middle term is absent for k=0. The first and last terms
are O(H⁻¹(log H)^(k−2)); for k≥1 the middle term is
O(H⁻¹(log H)^(k−3)). Thus the asserted bound applies to the
modulus of the complex derivative, not merely the variation of its
real part. The sharper weight sizes are

\[
 w_0=O((\log H)^{-2}),\quad w_1=O((\log H)^{-1}),\quad
 w_2=\frac1{16\pi}+O((\log H)^{-1})
 \tag{20}
\]

uniformly on the interval, as complex-valued weights. The last assertion
uses b/T²=1/(4π)+O(1/H) and ω/L=1/2+O(1/log H), both uniformly.
It includes the imaginary part of b, which is O(1/H) after division by T².

The residual R in (11) is negligible even pointwise. From (6), (13),
(14), b'=O(H), b''=O(1) and bq=O(1),

\[
 \frac{|R|}{T^2L^2}
    \le C H^{-1/2}(\log H)^{-1}
 \tag{21}
\]

on the entire interval. This explicitly covers b', b'' and the envelope
curvature; no derivative of q is required.

Apply (16) to each product in bK. The diagonal constants for (a,c)=(1,1), (0,2), (2,0),
(1,0), (0,1) are respectively μ_2, −μ_2, −μ_2, iμ_1, −iμ_1.
Equations (10)–(11) and (21) therefore give

\[
 \langle\mathcal B\rangle_H
 =-\operatorname{Re}\{4\mu_2\langle w_0\rangle_H
              -8\mu_1\langle w_1\rangle_H
              +4\mu_0\langle w_2\rangle_H\}
          +O\big(H^{-1/2}(\log H)^2\big).
 \tag{22}
\]

Equivalently its complete diagonal is

\[
 -\frac4H\int_H^{2H}\frac{\operatorname{Re}b}{T^2L^2}
                  (\mu_0\omega^2-2\mu_1\omega+\mu_2)\,dt.
\]

This is the diagonal after all projection terms have been included,
not an undifferentiated mean differentiated afterward. Inserting (20)
into (22) proves (2), including its coefficient and minus sign.

The error tends to zero. Choose H_0 so that its absolute value is at most
ζ(3)/(8π) for every H≥H_0. Then the average is at most −ζ(3)/(8π).
Continuity of B on the compact interval, with a strictly positive divisor,
ensures a minimum no greater than its average, proving (3). Such intervals
occur arbitrarily far out. Finally F_0 and G are even by L018 and L368;
their first derivatives are odd and their second derivatives are even.
A, T and L are even. Hence B is even, proving the reflected assertion. ∎

The required threshold was a fixed negative mean with vanishing errors.
The achieved limit is −ζ(3)/(4π), with both displayed errors vanishing.
The onset is not evaluated. This stops signing the linear coefficient as
eventually nonnegative but does not determine whether its negative part
can be dominated in the full comparison. L368's positive quadratic term,
L367's unsigned remainder and the unknown actual-theta margin still have
to be compared. L365's stopped common-global-regulator target is unchanged.

Critical audit completed 2026-10-05 under the separately approved
linear-response-mean-audit assessment. Equations (7)–(22) were checked
independently, including the exact factor four, both reflected jets,
analytic disks, all pole jets, all collisions and infinite tail ranges,
complex weight variation, the residual, and parity. Every estimate has
a constant uniform in H. If K bounds the error in (2) beyond a common
threshold H_*, choose H_0≥max(H_*,exp(4)) with
K(1/log H_0+H_0^(-1/2)(log H_0)^2)≤ζ(3)/(8π).
Both summands decrease for H≥exp(4), so this is one onset for every
dyadic interval, not a separate threshold for each interval. This audit
does not improve the theorem or evaluate H_0; it accepts a previously
pending local input. Its original direct mathematical inputs are unchanged.

**Mathlib.** Full signed-linear-response mean theorem: **not checked**.
The primary scalar truncation theorem, its differentiated specialization,
and matching mixed-mean coverage were not checked in Mathlib. The standard
Cauchy derivative estimate, integration by parts and absolute-series
operations are supporting tools; no full matching theorem or absence is
asserted. Zeta completion/reflection and gamma coverage are inherited only
as mathematical inputs from the cited canonical results. No numerical
arithmetic contract or mathematical script is used in this proof.
