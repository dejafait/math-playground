# Degree-eight literal-input full orbit — calculation record

The saved conditional target has prior SPECIALIZE coverage in [the completed assessment](literature/2026-10-04-general-smaller-input-lattice-inclusion.md). This turn uses exactly L010's packet K = Q_2(pi), pi^8 = 2, beta = 1, a = pi, T = O_K, J = log(O_K^times), I = J/4. No new source retrieval or changed hypothesis is needed.

The main gap is finite B >= A in IUT III, Corollary 3.12, step (xi-f). The intermediate target is the weaker rounded component-hull comparison on the actual packet that violates genuine inclusion. An exact full-orbit calculation distinguishes a lattice-membership defect hidden by the hull from a failure of the claimed local hull inequality itself. The required hull is hull(I), since floor(v_2(a)-v_2(beta)) = 0. A larger saturated hull stops this universal local mechanism; containment would instead show why the genuine-inclusion objection does not transfer. Original initial data, pilot membership, all indeterminacies and global normalization remain unresolved either way.

L007–L008 concern enlarged regions and L009 settles a different quadratic packet. L010 proves a point outside I but leaves this full-orbit comparison open. The present calculation therefore addresses a distinct remaining assertion rather than repeating those failures.

## Saved reasoning before final verification

L010 gives H = pi^9 O_K subset J and exact logarithm representatives q_1,...,q_8 modulo H. Because each q_j differs from an actual logarithm by an element of H, q_j is itself in J; the finite representative is an exact point in the literal logarithm image. Closedness and the unit-group reduction give J = sum_j Z_2 q_j + H.

The table gives v_2(J) >= -3/2, with equality at q_1. Consequently 8 pi J subset pi^13 O_K subset H subset J. This implies pi J subset I/2. L010 already gives pi O_K subset I. Its functional lambda is integral on I. For x_0 = pi q_1, lambda(x_0) = 1/2, so 2x_0 is primitive in I. Transitivity of the whole lattice automorphism group on primitive vectors then suggests G(pi O_K union pi J) = I/2, since every nonnegative power of 2 times x_0 remains in pi J.

An explicit sharp map avoids a computed lattice basis. Let w = 2 pi q_1, u = q_1/4 and d = u-w. Both u,w belong to I; lambda(w) = 1 and lambda(u) = -1. Define g(y) = y + lambda(y)d. Then lambda(d) = -2, so g^2 = identity and g preserves I. It sends x_0 to q_1/8. The latter has valuation -9/2, while the required hull(I) has minimum valuation -7/2. Check these exact finite identities before completing the proof.

Mathlib coverage for the full orbit and supporting local-field and lattice statements is **not checked**. The existing primary references cover the source definitions and setup, rather than this exact sharp packet calculation. No original-IUT flaw or candidate resolution is claimed.

## Completed result and decision

The canonical proof is [L011](../lemmas/L011-literal-degree-eight-orbit-exceeds-rounded-hull.md). Both branch enclosures are established using the field-valuation minimum of the exact log image and the ideal H; a computed lattice basis is unnecessary. The entire-group primitive-vector argument gives G(pi J) = I/2. The explicit involution g(y) = y + lambda(y)(q_1/4 - 2pi q_1) preserves I, squares to the identity and maps pi q_1 to q_1/8. The same map sends pi log(1+pi) into q_1/8 + I, which has the same sharp valuation.

The exact required and achieved hulls are respectively pi^(-28) O_K and pi^(-36) O_K, with radii 2^(7/2) and 2^(9/2). Thus the literal-input rounded comparison fails by a radius factor of two. [The finite certificate](../scripts/tensor-hull/degree-eight-orbit-result.json) checks the valuations, both enclosures and the involution matrix with exact fractions; reproduction command: `PYTHONDONTWRITEBYTECODE=1 python3 scripts/tensor-hull/check_degree_eight_orbit.py`. Infinite analytic inputs are reused from L010, and the full orbit is proved rather than sampled.

Outcome: **NEGATIVE**; kind: **RESEARCH**; classification: **POTENTIALLY_NEW** in the prior assessment's bounded-search sense. This is new local obstruction evidence rather than an imported exact theorem or a certified discovery beyond the literature. It stops the universal literal-input rounded-hull mechanism. The [failure record](../ATTEMPTS/011-universal-literal-input-rounded-hull.md) preserves the conclusion and its limits. No final-container failure, original initial-data example, normalized B >= A comparison or essential IUT flaw is obtained. The known characteristic-2 exclusion motivates a separately screened odd-prime diagnostic; no odd-prime calculation is performed here.
