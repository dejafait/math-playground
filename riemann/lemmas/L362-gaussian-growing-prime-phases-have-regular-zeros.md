# Lemma 362: growing prime phases give regular Gaussian zeros

**Hypotheses.** For R>1 set ε=R^(−2) and use the coefficients
and actual real-frequency series of L358:

\[
 a_R(n)=n^{-1/2}e^{-\pi(n/R)^2},\qquad
 S_\varepsilon(\xi)=\sum_{n\ge1}a_R(n)n^{-i\xi}.
\]

For a completely multiplicative unit-phase assignment χ define

\[
 T_R(\chi)=\sum_{n\ge1}a_R(n)\chi(n),\qquad
 W_R(\chi)=\sum_{n\ge1}a_R(n)(\log n)\chi(n).
 \tag{1}
\]

These series and every logarithmically weighted series used below
converge absolutely. A phase assignment is a test point on a prime
torus, not an asserted actual-frequency assignment.

**Conclusion.** There are constants R_0>1 and c>0 such that for
every R≥R_0 there is a unit-phase assignment χ_R satisfying

\[
 \chi_R(p)=1\quad(p>N_R),\qquad
 N_R=\left\lceil R\sqrt{8\log R}\right\rceil,
 \qquad T_R(\chi_R)=0,\qquad
 |W_R(\chi_R)|\ge c\frac{\sqrt R}{\log R}>0.
 \tag{2}
\]

This zero is regular: rotating two disjoint finite groups of prime
phases while fixing the other phases gives a real two-variable
Jacobian of T_R with smallest singular value at least
c√R/log R, after reducing c if necessary.

At each such fixed ε, for every H>0 and δ>0 an actual ξ≥H satisfies

\[
 |S_\varepsilon(\xi)|<\delta,\qquad
 |S_\varepsilon'(\xi)+iW_R(\chi_R)|<\delta.
 \tag{3}
\]

In particular inf_(ξ≥H)|S_ε(ξ)|=0, and arbitrarily small actual
series values can coexist with a derivative bounded away from zero.
The constants and the visit heights in (3) are not evaluated.
No rate relative to log ξ or control of the gamma phase is proved.
Thus neither (2) nor (3) proves L359's negative-sign condition, a
negative first Laguerre value for arbitrarily small ε, or an
actual-theta sign. The regulator-uniform global-sign question remains
open.

**Proof.** We first give the elementary prime supply needed for the
construction. This supplements the central-binomial upper estimate
in L361; it uses no prime-number-theorem error estimate. Write
θ(x)=Σ_(p≤x)log p and ψ(x)=Σ_(p^k≤x)log p. For integer n≥2,
put m=ceil(n/2). Every prime in (m,n] divides binom(2m,m), so

\[
 \theta(n)-\theta(m)\le2m\log2\le(n+1)\log2.
\]

Iterating n↦ceil(n/2) down to one gives
θ(n)≤(2n+2ceil(log_2 n))log 2. Consequently
θ(x)≤4(log 2)x for all sufficiently large real x. Conversely,
binom(2m,m)≥4^m/(2m+1). Each p-adic valuation of this binomial
coefficient is a sum of floor(2m/p^k)−2floor(m/p^k), whose terms
are zero or one. Thus log binom(2m,m)≤ψ(2m). Taking
m=floor(x/2) shows

\[
 \psi(x)\ge(x-2)\log2-\log(x+1).
\]

The identity ψ(x)−θ(x)=Σ_(k≥2)θ(x^(1/k)), with at most
log_2 x terms, and the elementary bound θ(y)≤y log y give
ψ(x)−θ(x)=O(√x(log x)²)=o(x). Hence, eventually,
θ(x)≥(log 2)x/2. Combining these bounds yields

\[
 \#\{p:x<p\le16x\}
 \ge\frac{\theta(16x)-\theta(x)}{\log(16x)}
 \ge\frac{4(\log2)x}{\log(16x)}.                 \tag{4}
\]

All endpoints here are real; θ(x)=θ(floor x), and the preceding
floor/ceiling arguments supply their claimed eventual bounds.

Choose a fixed a≥1, to be made sufficiently large below, and consider
three separated windows

\[
 \begin{split}
 I_1&=(aR,16aR],\\
 I_2&=(32aR,512aR],\\
 I_3&=(1024aR,16384aR].
 \end{split}                                    \tag{5}
\]

