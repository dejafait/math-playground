# C744o: Uniform full mixed-energy bound on the growing window

## Hypotheses

Fix ell=log(3)/2, finite M0,M1>=1 and the real nonnegative
chi in C_c^infinity(0,ell), positive on a nonempty open interval,
used in C744n. For real t, put T=|t| and

\[
 K(t)=\lfloor\log\log T/\ell\rfloor,\qquad L(t)=K(t)\ell.
\]

Use exactly L744(1)'s complex smooth cell-train families:
u in F_(K(t),M0), w in F_(K(t),M1). Thus both uncorrected
profiles have L2 norm one, and their zero extensions satisfy

\[
 \|u\|_{H^2}^2=\|u\|_2^2+\|u'\|_2^2+\|u''\|_2^2\le M0^2,
 \qquad \|w\|_{H^2}\le M1.
\]

Additionally require, for every cell j and sigma in {+1,-1},

\[
 \int_0^\ell e^{\sigma s/2}u_j(s)\,ds=0.                 \tag{1}
\]

Let f=e^(itx)w, h=h_(t,w) and v=v_(t,w)=f-h be precisely
C744n(1)'s correction, with the same fixed chi and matrix G.
Every norm and pairing is in the original unweighted L2 space;
the inner product is linear in its first slot. For the complete
generator used in L744 define

\[
 \mathcal E_L(a,b)=-\frac{\langle A_La,b\rangle+
                                      \langle a,A_Lb\rangle}{2}.
                                                               \tag{2}
\]

Both profiles may depend arbitrarily on t subject to the stated
constraints. No sign of E_L(u) or RH assumption is imposed.
Empty admitted families make no existence assertion.

## Conclusion

There is a finite constant C depending only on M0,M1,chi (ell fixed)
such that, for every real t with T>=e^3 and all admitted pairs,

\[
 \boxed{\ |\mathcal E_{L(t)}(u,v_{t,w})|
                       \le C\frac{\log T}{T^2}.\ }              \tag{3}
\]

In particular K(t)>=2. A stronger explicit bound is (12) below.
It covers the full complex pairing, both signs of t, all prime powers,
both varying profiles and the entire correction, with no K-dependent
constant. This is a REPRODUCTION by standard Fourier/Sobolev
specialization under the prior SPECIALIZE assessment
`drafts/literature/2026-11-11-growing-window-mixed-pairing-498.md`.
It establishes a local intermediate estimate, with no claim of
originality beyond the sources checked. The separate conceptual audit
below (11 November 2026, step502) accepts (3) and (12) under exactly
these hypotheses, including the stated threshold T>=e^3.

## Proof

### Complete polarization and exact poles

First allow any finite K>=2 and L=K ell, with these same profile
conditions. All functions u,w,f,h,v have smooth compact support
in (0,L), and lie in the actual generator domain by L744's smooth
domain argument. Any complex linear combination does too. Write
F_g(xi)=integral g(x)exp(-i xi x)dx and dmu=dxi/(2pi).
L744(6) is the complete energy identity on this smooth space.
Polarizing it gives

\[
 \begin{split}
 \mathcal E_L(a,b)&=Q_m(a,b)
  +F_a(i/2)\overline{F_b(-i/2)}
  +F_a(-i/2)\overline{F_b(i/2)}-\langle B_La,b\rangle,\\
 Q_m(a,b)&=\int_{\mathbb R}m(\xi)F_a(\xi)
                                \overline{F_b(\xi)}\,d\mu,\\
 m(\xi)&=\Re\psi(1/4+i\xi/2)-\log\pi,\\
 B_L&=\sum_{2\le n<e^L}\frac{\Lambda(n)}{\sqrt n}
                              (T_{\log n}+T_{\log n}^*).
 \end{split}                                                   \tag{4}
\]

