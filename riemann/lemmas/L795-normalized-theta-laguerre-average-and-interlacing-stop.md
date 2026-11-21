# Lemma 795: normalized theta/Laguerre average and full-support interlacing stop

## Hypotheses

Let K be the strictly positive theta kernel of L019, and put

\[
 m_j=M_{2j}=\int_0^\infty u^{2j}K(u)\,du,\qquad
 d\mu(u)=K(u)\,du/m_0.
\]

L021 gives 0<m_j<infinity for every integer j>=0. For an integer d>=0
define

\[
 P_d(x)=\sum_{j=0}^d(-1)^j\binom dj
       \frac{j!m_j}{(2j)!m_0}x^j,\qquad
 F_{d,u}(x)=\frac{d!}{(1/2)_d}
       L_d^{(-1/2)}(u^2x/4),\quad u\ge0.
\]

Here (a)_j is the rising factorial, with (a)_0=1, and the Laguerre
convention is NIST DLMF 18.5.12. An interlacer of a quadratic with
ordered real roots r_1<=r_2 is a real linear polynomial whose root lies
in [r_1,r_2], allowing endpoint equality. This is the degree-two case
of the common-interlacing definition cited below.

## Conclusion

For every fixed d and x in C the integral below is absolutely convergent,
and the following polynomial identity has exactly the stated scaling:

\[
 P_d(x)=\int_0^\infty F_{d,u}(x)\,d\mu(u).                 \tag{1}
\]

In the coefficient convention a_j=m_j/[8\,4^j(2j)!] of L776,
the coefficient magnitude in P_d is binom(d,j)j!4^j a_j/a_0.
In particular P_d(0)=1; no extra factor 8 or 4 is suppressed in (1).

For u>0 the quadratic F_{2,u} has positive leading coefficient and roots

\[
 \frac{6-2\sqrt6}{u^2},\qquad \frac{6+2\sqrt6}{u^2}.       \tag{2}
\]

The polynomials F_{2,1} and F_{2,4} have no common interlacer. More
strongly, the same holds for every pair F_{2,u},F_{2,v} with

\[
 u\in A=(9/10,11/10),\qquad v\in B=(39/10,41/10).         \tag{3}
\]

Both A and B have positive mu measure. Consequently there is no single
linear interlacer valid for all positive support scales, or even for
mu-almost every scale. This stops the proposed full-support
common-interlacing sufficient mechanism already in degree two.
It does not assert failure of real-rootedness of P_2, any other P_d,
or the actual Xi positivity statements.

## Proof

