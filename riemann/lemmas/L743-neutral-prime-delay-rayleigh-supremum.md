# L743: Cellwise neutrality preserves the finite prime-delay Rayleigh supremum

## Hypotheses

Fix an integer \(K\ge2\), put \(\ell=\log(3)/2\) and \(L=K\ell\),
and use the original complex space \(X=L^2((0,L),dx)\), with inner
product linear in the first argument. All tests are extended by zero.
Use precisely L740's finite arithmetic delays, restated as

\[
 (T_a u)(x)=\mathbf1_{x>a}u(x-a),\qquad
 a_n=\frac{\Lambda(n)}{\sqrt n},\qquad
 B_L=\sum_{2\le n<e^L}a_n(T_{\log n}+T_{\log n}^*).       \tag{1}
\]

Thus \(B_L=(P_L+P_L^*)/2\), where \(P_L\) is L740's arithmetic
term. This notation \(B_L\) denotes only (1), not the auxiliary
continuous-plus-arithmetic perturbation called \(B_L\) in L740's proof.
Every contributing prime power is retained. A delay \(a=L\) is zero.
Here \(\Lambda(p^r)=\log p\), and \(\Lambda(n)=0\) otherwise.

Use only the definition of the neutral space in L742 (2):

\[
 \mathcal N=\left\{f\in C_c^\infty(0,\ell):
     \int_0^\ell e^{s/2}f(s)\,ds
       =\int_0^\ell e^{-s/2}f(s)\,ds=0\right\},
 \quad
 \mathcal U_K=\left\{\sum_{j=0}^{K-1}f_j(x-j\ell):
                              f_j\in\mathcal N\right\}.  \tag{2}
\]

Functions and moment constraints may be complex. No RH assumption,
conditional conclusion of L742, positive spectral measure or source
positivity computation is used.

The external imports are:

