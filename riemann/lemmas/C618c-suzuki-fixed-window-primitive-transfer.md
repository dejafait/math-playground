# C618c: Fixed-window closed-form transfer for arbitrary complex tests

## Hypotheses

Fix \(a=\log 3\) and \(\phi\in L^2((-a,a);\mathbb C)\), with
ordinary Lebesgue measure. Use the primitive \(q=q_\phi\), transform
\(\Phi\), and energy \(E_0\) from C618a, and the functions
\(g_0,g_1,g_\infty,g\) and anchored quadratic form \(Q_a\) from
C618b. No reality, parity, mean-zero or smoothness assumption is made.
All spatial functions below are extended by zero off their interval.
Write
\[
 F_f(z)=\int_{\mathbb R}f(x)e^{-izx}\,dx,\qquad
 C_f(u)=\int_{\mathbb R}f(x+u)\overline{f(x)}\,dx,
 \qquad h(r)=\Re\psi(1/4+ir/2)-\log\pi.
\]
Let \(\mathfrak a_a\) be the closure of the smooth compact form
\[
 \frac1{2\pi}\int_{\mathbb R}h(r)|F_f(r)|^2\,dr
 +2\Re\bigl(F_f(i/2)\overline{F_f(-i/2)}\bigr)
 -2\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}\Re C_f(\log n),       \tag{1}
\]
and let \(A_a\) be its associated Friedrichs operator.

