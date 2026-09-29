# L028 — Integral Chern classes exclude the minimal cubic resolution

## Hypotheses

Let S, C in X=S x S, N=NS(S)_Q, U, A and omega be as in L027.
In particular A is q-self-adjoint with characteristic polynomial
z f(z), where

\[
f(z)=z^3+z^2-2z-1,\qquad A\omega=\lambda\omega,
\qquad f(\lambda)=0.
\]

Write W=im(A), K=ker(A), and pi_W, pi_K for the rational orthogonal
projections. Thus N=W perpendicular direct sum K, with dimensions
three and one. Both factors use L025's same metric and the diagonal
SU(2) action. No integrality of L025's chamber conjugation is assumed.

Suppose there is an actual exact sequence

\[
0\longrightarrow\mathcal E\longrightarrow P_2\longrightarrow P_1
\longrightarrow P_0\longrightarrow I_C\longrightarrow0,
\qquad
P_i=\bigoplus_j L_{ij},                                      \tag{1}
\]

where \(\mathcal E\) is locally free of positive rank r and each product line
bundle has

\[
c_1(L_{ij})=p_1^*a_{ij}+p_2^*b_{ij},\qquad a_{ij},b_{ij}\in W.
\]

Let M be any actual holomorphic line bundle on X and put
\(\mathcal F=\mathcal E\otimes M\). In Chern expressions the plain
F denotes this bundle; F,O,E,P in the divisor basis below retain
their meanings as divisor classes.

## Conclusion

The classes c_1(F) and c_2(F) cannot both be SU(2)-invariant.
Consequently no sequence (1) and integral terminal twist satisfy
the saved stable-bundle target. This exclusion does not require
stability or any hypotheses on the section maps beyond (1).

It holds for every rational chamber conjugation allowed in L025,
every positive rank and every integral twist. It concerns the fixed
three-presentation recipe with original factor classes in W and
transcendental ch_2 action U. It makes no assertion about recipes
with a different transcendental coefficient, or about the universal
Hodge conjecture. No transverse representative is constructed: the
known span remains 21-dimensional and the attained RM directions
remain three against four required.

## Proof

