# L024 — Conditional exact-level location by PVT citation

## Hypotheses

Let X,Y,Z be nonzero signed integers satisfying

\[
X^5+Y^3=Z^7,\qquad \gcd(X,Y,Z)=1.
\]

Assume the Q-algebra isomorphism

\[
\mathbb Q[T]/(15T^7-35T^6+21T^5-X^5/Z^7)
\simeq \mathbb Q[T]/(T^7-483T^2+3955T-3945).
\]

Set F=Q(sqrt(5)), t=-X^5/Y^3 and let J/F be the Jacobian of the smooth projective curve

\[
y^2=5x^6-12x^5+10tx^3+t^2.
\]

Use L019's geometric weight-two covariant Tate component with real multiplication defined over F. The **coefficient** prime (7) is inert; put E=F_(7), O=O_E and k=O/7O=F_49. Fix an algebraic closure of Q_7, with residue algebraic closure overline F_7. For each of the two embeddings iota:E -> overline Q_7, let sigma_iota:k -> overline F_7 be its residue embedding, and let rho_iota be the semisimplified reduction of an O-stable lattice extended through sigma_iota. Both embeddings are included separately. The **base** field of its Galois group remains F.

For the source's coordinate notation set

\[
(a,b,c)=(X,-Z,Y),\quad p=7,\quad
 a_0=a5^{-v_5(a)},\quad c_0=c3^{-v_3(c)},
\]

where v_l of a signed nonzero integer is v_l of its absolute value, so a_0 and c_0 retain their signs.

## Conclusion

For each iota separately there exist a cuspidal Hilbert newform f_iota over F of parallel weight two and trivial character, a prime lambda_iota above 7 of its coefficient field K_(f_iota), and a residual embedding

\[
j_iota:O_{K_{f_iota}}/lambda_iota\longrightarrow\overline{\mathbb F}_7
\]

such that, after extending the newform's semisimplified residual representation through j_iota,

\[
rho_iota\simeq \overline\rho_{f_iota,lambda_iota}^{\,j_iota}.
\]

The newform has exact level, as an ideal of O_F,

\[
\mathfrak n=(3)^{e_3}(\sqrt5)^{e_5},\qquad e_3,e_5\in\{2,3\},
\]

where the source's clauses, unchanged in its a,b,c notation, are

\[
e_3=\begin{cases}
2&3\mid ab,\\
2&3\mid c\ \text{and}\ (2c_0^3\equiv a^5\pmod9\ \text{or}\ -2c_0^3\equiv a^5\pmod9),\\
2&3\nmid abc\ \text{and}\ 4c^3\equiv a^5\pmod9,\\
3&\text{otherwise},
\end{cases}
\]

\[
e_5=\begin{cases}
2&5\mid bc,\\
2&5\mid a\ \text{and}\ c^3/a_0^5\equiv6,12,28\pmod{25},\\
2&5\nmid abc\ \text{and}\ c^3/a\equiv6,8,17,19\pmod{25},\\
3&\text{otherwise}.
\end{cases}
\]

The fractions mean multiplication by the inverse of the denominator modulo 25: a_0 is prime to 5 by definition, and a is prime to 5 in the third clause. In particular its denominator is a, exactly as printed, rather than a^5. The level depends only on the coordinates, but the two forms, coefficient fields, primes and residual identifications need not coincide. There is no restriction that K_(f_iota)=F.

## Proof

**Precise imported result.** Apply Ariel Pacetti and Lucas Villagra Torcomian, *On the generalized Fermat equation of signature (5,p,3)*, arXiv:2512.17845v1, 19 December 2025, Section 7.2, Theorem 7.8(i)–(ii), equation (35) and proof, [primary theorem](https://arxiv.org/html/2512.17845v1#S7.SS2). Its setup is a primitive solution of a^5+b^p+c^3=0 over the signed integers, with the plus component at t_0=-a^5/c^3 and a coefficient prime above p. Section 1.3 admits p>=7, so the endpoint p=7 is included. Its premise is residual irreducibility; its conclusion and proof give the exact level above, parallel weight two and trivial Nebentypus. The exact conductor cases and level-lowering conclusion are imported together, including the source's finite mod-25 computation. This is not an independent conductor computation or reproof.

**Matching the solution and representation.** The displayed substitution gives a^5+b^7+c^3=X^5-Z^7+Y^3=0. It is nontrivial and primitive, including coordinates of absolute value one. L019 verifies its plus geometric realization, integral real multiplication and the covariant Tate normalization using PVT Section 7.1 equation (32) and Remark 2.2. Thus t_0=t, and the component to which the theorem applies is the stated component of J. No further Tate or quadratic twist is made. Its coefficient completion is E, with unique coefficient prime (7), independently of the base prime with that notation. L020 supplies absolute irreducibility of rho_iota under exactly the stated algebra hypothesis. It therefore supplies the theorem's irreducibility premise.

**Coefficient identifications.** Fix one iota. Extend the geometric component to overline Q_7 through iota and reduce its stable lattice through sigma_iota; this is rho_iota by definition and L019's normalization. Apply Theorem 7.8 to this realization. The theorem's residual isomorphism is interpreted over overline F_7, with a prime lambda_iota of the newform coefficient field above 7 and the corresponding residual embedding j_iota. Equivalently one may embed its local coefficient completion into overline Q_7 and then use the induced residue embedding. No embedding of the newform coefficient field into F is required. Semisimplified reduction is lattice-independent, so the stable lattice used in the theorem does not impose another residual representation. This obtains the stated isomorphism and every printed level clause for the fixed iota. Apply the same theorem separately to the other iota; L020 supplies its irreducibility premise as well. The clauses are rational coordinate conditions and hence give the same level exponents for both applications.

L019 and L020 are the only direct local lemma inputs. L021–L022 and L023's audited local-line portion were reviewed in the saved source assessment as supporting checks of the source interfaces; they are not an independent derivation of this imported theorem. In particular L023's source-blocked type-to-level conclusion is not used, and its unfinished work remains parked.

**Scope and achieved threshold.** This KNOWN_IMPORTED application supplies the conditional ambient spaces needed for an irreducible-sector comparison. It establishes neither their packet exhaustion nor the assertion that all original solutions satisfy the algebra hypothesis. PVT Table 7.2's coefficient-field-F column does not exhaust arbitrary coefficient fields, and Theorem A's elimination is not an elimination at 7. L016's finite resultants cannot be promoted to an exclusion using location alone. No fixed-signature exclusion or complete Beal candidate follows, and no progress beyond the cited theorem is claimed. The continuation test of matching both geometric coefficient realizations succeeds; the source's conductor and automorphic claims remain cited inputs.

## Mathlib

Coverage of this full conditional exact-level statement, Hilbert newforms, PVT's conductor clauses and level lowering: **not checked**. The precise PVT theorem above is the mathematical source. No matching Mathlib declaration or formal verification is claimed; no independent reproof is needed for this cited import.
