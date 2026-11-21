# Uniform threshold ordering and the single-factor sextic count

## Hypotheses

Let D=d/dy, 1/4<=t<=5/18, T=1+D+tD^2, and let R be a monic
real quartic with four real roots, counted with multiplicity. Set

\[
 Q(y)=y^2+by+c,\qquad F=T(RQ),\qquad
 J=TR,\qquad K=R+2tR'.
\]

The threshold assertions assume that the roots r_1<...<r_4 of R
are distinct. In that case C020u supplies four simple real roots
alpha_1<...<alpha_4 of J and K(alpha_i)!=0. Define

\[
 s_i=\alpha_i+t\frac{R(\alpha_i)}{K(\alpha_i)},\qquad b_i=-2s_i.
                                                               \tag{1}
\]

The output real-root assertion allows arbitrary real b,c. For the
nonreal-count comparison additionally assume c>b^2/4. Write Z_c for
the number of nonreal roots, including multiplicities.

## Conclusion

For distinct-root R the thresholds satisfy

\[
 s_1<s_2<s_3<s_4,\qquad b_1>b_2>b_3>b_4.             \tag{2}
\]

Consequently F has at least four distinct real roots in this case,
for every real b,c. For arbitrary real-rooted quartic R, F has at
least four real roots counted with multiplicity. In particular,

\[
 c>b^2/4\quad\Longrightarrow\quad Z_c(RQ)=2,
 \qquad Z_c(T(RQ))\le2.                              \tag{3}
\]

Both closed t endpoints are included. These conclusions complete the
nominated arbitrary-quartic **single-factor** count target; their
independent conceptual audit1485 accepts the stated theorem. They do not cover general
allowed symbols, products of operators, other degrees or actual-Xi
factorizations. There is no RH candidate or paid exceptional-root
estimate here.

## Proof

**Previously available inputs and the missing difference.** C020u,
independently audited in step1482, gives the simple reference roots,
nonvanishing K, alternating K signs, the conditional four-real-root
conclusion from (2), and multiplicity-aware closure. C020t gives (2)
for the initial quartic R_*(y)=(y^2-1)(y^2-4), for every allowed t.
Only its audited strict threshold ordering is used below, not an
extension of its numerical enclosures to arbitrary spacings.

