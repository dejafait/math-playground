# Corollary 645k: the fixed one-third census still permits full Hankel cancellation

## Hypotheses

Use C645g's exact circle symbol and normalized Hardy-space convention,
at the fixed parameters

\[
 \delta=\frac14,\quad \eta=\frac1{100},\quad
 d=\frac54,\quad R=\frac{11}{8},\quad x=-d.
 \tag{1}
\]

For an integer \(m\ge8\), put \(n=3m\), \(t_j=j/n\) for
\(0\le j<n\), and

\[
 B_n(z)=\prod_{j=0}^{n-1}\frac{R(z-it_j)}{R^2+it_jz}.
 \tag{2}
\]

Define the rational parameters and the finite pole census

\[
 u=\frac{523}{400},\quad c=-u,\quad r=\frac{23}{400},\qquad
 a_k=c+r e^{2\pi i k/m}\quad(0\le k<m),\quad
 Z_n=\{a_0,\ldots,a_{m-1}\}.
 \tag{3}
\]

Give each pole the positive integer residue \(r_{a_k}=1\). These
are distinct simple poles. On the unit circle set, without changing
any complex phase,

\[
 q_n(\zeta)=\sum_{k=0}^{m-1}
   \frac{B_n(x)}{R B_n(a_k)}\frac1{\zeta-a_k/R},\qquad
 H_{q_n}f=P_-(q_nf):H^2\longrightarrow H^2_-.
 \tag{4}
\]

Circle measure is \(d\theta/(2\pi)\); \(H^2\) has nonnegative
Fourier modes and \(H^2_-\) strictly negative modes. No actual-Xi
realization, separation, interpolation, boundary upper estimate for
Xi, or sign assertion is assumed.

## Conclusion

The entire family is admissible for the fixed-third target:

\[
 x=a_0\in Z_n,\qquad |a_k|\le R-\eta,\qquad
 a_k\ne it_j,\qquad M=\sum_{a\in Z_n}r_a=m=\frac n3.
 \tag{5}
\]

In fact \(\Re a_k\le x\), although that extra restriction is not
needed in the target. The whole boundary and largest operator norm obey

\[
 \boxed{\displaystyle
 \|H_{q_n}\|\le\|q_n\|_\infty
       <2700n\exp\!\left(-\frac{253n}{8000}\right).}
 \tag{6}
\]

Consequently, along all \(n=3m\), \(m\ge8\),

\[
 e^{n/32}\|H_{q_n}\|
       <2700n e^{-3n/8000}\longrightarrow0.
 \tag{7}
\]

Thus no position-independent positive constant and onset can give
\(\|H_q\|\ge c_*e^{-n/32}\) for every census permitted by the
approved fixed \(\delta=1/4,\eta=1/100,M\le n/3\) target.
This is a synthetic obstruction, not a disproof of RH, a counterexample
to C645g's small-census conclusion, or a theorem about actual Xi.
The proof and exact arithmetic were completed on 1 November 2026.
A separate conceptual audit on that date verified the complete
argument without a mathematical correction; its checks appear below.
No certified novelty or RH resolution candidate is claimed.

## Proof

### Source scope and the changed quantitative step

The unchanged invocation-start
[EXPLORE assessment](../drafts/literature/2026-11-01-fixed-third-census-hankel.md)
covers exactly (1), (2), (4), the census \(M\le n/3\), and a
counterfamily satisfying (7). Its ready source comparison is reused.
C645i's audited \(M=10n\) counterfamily is a methodological comparison,
not a counterexample imported outside its hypotheses. Its much coarser
grid-variation estimate does not certify this census. Here the exact
combined logarithmic derivative gives a smaller uniform cost, and both
that cost and the product gain are evaluated at the new parameters.
This is why a fresh quantitative calculation is necessary.

