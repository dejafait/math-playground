# Corollary 645l: an anchor-line Chebyshev census permits full Hankel cancellation

## Hypotheses

Use C645g's exact symbol and normalized Hardy spaces at

\[
 \delta=\frac14,\quad \eta=\frac1{100},\quad
 d=\frac54,\quad x=-d,\quad R=\frac{11}{8}.
\]

Let \(m\ge3\) be odd, set \(n=3m\), and define

\[
 t_j=j/n\quad(0\le j<n),\qquad
 B_n(v)=\prod_{j=0}^{n-1}\frac{R(v-it_j)}{R^2+it_jv}.
 \tag{1}
\]

Put \(r=1/2\), and take the \(m\) distinct poles

\[
 a_k=x+ir\cos\frac{(2k-1)\pi}{2m},\qquad 1\le k\le m,
 \tag{2}
\]

each with original simple-pole residue \(r_{a_k}=1\). Retain all
complex phases in the symbol

\[
 q_n(\zeta)=\sum_{k=1}^m
     \frac{B_n(x)}{R B_n(a_k)}\frac1{\zeta-a_k/R},\qquad
 H_{q_n}f=P_-(q_nf):H^2\longrightarrow H^2_-.
 \tag{3}
\]

Circle measure is \(d\theta/(2\pi)\); \(H^2\) has nonnegative
Fourier modes and \(H^2_-\) strictly negative modes. No actual-Xi
realization, zero selection, independent boundary upper bound, or sign
assertion is a hypothesis.

## Conclusion

The family satisfies all hypotheses of the anchor-line target:

\[
 \Re a_k=x,\quad x\in\{a_k\},\quad |a_k|\le R-\eta,
 \quad a_k\ne it_j,\quad M=m=n/3.
 \tag{4}
\]

For every odd \(m\ge3\), the entire boundary and largest operator
norm satisfy

\[
 \boxed{\displaystyle
 \|H_{q_n}\|\le\|q_n\|_\infty<720n e^{-3n/80}.}
 \tag{5}
\]

In particular, along \(n=3m\) with \(m\) odd,

\[
 e^{n/32}\|H_{q_n}\|<720n e^{-n/160}\longrightarrow0.
 \tag{6}
\]

Thus a positive constant and onset uniform over the prescribed line
family cannot give \(\|H_q\|\ge c e^{-n/32}\). This is a
synthetic obstruction, not an off-line zeta zero, an RH disproof, or
a counterexample to C645g's smaller census. The proof and exact
arithmetic were completed on 1 November 2026. A separate conceptual
audit on 2 November 2026 verified (1)--(25) and the full-norm conclusion
without a mathematical correction; its checks are recorded below.
No certified novelty or RH resolution candidate is claimed.

## Proof

### Source scope and the specialized calculation

The unchanged invocation-start
[EXPLORE assessment](../drafts/literature/2026-11-01-anchor-line-hankel-census.md)
covers the exact line-supported norm target, including a counterfamily
controlling the largest norm. Its primary-source comparison is reused.
C645g supplies the definition and scaling; its small-census estimate
is not used. C645k's audited planar circle is a comparison, not a
mathematical input: its poles are not collinear.

