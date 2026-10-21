# L019 — Mixed seventh-power weight-two representation applicability

## Hypotheses

Let X,Y,Z be nonzero signed integers with gcd(X,Y,Z)=1 and

\[
X^5+Y^3=Z^7.
\]

Put F=Q(sqrt(5)), t=-X^5/Y^3, and let J/F be the Jacobian of the smooth projective curve

\[
C_t:\quad y^2=5x^6-12x^5+10tx^3+t^2.
\]

Write E=F_(7) for the completion at (7), O=O_E and k=O/7O=\mathbf F_49. Use the geometric, weight-two plus realization: the rank-two E-representation on the covariant Tate module of J with its F-action. Let rho be the semisimplified reduction of an O-stable lattice, viewed over an algebraic closure of k.

The Jacobian realization and its real multiplication are the cited inputs specified in the proof. No exceptional-algebra hypothesis and no residual irreducibility hypothesis is imposed.

## Conclusion

The representation rho meets the four representation hypotheses of L017:

1. det(rho)=chi_7, the mod-7 cyclotomic character;
2. it is unramified outside the primes over 3,5,7;
3. its Artin-conductor exponents at (3) and (sqrt(5)) are at most three;
4. at (7), after descent to a finite coefficient field, its underlying finite-field representation is the generic fibre of a finite flat group scheme killed by 7.

In particular, if rho is reducible over the algebraic closure, L017 gives

\[
\operatorname{tr}(rho(\operatorname{Frob}_{(29,\sqrt5-11)}))\in\{2,-2\}.
\]

