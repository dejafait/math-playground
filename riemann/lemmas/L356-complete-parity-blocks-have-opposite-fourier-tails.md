# Lemma 356: complete parity blocks have opposite first-associated Fourier tails

**Hypotheses.** For n≥1 and real u set

\[
 q_n(u)=(8\pi^2n^4e^{9u/2}-12\pi n^2e^{5u/2})
             e^{-\pi n^2e^{2u}},\qquad
 K(u)=\sum_{n\ge1}q_n(u).
\]

This is the actual theta kernel: L019 identifies its positive half-line
series, and L234 proves that this whole-line series is smooth and even.
Put

\[
 e(u)=\sum_{j\ge1}q_{2j}(u),\qquad
 o(u)=\sum_{j\ge1}q_{2j-1}(u),\qquad
 k_e(u)=e(|u|),\quad k_o(u)=o(|u|),\quad k_n(u)=q_n(|u|).
\]

Use the Fourier convention E(x)=∫_R k_e(u)e^(ixu)du and
O(x)=∫_R k_o(u)e^(ixu)du. For ε=0,1 define the complete blocks

\[
 A_\varepsilon(t)=\int_{\mathbb R}s^2
    \sum_{\substack{n,m\ge1\\n+m\equiv\varepsilon\pmod2}}
       k_n(s+t)k_m(s-t)\,ds,
 \qquad \widehat A_\varepsilon(\xi)=
       \int_{\mathbb R}A_\varepsilon(t)e^{i\xi t}\,dt.
\]

**Conclusion.** Both blocks are continuous, even and integrable, and
their defining infinite sums and Fourier integrals converge as specified
below. There is a strictly positive constant

\[
 b=\sum_{j\ge1}2v_j(8v_j^2-30v_j+15)e^{-v_j},
       \qquad v_j=4\pi j^2,
\]

such that e′(0)=−b and o′(0)=b. In particular, reflecting either complete
half-sum leaves a nonzero first-derivative jump. Exact scalar modular
resummation retains it, and includes the alternating dual phase of the
odd class. As x→+∞,

\[
 \boxed{\widehat A_0(2x)=-4b^2x^{-6}+O(x^{-8}),\qquad
        \widehat A_1(2x)= 4b^2x^{-6}+O(x^{-8}).}
\]

Thus the complete same-parity block A_0 is not positive definite. The
opposite-parity spectrum is eventually positive; its sign at every
frequency is not asserted. The two leading tails cancel in their total,
which remains exactly the unsigned actual-theta spectrum from L233:

\[
 \widehat A_0(2x)+\widehat A_1(2x)
       =\Xi'(x)^2-\Xi(x)\Xi''(x).
\]

No negative total spectrum, RH counterexample, new Laguerre sign or
extension of a zero-exclusion interval follows.

**Proof.** First supply bounds for the actual infinite half-sums. With
v=πn²e^(2u), repeated differentiation gives

\[
 q_n^{(\ell)}(u)=e^{u/2}P_\ell(v)e^{-v},\quad
 P_0(v)=8v^2-12v,\quad
 P_{\ell+1}=\tfrac12P_\ell+2vP_\ell'-2vP_\ell.
\]

Every P_ℓ is a fixed polynomial. For v≥π its absolute value is at most
C_ℓ exp(v/2), with a finite constant depending only on ℓ. Therefore,
for u≥0,

\[
 \sum_{n\ge1}|q_n^{(\ell)}(u)|
 \le C_\ell e^{u/2}\sum_{n\ge1}e^{-\pi n^2e^{2u}/2}
 \le C_\ell' e^{u/2}e^{-\pi e^{2u}/2}.
 \tag{1}
\]

The second inequality uses
Σ_n exp(−π(n²−1)/2)<∞ and e^(2u)≥1. On every compact real u interval
there is also a differentiated Gaussian bound with a positive lower
bound for e^(2u). Thus all series defining K,e,o can be differentiated
termwise locally to every order. On [0,∞), every derivative and every
polynomial-weighted derivative of e,o is integrable and decays faster
than every exponential by (1). In particular their reflected functions
are continuous and have all absolute moments. This estimates the two
infinite functions themselves; it does not pass an N-dependent
remainder from a finite truncation to infinity.

