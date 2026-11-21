# Reference-root locations and a conditional residual sign test

## Hypotheses

Let D=d/dy, 1/4<=t<=5/18, h>0, and define
\[
 S(y)=y^2-h^2,\quad R(y)=S(y)^2,\quad T=1+D+tD^2,
 \quad J=TR,\quad K=R+2tR'.
\]
Let Q(y)=y^2+b y+c be any real monic quadratic. Write F=T(RQ).
The reference-root conclusions below do not require Q to be positive
or F to have a multiple root.

For the conditional residual conclusion only, suppose that for some
real d there is a polynomial H with
\[
 F(y)=(y-d)^2H(y),                                      \tag{1}
\]
and impose the two strict outer threshold inequalities in (7) below.
Root counts include multiplicity; (1) does not assert exact multiplicity
two, H(d)!=0, or squarefreeness of H.

## Conclusion

Set
\[
 A(y)=S(y)+8ty,\qquad
 \eta_-=-4t-\sqrt{16t^2+h^2},\quad
 \eta_+=-4t+\sqrt{16t^2+h^2}.
\]
The quartic J has four distinct, simple real roots alpha_1,...,alpha_4,
with the strict locations
\[
 \alpha_1<\eta_-<\alpha_2<-h<\alpha_3<\eta_+<\alpha_4<h. \tag{2}
\]
In particular K(alpha_i) is nonzero, with signs (+,-,+,-).
Define the four real thresholds
\[
 b_i=-2\phi(\alpha_i),\qquad
 \phi(y)=y+\frac{tS(y)}{A(y)}.                           \tag{3}
\]
Then
\[
 F(\alpha_i)=K(\alpha_i)(b-b_i),\qquad
 b_2-b_3>2(\alpha_3-\alpha_2)>0.                         \tag{4}
\]

If in addition
\[
 b_1>b_2\quad\hbox{and}\quad b_3>b_4,                    \tag{7}
\]
then every factorization (1) has a quartic H with four distinct real
roots. This conditional conclusion retains all potential shared roots
with J and the possibility H(d)=0; it does not divide by y-d at a
zero of that factor.

**The two inequalities (7) are not proved here.** Thus no unconditional
root count for C020q's residual H, general (2,4) witness, or exclusion
of the full nominated sextic class follows. This is a uniform reference
root and middle-threshold result, followed by a conditional implication.
Independent critical audit1476 accepts this reference-root and
conditional residual result; its scope is detailed below.

## Proof

**Explicit reference polynomials and strict locations.** Differentiation
gives
\[
 J=S^2+4yS+4t(3y^2-h^2),\qquad K=S(S+8ty)=S A.           \tag{5}
\]
Since h,t>0, one has eta_-<-h<0<eta_+<h. For example,
sqrt(16t^2+h^2)<4t+h, by squaring two positive quantities, proves
eta_+<h; eta_-<-h follows from sqrt(16t^2+h^2)>h.
At either zero eta of A, substitute S(eta)=-8t eta into (5):
\[
 J(\eta)=4t\big((16t-5)\eta^2-h^2\big)<0.               \tag{6}
\]
Indeed 16t-5<=-5/9 and h>0. Meanwhile J(-h)=J(h)=8th^2>0,
and the monic quartic J tends to positive infinity at both infinities.
The intermediate value theorem supplies a root in each of
(-infinity,eta_-), (eta_-,-h), (-h,eta_+), (eta_+,h).
These four disjoint intervals already contain four distinct roots of
a degree-four polynomial. They therefore contain exactly one each;
each is simple, and there are no other roots. This proves (2), without
assuming an interlacing theorem or generic simplicity.

The roots of K=S A, in increasing order, are eta_-,-h,eta_+,h,
all distinct. Each factor is monic quadratic. Its sign in the four
intervals just used gives K(alpha_i) signs (+,-,+,-), respectively.
In particular neither S nor A vanishes at any alpha_i. This proves
that all divisions in (3) are legitimate.

**Evaluation and middle thresholds.** The ordinary product rule gives
the full polynomial identity
\[
 T(RQ)=Q(TR)+Q'(R+2tR')+tQ''R
       =QJ+(2y+b)K+2tR.
\]
At alpha_i the first term vanishes. Since R/K=S/A there, the remaining
expression equals K(alpha_i)(b+2alpha_i+2tS(alpha_i)/A(alpha_i)),
which is exactly (4)'s evaluation.
Direct quotient differentiation on any interval avoiding eta_-,eta_+
gives
\[
 \phi'(y)=1+\frac{8t^2(y^2+h^2)}{A(y)^2}>1.
\]
For the numerator calculation,
S'A-SA'=2y(S+8ty)-S(2y+8t)=8t(y^2+h^2).
By (2), the closed interval [alpha_2,alpha_3] lies in
(eta_-,eta_+), so the derivative formula is continuous there.
Integrating the strict inequality gives
phi(alpha_3)-phi(alpha_2)>alpha_3-alpha_2>0.
Multiplication by two proves the strict middle bound in (4).
This argument gives no comparison across either pole of phi; it cannot
be extended to the two outer pairs by an unsupported monotonicity claim.

**Conditional residual test, including equalities and shared roots.**
Under (7), the full order is b_1>b_2>b_3>b_4. Combining this with
the signs of K gives the following signs of F at its four reference
points. A zero in the table is retained as a zero, not assigned a sign.

