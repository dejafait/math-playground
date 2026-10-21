# Lemma 366: first Gaussian regulator response and a coupled gamma-scale remainder

**Hypotheses.** Use L357's real Fourier transform F_ε of the even,
zero-mode-subtracted Gaussian family, including F_0. For real ξ put

\[
 s=\tfrac14+\tfrac{i\xi}{2},\quad w=2s=\tfrac12+i\xi,\quad
 p=\xi^2+\tfrac14,\quad Q=p\Gamma(s)\pi^{-s},\quad
 A=|Q|=p|\Gamma(s)|\pi^{-1/4}.
\]

This is exactly the positive envelope A of L358. Write
Λ(v)=π^(−v/2)Γ(v/2)ζ(v), continued meromorphically, and
ξ_c(v)=v(v−1)Λ(v)/2 for the entire completion in L018;
ξ_c is distinguished from the real frequency ξ. Set
T=1+|ξ| and L=log(2+|ξ|). Constants below are absolute for this
fixed family and may depend on j, but not on ε or ξ.

**Conclusion.** The right derivative G=∂_εF_ε|_(ε=0) exists, including
its first two real frequency derivatives, and

\[
 \begin{aligned}
 F_0(\xi)&=-p\operatorname{Re}\Lambda(\tfrac12+i\xi)
              =2\xi_c(\tfrac12+i\xi),\\
 G(\xi)&=\pi\operatorname{Re}[Q\zeta(2s-2)]
       =p\operatorname{Re}[(s-1)\Lambda(2s-2)]\\
       &=p\operatorname{Re}\frac{\xi_c(-3/2+i\xi)}{-5/2+i\xi}
        =-p\operatorname{Re}\frac{\xi_c(5/2+i\xi)}{5/2+i\xi}.
 \tag{1}
 \end{aligned}
\]

For j=0,1,2, |ξ|≥40, and 0<ε≤1/(1+ξ²),

\[
 \frac{|\partial_\xi^j(F_\varepsilon-F_0-\varepsilon G)|}{A}
       \le C_j\varepsilon^2 T^4 L^j,\qquad
 \frac{|G^{(j)}|}{A}\le D_j T^2 L^j.                 \tag{2}
\]

In particular (2) meets the assessed, weaker test bound
C_j ε²T^(9/2)L^(j+2). Division is by A, never by F_0 or ζ.
No Laguerre sign or zero-exclusion statement is asserted.

