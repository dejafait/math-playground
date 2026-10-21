# Local weight-two lift at 7 — specialization coverage

TARGET: Establish a crystalline local lift of L019's residual representation at the base prime above 7 with determinant equal to the 7-adic cyclotomic character and Hodge–Tate weights (0,1) at both local embeddings, through both coefficient embeddings.
CHECKED: 2026-10-05
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the queries and primary reads completed in 2026-10-05-mixed-seventh-modular-location-after-restriction.md; no separate search or mathematical derivation was performed for this continuation.
SOURCE_EVIDENCE: Fontaine–Laffaille (1982), Section 9 setup and 9.10–9.12, printed pp. 600–606, and Theorem 8.4, pp. 595–596; Clozel–Harris–Taylor (2008), Section 2.4.1 and Lemma 2.4.1 with full proof, pp. 33–35, and Corollary 2.4.4, p. 37; Breuil–Diamond (2014), Theorem 3.2.2, author PDF pp. 36–37.
COMPARISON: Finite-flat classification and crystalline liftability cover the general mechanism over an unramified base; the desired coefficient-linear weight-two and fixed-determinant specialization still needs a proof. PVT already states the stronger global location, so this is reproduction of its local implementation rather than a novelty claim.
GAP: Justify coefficient actions, filtration multiplicities at both base embeddings, convention conversion, passage from compatible Artinian lifts to a lattice, and determinant correction preserving crystallinity and the residual representation.
REASON: A separate local interface test makes the BD prescription concrete without assuming good reduction of the original Jacobian or reconstructing packet data. The source comparison is ready, while this newly saved continuation requires separate supervisor approval before invocation.
SCOPE: Only local lifting of L019's geometric residual representation over the unramified quadratic completion at 7, after finite coefficient enlargement. Both embeddings and nonsplit local extensions remain included. No global modular-location or exact conductor theorem is approved here.

## Precise source scope

The [completed source comparison](2026-10-05-mixed-seventh-modular-location-after-restriction.md) records the inspected hypotheses, proofs, version qualifications and source-access evidence. The canonical local representation is L019's. L021's complete inertia cases may be used to check determinant/filtration compatibility, in which case its dependence on L020 and the exceptional-algebra assumption must remain explicit. Prefer the weaker hypotheses of L019 if the local lifting theorem does not require global absolute irreducibility; do not insert an unnecessary algebra assumption as an established fact about all solutions.

[Fontaine–Laffaille, Ann. Sci. ENS 15(4) (1982), 547–608, 9.11 and Proposition 9.12](https://www.numdam.org/article/ASENS_1982_4_15_4_547_0.pdf#page=59), supplies finite-flat classification and its generic-fibre identification over W(k), with p>2 and filtration degrees 0 and 1; [Theorem 8.4](https://www.numdam.org/article/ASENS_1982_4_15_4_547_0.pdf#page=50) supplies crystalline admissibility. [CHT, Publ. Math. IHES 108 (2008), Section 2.4.1 and Lemma 2.4.1](https://www.numdam.org/item/10.1007/s10240-008-0016-1.pdf#page=33), supplies coefficient-linear liftability for residual objects in the Fontaine–Laffaille image with graded multiplicities at most one at every embedding. Its full proof preserves filtration ranks by lifting filtered bases and divided Frobenius maps. The published Lemma 2.4.1 is the citation; a secondary fixed-determinant Proposition 2.4.3 citation is not used.

The exact local base, ramification index and residual determinant are established in L019. The general source does not automatically verify all coefficient and multiplicity hypotheses for this representation. Write those checks explicitly before applying liftability. The CHT functor's dual/twist convention must be reconciled with the geometric cyclotomic determinant; if applying it to a dual representation, restore the original representation and weights explicitly. Do not claim a fixed determinant from an unfixed-determinant lifting theorem. Any unramified determinant correction needs its own justified existence and preservation argument. These are the specialization differences for the next mathematical turn, not derivations completed here.

## Relevance and discriminating test

The main gap is uniform emptiness of residual Beal signatures. This narrower intermediate input could supply the p-adic prescribed lift in [BD Theorem 3.2.2](https://www.imo.universite-paris-saclay.fr/~breuil/PUBLICATIONS/extensions.pdf#page=36). The prospective downstream global application would additionally use PVT modularity, L020 and L021 in their conditional algebra branch, and explicit prescribed types at 3 and 5. Packet exhaustion, exact levels and global algebra applicability remain independent gaps.

Continue only if the lift reduces to the same rank-two residual module through each embedding, is crystalline with one weight 0 and one weight 1 at each base embedding in the BD convention, and has the full cyclotomic determinant. Stop the claimed specialization if coefficient actions, filtration ranks, a nonsplit extension or the determinant correction cannot be justified. Preserve the failed interface rather than assuming a semistable model of J. A proved local input alone is useful and is not a signature exclusion.

## Mathlib

Full matching local-lift theorem and its supporting finite-flat, Fontaine–Laffaille, crystalline and determinant results: **not checked**. No absence or formal verification is claimed. This is ready source coverage for a later REPRODUCTION, not a completed lemma.
