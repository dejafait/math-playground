# Lemma 358: regulated Mellin spectrum and fixed-regulator negative signs

**Hypotheses.** Use L357's ψ, P=2D_u²−1/2, a_ε, z_ε,
h_ε, reflected k_ε and real Fourier transform F_ε, with 0<ε≤1.
Put

\[
 s=\tfrac14+\tfrac{i\xi}{2},\qquad p=\xi^2+\tfrac14,\qquad
 S_\varepsilon(\xi)=\sum_{n\ge1}n^{-1/2}
       \exp(-\pi\varepsilon n^2-i\xi\log n).
 \tag{1}
\]

The finite interval sign assertions below use L037's explicit
outward Decimal arithmetic contracts. The analytic identities and
conditional tail statement do not depend on numerical arithmetic.

**Conclusion.** At every real ξ,

\[
 F_\varepsilon(\xi)=-p\operatorname{Re}\left[
       \Gamma(s)\pi^{-s}S_\varepsilon(\xi)
       -\frac{\varepsilon^{s-1/2}}{2\sqrt\pi}
           \Gamma(s)\Gamma(1/2-s)\right].
 \tag{2}
\]

This identity may be differentiated twice in ξ, including the
complete subtraction and real projection. In particular, define

\[
 A=p|\Gamma(s)|\pi^{-1/4}>0,\quad
 \phi=\operatorname{Im}\log\Gamma(s)-\tfrac\xi2\log\pi,\quad
 \alpha=\tfrac12\log\varepsilon,\quad
 \beta=\frac{\varepsilon^{-1/4}|\Gamma(s)|}{2\pi^{1/4}}.
\]

Then y=F_ε/A=−Re(e^(iφ)S_ε)+βcos(αξ) and, exactly,

