# L550 — Joint reflected profile and common Bochner density

## Hypotheses

Use V, Vsharp, mathfrak M_(A,B) and m_A from L549, with its full
two-endpoint smooth test class and kernel normalization. Fix an integer
d>=1, a compact logarithmic support Omega in R^d, and real exponents
a=(a_1,...,a_d). Let W_log(u)=W(exp(u_1),...,exp(u_d)) be smooth and
supported in Omega. Define the homogeneous single-profile seminorm

\[
 p_j(W)=\sum_{|\alpha|\le j}\|\partial^\alpha W_{\log}\|_\infty,
 \qquad h(y)=\prod_{i=1}^d y_i^{a_i},\qquad
 F_Y(y)=W(y)V^\sharp(Yh(y)),\quad Y>0.                 \tag{1}
\]

For any such profile G, use the Fourier convention

\[
 \widehat G(t)=\int_{\mathbb R^d}G_{\log}(u)e^{-it\cdot u}\,du,
 \qquad \|G\|_{J,\mathrm{sep}}
   =\int_{\mathbb R^d}(1+|t|)^J|\widehat G(t)|\,dt.       \tag{2}
\]

For the finite-row application, fix finite sets I and C, complex
coefficients c_(r,k), and positive coordinate vectors y_(r,k), for
r in I and k in C. Coefficients and evaluation vectors may depend on
the arithmetic block but are independent of t. The SAME W and Y
must be used for every pair in this block. Put

\[
 U_r=\sum_{k\in C}c_{r,k}F_Y(y_{r,k}),\qquad
 B_r(t)=\sum_{k\in C}c_{r,k}
                 \exp\bigl(it\cdot\log y_{r,k}\bigr).       \tag{3}
\]

All zero masks and hard restrictions can remain in c_(r,k) or in the
finite domains. No differentiability of those coefficients is assumed.
For a uniform norm bound assume, in addition, that for some real H>=0,

\[
 \|B(t)\|_{\ell^2(I)}\le Q(1+|t|)^H                  \tag{4}
\]

with Q independent of t. Uniformity in block labels requires the
corresponding uniform Q; it is not a consequence of finiteness alone.

## Conclusion

For A>=0 and integers j,J>=0,

\[
 p_j(F_Y)\le C\,m_A(Y)p_j(W)
                \mathfrak M_{A,\lceil4A\rceil+j+2}(V),       \tag{5}
\]

\[
 \|F_Y\|_{J,\mathrm{sep}}\le C\,m_A(Y)p_{J+d+2}(W)
                \mathfrak M_{A,\lceil4A\rceil+J+d+4}(V).     \tag{6}
\]

Constants depend only on the displayed fixed orders, d, Omega and a.
Dependence on W and V is explicit; constants are independent of Y and
the arithmetic labels. In particular A=0 is permitted. Supports,
dimension and orders are fixed, not arbitrary moving parameters.

With Ftilde=F_Y/m_A(Y), the following is an absolutely integrable
Bochner identity in the original finite-dimensional row Hilbert space:

\[
 U=\frac{m_A(Y)}{(2\pi)^d}
           \int_{\mathbb R^d}\widehat{\widetilde F}(t)B(t)\,dt,
 \qquad
 \|U\|_2\le\frac{m_A(Y)}{(2\pi)^d}
       \int_{\mathbb R^d}|\widehat{\widetilde F}(t)|
                                     \|B(t)\|_2\,dt.        \tag{7}
\]

If (4) holds and J>=H is an integer, then

\[
 \|U\|_2\le C Q m_A(Y)p_{J+d+2}(W)
                    \mathfrak M_{A,\lceil4A\rceil+J+d+4}(V).
                                                               \tag{8}
\]

An extension Bplus of the same separated formula to a larger finite
row set Iplus containing I may replace B inside the positive norm on
the right of (7). No identity for U or kernel comparison on the added
rows is asserted. Squaring (8) contributes m_A(Y)^2 once. An already
expanded quadratic expression with one kernel is a different object.

These statements verify the analytic common-profile primitive used
in L541; its concrete coefficient/domain specialization is written
there. They give no arithmetic norm estimate, infinite block summation,
marked identity, global closure or Xi sign by themselves.

## Proof

### Sources and scope of the reproduction

