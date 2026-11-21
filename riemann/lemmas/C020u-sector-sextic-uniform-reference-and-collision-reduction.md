# Uniform reference and collision reduction for the sextic count problem

## Hypotheses

Let D=d/dy, 1/4<=t<=5/18, T=1+D+tD^2, and let R be a monic
real quartic with four real roots counted with multiplicity. Write

\[
 Q=y^2+by+c,\quad F=T(RQ),\quad
 J=TR,\quad K=R+2tR',\quad A=T(yR),\quad C=T(y^2R).
\]

The reference-root assertions below assume the four roots of R are
distinct. The collision assertions instead allow all multiplicities
and assume c>b^2/4. A collision means F(d)=F'(d)=0 for real d;
it need not have exact multiplicity two.

## Conclusion

For distinct-root R, J has four simple real roots alpha_1<...<alpha_4,
K is nonzero at each, and

\[
 \frac{K(\alpha_i)}{J'(\alpha_i)}<0.                 \tag{1}
\]

Thus their K signs are (+,-,+,-). Define

\[
 b_i=-2\left(\alpha_i+t\frac{R(\alpha_i)}{K(\alpha_i)}\right).
                                                               \tag{2}
\]

If b_1>b_2>b_3>b_4, then F has at least four distinct real roots
for every real b,c. **This ordering is an unproved sufficient
condition for arbitrary R, not a conclusion of this lemma.** If the
ordering were proved for all distinct-root R and all allowed t, root
continuity would extend the required four-real-root count, including
multiplicities, to every R in the hypotheses.

For arbitrary R, every admissible collision has one of two forms:

1. R=(y-d)^4, and d is an output root of exact multiplicity two.
2. R(d),R'(d) are not both zero, and the two linear collision
   equations for the shifted quadratic coefficients are nonsingular,
   with strictly negative determinant. The exact admissibility test
   and parametrization are (8)--(9) below.

In particular, a double or triple input root cannot be an output
collision. No assertion about the remaining four output roots at a
nonsingular collision is proved. The universal count law, arbitrary
symbols/compositions and actual-Xi transfer remain unresolved. This
partial reduction is not an RH candidate. Independent conceptual
audit1482 accepts precisely these partial and conditional assertions;
it does not prove the threshold ordering or the count law.

## Proof

**Available preservation input and purpose.** Use only C020p's Walsh
preservation interface: T preserves real-rooted degree-six inputs,
including multiplicities and either nonzero leading coefficient,
throughout the closed t interval. The precise external input is Thomas
Craven and George Csordas, *Location of zeros. Part I: Real polynomials
and entire functions*, Illinois J. Math. **27**(2) (1983), 244--278,
Theorem 3.3 and remarks (1),(3), printed pp.257--258,
[primary scan](https://scispace.com/pdf/location-of-zeros-part-i-real-polynomials-and-entire-z3v2jd50yw.pdf).
C020p checks the convolution normalization using
Ty^6=y^4(y^2+6y+30t), with discriminant 36-120t>=8/3.
Assessment1478/review1479 reuses that inspected interface. C020p's
unrelated count argument is not an input here.

The same preservation holds for degrees four and five: for a
real-rooted degree-k polynomial p, approximate it coefficientwise by
p(y)(1-y/M)^(6-k), for real M tending to positive infinity. These
are real-rooted sextics, and their T images converge coefficientwise
to Tp. A nonreal zero of Tp would persist in a small disk disjoint
from the real axis, by Rouche's theorem, contradicting preservation
of the approximants. The leading coefficient of Tp equals that of p.
In this application choose the disk boundary free of zeros of Tp;
coefficient convergence gives uniform convergence on that boundary,
so the Rouché inequality is strict for all sufficiently large M.
The limiting polynomial is nonzero even though its degree drops.
This finite-degree specialization imports preservation, not a count
law for inputs already having a nonreal pair.

**A quartic inequality and absence of common reference roots.** For
any real-rooted quartic,

\[
 E(y):=3R'(y)^2-4R(y)R''(y)\ge0.                    \tag{3}
\]

Indeed, away from the roots write u_j=1/(y-r_j), listing the four
roots with multiplicities. Logarithmic differentiation gives
E/R^2=4 sum_j u_j^2-(sum_j u_j)^2
=sum_(i<j)(u_i-u_j)^2>=0. At a root, (3) follows by continuity
(or directly E=3R'^2). This is the elementary quartic Newton--Laguerre
inequality; its short verification also fixes the normalization used
in the collision calculation.

Suppose J(x)=K(x)=0 and R(x)!=0. Then

\[
 R'(x)=-\frac{R(x)}{2t},\qquad
 R''(x)=\frac{1-2t}{2t^2}R(x),\qquad
 E(x)=\frac{16t-5}{4t^2}R(x)^2<0,                  \tag{4}
\]

since 16t-5<=-5/9. This contradicts (3). If R has distinct roots
and R(x)=0, then K(x)=2tR'(x)!=0. Hence J and K have no common
real root in the distinct-root case.

**Simplicity of J.** Preservation makes J real-rooted. The product
rule gives A=yJ+K. For every nonzero real epsilon,

\[
 J-\epsilon A=T\big(R(1-\epsilon y)\big)
\]

is real-rooted by the degree-five specialization. If J had a root
alpha of multiplicity m>=2, then A(alpha)=K(alpha)!=0. In a real
neighborhood of alpha put f=J/A=(y-alpha)^m h(y), with h(alpha)!=0.
Shrink the neighborhood so h and
m h+(y-alpha)h' have fixed nonzero signs. If m is even, f has one
sign off alpha, so f=epsilon has no nearby real solution for epsilon
of the opposite sign. If m is odd and at least three, f is strictly
monotone there and has at most one nearby real solution. Meanwhile,
on a small complex disk containing only this zero of J and no zero
of A, Rouche's theorem gives exactly m zeros of J-epsilon A for
all sufficiently small nonzero epsilon. The real solutions just
counted are simple, because f' is nonzero away from alpha. Either
case therefore gives a nonreal zero, contradicting preservation.
Explicitly, choose the disk inside the preceding real neighborhood
on its real diameter and with neither J nor A vanishing on its
boundary. The bound
|epsilon| max_boundary |A| < min_boundary |J|
gives the multiplicity count m. Every real zero in this disk lies
on the diameter already counted; f=epsilon excludes alpha itself.
Thus neither a repeated real solution nor a real root outside that
neighborhood can supply the missing disk roots. The perturbed
polynomial has degree five for epsilon!=0, so its possible additional
root tending to infinity does not affect this local contradiction.
Consequently all four roots of J are simple.

**The reference signs are uniform in the spacings.** Fix any allowed
t. Join the ordered roots (-2,-1,1,2) to the ordered distinct roots
of R by linear interpolation of each root. Every intermediate quartic
remains monic with four distinct real roots. The preceding conclusions
hold along the whole path. Its four ordered J roots vary continuously;
none collide, and K never vanishes at them. The signs of K/J' are
therefore constant along the path. For the initial quartic
(y^2-1)(y^2-4), C020t's audited reference-root table gives K signs
(+,-,+,-), for this same t including either endpoint. At the ordered
roots of a monic simple quartic the J' signs are (-,+,-,+). All four
ratios are negative at the initial quartic, proving (1) at the final
one. This uses the proved signs in C020t; it does not extend that
lemma's numerical threshold enclosures to other spacings.
For clarity, each consecutive input gap on the path is a convex
combination of two positive gaps, hence positive. The coefficients
of the monic J are bounded on this compact path, which bounds all
its roots. Simple roots have continuous local labels; ordering and
the absence of collisions glue these labels along the whole path.
This argument is made separately for each fixed t, so it requires
no unproved uniform separation as t or the spacings vary.

**What still suffices for the count.** The exact product identity is

\[
 F=QJ+Q'K+2tR,\qquad F(\alpha_i)=K(\alpha_i)(b-b_i). \tag{5}
\]

Assume only for this paragraph that the four thresholds are strictly
descending. For b>b_2 choose indices (2,3,4); for b=b_2 choose
(1,3,4); for b_3<=b<b_2 choose (1,2,4); and for b<b_3 choose
(1,2,3). In each case the three ordered evaluations in (5) have
strict signs (-,+,-). These cases include all b=b_i; no selected
evaluation is zero. F is a monic sextic and positive at both real
infinities, so IVT gives four distinct real roots in four disjoint
open intervals. The c term vanishes in (5), so this conclusion
requires no restriction on c. With c>b^2/4, RQ has exactly two
nonreal roots, and this conditional conclusion is precisely the
required output bound.

To justify the proposed repeated-root extension, approximate any
ordered root multiset of R by strictly ordered real roots, holding
t,b,c fixed. If the conditional count were available for every such
approximant, the corresponding monic sextics would each have four
real roots. Their coefficients converge, so all roots are uniformly
bounded by the elementary monic polynomial root bound. Choose four
real roots from each sextic, and pass to a subsequence on which these
and the other two roots converge. The limiting factorization has at
least four real factors, with repetitions retained. Thus the limiting
output has at least four real roots counted with multiplicity. This
argument does not discard either t endpoint. It does not establish
the unproved ordering needed to invoke it.

**Uniform collision equations.** At a proposed collision d write

\[
 R(d+x)=r_0+r_1x+r_2x^2+r_3x^3+x^4,\qquad
 Q(d+x)=x^2+B_0x+C_0.
\]

Here B_0=b+2d and C_0=c+bd+d^2>B_0^2/4, so C_0>0.
The constant and linear output coefficients vanish exactly when

\[
 U B_0+V C_0=-2tr_0,\qquad
 U_1B_0+V_1C_0=-2r_0-6tr_1,                       \tag{6}
\]

where U=r_0+2tr_1, V=r_0+r_1+2tr_2,
U_1=r_0+2r_1+6tr_2, V_1=r_1+2r_2+6tr_3.
To check every shifted coefficient, if p_j is the coefficient of
x^j in R(d+x)Q(d+x), then

\[
\begin{array}{c|l}
j&p_j\\ \hline
0&r_0C_0\\
1&r_0B_0+r_1C_0\\
2&r_0+r_1B_0+r_2C_0\\
3&r_1+r_2B_0+r_3C_0\\
4&r_2+r_3B_0+C_0\\
5&r_3+B_0\\
6&1
\end{array}
\]

The output coefficient is p_j+(j+1)p_(j+1)+t(j+2)(j+1)p_(j+2),
with missing coefficients zero. Its j=0,1 rows give exactly (6);
in particular F'(d) is the j=1 coefficient, with no factorial loss.
Define Delta=UV_1-U_1V and N_0=U(-2r_0-6tr_1)+2tr_0U_1.
Elimination without division gives Delta C_0=N_0, and expansion gives

\[
\begin{split}
 N_0&=(2t-2)r_0^2-6tr_0r_1-12t^2r_1^2+12t^2r_0r_2\\
 &=-\frac{15}{2}(tr_1+\tfrac25r_0)^2
   -\frac32t^2(3r_1^2-8r_0r_2)
   +(2t-\tfrac45)r_0^2.                            \tag{7}
\end{split}
\]

The middle bracket is E(d)>=0 by (3), since R''(d)=2r_2.
Also 2t-4/5<=-11/45. If r_0!=0 the last term is strictly
negative. If r_0=0 and r_1!=0, (7) is -12t^2r_1^2<0.
Thus N_0<0 whenever r_0,r_1 are not both zero. Because C_0>0,
every such collision has Delta<0, in particular no singular
consistent system. There is no spacing-independent strictly negative
constant bound on N_0 asserted here; C020t's fixed-family constant
does not extend to arbitrary R.

For completeness put N_B=(-2tr_0)V_1+(2r_0+6tr_1)V. On this
nondegenerate part of the domain, admissible collisions are exactly

\[
 \Delta<0,\qquad M=4N_0\Delta-N_B^2>0,             \tag{8}
\]

with

\[
 B_0=N_B/\Delta,\quad C_0=N_0/\Delta,\quad
 b=B_0-2d,\quad c=C_0-dB_0+d^2.                    \tag{9}
\]

Cramer's rule proves both equations (6) for these values, and
C_0-B_0^2/4=M/(4 Delta^2). Conversely every admissible collision
in this part satisfies (8)--(9). The determinant also equals
AB'-A'B at d when B=J, because the two columns in (6) are
(A-dJ,A'-dJ') and (J,J'). No division by R(d) is used.
Here d is a fixed number in the derivative A'-dJ'; differentiating
yJ first and then evaluating at d gives A'-dJ'=J+K'=U_1.
Also c-b^2/4=C_0-B_0^2/4 exactly. Thus M>0 reconstructs the
strict original quadratic hypothesis, not merely C_0>0. The converse
uses N_0<0 and C_0>0 before dividing by Delta; it never assumes
nonsingularity to establish nonsingularity.

It remains to handle r_0=r_1=0. If R has root multiplicity m at d,
where 2<=m<=4, write R(d+x)=x^m S(x), S(0)!=0. The lowest
output term is

\[
 t m(m-1) S(0) C_0\,x^{m-2},                      \tag{10}
\]

with nonzero coefficient. For m=2 the output is nonzero at d;
for m=3 it has a simple root; and for m=4 it has an exact double
root. In the last case monicity and degree four give R=(y-d)^4.
This proves the complete collision classification, including all
input multiplicities and output roots of higher multiplicity in the
nonsingular case.

**Evidence and limits.** Equations (3)--(10), the preservation
specialization, local multiplicity argument and connected-root path
are the proof; no grid, approximate roots or numerical evidence is
used. The fixed-family reference signs are the existing audited
C020t input. The elementary square expansion (7) is the general
quartic version of its collision identity, with the lost absolute
constant explicitly removed. This additional argument is needed
because the imported Walsh theorem supplies preservation only.
The ready source comparison did not supply the requested partial
count; no originality is claimed for these elementary reductions.

The attempt has not proved b_1>b_2>b_3>b_4 for arbitrary spacings,
nor an alternative count argument, nor a counterexample. The sign
of Delta and positivity of M say nothing here about the residual
quartic's real-root count. Preservation is not substituted for the
missing count conclusion. C020o/q and the unrelated portion of
C020p remain unaudited; none is used. Actual-factor applicability,
paid exceptional loss, general symbols/compositions, all degrees,
signs, initialization and overlap remain independent gaps.

**Independent conceptual audit — 18 November 2026, step1482.**
The audit accepts the assertions above under the unchanged hypotheses,
with the preceding coefficient table and local-limit details making
the checks explicit. Only the stated C020p preservation interface and
the audited C020t reference signs are used. The factorial coefficients
are 6!, 5!*6 and 4!*30t; division by 6! gives 1,1,t. The
discriminant lower bound is 8/3 on the closed t interval. No theorem
asserting partial-count preservation has been substituted for Walsh.

The strictness checks are exact: 16t-5<=-5/9 in (4), and
2t-4/5<=-11/45 in (7). Expanding the first square in (7) gives
coefficients -15t^2/2, -6t and -6/5 on r_1^2, r_0r_1 and r_0^2;
adding the remaining terms gives exactly its first line. Equality
E(d)=0 is harmless: r_0!=0 makes the last term strict, while
r_0=0, r_1!=0 gives -12t^2r_1^2. If both vanish, (10) instead
gives nonzero lowest coefficients 2tS(0)C_0, 6tS(0)C_0 and
12tC_0 for m=2,3,4 respectively. These cover every missing
singular case without imposing simplicity on an output collision.

The four b cases in the conditional sign argument include b=b_1
in the first case, b=b_2 in the second, b=b_3 in the third, and
b=b_4 in the fourth. In each case the selected indices avoid any
zero evaluation and give strict (-,+,-); all remaining b lie in
the same four cases. The IVT intervals are disjoint and open.
For the conditional repeated-root limit, a single bound
1+max_(0<=j<6)|a_j| on roots of each monic output, together with
bounded convergent coefficients a_j, precludes roots escaping to
infinity. A subsequence of the six bounded root coordinates gives
the limiting factorization; its first four coordinates remain real.
This is multiplicity-aware closure, not a simplicity assertion.

No discrepancy requiring a changed mathematical conclusion was found.
This is reproduction and verification of the saved partial result,
not a new count theorem or an originality claim. The reference sign
table is reused as an already audited input; its numerical certificate
was not replayed and no new mathematical script was needed. The full
uniform threshold ordering, residual count and actual-Xi use remain
unproved. Both t endpoints and all input multiplicities are retained.

## Mathlib

Full matching coverage of this uniform reduction and of the Walsh
specialization has not been checked. Supporting ingredients are
finite polynomial algebra, the quartic Newton--Laguerre inequality,
Rouche's theorem/root continuity and IVT. No matching Lean theorem
or formal verification is asserted; unknown coverage is not absence.
