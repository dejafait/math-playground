# Corollary 645e: a uniform lower bound for three scaled pole moments

## Hypotheses

Retain C645d's exact complex product and synthetic cluster geometry.
Explicitly, let

\[
 0<\delta<\tfrac12,\qquad d=\tfrac32-\delta,\qquad
 R=\tfrac32-\tfrac\delta2,\qquad x=-d,
\]
\[
 n\in\mathbb Z,\quad n\ge5,\qquad t_j=j/n\ (0\le j<n),\qquad
 B_n(z)=\prod_{j=0}^{n-1}\frac{R(z-it_j)}{R^2+it_jz}.
 \tag{1}
\]

Let \(Z\) be a set of one, two or three distinct points containing
\(x\). Every additional point \(z\) satisfies

\[
 |z-x|<\delta/8,\qquad -\tfrac32<\Re z<-1,\qquad |z|<R.
 \tag{2}
\]

All points avoid the grid \(\{it_j:0\le j<n\}\), and every point
has assigned residue one. For \(k=0,1,2\), set

\[
 M_k=B_n(x)\sum_{z\in Z}\frac{[n(z-x)]^k}{B_n(z)}.
 \tag{3}
\]

For \(k=0\), the weight is identically one, including at \(x\).
There is no separation assumption, Xi realization, conjugation
symmetry, PSD hypothesis or interpolant. The set may depend on \(n\).
The amplitudes in (3) are the specified complex ratios, not free or
positive moment weights.

## Conclusion

For every parameter choice and cluster in these hypotheses,

\[
                  \max_{k=0,1,2}|M_k|\ \ge\ \frac1{81}.
 \tag{4}
\]

Thus the assessed question admits \(c_\delta=1/81\) and
\(N_\delta=5\); the bound in fact needs no dependence on \(\delta\).
It is uniform when distinct points approach each other or the anchor,
and when their scaled displacements \(n(z-x)\) become unbounded.

This is a finite-family partial result. A separate proof audit on
1 November 2026 verified (4) under exactly the stated hypotheses,
without a mathematical correction; its checks are recorded below.
It establishes neither actual-Xi signs nor a contour detector for an
arbitrary collection of poles. Other poles, multiplicities, Xi
realization, interpolation, contour clearance and weighted boundary
control remain unresolved. No RH resolution candidate is claimed.

## Proof

### Source scope and the purpose of a direct calculation

The prior
[EXPLORE assessment](../drafts/literature/2026-11-01-scaled-pole-moment-detector.md)
covers exactly (1)--(3), including collisions and unbounded scaled
displacements. Its inspected inverse-Vandermonde and Prony results
do not give (4): their quantitative inverse bounds involve separation
or configuration-dependent local constants. No theorem from those
sources is invoked as a lower bound here, and no novelty is inferred
from the absence of an inspected match.

The proof below uses the exact rational factors inherited from C645d,
a finite product expansion, a quadratic polynomial identity and the
triangle inequality. These elementary calculations are written out
because they exploit the correlated weights in (3). They do not
reprove a general interpolation or moment-inversion theorem. The
scalar cancellation theorem in C645d remains valid; its contraction
construction and external analytic inputs are not needed below.

### 1. Uniform control of an amplitude near the scaled anchor

For an additional point write \(h=z-x\), \(u=nh\), and
\(A_n(u)=B_n(x)/B_n(x+h)\). We use this notation only for points
satisfying (2), together with \(A_n(0)=1\). The parameter bounds give

\[
 d>1,\qquad R>5/4,\qquad |h|<\delta/8<1/16.
 \tag{5}
\]

For every real \(0\le t\le1\),

\[
 |x-it|\ge d>1,\qquad |R^2+itx|\ge R^2>25/16.
\]

In particular
\(|x+h-it|\ge d-|h|>15/16\) and
\(|R^2+it(x+h)|\ge R^2-|h|>3/2\).
All product values and ratios in use are consequently finite and
nonzero. This also checks the factor at \(t=0\).

The inverse of the normalized factor at \(t=t_j\) is exactly

\[
 q_j(h)=
 \frac{1+it_jh/(R^2+it_jx)}{1+h/(x-it_j)},\qquad
 A_n(u)=\prod_{j=0}^{n-1}q_j(h).
 \tag{6}
\]

Subtracting one in this formula gives

