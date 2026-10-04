# L008 — Canonical-beta rounding fails at the unit scalar

## Hypotheses

Let pi = sqrt(2), K = Q_2(pi), O = O_K and sigma(pi) = -pi. Normalize v_2(2) = 1 and |x|_2 = 2^(-v_2(x)). Tensor products of fields are over Q_2 and of lattices over Z_2. Put

I_K = (1/4) log(O^times), L = K tensor K, I = I_K tensor I_K,

T = O tensor O, J = log(O^times) tensor log(O^times), a = 1,

beta = 1 tensor 2pi, gamma = a beta^(-1) = 1 tensor (pi/4).

Identify L with K direct sum K by Phi(x tensor y) = (xy, x sigma(y)), and its maximal order O_L with O direct sum O. Let G = Aut(L : I) consist of all Q_2-linear extensions of Z_2-lattice automorphisms of I. For a subset X of L, G X means the union of g(X) over g in G, and hull(X) is the product of the smallest closed K-balls centered at zero containing its two component projections.

These are the log-shell normalization, automorphism group and component hull of [Dupuy–Hilado, arXiv:2004.13108v2, Definition 4.3.1 and §§6.1–6.3, printed pp. 17–22](https://arxiv.org/pdf/2004.13108v2#page=17). The two beta constraints, beta O_L subset T and component valuation v_2(beta) = 3/2, are verified in L007 and retained here. The scalar a = 1 is used away from the selected bad places in §6.3; it is outside §6.2's strict hypothesis |a|_2 < 1. This lemma tests the displayed rounding comparison extended to that scalar. It does not assert that this packet arises in original initial theta data or that G is the full original indeterminacy family.

## Conclusion

The rounded exponent is floor(v_2(a) - v_2(beta)) = -2. Nevertheless,

G(gamma I) = I/8, whereas G(I/4) = I/4.

Their component hulls are respectively

hull(G(gamma I)) = (1/64) O_L and hull(G(I/4)) = (1/32) O_L.

Thus the proposed rounded orbit-hull containment fails, with radii (64,64) instead of (32,32), even for the fixed canonical last-factor beta. An explicit witness is g(gamma e3) = e4/8 = (1/64,-1/64), where e1,e2,e3,e4 are the I-basis below and g swaps e1 and e4.

Before saturation, hull(gamma I) = (pi/32) O_L is contained in (1/32) O_L: its component radii are 2^(9/2) < 32. The failure therefore occurs when passing this component-hull comparison through arbitrary I-preserving automorphisms.

This conclusion concerns the auxiliary enlarged lattice gamma I. It does not show that the smaller (6.4) input beta^(-1) T union J has an image outside the rounded hull, that Lemma 6.3.1's final enclosure fails, or that the [native preserved-lattice enclosure](../foundations/04-native-local-enclosures.md) fails. It establishes no essential IUT flaw and no comparison of the actual normalized A and B.

## Proof

### Reuse of the exact lattice and admissibility

L007 establishes, independently of its choice of a,

I_K = Z_2 + (pi/4) Z_2, J = 16 I,

e1 = (1,1), e2 = (pi/4,pi/4), e3 = (pi/4,-pi/4), e4 = (1/8,-1/8),

and hull(I) = (1/8) O_L. It also checks both source constraints for beta = (2pi,-2pi), using the known monogenic different formula and the exact conductor of T. Those inputs are reused rather than rederived. In particular T subset I and beta J subset I, so the preceding inclusion beta^(-1) T union J subset gamma I remains valid when a = 1. This inclusion alone cannot transfer a counterexample from the larger set to the smaller one.

### Changed-scalar multiplication and full orbit

Since pi^2 = 2, multiplication by gamma = (pi/4,-pi/4) sends

e1 to e3, e2 to e4, e3 to e1/8, e4 to e2/8.

Its matrix in the ordered I-basis is

```text
0  0  1/8  0
0  0  0    1/8
1  0  0    0
0  1  0    0
```

Consequently M = gamma I is contained in I/8 and contains e1/8. Every g in G preserves I/8, so G M subset I/8. Conversely, any nonzero x in I/8 is 2^k w/8 for k >= 0 and w primitive in I. The primitive-vector argument proved in L007 gives a g in GL_4(Z_2) with g(e1) = w. Since 2^k e1/8 lies in M, x lies in G M. Zero also lies in M. This proves G M = I/8 for the whole group, without enumerating or sampling automorphisms. Lattice preservation gives G(I/4) = I/4.

### Exact component hulls and witness

For a rational scalar 2^n, the definition of the component hull and hull(I) = (1/8) O_L give hull(2^n I) = (2^n/8) O_L. The two saturated hulls are therefore (1/64) O_L and (1/32) O_L. In particular the required threshold is radius 32 in each K component, while the exact orbit reaches radius 64.

Let g interchange e1 and e4 and fix e2 and e3. It is a Z_2-lattice automorphism of I with an invertible Q_2-linear extension. Applying it to gamma e3 = e1/8 gives e4/8 = (1/64,-1/64). Both components have valuation -6, smaller than the rounded hull's minimum valuation -5; hence the witness lies outside that hull.

Without saturation, multiplication by gamma scales both component radii of I by 2^(3/2). Equivalently, it sends the component ideal (1/8) O to (pi/32) O up to sign. This gives minimum component valuation -9/2, greater than -5, and proves the stated unsaturated containment. Coordinate containment between these unsaturated hulls does not imply the saturated comparison.

### Scope and verification

The strict §6.2 statement at |a|_2 < 1 is not refuted by this unit-scalar example. The local test instead checks the rounding transition used when that computation is extended to the scalar appearing in §6.3. Fixing the canonical beta removes L007's particular favorable-choice escape for this test, but failure for this enlarged lattice still leaves the source's smaller input and final container to examine. No full IUT instance or essential dependence of the original comparison on this transition has been established.

The source assessment already reads the closest known shell-preservation result, [Mochizuki, November 2022 RIMS1968, Example 3.5.1(i), printed p. 100](https://www.kurims.kyoto-u.ac.jp/preprint/file/RIMS1968.pdf#page=101). That elementary statement preserves the shells of a fixed Z_p-lattice; it does not identify this enlarged lattice's orbit or its component hull. The native enclosure is imported by its named citation on its own input a O_L, without reproof. Neither known result supplies the disputed sharper comparison.

`PYTHONDONTWRITEBYTECODE=1 python3 scripts/tensor-hull/check_good_place.py` verifies the exact multiplication matrix, both component minima, the inverse relation beta gamma = 1 and the explicit witness. Its [output](../scripts/tensor-hull/good-place-result.json) uses exact fractions. L007 supplies the analytic logarithm argument; the proof above, not the finite checks, supplies the infinite orbit.

Classification: **POTENTIALLY_NEW** only in the bounded-search sense of the prior assessment. The known lattice/admissibility inputs are reused and standard shell preservation and native enclosures remain citation inputs. The changed-scalar calculation verifies a suspect auxiliary transition; no inspected source supplies this exact failure, and no certified originality or essential IUT flaw is claimed.

## Mathlib

Full unit-scalar canonical-beta tensor-orbit statement: **not checked**. Supporting p-adic logarithm, different, tensor decomposition, primitive-vector and lattice-automorphism coverage: **not checked**. The direct primary citations above support the setup and distinguish named supporting results from a match for the full statement; they are not claims of formal verification or absence from Mathlib.
