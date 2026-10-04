# L013 — The two-block locator cannot attain sixteen

## Hypotheses

Let F=F_(97^20), let H be the subgroup of order sixteen in F_97^*, and
let C=RS[F,H,8]. Use the event in
[the pinned model](../foundations/02-pinned-affine-line-model.md) on
1/4<=delta<5/16. Partition H into disjoint sets A,B,J of sizes 5,5,6.
Write
\[
 U(X)=\prod_{x\in A}(X-x),\quad
 V(X)=\prod_{x\in B}(X-x),\quad
 Q(X)=\prod_{x\in J}(X-x).
\]
Take exactly the two-block inputs of L008:
\[
 a_x=xQ(x),\quad b_x=-Q(x)\quad(x\in A),\qquad
 a_x=b_x=0\quad(x\notin A).
\]
Let L(T,X), D(T), and ell_x(T)=L(T,x) be L010's actual determinant
locator, Hankel determinant, and coordinate polynomials for these inputs.
For r in F, put J_r={x in J: U(x)/V(x)=r}. These ratios are defined
and nonzero, because J is disjoint from A and B.

## Conclusion

There is a constant kappa in F^* such that
\[
 L(T,X)=\kappa\,\frac{U(T)V(X)-V(T)U(X)}{X-T},\qquad
 D(T)=\kappa(U(T)-V(T)).                                  \tag{1}
\]
The quotient is a polynomial of degree four in each variable. D and all
sixteen ell_x are nonzero polynomials, so L010 applies to this entire
construction, including individual singular parameters.

There is at most one fiber J_r with r!=1 and |J_r|>=4. The number of
bad parameters is exactly
\[
 |B(a,b)|=
 \begin{cases}
 10,&\text{if no such fiber exists},\\
 11,&\text{if its size is four},\\
 15,&\text{if its size is five}.
 \end{cases}                                             \tag{2}
\]
No fiber has size six. Consequently this two-block construction cannot
satisfy the full sixteen-count equality criterion. In particular its
resultant cannot be c*P(T)^4 with c!=0 and P split squarefree of degree
sixteen **together with** simple coordinate roots and D nonzero at every
root of P. The power condition by itself is not excluded here.

The proof holds over every extension of F_97. Since these particular
inputs have prime-subfield coefficients, all their bad parameters already
lie in F_97. This is a restriction on the prescribed two-block family,
not an upper bound of fifteen for arbitrary input pairs.

## Proof

Set
\[
 K(T,X)=\frac{U(T)V(X)-V(T)U(X)}{X-T}.
\]
The numerator vanishes at X=T, so K is polynomial. Since U,V are monic
of degree five and are distinct, its X^4 coefficient is U(T)-V(T),
which is nonzero. Also K(T,X)=K(X,T), so its T-degree is exactly four.

