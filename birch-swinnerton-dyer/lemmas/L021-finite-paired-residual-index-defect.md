# L021 — Finite paired contribution to the residual Kurihara index

## Hypotheses

Let E/Q be non-CM and let p >= 5 be good ordinary. Assume that E[p]
is surjective, p does not divide #E(F_p), the Manin constant or any
Tamagawa factor, and E(Q_p)[p] = 0. Write
S = Sel(Q,E[p^infinity]) for the classical Selmer group and grant
corank_Z_p S = 2. Grant also residual Kurihara-family nonvanishing in
Sakamoto's N_(1,0), the square-free products of primes ell of good
reduction with ell = 1 mod p and E(F_ell)[p] cyclic of order p.
A residual index n is divisor-minimal if its Kurihara scalar is nonzero
and every proper divisor's scalar is zero.

Use the compatible Neron-period and discrete-logarithm normalizations
in the sources below. Changing primitive roots only multiplies the
scalars by units, so does not change vanishing. In particular, the
residual nonzero scalar is a reduction of a nonzero integral Kurihara
scalar. No finite Sha, rational rank, complex order, residual dimension,
or P_(2,0) witness is assumed.

The approved specialization is recorded in
[the integral/residual assessment](../drafts/literature/2026-10-05-integral-residual-index-defect.md).
L015 and L018 motivate the desired threshold but are not mathematical
inputs to this statement.

## Conclusion

Put D = Q_p/Z_p and F = S/S_div, where S_div is the maximal divisible
subgroup. There are finitely many positive exponents a_1,...,a_t such that

\[
S\simeq D^2\oplus F,\qquad
F\simeq\bigoplus_{j=1}^{t}(\mathbf Z/p^{a_j}\mathbf Z)^2.
\tag{1}
\]

Every divisor-minimal nonzero residual index n in N_(1,0) satisfies

\[
\nu(n)=\dim_{\mathbf F_p}\operatorname{Sel}(\mathbf Q,E[p])=2+2t.
\tag{2}
\]

Thus the minimum prime count over all nonzero residual indices in this
prime set is also 2+2t. A residual two-prime witness exists in N_(1,0)
if and only if F = 0. In Kim's notation for integral valuation minima,

\[
\operatorname{ord}(\widetilde\delta)=2,\quad
\partial^{(\infty)}(\widetilde\delta)=0,\quad
\operatorname{length}_{\mathbf Z_p}F
 =\partial^{(2)}(\widetilde\delta)=2\sum_{j=1}^{t}a_j.
\tag{3}
\]

Consequently the extra finite-quotient condition is equivalently
partial^(2)(tilde-delta) = 0. The residual excess counts positive paired
factors, not their lengths: when t > 0,
2 <= nu(n)-2 = 2t <= length_Z_p F, with equality on the right precisely
when every a_j = 1.

Residual system primitivity supplies partial^(infinity) = 0 and a
nonzero scalar at some index; the cited theorems do not replace it by
partial^(2) = 0. The formal calculation below shows that their module
and valuation conclusions retain positive finite factors. This is a
limitation of the proposed inference, not an arithmetic counterexample
to a possible stronger theorem about actual E. Nor does (2) produce a
P_(2,0) witness or identify the two divisible directions as rational.

## Proof

