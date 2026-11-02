# Corollary 645g: a sparse positive-residue census preserves the half grid exponent

## Hypotheses

Fix

\[
 0<\delta<\tfrac12,\qquad 0<\eta<\tfrac\delta2,\qquad
 d=\tfrac32-\delta,\qquad R=\tfrac32-\tfrac\delta2,\qquad x=-d.
\]

For an integer \(n\ge5\), put \(t_j=j/n\), \(0\le j<n\), and
retain the exact complex product

\[
 B_n(z)=\prod_{j=0}^{n-1}\frac{R(z-it_j)}{R^2+it_jz},\qquad
 \Lambda=\int_0^1-\log\!left(
 \frac{R\sqrt{d^2+t^2}}{\sqrt{R^4+d^2t^2}}\right)dt.
 \tag{1}
\]

Let \(Z\) be any finite set of distinct points in
\(\{|a|\le R-\eta\}\), containing \(x\) and avoiding every
\(it_j\). Assign each point a positive integer \(r_a\), and set
\(m=|Z|\) and \(M=\sum_{a\in Z}r_a\). These are simple poles
with residue multiplicities, not poles of order \(r_a\).
Define the proper rational circle symbol

\[
 q(\zeta)=\sum_{a\in Z}
       \frac{r_a B_n(x)}{R B_n(a)}\frac1{\zeta-a/R}.
 \tag{2}
\]

Use \(\|h\|_2^2=(2\pi)^{-1}\int_0^{2\pi}|h(e^{i\theta})|^2
\,d\theta\), \(H^2\) with nonnegative Fourier modes, and
\(H^2_-\) with strictly negative modes. The Hankel operator is
\(H_qh=P_-(qh):H^2\to H^2_-\), with its operator norm.
No pole separation, symmetry, positivity of the complex amplitudes in
(2), actual-Xi realization or interpolating function is assumed.

## Conclusion

Define the explicit positive constants

\[
 s=\frac\delta{64},\qquad
 A=1+\log\frac{4R}{s}=1+\log\frac{256R}{\delta},\qquad
 \rho_* =\frac{d+2s}{R}<1,
 \tag{3}
\]
\[
 c_\delta=\frac{\sqrt{1-\rho_*^2}}{2s},\qquad
 \kappa_\delta=\frac\delta{16A},\qquad N=5.
 \tag{4}
\]

The calculation gives the more explicit intermediate bound

\[
 \|H_q\|\ \ge\ \|q\|_2
 \ \ge\ c_\delta\exp\!\left(-\frac{\delta n}{16}-Am\right).
 \tag{5}
\]

Consequently, whenever \(M\le\kappa_\delta n\),

\[
 \boxed{\displaystyle
 \|H_q\|\ge c_\delta e^{-\delta n/8}
                 \ge c_\delta e^{-\Lambda n/2}.}
 \tag{6}
\]

The constants are independent of \(n,Z,(r_a)\), all pairwise
distances, and even of the allowed fixed \(\eta\). This proves the
approved synthetic half-exponent statement. A separate conceptual audit
on 1 November 2026 verified (1)--(21) without a mathematical correction;
its complete checks are recorded below. It is a local partial result, with
no claim of certified novelty or an RH resolution candidate.

## Proof

### Source scope and the quantitative difference

