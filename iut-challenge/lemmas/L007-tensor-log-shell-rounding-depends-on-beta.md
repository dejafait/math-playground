# L007 — Tensor log-shell rounding depends on the admissible beta

## Hypotheses

Let pi = sqrt(2), K = Q_2(pi), O = O_K, and sigma(pi) = -pi. Normalize v_2(2) = 1 and |x|_2 = 2^(-v_2(x)). Tensor products of lattices are over Z_2; tensor products of fields are over Q_2. Put

I_K = (1/4) log(O^times), L = K tensor K,

I = I_K tensor I_K, T = O tensor O, J = log(O^times) tensor log(O^times), a = 1 tensor pi.

The log-shell normalization and the following automorphism group are those of [Dupuy–Hilado, arXiv:2004.13108v2, Definition 4.3.1 and §6.2, printed pp. 17–20](https://arxiv.org/pdf/2004.13108v2#page=17). Identify L with K direct sum K by

Phi(x tensor y) = (xy, x sigma(y)), and O_L with O direct sum O.

Let G = Aut(L : I) be all Q_2-linear extensions of Z_2-lattice automorphisms of I. For X subset L, write G X = union of g(X) over g in G. Define hull(X) using the two K-component absolute-value radii, as in the source's §6.1. It is not a hull in four independent rational coordinates.

Set beta_2 = 1 tensor 2pi and beta_1 = 2pi tensor 1. The subscripts specify the tensor factor carrying the different generator. These are two permitted different-based choices for this packet, not two arbitrary elements selected only by their valuations.

This is exactly the screened local packet. No hypothesis makes it an instance of original IUT initial theta data or identifies G with the complete original indeterminacy family.

## Conclusion

1. The exact lattices are

   log(O^times) = 4 Z_2 + pi Z_2, I_K = Z_2 + (pi/4) Z_2, J = 16 I.

   An I-basis in the two K components is

   e1 = (1,1), e2 = (pi/4,pi/4), e3 = (pi/4,-pi/4), e4 = (1/8,-1/8).

   Therefore hull(I) = (1/8) O_L, with component radii (8,8).

2. Both choices satisfy the two beta constraints stated following (6.4): beta_i O_L subset T, and v_2 of each component of beta_i is 3/2 = sum(diff) - max(diff), where diff = (3/2,3/2). For both choices the preceding (6.4)–(6.5) step even has the literal inclusion

   a (beta_i^(-1) T union J) subset a beta_i^(-1) I.

3. For beta_2 the rounded exponent is floor(1/2 - 3/2) = -1 and

   G(a beta_2^(-1) I) = I/2, hull(G(a beta_2^(-1) I)) = (1/16) O_L.

   Thus (6.5)–(6.6) is exact for the source's last-factor derivative choice.

4. For beta_1 the same rounded exponent gives G(I/2) = I/2, but

   G(a beta_1^(-1) I) = I/16, hull(G(a beta_1^(-1) I)) = (1/128) O_L.

   This hull is not contained in hull(G(I/2)) = (1/16) O_L. Both component radii exceed the claimed rounded radii by the factor 8. Before automorphism saturation, the two hulls are equal. Consequently the two beta constraints alone do not imply the saturated rounding transition.

The result neither refutes an existential estimate that can choose beta_2 nor challenges the [native preserved-lattice enclosures](../foundations/04-native-local-enclosures.md). It does not establish an essential IUT flaw, a counterexample to Corollary 3.12, or a normalized comparison between A and B.

## Proof

### The actual logarithm lattice

Every element of K has a unique form r + s pi with r,s in Q_2. The valuations of the two nonzero summands have distinct parity in the integer valuation v_pi = 2v_2. Thus O = Z_2 + pi Z_2, pi is a uniformizer, and the residue field is F_2. In particular O^times = U1, where Un = 1 + pi^n O.

The convergent logarithm and exponential are inverse on pi^3 O and U3, giving log(U3) = pi^3 O. Here this is an exact analytic statement, not a finite series calculation. Indeed, for t in pi^3 O, v_2(t) >= 3/2. Every logarithm term t^n/n with n >= 2 has valuation strictly greater than v_2(t), since

(n-1)v_2(t) - v_2(n) >= (3/2)(n-1) - v_2(n) > 0.

The analogous exponential difference is at least (3/2)(n-1) - v_2(n!) > 0, using v_2(n!) <= n-1. Both series converge, retain the leading-term valuation, and their inverse formal identities hold on this domain by convergence. The logarithm is also a homomorphism on U1 and commutes with sigma; these are the convergent logarithm identities. In particular log(-1) = 0, since twice this value is log(1) = 0.

Take u = 1 + pi. The quotient U1/U3 has order 4: each successive quotient U1/U2 and U2/U3 is the additive residue field. Since

u^2 = 3 + 2pi, u^2 + 1 = 4 + 2pi in pi^3 O,

and -1 is not in U3, the class of u has order 4 and generates U1/U3. Therefore the logarithm image is the sum of Z_2 log(u) and pi^3 O. This also follows directly by writing a unit as u^j v with 0 <= j < 4 and v in U3: twice log(u) lies in pi^3 O, so the Z_2 multiples add only the same two logarithm cosets.

The identity u sigma(u) = -1 implies log(u) + sigma(log(u)) = 0. Its trace is zero, hence log(u) = b pi for some b in Q_2. Moreover

2 log(u) = log(-u^2), -u^2 = 1 - 4 - 2pi.

The increment -4-2pi has v_pi = 3. The leading-term property on U3 gives v_pi(2 log(u)) = 3 and hence v_pi(log(u)) = 1. It follows that b is a Z_2 unit. Since pi^3 O = 4 Z_2 + 2pi Z_2, we obtain

log(O^times) = 4 Z_2 + pi Z_2.

Dividing by 4 gives I_K, and tensoring gives J = 16 I and the displayed I-basis. The component valuations of e1,e2,e3,e4 are respectively 0, -3/2, -3/2, -3. Z_2-linear combinations cannot have a smaller component valuation, and e4 attains -3 in both components. This proves the stated hull. In particular I_K is not an O-module: pi times pi/4 = 1/2 does not belong to I_K.

### The beta constraints and the preceding inclusion

The monogenic different formula, applied to O = Z_2[pi] and f(X) = X^2-2, gives Diff(K/Q_2) = (f'(pi)) = (2pi). This is an application of the known formula in [Dupuy–Hilado §2.2, (2.1), printed p. 6](https://arxiv.org/pdf/2004.13108v2#page=6), not a new different theorem. Its valuation is 3/2.

Every element of T has the component form (z+pi w,z-pi w) with z,w in O. Thus

T = {(x,y) in O^2 : x-y in 2pi O}.

For the converse, w = (x-y)/(2pi) is integral and z = y+pi w is integral. In particular (2pi O)^2 subset T. Conversely, if (x,y) O_L subset T, multiply by (1,0) and (0,1) to see that x and y both lie in 2pi O. Hence the conductor is exactly (2pi O)^2.

The two beta images are beta_2 = (2pi,-2pi) and beta_1 = (2pi,2pi). Each generates this conductor as an O_L ideal, verifying the required maximal-order inclusion as well as the component valuations. They correspond to omitting either tied maximal-different factor in the source's [Theorem 2.8.1 and Remark 2.8.2, printed pp. 9–10](https://arxiv.org/pdf/2004.13108v2#page=9). This calculation needs both constraints; valuations alone would not establish admissibility.

Also O subset I_K implies T subset I. On the basis (1,pi/4) of I_K, multiplication by 2pi sends 1 to 8(pi/4) and pi/4 to 1. It therefore preserves I_K as a submodule. Consequently beta_i I subset I and beta_i J = 16 beta_i I subset I. These two inclusions imply respectively a beta_i^(-1) T subset a beta_i^(-1) I and a J subset a beta_i^(-1) I. This proves the literal (6.4)–(6.5) inclusion for both choices, and applying every g preserves it.

### Saturation and the failed rounding step

In the chosen I-basis, G is GL_4(Z_2). For beta_2, a beta_2^(-1) is the rational scalar 1/2. Every g in G fixes I/2, proving the first saturation and its hull.

For beta_1 put epsilon = (1,-1). Multiplication by epsilon/2 sends

e1 to 4e4, e2 to e3/2, e3 to e2/2, e4 to e1/16.

Thus M = a beta_1^(-1) I is contained in I/16 and contains e1/16. Since G preserves I/16, G M subset I/16. Conversely any nonzero vector of I/16 can be written as 2^k w/16 with k >= 0 and w primitive in I. A primitive vector extends to a Z_2-basis: one of its coordinates is a unit, and elementary invertible row operations send it to the first standard basis vector. Hence some g in G sends e1 to w. Since 2^k e1/16 belongs to M, its image is the chosen vector. Zero is also in M. Therefore G M = I/16.

For an explicit witness, let g swap e1 and e4 and fix e2,e3. It is a lattice automorphism, and

g(a beta_1^(-1) e4) = e4/16 = (1/128,-1/128).

Each component has absolute value 128. The rounded lattice I/2 has hull (1/16) O_L and radii 16. The witness proves failure of the saturated hull containment. Without saturation, multiplication by epsilon/2 scales both component absolute values by 2, so hull(M) = hull(I/2); carrying this hull comparison through arbitrary I-preserving linear automorphisms is the invalid operation in this example.

### Scope, source comparison and verification

The literature assessment already imports the native enclosure; it is not reproved here and bounds a different input region. Our failure concerns an enlargement a beta^(-1) I with one admissible beta. Choosing beta_2 instead makes the fixed transition exact. Thus neither the source's final existential packet estimate nor the native result is disproved by this choice-dependent example.

The bad-place initial theta data of the auxiliary paper excludes residue characteristic 2 (its §1, footnote 1, printed p. 2), and §6.3 uses a = 1 at other places. The screened nonunit a at p = 2 is consequently a §6.2 local test, not an asserted actual theta-pilot factor. Any extension requires a separate applicability assessment, including the allowed scalar, local field, all-image group and normalization.

The exact finite checks are reproduced by `python3 scripts/tensor-hull/check_packet.py`; its [output](../scripts/tensor-hull/result.json) checks both conductor inclusions, the preceding branch inclusions, action matrices, component valuations and the explicit witness. The analytic logarithm calculation and complete-orbit argument above, rather than finite truncations or sampled automorphisms, establish those infinite assertions.

Classification: **POTENTIALLY_NEW** only in the bounded-search sense. The native theorem and monogenic different formula are imported; the log-shell and orbit calculations are an explicit verification/specialization. The checked assessment did not supply this beta-dependent counterexample, but no claim of certified originality or a new essential IUT flaw follows.

## Mathlib

Full beta-dependent fixed-packet statement: **not checked**. Supporting p-adic log/exp, different, tensor decomposition, GL_4 lattice-action and Haar-volume coverage: **not checked**. The direct primary references above supply source definitions and standard different/enclosure inputs, not a Mathlib match for the full statement or a claim of formal verification.
