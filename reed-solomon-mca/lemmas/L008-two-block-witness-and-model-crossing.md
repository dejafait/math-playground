# L008 — Two blocks give a half-distance witness and a model crossing

## Hypotheses

Let F be a finite field of order q, let I have n elements, and let
the evaluation points x_i in F be pairwise distinct. Let r>=1 and k>=2
be integers satisfying n-k=2r, and let
\[
 C=\{(p(x_i))_{i\in I}:p\in F[X],\ \deg p<k\}.
\]
Use E_C from
[the pinned affine-line model](../foundations/02-pinned-affine-line-model.md).
For the general lower bound assume r/n<=delta<=1.

The special case takes F=F_(17^s), s>=1, the evaluation domain F_17^*
inside F, n=16, k=8, and r=4. The crossing statement further fixes s=32
and the prescribed error budget 2^-128.

## Conclusion

For every such code,
\[
 E_C(\delta)\ge\frac{2r+2}{q}\qquad(r/n\le\delta\le1).       \tag{1}
\]
This is a lower bound, not an assertion of the exact error on the cell.
It is witnessed by two disjoint coordinate sets of size r+1, with a
different matching codeword on one of the two sets of challenges.

In the special smooth example this supplies ten bad challenges over
every F_(17^s), so
\[
 E_C(\delta)\ge10/q\qquad(1/4\le\delta\le1).               \tag{2}
\]
For q=17^32, combining (2) with L007 gives the exact safe set for this
particular code and frozen event:
\[
 \{\delta\in[0,1]:E_C(\delta)\le2^{-128}\}=[0,1/4).        \tag{3}
\]
Thus 3/16 is its largest safe grid radius, 1/4 is the supremum of its
safe real radii, and there is no largest safe real radius. This is not
a resolution of the grand challenge: the ABF26 event, endpoint convention,
and field-size qualifications remain unverified, and other codes and
budgets are not determined here.

## Proof

Since n=k+2r>=2r+2, choose disjoint subsets A,B of I with
|A|=|B|=r+1. Let R=I minus (A union B), and put
\[
 Q(X)=\prod_{i\in R}(X-x_i).
\]
The empty product is one, so this includes k=2. The degree of Q is
n-2r-2=k-2. It vanishes at the coordinates in R and is nonzero at
every coordinate in A union B, because all evaluation points are distinct.
Define input words by
\[
 a_i=\begin{cases}x_iQ(x_i)&i\in A,\\0&i\notin A,\end{cases}
 \qquad
 b_i=\begin{cases}-Q(x_i)&i\in A,\\0&i\notin A.\end{cases}   \tag{4}
\]
We will exhibit one bad challenge at x_j for every j in A union B.
These 2r+2 challenges are distinct. The supports below all have size
n-r and are therefore admissible at every delta>=r/n.

First let j belong to A and take gamma=x_j. The combination a+gamma*b
is zero outside A and at j. It agrees with the zero codeword on
\[
 S_j=I\setminus(A\setminus\{j\}),\qquad |S_j|=n-r.
\]
Suppose b restricted to S_j were the restriction of a polynomial p of
degree less than k. It would vanish at all the n-r-1=k+r-1>=k
coordinates outside A. The polynomial root bound forces p=0. But its
value at j would have to be -Q(x_j), which is nonzero. This contradiction
proves failure on the same support S_j. The error off this support has
weight exactly r, since (x_i-x_j)Q(x_i) is nonzero for each i in A
other than j.

Now let j belong to B and again take gamma=x_j. The polynomial
\[
 p_j(X)=(X-x_j)Q(X)
\]
has degree k-1, so its evaluation belongs to C. It agrees with the
combination from (4) on A, is zero with that combination on R, and is
zero at j. Consequently it agrees on
\[
 T_j=I\setminus(B\setminus\{j\}),\qquad |T_j|=n-r.
\]
Suppose a polynomial p of degree less than k matched b on T_j. The
polynomial p+Q, also of degree less than k, would vanish on A union R,
which has n-r-1=k+r-1>=k distinct coordinates. The root bound forces
p=-Q. At j, however, b_j=0 whereas -Q(x_j) is nonzero. This again
proves failure on the same support. The error has weight exactly r on
B minus {j}, since p_j is nonzero at all those coordinates.

