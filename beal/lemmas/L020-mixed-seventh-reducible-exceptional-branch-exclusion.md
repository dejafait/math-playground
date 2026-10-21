# L020 — Conditional exclusion of the reducible exceptional-algebra branch

## Hypotheses

Let X,Y,Z be nonzero signed integers satisfying

\[
X^5+Y^3=Z^7,\qquad \gcd(X,Y,Z)=1.
\]

Put eta=X^5/Z^7 and suppose that the following Q-algebras are isomorphic:

\[
\mathbb Q[T]/(15T^7-35T^6+21T^5-\eta)
\quad\text{and}\quad
\mathbb Q[T]/(T^7-483T^2+3955T-3945).
\]

This is precisely the additional algebra hypothesis of L018; it is not assumed to hold for every primitive solution.

Let F=Q(sqrt(5)), t=-X^5/Y^3, and let J/F be the Jacobian of the smooth projective curve

\[
C_t:\quad y^2=5x^6-12x^5+10tx^3+t^2.
\]

Use L019's geometric weight-two, covariant Tate realization with its real multiplication defined over F. The coefficient prime (7) is inert, so the rank-two coefficient representation is over F_(7), with residue field F_49. Let rho be its semisimplified stable-lattice reduction, extended to the algebraic closure through either residue-field embedding. Set the **base** prime q=(29,sqrt(5)-11); its residue field has order 29. Frobenius denotes arithmetic Galois Frobenius acting on the covariant Tate module.

## Conclusion

For each of the two coefficient embeddings, rho is absolutely irreducible. Equivalently, there is no primitive signed nonzero solution satisfying both the displayed algebra-isomorphism hypothesis and reducibility of its geometric residual representation.

This excludes only the reducible exceptional-algebra branch. It does not exclude the irreducible branch, prove that every solution belongs to this algebra branch, exclude the full signature (3,5,7), or resolve Beal.

## Proof

