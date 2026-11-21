# Strict outer thresholds and exclusion of the two-double-input family

## Hypotheses

Let h>0, 1/4<=t<=5/18, D=d/dy, and T=1+D+tD^2. Set
\[
 S=y^2-h^2,\quad R=S^2,\quad A=S+8ty,\quad
 J=TR=S^2+4yS+4t(3y^2-h^2),\quad K=SA.
\]
Write alpha_1<alpha_2<alpha_3<alpha_4 for the four real simple roots
of J supplied by C020r. Its strict locations imply A(alpha_i)!=0.
Define, as there,
\[
 \phi(y)=y+tS(y)/A(y),\qquad b_i=-2\phi(\alpha_i).
\]
For the output conclusions, let Q(y)=y^2+b y+c be any real monic
quadratic and F=T(RQ). No sign or root hypothesis on Q is required.
For the residual conclusion only, suppose F=(y-d)^2H for some real
d and polynomial H. Neither H(d)!=0 nor squarefreeness is assumed.
All root counts include multiplicities unless explicitly called distinct.

## Conclusion

The two formerly unproved outer comparisons are strict throughout the
stated domain, including both endpoints in t:
\[
 b_1>b_2\quad\hbox{and}\quad b_3>b_4.                    \tag{1}
\]
Together with C020r they give b_1>b_2>b_3>b_4. Consequently:

1. F has at least four distinct real roots. In particular, when
   c>b^2/4, RQ has exactly two nonreal roots and F has at most two;
   this family cannot give the nominated (2,4) witness.
2. Whenever F=(y-d)^2H, the monic quartic H has four distinct simple
   real roots. This includes shared collision/reference roots and
   H(d)=0. The entire output is then real-rooted.

The centering and positive scaling already justified in C020r transfer
these conclusions to C020q's full two-double-input collision family.
No deformation from general four-real-root inputs to this family has
been proved. General inputs, other allowed symbols and products remain
outside this result. Independent critical audit1476 accepts the stated
restricted-family result; this is neither a whole-class sextic
impossibility theorem nor an RH candidate.

## Proof

**The adjacent-pair parameter is strictly greater than two.** By C020r,
with eta_+/-=-4t+/-sqrt(16t^2+h^2),
\[
 \alpha_1<\eta_-<\alpha_2<-h<\alpha_3<\eta_+<\alpha_4<h.
                                                               \tag{2}
\]
In particular alpha_4>0. We first prove alpha_3+alpha_4>0.
If alpha_3>=0 this is immediate. Otherwise put x=-alpha_3. Then
0<x<h, and the explicit quartic gives
\[
 J(x)-J(-x)=8x(x^2-h^2)<0.
\]
Since J(-x)=0, J(x)<0. A monic quartic with the four real roots in
(2) is nonnegative at and to the right of its largest root alpha_4.
It follows that x<alpha_4, proving the claim also in this case.

Set
\[
 r=2+\alpha_3+\alpha_4>2,\quad
 w_+=\alpha_3+\alpha_4=r-2,\quad
 w_-=\alpha_1+\alpha_2=-r-2.
\]
The last equality uses the y^3 coefficient 4 of J, so the sum of all
four roots is -4. Put a=h^2, z_+=alpha_3 alpha_4,
z_-=alpha_1 alpha_2, and V=r^2+12t-4. Factoring J into the two
adjacent-root quadratics and comparing the y^2 and y coefficients gives
\[
 z_-+z_+=V-2a,\qquad w_-z_++w_+z_-=4a.
\]
Substitution of w_+/- into the second equation gives
r(z_--z_+)=2V. Because r>2, division by r is valid, and hence
\[
 z_-+a=\frac{(r+2)V}{2r},\qquad
 z_++a=\frac{(r-2)V}{2r}.                              \tag{3}
\]
The constant coefficient of J gives z_-z_+=a^2-4ta. Substituting
(3) yields
\[
 \frac{(r^2-4)V^2}{4r^2}=a(V-4t),\qquad
 a=\frac{(r^2-4)(r^2+12t-4)^2}
          {4r^2(r^2+8t-4)}.                            \tag{4}
\]
Every denominator is positive: r>2 and t>0 imply r^2+8t-4>0.
This also shows V>0. No root branch or continuity assumption has
been used to obtain r>2 or the factorization formulas.

**A comparison across each pole.** Take either outer adjacent pair
(u,v)=(alpha_1,alpha_2) or (alpha_3,alpha_4), so u<v. By (2),
\[
 A(u)A(v)<0.                                           \tag{5}
\]
For example A is positive to the left of eta_- and negative between
its two roots, giving (5) for the first pair; the signs reverse for
the second pair. Direct subtraction, with these denominators nonzero,
gives
\[
 \phi(v)-\phi(u)
  =(v-u)\frac{E}{A(u)A(v)},\qquad
 E=A(u)A(v)+8t^2(uv+a).                                \tag{6}
\]
Indeed S(v)A(u)-S(u)A(v)=8t(v-u)(uv+a). Thus E<0 is the
precise sufficient sign needed here; monotonicity through a pole is
not being assumed.