**Scope and known inputs.** This is a reproduction/application of
integral Chern-class theory, the integral Kunneth theorem, Lefschetz
(1,1), and elementary linear algebra for an alternating form.
The invariant-form input is the same one inspected for L027:
Verbitsky, *Hyperholomorphic bundles*,
[Proposition 1.2 and Lemma 2.1, arXiv:alg-geom/9307008v1,
pp. 4 and 7](https://arxiv.org/pdf/alg-geom/9307008v1#page=7).
The conditional stable-bundle criterion in
[Theorem 2.5, p. 9](https://arxiv.org/pdf/alg-geom/9307008v1#page=9)
does not construct the required invariant Chern classes.
The saved EXPLORE assessment did not match this full exclusion to
a source; no originality is claimed. The new notebook consequence
is the obstruction for the exact surviving W recipe.

**The forced rational operator.** Suppose both Chern classes are
invariant. Set

\[
\nu(\mathcal F)=\operatorname{ch}_2(\mathcal F)
                         -\frac{c_1(\mathcal F)^2}{2r}.
\]

This class is invariant, since it equals
(r-1)c_1(F)^2/(2r)-c_2(F). It is unchanged by the line-bundle twist.
For a mixed tensor x tensor y use the correspondence convention
v -> q(v,x)y.

L027's Chern and minimal-subspace arguments, which use invariance
but not stability, apply to (1) with m=3 and e=1. They give

\[
T_{\nu(\mathcal F)}|_N
 =2\,\mathrm{id}+(A-2\,\mathrm{id})\pi_W
 =A+2\pi_K.                                                \tag{2}
\]

They also give, on writing the integral first Chern class as

\[
c_1(\mathcal F)=p_1^*\alpha+p_2^*\beta,
\qquad \alpha,\beta\in\operatorname{NS}(S),
\]

that alpha,beta lie in K. Indeed their W projections are rational
classes orthogonal to omega; L027 proves that only zero has this
property in W. This is separate orthogonality in each factor,
not just degree zero on X.

The mixed part of c_1(F)^2/(2r) is alpha tensor beta divided by r.
Because K is a nondegenerate line and alpha,beta lie in it, its
operator is zero on W and is q(alpha,beta)/r times the identity
on K. Thus

\[
D:=T_{\operatorname{ch}_2(\mathcal F)}|_N
 =A+\gamma\pi_K,\qquad
\gamma=2+\frac{q(\alpha,\beta)}r,\qquad
\det(z-D)=f(z)(z-\gamma).                                  \tag{3}
\]

Both summands in D are q-self-adjoint. In particular the possibly
different alpha and beta cause no asymmetry: they are proportional
on the one-dimensional K. Equation (3) has so far only been a
rational statement. We do not reduce A or pi_K modulo 2.

**The operator D is integral.** Integral Kunneth for a K3 self-product
gives a direct mixed summand
H^2(S,Z) tensor H^2(S,Z) in H^4(X,Z). K3 cohomology is torsion-free
and its odd groups vanish. The Chern-class identity gives

\[
\bigl(\operatorname{ch}_2(\mathcal F)\bigr)_{\rm mixed}
 =\alpha\otimes\beta-\bigl(c_2(\mathcal F)\bigr)_{\rm mixed}.
                                                               \tag{4}
\]

Both terms on the right are integral. Pairing with an integral
H^2 class therefore defines an integral endomorphism of H^2(S,Z).
Moreover ch_2(F) has Hodge type (2,2), so this endomorphism preserves
Hodge type on H^2. Lefschetz (1,1) identifies the integral (1,1)
classes with NS(S), proving that D preserves the actual integral
divisor lattice. No integral NS/T splitting is needed.

In an integral divisor basis D has an integer matrix. Since
tr(A)=-1, equation (3) implies gamma=tr(D)+1 is an integer.
This use of (4) is specific to the mixed component on this product;
it does not assert that ch_2 of every bundle on every variety is
integral. Nor is the rational class nu being declared integral.

**Reduction of the divisor lattice.** The integral-basis computation
in L020 identifies NS(S) with the lattice generated by F,O,E,P.
Its Gram matrix, as displayed in L025, is

\[
G=\begin{pmatrix}
0&1&0&1\\
1&-2&0&0\\
0&0&-2&1\\
1&0&1&-2
\end{pmatrix},\qquad \det(G)=-7.                            \tag{5}
\]

The determinant is odd and the lattice is even. Consequently the
induced pairing on V=NS(S)/2NS(S) is nondegenerate and alternating,
of dimension four over F_2. Self-adjointness and integrality of D
give a self-adjoint endomorphism D-bar of this space. From (3),

\[
\det(z-\bar D)=\bar f(z)(z-\bar\gamma),\qquad
\bar f(z)=z^3+z^2+1.                                       \tag{6}
\]

The cubic has no root over F_2, since its values at both 0 and 1
are 1. It is therefore irreducible and coprime to z-gamma-bar.
Cayley--Hamilton and the Bezout identity for these two coprime
polynomials give the primary decomposition

\[
V=V_f\oplus V_\gamma,
\quad V_f=\ker\bar f(\bar D),
\quad V_\gamma=\ker(\bar D-\bar\gamma),
\quad \dim V_f=3,\quad\dim V_\gamma=1.                     \tag{7}
\]

For example the dimensions follow from the characteristic factors
in (6), each occurring once. This decomposition is constructed from
the integral D after reduction; it is not an assumed integral
decomposition of the rational W and K.

For x in V_f and y in V_gamma, self-adjointness gives

\[
0=\bar q(\bar f(\bar D)x,y)
 =\bar q(x,\bar f(\bar D)y)
 =\bar f(\bar\gamma)\bar q(x,y)=\bar q(x,y).
\]

Thus the two primary subspaces are orthogonal. A nonzero vector in
the one-dimensional V_gamma is also orthogonal to V_gamma because
the form is alternating. It is therefore orthogonal to all of V,
contradicting nondegeneracy. This proves the exclusion.

**Limits and verification.** The contradiction precedes section-map
construction, exactness tests and metric stability. A rational
solution of the mixed tensor equation cannot be promoted to the
Chern character of an actual terminal twist. Rational chamber
conjugation cannot evade the argument, because (4) forces D itself
to preserve NS(S). No claim that the conjugating isometry is integral
was used. Multiplying or otherwise changing the required
transcendental action is outside this fixed-coefficient exclusion;
rational algebraicity of a cycle class is not refuted by it.

Run `python3 scripts/cubic-kahler/check_cubic_parity_obstruction.py`
for an independent finite check. It verifies (5), the irreducibility
test, and exhausts all 1024 self-adjoint endomorphisms of the
four-dimensional alternating space. Neither possible polynomial
in (6) occurs. This checks finite arithmetic; the geometric
integrality and rational-operator arguments are the proof above.

## Mathlib

Coverage of the full statement: **not checked**. No Mathlib match
or absence from checked sources is asserted. The named integral
Kunneth theorem, Lefschetz (1,1), Chern-character identity,
Cayley--Hamilton theorem and polynomial Bezout identity are
supporting inputs, not a cited match for the whole statement.
The direct Verbitsky links above support only the invariant-class
framework and its conditional bundle criterion. The parity
argument and its application to the forced operator are written
out here; no library lookup is a completion requirement.
