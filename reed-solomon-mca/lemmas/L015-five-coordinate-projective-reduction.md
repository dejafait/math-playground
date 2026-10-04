# L015 — Five-coordinate pencils reduce to rational point configurations

## Hypotheses

Let F=F_(97^20), H be the order-sixteen subgroup of F_97^*, and
C=RS[F,H,8]. Use L010's eight parity moments and pinned four-omission
event. For A subset H with |A|=5, let U_A be the moment image of
words supported on A. Fix a,b with sigma(a),sigma(b) in U_A, and
assume L010's D and every coordinate locator are nonzero polynomials.

Let J=H minus A. For each four-subset K of J define
\[
 f_K(X)=\prod_{y\in J\setminus K}(X-y),\qquad
 p_K=[(f_K(x))_{x\in A}]\in\mathbf P^4(\mathbb F_{97}).
\]
Let M(A) be the maximum number of these points on a projective line
defined over F_97. Its definition involves this finite configuration,
rather than arbitrary extension-field input weights.

## Conclusion

The 330 points p_K are distinct and have all coordinates nonzero, and
\[
 |B(a,b)|\le5+M(A).                                      \tag{1}
\]
If sigma(a),sigma(b) are dependent, the stronger bound |B(a,b)|<=1
holds. Multiplication by h in H preserves M(A), and the five-sets have
273 free multiplicative orbits.

In particular, if a nonpersistent sixteen-count pencil has two error
supports intersecting in three coordinates, their five-element union A
must satisfy M(A)>=11. The bound M(A)<=10 would suffice to exclude
sixteen for every pencil representable on that five-set.

No numerical value of M(A) is a premise of this lemma. Its accompanying
finite enumeration reports a maximum six; the unconditional mathematical
conclusion here is the reduction and necessary threshold (1).

## Proof

L010 proves ker(sigma)=C and minimum nonzero codeword weight nine.
Therefore sigma is injective on words supported on at most eight
coordinates. In particular its restriction to F^A is injective, so
sigma(a)+T sigma(b) has a unique polynomial representative
z(T)=u+T v supported on A. Its five coordinate weights are affine
polynomials over F. None is identically zero: otherwise the entire
pencil would be supported on at most four coordinates. A support of
size at most three forces D identically zero by the rank factorization;
a four-point support makes its coordinate locators identically zero by
the repeated-row determinant argument. Either violates the hypotheses.

Consider first independent sigma(a),sigma(b), equivalently independent
u,v. At most five finite parameters cancel one of the five nonzero
coordinate polynomials. Count those parameters separately, allowing
simultaneous cancellations. At every remaining parameter gamma,
z(gamma) has weight five. If a weight-w<=4 representative e exists,
z(gamma)-e is a codeword. It cannot be zero, since its two terms have
different weights. If w<=3, or if w=4 and supp(e) meets A, its support
has size at most eight. Minimum weight nine rules out both cases.
Thus w=4 and K=supp(e) is disjoint from A.

The nonzero codeword z(gamma)-e vanishes on J minus K, a set of seven
points. Its degree-less-than-eight polynomial is consequently
lambda*f_K, lambda in F^*: divide by the seven distinct linear factors
and use the degree bound. On A its values are z(gamma), giving
\[
 [z(\gamma)]=p_K.
\]
Conversely, if this identity holds, choose lambda so that
z(gamma)|_A=lambda*f_K|_A. The difference z(gamma)-lambda*f_K|_H
is supported on K and has four nonzero weights, since f_K is nonzero
at all four points of K. It has the required syndrome, and L010 gives
failure on the same agreement support under the stated hypotheses.

The map gamma -> [u+gamma v] is injective. Indeed, proportionality at
two parameters and independence of u,v imply that the scalar is one
and the parameters are equal. Thus each external point supplies at most
one finite parameter on the projective line span_F(u,v).

All coordinates of p_K lie in F_97 and are nonzero because A is
disjoint from its seven roots. To prove distinctness, suppose p_K=p_L.
For some lambda!=0, f_K-lambda*f_L vanishes on A and outside K union L; hence
its evaluation is a codeword supported on at most eight coordinates.
It is zero. Evaluation is injective for degree less than eight, so the
polynomials are proportional. Their simple zero sets J minus K and
J minus L agree, implying K=L.

An F-projective line containing two of these distinct rational points
is their F-span. It is the base extension of their F_97-span, so its
rational points in the configuration are counted by M(A). A line with
at most one configuration point also satisfies that bound, since
M(A)>=2. The external parameters therefore number at most M(A).
Adding the at-most-five cancellations proves (1).

If the two input syndromes are dependent, every nonzero syndrome of
the pencil is a scalar multiple of one fixed vector. A sparse
representative at any nonzero syndrome would represent the whole
polynomial pencil on that fixed support of size at most four, again
forcing D or a coordinate locator identically zero. Hence only a
zero-syndrome parameter can be bad, and there is at most one. A
constant nonzero syndrome has none; an identically zero syndrome is
excluded by D nonzero.

For h in H, replacing K,A,J by hK,hA,hJ gives
f_(hK)(h x)=h^7 f_K(x). This identifies the two configurations after
reordering coordinates, proving M(hA)=M(A). If hA=A, the action of h
on H has cycles of length ord(h), and A is a union of those cycles.
Thus ord(h) divides five and sixteen, forcing h=1. Every orbit has
sixteen members; binom(16,5)/16=273.

Finally, if two weight-four representatives at distinct parameters
have supports A_1,A_2 with intersection of size three, their union A
has size five. Solving the two moment equations at those parameters
shows sigma(a),sigma(b) in U_A. Equation (1) applies. For a count of
sixteen, it requires M(A)>=11, as claimed.

The exact bounded command
`python3 scripts/coefficient-feasibility/five_coordinate.py` enumerates
all 330 points for each of the 273 five-set orbits. It groups the 54285
point pairs by normalized Plucker coordinates; a line containing m
distinct points contributes exactly binom(m,2) pairs. It checks every
reported maximal line separately, verifies full orbit coverage, and
repeats one complete configuration using an independent Python pair
enumerator. Its recorded maximum is six (265 orbit representatives have
maximum five; eight have maximum six). This is finite configuration
evidence with explicit computational dependence, rather than a new
analytic theorem setting M(A). The field reduction proved above explains
its relevance to arbitrary F_(97^20) weights.

## Mathlib

Full five-coordinate projective reduction and threshold: **not checked**.
Supporting projective-line, Vandermonde, finite-field and minimum-distance
coverage: **not checked**. No full matching theorem, Lean verification or
library absence is claimed. The required point, field and orbit arguments
are written above.

The frozen event is supported by the previously read ArkLib
[CoreDefinitions.IsMCA and CoreDefinitions.mcaError](https://github.com/Verified-zkEVM/ArkLib/blob/e65197892890b8fd9b0dc05b8980273cf1d595cc/ArkLib/Data/CodingTheory/ProximityGap/ProximityGenerators.lean#L98).
ArkLib is separate from Mathlib; this is supporting definition coverage,
without a match for the reduction or the unread July ABF26 statement.
The reduction specializes the existing local moment/MDS tools, and
the step is classified as reproduction without a claim of originality.