Import the standard residue theorem, the simple-pole residue formula,
and the contour-integral inequality: R. W. Howell and J. H. Mathews,
*Complex Analysis*, online edition (front matter updated 22 August 2025),
[Section 8.1, Theorems 8.1.5 and 8.1.7](https://complexanalysis.org/web/sec_residue-thm.html),
and [Section 6.2, Theorems 6.2.18--6.2.19](https://complexanalysis.org/web/sec_contour-integrals.html),
as inspected in the reused coverage. The general theorems are not
reproved; their explicit kernel application is checked below. For the
normalized Hankel convention and contractive orthogonal projection,
reuse L. Baratchart, S. Chevillard and T. Qian, *Minimax principle and
lower bounds in H2-rational approximation*, J. Approx. Theory **206**
(2016), 17--47, [Section 4, (17)--(19)](https://arxiv.org/pdf/1501.01161v2)
(author preprint v2, 24 March 2015),
[DOI](https://doi.org/10.1016/j.jat.2015.03.004).
No Nehari/AAK theorem, least-singular-value claim, or numerical spectral
approximation is needed.

### 1. Admissibility and physical scaling

The \(m\) roots in (3) are distinct since \(r>0\), and

\[
 u-r=\frac54=d,\qquad u+r=\frac{273}{200}=R-\eta.
 \tag{8}
\]

Thus \(a_0=x\), \(\Re a_k\le-u+r=-d<0\), and
\(|a_k|\le u+r=R-\eta\). They avoid the entire imaginary-axis
grid. For \(|v|\le R\) and \(0\le t<1\),
\(|R^2+itv|\ge R^2-tR>R^2-R>0\). Hence \(B_n\) is
holomorphic near the closed physical disk and is nonzero at every
\(a_k,c,x\). All poles of \(q_n\) are strictly inside the unit
circle, making its boundary symbol continuous and bounded.

The factor \(1/R\) in (4) gives exactly

\[
 Q_n(z):=q_n(z/R)
       =B_n(x)\sum_{k=0}^{m-1}
          \frac1{B_n(a_k)(z-a_k)}.
 \tag{9}
\]

No residue multiplicity or scaling factor is discarded.

### 2. The combined grid derivative bounds the entire auxiliary disk

Choose

\[
 s=\frac{67}{1000},\qquad
 \frac rs=\frac{115}{134},\qquad
 R-u=\frac{27}{400},\qquad R-u-s=\frac1{2000}>0.
 \tag{10}
\]

For \(|w|\le s\), \(v=c+w\) lies strictly inside \(|v|<R\)
and has \(\Re v\le-u+s<0\). For
\(b_t(v)=R(v-it)/(R^2+itv)\), the exact identity is

\[
 \frac{b_t'(v)}{b_t(v)}
       =\frac{R^2-t^2}{(v-it)(R^2+itv)}.
 \tag{11}
\]

Both factors in the denominator are nonzero throughout this disk:

\[
 |v-it|\ge u-s>0,\qquad
 |R^2+itv|\ge\Re(R^2+itv)
      =R^2-t\Im v\ge R^2-ts\ge R^2-s>0.
 \tag{12}
\]

Since \(R^2-t^2>0\), (11)--(12) give

\[
 \left|\frac{b_t'(v)}{b_t(v)}\right|
       \le\frac{R^2-t^2}{(u-s)(R^2-s)}.
 \tag{13}
\]

Apply the ordinary derivative formula for the real logarithm of the
nonzero modulus along \(v=c+\theta w\), \(0\le\theta\le1\).
It yields

\[
 \log\left|\frac{b_t(c)}{b_t(c+w)}\right|
 =-\Re\int_0^1w\frac{b_t'(c+\theta w)}{b_t(c+\theta w)}d\theta
 \le\frac{s(R^2-t^2)}{(u-s)(R^2-s)}.
 \tag{14}
\]

This uses no choice of a complex logarithm branch and holds for every
complex \(w\) in the disk. With

\[
 D_0=(u-s)(R^2-s),\quad
 \gamma=\frac{s(R^2-1/3)}{D_0}
       =\frac{5008250}{108585927}<\frac7{150},\quad
 K=\frac{s}{2D_0}=\frac{536000}{36195309}<\frac1{50},
 \tag{15}
\]

the exact finite sum
\(\sum_{j=0}^{n-1}t_j^2=n/3-1/2+1/(6n)\) proves

\[
 \log\left|\frac{B_n(c)}{B_n(c+w)}\right|
 \le\gamma n+K-\frac{s}{6nD_0}
 <\frac{7n}{150}+\frac1{50}.
 \tag{16}
\]

The integer cross-product margins in (15) are respectively
\(7(108585927)-150(5008250)=8863989>0\) and
\(36195309-50(536000)=9395309>0\). In particular
\(|B_n(c)/B_n(c+w)|<2e^{7n/150}\), since
\(e^{1/50}\le(1-1/50)^{-1}<2\). The finite-sum correction and
the constant factor are retained; no limiting Riemann-sum assertion
is used for this upper bound.

### 3. A uniform full-boundary quadrature with the smaller census

Fix an arbitrary \(z\) on \(|z|=R\), and put

\[
 f_z(w)=\frac{B_n(c)}{B_n(c+w)(z-c-w)}.
 \tag{17}
\]

It is holomorphic near \(|w|\le s\), by (12) and
\(|z-c-w|\ge R-u-s=1/2000\). Thus (16) gives the bound,
uniform over the entire physical boundary,

\[
 \sup_{|w|=s}|f_z(w)|<4000 e^{7n/150}.
 \tag{18}
\]

The residue theorem applied on the positively oriented circle
\(|w|=s\) to
\(f_z(w)r^m/[w(w^m-r^m)]\) has only the enclosed simple
poles \(0\) and \(w_k=r e^{2\pi i k/m}\). The kernel has
residue \(-1\) at zero and \(1/m\) at each \(w_k\).
Consequently

\[
 \frac1m\sum_{k=0}^{m-1}f_z(w_k)-\frac1{z-c}
 =\frac1{2\pi i}\int_{|w|=s}
       f_z(w)\frac{r^m}{w(w^m-r^m)}\,dw.
 \tag{19}
\]

The contour inequality and \(|w^m-r^m|\ge s^m-r^m>0\)
give, with \(\theta_m=(r/s)^m\),

\[
 \left|\frac1m\sum_k f_z(w_k)-\frac1{z-c}\right|
 <4000 e^{7n/150}\frac{\theta_m}{1-\theta_m}.
 \tag{20}
\]

The elementary inequality \(\log(1-y)\le-y\), with
\(y=19/134\), and \(n=3m\) show

\[
 \theta_m\le e^{-19m/134}=e^{-19n/402}.
 \tag{21}
\]

For \(m\ge8\), \(19m/134\ge76/67>1\), so
\(\theta_m<e^{-1}<1/2\). Since
\(19/402-7/150=1/1675>0\), (20) becomes

\[
 \left|\frac1m\sum_k f_z(w_k)-\frac1{z-c}\right|
 <8000 e^{-n/1675}.
 \tag{22}
\]

Equations (9), (17), and \(|z-c|\ge R-u=27/400\) now give

\[
 |Q_n(z)|
 <m\left|\frac{B_n(x)}{B_n(c)}\right|
       \left(\frac{400}{27}+8000e^{-n/1675}\right)
 <2700n\left|\frac{B_n(x)}{B_n(c)}\right|.
 \tag{23}
\]

This estimate is for every \(|z|=R\), with uniform constants.
It retains the original complex inverse-grid amplitudes throughout.

### 4. The product gain exceeds the required rate

For real \(v\in[d,u]\) and \(0\le t\le1\), direct
differentiation of the nonzero factor modulus gives

\[
 D(v,t)=\frac{d}{dv}\log|b_t(-v)|
       =\frac{v}{v^2+t^2}-\frac{vt^2}{R^4+v^2t^2}.
 \tag{24}
\]

The first term decreases with \(v\), because
\(v\ge d>1\ge t\). The derivative with respect to \(v\)
of the second term before subtraction is
\(t^2(R^4-v^2t^2)/(R^4+v^2t^2)^2\ge0\), since
\(R^2>u\ge v\). Hence \(D(v,t)\ge D(u,t)=:f(t)\).
The function \(f\) decreases on \([0,1]\): its first term
decreases, and the second term before subtraction increases with
\(t\). It is positive, as is also evident from

\[
 f(t)=\frac{u(R^4-t^4)}{(u^2+t^2)(R^4+u^2t^2)}>0.
 \tag{25}
\]

The fundamental theorem of calculus in each of the finitely many
factors, followed by the left-endpoint rectangle inequality, gives

\[
 \log\left|\frac{B_n(c)}{B_n(x)}\right|
 =\sum_{j=0}^{n-1}\int_d^u D(v,j/n)dv
 \ge (u-d)\sum_{j=0}^{n-1}f(j/n)
 \ge rn\int_0^1 f(t)dt.
 \tag{26}
\]

Here \(u-d=r\). To evaluate a strict lower bound for the last
integral, use 64 right-endpoint rectangles and the following integers
\(b_k\), each satisfying \(f(k/64)\ge b_k/10000\).

| k | b_k (listed by increasing k) |
| --- | --- |
| 1--8 | 7646, 7640, 7630, 7616, 7598, 7577, 7551, 7522 |
| 9--16 | 7489, 7452, 7411, 7367, 7319, 7268, 7214, 7156 |
| 17--24 | 7095, 7031, 6963, 6893, 6820, 6744, 6666, 6584 |
| 25--32 | 6501, 6415, 6327, 6236, 6144, 6049, 5953, 5855 |
| 33--40 | 5756, 5654, 5552, 5448, 5343, 5237, 5129, 5021 |
| 41--48 | 4912, 4802, 4692, 4581, 4469, 4358, 4245, 4133 |
| 49--56 | 4020, 3907, 3795, 3682, 3569, 3456, 3344, 3232 |
| 57--64 | 3120, 3009, 2898, 2787, 2677, 2568, 2459, 2351 |

Every entry is a rational comparison in (25). More explicitly, if
\(f(k/64)=N_k/D_k\) in reduced form with \(D_k>0\), each
claim is the integer inequality \(10000N_k-b_kD_k\ge0\).
The exact-rational certificate stores all 64 values and their
nonnegative differences; the reproducible check below evaluates every
entry without floating point. The table sums to \(353938\), so

\[
 \int_0^1 f(t)dt
 \ge\frac1{64}\sum_{k=1}^{64}f(k/64)
 \ge\frac{353938}{640000}
 =\frac{176969}{320000}>\frac{11}{20}.
 \tag{27}
\]

Combining (26)--(27) proves, for every finite \(n\) in the family,

\[
 \log\left|\frac{B_n(c)}{B_n(x)}\right|
 >\frac{23}{400}\frac{11}{20}n
 =\frac{253n}{8000}.
 \tag{28}
\]

### 5. Largest-operator-norm bound, limit, and qualifications

The change of variables \(z=R\zeta\) identifies the boundary
suprema of \(Q_n\) and \(q_n\). Equations (23) and (28)
therefore give the stated uniform upper bound for \(\|q_n\|_\infty\).
Contractivity of \(P_-\) gives, for every \(h\in H^2\),

\[
 \|H_{q_n}h\|_2\le\|q_nh\|_2
       \le\|q_n\|_\infty\|h\|_2.
 \tag{29}
\]

This proves (6) for the largest operator norm. Since
\(253/8000-1/32=3/8000>0\), it proves (7). The limit follows
from exponential decay dominating \(n\); for example
\(e^{an}\ge (an)^2/2\) gives \(ne^{-an}\le2/(a^2n)\to0\)
for \(a=3/8000\). An asserted lower bound for every sufficiently
large integer \(n\) would also hold along the unbounded subsequence
\(n=3m\), contradicting (7).

The family obeys all prescribed synthetic hypotheses, including the
exact anchor, fixed clearance, distinct grid-avoiding poles, and
positive integer residues. No positive sign is assigned to the complex
weighted residues of \(q_n\). Their cancellation is controlled by
(19)--(23) on the whole circle, not by a single moment or a small
singular value. No actual-Xi census or realization is constructed.
This stops the universal fixed-third lower bound; it leaves C645g's
small-census theorem, possible restrictions arising from actual zeros,
other detectors, and the original RH target untouched.

### Verification record

Run from the active notebook:

```text
python3 scripts/one-sided-hankel/fixed-third-counterfamily-check.py
```

The script uses Python integer/Fraction arithmetic and writes the full
certificate to
`scripts/one-sided-hankel/fixed-third-counterfamily-check.json`.
It checked (8), (10), (15), the monotonicity parameter inequalities,
all 64 rational table entries and their sum in (27), both decay margins,
and the constants in (23). All checks passed. The actual lower rate is
\(253/8000\), versus the required \(1/32\), with margin
\(3/8000\); the quadrature error rate is \(1/1675>0\).
The script verifies arithmetic, not the analytic proof or any actual
Xi data. The subsequent separate conceptual audit is recorded next.

### Separate conceptual audit — 1 November 2026

This audit used the unchanged invocation-start EXPLORE assessment for
the exact fixed-third target. It read the entire proof (1)--(29),
C645g's hypotheses, symbol and scaling, the literal 64-entry table,
the arithmetic script, and the reused source hypotheses. C645i's
audited circle construction was checked as a method comparison, not
assumed to prove the new constants. No mathematical repair was needed.
The textbook title above was corrected to Howell--Mathews using the
already inspected source identity; theorem numbers and applications
are unchanged. The audit reproduces and verifies this local result;
it is not a new theorem beyond the sources checked.

**Admissibility and analyticity.** For every integer m>=8, n=3m>=24
satisfies the original n>=5 condition. The distinct polygon points
have unit original residues and total M=m. Equations (8) give the
exact anchor and closed clearance bound, including a possible leftmost
point on |a|=R-eta. The strictly negative real parts exclude all grid
zeros. Each factor denominator is nonzero throughout the physical
disk; thus all displayed symbol weights are defined. On |w|<=s,
the lower bounds u-s>0 and R^2-s>0 exclude both factors in (11),
and |z-c-w|>=1/2000 uniformly for |z|=R. These strict margins give
the pole-free neighborhood required for f_z in the residue theorem.
The scaling q_n(z/R)=Q_n(z) cancels exactly the single factor 1/R.

**Complex derivative and quadrature.** Subtracting
it/(R^2+itv) from 1/(v-it) gives exactly (R^2-t^2) divided by
their product. Positivity of that numerator holds for every grid
value. The real part of the second denominator is R^2-t Im(v),
so its lower bound R^2-s is valid everywhere on the auxiliary disk,
not just on the real diameter. Differentiating log|b_t| along the
straight segment proves (14) without a branch choice. The exact sum
of j^2/n^2 gives (16), including its constant and negative 1/n term.
Thus the bound for f_z is uniform in the external boundary point.

For the kernel r^m/[w(w^m-r^m)], the residue at zero is -1.
At each w_k it is r^m/[m w_k^m]=1/m. These are its only poles
inside |w|=s; f_z is holomorphic there. This verifies (19), including
the sign of f_z(0)=1/(z-c). On the contour its length 2*pi*s
cancels the 2*pi normalization and |w|=s, leaving exactly
theta_m/(1-theta_m). Equations (21)--(22) follow for every m>=8
from theta_m<=exp(-19n/402), 19m/134>1 and exp(1)>2.
The difference 19/402-7/150 is 1/1675, strictly positive.
No complex amplitude is replaced by its absolute value before the
residue identity, and no sample of the boundary substitutes for (18).

**Finite product gain and all arithmetic.** In (24), the v derivative
of the first term is negative since v>=d>1>=t. The v derivative
of the term being subtracted is nonnegative since R^2>u>=v and
t<=1. Thus D(v,t)>=D(u,t). In f(t), the first term decreases and
the subtracted term increases with t; (25) is positive even at t=1
because R^4>1. Accordingly the n left-endpoint rectangles bound
the integral from above in (26), and the 64 right-endpoint rectangles
bound it from below in (27). Both comparisons are for finite grids;
no asymptotic replacement of a sum is needed.

The original certificate was replayed. An independent exact check
then parsed all 64 integers from this proof and evaluated (25), using
its combined positive numerator rather than the script's difference
formula. For every k it verified 10000*N_k-b_k*D_k>=0 and checked
the original stored value, argument, lower integer, scale and rational
difference. All 64 rows agree, with integer sum 353938. The full
certificate, including every cross-product, is
`scripts/one-sided-hankel/fixed-third-counterfamily-audit.json`.
Reproduce it after the original check with:

```text
python3 scripts/one-sided-hankel/fixed-third-counterfamily-audit.py
```

The exact scalar checks give average 176969/320000>11/20,
gamma=5008250/108585927<7/150, K=536000/36195309<1/50,
and (400/27+8000)/3=216400/81<2700. Both integer margins in
(15) agree. The product rate is 253/8000>1/32, with margin
3/8000; the quadrature margin is 1/1675>0. Every check passed.
The executable replay verifies all rows, not a preview or a sampled
subset of the certificate. Analytic signs and uniformity are supplied
by the preceding argument, not by this arithmetic program.

**Norm and quantifiers.** The boundary estimate holds for all |z|=R,
and hence all |zeta|=1, with constants independent of m. Multiplication
by a bounded symbol on L2 followed by the contractive orthogonal
projection gives (29) for every H2 vector, in the stated normalized
spaces. This bounds the largest norm and does not assert equality
with the boundary supremum. For any proposed c_*>0 and onset,
the unbounded subsequence n=3m eventually has
2700*n*exp(-3*n/8000)<c_*, contradicting the lower bound.
All hypotheses of the approved synthetic target are respected.

The audit accepts the fixed-third obstruction. C645g supplies the
definition and scaling only; its lower-bound proof is not used.
C645i is methodological context, while C645h and C645j explain the
failed downstream bridge. The existing DAG row therefore stays
unchanged. No actual-Xi census, realization, independent upper bound
or sign has been proved, and this is not an RH candidate.

## Mathlib

Full matching coverage for this inverse-grid-weighted fixed-third
counterfamily is not checked. The named residue theorem, finite
geometric sums, exact rational arithmetic, and contractive orthogonal
projection are supporting standard facts, not a formalized match for
the new quantitative calculation. Unknown coverage is not evidence
of absence; no Lean verification is claimed.
