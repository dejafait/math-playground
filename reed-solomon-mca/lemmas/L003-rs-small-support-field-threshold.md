# L003 — Small RS supports control the all-radius field threshold

## Hypotheses

Let F be a finite field of order q, let I have cardinality n, and let
\(x_i\in F\), \(i\in I\), be pairwise distinct. Suppose \(1\le k<n\)
and let
\[
 C=\{(p(x_i))_{i\in I}:p\in F[X],\ \deg p<k\}.
\]
Use the exact support-event error \(E_C\) from
[the pinned affine-line model](../foundations/02-pinned-affine-line-model.md).
Put \(N=\binom n{k+1}\), and let \(0<\varepsilon\le1\).
No smoothness assumption is needed for the bound.

## Conclusion

Every bad challenge has a certificate on k+1 coordinates: the same affine
combination is a code restriction there, and the direction is not. The smaller
support need not satisfy the original radius's size requirement. Nevertheless,
for every \(\delta\in[0,1]\),
\[
 E_C(\delta)\le\min\{1,N/q\}.
\]
Thus \(q\ge N/\varepsilon\) makes every radius safe and gives largest safe
real radius 1 for this frozen model.

For an exact description, for every \(T\subseteq I\) of size k+1 define
\[
 h_T(z)=\sum_{i\in T}\frac{z_i}
 {\prod_{j\in T\setminus\{i\}}(x_i-x_j)},\qquad
 B(a,b)=\{-h_T(a)/h_T(b):|T|=k+1,\ h_T(b)\ne0\}.
\]
For each fixed pair (a,b), its bad-challenge set is contained in B(a,b) at
every radius and equals B(a,b) when \(\delta\ge1-(k+1)/n\).

If additionally \(q>\binom N2\), the count can be attained:
\[
 E_C(\delta)=N/q\qquad\bigl(1-(k+1)/n\le\delta\le1\bigr).
\]
Under this extra hypothesis, all radii are safe if and only if
\(q\ge N/\varepsilon\). This exactness condition can be stronger than the
sufficient safety threshold; no converse at smaller q is asserted.

At length 16 and the four listed rates, the corresponding values of N are
11440, 4368, 560, and 120, respectively. A smooth common domain exists over
\(F_{5^{64}}\), and all four codes are safe at every radius for
\(\varepsilon=2^{-128}\). These are model-only statements. They do not
identify the unread ABF26 event or determine its sharp radius at a given q.

## Proof

First recall the interpolation fact with its explicit formula. On distinct
points indexed by a set T of size k+1, the polynomial
\[
 f_{T,z}(X)=\sum_{i\in T}z_i
 \frac{\prod_{j\in T\setminus\{i\}}(X-x_j)}
 {\prod_{j\in T\setminus\{i\}}(x_i-x_j)}
\]
has degree at most k and value z_i at x_i. All denominators are nonzero.
It is unique: the difference of two such interpolants would have degree at
most k and k+1 distinct roots, so the polynomial root bound makes it zero.
Its coefficient of \(X^k\) is h_T(z). It follows that
\[
 z|_T\in C|_T\quad\Longleftrightarrow\quad h_T(z)=0.
\]
Indeed, vanishing of that coefficient gives a polynomial of degree less than
k; conversely, any such agreeing polynomial must equal the unique interpolant.
The same formula on any nonempty set of size at most k interpolates arbitrary
values with degree less than k. On the empty set the zero polynomial suffices.

Fix a, b, a bad challenge gamma, and a witnessing support S. The combination
\((a+\gamma b)|_S\) is a code restriction. If \(b|_S\) were a code
restriction, linearity would also make \(a|_S\) one, contradicting failure
on this same S. Thus \(b|_S\notin C|_S\). In particular |S| is at least
k+1, since smaller restrictions are fully interpolable.

Choose any k-element subset A of S, and interpolate b on A by its unique
polynomial p of degree less than k. Because b is not a code restriction on S,
there is j in S outside A with \(b_j\ne p(x_j)\). On
\(T=A\cup\{j\}\), b cannot be a code restriction: an agreeing polynomial
would agree with p at the k points of A and hence equal p by the root bound,
contradicting the value at j. The original combination remains a code
restriction after restricting from S to T. Therefore
\[
 h_T(b)\ne0,\qquad h_T(a)+\gamma h_T(b)=0,
 \qquad \gamma=-h_T(a)/h_T(b).
\]
This proves containment of the bad-challenge set in B(a,b). It was proved
after an arbitrary challenge-dependent S was chosen, without requiring a
support fixed in advance or claiming that T meets the same size threshold.