The positivity input is Hongmin Li, *Cutoff-free positivity of localized
Weil forms through the (log 11)/2 threshold*,
[paper45/v2, 9 November 2026](https://rstation.ai/problems/riemann_hypothesis/papers/45),
Theorem 1.1, in normalization (2.1). It states
\(\inf\sigma(A_b)>0\) for \(0<b\le(\log11)/2\), on the complete
complex closed form. Its computer-assisted certificate is imported,
not replayed here; no numerical gap is imported.

For the closure identification and the identity on smooth compact
tests, use Masatoshi Suzuki, *Weil's quadratic form via the screw
function*, [arXiv:2606.09096v3, 23 September 2026](https://arxiv.org/html/2606.09096v3),
Theorem 1.1, (2.9), and Sections 3.1–3.2, especially (3.2)–(3.4).
The precise smooth identity used is
\[
 \mathfrak a_a[f]=\iint g(x-y)f'(y)\overline{f'(x)}\,dy\,dx,
 \qquad f\in C_c^\infty(-a,a).                              \tag{2}
\]
We use (2) only on compact tests, not a global temperedness assertion
for \(g\). C618a supplies Plancherel and the actual primitive;
C618b supplies the complete decomposition and the gamma estimates.

## Conclusion

The possibly discontinuous \(q_\phi\) belongs to the domain of
\(\mathfrak a_a\), and (1) holds for it with absolute convergence.
Exactly, with no extra factor or mean correction,
\[
 \boxed{Q_a(\phi)=\mathfrak a_a[q_\phi].}                   \tag{3}
\]
If \(\lambda_a=\inf\sigma(A_a)\), then the cited theorem gives
\[
 \boxed{Q_a(\phi)\ge\lambda_a\|q_\phi\|_2^2
                 =\frac{\lambda_a}{2\pi}E_0(\phi),
         \qquad \lambda_a>0.}                             \tag{4}
\]
This is strictly positive for every nonzero \(\phi\) in \(L^2\).
The constant is independent of the test but not made numerical.
It multiplies the primitive energy, not \(\|\phi\|_2^2\).

This is a specialization of known supported positivity. The argument
below supplies the domain and normalization transfer omitted from the
source comparison; it does not reprove Li's certificate. It proves
no all-window positivity, actual-Xi realization or all-degree claim.
L030-L032/C032a remain the contextual main gap, not premises. The
specialization passed the conceptual review1130 recorded below.

## Proof

### The jump and a dominating Fourier bound

Put \(m=\int_{-a}^a\phi(t)\,dt\). C618a gives absolutely continuous
restrictions of \(q\) to the two half-intervals, derivative \(-\phi\)
there, zero outer traces, and jump \(q(0+)-q(0-)=m\).
Integration by parts against a smooth compact test on each half gives
the distributional identity
\[
 Dq=\mu:=-\phi(x)\,dx+m\delta_0.                           \tag{5}
\]
Indeed the two inner endpoint contributions are
\([q(0+)-q(0-)]\eta(0)\); the outer ones vanish. Thus there are
no atoms at \(\pm a\), and \(\|\mu\|_{\rm TV}\le2\|\phi\|_1\).
The atom at zero is retained even when \(m\ne0\).

From C618a, \(\Phi(\phi,z)=iF_q(-z)\). The elementary bounds on
its removable quotient therefore give, for real \(r\ne0\),
\[
 |F_q(r)|\le M(r):=\min\{a\|\phi\|_1,\,2\|\phi\|_1/|r|\}.
                                                               \tag{6}
\]
At zero use the first bound. Since \(\phi\in L^1\) on this finite
interval and \(\int_1^\infty\log(3+r)r^{-2}dr<\infty\),
\[
 N(q)^2:=\int_{\mathbb R}\log(3+|r|)|F_q(r)|^2dr<\infty.     \tag{7}
\]
Neither (5) nor (7) asserts \(q\in H_0^1\).

### Smooth approximation inside the exact support

Choose a real nonnegative \(\rho\in C_c^\infty(-1,1)\) with
\(\int\rho=1\). For integers \(k\ge2\), set
\[
 s_k=1-1/k,\quad \epsilon_k=a/(2k),\quad
 q_k(x)=\bigl(q(\,\cdot/s_k)*\rho_{\epsilon_k}\bigr)(x),
 \qquad \rho_\epsilon(x)=\epsilon^{-1}\rho(x/\epsilon).
\]
Then \(q_k\) is smooth and its support lies in
\([-a+a/(2k),a-a/(2k)]\), strictly inside \((-a,a)\). Fubini and
the scaling substitution, applicable to the compact \(L^1\) factors,
give
\[
 F_{q_k}(r)=s_kF_q(s_kr)F_\rho(\epsilon_kr).                \tag{8}
\]
Here \(|F_\rho(r)|\le1\) on the real axis and
\(F_\rho(\epsilon_kr)\to1\). Continuity of \(F_q\) gives
pointwise convergence in (8) to \(F_q(r)\). Furthermore
\(|F_{q_k}(r)|\le M(r)\): the constant bound gains the factor
\(s_k\le1\), and the \(1/|r|\) bound cancels it.
Dominated convergence, with majorant
\(4\log(3+|r|)M(r)^2\), proves
\[
 N(q_k-q)\longrightarrow0.                                 \tag{9}
\]
Plancherel also yields \(q_k\to q\) in \(L^2\), since the
weight in (9) is bounded below by \(\log3>0\).

To verify that (9) is sufficient for form closure rather than merely
Fourier convergence, the following upper bound is enough. C618b's
digamma estimate gives \(|h(r)|\le K\log(3+|r|)\) for a fixed
finite \(K\). For any test \(f\) supported in \([-a,a]\),
\[
 |F_f(\pm i/2)|\le(2\sinh a)^{1/2}\|f\|_2,\qquad
 |C_f(u)|\le\|f\|_2^2.                                    \tag{10}
\]
The first inequality is Cauchy–Schwarz against \(e^{\pm x/2}\);
the second uses the unitary translation on \(L^2(\mathbb R)\).
Only \(n\le e^{2a}=9\) can contribute to the prime term. Hence,
on smooth compact tests,
\[
 |\mathfrak a_a[f]|\le\frac K{2\pi}N(f)^2+
 \left(4\sinh a+2\sum_{2\le n\le9}\frac{\Lambda(n)}{\sqrt n}\right)
 \|f\|_2^2.                                                \tag{11}
\]
Choose any scalar \(c\) making
\(\mathfrak a_a[f]+c\|f\|_2^2\ge\|f\|_2^2\), using the
cited semiboundedness. Equation (11) and Plancherel bound this
positive form norm by a constant times \(N(f)^2\). By (9),
\(q_k-q_\ell\) tends to zero in that form norm. The closed-form
completion therefore contains their \(L^2\) limit \(q\).
This uses no converse assertion that finite interior difference
energy alone characterizes the domain.

All terms in (1) pass to this limit. For the gamma integral use
\(|h|\le K\log(3+|r|)\) and (9), or its displayed integrable
majorant. The two pole moments converge by (10). For every real \(u\),
\[
 |C_{q_k}(u)-C_q(u)|
 \le(\|q_k\|_2+\|q\|_2)\|q_k-q\|_2\longrightarrow0.       \tag{12}
\]
The prime sum has the same finite index set for all \(k\). Thus
the closed form value on \(q\) is exactly (1), with an absolutely
integrable gamma term and finite remaining terms.

### The anchored limit, including both complex cross terms

For a finite complex measure \(\nu\) write
\(J_b(\nu)=\iint b(x-y)\,d\nu(y)\,\overline{d\nu(x)}\)
when \(b\) is continuous on the relevant compact difference set.
This is an ordinary absolutely convergent measure integral, bounded
by \(\sup|b|\,\|\nu\|_{\rm TV}^2\).

Equation (5), scaling, and differentiation of convolution imply
\[
 q_k'(x)dx=\mu_k:=((x\mapsto s_kx)_*\mu)*\rho_{\epsilon_k}.
                                                               \tag{13}
\]
There is no extra factor \(s_k\) in the pushforward derivative:
the absolutely continuous part has density
\(-s_k^{-1}\phi(x/s_k)\), and the zero atom still has mass \(m\).
By Fubini, \(J_b(\mu_k)\) is the integral against
\(d\mu(y)\overline{d\mu(x)}\) of the average of
\(b(s_k(x-y)+u-v)\) with weights
\(\rho_{\epsilon_k}(u)\rho_{\epsilon_k}(v)\).
Both arguments lie in \([-2a,2a]\), and
\[
 |s_k(x-y)+u-v-(x-y)|\le 2a/k+2\epsilon_k=3a/k.
\]
Uniform continuity on that compact interval consequently gives
\[
 |J_b(\mu_k)-J_b(\mu)|
 \le\|\mu\|_{\rm TV}^2\,\omega_b(3a/k)\longrightarrow0,    \tag{14}
\]
where \(\omega_b\) is its modulus of continuity. This proves the
double-measure limit directly, including the atom-atom term; weak
convergence alone has not been substituted for a product argument.

Use (2) for each smooth \(q_k\), then form convergence and (14)
with \(b=g\). The result is \(\mathfrak a_a[q]=J_g(\mu)\).
Expanding (5) gives
\[
\begin{split}
 J_g(\mu)={}&\iint g(x-y)\phi(y)\overline{\phi(x)}\,dy\,dx\\
 &-m\int g(x)\overline{\phi(x)}\,dx
 -\overline m\int g(-y)\phi(y)\,dy+|m|^2g(0).
\end{split}                                                   \tag{15}
\]
This is exactly the four-term anchored definition of \(Q_a(\phi)\).
Every integral is absolute because \(g\) is continuous on the compact
set and \(\phi\in L^1\). In particular the two cross terms have
the required different conjugations for a complex test. Equation (3)
follows, including all tests with \(m\ne0\).

### Check of the pole, primes and gamma normalization

For completeness the same limit verifies each part of C618b,
without transferring an unsigned or truncated form. Apply (14) to
each continuous \(g_j\), and expand as in (15). It shows that the
anchored component \(I_j\) equals
\(\lim_k\iint g_j(x-y)q_k'(y)\overline{q_k'(x)}\,dy\,dx\).

