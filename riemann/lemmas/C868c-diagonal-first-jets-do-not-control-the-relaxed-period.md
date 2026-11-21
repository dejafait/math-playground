# Corollary 868c: diagonal first jets lose the period in a precise relaxation

## Hypotheses

Retain L868's actual coefficient on X=(C*)^2,

\[
 F=-C\frac{G(z_1)G(z_2)(z_1-z_2)^2}{z_1^2z_2^2},\qquad
 z_j=R e^{x_j+i y_j},\qquad C,R>0,
\]

where L847's entire G has power series G(z)=sum_{n>=0} a_n z^n,
a_n>0, in particular a_0>0. All angular means below are normalized
by (2pi)^(-2). The diagonal D is z1=z2, equivalently x1=x2 and
y1=y2 modulo 2pi. An admissible triple means the full real C1,
angularly periodic class

\[
 h\geq0,\qquad q^2+r^2\leq |F|^2,\qquad
 r_{x_j}=q_{y_j},\qquad (q+h)_{x_j}=-r_{y_j}\quad(j=1,2).
 \tag{1}
\]

Use C868a's constants A=mean q(s,s,.), H=mean h(s,s,.)>=0 and
L868's K=mean(q+h)=A+H. The sharp no-gain threshold is K>=-|M|,
where M=mean F. C868b's fixed-fiber and correction-mode restrictions
are retained. No simplicity, C2 regularity, growth estimate, graph
existence or RH is assumed; no zero divisor is removed.

## Conclusion

Every admissible triple satisfies, at every p in D,

\[
 q(p)=r(p)=0,\quad dq(p)=dr(p)=0,\quad
 h_{x_1}(p)=h_{x_2}(p)=0.                                 \tag{2}
\]

Consequently h(s,s,v,v)=b(v), independent of s, for a nonnegative
C1 periodic b. The closure equations restricted to D impose no
additional equation on h_y1,h_y2. If h(p)=0, nonnegativity separately
forces dh(p)=0. These conclusions include D's intersections with
all G-zero divisors.

These necessary first-jet data do **not** bound A in the following
precise relaxation. Fix any H>=0 and allow A to be any real number.
There are global smooth periodic q,r,h satisfying both closure
equations, h=H, every F-zero value condition q=r=0, all of (2),
and actual domination q^2+r^2<=|F|^2 on an open neighborhood of
the whole D. They also satisfy all the stated mean and correction-
mode restrictions of C868a/b, with K=A+H and the chosen A,H.
Their diagonal first jets are identical for fixed H and all A.

For A!=0 these explicit triples violate domination somewhere away
from D. They are counterexamples only to an implication from the
specified relaxed conditions to a period bound, **not** admissible
certificates. No full-class bound, strict gain, graph obstruction,
Xi sign or RH conclusion is obtained. The local first-jet mechanism
is stopped unless supplied with additional global domination control.
The independent replay below accepts this scoped diagnostic;
the source search supplies no certified originality claim.

## Proof

### Approved scope and standard operations

The assessment saved before invocation is
`drafts/literature/2026-11-06-actual-f-diagonal-first-jet-test.md`.
Its EXPLORE scope permits the actual quadratic estimate, all first
differentials, substitution in the existing closure system and a
strictly qualified necessary-data obstruction. We reuse its source
screen and the earlier diagonal/fixed-fiber stops; none is a premise
asserting global flexibility.

