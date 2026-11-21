# Corollary 028m: half-stable boundary PF does not propagate globally

## Hypotheses

Fix this single function, independently of every order parameter:
\[
 p(x)=\frac{e^{-1/(4x)}}{2\sqrt\pi\,x^{3/2}}\quad(x>0),
 \qquad p(x)=0\quad(x\le0).
\]
For integers \(k\ge1\), put
\[
 d_k=k(k-1)/2,\qquad
 D_k(p;x)=(-1)^{d_k}\det[p^{(i+j)}(x)]_{i,j=0}^{k-1}.
\]

Import the positive half-stable law from Thomas Simon,
*Positive stable densities and the bell-shape*,
[arXiv:1302.0956v1, 5 February 2013](https://arxiv.org/pdf/1302.0956v1),
Introduction p.2: its Laplace transform is \(e^{-\sqrt s}\), and
\(X_{1/2}\) has the law of \(1/(4\Gamma_{1/2})\).
Section 3.2, pp.9–10, gives its self-decomposability with zero drift
and decreasing spectral function \(t^{-1/2}/(2\sqrt\pi)\).
The normalization of our displayed density is checked below.

For the finite-interval transfer import only Suvrit Sra,
*On some positivity properties of the Riemann Xi function*,
[arXiv:2611.02944v1, 2 November 2026](https://arxiv.cnoctave.top/pdf/2611.02944),
Lemma C.16, first assertion (C.47), pp.37–38, and its
positive-initial-Wronskian input Lemma C.1, p.20.
Precisely: if \(f\in C^{2m-2}(I)\) and \(D_j(f;t)>0\)
on the interval \(I=(a,b)\) for \(1\le j\le m\), its ordered
translation minors of size \(k\le m\) are positive when
\(a<x_1-y_k\) and \(x_k-y_1<b\).
No actual-Xi density theorem, global PF assertion, support-boundary
variant, or identity of different manuscript versions is imported.

## Conclusion

The zero extension of \(p\) is a smooth probability density, positive
on \((0,\infty)\), flat at zero, with a self-decomposable law.
For every fixed integer \(m\ge1\) there exists \(\epsilon_m>0\)
such that, for every \(1\le k\le m\),
\[
 \det[p(x_i-y_j)]_{i,j=1}^k>0
 \quad\text{if }x_1<\cdots<x_k,\ y_1<\cdots<y_k,
 \quad0<x_i-y_j<\epsilon_m\quad\text{for all }i,j.       \tag{1}
\]
More precisely, with \(x_s=1/(2\sqrt s)\) and
\(v_s=1/(4s^{3/2})\), every fixed \(k\) satisfies
\[
 \frac{D_k(p;x_s)}
 {p(x_s)^k v_s^{-d_k}\prod_{j=0}^{k-1}j!}\longrightarrow1
 \quad(s\longrightarrow\infty).                       \tag{2}
\]
Nevertheless, the increasing tuples \(x=(2,3)\), \(y=(0,1)\)
give the strictly negative global minor
\[
 \det\begin{pmatrix}p(2)&p(1)\\p(3)&p(2)\end{pmatrix}
 =\frac{e^{-1/4}}{32\pi}
  -\frac{e^{-1/3}}{4\pi\,3^{3/2}}<0.                  \tag{3}
\]
Thus smoothness, positivity, self-decomposability and the
order-dependent boundary property (1) do not imply global PF,
even of order two. This is the countermodel to the exact generic
implication in nomination1684; it is not a counterexample to RH.

There is no order-uniform neighborhood claim. This law has neither
global log-concavity nor an entire reciprocal Laplace transform,
and does not realize actual Xi. No conclusion about C028g's
\(S_F\), or the missing all-degree actual-Xi signs, follows.
This is an explicit specialization of the assessed Gaussian
determinant method, not a claim of a new general PF theorem or
of originality beyond the sources checked. The separate conceptual
audit1688 below validates this scoped countermodel relative to the
precisely cited external inputs.

## Proof

### The fixed law and its endpoint

The density of \(\Gamma_{1/2}\) is
\(q(t)=t^{-1/2}e^{-t}/\sqrt\pi\) for \(t>0\).
Under \(t=1/(4x)\), its transformed density is
\[
 q(1/(4x))\frac1{4x^2}
 =\frac{e^{-1/(4x)}}{2\sqrt\pi\,x^{3/2}}=p(x).
\]
This proves mass one and identifies exactly the normalization in
the cited stable-law and self-decomposability assertions.
Smoothness and positivity hold in the interior. Inductively each
derivative is a finite sum of constant multiples of
\(e^{-1/(4x)}x^{-3/2-n}\), with nonnegative integers \(n\).
Every such term tends to zero as \(x\downarrow0\).
The derivative extensions therefore agree to every order with zero
on the negative half-line. This proves the asserted smooth flat
extension, not just almost-everywhere density identification.

### Exact tilted density and every fixed derivative

Let \(B(s)=\sqrt s\) for \(s>0\). Define the normalized tilt
\[
 f_s(u)=e^{B(s)-su}p(u),\qquad
 \sigma_s=\sqrt{v_s}=\frac1{2s^{3/4}},\qquad
 g_s(z)=\sigma_s f_s(x_s+\sigma_s z).
\]
The imported Laplace transform normalizes \(f_s\).
Differentiating that transform gives its mean \(B'(s)=x_s\)
and variance \(-B''(s)=v_s>0\). Differentiation is legitimate:
for every fixed positive \(s\), \(u^r e^{-su}\) is bounded
on \(u\ge0\), and the same domination holds in a neighborhood
of \(s\) using \(e^{-su/2}\).

Put \(a=s^{1/4}\). Then \(x_s=1/(2a^2)\),
\(\sigma_s=1/(2a^3)\), and direct substitution gives, for real
\(z>-a\), the exact identity
\[
 g_s(z)=\frac1{\sqrt{2\pi}}(1+z/a)^{-3/2}
     \exp\!\left(-\frac{z^2}{2(1+z/a)}\right).         \tag{4}
\]
Indeed the prefactor is
\(\sigma_s x_s^{-3/2}/(2\sqrt\pi)=1/\sqrt{2\pi}\),
and the exponent is
\[
 a^2-\frac{a^2}2(1+z/a)-\frac{a^2}{2(1+z/a)}
 =-\frac{z^2}{2(1+z/a)}.
\]

For each fixed radius \(R>0\), take \(a>2R\). The right side
of (4) is holomorphic on a neighborhood of \(|z|\le R\), using
the logarithm of \(1+z/a\) that is zero at \(z=0\).
There \(1+z/a\to1\) uniformly, its inverse stays bounded,
and its logarithm tends uniformly to zero. Hence (4) converges
uniformly on that complex disk to
\(\varphi(z)=(2\pi)^{-1/2}e^{-z^2/2}\).
Cauchy's integral formula, on any fixed circle of positive radius,
now gives
\[
 g_s^{(r)}(0)\longrightarrow\varphi^{(r)}(0)
 \quad\text{for every fixed integer }r\ge0.            \tag{5}
\]
For example its derivative error is at most \(r!R^{-r}\)
times the uniform function error on \(|z|=R\).
Real derivatives agree with these analytic derivatives by (4).
Thus no Fourier inversion, tail domination, or inference from
pointwise Gaussian convergence is needed. Also
\(g_s(0)=\varphi(0)>0\) exactly.

### Gaussian determinant and the exact congruences

If \(Z\) is a standard normal random variable, the elementary
Gaussian Taylor and moment formulas give
\(\varphi^{(n)}(0)=\varphi(0)i^n\mathbb E Z^n\).
Factoring \(i^r\) from row \(r\) and \(i^t\) from column \(t\)
gives a total factor \(i^{k(k-1)}=(-1)^{d_k}\).
The sign in \(D_k\) cancels it. The remaining moment determinant
is the Gram determinant of \(1,Z,\ldots,Z^{k-1}\).

For completeness, monic probabilists' Hermite polynomials
\(H_j=(-1)^j e^{z^2/2}(d/dz)^j e^{-z^2/2}\) change this monomial
basis by a triangular matrix with diagonal one. Integration by
parts \(j\) times gives
\(\int H_j(z)q(z)\varphi(z)\,dz=\int q^{(j)}(z)\varphi(z)\,dz\)
for every polynomial \(q\); all boundary terms vanish because
polynomials times the Gaussian tend to zero. They are consequently
orthogonal, with squared norm \(j!\). It follows that
\[
 D_k(\varphi;0)=\varphi(0)^k\prod_{j=0}^{k-1}j!>0.
\]
Using precisely the finitely many limits (5) through order
\(2k-2\) and continuity of a determinant,
\[
 \frac{D_k(g_s;0)}{g_s(0)^k}
 \longrightarrow\prod_{j=0}^{k-1}j!.                 \tag{6}
\]

To transfer (6), for \(M_f(u)=[f^{(i+j)}(u)]_{i,j=0}^{k-1}\),
Leibniz's rule gives
\[
 M_{e^{cu}f}(u)=e^{cu}T_cM_f(u)T_c^{\mathsf T},
 \qquad (T_c)_{ij}=\binom ij c^{i-j}\ (j\le i),
\]
and zero above the diagonal. The identity follows by the binomial
convolution \(\sum_{r+t=n}\binom ir\binom jt=\binom{i+j}n\)
for each derivative coefficient. Since \(\det T_c=1\),
\(D_k(f;u)/f(u)^k\) is invariant under multiplication by a
positive constant or by a real exponential. Under
\(g(z)=\sigma f(x+\sigma z)\) with \(\sigma>0\), the
determinant has factor \(\sigma^{k+2d_k}=\sigma^{k^2}\),
while the density power has factor \(\sigma^k\). Therefore
\[
 \frac{D_k(p;x_s)}{p(x_s)^k}
 =\sigma_s^{-2d_k}\frac{D_k(g_s;0)}{g_s(0)^k}.
\]
Equations (6) and \(\sigma_s^2=v_s\) prove (2).
As a low-order sign/power check, direct differentiation gives
\[
 D_2(p;x)=p(x)^2\frac{1-3x}{2x^3},\qquad v_s=2x_s^3,
\]
in agreement with the normalized limit one.

### Whole boundary intervals and ordered tuples

Fix \(m\). For every \(k\le m\), the positive limit (2)
gives \(D_k(p;x_s)>0\) for all sufficiently large \(s\),
since every factor in its denominator is positive.
Take a common threshold \(S_m>0\) for these finitely many
orders. The map \(s\mapsto x_s\) is continuous and strictly
decreasing, with image \((0,1/(2\sqrt{S_m}))\) on
\((S_m,\infty)\). Thus all \(D_k\), \(k\le m\), are
positive throughout that interval. Set
\(\epsilon_m=1/(2\sqrt{S_m})\).

Smoothness supplies the regularity required by the cited Lemma C.16.
For tuples in (1), their extreme differences satisfy
\(0<x_1-y_k\le x_i-y_j\le x_k-y_1<\epsilon_m\),
which are exactly its finite-interval conditions. Thus the lemma
applies on \(I=(0,\epsilon_m)\).
To make its domain restriction explicit, every intermediate point
in \([x_1,x_k]\times[y_1,y_k]\) has its difference in this same
interval. For each fixed \(y\), the functions
\(x\mapsto(-1)^j p^{(j)}(x-y)\) have initial Wronskians
\(D_r(p;x-y)>0\). The first Wronskian criterion gives positive
evaluation determinants at every initial subset of the \(x_i\).
Those determinants are the transposed initial Wronskians of
\(y\mapsto p(x_i-y)\). The second criterion gives (1).
The strict endpoint margins allow open interval enlargements
inside the certified difference domain. This application does
not reach any value outside that domain or exchange the limits
\(m\to\infty\) and \(s\to\infty\).

### Exact failure at global order two

For the tuples in (3), all four arguments are positive and the
ratio of the positive products is
\[
 R=\frac{p(2)^2}{p(1)p(3)}
   =\left(\frac34\right)^{3/2}e^{1/12}.
\]
Since \(\log(4/3)=\int_1^{4/3}dt/t>1/4\),
\[
 \log R=-\tfrac32\log(4/3)+\tfrac1{12}
         <-\tfrac38+\tfrac1{12}=-\tfrac7{24}<0.
\]
This proves (3) without numerical approximation. It also agrees
with Simon's p.2 statement that the additive stable kernel fails
TP2, but that statement alone was not used as a witness.
The earlier formula for \(D_2\) shows explicitly why global
log-concavity is not present. Moreover the reciprocal transform
is \(e^{\sqrt s}\) for \(s>0\); its right derivative diverges
as \(s\downarrow0\), so it has no entire extension agreeing
there. These qualifications prevent importing this countermodel
into an implication requiring actual-Xi extra structure. ∎

### Separate conceptual audit — 19 November 2026, step1688

**Verdict: passes for the exact nomination1684, relative to the cited
law and Wronskian inputs.** This is a verification of the specialization,
not a new general theorem, an independent audit of the source manuscripts,
or a proof about actual Xi. Assessment1686, approved1687, covers this
audit. The primary-source coverage of Simon v1 and Sra v1 is reused;
neither a later manuscript version nor the support-boundary assertion
of Lemma C.16 is needed. C466a/audit883 is method precedent only.

The normalization check uses the absolute Jacobian \(1/(4x^2)\)
of the inverse-gamma substitution. It identifies one probability law,
independent of \(m\); Simon's spectral function at \(\alpha=1/2\)
is exactly \(t^{-1/2}/(2\sqrt\pi)\), with zero drift. The derivative
description at zero proves the smooth zero extension to every order.
Neither bell-shape nor a finite-order numerical test replaces these
premises.

In (4), for \(a>2R\) the image of \(|z|\le R\) under \(1+z/a\)
lies in the disk of radius \(1/2\) about one. The analytic logarithm
normalized at one is therefore unambiguous there, and its inverse and
logarithm converge uniformly to one and zero, respectively. The
exponent converges uniformly to \(-z^2/2\). Applying Cauchy's formula
on that fixed circle proves each derivative limit in (5); only the
finite set \(0\le r\le2k-2\) is used at order \(k\). No global
holomorphic extension of the zero-extended density is asserted.

The two Gaussian row/column factors multiply to
\(i^{2\sum_{j=0}^{k-1}j}=(-1)^{d_k}\), cancelling precisely the
sign in \(D_k\). Hermite integration by parts gives the monic Gram
norms \(j!\), hence a strictly positive limit. Leibniz convolution
verifies the displayed triangular congruence entry by entry, and the
positive constant used to normalize the tilt cancels after division
by the density power. Under scaling, the total determinant exponent is
\(k+2\sum_{j=0}^{k-1}j=k^2\); after normalization the exponent is
\(2d_k\). Thus (2) has \(v_s^{-d_k}\), with no missing density
factor or reversed sign. The displayed \(D_2\) formula independently
checks this sign and power.

For each fixed \(m\), finitely many eventual thresholds have a common
maximum \(S_m\). Since \(s=1/(4x^2)\), every
\(0<x<1/(2\sqrt{S_m})\) is attained, not merely a sequence of
points tending to zero. This is the required whole open interval.

For clarity, the two Wronskian domains can be fixed simultaneously.
For a permitted pair of \(k\)-tuples, choose \(\delta>0\) with
\[
 2\delta<\min\{x_1-y_k,\ \epsilon_m-(x_k-y_1)\}.
\]
Put \(J_x=(x_1-\delta,x_k+\delta)\) and
\(J_y=(y_1-\delta,y_k+\delta)\). Every difference on
\(J_x\times J_y\) lies in \((0,\epsilon_m)\). For each fixed
\(y\in J_y\), the size-\(r\) initial Wronskian on \(J_x\) of
\(u_j(x)=(-1)^j p^{(j)}(x-y)\), \(0\le j<k\), is
\[
 \det[(-1)^j p^{(i+j)}(x-y)]_{i,j=0}^{r-1}
   =D_r(p;x-y)>0.
\]
The first criterion therefore gives
\(\det[(-1)^j p^{(j)}(x_i-y)]_{1\le i\le r,\,0\le j<r}>0\)
for every \(y\in J_y\) and every \(r\le k\). Its transpose is
exactly the initial Wronskian of the first \(r\) functions
\(F_i(y)=p(x_i-y)\), ordered by increasing \(x_i\). Thus their
initial Wronskians are positive on all of \(J_y\), and the second
criterion gives the desired ordered evaluation determinant at the
\(y_j\). Transposition preserves its sign. The largest derivative
order required is \(2k-2\le2m-2\), which the smooth density supplies.
This verifies both interval restrictions and both orientations without
assuming any global differential sign.

Finally \((2,3)\) and \((0,1)\) are strictly increasing tuples with
positive cross differences \(2,1,3,2\). The two positive products in
(3) have ratio \((3/4)^{3/2}e^{1/12}\). On \([1,4/3]\), the
integrand \(1/t\) exceeds \(3/4\) except at the right endpoint, so
the proof's strict bound \(\log R<-7/24<0\) is valid. This supplies
a negative minor of the very same law, with no numerical certificate.

All nomination1684 premises are therefore met while its global PF
conclusion fails. The audit retains stop1686 at that scope. It supplies
no common \(\epsilon\) for all orders, global log-concavity, entire
reciprocal transform, actual-Xi realization, or vanishing \(S_F\).
No load-bearing error or uncovered repair was found. Full matching
Mathlib coverage remains unchecked.

## Mathlib

Full matching coverage has not been checked. No Mathlib declaration
for this complete countermodel, stable self-decomposability, or the
finite-window PF criterion is asserted. Cauchy's integral formula,
determinant congruences and Gaussian integration by parts are
supporting standard inputs, not a claimed matching formal theorem.