Import the residue theorem, simple-pole formula and contour-integral
inequality from R. W. Howell and J. H. Mathews, *Complex Analysis*,
online edition (front matter updated 22 August 2025),
[Section 8.1, Theorems 8.1.5 and 8.1.7](https://complexanalysis.org/web/sec_residue-thm.html),
and [Section 6.2, Theorems 6.2.18--6.2.19](https://complexanalysis.org/web/sec_contour-integrals.html),
as inspected in the reused assessments. The normalized Hankel convention
and contractive orthogonal projection are those of L. Baratchart,
S. Chevillard and T. Qian, *Minimax principle and lower bounds in
H2-rational approximation*, J. Approx. Theory **206** (2016), 17--47,
[Section 4, (17)--(19), author preprint v2, 24 March 2015](https://arxiv.org/pdf/1501.01161v2),
[DOI](https://doi.org/10.1016/j.jat.2015.03.004).
No Nehari/AAK conclusion or least singular value is needed.

The nodes (2) are the classical Gauss--Chebyshev nodes. The elementary
polynomial/residue identity below is written out to keep the number of
unit residues and the error for this varying, complex, n-dependent
integrand explicit. It is not a claimed new quadrature theorem or a
reproof of a general approximation theorem. The new local calculation
is the evaluated full-boundary rate at these exact parameters.

### 1. Admissibility, scaling, and two fixed contours

Cosine is strictly decreasing on \((0,\pi)\), so (2) gives distinct
poles. For odd m, \(k=(m+1)/2\) gives \(a_k=x\). Set

\[
 D=d^2=25/16,\quad U=R^2=121/64,\quad
 r_0=\sqrt{D+r^2}=\sqrt{29}/4.
\]

Then \(|a_k|\le r_0<R-\eta\), since
\((R-\eta)^2-r_0^2=2029/40000>0\). Every pole has real part
\(x<0\), avoiding the imaginary-axis grid. Also \(n=3m\ge9\)
and \(M=m\). For \(|v|\le R\) and \(0\le t<1\),
\(|R^2+itv|\ge R^2-tR>0\). Hence all weights are defined,
and (3) has a continuous bounded boundary symbol.

The scale factor in (3) gives exactly

\[
 Q_n(z):=q_n(z/R)
   =\sum_{k=1}^m F_z(a_k),\qquad
 F_z(v)=\frac{B_n(x)}{B_n(v)(z-v)},\quad |z|=R.
 \tag{7}
\]

Consider the left arc \(\Gamma\) of \(|v|=r_0\) from
\(x-ir\) to \(x+ir\), passing through \(-r_0\). It has
\(\Re v\le x\), \(|\Im v|\le r\), and

\[
 |z-v|\ge R-r_0>\frac{R^2-r_0^2}{2R}=\frac5{176}.
 \tag{8}
\]

Separately let E be the ellipse centered at x, with horizontal
semiaxis \(s=1/10\) and vertical semiaxis
\(b=\sqrt{r^2+s^2}=\sqrt{26}/10\). For
\(v=x+s\cos\theta+ib\sin\theta\), completing the square in
\(c=\cos\theta\) gives

\[
 |v|^2=D+b^2-2ds c-r^2c^2
 \le D+b^2+D s^2/r^2=377/200<R^2.
 \tag{9}
\]

The maximum occurs at \(c=-ds/r^2=-1/2\). In particular the
filled ellipse is strictly inside the disk, has
\(\Re v\le-u\), where \(u=d-s=23/20\), and on its boundary

\[
 |z-v|\ge R-\sqrt{377/200}>\frac{9}{4400}.
 \tag{10}
\]

The grid zeros of B lie to the right of both contours. Thus F_z is
holomorphic near the closed ellipse and near the lune between
\(\Gamma\) and the vertical segment. This holds uniformly in
\(|z|=R\), by the fixed positive distances (8), (10).

### 2. A gain on the whole left arc

Write \(b_t(v)=R(v-it)/(R^2+itv)\). At a point with
\(|v|=r_0\) and \(\Im v=y\),

\[
 |b_t(v)|^2=
 \frac{R^2(r_0^2+t^2-2ty)}{R^4+t^2r_0^2-2R^2ty}.
 \tag{11}
\]

The denominator is nonzero. For \(0\le t\le1\), this decreases
with y (is constant when t=0): the derivative numerator after a
positive denominator is
\(2tR^2(R^2-r_0^2)(t^2-R^2)\le0\). Its minimum on
\(\Gamma\) therefore occurs at \(a_+=x+ir\).

For this endpoint define

\[
 G(t)=\frac{|b_t(a_+)|^2}{|b_t(x)|^2}
  =\frac{(D+(r-t)^2)(U^2+Dt^2)}
         {((U-rt)^2+Dt^2)(D+t^2)}.
\]

Direct subtraction yields

\[
 E(t):=1-G(t)^{-1}
 =\frac{r(U-t^2)K(t)}{(D+(r-t)^2)(U^2+Dt^2)},\qquad
 K(t)=r(U+t^2)-2t(U-D)
     =\frac12(t-21/32)^2+1495/2048.
 \tag{12}
\]

Every term displayed is positive for \(0\le t\le1\), and
\(\log G(t)\ge1-G(t)^{-1}=E(t)\). The following four
uniform lower bounds are rational:

| interval [a,b] | minimum of K | lower bound for E(t) | simpler lower bound e |
| --- | --- | --- | --- |
| [0,1/4] | 13/16 | 288/2581 | 11/100 |
| [1/4,1/2] | 95/128 | 19950/211133 | 9/100 |
| [1/2,3/4] | 1495/2048 | 575/8584 | 13/200 |
| [3/4,1] | 47/64 | 21432/610189 | 7/200 |

To verify each row, bound its numerator in (12) below by
\(r(U-b^2)\min_{[a,b]}K\) and its denominator above by
\((D+\max\{(r-a)^2,(r-b)^2\})(U^2+Db^2)\).
The quadratic minimum is attained at the nearest point of the interval
to \(21/32\). These substitutions give exactly the listed fractions.
Their margins over the simpler bounds are respectively
\(409/258100\), \(94803/21113300\), \(213/107300\), and
\(15077/122037800\), all positive. The four e's sum to 3/10.

Each half-open quarter interval contains at least \(\lfloor n/4\rfloor\)
of the grid points \(j/n\), including for n not divisible by four.
Using (11), (12), and \(\lfloor n/4\rfloor\ge n/4-1\) gives

\[
 \log\left|\frac{B_n(v)}{B_n(x)}\right|
 \ge\frac12\sum_{j=0}^{n-1}E(j/n)
 \ge\frac3{20}\lfloor n/4\rfloor
 \ge\frac{3n}{80}-\frac3{20},\qquad v\in\Gamma.
 \tag{13}
\]

Thus \(|B_n(x)/B_n(v)|<2e^{-3n/80}\) on the entire arc;
\(e^{3/20}\le(1-3/20)^{-1}=20/17<2\). This finite-grid
estimate uses neither a Riemann-sum limit nor an asymptotic premise.

### 3. The continuous arcsine average is exponentially small

Define

\[
 A_n(z)=\frac1\pi\int_{-r}^r
       \frac{F_z(x+iy)}{\sqrt{r^2-y^2}}\,dy.
 \tag{14}
\]

Let \(S(v)=\sqrt{(v-x)^2+r^2}\), choosing the branch positive
at real points immediately to the left of x. In the open lune and
on the open segment the radicand has positive real part: write
\(v-x=h+iy\), with \(|y|<r\), so its real part is
\(h^2+r^2-y^2>0\). Thus this branch is holomorphic there, and
on the segment its value is \(\sqrt{r^2-y^2}\).

Apply the residue theorem with no enclosed poles to \(F_z/S\)
on the lune truncated at its two endpoints. Its only endpoint
singularities are of order \(|v-a_\pm|^{-1/2}\): the zeros of
the radicand are simple, and F_z is holomorphic near them. The
small connecting arc integrals tend to zero as O(sqrt(epsilon)).
Both remaining integrals are absolutely convergent. Passing to the
limit therefore replaces the upward segment by \(\Gamma\), also
oriented from its lower endpoint to its upper endpoint:

\[
 A_n(z)=\frac1{\pi i}\int_\Gamma \frac{F_z(v)}{S(v)}\,dv.
 \tag{15}
\]

This is an equality for each finite n and each boundary z; no infinite
n limit has been interchanged with an integral.

Put \(\alpha=\arctan(r/d)\in(0,\pi/2)\). Parameterize the
arc, ignoring orientation for its absolute integral, by
\(v=-r_0e^{i\theta}\), \(-\alpha\le\theta\le\alpha\).
Since \(|S(v)|=\sqrt{|v-a_+||v-a_-|}\),

\[
 \begin{aligned}
 \int_\Gamma\frac{|dv|}{|S(v)|}
 &=\frac12\int_{-\alpha}^{\alpha}
   \frac{d\theta}
    {\sqrt{\sin((\alpha-\theta)/2)\sin((\alpha+\theta)/2)}}\\
 &\le\frac\pi2\int_{-\alpha}^{\alpha}
                 \frac{d\theta}{\sqrt{\alpha^2-\theta^2}}
 =\frac{\pi^2}{2}.
 \end{aligned}
 \tag{16}
\]

Here \(\sin t\ge2t/\pi\) on \([0,\pi/2]\), by
concavity, applies to both arguments. Combining (8), (13), (15),
and (16), then using \(\pi<4\), proves the uniform bound

\[
 |A_n(z)|<\frac{\pi}{R-r_0}e^{-3n/80}
       <144e^{-3n/80},\qquad |z|=R.
 \tag{17}
\]

### 4. A controlled inverse-grid cost on the ellipse

The required estimate is

\[
 \left|\frac{B_n(x)}{B_n(v)}\right|
       \le(25/23)^n<e^{2n/23},\qquad v\in E.
 \tag{18}
\]

Here is the factor comparison, including its geometry. Normalize
\(w=v/R\), \(\tau=t/R\), \(h=u/R=46/55\), and
\(\sigma=|(w-i\tau)/(1+i\tau w)|\). For points of E,
\(|w|<1\), \(\Re w\le-h\), and \(0<\sigma<1\).
Completing the square in
\(|w-i\tau|^2=\sigma^2|1+i\tau w|^2\) gives a circle
with imaginary-axis center and radius
\(\sigma(1-\tau^2)/(1-\sigma^2\tau^2)\). It follows that

\[
 h\le\frac{\sigma(1-\tau^2)}{1-\sigma^2\tau^2},\qquad
 \sigma\ge
 \frac{2h}{1-T+\sqrt{(1-T)^2+4h^2T}}
 \ge\frac{h(1+T)}{1+h^2T},\quad T=\tau^2.
 \tag{19}
\]

The middle formula includes T=0 by direct substitution. For the last
inequality, write the square root as
\((1+T)\sqrt{1-4(1-h^2)T/(1+T)^2}\) and use
\(\sqrt{1-a}\le1-a/2\) for \(0\le a\le1\).
Here \(4T\le(1+T)^2\), so this range is respected.

Set \(p=d^2/R^2=100/121\) and \(H=h^2=2116/3025\).
The difference between the right and left sides of

\[
 (1+T/p)(1+HT)^2\le(1+pT)(1+T)^2
 \tag{20}
\]

has zero constant coefficient and the following positive coefficients
of T, T^2, T^3:

\[
 \begin{aligned}
 p+2-1/p-2H&=2631/12100,\\
 1+2p-2H/p-H^2&=4307991/9150625,\\
 p-H^2/p&=443136/1890625.
 \end{aligned}
\]

Thus (20) holds for all T>=0. Since
\(|b_t(x)|^2=(p+T)/(1+pT)\), (19)--(20) give

\[
 \frac{|b_t(x)|^2}{|b_t(v)|^2}
 \le\frac{(p+T)(1+HT)^2}{H(1+pT)(1+T)^2}
 \le\frac pH=\left(\frac{25}{23}\right)^2.
\]

Multiplication over all n factors proves (18); its exponential
relaxation uses \(\log(1+2/23)<2/23\). Equations (10), (18)
give

\[
 \sup_{v\in E}|F_z(v)|<500e^{2n/23}\quad(|z|=R).
 \tag{21}
\]

### 5. The finite-node error retains the factor 2m

Write \(w=v-x\) and \(f(w)=F_z(x+w)\). The positively
oriented ellipse in w coordinates is parameterized by

\[
 w=\frac{ir}{2}(\lambda+\lambda^{-1}),\qquad
 |\lambda|=\rho=\frac{\sqrt{26}+1}{5}>1.
 \tag{22}
\]

Its semiaxes are exactly s,b. Along it set
\(S_0(w)=ir(\lambda-\lambda^{-1})/2\); this is the branch
of \(\sqrt{w^2+r^2}\) asymptotic to w outside the vertical
segment. In particular \(dw/S_0=d\lambda/\lambda\).

Let \(P_m(w)=\prod_{k=1}^m(w-ir\cos((2k-1)\pi/(2m)))\).
The elementary Chebyshev recurrence gives, up to a nonzero constant,
\(P_m(w)=T_m(w/(ir))\), and
\(T_m((\lambda+\lambda^{-1})/2)
=(\lambda^m+\lambda^{-m})/2\).
Indeed the latter identity follows by induction from
\(T_0=1,T_1=t,T_{j+1}=2tT_j-T_{j-1}\); it gives precisely
the m distinct zeros listed in (2). Logarithmic differentiation yields

\[
 \frac{P_m'(w)}{mP_m(w)}
 =\frac1{S_0(w)}\frac{\lambda^{2m}-1}{\lambda^{2m}+1}
 =\frac1{S_0(w)}-
       \frac2{S_0(w)(\lambda^{2m}+1)}.
 \tag{23}
\]

By the residue theorem the contour integral of
\(f(w)P_m'(w)/(mP_m(w))\), divided by \(2\pi i\), is
\(m^{-1}\sum_k F_z(a_k)\). All poles are simple with residue
\(f(a_k-x)/m\), and f is holomorphic throughout the ellipse.
The analogous integral with \(1/S_0\) is \(A_n(z)\): under
(22) it becomes the integral of
\(f(ir(\lambda+\lambda^{-1})/2)d\lambda/\lambda\).
The integrand is holomorphic in the annulus between radii 1 and rho,
including neighborhoods of both circles. Contour deformation to
\(|\lambda|=1\), followed by \(\lambda=e^{i\theta}\),
gives \((2\pi)^{-1}\int_0^{2\pi}f(ir\cos\theta)d\theta\),
which equals (14). This also verifies the normalization at the two
traversals of the segment and at its endpoints.

Since \(|\lambda^{2m}+1|\ge\rho^{2m}-1\) and
\(\int_E|dw|/|S_0|=2\pi\), (21), (23) prove

\[
 \left|\frac1m\sum_k F_z(a_k)-A_n(z)\right|
 \le\frac{2\sup_E|F_z|}{\rho^{2m}-1}.
 \tag{24}
\]

Only m nodes and m unit residues occur in this formula; the exponent
2m is the exact Chebyshev identity, not an enlarged pole census.

For the rate, elementary differentiation and integration give

\[
 \log\rho=\int_0^{1/5}\frac{dt}{\sqrt{1+t^2}}
 \ge\frac1{\sqrt{26}}>\frac5{26}.
\]

For m>=3, \(2m\log\rho>15/13>1\), so
\(\rho^{2m}>e>2\) and
\((\rho^{2m}-1)^{-1}<2\rho^{-2m}\). Recalling n=3m,
we obtain the full-boundary error bound

\[
 \left|\frac1m\sum_k F_z(a_k)-A_n(z)\right|
 <2000\exp\left[-\left(\frac5{39}-\frac2{23}\right)n\right]
 =2000e^{-37n/897}.
 \tag{25}
\]

Both rates exceed the required 1/32. More specifically,
\(37/897-3/80=269/71760>0\), so (17), (25) and (7) give

\[
 \sup_{|z|=R}|Q_n(z)|
 <(144+2000)m e^{-3n/80}<720n e^{-3n/80}.
\]

### 6. Operator norm, limit, and qualifications

Scaling identifies this supremum with \(\|q_n\|_\infty\).
For every \(f\in H^2\), contractivity of orthogonal projection gives
\(\|H_{q_n}f\|_2\le\|q_nf\|_2
\le\|q_n\|_\infty\|f\|_2\). This proves (5) for the
largest operator norm, with no numerical spectral inference.

Since \(3/80-1/32=1/160\), (6) follows. The exponential dominates
n; for example \(e^{n/160}\ge(n/160)^2/2\). The subsequence
\(n=3m\), m odd, is unbounded and therefore suffices to refute a
lower constant/onset asserted for every sufficiently large n.

The positive quantities used in (12)--(13) are modulus comparisons,
not positive complex residues in q. The entire complex integrand is
retained in (14)--(25); both the continuous integral and finite-node
error are controlled uniformly on the whole boundary. No limit of
discrete measures, infinite-support theorem, spacing hypothesis or
positive complex measure has been introduced. The contour endpoints,
finite-grid correction, disk scale and residue census are all retained.

This stops the proposed synthetic anchor-line bound; the separate
audit below confirms its stated scope. Actual-Xi layer isolation, other-pole
control, admissible census and clearance, realization, an independent
useful boundary upper bound and all-degree signs remain unresolved.
Neither the old planar construction nor an actual-Xi obstruction is
silently substituted for the family (2).

### Verification record

Run from the active notebook:

```text
python3 scripts/one-sided-hankel/anchor-line-chebyshev-check.py
```

The script writes the full exact-rational certificate to
`scripts/one-sided-hankel/anchor-line-chebyshev-check.json`.
All four interval bounds, three factor-polynomial coefficients,
geometric margins, finite-grid constants, prefactors and exponent
comparisons passed. The complete load-bearing gain table, coefficient
margins and rates were inspected using the shared JSON inspector.
The achieved exponent is 3/80, the required exponent 1/32, and the
strict margin 1/160. The finite-node error exponent is 37/897.
This checks arithmetic, not the correctness of the analytic argument,
its source scope, or any actual-Xi data. The following conceptual audit
is separate from that arithmetic certificate.

### Independent conceptual audit — 2 November 2026

The audit reused the unchanged EXPLORE assessment and its inspected
primary-source scope. It read the full argument, C645g's exact spaces
and scaling, the construction checkpoint/history, the recorded stop,
and the complete arithmetic script. No new operator theorem, source
extension, pole hypothesis or actual-Xi input was used. The audit
reproduces the existing local result; it is not a new discovery.

**Geometry and singularities.** The nodes are m distinct simple poles,
with the anchor present exactly because m is odd. The squared clearance
margin is 2029/40000. The maximum in (9) occurs at c=-1/2, giving
377/200 and a squared disk margin 9/1600. These estimates apply to
the filled ellipse as well, since it is the convex hull of its boundary
and the squared norm is convex. The inverse product has poles only at
the imaginary-axis grid, outside the closed ellipse and the lune.
For each fixed n, F_z is holomorphic on a common neighborhood of
these compact sets for every boundary z; the positive distances in
(8) and (10) control the factor z-v uniformly.

**Arc gain and finite grid.** In (11), differentiation with respect
to y has numerator 2tU(U-r_0^2)(t^2-U), which is nonpositive.
Thus the upper endpoint gives the minimum modulus on the arc.
For (12), subtracting the denominator of G from its numerator gives
exactly r(U-t^2)[r(U+t^2)-2t(U-D)]; this verifies both the identity
and its sign, rather than only the four numerical margins. The
quadratic vertex is 21/32. Each interval [j/4,(j+1)/4) has at least
floor(n/4) grid points, with no endpoint counted twice. The logarithm
inequality applies since G>0. The factor 1/2 converts the squared
factor modulus to log modulus and gives exactly 3n/80-3/20.

**First square-root branch and endpoint deformation.** Throughout the
open lune, |y|<r and Re((v-x)^2+r^2)=h^2+r^2-y^2>0. The branch
in (15) therefore extends consistently from its positive values on the
open segment. Its endpoint zeros are simple. On a sufficiently small
connecting arc, |S| is bounded below by a constant times the square
root of endpoint distance, while |F_z| is bounded uniformly in z
for each fixed n. Thus those integrals are O_n(sqrt(epsilon))
uniformly in z and tend to zero. Uniformity in n of this limiting
operation is neither asserted nor needed: (15) is exact for each n,
and (16)--(17) give the subsequent estimates uniform in n and z.
The upward segment and upward left arc have the same integral by
the oriented closed boundary of the lune. The chord lengths on
|v|=r_0 give exactly the factor 1/2 in (16), and its two sine
arguments lie in [0,alpha], a subset of [0,pi/2]. The endpoint
singularities are integrable and the bound pi^2/2 is valid.

**Ellipse factor comparison.** The normalized disk identity
|1+i*tau*w|^2-|w-i*tau|^2=(1-tau^2)(1-|w|^2)>0
justifies 0<sigma<1. Completing the square yields center
i*tau*(1-sigma^2)/(1-sigma^2*T) and the radius in (19).
The center has zero real part, so the radius is at least h.
Solving that quadratic inequality gives the middle expression in
(19), including T=0. The square-root upper bound makes its denominator
at most 2(1+HT)/(1+T), proving the last inequality with the correct
direction. The three positive coefficients in (20) were independently
expanded and matched to the certificate. No sign of Im(v), separation
of poles or positivity of complex amplitudes enters this comparison.

**Second branch, winding and census.** In (22), lambda=rho*exp(i*theta)
gives w=-s*sin(theta)+i*b*cos(theta), a counterclockwise ellipse
traversed once. S_0 is the exterior branch asymptotic to w; on the
negative real ray it has the opposite sign to S in the first contour
argument. The proof never identifies these two branches. The explicit
identities dw/S_0=d(lambda)/lambda and (23) fix the sign and
normalization in the second argument. The intermediate lambda circles
map inside the filled ellipse, so the pullback of f is holomorphic
throughout a neighborhood of the closed annulus 1<=|lambda|<=rho.
Deformation to the unit circle is legitimate even at the two segment
endpoints. Its full period gives the arcsine average, not twice that
average. The logarithmic derivative has exactly m simple residues
1/m. The power 2m results from multiplying the exact rational identity
by lambda^m; it does not count additional poles or residues.

**Uniform rate and largest norm.** The lower bound log(rho)>5/26
and m>=3 imply rho^(2m)>2, so the denominator estimate in (24)
is uniform over the entire asserted family. The two decay rates are
3/80 and 37/897, with difference 269/71760>0. Multiplying the
average by m=n/3 gives prefactor 2144/3<720 in front of n.
The exact scaling (7) introduces no extra R; projection contractivity
then bounds the largest H2-to-H2_minus operator norm by the whole
boundary supremum. The unbounded odd-m subsequence gives the required
limit with strict exponent margin 1/160. No scalar or least-singular-
value observation substitutes for this bound.

The existing exact-rational script was replayed successfully. The full
selected certificate values /gain_table, /factor_polynomial_coefficient_margins,
/geometry, /bounds and /checks were inspected with the shared JSON
inspector. All checks passed. This analytic audit found no failed claim
or correction; it confirms only the synthetic stop (5)--(6). The
general named residue and projection inputs retain their cited source
scope; their general proofs and full Mathlib coverage were not newly
audited. Actual-Xi realization, usable upper bounds and signs remain open.

## Mathlib

Full matching Mathlib coverage for this exact inverse-grid-weighted
Chebyshev counterfamily and its uniform exponential bound was not
checked. No absence is inferred. The general residue theorem and
Hardy-space conventions are imported from the precise sources above;
no formalization or exhaustive coverage claim is made.