For the pole part, \(-g_0''(t)=e^{t/2}+e^{-t/2}\).
Twice integrating by parts on the compact smooth tests gives
\[
 I_0=2\Re\bigl(F_q(i/2)\overline{F_q(-i/2)}\bigr).          \tag{16}
\]
The boundary terms vanish for every \(q_k\); passage to \(q\)
uses (10), not integration by parts through its jump. This retains
the pole form's possible negative sign.

Locally, the prime part is a finite sum of
\(\alpha_n(|t|-d_n)_+\), where
\(\alpha_n=\Lambda(n)/\sqrt n\), \(d_n=\log n>0\).
Its second distributional derivative is
\(\alpha_n(\delta_{d_n}+\delta_{-d_n})\). Smooth integration
by parts followed by (12) therefore gives
\[
 I_1=-2\sum_{n\ge2}\alpha_n\Re C_q(d_n).                    \tag{17}
\]
Here \(C_q(-u)=\overline{C_q(u)}\), by substitution, without
assuming \(q\) real. At \(d_n\ge2a\) the overlap has measure
zero, so the term is zero, including \(n=9\). The active prime
powers are \(2,3,4,5,7,8\); no boundary mass at \(\log9\)
is inserted. The jump of \(q\) at one point changes no correlation
integral.

Finally C618b, (3), supplies the full gamma component. Its weight
\(W(r)=\tfrac12\Re\psi(1/4-ir/2)-\tfrac12\log\pi\)
is real and even, so \(h(r)=2W(r)\). Since
\(\Phi(\phi,r)=iF_q(-r)\), change \(r\) to \(-r\) in one
of the two absolutely convergent terms to obtain
\[
 I_\infty=\frac1{2\pi}\int W(r)
     (|\Phi(\phi,r)|^2+|\Phi(\phi,-r)|^2)\,dr
 =\frac1{2\pi}\int h(r)|F_q(r)|^2\,dr.                    \tag{18}
\]
Equations (16)–(18) match every term of (1). They independently
check that (3) has neither a factor two nor a missing pole or prime
contribution. No contour involving zeros is needed in this transfer.

### Import of the supported sign

The support comparison is exact: \(2\log3=\log9<\log11\).
Thus Li's cited Theorem 1.1 applies to \(A_a\), giving
\(\lambda_a>0\). The spectral lower bound of an associated closed
form is \(\mathfrak a_a[q]\ge\lambda_a\|q\|_2^2\) throughout
its form domain (also Suzuki (1.7)); membership was proved above.
C618a gives \(E_0=2\pi\|q\|_2^2\), proving (4).

