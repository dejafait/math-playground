# Lemma 364: a joint gamma-window return threshold for regulated signs

**Hypotheses.** Fix R sufficiently large for L363, set ε=R^(−2),
and use its m_R>0, λ_R>0 and phase templates. Use the exact
S_ε, A, φ, ω=φ′ and beta term in L358 and the sign bound U in
L359. Put

\[
 M_j=\sum_{n\ge1}n^{-1/2}e^{-\pi(n/R)^2}(\log n)^j
 \quad(j=0,1,2),\qquad
 \kappa_R=\min\left\{\frac1{16},
       \frac{m_R\log2}{128M_1},\frac{m_R\log2}{128M_2}\right\}>0.
 \tag{1}
\]

For sufficiently large H, define

\[
 \begin{gathered}
 N_H=\left\lceil R\sqrt{8\log\log H}\right\rceil,\qquad
 d_H=\#\{p:p\le N_H\},\qquad D_H=d_H+1,\qquad
 \delta_H=\kappa_R/\omega(H),\\
 X_H=64D_H\delta_H^{-2},\qquad
 K_H=\lceil X_H\log X_H\rceil,\qquad
 \beta_H=(2K_H+1)^{-D_H},\\
 \Delta_H=\min_{\substack{0\ne k\in\mathbb Z^{d_H}\\
                         \|k\|_\infty\le K_H}}
                     \left|\sum_{p\le N_H}k_p\log p\right|>0.
 \end{gathered}                                                    \tag{2}
\]

The positivity of Δ_H follows from unique prime factorization.
There is no imported quantitative logarithmic-form theorem in these
hypotheses. The premise (LF) below is explicitly conditional and unproved.

**Conclusion.** There is H_R<∞ such that for H≥H_R the two inequalities

\[
 H\Delta_H\beta_H\ge8,\qquad \sqrt H\,\beta_H\ge96                 \tag{3}
\]

force an **actual** x∈[H,2H] with