Write w=u+v and P=uv+a. Expanding A(u)A(v) in these symmetric
variables gives
\[
 \begin{split}
 A(u)A(v)&=P^2-aw^2+8tw(uv-a)+64t^2uv,\\
 E&=P(P+8tw+72t^2)-a(w+8t)^2.                           \tag{7}
 \end{split}
\]
For the lower pair put W=-r and for the upper pair put W=r.
Then w=W-2, and (3)--(4) read
\[
 P=\frac{(W-2)(W^2+12t-4)}{2W},\qquad
 a=\frac{(W^2-4)(W^2+12t-4)^2}{4W^2(W^2+8t-4)}.
\]
All divisions are valid because |W|=r>2. Substitution into (7)
and collection of terms gives the exact factorization
\[
 E=\frac{2t(W-2)(W^2+12t-4)}{W^2(W^2+8t-4)}\,
       \mathcal B_t(W),                                \tag{8}
\]
where
\[
 \mathcal B_t(W)=(10t-3)W^3+(6-24t)W^2
       +(48t^2-60t+12)W-192t^2+136t-24.                 \tag{9}
\]
For a denominator-free verification of (8), multiply (7) by
4W^2(W^2+8t-4). With V=W^2+12t-4, its numerator is
\[
 (W-2)^2V^2(W^2+8t-4)
 +2W(W-2)V\{8t(W-2)+72t^2\}(W^2+8t-4)
 -(W^2-4)V^2(W-2+8t)^2.
\]
Factoring (W-2)V leaves
\[
 V[(W-2)(W^2+8t-4)-(W+2)(W-2+8t)^2]
 +16tW(W-2+9t)(W^2+8t-4)=8t\mathcal B_t(W),
\]
which proves (8) by expansion of the displayed cubic (9).

**Both branch signs, with the endpoint retained.** Set s=r-2>0.
Expanding (9) at W=r=2+s gives
\[
 \mathcal B_t(r)=-(3-10t)s^3-12(1-3t)s^2
                 -12t(3-4t)s-96t^2<0.                \tag{10}
\]
Here 3-10t>=2/9, 1-3t>=1/6, 3-4t>=17/9, and t>=1/4,
so in fact this expression is at most -96t^2<=-6.
For the other branch, expansion at W=-r=-2-s gives
\[
 \mathcal B_t(-r)=(3-10t)s^3+12(2-7t)s^2
             +12(4-13t-4t^2)s+16t(5-18t)>0.            \tag{11}
\]
The first two coefficients satisfy 3-10t>=2/9 and
2-7t>=1/18. The function 4-13t-4t^2 is strictly decreasing on
this interval and has value 13/162 at t=5/18. Finally 5-18t>=0.
Thus the right side of (11) is at least
\[
 (2/9)s^3+(2/3)s^2+(26/27)s>0.
\]
This is still strict when t=5/18 and the constant term vanishes;
s>0 follows from h>0 and has not been replaced by s>=0.

In (8) all factors other than W-2 and the cubic are positive.
For W=r>2, (10) therefore gives E<0. For W=-r<-2, W-2<0
and (11) again gives E<0. Equations (5)--(6) yield phi(v)>phi(u)
for both pairs. Multiplication by -2 proves (1). C020r already proves
the strict middle comparison, so the complete threshold order follows.

**Counts and multiplicities.** C020r proves the product-rule evaluation
F(alpha_i)=K(alpha_i)(b-b_i), with K signs (+,-,+,-).
Its complete sign table under the now-proved strict order supplies,
for every real b, three increasing reference points where the F signs
are strictly (-,+,-). The table includes each equality b=b_i; c does
not enter the evaluations. Since F is monic of degree six and positive
at both real infinities, these three values give four roots in disjoint
open intervals by the intermediate value theorem. They are distinct;
this does not assert their simplicity or that F has only four real roots.
Degree six bounds the remaining number of roots, with multiplicity,
by two. When c>b^2/4 the input has precisely the stated four real
and two nonreal roots, proving the family exclusion.

If F=(y-d)^2H, C020r's conditional residual conclusion now applies
unconditionally on our h,t domain. In detail, none of the three
strictly signed reference points can equal d. At them H has the
same signs, because (alpha_i-d)^2>0. H is monic quartic, and its
positive values at the two infinities give four distinct real roots
in the same four disjoint intervals. Degree four exhausts all roots
and forces simplicity. This proof retains H(d)=0 and a possible
coincidence of d with an unselected reference root. It neither divides
by zero nor assumes the collision has exact multiplicity two.

