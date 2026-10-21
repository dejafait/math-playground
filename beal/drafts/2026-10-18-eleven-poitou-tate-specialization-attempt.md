# Fixed-tuple specialization — working checkpoint

Approved target: Specialize Poitou–Tate to L086's tuple, verifying support, archimedean signs and whether cubic norm correction preserves every prescribed local class.

Inputs read: L069's entire field and signatures; L074's supported spaces and scalar correction; L084's exact T; L086's complete eta and reciprocity proof. L073/L077/L082/L085 are used through these canonical interfaces. ATTEMPTS/038 and /040 retain their stops. The ready SPECIALIZE assessment is drafts/literature/2026-10-18-eleven-poitou-tate-specialization.md.

Attempt in progress: identify H^1(G_{D,S},mu_2) with H_{D,S}, completing eta by identity at every infinite place. Even valuations outside S give unramified Kummer extensions by the odd-residue unit theorem; the converse follows because an odd valuation cannot become the valuation of a square in an unramified extension. Apply the imported exact localization theorem, without evaluating the full dual.

Proposed norm correction: for a hypothetical supported lift a, let n=N_D/K(a) and b=a/n. Support is preserved, N(b)=n^(-2), and loc_v(n) is square at each prescribed base place because the complete prescribed local norm is square. Thus scalar division preserves every prescribed field component. At real places eta is positive and norm is positive. Check these assertions completely before recording a result.

Expected exact criterion: all full supported dual Hilbert products must be +1. For this eta only the two M components contribute; the product is (-1) raised to the sum of the two normalized M valuations of the dual element. This is not an evaluation of that functional on the complete supported group, a global witness, or a dimension bound.

Completed: the full proof and precise primary citations are canonical in `lemmas/L092-fixed-tuple-supported-poitou-tate-criterion.md`. Support, both real signs and all nine finite field components survive the correction. The exact full-dual criterion is established, but its functional is not evaluated. No global witness or dimension improvement follows. No mathematical scripts were written or run; separate critical application audit is the proposed continuation, requiring its own scope review.