**Source scope and reason for the specialization.** The matching claim occurs in [Chocian, arXiv:2609.26996v1, Section 6.2, equations (34) and (36)–(40)](https://arxiv.org/html/2609.26996v1#S6.SS2). We reproduce its bounded reducible-sector assembly rather than import the unverified complete exclusion. L016 establishes the terminal finite separation, L017 the character restriction, L018 the conditional parameter restriction, and L019 the original-solution representation hypotheses. The difference checked here is the good-reduction and two-component trace interface joining these statements. The geometric realization is the named construction in [Pacetti–Villagra Torcomian, arXiv:2512.17845v1, Section 7.1, equation (32), and Remark 2.2](https://arxiv.org/html/2512.17845v1#S7.SS1). The rank-two coefficient decomposition and cyclotomic determinant are the supporting inputs of [Billerey–Chen–Dieulefait–Freitas, arXiv:2205.15861v5, Section 2.2, Definition 2.5, equation (2.7), and Theorem 2.8](https://arxiv.org/html/2205.15861v5#S2.SS2), in the same geometric normalization used in L019. No packet enumeration or original descent is used.

**Parameter and good reduction at the fixed base prime.** L018 gives 29 not dividing XYZ and the reductions of eta as 10,14,24,28. The original equation gives the exact identity

\[
t=-X^5/Y^3=\eta/(\eta-1).
\]

Thus t lies in Z_29 and its residues are respectively 14,10,25,15. In particular neither t nor t-1 vanishes modulo q. Since t is rational and q has residue field F_29, these are also its residues at the specified base prime, with no coefficient-embedding choice involved.

Over the local ring R=O_(F_q), form the double cover of the projective x-line by gluing the two charts

\[
y^2=5x^6-12x^5+10tx^3+t^2,
\qquad
v^2=5-12u+10tu^3+t^2u^6,
\]

with u=1/x and v=y/x^3 on their overlap. This is a finite locally free degree-two cover of P^1_R and hence proper and flat over R. The generic fibre is smooth by L019. The affine part of the special fibre is smooth by L016's squarefreeness check and the fact that 2 is a unit. At infinity the reduction has v=11 or 18 when u=0, and its derivative with respect to v is 2v, nonzero at both points. The two charts therefore give a smooth proper genus-two model over R. Its special fibre is exactly the C_(t mod q) of L016; the model also has the section x=0,y=t.

The Jacobian of a smooth proper curve with this section extends as the relative degree-zero Picard abelian scheme. Thus J has good reduction at q, with special fibre the Jacobian of that same curve. Smooth proper base change, or the equivalent good-reduction Tate-module identification, makes its 7-adic Frobenius characteristic polynomial the polynomial computed in L016 from the complete point counts. These standard Jacobian and good-reduction facts are supporting inputs; no equality between unrelated raw hypergeometric traces is asserted.

**Four-dimensional Frobenius versus both coefficient components.** Write r=t mod q and let A,B be the integers in its row of L016. On the four-dimensional Q_7 Tate space the Frobenius characteristic polynomial is

\[
Q_r(U)=U^4-AU^3+BU^2-29AU+29^2.
\]

The real-multiplication action is defined over F, so it commutes with G_F and with this Frobenius. After extending coefficients to an algebraic closure of Q_7, the two embeddings of the degree-two coefficient field split the Tate space into two rank-two components. The geometric determinant theorem cited above gives determinant 29 on **each** component. If their traces are a and b, then

\[
Q_r(U)=(U^2-aU+29)(U^2-bU+29).
\]

Comparing coefficients, without choosing one trace in preference to the other, gives

\[
a+b=A,\qquad ab=B-58.
\]

Consequently both traces satisfy the same integral relation

\[
P_r(a)=P_r(b)=0,\qquad P_r(S)=S^2-AS+B-58.
\]

This is exactly L016's two-trace polynomial. The argument needs only the inherited real multiplication, not a claim that the special fibre's full endomorphism algebra is unchanged or that Frobenius has distinct eigenvalues.

**Lattice reduction and Frobenius convention.** A stable lattice for the rank-two representation has integral Frobenius matrices, so its trace is integral at the coefficient prime (7). The same holds after either embedding. Reducing the preceding monic integral relations therefore gives

\[
\overline P_r(\operatorname{tr}\rho(\operatorname{Frob}_q))=0
\]

for either residue-field embedding into the algebraic closure of F_7. Semisimplification preserves traces, so it does not change this relation. Nothing here asserts that the two traces initially lie in F_7, or discards the second embedding of F_49.

For clarity about normalization, arithmetic Galois Frobenius on the covariant Tate module at a good prime corresponds to the q-power endomorphism of the special fibre. This is the endomorphism whose characteristic polynomial is obtained from Weil's point-count formula in L016. The equivalent cohomological formula uses geometric Frobenius on H^1. We do not substitute inverse Frobenius into Q_r or apply another Tate twist. The determinant used above is the value of the 7-adic cyclotomic character on arithmetic Frobenius, namely 29, reducing to 1 modulo 7. This is the same convention as L017.

**Contradiction in the reducible sector.** Suppose that rho is reducible for one coefficient embedding. L019 supplies all four hypotheses of L017 for this geometric representation, so L017 gives

\[
\operatorname{tr}\rho(\operatorname{Frob}_q)\in\{2,-2\}=\{2,5\}.
\]

The preceding trace relation requires that value to be a root of P_r modulo 7. L016 proves this impossible: its last two resultant columns, equivalently evaluations at 2 and 5, are

| r | P_r(2) modulo 7 | P_r(5) modulo 7 |
| --- | --- | --- |
| 14 | 1 | 5 |
| 10 | 6 | 3 |
| 25 | 1 | 1 |
| 15 | 4 | 3 |

Every entry is nonzero. Hence neither reducible trace is a possible component trace. This contradiction applies to either coefficient embedding and proves the stated absolute irreducibility.

**Achieved and required thresholds.** The achieved threshold is zero solutions in the explicitly defined reducible exceptional-algebra branch. Zero solutions of the entire fixed signature would additionally require exclusion of the irreducible branch and coverage of all possible descent algebras; neither is established here. Beal requires emptiness for every residual signature. This assembly is a REPRODUCTION of a claim in the checked literature, not progress beyond that literature or a complete candidate resolution.

## Mathlib

Coverage of the full conditional branch exclusion: **not checked**. Coverage of the supporting smooth proper model, relative Jacobian, Tate-module good reduction, real-multiplication decomposition and lattice-trace results: **not checked**. The named PVT construction and BCDF decomposition/determinant results are supporting inputs with direct links above. [Chocian Section 6.2](https://arxiv.org/html/2609.26996v1#S6.SS2) matches the conditional assembly claim being reproduced; it is not imported as a verified complete signature theorem. No matching Mathlib declaration or formal verification is claimed.
