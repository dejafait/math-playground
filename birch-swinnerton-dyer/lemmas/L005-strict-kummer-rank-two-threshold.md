# L005 — A nonzero strict Kummer class forces rational rank at least two

## Hypotheses

Let E/Q be an elliptic curve with good reduction at a prime p >= 5.
Put W = E(Q) tensor_Z Q_p and r = rank E(Q). Write

\[
S=\left(\varprojlim_n\operatorname{Sel}_{p^n}(E/\mathbf Q)\right)
       \otimes_{\mathbf Z_p}\mathbf Q_p,\qquad
V_{\mathrm{loc}}=
\left(\varprojlim_n E(\mathbf Q_p)/p^n E(\mathbf Q_p)\right)
       \otimes_{\mathbf Z_p}\mathbf Q_p.
\]

The Selmer transitions are induced by multiplication by p on torsion
coefficients; on point quotients they are reduction. Let j: W -> S be
the rational Kummer injection and lambda_p: S -> V_loc be localization
through the local Kummer images. A *strict* class here means a class in
ker(lambda_p). This definition concerns one fixed prime p.

For the rank certificate conclusion only, also assume E is non-CM,
p is ordinary, and the coefficient a_2 of the primitive ordinary
L_p(E,T) in L004's normalization is rigorously nonzero.

## Conclusion

1. The space V_loc has dimension one, and

   \[
   \dim_{\mathbf Q_p}\bigl(j(W)\cap\ker\lambda_p\bigr)
     =\begin{cases}0&r=0,\\r-1&r\ge1.\end{cases}
   \tag{1}
   \]

   Consequently, one nonzero strict class **in j(W)** implies r >= 2.
   Two independent constructed classes are unnecessary for this lower
   bound. The conclusion concerns existence of rational points, not
   an algorithm producing their coordinates.

2. Under the additional coefficient hypotheses, that one strict Kummer
   class implies r = ord_T f_X = ord_T L_p = 2. Both defects in L004
   vanish, p-primary Sha is finite, and the cyclotomic height is
   nondegenerate. To conclude the Clay assertion for this E still
   requires a separate proof that m(E) = 2.

3. If r = 2 and P,Q are a rational basis modulo torsion, set

   \[
   R_p=\log_p(P)Q-\log_p(Q)P\in W.
   \tag{2}
   \]

   Then R_p is nonzero and spans the strict Kummer line after applying
   j. Changing P,Q rescales R_p by the determinant of the basis change.
   Formula (2) presupposes the points; it does not construct them.

There is an exact sequence

\[
0\longrightarrow W\xrightarrow{j}S
\xrightarrow{q}V_p\Sha(E/\mathbf Q)\longrightarrow0,
\qquad V_p\Sha=(\varprojlim_n\Sha[p^n])\otimes\mathbf Q_p,
\tag{3}
\]

where the Sha transitions are multiplication by p. For a proposed
Selmer class, (1) requires q(kappa) = 0 in addition to nonvanishing and
strictness. No such membership theorem for generalised Kato classes is
proved here, and finiteness of Sha is not an assumption of (1).

## Proof

