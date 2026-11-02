# Corollary 645i: a one-sided circle census can beat the proposed Hankel exponent

## Hypotheses

Use C645g's exact complex symbol and normalized Hardy-space convention.
For this counterfamily fix

\[
 \delta=\frac25,\quad \eta=\frac1{100},\quad C=10,\quad
 d=\frac{11}{10},\quad R=\frac{13}{10},\quad x=-d,
 \qquad n\in\mathbb Z,\quad n\ge5.
 \tag{1}
\]

Thus \(d=3/2-\delta\), \(R=3/2-\delta/2\), and
\(0<\eta<\delta/2<1/4\). Put \(t_j=j/n\), \(0\le j<n\), and

\[
 B_n(z)=\prod_{j=0}^{n-1}\frac{R(z-it_j)}{R^2+it_jz}.
 \tag{2}
\]

Define

\[
 u=\frac{239}{200},\qquad c=-u,\qquad r=\frac{19}{200},
 \qquad m=10n,\qquad
 a_k=c+r\exp(2\pi i k/m)\quad(0\le k<m).
 \tag{3}
\]

Let \(Z_n=\{a_0,\ldots,a_{m-1}\}\), with residue \(r_{a_k}=1\)
at every point. These are distinct simple poles, not poles of higher
order. On the unit circle use exactly

\[
 q_n(\zeta)=\sum_{k=0}^{m-1}
       \frac{B_n(x)}{R B_n(a_k)}\frac1{\zeta-a_k/R},
 \qquad H_{q_n}f=P_-(q_nf):H^2\longrightarrow H^2_-,
 \tag{4}
\]

where circle measure is \(d\theta/(2\pi)\), \(H^2\) has nonnegative
Fourier modes, and \(H^2_-\) has strictly negative modes. There is no
actual-Xi, positive-real interpolation or sign hypothesis.

## Conclusion

Every family (3) satisfies the exact proposed one-sided geometry:

\[
 x\in Z_n,\qquad \Re a_k\le x,\qquad |a_k|\le R-\eta,\qquad
 a_k\ne it_j,\qquad M=\sum_{a\in Z_n}r_a=10n=Cn.
 \tag{5}
\]

Nevertheless, for every integer \(n\ge5\),

\[
 \boxed{\displaystyle
 \|H_{q_n}\|\le\|q_n\|_\infty
           <4100n\exp\!\left(-\frac{513n}{10000}\right).}
 \tag{6}
\]

In particular,

\[
 e^{\delta n/8}\|H_{q_n}\|
 <4100n\exp\!\left(-\frac{13n}{10000}\right)
 \longrightarrow0.
 \tag{7}
\]

Thus there cannot be a positive constant \(c_{\delta,\eta,C}\) and
an onset giving the proposed lower bound
\(\|H_q\|\ge c_{\delta,\eta,C}e^{-\delta n/8}\) for all admissible
families at every fixed \(\delta,\eta,C\): (1) supplies one fixed
parameter triple violating it. This does not contradict C645g's much
smaller census coefficient.

An independent conceptual audit on 1 November 2026 verified (1)--(23)
without a mathematical correction; its checks are recorded below.
This local counterfamily stops the synthetic universal claim, not RH,
all Hankel detectors, or a theorem about actual Xi. The source search
does not certify originality.

## Proof

### Source scope and purpose of the calculation

The unchanged invocation-start
[EXPLORE assessment](../drafts/literature/2026-11-01-one-sided-pole-hankel-census.md)
explicitly covers an admissible asymptotic counterfamily to (7)'s
opposite lower-bound claim, with arbitrary fixed linear census
coefficient, arbitrarily close distinct poles and the exact complex
weights. Reuse its one-sided-source comparison and the saved
full-pole operator assessment; no new theorem-level coverage is assumed.