| Location of b | Signs at alpha_1,alpha_2,alpha_3,alpha_4 | Indices with signs (-,+,-) |
| --- | --- | --- |
| b<b_4 | -,+,-,+ | 1,2,3 |
| b=b_4 | -,+,-,0 | 1,2,3 |
| b_4<b<b_3 | -,+,-,- | 1,2,3 |
| b=b_3 | -,+,0,- | 1,2,4 |
| b_3<b<b_2 | -,+,+,- | 1,2,4 |
| b=b_2 | -,0,+,- | 1,3,4 |
| b_2<b<b_1 | -,-,+,- | 1,3,4 |
| b=b_1 | 0,-,+,- | 2,3,4 |
| b>b_1 | +,-,+,- | 2,3,4 |

In every row the three selected values are strictly nonzero. If (1)
holds, none of these three points can equal d, since F(d)=0.
At each selected point, division by (alpha_i-d)^2>0 is legitimate,
so H has the same signs (-,+,-) at three increasing points.
The leading coefficient of F is one and its degree is six, because
T preserves the leading term; thus H is monic of degree four.
Its values tend to positive infinity at both real ends. The four
successive sign changes, including the two ends, give four distinct
real roots in disjoint open intervals by the intermediate value
theorem. Degree four then exhausts all roots and forces simplicity.
This proves the conditional conclusion even if d coincides with an
unselected reference point. No case H(d)=0 was removed: such a root,
if present, must fit the four roots just counted.

**Exact link to C020q.** In that lemma, put
\[
 m=-l/(2k),\qquad h=\frac{\sqrt{l^2-4k}}{2|k|}>0,
 \qquad y=x-m.
\]
Then 1+lx+kx^2=k(y^2-h^2). Dividing the input and output by k^2>0
normalizes its squared factor to R as above. Its quadratic becomes
Q(y)=y^2+(B+2m)y+(m^2+Bm+C); its positive discriminant gap is
unchanged, since the new constant minus (B+2m)^2/4 equals C-B^2/4.
Its collision location becomes d=-m. Its residual becomes
H_C020q(y+m)/k^2. Translation commutes with T and preserves real roots
and all multiplicities. Thus (2)--(4) apply on the entire C020q
domain, including every t endpoint and every possible shared root
with the collision. Only the two additional conditions (7) are missing
for this particular sufficient residual-count proof. This is not a
claim that (7) are necessary for four real residual roots.

**Verification and source comparison.** The exact rational exploratory
checks are reproducible with
`python3 scripts/quartic-differential/sector-sextic-reference-signs-1474.py`;
the full adjacent JSON saves all polynomials, Sturm chains, root
intervals, interval evaluations and tested parameters. They support no
universal claim. The uniform proof above uses explicit polynomial
identities and the intermediate value theorem, not that finite list.
The initial admissible point l=0,k=-1,t=5/18 has
Delta=-115/27, M=38024/729, B=-54/115, C=89/115 and reference signs
(-,+,-,-), exactly enclosed in certificate1474. That is a positive
instance of the test, not the requested (2,4) witness.

The reused EXPLORE assessment1468/review1469 covers this fixed sextic
attempt. Its imported preservation interface is Thomas Craven and
George Csordas, *Location of zeros. Part I: Real polynomials and entire
functions*, Illinois J. Math. **27**(2) (1983), 244--278, Theorem3.3,
remarks(1),(3), pp.257--258,
[primary scan](https://scispace.com/pdf/location-of-zeros-part-i-real-polynomials-and-entire-z3v2jd50yw.pdf).
Walsh's theorem and the factorial specialization recorded in C020p
supply universal preservation, but not the explicit strict intervals,
sign thresholds or their outer comparisons. The elementary argument
here is needed for those additional data; it is not a reproof of
Walsh or a replacement for its hypotheses. C020p's fourfold exclusion
and C020o's inverse obstruction are comparisons, not premises here.
No originality conclusion follows from the recorded search. General
four-real-root inputs, products, actual-Xi correspondence, paid divisor
loss, unbounded degrees, signs, initialization and overlap remain open.

**Independent critical audit1476.** The audit reads this proof and C020s
in full and checks the strict root intervals before using any algebraic
root parametrization. In (6), 16t-5<=-5/9 and h>0 make J(eta)<0;
J(+/-h)=8th^2>0. The four disjoint intervals therefore exhaust quartic
degree, including both endpoints in t, and every root is simple.
The four K signs follow from its ordered distinct factors. Neither
the evaluation nor phi' divides at a zero of A; the entire middle
interval lies strictly between A's poles. Its integrated inequality
is strict because the displayed derivative excess is positive there.

The full nine-row table was rederived from b_1>b_2>b_3>b_4 and the
four K signs. Each equality row still has three strictly signed values
(-,+,-) at increasing indices. At these points F!=0 excludes d,
so division by (alpha_i-d)^2 is valid. The two ends and these three
values give four disjoint open root intervals for the monic quartic
H. Degree four forces simplicity; no step needs H(d)!=0. An
unselected alpha_i may equal d. The centering formula was checked
without assuming k>0: h^2=(l^2-4k)/(4k^2)>0, the square scaling is
k^2>0, and x=y+m sends the collision at zero to d=-m.
This checks the transfer identities, not all of C020q's separate
parametrization claims.

Independent standard-library rational polynomial arithmetic, importing
no previous mathematical script, is reproducible with
`python3 scripts/quartic-differential/sector-sextic-independent-audit-1476.py`.
The adjacent JSON stores the full identity operands, zero differences,
all nine order cases and exact endpoint bounds. All 31 checks pass;
the proof's IVT and strict inequalities, audited above and in C020s,
remain essential. The conditional conclusion is accepted at its stated
hypotheses, without adding an outer-comparison premise to the
unconditional reference-root claims. This audit produces no new
general-input reduction or count theorem.

## Mathlib

Full matching coverage of the reference-root locations and threshold
comparison has not been checked. The argument uses polynomial algebra,
the intermediate value theorem and elementary differentiation; no
matching Lean theorem or formal proof is asserted. Unknown coverage
is not evidence of absence.
