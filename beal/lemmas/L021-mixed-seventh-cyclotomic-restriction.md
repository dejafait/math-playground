# L021 — Conditional cyclotomic-restriction absolute irreducibility

## Hypotheses

Let X,Y,Z be nonzero signed integers such that

\[
X^5+Y^3=Z^7,\qquad \gcd(X,Y,Z)=1.
\]

Put eta=X^5/Z^7 and assume the Q-algebra isomorphism

\[
\mathbb Q[T]/(15T^7-35T^6+21T^5-\eta)
\simeq \mathbb Q[T]/(T^7-483T^2+3955T-3945).
\]

Set F=Q(sqrt(5)), t=-X^5/Y^3, and let J/F be the Jacobian of the smooth projective curve

\[
y^2=5x^6-12x^5+10tx^3+t^2.
\]

Use the geometric weight-two covariant Tate representation with real multiplication defined over F, as in L019 and L020. Let rho be its semisimplified stable-lattice reduction at the coefficient prime (7), extended from k=F_49 to an algebraic closure of F_7 through either of the two coefficient embeddings. No semistable-reduction hypothesis on J is imposed.

## Conclusion

For either coefficient embedding,

\[
\rho|_{G_{F(\zeta_7)}}\quad\text{is absolutely irreducible}.
\]

This establishes a conditional residual-restriction input for a later modular-location application. It does not establish that application's other hypotheses, exhaust its modular packets, remove the displayed algebra hypothesis, or exclude the entire signature (3,5,7).

## Proof

**Source scope.** L019 supplies finite flatness at the base prime p=(7) and det(rho)=chi_7. L020 supplies absolute irreducibility over G_F, with exactly the algebra hypothesis above. We specialize the mechanism of [Billerey–Chen–Dieulefait–Freitas, arXiv:2205.15861v5, Lemma 6.9 and its proof](https://arxiv.org/html/2205.15861v5#S6.SS2), replacing its good-or-multiplicative reduction assumption by the established finite-flat generic-fibre input. Thus its stated lemma is not directly imported. The related cyclotomic mechanism is [Dieulefait–Pacetti, arXiv:2108.07577v2, Lemma 1.13 and proof](https://arxiv.org/html/2108.07577v2#S1.SS5), stated over Q. We give the elementary cyclic-quotient argument over F below, without importing its Q-specific conclusion or Feit's theorem. The changed hypotheses justify this reproduction; no claim of progress beyond the checked literature is made.

**Coefficient extension and finite-flat constituents.** Write K=F_p. By L019, K/Q_7 is unramified of degree two, with absolute ramification index e=1 and residue cardinality q=49. There is a finite coefficient field k_0 containing the chosen copy of k over which rho is defined and whose underlying F_7 module has a finite flat model over O_K, killed by 7. Enlarge k_0 to any finite field k' needed to define the constituent lines and containing F_2401. On underlying F_7 representations,

\[
V\otimes_{k_0} k'\simeq V^{\oplus [k':k_0]},
\]

by choosing a k_0-basis of k'; Galois acts trivially on the scalar factor. The product of that many copies of the finite flat model realizes this representation. This assertion concerns scalar extension, not a field extension of K and not a Tate twist.

