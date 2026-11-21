# L912: the fixed-grid quadratic full Hall cut is positive

## Hypotheses

Keep precisely L905's full actual-theta marginal, normalization A0>0,
x=16,y=0, four demands F={-2,-1,0,1}, and their five adjacent resources.
All theta indices and both transverse spatial directions are included.
Use the unchanged partition M=128, h=pi/(64M), 4096 t cells of width h
on [0,pi/2] and 1152 q cells of width 2h on [0,9pi/32].

Assume L037's outward Decimal arithmetic/exp/Machin-pi contracts and
trusted execution of the scripts below. Decimal precision is 70;
fixed-point interval accumulations use exact Python integers. This is
a computer-assisted calculation, not independently formally verified.
The separate critical review in step168 validates this finite certificate
under these arithmetic contracts; its complete replay is recorded below.
No RH, zero simplicity, total-transform sign or infinite allocation
is assumed.

## Conclusion

The full cut has the strict rational bounds

\[
 \frac{15}{10^6}<A_0H(F)<\frac{27}{10^6},\qquad
 \frac{69}{10^5}<H(F)<\frac{116}{10^5}.
 \tag{1}
\]

In particular H(F)>0. Together with L905's fourteen proper-cut signs,
this passes all fifteen necessary cuts for this selected block. The
conclusion supplies no infinite allocation, residual identity, other
lobe/height sign or higher mixed sign. It is a known-method numerical
specialization; no general mathematical novelty is claimed. The earlier
whole-box mesh stop remains correct for that method and budget.

## Proof