Import the standard residue theorem and simple-pole residue rule from
R. W. Howell and J. H. Mathews, *Complex Analysis*, online edition
(front matter updated 22 August 2025),
[Section 8.1, Theorems 8.1.5 and 8.1.7](https://complexanalysis.org/web/sec_residue-thm.html),
and the contour integral inequality from
[Section 6.2, Theorems 6.2.18--6.2.19](https://complexanalysis.org/web/sec_contour-integrals.html).
Their inspected cases were reused in C645g. The normalized Hankel
convention and orthogonal Riesz projections are those of
L. Baratchart, S. Chevillard and T. Qian, *Minimax principle and lower
bounds in H2-rational approximation*, J. Approx. Theory **206** (2016),
17--47, [Section 2 and (17)--(19)](https://www.must.edu.mo/images/SCSE/qiantao/QianTao_P147.pdf),
[DOI 10.1016/j.jat.2015.03.004](https://doi.org/10.1016/j.jat.2015.03.004),
as inspected in the saved assessment. The approval also inspected the
accessible [author preprint, arXiv:1501.01161v2](https://arxiv.org/pdf/1501.01161v2),
24 March 2015, Section 2 pp.2--3 and (17) p.7, for the same normalized
spaces and projection convention. Only the contraction bound is used.

Neither Nehari/AAK nor a general quadrature theorem is reproved. The
residue theorem is applied below to one explicit kernel; its residues,
analyticity and norm costs are checked because they decide the exact
weighted question. C645g supplies the exact rescaling in (8), not its
census-cost estimate. C645d's scalar cancellation and C645h's boundary
interpretation are comparisons, not mathematical inputs to (6).

### 1. Admissibility and exact physical scaling

The points in (3) are distinct because \(r>0\) and the \(m\)-th
roots of unity are distinct. At \(k=0\),
\(a_0=-239/200+19/200=-11/10=x\). For every k,

\[
 \Re a_k\le -u+r=x<0,\qquad
 |a_k|\le u+r=\frac{129}{100}=R-\eta.
\]

They therefore avoid every imaginary-axis grid point. Each residue is
the positive integer one, so \(M=m=10n\), proving (5).
For \(|z|\le R\), \(0\le t_j<1\),

\[
 |R^2+it_jz|\ge R^2-R>0.
\]

Consequently \(B_n\) is holomorphic near the closed disk, with zeros
only at the grid. In particular \(B_n(a_k)\), \(B_n(x)\), and
\(B_n(c)\) are finite and nonzero. All poles of (4) are strictly
inside the unit circle, so its boundary symbol is continuous and
bounded, and \(H_{q_n}\) is a bounded operator.

The exact physical-coordinate identity of C645g (8) gives

\[
 Q_n(z):=q_n(z/R)
     =B_n(x)\sum_{k=0}^{m-1}\frac1{B_n(a_k)(z-a_k)}.
 \tag{8}
\]

The factor \(1/R\) in (4) cancels against
\((z/R-a_k/R)^{-1}=R/(z-a_k)\); no additional scale or conjugate
is introduced.

### 2. A uniform full-boundary residue quadrature

Set \(s=1/10\); this is an auxiliary radius, not a complex
coordinate. Then

\[
 0<r<s,\qquad \frac rs=\frac{19}{20},\qquad
 R-u-s=\frac1{200}.
 \tag{9}
\]

For a fixed arbitrary \(z\) on \(|z|=R\), consider

\[
 f_z(w)=\frac{B_n(c)}{B_n(c+w)(z-c-w)}.
 \tag{10}
\]

It is holomorphic on a neighborhood of \(|w|\le s\). Indeed,
\(|c+w|\le u+s=259/200<R\), so the grid denominators do not
vanish; also \(\Re(c+w)\le-u+s=-219/200<0\), excluding every
grid zero. Finally

\[
 |z-c-w|\ge R-u-s=\frac1{200}.
 \tag{11}
\]

For \(0\le t<1\), the ratio of the single grid factors at c and
c+w is exactly

\[
 \frac{1+itw/(R^2+itc)}{1+w/(c-it)}.
\]

On \(|w|\le s\), its modulus is at most
\((1+s/R^2)/(1-s/u)\), since \(|R^2+itc|\ge R^2\) and
\(|c-it|\ge u\). The elementary inequalities
\(\log(1+y)\le y\) for \(y\ge0\), and
\(-\log(1-y)\le y/(1-y)\) for \(0\le y<1\), give

\[
 \log\left|\frac{b_t(c)}{b_t(c+w)}\right|
 \le s\left(\frac1{R^2}+\frac1{u-s}\right)
 =s\,\frac{55700}{37011}<2s=\frac15,
 \quad b_t(v)=\frac{R(v-it)}{R^2+itv}.
 \tag{12}
\]

Hence \(|B_n(c)/B_n(c+w)|\le e^{n/5}\), and (11) yields the
uniform bound

\[
 \sup_{|w|=s}|f_z(w)|\le200e^{n/5}.
 \tag{13}
\]

Apply the imported residue theorem on the counterclockwise circle
\(|w|=s\) to

\[
 f_z(w)\frac{r^m}{w(w^m-r^m)}.
\]

Its only enclosed poles are 0 and \(r\exp(2\pi i k/m)\).
At 0 the kernel's residue is \(-1\); at a root \(w_k^m=r^m\),
it is \(r^m/(w_k\,m w_k^{m-1})=1/m\). Every pole is simple
and lies strictly inside the contour; \(f_z\) is holomorphic there.
It follows exactly that

\[
 \frac1m\sum_{k=0}^{m-1}f_z(r e^{2\pi i k/m})-f_z(0)
 =\frac1{2\pi i}\int_{|w|=s}
            f_z(w)\frac{r^m}{w(w^m-r^m)}\,dw.
 \tag{14}
\]

The contour inequality, its length \(2\pi s\), and
\(|w^m-r^m|\ge s^m-r^m>0\) give

\[
 \left|\frac1m\sum_k f_z(r e^{2\pi i k/m})
                 -\frac1{z-c}\right|
 \le 200e^{n/5}\frac{(19/20)^m}{1-(19/20)^m}.
 \tag{15}
\]

For \(m=10n\), use \(\log(1-1/20)\le-1/20\) to obtain
\((19/20)^m\le e^{-n/2}\). For \(n\ge5\) this is less than
1/2: \(e^{5/2}\ge1+5/2>2\). Thus the right side of (15) is
at most \(400e^{-3n/10}\). Since
\(|z-c|\ge R-u=21/200\), (8), (10), and (15) give

\[
 \begin{aligned}
 |Q_n(z)|
 &\le m\left|\frac{B_n(x)}{B_n(c)}\right|
        \left(\frac{200}{21}+400e^{-3n/10}\right)\\
 &<4100n\left|\frac{B_n(x)}{B_n(c)}\right|.
 \end{aligned}
 \tag{16}
\]

Every estimate holds for the entire boundary \(|z|=R\), uniformly
in z and n. No weighted residue was replaced by a positive number.
The cancellation in (14) retains the full complex \(B_n(a_k)\).

### 3. A strict product exponent, with rational bounds

For a real \(v\in[d,u]\) and \(0\le t\le1\), the logarithmic
derivative of the grid-factor modulus at \(-v\) is

\[
 D(v,t):=\frac{d}{dv}\log|b_t(-v)|
       =\frac{v}{v^2+t^2}-\frac{v t^2}{R^4+v^2t^2}.
 \tag{17}
\]

It decreases with v on this rectangle. The derivative of its first
term is \((t^2-v^2)/(v^2+t^2)^2<0\), since \(v\ge d>1\).
The derivative of the second term before subtraction is
\(t^2(R^4-v^2t^2)/(R^4+v^2t^2)^2\ge0\), since
\(R^4>u^2\ge v^2t^2\). Consequently \(D(v,t)\ge D(u,t)\).
Also \(f(t):=D(u,t)\) decreases on \([0,1]\): its first
term decreases with t, and the term being subtracted increases.
It is positive, as can also be read from

\[
 f(t)=\frac{u(R^4-t^4)}
                 {(u^2+t^2)(R^4+u^2t^2)}>0.
 \tag{18}
\]

Both facts are statements about real logarithms of nonzero moduli;
no complex logarithm branch is being chosen. The fundamental theorem
of calculus applied to each factor in the finite product gives

\[
 \log\left|\frac{B_n(c)}{B_n(x)}\right|
 =\sum_{j=0}^{n-1}\int_d^u D(v,j/n)\,dv
 \ge (u-d)\sum_{j=0}^{n-1}f(j/n).
 \tag{19}
\]

As f is decreasing, the left-endpoint rectangles give
\[
 \frac1n\sum_{j=0}^{n-1}f(j/n)\ge\int_0^1 f(t)\,dt
       \ge\frac18\sum_{k=1}^8 f(k/8).
 \tag{20}
\]

Here is a finite rational verification of the last threshold. In
the table \(f(k/8)=N_k/D_k\), with \(D_k>0\), and
\(1000N_k-b_kD_k>0\); hence \(f(k/8)>b_k/1000\).

| k | \(N_k\) | \(D_k\) | \(b_k\) | \(1000N_k-b_kD_k\) |
| --- | --- | --- | --- | --- |
| 1 | 174732684900 | 212757543401 | 821 | 58741767779 |
| 2 | 3490172448 | 4495483021 | 776 | 1677623704 |
| 3 | 34707536980 | 49103168593 | 706 | 40699953342 |
| 4 | 21365452800 | 34506704737 | 619 | 5802567797 |
| 5 | 165411684900 | 317886962093 | 520 | 110464611640 |
| 6 | 77694311200 | 186471824653 | 416 | 122032144352 |
| 7 | 27776536980 | 88715988157 | 313 | 8432686859 |
| 8 | 709772640 | 3328628033 | 213 | 774868971 |

These values follow by substituting \(u=239/200\), \(R=13/10\)
in (17); the positive integer cross-products make the comparisons
independent of floating-point arithmetic. Their sum yields

\[
 \frac18\sum_{k=1}^8f(k/8)>
 \frac{821+776+706+619+520+416+313+213}{8000}
 =\frac{137}{250}>\frac{27}{50}.
 \tag{21}
\]

Since \(u-d=19/200\), (19)--(21) imply

\[
 \log\left|\frac{B_n(c)}{B_n(x)}\right|
 \ge \frac{19}{200}\frac{27}{50}n
 =\frac{513n}{10000}.
 \tag{22}
\]

The strict rational margin in (21) is more than required. Equations
(19)--(22) hold for every finite n; they do not invoke a limit of
Riemann sums or discard their discretization error.

### 4. The whole operator and the failed uniform lower bound

The map \(z=R\zeta\) identifies the full boundary maxima of \(Q_n\)
and \(q_n\). Equations (16) and (22) thus bound
\(\|q_n\|_\infty\) as in (6). For every \(f\in H^2\), the
orthogonal projection convention gives

\[
 \|H_{q_n}f\|_2
 \le\|q_nf\|_2\le\|q_n\|_\infty\|f\|_2.
 \tag{23}
\]

This proves the bound on the largest operator norm, without identifying
it with a boundary norm or using a least singular value.
Since \(\delta/8=1/20=500/10000\), multiplication by
\(e^{\delta n/8}\) proves (7). Its limit follows, for example,
from \(e^{an}\ge (an)^2/2\) for \(a=13/10000>0\), giving
\(n e^{-an}\le2/(a^2n)\to0\).

If the proposed lower bound held at the fixed parameters (1), its
positive constant would bound the left side of (7) from below for
every sufficiently large integer n. Equation (7) contradicts that
claim. The family respects every stated synthetic assumption even
though its pole distances shrink as n grows; no lower pole-separation
bound was assumed.

### Verification, relevance and limitations

The exact rational arithmetic is reproducible from the active notebook:

    python3 scripts/one-sided-hankel/circle-counterfamily-arithmetic.py

The complete certificate is
[circle-counterfamily-arithmetic.json](../scripts/one-sided-hankel/circle-counterfamily-arithmetic.json).
It records every table entry and cross-product, parameter margins,
the factor constant, the actual/required exponents and all failures.
Fourteen exact rational checks passed. Its full load-bearing table was
inspected with the shared JSON inspector. The script checks arithmetic
only; it does not prove the analytic identities, justify hypotheses,
or replace the full argument (8)--(23). No numerical norm experiment
is used as evidence for an asymptotic assertion.

The construction retains a rightmost anchor but distributes a linear
number of poles around a circle on its left. The explicit residue
quadrature shows why their full weighted boundary function can
approximate the center term exponentially well. This defeats the
arbitrary-fixed-C claim without contradicting a sparse-census theorem,
and is materially different from C645d's scalar cancellation.

Actual-Xi rightmost-anchor selection, complete counts and clearance,
realization, interpolation and a sufficiently small independent
boundary upper bound remain unresolved. No proposed Xi realization
of (3), off-line zeta zero or RH resolution candidate is supplied.
Any replacement for the stopped synthetic claim needs an additional
quantitative restriction or a different mechanism, assessed separately.

### Independent conceptual audit — 1 November 2026

The separate audit used the invocation-start SPECIALIZE assessment
[approved for this exact family](../drafts/literature/2026-11-01-c645i-one-sided-counterfamily-audit.md).
It read all of (1)--(23), C645g's definitions and scaling, the arithmetic
script and the complete load-bearing certificate values. No mathematical
correction was needed. The textbook attribution above was corrected from
Beck et al. to Howell--Mathews; the linked theorem numbers are unchanged.

**Geometry and analyticity.** The radius is positive, the polygon points
are distinct, and its rightmost point is exactly x. The maximum modulus
bound is 129/100=R-eta, including the leftmost point, so every pole
stays at least eta from |z|=R. Residues of the underlying simple
poles are the integers one; the residues of q remain complex. Their
nonvanishing follows from grid avoidance, not a positivity assertion.
On |w|<=s the image c+w lies in |v|<=259/200<R with real part at most
-219/200. This excludes both grid zeros and grid-factor denominators.
The remaining denominator has modulus at least 1/200 uniformly for
every |z|=R. These strict margins give an open neighborhood on which
f_z is holomorphic, as required by the imported contour theorem.

**Quadrature and its uniform error.** Direct cancellation gives (8),
with exactly one 1/R canceled. For the kernel in (14), multiplying by w
and evaluating at zero gives -1; division by the derivative m*w_k^(m-1)
at w_k gives 1/m. Thus the signs and normalization in (14) are correct.
The kernel has no other poles in the auxiliary disk. On its boundary,
the contour length 2*pi*s cancels the 2*pi and the factor |w|=s;
the remaining factor is precisely (r/s)^m/(1-(r/s)^m).
The single-factor ratio in (12) retains both complex numerator and
denominator. Its logarithmic bound is s*(55700/37011)<1/5;
combined with (11) this proves (13) uniformly in z. With m=10n and
n>=5, (r/s)^m<=exp(-n/2)<1/2, so the complete error in (15) is at
most 400*exp(-3n/10). There is no sampled-boundary or limiting argument.
Finally 10*(200/21+400)=86000/21<4100 proves the strict prefactor in
(16), even after discarding the extra exponential decay of this error.

**Finite-grid exponent.** Differentiating the real log modulus gives
(17). Throughout d<=v<=u and 0<=t<=1, v>t and R^4>u^2>=v^2*t^2;
these signs make D decrease with v. The first term of f decreases with t,
and the subtracted term increases, so both rectangle inequalities in
(20) have the stated directions, for every finite n. Positivity in (18)
also holds at both endpoints since R^4>1. The script was replayed and
all eight exact fractions, all eight positive cross-products, parameter
values, exponent values and fourteen check results were inspected with
the shared JSON inspector. They agree with the canonical table. The
lower rectangle average is 137/250>27/50, and multiplication by
u-d=19/200 gives (22). A floating-point approximation to the integral
is not used in this verification.

**Operator norm and quantifiers.** Each q_n is continuous on the full
unit circle. Multiplication by q_n has norm at most its boundary
supremum on L2, and P_- is an orthogonal projection; hence (23) applies
to every H2 input. This is an upper bound for the largest operator norm,
not an identification with the boundary norm or a small singular value.
The achieved exponent 513/10000 exceeds delta/8=500/10000 by
13/10000. The polynomial prefactor is absorbed by the strictly positive
exponential gap as in (7), along all integers n>=5. Thus every proposed
positive constant and onset at this fixed parameter triple is refuted.

The audit accepts this local stop. C645g's symbol/scaling is the only
local lemma input; its sparse lower bound is not used. The other
corollaries discussed above are comparisons. No DAG edge changed.
No actual-Xi pole selection, census, clearance, interpolant or useful
boundary upper bound has been obtained, and this is not an RH candidate.

## Mathlib

Full matching coverage for this exact weighted regular-polygon
counterfamily is not checked. The residue theorem, elementary finite
product calculus and contractive orthogonal projection are standard
inputs; no particular Mathlib declaration or local Lean replay is
claimed. Unknown coverage is not evidence of absence.