If \(q=0\) almost everywhere, its absolutely continuous restriction
on each half is identically zero and hence has derivative zero there.
As that derivative is \(-\phi\), this forces \(\phi=0\) almost
everywhere. Thus \(E_0>0\) for every nonzero test, including tests
of nonzero integral. This completes the fixed-window transfer.

All-support signs and Xi realization remain independent unresolved
questions. Neither numerical evidence nor RH-equivalent global
positivity is used as a substitute for them.

### Independent conceptual review — 16 November 2026, step1130

Accepted (3)–(4) for the full stated complex \(L^2\) class under
the pre-existing SPECIALIZE assessment1128, approved separately
in1129. No correction to the argument, hypotheses or constants was
needed. This establishes the reviewed local applicability of the
cited fixed-window theorem; it supplies neither a stronger supported
positivity theorem nor a numerical value of \(\lambda_a\).

The review read C618a and C618b, checked Li paper45/v2 Theorem 1.1
and (2.1), and checked Suzuki v3 Theorem 1.1, (1.7), (2.9) and
Sections 3.1–3.2, including both boundary contributions and both
frequency ranges in (3.3)–(3.4). Li's form convention agrees term
by term with (1). Suzuki's \(D=i\,d/dx\) gives the same smooth
identity: the factors \(i\) and \(\overline i=-i\) multiply to
one. His \(g\), including the Lerch series, is C618b's \(g\).
Only the compact smooth identity and the closed-form framework
are imported. No global temperedness or endpoint-free domain
characterization is needed.

The decisive analytic checks were the following.

- **Exact domain.** The contraction leaves margin \(a/k\), and
  convolution uses only \(a/(2k)\), so every approximant belongs
  to the smooth core of this very interval. From (6) and (8), the
  common majorant is \(M\), including low frequencies. Hence
  (9) controls differences of approximants in the weighted norm.
  If \(B=4\sinh a+2\sum_{2\le n\le9}\Lambda(n)/\sqrt n\),
  (11) gives explicitly on the core
  \[
  \|f\|_{\mathfrak a,c}^2
  :=\mathfrak a_a[f]+c\|f\|_2^2
  \le\left(\frac K{2\pi}+
       \frac{B+|c|}{2\pi\log3}\right)N(f)^2.
  \]
  Choose \(c\) with \(\|f\|_{\mathfrak a,c}^2\ge\|f\|_2^2\).
  Completeness and this embedding identify the form limit with
  the already established \(L^2\) limit \(q\). This is a form
  Cauchy argument, not just membership in a Fourier-weight space.
  The gamma term converges by weighted Cauchy–Schwarz, and (10),
  (12) control all remaining terms. No equality of the form and
  operator domains is asserted.
- **Jump and complex product limit.** The half-interval integration
  by parts gives precisely \(-\phi\,dx+m\delta_0\); its total
  mass is zero and its outer endpoint masses are zero. Under
  contraction its absolutely continuous density is
  \(-s_k^{-1}\phi(x/s_k)\), with atom still \(m\delta_0\).
  In (14), the finite product measure has total variation at most
  \(\|\mu\|_{\rm TV}^2\); the real nonnegative mollifier has
  total mass one in each variable. The two kernel arguments stay
  in \([-2a,2a]\), and their distance is at most \(3a/k\).
  Thus the stated uniform modulus bound covers both cross terms
  and the atom-atom term, even for complex \(m\). Expanding the
  limit gives (15) with exactly the two different conjugations.
- **Signs and normalization.** The double integration by parts
  produces \(-g_j''\). The pole gives the signed product in
  (16), while each prime hinge gives the two negative translates
  in (17). Overlap at \(d_n=2a\) is a null set for \(L^2\)
  correlations, including the entering prime power \(n=9\).
  The gamma comparison uses evenness of \(W\), not evenness of
  an individual complex Fourier modulus. Consequently \(h=2W\)
  and \(E_0=2\pi\|q\|_2^2\) give precisely (4). The strict
  support inequality \(\log9<\log11\) supplies Li's hypothesis.
  Injectivity follows from the derivative on each open half,
  without imposing zero mean.

C618a and C618b remain the direct local mathematical inputs. The
source certificate was not replayed. All-window positivity,
energy-weighted comparisons beyond known windows, and actual-Xi
realization remain unresolved; this audit introduces no premise
that assumes any of them.

## Mathlib

Full matching coverage and supporting theorem names were not checked
in Mathlib. This is not evidence of absence. The analytic imports
are the named Fourier/Plancherel input of C618a and the precisely
cited source forms and positivity above; the discontinuous-primitive
specialization and limiting arguments are supplied here. There is
no Lean verification, numerical spectral-gap computation or replay
of the external positivity certificate in this step.