The preservation input underlying those results is Thomas Craven and
George Csordas, *Location of zeros. Part I: Real polynomials and entire
functions*, Illinois J. Math. **27**(2) (1983), 244--278, Theorem3.3
and remarks (1),(3), printed pp.257--258,
[primary scan](https://scispace.com/pdf/location-of-zeros-part-i-real-polynomials-and-entire-z3v2jd50yw.pdf).
Its Walsh specialization and normalization are already justified in
C020p's preservation interface and C020u: Ty^6=y^4(y^2+6y+30t),
with 36-120t>=8/3. No new preservation theorem is being reproved or
treated as a partial-count theorem. Assessment1478/review1479 did not
supply the uniform count assertion; the additional argument needed
here is the exclusion of equal thresholds. C020p's unrelated count
proof and C020o/q are not used.

**Polynomial vectors at reference roots, including shared roots.**
For now assume the r_j distinct and let

\[
 R_j(y)=\prod_{k\ne j}(y-r_k).
\]

At a real root x of J define

\[
 a(x)=x+tR(x)/K(x),\quad h_x=x-a(x)=-tR(x)/K(x),
 \quad v_j(x)=-tR_j(x)/K(x).                         \tag{4}
\]

These expressions divide only by nonzero K(x). In particular they
are defined when R(x)=0; no reciprocal (x-r_j) is used as a definition.
The polynomial identities

\[
 \sum_jR_j=R',\qquad \sum_jR_j^2=R'^2-RR''           \tag{5}
\]

hold everywhere: away from the input roots they follow by
logarithmic differentiation, and hence hold as polynomial identities.
Since J(x)=0, R''(x)=-(R(x)+R'(x))/t. Therefore

\[
\begin{split}
 \sum_jv_j(x)&=-\frac{tR'(x)}{K(x)}
             =-\frac12-\frac{h_x}{2t},\\
 \|v(x)\|^2&=\frac{t^2(R'(x)^2-R(x)R''(x))}{K(x)^2}
             =\frac14+\frac{(4t-1)R(x)^2}{4K(x)^2}
             =\frac14+\frac{(4t-1)h_x^2}{4t^2}.
\end{split}                                                    \tag{6}
\]

For the second equality in the norm row, expand
K^2+(4t-1)R^2=4t^2R'^2+4tRR'+4tR^2 and use J(x)=0.
Set delta=4t-1, so 0<=delta<=1/9. Eliminating h_x in (6) shows
that every v(x) lies on the same ellipsoid in R^4:

\[
 \|v\|^2=\delta\left(\sum_jv_j+\frac12\right)^2+\frac14.
                                                               \tag{7}
\]

**Equal thresholds force an inner product of -1/2.** For distinct
real x,z one has the identity

\[
 \sum_jR_j(x)R_j(z)
   =\frac{R'(x)R(z)-R(x)R'(z)}{z-x}.                \tag{8}
\]

Away from input roots this is the difference of logarithmic
derivatives divided by z-x, after multiplication by R(x)R(z).
Multiplying (8) by z-x makes it a polynomial identity in x,z,
so it remains valid at all input roots when x!=z.

Suppose x and z are distinct roots of J and a(x)=a(z)=a. Then
h_x=x-a, h_z=z-a, and (4) and K=R+2tR' give

\[
 \frac{R(x)}{K(x)}=-\frac{h_x}{t},\qquad
 \frac{R'(x)}{K(x)}=\frac{t+h_x}{2t^2},
\]

with the same formulas at z. Substituting into (8) yields

\[
 v(x)\mathbin{\cdot}v(z)
 =\frac{t^2}{z-x}
  \left(\frac{(t+h_x)(-h_z)}{2t^3}
        -\frac{(-h_x)(t+h_z)}{2t^3}\right)
 =\frac{h_x-h_z}{2(z-x)}=-\frac12.                 \tag{9}
\]

All these equations allow R(x)=0 or R(z)=0. A shared reference/input
root therefore has not been silently excluded.

**A sharp enough bound for the whole ellipsoid.** Put
e=(1,1,1,1)/2, a unit vector. Write v=Xe+Z with Z perpendicular to e,
and set d=1-4delta>0. Completing the square in (7), using sum v_j=2X,
gives

\[
 \frac{(X-A_0)^2}{A_2}+\frac{\|Z\|^2}{B_2}=1,
 \quad A_0=\frac{\delta}{d},\quad
 A_2=\frac{1-3\delta}{4d^2},\quad
 B_2=\frac{1-3\delta}{4d}.                          \tag{10}
\]

Here A_2 and B_2 denote squared radii, both strictly positive. Put

\[
 M=A_2-A_0^2=\frac{1+\delta}{4d}\le\frac12.         \tag{11}
\]

The last inequality is exactly 9delta<=1, and is strict when
delta<1/9. Also M>0, so sqrt(A_2)>A_0>=0.

For any two vectors v=Xe+Z and w on the ellipsoid, the usual
Cauchy--Schwarz inequality, after scaling its principal axes, gives

\[
 v\cdot w\ge A_0X-\sqrt{A_2X^2+B_2\|Z\|^2}.       \tag{12}
\]

Explicitly write w=A_0e+sqrt(A_2)u_0e+sqrt(B_2)U with
u_0^2+||U||^2=1 and U perpendicular to e, and take the inner
product. Thus (12) does not assume v=w or a special position of w.

For v on (10), direct substitution yields

\[
\begin{split}
 &(M+A_0X)^2-(A_2X^2+B_2\|Z\|^2)\\
 &=M\big(A_2-(X-A_0)^2\big)-B_2\|Z\|^2\\
 &=\left(\frac{MA_2}{B_2}-B_2\right)\|Z\|^2
 =\frac{\delta(2-3\delta)}{d^2}\|Z\|^2\ge0.        \tag{13}
\end{split}
\]

Moreover X>=A_0-sqrt(A_2), so the other side of the square comparison
has a fixed positive sign:

\[
 M+A_0X\ge A_2-A_0\sqrt{A_2}
              =\sqrt{A_2}(\sqrt{A_2}-A_0)>0.        \tag{14}
\]

Taking square roots in (13) is therefore legitimate. Combining
(12)--(14) proves

\[
 v\cdot w\ge -M.                                  \tag{15}
\]

For delta<1/9, (11) makes (15) strictly greater than -1/2.
For delta=1/9, equality v.w=-1/2 requires equality in (13), and
its positive coefficient forces Z=0. In this case (10) gives
X=A_0+sqrt(A_2) or X=A_0-sqrt(A_2); neither is zero because M>0.
Thus all four coordinates of v are equal and nonzero. Only this
necessary equality condition is used; sufficiency is not needed.
The lower endpoint delta=0 causes no equality issue, since M=1/4.

**The endpoint equality cannot occur for distinct input roots.**
If R(x)!=0, (4) becomes v_j(x)=-tR(x)/(K(x)(x-r_j)).
Equality of its four nonzero coordinates would force all four
x-r_j to be equal, contradicting distinctness. If R(x)=0, then
x=r_m for a unique m; R_m(x)=R'(x)!=0 and all other R_j(x)=0.
Since K(x)=2tR'(x), the vector has coordinate -1/2 at m and zero
elsewhere, also contradicting the equality condition. Consequently
the inner product in (9) is impossible throughout the closed t
interval. No two distinct roots of J have equal a(x).

**Transporting the strict order and completing the count.** Fix any
allowed t. Move the four ordered roots of R_* to those of R by
linear interpolation. Each consecutive gap stays positive. Along
this compact path C020u makes the four ordered J roots simple,
continuous and bounded, and K stays nonzero at each. Hence every
s_i in (1) is continuous along the path. The preceding argument
prevents equality between any two s_i anywhere on that path.
C020t's strict initial order s_1<s_2<s_3<s_4 therefore persists,
proving (2). This argument is made separately for each fixed t;
it needs no uniform positive gap as roots coalesce or t approaches
an endpoint.

For clarity, the conditional count from C020u uses the exact identity
F=QJ+Q'K+2tR and hence F(alpha_i)=K(alpha_i)(b-b_i).
Its K signs are (+,-,+,-). For b>b_2 use indices (2,3,4);
for b=b_2 use (1,3,4); for b_3<=b<b_2 use (1,2,4); and
for b<b_3 use (1,2,3). In each case the three selected evaluations
have strict signs (-,+,-). This covers every b, including all
threshold equalities. Since F is a monic sextic, it is positive at
both real infinities, and the four disjoint open sign intervals
give four distinct real roots. The value of c is irrelevant to
these evaluations.

Finally, approximate any repeated-root real quartic R by monic
quartics with distinct real roots, holding t,b,c fixed. C020u's
audited closure applies: the resulting monic sextics converge in
coefficients, their roots are uniformly bounded, and a subsequence
of four chosen real roots converges to four real factors of the
limiting output, with repetitions retained. Thus there are at least
four real roots counted with multiplicity for the limiting F.
If c>b^2/4, Q has exactly two nonreal roots and no real roots,
so (3) follows. Neither endpoint nor any input multiplicity is lost.

**Evidence and qualifications.** The proof is the polynomial identities,
the full ellipsoid inequality with its equality case, and transport
from the already audited fixed reference. No grid, approximate roots,
new external theorem or numerical certificate is used. The attempted
monotonicity argument between poles alone would have been inadequate;
(8)--(15) instead exclude equality across different branches. This
argument is accepted by independent conceptual audit1485 below. The ready
source assessment did not identify a matching count theorem; this
is local progress under that assessment, not a claim of originality.
The earlier fixed-family and coefficient-method stops are preserved.

In particular, preservation alone has not been substituted for a count
bound, and (3) is not extended by iteration or to arbitrary symbols.
Actual-factor correspondence, a paid actual exceptional-root loss,
all-degree signs, initialization and overlap remain unproved.

**Independent conceptual audit — 18 November 2026, step1485.**
The audit accepts (2)--(3) with exactly the hypotheses above. This is
verification of the saved argument, not a new theorem or an assertion
of originality. The unchanged EXPLORE assessment1483/review1484 covers
this audit. Only C020t's audited initial strict order and C020u's
audited reference-root, sign and conditional-count/closure assertions
are mathematical inputs. In particular C020u does not use (2) to
prove its simple reference roots or K signs; there is no circular
assumption of the order being proved here. Its collision classification
and the unrelated C020p/o/q count arguments are not used.

The following checks isolate the load-bearing strictness and boundary
issues. Put S=sum_j v_j. At a J root, (5) gives
S=-tR'/K and ||v||^2=t^2(R'^2-RR'')/K^2. Substitution of
R''=-(R+R')/t and K=R+2tR' gives (6) exactly, hence
||v||^2-delta S^2-delta S=(1+delta)/4. With S=2X this is

\[
 dX^2-2\delta X+\|Z\|^2=(1+\delta)/4,\qquad
 d(X-\delta/d)^2+\|Z\|^2=(1-3\delta)/(4d).
\]

Thus both radii and the center in (10) have the stated values.
Throughout the closed parameter interval d>=5/9 and 1-3delta>=2/3,
so every division and square root in (10)--(14) is legitimate.
The factorization
1-3delta-4delta^2=(1+delta)(1-4delta) verifies (11),
including its exact equivalence M<=1/2 iff 9delta<=1.
Writing w in scaled unit-sphere coordinates proves (12) for every
w on the ellipsoid; it imposes no further relation between v and w.
In (13), MA_2/B_2-B_2=M/d-B_2=delta(2-3delta)/d^2.
Equation (14) is strictly positive since A_2-A_0^2=M>0.
Consequently no sign is lost when passing from the squared comparison
to sqrt(A_2 X^2+B_2||Z||^2)<=M+A_0X, which proves (15).

At delta=0 the bound is v.w>=-1/4, already strict relative to -1/2.
At delta=1/9 the constants are d=5/9, A_0=1/5, A_2=27/50,
B_2=3/10, M=1/2, and the coefficient in (13) is 3/5>0.
If v.w=-1/2, both inequalities in
v.w>=A_0X-sqrt(A_2 X^2+B_2||Z||^2)>=-M must be equalities.
Hence Z=0. Also X=1/5 +/- sqrt(27/50) is nonzero. Its four
coordinates X/2 are therefore equal and nonzero, the exact necessary
condition used in the proof, rather than an assumed equality case.

For (8), multiplying by z-x yields an identity of polynomials in
two variables, so its verification away from input roots proves it
also at shared roots. Under a(x)=a(z), substitution gives (9) with
h_x-h_z=x-z, hence the sign is -1/2. The only denominators are
K(x), K(z), t and z-x, all nonzero. If x=r_m, distinctness gives
R_m(x)=R'(x)!=0 and K(x)=2tR'(x); the vector is exactly
-(1/2)e_m. If x is not an input root, equality of the four nonzero
coordinates forces equality of the four reciprocals 1/(x-r_j),
and thus equality of the roots. Neither case permits endpoint equality.
This checks the shared R/J root issue without an excluded pole limit.

For each fixed t, linear interpolation of ordered input roots stays
in the distinct-root domain. The monic coefficients of J stay bounded
on that compact path, and its four simple ordered roots are continuous.
Nonvanishing K at each reference root makes every threshold continuous;
the collision exclusion then fixes every pairwise order. C020t supplies
the initial order for this same t, including both endpoints. No
uniform lower bound on the gaps across all quartics is required.

The four b cases in the proof give strict signs (-,+,-) at their
three selected ordered points. In particular b=b_1 is in the first
case, b=b_2 in the second, b=b_3 in the third and b=b_4 in the
fourth; each selection avoids its zero evaluation. The two exterior
intervals and two interior intervals therefore each contain a real
root, regardless of c. For the repeated-root limit, choose four real
roots of each monic output and its remaining two complex roots. A
single bound 1+max_(j<6)|a_j|, uniform over the convergent coefficient
sequence, bounds all six. A subsequence of these six coordinates
converges, and the limit of their factorizations is F. The first four
factors remain real, with any coincidences counted as multiplicities.
Degree stays six, and t,b,c are fixed, so neither roots at infinity
nor a changed parameter boundary can invalidate this closure.

No discrepancy was found and no numerical replay or new mathematical
script was needed. The fixed-reference rational certificate remains
the already audited C020t input, not a newly verified computation.
The source-normalization and Walsh scope are reused from C020u/audit1482;
preservation alone never supplies the nonreal-input count. This audit
does not prove a general-symbol or composition extension, an all-degree
bound, actual-Xi applicability or any paid exceptional-root estimate.

## Mathlib

Full matching coverage of (2)--(3) and of the ellipsoid argument has
not been checked. Supporting ingredients are finite polynomial
identities, the Euclidean Cauchy--Schwarz inequality, IVT and continuity
of polynomial roots, with the Walsh input cited above. No matching
Lean theorem or formal verification is asserted; unchecked coverage
does not imply absence.
