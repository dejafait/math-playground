# L005 — Sharp error when the support may omit one coordinate

## Hypotheses

Let F be a finite field of order q, let I have cardinality n, and let
\(x_i\in F\), \(i\in I\), be pairwise distinct. Assume
\(1\le k\le n-3\), and put
\[
 C=\{(p(x_i))_{i\in I}:p\in F[X],\ \deg p<k\}.
\]
Use the exact support-event error \(E_C\) from
[the pinned affine-line model](../foundations/02-pinned-affine-line-model.md).
Let \(1/n\le\delta<2/n\) and \(0<\varepsilon\le1\).
No smoothness or additional lower bound on q is assumed beyond the existence
of the n distinct evaluation points.

## Conclusion

The error on this radius cell is exactly
\[
 E_C(\delta)=\frac{2}{q}.
\]
Consequently this cell is safe at error budget epsilon if and only if
\(q\ge2/\varepsilon\). For \(\varepsilon=2^{-128}\), the exact condition
is \(q\ge2^{129}\). This is a statement about the given code's field;
it does not replace that field by a larger one.

In particular, the formula applies to all four listed rates on any smooth
domain of length n>=16. It determines this cell only: no largest safe radius,
claim at the excluded endpoint \(\delta=2/n\), or identification with the
unread ABF26 event is asserted.

## Proof

Since \(n-2<n(1-\delta)\le n-1\), the admissible supports are precisely
I and the sets \(I\setminus\{i\}\). This includes both support sizes and
uses the strict upper endpoint of the stated radius interval.

Write \(Q=F^I/C\), let \(\pi:F^I\to Q\) be the quotient map, let e_i
be the i-th coordinate vector, and set \(u_i=\pi(e_i)\) and
\(U_i=F u_i\). Every nonzero codeword has at least n-k+1>=4 nonzero
coordinates: a nonzero polynomial of degree less than k has at most k-1
roots, by the polynomial root bound. It follows that the images of any set
of at most three distinct coordinate vectors are linearly independent.
Indeed, a vanishing linear combination of their images would give a
codeword supported on at most three coordinates. Such a codeword must be
zero, and the coordinate vectors themselves are independent. In particular
each U_i is one-dimensional and these subspaces are pairwise distinct.

For any word z,
\[
 z|_{I\setminus\{i\}}\in C|_{I\setminus\{i\}}
 \quad\Longleftrightarrow\quad \pi(z)\in U_i.
\]
To prove this equivalence, agreement with some c in C away from i means
z-c is a scalar multiple of e_i; conversely that relation gives the required
agreement. Full-support membership is simply \(\pi(z)=0\).

Fix a,b and set \(A=\pi(a)\), \(B=\pi(b)\). On any support where
\(a+\gamma b\) is a code restriction, failure of either input to be a
code restriction is equivalent to failure of b alone. If b were a code
restriction, subtracting \(\gamma b\) would show that a is one too;
the reverse implication follows from the event's disjunction. Thus the
full support witnesses gamma exactly when
\[
 A+\gamma B=0,\qquad B\ne0,
\]
and a support omitting i witnesses it exactly when
\[
 A+\gamma B\in U_i,\qquad B\notin U_i.                 \tag{1}
\]
These descriptions preserve failure on the same support as agreement.

If B=0, neither condition can hold, so there are no bad challenges. Suppose
B is nonzero and consider the affine line \(\ell=A+F B\) in Q; its
parameter gamma is injective.

If zero belongs to this line, let gamma_0 be its unique zero parameter.
For any other gamma,
\(A+\gamma B=(\gamma-\gamma_0)B\) is a nonzero multiple of B.
Membership in U_i then forces B into U_i, which violates (1). Full-support
membership also fails away from gamma_0. Hence only gamma_0 is bad, and it
is bad on the full support. This handles lines contained in some U_i as
well as other lines through the origin.

