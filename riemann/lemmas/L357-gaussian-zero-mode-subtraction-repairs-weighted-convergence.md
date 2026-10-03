# Lemma 357: Gaussian zero-mode subtraction repairs weighted convergence

**Hypotheses.** Let ψ(t)=Σ_(n≥1)exp(−πn²t) for t>0,
P=2D_u²−1/2, and k be the actual smooth even theta kernel,
equal on u≥0 to K from L019. For 0≤ε≤1 and u∈R define

\[
 a_\varepsilon(u)=e^{u/2}\psi(e^{2u}+\varepsilon),\qquad
 z_\varepsilon(u)=\tfrac12e^{u/2}(e^{2u}+\varepsilon)^{-1/2},
\]

\[
 h_\varepsilon=P(a_\varepsilon-z_\varepsilon),\qquad
 k_\varepsilon(u)=\tfrac12[h_\varepsilon(u)+h_\varepsilon(-u)],\qquad
 F_\varepsilon(\xi)=\int_{\mathbb R}k_\varepsilon(u)e^{i\xi u}\,du.
\]

The extension to ε=0 in these definitions is pointwise at each real u;
no individual whole-line integral of a_0 or z_0 is assumed.

**Conclusion.** h_0=k_0=k. All h_ε are smooth, and all k_ε are smooth
and even with every absolute polynomial moment. There is a finite
constant C, independent of ε and u, such that

\[
 |h_\varepsilon(u)-k(u)|\le C\varepsilon e^{-5|u|/2},\qquad
 |k_\varepsilon(u)-k(u)|\le C\varepsilon e^{-5|u|/2}.
 \tag{1}
\]

In particular,

\[
 \int_{\mathbb R}(1+u^2)|k_\varepsilon(u)-k(u)|\,du
       \le \tfrac{132}{125}C\varepsilon\longrightarrow0.
 \tag{2}
\]

For j=0,1,2 the real-axis derivatives F_ε^(j) converge uniformly to
F_0^(j), with error O(ε). Their first Laguerre combinations satisfy

