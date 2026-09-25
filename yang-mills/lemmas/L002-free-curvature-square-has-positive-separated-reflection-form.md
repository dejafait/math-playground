# L002 — Free curvature square has a positive separated reflection form

## Hypotheses

Write a Euclidean point as z = (x,t), with x in R^3 and t = x_4, and let theta(x,t) = (x,-t). Fourier inversion uses measure d^n p/(2 pi)^n. Take independent real centered Gaussian generalized fields A_mu^a, with a = 1,2,3 and mu = 1,2,3,4, whose covariance is

\[
\mathbb E[A_\mu^a(\phi)A_\nu^b(\psi)]
=\delta_{ab}\delta_{\mu\nu}
\int_{\mathbb R^4}\frac{\overline{\widehat\phi(p)}\widehat\psi(p)}{|p|^2}
\frac{d^4p}{(2\pi)^4}
\]

for real Schwartz tests. This is a specified free Gaussian model, with no infrared regulator. The covariance is finite on Schwartz tests, positive, and real on real tests; an isonormal Gaussian process on the completion in this covariance norm constructs these smeared fields.

Set B^a = partial_1 A_2^a - partial_2 A_1^a. With Hermitian SU(2) generators T^a satisfying Tr(T^a T^b) = delta_(a,b)/2, the free part of Tr(F_12^2) in this canonical field normalization is (1/2) sum_a (B^a)^2. Adding gradients to A leaves B unchanged, and orthogonal adjoint color rotations preserve this sum. No identification with an interacting renormalized operator is assumed.

Choose the fixed radial mollifier

\[
\eta(z)=c_\eta
\begin{cases}
\exp[-1/(1-|z|^2)],&|z|<1,\\
0,&|z|\ge1,
\end{cases}
\qquad \int\eta=1,
\qquad \eta_\varepsilon(z)=\varepsilon^{-4}\eta(z/\varepsilon).
\]

Let B_epsilon^a = eta_epsilon * B^a, v_epsilon = E[(B_epsilon^a(z))^2], and, for a complex smooth compactly supported test f,

\[
O_\varepsilon(f)=\frac12\sum_{a=1}^3
\int f(z)\bigl((B_\varepsilon^a(z))^2-v_\varepsilon\bigr)\,dz.
\]

These integrals exist in the ordinary Gaussian L^2 space at each positive epsilon and have mean zero. For f supported in t > 0, define the separated reflection form

\[
Q_\varepsilon(f)=
\mathbb E\bigl[\overline{O_\varepsilon(\theta f)}\,O_\varepsilon(f)\bigr],
\qquad (\theta f)(z)=f(\theta z).
\]

The magnetic component B is even under time reflection. The radial mollifier respects this convention. We only take epsilon small enough that the smeared positive-time insertion remains away from t = 0.

## Conclusion

For every such positive-time test, the limit q_0(f) = lim_(epsilon down to 0) Q_epsilon(f) exists, is finite, and equals

\[
q_0(f)=\frac32\int\!\int
\overline{f(z)}f(w)\,C(\theta z-w)^2\,dz\,dw\ge0,
\]

where the integrals have z,w in the support of f and the off-diagonal curvature covariance is

\[
C(x,t)=
\frac{t^2+x_3^2-x_1^2-x_2^2}
{\pi^2(t^2+|x|^2)^3},\qquad (x,t)\ne0.
\]

Here is one explicit test with a quantitative positive bound. Define

\[
b(s)=\begin{cases}\exp[-1/(1-s^2)],&|s|<1,\\0,&|s|\ge1,\end{cases}
\quad I=\int_{-1}^1b(s)\,ds,
\quad
f_*(x,t)=\frac{128}{I^4}b(2t-3)\prod_{j=1}^3b(4x_j).
\]

Then f_* is nonnegative, has integral one, and is supported in [1,2] times [-1/4,1/4]^3. With

\[
c_*:=\frac{224}{\pi^2 67^3},
\qquad
q_0(f_*)\ge\frac32 c_*^2>0.
\]

For all sufficiently small epsilon, Q_epsilon(f_*) >= q_0(f_*)/2 >= 3 c_*^2/4. This is a cutoff-independent lower bound in the specified free model only.

Wick subtraction has a precise limitation here. For every nonzero real smooth compactly supported f, with no support restriction needed,

\[
\varepsilon^4\mathbb E[O_\varepsilon(f)^2]
\longrightarrow
\frac32\|C_1\|_{L^2(\mathbb R^4)}^2\|f\|_{L^2(\mathbb R^4)}^2>0,
\]

where C_1 is the covariance of B_1^a. Thus these composites do not converge in ordinary Gaussian L^2 as epsilon goes to zero. The separated reflection limit does not assert a limit of all Euclidean moments, a full composite-field construction, interacting reflection positivity, or a positive mass gap.

## Proof

### 1. The free curvature covariance and its regularization

The scalar inverse Fourier transform of |p|^-2 is, away from zero,

\[
D(z)=\int_0^\infty(4\pi s)^{-2}
e^{-|z|^2/(4s)}\,ds=\frac1{4\pi^2|z|^2}.
\]

