# Lemma 363: displaced prime phases match every gamma rotation

**Hypotheses.** Use L362's coefficients, with R>1 and ε=R^(−2):

\[
 a_R(n)=n^{-1/2}e^{-\pi(n/R)^2},\qquad
 T_R(\chi)=\sum_{n\ge1}a_R(n)\chi(n),\qquad
 W_R(\chi)=\sum_{n\ge1}a_R(n)(\log n)\chi(n).
\]

Here χ is a completely multiplicative unit-phase assignment. Use
L358's exact positive A, gamma phase φ, ω=φ′, beta amplitude β
and α=(log ε)/2. All frequency derivatives are real derivatives.
There is no assumption that χ(n)=n^(−iξ).

For a fixed assignment χ and a fixed real center x define the test
functions, freezing both χ and x during differentiation,

\[
 \mathcal S_{\chi,x}(t)=\sum_{n\ge1}a_R(n)\chi(n)n^{-i(t-x)},
 \qquad
 \mathcal F_{\chi,x}(t)=A(t)
 \left[-\operatorname{Re}\bigl(e^{i\phi(t)}\mathcal S_{\chi,x}(t)\bigr)
                       +\beta(t)\cos(\alpha t)\right].             \tag{1}
\]

These are real-frequency test functions. They equal the actual
S_ε,F_ε only when χ(n)=n^(−ix). No Fourier-kernel positivity or
zero-preserving property is asserted for arbitrary χ.

**Conclusion.** There are R_0>1 and c>0 such that for every R≥R_0
there are m_R≥c√R/log R and λ_R>0 with the following property.
For every 0≤λ≤λ_R and every prescribed angle φ_0, some χ satisfies

\[
 \chi(p)=1\quad(p>N_R),\qquad
 N_R=\left\lceil R\sqrt{8\log R}\right\rceil,\qquad
 T_R(\chi)=\lambda W_R(\chi),\qquad
 e^{i\phi_0}W_R(\chi)\in[m_R,\infty)\subset\mathbb R.              \tag{2}
\]

In particular, for each such fixed R there is X_R<∞ such that at
every x≥X_R there is a phase assignment χ_x as in (2), with
λ=1/ω(x) and φ_0=φ(x), for which

\[
 \frac{\mathcal F_{\chi_x,x}'(x)^2
       -\mathcal F_{\chi_x,x}(x)\mathcal F_{\chi_x,x}''(x)}{A(x)^2}
       \le-\tfrac12|W_R(\chi_x)|^2<0.                            \tag{3}
\]

After increasing X_R if necessary, the following is a sufficient
condition for an **actual** negative first sign at x≥X_R:

\[
 \left|S_\varepsilon(x)-T_R(\chi_x)\right|
       \le\frac{m_R}{16\omega(x)},\qquad
 \left|iS_\varepsilon'(x)-W_R(\chi_x)\right|\le\frac{m_R}{16}.
                                                                    \tag{4}
\]

Under (4), (F_ε′²−F_εF_ε″)/A²≤−m_R²/2. No x satisfying (4)
is constructed. The templates in (2)–(3) do not give negative
values of the actual regulated family, bad regulators approaching
zero, or an actual-theta sign.

**Proof.** Retain the finite background and three separated prime
groups Q_1,Q_2,Q_3 in L362's proof, rather than fix the third group
angle to zero. We use its proved estimates (7)–(15), including the
elementary prime supply, simultaneous random-background bounds and
uniform infinite Gaussian tail. Their role here is to supply the
following data, for a fixed sufficiently large a and then all
sufficiently large R. Put ℓ=log(aR), M as in that proof and
ζ=exp(2πi/3). With three real group angles t_j,

\[
 \begin{aligned}
 T(t)&=B+\sum_{j=1}^3L_je^{it_j}+E(t),\\
 W(t)-\ell T(t)&=B_1+
                \sum_{j=1}^3L_j(\mu_j+\rho_j)e^{it_j}+E_1(t).
 \end{aligned}                                                     \tag{5}
\]

These are the full infinite sums for the prescribed background and
group phases. Here L_j>0, M≥c_a√R/log R, and

\[
 \mu_1\in[0,\log16],\quad
 \mu_2\in[\log32,\log512],\quad
 \mu_3\in[\log1024,\log16384],\quad \mu_2-\mu_1\ge\log2.           \tag{6}
\]

For any fixed tolerance δ>0, the construction permits

