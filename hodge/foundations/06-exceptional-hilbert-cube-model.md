# The exceptional Hilbert-cube moduli model

Source statement and proof read on 2026-10-03. This is a known
input imported by citation in a literature-only turn.

## Hypotheses

Let S be a smooth projective complex K3 surface. Write omega
for its fundamental class and v_0=v(O_S)=1+omega. Let l>=2
be an integer. Let H be a general ample polarization in the
sense of Yoshioka's section 0.2, and let M_H(v) denote
Gieseker-stable torsion-free sheaves with Mukai vector v.
Retain that polarization hypothesis.

## Conclusion

Yoshioka's Proposition 3.4 states, for rank(v_0)=1, that

\[
M_H(lv_0-(l+1)\omega)\simeq S^{[l+1]},
\]

and that the Mukai homomorphism theta_v is a Hodge isometry.
For l=2 this is the global model M_H(2,0,-1) isomorphic to
S^[3], including its nonreduced boundary. This is theorem
applicability, with no RM or Picard-rank-one restriction.

## Proof

Import [Kota Yoshioka, *Irreducibility of moduli spaces of vector
bundles on K3 surfaces*, arXiv:math/9907001v2, 7 February 2000,
Proposition 3.4 and proof, equations (3.42)--(3.47), PDF
p. 16](https://arxiv.org/pdf/math/9907001v2#page=16), with
[the general-polarization setup, PDF p. 2](https://arxiv.org/pdf/math/9907001v2#page=2).
The proof constructs a global isomorphism using a contravariant
reflection-and-dual functor, rather than only a birational map.
No reproof is made here. Compatibility with L039's weighted
support morphism is a separate application not established
in this source note. The theorem does not construct a map
S -> S^[3] with non-scalar cubic-RM action.

## Mathlib

Coverage: **not checked** for this full theorem or its moduli,
reflection-transform and Mukai-map inputs. The named primary
statement matches the global moduli model; it is not a Mathlib
match or a theorem about an independent non-scalar support map.