The invocation-start
[EXPLORE assessment](../drafts/literature/2026-11-01-positive-residue-hankel-exponent-test.md)
covers exactly (1)--(2), including arbitrarily close poles and the
growing census. The inspected operator convention is L. Baratchart,
S. Chevillard and T. Qian, *Minimax principle and lower bounds in
H2-rational approximation*, J. Approx. Theory **206** (2016), 17--47,
[Theorem 2 and (17)--(19)](https://www.must.edu.mo/images/SCSE/qiantao/QianTao_P147.pdf),
[DOI 10.1016/j.jat.2015.03.004](https://doi.org/10.1016/j.jat.2015.03.004).
Its norm/distance identity and the finite rational matrix construction
do not themselves evaluate (6). Neither Nehari/AAK nor the model-space
theorem needs a reproof or a spectral calculation here: testing the
operator on the constant function suffices after the quantitative
estimate below. This is not an assertion that weighted residues are
positive or that the symbol is inner.

Import the standard residue theorem and simple-pole rule from R. W.
Howell and J. H. Mathews, *Complex Analysis*, online edition
(front matter updated 22 August 2025),
[Section 8.1, Theorems 8.1.5 and 8.1.7](https://complexanalysis.org/web/sec_residue-thm.html),
and the absolute contour-integral inequality from
[Section 6.2, Theorems 6.2.18--6.2.19](https://complexanalysis.org/web/sec_contour-integrals.html).
Their inspected scope and the same rational factors are recorded in
C645f; they are imported, not reproved. Only C645c's audited,
unconditional product-rate assertion \(\Lambda>\delta/4\) is used
from that corollary, at the last step. None of its conditional zeta
hypotheses or envelope conclusions is used.

The elementary finite Fourier, logarithm-integral and factor estimates
are included because they evaluate the missing census cost. They are
not an attempted new proof of the general operator theorems. C645d's
scalar cancellation and C645e/C645f's small-cluster bounds are
comparisons, not premises of the quantitative argument.

### 1. The exact scaling and a polynomial bound for the rational symbol

The geometry gives \(1<d<R<3/2\) and \(R>5/4\). For \(|z|\le R\),

\[
 |R^2+it_jz|\ge R^2-t_jR\ge R^2-R>0.
 \tag{7}
\]

Thus \(B_n\) is holomorphic on a neighborhood of the closed disk,
and its only zeros in that disk are the grid points. In particular
all \(B_n(a)\), including \(B_n(x)\), are nonzero. Every pole of
\(q\) lies strictly inside the unit circle, so \(q\) is bounded
and continuous on it and \(H_q\) is bounded. The geometric expansion

\[
 \frac1{\zeta-a/R}=\sum_{k=0}^\infty(a/R)^k\zeta^{-k-1}
 \qquad (|\zeta|=1)
\]

converges absolutely and uniformly, since \(|a|/R\le1-\eta/R<1\).
There are finitely many poles. Hence \(q\) has only strictly negative
Fourier modes, \(H_q1=q\), and \(\|q\|_2\le\|H_q\|\), with
\(\|1\|_2=1\). No least-singular-value estimate is involved.

In physical disk coordinates, the factor \(1/R\) in (2) gives exactly

\[
 Q(z):=q(z/R)=B_n(x)\sum_{a\in Z}\frac{r_a}{B_n(a)(z-a)}.
 \tag{8}
\]

Put \(D(z)=\prod_{a\in Z}(z-a)\). The function
\(T(\zeta)=D(R\zeta)q(\zeta)\) is a polynomial of degree at most
\(m-1\): in each summand of (8) exactly one linear factor cancels.
On \(|\zeta|=1\), each factor of \(D(R\zeta)\) has modulus
at most \(R+|a|\le2R\), and therefore

\[
 \|T\|_2\le(2R)^m\|q\|_2.
 \tag{9}
\]

Write \(T(\zeta)=\sum_{k=0}^{m-1}c_k\zeta^k\), inserting zero
coefficients if necessary. Finite Fourier orthogonality gives
\(\sum|c_k|^2=\|T\|_2^2\). For \(|z|<R\), Cauchy--Schwarz
and the geometric sum consequently give

\[
 \begin{aligned}
 |D(z)Q(z)|
 &\le\Bigl(\sum|c_k|^2\Bigr)^{1/2}
       \Bigl(\sum_{k=0}^{m-1}|z/R|^{2k}\Bigr)^{1/2}\\
 &\le\frac{(2R)^m\|q\|_2}{\sqrt{1-|z|^2/R^2}}.
 \end{aligned}
 \tag{10}
\]

At a pole this is a statement about the polynomial extension of
\(DQ\). We divide by \(D\) only on a circle without poles below.
The exact pole locations and complex amplitudes have not been altered.

### 2. A circle with a controlled full-denominator cost

For each \(a\in Z\), set \(u_a=|a-x|\). For any real \(u\),
substitution \(r=s+st\), \(v=(u-s)/s\), gives the finite improper
integral

\[
 \frac1s\int_s^{2s}\log\frac{2R}{|r-u|}\,dr
 =\log\frac{2R}{s}+\int_0^1-\log|t-v|\,dt
 \le 1+\log\frac{4R}{s}=A.
 \tag{11}
\]

Here is the complete uniform bound on the last integral. For
\(0\le v\le1\) its value, with \(0\log0=0\), is

\[
 1-v\log v-(1-v)\log(1-v)\le1+\log2.
\]

The entropy expression attains its maximum at \(v=1/2\), as follows
by differentiating on \((0,1)\) and taking its endpoint limits.
For \(v<0\), \(|t-v|\ge t\), so the integral is at most
\(\int_0^1-\log t\,dt=1\). For \(v>1\), comparison with
\(1-t\) gives the same bound. All possible singularities are
integrable logarithms, which justifies (11) at every \(u\).

Sum (11) over the finite set \(Z\). There exists
\(r\in[s,2s]\), different from every \(u_a\), for which

\[
 \sum_{a\in Z}\log\frac{2R}{|r-u_a|}\le Am.
 \tag{12}
\]

Indeed the average of this sum is at most \(Am\); away from its
finitely many logarithmic singularities it is continuous and finite,
so it cannot be strictly greater than \(Am\) everywhere there.
This selects a radius using all poles, including poles far from the
anchor. No spacing between any two \(a\)'s has been required.

On the entire circle \(\Gamma=\{|z-x|=r\}\), the reverse triangle
inequality gives \(|z-a|\ge|r-u_a|>0\). Exponentiating (12) yields

\[
 \frac{|D(z)|}{(2R)^m}
 \ge\prod_{a\in Z}\frac{|r-u_a|}{2R}\ge e^{-Am}
 \quad (z\in\Gamma).
 \tag{13}
\]

Also \(|z|\le d+2s<R\), since
\(R-d-2s=15\delta/32>0\). Combining (10) and (13),

\[
 \sup_{\Gamma}|Q|
 \le\frac{e^{Am}\|q\|_2}{\sqrt{1-\rho_*^2}}.
 \tag{14}
\]

The possible closeness of distinct poles or of their radial distances
only affects the chosen circle; the evaluated constant in (14) is
unchanged. This is the required uniformity, not a numerical preview
or a separation-dependent matrix inverse.

### 3. The exact grid weight on that local circle

Write \(z=x+h\), where \(|h|\le2s=\delta/32<1/16\). For each
\(0\le t=t_j<1\), the ratio of the corresponding factors in (1) is

\[
 \frac{1+h/(x-it)}{1+ith/(R^2+itx)}.
 \tag{15}
\]

Since \(|x-it|\ge d\) and \(|R^2+itx|\ge R^2\), its modulus is
at most \((1+|h|/d)/(1-|h|/R^2)\). The denominator here is positive.
For \(y\ge0\), \(\log(1+y)\le y\); for \(0\le y<1\),
\(-\log(1-y)\le y/(1-y)\). Thus the logarithm of this positive
upper bound is at most

\[
 |h|\left(\frac1d+\frac1{R^2-|h|}\right)
 \le 2|h|,
 \tag{16}
\]

because \(d>1\) and \(R^2-|h|>25/16-1/16=3/2\).
Multiplying the \(n\) bounds proves

\[
 \sup_{\Gamma}|B_n(z)|
 \le |B_n(x)|e^{2nr}\le|B_n(x)|e^{4ns}.
 \tag{17}
\]

No modulus was substituted for the complex factor in the definition
of the residues; (17) is only a bound on the multiplier along a contour.

### 4. A positive local residue sum and the explicit threshold

The disk bounded by \(\Gamma\) is strictly inside \(|z|<R\),
and \(\Gamma\) avoids every pole of \(Q\) by (12). Equation (7)
excludes all poles of \(B_n\) there. Multiplication of (8) by
\(B_n(z)\) gives at each \(a\in Z\) the exact simple-pole residue

\[
 \operatorname{Res}_{z=a}(B_nQ)=r_a B_n(x).
 \tag{18}
\]

All original poles are accounted for; those outside \(\Gamma\) are
holomorphic within it and are already included in the cost (14).
The grid points introduce no poles into \(B_nQ\). With the
counterclockwise orientation, the residue theorem therefore gives

\[
 \frac1{2\pi i}\int_\Gamma B_n(z)Q(z)\,dz
 =B_n(x)\sum_{|a-x|<r}r_a.
 \tag{19}
\]

The anchor lies strictly inside, and all \(r_a\) are positive
integers. Thus the sum on the right is a positive integer at least
one. This is the only noncancellation assertion: it concerns the
residues after multiplication by the exact \(B_n\), not the complex
weighted residues in (2).

The contour length is \(2\pi r\). Taking moduli in (19) and using
(14), (17), and \(r\le2s\), gives

\[
 \begin{aligned}
 |B_n(x)|
 &\le r\sup_\Gamma|B_n|\sup_\Gamma|Q|\\
 &\le\frac{2s|B_n(x)|}{\sqrt{1-\rho_*^2}}
           e^{4ns+Am}\|q\|_2.
 \end{aligned}
 \tag{20}
\]

Divide by the nonzero anchor modulus. Since \(4s=\delta/16\),
this proves (5). Positive integer residues also give \(m\le M\).
Under the census hypothesis in (6),

\[
 4ns+Am\le\frac{\delta n}{16}+AM
 \le\frac{\delta n}{16}+A\kappa_\delta n
 =\frac{\delta n}{8}.
 \tag{21}
\]

Finally import C645c's product-rate inequality
\(\Lambda>\delta/4\), valid without its conditional zeta data.
It implies \(\delta/8<\Lambda/2\), proving (6) for every integer
\(n\ge5\) with an allowed census. This supplies explicit constants,
not just positivity for each fixed configuration or an unevaluated
operator formula. If no census satisfies \(M\le\kappa_\delta n\)
for a small \(n\), that quantified case is simply empty; all
sufficiently large \(n\) admit at least the one-point census.

### Qualifications and remaining use

The norm comparison in (5) proves more than merely detecting a small
nonzero singular value: a fixed unit input to the full operator already
has the stated output norm. C645d's scalar sum can still vanish; the
local contour here changes its weight and counts positive residues
only after restoring \(B_n\). Arbitrarily close distinct simple poles
are included; a literal confluent higher-order pole is not a hypothesis.
No limiting passage to such a pole is used.

This proof concerns only the explicitly defined rational symbol. It
does not identify it with the Hankel operator of an actual residual
\(B_n(x)(F-P)/B_n\). That full principal-part and interpolation
application, an actual-Xi census meeting the small coefficient
\(\kappa_\delta\), contour clearance and realization, and a smaller
independent boundary upper bound remain unresolved. A general
\(O(\log\text{height})\) pole count does not supply this census
condition for a logarithmic grid. The argument neither establishes
actual-Xi signs nor removes the all-degree mixed-positivity gap.

The original proof attempt was recorded under the ready EXPLORE
comparison; the separate audit below reproduces and verifies it. Neither
step certifies originality beyond the sources checked. No mathematical
script or numerical evidence is needed for the finite calculation
(7)--(21). The downstream application remains separate from this audit.

### Independent conceptual audit — 1 November 2026

The unchanged invocation-start EXPLORE assessment covers this exact
norm target. This audit independently checked the complete proof,
including all quantified configurations, and accepts (5)--(6).
No new estimate, altered hypothesis or mathematical repair was needed.
The primary-source comparison was reused, including the precise residue
and contour statements recorded above. The operator result is used only
as a convention/comparison: the actual norm test is the constant input.

1. **Pole order, scaling and Hardy normalization.** Since
   \(R^2-t_jR>0\), the rational grid denominators cannot vanish
   anywhere on the closed disk. Grid avoidance makes every amplitude
   finite and nonzero. For each allowed configuration, the negative
   Fourier series converge absolutely and uniformly on the circle;
   this uses its positive \(\eta\), not a uniform bound on the
   amplitudes. Hence \(H_q1=q\) exactly and \(\|1\|_2=1\).
   The substitution \(\zeta=z/R\) cancels the amplitude's \(1/R\)
   against \((z/R-a/R)^{-1}=R/(z-a)\). Thus (8) has no missing
   scale or conjugation. In particular
   \[
   T(\zeta)=B_n(x)\sum_{a\in Z}\frac{r_a}{B_n(a)}
                      \prod_{b\in Z\setminus\{a\}}(R\zeta-b).
   \]
   This is a polynomial of degree at most \(m-1\), even if its
   leading coefficients cancel or the positive integer residues are
   arbitrarily large. Its coefficient norm is exactly the normalized
   circle norm in (9). Applying Cauchy--Schwarz to its finite sum gives
   (10), with \(1-|z|^2/R^2\) in the denominator. At a pole only
   the polynomial extension is evaluated; later division takes place
   on a circle avoiding all poles.

2. **One radius controls all poles and all angles.** The change of
   variables in (11) gives the stated expression for every real u.
   For \(v\in[0,1]\), splitting the integral at v gives precisely
   \(1-v\log v-(1-v)\log(1-v)\), including the endpoint limits.
   Its maximum is \(1+\log2\); for v outside that interval the
   comparisons with t or \(1-t\) give at most 1. Each integrand
   is absolutely integrable on this finite interval, so the finite
   sum can be integrated without any interchange issue. To justify
   existence in (12) explicitly, suppose the sum were greater than
   Am at every nonsingular radius. Its difference from Am would be
   nonnegative almost everywhere and, by continuity near any regular
   point, bounded below by a positive number on a nonempty interval.
   Its integral would then be strictly positive, contrary to (11).
   The selected radius therefore avoids all finitely many radial
   distances and satisfies (12). The reverse triangle inequality
   bounds every factor of D on the entire same circle, giving (13).
   Neither closeness between poles nor equal radial distances changes
   this argument. All poles, including those outside the local circle,
   enter its cost \(Am\).

3. **Interior and grid-factor constants on the full parameter range.**
   The exact clearance of the local circle is
   \(R-d-2s=15\delta/32>0\), so \(0<\rho_*<1\).
   Also \(|h|\le2s=\delta/32<1/16\), \(d>1\), and
   \(R^2-|h|>25/16-1/16=3/2\). The denominator in (15)
   has modulus at least \(1-|h|/R^2>0\). Consequently the
   logarithmic upper bound in (16) is at most
   \(|h|(1/d+1/(R^2-|h|))\le2|h|\), including h=0.
   Multiplication of these positive modulus bounds gives (17) with
   \(2nr\le4ns\). It does not require a complex logarithm branch,
   or replace any amplitude in q by its modulus. The bound (14)
   uses the interior evaluation factor at \(\rho_*\), not at a
   point approaching the outer boundary. This explains why the
   resulting lower-bound constants are independent of \(\eta\).

4. **Complete local residue accounting and the contour normalization.**
   All poles of Q are the specified distinct simple poles. The
   multiplier \(B_n\) is holomorphic on a neighborhood of the
   local closed disk and nonzero at each pole. It changes its residue
   to exactly \(r_a B_n(x)\); its grid zeros introduce no pole.
   The contour avoids all poles. The residue theorem thus applies
   with positive orientation and exactly the sum in (19).
   The anchor x is strictly inside since \(r\ge s>0\), so the
   sum is a positive integer at least one. Positivity is used for
   this restored residue sum only. Taking absolute values and using
   \(|dz|=r\,d\theta\) cancels the \(2\pi\) in the integral,
   leaving the factor r in (20), with no additional R. Combining
   (14) and (17), and dividing by \(|B_n(x)|>0\), gives exactly
   \(\sqrt{1-\rho_*^2}(2s)^{-1}e^{-4ns-Am}\).

5. **Census, rate and endpoint quantifiers.** Positive integer residues
   give \(m\le M\). Thus \(4s=\delta/16\) and
   \(A\kappa_\delta=\delta/16\) yield (21) exactly.
   C645c's inspected rate argument uses only d, R and the continuous
   positive real product integrand for this conclusion. Its conditional
   zero, zeta derivative and envelope data are not used. Its integral
   is exactly (1), so \(\Lambda>\delta/4\) supplies the claimed
   direction of the final exponential inequality. All constants are
   positive for each fixed allowed \(\delta\); no uniform positive
   census coefficient as \(\delta\downarrow0\) is asserted.
   For n with \(\kappa_\delta n<1\) the census hypothesis has
   no example, since x is present. This is a legitimate empty case;
   for all sufficiently large n the one-point unit-residue example
   satisfies it. There is no hidden large-n onset beyond N=5 in
   the quantified inequality.

The audit includes poles arbitrarily near one another, the grid or the
allowed outer radius, while retaining distinctness and grid avoidance.
It does not take a limit to higher-order poles, weaken the positivity
or integrality assumption, or identify q with an actual-Xi residual.
C645d's scalar cancellation remains compatible with the norm bound.
The only local mathematical theorem input remains C645c's unconditional
rate assertion; the DAG row therefore needs no change. Matching Mathlib
coverage and novelty beyond the inspected literature remain unchecked.

## Mathlib

Full matching coverage for this weighted sparse-census Hankel bound
has not been checked. The inspected sources are the primary operator
paper, the residue/contour statements recorded above, and C645c's
canonical product-rate argument. Supporting Mathlib Fourier,
polynomial, contour and logarithm results were not searched in this
step. No claim of absence or formal verification is made.
