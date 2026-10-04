# L009 — The smaller good-place input has a sharp contained orbit

## Hypotheses

Let pi = sqrt(2), K = Q_2(pi), O = O_K and sigma(pi) = -pi. Normalize v_2(2) = 1 and |x|_2 = 2^(-v_2(x)). Field tensors are over Q_2 and lattice tensors over Z_2. Put

I_K = (1/4) log(O^times), L = K tensor K, I = I_K tensor I_K,

T = O tensor O, J = log(O^times) tensor log(O^times), a = 1,

beta = 1 tensor 2pi, gamma = beta^(-1) = 1 tensor (pi/4).

Use Phi(x tensor y) = (xy, x sigma(y)) to identify L with K direct sum K, and O_L with O direct sum O. Let G = Aut(L : I) be the Q_2-linear extensions of all Z_2-lattice automorphisms of I. For X subset L, G X is the union of g(X) over g in G. The component hull is the product of the smallest closed K-balls centered at zero containing the two component projections.

These definitions and the literal smaller input beta^(-1) T union J are from [Dupuy–Hilado, arXiv:2004.13108v2, Definition 4.3.1 and (6.4)–(6.7), printed pp. 17–20](https://arxiv.org/pdf/2004.13108v2#page=17). L007 supplies the exact logarithm lattice, tensor decomposition and both conductor-based beta constraints. The scalar a = 1 is outside §6.2's strict hypothesis |a|_2 < 1 and is used at other places in §6.3; this is the screened local extension, with no assertion of original initial theta data or of the full original indeterminacy family.

## Conclusion

The literal smaller-input orbit is exactly

G(beta^(-1) T union J) = I/2.

Consequently

hull(G(beta^(-1) T union J)) = (1/16) O_L subset (1/32) O_L = hull(I/4).

The achieved component radii are exactly (16,16), half of the required (32,32). They are attained by the image of beta^(-1)(1 tensor pi) under the basis swap e1 <-> e4 described below. Thus the failed enlarged-lattice rounding does not produce a smaller-input counterexample in this packet: the smaller input satisfies the desired rounded containment for every g in G.

This does not prove the bound for other packets, a final all-image enclosure, the native initial-data hypotheses, or finite B >= A. It demonstrates no essential IUT flaw.

## Proof

### Reused lattice and the exact smaller input

L007 establishes

I_K = Z_2 + (pi/4) Z_2, J = 16 I,

e1 = (1,1), e2 = (pi/4,pi/4), e3 = (pi/4,-pi/4), e4 = (1/8,-1/8),

and hull(I) = (1/8) O_L. It also establishes O = Z_2 + pi Z_2 and the admissibility of beta = (2pi,-2pi). These analytic and conductor inputs are reused, not reproved.

The elementary tensor basis of T is 1 tensor 1, pi tensor 1, 1 tensor pi, pi tensor pi. In the displayed I-basis it is respectively

e1, 4e2, 4e3, 16e4.

Multiplication by gamma = (pi/4,-pi/4), using pi^2 = 2, sends

e1 to e3, e2 to e4, e3 to e1/8, e4 to e2/8.

Therefore M = beta^(-1) T has the exact Z_2-basis

e3, 4e4, e1/2, 2e2.

In particular M subset I/2 and e1/2 belongs to M. Also J = 16 I subset I/2. Both branches of the literal union thus satisfy genuine lattice inclusion before applying any automorphism. In fact J subset M: its four generators 16e1, 16e2, 16e3, 16e4 are respectively 32(e1/2), 8(2e2), 16e3, 4(4e4). This verifies the union explicitly; it is not replaced by an unexamined enlarged lattice.

### Whole-group saturation

Every g in G preserves I/2, by Q_2-linearity and preservation of I. Hence

G(M union J) subset I/2.

For the reverse inclusion, any nonzero x in I/2 can be written x = 2^k w/2 with k >= 0 and w primitive in I. To see this, write x = z/2 with z in I and take k to be the minimum valuation of the four nonzero I-coordinates of z. At least one coordinate of w = z/2^k is a unit. L007's elementary primitive-vector argument gives a lattice automorphism g with g(e1) = w: a unit coordinate permits invertible row operations over Z_2 that extend the vector to a basis. Since 2^k e1/2 belongs to M, its image x lies in G M. Zero also belongs to M. Thus

G M = I/2, and G(M union J) = I/2.

This proves the assertion for the whole automorphism group; no finite sampling is used.

### Component hull, required threshold and sharpness

Scaling the known component hull of I by the rational scalar 1/2 gives

hull(I/2) = (1/16) O_L.

Likewise hull(I/4) = (1/32) O_L. Both components of beta have valuation 3/2, so the source's rounded exponent at a = 1 is floor(0 - 3/2) = -2 and its rounded lattice is I/4. The attained radius 16 is smaller than the required upper radius 32; equivalently the attained minimum component valuation -4 is greater than the permitted minimum -5. Thus this is a strict containment, not a weakening of the required bound.

For a sharp point, 1 tensor pi = 4e3 belongs to T and

beta^(-1)(1 tensor pi) = e1/2.

Let g swap e1 and e4 and fix e2 and e3. This is a Z_2-lattice automorphism, and

g(beta^(-1)(1 tensor pi)) = e4/2 = (1/16,-1/16).

Both components have absolute value 16, proving sharpness. Unlike the enlarged-lattice witness, its source point is in T itself.

### Scope, literature comparison and verification

The prior SPECIALIZE assessment singles out this literal smaller-input verification because the source reaches its claimed bound through the larger beta^(-1) I. That larger set's failure cannot be transferred to a subset. Here a genuine inclusion in I/2 proves the desired smaller-input bound independently of that transition. The justification is needed to verify the suspect deduction, rather than to duplicate a theorem whose exact fixed-packet conclusion was already independently established in the assessment.

The known native estimate, IUT IV Proposition 1.2(ii) with Proposition 1.4(iii), remains a named citation input in [the native enclosure record](../foundations/04-native-local-enclosures.md), on its own maximal-order input. The shell-preservation statement in [Mochizuki, November 2022 RIMS1968, Example 3.5.1(i), printed p. 100](https://www.kurims.kyoto-u.ac.jp/preprint/file/RIMS1968.pdf#page=101) is supporting context; it does not compute the position of the smaller region. Neither theorem is reproved or treated as a match for the exact sharp orbit here.

`PYTHONDONTWRITEBYTECODE=1 python3 scripts/tensor-hull/check_smaller_input.py` verifies the multiplication on the actual tensor-order basis, both branch inclusions, the rounded and attained component minima and the sharp smaller-input witness. Its [output](../scripts/tensor-hull/smaller-input-result.json) uses exact fractions. The analytic lattice input and universal orbit argument, not the finite checks, establish the infinite assertions.

Classification: **REPRODUCTION**. This is a direct specialization verifying the source's claimed smaller-input containment, with a sharp packet calculation that the assessment did not independently match to a theorem. It is not an imported exact orbit theorem or a claimed discovery beyond the checked literature. No originality, final-enclosure failure or original IUT flaw is claimed.

## Mathlib

Full smaller-input sharp-orbit statement: **not checked**. Supporting p-adic logarithm, tensor decomposition, primitive-vector and lattice-action coverage: **not checked**. The named primary sources above distinguish supporting definitions and results from a match for the full statement; no absence from Mathlib or formal verification is asserted.