We verify the locator identity on the actual affine moments. For i=1,...,4,
the pairing of the i-th moment row with the X-coefficients of K is
\[
 \sum_{x\in A}(x-T)Q(x)x^i K(T,x)
   =U(T)\sum_{x\in A}Q(x)V(x)x^i.                         \tag{3}
\]
This is a polynomial identity: multiplying K(T,x) by x-T removes its
defining denominator, and U(x)=0 on A. Now UVQ=X^16-1. Differentiating
and evaluating at x in A gives
\[
 U'(x)V(x)Q(x)=16x^{15},\qquad
 Q(x)V(x)x^i=16\frac{x^{i-1}}{U'(x)},
\]
using x^16=1 and U'(x)!=0. For 0<=j<=3,
\[
 \sum_{x\in A}\frac{x^j}{U'(x)}=0.                       \tag{4}
\]
Indeed, interpolate X^j on the five points A with the polynomials
U(X)/((X-x)U'(x)). The interpolation identity follows from the root
bound; comparing its X^4 coefficients proves (4). Thus (3) is zero,
and K belongs to the kernel of L010's four-by-five moment matrix over F(T).

Choose alpha in A. L008's zero-codeword representative at T=alpha has
support A minus {alpha}, of size four, with all four error values nonzero.
The Vandermonde factorization of its moment matrix gives D(alpha)!=0
(equivalently, the product identity in L010's proof). Hence that matrix
has rank four over F(T). Its kernel is one-dimensional, and its signed
minor vector L is nonzero. Therefore L=f(T)K for some f in F(T)^*.

The X-coefficients of K have gcd one in F[T]. Otherwise a common
nonconstant factor would have a root t over an algebraic closure, with
K(t,X)=0 identically. Then U(t)V(X)=V(t)U(X). Since U,V are linearly
independent, U(t)=V(t)=0, contrary to their disjoint root sets. Bezout's
identity for the coefficient gcd now expresses f as an F[T]-linear
combination of the coefficients of L, so f is polynomial. L has T-degree
at most four by its four-by-four affine minors. Since K has T-degree
four, f must be a nonzero constant kappa. This proves (1).

For fixed x in H, K(T,x) cannot be zero identically: its numerator would
give V(x)U(T)=U(x)V(T), again forcing U(x)=V(x)=0. Thus every ell_x is
nonzero. Also U-V is nonzero. These facts check all of L010's hypotheses,
and its original-event identification and converse locator test may now
be used. In particular a counted locator root is bad on its own agreement
support; this is not a substitution of closeness for input failure.

The ten parameters in A union B are bad by L008. There are no decodable
parameters of weight below four. For gamma in A the known weight-four
representative is unique, since the code's minimum weight is nine. For
gamma outside A, z=a+gamma*b has weight five, supported on A. If z-e
were a codeword for some error e of weight at most three, it would have
weight at most eight, hence be zero; that would force e=z of weight five.
If e has weight four and shares any coordinate with A, z-e again has
weight at most eight and gives the same contradiction. Thus every extra
representative has weight four and support disjoint from A. The minimum
weight assertion follows directly from the root bound for a nonzero
polynomial of degree at most seven on sixteen distinct points.

Consider a bad gamma outside A union B. Its weight is four, so D(gamma)
is nonzero by L010's Vandermonde identity. Formula (1) implies
\[
 r=U(\gamma)/V(\gamma)\ne1.
\]
For x in A or B, formula (1) shows L(gamma,x)!=0. Hence its four
coordinate roots lie in J. Each is a root of U-rV, so each belongs to J_r.
The same conclusion holds at x=gamma if gamma belongs to J: a root
of the divided difference there requires a repeated root of U-rV,
which is still a root of that polynomial. Thus |J_r|>=4 is necessary.

The polynomial U-rV is nonzero for every r, since U,V are independent.
It has degree at most five, so each fiber has size at most five. Fibers
are disjoint subsets of a six-element set, so at most one has size at
least four. The case r=1 cannot produce an extra bad parameter: at
every root of U-V the determinant D is zero, while all decodable
parameters here have weight four and D nonzero.

For the remaining r!=1, r is also nonzero. Define the monic degree-five
polynomial
\[
 F_r(X)=\frac{U(X)-rV(X)}{1-r}.
\]
It has no root in A union B. If J_r has size four, put
W(X)=product_(x in J_r)(X-x). Then F_r=(X-gamma_r)W for a unique
gamma_r in F. Formula (1), evaluated at gamma_r, makes the monic
locator exactly W: its numerator is a nonzero scalar times F_r and
division removes X-gamma_r. This remains true if gamma_r lies in J_r
and F_r has a repeated root there. D(gamma_r)!=0 since
U(gamma_r)=rV(gamma_r), V(gamma_r)!=0, and r!=1. L010's converse
therefore supplies exactly this one additional bad parameter. Conversely
any additional parameter with this fiber must remove its own linear
factor from F_r leaving all four distinct fiber roots, so it must equal
gamma_r.

If J_r has size five, F_r=product_(x in J_r)(X-x) has five simple
roots. For each gamma in J_r, the locator is its quotient by X-gamma,
with four distinct roots in H and D(gamma)!=0. L010 again proves it bad.
These five are the only additional parameters, since any such parameter
must be a root of F_r. This proves (2). All ratios, and the lone residual
linear root in the size-four case, are defined over F_97, which also proves
the extension-field assertion. No hypothesis that samples exhaust all
partitions or all input words was used.

Finally, import the monic split resultant product formula: here
Res_X(X^16-1,L(T,X))=product_(x in H) ell_x(T). If this product were
c*P^4 with P split squarefree of degree sixteen and the additional
simple-coordinate and D-nonvanishing conditions held, each root would
occur at four distinct coordinates. Its degree 64 also forces all
coordinate degrees to be four. L010's equality criterion would then
give sixteen bad parameters, contradicting (2). This uses the supporting
product identity, not a generic perfect-power theorem as an existence
claim for the moment pencil.

The exact auxiliary command `python3 scripts/resultant-pencil/check.py`
tests actual minors, the divided-difference identity, resultant powers,
fiber counts and F_(97^20) splitting on supplied prime-subfield inputs.
Its finite search does not establish the uniform restriction; the proof
above does. It independently checks the original event on all admissible
supports for one sample, without using the locator as a decoder.

## Mathlib

Coverage of this full locator identity and fiber classification: **not
checked**. No matching theorem or Lean verification is claimed. Supporting
resultant product coverage is **present** in the previously inspected
[Resultant.Basic at commit 300d0e535721bc098547106fc297d8ba2a63f6bb](https://github.com/leanprover-community/mathlib4/blob/300d0e535721bc098547106fc297d8ba2a63f6bb/Mathlib/RingTheory/Polynomial/Resultant/Basic.lean):
`Polynomial.resultant_prod_left`, `Polynomial.resultant_X_sub_C_left`
and `Polynomial.resultant_eq_prod_eval`. The full coding classification
is **absent from that source checked**; other Mathlib files were not
searched for a full match. Supporting interpolation, determinant and
Vandermonde coverage is **not checked**.

The imported resultant formula is also Milne, *Fields and Galois Theory*
v5.10 (September 2022),
[Proposition 4.35(b), printed p. 58](https://www.jmilne.org/math/CourseNotes/FT.pdf#page=58).
It supports the final product equality, not (1) or (2). The specialization
to these actual moments and the fiber restriction were not matched by the
saved literature assessment; they are potentially beyond the sources
checked, without a claim of originality. No July ABF26 correspondence
or resolution of the grand challenge is asserted.