This follows by writing |p|^-2 as integral_0^infinity exp(-s|p|^2) ds, Fourier transforming the Gaussian, and substituting |z|^2/(4s) in the displayed integral. These identities also hold as tempered distributions. Near p = 0, |p|^-2 is locally integrable in four dimensions, and Schwartz decay controls large p.

Differentiating at both endpoints of a covariance introduces the opposite sign on the second derivative. Independence of A_1 and A_2 therefore gives

\[
\mathbb E[B^a(z)B^b(w)]=\delta_{ab}C(z-w),
\qquad
\widehat C(p)=\frac{p_1^2+p_2^2}{|p|^2},
\qquad
C=-(\partial_1^2+\partial_2^2)D.
\]

The notation for the first identity is distributional. Off the origin, direct differentiation yields the formula in the conclusion: if r^2 = |x|^2+t^2, then

\[
-(\partial_1^2+\partial_2^2)\frac1{4\pi^2r^2}
=\frac1{\pi^2r^4}-\frac{2(x_1^2+x_2^2)}{\pi^2r^6}.
\]

Only this off-diagonal restriction is used for the reflection limit. No choice of distributional contact term is made by treating that formula as a locally integrable function at zero.

For possibly different mollification scales, put

\[
C_{\varepsilon,\delta}(z-w)
=\mathbb E[B_\varepsilon^a(z)B_\delta^a(w)]
=(\eta_\varepsilon*\eta_\delta*C)(z-w).
\]

The absence of a reversed mollifier follows from eta being even. Its Fourier transform is the bounded multiplier (p_1^2+p_2^2)/|p|^2 times the two rapidly decreasing mollifier transforms. The covariance is smooth and bounded at each fixed pair of positive scales. In particular, v_epsilon is finite. The Gaussian fourth moments are also finite and uniformly bounded in z at each fixed scale; integration against a compactly supported f defines O_epsilon(f) in L^2, for example as a Bochner integral.

Let the support of f lie in t >= tau > 0. Every theta z - w in the reflection integral has time coordinate at most -2 tau. For epsilon + delta < tau, convolution at these arguments uses C only away from zero. On their compact set of arguments, smoothness and the approximate-identity property give

\[
C_{\varepsilon,\delta}(\theta z-w)
\longrightarrow C(\theta z-w)
\]

uniformly as epsilon, delta go to zero. In detail, all shifts have size at most epsilon + delta, remain in a fixed compact set disjoint from zero, and the supremum of the difference is bounded by the modulus of continuity of C there. The normalized nonnegative mollifiers do not increase that bound.

### 2. Wick centering and the separated limit

If X,Y are jointly centered real Gaussian variables with variances a,b and covariance c, then

\[
\mathbb E[(X^2-a)(Y^2-b)]=2c^2.
\]

Indeed their joint moment generating function is exp[(a s^2+2c s u+b u^2)/2]; its s^2 u^2 coefficient gives E[X^2 Y^2] = ab + 2c^2. Distinct colors have zero covariance and are independent. The factor 1/2 in each composite, three colors, and the factor 2 from this identity give

\[
\mathbb E\bigl[\overline{O_\varepsilon(\theta f)}O_\delta(f)\bigr]
=\frac32\int\!\int\overline{f(z)}f(w)
C_{\varepsilon,\delta}(\theta z-w)^2\,dz\,dw.
\]

To see the reflected arguments, change the integration variable of the first insertion from z to theta z. Complex conjugation affects f, while the Gaussian field is real. The subtraction of v at each scale removes all within-insertion contractions exactly.

Uniform convergence of the kernel on this compact separated set proves the asserted finite limit by domination. It also proves the mixed-scale limit in this display; no interchange of coincident composite limits is used.

### 3. Nonnegativity and a check on the reflection sign

For u > 0, spatial Fourier inversion gives

\[
C(x,u)=\int_{\mathbb R^3}
e^{ik\cdot x-|k|u}\,w(k)\,\frac{d^3k}{(2\pi)^3},
\qquad
w(k)=\frac{k_1^2+k_2^2}{2|k|}\ge0,
\]

with w(0) = 0. The one-dimensional transform identity behind this is

\[
\int_{\mathbb R}\frac{e^{ipu}}{p^2+\omega^2}\frac{dp}{2\pi}
=\frac{e^{-\omega|u|}}{2\omega}\quad(\omega>0),
\]

obtained by Fourier transforming exp(-omega |u|), whose transform is 2 omega/(omega^2+p^2). Spatial derivatives multiply by k_1^2+k_2^2. The spatial integral is absolutely convergent for u > 0.

Define the Laplace–Fourier transform

\[
\mathcal F_f(E,K)=\int_0^\infty\!\int_{\mathbb R^3}
f(x,t)e^{-Et-iK\cdot x}\,dx\,dt.
\]

Inserting two copies of the covariance formula in the reflection integral gives