**Proof.** The sources approved in the saved regulator-response
assessment are used only for scalar Mellin inversion, zeta reflection,
and gamma estimates: Paris, *The asymptotic expansion of a generalisation
of the Euler-Jacobi series*, arXiv:1503.07329v1, §2, (2.1)–(2.6),
[pp. 2–5](https://arxiv.org/html/1503.07329v1); NIST
[DLMF 25.4.1–5](https://dlmf.nist.gov/25.4) and
[5.11.9–13](https://dlmf.nist.gov/5.11#E9).
Paris's fixed-real-exponent theorem is not applied at the growing
complex exponent. We prove the required family-specific uniformity.

First justify the derivative at zero on the kernel side. In L357's
notation x=e^(2u), f(t)=ψ(t)−t^(−1/2)/2, and

\[
 \partial_\varepsilon h_\varepsilon(u)
   =e^{u/2}[12x f''(x+\varepsilon)+8x^2 f'''(x+\varepsilon)].
 \tag{3}
\]

L357's proof, (9)–(11), bounds (3), for every 0≤ε≤1, by
C exp(−5|u|/2). It is pointwise continuous at ε=0. Reflecting and
averaging gives the same common envelope for ∂_εk_ε. Dominated
convergence, also with weights |u|^j for j≤2, proves the right
parameter derivative and its two frequency derivatives. More explicitly,
the difference quotient is the integral average of (3) over [0,ε],
so it has this same envelope. Thus the derivative does not integrate
the individually divergent generators at ε=0. Its kernel is the even
reflection average of the expression (3) with ε=0.

For ε>0 apply inverse Mellin inversion of exp(−t) to L358's
S_ε=Σ_(n≥1)n^(−2s)exp(−πεn²). On Re z=1,

\[
 S_\varepsilon(\xi)=\frac1{2\pi i}
     \int_{1-i\infty}^{1+i\infty}
        \Gamma(z)(\pi\varepsilon)^{-z}\zeta(2s+2z)\,dz.
 \tag{4}
\]

The interchange with the n sum is absolute: Re(2s+2z)=5/2,
Σ_n n^(−5/2)<∞, and ∫_R|Γ(1+iv)|dv<∞. These bounds apply at
each fixed positive ε. They are not an ε=0 interchange.

Shift (4) to Re z=−5/2. The poles crossed are the simple zeta pole
at z=1/2−s and the gamma poles z=0,−1,−2. The zeta residue in z
is 1/2, so its contribution is

\[
 \tfrac12\Gamma(1/2-s)(\pi\varepsilon)^{s-1/2}.
 \tag{5}
\]

For completeness, the horizontal edges vanish at fixed ε and ξ.
The strip estimate (4) in L320, with R=5, and the completed-zeta
formula give polynomial vertical growth for ζ(v) on
−9/2≤Re v≤5/2 at large |Im v|. To divide by Γ(v/2), use its
vertical Stirling estimate after finitely many recurrence steps; the
exponential factors cancel, and v(v−1) is bounded away from zero
at those heights. This bound is uniform in Re v in the stated compact
strip. Gamma in the contour variable has exponential decay
exp(−π|Im z|/2) times a fixed polynomial, uniformly for
−5/2≤Re z≤1. At horizontal height V>2|ξ|+2 the zeta argument's
height is comparable to V. The remaining factor (πε)^(−Re z) is
bounded on this finite horizontal interval for fixed ε. Thus both
horizontal integrals tend to zero. Bounded-height poles are enclosed
before taking V to infinity. No uniform limit in ε or ξ is needed
for this exact displacement.

Multiplication of (5) by Γ(s)π^(−s) gives precisely

\[
 \frac{\varepsilon^{s-1/2}}{2\sqrt\pi}
        \Gamma(s)\Gamma(1/2-s),
\]

the full subtraction in L358, (2). It cancels as a complex identity
before taking a real part or differentiating. In particular no
ε^(−1/4) term, or frequency derivative of such a term, is omitted.
The gamma residues therefore give the exact formula

\[
 F_\varepsilon=-\operatorname{Re}\left\{Q\left[
       \zeta(2s)-\pi\varepsilon\zeta(2s-2)
       +\frac{(\pi\varepsilon)^2}{2}\zeta(2s-4)
       +r_\varepsilon(\xi)\right]\right\},         \tag{6}
\]

where

\[
 r_\varepsilon(\xi)=\frac1{2\pi i}
       \int_{-5/2-i\infty}^{-5/2+i\infty}
        \Gamma(z)(\pi\varepsilon)^{-z}\zeta(2s+2z)\,dz.
 \tag{7}
\]

We now establish differentiated, uniform bounds for (7). The scalar
functional equation, for example DLMF 25.4.2, writes

\[
 \zeta(v)=2^v\pi^{v-1}\sin(\pi v/2)\Gamma(1-v)\zeta(1-v).
 \tag{8}
\]

On a fixed closed negative-real-part strip, absolute convergence of
the right-hand Dirichlet series, the vertical gamma estimate, and
|sin(πv/2)|≤C exp(π|Im v|/2) give

\[
 |\zeta(\sigma+it)|\le C(2+|t|)^{1/2-\sigma}.
 \tag{9}
\]

Here we may take the three closed strips |Re v−σ|≤1/4 centered
at σ=−3/2,−7/2,−9/2. On their union Re(1−v)≥9/4, so the
absolute Dirichlet bound is at most ζ(9/4); all gamma arguments
1−v have positive real part. The constants in vertical Stirling
are uniform over this finite union. For bounded |t| the same bound
follows by compactness and holomorphy, so (9) holds for every t.
There is no pole in these neighborhoods.

Cauchy's derivative estimate on disks of radius
ρ=min(1/4,1/log(2+|t|)) centered at σ+it now yields, for b=0,1,2,

\[
 |\zeta^{(b)}(\sigma+it)|
       \le C_b(2+|t|)^{1/2-\sigma}\log^b(2+|t|).
 \tag{10}
\]

Indeed the power variation across the disk costs at most a constant:
(2+|t|)^ρ≤e, and the bounded change in height also costs a constant.
The reciprocal radius is at most a fixed multiple of log(2+|t|).
This explains the derivatives without differentiating an asymptotic
error. Equation (10) is used at the three fixed centers above, not
as a claim uniform over all negative σ.

On z=−5/2+iv the zeta argument is −9/2+i(ξ+2v).
Also |Γ(−5/2+iv)|≤C(1+|v|)^(−3)exp(−π|v|/2), with a larger
constant at bounded v; the line contains no gamma pole. Differentiation
in ξ of ζ(2s+2z) contributes i^bζ^(b), and does not differentiate
(πε)^(−z). Equations (7) and (10) imply

\[
 |r_\varepsilon^{(b)}(\xi)|
       \le E_b\varepsilon^{5/2}T^5L^b,
       \qquad b=0,1,2.                            \tag{11}
\]

To see the uniform integrability explicitly, use
2+|ξ+2v|≤2(2+|ξ|)(1+|v|) and bound its logarithm by a constant
multiple of L(1+log(1+|v|)). The remaining majorant is
|Γ(−5/2+iv)|(1+|v|)^5(1+log(1+|v|))^b, whose integral is finite
by exponential gamma decay. This majorant also justifies both
frequency derivatives under (7), locally uniformly in ξ. It
covers the neighborhood ξ+2v=0 as well as both large-height tails.
No constant in (11) depends on the frequency or the regulator.

Explicitly, put
M_b=∫_R |Γ(−5/2+iv)|(1+|v|)^5(1+log(1+|v|))^b dv.
At infinity its integrand is O((1+|v|)^2
exp(−π|v|/2)(1+log(1+|v|))^b), and it is continuous on every
bounded interval, so M_b<∞. The constant E_b in (11) can be
chosen as a fixed multiple of π^(5/2)M_b/(2π), using (10) and
2+|ξ|≤2T. In particular, near v=−ξ/2 we use the bounded-height
case of (10), not a large-height expansion with a vanishing argument.
For differentiation, fix any compact ξ interval and apply this same
majorant with its largest T and L. This proves local dominated
differentiation while the displayed final constants remain global.

The external factor Q satisfies, for a=0,1,2 and |ξ|≥40,

\[
 |Q^{(a)}|/A\le B_a L^a.                         \tag{12}
\]

For a=0 this is equality. For the others, set Ψ=Γ′/Γ. L358's
controlled differentiated Stirling and recurrence formulas give
Ψ(s)=O(L) and Ψ′(s)=O(1) in this range. Equivalently these follow
from the scalar log-Stirling remainder and Cauchy estimate already
used there. Direct differentiation gives
Q′/Q=2ξ/p+(i/2)(Ψ(s)−log π) and
(Q′/Q)′=2/p−4ξ²/p²−Ψ′(s)/4. These prove (12), including negative
ξ by conjugation. This concerns derivatives of Q, not derivatives
of the envelope used as divisor after differentiation.

For each fixed ξ, (11) and (6), together with L357's convergence,
identify F_0=−Re[Qζ(2s)] and
G=π Re[Qζ(2s−2)]. This agrees with the derivative justified in
(3). The identity for F_0 in (1) follows because
w(w−1)=−p and ξ_c(w) is real on w=1/2+iξ by L018.
The completion identity extends meromorphically from L018's
right-half-plane identity by the identity theorem, so it applies at
2s−2=−3/2+iξ as well. Gamma recurrence gives
πΓ(s)π^(−s)ζ(2s−2)=(s−1)Λ(2s−2). Since
ξ_c(2s−2)=(s−1)(2s−3)Λ(2s−2), this proves the first shifted
quotient in (1). L018's reflection and conjugation give
ξ_c(−3/2+iξ)=ξ_c(5/2−iξ); conjugating the quotient's real part
changes its denominator to −5/2−iξ=−(5/2+iξ).
This proves the last expression, including its minus sign.

Subtract F_0+εG in (6). Equation (10) at σ=−7/2, with height ξ,
bounds the remaining second-order residue and its b derivatives by
C_b ε²T^4L^b. Apply Leibniz's rule, (11), and (12) to obtain

\[
 \frac{|\partial_\xi^j(F_\varepsilon-F_0-\varepsilon G)|}{A}
   \le C_j[\varepsilon^2T^4+\varepsilon^{5/2}T^5]L^j.
 \tag{13}
\]

The coupled condition supplies
εT²≤(1+|ξ|)²/(1+ξ²)≤2, hence
ε^(5/2)T^5≤sqrt(2) ε²T^4. This proves the first bound in (2).
Equation (10) at σ=−3/2 and (12) give the second. Both real
projection and the full subtracted transform have been retained. ∎

The exact assessed test is met with a smaller polynomial and logarithmic
power. The meaningful small parameter for these logarithmically scaled
frequency jets is εT²: their normalized remainder is
O((εT²)²) after division by L^j, and their first response is
O(εT²). At the allowed upper boundary ε≈|ξ|^(−2), (2) only gives
O(L^j), not a vanishing remainder or a signed approximation.
For an unscaled o(1) remainder in all three jets a sufficient condition
is εT²L→0. Making also the entire first response o(1) in all three
unscaled jets is assured by εT²L²→0. None of these upper bounds
establishes a lower sign margin. Higher Laguerre estimates and the
main global positivity gap remain unresolved; no RH candidate arises.

This is a **REPRODUCTION**, specializing the assessed scalar contour
and completion tools. The closest checked fixed-exponent expansion
does not state this coupled two-derivative bound; no originality beyond
the sources checked is claimed. The previous fixed-regulator global-sign
stop remains in force for that certificate.

**Critical audit, 2026-10-05.** The conclusions (1)–(2) survive with
their stated domain and constants; no stronger bound is asserted.
The moving pole has real part 1/4, disjoint from all three crossed
gamma poles, and its residue cancels the complex subtraction before
any derivative. The contour displacement is exact at fixed parameters;
the subsequent global majorant, including the bounded shifted-height
region, supplies the uniformity. In Leibniz's rule each term is bounded
by a constant times L^(j−b) times the b-th derivative bound, yielding
exactly L^j in (13), without differentiating a big-O remainder.
All frequency derivatives hold ε fixed: restricting their values to
the coupled domain does not take derivatives along a curve ε=ε(ξ).
The response quotient uses meromorphic continuation before reflection,
and F_0=2ξ_c, rather than ξ_c, is retained. The three input estimates
are unconditional analytic estimates, independent of L358's numerical
sign certificates. Thus this audit validates the previously pending
specialization, not new mathematics beyond the sources checked or a
relative estimate at zeros of F_0. The positive divisor A has no zeros;
an actual signed margin and higher Laguerre levels remain unproved.

**Mathlib.** Full regulator-response and coupled-remainder statement:
**not checked**. L357 retains the present supporting Poisson reference
[Real.tsum_exp_neg_mul_int_sq](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/SpecialFunctions/Gaussian/PoissonSummation.html#Real.tsum_exp_neg_mul_int_sq)
and smooth-series reference
[hasDerivAt_tsum_of_isPreconnected](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Calculus/SmoothSeries.html#hasDerivAt_tsum_of_isPreconnected)
from its previously checked sources. These support kernel interchanges,
not the full statement (1)–(2). Gamma/zeta Mellin and Cauchy coverage
in Mathlib was not checked here; no absence is asserted.
