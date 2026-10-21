# L018 — Conditional exceptional-field parameter bridge at 29

## Hypotheses

Let X,Y,Z be nonzero signed integers with gcd(X,Y,Z)=1 and

\[
X^5+Y^3=Z^7.
\]

Put Phi(T)=15T^7-35T^6+21T^5, eta=X^5/Z^7, and

\[
A_\eta=\mathbb Q[T]/(\Phi(T)-\eta),\qquad
E=\mathbb Q[T]/(T^7-483T^2+3955T-3945).
\]

Assume A_eta and E are isomorphic as Q-algebras. This is an explicit additional hypothesis; it is not established for every original solution.

The conditional restriction is claimed in Chocian, [arXiv:2609.26996v1, Section 6.2, between (37) and (38)](https://arxiv.org/html/2609.26996v1#S6.SS2). Rafik, [Preprints.org 202609.1761, version 1, Proposition 10, Table 3 and Table A1](https://www.preprints.org/manuscript/202609.1761), gives the same tables under a stronger Branch (II) hypothesis. This proof independently reconstructs the implication under the explicit hypotheses above; it does not import Branch (II), the original descent or either paper's full exclusion.

## Conclusion

The prime 29 does not divide XYZ. The well-defined reduction of eta belongs to

\[
\{10,14,24,28\}\subset\mathbb F_{29}.
\]

In that order, t0=eta/(eta-1) reduces to 14,10,25,15, the four curve parameters used in L016. This establishes only a conditional parameter restriction, not zero integer solutions of the signature or Beal.

## Proof

**Coprimality and separability.** If a prime divides two coordinates, the equation forces it to divide the third. Thus the primitive triple is pairwise coprime, and 29 can divide at most one coordinate. Since X and Y are nonzero, eta is neither zero nor one over Q. The derivative Phi'(T)=105T^4(T-1)^2 shows that Phi(T)-eta is separable over Q. All arguments below retain arbitrary positive coordinate valuations, both signs and coordinates equal to plus or minus one.

**Local root-lifting principle.** Write p=29. We use simple-root Hensel lifting and the existence and uniqueness of unramified extensions with a prescribed finite residue extension: Milne, [Algebraic Number Theory v3.08](https://www.jmilne.org/math/CourseNotes/ANT.pdf), Proposition 7.31 (p. 120) and Proposition 7.50 with proof (pp. 127–128). Over a finite unramified extension of Q_p, every simple residue root of an integral polynomial lifts uniquely to an integral root with that residue. The polynomial need not have unchanged degree after reduction.

In particular, suppose a simple residue root has Frobenius orbit length d. Lift it in the unramified extension K_d/Q_p of degree d. Its lift s lies in K_d, and Q_p(s) has residue field containing the original residue root. Therefore [Q_p(s):Q_p] is at least d and at most [K_d:Q_p]=d, so it is exactly d. The extension is unramified. Multiplication by a nonzero Q_p scalar or translation by a Q_p scalar does not change Q_p(s). Hensel uniqueness also makes conjugate roots lift equivariantly under residue Frobenius. Consequently each residue orbit supplies one unramified irreducible factor of exactly that degree. Distinct roots counted in disjoint valuation or residue clusters remain distinct. Once seven such roots have been produced for a degree-seven polynomial, they exhaust its geometric roots; no further cluster or ramified factor can remain.

For an unramified separable Q_p-algebra, its multiset of field-factor degrees is invariant under Q_p-algebra isomorphism: the isomorphism permutes the primitive idempotents and identifies the corresponding simple fields. A Q-algebra isomorphism base changes to one over Q_p, so the assumed isomorphism preserves these degrees.

**Exceptional algebra.** The exceptional polynomial g reduces to

\[
\overline g(T)=(T+4)(T^3+19T^2+18T+10)(T^3+6T^2+21).
\]

The two cubics have no roots among the 29 residues, so they are irreducible. The factors are distinct and their product is the reduction of g. In particular the reduction is squarefree. The lifting principle proves that E tensor Q_29 is the product of unramified extensions of degrees [1,3,3]. This uses neither irreducibility of g over Q nor a global field enumeration; the algebra-isomorphism hypothesis suffices.

**Finite tables and their exact verification.** In F_29 the only possible repeated roots of Phi(T)-e are T=0,1, with values e=0,1. For every e=2,...,28 the polynomial is squarefree. Its full factor-degree table, grouped by equal types, is

| Factor degrees | e |
| --- | --- |
| [7] | 2,3,5,6,8,9,13,15,18,22,26 |
| [1,2,4] | 4,11,12,17,25 |
| [2,2,3] | 7 |
| [1,3,3] | 10,14,24,28 |
| [1,1,1,2,2] | 16,19 |
| [1,1,5] | 20,21,23,27 |

For the degenerate branches the fixed reductions are

\[
\psi(T)=15T^2-35T+21,\qquad
h(V)=35+105V+126V^2+70V^3+15V^4.
\]

They are squarefree, with types [1,1] and [1,1,2], respectively, and nonzero constant terms. For every u in F_29^*, the squarefree binomial types are

| Reduction | Binomial type | Combined with fixed factor |
| --- | --- | --- |
| 21S^5-u | [1,2,2] | [1,1,1,2,2] with psi |
| 35S^3-u | [1,2] | [1,1,1,2,2] with h |
| 15S^7-u, u=6,14,15,23 | [1,1,1,1,1,1,1] | same |
| 15S^7-u, all other nonzero u | [7] | same |

Here every one of the 28 unit residues in each row family is tested; no power-class restriction from a hypothetical solution is imposed. For independent explanation of the binomial types, F_29^* is cyclic of order 28. Fifth and third powering are bijective, so after a rational root is chosen the nontrivial fifth roots of unity have orbit length ord_5(29)=2 and the nontrivial third roots have orbit length ord_3(29)=2. Seventh roots of unity are already in F_29. A seventh-power binomial either splits completely or Frobenius acts by multiplication by a nonidentity seventh root of unity, a single cycle of length seven. The split condition is u/15 in (F_29^*)^7={1,12,17,28}, giving the four displayed units.

The complete standard-library reproducer is [check_parameters.py](../scripts/mixed-seventh-certificate/check_parameters.py), run by `python3 scripts/mixed-seventh-certificate/check_parameters.py`; its output is [parameter-results.json](../scripts/mixed-seventh-certificate/parameter-results.json). This is exact residue arithmetic, without floating point or a height cutoff. For each squarefree polynomial f it computes

\[
D_d=\deg\gcd(f,T^{29^d}-T)\quad(1\le d\le\deg f).
\]

If n_e is the number of irreducible factors of degree e, the finite-field Frobenius theorem gives D_d=sum_(e|d) e n_e. Solving in increasing d determines the multiset uniquely. Each power is obtained by repeated squaring and polynomial division modulo f, and every squarefreeness gcd and the sum of all factor degrees are checked. This uses Milne, [Fields and Galois Theory v5.10](https://www.jmilne.org/math/CourseNotes/FT.pdf), Propositions 4.20 and 4.26 and Corollary 4.22 (pp. 53–55), for cyclic Frobenius and irreducible orbit lengths.

For g and the four matching ordinary polynomials, exact division separately finds a linear factor and two root-free cubics and multiplies them back to the monic polynomial. Thus the key type [1,3,3] is also checked by explicit factorizations, rather than only by the Frobenius gcd calculation. The table includes 27 ordinary cases, 84 unit cases and three fixed polynomials (g,psi,h). It reproduces the source tables without assuming them in the local transport argument.

**Case 29 divides X.** Let a=v_p(X)>0. Coprimality makes Y,Z units, and eta=p^(5a)u for a unit u in Z_p. The unscaled polynomial Phi(T)-eta has reduction T^5 psi(T). The two simple nonzero roots of psi lift to two unit roots T. For the roots close to zero, substitute T=p^a S and divide by p^(5a):

\[
21S^5-35p^aS^6+15p^{2a}S^7-u.
\]

This is integral and reduces to 21S^5-u, with five simple nonzero geometric roots. Each lifts by the principle above, producing five roots T of valuation exactly a. Their fields have degrees [1,2,2]; the other two unit roots each have degree one. These seven distinct roots exhaust Phi(T)-eta. Its local algebra therefore has type [1,1,1,2,2], contradicting [1,3,3]. Notice that applying unchanged-degree monic factorization Hensel directly to the scaled reduction would be unjustified; the simple-root argument accounts for every root instead.

**Case 29 divides Y.** Let b=v_p(Y)>0. Now X,Z are units and eta-1=-Y^3/Z^7=p^(3b)u for a unit u. Direct expansion gives

\[
\Phi(1+V)-1=V^3h(V).
\]

Thus Phi(1+V)-eta reduces to V^3 h(V). The four simple nonzero roots of h lift to roots with v_p(T-1)=0, of factor degrees [1,1,2]. Substituting V=p^b S and dividing by p^(3b) gives

\[
S^3h(p^bS)-u,
\]

whose reduction is 35S^3-u. Its three simple roots lift to roots with v_p(T-1)=b and degrees [1,2]. Again all seven roots are accounted for, and the combined type [1,1,1,2,2] contradicts the exceptional type.

**Case 29 divides Z.** Let c=v_p(Z)>0. Coprimality makes X,Y units and eta=p^(-7c)u with u a unit. Substituting T=p^(-c)S and multiplying by p^(7c) gives

\[
15S^7-35p^cS^6+21p^{2c}S^5-u.
\]

Its reduction is 15S^7-u, with seven simple nonzero geometric roots. They all lift and give all seven roots of Phi(T)-eta, each with valuation -c. The local algebra type is either seven linear factors or [7], by the complete unit table. Neither equals [1,3,3].

The contradictions eliminate every possible positive valuation of a coordinate. Hence p does not divide XYZ.

**Ordinary case and parameter conversion.** All coordinates are now p-adic units. The equation gives eta and eta-1=-Y^3/Z^7 both units, so the reduction e of eta belongs to {2,...,28}. The reduction Phi(T)-e has unchanged degree seven and is squarefree. Root lifting gives its ordinary table type for A_eta tensor Q_p. It must equal [1,3,3], so e is one of 10,14,24,28. Since e-1 is a unit, the t0 conversion is valid; direct residue division gives the asserted 14,10,25,15. This completes the conditional implication.

**Scope and remaining threshold.** This is reproduction of a source claim using independently checked field-specific arithmetic and named general inputs. The explicit exceptional-algebra isomorphism remains a hypothesis. Neither original descent applicability, modular-packet exhaustion, original representation hypotheses, pure-field elimination nor uniform residual-signature emptiness is established here. Four surviving parameters are not zero solutions, and this does not revive the stopped unrestricted congruence approach: the sieve uses an additional global algebra-isomorphism condition.

## Mathlib

Coverage of the full conditional implication: **not checked**. Coverage of supporting Hensel, unramified-extension, finite-field Frobenius and algebra base-change results: **not checked**. The Milne references above support the local transport and factor computation; [Chocian Section 6.2](https://arxiv.org/html/2609.26996v1#S6.SS2) matches the complete conditional restriction being reproduced. Rafik's Proposition 10 retains its stronger branch hypothesis. No Mathlib declaration or formal verification is asserted.
