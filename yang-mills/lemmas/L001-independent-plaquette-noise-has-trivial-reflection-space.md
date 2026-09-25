# L001 — Independent plaquette noise has a trivial reflection space

## Hypotheses

Use product normalized Haar measure on positively oriented SU(2) links of the infinite lattice Z^4, corresponding to Wilson coefficient beta = 0. Let e_1,...,e_4 be the coordinate vectors and set

\[
V_x=U_{x,1}U_{x+e_1,2}U_{x+e_2,1}^{-1}U_{x,2}^{-1},
\qquad W_x=\operatorname{Tr}V_x.
\]

Only plaquettes in this fixed (1,2) orientation are used. They are gauge-invariant observables. For real f in C_c^infinity(R^4), define

\[
X_a(f)=a^2\sum_{x\in\mathbb Z^4}f(ax)W_x,
\qquad a\downarrow0.
\]

Each sum is finite. Let theta reflect the fourth coordinate, and use the positive-time polynomial reflection form defined in the foundations.

## Conclusion

The W_x are independent and identically distributed, with mean zero, variance one, symmetric law, and absolute value at most two. For every finite family of test functions, the joint laws and all joint moments of X_a converge to those of centered Gaussian white noise Phi with

\[
\mathbb E[\Phi(f)\Phi(g)]=\int_{\mathbb R^4}f(z)g(z)\,dz.
\]

For its whole positive-time polynomial algebra,

\[
\langle F,G\rangle_{\rm OS}
=\overline{\mathbb EF}\,\mathbb EG.
\]

Consequently the reflection quotient and its completion are one-dimensional, and every centered polynomial observable represents zero. Positive-time translations induce the identity, so their Hamiltonian is zero and has no excited spectrum. The gap supremum is infinite, not a finite positive mass.

This is a negative test of the specified beta = 0 plaquette-field construction. It does not prove triviality of every possible lattice observable sector, does not address beta depending on a, and is not a disproof of Yang–Mills existence. Convergence asserted here is of finite families of smeared observables and all their moments; no topology on an entire space of distributions is needed or asserted.

## Proof

### 1. Exact independence by removing an exposed edge

Take a finite nonempty set S of distinct plaquette basepoints and select x in S with maximal first coordinate. The edge (x+e_1,2) occurs in V_x. Among all fixed-orientation plaquettes, it occurs only in V_x and V_(x+e_1). The latter is absent from S by maximality.

Condition on every link other than this edge. For any bounded measurable function h, two-sided Haar invariance gives

\[
\mathbb E\big[h(\operatorname{Tr}(A U_{x+e_1,2}B))
\mid\text{other links}\big]
=\int_{SU(2)}h(\operatorname{Tr}U)\,dU,
\]

where A and B are the fixed products of the other three links. This constant does not depend on the conditioned links. The other W_y, y in S without x, do not involve the integrated edge. Hence in the expectation of a product of bounded functions of the W_y, the factor at x integrates to its Haar-trace mean. Remove x and repeat. Induction factors every such finite joint expectation, proving independence and the common Haar-trace law.

The argument uses the infinite lattice and one orientation. It makes no independence claim for all orientations or for a periodic lattice with wrapping plaquettes.

### 2. The single-plaquette law

Identify SU(2) with unit quaternions q = (q_0,q_1,q_2,q_3) on S^3. Uniform spherical measure is normalized Haar measure because multiplication by a unit quaternion is an orthogonal transformation. In the fundamental representation Tr(q) = 2q_0. Antipodal invariance gives a symmetric trace law and mean zero. Coordinate symmetry and sum_j q_j^2 = 1 give E q_0^2 = 1/4. Thus E W_x^2 = 1, and |W_x| <= 2.

Independence now yields the exact covariance

\[
\mathbb E[X_a(f)X_a(g)]
=a^4\sum_x f(ax)g(ax)
\longrightarrow\int fg.
\]

In particular this is a nonzero probabilistic limit for nonzero f. For disjoint supports the covariance is identically zero, already before the limit.

### 3. Convergence of laws and of all polynomial moments

Write chi(s) = E exp(i s W_0). Symmetry, variance one, and bounded fourth moment imply, for real s near zero,

\[
\chi(s)=1-\tfrac12s^2+O(s^4),\qquad
\log\chi(s)=-\tfrac12s^2+O(s^4).
\]

The real logarithm exists near zero since chi(0) = 1. These remainders follow from Taylor's formula for cosine and then for log(1+u). For fixed f and t, all arguments t a^2 f(ax) are uniformly near zero when a is small. The number of nonzero summands is O_f(a^-4); therefore independence gives

