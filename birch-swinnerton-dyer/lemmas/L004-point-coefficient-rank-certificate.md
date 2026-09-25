# L004 — Independent points and a p-adic coefficient certify rank

## Hypotheses

Let E/Q be a non-CM elliptic curve and p >= 5 a prime of good ordinary
reduction. Use the classical cyclotomic Selmer dual X, Lambda, A =
Lambda_(T), M = X tensor_Lambda A, and characteristic generator f_X from
[the control foundations](../foundations/03-cyclotomic-control.md).
Use the primitive ordinary p-adic L-function and Kato divisibility from
[the divisibility foundations](../foundations/05-kato-divisibility.md).
Write

\[
\begin{gathered}
L_p(E,T)=\sum_{j\ge0}a_jT^j,\qquad
r=\operatorname{rank}E(\mathbf Q),\qquad h=\operatorname{ord}_T f_X,\\
D=\Sha(E/\mathbf Q)[p^\infty],\qquad
s=\operatorname{corank}_{\mathbf Z_p}D,\qquad
\delta=\operatorname{length}_A(TM).
\end{gathered}
\]

Let k,n be nonnegative integers. Suppose P_1,...,P_k in E(Q) have
linearly independent images in E(Q) tensor_Z Q, and suppose a_n != 0
is proved. The point condition requires independence, not merely
distinct points or individually infinite orders. No full basis or
saturation of their span is required. For k = 0 this condition is empty.

A sufficient finite-precision coefficient certificate consists of an
exact rational b, an integer N, and a proved bound

\[
v_p(a_n-b)\ge N>v_p(b),\qquad v_p(p)=1.
\tag{1}
\]

Finite p-primary Sha, a nonzero p-adic regulator, and any BSD conjecture
are not hypotheses.

## Conclusion

Put ell = ord_T L_p(E,T). Then ell is finite and

\[
k\le r\le r+s+\delta=h\le\ell\le n,
\qquad (r-k)+s+\delta\le n-k.
\tag{2}
\]

In particular, when k = n,

\[
\boxed{r=h=\ell=n,\qquad s=\delta=0.}
\tag{3}
\]

In this matching case D is finite, TM = 0,
M is isomorphic to (A/(T))^n, and the natural map
M[T] -> M/TM is an isomorphism. The canonical cyclotomic p-adic height
is nondegenerate as well, using L003's converse in its non-CM scope.
All coefficients a_j with j < n vanish exactly.

These are arithmetic and p-adic conclusions. They prove the local Clay
rank assertion for this E only if a separate proof also supplies n =
m(E). No bound on the order of the finite group D, finiteness of the
whole Sha, or refined leading-coefficient formula is asserted.

## Proof

**The two certificates give opposite bounds.** Mordell's theorem
identifies E(Q) tensor Q with a Q-vector space of dimension r. The
independent point images therefore imply k <= r. By definition, the
nonzero coefficient a_n implies that L_p is nonzero and that its least
nonzero coefficient occurs at an index ell <= n. There is no need to
assume any lower coefficient vanishes.

Kato's checked divisibility gives L_p = f_X g with g in Lambda[1/p].
Since L_p is nonzero and f_X is nonzero, g is nonzero. As power series
over Q_p, write f_X = T^h u and g = T^t v, where t >= 0 and u(0),v(0)
are nonzero. The coefficient of T^(h+t) in their product is u(0)v(0),
which is nonzero because Q_p is a field; all lower coefficients vanish.
Consequently ell = h + t >= h. This also explains why divisibility up
to a power of p is sufficient for this order comparison.

**Keep the defects.** L002 gives h = r+s+delta with s,delta >= 0 for
this classical Selmer dual. Combining it with the preceding bounds
proves the chain in (2), and subtracting k from h <= n proves its last
inequality. If k = n, each term in the chain lies between the same
endpoints. Hence all are n and the two nonnegative defects vanish.

**Consequences of equality.** Since h = r, L003(1) gives finite D and
the asserted isomorphism M[T] -> M/TM. L002 gives TM = 0 and its cyclic
decomposition now consists of h = n copies of A/(T). With D finite,
L003(3) applies because E is non-CM and yields nondegenerate canonical
cyclotomic height. None of these conclusions was used to establish
the bounds. The equality ell = n forces a_j = 0 for j < n by the
definition of order. This includes n = 0 with empty points and zero M.

**Why the finite-precision condition suffices.** Under (1), b is nonzero
and the error a_n-b has strictly larger valuation than b. The strong
triangle inequality with unequal valuations gives
v_p(a_n) = v_p(b) < infinity, proving a_n != 0. Equivalently, divide
by b: (a_n-b)/b lies in p Z_p, so a_n/b is a unit. If the proved
enclosure contains zero, this argument gives no certificate. In
particular, an output O(p^N) never proves exact vanishing by itself.

**Threshold and scope.** The achieved bound from k points and degree n
is the actual interval [k,n] together with the defect bound in (2).
Only the matching threshold k = n eliminates both defects by this
argument. The independent-point input is absent from the older abstract
countermodels; their failures therefore do not conflict with (3).
Normalizing L_p by a nonzero constant, even a power of p, does not
affect the argument. A change of generator gives an invertible formal
coordinate at T = 0 and preserves order, but a coefficient certificate
must use its stated coordinate and normalization.

The missing uniform input is not repaired by this conditional lemma:
one must produce the points and coefficient certificate for suitable
E,p,n and independently connect n to the complex analytic order. This
is a standard matching-bounds argument made precise for the recorded
defects, not a candidate resolution of BSD.

## Mathlib

Full statement, including its arithmetic hypotheses: **not checked**.
Supporting power-series order, finite-dimensional independence, and
nonarchimedean valuation facts: **not checked**. No library absence or
full match is claimed. Named arithmetic theorems and direct links are
retained in the foundations; all deductions and the finite-precision
test are proved above.