The exact resummation can be checked before integrating in any
unbounded variable. Write θ(y)=Σ_{j∈Z}exp(−πj²y) and
α(y)=Σ_{j∈Z}(−1)^j exp(−πj²y). The full even and odd index classes
are respectively θ(4y) and θ(y)−θ(4y). Applying the scalar Poisson
identity of L016, and using α(z)=2θ(4z)−θ(z), gives

\[
 \theta(4y)=\frac{1}{2\sqrt y}\theta\!\left(\frac1{4y}\right),
 \qquad
 \theta(y)-\theta(4y)=\frac{1}{2\sqrt y}
                  \alpha\!\left(\frac1{4y}\right).
 \tag{2}
\]

These are standard scalar and characteristic theta transformations,
specialized to the two sublattices. Supporting named identities are
[DLMF 20.7.32–33](https://dlmf.nist.gov/20.7#E32) and the
[characteristic transformation, 21.5.9](https://dlmf.nist.gov/21.5#E9);
no positive-definiteness preservation statement is imported.

Keep the actual polynomial weight by writing P=2D_u²−1/2. The two
half-line generators, extended for this calculation to all real u,
are

\[
 a_e(u)=\tfrac12e^{u/2}[\theta(4e^{2u})-1],\qquad
 a_o(u)=\tfrac12e^{u/2}[\theta(e^{2u})-\theta(4e^{2u})].
\]

Direct differentiation, as in L019, gives e=P a_e and o=P a_o.
Substituting (2), including its factor and zero-frequency terms, gives

\[
 a_e(u)=\tfrac14e^{-u/2}\theta(e^{-2u}/4)-\tfrac12e^{u/2},
 \qquad
 a_o(u)=\tfrac14e^{-u/2}\alpha(e^{-2u}/4).
 \tag{3}
\]

The pure exponentials in (3) are annihilated by P. Differentiating all
remaining factors, justified on compact intervals by the Gaussian
bounds, gives the exact weighted formulas

\[
 e(u)=2^{-1/2}\sum_{j\ge1}q_j(-u-\log2),\qquad
 o(u)=2^{-1/2}\sum_{j\ge1}(-1)^j q_j(-u-\log2).
 \tag{4}
\]

In particular the odd dual phase is retained. No derivative of the
prefactor has been dropped: P acts on the entire expression in (3),
which is exactly the source of the two polynomial terms in q_j.
We will not integrate or interchange these dual series on the whole
line. All such estimates below use (1) on the original half-line.

There is also the direct sublattice identity
q_(2j)(u)=2^(−1/2)q_j(u+log2). Hence, using the smooth even K from L234,

\[
 e(u)=2^{-1/2}K(u+\log2)=2^{-1/2}K(-u-\log2),\qquad
 o(u)=K(u)-e(u).
 \tag{5}
\]

Thus zero of the reflected even half-sum is a shifted point of K,
rather than its evenness center. L234's boundary calculation gives

\[
 d_n:=q_n'(0)=-2\pi n^2(8\pi^2 n^4-30\pi n^2+15)e^{-\pi n^2},
       \qquad \sum_{n\ge1}d_n=K'(0)=0.
\]

The series of derivatives converges absolutely by (1). For every even n,
v=πn²>12, and 8v²−30v+15=v(8v−30)+15>0. Consequently
e′(0)=Σ_j d_(2j)=−b<0 and o′(0)=b.
The jumps of k_e′ and k_o′ at zero are respectively −2b and 2b.
Equations (2)–(5) cancel their sum, not either jump separately.

Next justify the associated-block Fourier formulas. On the positive
half-line every q_n is positive by L019, so 0≤k_e,k_o≤K and
k_e+k_o=K. Tonelli and the same absolute moment change of variables
as in L233 therefore give

\[
 A_0=A(k_e)+A(k_o),\qquad
 A_1(t)=\int s^2[k_e(s+t)k_o(s-t)+k_o(s+t)k_e(s-t)]\,ds,
 \tag{6}
\]

where A(f)(t)=∫s²f(s+t)f(s−t)ds. Their sum is A(K). It is continuous
and integrable, as are the individual terms: continuity follows by
domination on compact t intervals from their exponential envelopes;
for integrability put u=s+t,v=s−t and use
∫∫(|u|+|v|)²K(u)K(v)du dv<∞. These bounds also justify the complete
double-series expansion and every Fourier/Fubini interchange in (6).
Evenness follows by t↦−t and interchange of the two indices.

Apply L233 to k_e and k_o for A_0. For the symmetric cross term A_1,
either perform the same absolutely integrable change of variables or
polarize L233's formula at k_e+k_o. One obtains, exactly for real x,

\[
 \widehat A_0(2x)=\tfrac14[(E')^2-EE''+(O')^2-OO''],\qquad
 \widehat A_1(2x)=\tfrac14[2E'O'-E''O-EO''].
 \tag{7}
\]

In particular the second derivatives and the frequency scaling have
not been replaced by absolute squares.

For a smooth half-line h with the derivative bounds just established,
repeated integration by parts gives

\[
 \int_0^\infty h(u)\cos(xu)\,du
    =-h'(0)x^{-2}+h'''(0)x^{-4}+O_h(x^{-6}),
\]

and

\[
 \int_0^\infty h(u)\sin(xu)\,du
    =h(0)x^{-1}-h''(0)x^{-3}+O_h(x^{-5}).
\]

Here the remainders are bounded by finite boundary derivatives and
L¹ norms of derivatives of h; the boundary at infinity vanishes by
(1). Applying these separately to h=e,u e,u²e, and differentiating
only the original Fourier integral by its absolute moments, gives

\[
 E=-2d x^{-2}+O(x^{-4}),\quad E'=4d x^{-3}+O(x^{-5}),\quad
 E''=-12d x^{-4}+O(x^{-6}),\qquad d=e'(0)=-b.
 \tag{8}
\]

For example (u e)″(0)=2d and (u²e)‴(0)=6d. The same calculation
for o has d replaced by −d. No big-O remainder has been differentiated.
Substitution in (7) gives for A_0 the coefficient
2(16−24)d²/4=−4d² and for A_1 the coefficient
(−32+24+24)d²/4=4d². Every remaining product is O(x^(−8)), proving
both asserted tails with controlled constants for the infinite sums.

The Fourier transform of a continuous integrable positive-definite
function must be nonnegative at every real frequency; L233 proves
this necessity directly by integrating its finite quadratic forms
over a long interval. Since b>0, the A_0 tail is strictly negative
for all sufficiently large x, which excludes positive definiteness.
An exact modular rewrite of the same integrable A_0 cannot change
this Fourier value. Thus (2)–(4), or any further exact weighted
resummation, cannot supply separate positive definiteness of both
saved blocks.

Finally k_e+k_o=K, so summing (7) gives L233's actual-theta expression.
The cancellation is stronger than just its leading coefficient:
K is smooth and even, and its polynomial-weighted derivatives are
integrable by (1) and reflection. Whole-line integration by parts
makes its Fourier transform and its first two derivatives decay
faster than every inverse power. This still provides no sign of their
Laguerre combination. The proof stops the separate-block certificate
while leaving the full first sign and all higher missing signs open. ∎

The closest recorded result is L234's finite reflected-sum obstruction.
This specialization verifies its boundary-tail method for two complete
infinite arithmetic classes, with convergent derivative envelopes and
the exact weighted coset transformation. It is a reproduction of that
method in the saved target. The inspected sources did not supply the
full parity-block conclusion; no originality is claimed. The required
threshold was nonnegative spectrum at every frequency in both blocks;
an eventually negative complete block fails it, even though all its
spatial summands are positive.

Direct differentiation in this step also corrects the previously
recorded derivative polynomial in L234 and its copied formula in L254:
the coefficient of v² is 60. Their sign conclusions and Fourier-tail
statements are unaffected, since the corrected derivative is negative
for every n≥2 and its full sum is still zero. The recurrence preceding
(1) provides an independent exact check of this correction.

**Mathlib.** Full parity-block statement and supporting Fourier-tail or
positive-definiteness results: **not checked**. The saved L016 reference
check lists the scalar Gaussian Poisson formula as a present supporting
result,
[Real.tsum_exp_neg_mul_int_sq](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/SpecialFunctions/Gaussian/PoissonSummation.html#Real.tsum_exp_neg_mul_int_sq),
and smooth-series differentiation,
[hasDerivAt_tsum_of_isPreconnected](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Calculus/SmoothSeries.html#hasDerivAt_tsum_of_isPreconnected).
Those are supporting inputs, not a match for the complete block signs;
their current library versions were not rechecked in this step. No
Mathlib absence or full matching theorem is asserted.
