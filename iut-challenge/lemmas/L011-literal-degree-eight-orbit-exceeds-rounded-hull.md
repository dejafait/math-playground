# L011 — The literal degree-eight orbit exceeds its rounded hull

## Hypotheses

Use L010's local packet: K = Q_2(pi), pi^8 = 2, O = O_K, v_2(2) = 1, T = O, J = log(O^times), I = J/4, a = pi and beta = 1. Let G be all Q_2-linear extensions of Z_2-lattice automorphisms of I. For a subset X of K, G X is the union of g(X) over g in G; hull(X) is the smallest closed K-ball centered at zero containing X, using |x|_2 = 2^(-v_2(x)).

These are the same source definitions and derivative-product conductor choice as before: [Dupuy–Hilado, arXiv:2004.13108v2, Definition 4.3.1 and §§6.1–6.2, printed pp. 17–20](https://arxiv.org/pdf/2004.13108v2#page=17), with beta = 1 the empty product in [Theorem 2.8.1 and Remark 2.8.2, printed pp. 9–10](https://arxiv.org/pdf/2004.13108v2#page=9). The scalar satisfies the strict local condition |a|_2 < 1, and floor(v_2(a)-v_2(beta)) = 0.

This is a finite nonempty one-factor local packet. It is not asserted to be original initial theta data, nor is G identified with the full original IUT image family.

## Conclusion

The full orbit of the literal smaller input is exactly

G(a(beta^(-1) T union J)) = G(pi O union pi J) = I/2.

Its component hull therefore violates the rounded comparison:

hull(G(pi O union pi J)) = pi^(-36) O is not contained in hull(G I) = hull(I) = pi^(-28) O.

The achieved radius is 2^(9/2), twice the required radius 2^(7/2). Equivalently, the achieved minimum field valuation -9/2 is below the required threshold -7/2. An explicit I-preserving involution sends a point in pi J to the sharp hull boundary. The same involution also sends L010's actual logarithm witness pi log(1+pi) to that boundary.

This refutes the universal local rounded-hull comparison on the screened literal input, with no intermediate enlargement or unfavorable beta choice. It does not refute the source's final container, the cited native enclosure with different corrections, or Corollary 3.12 under its original hypotheses, and does not demonstrate an essential IUT flaw.

## Proof

### Exact log image and its field-valuation minimum

L010 supplies the exact logarithm-tail ideal H = pi^9 O = log(1+pi^9 O), and representatives q_1,...,q_8 with log(1+pi^j)-q_j in H. In particular,

q_1 = pi + pi^2/2 + pi^3 + 5pi^4/4 + pi^5 + 3pi^6/2 + pi^7.

Every q_j belongs to J, since H subset J. This is an exact membership assertion: q_j = log((1+pi^j)/v_j) for a v_j in 1+pi^9 O with log(v_j) = log(1+pi^j)-q_j. Thus the rational representative q_1 may itself be used as a literal logarithm-image point.

The compact unit group has a continuous logarithm, so its additive image J is closed and stable under Z_2 multiplication. L010's reduction of all units modulo 1+pi^9 O then gives

J = sum_(j=1)^8 Z_2 q_j + H.

For y = sum_(r=0)^7 c_r pi^r, the field valuation is min_r(v_2(c_r)+r/8), because nonzero summands have distinct fractional valuation parts. Applying this to L010's eight representatives gives valuations

(-3/2, -1/2, -1/2, 1/2, 1/4, 1/2, 3/4, +infinity).

H has minimum valuation 9/8. Therefore every element of J has valuation at least -3/2, with equality at q_1; its unique lowest-valued summand is 5pi^4/4. Dividing by 4 gives the exact minimum -7/2 on I and

hull(I) = {y : v_2(y) >= -7/2} = pi^(-28) O.

J contains H and is bounded, so it is a full Z_2-lattice of rank eight. This also justifies the lattice automorphism and primitive-vector arguments below.

### Both literal branches lie in I/2

For every y in J the preceding bound gives

v_2(8pi y) >= 3 + 1/8 - 3/2 = 13/8 > 9/8.

Consequently 8pi J subset pi^13 O subset H subset J. Dividing by 4 gives 2pi J subset I, or pi J subset I/2. Also 4pi O subset H subset J, hence pi O subset I. Both branches of the literal union are thus contained in I/2. Every g in G preserves I/2, so

G(pi O union pi J) subset I/2.

This argument uses the actual logarithm image and tensor order. It does not replace either branch by beta^(-1) I.

### Entire-group saturation

Use L010's separating functional

lambda(sum_r c_r pi^r) = 2c_0 - 2c_2 - 4c_4 + 2c_5,

which satisfies lambda(I) subset Z_2. Let x_0 = pi q_1 in pi J and w = 2x_0. The exact finite identities are lambda(q_1) = -4, lambda(x_0) = 1/2 and lambda(w) = 1. The branch enclosure gives w in I; its functional value proves w not in 2I, so w is primitive in I.

The group of lattice automorphisms is transitive on primitive vectors. Indeed, in any Z_2-basis, a primitive vector has a unit coordinate. An invertible coordinate swap, multiplication by the inverse unit and elementary row subtractions take it to the first basis vector. Composing two such operations maps any primitive vector to any other.

Given any nonzero z in I/2, write z = 2^k t/2 with k >= 0 and t primitive in I, by taking the minimum I-coordinate valuation of 2z. Choose g in G with g(w) = t. Since 2^k x_0 belongs to pi J, we obtain z = g(2^k x_0). Zero also belongs to pi J. Thus G(pi J) = I/2, proving the full-orbit equality.

### Explicit involution and sharp witness

Put u = q_1/4 in I and d = u-w in I. We have lambda(u) = -1 and lambda(d) = -2. Define the Q_2-linear map

g(y) = y + lambda(y)d.

Its integral functional coefficients relative to I and d in I give g(I) subset I. Moreover

g(g(y)) = y + (2+lambda(d))lambda(y)d = y,

so g is an involution and g(I) = I. It therefore belongs to G. Since lambda(w) = 1, it sends w to u, and hence

g(x_0) = q_1/8.

The field valuation of this point is -3/2-3 = -9/2. It is in the orbit of the literal branch pi J and lies outside hull(I), whose minimum valuation is -7/2. Also L010 gives pi log(1+pi)-x_0 in pi H subset I. Applying g shows

g(pi log(1+pi)) in q_1/8 + I.

Every error in I has valuation at least -7/2, strictly greater than -9/2, so this actual logarithm witness has the same sharp image valuation. No approximate logarithm is used as an exact point without controlling its error.

Finally scaling I by 1/2 lowers its field-valuation minimum by one, and the full-orbit equality gives hull(I/2) = pi^(-36) O. All g preserve I, so hull(G I) = hull(I). This establishes both the sharp achieved hull and its factor-two failure relative to the required rounded hull.

### Source comparison, scope and verification

The prior SPECIALIZE assessment explicitly covers the same-packet full-orbit diagnostic after failure of genuine inclusion. The normalization and conductor setup are imported; L010's analytic tail and unit-generation results are reused. The difference derived here is the sharp orbit and explicit involution on the literal region, verifying the auxiliary rounded comparison independently of the already failed enlargement. The checked sources did not supply this counterexample; classification is **POTENTIALLY_NEW** only in that bounded-search sense, without certified originality.

The [native enclosure record](../foundations/04-native-local-enclosures.md) retains IUT IV Proposition 1.2(ii) and Proposition 1.4(iii) by citation, with different input and correction terms. Neither is refuted or reproved. The supporting integer-power shell-preservation statement, [November 2022 RIMS1968 Example 3.5.1(i), printed p. 100](https://www.kurims.kyoto-u.ac.jp/preprint/file/RIMS1968.pdf#page=101), does not place pi J in the required shell. The exclusion of residue characteristic 2 from the auxiliary paper's bad-place initial theta data remains as recorded in the prior scope. Initial-data realization, the actual image family, the distinguished pilot, final container and normalized B >= A remain unresolved.

`PYTHONDONTWRITEBYTECODE=1 python3 scripts/tensor-hull/check_degree_eight_orbit.py` checks the finite representatives' valuation extrema, both branch enclosures, lambda, the involution matrix and its square, and the sharp witness. Its [certificate](../scripts/tensor-hull/degree-eight-orbit-result.json) uses exact fractions. L010 supplies the infinite analytic inputs, and the proof above supplies the whole-group assertion.

## Mathlib

Full literal degree-eight sharp-orbit counterexample: **not checked**. Supporting local-field logarithm, lattice automorphism, primitive-vector and valuation coverage: **not checked**. The named primary sources and direct links above provide setup and supporting statements rather than a matching theorem for the full result. No Mathlib absence or formal verification is asserted.
