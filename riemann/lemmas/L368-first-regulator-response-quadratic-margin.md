# Lemma 368: a uniform quadratic margin for the first regulator response

**Hypotheses.** Let G be the right regulator response in L366 (1),
with its ordinary real frequency derivatives. Use the same positive envelope

\[
 A(t)=(t^2+\tfrac14)|\Gamma(\tfrac14+it/2)|\pi^{-1/4},
 \qquad T=1+|t|,\qquad L=\log(2+|t|).
\]

No hypothesis on zeros of zeta in the critical strip is made. All
constants and the eventual onset below are independent of t; the onset
is not numerically evaluated. There is no positive regulator in this
statement: G is the derivative at regulator zero, not F_ε.

**Conclusion.** Uniformly as |t| tends to infinity,

\[
 \frac{G'(t)^2-G(t)G''(t)}{A(t)^2T^4L^2}
   =\frac{|\zeta(5/2+it)|^2}{64\pi^2}+O(L^{-1}).       \tag{1}
\]

In particular there is a finite H such that, for every |t|≥H,

\[
 G'(t)^2-G(t)G''(t)\ge c A(t)^2T^4L^2,\qquad
 c=\frac1{128\pi^2\zeta(5/2)^2}>0.                    \tag{2}
\]

This proves a positive eventual lower bound for L367's quadratic
coefficient \(\mathcal C\), namely \(\mathcal C\ge c\).
It supplies no sign for its linear coefficient, F_0, F_ε, or higher
Laguerre levels, and does not change L365's fixed-regulator stop.

**Proof.** This is a **REPRODUCTION** of carrier-phase dominance,
specializing the real-projection expansion in L358 to the response
identified in L366. The scalar inputs are the already assessed Euler
product and gamma asymptotics. The quantitative conclusion is proved
here; it is not claimed to be a theorem stated in those sources or a
discovery beyond them. We retain every envelope term and never divide by G.

First take t>0 and put
\(s=1/4+it/2\), \(v=5/2+it=2s+2\), \(p=t^2+1/4\),
\(Q=p\Gamma(s)\pi^{-s}\), and \(Z(t)=\zeta(v)\).
L366's audited reflected identity gives
\(G=-p\operatorname{Re}(\xi_c(v)/v)\).
The completed-zeta definition used there is
\(\xi_c(v)=v(v-1)\Gamma(v/2)\pi^{-v/2}\zeta(v)/2\).
At this v its factors have no poles. Gamma recurrence
\(\Gamma(s+1)=s\Gamma(s)\), already used in L366, therefore yields
the exact carrier

\[
 G(t)=\operatorname{Re}(Q(t)b(t)Z(t)),\qquad
 b(t)=-\frac{s(s+1/2)}{\pi}
      =\frac{t^2/4-3/16-it/2}{\pi}.                  \tag{3}
\]

This checks both the reflection minus sign and the completion's factor 1/2.
In particular

\[
 |b(t)|^2=\frac{(t^2/4+1/16)(t^2/4+9/16)}{\pi^2}.   \tag{4}
\]

The polynomial b has no real zero: its imaginary part vanishes only at
t=0, where its real part is nonzero. Q is also nonzero on the real axis.
Let B=|Qb|=A|b|>0, and choose a smooth phase θ on the positive half-line
so that Qb=B exp(iθ). Such a phase exists on this interval because the
carrier never vanishes; a different constant branch has the same derivatives.
Write ω=θ′ and q=(log B)″.

The right-line zeta inputs give uniform bounds without a critical-strip
premise. For j=0,1,2 put

\[
 M_j=\sum_{n\ge1}(\log n)^j n^{-5/2},\quad
 M_0=\zeta(5/2),\qquad m=1/\zeta(5/2).
\]

At n=1 the factor is 1 for j=0 and zero for j>0. These sums are finite:
on \(2^k\le n<2^{k+1}\), their sum is bounded by
\(2^{-3k/2}((k+1)\log2)^j\), with the factor interpreted as 1 when j=0.
The resulting geometric-polynomial series converges. The Dirichlet series
and its first two derivatives converge locally uniformly on Re v>1,
using the same bounds with a slightly smaller fixed real part. The
standard holomorphic-series differentiation theorem therefore gives

\[
 Z^{(j)}(t)=\sum_{n\ge1}(-i\log n)^j n^{-5/2-it},
 \qquad |Z^{(j)}(t)|\le M_j.                        \tag{5}
\]

The scalar series is [DLMF 25.2.1](https://dlmf.nist.gov/25.2#E1),
whose hypothesis Re v>1 holds on this fixed line. L005 gives an absolutely
convergent Euler logarithm \(\mathscr L(v)\) with
\(\exp\mathscr L(v)=\zeta(v)\). Its absolute majorant on Re v=5/2 is
\(\mathscr L(5/2)=\log\zeta(5/2)\), hence

\[
 |Z(t)|=\exp(\operatorname{Re}\mathscr L(v))
      \ge \exp(-\log\zeta(5/2))=m>0.                \tag{6}
\]

This imports L005 on its actual domain; it supplies a uniform lower bound,
rather than just nonvanishing.

For the controlled carrier derivatives put Ψ=Γ′/Γ. Import the previously
assessed scalar expansions
[DLMF 5.11.2](https://dlmf.nist.gov/5.11#E2) and
[5.15.8](https://dlmf.nist.gov/5.15#E8), retaining their sector
qualifications and the digamma remainder control in
[§5.11(ii)](https://dlmf.nist.gov/5.11#ii):

\[
 \Psi(s)=\operatorname{Log}s-\frac1{2s}+O(t^{-2}),
 \qquad
 \Psi'(s)=\frac1s+\frac1{2s^2}+O(t^{-3}).            \tag{7}
\]

The arguments s have positive fixed real part and remain, for large t,
inside |arg s|≤3π/4, separated from the negative real axis. The errors
are uniform. The second formula is a separately controlled polygamma
expansion; no uncontrolled O term in the first is differentiated.
For an explicit check of the rational phase correction, (3) gives exactly

\[
 \frac{b'}b=\frac i2\left(\frac1s+\frac1{s+1/2}\right),\qquad
 \frac{b''}b-\left(\frac{b'}b\right)^2
       =\frac14\left(\frac1{s^2}+\frac1{(s+1/2)^2}\right).
\]

In particular \(b'/b=2/t+O(t^{-2})\), the second expression is
O(t⁻²), and the imaginary part needed below is exactly

\[
 \operatorname{Im}(b'/b)
   =\frac12\left(
       \frac{1/4}{1/16+t^2/4}
       +\frac{3/4}{9/16+t^2/4}\right)=O(t^{-2}).
\]

All denominators are positive for real t, and these estimates are
uniform for t≥1. This explicitly checks the stronger imaginary-part
order used in the first line of (8).

Taking the imaginary part of the logarithmic derivative of Qb and
differentiating its exact expression gives

\[
\begin{aligned}
 \omega&=\tfrac12(\operatorname{Re}\Psi(s)-\log\pi)
                +\operatorname{Im}(b'/b)
        =\tfrac12\log(t/(2\pi))+O(t^{-2}),\\
 \omega'&=-\tfrac14\operatorname{Im}\Psi'(s)
                +\operatorname{Im}(b''/b-(b'/b)^2)=O(t^{-1}),\\
 q&=\frac2p-\frac{4t^2}{p^2}-\tfrac14\operatorname{Re}\Psi'(s)
                +\operatorname{Re}(b''/b-(b'/b)^2)=O(t^{-2}). \tag{8}
\end{aligned}
\]

For the first line, Re Log s=log(t/2)+O(t⁻²) and Re(1/s)=O(t⁻²).
For the last line, (7) gives Re Ψ′(s)=O(t⁻²), since
Re(1/s)=O(t⁻²) and |1/s²|=O(t⁻²). Thus q includes the full
amplitude curvature, with both the p and b factors.

Set C=exp(iθ)Z, D=exp(iθ)Z′, E=exp(iθ)Z″ and r=Re C, so G=B r.
The exact normalization identity of L358 (3), applied to this positive B, is

\[
 \frac{G'^2-GG''}{B^2}=r'^2-rr''-q r^2.
\]

It follows by two differentiations of B r; the B′r′ terms cancel.
Direct differentiation of C gives

\[
 r'=\operatorname{Re}D-\omega\operatorname{Im}C,\qquad
 r''=\operatorname{Re}E-2\omega\operatorname{Im}D
                -\omega'\operatorname{Im}C-\omega^2\operatorname{Re}C.
\]

The complete quadratic expansion is consequently

\[
\begin{aligned}
 \frac{G'^2-GG''}{B^2}={}&\omega^2|Z|^2
       +2\omega\operatorname{Im}(Z'\overline Z)
       +(\operatorname{Re}D)^2-\operatorname{Re}C\operatorname{Re}E\\
    &+\omega'\operatorname{Re}C\operatorname{Im}C
       -q(\operatorname{Re}C)^2.                    \tag{9}
\end{aligned}
\]

In particular its signed cross term is
\(2\omega(\operatorname{Re}C\operatorname{Im}D
-\operatorname{Re}D\operatorname{Im}C)
=2\omega\operatorname{Im}(Z'\overline Z)\).
The remaining two phase-square contributions combine as
\(\omega^2[(\operatorname{Im}C)^2+(\operatorname{Re}C)^2]\);
no assumption on the phase or nonzero value of the real projection
has entered this combination.

The absolute value of all terms after the leading one is at most

\[
 2|\omega|M_0M_1+M_1^2+M_0M_2
       +\tfrac12|\omega'|M_0^2+|q|M_0^2=O(L).       \tag{10}
\]

Here |Re C Im C|≤|C|²/2. Every constant is independent of t and of
the phase of Z. Equations (8)–(10) prove
\((G'^2-GG'')/B^2=\omega^2|Z|^2+O(L)\).

By (4) and (8), with T=1+t and L=log(2+t),

\[
 \frac{|b|^2}{T^4}=\frac1{16\pi^2}+O(t^{-1}),\qquad
 \frac{\omega^2}{L^2}=\frac14+O(L^{-1}).
\]

Since |Z|≤M_0 and B²=A²|b|², these estimates prove (1) for t>0,
with a single finite uniform error constant K. By (6) the result is at least
\(m^2/(64\pi^2)-K/L\). Choose H large enough that all estimates hold and
\(L\ge128\pi^2K/m^2\); this proves (2). This is a finite existence
threshold, not an evaluated numerical bound.
More explicitly, if the uniform bound K/L holds for t≥t₀≥1,
one permissible choice is
\(H=\max\{t_0,\exp(128\pi^2K/m^2)\}\).
Neither K nor t₀ depends on t. Thus there is a single onset for the
whole ray, not a separate threshold for each zeta phase.

Finally Q(−t), b(−t) and Z(−t) are the complex conjugates of their values
at t. Gamma conjugation follows from its absolutely convergent Euler
integral at Re s=1/4; zeta conjugation here follows from its absolutely
convergent series at Re v=5/2. The real-coefficient polynomial factors
in s and the real logarithm of π preserve these identities.
Formula (3) makes G real and even. G′ is odd and G″ is even,
so G′²−GG″ is even. A, T, L and |ζ(5/2+it)| are also even.
This proves (1)–(2) for both signs. At zeros of G the identities (9)
and (10) still apply: division was only by the strictly positive B. ∎

The comparison with L367 uses its definition
\(\mathcal C=(G'^2-GG'')/(A^2T^4L^2)\), not an additional premise.
Its signed linear term and remainder still need separate comparisons with
any proposed actual-theta margin. This result alone cannot transfer
positivity to F_0, and no RH candidate is claimed.

Critical audit completed 2026-10-05 under the separately approved
response-quadratic-audit assessment: the original coefficient, lower-bound
constant, domain and qualifications survive. The explicit rational
derivatives, cross-term check and common-onset choice above clarify the
existing proof; they do not strengthen its conclusion.

**Mathlib.** Full response quadratic margin: **not checked**.
Supporting right-half-plane Euler-product/nonvanishing coverage is inherited
from L005, including
[riemannZeta_eulerProduct_exp_log](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/EulerProduct/DirichletLSeries.html#riemannZeta_eulerProduct_exp_log).
These are supporting scalar theorems, not a matching nonlinear margin theorem.
Gamma-jet and real-projection coverage was not checked here; no absence
or novelty inference is made.