OpenAI, *The Quasi-Riemann Hypothesis*, 30 September 2026,
[build/paper.tex at commit 1581d4cbdd69a0faf34b2089614fe2a814316a6a](https://raw.githubusercontent.com/openai/math/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex),
`lem:reflection-common-profile`, `eq:reflection-common-measure` and
`eq:reflection-common-minkowski`, lines 2386–2459, already states the
joint estimate and norm consequence. The application is
`eq:reflection-actual-annuli`, lines 7377–7420 and 7444–7454.
The saved SPECIALIZE assessment covers this exact audit. Reproduction
is needed to discharge the retained primitive and verify its application
hypotheses; no stronger estimate or mathematical novelty is claimed.

Import only the standard finite-dimensional smooth Fourier calculus
in that manuscript's `lem:smooth-calculus`, definitions 1019–1038,
statement 1039–1055 and proof 1123–1140: for a compactly supported
logarithmic profile G,

\[
 \|G\|_{J,\mathrm{sep}}\le C_{J,d,\Omega}p_{J+d+2}(G),
 \qquad
 G(y)=(2\pi)^{-d}\int\widehat G(t)\prod_i y_i^{it_i}\,dt.
                                                               \tag{9}
\]

Its finite order follows from (1-Delta)^m with
J+d<2m<=J+d+2; compact support removes boundary terms and
the weighted integral of (1+|t|^2)^(-m) is finite. This is the
ordinary Fourier inversion theorem for smooth compact support. The
source's final joint bound or its assertion of commonness is not used
as a premise. The Bochner norm inequality is used only after checking
integrability below.

### Derivative and Fourier estimates

If W=0 every claim is immediate. Otherwise compactness gives constants
0<c<=C_1<infinity with c<=exp(a dot u)<=C_1 for u in Omega.
For such h and every Y>0,

\[
 m_A(Yh)\le C_2m_A(Y),\qquad
 C_2=\max\{C_1^{1/4},\min(1,c)^{-A}\}.              \tag{10}
\]

Indeed (Yh)^(1/4)<=C_1^(1/4)Y^(1/4), while
1+Yh>=min(1,c)(1+Y). Bound each of the two entries of the
minimum by the corresponding entry times C_2, then take the minimum.
This argument also holds when A=0.

Write D=x d/dx. For every multi-index beta,

\[
 \partial_u^\beta\bigl[V^\sharp(Y\exp(a\cdot u))\bigr]
    =a^\beta(D^{|\beta|}V^\sharp)(Y\exp(a\cdot u)).    \tag{11}
\]

This follows by repeated chain rule, with exponent zero interpreted
as 1; no division by a_i is required when an exponent vanishes.
Leibniz gives, for |alpha|<=j, a finite sum of
(partial^(alpha-beta) W_log) a^beta D^|beta| Vsharp.
Every derivative of W_log is supported in Omega. Apply L549 (2),
then (10), to each term and use monotonicity of mathfrak M_(A,B)
in its integer order B. The maximum derivative order of Vsharp is j.
Summing gives (5), with the homogeneous p_j(W), including its order
zero term and without adding a constant 1. Apply (9) at order J to
F_Y and then (5) with j=J+d+2. The Mellin order is exactly
ceil(4A)+J+d+4, proving (6).

Because m_A(Y)>0, division by it is legitimate at every finite Y>0.
Equation (6) bounds every fixed weighted Fourier norm of Ftilde,
uniformly in Y with the displayed test norms. At A=0 the scalar is
min(Y^(1/4),1) directly, with no limiting argument in A.

### Commonness and the finite-row Bochner integral

The density Fhat is the Fourier transform of the ONE function in (1).
Changing r or k changes only its evaluation vector y_(r,k), not that
function. Equation (9) can therefore be inserted into every summand
of (3) using the same Fourier density and the same Lebesgue measure.

For each r define L_r=sum_(k in C)|c_(r,k)|. Since coordinates are
positive, each exponential in (3) has modulus one. Thus

\[
 \|B(t)\|_2\le\left(\sum_{r\in I}L_r^2\right)^{1/2}<\infty
                                                               \tag{12}
\]

for every t, with this finite bound allowed to depend on the block.
Each component of B is a finite sum of continuous exponentials.
The density is continuous, since F_log is integrable and dominated
convergence applies to its defining Fourier integral. Their product
is a continuous map into C^I and hence strongly measurable. Equations
(6) at J=0 and (12) give
integral |Fhat(t)| ||B(t)||_2 dt<infinity. This proves absolute
Bochner integrability BEFORE using any desired uniform arithmetic
estimate. Componentwise Fourier inversion, finite summation and the
continuous coordinate projections identify the integral with U.
The Bochner triangle inequality now proves (7).

If (4) is available, its polynomial growth is dominated by the Jth
Fourier moment for any integer J>=H. Substitution in (7), followed
by (6), proves (8). This step, rather than the crude finite bound
(12), provides uniformity. Restriction from C^Iplus to C^I is a
contraction, so ||B(t)||_(ell2(I))<=||Bplus(t)||_(ell2(Iplus))
pointwise when the formulas agree on I. This proves the stated order
of enlargement. No F_Y value on Iplus minus I enters the identity.

Empty sets give the zero vector. The same argument permits bounded
norm ranges and unit coordinates: log(1)=0 and all phases remain
continuous. It does not justify exchanging an infinite collection of
blocks with inversion; that requires separate summability. Similarly,
row-dependent cutoffs or Y cannot simply be put outside the profile.

For an external pure twist V_(u0)(x)=x^(iu0)V(x), L549 (5) displays
the extra cost (1+|u0|)^B at B=ceil(4A)+J+d+4 in (6)–(8).
If a separated estimate has additional height degree H, choose J>=H
first. There is no uniformity in unbounded derivative order or in
moving cutoffs without bounds for the displayed seminorms.

## Mathlib

Full matching coverage of this joint estimate and its arithmetic
application has not been checked. The prior source assessment inspected
[MeasureTheory.norm_integral_le_integral_norm](https://leanprover-community.github.io/mathlib4_docs/Mathlib/MeasureTheory/Integral/Bochner/Basic.html#MeasureTheory.norm_integral_le_integral_norm)
in Bochner.Basic. This supports the generic norm inequality, with a
complex Hilbert space viewed as a real normed space. It does not
establish the common-density identity, measurability or integrability;
those obligations were verified above. No formalization is claimed.
