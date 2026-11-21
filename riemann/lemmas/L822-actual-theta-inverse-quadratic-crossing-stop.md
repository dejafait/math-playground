# Lemma 822: actual theta inverse averaging increases quadratic crossings

## Hypotheses

Use the actual, untruncated theta kernel K of L019 and the normalization
of L795:

\[
m_j=\int_0^\infty u^{2j}K(u)\,du,\qquad
d\mu(u)=K(u)\,du/m_0.
\]

L021 gives finite positive m_j, in particular for 0<=j<=3. The law mu
is a probability measure with positive measure on every nonempty open
subinterval of (0,infinity). On the real vector space of polynomials
of degree at most three, define the linear operators

\[
(A_3p)(x)=\int_0^\infty p(u^2x)\,d\mu(u),\qquad
B_3(x^j)=\frac{m_0}{m_j}x^j\quad(0\le j\le3).
\]

For a nonzero real polynomial p, let v_+(p) be the supremum of the
number of sign alternations in finite sequences of nonzero values
p(x_1),...,p(x_r), where 0<x_1<...<x_r<infinity. Set v_+(0)=0.
Values equal to zero are omitted, rather than assigned a sign.

## Conclusion

Both compositions A_3 B_3 and B_3 A_3 are the identity. Both operators
preserve the degree of every nonzero input in the stated space.
Nevertheless, for the single admissible input f(x)=(1-x)^2,

\[
v_+(f)=0,\qquad v_+(B_3f)=2.
\]

Thus B_3 is not variation diminishing on (0,infinity) for all nonzero
real polynomials of degree at most three. This rejects that universal
inverse premise for the actual theta law. It asserts nothing against
restricted input classes, actual averaged Laguerre root counts, mixed
positivity or RH.

## Proof

**Finite inverse and integrability.** If p(x)=sum_(j=0)^3 c_j x^j,
then for each real x,

\[
\int_0^\infty |p(u^2x)|\,d\mu(u)
\le\sum_{j=0}^3 |c_j||x|^j\frac{m_j}{m_0}<\infty.
\]

Integrating this finite sum gives

\[
(A_3p)(x)=\sum_{j=0}^3c_j\frac{m_j}{m_0}x^j.
\]

All these multipliers are positive and nonzero; for j=0 the multiplier
is 1. Multiplication by m_0/m_j in the monomial basis cancels them
in either order, proving both inverse identities. A nonzero leading
coefficient remains nonzero under each operator, including for constant
inputs. No infinite sum or interchange of limits is used.

**Strictness for the actual law.** Apply the named Cauchy–Schwarz
inequality, including its linear-dependence equality characterization,
to 1 and u^2 in the real Hilbert space L2(mu). Their squared norms are
1 and m_2/m_0, and their inner product is m_1/m_0. These are finite
by L021. Equality would require u^2=c for mu-almost every u, for a
real constant c. This is impossible: each of (1,2) and (3,4) has positive
mu measure by L019/L795, so a full-measure set on which u^2=c would
meet both intervals. The corresponding squared values lie in the
disjoint intervals (1,4) and (9,16). Consequently

\[
m_1^2<m_0m_2.                                           \tag{1}
\]

This argument retains the actual full support; a point-mass law would
not satisfy the strict conclusion.

**The fixed image and all its roots.** Set a=m_0/m_1 and b=m_0/m_2.
Both are strictly positive. Since denominators are positive, (1) is
equivalent to a^2>b. The definition of B_3 gives exactly

\[
q(x):=(B_3f)(x)=1-2ax+bx^2.
\]

It has degree two, q(0)=1, positive leading coefficient b and
discriminant 4(a^2-b)>0. By the quadratic formula its roots are

\[
r_- =\frac{a-\sqrt{a^2-b}}{b},\qquad
r_+ =\frac{a+\sqrt{a^2-b}}{b}.
\]

Since b>0 and 0<sqrt(a^2-b)<a, these satisfy 0<r_-<r_+<infinity.
Both are simple. Factoring q=b(x-r_-)(x-r_+) gives positive values
on (0,r_-), negative values on (r_-,r_+) and positive values on
(r_+,infinity). Choosing one point in each interval gives two sign
alternations. There cannot be more: by continuity each alternation
between successive sample points requires a root in the open interval
between them, and these intervals are disjoint. This quadratic has
exactly two roots. Hence v_+(q)=2.

