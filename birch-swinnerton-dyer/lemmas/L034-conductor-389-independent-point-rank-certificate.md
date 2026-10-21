# L034 — Published independent points complete the fixed rank certificate

## Hypotheses

Let E/Q have the equation y^2+y=x^3+x^2-2x, with Weierstrass
coefficients [0,1,1,-2,0]. Set P=(0,0), Q=(1,0) and p=7.
Use the classical cyclotomic Selmer dual X and A=Lambda_(T),
M=X tensor_Lambda A, f_X of L004. Use exactly L033's primitive
ordinary L_7(E,T)=sum a_j T^j: trivial Teichmuller branch, total
minimal real period and kappa(gamma)=8. The normalization is that of
[foundations/05](../foundations/05-kato-divisibility.md).

The arithmetic point input is the published computational group result
of J. E. Cremona, *Algorithms for Modular Elliptic Curves*, corrected
online second edition (CUP, 1997), Table 2, printed p.257, row 389A1,
interpreted by Chapter 4, printed p.105. Its provenance and qualifications
are specified below. L030 supplies minimality and non-CM; audited L033
supplies the ordinary prime and coefficient enclosure. No complex
analytic order or finiteness of Sha is a hypothesis.

## Conclusion

The images of P,Q in E(Q) tensor_Z Q are independent, and

\[
\operatorname{rank}E(\mathbf Q)
=\operatorname{ord}_T f_X
=\operatorname{ord}_T L_7(E,T)=2.
\]

The group Sha(E/Q)[7^infinity] is finite, TM=0,
M is isomorphic to (A/(T))^2, and the natural map
M[T] -> M/TM is an isomorphism. The canonical cyclotomic 7-adic
height on E(Q) tensor_Z Q_7 is nondegenerate. Also a_0=a_1=0
exactly and v_7(a_2)=0.

These are fixed-instance arithmetic and p-adic conclusions. This file
does not establish the complex analytic order m(E), full Sha finiteness,
its 7-primary order, or a refined leading-coefficient formula. It is not
a BSD candidate. Rank two itself is already covered by the imported
published basis result; the local advance is completing the notebook's
point/coefficient application, not a discovery beyond the checked sources.

## Proof

**Precise known point input and model match.** The general Weierstrass
convention is y^2+a_1 xy+a_3 y=x^3+a_2 x^2+a_4 x+a_6. Thus the
coefficient vector [0,1,1,-2,0] is precisely the displayed equation.
For P both sides are zero; for Q the right side is 1+1-2=0 and
the left side is zero. These substitutions check rational membership,
not independence.

