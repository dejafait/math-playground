# C003a — An algebraic Fermat graph outside the diagonal span

## Hypotheses

Let S be the Fermat quartic surface

\[
x_0^4+x_1^4+x_2^4+x_3^4=0\quad\text{in }\mathbb P^3_{\mathbb C},
\]

let X = S x S, and let g be its algebraic automorphism

\[
g(x_0:x_1:x_2:x_3)=(i x_0:x_1:x_2:x_3).
\]

Let z be the cohomology class of the graph of g inverse, with the graph convention Gamma_f = {(s,f(s)): s in S}. Use N, T, E, D^2(X), Phi, and the ample class H from L003.

## Conclusion

The class z is rational and algebraic, but

\[
z\notin D^2(X)+\mathbb Q[\Delta_S].
\]

Thus dim_Q E is at least two, and the residual quotient in L003 has dimension at least one. Subtracting a rational divisor-product class from z gives an algebraic H-primitive representative with the same nonzero residual class. This disproves the assertion that divisor products and the diagonal universally span Hodge classes on quartic self-products. It is not a counterexample to the Hodge conjecture, and no exact dimension or full spanning claim for this Fermat example is needed.

## Proof

The Fermat surface is smooth: simultaneous vanishing of its four partial derivatives would force all homogeneous coordinates to be zero. The map g preserves its equation and has an algebraic inverse, so its inverse graph is an algebraic codimension-two subvariety of X. Its fundamental class is integral, hence rational. The use of the coefficient i in the equation for the automorphism does not change the coefficient field of singular cohomology.

**The action on the holomorphic two-form.** Put F = sum x_j^4 and

\[
\Omega=\sum_{j=0}^3(-1)^j x_j\,
dx_0\wedge\cdots\wedge\widehat{dx_j}\wedge\cdots\wedge dx_3.
\]

The degree-zero homogeneous form Omega/F descends to a rational three-form on projective space with a simple pole along S. By the residue form of adjunction its residue omega is a global holomorphic two-form on S. It is nonzero: on the chart x_3 = 1, where u_2 is nonzero, its expression up to a fixed sign is du_0 wedge du_1 divided by 4u_2^3. Smoothness gives such local residue expressions and their gluing; adjunction gives the one-dimensional space H^(2,0)(S).

Each summand of Omega is multiplied by i under g, while g^*F = F. Functoriality of the residue therefore gives

\[
g^*\omega=i\omega.
\]

One can also check the factor directly in the displayed affine expression. This standard residue description for this very surface is recorded in Shigeru Mukai, *Lecture notes on K3 and Enriques surfaces*, notes by Slawomir Rams, [Example 3.3, p. 4](https://www.impan.pl/~pragacz/mukai2.pdf#page=4). The source supports the form and automorphism calculation; the quotient assertion is proved using L003.

Automorphisms preserve both the cup-product pairing and the rational divisor subspace N, so g^* preserves T and is a rational Hodge endomorphism. Also omega belongs to T_C because it pairs trivially with every (1,1)-class.

**The graph convention and the separation.** For any algebraic automorphism f, write j_f(s) = (s,f(s)). The projection formula gives

\[
T_{[\Gamma_f]}(v)
=(\pi_2)_*\bigl(\pi_1^*v\smile(j_f)_*1\bigr)
=(\pi_2j_f)_*(j_f^*\pi_1^*v)=f_*v.
\]

For an isomorphism f, pushforward on cohomology is (f inverse)^*. With f = g inverse, this yields Phi(z) = g^* restricted to T. Its complexification takes omega to i omega. A rational scalar multiple r id_T would instead take omega to r omega, which is impossible since omega is nonzero and i is not rational. Hence Phi(z) is not in Q id_T. The inverse-image identity in L003 proves z is outside D^2(X) + Q[Delta_S]. The maps id_T and Phi(z) are rationally linearly independent, proving the dimension lower bounds.

Finally, L003 decomposes z uniquely as d + k with d in D^2(X) and k in the rational (2,2)-part of T tensor T. The class d is algebraic, so k = z-d is algebraic. L003 makes k H-primitive. Since subtracting d does not change its class modulo D^2(X) + Q[Delta_S], this primitive representative still has nonzero residual class. No Picard-rank calculation, description of all endomorphisms, or nonalgebraicity assertion enters the argument.

## Mathlib

Coverage of the full statement: **not checked**. No full or supporting Mathlib match, and no absence from Mathlib, is claimed. The direct Mukai reference above supports the residue and symmetry calculation, not the full quotient conclusion. The needed quotient and primitive-representative statements are the mathematical input L003.