There are N possible T, and each supplies at most one challenge. Consequently
\(|B(a,b)|\le\min\{q,N\}\). Division by q and maximization over all a,b
prove the uniform bound. This includes b=0, when no T contributes and no
challenge can be bad. If \(q\ge N/\varepsilon\), the bound proves safety
on all of [0,1], including its largest element 1.

Conversely, any gamma in B(a,b) has a T with h_T(b) nonzero and
\(h_T(a+\gamma b)=0\). The kernel characterization proves the two required
membership conditions on T. When \(\delta\ge1-(k+1)/n\), its cardinality
k+1 is at least \(n(1-\delta)\), so T is an admissible bad support. This
proves the exact terminal-radius event. No converse for smaller radii follows.

For attainment, take \(b_i=x_i^k\). Its degree-at-most-k interpolant on
every T is \(X^k\), so h_T(b)=1. The linear forms h_T and h_U on \(F^I\)
are distinct whenever T and U are distinct: choose i in T outside U; h_T has
a nonzero coefficient at coordinate i while h_U has coefficient zero there.
Each equality \(h_T(a)=h_U(a)\) consequently defines a hyperplane with
exactly \(q^{n-1}\) elements. This cardinality follows by solving for any
coordinate with nonzero coefficient after choosing all other coordinates.
There are \(\binom N2\) unordered pairs of supports. When
\(q>\binom N2\), the union of these hyperplanes has size at most
\(\binom N2 q^{n-1}<q^n\). Choose a outside the union. (If N=1, the union
is empty.) The N values \(-h_T(a)\) are then distinct, so B(a,b) has size N.
This single pair attains error N/q at every terminal radius. The upper bound
proves equality. Its value at radius 1 also proves the asserted necessity
of \(q\ge N/\varepsilon\) for all-radius safety under the extra hypothesis.

For the smooth example, finite-field existence and cyclicity of the
multiplicative group give a field of order \(5^{64}\) and a subgroup H of
order 16, since \(5^4\equiv1\pmod{16}\) and 4 divides 64. The codes on H
with k equal to 8, 4, 2, and 1 have the listed rates. Direct binomial
calculation gives the four N values above, with maximum 11440. Finally,
\[
 5^7>2^{16},\qquad
 5^{64}=5^8(5^7)^8>390625\cdot2^{128}>11440\cdot2^{128}.
\]
Hence all four codes are safe at every radius at the prescribed budget.

The achieved bound requires \(q\ge2^{128}\binom n{k+1}\) for this
all-radius conclusion. It can be a very large sufficient bound: for n=256
and k=128, its right side lies strictly between \(2^{379}\) and
\(2^{380}\). It supplies neither an optimal radius below the terminal
range nor safety at that budget when its field-size inequality fails.
Moreover, the attainment proof's separate condition \(q>\binom N2\)
must not be dropped when inferring a necessary threshold. The actual given
code and the unresolved ABF26 qualifications still matter.

The auxiliary script `python3 scripts/small-support/check.py` checks direct
punctured-code events against these certificates in small prime fields, an
explicit distinct-root example, and the exact integer comparisons. The
general claims follow from interpolation and counting above, not enumeration.

## Mathlib

Coverage of the full result and of supporting interpolation/counting theorems
in Mathlib: **not checked**. No matching formal theorem or Lean verification
is claimed. The interpolation and hyperplane-counting arguments are proved
above. The finite-field existence and cyclicity facts are the standard inputs
stated in the model foundation.

The separate ArkLib declarations
[`CoreDefinitions.IsMCA` and `CoreDefinitions.mcaError`](https://github.com/Verified-zkEVM/ArkLib/blob/e65197892890b8fd9b0dc05b8980273cf1d595cc/ArkLib/Data/CodingTheory/ProximityGap/ProximityGenerators.lean#L98)
are the previously checked sources for the event definitions, not a match for
this bound or a certification of its correspondence with current ABF26.
