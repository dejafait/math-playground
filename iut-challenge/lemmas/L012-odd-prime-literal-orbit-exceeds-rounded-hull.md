# L012 — The odd-prime literal orbit exceeds its rounded hull

## Hypotheses

Let K = Q_3(pi), pi^9 = 3, O = O_K and v_3(3) = 1. Use the nonempty one-factor packet T = O, J = log(O^times), I = J/6, scalar a = pi and beta = 1. Extend the convergent logarithm on principal units to O^times by log(-1) = 0. Let G consist of the Q_3-linear extensions of all Z_3-lattice automorphisms of I. For X subset K, G X means the union of g(X) over all g in G, and hull(X) is the smallest closed K-ball centered at zero containing X, for |x|_3 = 3^(-v_3(x)).

The lattice is exactly the normalization in [Dupuy–Hilado, arXiv:2004.13108v2, Definition 4.3.1, printed p. 17](https://arxiv.org/pdf/2004.13108v2#page=17). Multiplication by the Z_3-unit 2 gives J/6 = J/3 as lattices. In [Theorem 2.8.1 and Remark 2.8.2, pp. 9–10](https://arxiv.org/pdf/2004.13108v2#page=9), omitting the only field factor gives the empty derivative product beta = 1. Thus beta O subset T and v_3(beta) = sum(d_i)-max(d_i) = 0. The scalar satisfies |a|_3 < 1, and the rounded exponent floor(v_3(a)-v_3(beta)) is zero.

These are the unchanged local hypotheses approved in the prior SPECIALIZE assessment. No realization as original initial theta data, identification with the complete IUT image family, or passage to the normalized degrees A and B is assumed.

## Conclusion

The entire orbit of the two literal input branches is

G(pi O union pi J) = G(pi J) = I/3.

It therefore fails the rounded comparison:

hull(G(pi O union pi J)) = pi^(-27) O is not contained in hull(G I) = hull(I) = pi^(-18) O.

The achieved radius is 27, three times the required radius 9; the achieved minimum valuation -3 is below the required -2. An explicit I-preserving involution reaches the sharp boundary from a literal log-image point and also from the actual input pi log(1+pi).

This removes the residue-characteristic-2 restriction from the previously recorded local literal-input obstruction. It does not establish initial-data applicability, failure of the source's final container, or an essential flaw in IUT III, Corollary 3.12.

## Proof

### Field and an exact logarithm ideal

X^9-3 is Eisenstein, so K has degree nine and pi is a uniformizer. In the basis 1,pi,...,pi^8, write y = sum_(r=0)^8 c_r pi^r. The nonzero summands have distinct fractional valuation parts r/9, so

v_3(y) = min_r(v_3(c_r)+r/9).

This is nonnegative exactly when every c_r belongs to Z_3. Hence O = Z_3[pi] and its residue field is F_3. The monogenic different generator is 9pi^8, of valuation 26/9; the one-factor conductor choice still omits it and gives beta = 1.

Put U_j = 1+pi^j O and H = pi^5 O. Its minimum valuation 5/9 is strictly greater than 1/(3-1) = 1/2. The convergent logarithm and exponential are inverse bijections between U_5 and H. To check the domain explicitly, for t in H the n-th logarithm and exponential terms, n >= 2, exceed the valuation of t by at least

(5/9)(n-1)-v_3(n) and (5/9)(n-1)-v_3(n!), respectively.

Both are positive: v_3(n) <= (n-1)/2, and Legendre's formula gives v_3(n!) <= (n-1)/2. These bounds also give convergence and preservation of the leading term. The inverse formal power-series identities apply on this domain. In particular log(U_5) = H subset J.

The residue units are +/-1 and have logarithm zero. Every other unit reduces to U_1 after multiplication by one of these signs. For 1 <= j <= 4, the quotient U_j/U_(j+1) is the additive F_3, with generator the class of 1+pi^j. Removing these four successive classes expresses every unit as

u = (-1)^epsilon product_(j=1)^4 (1+pi^j)^(epsilon_j) times v,

where epsilon_j belongs to {0,1,2} and v belongs to U_5. The logarithm is a continuous homomorphism on U_1. Its image J is closed because O^times is compact, and it is Z_3-stable by continuity from integer multiplication. Thus these four logarithms and H account for the full image, not a sampled subgroup.

### Finite representatives with a proved tail

For 1 <= j <= 4 put

S_j = sum_(k=1)^80 (-1)^(k+1) pi^(jk)/k.

For k in [3^h,3^(h+1)), h >= 4, its term has integer uniformizer valuation

jk-9v_3(k) >= 3^h-9h.

The lower bound is 45 at h = 4 and increases thereafter, with next increment 2*3^h-9 > 0. Therefore every term with k >= 81 belongs to H, the valuations tend to infinity, and the whole convergent tail belongs to the closed ideal H. Consequently log(1+pi^j)-S_j belongs to H.

The coordinate description of H is c_0,...,c_4 in 3Z_3 and c_5,...,c_8 in Z_3. Substituting pi^9 = 3 into the finite sums gives the following representatives modulo H:

| j | q_j coordinates (c_0,...,c_8) | v_3(q_j) |
| --- | --- | --- |
| 1 | (7/3, 1, 1, 7/3, 2, 0, 1/3, 0, 0) | -1 |
| 2 | (1, 0, 1, 1, 1, 0, 1/3, 0, 0) | -1/3 |
| 3 | (1, 0, 0, 1, 0, 0, 0, 0, 0) | 0 |
| 4 | (0, 0, 0, 1, 1, 0, 0, 0, 0) | 1/3 |

Each row is a finite rational congruence. The certificate checks its difference from S_j coordinate by coordinate, using v_3(c_r difference) >= ceil((5-r)/9), without invoking a residue-reduction algorithm. Together with the proved tail, this gives log(1+pi^j)-q_j in H.

Every q_j is itself in the exact logarithm image. Indeed, if h_j = log(1+pi^j)-q_j in H, then

q_j = log((1+pi^j) exp(-h_j)).

The displayed argument is a unit, since exp(-h_j) belongs to U_5. The all-unit reduction and Z_3-stability now yield the exact lattice

J = sum_(j=1)^4 Z_3 q_j + H.

It is a full rank-nine lattice: it is bounded and contains H. The valuation formula gives the four minima in the table, and H has minimum 5/9. It follows that J has minimum -1, attained by q_1. Dividing by 6 lowers this by one. Thus I has exact minimum -2 and hull(I) = pi^(-18) O, of radius 9.

### Enclosing both literal branches

Since 6O has minimum valuation 1 >= 5/9, it is contained in H subset J. Hence O subset I and pi O subset I. This also follows directly from 6pi O subset H.

Every y in J has valuation at least -1. Therefore

v_3(18pi y) >= 2+1/9-1 = 10/9 > 5/9,

giving 18pi J subset H subset J. Equivalently, 3pi J subset I, so pi J subset I/3. All g in G preserve I/3. Both literal branches, and therefore their full orbit, are contained in I/3. No enlarged intermediate lattice has been substituted for the input.

### Integral functionals and a sharp automorphism

For y = sum c_r pi^r define

alpha(y) = 18c_0/7, and eta(y) = -3c_0/49+c_1/7.

The functional eta is distinct from the conductor scalar beta = 1. On q_1,...,q_4 the alpha values are (6,18/7,18/7,0), and the eta values are (0,-3/49,-3/49,0). All lie in 3Z_3. On H the same is true, since c_0,c_1 belong to 3Z_3. Thus alpha(J), eta(J) subset 3Z_3 and, since v_3(6) = 1, both functionals are integral on I.

Let x_0 = pi q_1 in pi J, w = 3x_0 in I and u = q_1/6 in I. Multiplication by pi sends coordinates to (3c_8,c_0,...,c_7), so direct substitution gives

alpha(u) = 1, eta(u) = 0, alpha(w) = 0, eta(w) = 1.

In particular w is primitive in I: membership in 3I would force eta(w) in 3Z_3. The value eta(x_0) = 1/3 also witnesses the failure of genuine membership of that literal point in I.

Set d = w-u in I and f = alpha-eta, integral on I. Then f(d) = -2. Define the Q_3-linear map

g(y) = y+f(y)d.

It sends I into I, and direct composition gives g^2(y) = y+(2+f(d))f(y)d = y. Its inverse is therefore itself, giving g(I) = I. It belongs to G and swaps w and u. Consequently

g(x_0) = u/3 = q_1/18,

of field valuation -1-2 = -3. This is a point in the orbit of the literal logarithm branch outside hull(I), whose minimum is -2.

The actual infinite-log input has the same sharp image. Its difference from x_0 belongs to pi H subset O subset I, so

g(pi log(1+pi)) belongs to q_1/18+I.

Every error in I has valuation at least -2, strictly greater than -3. It cannot cancel the lowest term of q_1/18. Thus this literal point also maps to valuation -3; no finite truncation is mistaken for an exact logarithm without controlling its error.

### Saturating the entire lattice

Automorphisms of a finite free Z_3-lattice are transitive on primitive vectors. In a basis a primitive vector has a unit coordinate; a coordinate swap, multiplication by its inverse unit, and elementary row subtractions take it to the first basis vector. Composing two such operations takes any primitive vector to any other.

For nonzero z in I/3, write 3z = 3^k t, k >= 0, with t primitive in I, by taking the minimum valuation of its I-coordinates. Choose g_z in G taking w to t. Because J is Z_3-stable, 3^k x_0 belongs to pi J, and

g_z(3^k x_0) = 3^k t/3 = z.

Zero also belongs to pi J. This proves G(pi J) = I/3, and the order branch does not enlarge it. Scaling I by 1/3 lowers its minimum from -2 to -3, yielding hull(I/3) = pi^(-27) O, of radius 27. Every g preserves I, so hull(G I) = hull(I). The achieved/required radius ratio is exactly three.

### Source comparison, scope and verification

The prior [odd-prime assessment](../drafts/literature/2026-10-04-odd-prime-literal-orbit.md) imports the lattice normalization, conductor construction and supporting logarithm results. The difference derived here is the exact log lattice and sharp whole-group hull for that unchanged packet. The [November 2022 RIMS1968 Example 3.5.1(ii)–(iii), printed pp. 100–101](https://www.kurims.kyoto-u.ac.jp/preprint/file/RIMS1968.pdf#page=101), allows field-dependent bounded valuation discrepancy; this threefold sharp failure is compatible with that supporting statement. It does not refute it. Claims depending on unread March 2024 revision interiors remain parked.

The suspect auxiliary transition in [Dupuy–Hilado §6.2, displayed (6.4)–(6.8), printed p. 20](https://arxiv.org/pdf/2004.13108v2#page=20) is audited only at its rounded-hull step. No consequence for its final container is proved here. The [native enclosure record](../foundations/04-native-local-enclosures.md) retains IUT IV Proposition 1.2(ii) and Proposition 1.4(iii) with their different input and corrections; neither is reproved or refuted. Unlike the earlier nonunit characteristic-2 packet, this packet has odd residue characteristic, but all other original-data and essentiality bridges still require proof.

Classification is **POTENTIALLY_NEW** solely in the prior bounded-search sense: the inspected sources did not provide this exact local computation. Supporting inputs are imported; the lattice and counterexample are derived. No certified originality, original IUT instance or challenge resolution is claimed.

`PYTHONDONTWRITEBYTECODE=1 python3 scripts/tensor-hull/check_degree_nine_odd_orbit.py` checks the finite sums, all residue congruences, generator extrema, integral functionals, branch enclosures, involution matrix and sharp witness with exact fractions. Its [certificate](../scripts/tensor-hull/degree-nine-odd-orbit-result.json) records those checks. The infinite analytic statements and whole-group saturation are proved above, rather than inferred from computation.

## Mathlib

Full odd-prime literal-input sharp-orbit statement: **not checked**. Supporting local-field logarithm/exp, unit-filtration, valuation, lattice and automorphism coverage: **not checked**. The named primary statements and direct links above supply setup and supporting results, not a matching Mathlib theorem for the full conclusion. No absence from Mathlib or formal verification is asserted.