\[
\begin{aligned}
\log\mathbb E e^{itX_a(f)}
&=-\frac{t^2}{2}a^4\sum_x f(ax)^2
  +O_f\!\left(t^4a^8\sum_x|f(ax)|^4\right)\\
&\longrightarrow-\frac{t^2}{2}\int f^2,
\end{aligned}
\]

because the remainder is O_(f,t)(a^4). For a finite family f_1,...,f_k, apply the same argument to sum_j t_j f_j. The joint characteristic functions converge to exp[-(1/2) integral (sum_j t_j f_j)^2], continuous at the origin. The Lévy continuity theorem gives the claimed Gaussian joint-law convergence.

For completeness, convergence in law alone would not suffice for arbitrary polynomial moments. Here moment convergence is separate and exact. If kappa_r(W_0) denotes the r-th cumulant, independence and multilinearity give

\[
\kappa\big(X_a(f_1),\ldots,X_a(f_r)\big)
=\kappa_r(W_0)a^{2r}\sum_x\prod_{j=1}^r f_j(ax).
\]

All cumulants exist because W_0 is bounded. The first is zero, the second converges to integral f_1 f_2, and for fixed r >= 3 the displayed expression is O(a^(2r-4)), hence tends to zero. The constant depends on r and the fixed test functions; no uniformity in r is claimed.

To justify the identity, cumulants are the derivatives at zero of the logarithm of the joint moment generating function. Independence makes that logarithm a sum over x, and differentiation produces the displayed weights. Expanding the exponential back gives the moment–cumulant formula

\[
\mathbb E\prod_{j=1}^r Y_j
=\sum_{\pi}\prod_{B\in\pi}\kappa(Y_j:j\in B),
\]

where pi ranges over the finitely many partitions of {1,...,r}. The limiting terms are exactly pair partitions. Thus all mixed moments converge to the Gaussian moments, including the reflection forms of any fixed polynomials in smeared fields.

The limiting Gaussian family can also be constructed directly: choose a real orthonormal basis (h_n) of L^2(R^4), independent standard Gaussians (xi_n), and set Phi(f) = sum_n xi_n <f,h_n>, with convergence in mean square. This gives precisely the stated joint laws and covariance. The covariance is Euclidean invariant.

### 4. The entire positive-time reflection quotient collapses

If f and g are supported strictly in z_4 > 0, then theta f is supported strictly in z_4 < 0. Hence integral (theta f)g = 0. Any finite Gaussian vectors formed from the positive and negative half-spaces have zero cross-covariance, so their joint Gaussian characteristic function factors. They are independent.

Take arbitrary positive-time polynomial observables F and G. Independence of the two Gaussian vectors implies

\[
\mathbb E[\overline{F^\theta}G]
=\overline{\mathbb E F^\theta}\,\mathbb E G.
\]

Reflection invariance of the Gaussian covariance gives E F^theta = E F. This proves the asserted form for all polynomials, including complex coefficients. Its null space is exactly those F with E F = 0. Sending the class of F to E F is an isometry onto C because constants are included. The completed quotient is therefore C with vacuum 1.

Positive-time translations preserve expectations by translation invariance of white noise. On the quotient they act as the identity, giving H = 0 and spectrum {0}. Thus every interval (0,Delta) is empty of spectrum, for every Delta > 0: there is no finite positive excited mass.

This computation is stronger than checking only linear fields: every centered polynomial class vanishes. Conversely it is confined to the algebra of this limiting field. A claim about an enlarged collection of gauge observables would need a separate argument.

### 5. Comparison with the required threshold

For a nonzero f, the achieved Euclidean variance is integral f^2 > 0. For f supported at positive times, the achieved centered reflection norm is zero. A physical nontriviality test in this sector would instead require some centered F with <F,F>_OS > 0. No such F exists here, and the finite-mass condition also fails. Neither renaming the probabilistic noise as a quantum field nor an empty excited spectrum closes this gap.

The factor a^2 is a^4 times the field normalization a^-2. More generally, multiplying X_a by a deterministic factor tending to a finite constant gives another constant multiple of this noise, with the same reflection-space conclusion. No claim about arbitrary divergent normalizations is needed for this negative result.

## Mathlib

Coverage of the full statement: **not checked**. Coverage of supporting Haar, Gaussian, characteristic-function, and quotient-space facts: **not checked**. No theorem names or library links are asserted without inspection. The informal proof above supplies the specialized mathematical argument; the named Lévy continuity theorem is its standard probability input.