\[
 \max_j|L_j/M-1|,\quad |B|/M,\quad |B_1|/M,\quad
 \max_j|\rho_j|,\quad
 (\|E\|_{C^2}+\|E_1\|_{C^2})/M\ \le\delta.                      \tag{7}
\]

Indeed, first choose a to make d_0(a),d_1(a)/(1−d_0(a)) as
small as needed; then take R large for the raw-weight overshoot,
background bounds and tail/M to be small. The norms in (7) now
include all three group variables, uniformly in their angles. This
extension of the tail estimate follows from the same argument:
the total number of selected prime factors of n, with multiplicity,
is at most log n/log R, so any group derivative of order at most
two is bounded by that quantity squared. The centered logarithm
adds at most log a+n/R, as in L362. The resulting common tail is
O_a(R^(1/2−2π))=o(M). Gaussian majorants justify all these phase
derivatives. Thus varying the third angle introduces no uncontrolled
tail or derivative.

Let θ range over R/(2πZ), set t_3=θ and t_j=θ+u_j for j=1,2,
and normalize

\[
 G_\theta(u)=M^{-1}e^{-i\theta}T(\theta+u_1,\theta+u_2,\theta),
 \qquad g(u)=e^{iu_1}+e^{iu_2}+1.
\]

The C² distance between G_θ and g near
u_*=(2π/3,4π/3) is O(δ), uniformly in θ. Regarding complex
values as two real coordinates, g(u_*)=0 and its derivative J_0
has columns iζ,i\overline ζ, with determinant √3/2. Fix a small
ball around u_*. The equation G_θ(u_*+h)=0 is

\[
 h=-J_0^{-1}\bigl(G_\theta(u_*+h)-J_0h\bigr).                   \tag{8}
\]

On a ball |h|≤Kδ, its right side has size at most
Cδ+C(|h|²+δ|h|), and derivative norm at most C(|h|+δ).
Choose fixed K sufficiently large and then δ sufficiently small.
The map preserves this ball and contracts by a factor at most 1/2,
uniformly in θ. It has a unique fixed point h_0(θ)=O(δ).
The fixed point is continuous and 2π-periodic in θ: the map has
these properties, and its iterates converge uniformly. The same
estimates keep the two-variable real Jacobian invertible, with
inverse norm O(1/M).

At this zero T=0, so (5) is an expression for W itself. Define

\[
 z_R=\mu_1\zeta+\mu_2\overline\zeta+\mu_3,\qquad
 r_*=(\sqrt3/2)\log2>0.
\]

Then Im z_R=(√3/2)(μ_1−μ_2)≤−r_*, while |z_R| is bounded
above by a fixed constant from (6). Equations (5)–(8) imply

\[
 \left|M^{-1}W(t(\theta,0))-e^{i\theta}z_R\right|\le C\delta,
                                                                    \tag{9}
\]

uniformly in θ, with C independent of R. Choose the tolerance
so this bound is less than r_*/4.

Now replace G_θ by

\[
 G_{\theta,\lambda}(u)=M^{-1}e^{-i\theta}
                 [T(t)-\lambda W(t)].                            \tag{10}
\]

Hold R fixed. The full series for W and its first two group
derivatives converge uniformly; their norms on the fixed ball are
finite. Thus λW/M is a C² perturbation tending uniformly to zero
as λ→0. The contraction (8), with G_(θ,λ), supplies a unique
continuous periodic h_λ(θ), for every sufficiently small λ≥0,
with h_λ→h_0 uniformly as λ→0. This follows directly by
subtracting the two contraction equations: their fixed-point
distance is at most twice the uniform distance of the maps.
Uniform continuity of W on this compact set then permits one
λ_R>0, valid for every θ and 0≤λ≤λ_R, such that

\[
 T(t(\theta,\lambda))=\lambda W(t(\theta,\lambda)),\qquad
 \left|M^{-1}W(t(\theta,\lambda))-e^{i\theta}z_R\right|<r_*/2.
                                                                    \tag{11}
\]

In particular |W|≥m_R:=r_*M/2≥c√R/log R. To see every
argument without assuming a rotation symmetry of the background,
write the second expression in (11) as

\[
 W(t(\theta,\lambda))=M e^{i\theta}z_R[1+q_\lambda(\theta)],
 \qquad |q_\lambda(\theta)|<1/2.
\]

