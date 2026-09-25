# L004 — Bad-support multiplicity gives a radius-dependent error bound

## Hypotheses

Let F be a finite field of order q, let I have cardinality n, and let the
evaluation points \(x_i\in F\), \(i\in I\), be pairwise distinct. Suppose
\(1\le k<n\), and set
\[
 C=\{(p(x_i))_{i\in I}:p\in F[X],\ \deg p<k\}.
\]
Use the error \(E_C\) from
[the pinned affine-line model](../foundations/02-pinned-affine-line-model.md).
For \(S\subseteq I\) and \(b\in F^I\), define
\[
 D_S(b)=\left|\{T\subseteq S:|T|=k+1,\ b|_T\notin C|_T\}\right|.
\]
For a radius \(\delta\in[0,1]\), put
\[
 m=\max\{k+1,\lceil n(1-\delta)\rceil\},\qquad
 N=\binom n{k+1},\qquad
 K_m=\left\lfloor\frac{N}{\binom{m-1}k}\right\rfloor.
\]
Here \(k+1\le m\le n\). Smoothness is not needed for the bound.

## Conclusion

If \(|S|=s\ge k+1\) and \(b|_S\notin C|_S\), then
\[
 D_S(b)\ge\binom{s-1}k.
\]
Equality holds exactly when b agrees with some degree-less-than-k polynomial
at all but one of the coordinates in S. In particular this multiplicity
factor is sharp.

For every fixed pair a,b, the number of bad challenges at radius delta is at
most
\[
 \min\left\{q,\left\lfloor\frac{D_I(b)}{\binom{m-1}k}\right\rfloor\right\}.
\]
Consequently
\[
 E_C(\delta)\le\min\{1,K_m/q\}.
\]
For \(0<\varepsilon\le1\), the inequality \(q\ge K_m/\varepsilon\)
is sufficient for safety at this radius. This is an upper bound, not a
sharp-error or largest-safe-radius assertion. Sharpness of the local
multiplicity does not imply sharpness of the uniform error bound.

For example, take \(n=256\), \(k=128\), and \(q=257^{32}\). A smooth
domain of size 256 exists over F, and on any such domain
\[
 E_C(\delta)\le2^{-128}\qquad(0\le\delta<90/256).
\]
In particular the grid radius \(89/256\) is safe. The sufficient test above
does not certify the next cell starting at \(90/256\); this is not a claim
that the next cell is unsafe. The previous all-radius sufficient threshold
\(q\ge2^{128}N\) is not met by this example.

All conclusions concern the frozen model; its correspondence with current
ABF26 and the challenge's field-size and endpoint qualifications remain open.

## Proof

L003's interpolation calculation gives two facts used here. Every restriction
on at most k coordinates is a code restriction, and for each (k+1)-set T,
\[
 h_T(z)=\sum_{i\in T}\frac{z_i}
 {\prod_{j\in T\setminus\{i\}}(x_i-x_j)}
 \quad\text{satisfies}\quad
 z|_T\in C|_T\ \Longleftrightarrow\ h_T(z)=0.
\]
Also, two degree-less-than-k polynomials agreeing at k distinct evaluation
points are equal, by the polynomial root bound.

First prove the multiplicity assertion by induction on s, with k fixed.
If s=k+1, the only possible T is S itself. Its restriction fails, so
\(D_S(b)=1=\binom{k}k\). Interpolating b on any k of these coordinates
gives a degree-less-than-k polynomial which necessarily disagrees at the
remaining coordinate. Thus the equality characterization also holds here.

Suppose now s>k+1. If some i in S has
\(b|_{S\setminus\{i\}}\in C|_{S\setminus\{i\}}\), choose a
degree-less-than-k polynomial p agreeing there. It must disagree at i,
since b is not a code restriction on S. Every (k+1)-subset avoiding i agrees
with p and hence does not contribute to \(D_S(b)\). Every (k+1)-subset
containing i does contribute: a polynomial agreeing on it would agree with
p on its other k points, hence equal p, contradicting the value at i.
There are exactly \(\binom{s-1}k\) such subsets. This proves equality in
this case, and shows directly that any one-coordinate alteration of a code
restriction attains the claimed multiplicity.

Otherwise every deletion \(S\setminus\{i\}\) still has a noncode
restriction. Induction applies to all s deletions and gives
\[
 \sum_{i\in S}D_{S\setminus\{i\}}(b)
 \ge s\binom{s-2}k.
\]
Every failing (k+1)-subset of S is contained in precisely s-k-1 of those
deletions, independently of its values. Thus the left side equals
\((s-k-1)D_S(b)\). Since s-k-1>0,
\[
 D_S(b)\ge\frac{s}{s-k-1}\binom{s-2}k
       =\frac{s}{s-1}\binom{s-1}k
       >\binom{s-1}k.
\]
This completes the induction and shows that equality requires the first
case, namely agreement with a polynomial at all but one coordinate.