**Local logarithm and its kernel.** Use an integral minimal equation
at p and a Neron invariant differential. The reduction kernel
U = E_1(Q_p) is an open subgroup of finite index in E(Q_p), identified
with the elliptic formal group on p Z_p. The inputs are
[Milne, *Elliptic Curves*, second edition, Theorem II.4.1 and Aside II.4.4,
printed pages 62--65](https://www.jmilne.org/math/Books/EC2.pdf#page=67).
These are supporting local structure statements; the deductions below
are not asserted to be a theorem quoted there.

In a formal parameter t the normalized invariant differential is
(1 + sum_{k>=1} b_k t^k)dt with b_k in Z_p. Its integral is the formal
logarithm

\[
L(t)=t+\sum_{k\ge2}\frac{b_{k-1}}{k}t^k.
\]

It converges on p Z_p. For k >= 2, k-1-v_p(k) >= 1 since p >= 5.
Consequently, for t,u in p Z_p the k-th term in
L(t)-L(u)-(t-u) has valuation at least v_p(t-u)+1. Thus L(t)-t is
a strict contraction on p Z_p. Solving t = y-(L(t)-t) proves that L
is a bijection p Z_p -> p Z_p, and the same estimate proves injectivity.
The identity L(F(t,u)) = L(t)+L(u) follows by differentiating using
invariance of the differential and evaluating at the identity.
Therefore log_p: U -> p Z_p is a group isomorphism.

Let d = [E(Q_p):U]. Extend the logarithm by
log_p(A) = d^(-1) log_p([d]A). This is a homomorphism agreeing with
the preceding one on U. If log_p(A) = 0, injectivity on U gives
[d]A = 0. Conversely torsion is killed by any homomorphism to Q_p.
Hence its kernel on E(Q_p) is exactly the torsion subgroup.

The inclusion U -> E(Q_p) and multiplication by d in the reverse
direction have composites [d]. They induce maps on p-adic completions
whose composites are still [d]. After tensoring with Q_p these maps
are isomorphisms, since d is invertible in Q_p. Thus V_loc is identified
by the logarithm with Q_p. This uses the completed local group, not
the generally different algebraic tensor E(Q_p) tensor_Z Q_p.

**The Kummer subspace.** Take inverse limits in the finite Kummer exact
sequences from [the standard inputs](../foundations/02-standard-inputs.md).
Their left terms E(Q)/p^n E(Q) have surjective transition maps. Hence
the inverse-limit sequence is exact: a compatible Sha system can be
lifted recursively, correcting each new Selmer lift by an element of
the next point quotient to agree with the preceding lift. Mordell's
theorem identifies the left inverse limit, after tensoring with Q_p,
with W. Since Q_p is flat over Z_p, (3) follows. This also proves that
j is injective. The unique finite-level local Kummer preimages define
lambda_p compatibly, so its restriction to j(W) is ordinary localization
of points followed by completion.

**Dimension threshold.** If r = 0, W = 0. If r >= 1, choose a
nontorsion rational point P. Its image in E(Q_p) remains nontorsion:
an equality [n]P = 0 after extending Q to Q_p is already the same
equality over Q. The local kernel calculation gives log_p(P) != 0.
Therefore the linear map ell_p = log_p composed with lambda_p composed
with j from W to Q_p has rank exactly one. Rank-nullity proves (1).
A nonzero strict vector in j(W) then excludes both r = 0 and r = 1.

Under the additional coefficient hypotheses, Mordell's theorem now
supplies two independent rational points. Apply L004 with k = n = 2
to obtain all conclusions in part 2. Kummer membership is used before
L004 gives finite p-primary Sha, so finiteness is not used circularly
to identify the starting class with a point.

**The single line.** For r = 2, linearity gives ell_p(R_p) = 0.
As log_p(P) != 0 and P,Q are linearly independent in W, the coefficient
of Q in (2) proves R_p != 0. The kernel has dimension one, so R_p
spans it. For P' = aP+bQ and Q' = cP+dQ, expansion gives
log_p(P')Q'-log_p(Q')P' = (ad-bc)R_p. Thus different basis choices
cannot yield two independent vectors by this construction.

Finally, (3) identifies the exact additional requirement on a Selmer
class as q(kappa) = 0. Strictness alone is a local condition and does
not establish that equality. Even at the level of vector spaces,
(3) together with a nonzero strict class allows W = 0, S = Q_p^2,
V_p Sha = Q_p^2, q the identity, and lambda_p(x,y) = x. This is only
a model of the specified data, not an elliptic curve or a BSD
counterexample. It explains why the proven twisted Selmer conclusions
in the [source audit](../foundations/06-generalised-kato-scope.md) are
insufficient for the rational lower bound without more arithmetic.

## Mathlib

Full statement including the arithmetic and local logarithm inputs:
**not checked**. Supporting rank-nullity, inverse-limit exactness, and
formal-group logarithm coverage: **not checked**. The direct Milne
reference supplies supporting mathematical results, not a Mathlib
match for the full statement. No unproved generalised Kato conjecture
is used in this proof.