**Verification, sources and scope.** Run
`python3 scripts/quartic-differential/sector-sextic-outer-thresholds-1475.py`.
The adjacent JSON stores the complete sparse rational polynomials,
the branch expansions, all fifteen exact checks and the bounds used
above. These are algebra checks, not a substitute for (2), the argument
r>2, the inequalities or the root-count proof. An initial failed guess
that an intermediate numerator was divisible by t^2 is recorded there;
the correct factor is 8t, as explicitly displayed above. No failed
guess is used, and no sampled root values or parameter grid are needed.

The unchanged EXPLORE assessment1468/review1469 covers this bounded
fixed-sextic attempt. Its preservation interface is Thomas Craven and
George Csordas, *Location of zeros. Part I: Real polynomials and entire
functions*, Illinois J. Math. **27**(2) (1983), 244--278, Theorem3.3
and remarks(1),(3), pp.257--258,
[primary scan](https://scispace.com/pdf/location-of-zeros-part-i-real-polynomials-and-entire-z3v2jd50yw.pdf).
That interface is not being reproved or used as an unstated partial
root-count theorem: the explicit outer comparison is the additional
calculation needed here. C020o's inverse obstruction, C020p's fourfold
exclusion and the failed expanded-discriminant certificate1473 remain
comparisons and prior stops, not premises of this proof. No originality
conclusion follows from the recorded literature search.

This is local progress on a restricted input family. The full nominated
class allows general four-real-root inputs and symbols of higher degree;
neither an extremal reduction to double roots nor a composition law is
supplied here. Actual-Xi operator correspondence, paid exceptional-root
loss, unbounded degrees, signs, initialization and overlap remain open.

**Independent critical audit1476.** This audit accepts C020r's
reference locations and conditional count only after checking their
proof and complete order table. In particular eta_+>0 forces
alpha_4>0. If alpha_3<0, x=-alpha_3 lies strictly between 0 and h,
so J(x)=8x(x^2-h^2)<0. A monic quartic cannot be negative at or
beyond its largest real root. Thus x<alpha_4. The other case,
alpha_3>=0, is immediate; both prove r>2 before any division or
choice of an algebraic branch. This reasoning does not include h=0.

Independently comparing the entire adjacent-pair factorization to J
gives (3) and the constant relation (4), not just a selected resolvent
equation. Its denominator r^2+8t-4 is positive. In each outer pair,
A(u)A(v)<0 follows from the strict locations. Direct subtraction
gives exactly (6), and expansion in w=u+v, P=uv+h^2 gives (7).
After clearing 4W^2(W^2+8t-4), the numerator in (8) equals
8t(W-2)(W^2+12t-4) B_t(W). This verifies its factor and sign;
no t^2 divisibility claim is needed. All cleared factors divided out
are nonzero on |W|=r>2, t>=1/4.

The two shifted cubic expansions (10)--(11) were separately checked.
For the only quadratic coefficient requiring an endpoint argument,
\[
 (4-13t-4t^2)-13/162
  =(5/18-t)(127/9+4t)\ge0.
\]
All other coefficient bounds follow from their displayed linear
forms on [1/4,5/18]. Hence the upper branch is <=-6 and the lower
branch is >=(2/9)s^3+(2/3)s^2+(26/27)s>0 for s=r-2>0.
At t=5/18 the lower constant vanishes, but its linear term remains
strictly positive. A uniform positive margin as h tends to zero is
not asserted or required. The sign of W-2 in (8), together with
these opposite cubic signs, makes E<0 for both pairs. Since the
denominator in (6) is negative, both phi differences are positive,
which gives the claimed strict descending threshold order.

For arbitrary real b,c, the rechecked table supplies three strict
(-,+,-) values of F, independently of c. Its monic sextic ends give
four distinct real roots, leaving at most two nonreal roots counted
with multiplicity. If F=(y-d)^2H, the selected points are different
from d and transfer the same signs to H. Its monic quartic degree
forces four simple real roots, including the permitted H(d)=0 case.
The product with the real squared collision factor is real-rooted.
No assumption of an exactly double collision or generic simplicity
was introduced. C020r's positive scaling and translation justify the
stated transfer; C020q's elimination is not needed for this exclusion.

Run the independent script
`python3 scripts/quartic-differential/sector-sextic-independent-audit-1476.py`.
Its full adjacent JSON saves 31 successful exact checks, including
all nine threshold-order cases, both complete shifted cubics, the
cleared pair factorization and endpoint values, with no failures.
No previous script is imported or old certificate overwritten.
These checks accompany the analytic audit above; they do not prove
the conclusion by sampling. This accepts the existing restricted
input theorem and adds no theorem beyond it or the sources checked.
General four-real-root inputs, other symbols, products and actual-Xi
transfer remain outside the audited conclusion.

## Mathlib

Full matching coverage of these outer thresholds and this finite-degree
root-count exclusion has not been checked. The proof uses polynomial
factorization, symmetric coefficients, explicit inequalities and the
intermediate value theorem. The exact certificate is not a Lean proof;
unknown coverage is not evidence of absence.