For each fixed d∈{a,32a,1024a}, (4) implies

\[
 \sum_{dR<p\le16dR}a_R(p)
 \ge\frac{4(\log2)dR}{\log(16dR)}
           (16dR)^{-1/2}e^{-\pi(16d)^2}
 \ge c_d\frac{\sqrt R}{\log R}                  \tag{6}
\]

for all sufficiently large R, with c_d>0. These constants may be
extremely small; only positivity and eventual comparison are used.
Let M be one quarter of the smallest of the three raw sums in (6).
In each window select a subset Q_j of its primes by adding terms
until its raw weight first reaches M. There is enough weight to do
so. If w_max=max_(p in the three windows)a_R(p), this ensures

\[
 M\le\sum_{p\in Q_j}a_R(p)\le M+w_{\max},\quad
 M\ge c_a\sqrt R/\log R,\quad
 w_{\max}=O_a(R^{-1/2}),\quad w_{\max}/M\to0.     \tag{7}
\]

The selections depend only on the positive raw coefficients, before
any random phases are chosen. Put Q=Q_1∪Q_2∪Q_3 and N=N_R.
For sufficiently large R, N>16384aR and N<R². No n≤N can have
two prime factors from Q, counting multiplicities, since every such
prime exceeds aR≥R. Thus its prime-phase polynomial is affine in
the selected phases:

\[
 T_{R,N}=B+\sum_{p\in Q}A_p\chi(p),\qquad
 A_p=\sum_{m\le N/p}a_R(pm)\eta(m).               \tag{8}
\]

Here η assigns phases to the primes ≤N outside Q, and B sums
integers n≤N with no Q factor. Every m in A_p has no Q factor.
Randomize these background prime phases independently with uniform
circle measure. Unique factorization gives
E[η(n)overline{η(m)}]=0 for distinct n,m supported on background
primes, and one when n=m: each prime integral of a nonzero integer
power is zero. Define the centered background derivative

\[
 B_1=\sum_{\substack{n\le N\\p\nmid n\ \text{for all }p\in Q}}
              a_R(n)\log\frac n{aR}\,\eta(n).
\]

Since a_R(n)²≤1/n, the two exact orthogonality estimates are

\[
 E|B|^2\le1+\log N,\qquad
 E|B_1|^2\le D_R^2(1+\log N),\qquad
 D_R=\log(aR)+\log N.                           \tag{9}
\]

For n≤N, |log(n/(aR))|≤D_R. A background point where
|B|²+|B_1|²/D_R² is no greater than its average therefore satisfies
|B|≤√(2(1+log N)) and |B_1|≤D_R√(2(1+log N)). Fix such a
point. In view of (7), B/M→0 and B_1/M→0 as R→∞, with a fixed.
This is an existence argument on a finite torus, not a probabilistic
claim about the actual zeta function.

The selected coefficients are dominated by their prime terms.
Indeed, uniformly in all background phases, define

\[
 d_0(a)=\sum_{m\ge2}m^{-1/2}e^{-\pi a^2(m^2-1)},\qquad
 d_1(a)=\sum_{m\ge2}m^{-1/2}(\log m)e^{-\pi a^2(m^2-1)}.
\]

Both sums tend to zero as a→∞, by their summable a=1 Gaussian
majorants. For p∈Q, division of (8) by a_R(p) shows
|A_p/a_R(p)−1|≤d_0(a). Likewise, if

\[
 C_p=\sum_{m\le N/p}a_R(pm)\log\frac{pm}{aR}\,\eta(m),
\]

then, whenever d_0(a)<1,

\[
 \left|\frac{C_p}{A_p}-\log\frac p{aR}\right|
       \le\frac{d_1(a)}{1-d_0(a)}.               \tag{10}
\]

To see this, write A_p=a_R(p)(1+r_0), |r_0|≤d_0(a), and
C_p=log(p/(aR))A_p+a_R(p)r_1, |r_1|≤d_1(a).
This explicitly retains the complex coefficient correction.

Set L_j=Σ_(p∈Q_j)|A_p| and assign each selected prime the phase
χ(p)=overline{A_p}|A_p|^(−1)e^(i t_j). Then

