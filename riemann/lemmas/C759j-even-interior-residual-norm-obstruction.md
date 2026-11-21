# C759j: Concentration obstructs unrestricted interior residual control

## Hypotheses

Use exactly C759a(1),(5)-(6) and C759h Proof1-2: the complete closed
Weil form on real L2(-1,1), zero extension to the line, restricted to
the even subspace. Let A_e be its self-adjoint form operator. Retain
both poles and every shift n=2,3,4,5,7, with a_n=Lambda(n)/sqrt(n).
No neutrality, spectral projection, eigenfunction sign or spectral
gap beyond C759h's established floor is assumed. Put

\[
 h(s)=(\max\{1-s^2,0\})^2,\qquad
 f_\varepsilon(x)=h(x/\varepsilon),\qquad 0<\varepsilon<1/8.
\]

The Fourier convention is F_f(t)=integral f(x)exp(-itx)dx, with
Plancherel measure dt/(2pi). The primary standard Fourier inputs are
Gerald Teschl, *Mathematical Methods in Quantum Mechanics*, second
edition (2014), GSM157, Section7.1, equation7.3, Theorem7.5 and
Lemma7.6, printed pp187-190,
[author-hosted primary text](https://www.mat.univie.ac.at/~gerald/ftp/book-schroe/schroe2.pdf).
These give the L2 extension and its agreement with the integral on
L1 intersect L2. The unitary convention there is converted by the
factor sqrt(2pi). Its Schwartz-only derivative/dilation lemmas are
not assumed to apply to h: the needed identities are justified below.

## Conclusion

Each f_epsilon lies in D(A_e), and

\[
 \|f_\varepsilon\|_{L^\infty(-1/4,1/4)}=1,\qquad
 0<\|(A_e+16I)f_\varepsilon\|_2
 \le\sqrt\varepsilon\bigl(\log(1/\varepsilon)+40\bigr).
 \tag{1}
\]

Consequently the ratio in the approved test tends to infinity as
epsilon decreases to zero. In particular there is no finite constant
M such that, for every real even f in D(A_e),

\[
 \|f\|_{L^\infty(-1/4,1/4)}\le M\|(A_e+16I)f\|_2.       \tag{2}
\]

This is an obstruction to the unrestricted residual norm conversion,
not to ground-state sign/simplicity, a conversion on a restricted
spectral or error class, stronger residual norms, or RH. No endpoint
weight or eigenfunction enclosure is certified. This is an ordinary
REPRODUCTION/specialization of Fourier tools to the complete local
operator; neither originality nor progress beyond known general
embedding theory is claimed. The independent audit in Proof4 accepts
this scoped obstruction; it supplies no additional sign conclusion.

## Proof

### 1. Domain, normalization and the complete action

The zero-extended h is C1: its polynomial value and first derivative
both vanish at +/-1. Its weak first derivative equals -4s+4s^3 on
(-1,1), and is zero outside. Thus f_epsilon is even, C1 and supported
on [-epsilon,epsilon], and belongs to H1_0(-1,1). C759h Proof2
therefore puts it in D(A_e) with the actual compressed action

\[
 A_ef=(m(D)f_0)|_{(-1,1)}+2c\langle c,f\rangle
 -\sum_{n=2,3,4,5,7}a_n
       [f_0(\cdot+\log n)+f_0(\cdot-\log n)],
 \quad c(x)=\cosh(x/2).                                  \tag{3}
\]

Here f_0 denotes zero extension; the multiplier acts on the full line
before restriction. No periodic or Dirichlet multiplier is substituted.
The rank-one term represents both poles: on the even space both
functionals F_f(i/2),F_f(-i/2) equal <c,f>.

Direct polynomial integration gives

\[
 \|h\|_1=16/15,\qquad
 H_0^2:=\|h\|_2^2
 =2(1-4/3+6/5-4/7+1/9)=256/315<1,
 \quad\|f_\varepsilon\|_2=\sqrt\varepsilon H_0.           \tag{4}
\]

The continuous bump has maximum1 at zero and approaches that maximum
on sets of positive measure, proving its essential supremum assertion.

### 2. Full Fourier tail for the non-Schwartz trial

Let H(u)=integral h(s)exp(-ius)ds. Since h is integrable, substitution
in this integral gives exactly

\[
 F_{f_\varepsilon}(t)=\varepsilon H(\varepsilon t).       \tag{5}
\]

Lemma7.6 makes this also the L2 transform identity. For u!=0,
integration by parts twice on [-1,1] has no boundary terms, because
h and h' vanish at both endpoints. Hence

\[
 H(u)=-u^{-2}\int_{-1}^1(-4+12s^2)e^{-ius}ds,
 \qquad |H(u)|\le\min\{16/15,16/u^2\}.                 \tag{6}
\]

Indeed integral(4+12s^2)ds=16. This argument uses the actual
piecewise polynomial and does not invoke a Schwartz derivative rule.
Its weak second derivative is the displayed bounded polynomial inside
the interval and zero outside; no endpoint delta terms occur since
h' is continuous there.

Put ell(u)=log(1+u^2)/2 and define

\[
 K^2=\int_{\mathbb R}\ell(u)^2|H(u)|^2\frac{du}{2\pi}.
\]

On |u|<=1, ell(u)<=1; on |u|>=1, ell(u)<=log|u|+1.
Using (6) on the two entire regions gives

\[
 \begin{split}
 K^2&\le\frac{256}{\pi}
 \left(\frac1{225}+\int_1^\infty
             \frac{(\log u+1)^2}{u^4}\,du\right)\\
 &=\frac{256}{\pi}\left(\frac1{225}+\frac{17}{27}\right)
 <\frac{109568}{2025}<64.                                \tag{7}
 \end{split}
\]

The tail integral is complete: putting v=log u changes it to
integral_0^infinity (v+1)^2 exp(-3v)dv=2/27+2/9+1/3=17/27,
by integration by parts. The strict inequality uses pi>3.
In particular K<8. No low-frequency region, high-frequency remainder
or sampled tail is suppressed.

### 3. Logarithmic scaling and every bounded perturbation

C759a(5) gives, on the full real axis,

\[
 m(t)=\ell(t)-\log(2\pi)-\Re\widehat r(it),\qquad
 \|r\|_1\le\log2+4,
 \quad |m(t)|\le\ell(t)+B,
 \quad B=\log(4\pi)+4<7.                                \tag{8}
\]

For example pi<4 and log2<7/10 imply B<34/5<7, as in
C759h Proof1. For 0<epsilon<1 set L=log(1/epsilon)>0. Then

\[
 \ell(u/\varepsilon)\le L+\ell(u),
\]

because epsilon^2+u^2<=1+u^2. Plancherel, (5), a change of variable
u=epsilon t and the L2 triangle inequality therefore give

\[
 \begin{split}
 \|m(D)(f_\varepsilon)_0\|_{L^2(\mathbb R)}
 &=\sqrt\varepsilon\left(
     \int|m(u/\varepsilon)H(u)|^2\frac{du}{2\pi}
                                  \right)^{1/2}\\
 &\le\sqrt\varepsilon\bigl((L+B)H_0+K\bigr).
                                                               \tag{9}
 \end{split}
\]

Finiteness and every triangle inequality are justified by (4),(7);
this retains the transformed low-frequency part and the full tail.
Restriction to (-1,1) only decreases the L2 norm.

For the prime part of (3), C759a Proof3 and C759h Proof1 supply
the complete compressed-shift bound

\[
 \left\|\sum_{n=2,3,4,5,7}a_n
       [f_0(\cdot+\log n)+f_0(\cdot-\log n)]\right\|_{L^2(-1,1)}
 \le C\|f\|_2,
 \quad C=\sqrt2a_2+a_3+a_4+a_5+a_7<4.                  \tag{10}
\]

This bound uses the compressed shifts, as specified there. All five
remain included; displaced supports are not grounds to drop any term.
For the full even pole operator Cauchy--Schwarz gives

\[
 \|2c\langle c,f\rangle\|_2\le P\|f\|_2,
 \qquad P=2\|c\|_2^2=2(1+\sinh1)<5.                    \tag{11}
\]

The last bound follows already from e<3. Combining (3),(4),(9)-(11)
with the entire shift16 yields

\[
 \begin{split}
 \|(A_e+16I)f_\varepsilon\|_2
 &\le\sqrt\varepsilon\bigl((L+B+16+C+P)H_0+K\bigr)\\
 &<\sqrt\varepsilon\bigl((L+32)H_0+8\bigr)
 <\sqrt\varepsilon(L+40).
 \end{split}                                                \tag{12}
\]

Finally C759h's full spectral floor A_e>=-10I gives
||(A_e+16I)f_epsilon||_2>=6||f_epsilon||_2>0. For instance this
follows by pairing with f_epsilon and Cauchy--Schwarz. Thus division
is legitimate. The ratio is at least
1/[sqrt(epsilon)(log(1/epsilon)+40)], which tends to infinity.
Applying a hypothetical (2) to these domain elements contradicts this
limit. Only the stated unrestricted conversion is excluded.

### 4. Independent audit833 — 13 November2026

The approved audit replays (1)-(12) against C759a(1),(5)-(6),
Proof1/3 and C759h Proof1-2, reusing assessment831's primary Fourier
coverage. It finds no mathematical fault. In particular:

* The derivative -4s+4s^3 vanishes at both endpoints, as does h.
  The zero extension has no jumps in either h or h'; its second
  distributional derivative is (-4+12s^2)1_{(-1,1)}. Thus both
  integrations by parts in (6) have zero boundary terms. The form
  realization and its even restriction are exactly C759a's, rather
  than a periodic or spectral-Dirichlet surrogate. In addition to
  C759h's H1_0 criterion, (7)-(9) directly show mF_f in L2. Pairing
  it with any form-domain g by Plancherel gives a bounded L2
  functional; the bounded perturbations give the full action (3).
  This independently verifies the representation-theorem domain
  condition for this family without applying a Schwartz derivative
  identity to it.
* Integral substitution gives (5) for all real t. Plancherel is used
  with dt/(2pi), so its change of variable gives sqrt(epsilon),
  not epsilon, in (9). Direct integration verifies all three
  constants in (4). The low part of K^2 is at most
  256/(225pi); the two tails together contribute at most
  (256/pi)(17/27). The tail moment is
  1/3+2/9+2/27=17/27, and
  (256/3)(1/225+17/27)=109568/2025<64.
  Thus the K<8 bound includes both infinite tails and the whole
  central interval. The inequality ell(u/epsilon)<=L+ell(u)
  is pointwise, including u=0, so the triangle inequality in (9)
  involves finite L2 quantities on the entire line.
* For completeness, C<16/5 can be checked without the unrelated
  numerical certificate in C759a. Since Lambda(4)=log2, its sum is
  C=(3/2)log2+log3/sqrt3+log5/sqrt5+log7/sqrt7.
  Positive exponential-series partial sums give

  \[
  \begin{array}{c|c|c}
  q&N&\sum_{k=0}^N q^k/k!\\\hline
  7/10&4&482921/240000>2\\
  11/10&5&36015101/12000000>3\\
  33/20&5&661847831/128000000>5\\
  39/20&7&5033451128491/716800000000>7
  \end{array}
  \]

  Hence log2<7/10, log3<11/10, log5<33/20 and log7<39/20.
  Squaring verifies sqrt3>17/10, sqrt5>11/5 and sqrt7>13/5.
  Therefore

  \[
   C<21/20+11/17+3/4+3/4=1087/340<16/5<4.
  \]

  C759a's fiber proof applies to all five compressed shifts:
  2log2<2<3log2, whereas 1<log n<2 for n=3,4,5,7.
  Each three-coordinate path has norm at most sqrt2, each
  two-coordinate path at most1. These are full-space bounds,
  valid on the invariant even subspace; no commutation of different
  shifts or deletion of a displaced bump is used.
* The odd sinh functional vanishes for even f, so both poles give
  exactly 2c<c,f>. Integrating c^2 gives ||c||^2=1+sinh1;
  e<3 implies sinh1<3/2 and P<5. The complete shift16 and all
  bounded terms are consequently present in (12).
  The elementary bounds pi<4 and log2<7/10 give B<34/5<7;
  B+16+C+P<32, H0<1, K<8 prove (12) as stated.
* The same independent C bound also pays the denominator without
  appealing to a sampled spectrum: m_*>-34/5 and C<16/5 imply
  Q(f)>-10||f||^2 for nonzero even form-domain f, since its pole
  term is nonnegative. The weaker closed inequality A_e>=-10I
  follows. For this nonzero domain element,
  <(A_e+16I)f,f>>=6||f||^2; Cauchy--Schwarz gives the strictly
  positive lower bound in Proof3. Finally, putting L=log(1/epsilon)
  makes the upper residual bound e^(-L/2)(L+40), which tends to0.
  Its reciprocal diverges. No lower bound on the actual residual
  rate, or inference about a restricted error class, is needed.

Verdict: domain membership and estimate (1) hold with their stated
hypotheses; the universal bound (2) is impossible. This completes
verification of the existing REPRODUCTION, not a new concentration
result or progress beyond the sources compared. Ground-state
sign/simplicity, full lowest-even isolation, parity, bounded-residual
conversion and actual-Xi realization remain unresolved. The stopped
unrestricted L2 conversion should not be repeated without a changed
error class or norm. No new dependency or computational spectrum is used.

## Mathlib

Full matching theorem and supporting Fourier/form-operator coverage
were not checked. No formalization or absence claim is made. Precise
standard imports and the reason for the actual-operator specialization
are given above; no general embedding theorem is reproved.