For the field action and subquotients use [Raynaud, *Schémas en groupes de type (p,...,p)*, Bull. Soc. Math. France 102 (1974), 241–280, Proposition 3.3.2(2) and Corollary 3.3.6(1), printed pp. 265–268](https://www.numdam.org/article/BSMF_1974__102__241_0.pdf#page=26). Since e=1<7-1, generic-fibre morphisms extend uniquely; coefficient endomorphisms therefore extend, and their field-action identities hold by uniqueness. A generic-fibre submodule has finite flat schematic closure over the valuation ring, and the finite flat quotient realizes the quotient module. One can also apply Raynaud's flat-kernel and flat-cokernel statement in this range. Thus successive subquotients used here retain finite flatness. The same statements apply after strict henselization: this changes the generic Galois group to inertia and preserves e=1.

Consequently [Raynaud, Theorem 3.4.3 and Corollary 3.4.4, printed p. 270](https://www.numdam.org/article/BSMF_1974__102__241_0.pdf#page=30) apply to every underlying F_7 Jordan–Hölder inertia factor. Its scalar characters over the algebraic closure have fundamental-character digits 0 or 1. If a character has minimal field F_(7^d) and is expressed at a level m divisible by d, its exponent is multiplied by

\[
(7^m-1)/(7^d-1)=1+7^d+\cdots+7^{m-d};
\]

this simply repeats its d digits. Different embeddings cyclically rotate the digits, preserving the bound. This explains both coefficient enlargement and the use of a nonminimal level below; no character is assumed to take values in F_7.

Choose compatible fundamental characters omega_m on inertia of order 7^m-1, normalized so that

\[
\chi_7|_I=\omega_2^8=\omega_4^{400},\qquad
\omega_2=\omega_4^{50}.
\]

These are the standard norm compatibilities for fundamental characters at the unramified local field. We work over the algebraic closure throughout; each of the following local cases is therefore exhaustive regardless of the initial coefficient embedding.

**Locally reducible case.** Suppose rho restricted to G_K has an invariant line. Its two scalar constituents alpha,beta have trivial wild inertia, since finite multiplicative groups in characteristic 7 have order prime to 7. For a tame generator tau and local Frobenius phi, the tame relation phi tau phi^(-1)=tau^49 shows that a character of G_K has inertia values of order dividing 48. By the finite-flat digit statement just justified,

\[
\alpha|_I=\omega_2^a,\quad \beta|_I=\omega_2^b,
\qquad a,b\in\{0,1,7,8\}.
\]

The determinant requires a+b=8 modulo 48. Since 0<=a+b<=16, this is the integer equality a+b=8. Thus the unordered pair is either {0,8} or {1,7}. Their ratio orders are respectively

\[
48/\gcd(48,8)=6,\qquad 48/\gcd(48,6)=8.
\]

This conclusion does not require the local representation to split. A lift of a tame generator has these two distinct eigenvalues, so its matrix is diagonalizable over the algebraic closure and has precisely the indicated projective order. Thus projective inertia contains an element of order 6 or 8 even if a local extension is nonsplit.

**Locally absolutely irreducible case.** Now suppose rho restricted to G_K is irreducible over the algebraic closure. Apply [Imai, *On the connected components of moduli spaces of finite flat models*, arXiv:0801.1948v4 (14 November 2010), Lemma 1.1 and proof, pp. 1–2](https://arxiv.org/pdf/0801.1948v4#page=2), with q=49 and enlarged coefficients containing F_(q^2). It gives trivial wild inertia and the two tame characters

\[
\omega_4^s,\quad \omega_4^{49s},\qquad 50\nmid s.
\]

The mechanism is that wild invariants of a finite 7-group are nonzero and stable under the full local group, hence fill an irreducible module. Tame inertia is then semisimple; scalar inertia would leave an eigenline for Frobenius invariant, whereas two distinct inertia lines must be exchanged by Frobenius. This gives the displayed conjugate pair, as in Imai's proof.

Raynaud's digits allow the representative

\[
s=r_0+7r_1+49r_2+343r_3,\qquad r_i\in\{0,1\},\quad 0\leq s\leq400.
\]

This remains valid if an inertia character initially has smaller minimal field, by digit repetition above. The determinant, rather than an assumed complementary-digit rule, imposes

\[
50s\equiv400\pmod{2400},\qquad s\equiv8\pmod{48}.
\]

Reducing the digit expression modulo 48 gives

\[
(r_0+r_2)+7(r_1+r_3)\equiv8\pmod{48}.
\]

The left side lies between 0 and 16, so it equals 8. Both parenthesized sums lie in {0,1,2}; necessarily both equal 1. Therefore

\[
s\in\{8,56,344,392\}.
\]

All four satisfy 50 not dividing s, and each has gcd(50,s)=2. The ratio of the two inertia characters has order

\[
\frac{2400}{\gcd(2400,48s)}
=\frac{50}{\gcd(50,s)}=25.
\]

Thus in this case projective inertia is cyclic of order 25. The complete local alternatives relevant here give an element of order 6, 8 or 25; in particular none allows projective inertia of order at most two.

**The cyclotomic extension and its quadratic subfield.** The unique quadratic subfield of Q(zeta_7) is Q(sqrt(-7)), so it is distinct from F=Q(sqrt(5)). As F is quadratic, F intersects Q(zeta_7) in Q. Hence

\[
\operatorname{Gal}(F(\zeta_7)/F)\simeq C_6
\]

and its unique quadratic subextension is M=F(sqrt(-7)). The quadratic cyclotomic identification is the standard one Q(sqrt(p^*)) also used in Dieulefait–Pacetti Lemma 1.13. At p, the polynomial U^2+7 is Eisenstein over O_K, since v_K(7)=1. Consequently M/F is ramified at p and inertia surjects onto Gal(M/F). This ramification assertion uses the base prime over 7, independently of the coefficient embeddings.

**Elementary restriction argument.** Suppose for a contradiction that rho restricted to N=G_(F(zeta_7)) is reducible. All representations and invariant lines in this paragraph are over the algebraic closure. Because N is normal in G=G_F, the group G permutes the set of N-invariant lines. If there is exactly one such line, it is G-invariant, contrary to L020.

If N acts by scalars, choose g in G lifting a generator of G/N=C_6. Every matrix in rho(G) is a scalar times a power of rho(g). An eigenline of rho(g) is then G-invariant, again a contradiction. Finally, if N has more than one invariant line and does not act by scalars, it has exactly two: choose two as a basis, so N is diagonal; one nonscalar element of N then has just those two eigenlines. Global irreducibility forces G to interchange the two lines. The resulting nontrivial permutation character G to C_2 is trivial on N, so its kernel is G_M by uniqueness of the quadratic subextension of G/N.

In this last case rho(G) consists of diagonal and antidiagonal matrices in that basis. Its image is finite: rho descends to a finite coefficient field. The diagonal subgroup has order prime to 7, being a subgroup of a product of finite multiplicative groups, and its index is two. Thus the whole image has order prime to 7. Wild inertia has trivial image, and the inertia image is a finite quotient of tame inertia, hence cyclic. Its projective image is cyclic as well.

Ramification of M/F at p provides an inertia element whose matrix interchanges the two lines, hence is antidiagonal. The square of an invertible antidiagonal matrix is scalar, so that element has projective order two. Let C be the cyclic projective inertia image and D its diagonal subgroup. The map C to C_2 given by the line permutation is surjective with kernel C intersect D. In a cyclic group a surjection to C_2 sends a generator outside its kernel. Such a generator is therefore represented by an antidiagonal matrix and has order two. It follows that C itself has order two. This contradicts the local element of order 6, 8 or 25 established above.

All possibilities for a reducible restriction have led to a contradiction. Hence the restriction is absolutely irreducible. The argument began with an arbitrary one of the two coefficient embeddings; L019 and L020 apply to each, and the coefficient and digit steps preserve both. The conclusion therefore holds for each embedding.

**Threshold and limitations.** The local threshold required to eliminate the quadratic obstruction was projective inertia larger than two; the exhaustive cases provide orders 6, 8 and 25. Only the stated conditional restriction is proved. L020's algebra isomorphism remains an assumption, and the modular-location, packet-exhaustion, global-descent and uniform-signature steps remain separate. No complete Beal candidate is obtained.

## Mathlib

Coverage of this full finite-flat restriction specialization: **not checked**. Coverage of the supporting Raynaud finite-flat, Imai inertia, cyclotomic-field and normal-subgroup results: **not checked**. The precise primary citations above are supporting mathematical inputs; no matching Mathlib declaration or formal verification is claimed. The specialization is recorded as REPRODUCTION, not certified originality.