\[
 \frac{F_\varepsilon'(x)^2-F_\varepsilon(x)F_\varepsilon''(x)}{A(x)^2}
          \le-\frac{m_R^2}{2}<0.                                  \tag{4}
\]

The second inequality in (3) holds automatically eventually at fixed
R. The first is the unresolved arithmetic requirement. Replacing Δ_H
by the elementary lower bound exp(−K_H θ(N_H)), where
θ(N)=Σ_(p≤N)log p, does not certify it, even after optimizing the
degree within this separating cosine-power bump. This is a failure
of that upper-error certificate, not a lower bound on actual return times.

Here is a sufficient, deliberately weak arithmetic premise:

\[
 \begin{split}
 &\text{there is a fixed }C>0\text{ such that for every }N\ge2,
     \ K\ge1,\text{ and every nonzero prime-indexed integer vector}\ k,\\
 &\qquad \|k\|_\infty\le K\quad\Longrightarrow\quad
 \left|\sum_{p\le N}k_p\log p\right|
       \ge\exp\{-\exp(CN\log(N+2))\log(2+K)\}.                    \tag{LF}
 \end{split}
\]

**If (LF) is established**, then (3) holds for every sufficiently
large H at each fixed R in L363's range. Thus (4) would occur in
every sufficiently high dyadic interval at each sufficiently small
fixed regulator. In particular (LF) would stop the proposed common
global-first-sign threshold for this family. No assertion that (LF)
has been proved or imported is made here, and no actual negative
regulator beyond the existing six finite certificates is established.

**Proof.** First freeze the template and the prime cutoff at H,
rather than select a template at an unknown visit x. L358's covered
digamma/trigamma expansions give, with R fixed,

\[
 \omega(t)=\tfrac12\log(t/(2\pi))+O(t^{-2}),\qquad
 \omega'(t)=\frac1{2t}+O(t^{-2}).                                \tag{5}
\]

For the second formula use its exact identity
ω′=−Im Ψ_1(1/4+it/2)/4 and the cited expansion
Ψ_1(s)=1/s+O(|s|^(−2)). Consequently, eventually on [H,2H],

\[
 \frac1{8H}\le\omega'(t)\le\frac1H,\qquad
 \omega(t)-\omega(H)=O(1),\qquad \omega(t)/\omega(H)\le2.          \tag{6}
\]

Take H sufficiently large that 1/ω(H)≤λ_R. Apply L363 at
λ=1/ω(H) and prescribed gamma angle zero. It supplies a fixed
completely multiplicative assignment χ_H such that

\[
 T_R(\chi_H)=W_R(\chi_H)/\omega(H),\qquad
 W:=W_R(\chi_H)\in[m_R,M_1]\subset\mathbb R.                     \tag{7}
\]

Its prime support is through the fixed N_R of L363, and N_H≥N_R
eventually. No selected phase is differentiated with respect to H or t.

The larger cutoff in (2) controls the infinite actual-series tail
at the required shrinking tolerance. For j=0,1,2, splitting the
Gaussian exponent into two halves gives

\[
 \begin{aligned}
 t_j(N_H)&:=\sum_{n>N_H}n^{-1/2}e^{-\pi(n/R)^2}(\log n)^j\\
 &\le e^{-\pi N_H^2/(2R^2)}
       \sum_{n\ge1}n^{-1/2}e^{-\pi n^2/(2R^2)}(\log n)^j
 \le C_{R,j}(\log H)^{-4\pi}
       =o_R(\omega(H)^{-2}).                                     \tag{8}
 \end{aligned}
\]

Every constant on the right is finite at fixed R. This bound is
uniform over all prime phases and retains the entire omitted series.

Suppose t∈[H,2H] satisfies the joint circular-distance conditions

\[
 \operatorname{dist}(-t\log p,\arg\chi_H(p))<\delta_H
       \ (p\le N_H),\qquad
 \operatorname{dist}(\phi(t),0)<\delta_H.                         \tag{9}
\]

For n≤N_H, multiplying its prime phases and telescoping gives
|n^(−it)−χ_H(n)|≤δ_H Ω(n)≤δ_H log n/log 2. Therefore (1),
(8) and sufficiently large H give

\[
 \left|S_\varepsilon(t)-\frac W{\omega(H)}\right|
        \le\frac{m_R}{64\omega(H)},\qquad
 |W_a-W|\le\frac{m_R}{64\omega(H)},\qquad
 W_a=iS_\varepsilon'(t).                                        \tag{10}
\]

For example the head error in each inequality is at most
m_R/(128ω(H)), and the two tails fit the remaining half.
The bound Ω(n)≤log n/log 2 includes prime multiplicities; no
independence of integer phases is assumed.

Set V=S_ε′+iω(t)S_ε. By (6), (7), (10), and fixed R,

\[
 |V|=|\omega(t)S_\varepsilon(t)-W_a|
 \le\frac{m_R}{32}
       +\frac{M_1|\omega(t)-\omega(H)|}{\omega(H)}
       +\frac{m_R}{64\omega(H)}\le\frac{m_R}{8}                  \tag{11}
\]

eventually. Also δ_H≤1/16 and ω(H)≥1 eventually. Thus (9)–(10)
give, using cos u≥1−u²/2,

\[
 |\operatorname{Im}(e^{i\phi(t)}S_\varepsilon'(t))|
  =|\operatorname{Re}(e^{i\phi(t)}W_a)|
  \ge(511/512)m_R-m_R/64>15m_R/16.                              \tag{12}
\]

The value bound in (10) is c=|S_ε(t)|=O_R(1/ω(H)); its second
derivative has the unconditional bound e≤M_2. L358–L359 give
γ→0 and E_β=O_R((1+ω(t)²)β(t))→0, uniformly on this interval;
the β(t) here is the exact beta amplitude, distinct from β_H.
Their sufficient upper sign bound consequently satisfies

\[
 U\le(m_R/8)^2-(15m_R/16)^2+cM_2+\gamma c^2+\mathcal E_\beta
       =-221m_R^2/256+o_R(1)\le-m_R^2/2.                        \tag{13}
\]

This proves (4) from a visit to (9), retaining subtraction and
real projection at the same actual t as φ and ω.

We next give the quantitative joint-window visit test. Reuse L336's
cosine-power bump, translated to the centers in (9), now in D_H
coordinates including the gamma phase. As a function on the torus it is

\[
 g_H(\theta,\psi)=
 \prod_{p\le N_H}\left[\frac{1+\cos(\theta_p-\arg\chi_H(p))}{2}\right]^{K_H}
       \left[\frac{1+\cos\psi}{2}\right]^{K_H}.                  \tag{14}
\]

Its Fourier support has |k_p|≤K_H, |l|≤K_H, its coefficients
have absolute sum one, and its constant coefficient is

\[
 b_H=\left[4^{-K_H}\binom{2K_H}{K_H}\right]^{D_H}\ge\beta_H.
\]

These are the exact binomial identities in L336; translation changes
only coefficient phases. Outside the open box (9), at least one
factor is at most cos²(δ_H/2), so
g_H≤exp(−K_H δ_H²/4)≤β_H/4. The last inequality is L336's
proved X=64Dδ^(−2), K=ceil(X log X) estimate with D=D_H.

For the orbit average on [H,2H], a Fourier term has phase

\[
 f(t)=-\nu_k t+l\phi(t),\qquad
 \nu_k=\sum_{p\le N_H}k_p\log p.
\]

If l=0 and k≠0, direct integration bounds its normalized
integral by 2/(HΔ_H). For l≠0, (6) makes f′ monotone and
|f″|≥|l|/(8H)=:η. This supplies an elementary bound independent
of ν_k, including stationary points: the interval where |f′|≤a
has length at most 2a/η. Its complement has at most two intervals.
On each, integration by parts bounds the integral by 3/a, because
the endpoint terms cost at most 2/a and the variation of 1/f′
at most 1/a. Taking a=√η yields

\[
 \left|\frac1H\int_H^{2H}e^{if(t)}dt\right|
    \le\frac{8}{H\sqrt\eta}
    \le\frac{24}{\sqrt{|l|H}}\le\frac{24}{\sqrt H}.              \tag{15}
\]

This proof permits an empty central interval or one meeting an
endpoint. It imports no stationary-phase or equidistribution theorem.
Summing the finite Fourier expansion with coefficient absolute sum
one therefore gives the unconditional discrepancy estimate

\[
 \left|\frac1H\int_H^{2H}
        g_H((-t\log p)_{p\le N_H},\phi(t))dt-b_H\right|
       \le\frac2{H\Delta_H}+\frac{24}{\sqrt H}.                 \tag{16}
\]

Under (3), its right side is at most β_H/2. The average is then
at least β_H/2, whereas absence of a visit would bound it by
β_H/4. A visit exists and (13) proves the first assertion.
All sums in this argument are finite Fourier sums; (8) already
controls the infinite Dirichlet-series transfer.

For the growth comparison let y=log log H and hold R fixed. From
(1), (2), (5) and the elementary bound d_H≤N_H,

\[
 N_H=O_R(\sqrt y),\quad
 \log\delta_H^{-1}=y+O_R(1),\quad
 \log K_H=2y+O_R(\log(y+2)),\quad
 \log\beta_H^{-1}=O_R(y^{3/2})=o(\log H).                       \tag{17}
\]

Thus √H β_H→∞, proving that the gamma harmonics meet the needed
window mass. The elementary integer-product estimate in L336 gives
Δ_H≥exp(−K_H θ(N_H)). Using only this estimate in the first
condition (3) requires

\[
 \log H\ge K_H\theta(N_H)+D_H\log(2K_H+1)+\log8.                \tag{18}
\]

It fails: θ(N_H)≥log 2 eventually and K_H≥64δ_H^(−2), which
already grows like a positive R-dependent multiple of (log H)².
Nor does optimizing this bump degree fix that particular certificate.
For any positive integer degree K its constant coefficient is at
most 1/2. Separation of its outside bound q^K, q=cos²(δ_H/2),
from its constant term requires K>log 2/(−log q). L336 proves
−log q≤δ_H²/2 for δ_H≤1, so K>2(log 2)δ_H^(−2).
The same elementary worst-frequency discrepancy then requires a
length exceeding a constant times 2^K, again beyond H here.
Neither argument says that the actual Δ_H is as small as the
elementary lower bound, or that actual visits fail.

Finally, **conditionally** on (LF), (2) implies

\[
 -\log\Delta_H
   \le\exp(CN_H\log(N_H+2))\log(2+K_H)
   =\exp(O_R(\sqrt y\log(y+2)))\,O_R(y)
   =o(e^y)=o(\log H).                                            \tag{19}
\]

Together (17) and (19) give HΔ_H β_H→∞, proving (3).
This proves the stated implication from (LF), without using it as
an established premise. Since L363 permits every sufficiently large
R, that implication would supply negative values for every sufficiently
small fixed ε, with an unevaluated ε-dependent onset. A uniform
onset in ε is unnecessary to refute a common global-sign threshold.
No passage of these escaping negative values to actual theta is
licensed by L357's O(ε) absolute-error limit. ∎

This is a **REPRODUCTION** of L336's finite bump/return tools and
the gamma estimates and projected-sign bounds already specialized
in L358–L359 and L363. The elementary split in (15) states its whole
proof; no new analytic theorem is imported. The supporting primary
gamma inputs remain [DLMF 5.11.1–3](https://dlmf.nist.gov/5.11#E1)
and [5.15.8–9](https://dlmf.nist.gov/5.15#E8), already read in the
saved assessment. They are not a match for the arithmetic bound (LF).
No novelty beyond the sources checked is claimed.

The unconditional result resolves the cost of matching the gamma
phase in this joint averaging test and precisely reduces occurrence
to prime-logarithm separation. Its elementary arithmetic implementation
fails at the required shrinking scale. An explicit stronger theorem
on linear forms in logarithms is an **unread source lead**, not an
imported result; the next separate assessment must test (LF), including
its dependence on the number and sizes of primes. The actual negative
regulator quantifier and all actual-zeta ranges remain unresolved.

**Mathlib.** Full joint-window discrepancy, conditional sign-transfer
and arithmetic-threshold statements: **not checked**. Supporting
gamma, finite Fourier, prime-factorization and logarithmic-form
coverage is also **not checked** here. The named DLMF formulas are
supporting results only; no full matching theorem or library absence
is asserted. General documentation is
[Mathlib](https://leanprover-community.github.io/mathlib4_docs/).