\[
 \frac{F_\varepsilon'^2-F_\varepsilon F_\varepsilon''}{A^2}
       =y'^2-yy''-(\log A)''y^2.                 \tag{3}
\]

There are certified negative values at the following three exact
rational pairs. The intervals displayed are deliberately enlarged
from the saved outward enclosures of (3).

| ε | ξ | enclosure of (F_ε′²−F_εF_ε″)/A² |
|---|---|---|
| 1/100 | 42679/5 | [−53/1000, −52/1000] |
| 3/1000 | 87587/10 | [−2636/1000, −2635/1000] |
| 1/1000 | 87029/5 | [−6744/1000, −6743/1000] |

Consequently a common threshold ε_0 for nonnegativity at every real
frequency and every 0<ε≤ε_0, if one exists, must satisfy ε_0<1/1000.
The finite examples do not show failure for arbitrarily small ε.

At fixed ε, let ω=φ′. Writing C=e^(iφ)S_ε, D=e^(iφ)S_ε′ and
E=e^(iφ)S_ε″ gives, as ξ→+∞,

\[
 \begin{aligned}
 \frac{F_\varepsilon'^2-F_\varepsilon F_\varepsilon''}{A^2}
 ={}&\omega^2|S_\varepsilon|^2
       +2\omega\operatorname{Im}(S_\varepsilon'\overline{S_\varepsilon})
       +(\operatorname{Re}D)^2-\operatorname{Re}C\operatorname{Re}E\\
    &+\omega'\operatorname{Re}C\operatorname{Im}C
       -(\log A)''(\operatorname{Re}C)^2
       +O_\varepsilon((1+\omega^2)\beta).        \tag{4}
 \end{aligned}
\]

Here ω=(1/2)log(ξ/(2π))+O(ξ^(−2)), ω′=O(1/ξ),
(log A)″=O(1/ξ²), and β=O_ε(ξ^(−1/4)exp(−πξ/4)).
If inf_(ξ∈R)|S_ε(ξ)|>0, (4) is strictly positive for all
sufficiently large ξ. No such lower bound is established for all
sufficiently small ε; (4) itself leaves the cancellation regime
unsigned. No actual-zeta Laguerre sign, zero-exclusion interval,
or higher associated-spectrum condition follows.

**Proof.** At fixed positive ε, the separate generators are now
integrable with every polynomial weight in u. As u→−∞,
a_ε=O_ε(e^(u/2)) and z_ε=O_ε(e^(u/2)); their first two u
derivatives have the same bound. As u→+∞, a_ε and its derivatives
decay faster than every exponential, while z_ε and its first two
derivatives are O(e^(−u/2)). These bounds follow directly from the
damped Gaussian series and the explicit z_ε. The local derivative
sums have Gaussian majorants at fixed ε. Thus two integrations by
parts have vanishing boundary terms, and

\[
 \widehat h_\varepsilon(\xi)
   =-(2\xi^2+1/2)\int_{\mathbb R}
                   (a_\varepsilon-z_\varepsilon)(u)e^{i\xi u}\,du.
 \tag{5}
\]

Reflection of the real h_ε conjugates its real-frequency transform.
The transform of its even reflection average is therefore
Re ĥ_ε. This retains the real projection in (2).

Substitute x=exp(2u) in the integral of (5). It becomes
(1/2)∫_0^∞ x^(s−1)[ψ(x+ε)−(x+ε)^(−1/2)/2]dx.
Both separate integrals converge absolutely: Re s=1/4, the Gaussian
sum is bounded at zero by ψ(ε), and the zero mode at infinity has
power x^(−5/4). The same bounds with |log x|^j, j≤2, are
integrable. For the series term, absolute summation of the integrals
is bounded by a constant times Σ_n exp(−πεn²)n^(−1/2).
With logarithmic weights, substitution v=πn²x adds only bounded
Gaussian-log integrals and powers of log n, still summable.
These are the bounds for the interchange and both ξ derivatives.

Import Euler's gamma Mellin integral
[DLMF 5.9.1](https://dlmf.nist.gov/5.9#E1), with ν=s, μ=1
and z=πn², and the positive-half-line beta integral
[DLMF 5.12.3](https://dlmf.nist.gov/5.12#E3), with parameters
s and 1/2−s. Their real parts are positive. They give respectively

\[
 \int_0^\infty x^{s-1}\psi(x+\varepsilon)\,dx
       =\Gamma(s)\pi^{-s}S_\varepsilon(\xi),\qquad
 \int_0^\infty x^{s-1}(x+\varepsilon)^{-1/2}\,dx
       =\frac{\varepsilon^{s-1/2}\Gamma(s)\Gamma(1/2-s)}{\sqrt\pi}.
\]

The factor 1/2 from du and the separate zero-mode factor 1/2,
together with (5), prove (2). These are applications of the covered
scalar transforms; neither scalar theorem includes this P, reflection
or infinite series. At ε=0 the separate integral argument is invalid
and is not used.

For real ξ, 1/2−s=conj s and Γ(conj s)=conj Γ(s). Thus the beta
product in (2) is |Γ(s)|²ε^(−1/4)exp(iαξ)/(2√π). Division by A
proves the expression for y. Differentiating F=A y shows
F′²−FF″=A²[y′²−yy″−(log A)″y²], proving (3).

For clarity, all quantities used in the computation can be evaluated
with differentiated identities, rather than differentiating an
uncontrolled numerical error. With Ψ=Γ′/Γ and Ψ_1=Ψ′, set

\[
 \begin{gathered}
 \omega=(\operatorname{Re}\Psi(s)-\log\pi)/2,
 \quad\omega'=-\operatorname{Im}\Psi_1(s)/4,\qquad
 q=(\log A)''=2/p-4\xi^2/p^2-\operatorname{Re}\Psi_1(s)/4,\\
 b=(\log\beta)'=-\operatorname{Im}\Psi(s)/2,
 \quad b'=-\operatorname{Re}\Psi_1(s)/4.
 \end{gathered}
\]

Termwise differentiation gives
S_ε^(j)=Σ_n(−i log n)^j n^(−1/2)exp(−πεn²−iξlog n), j≤2.
In particular,

\[
 \begin{aligned}
 y'={}&-\operatorname{Re}[e^{i\phi}(S_\varepsilon'+i\omega S_\varepsilon)]
       +\beta[b\cos(\alpha\xi)-\alpha\sin(\alpha\xi)],\\
 y''={}&-\operatorname{Re}[e^{i\phi}(S_\varepsilon''+2i\omega S_\varepsilon'
                          +(i\omega'-\omega^2)S_\varepsilon)]\\
       &+\beta[(b^2+b'-\alpha^2)\cos(\alpha\xi)
                         -2\alpha b\sin(\alpha\xi)].             \tag{6}
 \end{aligned}
\]

Here is the complete error argument for the finite certificate.
It uses exact rational inputs, L037's 70-digit interval operations
and π enclosure, and elementary logarithm, arctangent and sine/cosine
series with explicit tails. For the logarithm, after exact powers-of-two
reduction to 1≤x≤3, use log x=2Σ_(j≥0)t^(2j+1)/(2j+1),
t=(x−1)/(x+1), |t|≤1/2. After 96 terms its absolute tail is at most
2|t|^193/[193(1−|t|²)]. Arctangent reductions use the reciprocal
and angle-addition identities until |x|≤1/2; the 96-term alternating
series has the safe absolute tail |x|^193/[193(1−|x|²)]. All reductions
are within their checked principal real branches. After subtracting
an integer multiple of 2π, the trigonometric argument has absolute
value below four; the degree-49 Taylor polynomials have error at most
|x|^50/50!. These are the reused routines in
`scripts/laguerre/certify_bessel_gaps.py` and
`scripts/laguerre/certify_conditional_cosine.py`; no float enters
an acceptance check.

To enclose gamma, put w=s+32 and use the analytic logarithmic Stirling
expression

\[
 L(w)=(w-1/2)\log w-w+\tfrac12\log(2\pi)+\frac1{12w}.
\]

Import [DLMF 5.11.1 and §5.11(ii)](https://dlmf.nist.gov/5.11#ii):
for Re w>0, the remainder after 1/(12w) is bounded by the first
omitted term times sec(arg(w)/2)^4, hence by 1/(90|w|³).
On the complex disk of radius one about w, Re(w+z)>0 and
|w+z|≥ξ/2−1. Thus, with r=1/[90(ξ/2−1)³], the analytic remainder
R obeys |R|≤r, |R′|≤r and |R″|≤2r at the center, the latter two
by Cauchy's derivative estimate. Gamma recurrence gives

\[
 \begin{aligned}
 \log\Gamma(s)&=L(w)-\sum_{j=0}^{31}\log(s+j)+R(w),\\
 \Psi(s)&=\log w-\frac1{2w}-\frac1{12w^2}
                   -\sum_{j=0}^{31}\frac1{s+j}+R'(w),\\
 \Psi_1(s)&=\frac1w+\frac1{2w^2}+\frac1{6w^3}
                   +\sum_{j=0}^{31}\frac1{(s+j)^2}+R''(w).
 \end{aligned}
\]

Every complex logarithm is computed in the right half-plane using
log|z|=(1/2)log(Re(z)²+Im(z)²) and arg z=arctan(Im(z)/Re(z)).
The rectangular complex enclosures widen each real and imaginary
component by r, r and 2r respectively. This controls both frequency
derivatives without differentiating a big-O term.

For the infinite damped series choose last indices N=40,80,150 for
the displayed cases and m=N+1. For j=0,1,2 and n≥1,
n^(−1/2)(log n)^j≤n². The ratios of successive n²exp(−πεn²)
decrease, so a common absolute tail bound for S_ε and its first two
derivatives is

\[
 T=\frac{m^2e^{-\pi\varepsilon m^2}}
           {1-((m+1)/m)^2e^{-\pi\varepsilon(2m+1)}}.
\]

Each denominator is checked positive. Add [−T,T] to both components
of every finite complex sum. Evaluating (6) and then (3) yields the
outward intervals recorded in
`scripts/gaussian-zero-mode/first-spectrum-certificate.json`.
Their upper endpoints are respectively below −52/1000, −2635/1000
and −6743/1000. Since A>0, all three unnormalized signs are negative.
Reproduce the certificate with
`PYTHONDONTWRITEBYTECODE=1 python3 scripts/gaussian-zero-mode/certify_first_spectrum.py`.
The hypothesis ε_0≥1/1000 would include the third regulator and
contradict its certified negative value. This proves the asserted
necessary restriction, with the stated arithmetic contracts.

Finally, the covered differentiated gamma expansions
[DLMF 5.11.1–3](https://dlmf.nist.gov/5.11#E1),
[5.11.9](https://dlmf.nist.gov/5.11#E9) and
[5.15.8–9](https://dlmf.nist.gov/5.15#E8)
apply in the fixed right-half-plane sector and imply the asymptotics
following (4). At fixed ε, each S_ε^(j), j≤2, is bounded uniformly
in ξ by M_j=Σ_n n^(−1/2)exp(−πεn²)(log n)^j<∞. Also b and b′
are bounded at large ξ, so βcos(αξ) and its first two derivatives
are O_ε(β). Expanding (3), every product involving this term is
O_ε((1+ω²)β).

For T_0=Re C, direct differentiation gives
T_0′=Re D−ω Im C and
T_0″=Re E−2ω Im D−ω²Re C−ω′Im C.
Substitution proves the main expression in (4), including its signed
cross term. If |S_ε|≥m_ε>0 uniformly, its leading term is at least
ω²m_ε², the cross term has absolute value at most 2|ω|M_0M_1,
and every remaining nonvanishing term is bounded or tends to zero.
As ω→∞, strict positivity follows. The conclusion is conditional:
Gaussian damping does not supply the assumed lower bound here. ∎

This is a **REPRODUCTION** applying the named gamma/beta and
Stirling inputs to the exact approved family. The inspected sources
did not state (2) with this subtraction/reflection or the displayed
negative values; no originality is claimed. The three negative
regulators obstruct a common threshold at or above 1/1000, rather
than refuting the required existence of some ε_0>0. The vanishing
regulator sign certificate remains open. L357's absolute-error limit
and all previously established actual-zeta ranges are unchanged.

**Mathlib.** Full regulated Mellin identity, differentiated sign
formula, conditional tail statement and finite certificates: **not
checked**. Supporting gamma, beta, Cauchy derivative and Fourier
theorems are also **not checked** in Mathlib in this step. L037's
arithmetic contract is reused; no full matching library theorem or
library absence is asserted. General documentation:
https://leanprover-community.github.io/mathlib4_docs/.