For clarity, each side is a Hermitian sesquilinear form, linear in
a, and its diagonal is L744(6). Equality of the diagonals determines
the real part of the off-diagonal by the value at a+b and its
imaginary part by the value at a+i b, hence determines the whole
form. This checks the conjugations in (4); the pole form is not a
modulus square. Smooth Fourier transforms and L744(8)'s bound below
make these scalar integrals absolutely convergent.

Condition (1) gives F_u(sigma i/2)=0: split the finite integral into
cells and multiply each zero local moment by e^(sigma j ell/2).
C744n's unchanged complex-linear correction likewise gives
F_v(sigma i/2)=0 exactly for both signs. Thus both pole products in
(4) vanish. We estimate Q_m(u,f)-Q_m(u,h) and
<B_Lu,f>-<B_Lu,h> separately. Their intermediate pole terms need
not be estimated; (4) has already been applied to the actual pair u,v.

### Weighted overlap for arbitrary two H2 profiles

Use L744(8)'s already justified global bound

\[
 |m(\xi)|\le W(\xi)=A+\log(2+|\xi|),\qquad
 A=2+8\sqrt2/3+\log(4\pi).                                 \tag{5}
\]

Its source is DLMF 5.11.2 and 5.11(ii)'s complex remainder on
z=1/4+i xi/2, including bounded xi. We import that specialization
without rederiving the digamma asymptotic. For the Fourier identities
we import Plancherel and Fourier differentiation in the convention
above: Andras Vasy, *Math 172: The Fourier Transform — Basic Properties
and the Inversion Formula*, [author-hosted notes](https://math.stanford.edu/~andras/172-4.pdf),
undated version inspected in the prior assessment, pp.1-2 and
Lemma 0.4/proof, p.13. Smooth compactly supported zero extensions
satisfy its decay hypotheses. These identities are supporting imports;
the following quantitative application is the required specialization.

Set p(s)=1+s^2+s^4. Plancherel gives

\[
 \int p(\xi)|F_u(\xi)|^2d\mu=\|u\|_{H^2}^2\le M0^2,
 \qquad \int p(\eta)|F_w(\eta)|^2d\mu\le M1^2.              \tag{6}
\]

For T>=2 and any xi, let r=max(|xi|,|xi-t|). The triangle inequality
gives r>=T/2>=1. Since sqrt(p(s))>=1 and sqrt(p(s))>=s^2,
the product sqrt(p(xi)p(xi-t)) is at least r^2. Also |xi|<=r.
The function g(r)=[A+log(2+r)]/r^2 is decreasing for r>=1:
its derivative has numerator r/(2+r)-2[A+log(2+r)]<0, since A>1.
Consequently, on the entire real line,

\[
 \frac{|m(\xi)|}{\sqrt{p(\xi)p(\xi-t)}}
 \le\frac{A+\log(2+r)}{r^2}
 \le\frac{4[A+\log(2+T/2)]}{T^2}.                          \tag{7}
\]

There is no discarded neighborhood of xi=0 or xi=t and no assumption
of disjoint Fourier supports. As F_f(xi)=F_w(xi-t), multiply (7)
by sqrt(p(xi))|F_u(xi)| sqrt(p(xi-t))|F_w(xi-t)| and integrate.
Cauchy--Schwarz and (6), with a translation of the second integral,
give

\[
 |Q_m(u,f)|\le\frac{4M0M1[A+\log(2+T/2)]}{T^2}.             \tag{8}
\]

Every constant here is independent of the support and the profiles.

### All delays and the whole correction

For any a>=0 the zero-extension formulas for the truncated delay and
its adjoint give

\[
 \langle T_au,f\rangle=\int_{\mathbb R}
           u(x-a)\overline{w(x)}e^{-itx}dx,\qquad
 \langle T_a^*u,f\rangle=\int_{\mathbb R}
           u(x+a)\overline{w(x)}e^{-itx}dx.
\]

These formulas include the support restrictions because w vanishes
outside (0,L) and u is zero-extended. Each envelope product is smooth
and compactly supported on the full line, for every a. Two integrations
by parts therefore have no boundary terms. Product differentiation
and L2 Cauchy--Schwarz bound either second-derivative L1 norm by

\[
 \|u''\|_2\|w\|_2+2\|u'\|_2\|w'\|_2
                          +\|u\|_2\|w''\|_2\le4M0M1.
\]

Translations preserve each derivative norm. Hence, uniformly in a
and both signs of t, each pairing has modulus at most 4M0M1/T^2.
With C_prime(L)=2 sum_(2<=n<e^L) Lambda(n)/sqrt(n), finite summation
and the contraction norm of each delay now give

\[
 |\langle B_Lu,f\rangle|\le C_{\rm prime}(L)\frac{4M0M1}{T^2},
 \qquad \|B_L\|\le C_{\rm prime}(L).                         \tag{9}
\]

No cell boundary or shifted overlap boundary contributes: the products
used above are full-line smooth zero extensions. A delay at L is
zero; including it would not change a pairing.

Import C744n(4)-(5)'s correction bound, valid before choosing K(t):
define

\[
 H=\|G^{-1}\|(\|b_+\|_{H^2}^2+\|b_-\|_{H^2}^2)^{1/2}
                  \sqrt{33\ell e^\ell/8}\,M1.
\]

Then ||h||_(H2)<=H/T^2, independently of K and w. No reproof or
profile-dependent small-o assertion is needed. L744(13) also records
W(xi)<=(A+3)(1+xi^2), so weighted Cauchy--Schwarz and Plancherel give

\[
 |Q_m(u,h)|\le(A+3)\|u\|_{H^1}\|h\|_{H^1}
                          \le\frac{(A+3)M0H}{T^2},\qquad
 |\langle B_Lu,h\rangle|\le C_{\rm prime}(L)\frac{H}{T^2}.
                                                               \tag{10}
\]

The second estimate uses ||u||_2=1. This retains the entire correction
in both parts of (4), including the arithmetic factor.

### Growing window, explicit bound and qualifications

C744n(7)-(8) import Rosser--Schoenfeld, *Approximate formulas for some
functions of prime numbers*, Illinois J. Math. 6(1) (1962), 64-94,
[Theorem 12, (3.35), p.71](https://doi.org/10.1215/ijm/1255631807):
psi(x)<c x for x>0, c=1.03883. Its finite Abel-summation specialization
already proves

\[
 C_{\rm prime}(L)\le4c e^{L/2}.
                                                               \tag{11}
\]

This is the entire nonnegative prime-power mass, with the factor two
and the strict cutoff included. We reuse that result, not a prime-only
replacement or a new arithmetic estimate. With the prescribed K(t),
L(t)<=log log T, and thus C_prime(L(t))<=4c sqrt(log T). If T>=e^3,
then log log T>=log3=2ell and K(t)>=2. Combining (4), (8)-(11) gives

\[
 |\mathcal E_{L(t)}(u,v)|\le\frac1{T^2}\left\{
 4M0M1[A+\log(2+T/2)]+(A+3)M0H
             +4c\sqrt{\log T}(4M0M1+H)\right\}.             \tag{12}
\]

For T>=e^3>4, log(2+T/2)<=log T, log T>=3 and
sqrt(log T)<=log T. One admissible constant in (3) is therefore

\[
 C=4M0M1(1+A/3)+(A+3)M0H/3+4c(4M0M1+H).
\]

All estimates preceded the K(t) substitution, so no fixed-window
asymptotic has been substituted outside its quantifiers. Both complex
profiles can vary with t; all carrier estimates depend only on |t|.
The test's required O_(M0,M1,chi)(T^-2 log T) rate is attained.

This pays one signed low/high interaction. It supplies no independent
lower margin for E_L(u), no density or general decomposition theorem,
no many-interaction summation bound and no non-neutral complement
sign. The central actual-Xi positivity gap remains open. L742's
summability, L750's corrected-IMS and L745's general-sign scope stops
are not removed. No RH counterexample or complete solution is claimed.

### Separate conceptual audit (11 November 2026, step502)

**Verdict and scope.** Assertions (1)-(12), including the explicit
constant following (12), pass without a mathematical repair. This
REPRODUCTION audit uses the prior SPECIALIZE assessment
`drafts/literature/2026-11-11-growing-window-mixed-audit-500.md`.
The named Fourier and arithmetic theorems and L744's specialized
digamma bound are imported with their citations above. The checks
below verify this two-profile application, not those source theorems
anew. This validates a local input; it is not a discovery beyond the
sources checked or a positivity proof.

**Domain, Hermitian convention and exact moments.** For each finite
K, the union of the finitely many compact cell supports is compact
in (0,L). Each zero extension and each finite complex linear
combination is smooth. L744's domain argument and identity (6) apply
to this entire smooth vector space, not just its unit-norm or neutral
subset. They therefore apply to the combinations used in polarization.
For a first-slot-linear Hermitian form H with diagonal q,

\[
 H(a,b)=\tfrac14\{q(a+b)-q(a-b)
                   +i[q(a+ib)-q(a-ib)]\}.
\]

The form (2) is Hermitian, since conjugate symmetry of the original
inner product interchanges its two terms. The scalar form in (4) is
Hermitian because m is real; the arithmetic form is Hermitian because
B_L is self-adjoint. The two displayed pole products together are
Hermitian and have diagonal 2 Re(F_a(i/2) overline(F_a(-i/2))).
Thus their diagonals equal L744(6), and the identity just displayed
verifies all conjugations and the sign of (4).

For a cell j, G(G^-1 d_j)=d_j uses the complex-linear inverse, with
no conjugation of the data. It makes each local moment of v zero.
Hypothesis (1) does the same for u. Global Fourier evaluations at
sigma i/2 are the corresponding finite sums with weights
e^(sigma j ell/2). Hence every such evaluation is exactly zero;
there is no residual amplified by the growing window. In particular
both products in (4) vanish. The proof never estimates the two poles
separately after expanding v=f-h or replaces them by modulus squares.

**Global Fourier overlap.** Smooth zero extensions satisfy the
inspected Vasy differentiation and Plancherel hypotheses. Their
derivatives through order two give precisely p(s)=1+s^2+s^4 in
(6), with measure dxi/(2pi). If r=max(|xi|,|xi-t|), one factor in
sqrt(p(xi)p(xi-t)) is at least r^2 and the other is at least one.
For either sign of t, T<=|xi|+|xi-t|<=2r. Since |xi|<=r, the
global L744(8) majorant yields the first inequality in (7).
Direct differentiation gives

\[
 \frac{d}{dr}\frac{A+\log(2+r)}{r^2}
 =\frac{r/(2+r)-2A-2\log(2+r)}{r^3}<0\quad(r\ge1).
\]

This verifies its second inequality for every real xi, including
xi near either 0 or t and arbitrarily far tails. Multiplying by the
two p-weighted Fourier absolute values, then applying Cauchy--Schwarz
with the translation eta=xi-t, gives (8). Both squared integrals
are bounded by M0^2 and M1^2. No support measure, disjointness,
unspecified Schwartz seminorm or higher derivative enters the bound.
The same argument establishes absolute integrability of this mixed
integrand, in addition to the individual smoothness argument in (4).

**Truncated shifts and their adjoints.** For x in (0,L), the delay
is u(x-a), with its zero extension enforcing x>a; its adjoint is
u(x+a), with that extension enforcing x+a<L. Pairing with w and
extending the integral to the full line therefore gives both formulas
above (9). For either sign choice, set
P_a(x)=u(x +/- a) overline(w(x)). Its second derivative is
u''(x +/- a) overline(w(x))+2u'(x +/- a) overline(w'(x))
+u(x +/- a) overline(w''(x)). The product is globally smooth and
compactly supported; two integrations by parts against e^(-itx)
give an absolute bound T^-2 ||P_a''||_1 without boundary terms.
Translation invariance of the full-line L2 norms and three
Cauchy--Schwarz inequalities give ||P_a''||_1<=4M0M1.
This holds simultaneously for all a, even when shifted cell endpoints
meet. There is no differentiation of a discontinuous cutoff.

Each coefficient Lambda(n)/sqrt(n) in B_L is nonnegative. Summing
the two delay bounds thus gives C_prime(L)*4M0M1/T^2, with exactly
the factor two in C_prime. The same delays are contractions, so their
operator-norm sum is at most C_prime(L). This verifies both parts of
(9), including every prime power and the vanishing delay operator at a=L.

**Entire correction and parameter dependence.** C744n(4)-(5) gives
||h||_(H2)<=H/T^2 with the H stated here after substituting M=M1.
Its proof sums squared cell norms, not their absolute norms, so no
factor K or sqrt(K) is hidden. That estimate holds for all T>0;
C744n's additional denominator onset T_0 is not required here.
The present proof never divides by ||v||, assumes v is nonzero,
or squares a possibly negative lower bound for that norm.

The scalar inequality |m|<=W<=(A+3)(1+xi^2), followed by weighted
Cauchy--Schwarz and Plancherel, bounds |Q_m(u,h)| by
(A+3)||u||_(H1)||h||_(H1)<=(A+3)M0H/T^2. The arithmetic term
is at most ||B_L|| ||u||_2 ||h||_2<=C_prime(L)H/T^2.
This checks (10), including the unit normalization of u and the
full arithmetic cost of h. The correction is not suppressed on
the ground that its unweighted norm is small.

**Floor, prime mass and explicit constant.** C744n(7)-(8) applies
the cited Rosser--Schoenfeld theorem to the inclusive prime-power
sum and gives at most 2c sqrt(X)-c before the factor two, for
X=e^L. Positivity of its coefficients bounds the strict sum by
that inclusive sum. Consequently C_prime(L)<=4c e^(L/2),
as required in (11), independently of how close X is to an integer.
For every T>=e^3, log log T>=log3=2ell, so the prescribed floor
gives K>=2 and L<=log log T. Substituting this in (11) gives
C_prime(L)<=4c sqrt(log T). No limit in K is taken.

Taking absolute values in the four remaining pairings of (4)
adds respectively the bounds (8), the scalar part of (10), the
first part of (9), and the arithmetic part of (10). This is exactly
(12), including the factor (4M0M1+H) multiplying the full prime mass.
Since T>=e^3>4, one has 2+T/2<=T, log T>=3 and
sqrt(log T)<=log T. Term by term the numerator of (12) is at most

\[
 \bigl[4M0M1(1+A/3)+(A+3)M0H/3
                         +4c(4M0M1+H)\bigr]\log T.
\]

This checks the advertised C and proves (3) at its stated threshold,
without an implicit profile-dependent onset. All support-dependent
operations were finite identities; all quantitative constants depend
only on M0,M1,chi and the fixed ell. Neither t-sign nor a varying
choice of the two profiles changes any of these checks.

**Use and limitations.** C744o is now available as this single full
complex interaction estimate. Its only direct local mathematical
inputs remain L744 and C744n. No low-block lower bound, positive
complement, collective carrier estimate, density assertion or
all-window sign follows from the audit. The L742, L750 and L745
scope stops remain unchanged. Full matching Mathlib coverage has
not been checked; no numerical or formal verification is claimed.

## Mathlib

Full matching Mathlib coverage is not checked. Plancherel, Fourier
differentiation and integration by parts are standard supporting
results, but their use here is not a verified formalization of this
complete generator, correction family or uniform mixed estimate.
No absence claim or formal proof claim is made.