**Imported structure and coefficient identification.** Apply Chan-Ho
Kim, *The structure of Selmer groups and the Iwasawa main conjecture for
elliptic curves*, author text dated 2025-05-12,
[Theorem 1.8(1)--(3), printed p. 6](https://preprint.press.jhu.edu/ajm/sites/default/files/AJM-kim.pdf#page=7).
Its assumptions are p >= 5, surjective E[p], a prime-to-p Manin constant,
and nonzero integral Kurihara collection. Our residual nonvanishing
implies the last assumption. The structural clauses give (1) and
ord(tilde-delta) = corank S = 2. We do not use clauses (4)--(6), which
add finite p-primary Sha to identify rational rank and Sha.

The remaining local-torsion and Tamagawa hypotheses match
[Kim, Theorem 1.10, printed p. 7](https://preprint.press.jhu.edu/ajm/sites/default/files/AJM-kim.pdf#page=8).
Its residual-nonvanishing implication gives partial^(infinity) = 0.
Together with Theorem 1.8(3), this proves (3).
Here partial^(i) denotes Kim's minimum scalar p-valuation at integral
indices with i prime factors, as defined in Section 1.5.1; it is not the
residual prime count.

For the natural identification
Sel(Q,E[p]) = S[p], use
[Kim, Section 5.3.1, printed p. 27](https://preprint.press.jhu.edu/ajm/sites/default/files/AJM-kim.pdf#page=28),
which cites Mazur--Rubin, Lemma 3.5.3. Surjectivity of E[p] gives
E(Q)[p] = 0, so the global coefficient identification applies. These are
classical Kummer local conditions; no vanishing of local H^0 is asserted.
Import this identification and the structure theorem rather than
reproving them.

**Take p-torsion and count primes.** Each D summand has p-torsion F_p.
Each positive cyclic factor Z/p^a has p-torsion of dimension one,
regardless of a. Taking p-torsion in (1) therefore gives

\[
\dim_{\mathbf F_p}S[p]=2+2t.
\tag{4}
\]

Apply Ryotaro Sakamoto, *p-Selmer group and modular symbols*,
Doc. Math. 27 (2022), 1891--1922,
[Definition 1.4 and Theorem 1.5, p. 1893](https://ems.press/content/serial-article-files/29299?nt=1#page=3),
also [Theorem 4.8 and proof, p. 1919](https://ems.press/content/serial-article-files/29299?nt=1#page=29).
Section 1.1 assumes good ordinary p > 3, surjective E[p], and p prime
to #E(F_p) and the Tamagawa product, all retained here. Its theorem
identifies the prime count of every divisor-minimal residual witness
with dim Sel(Q,E[p]); this and (4) prove (2).

A nonzero residual witness has finitely many divisors, so it contains a
divisor-minimal nonzero witness. Hence every nonzero witness has at
least 2+2t prime factors, and divisor-minimal witnesses attain that
bound. Existence was granted, so the minimum is attained. It is two
exactly when t = 0, equivalently F = 0. A finite p-group has length zero
exactly when it is zero; (3) proves the valuation reformulation. Summing
the lengths of the paired cyclic factors proves the stated comparison
of excess and length.

**Primitivity audit and its limit.** Sakamoto's
[Proposition 3.19 and proof, pp. 1915--1916](https://ems.press/content/serial-article-files/29299?nt=1#page=25),
together with [Lemma 4.2, p. 1917](https://ems.press/content/serial-article-files/29299?nt=1#page=27),
equates residual scalar nonvanishing somewhere with the Kato-derived
rank-zero system being a basis at every coefficient depth. Its proof
writes the system as a times a basis of a free rank-one system module;
primitivity means a is a unit. This does not say that every scalar
evaluation of that basis is a unit, or that a unit evaluation occurs
at the first integral nonzero index. Theorem 4.8 locates the first
residual witness at dim Sel_p, which can exceed corank S by (4).

For a bounded check of precisely the imported module/valuation
constraints, fix any integer a >= 1 and take the formal discrete module

\[
S^{\rm form}=D^2\oplus(\mathbf Z/p^a\mathbf Z)^2.
\tag{5}
\]

Its dual has presentation diag(0,0,p^a,p^a) on four generators.
By the minors definition of Fitting ideals, its zeroth and first
Fitting ideals are zero, its second is (p^(2a)), its third is (p^a),
and its fourth is the unit ideal. Indeed the only nonzero 2 by 2 minor
of that diagonal matrix is p^(2a); the nonzero 1 by 1 minors generate
(p^a); every 3 by 3 or 4 by 4 minor uses a zero diagonal entry.
Its higher Fitting ideals are unit ideals. The even-index valuation
data partial^(2) = 2a and partial^(2i) = 0 for i >= 2, with
partial^(infinity) = 0 and integral order two, satisfy Kim's displayed
structure and Fitting formulas: the first paired exponent is
(2a-0)/2 = a and all later exponents are zero. Its residual dimension
is four, exactly the count predicted by (2), rather than the required
two. This works for every a >= 1, while a = 0 removes the finite pair.

This formal check realizes only those module and numerical constraints.
It constructs neither an elliptic curve, modular-symbol collection nor
full primitive Kolyvagin system. It therefore licenses abandoning the
inference from primitivity to F = 0 based on these constraints alone,
without asserting that a full arithmetic family with (5) has been
constructed. The remaining finite condition requires independent input;
primitivity already used above supplies no such condition in this audit.

## Mathlib

Full matching Kim/Sakamoto theorem: not checked. Supporting finite
cyclic p-torsion, dimension and Fitting-minor calculations were proved
explicitly here; Mathlib coverage of those supporting results was not
checked. No absence or formalization claim is made. This is a local
specialization of known structure and index theorems, not a claim of
progress beyond those sources.
