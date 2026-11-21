# C744h: Exactly neutral finite even tests admit exactly neutral smooth form approximants

## Hypotheses

Put \(\ell=\log(3)/2\), \(a=5\ell/2\), \(L=2a\), and
\(b_j=-a+j\ell\), \(0\le j\le5\). The open cells are
\(I_j=(b_j,b_{j+1})\), with centers \(t_j=(j-2)\ell\).
All functions are complex valued and extended by zero to the real line.
Use exactly C744b's physical moments and even normalization:

\[
 (Cf)_{j,\sigma}=\int_{I_j}e^{\sigma(x-t_j)/2}f(x)\,dx,
 \quad 0\le j<5,\quad \sigma=\pm1;
 \qquad
 f(x)=\frac1{\sqrt2}\sum_{q=0}^{83}z_q e_q^+(|x|)
 \quad (|x|<a),                                      \tag{1}
\]

where \(z_q\in\mathbb C\), \(e_0^+=a^{-1/2}\), and
\(e_q^+(x)=(2/a)^{1/2}\cos(q\pi x/a)\) for \(q\ge1\).
Assume **all ten equations \(Cf=0\) exactly**. No numerical moment
residual or projected constraint is substituted for this assumption.

Use the centered form of L744(6), with the Fourier convention
\(F_w(\xi)=\int w(x)e^{-i\xi x}\,dx\):

\[
 q(w)=\int_{\mathbb R}m(\xi)|F_w(\xi)|^2\frac{d\xi}{2\pi}
  +2\Re\bigl(F_w(i/2)\overline{F_w(-i/2)}\bigr)
  -\langle B_Lw,w\rangle,
 \quad m(\xi)=\Re\psi(1/4+i\xi/2)-\log\pi.           \tag{2}
\]

Here \(B_L\) is the complete finite Hermitian prime-delay operator
of L744(2), translated to \((-a,a)\). Its norm is at most
\(C_{\rm prime}=2\sum_{2\le n<e^L}\Lambda(n)/\sqrt n\).
No prime power, pole, or mixed term is omitted. On smooth tests (2)
is the complete energy, and \(\overline E_L\) denotes its smooth
semibounded form closure, not the domain of its generator.