\[
 q_j(h)-1=
 \frac{h\left(it_j/(R^2+it_jx)-1/(x-it_j)\right)}
      {1+h/(x-it_j)}.
\]

Since \(|1+h/(x-it_j)|\ge1-|h|/d>15/16\), it follows that

\[
 |q_j(h)-1|
 \le\frac{16}{15}\left(\frac{16}{25}+1\right)|h|
 =\frac{656}{375}|h|\le2|h|.
 \tag{7}
\]

Expand the finite product in (6) using \(q_j=1+(q_j-1)\), then
apply the triangle inequality term by term. For \(|u|<1/2\),

\[
\begin{aligned}
 |A_n(u)-1|
 &\le (1+2|h|)^n-1
   =\sum_{m=1}^n {n\choose m}(2|h|)^m\\
 &\le\sum_{m=1}^n (2n|h|)^m
   \le\frac{2|u|}{1-2|u|}.
\end{aligned}
 \tag{8}
\]

Here \({n\choose m}\le n^m\); the last bound is the elementary
geometric sum with ratio \(2|u|<1\). There is no infinite product,
logarithm branch, asymptotic approximation or interchange of limits.
In particular, every admissible point with \(|u|\le1/8\) obeys

\[
                  |A_n(u)-1|\le\tfrac13,
                  \qquad |A_n(u)|\le\tfrac43.
 \tag{9}
\]

The point need not range over the whole scaled disk: (9) is used only
for the admissible points already present in \(Z\). No extra geometric
assumption is introduced if \(\delta\) is very small.

### 2. Three points: an annihilating polynomial forces a near-anchor point

Suppose \(Z\) has three points. Denote the two nonzero additional
scaled displacements by \(u,v\) and their exact amplitudes by
\(A=A_n(u)\), \(B=A_n(v)\). Equation (3) becomes

\[
 M_0=1+A+B,\qquad M_1=uA+vB,\qquad M_2=u^2A+v^2B.
 \tag{10}
\]

Let \(\varepsilon=\max_{0\le k\le2}|M_k|\). Multiplying out (10),
the coefficient of each of \(A\) and \(B\) cancels in the identity

\[
              M_2-(u+v)M_1+uvM_0=uv.
 \tag{11}
\]

Consequently

\[
 |uv|\le\varepsilon(1+|u+v|+|uv|)
       \le\varepsilon(1+|u|)(1+|v|).
 \tag{12}
\]

If both \(|u|\ge1/8\) and \(|v|\ge1/8\), then (12) gives

\[
 \varepsilon\ge
 \frac{|u|}{1+|u|}\frac{|v|}{1+|v|}\ge\frac1{9^2}=\frac1{81}.
 \tag{13}
\]

This step divides by neither \(u-v\) nor a minimum separation. It
also retains arbitrary large \(|u|\) or \(|v|\), so an escaping
scaled displacement causes no loss in the constant.

### 3. Three points: small moments would force both weights near +1

For a contradiction suppose \(\varepsilon<1/81\). By (13), exchange
the names of the additional points if necessary to arrange
\(|u|<1/8\). Equation (9) yields
\(|A-1|\le1/3\) and \(|A|\le4/3\).

The zeroth moment in (10) then forces

\[
 |B|=|M_0-(1+A)|
 \ge |1+A|-|M_0|
 \ge 2-|A-1|-\varepsilon
 \ge\tfrac53-\varepsilon>\frac{134}{81}.
 \tag{14}
\]

Using the first moment,

\[
 |v|\,|B|=|M_1-uA|
 \le\varepsilon+|u||A|
 <\frac1{81}+\frac16=\frac{29}{162}.
\]

Thus

\[
                  |v|<\frac{29/162}{134/81}
                        =\frac{29}{268}<\frac18,
 \tag{15}
\]

where the last comparison is \(232<268\). Apply (9) to this actual
second point to obtain \(|B-1|\le1/3\). Now (10) gives

\[
 |M_0|=|3+(A-1)+(B-1)|
      \ge3-|A-1|-|B-1|\ge\frac73,
 \tag{16}
\]

contrary to \(|M_0|\le\varepsilon<1/81\). This proves (4) for
three points, including all arbitrarily close distinct configurations.

### 4. One or two points

For \(Z=\{x\}\), the moments are \((1,0,0)\), so (4) holds.

If there is one additional point, write its scaled displacement and
amplitude as \(u\) and \(A\). Then
\(M_0=1+A\), \(M_1=uA\), and