The argument of 1+q has a continuous 2π-periodic choice in
(−π/2,π/2), because its real part is positive. Consequently
θ+arg z_R+arg(1+q_λ(θ)) increases by exactly 2π between the
endpoints θ=0 and θ=2π. The intermediate value theorem gives
every argument modulo 2π; monotonicity is unnecessary. Choosing
the argument −φ_0 proves (2). Only primes through N_R were
changed from +1. This proves the displaced-circle statement for
every sufficiently large R, with no evaluated size for λ_R.

Fix such R for the rest of the proof and put
M_j=Σ_n a_R(n)(log n)^j<∞, j=0,1,2. At a sufficiently large
real x, L358 gives ω(x)>0 and 1/ω(x)≤λ_R. Use (2) at the
actual gamma angle φ(x), and write d=|W_R(χ_x)|≥m_R. The
frozen jets of (1) at x are

\[
 S=T=W/\omega,\qquad S'=-iW,\qquad
 S''=-\sum_n a_R(n)(\log n)^2\chi_x(n).
\]

Thus c=|S|=d/ω, e=|S″|≤M_2, V=S′+iωS=0 and
Im(e^(iφ)S′)=−d. L359's exact algebra and beta-error bound
apply to these jets; their derivation uses no particular prime
assignment. Its sufficient upper bound is therefore

\[
 U\le-d^2+\frac{dM_2}{\omega}
             +\frac{\gamma d^2}{\omega^2}+\mathcal E_\beta,
 \qquad \gamma=|\omega'|/2+|(\log A)''|.                           \tag{12}
\]

At fixed R, the absolute M_j bounds make the beta error uniform
over every phase assignment:
E_β=O_R((1+ω²)β)→0. L358 also gives γ→0 and ω→∞. Dividing
(12) by d²≥m_R² and taking x sufficiently large proves (3).
The phases selected for one x are held fixed in the jets; no
derivative of the selection χ_x is taken.

Finally suppose (4) holds at an actual x. Write W_a=iS_ε′(x).
Since ωT=W and e^(iφ)W=d is positive real,

\[
 |S_\varepsilon'+i\omega S_\varepsilon|
   =|\omega S_\varepsilon-W_a|\le m_R/8,\qquad
 |\operatorname{Im}(e^{i\phi}S_\varepsilon')|
   =|\operatorname{Re}(e^{i\phi}W_a)|\ge15m_R/16.
\]

Also c≤(M_1+m_R/16)/ω and e≤M_2. The first two terms of
L359's U are at most
(m_R/8)²−(15m_R/16)²=−221m_R²/256. Its ce term tends to
zero with this bound on c; γc² and the uniformly bounded beta
error tend to zero as well. Increasing X_R to make their sum at
most 93m_R²/256 proves the claimed upper bound −m_R²/2 for
the actual normalized sign. No second-moment approximation is
needed, only its absolute M_2 bound. ∎

This is a **REPRODUCTION** of the contraction and triangle data
in L362, elementary continuous argument control, and L359's
projected sign identity, specialized to the ready spectral target.
The gamma/beta and differentiated asymptotic inputs remain the
ones already cited in L358, including
[DLMF 5.11.1–3](https://dlmf.nist.gov/5.11#E1) and
[5.15.8–9](https://dlmf.nist.gov/5.15#E8). The closest screened
smoothed-series result, Paris, [arXiv:1503.07329v1](https://arxiv.org/pdf/1503.07329v1),
§2 and Theorem 1, does not supply these prime-phase controls or
actual-frequency visits. No originality beyond the checked sources
is claimed. No scalar transform theorem is reproved here.

The result removes local displacement and gamma-rotation obstacles
on the growing prime torus. It also rules out a nonnegative tail
certificate uniform over all unit-phase assignments in this class.
The remaining arithmetic requirement is (4) at the **same actual
frequency** as ω and φ. Its value window shrinks as 1/log x for
fixed R. L362's qualitative visits concern a fixed zero template
with an error independent of visit height; they do not imply (4)
for these displaced and rotated templates. Neither the existence
nor nonexistence of such visits is proved. The six finite bad
regulators and the condition ε_0<1/1000000 remain the only recorded
actual negative-sign evidence in this branch.

**Mathlib.** Full displaced-circle, every-angle template and actual
sign-transfer statements: **not checked**. Supporting contraction,
continuous-argument, complex norm and gamma/Fourier coverage is
also **not checked** here. The named DLMF inputs are supporting
formulas rather than a full matching theorem. No library absence
is asserted; general documentation is
[Mathlib](https://leanprover-community.github.io/mathlib4_docs/).