Now fix a,b before choosing a challenge. For every \(\gamma\in F\), let
\[
 \mathcal T_\gamma=
 \{T\subseteq I:|T|=k+1,\ h_T(b)\ne0,
                    \ h_T(a)+\gamma h_T(b)=0\}.
\]
Every failing restriction of b on a (k+1)-set belongs to exactly one of
these families, since its unique possible value is
\(\gamma=-h_T(a)/h_T(b)\). Therefore
\[
 \mathcal T_\gamma\cap\mathcal T_\eta=\varnothing\quad(\gamma\ne\eta),
 \qquad \sum_{\gamma\in F}|\mathcal T_\gamma|=D_I(b)\le N.
\]
These families are small certificates, not necessarily admissible supports
at the original radius.

If gamma is bad at radius delta, take any witnessing support S of size s.
The combination \((a+\gamma b)|_S\) is a code restriction, whereas a or b
fails on this same S. Linearity forces b to fail: otherwise subtracting
\(\gamma b|_S\) would also make a a code restriction. Since restrictions
on at most k points never fail, s is at least k+1, and radius admissibility
also gives \(s\ge\lceil n(1-\delta)\rceil\). Hence s>=m.

The combination remains a code restriction on every T contained in S.
Consequently each of its \(D_S(b)\) failing b-restrictions belongs to
\(\mathcal T_\gamma\). The proved multiplicity and monotonicity of
binomial coefficients with fixed k give
\[
 |\mathcal T_\gamma|\ge D_S(b)\ge\binom{s-1}k\ge\binom{m-1}k.
\]
Summing only over the bad challenges and using the partition above proves
\[
 |\{\text{bad challenges}\}|\binom{m-1}k\le D_I(b)\le N.
\]
The count is an integer and at most q. This gives the asserted pair-specific
bound, uniformly for all pairs, including b=0 when \(D_I(b)=0\). Dividing
by q and maximizing over a,b proves the error bound. Neither the support nor
the agreeing polynomial was required to be fixed across challenges.

When m=k+1 the denominator is one, recovering L003's upper bound. For
m>k+1 it is strictly larger than one, so the certificate count improves.
Neither condition asserts that the new count can be attained simultaneously
for enough challenges. In particular, failing the sufficient field-size test
does not establish an unsafe radius.

For the numerical example, 257 is prime and the finite-field existence
theorem gives a field of order \(257^{32}\). Since
\(257\equiv1\pmod{256}\), its multiplicative group has order divisible
by 256. Cyclicity gives a subgroup H of order 256, which is a smooth domain
in the pinned model. Its dimension-128 RS code has rate 1/2.
With \(N=\binom{256}{129}\), exact integer arithmetic gives
\[
 K_{167}=\left\lfloor\frac{N}{\binom{166}{128}}\right\rfloor
 =128219789898315536563797797674837788012<2^{127},
\]
\[
 K_{167}2^{128}\le257^{32}<K_{166}2^{128},\qquad
 2^{256}<257^{32}<2^{257}<2^{379}<N2^{128}.
\]
If \(\delta<90/256\), then \(256(1-\delta)>166\), so m>=167.
The denominator grows with m, and \(K_m\le K_{167}\). The sufficient
condition therefore proves the stated safety throughout that real interval.
At \(\delta=90/256\), m=166 and the sufficient inequality fails.
The strict endpoint and the absence of an unsafety conclusion are essential.

The auxiliary command `python3 scripts/certificate-multiplicity/check.py`
checks the general formula against direct polynomial membership in small
prime fields, including every support and challenge for the chosen parameter
sets. It also checks one-coordinate equality examples and the exact integer
comparisons. The induction and partition argument prove the general result;
these finite checks do not resolve the challenge.

## Mathlib

Coverage of the full statement and of supporting interpolation and finite
counting results in Mathlib: **not checked**. No matching library theorem or
Lean verification is claimed. The new multiplicity argument is proved above;
the standard finite-field existence and cyclicity inputs are stated in the
model foundation.

The previously checked ArkLib declarations
[`CoreDefinitions.IsMCA` and `CoreDefinitions.mcaError`](https://github.com/Verified-zkEVM/ArkLib/blob/e65197892890b8fd9b0dc05b8980273cf1d595cc/ArkLib/Data/CodingTheory/ProximityGap/ProximityGenerators.lean#L98)
support the frozen event definition. ArkLib is a separate library, and these
definitions are not a match for the multiplicity theorem or its error bound.