Cremona's [Chapter 4, p.105](https://johncremona.github.io/book/fulltext/chapter4.pdf#page=2)
defines Table 2's entries as generators of the Mordell--Weil group
modulo torsion. Its [Table 2, p.257, row 389A1](https://johncremona.github.io/book/fulltext/table2.pdf#page=3)
lists (0,0),(1,0). The author's
[ecdata TABLE TWO: GENERATORS](https://johncremona.github.io/ecdata/)
identifies this example explicitly as [0,1,1,-2,0] with those two
generators. The matching
[allgens row](https://raw.githubusercontent.com/JohnCremona/ecdata/master/allgens/allgens.00000-09999)
is `389 a 1 [0,1,1,-2,0] 2 [] [0:0:1] [1:0:1]`, inspected
2026-10-08 in the prior source assessment. Capital A in the book is
lowercase a in that data. The projective points have z=1, hence give
exactly the stated affine coordinates without any change of model.

Import the published basis assertion, not a numerical rank label,
regulator, or a BSD-based prediction. The corrected edition and
[errata of 26 September 2003](https://johncremona.github.io/book/errata.pdf)
have no correction to this entry. Cremona's *The elliptic curve database
for conductors to 130000*, ANTS VII, LNCS 4076 (2006),
[Sections 2.3--2.4, PDF pp.5--6, and 3.4, PDF pp.13--15](https://johncremona.github.io/papers/ecdb_ants.pdf)
describe point search, 2-descent, saturation and arithmetic verification
of rank-two entries. They acknowledge possible software/data-processing
errors and finite-index qualifications for some larger database entries.
The original execution transcript is not independently replayed here.
This is a precise cited computational group result. Even a finite-index
qualification would not impair the independence consequence used here;
no saturation or exact torsion assertion is needed in the application.

By the imported basis assertion, E(Q)/E(Q)_tors is free with the two
displayed basis images. Tensoring with Q makes them a Q-basis. More
explicitly, a rational relation can be multiplied by a common denominator;
its integral relation in the free quotient has both coefficients zero.
This gives L004's independent-point premise k=2. Distinctness or the
coordinate substitutions alone would not give it. Reproving the known
height/descent calculation would supply no additional needed hypothesis.

**All remaining L004 premises.** L030 proves that the displayed integral
equation is globally minimal with discriminant 389 and is non-CM.
L033 proves that 7 is a good ordinary prime: 7 does not divide 389,
#E(F_7)=13 and the Frobenius trace is -5, a 7-adic unit. In particular
p>=5. Its audited coefficient is for precisely the primitive ordinary
series and coordinate stipulated above, with no Euler-factor removal.
It gives

\[
v_7(a_2-13/256)\ge1>v_7(13/256)=0.
\]

Since 7 divides neither 13 nor 256, L004's strict finite-precision test
applies and gives a_2 nonzero with valuation zero. The source-backed
point pair and this coefficient therefore meet every L004 premise with
k=n=2. No residual-surjectivity condition is added: the checked Kato
divisibility in foundations/05 covers both representation cases after
inverting 7. Neither a lower coefficient's vanishing nor finite Sha
was used as a premise.

**Application and scope.** Put r=rank E(Q),
s=corank_Z_7 Sha(E/Q)[7^infinity], delta=length_A(TM),
h=ord_T f_X and ell=ord_T L_7. L004 gives the complete chain

\[
2\le r\le r+s+\delta=h\le\ell\le2.
\]

Every term is two; hence s=delta=0. All the asserted finite-primary,
module and height consequences are exactly L004's matching-case
conclusions, using its L003 converse in the now-checked non-CM scope.
The equality ell=2 yields a_0=a_1=0 exactly; finite approximations
were not used to infer those equalities. The coefficient valuation was
already obtained from the strict enclosure.

The intermediate test succeeds at the actual required threshold of two
independent points and degree two. General uniform production of such
points and coefficients, and their comparison with complex order, remain
unresolved. No other premises of the L026/L025 general route have been
silently supplied. The stopped precision schedule of L033 and the
production obstructions of ATTEMPTS/022--023 are unaffected.

**Separate critical audit, 2026-10-08.** The approved fixed-scope audit
passes. It reuses the inspected primary evidence in the point assessment
and the completed L033 audit; it does not replay Cremona's descent or
L033's finite arithmetic. The table's group interpretation, exact model,
rank-two entry and two listed generators together supply a basis of the
free quotient. A list of two generators without the rank/basis assertion
would not suffice. The coordinate conversion at z=1 and rational
membership checks above agree with that assertion. The source's
computational provenance remains an explicit qualification.

The arithmetic inputs are precisely L030's minimal non-CM model and
L033's good ordinary prime and primitive coefficient. Here 7>=5,
7 does not divide 389, and 7 does not divide the trace -5. The symbol
normalization uses the total minimal real period, the trivial branch
and gamma with kappa(gamma)=8 throughout. The certified quadratic
coefficient is not substituted from a differently scaled coordinate.
The limiting error threshold is N=1, not the unit-root precision 3;
it strictly exceeds v_7(13/256)=0. Thus the coefficient has valuation
zero even though its exact value need not be 13/256.

For the consequence audit, write D=Sha(E/Q)[7^infinity]. The classical
control and Kummer inputs of L002 give h=r+s+delta, with both defects
nonnegative. Kato divisibility as recorded in foundations/05 gives
L_7=f_X g with g in Lambda[1/7], in both representation cases. This
ring embeds in Q_7[[T]], so g has no negative T-powers. The nonzero
quadratic coefficient makes L_7 and hence g nonzero, giving h<=ell<=2.
The independent points give 2<=r. This checks every link of the squeeze
without using complex order, lower coefficient vanishing or finite Sha.

To check finiteness rather than just zero corank, D^vee is a submodule
of the finitely generated Z_7-module S_0^vee. It is finitely generated
and has rank s=0, hence is finite; Pontryagin duality makes D finite.
Since delta=length_A(TM)=0, TM=0. The DVR decomposition of L002 and
length_A(M)=h=2 then give M=(A/(T))^2 up to isomorphism. In particular
M[T]=M and M/TM=M, so their natural map is the identity under these
canonical identifications, not merely an equality of dimensions.
These arguments check the finite-primary and module conclusions
independently of any height nondegeneracy premise.

Finally the arithmetic converse is Stein--Wuthrich, Theorem 6.1,
printed p.1776, cited in foundations/04 and used in L003. Its classical
Selmer convention, standing non-CM restriction and odd good ordinary
prime all match; h=r (and the now-proved finite D) yields nondegeneracy
of the canonical cyclotomic height. This is an algebraic characteristic
order theorem, not the conjectural analytic p-adic BSD formula.
The exact equality ell=2 proves a_0=a_1=0 by the definition of order.
No claim about |D| follows from this order argument: the unspecified
power of 7 in the divisibility provides no integral valuation bound.
Full Sha finiteness and complex order remain outside the conclusion.
All asserted consequences pass, with the required and achieved
point/coefficient thresholds both equal to two. This is local
verification of the known-result application, not a new theorem
beyond the checked sources or a BSD candidate.

## Mathlib

Full matching coverage for this published fixed basis result and its
arithmetic/p-adic application: **not checked**. Supporting rational
point, tensor-independence and valuation coverage: **not checked**.
No absence claim is made. The known arithmetic result is imported by
the precise citations above; this write-up is an informal application,
not a formal or independently replayed proof of the published descent.