Import Jiří Lebl, *Basic Analysis II*, v6.3 (15 May 2026),
[Definition 8.3.1/Proposition 8.3.2, pp35-36, Theorem 8.3.7 and
complete proof p38, Definition 8.3.8 p39](https://www.jirka.org/ra/realanal2.pdf#page=35),
for differentials and the C1 chain rule in open real coordinate
charts. For constancy on finite intervals and the interior-zero
minimum use Lebl, *Basic Analysis I*,
[Definition 4.1.1](https://www.jirka.org/ra/html/sec_der.html),
[Lemma 4.2.2, Theorem 4.2.4 and Proposition 4.2.6](https://www.jirka.org/ra/html/sec_mvt.html).
These sources were inspected in the reused assessment, not newly
browsed or reproved here. All points are interior to X, and angles
are taken on open local charts; the original functions are C1.

For the compact power-series means below use the actual entire
power series in L847. Its compact Laurent/power-series operations
are covered by Lebl, *Guide to Cultivating Complex Analysis*, v1.10
(5 November 2026), [Theorem 4.4.2, pp104-107](https://www.jirka.org/ca/ca.pdf#page=104),
as already inspected for L847. Only compact circles at fixed finite
radii occur. There is no infinite differentiated Fourier series,
new Stokes application, extension theorem or limit at infinity.
The computation below is the target-specific specialization of
these standard operations, not a reproof of them.

### Actual quadratic domination controls every first differential

Fix p in D and a small closed logarithmic coordinate neighborhood
inside X. In this chart set u=x1-x2, v=y1-y2 using compatible angle
branches. The identity z1-z2=z2(e^(u+i v)-1) and bounded first
real derivatives of the exponential on the compact chart imply

\[
 |z_1-z_2|\leq B_1\sqrt{u^2+v^2}.
\]

For example apply the one-variable fundamental theorem of calculus
to the exponential on the segment from 0 to u+i v; its derivative
has bounded modulus there. The G factors and inverse-coordinate
factors are bounded on the same neighborhood. Hence a finite B,
depending on this neighborhood, satisfies

\[
 |q|,|r|\leq |F|\leq B(u^2+v^2).                         \tag{3}
\]

This uses boundedness, never nonvanishing, of G. At p it gives
q=r=0. Change any one of x1,x2,y1,y2 by a small real t, holding
the other three fixed at p. Then u^2+v^2=t^2, including the changes
of the second coordinate with their opposite sign. Each difference
quotient for q and r therefore has modulus at most B|t| and tends
to zero. All four partial derivatives vanish. Since q,r are C1,
these are their full differentials: dq=dr=0 at p. This includes
normal directions; it is not inferred from value vanishing alone.

Now substitute these derivatives into BOTH equations in (1), for
each j. The first becomes 0=0, and the second gives h_xj=0.
No h_yj appears in these equations. By the C1 chain rule,

\[
 \partial_s h(s,s,v,v)=h_{x_1}+h_{x_2}=0.
\]

Constancy on every finite s interval proves the asserted trace b(v).
Periodicity, C1 regularity and nonnegativity descend to that trace.
If h(p)=0, each coordinate restriction has an interior minimum,
so all its first derivatives vanish. We do not differentiate the
closure system again or assume second partial derivatives.

### A global closure family with arbitrary relaxed mean

Define holomorphic functions on X by the explicit identities

\[
 V=\frac{z_1^2(z_1-z_2)^2}{z_2^2},\qquad
 W=FV=-C\frac{G(z_1)G(z_2)(z_1-z_2)^4}{z_2^4}.
 \tag{4}
\]

These formulas are valid at every zero; no division by F or G is
made. For a real parameter lambda set

\[
 p_\lambda=\lambda W,\qquad q=\operatorname{Re}p_\lambda,
 \qquad r=-\operatorname{Im}p_\lambda,\qquad h=H.          \tag{5}
\]

The new symbol p_lambda here is a complex coefficient, not a point
of D. These are global smooth functions on X, hence periodic on
the angular cover. Holomorphic differentiation and the chain rule
give p_yj=i p_xj in logarithmic coordinates. Taking real and
imaginary parts gives exactly r_xj=q_yj and q_xj=-r_yj; since h
is constant, these are both closure equations in (1) everywhere.
Also h>=0. Formula (4) retains both G-zero divisors and D, including
every intersection. Its fourth diagonal factor makes q,r and their
first differentials zero on D; h has zero differential everywhere.

For every lambda, including zero, the open set

\[
 U_\lambda=\{z\in X:|\lambda V(z)|<1\}
\]

contains the entire D. On it the exact identity

\[
 \sqrt{q^2+r^2}=|\lambda V|\,|F|\leq|F|                 \tag{6}
\]

proves actual domination, including all zero intersections. This
neighborhood may depend on lambda and need not have a fixed width
at noncompact ends. No uniform neighborhood is asserted or needed
for a counterexample to the stated relaxation.

To compute the mean on any fixed product of coordinate circles,
expand only the finite polynomial (z1-z2)^4 and the entire power
series for G(z1). All z1 powers are nonnegative. The sole z1^0
term of G(z1)(z1-z2)^4 is a0 z2^4. Thus integration in y1 first,
followed by integration in y2, gives

\[
 \langle W\rangle_{y_1}=-C a_0 G(z_2),\qquad
 \langle W\rangle_{y_1,y_2}=-C a_0^2.                    \tag{7}
\]

Termwise compact integration is justified by uniform convergence
on the fixed circles; the finite polynomial introduces no issue.
Consequently mean q=-lambda C a0^2, mean r=0 and mean h=H at every
radial point. Choosing

\[
                    \lambda=-A/(C a_0^2)
\]

realizes any prescribed real A and yields K=A+H. In particular
the means on equal radii and on C868b's fixed radial line agree
with those results. Every nonzero h Fourier coefficient is zero.
Both mode bounds therefore hold. C868b's opposite-index finite
positivity test is H sum_j |c_j|^2>=0, since its zero coefficient
is H and all its other coefficients vanish. The H=0 angular
independence conclusions hold as well. The nonzero coefficient
profile identities in C868a follow from its closure-only calculation,
which uses neither domination nor a growth assumption. Thus this
family satisfies the stated necessary restrictions, without being
asserted to satisfy the hypotheses of C868a/b globally.

For fixed H all lambda give the same diagonal jets: q=r=0,
dq=dr=0, h=H, dh=0. Therefore those jets, even combined with
global closure, all F-zero values, these Fourier restrictions and
domination on some open neighborhood of D, cannot restrict A or
force A+H>=-|M|. One may choose A<-|M|-H in this relaxed class.
This is an explicit counterexample to that *relaxed* implication,
not merely a failure to find a proof of it.

### The essential missing condition is genuinely violated

If lambda!=0, take z2=R and z1=t>2R positive. L847's positive
coefficients imply G(t)>0 and G(R)>0, so F(t,R)!=0. Further,

\[
 |\lambda V(t,R)|
  =|\lambda|\frac{t^2(t-R)^2}{R^2}
  \geq |\lambda|\frac{t^4}{4R^2}>1
\]

whenever additionally t>(4R^2/|lambda|)^(1/4). At this finite
point (6)'s equality gives |q-ir|>|F|. Every nonzero-A member
therefore fails global domination explicitly. At lambda=0 the
family is admissible but has A=0, K=H>=0 and no strict gain.
No member supplies an actual counterexample to a period theorem.

The diagnostic supplies new negative evidence about the reduction:
first derivatives vanish, and even a stronger neighborhood version
of that local information has arbitrary period in a global closed
family retaining all zero values. Any successful full-class proof
must use quantitative domination away from this neighborhood, or
some additional consequence of it absent from the tested relaxation.
The original full-class rigidity question remains open; no logical
independence from its full assumptions is claimed. This stops the
unchanged diagonal first-jet mechanism. Graph realization and actual-
Xi all-degree mixed positivity remain independent gaps.

### Independent replay, 6 November 2026, step37

Use the invocation-start EXPLORE assessment
`drafts/literature/2026-11-06-diagonal-first-jet-obstruction-audit.md`,
approved separately in step36. This audit reuses its inspected calculus
and compact-series inputs, and L847/L868/C868a/C868b at their stated
scopes. It does not import a global period theorem. The following
checks reproduce the submitted calculation, rather than infer its
validity from the assessment or from the earlier stop decision.

At any point of D, choose compatible open angle charts and a compact
coordinate neighborhood with nonzero coordinates. For w=u+iv,
the identity e^w-1=w integral_0^1 e^(tw) dt bounds its modulus by
a constant times |w| on that neighborhood. The bounded z2, G factors
and inverse coordinates therefore give (3). Each of the four separate
coordinate increments has u^2+v^2=t^2. Since q(p)=r(p)=0, its difference
quotients tend to zero, with bound B|t|. C1 regularity identifies the
four partial derivatives with the full differential. This argument
requires no lower bound on G, so also covers intersections with one
or both G-zero divisors, whatever their multiplicities.

For each j, r_xj=q_yj becomes 0=0, whereas
q_xj+h_xj=-r_yj gives h_xj=0. Neither equation contains h_yj.
This last observation describes the pointwise restricted equations;
it asserts no extension theorem for arbitrary prescribed h jets.
The trace derivative in s is h_x1+h_x2=0 on D; finite-interval
constancy gives b(v). If h(p)=0, each of its four coordinate
restrictions has an interior minimum, so all four derivatives vanish.
Thus both the normal and tangential conclusions, including the
nonnegativity qualification, are checked at the original C1 regularity.

Multiplying F by V cancels z1^2 and combines the two squared
diagonal factors, giving exactly W=-C G(z1)G(z2)(z1-z2)^4/z2^4.
There is no cancellation of a zero of G and no division by F.
All expressions are holomorphic on X, including every F-zero point.
Consequently the constructed q,r are smooth and periodic; W and its
first differential vanish on D. With p=lambda W, the identities
p_yj=i p_xj give

\[
 r_{x_j}=-\operatorname{Im}p_{x_j}
          =\operatorname{Re}(i p_{x_j})=q_{y_j},\qquad
 -r_{y_j}=\operatorname{Im}(i p_{x_j})
          =\operatorname{Re}p_{x_j}=q_{x_j}.
\]

Since h=H is constant, both closure equations hold globally for
both j. Also q-ir=p, so its modulus is exactly |lambda V||F|.
Continuity makes U_lambda open and V=0 on the entire D places D
inside it. This proves domination there even at all zero intersections,
without a uniform collar or a noncompact estimate. At lambda=0 the
same statements hold with U_lambda=X.

For the mean, on every fixed finite product of circles the entire
G series converge absolutely and uniformly. Multiplication by the
finite fourth-degree polynomial preserves uniform convergence, and
z2^-4 is bounded there. In integration first in y1, all nonconstant
nonnegative z1 powers vanish. The only constant term is a0 z2^4,
from G(z1)(z1-z2)^4; hence the remaining function is -C a0 G(z2).
Its angular mean is -C a0^2. This checks (7) with both signs and
normalizations. Thus q has mean -lambda C a0^2=A at *every* radial
point, r has mean zero, and S=q+h has mean A+H. There is no moving
circle limit. A value q=0 at the fixed-angle G-zero fiber does not
say that the whole angular torus vanishes; it is consistent with this
nonzero torus mean. Positivity of C and a0 makes the choice of lambda
valid for every real A.

The retained restrictions must be checked without applying domination-
dependent theorems wholesale to this family. The equal-radius means
and the fixed-zero-fiber radial-line means follow directly from the
just-computed all-radius means. Every nonzero Fourier coefficient of
h=H is zero, so every correction bound of C868a/b holds, including
the opposite-index modes at arbitrary radial differences. In the finite
positivity test the only nonzero sequence term is its index-zero value
H; the expression is exactly H sum_(j=0)^N |c_j|^2>=0, including
N=0 and H=0. At H=0 the constructed h vanishes everywhere, which
implies both stated angular-independence conclusions.

For completeness, the nonzero-mode profile equations use only closure:
compact differentiation and angular integration by parts give
partial_xj rhat_n=i n_j qhat_n and
partial_xj Shat_n=-i n_j rhat_n. For n!=0, derivatives of rhat_n
and Shat_n in directions perpendicular to n vanish. The connected
affine lines n.x=t therefore give C1 profiles R_n(t), B_n(t).
Choose j with n_j!=0. Differentiation gives R_n'=i qhat_n,
so qhat_n also has a C1 profile Q_n; then B_n'=-i R_n,
B_n''=Q_n and R_n=i B_n'. Since Q_n is C1, B_n is C3.
Finally hhat_n=B_n-B_n''=0 here. This replays all four identities
with the correct signs, using smooth functions on compact slices,
not domination, a formal differentiated Fourier series or radial
growth. It completes the claimed list of retained restrictions.

For nonzero A, lambda is nonzero. Choose a finite positive t strictly
larger than both 2R and (4R^2/|lambda|)^(1/4), with z2=R and z1=t.
Every coefficient of G is positive, so G(t),G(R)>0. The coordinates
and t-R are nonzero; thus F(t,R)!=0. At this point
|lambda V|=|lambda|t^2(t-R)^2/R^2>
|lambda|t^4/(4R^2)>1. Hence |q-ir|>|F| and domination fails.
The test is finite for each nonzero lambda, however small. At A=0
the constructed q,r vanish and K=H>=0, so there is no strict gain.

No defect was found. The audit accepts the necessary first jets and
the arbitrary-period counterexample in the precisely stated relaxed
class. It supplies no admissible nonzero-A triple and no estimate of
K under full global domination. The unchanged local first-jet route
remains stopped; quantitative global period control, coupled graphs
and Xi transfer remain unresolved. This is validation of the local
diagnostic, not a new theorem beyond the checked sources or a further
period attempt.

## Mathlib

Full matching coverage and supporting formal coverage are unchecked;
unknown availability is not evidence of absence. The cited ordinary
calculus and compact power-series operations are standard imported
inputs. The specialization, explicit relaxed family and its failure
of full domination passed the independent informal replay above. No numerical evidence,
mathematical script, formal verification or originality claim is used.
