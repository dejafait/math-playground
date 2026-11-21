# Corollary 466a: reciprocal-Xi fixed-order boundary PF positivity

## Hypotheses

Use the actual completion and conventions of L018, and put
$c_0=\xi(1/2)>0$,
$h(z)=\xi(1/2+\sqrt z)/c_0$. Evenness about $1/2$ makes
this an entire function of $z$, independent of the square-root choice.
For positive real $s$, put $B(s)=\log h(s)$.

Import the **one-sided density assertion only** from Suvrit Sra,
*On some positivity properties of the Riemann Xi function*,
[version-specific primary Hub text W_pr5z5huy_v1](https://hub.valency.io/works/W_pr5z5huy_v1),
Theorem 1.1, Lemma 2.4 (including its Appendix B proof), and
Corollary 2.5: there is a probability density $\theta_1\in C^\infty(\mathbb R)$,
zero on $( -\infty,0]$, positive on $(0,\infty)$, with
\[
 \int_0^\infty e^{-zu}\theta_1(u)\,du=h(z)^{-1}
 \quad(\operatorname{Re}z>0).
\]
Set $\Theta=\theta_1/c_0$; its mass is $1/c_0$, not one.

The source's density construction uses the critical strip and zero
symmetries, the paired Hadamard product, its zero-counting input
\[
 |N(Y)-M(Y)|\le\tfrac18\log(Y+2)+4\quad(Y\ge0),\qquad
 M(Y)=\tfrac{Y}{2\pi}(\log(Y/(2\pi))-1),\quad M(0)=0,
\]
and verified critical-line zeros through height 100, with first ordinate
$14<\gamma_1<15$. These are the hypotheses recorded in its
Section 2.1, equations (6)–(8); Lemma 2.2 at $U=100$, Proposition 2.3
and Lemma 2.4 supply the stated density. The counting bound is attributed
there to Bellotti–Wong, and the finite zero input to Platt–Trudgian and
rigorous first-zero isolation. They remain cited external inputs; this
audit does not independently replay those theorems or zero certificates.
No critical-line assertion above height 100, simplicity assumption,
global PF property, or RH is an additional hypothesis of this argument.
The source's other Gaussian-mixture assertions are not used.

## Conclusion

For each fixed integer $m\ge1$ there is $\epsilon_m>0$ such that,
for $1\le k\le m$,
\[
 \det[\Theta(x_i-y_j)]_{i,j=1}^k>0
\]
whenever $x_1<\cdots<x_k$, $y_1<\cdots<y_k$, and
$0<x_i-y_j<\epsilon_m$ for every $i,j$.

More precisely, define
\[
 d_k=\frac{k(k-1)}2,\quad
 \mathcal D_k(p;x)=(-1)^{d_k}\det[p^{(i+j)}(x)]_{i,j=0}^{k-1},
 \quad x_s=B'(s),\quad v_s=-B''(s).
\]
Then $v_s>0$ eventually and, for every fixed $k$,
\[
 \frac{\mathcal D_k(\Theta;x_s)}
 {\Theta(x_s)^k v_s^{-d_k}\prod_{j=0}^{k-1}j!}\longrightarrow1
 \quad(s\longrightarrow\infty).
\]
This is Sra's Proposition C.8, reproduced and analytically audited here.
There is no effective value of $\epsilon_m$, common neighborhood for
all orders, global PF conclusion, or sign for L030's logarithmic-Hankel
forms. The last forms involve algebraic squares of reciprocal-zero
polynomials and are different from these density minors.

## Proof

The audit follows Proposition C.8, equations (C.8)–(C.10), rendered as
(31)–(33) in the cited HTML, through its final tilt/scale identity.
Reproduction is needed to verify its all-frequency derivative limit and
local-domain transfer, not to claim a new saddlepoint or PF theorem.

### Complex domain and differentiated saddle estimate

Use the principal square root $q=\sqrt z$ when $\operatorname{Re}z\ge0$
and $|z|$ is large. Then
$ |\arg q|\le\pi/4$ and
$\operatorname{Re}q\ge|q|/\sqrt2$.
L018's formula gives
\[
 h(z)=\frac{(z-1/4)\pi^{-(q+1/2)/2}
                   \Gamma(q/2+1/4)\zeta(q+1/2)}{2c_0}.
\]
All factors are nonzero on this large right-half-plane region: in
particular $\operatorname{Re}(q+1/2)>1$ permits the Euler product.
Their analytic logarithms choose the branch real on the positive axis.
The shifted gamma argument stays in the fixed sector
$|\arg(q/2+1/4)|\le\pi/4$, with modulus comparable to $|q|$.

Apply [NIST DLMF 5.11.1](https://dlmf.nist.gov/5.11#E1), whose
asymptotic expansion is uniform in a fixed sector
$|\arg w|\le\pi-\delta$, and the Euler-product estimate
$\log\zeta(q+1/2)=O(2^{-\operatorname{Re}(q+1/2)})$.
For the latter estimate the absolutely convergent logarithmic Euler
series at real part at least 2 is bounded by a constant times its
first exponential scale, uniformly in the imaginary part.
Expansion of the fixed shift $1/4$ in the gamma argument yields
\[
 B(z)=\frac{\sqrt z}{2}
       \left(\log\frac{\sqrt z}{2\pi}-1\right)
       +\frac78\log z+C+R(z),\qquad
 |R(z)|\le C_R|z|^{-1/2}.                 \tag{1}
\]
Here $C$ is real and the remainder is analytic on the region in use.
In particular, the logarithmic coefficient combines $2\log q$
from the polynomial factor with $-\tfrac14\log q$ from gamma,
giving $\tfrac74\log q=\tfrac78\log z$.

For $|z-s|\le s/2$, a Cauchy disk of radius $s/4$ stays in
$\operatorname{Re}z\ge s/4$, and its modulus is comparable to $s$.
Cauchy's estimates therefore bound the $j$-th derivative of $R$
by $O_j(s^{-j-1/2})$ there. Differentiating the explicit part of (1)
gives, with $w=\sqrt s$ and $L=\log(w/(2\pi))-1$,
\[
 x_s=\frac{\log(w/(2\pi))}{4w}+\frac7{8s}+O(s^{-3/2}),\qquad
 v_s=\frac{L}{8s^{3/2}}+\frac7{8s^2}+O(s^{-5/2}),            \tag{2}
\]
and $B'''(z)=O(s^{-5/2}\log s)$ on the stated half-radius disk.
Consequently $x_s\sim\log s/(8\sqrt s)>0$,
$v_s\sim\log s/(16s^{3/2})>0$, and $x_s'=-v_s<0$ eventually.
It follows that $s\mapsto x_s$ maps a sufficiently late half-line
continuously and strictly decreasingly onto an entire interval next
to zero, not just a sequence approaching zero.

### Tilt and weighted Fourier inversion

The normalized tilted density and its standardization are
\[
 f_s(u)=e^{B(s)-su}\theta_1(u),\quad
 \sigma_s=\sqrt{v_s},\quad
 g_s(z)=\sigma_s f_s(x_s+\sigma_s z).
\]
Differentiating its Laplace transform is justified by
$u^j e^{-su}\le C_{j,s}$ on the nonnegative half-line.
Thus $f_s$ has mean $x_s$ and variance $v_s$.
The characteristic function of $g_s$ is
\[
 \phi_s(t)=\exp\{B(s)-B(s-it/\sigma_s)-itx_s/\sigma_s\}.
\]
For fixed $t$, the Taylor segment lies in the disk above for large $s$,
since $s\sigma_s\longrightarrow\infty$. The linear terms cancel,
the quadratic term is $-t^2/2$, and the remainder is bounded by
\[
 O\bigl(|t|^3\sigma_s^{-3}s^{-5/2}\log s\bigr)
   =O_t(s^{-1/4}(\log s)^{-1/2})=o(1).
\]
Hence $\phi_s(t)\to e^{-t^2/2}$ pointwise.

The required domination holds on the whole real frequency axis.
Write $\sqrt{1+iu}=a+ib$. Then $a\ge1$, $a^2-b^2=1$, and
$\eta=|b|/a\in[0,1)$. Direct algebra gives
\[
 \operatorname{Re}[(a+ib)\log(a+ib)]
 =a\{\operatorname{arctanh}(\eta^2)-\eta\arctan\eta\}\ge0. \tag{3}
\]
Indeed the braces vanish at zero and have derivative
$\eta/(1-\eta^2)-\arctan\eta\ge0$, since
$\arctan\eta\le\eta\le\eta/(1-\eta^2)$.
In subtracting (1) at $s(1+iu)$ and $s$, the other logarithmic term
$(7/8)\log|1+iu|$ is nonnegative as well. The two remainders have
absolute sum at most $2C_R/w$, uniformly for all real $u$.
Thus, for large $s$ with $L>0$,
\[
 \operatorname{Re}B(s+isu)-B(s)
       \ge \frac{wL}{2}(a-1)-\frac{2C_R}{w}.                \tag{4}
\]
Furthermore,
\[
 a-1=\frac{u^2}{2(a+1)(\sqrt{1+u^2}+1)}
       \ge c_1\min\{u^2,\sqrt{|u|}\}.                    \tag{5}
\]
To check the positive absolute constant in (5), the ratio to the
right-hand minimum is positive and continuous away from zero; its
limits at zero and infinity are respectively $1/8$ and $1/\sqrt2$.
Compactness on the intervening ranges gives a strictly positive infimum.

Set $A_s=s\sigma_s$. Equation (2) gives
$A_s^2\sim wL/8$ and $A_s\to\infty$.
Substitution of $u=-t/A_s$ into (4)–(5) proves, with positive constants
independent of sufficiently large $s$,
\[
 |\phi_s(t)|\le C_2
    \exp[-c\min\{t^2,A_s^{3/2}\sqrt{|t|}\}]
 \le C_2\exp[-c\min\{t^2,\sqrt{|t|}\}].                 \tag{6}
\]
The last inequality uses $A_s\ge1$. For every fixed integer $r\ge0$,
the last function times $|t|^r$ is integrable: at infinity it is
a polynomial times $e^{-c\sqrt{|t|}}$, and near zero it is bounded
by a constant times $|t|^r$.

The standard Fourier inversion theorem for an integrable characteristic
function, followed by differentiation under an absolutely convergent
integral, identifies
\[
 g_s^{(r)}(0)=\frac1{2\pi}\int_{\mathbb R}(-it)^r\phi_s(t)\,dt.
\]
The inverse transform is the given continuous density, not merely an
almost-everywhere unidentified version. Dominated convergence using (6)
then gives $g_s^{(r)}(0)\to\varphi^{(r)}(0)$ for every fixed $r$,
where $\varphi(z)=(2\pi)^{-1/2}e^{-z^2/2}$.
For size $k$, precisely the finitely many derivatives through $2k-2$
are needed. There is no uniform claim as $k\to\infty$.

### Determinant normalization and local ordered minors

For a standard normal $Z$,
$\varphi^{(n)}(0)=\varphi(0)i^n\mathbb E Z^n$.
Factoring the powers of $i$ from rows and columns cancels the sign
$(-1)^{d_k}$ in $\mathcal D_k$. The Gaussian moment Gram determinant
is $\prod_{j=0}^{k-1}j!$, by the monic Hermite orthogonality formula
(also used explicitly in Proposition C.8). Therefore
\[
 \mathcal D_k(\varphi;0)=\varphi(0)^k\prod_{j=0}^{k-1}j!>0.
\]
Continuity of a finite determinant and the derivative limits imply
\[
 \frac{\mathcal D_k(g_s;0)}{g_s(0)^k}
       \longrightarrow\prod_{j=0}^{k-1}j!.
\]
The denominator stays positive, since $g_s(0)\to\varphi(0)>0$.

To check the exact transfer, Leibniz's rule gives
$M_{e^{cx}p}=e^{cx}T_cM_pT_c^{\mathsf T}$, where
$(M_p)_{ij}=p^{(i+j)}$ and
$(T_c)_{ij}=\binom ij c^{i-j}$ for $j\le i$.
The triangular matrix has determinant one; constant density factors
also cancel in $\mathcal D_k(p)/p^k$. Thus tilting and division by
$c_0$ do not change this ratio. Scaling $g_s(z)=\sigma_s
f_s(x_s+\sigma_s z)$ contributes $\sigma_s^{k^2}$ to its
differential determinant and $\sigma_s^k$ to its density power.
Consequently
\[
 \frac{\mathcal D_k(\Theta;x_s)}{\Theta(x_s)^k}
 =\sigma_s^{-k(k-1)}\frac{\mathcal D_k(g_s;0)}{g_s(0)^k}.
\]
Since $\sigma_s^2=v_s$, this proves the claimed ratio limit.
For fixed $m$, choose one sufficiently large $s$-threshold for all
$k\le m$. The interval-surjectivity proved after (2) gives
$\mathcal D_k(\Theta;x)>0$ on a common interval
$(0,\epsilon_m)$ for those finitely many $k$.

It remains to verify the domain specialization of Sra's Lemmas C.1
and C.6, the classical positive-initial-Wronskian criterion.
If every prescribed cross difference is in this interval, then
\[
 0<x_1-y_k\le x-y\le x_k-y_1<\epsilon_m
\]
for every $x\in[x_1,x_k]$, $y\in[y_1,y_k]$.
The strict bounds permit small open enlargements of these intervals.
For each such $y$, the functions
$x\mapsto(-1)^j\Theta^{(j)}(x-y)$, $0\le j<k$, have positive
initial Wronskians: their size-$r$ Wronskian is exactly
$\mathcal D_r(\Theta;x-y)$. Lemma C.1 gives positive ordered
evaluation determinants at any initial subset of the $x_i$.
These are the transposed initial Wronskians of
$y\mapsto\Theta(x_i-y)$, with the $x_i$ in increasing order.
A second application of C.1 on the $y$-interval gives the required
ordered minor. Transposition does not change its determinant.
All intermediate points remain in the displayed rectangle, and
$C^{2m-2}$ regularity is supplied by the imported smooth density.
This pays the local domain and strictness requirements in C.6 without
assuming its global hypotheses. ∎

Audit completed 14 November 2026, step883. No failed premise was found
in this selected analytic chain. This conclusion is relative to the
cited density and standard theorem inputs, not a verification of the
entire manuscript or newer inaccessible versions. In particular,
letting $m$ grow with $s$, propagating these signs away from zero,
and transferring them to L030 remain unproved.

## Mathlib

Full matching coverage has not been checked. The Fourier inversion,
dominated convergence, Cauchy estimates and determinant identities are
standard supporting mathematics, but no specific Mathlib declaration
is asserted here. Unknown coverage is not evidence of absence.