\[
q_0(f)=\frac32\int_{\mathbb R^3}\!\int_{\mathbb R^3}
w(k)w(l)
\left|\mathcal F_f(|k|+|l|,k+l)\right|^2
\frac{d^3k\,d^3l}{(2\pi)^6}\ge0.
\]

All exchanges here are absolutely justified: w(k) <= |k|/2, and positive-time support gives |F_f(E,K)| <= ||f||_1 exp(-tau E). For the unsquared expanded integrals the same bound follows from integrating |f(z)f(w)| first. The resulting product of integrals of |k| exp(-2 tau |k|) is finite in three dimensions. Thus the sign is the sign of a squared modulus, not a supposed pointwise positivity of the unsquared covariance for all separations. Polarization also gives a positive semidefinite form on linear combinations of these single composite insertions; this is not a proof about their whole polynomial algebra.

### 4. An explicit positive test and lower bound

The one-dimensional changes of variables v = 2t-3 and v_j = 4x_j show that the integral of b(2t-3) product_j b(4x_j) is I^4/128. Thus the stated f_* is smooth, nonnegative, compactly supported at positive times, and has integral one.

For z = (x,t) and w = (y,s) in its support, set u = t+s and r_j = x_j-y_j. Then

\[
2\le u\le4,\qquad |r_j|\le\tfrac12,
\qquad u^2+r_3^2-r_1^2-r_2^2\ge\tfrac72,
\qquad u^2+|r|^2\le\tfrac{67}{4}.
\]

Since C is even in its time argument,

\[
C(\theta z-w)\ge
\frac{7/2}{\pi^2(67/4)^3}
=\frac{224}{\pi^2 67^3}=c_*.
\]

Integration against f_*(z)f_*(w), of total integral one, gives q_0(f_*) >= 3 c_*^2/2. Its positive limit and convergence of Q_epsilon give Q_epsilon >= q_0/2 for all sufficiently small epsilon. No lower bound on an interacting remainder enters this conclusion.

### 5. Why the ordinary composite limit has not been constructed

Write C_epsilon = C_(epsilon,epsilon). Its Fourier multiplier is

\[
\frac{p_1^2+p_2^2}{|p|^2}|\widehat\eta(\varepsilon p)|^2.
\]

The first factor is homogeneous of degree zero, so Fourier scaling gives the exact identity C_epsilon(h) = epsilon^-4 C_1(h/epsilon). The multiplier at epsilon = 1 is in L^2: it is bounded near zero and rapidly decreasing at infinity. Plancherel implies C_1 is in L^2. It is nonzero because eta_hat(0) = 1 and the first factor is positive on an open set arbitrarily near zero. Thus ||C_1||_2^2 is finite and strictly positive.

Applying the same Gaussian fourth-moment identity without reflection, followed by y = z-epsilon v, gives for real f

\[
\varepsilon^4\mathbb E[O_\varepsilon(f)^2]
=\frac32\int_{\mathbb R^4}C_1(v)^2
\left(\int_{\mathbb R^4}f(z)f(z-\varepsilon v)\,dz\right)dv.
\]

For fixed v the inner integral tends to ||f||_2^2, by continuity of translations in L^2. Its absolute value is at most ||f||_2^2 by Cauchy–Schwarz. The integrable dominator C_1(v)^2 ||f||_2^2 proves the stated limit by dominated convergence. For f nonzero, the variance therefore diverges as a strictly positive constant times epsilon^-4. An L^2-convergent family would have bounded L^2 norm, so such convergence is impossible with this centering alone.

This divergence does not invalidate a limit of separated reflection forms: the latter never probes the coincident singularity. It does prohibit inferring ordinary all-moment convergence of the composites from the positive separated limit. No stronger claim about possible distributional renormalizations or other modes of convergence is made.

### 6. Comparison with the required bound

The achieved threshold is a strictly positive free coefficient with fixed field normalization and no infrared cutoff. In a prospective interacting comparison with the same leading coefficient, a real remainder satisfying |R_(rho,ell)(f_*)| <= q_0(f_*)/2 uniformly in the ultraviolet cutoff would imply Q_(rho,ell)(f_*) >= q_0(f_*)/2. No such remainder estimate is proved here. If an infrared regulator changes the free covariance, its coefficient q_(0,ell) must first be computed or controlled; it cannot silently be replaced by the q_0 computed above.

This single free coefficient meets neither the interacting nontriviality requirement nor the mass-gap target. Matching composite normalization, convergence of the needed interacting moments, positivity on the entire limiting algebra, the other field axioms and gauge groups, and finite positive mass after infrared removal all remain unproved. The ordinary-variance divergence explains one reason a full composite construction cannot be replaced by the present separated calculation.

## Mathlib

Coverage of the full statement: **not checked**. Coverage of supporting Fourier, Gaussian, Wick-moment, dominated-convergence, and Plancherel results: **not checked**. No inspected Mathlib theorem or direct library link is asserted. The specialized reflection calculation and its regularization limitation are proved above; the standard isonormal Gaussian construction, Fourier inversion, Plancherel theorem, and dominated convergence theorem are the named analytic inputs.