- **Dirichlet's simultaneous approximation theorem**: for a finite
  list \(\theta_1,\ldots,\theta_d\) of real numbers, one has positive
  integer simultaneous denominators with errors tending to zero.
  Precisely, for every integer \(M>1\), there is \(0<m<M\) with
  \(\max_\nu\|m\theta_\nu\|_{\mathbb R/\mathbb Z}
  \le M^{-1/d}\). See Pete L. Clark,
  *Geometry of Numbers with Applications to Number Theory*,
  [author-hosted PDF](https://plclark.github.io/PeteLClark/Expositions/geometryofnumbers.pdf),
  Theorem 13.3 and Corollary 13.4, printed p.72, 159-page version
  inspected on 4 November 2026. No rational-independence hypothesis
  is required. The theorem is imported, not its Minkowski proof.
- The standard named **Riemann–Lebesgue lemma**: if \(h\in L^1(\mathbb R)\),
  then \(\int h(s)e^{its}ds\to0\) as \(|t|\to\infty\).
  The proof below checks this hypothesis for each use.

## Conclusion

For every fixed \(K\) as above,

\[
 \boxed{\quad
 \sup_{0\ne u\in\mathcal U_K}
       \frac{\langle B_Lu,u\rangle}{\|u\|_2^2}
 =
 \sup_{0\ne u\in C_c^\infty(0,L)}
       \frac{\langle B_Lu,u\rangle}{\|u\|_2^2}.
 \quad}                                                   \tag{3}
\]

This is an unconditional equality for the complete finite arithmetic
operator in the unweighted norm. It gives no value or attained maximizer
for either supremum, no estimate uniform in \(K\), and no preservation
of the complete energy under modulation.

The proof is a standard-mechanism specialization/REPRODUCTION under the
prior EXPLORE assessment, not a certified originality claim. The separate
audit in step 285 below accepts (3) within its scope. Its negative relevance is precise:
these exact moments alone cannot strictly improve this prime-only
upper Rayleigh bound. L741's energy norm and L742's energy-normalized
couplings remain different questions.

## Proof

### 1. Bounded form and the cell-interior core

For \(0<a<L\), substitution in the inner product gives

\[
 (T_a^*u)(x)=\mathbf1_{x<L-a}u(x+a),\qquad
 \|T_a\|,\|T_a^*\|\le1.
\]

For \(a\ge L\) both operators are zero. Thus \(B_L\) is bounded
self-adjoint, with

\[
 \|B_L\|\le C_L:=2\sum_{2\le n<e^L}a_n<\infty.             \tag{4}
\]

Set \(q(u)=\langle B_Lu,u\rangle\), a real number. For any \(u,v\in X\),

\[
 |q(u)-q(v)|\le C_L\|u-v\|_2(\|u\|_2+\|v\|_2).           \tag{5}
\]

Let \(\mathcal C_K\) consist of finite sums
\(\sum_j w_j(x-j\ell)\) with \(w_j\in C_c^\infty(0,\ell)\),
without moment constraints. It is contained in \(C_c^\infty(0,L)\):
each summand vanishes in a neighborhood of its cell endpoints.

For any \(v\in C_c^\infty(0,L)\), choose smooth cell cutoffs
\(0\le\chi_{j,r}\le1\), compactly supported in
\((j\ell,(j+1)\ell)\), tending pointwise to one in that open cell.
Then
\(v_r=v\sum_{j=0}^{K-1}\chi_{j,r}\in\mathcal C_K\).
The sum of these cutoffs is at most one. Except at the finitely
many cell endpoints, \(v_r\to v\); dominated convergence applied
to \(|v_r-v|^2\le |v|^2\) gives \(v_r\to v\) in \(L^2\).
If \(v\ne0\), then \(v_r\ne0\) eventually. Equation (5) and
convergence of the norms give convergence of their Rayleigh values.
Consequently the right side of (3) also equals

\[
 S_{\mathcal C}:=\sup_{0\ne w\in\mathcal C_K}
                           \frac{q(w)}{\|w\|_2^2}.        \tag{6}
\]

This is density of the unconstrained cell-interior core. It is not
an assertion that the neutral subspace is dense in \(L^2\).

### 2. Arbitrarily large simultaneous returns for every delay

List the finitely many integers \(2\le n<e^L\), including those with
zero coefficient if desired. The list is nonempty since \(K\ge2\).
Apply Dirichlet's theorem to
\(\theta_n=\log n/(2\pi)\), taking integers \(M\to\infty\).
Obtain positive integers \(m_M<M\) whose simultaneous errors tend
to zero.

If the set of \(m_M\) is unbounded, select a subsequence with
\(m_{M_r}\to\infty\). Necessarily \(M_r\to\infty\), so its errors
still tend to zero. If it is bounded, some positive integer \(m_*\)
occurs for infinitely many \(M\). Along these \(M\),
\(\|m_*\theta_n\|\le M^{-1/d}\to0\); hence
\(m_*\theta_n\in\mathbb Z\) for every \(n\). Then \(r m_*\) are
arbitrarily large exact simultaneous returns. In either case there
is a sequence \(t_r\to+\infty\) such that

\[
 \max_{2\le n<e^L}|e^{it_r\log n}-1|\longrightarrow0.      \tag{7}
\]

The implication from approximation error to (7) uses
\(|e^{2\pi iz}-1|\le2\pi\|z\|_{\mathbb R/\mathbb Z}\).
This application supplies the unboundedness missing from the bare
existence of small denominators; it assumes no independence of
prime logarithms. L334 uses the same standard recurrence dichotomy
for a different arithmetic series. No new recurrence theorem or
result about that series is asserted or needed here.

Let \(M_tu(x)=e^{itx}u(x)\). This is unitary on the original \(X\);
direct substitution gives

\[
 M_t^*T_aM_t=e^{-ita}T_a,\qquad
 M_t^*T_a^*M_t=e^{ita}T_a^*.
\]

Therefore (4) and the finite sum imply

\[
 \eta_r:=\|M_{t_r}^*B_LM_{t_r}-B_L\|
 \le2\sum_{2\le n<e^L}a_n|e^{it_r\log n}-1|
 \longrightarrow0.                                      \tag{8}
\]

No delay is omitted, and no limit in \(K\) or infinite arithmetic
sum is taken. In particular
\(|q(M_{t_r}w)-q(w)|\le\eta_r\|w\|_2^2\).

### 3. A fixed exact smooth moment correction

Choose a real nonnegative \(\chi\in C_c^\infty(0,\ell)\) which
is positive on a nonempty open subinterval. For
\(\sigma,\tau\in\{+1,-1\}\), put

\[
 b_\tau(s)=\chi(s)e^{\tau s/2},\qquad
 G_{\sigma\tau}=\int_0^\ell
                      \chi(s)e^{(\sigma+\tau)s/2}\,ds.    \tag{9}
\]

The real symmetric matrix \(G\) is positive definite. Indeed, for
complex numbers \(c_+,c_-\),

\[
 c^*Gc=\int_0^\ell\chi(s)
             |c_+e^{s/2}+c_-e^{-s/2}|^2ds.
\]

If this vanishes, continuity forces the expression in absolute
value to vanish on the interval where \(\chi>0\). Multiplying by
\(e^{s/2}\) gives \(c_+e^s+c_-=0\) there. Differentiation yields
\(c_+=0\), then \(c_-=0\). Hence \(G\) is invertible.

For every \(d=(d_+,d_-)\in\mathbb C^2\), the function
\(h_d=\sum_\tau (G^{-1}d)_\tau b_\tau\) is in
\(C_c^\infty(0,\ell)\), has moments
\(\int e^{\sigma s/2}h_d(s)ds=d_\sigma\) exactly, and obeys

\[
 \|h_d\|_2\le C_\chi |d|,\qquad
 C_\chi=\|G^{-1}\|_{\mathbb C^2\to\mathbb C^2}
                     (\|b_+\|_2^2+\|b_-\|_2^2)^{1/2}<\infty. \tag{10}
\]

This explicitly supplies a right inverse with fixed smooth supports.
It is not just asymptotic satisfaction of the constraints.

### 4. Correct the modulated cells and pass to the Rayleigh value

Fix a nonzero \(w\in\mathcal C_K\), normalize \(\|w\|_2=1\),
and write \(w(x)=\sum_j w_j(x-j\ell)\). On cell \(j\) the
modulated profile is \(e^{it_r(s+j\ell)}w_j(s)\). Its two moments are

\[
 d_{j,\sigma,r}
  =e^{it_rj\ell}\int_0^\ell
                  e^{\sigma s/2}w_j(s)e^{it_rs}\,ds.      \tag{11}
\]

The zero extension of \(e^{\sigma s/2}w_j(s)\) is in
\(L^1(\mathbb R)\), since it is smooth with compact support.
Riemann–Lebesgue and \(|e^{it_rj\ell}|=1\) imply
\(d_{j,\sigma,r}\to0\) for both signs and every one of the finitely
many cells.

Use (10) to form \(h_{j,r}=h_{d_{j,\cdot,r}}\), and set

\[
 h_r(x)=\sum_{j=0}^{K-1}h_{j,r}(x-j\ell),\qquad
 u_r=M_{t_r}w-h_r.
\]

Each cell of \(u_r\) is smooth, compactly supported in its interior,
and has exactly zero moments by (9)--(11). Thus
\(u_r\in\mathcal U_K\). The equivalent moments using \(e^{\sigma x/2}\)
on cell \(j\) also vanish, because the local moments differ by the
nonzero factor \(e^{\sigma j\ell/2}\).

Disjoint cell supports and (10) give

\[
 \delta_r^2:=\|h_r\|_2^2
   =\sum_j\|h_{j,r}\|_2^2
   \le C_\chi^2\sum_j|d_{j,\cdot,r}|^2\longrightarrow0.    \tag{12}
\]

Since \(\|M_{t_r}w\|_2=1\), one has
\(\|u_r\|_2\ge1-\delta_r>0\) eventually and
\(|\|u_r\|_2^2-1|\le2\delta_r+\delta_r^2\).
Equations (5) and (8) give

\[
 |q(u_r)-q(w)|
 \le \eta_r+C_L(2\delta_r+\delta_r^2).
\]

In particular, for \(\delta_r<1\), the following explicit error
bound checks both numerator and denominator:

\[
 \left|\frac{q(u_r)}{\|u_r\|_2^2}-q(w)\right|
 \le
 \frac{\eta_r+2C_L(2\delta_r+\delta_r^2)}
      {(1-\delta_r)^2}\longrightarrow0.                  \tag{13}
\]

Thus every Rayleigh value of \(\mathcal C_K\) is a limit of values
of nonzero, exactly neutral smooth tests. The supremum over
\(\mathcal U_K\) is at least \(S_{\mathcal C}\). The reverse
inequality follows from
\(\mathcal U_K\subset C_c^\infty(0,L)\) and (6). This proves (3).
No existence of an extremizer is assumed.

### Qualifications and downstream use

The achieved threshold is equality, not merely an inconclusive upper
bound. It stops an improvement of this particular prime-only
\(L^2\) Rayleigh supremum based solely on the cell moments.
It does not stop estimates coupling arithmetic to the archimedean
energy: (8) controls only \(B_L\), and the unitary identity for
the unweighted norm gives no bound for the logarithmic Fourier
weight in the complete energy. No energy-normalized equality or
complete-form sign follows. Moment complements, adjacent and global
signed interactions, and actual-Xi mixed positivity remain open.

The local duplicate check distinguishes L730's density theorem for
unbounded arithmetic moment functionals on a different space.
The present bounded exponential constraints need not have dense kernel;
the proof instead preserves one bounded quadratic value under recurrence.
Only the identified operator-and-exact-correction specialization is
proved. Dirichlet and Riemann–Lebesgue are imported rather than reproved.

### Separate proof audit (4 November 2026, step 285)

The unchanged fixed-K statement (3) passes this replay. Only L740 (4)'s
delays and L742 (2)'s definition are mathematical inputs from those files;
in particular L742's RH hypothesis is not imported.

1. **Complete operator and conjugations.** L740 has
   \(P_L=2\sum a_nT_{\log n}\), so (1) is exactly
   \((P_L+P_L^*)/2\). Changing variables in
   \(\int_a^L u(x-a)\overline{v(x)}dx\) gives the stated adjoint
   with no boundary term. Zero extension makes the endpoint delay zero.
   All coefficients are real nonnegative, so (4) bounds both the
   self-adjoint form and its absolute Rayleigh values. With the inner
   product linear in its first argument, unitary conjugation gives
   precisely the two opposite phases in (8); neither is a complex
   bilinear pairing or a discarded prime power.

2. **Core and order of limits.** The cell cutoffs have disjoint open
   supports. Their sum lies in [0,1], so dominated convergence applies
   even when the original test is nonzero at cell boundaries, a finite
   null set. Equation (5) and norm convergence justify (6). First fix a
   nonzero core test and K; only then take the modulation limit. Taking
   the supremum afterwards requires no uniformity over tests, maximizing
   vector or K-limit.

3. **Unbounded returns.** The delay list is finite and nonempty since
   \(e^L=3^{K/2}\ge3\). Unbounded selected denominators force their
   M's to infinity. Otherwise one positive denominator occurs for
   unbounded M and is an exact return for every phase; its multiples
   tend to infinity. These cases exhaust the imported Dirichlet
   conclusion and justify using Riemann–Lebesgue along (7). Finiteness
   of the delay list then gives operator-norm convergence in (8).

4. **Exact complex moment correction.** Matrix (9) is real symmetric
   positive definite also on complex vectors, by its displayed integral.
   Its inverse supplies a complex-linear right inverse to the two
   integrals, which have no conjugation on the test function.
   Cauchy–Schwarz on the two coefficients gives (10). Each integrand in
   (11), extended by zero, is compactly supported and L1. Both moments
   therefore tend to zero despite the cell phase, whose modulus is one.
   Finite K and disjoint supports give (12). Correction preserves smooth
   compact support in every cell and kills the moments exactly.

5. **Normalization and both supremum inequalities.** Set
   \(a_r=\|u_r\|_2^2\). The reverse triangle inequality gives
   \(a_r\ge(1-\delta_r)^2\), while
   \(|a_r-1|\le2\delta_r+\delta_r^2\). Since \(|q(w)|\le C_L\),
   the identity
   \(q(u_r)/a_r-q(w)=[q(u_r)-q(w)+(1-a_r)q(w)]/a_r\)
   gives (13), including its factor 2. Corrected tests are nonzero
   eventually. Their quotients approach each normalized core quotient,
   proving one supremum inequality; inclusion proves the reverse.

No defect or additional hypothesis was found. This audit verifies the
local standard-mechanism specialization, not a new theorem beyond the
sources checked or a source-proof/computation replay. It certifies only
the prime-only, unweighted, fixed-K obstruction. The logarithmic Fourier
cost of the complete energy is neither bounded nor preserved by this
argument, so no energy-normalized equality, all-window sign or RH
conclusion follows. Full matching Mathlib coverage remains unchecked.

## Mathlib

Full matching Mathlib coverage of (3) has not been checked. The prior
assessment does not identify such a theorem; this is not evidence of
absence. No formal verification is claimed. The proof uses the named
simultaneous approximation and Riemann–Lebesgue inputs with their
explicit hypotheses, and gives the finite-window, smooth correction
and Rayleigh-limit details above.