**Source use and application work.** The approved assessment is
`drafts/literature/2026-11-09-hall-full-cut-taylor-enclosure.md`.
The known validated-inclusion method is Makino–Berz, *Taylor Models and
Other Validated Functional Inclusion Methods*, IJPAM 4 (2003), publisher
PDF pp379–452, [Definitions 1–3, pp383–385; integration (2.7), p389;
Theorem 2 and its induction proof, pp390–391; Section 6, pp415–416](https://www.ijpam.eu/contents/2003-4-4/2/2.pdf).
Taylor's theorem with its third-order remainder and the standard
Cauchy derivative formula, NIST DLMF
[1.9(iii), (1.9.30)–(1.9.31)](https://dlmf.nist.gov/1.9#E31), supply
the elementary polynomial enclosure used here. All Cauchy circles are
inside the known holomorphic strip. These sources do not sign this
cut or provide its numerical constants. The following effective jet,
remainder and weighted-integration estimates are the necessary local
application; no general Taylor-model or matching theorem is reproved.

**The exact full cut.** Reuse L905's normalization, reflection and
absolute-domination argument. In its notation,

\[
 A_0H(F)=2\sum_{\ell=0}^4 B_\ell
 =2\int_0^{9\pi/32}\cos(16q)
       \left(2\int_0^\infty t^2 k(t+q/2)k(t-q/2)\,dt\right)dq,
 \tag{2}
\]

where k is the full even kernel, k(u)=K(|u|). The five B intervals
are exactly those of L905. No resource or demand is dropped.
L908's normalization proof gives k=4W on the real line. L910's
locally uniformly convergent theta series extends this k holomorphically
and evenly to |Im z|<pi/4. Thus (2)'s amplitude is smooth even on
rectangles meeting t=q/2; no reflected finite-head smoothness is used.

**Effective full-kernel Cauchy remainder.** Put c=7pi/8. L910's
closed-strip envelope, multiplied by four, is

\[
 |k(x+iy)|\le16\pi^2\exp(9r/2-ce^{2r}),\quad
 r=|x|,\quad |y|\le1/4.
\]

Since c>9/4, the exponent decreases for r>=0. Interval evaluation
certifies 16pi^2 exp(-c)<10.107<11. Every circle of radius 1/4
about a real point has its closed disk inside |Im z|<pi/4 and inside
the closed strip of this bound. Cauchy's formula therefore gives

\[
 |k^{(j)}(x)|\le j!4^j\,11\quad(x\in\mathbb R,\ j\ge0).
 \tag{3}
\]

For one rectangle let t0=(i+1/2)h, q0=(2j+1)h, u0=(i+j+1)h,
v0=(i-j)h, tau=t-t0, eta=q-q0. Then |tau|<=h/2, |eta|<=h and
du=tau+eta/2, dv=tau-eta/2 both have magnitude <=h.
Apply real one-variable Taylor's theorem to
g(s)=k(u0+s du)k(v0+s dv), 0<=s<=1. By (3),

\[
 \frac{|g'''(s)|}{6}
 \le\frac16\sum_{r=0}^3 {3\choose r}h^3
             (r!4^r11)((3-r)!4^{3-r}11)
 =256\,11^2h^3=:R.
 \tag{4}
\]

Hence the total-degree-two Taylor polynomial of the amplitude differs
pointwise by at most R, uniformly on every rectangle, including seam
rectangles. This is a remainder for the full analytic kernel, not a
piecewise polynomial approximation to a nonsmooth reflected head.

**Certified center jets, including their infinite theta tails.** On
u>=0 write v_n=pi n^2 exp(2u). The three derivative summands are
exp(u/2-v_n) P_r(v_n), r=0,1,2, with

\[
 P_0=8v^2-12v,\quad P_1=-16v^3+60v^2-30v,
 \quad P_2=32v^4-224v^3+330v^2-75v.
 \tag{5}
\]

The differential rule P -> 2vP'+(1/2-2v)P proves (5). Compact
termwise differentiation follows from L910's polynomial-Gaussian
majorants. L312 supplies uniform errors for the n<=4 heads through
order one: epsilon0=160000 exp(-75) and epsilon1=80000000 exp(-75).
For the missing second derivative, v>=3 gives

\[
 |P_2(v)|\le(32+224/3+330/9+75/27)v^4<147v^4.
\]

Since pi<4, the absolute n-th term is bounded by
37632 n^8 exp(17u/2-3n^2 exp(2u)). For n>=5 this exponent
decreases on u>=0, so its maximum occurs at zero. Successive
majorants 37632 n^8 exp(-3n^2) have ratio at most
(6/5)^8 exp(-33)<1/2. The complete second-derivative tail is therefore

\[
 2\cdot37632\cdot5^8e^{-75}
 <30000000000e^{-75}=:\epsilon_2.
 \tag{6}
\]

Evaluate all n<=4 summands of (5) with intervals at every nonnegative
lattice center kh, 0<=k<=5247, and add [-epsilon_r,epsilon_r].
Full evenness gives k^(r)(-u)=(-1)^r k^(r)(u). At zero use the exact
full identity k'(0)=0, after checking that the head-plus-tail interval
contains zero. Thus no finite-head derivative jump is differentiated,
even at a center on the seam. All three center-jet errors enter the
polynomial coefficient intervals. There is no additional finite-domain
value-tail error to pay after using these full-jet intervals and (4).

**Polynomial coefficients and weighted moments.** Denote center
derivatives by a_r=k^(r)(u0), b_r=k^(r)(v0). The coefficients of
1,tau,eta,tau^2,tau eta,eta^2 are respectively

\[
 a_0b_0,\quad a_1b_0+a_0b_1,\quad(a_1b_0-a_0b_1)/2,
\]
\[
 (a_2b_0+2a_1b_1+a_0b_2)/2,\quad
 (a_2b_0-a_0b_2)/2,\quad
 (a_2b_0-2a_1b_1+a_0b_2)/8.
 \tag{7}
\]

Integrate (7) by linearity against the separable signed weight
2t^2 cos(16q). These are exact signed polynomial moments; no positivity
assumption is imposed on the individual polynomial terms.
For d=h/2, J0=2d,J2=2d^3/3,J4=2d^5/5,

\[
 T_0=2(t_0^2J_0+J_2),\quad T_1=4t_0J_2,
 \quad T_2=2(t_0^2J_2+J_4).
 \tag{8}
\]

Here T_r=integral 2t^2(t-t0)^r dt over the cell. Put
s_A=sin(32jh), c_A=cos(32jh), s_B=sin(32(j+1)h),
c_B=cos(32(j+1)h). The q moments Q_r=integral cos(16q)(q-q0)^r dq are

\[
 Q_0=(s_B-s_A)/16,
\]
\[
 Q_1=h(s_B+s_A)/16+(c_B-c_A)/256,
\]
\[
 Q_2=h^2(s_B-s_A)/16+2h(c_B+c_A)/256
                       -2(s_B-s_A)/4096.
 \tag{9}
\]

For example, the antiderivatives for powers one and two in w=q-q0
are w sin(16q)/16+cos(16q)/256 and
w^2 sin(16q)/16+2w cos(16q)/256-2sin(16q)/4096;
these prove (9). Expanding 2(t0+tau)^2 proves (8).
The reused trigonometric helper encloses sin/cos by degree-49 Taylor
polynomials after exact integer-period reduction, checks radius<=4,
and adds radius^50/50!. Exact pi/2 endpoint values are used only after
containment checks. Machin pi is propagated through h, all centers,
weights and endpoints; there is no unaccounted endpoint strip.

**Exact accumulation and complete errors.** Convert each derivative
interval and each T_r,Q_r interval to outward integer endpoints at
scale S=10^40, using exact Fraction floor/ceiling. Multiply (7)'s
coefficients by eight before integer evaluation; all coefficients are
then integral combinations of products of jet intervals. Each cell's
coefficient-times-moment product has denominator 8S^4. Sum the lower
and upper integers exactly across all 4,718,592 cells. Both signs
are retained at every interval multiplication; fixed-sign cosine is
needed only for the absolute-weight error budget, not for the terms
in (7). Finally convert the exact integer totals back to outward
Decimal intervals. This includes coefficient, moment, pi,
trigonometric and fixed-point roundoff errors without dropping terms.

Let P denote twice the sum of the five polynomial lobe integrals.
Because the cosine zeros are exact cell boundaries,

\[
 \int_0^{9\pi/32}|\cos(16q)|dq=9/16,\qquad
 \int_0^{\pi/2}2t^2dt=\pi^3/12.
\]

The total error from (4), including (2)'s outer factor two, is

\[
 E_T=2R(\pi^3/12)(9/16).
 \tag{10}
\]

The script uses an outward sum of all strictly signed Q0 weights for
9/16. L905's uniform complete spatial-density error remains unchanged,

\[
 E_s=131072e^{-106}
 \left(9/(4\cdot231)+3/231^2+2/231^3\right).
\]

Thus the complete unbounded transverse contribution costs at most
E_space=2(9/16)E_s. Both transverse directions are already included
in L905's density. No q tail outside the specified lobes belongs to
this cut. The full enclosure is P+[-E_T-E_space,E_T+E_space].

**Certificate and numerical comparisons.** Reproduce the single
declared grid and degree with

```
python3 scripts/theta-marginal/full_cut_taylor_166.py
```

The complete certificate is `scripts/theta-marginal/full-cut-taylor-166.json`.
It records all 5248 full-jet center triples, all T/Q moment triples,
every exact lobe/term integer accumulator, analytic errors and
arithmetic metadata. The following are deliberately enlarged strict
rational enclosures of the saved complete fields:

| Quantity | Lower | Upper |
| --- | --- | --- |
| P | 0.0000210692395139 | 0.0000210692395140 |
| E_T | 0.0000050783896188 | 0.0000050783896189 |
| E_space | 0 | 134/10^45 |
| A0 H(F) | 0.0000159908498950 | 0.0000261476291328 |
| H(F) | 0.00069527353325 | 0.00115284233752 |

For normalization only, reuse L905's step139-audited positive A0
interval [0.02268101047464037726385090842105727470982455817118562165493224167957267,
0.02299936518530665454415554335237575455685097101203455571359683203274323].
The certificate pins its original M=128 source bytes by SHA256.
Positivity of the raw cut is independent of the width of this normalizer.
The full `/bounds`, `/result` and `/normalizer` fields were inspected,
not only a preview. Rational comparisons give (1). The checks script
below checks the saved exact aggregate/scaling and all moment consistency
against independent centered-polynomial/series expressions;
it is internal verification, distinct from the independent critical audit below.

```
python3 scripts/theta-marginal/check_full_cut_taylor_166.py
```

This fixes one finite sign left unresolved by whole-box inclusion.
It proves no criterion equivalent to RH, no all-block allocation and
no positivity for any additional mixed form. The degree and mesh were
not increased. The historical M=64/128 whole-box inconclusive evidence
is retained unchanged.

**Separate conceptual audit, 9 November 2026 — step168.** The exact audit
scope was approved before invocation in
`drafts/literature/2026-11-09-full-cut-quadratic-certificate-audit.md`.
The Taylor/Cauchy primary inputs above are reused. No new general theorem,
grid refinement, degree increase or neighboring-cut calculation is used.

First, L908's termwise normalization gives exactly k=4W, and L910's
even holomorphic series and envelope hold without a zero premise. For
negative real parts reflection changes the imaginary sign as well, staying
inside the same closed strip. Since 1/4<pi/4, every required closed disk
is contained in the holomorphic domain. The derivative of
9r/2-c exp(2r) is 9/2-2c exp(2r)<0 for r>=0. Thus the global constant
11 in (3) applies at every real point on every Taylor segment. Each
Leibniz term in |g'''|/6 contributes at most 64*121*h^3, and the four
terms give (4). This proves the full analytic remainder across the seam;
no smoothness of K_4(|u|) is needed.

The audit differentiated P0 by the stated differential rule twice and
checked (5). In (6) the coefficient is
32+224/3+330/9+75/27=1315/9<147. After pi^4<256 the n-th majorant is
37632 n^8 exp(17u/2-3n^2 exp(2u)); its logarithmic derivative in u is
17/2-6n^2 exp(2u)<0 for n>=5. The ratio of successive maxima is at most
(6/5)^8 exp(-33)<1/2, and twice the first maximum's coefficient is
29400000000<30000000000. The value and first-derivative tails in L312
were checked on the same u>=0 domain. These complete tails, local uniform
termwise differentiation, and full-kernel parity justify every center,
including the exact first derivative at zero.

The independent implementation is

```
python3 scripts/theta-marginal/audit_full_cut_168.py
```

It imports only the reviewed L037 arithmetic module, uses 100-digit
outward arithmetic for its independent setup, and keeps the original
70-digit certificate read-only. The underlying Decimal/exp implementation
is still trusted. The audit computes all 5248 center triples using
normalized formal series through order two: multiplication is convolution
and the exponential recurrence is
b_n=(sum_(j=1)^n j a_j b_(n-j))/n, obtained from B'=A'B.
Applied to exp(2(u+z)), exp((u+z)/2) and the four theta summands, this
computes the derivatives without using the printed P1/P2 expressions.
It adds all three full theta tails. At u=0 the unmodified full first-jet
interval contains zero; only then is it replaced by the exact parity value.
Every independently valid derivative interval is contained in its saved
fixed-point interval. Mere overlap is not used as verification.

All 4096 triples T_r are independently recomputed from

\[
 T_r=2h^{r+3}\int_{-1/2}^{1/2}(i+1/2+z)^2z^r\,dz.
\]

All 1152 triples Q_r are recomputed by integrating the centered expansion
of cos(16(q0+w)) through power 20 in w. Its coefficient cycle is
cos(16q0), -sin(16q0), -cos(16q0), sin(16q0), multiplied by 16^m/m!.
For r=0,1,2, Taylor's real remainder and absolute integration give

\[
 |Q_r-Q_r^{[20]}|
 \le \frac{2\,16^{21}h^{22+r}}{21!(22+r)}.
\]

The phase is exactly 16q0=(2j+1)pi/512. Independent trigonometric sums
use exact rational period reduction to [-pi,pi], degree-81 Taylor
polynomials (the degree-81 cosine coefficient is zero), and remainder
|x|^82/82!. Each resulting moment interval is contained in the original
fixed interval, including cells adjacent to cosine zeros. This auxiliary
series evaluates the same exact moments; the amplitude degree remains two.
The original endpoint formulas (9), radius-4 degree-49 trigonometric
remainder, and exact pi/2 endpoint replacements were also checked directly.

The six bivariate coefficients are generated independently by expanding
(tau+eta/2)^r(tau-eta/2)^s/(r!s!), for all r+s<=2, multiplying their
coefficients by eight. The generated integer matrix agrees with (7).
With these generated coefficients, exact sign-split interval multiplication
reconstructs all 4,718,592 cells from the now-validated arrays. This includes
662976 negative v0 centers and 1152 zero v0 centers. Every one of the
thirty exact lobe/term accumulator pairs is identical to the original.
The two jet factors and two moment factors account for S^4; multiplying
coefficients by eight accounts for the denominator 8S^4=8*10^160.
The outer factor two is applied once; 2t^2 is already in T_r.

The error budget is independently recomputed from the four Leibniz terms,
integral 2t^2=pi^3/12 and the exact absolute cosine integral 9/16.
For the unbounded t tail, L905's audited argument gives t-q/2>=23pi/64>0;
the full kernel product is at most 65536 exp(9t-6 exp(2t)). Enlarging to
t=3/2+w gives exponent <=-106-231w, and integrating 2t^2 gives exactly
E_s above. Both t directions and the q reflection are therefore counted
once each, and no finite-domain theta tail is silently omitted or paid
twice. All independently recomputed error intervals are contained in the
original bound fields. Exact rational checks also validate the original
polynomial/error addition, normalization and strict inequalities (1).

The normalizer source hash is
`b8878445443377d60d7af63f3981c477853027ca3e92e2ece237ce41eb902401`.
It agrees with the M=128 source hash in the complete step139 audit
`scripts/theta-marginal/variable-hall-audit-139.json`; that audit has no
failed checks. The A0 field is reused exactly and has positive lower
endpoint. No new normalizer calculation or normalization assumption is
substituted. The raw sign is established before division by A0.

Full independent setup arrays, generated coefficient matrix, all 1152
row/term accumulator pairs, all final accumulators and 34647 successful
checks are retained in `scripts/theta-marginal/full-cut-audit-168.json`.
There are no failed checks in this completed replay. Its full result,
error-budget and coefficient-matrix fields were inspected, and every
load-bearing array and accumulator was checked by the complete script.
The independently enclosed raw interval lies strictly within the original
interval and still satisfies the displayed rational bounds. This validates
the finite pass only, with the original arithmetic qualifications.

The first audit implementation mistakenly used (2j+1)pi/256 as its center
phase. The first Q0 containment check rejected it, after every center jet
and t moment had passed. The corrected denominator is 512 as derived
above. Preserve the failed audit code and certificate as
`scripts/theta-marginal/audit_full_cut_initial_phase_error_168.py` and
`scripts/theta-marginal/full-cut-audit-initial-phase-error-168.json`.
This was an error in the new audit, not a failure or repair of step166.
Only the corrected audit command above reproduces the accepted result.
The original calculation, its internal checks and historical whole-box
stops remain unchanged. Infinite allocation and mixed positivity remain
unproved; this is neither an RH criterion nor a complete candidate.

## Mathlib

Full matching result and supporting Taylor-model/interval-integration
coverage: not checked. No absence claim is made. The named standard
Cauchy formula and Taylor theorem are mathematical inputs with their
hypotheses verified above; Mathlib availability is not a completion
gate. The numerical part retains L037's explicit trusted arithmetic
qualifications.