If zero does not belong to the line, A and B are linearly independent and
the full support never witnesses a challenge. Every bad challenge must
satisfy (1) for some i and gives a nonzero intersection point
\(P_i=A+\gamma B\) in U_i. A fixed i can supply at most one challenge:
subtracting two such relations would put B in U_i. A nonzero point also
belongs to at most one U_i, since these one-dimensional subspaces are
distinct. If three distinct bad challenges existed, they would therefore
give nonzero scalar multiples of three distinct coordinate images. Those
three vectors are independent by the weight argument, but all lie in
\(\operatorname{span}(A,B)\), which has dimension two. This contradiction
proves at most two bad challenges for every pair a,b.

For attainment, choose distinct i,j, take \(a=e_i\), and take
\(b=e_j-e_i\). At gamma=0 the combination is e_i, which agrees with the
zero codeword off i. Its direction image \(B=u_j-u_i\) does not lie in
U_i, by independence of u_i,u_j. Thus the support omitting i witnesses a
bad challenge. At gamma=1 the combination is e_j and B does not lie in
U_j, so the support omitting j witnesses another bad challenge. These two
field elements are distinct, including in characteristic two. The uniform
upper bound proves that this pair attains exactly two, so division by q and
maximization over a,b give the stated formula.

Multiplying \(2/q\le\varepsilon\) by the positive quantities q and
\(1/\varepsilon\) gives precisely \(q\ge2/\varepsilon\). When n>=16
and k/n is one of 1/2, 1/4, 1/8, or 1/16, we have 1<=k<=n/2<=n-3;
thus these parameters satisfy the hypothesis on any available smooth domain.

For comparison, L004 at this support cutoff permits
\[
 K_{n-1}=\left\lfloor
 \frac{\binom n{k+1}}{\binom{n-2}k}\right\rfloor
 =\left\lfloor\frac{n(n-1)}{(k+1)(n-k-1)}\right\rfloor
\]
bad challenges. For length 16 and k=8,4,2,1, these numbers are 3,4,6,8,
respectively. The present exact count is 2 in all four cases. This comparison
does not use the multiplicity bound to prove the new formula. It sharpens a
small-radius cell and does not extend L004's certified interval
\(\delta<90/256\) for its length-256 example.

The argument only uses the absence of nonzero codewords of weight at most
three. That condition cannot simply be dropped. For example, over F_5 take
evaluation points 0,1,2,3, k=2, a=(0,0,0,1), and b=(0,0,1,1). The challenges
0,1,2,4 agree with the polynomials 0,X-1,X,0 on supports omitting coordinates
3,0,1,2 respectively. On each of these triples b has two equal values and
one different value, so it cannot agree with an affine polynomial: a
nonconstant affine polynomial is injective, and a constant one has all
values equal. Thus all four challenges are bad at support cutoff three.
Here k=n-2, outside the stated hypotheses.

The auxiliary command `python3 scripts/one-coordinate/check.py` checks this
boundary example and enumerates the original support event using evaluated
polynomials, over both prime fields and F_4, for every pair modulo independent
codeword translations. It also checks the displayed attaining pair. The
general result is proved above; finite enumeration is auxiliary.

## Mathlib

Coverage of the full statement and its supporting quotient-space and
minimum-distance facts in Mathlib: **not checked**. No matching library
theorem or Lean verification is claimed. The needed weight bound and quotient
argument are proved above from the polynomial root bound.

The previously read ArkLib declarations
[`CoreDefinitions.IsMCA` and `CoreDefinitions.mcaError`](https://github.com/Verified-zkEVM/ArkLib/blob/e65197892890b8fd9b0dc05b8980273cf1d595cc/ArkLib/Data/CodingTheory/ProximityGap/ProximityGenerators.lean#L98)
support the frozen event definition. ArkLib is separate from Mathlib; these
definitions are not a matching theorem for this sharp error or a certification
of the current ABF26 correspondence.