\[
 T_{R,N}(t)=B+\sum_{j=1}^3L_je^{it_j},\qquad
 W_{R,N}(t)-\log(aR)T_{R,N}(t)
       =B_1+\sum_{j=1}^3L_j(\mu_j+\rho_j)e^{it_j},       \tag{11}
\]

where μ_j is the real |A_p|-weighted mean of log(p/(aR))
on Q_j, and |ρ_j|≤d_1(a)/(1−d_0(a)). In particular

\[
 \begin{split}
 \mu_1&\in[0,\log16],\quad
 \mu_2\in[\log32,\log512],\quad
 \mu_3\in[\log1024,\log16384],\\
 \mu_2-\mu_1&\ge\log2,\qquad
 L_j/M=1+O(d_0(a))+o_R(1).                       \tag{12}
 \end{split}
\]

Fix t_3=0. With B=0 and L_1=L_2=L_3=M, the first expression in
(11) vanishes at t_1=2π/3, t_2=4π/3. Its two real derivative
columns, divided by M, are i exp(2πi/3) and i exp(4πi/3), with
determinant √3/2. The normalized centered derivative at this point
has imaginary part

\[
 \operatorname{Im}\left(\sum_{j=1}^3\mu_je^{it_j}\right)
       =\frac{\sqrt3}{2}(\mu_1-\mu_2)
       \le-\frac{\sqrt3}{2}\log2<0.              \tag{13}
\]

These assertions persist uniformly under sufficiently small
perturbations of L_j/M, B/M, B_1/M and ρ_j. Here is why the
uniform qualification is valid. The three μ_j range in the fixed
compact intervals in (12). The zero of the two-variable triangle
is a continuous smooth function of the three normalized lengths
and the complex normalized background near their displayed values,
by its invertible Jacobian (equivalently, intersect the two circles
with a strict, nondegenerate triangle). Neither its local zero nor
its Jacobian depends on μ_j. The centered expression in (11) is
continuous in that local zero, the lengths and μ_j; the negative
margin in (13) is uniform on their compact product. Thus one
positive perturbation tolerance suffices for all these μ_j, retains
an inverse Jacobian norm at most C/M, and retains a centered
derivative magnitude at least c_1M, with fixed C,c_1>0.

First choose a large enough that d_0(a) and d_1(a)/(1−d_0(a))
are less than one quarter of a sufficiently small such tolerance.
Then choose R large enough for (7), (9) and the remaining o_R(1)
errors to fit the reserved margin. The finite polynomial
now has a zero t_*=(t_1,t_2), with t_3=0, and

\[
 \|J_*^{-1}\|\le C/M,\qquad
 |W_{R,N}(t_*)-\log(aR)T_{R,N}(t_*)|\ge c_1M.    \tag{14}
\]

Next retain the infinite series, setting χ(p)=1 for p>N. Let
E(t)=T_R(t)−T_{R,N}(t), and let E_1 be the corresponding tail
of the centered derivative W_R−log(aR)T_R. Each full term is a
constant unit phase times exp(i(v_1t_1+v_2t_2)); v_j counts selected
prime factors from Q_j, with multiplicity. Since every selected
prime is >R, v_1+v_2≤log n/log R. For n>N, put x=n/R≥1.
When R≥e,

\[
 \frac{\log n}{\log R}\le1+\log x\le1+x,\qquad
 \left|\log\frac n{aR}\right|\le\log a+x.
\]

Consequently every t derivative of total order ≤2 of E and E_1
is dominated by

\[
 C_a\sum_{n>N}n^{-1/2}(1+n/R)^3e^{-\pi(n/R)^2}
       \le C'_a R^{1/2-2\pi}=:\tau_R.            \tag{15}
\]

For the last inequality, split the Gaussian into exponents π/4,
π/4 and π/2. The first factor is at most R^(−2π), since
(N/R)²≥8log R. The second absorbs (1+x)³, with an absolute
finite supremum. The remaining sum is H(1/(2R²))=O(√R), by
the scalar Gaussian sum/integral calculation in L360. These bounds
justify the two termwise phase derivatives by uniform convergence.
They also show τ_R/M→0. No derivative of an uncontrolled remainder
has been used.

