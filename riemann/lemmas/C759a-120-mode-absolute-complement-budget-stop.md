# C759a: The fixed 120-mode absolute complement estimate is insufficient

## Hypotheses

Use the complete unneutralized Weil form Q of L744(6), with L741's
full-line normalization, on real L2(-1,1), extended by zero. Write

\[
 F_f(t)=\int_{-1}^1 f(x)e^{-itx}\,dx,\qquad
 m(t)=\Re\psi(1/4+it/2)-\log\pi,
\]
\[
 Q(f)=\int m(t)|F_f(t)|^2\frac{dt}{2\pi}
 +2F_f(i/2)F_f(-i/2)
 -2\sum_{n\in\{2,3,4,5,7\}}a_n C_f(\log n),
 \quad a_n=\frac{\Lambda(n)}{\sqrt n}.
 \tag{1}
\]

Here C_f(u)=integral f(x+u)f(x)dx and Lambda(p^r)=log p. These are
all overlapping prime powers: log7<2<log8. The real closed form is
the closure of its smooth compact restriction. The imported realization
and core theorem is Suzuki, *Weil's quadratic form via the screw
function*, [arXiv:2606.09096v2](https://arxiv.org/html/2606.09096v2),
Theorem1.1, Corollary1.2 and Sections3.2,4.1-4.2,4.5. Its small-window
positivity theorem is not used. Form-domain specialization is given below.

Fix N=120. In the odd sector retain exactly
V=span{sin(pi*j*x):1<=j<=N}, and let W be its L2 orthogonal
complement in the full odd space. The even trial 1/sqrt2 belongs to
the prescribed even block span{1/sqrt2,cos(pi*j*x):1<=j<=120}.
No smooth minimizer, neutrality, RH, finite-to-infinite spectral
extrapolation, or source positivity certificate is assumed.

The conditional Schur criterion to be tested is Andrews--Connes--La
Gatta, *The uncertainty operator, the Weil ground state and the zeros
of zeta*, [arXiv:2611.13129v1](https://arxiv.org/html/2611.13129v1),
Lemma8.16 with its form-dual coupling hypothesis. After shifting by
tau it requires a strictly positive complementary lower bound before
the finite Schur estimate can be used. Its generic criterion is imported,
not reproved; this attempt stops at that prerequisite.

## Conclusion

Define the following *lower-estimate coefficients*, not eigenvalues:

\[
 \begin{split}
 m_*&=-\log(4\pi)-4,\\
 C&=\sqrt2 a_2+a_3+a_4+a_5+a_7,\\
 P_N&=\frac{8\sinh^2(1/2)}{\pi^2N},\\
 h(T)&=\log\frac{T}{2\pi}-\frac2{T^2},\\
 p(T)&=\min\left\{1,
  \frac{4T}{\pi^3N(1-(T/(121\pi))^2)^2}\right\},\\
 \ell(T)&=(1-p(T))h(T)+p(T)m_*-C-P_N,
                  \qquad 1\le T<121\pi.
 \end{split}                                                    \tag{2}
\]

For every w in the full form domain intersected with W,

\[
 Q(w)\ge\ell(T)\|w\|_2^2.                                     \tag{3}
\]

The complete interval certificate proves

\[
 \begin{gathered}
 0.052852<Q(1/\sqrt2)<0.053831< U:=0.054<\tau:=0.055,\\
 C\in(3.12925,3.12926),\quad P_N\in(0.0018341,0.0018343),\\
 \ell(100)\in(-1.517752,-1.517751),\qquad
 \sup_{1\le T<121\pi}\ell(T)<-0.1561.                         \tag{4}
 \end{gathered}
\]

Thus this entire threshold family supplies no positive shifted
complementary bound, for **any nonnegative shift**, even after using
the finite shift-chain improvement over the crude prime norm sum.
In particular it cannot supply d>0 for the indicated even trial and
tau. The prescribed certificate stops at N=120 without computing B
or the finite Schur matrix. Optimizing the even Ritz vector would not
repair this lower-estimate family at a nonnegative shift.

This is a negative result about this sufficient estimate only.
An upper bound on ell is **not** an upper bound on the odd Rayleigh
infimum. No failure of the actual parity inequality, no failure of
every possible 120-mode certificate, no even simplicity/sign and no
Xi realization or RH conclusion follows. A negative even trial and
a different lower-bound mechanism have not been excluded. This is a
REPRODUCTION under the saved source scope, not a novelty claim. The
analytic and computational argument passed the separate conceptual
audit in Section6; this establishes the scoped method stop only.

## Proof

### 1. Domain, parity and the complete split

L741(13),(16)-(17), used at arbitrary fixed length in L744(5)-(6), give

\[
 m(t)=\tfrac12\log(1+t^2)-\log(2\pi)-\Re\widehat r(it),
 \qquad \|r\|_1\le\log2+4.                                  \tag{5}
\]

Consequently m differs from the nonnegative logarithmic weight by a
bounded function, and m(t)>=m_*. The prime operators and pole
functionals on the fixed interval are bounded in L2. The form norm
of Q after a sufficiently large scalar shift is therefore equivalent
to the supported Fourier norm

\[
 \|f\|_{\mathcal V}^2=\int
   (1+\tfrac12\log(1+t^2))|F_f(t)|^2\frac{dt}{2\pi}.          \tag{6}
\]

Its space is complete: a Cauchy sequence converges in weighted Fourier
L2 and in physical L2, and the support condition is closed. Smooth
compact functions are dense here. Explicitly, contract support by
f_r(x)=r^(-1/2)f(x/r), r<1, then mollify inside the resulting margin.
On Fourier transforms dilation gives r^(1/2)F_f(rt). For 1/2<r<1
the logarithmic weights after change of variable are uniformly
comparable, so dilation converges strongly first on compactly supported
Fourier functions and then by density. The bounded mollifier multiplier
converges pointwise to1; dominated convergence gives norm convergence.
This identifies the weighted domain with the closure in the cited
Suzuki theorem at this interval, without extending L741's particular
length-log3 positivity theorem.

Reflection is an isometry of (6) and leaves every term of (1) invariant.
The projections (f(x)+/-f(-x))/2 are bounded in that norm and preserve
the smooth core. Applying them to a core approximation proves that
the smooth parity infima equal the closed parity infima. Fourier
transforms of each zero-extended sine, cosine and constant are bounded
near0 and O(1/|t|) at infinity, hence belong to (6); endpoint jumps
in the even basis cause no domain defect.

The finite L2 projection onto V is bounded in the form norm because
each of its finitely many vectors has finite form norm and its
coefficients are bounded by the L2 norm. Thus the form domain splits
into V and its intersection with W. The latter is closed in the form
norm and L2-dense in W: apply I-P_V to the dense odd domain. The
complementary restricted form is closed and semibounded. These facts
pay the domain/core prerequisites, but supply no positive d or
quantitative form-dual coupling estimate.

### 2. The entire Fourier complement, without a tail truncation

The sine system s_j(x)=sin(pi*j*x), j>=1, is an orthonormal basis of
the real odd L2 space. For |t|<j*pi direct integration gives

\[
 F_{s_j}(t)=\frac{2i(-1)^j j\pi\sin t}{j^2\pi^2-t^2}.       \tag{7}
\]

For unit w in W its L2 sine coefficients satisfy sum_{j>N}|c_j|^2=1.
The functional f->F_f(t) is continuous on supported L2, so the
Fourier transform of the partial sums converges at each t. Applying
Cauchy--Schwarz to (7), for |t|<=T<121*pi, yields

\[
 |F_w(t)|^2\le
 \frac{4\sin^2t}{\pi^2(1-(T/(121\pi))^2)^2}
            \sum_{j>N}\frac1{j^2}
 \le\frac{4}{\pi^2N(1-(T/(121\pi))^2)^2}.                  \tag{8}
\]

The last inequality is the decreasing-integrand comparison with
integral_N^infinity x^(-2)dx. This accounts for every omitted sine
mode. Plancherel and integration of (8) give low-frequency mass at
most p(T), including the cap by total mass1.

L744(8), from [DLMF5.11.2](https://dlmf.nist.gov/5.11.E2) and its
[sector remainder](https://dlmf.nist.gov/5.11#ii), gives
m(t)>=log(|t|/(2*pi))-2/t^2 for |t|>=1. This expression increases
with |t|, so the high-frequency mass has symbol at least h(T).
The certificate verifies h(1)>m_*; monotonicity gives h(T)>m_* for
all admissible T. Using (5) on the low mass proves the archimedean
lower coefficient (1-p(T))h(T)+p(T)m_*. All integrals are legitimate
on (6); no termwise prime or zero sum is being taken.

### 3. Complete prime cost and projected odd pole

Translate the interval to (0,2) and let T_d be the right shift with
zero extension. Decompose it into fibers x=t+kd, 0<=t<d. If
2d<2<3d, each fiber has at most three coordinates; if d>1 it has
at most two. For three coordinates,

\[
 |2\Re(z_0\overline z_1+z_1\overline z_2)|
 \le\sqrt2(|z_0|^2+|z_1|^2+|z_2|^2),                     \tag{9}
\]

by |z_0+z_2|<=sqrt(2)(|z_0|^2+|z_2|^2)^(1/2) and 2ab<=a^2+b^2.
For two coordinates the corresponding constant is1 by the same
last inequality. Integrating over fibers proves the bounds for
T_d+T_d^*. The enclosed delay inequalities show that n=2 uses
sqrt2, and n=3,4,5,7 use1. Multiplication by their positive a_n and
the triangle inequality give the complete lower arithmetic cost -C.
This bound holds on the full space and hence on W. It does not set
any delay to zero or assume independent prime phases.

For odd real w put g(x)=sinh(x/2). Its pole product in (1) is
-2|<w,g>|^2. Since w is orthogonal to the first N sine modes, only
g's sine tail contributes. Direct integration gives

\[
 \langle g,s_j\rangle=
 -\frac{2(-1)^j j\pi\sinh(1/2)}{j^2\pi^2+1/4}.
\]

Parseval, Cauchy--Schwarz and sum_{j>N}j^(-2)<=1/N give
2|<w,g>|^2<=P_N||w||^2. Thus both poles, including their negative
odd sign, have been retained. Combining all three estimates proves
(3). This proof concerns the entire complementary form, not a large
finite approximation.

### 4. Failure for every threshold in this estimate family

Let p_100=p(100); the certificate gives 0<p_100<1. The un-capped
expression defining p increases on (0,121*pi), hence so does p.
For 1<=T<=100 the archimedean mixture is at most h(T), which is
strictly below log(100/(2*pi)). Discarding the negative pole cost
therefore gives the upper bound on ell

\[
 E_1=\log(100/(2\pi))-C.
\]

For 100<=T<121*pi use h(T)<H:=log(121/2), m_*<-5 and p(T)>=p_100.
Since H+5>0, this gives the second upper bound

\[
 E_2=(1-p_{100})H-5p_{100}-C.                               \tag{10}
\]

Interval evaluation gives E_1<-0.3619 and E_2<-0.1561119.
This proves the uniform inequality in (4), including near the first
omitted frequency where the mass cap is1. It is a continuum argument
with two interval cases, not a sampling of T. Subtracting tau>=0
only worsens the bound. Failure here precedes, and does not prejudge,
any exact Schur-complement sign or the sign of the full odd form.

### 5. Even trial and full interval certificate

The general defining entries in Connes--Consani--Moscovici,
*Zeta Spectral Triples*, [arXiv:2511.22755v1](https://arxiv.org/html/2511.22755v1),
Lemma2.3 and (4.2)-(4.4), are used with lambda=e, L=2 and the
zero mode. L759's general integral reduction supplies the scalar
calculation, but none of its different-window numerical enclosures
is reused. The normalized constant has C_f(y)=1-y/2 for 0<=y<=2.
With rho(y)=exp(y/2)/(2*sinh y), define

\[
 B=\int_0^2\rho(y)(1-e^{-y/2})dy,\quad
 D_0=\int_0^2 y\rho(y)dy.
\]

The exact trial value is

\[
 16\sinh^2(1/2)-\gamma-\log(4\pi\tanh1)-2B+D_0
              -\sum_n a_n(2-\log n).                       \tag{11}
\]

This retains the source exterior archimedean correction and both
poles. For b_k=2k+1/2 the geometric series for rho gives

\[
 \begin{split}
 B&=\sum_{k\ge0}\left[
 \frac{1-e^{-2b_k}}{b_k}
 -\frac{1-e^{-2(b_k+1/2)}}{b_k+1/2}\right],\\
 D_0&=\sum_{k\ge0}\left[
 \frac{1-e^{-2b_k}}{b_k^2}-\frac{2e^{-2b_k}}{b_k}\right].
 \end{split}                                                \tag{12}
\]

The underlying integrands are nonnegative, so Tonelli justifies
these identities. Since 0<=1-e^{-y/2}<=y/2, after k=0,...,511
the B tail lies in [0,R_2/2] and the D_0 tail in [0,R_2], where
R_2=b_512^(-2)+1/(2b_512). This follows by integration to infinity
and the decreasing sum-integral comparison. No numerical quadrature
or infinite-series truncation without a bound is used.

Reproduce from the notebook with

    python3 scripts/spectral-triples/complement-budget-793.py

The full artifact is `scripts/spectral-triples/complement-budget-793.json`.
It records every finite series term, analytic tail bounds, constants,
complete prime list, all decisive intervals, checks, failures and script
hash. Arithmetic uses 60-digit Decimal outward intervals. ln, exp and
sqrt are expanded by adjacent representable endpoints, following the
correct-rounding semantics documented in the
[Python Decimal reference](https://docs.python.org/3/library/decimal.html)
and the already assessed L759 convention. Machine arithmetic is a
software trust assumption, not a formal proof of the interpreter.

Pi uses Machin's identity and 60 alternating arctangent terms with
the next-term remainder. Gamma uses H_128-log128-1/(2*128)+1/(12*128^2),
with radius 1/(60*128^4): this is L759's Euler--Maclaurin enclosure
at m=2, from [DLMF2.10.1](https://dlmf.nist.gov/2.10.E1) and the
[periodic Bernoulli bound](https://dlmf.nist.gov/24.8.E1). All rounding
and analytic tail errors enter (11) before its comparison with U.
Every final certificate check passes. These bounds certify only one
even trial; they do not approximate or order the full infima by two
Ritz values.

The first execution is preserved as
`scripts/spectral-triples/complement-budget-793-first-pass.json`.
It failed an unnecessarily asserted C>3.13 check: the calculated
enclosure is about3.12925229. The final check uses C>3.129; the
uniform stop uses the entire enclosed C, not that coarse bound.
The trial upper/shift were tightened from0.1/0.11 to0.054/0.055.
No failed mathematical evidence was discarded.

### 6. Separate conceptual and arithmetic audit (13 November 2026, step795)

The unchanged SPECIALIZE assessment
`drafts/literature/2026-11-13-full-weil-complement-budget-audit-793.md`
authorizes this exact audit. The variational/core and conditional Schur
inputs retain the precise citations above. This is REPRODUCTION of a
standard-method specialization, not a new sign theorem or an independent
audit of every cited source proof. No mathematical correction was needed.

**Closed domain and parity.** Formula(5) follows from L741's full-line
identities, as explicitly specialized to arbitrary finite L in L744;
the length-log3 positivity assertion is never used. Its bounded remainder
gives exactly m_*=-log(4pi)-4. Boundedness of the five shifts and the
two evaluation functionals makes the shifted form norm equivalent to(6).
For the core argument, the dilation operators are uniformly bounded in
weighted Fourier L2 for 1/2<r<1. Strong continuity is first checked on
continuous compactly supported Fourier functions, which are dense in
that weighted space, and then extended by uniform boundedness. This
justifies the density step in Section1 even when f is only in the form
domain. A nonnegative smooth mollifier of integral1 has Fourier multiplier
of modulus at most1; choosing its support smaller than the contracted
margin proves the asserted approximation without crossing the endpoints.
It may be chosen even and real. Reflection preserves(6), the pole product
and C_f(d), so parity projection preserves the core and the norm limit.
For a nonzero limit the L2 denominators also converge, proving equality
of the smooth and closed Rayleigh infima. The finite sine projection is
bounded from L2 into the form domain; its complement therefore gives a
closed semibounded restricted form and a dense domain in W. None of
these statements supplies complement positivity or a coupling estimate.

**Complete complement and arithmetic factors.** Each sine has L2 norm1
on(-1,1). Formula(7), including its sign, follows by integrating the
two exponentials. Fourier evaluation at any real t is a bounded L2
functional, with norm at most sqrt2. Thus convergence of sine partial
sums suffices for the Cauchy--Schwarz bound(8); pointwise convergence
of an arbitrarily differentiated Fourier series is not assumed.
Integration over an interval of length2T against dt/(2pi) gives exactly
4T/(pi^3 N(1-(T/(121pi))^2)^2). The cap by1 is Plancherel, and
sum_(j>120) j^-2<=1/120 accounts for the entire tail. The cited
L744(8) remainder applies for |t|>=1; h increases there, and its minimum
h(1)>m_* is certified. Since h-m_*>0, replacing the actual low mass
by its *upper* bound p makes the archimedean lower estimate smaller,
which is the required direction.

On the length2 interval, the log2 fibers have at most three entries;
the other four delays have at most two. The strict enclosed delay
inequalities certify these lengths. Their adjacency forms have bounds
sqrt2 and1 respectively by(9), including shorter fibers. The operator
sum is A=sum_n a_n(T_(log n)+T_(log n)^*), so the prime contribution
is -<Aw,w>, with no missing factor2. All prime powers below e^2 are
2,3,4,5,7; n=6 has Lambda(6)=0 and log8>2 excludes every later delay.
For odd real w, F_w(i/2)=<w,sinh(x/2)> and F_w(-i/2) is its negative.
Squaring the displayed sine coefficients and multiplying by2 gives
exactly P_N=8sinh^2(1/2)/(pi^2 N). These checks preserve the unfavorable
pole sign and every omitted sine mode.

**Uniform bound direction.** On the first threshold interval the
mixture is at most h(T)<log(100/(2pi)). On the second, replace h by
H=log(121/2) and m_* by -5, both upwards. The resulting expression is
H-p(T)(H+5), decreasing in p because H+5>0. Replacing p(T) by p(100)
therefore increases it. This proves(10) also when the cap has reached1.
Dropping -P_N increases both estimates. The two cases cover the entire
half-open threshold range, with the first omitted frequency excluded
as required by(7)-(8). These are upper bounds on the *produced lower
coefficient*. They give no upper bound on an odd eigenvalue or Rayleigh
infimum, and failure of this certificate is not a failure of Lemma8.16.

**Even trial and analytic errors.** The constant has norm1,
C_f(y)=1-y/2, and F_f(plus or minus i/2)=2sqrt2 sinh(1/2).
Its pole contribution is consequently16sinh^2(1/2), and the full
prime contribution is -sum a_n(2-log n). In L759's general diagonal
entry set n=0,L=2: S_0=C_0=0, 2D_0/L=D_0, and the exterior factor
(e^L-1)/(e^L+1) is tanh1. This gives exactly(11), including the sign
of the archimedean contribution and its exterior correction.
The expansion rho=sum exp(-(2k+1/2)y) has nonnegative terms. The
nonnegative B and D_0 integrands justify Tonelli at y=0, not just
away from that endpoint. Each omitted D_0 integral is at most b_k^-2;
each omitted B integral is at most b_k^-2/2. The decreasing integral
comparison gives R_2=b_512^-2+1/(2b_512) exactly. The gamma enclosure
uses m=2 in L759's stated Euler--Maclaurin bound: since B_4=-1/30,
2|B_4|/(4*128^4)=1/(60*128^4). All upper-endpoint derivative terms
vanish and the remainder integral is absolutely convergent. Machin's
identity has the usual first-quadrant branch; after60 terms the
alternating remainder is bounded by (1/k)^121/121 for k=5,239.
No numerical quadrature or favorable remainder sign is needed.

**Implementation and all certificate entries.** Every line of the
original script was checked. Decimal inputs are exact integers or
decimal strings. Basic interval arithmetic uses explicit floor/ceiling
contexts; negation uses copy_negate, avoiding ambient rounding. General
interval multiplication and reciprocal bounds have the correct endpoint
directions. All actual divisors exclude0 and all logarithm/square-root
arguments are positive. For ln,exp,sqrt, the documented correctly rounded
result expanded to adjacent representable endpoints encloses the exact
value. The exponent range used here is well inside the normal range
even at k=511. Integer powers and sums introduce no binary float input.

Run from the notebook:

    python3 scripts/spectral-triples/complement-budget-audit-795.py

The original script and both original certificates remain unchanged.
An exact-byte copy is replayed under ambient Decimal precision7 into
`scripts/spectral-triples/audit-795/`; its parsed certificate matches
the saved final certificate in every field, including every series row.
The audit separately uses exact Fraction interval arithmetic, 90-digit
outward Decimal transcendental endpoints, rational Machin sums and a
rational Euler--Maclaurin radius. It checks containment of independently
computed enclosures in every saved constant, prime row, all512 B/D_0
rows, all aggregate trial details and all decisive bounds. No preview
or success flag substitutes for these complete comparisons.

The full audit certificate is
`scripts/spectral-triples/complement-budget-audit-795.json`:
2105 checks, zero failures. In particular the published uniform bound
is verified at -0.1561, stronger than the generator's coarse -0.14
boolean. The entire trial interval lies strictly between0.052852 and
0.053831, below U=0.054<tau=0.055. The first-pass C>3.13 failure is
still preserved, and its decisive uniform ceiling equals the final
one exactly. Both interval implementations retain the common Decimal/
libmpdec and Python arithmetic trust assumptions; this is not a formal
verification of those libraries. It is also not a finite eigenspectrum
certificate. Full odd coercivity, form-dual coupling, Schur sign, parity
ordering, even simplicity, Xi realization and global signs remain open.

## Mathlib

Full matching coverage for this localized Weil form, its source
realization, or the quantitative complement bound has not been checked.
Plancherel, Fourier sine completeness and finite-dimensional quadratic
inequalities are supporting standard inputs; no matching Mathlib
theorem is asserted. Unknown coverage is not evidence of absence.
