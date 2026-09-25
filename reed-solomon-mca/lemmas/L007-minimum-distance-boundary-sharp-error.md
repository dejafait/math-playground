# L007 — Sparse-error dichotomy at the minimum-distance boundary

## Hypotheses

Let F be a finite field of order q, let n pairwise distinct evaluation
points x_i lie in F, and let C be their Reed–Solomon code of dimension k.
Assume that r,k are positive integers satisfying
\[
 n-k+1=3r,\qquad r/n\le\delta<(r+1)/n.
\]
Use E_C from
[the pinned affine-line model](../foundations/02-pinned-affine-line-model.md).
The special example below takes F=F_{17^s}, s>=1, the evaluation domain
F_17^* inside F, n=16, k=8, and r=3.

## Conclusion

Writing M=max{r+1,floor(n/r)}, one has
\[
 \frac{r+1}{q}\le E_C(\delta)\le\min\{1,M/q\}.                 \tag{1}
\]
The upper bound comes from a dichotomy: for any input pair, either all
chosen sparse errors have one affine lift, giving at most r+1 bad
parameters, or all their supports are disjoint sets of size r, giving
at most floor(n/r). Consequently, if floor(n/r)<=r+1, the error is
exactly (r+1)/q even at this distance boundary. In particular, n=256,
k=128, r=43 gives the exact error 44/q on [43/256,44/256).

For the stated smooth length-16 example, the second branch is attained:
\[
 E_C(\delta)=5/q\quad\text{for}\quad3/16\le\delta<1/4.       \tag{2}
\]
Thus extending L006's formula unconditionally to n-k+1=3r is false:
it would give 4/q in this example. Equation (2) is safe at the prescribed
budget precisely when q>=5*2^128. In this field tower the least exponent
meeting that condition is s=32. This is a cell result for the frozen event,
not the maximal safe radius or a resolution of the ABF26 correspondence.

## Proof

Every nonzero codeword has weight at least n-k+1=3r: a nonzero polynomial
of degree less than k has at most k-1 roots, by successive division by
its distinct linear factors. The radius hypothesis means that the allowed
supports are exactly all S with |S|>=n-r.

Fix input words a,b and let Gamma be their bad-parameter set. For each
gamma in Gamma choose a witnessing support S_gamma and codeword c_gamma,
and put e_gamma=a+gamma*b-c_gamma. Its weight is at most r. On a support
where the combination is a code restriction, the original input-failure
disjunction is equivalent to b not being a code restriction: if b were
one, subtraction would make a one too. No common support or codeword is
assumed. If Gamma has at most one element there is nothing to prove.

Choose distinct gamma_0,gamma_1 in Gamma and interpolate their errors as
\[
 e(t)=u+tv,\quad
 v=\frac{e_{\gamma_1}-e_{\gamma_0}}{\gamma_1-\gamma_0},\quad
 u=e_{\gamma_0}-\gamma_0v.
\]
Then a-u and b-v belong to C. For every gamma in Gamma,
e_gamma-e(gamma) belongs to C and has support in the union of the
three error supports, whose total size is at most 3r.

First suppose e_gamma=e(gamma) for every gamma in Gamma. Let J be the
set of coordinates where (u_i,v_i) is not (0,0), and write t=|J|<=2r.
Every coordinate affine polynomial u_i+Xv_i with i in J has at most
one root. If t>r, each bad parameter must be a root of at least t-r
coordinates, so
\[
 |\Gamma|(t-r)\le t,\qquad
 |\Gamma|\le\lfloor t/(t-r)\rfloor\le r+1.
\]
If t<=r, use the failure on the witnessing support. Because b-v is a
codeword, v|_{S_gamma} is not a code restriction and in particular is
nonzero. Some i in S_gamma has v_i!=0, while e_gamma vanishes there.
Thus gamma is a root of one of at most t nonconstant coordinate affine
polynomials, and |Gamma|<=t<=r. This handles sparse lines on which
closeness alone holds at every parameter.

Otherwise choose gamma_2 whose discrepancy is nonzero. Its weight must
be at least 3r, so the three error supports A_0,A_1,A_2 are disjoint
sets of size exactly r. More generally, for any three distinct parameters
the difference between one error and the affine interpolation of the
other two is a codeword. If it is nonzero, the same argument forces
three disjoint supports of size r.

Take any further gamma. For the triple gamma_0,gamma_1,gamma, a zero
discrepancy would express e_gamma as a combination of e_gamma_0 and
e_gamma_1 with both coefficients nonzero. Their disjoint full supports
would give weight 2r, contradicting weight at most r. The discrepancy
is therefore nonzero, forcing A_gamma to have size r and be disjoint
from A_0 and A_1. Applying the same reasoning to gamma_0,gamma_2,gamma
forces disjointness from A_2. For any two further parameters gamma,eta,
the triple gamma_0,gamma,eta likewise forces A_gamma and A_eta to be
disjoint. Hence all the error supports are pairwise disjoint sets of
size r, and |Gamma|*r<=n. This proves the upper bound in (1).

For the lower bound, q>=n>=3r>=r+1 permits r+1 distinct coordinates
i_0,...,i_r and r+1 distinct field elements alpha_0,...,alpha_r.
Put a_{i_j}=-alpha_j and b_{i_j}=1, with both words zero elsewhere.
At gamma=alpha_j the combination is zero on
S_j=I minus {i_h:h!=j}, which has size n-r. If a codeword agreed
with b on S_j, it would vanish outside these r+1 coordinates and be
nonzero at i_j. Its weight would be at most r+1<3r, a contradiction.
These r+1 parameters are bad on their respective supports. This proves
(1), and yields the asserted equality whenever floor(n/r)<=r+1.
For n=256,r=43, floor(256/43)=5<44, as claimed.

