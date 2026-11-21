# Corollary 466g: growing-order reciprocal-density boundary signs

## Hypotheses

Use C466a's actual density $p=\theta_1$, $c_0=\xi(1/2)>0$,
$h(z)=\xi(1/2+\sqrt z)/c_0$, $B(s)=\log h(s)$,
$x_s=B'(s)$, $v_s=-B''(s)$ and $\sigma_s=\sqrt{v_s}$, with
the completion conventions of L018. All logarithms below are natural.
Retain C466a's external density qualifications: the critical strip and
zero symmetries, paired Hadamard product, the stated counting estimate
$|N(Y)-M(Y)|\le\frac18\log(Y+2)+4$ for $Y\ge0$, where
$M(Y)=\frac{Y}{2\pi}(\log(Y/(2\pi))-1)$ for $Y>0$ and $M(0)=0$,
and the verified critical-line zeros through height 100, including
$14<\gamma_1<15$.
As in C466a, these are cited external inputs, not independently replayed
certificates. No RH, simplicity, or global PF assumption is made.

Precisely, the density input is Suvrit Sra, *On some positivity
properties of the Riemann Xi function*,
[version-specific primary text W_pr5z5huy_v1](https://hub.valency.io/works/W_pr5z5huy_v1),
Theorem 1.1, Lemma 2.4 and its Appendix B proof, and Corollary 2.5:
$p$ is a smooth probability density, zero on $(-\infty,0]$, strictly
positive on $(0,\infty)$, with Laplace transform $1/h$ on
$\operatorname{Re}z>0$. The proof uses only this input and C466a's
audited analytic estimates and identities. The later source
[arXiv:2611.02944v1](https://arxiv.org/html/2611.02944v1), Proposition
C.25, states a fixed-order boundary conclusion; it is not cited as
a growing-order theorem.

Write
\[
 d_m=m(m-1)/2,\qquad
 \mathcal D_m(p;x)=(-1)^{d_m}
       \det[p^{(i+j)}(x)]_{i,j=0}^{m-1}.
\]

## Conclusion

There is one constant $S>1$ such that for every real $s\ge S$ and
every integer $2\le m\le\lfloor(\log s)^{1/4}\rfloor$,
\[
 \left|\frac{\mathcal D_m(p;x_s)}
 {p(x_s)^m v_s^{-d_m}\prod_{j=0}^{m-1}j!}-1\right|
 \le \frac12.                                                    \tag{1}
\]
In particular $\mathcal D_m(p;x_s)>0$ throughout that range. The same
ratio statement holds for $\Theta=p/c_0$. The proof actually gives the
upper bound $\exp(2s^{-1/8})-1$ in (1) after increasing $S$.

The onset is existential, independent of both $m$ and the subsequently
chosen $s$; no numerical value is claimed. This is a quantitative
specialization of the assessed saddle method, not a claim of certified
originality. The proof was recorded in step908 and passed the separate
conceptual audit909 below. It gives neither a common boundary interval for all
orders nor global PF, contact signs, propagation, L030 positivity, or RH.

## Proof

### 1. Fixed analytic inputs with common constants

Set $\ell=\log s$, $\varepsilon_s=s^{-1/4}\ell^{-1/2}$ and
$A_s=s\sigma_s$. C466a's equations (1)--(2) and their Cauchy estimate
give, for one sufficiently large $s$-threshold,
\[
 v_s\sim \frac{\ell}{16s^{3/2}},\qquad
 A_s\sim \frac14 s^{1/4}\sqrt\ell,\qquad
 \sup_{|z-s|\le s/2}|B'''(z)|\le C_B s^{-5/2}\ell.                 \tag{2}
\]
Here and throughout, constants are independent of derivative order,
matrix size and $s$ above the fixed threshold. Only the third derivative
in (2) is used; no replacement of C466a's $O_j$ constants by a uniform
bound in $j$ is being made.

Use C466a's standardized tilted density
\[
 f_s(u)=e^{B(s)-su}p(u),\qquad
 g_s(z)=\sigma_s f_s(x_s+\sigma_s z),
\]
with characteristic function
\[
 \phi_s(t)=\exp\{B(s)-B(s-it/\sigma_s)-itx_s/\sigma_s\}.
\]
C466a's equation (6), before its final weakening, gives constants
$C_2,c>0$ with
\[
 |\phi_s(t)|\le C_2e^{-cF_s(t)},\qquad
 F_s(t)=\min\{t^2,A_s^{3/2}\sqrt{|t|}\}.                          \tag{3}
\]
All statements here are simultaneous for every real $t$ and sufficiently
large $s$. Weighted Fourier inversion is valid for every finite
derivative order by (3); we estimate its integrals directly rather than
apply fixed-order dominated convergence with a varying order.

### 2. Uniform weighted Fourier errors

Let $T=\ell$. Equation (2) implies $1\le T\le A_s/2$ eventually.
Taylor's formula along the complex segment from $s$ to
$s-it/\sigma_s$, for $|t|\le T$, and (2) give
\[
 B(s)-B(s-it/\sigma_s)-itx_s/\sigma_s
      =-t^2/2+\rho_s(t),\qquad
 |\rho_s(t)|\le C_3\varepsilon_s|t|^3.                            \tag{4}
\]
Indeed the Taylor remainder is at most
$|t|^3\sigma_s^{-3}\sup|B'''|/6$, and (2) bounds its coefficient
by $C_3s^{-1/4}\ell^{-1/2}$. The linear terms cancel exactly and
$B''(s)=-\sigma_s^2$ fixes the negative quadratic sign.
Since $\varepsilon_s T^3\to0$, increase the threshold so that
$|\rho_s(t)|\le1$ on this entire interval. Using
$|e^z-1|\le |z|e^{|z|}$, we obtain
\[
 |\phi_s(t)-e^{-t^2/2}|
       \le eC_3\varepsilon_s |t|^3e^{-t^2/2}\quad(|t|\le T).       \tag{5}
\]
For every integer $r\ge0$, its weighted integral is bounded by a
constant times $\varepsilon_s(r+3)!$, because
\[
 \int_{\mathbb R}|t|^{r+3}e^{-t^2/2}\,dt
 \le 2e^{1/2}\int_0^\infty t^{r+3}e^{-t}\,dt
 =2e^{1/2}(r+3)! .                                               \tag{6}
\]
The inequality follows from $t^2/2\ge t-1/2$ for $t\ge0$.

For $|t|\ge T$, both functions in the minimum defining $F_s$ are
increasing in $|t|$. Since $T\le A_s$, $F_s(T)=T^2$, and hence
$F_s(t)\ge T^2$. Also $T,A_s\ge1$ imply $F_s(t)\ge\sqrt{|t|}$
on this range. Splitting the exponent in half therefore gives
\[
 |\phi_s(t)|\le C_2e^{-cT^2/2}e^{-c\sqrt{|t|}/2}.
\]
The Gaussian satisfies
$e^{-t^2/2}\le e^{-T^2/4}e^{-\sqrt{|t|}/4}$ on the same range.
With $b=\min\{c/2,1/4\}>0$, the entire weighted tail difference is
at most
\[
 \begin{aligned}
 \int_{|t|>T}|t|^r|\phi_s(t)-e^{-t^2/2}|\,dt
 &\le (C_2+1)e^{-bT^2}
                 \int_{\mathbb R}|t|^r e^{-b\sqrt{|t|}}\,dt\\
 &=4(C_2+1)e^{-bT^2}\frac{(2r+1)!}{b^{2r+2}}.                    \tag{7}
 \end{aligned}
\]
The last identity uses $u=\sqrt{|t|}$ and the gamma integral.
It includes the whole range beyond $A_s$, not just the Gaussian part
of (3).

Let $\varphi(z)=(2\pi)^{-1/2}e^{-z^2/2}$ and $a=\varphi(0)>0$.
Fourier inversion, (5)--(7) and $T=\ell$ yield a constant $K_0\ge1$
such that, simultaneously for all integers $r\ge0$,
\[
 |g_s^{(r)}(0)-\varphi^{(r)}(0)|
 \le K_0^{r+1}(2r+3)!
                    (\varepsilon_s+e^{-b\ell^2}).                \tag{8}
\]
For example (6) is absorbed using $(r+3)!\le(2r+3)!$; (7)'s
$b^{-2r-2}$ is absorbed into the fixed base $K_0$. Factors $1/(2\pi)$
and the fixed constants are also absorbed. There is no order-dependent
onset in (8). Since $e^{-b\ell^2}\le\varepsilon_s$ eventually,
increase a fixed base $K\ge1$ to include the factor 2 and $1/a$.
Then
\[
 \frac{|g_s^{(r)}(0)-\varphi^{(r)}(0)|}{a}
       \le \varepsilon_s K^{r+1}(2r+3)!
       \quad(r\ge0).                                           \tag{9}
\]

### 3. A sufficient Gaussian conditioning bound

For a given $m\ge2$, set
\[
 H_m=[\varphi^{(i+j)}(0)/a]_{i,j=0}^{m-1},\qquad
 E_{s,m}=[(g_s^{(i+j)}(0)-\varphi^{(i+j)}(0))/a]_{i,j=0}^{m-1}.
\]
C466a's Gaussian/Hermite determinant identity gives
\[
 \det H_m=(-1)^{d_m}\prod_{j=0}^{m-1}j! .                         \tag{10}
\]
In particular it is nonsingular. Its odd-derivative entries vanish,
and the even ones of order $2k\le2m-2$ have absolute value
$(2k)!/(2^k k!)\le (2m)!$. Every $(m-1)$-minor is consequently at
most $(m-1)![(2m)!]^{m-1}$ in absolute value, by its permutation
expansion. Dividing the adjugate by (10), whose absolute value is at
least 1, and using $\|M\|_2\le m\max_{ij}|M_{ij}|$, gives
\[
 \|H_m^{-1}\|_2\le m![(2m)!]^{m-1}.                              \tag{11}
\]
This intentionally coarse finite bound pays conditioning without any
positive-definite assertion about this signed derivative matrix.
Equation (9), with $0\le i+j\le2m-2$, gives
\[
 \|E_{s,m}\|_2\le m\varepsilon_s K^{2m}(4m)!.
\]
Thus, writing
\[
 Q_m=m\,m![(2m)!]^{m-1}K^{2m}(4m)!,
\]
we have $\|H_m^{-1}\|_2\|E_{s,m}\|_2\le\varepsilon_s Q_m$.

Import I. C. F. Ipsen and R. Rehman, *Perturbation Bounds for
Determinants and Characteristic Polynomials*, SIAM J. Matrix Anal.
Appl. **30**(2) (2008), 762--776,
[Corollary 2.14 and proof, p. 770](https://ipsen.math.ncsu.edu/ps/simax070477.pdf).
For complex square $H,E$ with $H$ nonsingular, it states
$|\det(H+E)-\det H|/|\det H|
\le(1+\|H^{-1}\|_2\|E\|_2)^m-1$.
These are exactly the hypotheses of (10)--(11); no Hermitian condition
on $E$ is required. This general theorem is imported, not reproved.
It yields
\[
 \left|\frac{\det(H_m+E_{s,m})}{\det H_m}-1\right|
 \le e^{m\varepsilon_s Q_m}-1.                                  \tag{12}
\]

### 4. Simultaneous orders and normalization by the actual density

The elementary estimate $n!\le n^n$ shows that for $m\ge2$,
\[
 \begin{aligned}
 \log(mQ_m)
 &\le 2\log m+m\log m
       +2m(m-1)\log(2m)+2m\log K+4m\log(4m)\\
 &\le C_K m^2\log(m+1),                                        \tag{13}
 \end{aligned}
\]
with one fixed $C_K$. If $2\le m\le\ell^{1/4}$, the right side is
at most $C_K\ell^{1/2}\log(\ell+1)=o(\ell)$ (after taking
$\ell\ge1$). In particular, choose one threshold so it is at most
$\ell/8$ for all the indicated $m$. Then
\[
 u_{s,m}:=m\varepsilon_s Q_m
 \le e^{-\ell/8}\ell^{-1/2}\le s^{-1/8}.                         \tag{14}
\]
All thresholds so far depend only on fixed input constants.

For the actual density value, (9) at $r=0$ gives
\[
 \eta_s:=g_s(0)/a-1,\qquad |\eta_s|\le 6K\varepsilon_s.
\]
Eventually $|\eta_s|\le1/2$, so $|\log(1+\eta_s)|\le2|\eta_s|$.
For the entire order range,
\[
 v_{s,m}:=m|\log(1+\eta_s)|
 \le12K\ell^{1/4}\varepsilon_s\le s^{-1/8}                       \tag{15}
\]
after one further increase of the threshold. The last inequality
follows from $12K e^{-\ell/8}\ell^{-1/4}\to0$.
Since $g_s(0)>0$, the logarithm and the real power are well-defined.

Let $q_{s,m}=\det(H_m+E_{s,m})/\det H_m$ and
$b_{s,m}=(1+\eta_s)^{-m}$. From (12), $|q_{s,m}-1|\le e^{u_{s,m}}-1$;
from (15), $|b_{s,m}|\le e^{v_{s,m}}$ and
$|b_{s,m}-1|\le e^{v_{s,m}}-1$. Hence
\[
 \begin{aligned}
 \left|\frac{\mathcal D_m(g_s;0)}
 {g_s(0)^m\prod_{j=0}^{m-1}j!}-1\right|
 &=|q_{s,m}b_{s,m}-1|\\
 &\le(e^{u_{s,m}}-1)e^{v_{s,m}}+e^{v_{s,m}}-1\\
 &\le e^{2s^{-1/8}}-1.                                         \tag{16}
 \end{aligned}
\]
Here (10) accounts for the sign $(-1)^{d_m}$ exactly.
Choose the common $S$ larger if necessary so that the last expression
is at most $1/2$ and all previous thresholds hold. For every real
$s\ge S$, (16) then holds simultaneously for every permitted integer
$m$. This is a uniform estimate, not a selection of finitely many
fixed-order onsets depending on $m$.

### 5. Transfer back to the actual density

C466a's exact tilt/scale identity, valid at every finite order, is
\[
 \frac{\mathcal D_m(p;x_s)}{p(x_s)^m}
 =v_s^{-d_m}\frac{\mathcal D_m(g_s;0)}{g_s(0)^m}.
\]
Its triangular Leibniz congruence has determinant one; it is an identity,
so introduces no order-dependent error. Inserting it into (16) proves
(1). All denominator factors are positive, proving the strict sign.
Multiplication of the density by $1/c_0$ multiplies its size-$m$
determinant and its density power by the same positive factor, proving
the assertion for $\Theta$. No extension away from $x_s$, no all-order
limit at a fixed $x$, and no logarithmic-Hankel sign is used. ∎

The new work is the explicit weighted-error/conditioning comparison
and common onset for the stated range. The general saddle input,
Gaussian determinant, tilt/scale transfer and determinant perturbation
theorem are imported or reused as specified. Assessment906 found no
matching statement among the sources checked; this is not proof of
novelty. No numerical certificate or mathematical script is needed for
the existential estimates above.

### Independent conceptual audit, 14 November 2026, step909

The claimed range and normalized error pass the independent audit,
relative to the precisely cited density inputs in the hypotheses.
No failed inequality, extra premise, or change to the conclusion was
found. This verifies the recorded specialization; it establishes no
further theorem beyond (1) and does not certify originality. The
following checks address the order-dependent analytic obligations.

**Analytic domain and Fourier weights.** C466a's analytic logarithm is
available throughout the half-radius disk in (2). The segment in (4)
stays there because its length is at most $T/\sigma_s\le s/2$.
Taylor's integral remainder uses only the third derivative, with factor
$1/6$; using $\sigma_s\asymp s^{-3/4}\ell^{1/2}$ gives precisely
$s^{-1/4}\ell^{-1/2}$. The conditions $T\le A_s/2$ and
$C_3\varepsilon_sT^3\le1$ hold for every sufficiently large real $s$,
independently of $r$ and $m$.

For $|t|\ge T\ge1$ and $A_s\ge T$, both terms defining $F_s(t)$
are at least $T^2$, and both are at least $\sqrt{|t|}$.
Consequently $F_s(t)\ge(T^2+\sqrt{|t|})/2$, which verifies
the split in (7) even for $|t|>A_s$. Independently,
$2t^2\ge T^2+\sqrt{|t|}$ verifies the Gaussian split.
The substitution $u=\sqrt{|t|}$ on both half-axes gives exactly
$4\int_0^\infty u^{2r+1}e^{-bu}\,du
=4(2r+1)!b^{-2r-2}$. Together with (6), this proves that a single
base $K$ absorbs every prefactor in (9) for all integers $r\ge0$.
Absolute weighted inversion identifies the derivatives of the given
smooth density. It is used separately at each finite $r$ with one
explicit bound; no infinite-order differentiation or varying-order
dominated-convergence limit is taken.

**Matrix sign and amplification.** If $M_{ij}=\mathbb E Z^{i+j}$
and $U=\operatorname{diag}(1,i,\ldots,i^{m-1})$, then
$H_m=UMU$, not a Hermitian congruence. Thus its determinant has
the factor $\det(U)^2=(-1)^{d_m}$ and magnitude
$\prod_{j=0}^{m-1}j!$. This checks the sign in (10) without treating
$H_m$ as positive definite. Every cofactor contains $(m-1)!$ terms;
the spectral-norm bound then yields exactly (11). At maximal derivative
order $r=2m-2$, (9) costs $K^{2m-1}(4m-1)!$, which is indeed no
larger than the displayed $K^{2m}(4m)!$. The cited Ipsen--Rehman
Corollary 2.14 applies to this nonsingular complex matrix and the full
error matrix, and (12) retains the finite perturbation error.

**Common onset and actual normalization.** Equation (13), maximized
over $2\le m\le\ell^{1/4}$, costs at most
$C_K\ell^{1/2}\log(\ell+1)=o(\ell)$; there is no dependence of
its threshold on a subsequently chosen $m$. Multiplication by
$\varepsilon_s=e^{-\ell/4}\ell^{-1/2}$ gives (14).
For (15), the ratio of its first upper bound to $s^{-1/8}$ is
$12K e^{-\ell/8}\ell^{-1/4}\to0$. Since $\eta_s$ is real and
$|\eta_s|\le1/2$, the real logarithm inequality applies. Therefore
the errors in both the determinant and its actual denominator combine
to at most $e^{u_{s,m}+v_{s,m}}-1\le e^{2s^{-1/8}}-1$.
Taking the maximum of the finitely many fixed thresholds, including
$2s^{-1/8}\le\log(3/2)$, gives one $S$ valid on the whole half-line.
There is no maximum over a growing collection of fixed-order onsets.

Finally, scaling contributes $\sigma_s^{m^2}$ to the determinant
and $\sigma_s^m$ to the density power, so the inverse transfer factor
is $\sigma_s^{-m(m-1)}=v_s^{-d_m}$. The triangular tilt identity
is exact at every finite $m$ and its determinant is one. The ratio is
real and within $1/2$ of one, and $p(x_s),v_s$ and the factorial
product are positive, establishing the strict sign in precisely (1).

C466a supplies all the reused analytic estimates and the inherited
L018 completion convention. The external density/counting/
finite-zero inputs and the standard perturbation theorem remain cited
inputs, not newly replayed source proofs or certificates. Contact
forcing, simultaneous contacts, propagation, all-order global PF and
the L030-L032/C032a interface remain unresolved. No numerical check
or mathematical script is needed for this existential comparison.

## Mathlib

Full matching coverage is not checked. C466a's supporting Fourier,
Cauchy and Gaussian/Hermite inputs and the cited finite perturbation
theorem are used as informal mathematical results; no specific Mathlib
declaration for this growing-order specialization is asserted.
Unknown coverage is not evidence of absence.
