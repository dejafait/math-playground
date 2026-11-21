# C034x: coherent balanced factors obstruct the fixed-state block upper

## Hypotheses

Use precisely C034r's full theta kernel \(\Phi\), its input
\[
 g(y)=e^{-1/(1-y^2)}1_{|y|<1},\qquad h=-g''+g/4,\qquad
 \psi=C_\Phi h.
\]
Let \(E=L^2(\mathbb R,e^{-y/2}dy)\), \(Jf=e^{-y/4}f\), and
\(T_rf(y)=f(y+r)\). Fourier transforms have phase \(e^{-iuy}\)
and Plancherel factor \(1/(2\pi)\). The projection \(\Pi_H\)
is defined by \(\widehat{J\Pi_Hf}=1_{[-H,H]}\widehat{Jf}\).
For real \(X\ge2\), put
\[
 I_X=\{m\in\mathbb N:3\sqrt X/4<m\le5\sqrt X/6\},
\]
\[
 V_X(\alpha,\beta)=
 \sum_{\substack{m,n\in I_X\\X/2<mn\le X}}
 \alpha_m\beta_n\log(X/(mn))(mn)^{-1/2}
                  T_{\log(mn/X)}\psi.
\]
The sum is over ordered pairs, including all multiplicities of repeated
products. The factor coefficients may be complex with
\(|\alpha_m|,|\beta_n|\le1\). There is no selected zero or RH premise.

## Conclusion

There is a constant \(c_h>0\), independent of real \(X\), such that
\[
 \|\Pi_{4\log X}V_X(1,1)\|_E^2\ge c_hX
                   \qquad(X\ge576).                              \tag{1}
\]
Here \(V_X(1,1)\) uses both factor sequences identically one. Hence for
each fixed \(0<\varepsilon<1/2\) there is no finite constant
\(C_{h,\varepsilon}\) giving
\[
 \|\Pi_{4\log X}V_X(\alpha,\beta)\|_E^2
 \le C_{h,\varepsilon}X^{1/2+\varepsilon}                         \tag{2}
\]
uniformly in these coefficients for all sufficiently large real \(X\).
This refutes only this arbitrary-factor intermediate inequality. It
neither refutes nor proves an upper for C034r's signed Möbius source,
its cumulative energy, the whole completion, or actual-Xi mixed signs.
The positive constant is existential, not a numerical certificate.

## Proof