\[
 \sup_{\xi\in\mathbb R}
 \left|F_\varepsilon'(\xi)^2-F_\varepsilon(\xi)F_\varepsilon''(\xi)
       -[F_0'(\xi)^2-F_0(\xi)F_0''(\xi)]\right|=O(\varepsilon).
 \tag{3}
\]

No sign of any of these combinations, complex-plane convergence,
or higher Laguerre condition is asserted.

**Proof.** Import the scalar Gaussian Poisson identity in L016,
equivalently [DLMF 20.7.32](https://dlmf.nist.gov/20.7#E32) or
Sutherland, *The functional equation*, MIT 18.785 Lecture 17,
Lemma 17.10, [pp. 2–3](https://math.mit.edu/classes/18.785/2019fa/LectureNotes17.pdf#page=2).
Its normalization is θ(t)=1+2ψ(t)=t^(−1/2)θ(1/t). Hence, exactly,

\[
 f(t):=\psi(t)-\tfrac12t^{-1/2}
       =R(t)-\tfrac12,\qquad
 R(t):=t^{-1/2}\psi(1/t).
 \tag{4}
\]

We specialize this known identity; we do not reprove Poisson summation
or infer a uniform integral estimate from the identity alone.
On every compact t interval in (0,∞), each differentiated Gaussian
series is bounded by Σ_n C n^(2j)exp(−c n²) for c>0.
This proves local uniform convergence and all required derivatives.

Put x=e^(2u). For any smooth f, differentiation of the entire
prefactor, using D_u x=2x, gives

\[
 P[e^{u/2}f(x+\varepsilon)]
       =e^{u/2}[12x f'(x+\varepsilon)+8x^2 f''(x+\varepsilon)].
 \tag{5}
\]

Thus this is h_ε, and

\[
 \partial_\varepsilon h_\varepsilon(u)
       =e^{u/2}[12x f''(x+\varepsilon)+8x^2 f'''(x+\varepsilon)].
 \tag{6}
\]

The constant −1/2 in (4), after multiplication by e^(u/2), is
annihilated by P. All derivatives of z_ε have been retained in (5).
At ε=0, z_0=e^(−u/2)/2 is also annihilated by P. Therefore h_0=P A,
where A(u)=e^(u/2)ψ(e^(2u)). L016's transformation gives
A(u)−A(−u)=−sinh(u/2). Since P commutes with reflection and kills
sinh(u/2), P A is even. It agrees on u≥0 with L019's K, so h_0=k
on all of R and k_0=k. This also gives its smooth even extension.

We now bound (6) uniformly, including its moving small-parameter
region. For j≤3, repeated differentiation of R gives a finite sum

\[
 R^{(j)}(t)=\sum_{\ell=0}^j
       c_{j\ell}t^{-(j+\ell+1/2)}\psi^{(\ell)}(1/t),
 \tag{7}
\]

with constant coefficients. This form follows by the product and
chain rules; differentiating ψ^(ℓ)(1/t) introduces −t^(−2).
For 0<t≤1, L016's derivative tail bound at 1/t≥1 implies

\[
 |R^{(j)}(t)|\le C_j^* t^{-2j-1/2}e^{-\pi/t}.
 \tag{8}
\]

The bound tends to zero at t=0 and is bounded on (0,1]. On [1,2],
the locally uniformly differentiable series makes R^(j) continuous,
hence bounded. Consequently the two constants

\[
 M_j=\sup_{0<t\le2}|R^{(j)}(t)|<\infty,\qquad j=2,3,
\]

are finite. If u≤0, then 0<x≤1 and x+ε≤2. Equations (4) and (6)
therefore give, for every 0≤ε≤1,

\[
 |\partial_\varepsilon h_\varepsilon(u)|
 \le e^{u/2}(12x M_2+8x^2M_3)
 \le (12M_2+8M_3)e^{5u/2}.
 \tag{9}
\]

This bound requires neither x≫ε nor x≪ε and includes x comparable
to ε. The regulated subtraction's individually large zero-mode
terms have canceled before this estimate is made.

For u≥0, use the original series at t=x+ε≥x≥1. Direct derivatives are

\[
 f''(t)=\psi''(t)-\tfrac38t^{-5/2},\qquad
 f'''(t)=\psi'''(t)+\tfrac{15}{16}t^{-7/2}.
 \tag{10}
\]

Let C_2,C_3 be the finite tail constants from L016. From (6) and
(10), since e^(u/2)=x^(1/4),

\[
 |\partial_\varepsilon h_\varepsilon(u)|
 \le x^{1/4}(12C_2x+8C_3x^2)e^{-\pi x}+12x^{-5/4}
 \le C_+ e^{-5u/2},
 \tag{11}
\]

where one possible finite C_+ is
12+sup_(x≥1)(12C_2x^(5/2)+8C_3x^(7/2))exp(−πx).
The algebraic coefficient 12 is 12·(3/8)+8·(15/16);
the polynomial times a Gaussian in this supremum is bounded.

Take C=max(12M_2+8M_3,C_+). At every fixed u, integrate (6)
from 0 to ε using (9)–(11). Since h_0=k, this proves the first
bound in (1). The second follows by reflection and evenness of k:
each of its two summands has the same bound Cεexp(−5|u|/2).
This is a pointwise common envelope on the whole line, not just
compact convergence of a differentiated sum.

By L019 and evenness, k has every absolute polynomial moment.
Equation (1) therefore gives the same property for h_ε and k_ε.
They are smooth by the local series bounds and smooth positive
parameter x+ε; reflection preserves smoothness. Finally,

\[
 \int_{\mathbb R}(1+u^2)e^{-5|u|/2}\,du
       =\frac{2}{5/2}+\frac{4}{(5/2)^3}=\frac{132}{125}.
\]

This proves (2), with a uniform bound on escaping weighted tails.

The moment bounds justify differentiating the real Fourier integral:
F_ε^(j)(ξ)=∫(iu)^j k_ε(u)exp(iξu)du for j≤2. Since
|u|^j≤1+u² for these j, (2) bounds each uniform derivative error
by (132/125)Cε. All three derivatives are uniformly bounded in ε
and ξ by the corresponding absolute moments of k and the common
error envelope. Subtracting the products in (3) and using these
uniform bounds proves (3); for example its absolute error is at most

\[
 |F_\varepsilon'-F_0'|(|F_\varepsilon'|+|F_0'|)
 +|F_\varepsilon-F_0||F_\varepsilon''|
 +|F_0||F_\varepsilon''-F_0''|.
\]

All preceding interchanges use compact Gaussian bounds or a stated
absolute moment envelope. In particular no integration of separate
divergent generators is involved. ∎

The required threshold in the saved assessment was precisely (2).
It is met, repairing this regulated family's version of the
whole-line obstruction in L235. L235's finite averages remain a
different, failed construction. This result applies the covered
scalar Poisson and derivative-tail tools and is a **REPRODUCTION**;
the inspected sources did not state the full regulated weighted
limit, and no originality is claimed. The exact rational derivative
audit can be reproduced with
`python3 scripts/gaussian-zero-mode/check_derivatives.py`.

The downstream quantity is the first associated spectrum from L233.
Equation (3) controls its error in absolute size but supplies no
nonnegative margin for any approximant. The limiting expression can
be arbitrarily small at large real frequencies; an O(ε) absolute
bound alone cannot sign it. Positivity of the approximation and
the higher levels remain separate missing inputs. No established
actual-zeta sign or zero-exclusion range is extended here.

**Mathlib.** Full regulated weighted-convergence statement: **not
checked**. The saved L016 check records the scalar Poisson theorem
[Real.tsum_exp_neg_mul_int_sq](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/SpecialFunctions/Gaussian/PoissonSummation.html#Real.tsum_exp_neg_mul_int_sq)
and smooth-series differentiation
[hasDerivAt_tsum_of_isPreconnected](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Calculus/SmoothSeries.html#hasDerivAt_tsum_of_isPreconnected)
as present supporting results in the documentation it checked.
They are not matches for (1)–(3), and their live versions were not
rechecked. Target-specific integral and Fourier coverage is **not
checked**, rather than asserted absent.