**Imported formula and coefficient specialization.** NIST DLMF,
version 1.2.8 (15 September 2026),
[18.5.12](https://dlmf.nist.gov/18.5.E12) and
[13.2.2](https://dlmf.nist.gov/13.2.E2), give

\[
 \frac{d!}{(\alpha+1)_d}L_d^{(\alpha)}(z)
 ={}_1F_1(-d;\alpha+1;z)
 =\sum_{j=0}^d\frac{(-d)_j}{(\alpha+1)_j\,j!}z^j.
\]

The parameter b=alpha+1=1/2 is not a nonpositive integer. Thus the
formula is valid here, its denominators are nonzero, and it terminates
because d is a nonnegative integer. The elementary finite products give

\[
 \frac{(-d)_j}{j!}=(-1)^j\binom dj,\qquad
 (1/2)_j=\frac{1\cdot3\cdots(2j-1)}{2^j}
        =\frac{(2j)!}{4^j j!}\quad(0\le j\le d).
\]

The latter equality also holds at j=0 by the empty-product convention.
No Gamma duplication or continuation through Gamma poles is needed.
Substituting z=u^2x/4 proves

\[
 F_{d,u}(x)=\sum_{j=0}^d(-1)^j\binom dj
                  \frac{j!}{(2j)!}u^{2j}x^j.             \tag{4}
\]

In particular the constant term is 1. For each fixed x,

\[
 \int_0^\infty |F_{d,u}(x)|\,d\mu(u)
 \le \sum_{j=0}^d\binom dj\frac{j!}{(2j)!}|x|^j
                        \frac{m_j}{m_0}<\infty.
\]

Only finitely many integrable summands are exchanged with the integral.
Integrating (4) proves (1). Inserting L776's a_j gives the stated
coefficient relation directly; none of that lemma's conditional zero
count, Fredholm identity or norm hypothesis is used.

For context, alpha=-1/2 also satisfies alpha>-1 in the classical
Laguerre orthogonality theorem, with weight z^alpha e^(-z) on
(0,infinity): DLMF [Table 18.3.1](https://dlmf.nist.gov/18.3.T1) and
[18.2(vi)](https://dlmf.nist.gov/18.2#vi). Hence for d>=1 and u>0
these references have d simple positive roots. This standard fact is
imported, not reproved or extended to averages. At u=0 the reference
is 1 and its degree drops; mu has no atom there. The obstruction below
uses only u>0 and does not depend on this endpoint or on the general
orthogonality theorem.

**Exact quadratic test.** Formula (4) at d=2 is

\[
 F_{2,u}(x)=1-u^2x+\frac{u^4}{12}x^2.
\]

The quadratic formula proves (2), with discriminant (2/3)u^4>0.
Write a=6-2sqrt(6), b=6+2sqrt(6). Since sqrt(6)<5/2, we have a>1
and b<11. Thus the interlacer intervals for u=1 and u=4 satisfy

\[
 b/16<11/16<1<a;
\]

they are disjoint. Their leading coefficients are respectively 1/12
and 256/12, both positive, and both polynomials have degree two.

For the robust statement, (3) and positivity of a,b imply

\[
 \frac b{v^2}<\frac{1100}{1521}
 <\frac{100}{121}<\frac a{u^2}.
\]

The middle comparison is exact: 1100*121=133100<152100=100*1521.
So even the upper root for v lies strictly below the lower root for u,
uniformly on the displayed neighborhoods.

**Support and the almost-everywhere premise.** L019's differentiated
theta series converges locally uniformly and defines continuous K>0
on [0,infinity). In particular each nonempty open subinterval of
(0,infinity) has strictly positive integral against K(u)du: choose a
point in the interval and then a smaller neighborhood where K has a
strictly positive lower bound. Thus A and B have positive mu measure,
and 1 and 4 belong to the support. No positive point mass is asserted.
If one linear polynomial interlaced F_{2,u} for u in a full-mu-measure
set E, then E would meet both A and B. Selecting one scale from each
intersection contradicts the uniform interval separation. Thus changing
the references on a null set cannot supply a common interlacer.

**Scope of the imported sufficient criterion.** A. Marcus, D. Spielman
and N. Srivastava, *Interlacing families II: Mixed characteristic
polynomials and the Kadison--Singer problem*, Annals of Mathematics
182 (2015), 327--350,
[Definition 3.1, pp.331--332, and Lemma 3.5, p.333](https://www.cs.yale.edu/homes/spielman/PAPERS/Marcus_Spielman_Srivastava_IFII.pdf),
use weak root alternation and, for a finite collection of equal-degree
real polynomials with positive leading coefficients, equate common
interlacing with real-rootedness of every convex combination. We use
the definition to exclude its common-interlacing premise on a finite
pair from the support. No extension of the finite lemma to an integral
is asserted or needed for this exclusion. Failure of that sufficient
premise is not failure of the particular average in (1). Full unbounded
theta support is retained throughout; there is no truncation or limit
of an interlacing family. Actual-weighted compensation, other realizations,
degree-uniform signs and the main RH gap remain unresolved.

## Mathlib

Full matching coverage has not been checked. Availability of the
Laguerre expansion, theta-weighted averaging specialization and
common-interlacing obstruction in Mathlib is unknown; no formal theorem
is claimed. The elementary finite-product and quadratic calculations
above form the complete local specialization of the cited results.