This is the finite obstruction test authorized by assessment2101 and
its separate approval2102. The existing comparison with Green and Tao,
*Quadratic uniformity of the Möbius function*, arXiv:math/0606087v2,
22 September 2007, Lemma4.1 and Proposition4.2,
[Section4](https://arxiv.org/html/math/0606087v2#S4), is reused.
Those theorems concern Type I/II alternatives and are not applied to
\(V_X\); they supply neither (1) nor (2). The short proof is needed
to check the actual weighted state and frequency average. It makes
no claim of originality beyond the sources checked. Plancherel's
theorem is the only standard analytic theorem invoked in addition
to the already established C034r operator and multiplier identities.

### The rectangle and the exact finite transform

Every pair in \(I_X^2\) satisfies
\[
 9X/16<mn\le25X/36.
\]
Since \(9/16>1/2\) and \(25/36<1\), the hyperbolic cutoff in
\(V_X\) deletes no pair, for every real \(X\). Its cardinality is
\[
 N_X=\lfloor5\sqrt X/6\rfloor-\lfloor3\sqrt X/4\rfloor
       \ge\sqrt X/12-1\ge\sqrt X/24\quad(X\ge576).              \tag{3}
\]
This uses precisely the strict lower and inclusive upper endpoints;
the floor formula also holds when either endpoint is an integer.

C034r section2 gives \(JT_r=e^{r/4}T_rJ\) and
\[
 \widehat{J\psi}(u)=W(u),\qquad
 W(u)=\Xi(u-i/4)\widehat{Jh}(u).
\]
Translation with the stated Fourier phase therefore gives the exact
finite identity
\[
 \widehat{JV_X(1,1)}(u)=W(u)S_X(u),
\]
\[
 S_X(u)=\sum_{(m,n)\in I_X^2}a_{m,n,X}e^{iu\log(mn/X)},\qquad
 a_{m,n,X}=\log(X/(mn))(mn)^{-1/2}(mn/X)^{1/4}.                   \tag{4}
\]
This agrees with C034w(7)'s normalization; its tail theorem and its
completion hypotheses are not used. In particular the factor
\((mn/X)^{1/4}\) is retained. Every \(a_{m,n,X}\) is positive.
Define \(d=\log(36/25)(9/16)^{1/4}>0\). The product bounds give
\[
 a_{m,n,X}\ge dX^{-1/2},\qquad
 |\log(mn/X)|\le\log(16/9).                                    \tag{5}
\]
For the first inequality, use separately
\(\log(X/(mn))\ge\log(36/25)\), \((mn)^{-1/2}\ge X^{-1/2}\),
and \((mn/X)^{1/4}\ge(9/16)^{1/4}\). No repeated product was
identified with a single term in (4).

### A positive-measure interval and its integrated lower bound

C034r section5 establishes continuity of \(W\) and the strict value
\[
 W(0)=\frac3{16}\Xi(-i/4)\int_{\mathbb R}g(y)e^{-y/4}dy>0.
\]
Its positivity uses the actual positive theta kernel and this fixed
input; it assumes no nonvanishing statement for zeta in a half-plane.
Thus choose \(b=W(0)/2>0\) and \(\eta_0>0\) such that
\(|W(u)|\ge b\) whenever \(|u|\le\eta_0\). Fix
\[
 \eta=\min\{\eta_0,1,\pi/(3\log(16/9))\}>0.
\]
For every \(|u|\le\eta\), (5) gives
\(|u\log(mn/X)|\le\pi/3\), hence every cosine in (4) is at
least \(1/2\). Consequently (3)-(5) imply
\[
 |S_X(u)|\ge\Re S_X(u)
 \ge\tfrac12N_X^2dX^{-1/2}
 \ge\frac d{1152}\sqrt X\qquad(X\ge576,\ |u|\le\eta).          \tag{6}
\]
This bounds the modulus of the full sum; it does not replace its
square by its diagonal or omit any cross terms.

For \(X\ge576\), \(4\log X\ge1\ge\eta\). Plancherel and (4)
therefore give
\[
 \begin{split}
 \|\Pi_{4\log X}V_X(1,1)\|_E^2
 &=\frac1{2\pi}\int_{-4\log X}^{4\log X}|W(u)S_X(u)|^2du\\
 &\ge\frac1{2\pi}\int_{-\eta}^{\eta}
               b^2\frac{d^2}{1152^2}X\,du
 =\frac{\eta b^2d^2}{\pi\,1152^2}X.
 \end{split}
\]
This proves (1) with the displayed positive coefficient as \(c_h\).
All sums are finite and the vector belongs to \(E\), by C034r's
bounded convolution and translation operators, so no infinite
arithmetic interchange or limiting Plancherel operation is involved.

If (2) held for any fixed \(0<\varepsilon<1/2\), its application
to these admissible coefficients would imply
\(c_hX^{1/2-\varepsilon}\le C_{h,\varepsilon}\) for all sufficiently
large real \(X\), a contradiction. Nothing is asserted against (2)
for \(\varepsilon\ge1/2\). These coefficients are not \(\mu(mn)\),
and positive mass from this diagnostic cannot be transferred to a
signed decomposition without controlling its full recombination.

### Mathematical audit2105 (2026-11-21)

The complete proof above was replayed under the unchanged approved
assessment2103/approval2104. The relevant C034r hypotheses and
sections1,2,5 were inspected, as was C034w(7). No additional
number-theoretic theorem is applied. This is verification of the local
obstruction, not a new arithmetic estimate or an independent reproof
of the external comparison sources.

**Weighted transform and actual input.** Directly changing variables
in the weighted norm gives
\(\|T_rv\|_E^2=e^{r/2}\|v\|_E^2\), and
\(JT_rv=e^{r/4}T_rJv\). With the stipulated Fourier phase,
\(\widehat{T_rJv}(u)=e^{iur}\widehat{Jv}(u)\). Moreover
\(JC_\Phi J^{-1}\) is convolution by \(e^{-y/4}\Phi(y)\);
its transform is \(\Xi(u-i/4)\), since
\(-i(u-i/4)y=-iuy-y/4\). These facts verify every multiplier
and sign in (4), particularly \((mn/X)^{1/4}\), rather than an
unweighted surrogate. C034r's exponential-moment bounds and compact
smooth input ensure both this convolution and all finite translated
vectors belong to the required spaces. The multiplier \(W\) is
continuous on the real line.

For the value at zero, integrate twice by parts, using the vanishing
of every derivative of \(g\) at its support endpoints:
\[
 \int e^{-y/4}g''(y)\,dy=\frac1{16}\int e^{-y/4}g(y)\,dy,
 \qquad
 \widehat{Jh}(0)=\frac3{16}\int e^{-y/4}g(y)\,dy>0.
\]
Every summand of the actual \(\Phi(y)\) is positive: its remaining
factor is
\(2\pi n^2e^{5|y|/2}(2\pi n^2e^{2|y|}-3)>0\).
Thus \(\Xi(-i/4)=\int e^{-y/4}\Phi(y)\,dy>0\).
This checks \(W(0)>0\) without importing any of C034r's
conditional selected-zero conclusions. Continuity then provides
\(\eta_0\) for the specified \(b=W(0)/2\).

**Every real endpoint and the full square.** Write \(t=\sqrt X\).
Counting integers in \((3t/4,5t/6]\) gives precisely the difference
of floors in (3), even at integer endpoints. Since
\(\lfloor b\rfloor\ge b-1\) and \(\lfloor a\rfloor\le a\),
\(N_X\ge t/12-1\ge t/24\) for every real \(t\ge24\).
Every ordered pair then satisfies the displayed strict lower product
bound and inclusive upper bound. The cutoff therefore removes no
term. There are \(N_X^2\) terms, including repeated products and
the pairs with equal indices. All three factors in the lower bound
for \(a_{m,n,X}\) are positive, so multiplying their separate
bounds in (5) is valid.

On the closed interval \([-\eta,\eta]\), every phase in (4) has
absolute value at most \(\pi/3\). Positivity of the amplitudes
therefore gives
\[
 \Re S_X(u)\ge\frac12N_X^2dX^{-1/2}
 \ge\frac{d}{2\cdot24^2}\sqrt X
 =\frac{d}{1152}\sqrt X>0.
\]
Taking \(|S_X|\ge\Re S_X\) controls the complete sum before
squaring; no sign of an individual cross term is assumed. Since
\(4\log X\ge1\ge\eta\) for \(X\ge576\), the projection
contains this entire interval. Its length is \(2\eta\), so
Plancherel's factor \(1/(2\pi)\) gives exactly
\(c_h=\eta b^2d^2/(\pi1152^2)>0\), independent of real \(X\).
There is no unproved passage from a point value to positive integrated
mass, or from an integer subsequence to all real \(X\).

**Quantifiers and disposition.** The all-one factors are admissible
for each \(X\), and \(X^{1/2-\varepsilon}\) is unbounded exactly
in the asserted range \(0<\varepsilon<1/2\). Thus (1) and its
stated obstruction to (2) pass this audit without repair. At
\(\varepsilon=1/2\) this contradiction disappears. The result
remains confined to the arbitrary-factor uniform inequality; it
asserts no estimate or obstruction for the actual signed Möbius
source, cumulative energy, full completion or mixed positivity.
C034r is the sole direct local mathematical input. C034w is only a
normalization comparison, and Green--Tao only a literature comparison;
neither adds a dependency. Full matching Mathlib coverage remains
unchecked, and no formal verification is claimed.

## Mathlib

A full matching theorem has not been checked; availability is unknown.
Supporting finite sums, floor bounds, Fourier translation and
Plancherel results have not been matched to exact theorem names in
this weighted normalization. No formal verification or absence claim
is made. Reference: [Mathlib documentation](https://leanprover-community.github.io/mathlib4_docs/).