The root bound used twice here follows by factoring X-x_i for each
distinct root of a nonzero polynomial; its number of roots cannot exceed
its degree. All the arguments take place over F itself. In particular,
they exclude matching polynomials with coefficients anywhere in F, not
only in a smaller field containing the construction's coefficients.

Thus each of the 2r+2 parameters has a code restriction of the combination
and a noncode restriction of b on the very same admissible support.
The original disjunction of input failures therefore holds. The uniform
sampling probability for this fixed pair is at least (2r+2)/q, and
maximizing over pairs proves (1). There is no assumption of one codeword
or one support shared by different challenges.

For the special example, identify coordinates with 1,...,16 in the prime
subfield F_17. Take
\[
 A=\{1,2,3,4,5\},\qquad B=\{6,7,8,9,10\},
 \qquad Q(X)=\prod_{j=11}^{16}(X-j).
\]
In F_17[X] this product is
\[
 Q(X)=X^6+4X^5+5X^4+4X^3+9X^2+13X+6.
\]
The words (4), ordered by coordinates 1,...,16, are
\[
 a=(8,13,16,8,5,0,0,0,0,0,0,0,0,0,0,0),
\]
\[
 b=(9,2,6,15,16,0,0,0,0,0,0,0,0,0,0,0).
\]
The ten distinct parameters 1,...,10 have the supports proved above.
Their verification uses only the prime-subfield data and the root bound
over the full extension, so (2) holds for every s>=1. The domain is the
multiplicative subgroup F_17^* of order 16=2^4 in every such extension.
It is smooth in the frozen definition, and its rate is the listed 1/2.

To prove (3), L007 gives E_C(delta)=5/q on [3/16,1/4), uniformly over
all input words in each extension field. Exact integer comparison gives
\[
 5\cdot2^{128}\le17^{32}<7\cdot2^{128}<10\cdot2^{128}.
\]
The error E_C is nondecreasing in delta: increasing delta only enlarges
the permitted collection of supports for every fixed pair, and the same
is true after maximizing over pairs. It follows from the safety at 3/16
and throughout [3/16,1/4) that every delta<1/4 is safe. Equation (2)
and the strict comparison above make every delta>=1/4 unsafe. This
proves (3), including its excluded endpoint. The field and the code
remain fixed throughout this comparison.

The count ten exceeds the actual allowable integer count
floor(17^32/2^128)=6. For comparison, L004's upper count on this cell
is floor(binomial(16,9)/binomial(11,8))=69. Thus the present result is
an explicit unsafety witness; it does not identify the sharp count between
ten and 69 or infer unsafety from failure of that sufficient upper bound.
At n=256,k=128,r=64, the same general construction supplies only 130
parameters, and 130*2^128<257^32. It therefore does not settle the
security threshold for that earlier larger-field example.

The bounded search in `scripts/four-error-search/search.cpp` found a
seven-parameter example whose supports motivated the two-block construction.
Its seed, stopping point, and output are saved in
`scripts/four-error-search/search-result.txt`. The proof above does not
rely on that decoder or on an exhaustive maximization. The auxiliary
command `python3 scripts/four-error-search/check.py` independently tests
the original punctured-code event for the discovered seven supports,
checks the ten displayed witnesses and their degree-seven codewords,
and checks all 17 parameters and all 2517 admissible supports for (4)
over F_17. That last finite check gives exactly {1,...,10} for this
pair over F_17. No claim of global sharpness or absence of additional
extension-field parameters is inferred from it.

## Mathlib

Coverage of the full two-block lower bound, model crossing, and supporting
interpolation facts in Mathlib: **not checked**. No matching theorem or
Lean verification is claimed. The full construction is proved by explicit
polynomials and the root bound; L007 supplies the special code's safe side.

The previously read ArkLib declarations
[`CoreDefinitions.IsMCA` and `CoreDefinitions.mcaError`](https://github.com/Verified-zkEVM/ArkLib/blob/e65197892890b8fd9b0dc05b8980273cf1d595cc/ArkLib/Data/CodingTheory/ProximityGap/ProximityGenerators.lean#L98)
support the frozen event definition. ArkLib is separate from Mathlib;
these declarations are not a match for this theorem and do not certify
its correspondence with the unread ABF26 definition.