For clarity an explicit contraction supplies the full-series zero.
For h near zero write the finite polynomial at t_*+h as
J_*h+Q(h); it has |Q(h)|≤C M|h|² and
||DQ(h)||≤C M|h|, because the lengths in (11) are O(M).
The equation T_R(t_*+h)=0 is

\[
 h=-J_*^{-1}\bigl(Q(h)+E(t_*+h)\bigr).          \tag{16}
\]

On a closed ball |h|≤Kτ_R/M, with K fixed and sufficiently
large, (14)–(15) imply that the right side maps the ball into
itself and has Lipschitz constant O(τ_R/M)<1/2 for large R.
Successive iteration therefore converges geometrically to a fixed
point; this is the Banach contraction argument with its hypotheses
checked. At that point the change of the finite Jacobian and the
tail Jacobian is O(τ_R), so its smallest singular value remains
at least c_2M. The centered finite derivative in (11) has gradient
O(M), because the μ_j and ρ_j lie in fixed bounded sets. Its change
is O(τ_R), as is E_1. Thus the full centered derivative still has
magnitude at least c_1M/2. At a full zero the centered derivative
equals W_R. Equation (7) proves every assertion in (2), including
regularity. All selected and background phases are unit phases,
and only primes through N are changed from +1.

Finally fix this R and χ_R. Reuse the finite prime-phase visit
argument proved in L335. Its product trigonometric bump can be
translated from phases π to any finite prescribed prime-phase box;
the constant Fourier coefficient is unchanged. Unique factorization
still makes every nonconstant integer combination of prime logarithms
nonzero. Time averaging therefore guarantees visits to any such
box at arbitrarily large positive frequencies. This supplies only
qualitative visits, with the finite box and R fixed.

To apply it to (1), choose an integer cutoff K≥N so large that the
absolute tails of both Σa_R(n) and Σa_R(n)log n past K are less
than δ/4. Prescribe χ_R(p) on every prime ≤K, including +1 on
N<p≤K. Continuity of the two finite phase polynomials provides a
box where each differs from its template by less than δ/2. An
arbitrarily late visit, plus both series tails, proves (3), since
S_ε′=−iΣa_R(n)(log n)n^(−iξ) and T_R(χ_R)=0. Shrinking δ
gives the infimum assertion and preserves |S_ε′|≥|W_R(χ_R)|/2
at sufficiently accurate visits. ∎

This is a **REPRODUCTION** of elementary prime counting, independent
phase orthogonality, triangle geometry, Gaussian summation and
contraction/finite-phase visit arguments, specialized to the assessed
coefficients. The closest screened smoothed-series source, Paris,
*The asymptotic expansion of a generalisation of the Euler-Jacobi
series*, [arXiv:1503.07329v1](https://arxiv.org/pdf/1503.07329v1),
§2 and Theorem 1, does not supply these growing unit-phase controls
or regular zeros; its even-integer exponent hypotheses are not
invoked outside their domain. The needed difference is the growing
background and quantitative regularity, rather than another scalar
Mellin reproof. No originality beyond the checked literature is
claimed.

The fixed-head and small-support obstructions in L360–L361 are
preserved: here the background phases throughout the growing range
below R are free, and the allowed support reaches N_R, beyond the
o(log²(1/ε)) range. The new
input removes a value-noncancellation obstacle and disproves the
bounded-away-from-zero premise of L358's conditional positive tail
for sufficiently small regulators. It does not disprove that tail's
conclusion. At a template with T_R=0, L359's leading first sign is
(Re(e^(iφ)S′))², not an automatic negative value. For its negative
test one needs the displaced condition ωS≈iS′ and a suitably rotated
derivative, at the same actual frequency. Qualitative visits in (3)
give no control of ω(ξ) times their error, since ω(ξ)~(log ξ)/2.
Those occurrence and rotation steps remain unproved. No negative
regulator family or RH candidate is recorded.

**Mathlib.** Full regular-zero construction and simultaneous
small-value/derivative occurrence: **not checked**. Supporting
prime-count, torus orthogonality, triangle/implicit-function,
contraction and phase-visit coverage is also **not checked** here.
The scalar gamma integral inherited through L360 is
[DLMF 5.9.1](https://dlmf.nist.gov/5.9#E1), a supporting result
rather than a match for (2)–(3). No full matching theorem or library
absence is asserted; general documentation is
[Mathlib](https://leanprover-community.github.io/mathlib4_docs/).