\[
                       M_1-uM_0=-u.
\]

If \(|u|\ge1/8\), the triangle inequality implies

\[
 \max(|M_0|,|M_1|)\ge\frac{|u|}{1+|u|}\ge\frac19.
\]

If \(|u|<1/8\), equation (9) instead gives
\(|M_0|=|2+(A-1)|\ge5/3\). Both alternatives imply (4).
No additional case depends on a limiting interpretation at a collision.

### Independent proof audit — 1 November 2026

The audit reused the unchanged EXPLORE assessment for (1)--(3),
read the complete proof above and compared the definitions with C645d
(1)--(2) and L645's scaled factors. It did not import C645d's
cancellation proof or any new external theorem. The following checks
verify the claimed uniformity rather than just pointwise nonvanishing.

* For a single factor, taking its value at \(x\) divided by its value
  at \(x+h\) cancels \(R\) and gives exactly (6). In particular the
  term \(it_jh/(R^2+it_jx)\) is in the numerator. Since \(x=-d\)
  is real, \(|R^2+it_jx|\ge R^2\); the bounds in (5) imply the
  two perturbed denominators exceed \(15/16\) and \(3/2\),
  respectively. Thus neither a factor zero nor a rational pole is
  hidden in the ratios, including \(j=0\).
* The coefficient in (7) is exactly
  \((16/15)(1+16/25)=656/375<2\). Expansion of the finite product
  bounds the sum of every nonempty subset of factor errors by
  \((1+2|h|)^n-1\). Bounding each binomial coefficient by \(n^m\)
  and extending the resulting nonnegative finite sum geometrically
  is valid for \(2|u|<1\). At \(|u|=1/8\) its bound is
  \((1/4)/(3/4)=1/3\). No restriction on all other scaled nodes
  enters this estimate.
* In (11), the coefficients of \(A\) and \(B\) are
  \(u^2-(u+v)u+uv=0\) and \(v^2-(u+v)v+uv=0\).
  The anchor contributes \(uv\). Therefore (12) holds for arbitrary
  complex nodes and weights. The increasing function \(r/(1+r)\)
  is at least \(1/9\) when \(r\ge1/8\); (13) handles all such
  nodes, including arbitrarily large ones, without dividing by their
  difference.
* In the remaining three-point case,
  \(5/3-1/81=134/81>0\) and
  \(1/81+1/6=29/162\). Thus division by the lower bound on
  \(|B|\) is legitimate and yields exactly \(29/268<1/8\).
  Both weights then satisfy (9), forcing \(|M_0|\ge7/3\).
  The contradiction excludes every \(\varepsilon<1/81\), which
  proves the non-strict conclusion (4), including its endpoint.
* A singleton has \(M_0=1\). For a two-point set the linear identity
  gives the bound \(1/9\) whenever \(|u|\ge1/8\), while (9)
  gives \(5/3\) otherwise. These cases exhaust the allowed set
  sizes. Arbitrarily close distinct points require no limiting
  argument; every inequality holds for each such configuration.

No additional assumption on \(\delta\), separation, symmetry,
bounded scaled displacement or Xi realization was used. The proof is
uniform for all the asserted \(n\ge5\); in fact its estimates need
only positivity and integrality of \(n\), but no enlarged statement is
needed here. The audit establishes the stated finite-family input,
not originality, a larger-cluster result or a boundary estimate.

### Qualifications and remaining gap

The anchor contributes exactly one to \(M_0\); the unit-residue and
correlated-weight hypotheses force every other sufficiently near-anchor
amplitude close to +1. The argument would not follow for freely assigned
complex amplitudes. Its quadratic identity annihilates the two other
nodes, so the proof does not extend as stated to larger clusters or
unrestricted multiplicities.

The scalar cancellation in C645d is consistent with (4): this result
bounds the maximum of three moments, not the zeroth moment alone.
A later contour application must identify the full pole contribution,
remove or account for grid singularities, justify a zero-avoiding
contour and control the boundary costs of these polynomial weights.
No such identity or estimate is asserted here, and no actual-Xi sign
or off-line zero is inferred.

## Mathlib

Full matching coverage for (4) is **not checked**; availability is
unknown. No specific Mathlib theorem is used or claimed to formalize
this finite-product estimate and three-moment argument. The proof is
informal; documentation validation is not Lean verification.