The input f is strictly positive for x>0 except at its double root
x=1. Every permitted nonzero sample value is positive, so v_+(f)=0.
There is no endpoint root for either f or q. In general a nonzero real
polynomial changes sign at an interior root precisely when its
multiplicity is odd: locally write it as (x-r)^k h(x), with h continuous
and nonzero near r. Between successive roots its sign is constant.
This also explains directly why the input's even root contributes no
crossing and each simple output root contributes one. The zero
polynomial convention does not affect this nonzero witness.

**Relation to the known quadratic diagnostic.** A. Guterman and
B. Shapiro, *On linear operators preserving the set of positive
polynomials*, Journal of Fixed Point Theory and Applications 3 (2008),
411–429, [author manuscript, Lemma 3.2, pp.7–8, complete i=1
proof](https://staff.math.su.se/shapiro/Articles/FinalPosit.pdf)
(unversioned manuscript inspected 2026-11-05), give the necessary
diagonal condition lambda_1^2<=lambda_0 lambda_2 for preservation of
strict positivity on the whole real line when degree two is available.
For the present inverse multipliers, lambda_0=1, lambda_1=a and
lambda_2=b, (1) violates that condition. The reference's strictly
positive input convention does not include our square, and its domain
is the whole real line. We therefore use its quadratic discriminant
method, rather than import an unstated half-line sign-count theorem.
The explicit roots and crossing analysis above supply exactly the
changed-domain specialization for this nonnegative input, which the
universal inverse premise does include. This is reproduction of a
known method with the actual law, not a new general preserver theorem.
No real-rootedness multiplier classification or inverse-hyperbolicity
equivalence is needed or asserted. The test stops here; no cubic
sweep or conclusion about all restricted inverse constructions follows.

**Independent audit, 5 November 2026 (step619).** Replayed the proof under
the pre-existing SPECIALIZE assessment
`drafts/literature/2026-11-05-theta-inverse-quadratic-audit.md`.
The audit accepts the statement without repair. This verifies a local
specialization of known mathematics, not a new general theorem.

For each real x the displayed absolute-integral bound uses exactly
m_0 through m_3 and a finite sum. Thus both maps act on the stated
four-dimensional space; the diagonal multipliers and their reciprocals
are finite and strictly positive, including the constant multiplier 1.
This verifies both compositions and degree preservation, rather than
only a right inverse. L019/L021 and L795's support passage supply the
actual law; no additional hypothesis on zeros of Xi is used.

The equality check is valid in L2(mu): 1 has norm 1, and u^2 has
finite squared norm m_2/m_0. Equality implies u^2=c almost everywhere.
A full-measure set meets each positive-measure interval (1,2) and
(3,4), where the possible values of u^2 are disjoint. Equality is
therefore excluded. In particular the discriminant comparison is
exactly
\[
a^2-b=\frac{m_0(m_0m_2-m_1^2)}{m_1^2m_2}>0.
\]
All denominator and strictness hypotheses are paid by the actual law.

Since 0<sqrt(a^2-b)<a and b>0, both displayed output roots are finite,
strictly positive and distinct. The factorization gives the three
successive signs +,-,+. Every alternation in any finite nonzero sample
sequence forces a root in a disjoint intervening open interval, so
the exhibited two alternations are also the exact maximum. The square
has only positive nonzero values, even across its double root; its
count is exactly zero under the stated convention. Hence the stop
does include the proposed universal class's even-root inputs. It
does not exclude a separately specified restricted class. No cubic
sweep, numerical moment enclosure, reference-Laguerre application,
mixed-positivity transfer or RH conclusion is established. The cited
whole-line strict-positivity theorem remains methodological context;
the local proof itself supplies the changed-domain conclusion.

## Mathlib

Full matching coverage is not checked. Neither the actual-theta
inverse specialization nor this precise half-line count is claimed
to be present or absent in Mathlib. Supporting named mathematical
inputs are Cauchy–Schwarz with its equality case, the quadratic formula
and the intermediate value theorem; formal coverage and theorem names
for these applications have not been checked. No formal proof is claimed.