It remains to attain five in the smooth example. All the following
coefficients lie in the prime subfield F_17 and hence in every extension.
Set
\[
 U(X)=X^{16}-1,\quad B(X)=X^2-X,\quad
 P_t(X)=X^3-tX^2+(t-3)X+1.
\]
For t in T={0,3,6,10,14}, the following factorizations hold in F_17[X]:

| t | Roots A_t of P_t |
|---|---|
| 0 | 7, 13, 14 |
| 3 | 4, 5, 11 |
| 6 | 3, 8, 12 |
| 10 | 2, 9, 16 |
| 14 | 6, 10, 15 |

These identities follow by multiplying the three linear factors in each
row: the sums of roots are t, sums of pairwise products are t-3, and
products are -1 modulo 17. The five disjoint triples cover F_17^*
minus {1}. In particular B is nonzero on every triple, and each P_t
has simple roots. Define words f_t supported on A_t by
\[
 f_t(x)=\frac{U'(x)}{P_t'(x)B(x)^2}\quad(x\in A_t),\qquad
 f_t(x)=0\quad(x\notin A_t).
\]
Every displayed nonzero-coordinate value is nonzero: U has sixteen
simple roots and all denominators are nonzero. Thus f_t has weight three.

For three distinct s,t,u in T, the polynomial
\[
 H_{s,t,u}(X)=\frac{U(X)}{P_s(X)P_t(X)P_u(X)}
\]
exists and has degree seven. At a root x of P_s, cancellation of X-x
gives
\[
 H_{s,t,u}(x)
 =\frac{U'(x)}{P_s'(x)P_t(x)P_u(x)}
 =\frac{f_s(x)}{(s-t)(s-u)},
\]
since P_t(x)=(s-t)B(x) and P_u(x)=(s-u)B(x). The corresponding
identities hold on A_t,A_u, and H vanishes at every other evaluation
point. Its evaluation word is therefore
\[
 \frac{f_s}{(s-t)(s-u)}+
 \frac{f_t}{(t-s)(t-u)}+
 \frac{f_u}{(u-s)(u-t)}\in C.                            \tag{3}
\]
Define a=f_0 and b=(f_3-f_0)/3. For t=0,3 the word a+tb equals f_t.
For each other t in T, multiplying (3) for 0,3,t by t(t-3) shows
\[
 c_t:=a+tb-f_t=-t(t-3)\operatorname{ev}(H_{0,3,t})\in C.
\]
Use c_0=c_3=0. Thus a+tb agrees with c_t on S_t=F_17^* minus A_t,
of size thirteen, at each of these five distinct parameters.

The same-support failure also holds. Suppose b|_{S_t} were a code
restriction, and take d in C agreeing with b there. Then g=b-d is
supported on A_t. For any other s in T,
\[
 a+sb-(c_t+(s-t)d)=f_t+(s-t)g
\]
is supported on A_t, whereas a+sb-c_s=f_s is supported on A_s.
Their difference is a codeword of weight at most six, hence is zero
by distance nine. This would put the nonzero word f_s on both of the
disjoint sets A_t,A_s, a contradiction. Therefore b fails on every S_t.
All five parameters are bad in the original event. The upper bound (1)
is five for n=16,r=3, proving (2).

The domain F_17^* is a multiplicative subgroup of order 16=2^4 in every
extension field, so it is smooth in the frozen definition and has the
listed rate 1/2. For reproducibility, coordinates ordered as 1,...,16 give
\[
 a=(0,0,0,0,0,0,6,0,0,0,0,0,7,8,0,0),
\]
\[
 b=(0,0,0,15,14,0,15,0,0,0,9,0,9,3,0,0).
\]
The algebra above is valid in every F_{17^s}; it does not infer a field
threshold from an example over only F_17. Exact integer comparison gives
17^31<5*2^128<=17^32<7*2^128. L004's sufficient count on this cell
is floor(binomial(16,9)/binomial(12,8))=23, so it does not certify this
cell at q=17^32, while (2) does. The length-256 boundary equality adds
one exact cell to L006, ending at the excluded endpoint 44/256; it
still does not extend L004's sufficient interval delta<90/256 there.
At q=17^32 the actual budget permits at most six bad parameters, so a
seven-parameter construction on a later cell would establish unsafety.

`python3 scripts/distance-boundary/check.py` checks the factorizations,
codewords, failure on each claimed support, all seventeen parameters
and all 697 admissible supports for this explicit pair, and the integer
comparisons. It is not an exhaustive maximization over pairs; the uniform
upper bound and extension-field claim are proved above.

## Mathlib

Coverage of the full dichotomy, the sharp example, and supporting sparse
error results in Mathlib: **not checked**. No matching theorem or Lean
verification is claimed. The proof uses the polynomial root bound,
finite counting, explicit polynomial identities, and linearity.

The previously read ArkLib declarations
[`CoreDefinitions.IsMCA` and `CoreDefinitions.mcaError`](https://github.com/Verified-zkEVM/ArkLib/blob/e65197892890b8fd9b0dc05b8980273cf1d595cc/ArkLib/Data/CodingTheory/ProximityGap/ProximityGenerators.lean#L98)
support the frozen event definition. ArkLib is separate from Mathlib;
these declarations are not a match for this theorem and do not certify
its correspondence with the unread ABF26 definition.
