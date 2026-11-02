# Corollary 604a: the layer endpoint scale and its signed cancellation

## Hypotheses

Use exactly L604's hypotheses and definitions of p, h, tau, c, F,
H_s, M and R. Thus p is a strictly positive even smooth probability
density on R, every derivative decreases faster than every exponential,
and tau=h/p is nonincreasing on (0,infinity). Write

\[
D=F'^2-FF'',\quad \ell=\lim_{a\to\infty}\tau(a),\quad
q(a)=-\tau'(a),\quad V=c-\ell,\quad
J_a(x)=2\int_0^a p(u)\cos(xu)\,du.
\]

L604 gives smoothness, evenness and 0<tau<=c, so ell exists in [0,c],
q>=0, and integral_0^infinity q=V. No strict decrease, inverse tau,
global bound on tau', or zero limiting floor is assumed.

## Conclusion

Define the density-dependent constants

\[
\begin{split}
w(a)&=q(a)p(a)^2=a p(a)^2+h(a)p'(a),\\
A&=2\int_0^\infty w(a)\,da,\qquad
P=\sup_{a\ge0}p(a),\\
B&=2\left(\sup_{a\ge0}|p'(a)|+\int_0^\infty|p''(a)|\,da\right),
\qquad W=\int_0^\infty|w'(a)|\,da.
\end{split}                                                     \tag{1}
\]

These constants are finite. For every real x!=0,

\[
M(x)=\ell F(x)^2+\int_0^\infty q(a)J_a(x)^2\,da,              \tag{2}
\]
\[
\left|M(x)-\ell F(x)^2-\frac{A}{x^2}\right|
\le \frac{W+4PBV}{|x|^3}+\frac{B^2V}{|x|^4}.                 \tag{3}
\]

If tau is nonconstant, A>0, and as |x| tends to infinity,

\[
M(x)=A/x^2+O_p(|x|^{-3}),\qquad
R(x)=-A/x^2+O_p(|x|^{-3}).                                  \tag{4}
\]

In particular R is eventually strictly negative. Moreover, for every
integer N>=0,

\[
D(x)=O_{p,N}(|x|^{-N}),\qquad
\frac{M(x)+R(x)}{M(x)}=O_{p,N}(|x|^{-N})                     \tag{5}
\]

in the second assertion at sufficiently large |x| where M>0.
Thus R/M=-1+O_p(|x|^{-1}); (5) is the stronger cancellation statement.
For constant tau, A=0, ell=c, M=cF^2 and R=0, as in L604.

There is no conclusion about the sign of D, separate asymptotics of
R_+ or R_-, a density-uniform constant or onset, actual-theta
applicability, or higher signs. Algebraic endpoint terms must cancel
to every algebraic relative order in the exact identity. Controlling
only an error o(|x|^-2), or finitely many further inverse powers, does
not by itself determine the residual sign.

## Proof

**Imported analytic inputs.** Use the following standard theorems,
whose source comparison preceded this calculation:

* NIST DLMF, v1.2.8 (15 September 2026), [Section 2.3(i),
  (2.3.4)-(2.3.6)](https://dlmf.nist.gov/2.3#i): endpoint expansion of
  Fourier integrals with remainder bounded by the integral of the
  absolute relevant derivative times the corresponding inverse
  frequency power. The infinite-endpoint version requires uniform
  convergence of the derivative integrals.
* Filippo Riva and Lorenzo Nardini, *Existence and uniqueness of dynamic
  evolutions for a one-dimensional debonding model with damping*,
  [35-page author preprint](https://cvgmt.sns.it/media/doc/paper/3947/Preprint.pdf),
  Appendix A, Lemma A.1, (A.1), Remark A.2 and noninjective proof,
  printed pp.31-32 (unversioned PDF inspected 1 November 2026):
  substitution for a nondecreasing Lipschitz map and nonnegative
  measurable integrand, with Borel representatives in weighted
  compositions. The stated nonincreasing variant uses orientation
  reversal. This permits flat fibres.
* John K. Hunter, *Notes on Partial Differential Equations*,
  [2009 Appendix 5.A](https://www.math.ucdavis.edu/~hunter/m218a_09/ch5A.pdf),
  Definition 5.15, (5.11), Theorem 5.25 and the Schwartz-preservation
  statement, printed pp.132,134-137: the Fourier transform preserves
  Schwartz space, with its derivative/monomial identities. A fixed
  Fourier normalization and frequency reflection preserve that class.

The theorems are imported; the following checks assemble them for
L604's layers. This is a standard specialization, not a novelty claim.

**All levels, including a floor and flat fibres.** For ell<s<c,
monotonicity and continuity make {u:tau(u)>s} a symmetric interval
with finite radius a(s)>0. Its endpoints do not affect its integral,
so H_s(x)=J_{a(s)}(x). Levels 0<s<ell give H_s=F. The single level
s=ell and the other endpoint levels have zero ds measure.

The map s to H_s(x) is Borel: it is the integral against the jointly
Borel indicator 1_{tau(u)>s}, dominated by p(u). Fix x and take the
bounded nonnegative Borel function
g(s)=1_{ell<s<c}|H_s(x)|^2 on the real line. On each compact interval
[0,L], tau is smooth and Lipschitz. The cited substitution theorem gives

\[
\int_0^L q(a)g(\tau(a))\,da
=\int_{\tau(L)}^c g(s)\,ds.
\]

Pass to L tending to infinity by nonnegative monotone convergence.
At every a>0 with q(a)>0, tau'(a)<0. Monotonicity then implies
tau(u)>tau(a) for 0<=u<a and tau(u)<tau(a) for u>a: equality at
another point would force constancy on the intervening interval and
contradict the derivative at a. Also ell<tau(a)<c. Consequently
H_{tau(a)}=J_a at every such a. Where q=0 both weighted integrands
vanish. In particular an entire flat fibre, or an attained floor,
introduces no extra term. Thus

\[
\int_\ell^c |H_s(x)|^2\,ds=\int_0^\infty q(a)J_a(x)^2\,da.
\]

Adding the floor contribution proves (2), without differentiating an
inverse function. The constant case has V=0 and follows immediately.

**Uniform endpoint error before squaring.** Evenness gives p'(0)=0.
The finite-interval endpoint formula through the p' terms gives,
for every a>=0 and x!=0,

\[
J_a(x)=\frac{2p(a)\sin(xa)}x+\frac{E_a(x)}{x^2},\qquad
E_a(x)=2p'(a)\cos(xa)-2\int_0^a p''(u)\cos(xu)\,du.
\]

This is the cited endpoint formula with its explicit integral
remainder; no fixed-a asymptotic is used as a uniform estimate.
The density assumptions make B finite and give |E_a(x)|<=B for
all a,x. Therefore, since integral q=V,

\[
\left|\int_0^\infty q(a)J_a(x)^2\,da
-\frac4{x^2}\int_0^\infty w(a)\sin^2(xa)\,da\right|
\le\frac{4PBV}{|x|^3}+\frac{B^2V}{|x|^4}.                  \tag{6}
\]

All integrals here are absolutely finite: q is integrable, p and
p' are bounded, and the error is uniformly bounded. This also
justifies the cross and square terms in (6).

**The oscillatory weight and coefficient.** Differentiating h gives
h'=-a p on the positive half-line. Direct differentiation of tau=h/p
gives the formula for w in (1), and then

\[
w'(a)=p(a)^2+a p(a)p'(a)+h(a)p''(a).                         \tag{7}
\]

Since 0<h<=cp and every derivative of p has the stipulated decay,
these formulas show w,w' are integrable and w tends to zero at
infinity. Also w(0)=h(0)p'(0)=0. These checks avoid any unproved
growth bound on derivatives of the ratio tau. In particular W is
finite. The infinite-endpoint Fourier bound applies to w: the
derivative integral is absolutely and hence uniformly convergent
in frequency, and both endpoint values of w are zero. It gives

\[
\left|\int_0^\infty w(a)\cos(2xa)\,da\right|
\le \frac{W}{2|x|}.                                       \tag{8}
\]

Using sin^2(xa)=(1-cos(2xa))/2 in (6), and then (8), proves (3)
with the coefficient A in (1), including every factor of two.
Nonnegativity follows from w=q p^2>=0. If tau is nonconstant,
there exist 0<=r<s with tau(r)>tau(s). The fundamental theorem of
calculus gives integral_r^s q>0. Since p has a positive minimum on
[r,s], integral_r^s q p^2>0, and hence A>0. Also A<=2P^2V<infinity.

**Full determinant and signed cancellation.** The all-derivative
decay puts p and each u^j p, for j=1,2, in Schwartz space. Hunter's
theorem therefore puts F,F',F'' in Schwartz space under our
unnormalized positive-exponent convention. Differentiation of F is
also directly justified by the corresponding absolute moments.
Thus ell F^2 and D decrease faster than every inverse power.
Equation (3) now proves the M assertion in (4). The exact, audited
L604 identity D=M+R proves the R assertion in (4) and the first
bound in (5). Since A>0, for large |x|, M>=A/(2x^2), and R<0.
For a prescribed N, using D=O_{p,N}(|x|^{-N-2}) and dividing by
this lower bound proves the second bound in (5).

This comparison retains the complete signed R of L604. It neither
discards R_+ or R_- nor bounds them separately. Rapid absolute decay
of D does not sign it; L607's generic counterexample remains a
contrast, not an input. No density-family search, theta substitution,
integrated positivity assertion or higher determinant is used here.
The constant comparison M=cF^2, R=0, D=cF^2 is exactly L604's,
so it has no positive algebraic coefficient and no contradiction.

**Independent audit, 1 November 2026.** The unchanged calculation
passes the following hypothesis and constant checks. For fixed x,
|H_s(x)|<=1 and the jointly Borel level indicator make the substituted
g a bounded Borel function. Local Lipschitz regularity of tau suffices
on each [0,L]; neither global Lipschitz regularity nor an inverse is
needed. Both sides increase to the asserted half-line integrals.
Equality H_{tau(a)}=J_a is used only where q(a)>0, so a flat fibre,
an initial plateau or an attained floor cannot contribute an atom.
The floor term is ell F^2 even when ell>0. When V=0, monotonicity
forces tau=c and no nonconstant-case division is made.

The endpoint formula includes -2p'(0)/x^2=0. Its uniform remainder
gives the cross term 4PBV/|x|^3 and the squared error B^2V/|x|^4
before any limit in a. In (7), the three terms have absolute integral
bounded by integral p^2, integral a|p p'| and c integral p|p''|,
respectively; each is finite under the stated decay. Thus the use of
W is justified without controlling tau'' or sup|tau'|. The oscillatory
correction to A/x^2 is -2/x^2 times integral w cos(2xa), whose bound
is exactly W/|x|^3. The coefficient in (3) has no missing factor.

For a strict drop of tau on [r,s], positivity and continuity of p
give m=min{p(a)^2:r<=a<=s}>0 and A>=2m integral_r^s q>0.
This is the only strictness needed. Schwartz preservation applies to p and its polynomial
multiples, under a constant rescaling and frequency reflection of the
cited convention. After obtaining M>=A/(2x^2), the relative bound
of order |x|^-N uses the absolute D bound of order |x|^(-N-2).
It therefore holds at all sufficiently large positive and negative
frequencies, without dividing at finite zeros of M. L604 then gives
R=D-M and the eventual strict negative sign of R, but no sign of D.

No identity, bound or hypothesis required correction. This is an
independent verification of the existing local specialization, not a
new theorem beyond the assessed analytic inputs. L604 remains the
direct local mathematical input; its L233 normalization is unchanged.
The imported analytic theorems have not been independently reproved.
No actual-theta applicability, uniform onset, separate R_+/R_- bound
or higher-sign conclusion is added.

## Mathlib

Full matching-result and supporting-result coverage not checked; no
absence or formalization claim is made. Precise analytic citations
and their specialization checks are above. The prior literature
assessment covers this calculation as REPRODUCTION; it does not
certify originality. The independent audit above validates the stated
specialization, and supplies no actual-Xi sign or RH resolution.
