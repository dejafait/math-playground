# L015 — The fixed-prime p^2 lifting criterion for the prime-deletion basis

## Hypotheses

Let E/Q be non-CM, and let p >= 5 be good ordinary. Assume that
the action on E[p] is surjective, p does not divide #E(F_p), the
Manin constant or any Tamagawa factor, and E(Q_p)[p] = 0. Neither
finite p-primary Sha nor positive rational rank is assumed.

Use Sakamoto, *p-Selmer group and modular symbols*, Documenta Math.
27 (2022), 1891--1922, DOI 10.4171/DM/X21, in the precise scope of
[the saved SPECIALIZE assessment](../drafts/literature/2026-10-03-rank-zero-extra-relaxed-prime.md).
Put R_m = Z/p^m Z, T_m = E[p^m], S_m = Sel(Q,T_m), for m = 1,2.
F_cl is the classical Kummer Selmer structure. A superscript ell
relaxes the condition at ell; (d) imposes transverse conditions at
the prime divisors of d. These are the conventions of
[Definitions 2.3--2.5, printed p. 1898](https://ems.press/content/serial-article-files/29299?nt=1#page=8).

Let N = ell_1 ell_2 be delta-minimal modulo p: its mod-p Kurihara
number is nonzero and those of all proper positive divisors vanish.
Retain this as an additional premise; it is not supplied by analytic
order two. The primes are distinct and lie in P_(1,0).

For the level-two conclusions additionally require both primes in

\[
\mathcal P_{2,0}
 =\{\ell\text{ of good reduction}:\quad
       E(\mathbf F_\ell)[p^2]\simeq\mathbf Z/p^2\mathbf Z,
       \quad\ell\equiv1\pmod{p^2}\}.
\tag{1}
\]

This is [Section 2.3, printed p. 1902](https://ems.press/content/serial-article-files/29299?nt=1#page=12).
Membership in P_(1,0) alone checks neither condition at depth two.
No numerical primes were specified in the saved target, so (1) is
an explicit eligibility test, not a computed claim about their values.

Use the coefficient-compatible systems kappa^(m) = kappa_(xi,m,0)
constructed in [Theorem 3.17 and the proof of Proposition 3.19,
printed pp. 1915--1916](https://ems.press/content/serial-article-files/29299?nt=1#page=25).
Fix the same generators of G_ell at both levels and compatible bases
for the rank-one singular quotients. Trivialize the G_d tensor factors
using these generators. Since ell_i belongs to P_(2,0), their orders
are divisible by p^2, so R_m tensor G_ell_i is identified with R_m.
On common indices, reduction rho induced by
[p]: E[p^2] -> E[p] then sends kappa^(2) to kappa^(1).
Write delta_m(d) for the scalarized delta(kappa^(m))_d, and set

\[
c_i^{(m)}=\kappa_{\ell_j,\ell_i}^{(m)},\qquad
g_i=\kappa_{1,\ell_i}^{(2)},\qquad j\ne i.
\tag{2}
\]

The mod-p nonvanishing comparison in Lemma 4.2 identifies the
delta-minimal premise with delta_1(N) != 0 and delta_1(e) = 0
for every proper divisor e of N.

## Conclusion

Assuming (1), the following three conditions are equivalent:

1. Both actual prime-deletion components c_1^(2), c_2^(2) lie in S_2.
2. The classical coefficient reduction rho: S_2 -> S_1 is surjective.
3. Sha(E/Q)[p] = p Sha(E/Q)[p^2].

There are unique h_1,h_2 in S_1 with g_i = iota(h_i), where iota
is induced by the inclusion E[p] -> E[p^2]. Condition 1 is also
equivalent to h_1 = h_2 = 0. More explicitly, all possible failures
of classical membership are at the two auxiliary primes, and

\[
\begin{aligned}
v_{\ell_i}(c_i^{(2)})&=\delta_2(\ell_j),&
v_{\ell_j}(c_i^{(2)})&=\varphi_{\ell_j}^{fs}(g_i),\\
\delta_2(\ell_i)&=-\varphi_{\ell_i}^{fs}(g_i),&
\delta_2(1)&=0.
\end{aligned}
\tag{3}
\]

Here v_ell is the singular quotient map and phi_ell^fs is finite
projection followed by finite-singular comparison. The nonzero
terms in (3), if any, are killed by p. Testing only delta_2(ell_i)
therefore omits the other auxiliary localizations.

If the equivalent conditions hold, c_1^(2),c_2^(2) form an R_2-basis
of S_2. This is a finite-depth Selmer statement. It gives no rational
rank lower bound, no infinite compatible classical family, and no
production of N from m(E) = 2. The value of the obstruction in
condition 3 under the retained premises remains undetermined.

## Proof

**Imported residual basis and local facts.** Apply
[Theorem 4.8 and Corollary 4.10, printed pp. 1919--1920](https://ems.press/content/serial-article-files/29299?nt=1#page=29)
by citation. They give dim_(F_p) S_1 = 2 and a localization isomorphism

\[
S_1\xrightarrow{\sim}
 H^1_{ur}(\mathbf Q_{\ell_1},T_1)
 \oplus H^1_{ur}(\mathbf Q_{\ell_2},T_1).
\tag{4}
\]

The classes c_i^(1) are its diagonal basis: their localization at
ell_j, j != i, is zero, and that at ell_i is nonzero. The proof of
Corollary 4.10 also gives H^1_(F_cl^N)(Q,T_1) = S_1. One can see
this last equality directly from Sakamoto's
[Theorem 2.1, printed p. 1897](https://ems.press/content/serial-article-files/29299?nt=1#page=7):
the map from the sum of singular quotients to S_1^vee is dual to
(4) under the perfect local pairings, and is injective. Thus relaxing
the two primes adds no residual classes. In particular

\[
H^1_{F_{cl}^{\ell_i}}(\mathbf Q,T_1)=S_1,\qquad
A_i^{(1)}:=H^1_{F_{cl}^{\ell_i}(\ell_j)}(\mathbf Q,T_1)
          =\mathbf F_p c_i^{(1)}\subset S_1.
\tag{5}
\]

For the second equality, transverse and unramified conditions have
zero intersection at ell_j, and (4) identifies its strict kernel
with the indicated line.

At either eligible prime, Section 2.3 gives
H^1(Q_ell,T_m) = H^1_ur(Q_ell,T_m) direct-sum H^1_tr(Q_ell,T_m),
with both summands free of rank one over R_m. The coefficient maps
respect these summands, and

\[
0\longrightarrow H^1_{ur}(\mathbf Q_\ell,T_1)
 \xrightarrow{\iota}H^1_{ur}(\mathbf Q_\ell,T_2)
 \xrightarrow{\rho}H^1_{ur}(\mathbf Q_\ell,T_1)
 \longrightarrow0
\tag{6}
\]

is exact; the same statement holds for the transverse summand and
the corresponding singular quotient. For example, the unramified
module is T_m/(Fr_ell-1)T_m. Over Z/p^2 its Frobenius matrix has
one unit invariant factor, since its reduction has rank one, and
one zero invariant factor, since the quotient is free rank one.
This identifies rho with reduction and iota with multiplication
by p. The transverse assertion follows from the compatible
finite-singular isomorphism in Section 2.3. This verifies the
coefficient maps needed here, not merely their dimensions.

For the remaining local conditions use
[Corollary 2.15, printed p. 1902](https://ems.press/content/serial-article-files/29299?nt=1#page=12):
F_cl is Cartesian. Consequently the preimage under iota of a
classical local condition is the classical residual condition.
Together with (6), the same assertion holds for the relaxed and
transverse modifications used here. This is also the socle
compatibility recorded in Sakamoto's Lemma 2.2. At the real place
odd-p H^1 is zero, so no additional condition appears.

**Track the four auxiliary errors.**
[Definition 2.18 and the definition of delta, printed pp. 1903--1904](https://ems.press/content/serial-article-files/29299?nt=1#page=13)
give, with the fixed tensor trivializations,

\[
v_\ell(\kappa_{d\ell,q}^{(m)})
 =\varphi_\ell^{fs}(\kappa_{d,q}^{(m)}),\qquad
v_q(\kappa_{d\ell,q}^{(m)})
 =-\varphi_\ell^{fs}(\kappa_{d,\ell}^{(m)}),\qquad
\delta_m(d)=v_q(\kappa_{d,q}^{(m)}).
\tag{7}
\]

Take d = 1, ell = ell_j and q = ell_i to get the first two
equalities in (3). Take ell = ell_i and q = ell_j to get the third.
The same equations hold at level one.

Let g_i^(1) = kappa_(1,ell_i)^(1). It is classical away from ell_i,
and v_(ell_i)(g_i^(1)) = delta_1(1) = 0, so it belongs to S_1.
The third equation in (3) at level one gives
phi_(ell_i)^fs(g_i^(1)) = -delta_1(ell_i) = 0. The second equation
and classical membership of c_i^(1) give
phi_(ell_j)^fs(g_i^(1)) = 0. Finite-singular comparison is an
isomorphism on the unramified summands, so (4) implies g_i^(1) = 0.

Surjectivity of the residual representation gives H^0(Q,T_1) = 0.
The coefficient sequence 0 -> T_1 -> T_2 -> T_1 -> 0 therefore
gives an injective iota on global H^1, with image ker(rho).
Compatibility implies rho(g_i) = 0, hence g_i = iota(h_i) uniquely.
Cartesian propagation places h_i in H^1_(F_cl^(ell_i))(Q,T_1).
By (5), h_i belongs to S_1. Its singular localization at ell_i is
zero, and functoriality gives delta_2(1) = v_(ell_i)(g_i) = 0.
All remaining terms in (3) factor through iota, so are killed by p.

The component c_i^(2) is already classical at every prime except
ell_i and ell_j, including p. It is classical at these two primes
exactly when its two singular localizations in (3) are zero.
If both components are classical, the first equality gives
delta_2(ell_1) = delta_2(ell_2) = 0. The second and third equalities
then give both finite-singular coordinates of each iota(h_i) equal
to zero. Injectivity in (6) and (4) force h_i = 0. Conversely,
h_1 = h_2 = 0 makes all four errors zero by (3). This proves the
error-vector criterion.

**Compare actual family lifting with all classical lifting.**
If both c_i^(2) are classical, their reductions are the cited basis
of S_1. Thus rho: S_2 -> S_1 is surjective.

Conversely assume rho is surjective, and take y_i in S_2 with
rho(y_i) = c_i^(1). At ell_j, j != i, the residual localization
of y_i is zero by (4). Its localization is unramified, so (6)
writes it as iota(beta_j) for beta_j in H^1_ur(Q_(ell_j),T_1).
Choose b in S_1 with loc_(ell_j)(b) = beta_j, using (4). Then

\[
y'_i=y_i-\iota(b)
\tag{8}
\]

is classical, still reduces to c_i^(1), and has zero localization
at ell_j. In particular it belongs to
A_i^(2) = H^1_(F_cl^(ell_i)(ell_j))(Q,T_2).
The actual c_i^(2) belongs to this same group. Their difference
has zero reduction, hence equals iota(a) for a unique global
residual class. Cartesian propagation, including the transverse
condition verified in (6), gives a in A_i^(1). By (5), a is
classical, so iota(a) is classical. Equation (8) now shows that
c_i^(2) is classical. This proves conditions 1 and 2 equivalent;
an arbitrary lift was used only to test the actual prescribed family.

**Identify the descent defect without assuming finite Sha.** Apply
the Kummer sequences and their coefficient diagram in
Milne, *Elliptic Curves*, second edition (2021), Chapter IV,
[equation (29), printed p. 113](https://www.jmilne.org/math/Books/EC2.pdf#page=118)
and [the diagram on printed p. 129](https://www.jmilne.org/math/Books/EC2.pdf#page=134),
as already recorded in the standard inputs. The downward maps are
reduction on E(Q)/p^m E(Q) and multiplication by p on Sha[p^m].
Reduction E(Q)/p^2 E(Q) -> E(Q)/p E(Q) is surjective. A diagram
chase therefore gives the canonical isomorphism

\[
\operatorname{coker}(S_2\xrightarrow{\rho}S_1)
 \simeq\Sha(E/\mathbf Q)[p]\big/p\Sha(E/\mathbf Q)[p^2].
\tag{9}
\]

Indeed the quotient map from S_1 induces a surjection onto the
right side. If a class maps to p alpha for alpha in Sha[p^2],
lift alpha to S_2 and subtract its reduction. The remaining class
is rational Kummer and lifts through the surjective point-quotient
map. This proves that its kernel is exactly rho(S_2). Thus conditions
2 and 3 are equivalent. No assertion about the size or finiteness
of the entire Sha group is used.

Finally put r = rank E(Q). Surjective E[p] excludes rational
p-primary torsion. Since dim S_1 = 2, the Kummer sequence gives
|Sha[p]| = p^(2-r), so the achieved bound is r <= 2. Under
condition 3, multiplication p on Sha[p^2] has kernel Sha[p] and
image Sha[p]; hence |Sha[p^2]| = |Sha[p]|^2 and |S_2| = p^4.
An R_2-linear relation between c_1^(2),c_2^(2) first reduces to a
zero relation in their residual basis, so its coefficients are
divisible by p. The identity p c_i^(2) = iota(c_i^(1)), and global
injectivity of iota, then force both coefficients to vanish modulo
p^2. Their R_2-span has order p^4 and is all of S_2.

This does not establish condition 3. Even if it holds, a p^2 Selmer
basis leaves the rational Kummer subspace unmarked; the required
rank-two lower bound remains missing. The application reproduces
the consequences of the assessed Selmer/Kolyvagin theory and the
known Kummer diagram. No progress beyond checked literature or
arithmetic counterexample to automatic lifting is claimed.

## Mathlib

Full coverage of this fixed-prime family lifting equivalence:
**not checked**. Supporting coefficient exact sequences, Cartesian
local conditions, finite-singular comparison, Poitou--Tate duality
and Kummer diagrams: **not checked**. Sakamoto's Theorem 3.17 and
Corollary 4.10 match the construction and residual-basis inputs;
Theorem 2.1, Lemma 2.2, Corollary 2.15 and Section 2.3 support the
specialization. Milne's cited diagram supports (9). These precise
citations are not claimed Mathlib matches or matches for the entire
equivalence. No absence or certified novelty inference is made.