This is an applicability specialization of the cited general theorems and reproduces the representation interface asserted in [Chocian, arXiv:2609.26996v1, Section 6.2, equations (33)–(37)](https://arxiv.org/html/2609.26996v1#S6.SS2). It does not establish irreducibility, exceptional-field applicability, modular-packet exhaustion or a signature exclusion.

## Proof

**Domain and normalization.** Any prime dividing two of X,Y,Z divides the third by the equation. Thus the coordinates are pairwise coprime. The substitution

\[
(a,b,c)=(X,-Z,Y),\qquad (q,p,r)=(5,7,3)
\]

gives a primitive nontrivial solution of a^q+b^p+c^r=0, including coordinates of absolute value one. Moreover

\[
t=-a^5/c^3,\qquad t-1=b^7/c^3=-Z^7/Y^3.
\]

Hence t is finite and different from 0 and 1. The sextic is squarefree in characteristic zero: its derivative is 30x^2(x^3-2x^2+t). A common root x=0 would force t=0. For x nonzero, substituting t=x^2(2-x) into the sextic gives 4x^4(-x^2+x+1). A common root therefore has x^2=x+1 and consequently t=1. The smooth projective curve has genus two and its Jacobian has its canonical polarization.

The geometric identification used throughout is [Pacetti–Villagra Torcomian (PVT), arXiv:2512.17845v1, Sections 2.2 and 7.1, equation (32)](https://arxiv.org/html/2512.17845v1#S7.SS1): this Jacobian is the plus Euler-curve quotient, with real multiplication by F defined over F. Section 2.2 gives the O_F action on the new component; in this genus-two quotient there is no old component. These cited construction results are not independently recomputed here. An embedding of F into End_F(J) tensor Q is enough; no assertion that every special fibre has exactly this endomorphism algebra is needed.

We take the covariant Tate module of this polarized GL_2(F)-type abelian variety, not the raw hypergeometric normalization. PVT Remark 2.2 and [Golfieri Madriaga–Pacetti (GP), arXiv:2412.08804v2, Remark 6](https://arxiv.org/html/2412.08804v2#S2.SS3) specify the weight-two Tate adjustment. The geometric realization fixes that adjustment once. In particular, no argument below twists an already finite-flat residual representation and assumes that finite flatness is preserved.

The polynomial x^2-x-1 has no root modulo 7, and its discriminant is 5. Thus (7) is inert and unramified in F, O is unramified of degree two over Z_7 and k=F_49. The Tate lattice with its integral real multiplication is free of rank two over O. Working over k and then its algebraic closure retains both coefficient embeddings; restricting the coefficients to F_7 is unnecessary.

**Determinant.** Apply [Billerey–Chen–Dieulefait–Freitas, arXiv:2205.15861v5, Theorem 2.8](https://arxiv.org/html/2205.15861v5#S2): a polarized abelian variety of GL_2(F)-type over a totally real field, with F totally real, has cyclotomic determinant on each coefficient-prime Tate component. Here both fields are Q(sqrt(5)), and J has the canonical polarization. Reduction and semisimplification preserve determinant. This proves det(rho)=chi_7 without invoking modularity or residual irreducibility.

**The finite-flat lattice and every case at 7.** Use [GP, Theorem 4.3 and its proof, printed pp. 17–18](https://arxiv.org/pdf/2412.08804v2#page=17), with coefficients A=B=C=1 and its all-distinct family i=4, plus sign. Its odd-prime and coefficient conditions hold because 7 does not divide 2ABC. The supporting proof works on the torsion of the geometric Euler Jacobian; this is the finite-flat statement for the geometric normalization, rather than a consequence of finite image for the raw motive.

The Euler model in that proof has q=5,r=3,s=1, hence covering degree 15 and exponents (2,-8,8,-3), precisely the model used in PVT Section 7.1. Its new component and the quotient defining J are obtained through averaging for the covering action and the two involutions. The relevant averaging denominators divide powers of 15 and 4, hence are units at 7. Equivalently, pullback and norm for the quotient compose to multiplication by four. Therefore the 7-adic geometric component of J is a direct summand of the corresponding Euler Tate module. The finite-flat torsion conclusion in GP's geometric proof passes to this component; no division by 7 or extra Tate twist is involved.

For clarity, all of its local cases occur in the present specialization. Write v=v_7 on rational numbers. Pairwise coprimality makes the following list exhaustive:

| Coordinate case | v(t) | v(t-1) | Applicable case of GP's proof |
| --- | --- | --- | --- |
| 7 does not divide XYZ | 0 | 0 | smooth specialization |
| 7 divides X | 5v(X)>0 | 0 | first-coordinate branch |
| 7 divides Y | -3v(Y)<0 | -3v(Y)<0 | third-coordinate branch |
| 7 divides Z | 0 | 7v(Z)>0 | middle-coordinate multiplicative branch |

In the last row the local parameter u_0=t-1 has valuation divisible by the residual prime 7, exactly the hypothesis used in GP's multiplicative-case argument. The other branch valuations are multiples of the orders 5 and 3. The source theorem and proof, rather than an assertion that a semistable Jacobian always has finite-flat full torsion, supply the finite-flat conclusion in this row. None of these cases requires v(X),v(Y),v(Z) to be bounded or equal to one.

We may use the resulting geometric lattice before semisimplifying. The semisimplification has the same finite-flat property: for a finite flat commutative group scheme over a discrete valuation ring, a subgroup of the generic fibre extends by schematic closure to a finite flat subgroup, and its quotient is finite flat. Iterating along a composition series and taking the direct sum of these quotients realizes the semisimplification. This is the usual subgroup/quotient property in the finite-flat category; closure is flat here because its finite coordinate algebra is torsion-free over the discrete valuation ring. A composition series defined over a finite coefficient extension suffices. Thus the underlying F_7 module of rho has the property required in L017. By the Brauer–Nesbitt lattice-independence theorem, semisimplified residual representations of a fixed characteristic-zero representation are independent of the stable lattice, so this choice does not change rho or its traces.

**Ramification away from 7.** [GP, Theorem 4.2](https://arxiv.org/html/2412.08804v2#S4) and [PVT, Theorem 2.1(3)](https://arxiv.org/html/2512.17845v1#S2.SS3) give unramifiedness outside 3,5,7, including the even prime for the plus realization. A Tate normalization does not alter this assertion: at any finite prime away from 7 the 7-adic cyclotomic character is unramified. The signed substitution already checked meets the source domain. Passing to semisimplification preserves unramifiedness.

**Conductor bounds without irreducibility.** The compatible-system exponents are at most three at (3) and (sqrt(5)), by [PVT, Corollary 3.6/Table 3.2 and Proposition 3.14/Table 3.5](https://arxiv.org/html/2512.17845v1#S3). The bounds cover every coordinate-divisibility row. They do not use Theorem 7.8, which would require residual irreducibility. The geometric normalization has identical conductors at these primes because the normalizing twist is unramified there.

Here is the required reduction argument. Let V be the local E-representation, T a stable O-lattice and I inertia at either of these primes. The fixed lattice T^I=T intersect V^I is saturated in T. Consequently

\[
T^I/7T^I\ \hookrightarrow\ (T/7T)^I
\]

is injective, so the dimension of invariants cannot decrease on reduction. This proves that the tame contribution dim(V)-dim(V^I) cannot increase.

Wild inertia has finite image of order a power of the local residue characteristic, which is 3 or 5 and hence prime to 7. To see finiteness, intersect its compact image with an open pro-7 congruence subgroup in GL_2(O); that intersection is trivial. For every wild ramification subgroup, averaging over its finite image defines an integral invariant projector, since its order is invertible in O. Reduction preserves the rank of each such projector, so the codimensions used in the Swan conductor are unchanged. Summing with the same ramification weights gives equality of the characteristic-zero and residual Swan conductors. Combining tame and wild parts yields

\[
a(T/7T)\leq a(V)\leq3.
\]

Finally semisimplification cannot increase conductor: invariants of an extension have dimension at most the sum of invariant dimensions of its two factors, and the wild averaging projectors make the Swan conductor additive. Applying this along a composition series proves a(rho)<=3. This argument works for reducible and irreducible residual modules alike.

All four hypotheses have now been established for the same geometric residual representation. If it is reducible, apply L017 at the specified prime of norm 29 to obtain the displayed trace restriction. No use of the exceptional polynomial, the four finite parameters or an irreducible modular-packet list entered the proof.

**Scope and verification.** The check is a REPRODUCTION under the saved SPECIALIZE assessment. The finite-flat and geometric-realization theorems remain named imported inputs; their general proofs and quotient computations are not independently verified. The local valuations, domain, normalization compatibility and conductor-reduction argument above are the specialized audit. The achieved threshold is applicability of a conditional character lemma to original solutions. The required Beal threshold is zero positive primitive solutions for every residual signature, which this result does not reach.

## Mathlib

Coverage of the full applicability statement and its supporting Jacobian real multiplication, finite-flat, determinant and Artin-conductor results: **not checked**. PVT, GP and BCDF above provide supporting named results. Chocian Section 6.2 matches the interface claim being reproduced, not a verified complete signature exclusion. No matching Mathlib declaration, formal verification or progress beyond the checked literature is claimed.