The pre-invocation SPECIALIZE assessment is
`drafts/literature/2026-11-11-five-cell-exact-neutral-smooth-transfer-475.md`.
This result specializes the cutoff mechanism in Masatoshi Suzuki,
*Weil's quadratic form via the screw function*,
[arXiv:2606.09096v3, Section3.2, (3.2)-(3.4) and the following two frequency estimates](https://arxiv.org/html/2606.09096v3#S3.SS2),
already implemented with genuine compact cutoffs in C744c Section2.
The source handles outer boundaries without these ten constraints;
the internal boundaries and exact parity-compatible correction are
justified below. L743(9)-(10) supplies the fixed smooth two-moment
inverse. The general finite-dimensional complement method is also
recorded in H. Hofer, K. Wysocki and E. Zehnder, *A general Fredholm
theory I: A splicing-based differential geometry*, JEMS9(2007),841-876,
[Lemma2.12, p846](https://ems.press/content/serial-article-files/31611).
That lemma assumes a Banach space, a closed subspace with a finite
dimensional complement, and a dense linear subspace; it supplies a
complement in that dense subspace. We use L743's explicit inverse
instead of assuming the density needed to apply that abstract lemma.

## Conclusion

There is a fixed \(\kappa>0\), independent of \(f\) and the cutoff
parameter, such that \(q_\kappa=q+\kappa\|\cdot\|_2^2\) is a
positive form norm squared on the supported logarithmic Fourier
space. For every \(f\) in (1) with \(Cf=0\), there are even

\[
 f_\epsilon\in\bigoplus_{j=0}^4 C_c^\infty(I_j;\mathbb C),
 \qquad Cf_\epsilon=0,
 \qquad q_\kappa(f-f_\epsilon)\longrightarrow0.       \tag{3}
\]

In fact \(q_\kappa(f-f_\epsilon)=O_f(\epsilon\log(1/\epsilon))\).
Consequently \(f\) belongs to the smooth form closure, and
\(E_L(f_\epsilon)\to\overline E_L(f)=q(f)\), interpreting the
centered tests by translation to \((0,L)\). Every translated
approximant belongs to L743's original \(\mathcal U_5\), and both
global pole moments vanish exactly, for the limit and the approximants.

This pays only a domain-transfer issue for the stated finite neutral
space. It proves no positive energy margin, energy-saving correction,
infinite-complement bound, odd-sector sign or all-window assertion.
The fixed-half-energy stop in C744g is a contrast, not a premise.
The separate conceptual audit below (11 November 2026, step479)
accepts this specialization without changing its hypotheses or conclusion.

## Proof

### 1. A positive shift and the norm in which convergence is needed

Write
\[
 \|w\|_{\log}^2=\int_{\mathbb R}
      (1+\log(2+|\xi|))|F_w(\xi)|^2\frac{d\xi}{2\pi}.
                                                               \tag{4}
\]
By L744(8), \(m\) is bounded below and grows as
\(\log(|\xi|/(2\pi))+O(|\xi|^{-2})\) at infinity.
Therefore some \(s>0\) and \(0<\alpha\le\beta<\infty\) satisfy
\(\alpha(1+\log(2+|\xi|))\le m(\xi)+s
\le\beta(1+\log(2+|\xi|))\) everywhere: take the comparison
first outside a fixed compact interval, then increase \(s\) to pay
the bounded interval. C744c Section2 identifies this closed weighted
Fourier form and its bounded perturbations; no identification of
whole periodic and zero-extension domains is required.

On functions supported in \([-a,a]\), each of the two exponential
representers for \(F_w(\pm i/2)\) has squared L2 norm
\(2\sinh a\). Thus the absolute pole form is at most
\(4\sinh(a)\|w\|_2^2\). Put
\(M=4\sinh a+C_{\rm prime}\) and \(\kappa=s+M+1\).
Plancherel and the prime norm bound give

\[
 \alpha\|w\|_{\log}^2\le q_\kappa(w)
 \le (\beta+2M+1)\|w\|_{\log}^2.                  \tag{5}
\]

The associated Hermitian form is therefore an inner product on
the supported space of finite (4). Its completeness follows from
weighted Fourier completeness and the L2-closed support condition.
The smooth form closure embeds in this space; membership of our
particular \(f\) in that closure will follow from the approximants,
not from an asserted density theorem for the punctured interval.

The finite cosine function in (1) is smooth on \([-a,a]\) before
zero extension. Its extension has finite variation, including its
two endpoint jumps. Its Fourier transform is bounded by its L1 norm
and, away from zero, by its variation divided by \(|\xi|\).
These two bounds show directly that (4) is finite for \(f\), also
for the newly included modes64-83.

### 2. Cut off all six boundaries, retaining their Fourier cost

Fix a real even \(\eta\in C^\infty(\mathbb R)\) with
\(0\le\eta\le1\), \(\eta(y)=0\) for \(|y|\le1\), and
\(\eta(y)=1\) for \(|y|\ge2\). Its derivative is compactly
supported. For \(0<\epsilon<\min(\ell/8,1/2)\), define

\[
 \chi_\epsilon(x)=\prod_{j=0}^{5}\eta((x-b_j)/\epsilon),
 \qquad w_\epsilon=\chi_\epsilon f,
 \qquad g_\epsilon=f-w_\epsilon.                    \tag{6}
\]

The boundary set is invariant under reflection, so the cutoff and
\(w_\epsilon\) are even. The cutoff vanishes in a neighborhood of
each boundary. Hence \(w_\epsilon\) is genuinely smooth with compact
support inside each open cell, including after zero extension.

Set \(M_0=\sup_{[-a,a]}|f|\) and
\(M_1=\sup_{[-a,a]}|f'|\) for the smooth interior formula.
The support of \(g_\epsilon\) lies in six strips of total length
at most \(24\epsilon\). In particular

\[
 \|g_\epsilon\|_1\le24M_0\epsilon,
 \qquad \|g_\epsilon\|_2^2\le24M_0^2\epsilon.
\]

By differentiating the product in (6),
\(\int_{\mathbb R}|\chi_\epsilon'|\le6\|\eta'\|_1\).
The variation of the zero extension of \(g_\epsilon\) is at most

\[
 2M_0+24\epsilon M_1+6M_0\|\eta'\|_1.              \tag{7}
\]

The first term explicitly pays the two outer endpoint jumps.
There are no internal jumps: the original cosine formula agrees
on both sides of every internal boundary. Integration by parts for
this piecewise smooth function, retaining the outer endpoint terms,
now gives a constant \(K_f<\infty\), independent of \(\epsilon\),
such that

\[
 |F_{g_\epsilon}(\xi)|\le K_f\min(\epsilon,|\xi|^{-1})
 \quad(\xi\ne0),\qquad |F_{g_\epsilon}(0)|\le K_f\epsilon.
                                                               \tag{8}
\]

Split (4) at \(|\xi|=1/\epsilon\). The lower part is bounded
by \((K_f^2/\pi)\epsilon^2
\int_0^{1/\epsilon}(1+\log(2+x))\,dx\); the upper part is bounded
by \((K_f^2/\pi)\int_{1/\epsilon}^{\infty}
(1+\log(2+x))x^{-2}\,dx\).
For \(R>0\), integration by parts gives the latter integral as
\((1+\log(2+R))/R+\tfrac12\log(1+2/R)\).
Both parts are therefore \(O_f(\epsilon\log(1/\epsilon))\), so

\[
 \|g_\epsilon\|_{\log}^2
       =O_f(\epsilon\log(1/\epsilon)).                \tag{9}
\]

This is the specific internal-boundary specialization of the
inspected Suzuki/C744c mechanism; L2 convergence alone was not used
to conclude form convergence.

### 3. A fixed smooth right inverse in the form norm, with even parity

Use L743(9)'s fixed real nonnegative
\(\rho\in C_c^\infty(0,\ell)\), positive on an open interval,
and its invertible two-by-two matrix and smooth functions

\[
 G_{\sigma\tau}=\int_0^\ell\rho(s)e^{(\sigma+\tau)s/2}\,ds,
 \qquad \varphi_\tau(s)=\rho(s)e^{\tau s/2}.
\]

The invertibility, including for complex coefficients, is already
proved in L743(9)-(10) and is imported. Let
\(D=\operatorname{diag}(e^{\ell/4},e^{-\ell/4})\), with coordinate
order \(+1,-1\). For \(d\in\mathbb C^{10}\), set

\[
 Hd(x)=\sum_{j=0}^{4}\sum_{\tau=\pm1}
               (G^{-1}Dd_j)_\tau\varphi_\tau(x-b_j). \tag{10}
\]

Each summand is extended by zero outside its cell. It follows that
\(Hd\in\bigoplus_j C_c^\infty(I_j)\). On cell \(j\), the physical
weight is \(e^{\sigma(s-\ell/2)/2}\); hence
\((CHd)_{j,\sigma}=e^{-\sigma\ell/4}(GG^{-1}Dd_j)_\sigma
=d_{j,\sigma}\). This verifies the physical normalization, not only
the uncentered moments of L743.

For the ten standard coordinate vectors \(u_\nu\), let
\(h_\nu=Hu_\nu\). These are fixed smooth compact functions. Each has
finite (4): for example \(1+\log(2+|\xi|)\le c(1+\xi^2)\), and
Plancherel applied to \(h_\nu,h_\nu'\) bounds (4). Thus

\[
 \|Hd\|_{\log}\le K_H|d|,
 \qquad K_H=\left(\sum_{\nu=1}^{10}\|h_\nu\|_{\log}^2\right)^{1/2}
 <\infty.                                             \tag{11}
\]

This follows from the triangle inequality and finite-dimensional
Cauchy-Schwarz. Unlike a mere L2 estimate, it pays the correction
in the required form norm.

Write \(Rw(x)=w(-x)\) and \((Pd)_{j,\sigma}=d_{4-j,-\sigma}\).
C744b's change of variables gives \(CR=PC\), with no complex
conjugation. In particular \(P^2=1\) and even tests have \(PCw=Cw\).
Reflection is an isometry of (4), because
\(F_{Rw}(\xi)=F_w(-\xi)\) and the weight is even. For \(Pd=d\), put

\[
 H_+d=\tfrac12(Hd+RHd).
 \qquad CH_+d=\tfrac12(d+Pd)=d,
 \qquad\|H_+d\|_{\log}\le K_H|d|.                  \tag{12}
\]

Reflection permutes the cell interiors, so this remains smooth with
compact support in each cell and is even. This constructs an inverse
on the correct five-dimensional symmetric output space, without
pretending the ten even moment equations are independent. All maps
are complex linear; no real-coefficient restriction was introduced.

### 4. Exact correction and passage to the complete form

Since \(Cf=0\), let \(d_\epsilon=Cw_\epsilon=-Cg_\epsilon\).
The evenness of \(w_\epsilon\) gives \(Pd_\epsilon=d_\epsilon\).
The weights in (1) are at most \(e^{\ell/4}\) in absolute value,
so each coordinate of \(Cg_\epsilon\) is at most
\(e^{\ell/4}\|g_\epsilon\|_1\). Therefore

\[
 |d_\epsilon|\le\sqrt{10}e^{\ell/4}\|g_\epsilon\|_1
       =O_f(\epsilon).                              \tag{13}
\]

Define \(f_\epsilon=w_\epsilon-H_+d_\epsilon\). Equations (10)-(12)
give evenness, genuine compact support within every cell, and
\(Cf_\epsilon=d_\epsilon-d_\epsilon=0\) **exactly**. Moreover

\[
 \|f-f_\epsilon\|_{\log}
 \le\|g_\epsilon\|_{\log}+K_H|d_\epsilon|,
 \qquad
 \|f-f_\epsilon\|_{\log}^2
       =O_f(\epsilon\log(1/\epsilon)).                \tag{14}
\]

Here the correction has squared norm \(O_f(\epsilon^2)\); all cross
terms are controlled by the displayed norm inequality, not omitted.
Equations (5) and (14) prove (3) and smooth-closure membership.
Continuity of an inner product in its norm implies
\(q_\kappa(f_\epsilon)\to q_\kappa(f)\); L2 convergence then
subtracts the shift and proves convergence of the complete energy.

Finally, on each cell the uncentered local moment is
\(e^{\sigma\ell/4}\) times (1). Translation to \((0,L)\) thus gives
the defining moments of \(\mathcal U_5\). Also, for any \(Cw=0\),
\(F_w(\sigma i/2)=\sum_{j=0}^4e^{\sigma t_j/2}(Cw)_{j,\sigma}=0\).
This pays both global pole moments, including for complex tests.
No sign of the remaining form, bound on a growing window, or uniform
H2 cap on these approximants has been asserted.

### 5. Separate conceptual audit — 11 November 2026, step479

This audit uses the pre-invocation SPECIALIZE assessment
`drafts/literature/2026-11-11-five-cell-smooth-transfer-audit-477.md`.
It verifies this finite, complex, exactly neutral statement only.
The source comparison is reused: Suzuki Section3.2 supplies the
cutoff method; HWZ Lemma2.12 supplies background for finite-dimensional
correction, but is not invoked to assume an unproved core-density
hypothesis. L743(9)-(10)'s explicit inverse is the input actually used.
This is REPRODUCTION/local verification, not a new sign theorem or
an assertion of originality beyond the inspected sources.

**Complete form and its shift.** L744(6) is an identity on all smooth
compact tests at this fixed length; its proof does not require the
H2 cap used in that lemma's modulation conclusion. L744(8) gives the
large-frequency asymptotic in Section1, and boundedness on compact
frequency intervals. Hence the stated constants s, alpha and beta
exist. If p denotes the sum of the pole and negative prime forms,
then |p(w)|<=M||w||_2^2: both exponential representers have squared
norm 2sinh(a), and the complete finite prime operator has the norm
bound stated above. Thus

    q_kappa(w) = integral (m+s)|F_w|^2 dxi/(2pi)
                 + p(w) + (M+1)||w||_2^2

lies between alpha||w||_log^2+||w||_2^2 and
beta||w||_log^2+(2M+1)||w||_2^2. This verifies (5), including strict
positivity without assuming positivity of q. The weighted supported
space is complete; restriction of this closed positive form to the
smooth core is closable. Its closure is the norm closure of that core
inside the supported space, with the same value of q_kappa. No claim
that the whole supported space equals the core closure is needed.

**All six collars and both Fourier ranges.** For epsilon<ell/8 the
strips of radius 2epsilon about distinct boundaries are disjoint.
Four internal strips have length 4epsilon each, while the parts of
the two outer strips inside [-a,a] have total length 4epsilon. Thus
the asserted upper bound 24epsilon is conservative. The product
cutoff is zero on genuine collars of width epsilon. On every cell
its product with the cosine formula is smooth and vanishes near
both ends; its zero extension is smooth. Reflection permutes the
six factors and preserves the cutoff.

Inside (-a,a), the derivative of g_epsilon is
(1-chi_epsilon)f'-chi_epsilon'f. Integrating its absolute value
gives the last two terms of (7); the jumps at -a,a have total
absolute size at most 2M_0. At internal boundaries the original f
has a single smooth formula, so g_epsilon has no jump there. For
example, one epsilon-independent choice in (8) is

    K_f = max(24M_0, 2M_0+12M_1+6M_0||eta'||_1).

The L1 estimate supplies K_f epsilon, and integration by parts
against the finite complex variation measure supplies K_f/|xi|.
This argument applies equally to complex coefficients. For R=1/epsilon,
the low-frequency integral is at most
epsilon^2 R(1+log(2+R)). The exact high-frequency integral is

    integral_R^infinity (1+log(2+x))/x^2 dx
      = (1+log(2+R))/R + (1/2)log(1+2/R).

Both are O(epsilon log(1/epsilon)) as epsilon tends to zero, with
the common factor K_f^2/pi retained in the Fourier estimate. This
checks the whole integral, including arbitrarily high frequencies.
The same finite-variation argument makes the original finite cosine
sum an element of the weighted space before any closure assertion.

**Physical inverse and complex parity.** In cell coordinates x=b_j+s
one has x-t_j=s-ell/2. The matrix of the physical moments on the two
fixed smooth functions is exactly D^{-1}G. Hence the inverse in (10)
has moment matrix D^{-1}GG^{-1}D=I, with the positive exponent in
D essential. L743(9)'s Gram argument is valid over the complex field.
Each of the ten inverse images h_nu is fixed and has a smooth zero
extension; Plancherel for h_nu and its derivative bounds its logarithmic
norm. Finite-dimensional Cauchy-Schwarz therefore proves (11) in that
norm, not only in L2.

Changing variable x=-y gives (CRw)_(j,sigma)=(Cw)_(4-j,-sigma),
without conjugation. P has five two-element orbits, including the
two opposite moments in the middle cell, so its fixed space has
complex dimension five. For every datum in that space H_+ is even,
has the required cell-interior support, and satisfies CH_+=I.
Reflection is an isometry of the even logarithmic Fourier weight.
These facts prove the correction norm bound for arbitrary complex
data. As an additional continuity check, Cauchy-Schwarz on each cell
gives ||Cw||^2<=4sinh(ell/2)||w||_2^2, so the moment constraints are
also continuous in the shifted form norm.

**Exact equations and complete-energy limit.** Since Cf=0 exactly,
d_epsilon=-Cg_epsilon has Euclidean norm at most
24sqrt(10)exp(ell/4)M_0 epsilon. It is fixed by P. Thus subtracting
H_+d_epsilon from w_epsilon cancels all ten physical equations
exactly and preserves evenness and smooth support. The squared
correction norm is O_f(epsilon^2); the triangle inequality, or
its squared bound 2||g_epsilon||_log^2+2K_H^2|d_epsilon|^2,
retains all cross terms and proves (14). Together with (5), this
puts f in the smooth form closure and proves the claimed rate.

For the last passage, the inner-product inequality gives

    |q_kappa(f_epsilon)-q_kappa(f)|
      <= ||f_epsilon-f||_(q_kappa)
         (||f_epsilon||_(q_kappa)+||f||_(q_kappa)) -> 0.

Convergence in L2 then allows subtraction of kappa||.||_2^2,
so this is convergence of the complete energy, not just its shift.
Translation to (0,L) multiplies the two global Fourier pole moments
by reciprocal positive factors and preserves their product, Fourier
moduli on the real line, and every prime correlation. Each translated
local uncentered moment is exp(sigma ell/4) times the physical one.
This proves membership of every approximant in the original U_5.
The displayed sum of physical moments for F_w(sigma i/2) proves
both global cancellations exactly for the limit and approximants.

**Verdict and scope.** All parts of (3), its rate, and the complete
energy limit pass without repair. The existing direct mathematical
inputs are unchanged. Neither a uniform H2 bound nor a growing-window
estimate is obtained. C744g's half-energy stop remains valid;
unrestricted middle/distant interactions, odd signs and all-window
positivity remain open. This is no RH candidate.

## Mathlib

A full matching theorem for this constrained, even, five-cell
logarithmic form approximation was not checked in Mathlib. No formal
verification or absence claim is made. The proof uses standard
Plancherel, finite-dimensional linear algebra, reflection and norm
continuity; supporting results alone would not formalize the complete
analytic specialization.
